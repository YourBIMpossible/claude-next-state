"""Two-tier /next store loader and validator.

Tiers:
    queue.yaml          — ACTIVE operational queue + per-project reconcile watermarks.
    queue-archive.yaml  — closed-item provenance (live / dropped), immutable under
                          ordinary reconciliation. Optional: absent file = empty archive
                          (pre-migration installations keep working unchanged).

Why two tiers exist: reconciliation deduplicates discovered PRs/commits against every
item it can see. Closed items therefore cannot simply be deleted — a merged PR whose
only record was removed would be "rediscovered" as new work on the next sync. The
archive keeps that identity visible to reconciliation while keeping queue.yaml small
enough to hand-edit.

Contract exposed to consumers (render_queue.py, the /next skill, tests):

    store = load_store(state_dir)
    store.active_items      # list[dict] — queue.yaml items, authoritative for active work
    store.archived_items    # list[dict] — queue-archive.yaml items, historical provenance
    store.all_items         # active + archived (identity/graph union)
    store.ids               # id -> ("active"|"archive", item)
    store.pr_index          # "repo#123" (lowercased repo) -> [(id, tier), ...]
    store.commit_index      # short-sha (>=7 chars, lowered) -> [(id, tier), ...]
    store.watermarks        # reconciled: mapping from queue.yaml
    store.is_known_pr(ref)  / store.is_known_commit(sha) / store.find(id)

Validation is fail-loud (StoreError):
    - duplicate item id within a tier or across tiers;
    - active item with required fields missing or a status outside the closed vocabulary;
    - archive item whose status is not an allowed archived status, or missing
      archive metadata (archived_at);
    - unparsable YAML or wrong top-level shape;
    - schema_version mismatch between the tiers (when the archive declares one).

Canonical PR-identity rule: the PR/commit indexes are many-to-many — one PR may
legitimately be evidence on several items (folded work, cross-repo items). "Known"
means present in the combined index of BOTH tiers. Duplicate PR identity across
tiers is therefore not an error; duplicate ITEM identity is.

CLI:
    python queue_store.py [--state-dir DIR]          # validate + print summary, exit 0/1
    python queue_store.py --known-pr bimpossible#187 # dedup probe for reconcile sessions
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ACTIVE_FILE = "queue.yaml"
ARCHIVE_FILE = "queue-archive.yaml"

# item-model.md — closed status vocabulary.
ACTIVE_STATUSES = {
    "ready",
    "blocked_owner",
    "blocked_dep",
    "blocked_external",
    "in_flight",
    "landed",
    "live",
    "parked",
    "dropped",
}
# Statuses an ARCHIVED record may carry. `landed` is deliberately excluded from
# archive *eligibility* (it is actionable — "verify it"), but a record archived
# under an older policy must still load, so it is accepted here.
ARCHIVED_STATUSES = {"live", "landed", "dropped"}

# Hard identity fields — load fails without them. The remaining item-model "required"
# fields (unblocks, verification, source) are reported as defects, not load failures:
# the store predates strict validation and the renderer has always tolerated their
# absence with documented defaults.
REQUIRED_FIELDS = ("id", "title", "projects", "status")
SOFT_REQUIRED_FIELDS = ("unblocks", "verification", "source")
ARCHIVE_REQUIRED_META = ("archived_at",)

_PR_REF = re.compile(r"([A-Za-z0-9_.-]+)\s*#(\d+)")
_PR_URL = re.compile(r"github\.com/[^/\s]+/([^/\s]+)/pull/(\d+)")
_SHA = re.compile(r"\b([0-9a-f]{7,40})\b")


class StoreError(RuntimeError):
    """The store cannot be loaded without guessing. Do not rebuild from scratch —
    that destroys accumulated judgment. Fix the reported defect."""


@dataclass
class Store:
    active_items: list[dict]
    archived_items: list[dict]
    watermarks: dict
    schema_version: int
    ids: dict[str, tuple[str, dict]] = field(default_factory=dict)
    pr_index: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    commit_index: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    defects: list[str] = field(default_factory=list)

    @property
    def all_items(self) -> list[dict]:
        return self.active_items + self.archived_items

    def find(self, item_id: str) -> tuple[str, dict] | None:
        return self.ids.get(item_id)

    def is_known_pr(self, ref: str) -> list[tuple[str, str]]:
        """Return [(item_id, tier)] for a 'repo#N' ref (case-insensitive repo)."""
        m = _PR_REF.search(ref) or _PR_URL.search(ref)
        if not m:
            return []
        return self.pr_index.get(f"{m.group(1).lower()}#{m.group(2)}", [])

    def is_known_commit(self, sha: str) -> list[tuple[str, str]]:
        sha = sha.strip().lower()
        for k, v in self.commit_index.items():
            if k.startswith(sha) or sha.startswith(k):
                return v
        return []


def _load_yaml(path: Path, what: str) -> dict:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise StoreError(f"{what} ({path.name}) is not valid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise StoreError(f"{what} ({path.name}) top level must be a mapping, got {type(data).__name__}")
    return data


def _check_item(item: object, tier: str, n: int, defects: list[str]) -> dict:
    if not isinstance(item, dict):
        raise StoreError(f"{tier} item #{n} is not a mapping")
    missing = [f for f in REQUIRED_FIELDS if f not in item]
    if missing:
        ident = item.get("id", f"#{n}")
        raise StoreError(f"{tier} item {ident}: missing required field(s) {missing}")
    soft = [f for f in SOFT_REQUIRED_FIELDS if f not in item]
    if soft:
        defects.append(f"{tier} item {item['id']}: missing {soft} (item-model required)")
    status = item["status"]
    if tier == "archive":
        if status not in ARCHIVED_STATUSES:
            raise StoreError(
                f"archive item {item['id']}: status '{status}' is not an allowed archived "
                f"status {sorted(ARCHIVED_STATUSES)}"
            )
        meta_missing = [f for f in ARCHIVE_REQUIRED_META if not item.get(f)]
        if meta_missing:
            raise StoreError(f"archive item {item['id']}: missing archive metadata {meta_missing}")
    elif status not in ACTIVE_STATUSES:
        raise StoreError(
            f"active item {item['id']}: status '{status}' outside the closed vocabulary "
            f"{sorted(ACTIVE_STATUSES)}"
        )
    return item


def _index_evidence(item: dict, tier: str, pr_idx: dict, sha_idx: dict) -> None:
    """Harvest PR and commit identity from evidence refs/urls and verification.by."""
    texts: list[str] = []
    for ev in item.get("evidence") or []:
        if isinstance(ev, dict):
            texts.append(str(ev.get("ref", "") or ""))
            texts.append(str(ev.get("url", "") or ""))
    texts.append(str((item.get("verification") or {}).get("by", "") or ""))
    entry = (item["id"], tier)
    for text in texts:
        for m in _PR_REF.finditer(text):
            pr_idx.setdefault(f"{m.group(1).lower()}#{m.group(2)}", []).append(entry)
        for m in _PR_URL.finditer(text):
            pr_idx.setdefault(f"{m.group(1).lower()}#{m.group(2)}", []).append(entry)
        for m in _SHA.finditer(text.lower()):
            sha_idx.setdefault(m.group(1), []).append(entry)


def load_store(state_dir: Path) -> Store:
    active_path = state_dir / ACTIVE_FILE
    archive_path = state_dir / ARCHIVE_FILE

    active = _load_yaml(active_path, "active store")
    active_items_raw = active.get("items")
    if not isinstance(active_items_raw, list) or not active_items_raw:
        raise StoreError("queue.yaml holds no items — refusing to load an empty active store")
    schema_version = int(active.get("schema_version") or 1)

    archived_items_raw: list = []
    if archive_path.exists():
        archive = _load_yaml(archive_path, "archive store")
        arc_version = archive.get("schema_version")
        if arc_version is not None and int(arc_version) != schema_version:
            raise StoreError(
                f"schema_version mismatch: active={schema_version} archive={arc_version}"
            )
        archived_items_raw = archive.get("items") or []
        if not isinstance(archived_items_raw, list):
            raise StoreError("queue-archive.yaml items: must be a list")

    defects: list[str] = []
    ids: dict[str, tuple[str, dict]] = {}
    pr_idx: dict[str, list[tuple[str, str]]] = {}
    sha_idx: dict[str, list[tuple[str, str]]] = {}

    active_items, archived_items = [], []
    for tier, raw, bucket in (
        ("active", active_items_raw, active_items),
        ("archive", archived_items_raw, archived_items),
    ):
        for n, raw_item in enumerate(raw, 1):
            item = _check_item(raw_item, tier, n, defects)
            if item["id"] in ids:
                prev_tier, _ = ids[item["id"]]
                raise StoreError(
                    f"duplicate item id '{item['id']}' — already present in {prev_tier} tier"
                )
            ids[item["id"]] = (tier, item)
            _index_evidence(item, tier, pr_idx, sha_idx)
            bucket.append(item)

    return Store(
        active_items=active_items,
        archived_items=archived_items,
        watermarks=active.get("reconciled") or {},
        schema_version=schema_version,
        ids=ids,
        pr_index=pr_idx,
        commit_index=sha_idx,
        defects=defects,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=Path(r"F:\AI-Dev\.tools\state"))
    parser.add_argument("--known-pr", help="probe: is 'repo#N' already represented? exit 0=known 2=unknown")
    parser.add_argument("--known-commit", help="probe: is a sha already represented? exit 0=known 2=unknown")
    args = parser.parse_args()

    try:
        store = load_store(args.state_dir)
    except StoreError as exc:
        print(f"store validation FAILED: {exc}", file=sys.stderr)
        return 1

    if args.known_pr:
        hits = store.is_known_pr(args.known_pr)
        print(f"{args.known_pr}: {'KNOWN ' + str(hits) if hits else 'unknown'}")
        return 0 if hits else 2
    if args.known_commit:
        hits = store.is_known_commit(args.known_commit)
        print(f"{args.known_commit}: {'KNOWN ' + str(hits) if hits else 'unknown'}")
        return 0 if hits else 2

    from collections import Counter

    for d in store.defects:
        print(f"defect: {d}", file=sys.stderr)
    a = Counter(i["status"] for i in store.active_items)
    z = Counter(i["status"] for i in store.archived_items)
    print(
        f"OK — active {len(store.active_items)} {dict(a)} · archive {len(store.archived_items)} "
        f"{dict(z)} · ids {len(store.ids)} · PRs indexed {len(store.pr_index)} · "
        f"commits indexed {len(store.commit_index)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
