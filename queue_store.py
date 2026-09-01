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
    store.commit_index      # commit-shaped sha (7–40 hex, != 32; lowered) -> [(id, tier), ...]
                            #   harvested ONLY from kind: commit|pr evidence — never prose.
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
PROJECTS_FILE = "projects.yaml"

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

# Which evidence entries may feed the COMMIT index. A commit id is harvested ONLY from
# evidence that explicitly asserts commit/PR identity — never from free prose (a doc/run/
# log ref or a verification note), where a hex-looking token is far more likely an md5, a
# blob/tree object sha, or an incidental identifier than a commit. This is the fix for
# commit_index poisoning: deduplication is driven by declared commit evidence, not by
# arbitrary hex substrings that happen to appear in narrative text.
_COMMIT_EVIDENCE_KINDS = {"commit", "pr"}


def _is_commit_shaped(token: str) -> bool:
    """A git (SHA-1) commit id is 7–40 hex chars. Exactly 32 hex is the canonical MD5
    length and never a git abbreviation anyone writes (a full SHA-1 is 40), so it is
    rejected outright — this alone drops the md5 provenance hashes that used to be indexed
    as commits. Tree/blob object shas are also 40 hex and indistinguishable from a commit
    by shape; they are excluded structurally instead (see `_COMMIT_EVIDENCE_KINDS`) because
    they occur in prose, not in a `kind: commit` ref."""
    return 7 <= len(token) <= 40 and len(token) != 32


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
    """Harvest PR and commit identity from evidence.

    PR identity (`repo#N`) is distinctive and low-risk, so it is mined from ALL evidence
    text plus the verification note. Commit identity is mined ONLY from evidence entries
    whose `kind` explicitly asserts a commit/PR (`_COMMIT_EVIDENCE_KINDS`), and only for
    tokens that are commit-shaped (`_is_commit_shaped`). Free prose — doc/run/log refs, a
    verification note — never contributes to the commit index, so md5 provenance hashes,
    blob/tree object shas, and incidental hex identifiers can no longer be mistaken for
    commits during dedup."""
    entry = (item["id"], tier)
    projects = [str(p).lower() for p in (item.get("projects") or [])]

    pr_texts: list[str] = []
    commit_texts: list[str] = []
    for ev in item.get("evidence") or []:
        if not isinstance(ev, dict):
            continue
        ref = str(ev.get("ref", "") or "")
        url = str(ev.get("url", "") or "")
        pr_texts.append(ref)
        pr_texts.append(url)
        if str(ev.get("kind", "")).strip().lower() in _COMMIT_EVIDENCE_KINDS:
            commit_texts.append(ref)
            commit_texts.append(url)
    pr_texts.append(str((item.get("verification") or {}).get("by", "") or ""))

    for text in pr_texts:
        for m in _PR_REF.finditer(text):
            repo = m.group(1).lower()
            pr_idx.setdefault(f"{repo}#{m.group(2)}", []).append(entry)
            # Bare "PR#244" refs are repo-ambiguous — index them additionally under
            # each of the item's projects so probes by project key still hit.
            if repo in ("pr", "prs"):
                for proj in projects:
                    pr_idx.setdefault(f"{proj}#{m.group(2)}", []).append(entry)
        for m in _PR_URL.finditer(text):
            pr_idx.setdefault(f"{m.group(1).lower()}#{m.group(2)}", []).append(entry)
    for text in commit_texts:
        for m in _SHA.finditer(text.lower()):
            if _is_commit_shaped(m.group(1)):
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


def load_dormant(state_dir: Path) -> set[str]:
    """Project keys flagged `dormant: true` in projects.yaml — the key-set view of
    `load_dormant_targets` for callers that only need membership (the renderer).

    A dormant project is a checkout under top-down reassessment: `/next` must never emit
    or run a probe against it. Absent registry or absent flag => empty set (no project is
    dormant), so installations without the flag keep loading unchanged. Shares
    `load_dormant_targets`' fail-loud contract: a malformed dormant entry is a StoreError,
    never a silent skip."""
    return set(load_dormant_targets(state_dir))


