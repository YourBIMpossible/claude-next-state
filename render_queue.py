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


def cone_size(
    item_id: str, unblocks: dict[str, list[str]]
) -> tuple[int, int, list[str], list[str]]:
    """Transitive closure of `unblocks`, breadth-first.

    Returns (display_size, rank_size, cycle_ids, dangling_ids) — two DISTINCT cone
    counts, computed in the same walk:

    - `display_size` — every distinct id reached, INCLUDING unknown/dangling ids
      (each counted once). This is the `unblocks N` shown on the line, per
      item-model.md ("Unknown ids count as 1 and are reported as dangling references";
      "`unblocks N` is the cone size").
    - `rank_size` — only *resolved* nodes (ids that exist in the store), accumulated
      explicitly during traversal. This is the topology that decides graph shape and
      cone-ranking. Unknown/dangling/stale ids never enter it, so a dead edge cannot
      inflate leverage and flip a flat actionable graph to "deep".

    A revisited id stops that branch and is counted once (a cycle); it was already
    tallied as a resolved node on its first visit, so cycles remain resolved references
    counted once. Cycles and dangling ids are both data defects the caller surfaces
    rather than silently absorbing.
    """
    seen: set[str] = set()
    resolved: set[str] = set()
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
        resolved.add(nxt)
        queue.extend(unblocks[nxt])
    return len(seen), len(resolved), cycles, dangling


# Statuses an owner can actually move — the set whose cone depth decides "flat vs deep"
# (item-model.md Step 1). A cone that only runs through non-actionable items is not
# leverage anyone can spend, so it must not decide graph shape.
ACTIONABLE_STATUSES = ("ready", "blocked_owner", "landed")


def graph_is_flat(items: list[dict], rank_cones: dict[str, int]) -> bool:
    """Flat graph (item-model.md Step 1): the top actionable *ranking* cone is <= 1, so
    `cone` carries no ranking signal and degenerates to 'point at the lone sink'. On a
    flat graph the renderer drops cone as a sort axis; it keeps the inclusive display
    cone only for the `unblocks N` line.

    Measured over `rank_cones` — resolved edges only. Unknown/dangling/stale unblocks
    ids never enter this count, so a dead edge can never make a flat actionable graph
    look deep and reactivate cone-first ordering."""
    actionable = [rank_cones[i["id"]] for i in items if i.get("status") in ACTIONABLE_STATUSES]
    return (max(actionable) if actionable else 0) <= 1


def sort_key(item: dict, rank_cones: dict[str, int], flat: bool) -> tuple:
    """Deterministic intra-section order.

    This orders items WITHIN a status section; it does not pick the single #1 move —
    that is chosen live by the skill using the full anchor-first model (stated focus
    vs roadmap order + finalization leverage), which reads inputs not in the store
    (the live phase ledger, dark-feature judgment). Here we use only store-derivable
    axes. On a deep graph, resolved `cone` leads (real unblock-leverage, item-model.md
    2a). On a flat graph it is meaningless (2b) and dropped, falling through to the
    stable tail: stranded owner-gated+S value, then effort, risk, id.

    The cone axis is `rank_cones` — resolved edges only — so a dangling ref that pads
    an item's displayed cone can never change its ranking position."""
    effort = item.get("effort") or "M"
    owner_gate = bool(item.get("owner_gate"))
    tail = (
        0 if (owner_gate and effort == "S") else 1,
        EFFORT_ORDER.get(effort, 1),
        -int(item.get("risk") or 0),
        item["id"],
    )
    return tail if flat else (-rank_cones[item["id"]], *tail)


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


