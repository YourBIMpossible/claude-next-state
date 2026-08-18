"""Render QUEUE.md from queue.yaml.

Implements the rendering + ranking rules in ~/.claude/skills/next/reference/item-model.md
exactly, so the same store produces the same order on every run. QUEUE.md is a generated
view; queue.yaml is the source of truth.

Usage: python render_queue.py [--state-dir DIR] [--generated-on YYYY-MM-DD] [--check]

Verify reproducibility (must print CHECK OK, exit 0):
    python render_queue.py --generated-on <date-in-QUEUE.md-header> --check

`--check` renders in memory and byte-compares against the existing QUEUE.md instead of
writing. Determinism note: the only run-dependent input is the generation date (header
line + the 30-day `live` window cutoff) — pin it with --generated-on to reproduce a
committed QUEUE.md exactly. Nothing else reads the clock, environment, or dict order
beyond yaml's insertion order, which is stable for a given queue.yaml.
"""

from __future__ import annotations

import argparse
import sys
from collections import deque
from datetime import date, datetime, timedelta
from pathlib import Path

import yaml

import queue_store
from queue_store import StoreError

EFFORT_ORDER = {"S": 0, "M": 1, "L": 2}

SECTIONS: list[tuple[str, tuple[str, ...]]] = [
    ("Blocked on you", ("blocked_owner",)),
    ("Landed — not verified live", ("landed",)),
    ("Next up", ("ready",)),
    ("In flight", ("in_flight",)),
    ("Blocked elsewhere", ("blocked_dep", "blocked_external")),
    ("Parked", ("parked",)),
    ("Live (last 30 days)", ("live",)),
]

EVIDENCE_WIDTH = 68
LIVE_WINDOW_DAYS = 30


class RenderError(RuntimeError):
    """Raised when the store cannot be rendered without guessing."""