# Characters that can extend a path segment or repo name. A candidate match bordered by one
# of these is part of a LONGER name (`F:/BIMpossible` inside `F:/BIMpossible-Workspace`),
# not a reference to the dormant checkout.
_TOKEN_NAME_CHARS = r"a-z0-9_.\-"


def load_dormant_targets(state_dir: Path) -> dict[str, str]:
    """Map each dormant project key -> the normalized checkout-path token used to detect
    commands targeting that repo.

    The token is the registry `path`, lowercased, backslashes folded to forward slashes, and
    trailing separators stripped, so one token matches `F:\\BIMpossible-Families`,
    `F:/BIMpossible-Families`, and subpaths of either. A dormant entry is a machine-read
    safety gate, so a malformed one fails loud instead of silently leaving the gate off: the
    entry must carry a `key` and a usable checkout `path` (a real directory path, not a bare
    drive root — the bare key alone would false-positive on prose and is never used as a
    fallback). Absent registry => {} (no project is dormant)."""
    path = state_dir / PROJECTS_FILE
    if not path.exists():
        return {}
    registry = _load_yaml(path, "project registry")
    out: dict[str, str] = {}
    for p in registry.get("projects") or []:
        if not (isinstance(p, dict) and p.get("dormant")):
            continue
        if not p.get("key"):
            raise StoreError(
                f"project registry: dormant entry {p!r} has no 'key' — the dormancy gate "
                "cannot protect a repo it cannot name; fix the entry, do not drop the flag"
            )
        key = str(p["key"]).lower()
        token = str(p.get("path") or "").strip().lower().replace("\\", "/").rstrip("/")
        if not token or "/" not in token or re.fullmatch(r"[a-z]:", token):
            raise StoreError(
                f"project registry: dormant project '{key}' needs a usable checkout 'path' "
                f"(got {p.get('path')!r}) — the command gate matches on it, so a missing or "
                "degenerate path would silently disable or brick the gate"
            )
        out[key] = token
    return out


def _command_targets_dormant(command: str, dormant_targets: dict[str, str]) -> list[str]:
    """Dormant keys the command references — by full checkout-path token (either separator
    spelling, subpaths included) or by the checkout's directory name as a standalone
    segment/name. The directory-name signal catches relative paths
    (`..\\BIMpossible-Families`), MSYS-style paths (`/f/bimpossible-families`), and GitHub
    `owner/repo` slugs that reuse the directory name. Both signals are boundary-checked: a
    token bordered by a name character is a longer, different name (`F:/BIMpossible` never
    matches `F:/BIMpossible-Workspace`). Static text analysis cannot see every indirection
    (an environment variable, a subst'd drive, a renamed remote) — this is a tripwire for
    the realistic spellings, not a sandbox; the dormancy policy itself is the guarantee."""
    cl = str(command).lower().replace("\\", "/")
    hits = []
    for key, token in dormant_targets.items():
        names = {token, token.rsplit("/", 1)[-1]}
        if any(
            re.search(
                rf"(?<![{_TOKEN_NAME_CHARS}]){re.escape(name)}(?![{_TOKEN_NAME_CHARS}])", cl
            )
            for name in names
            if name
        ):
            hits.append(key)
    return sorted(hits)