def render_item(item: dict, cones: dict[str, int], dormant: set[str]) -> list[str]:
    ver = item.get("verification") or {}
    level = str(ver.get("level", "claimed")).upper()
    item_projects = [str(p).lower() for p in (item.get("projects") or [])]
    dormant_legs = [p for p in item_projects if p in dormant]
    is_dormant_scoped = bool(item_projects) and len(dormant_legs) == len(item_projects)
    is_mixed_dormant = bool(dormant_legs) and not is_dormant_scoped
    if is_dormant_scoped:
        # A dormant-scoped item is unprobed by construction — its live_check is suspended,
        # so no stored verification can be current. Never render it as verified from prior
        # evidence; the badge states the truth (SUSPENDED) regardless of the stored level.
        level = "SUSPENDED"
    elif is_mixed_dormant and level == "VERIFIED":
        # Mixed scope: the live leg(s) may be genuinely verified, but the dormant leg is
        # unprobed and its state is unknown until reassessment. A whole-item VERIFIED badge
        # would over-claim — downgrade to PARTIAL so the suspended leg is never hidden behind
        # the active leg's evidence. Non-VERIFIED levels already under-claim and are left as-is.
        level = "PARTIAL"
    at = _as_date(ver.get("at"))
    at_str = at.isoformat() if at else "date-unknown"
    projects = "+".join(item.get("projects") or [])
    effort = item.get("effort") or "M"
    lines = [
        f"[{item['id']}] {item['title']}",
        f"       unblocks {cones[item['id']]} · {effort} · {projects} · "
        f"{level} {at_str} · {evidence_snippet(item)}",
    ]
    if is_dormant_scoped:
        lines.append(
            f"       ⏸ dormant project ({projects}) — probes suspended (non-executable); "
            "state unverifiable until whole-repo reassessment"
        )
    elif is_mixed_dormant:
        active_legs = [p for p in item_projects if p not in dormant]
        lines.append(
            f"       ⏸ dormant leg ({'+'.join(sorted(dormant_legs))}) suspended — "
            f"{'+'.join(active_legs)} leg tracked live; dormant leg unverifiable until "
            "whole-repo reassessment, so the item is not fully verified"
        )
    gated = sorted(set(str(p).lower() for p in (item.get("affects_projects") or [])) & dormant)
    if gated:
        lines.append(
            f"       ⛔ dormancy gate — governs dormant {'+'.join(gated)}; keeps the "
            "constraint visible without reactivating the repo"
        )
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
    cones: dict[str, int] = {}        # display cone — inclusive of dangling (item-model.md)
    rank_cones: dict[str, int] = {}   # ranking/shape cone — resolved nodes only
    all_cycles: list[tuple[str, list[str]]] = []
    all_dangling: list[tuple[str, list[str]]] = []
    for item in store.all_items:
        size, rank_size, cycles, dangling = cone_size(item["id"], unblocks)
        cones[item["id"]] = size
        rank_cones[item["id"]] = rank_size
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

    # Dormant projects referenced by active items — either scoped directly or governed via
    # `affects_projects`. Their constraint is disclosed on the board so no reader mistakes a
    # parked/suspended dormant item for silently-dropped work.
    dormant = queue_store.load_dormant(state_dir)
    referenced_dormant = sorted(
        d
        for d in dormant
        if any(
            d in [str(x).lower() for x in (i.get("projects") or [])]
            or d in [str(x).lower() for x in (i.get("affects_projects") or [])]
            for i in items
        )
    )

    flat = graph_is_flat(items, rank_cones)
    out: list[str] = [
        "<!-- GENERATED — DO NOT EDIT.",
        r"Canonical producer: F:\Claude-Profile\skills\next  (surfaced at ~/.claude/skills/next).",
        "Regenerate via render_queue.py after editing queue.yaml; never hand-edit this file.",
        "This is a repo-local read model, not a definition of /next behavior. -->",
        "",
        "# /next — work-item queue",
        "",
        f"Generated {generated_on.isoformat()} (synced). Anchor-first, leverage-ranked "
        "(per item-model.md). The single #1 move is chosen live by the skill from the "
        "anchor (stated focus, else roadmap order) and finalization leverage — not from dependency "
        "cone. This board is a status-grouped snapshot; within each section it orders by "
        "owner-gated+S, then effort, risk, id"
        + (", with `cone` leading only on a deep graph (this store is flat today)."
           if flat else ", with `cone` leading (deep graph).")
        + " Full algorithm: `~/.claude/skills/next/reference/item-model.md`.",
        "",
        f"Scope: `all`. Watermarks: {' · '.join(marks)}.",
    ]
    if barren:
        out.append(f"({'/'.join(barren)}: no items yet — run `init` to derive.)")
    out.append("")

    if referenced_dormant:
        out.append(
            f"> **Dormant project(s):** {', '.join(f'`{d}`' for d in referenced_dormant)} — "
            "reassessment-bound. Items scoped to them are parked; their probes are suspended "
            "(non-executable metadata) and render **SUSPENDED**, never verified. `/next` will "
            "not run or propose a command against a dormant repo."
        )
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
        bucket.sort(key=lambda i: sort_key(i, rank_cones, flat))
        out.append(f"## {title}")
        out.append("")
        for item in bucket:
            out.extend(render_item(item, cones, dormant))
            out.append("")

    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=Path(r"F:\Claude-Tools\state"))
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