def _as_date(value: object) -> date | None:
    """Coerce a YAML date/str to a date. Returns None rather than guessing."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def cone_size(item_id: str, unblocks: dict[str, list[str]]) -> tuple[int, list[str], list[str]]:
    """Transitive closure of `unblocks`, breadth-first.

    Returns (size, cycle_ids, dangling_ids). A revisited id stops that branch and is
    counted once; an unknown id counts as 1 and is reported. Both are data defects the
    caller surfaces rather than silently absorbing.
    """
    seen: set[str] = set()
    cycles: list[str] = []
    dangling: list[str] = []
    queue = deque(unblocks.get(item_id, []))
    while queue:
        nxt = queue.popleft()
        if nxt in seen:
            cycles.append(nxt)
            continue
        seen.add(nxt)
        if nxt not in unblocks:
            dangling.append(nxt)
            continue
        queue.extend(unblocks[nxt])
    return len(seen), cycles, dangling


def sort_key(item: dict, cones: dict[str, int]) -> tuple:
    effort = item.get("effort") or "M"
    owner_gate = bool(item.get("owner_gate"))
    return (
        -cones[item["id"]],
        0 if (owner_gate and effort == "S") else 1,
        EFFORT_ORDER.get(effort, 1),
        -int(item.get("risk") or 0),
        item["id"],
    )


def evidence_snippet(item: dict) -> str:
    evidence = item.get("evidence") or []
    ref = ""
    if evidence:
        ref = str(evidence[0].get("ref", "") or "")
    if not ref:
        ref = str(item.get("verification", {}).get("by", "") or "")
    ref = " ".join(ref.split())
    if len(ref) > EVIDENCE_WIDTH:
        return ref[:EVIDENCE_WIDTH] + "…"
    return ref


def render_item(item: dict, cones: dict[str, int]) -> list[str]:
    ver = item.get("verification") or {}
    level = str(ver.get("level", "claimed")).upper()
    at = _as_date(ver.get("at"))
    at_str = at.isoformat() if at else "date-unknown"
    projects = "+".join(item.get("projects") or [])
    effort = item.get("effort") or "M"
    lines = [
        f"[{item['id']}] {item['title']}",
        f"       unblocks {cones[item['id']]} · {effort} · {projects} · "
        f"{level} {at_str} · {evidence_snippet(item)}",
    ]
    if level == "CONTRADICTED":
        # item-model.md: CONTRADICTED renders with both readings beneath it.
        body = " ".join(str(ver.get("by", "")).split())
        lines.append(f"       ⚠ both readings unresolved — {body[:150]}…")
    return lines


def build(state_dir: Path, generated_on: date) -> str:
    store = queue_store.load_store(state_dir)
    registry = yaml.safe_load((state_dir / "projects.yaml").read_text(encoding="utf-8"))

    items = store.active_items
    if not items:
        raise RenderError("queue.yaml holds no items — refusing to render an empty view")

    # Cones are computed over the UNION of active + archived items so that moving a
    # closed item into the archive can never change the ranking of active work, and
    # active `unblocks` references into the archive are not reported as dangling.
    unblocks = {i["id"]: list(i.get("unblocks") or []) for i in store.all_items}
    cones: dict[str, int] = {}
    all_cycles: list[tuple[str, list[str]]] = []
    all_dangling: list[tuple[str, list[str]]] = []
    for item in store.all_items:
        size, cycles, dangling = cone_size(item["id"], unblocks)
        cones[item["id"]] = size
        if item not in items:
            continue  # defects are reported for active items only
        if cycles:
            all_cycles.append((item["id"], cycles))
        if dangling:
            all_dangling.append((item["id"], dangling))

    reconciled = store.watermarks
    marks = []
    for key, mark in reconciled.items():
        at = _as_date(mark.get("at"))
        marks.append(
            f"`{key}` = {at.isoformat() if at else '?'} @ `{mark.get('commit')}` PR#{mark.get('pr')}"
        )

    active = [p["key"] for p in registry["projects"] if p.get("active")]
    with_items = {p for i in items for p in (i.get("projects") or [])}
    barren = [k for k in active if k not in with_items and k not in reconciled]

    out: list[str] = [
        "<!-- GENERATED from queue.yaml. Do not hand-edit — edit queue.yaml, then regenerate. -->",
        "",
        "# /next — work-item queue",
        "",
        f"Generated {generated_on.isoformat()} (synced). Ranked by critical path (transitive "
        "`unblocks` cone), tiebreak:",
        "owner-gated+S effort, then effort, then risk, then id. Full algorithm:",
        "`~/.claude/skills/next/reference/item-model.md`.",
        "",
        f"Scope: `all`. Watermarks: {' · '.join(marks)}.",
    ]
    if barren:
        out.append(f"({'/'.join(barren)}: no items yet — run `init` to derive.)")
    out.append("")

    if all_cycles or all_dangling:
        out.append("> **Data defects found while ranking** (fix in `queue.yaml`):")
        for item_id, cyc in all_cycles:
            out.append(f"> - `{item_id}` unblocks-cycle through: {', '.join(sorted(set(cyc)))}")
        for item_id, dang in all_dangling:
            out.append(f"> - `{item_id}` dangling unblocks ids: {', '.join(sorted(set(dang)))}")
        out.append("")

    cutoff = generated_on - timedelta(days=LIVE_WINDOW_DAYS)
    for title, statuses in SECTIONS:
        # The Live section draws from BOTH tiers: `live` items migrate to the archive,
        # but recently verified ones stay visible in the operator view for the window.
        pool = store.all_items if title.startswith("Live") else items
        bucket = [i for i in pool if i.get("status") in statuses]
        if title.startswith("Live"):
            bucket = [
                i
                for i in bucket
                if (d := _as_date((i.get("verification") or {}).get("at"))) and d >= cutoff
            ]
        if not bucket:
            continue
        bucket.sort(key=lambda i: sort_key(i, cones))
        out.append(f"## {title}")
        out.append("")
        for item in bucket:
            out.extend(render_item(item, cones))
            out.append("")

    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=Path(r"F:\AI-Dev\.tools\state"))
    parser.add_argument("--generated-on", default=None, help="YYYY-MM-DD; defaults to today")
    parser.add_argument(
        "--check",
        action="store_true",
        help="don't write; byte-compare the rendered output against the existing QUEUE.md",
    )
    args = parser.parse_args()

    on = date.fromisoformat(args.generated_on) if args.generated_on else date.today()
    try:
        text = build(args.state_dir, on)
    except (RenderError, StoreError, KeyError, yaml.YAMLError) as exc:
        print(f"render failed: {exc}", file=sys.stderr)
        return 1

    target = args.state_dir / "QUEUE.md"
    if args.check:
        existing = target.read_text(encoding="utf-8") if target.exists() else ""
        if existing == text:
            print(f"CHECK OK — {target} reproduces byte-for-byte")
            return 0
        print(f"CHECK FAILED — rendered output differs from {target}", file=sys.stderr)
        for n, (a, b) in enumerate(zip(existing.splitlines(), text.splitlines()), 1):
            if a != b:
                print(f"  first diff at line {n}:\n    have: {a}\n    want: {b}", file=sys.stderr)
                break
        else:
            print("  files differ only in length/trailing content", file=sys.stderr)
        return 1

    target.write_text(text, encoding="utf-8")
    print(f"wrote {target} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