def dormancy_defects(active_items: list[dict], dormant_targets: dict[str, str]) -> list[str]:
    """Fail-loud list of active items that would let `/next` touch a dormant repo, or that
    misstate their verification while one of their legs is dormant.

    Checked on EVERY active item — declared scope does not exempt a command:

    1. **All-dormant item** — every project in `projects` is dormant — must carry no runnable
       `live_check` at all: with no live leg there is nothing legitimate to probe, so any command
       is a suspended probe that leaked back in.
    2. **Dormant-targeting command** — no `live_check` command on ANY item may reference a
       dormant checkout (by path or directory name, see `_command_targets_dormant`), whatever
       the item's declared legs. A mixed-scope item keeps its live-leg probes; an item with no
       dormant leg at all is still forbidden — mis-scoping is not a bypass.
    3. **Stored-level honesty** — a mixed-scope item (dormant + live legs) must not store
       whole-item `verification.level: verified`: its dormant leg is unprobeable, so the honest
       stored level is `partial` (item-model.md). Conversely `partial` is reserved for exactly
       that shape — stored on anything else it is a vocabulary violation.
    4. **live_check shape** — must be a string or a list of strings; any other shape (a mapping,
       a scalar) would evade the command scan, so it is itself a defect, never a crash.

    A governance item that merely *references* a dormant project via `affects_projects` (while
    its own `projects` are all live) keeps its live probes — that is how the gate stays visible
    without reactivating the dormant repo — but rule 2 still applies to its command text.

    Returns one message per violation; empty when the queue is dormancy-clean. Callers treat a
    non-empty result as a hard validation failure."""
    out: list[str] = []
    for item in active_items:
        projects = [str(p).lower() for p in (item.get("projects") or [])]
        dormant_legs = [p for p in projects if p in dormant_targets]
        live_legs = [p for p in projects if p not in dormant_targets]
        level = str((item.get("verification") or {}).get("level", "")).strip().lower()

        if dormant_legs and live_legs and level == "verified":
            out.append(
                f"active item {item['id']}: mixed-scope (dormant legs {dormant_legs}) but stores "
                f"verification.level: verified — the dormant leg is unprobeable, so whole-item "
                f"'verified' over-claims; store 'partial' (item-model.md)"
            )
        if level == "partial" and not (dormant_legs and live_legs):
            out.append(
                f"active item {item['id']}: stores verification.level: partial but is not "
                f"mixed-dormant-scoped — 'partial' is reserved for items with both a live and a "
                f"dormant leg (item-model.md)"
            )

        lc = item.get("live_check")
        if dormant_legs and not live_legs:
            if lc:
                out.append(
                    f"active item {item['id']}: scoped to dormant project(s) {projects} but carries a "
                    f"non-empty live_check — dormant-repo probes must be suspended (empty live_check; "
                    f"move command text to non-executable evidence)"
                )
            continue
        if not lc:
            continue
        if isinstance(lc, str):
            commands = [lc]
        elif isinstance(lc, list) and all(isinstance(c, str) for c in lc):
            commands = lc
        else:
            out.append(
                f"active item {item['id']}: live_check must be a string or a list of strings "
                f"(got {type(lc).__name__}) — any other shape evades the dormancy command scan"
            )
            continue
        for cmd in commands:
            hit = _command_targets_dormant(cmd, dormant_targets)
            if not hit:
                continue
            if dormant_legs:
                out.append(
                    f"active item {item['id']}: mixed-scope (dormant legs {dormant_legs}, live legs "
                    f"{live_legs}) but a live_check command targets dormant project(s) {hit}: "
                    f"{cmd!r} — suspend this command (move to non-executable evidence); the "
                    f"live-leg probes may remain"
                )
            else:
                out.append(
                    f"active item {item['id']}: declares no dormant leg yet a live_check command "
                    f"references dormant project(s) {hit}: {cmd!r} — mis-scoped items are not "
                    f"exempt from the gate; suspend the command (and declare the leg if the work "
                    f"truly spans it)"
                )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=Path(r"F:\Claude-Tools\state"))
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

    # Dormancy gate: a dormant-scoped active item with a runnable live_check is a hard
    # failure, not a soft defect — it is the exact condition that would let a drill run a
    # command against a reassessment-bound repo.
    dorm_defects = dormancy_defects(store.active_items, load_dormant_targets(args.state_dir))
    if dorm_defects:
        for d in dorm_defects:
            print(f"dormancy violation: {d}", file=sys.stderr)
        return 1

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
