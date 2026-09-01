# `/next` store

Backing store for the `/next` skill (`~/.claude/skills/next/`). Answers "where is this at" and
"what should I do now" without re-sifting the ledgers every session.

## Files

| File | Role |
|---|---|
| `projects.yaml` | Registry. What projects exist, where they live, how to probe them. Hand-edited. |
| `queue.yaml` | **Canonical ACTIVE** work-item store + reconcile watermarks. Hand-editable and machine-written. |
| `queue-archive.yaml` | Closed-item provenance (`live`/`dropped` records moved out of the active queue). **Never delete records here** — they are the dedup index that stops merged PRs from being rediscovered as new work. Immutable under ordinary reconciliation; reopening archived work = a NEW item in `queue.yaml` with `follow_up_of: <archived-id>`. |
| `QUEUE.md` | Generated human view. Do not hand-edit — regenerated from `queue.yaml` (+ recent archive `live` records for the 30-day Live section) by `render_queue.py`. |
| `render_queue.py` | Deterministic `QUEUE.md` renderer: status-grouped sections, anchor-first/leverage intra-section order (cone applied only on a genuinely deep graph, measured from resolved `unblocks` edges — dangling refs never count toward ranking). Same store → same bytes; `--check` verifies. |
| `queue_store.py` | Two-tier loader/validator + dedup probes. Run bare after any hand edit (`OK`, exit 0). `--known-pr repo#N` / `--known-commit sha` answer "is this already represented?" across both tiers (exit 0 = known, 2 = unknown). |
| `test_queue_store.py` | `python -m pytest test_queue_store.py -q` — includes a live-store render check. |
| `DESIGN.md` | Why this exists and what it deliberately does not do. |

Two-tier rules (full contract: `~/.claude/skills/next/reference/item-model.md`):

- Archive eligibility: `dropped` or `live`, and not referenced by any active item's `blocked_by`.
  `landed` never archives — it is actionable ("verify it").
- Archived records move verbatim plus `archived_at` / `archived_reason` / `source_queue_version`.
- The `reconciled:` block holds structured watermark values only; sync narrative belongs in the
  sync report / commit message. History lives in git (`git log -p queue.yaml`).
- Migration note: `MIGRATION-2026-08-17-two-tier.md`.

## Usage

```
/next                      portfolio board across active projects, then drill in
/next bimpossible          ranked queue + the #1 move for one project
/next bimpossible sync     reconcile against reality since the last watermark
/next bimpossible init     first derivation for a project with no items yet
/next all deep             re-derive everything from scratch, ignoring the store
```

Names resolve against `key` or `aliases` in `projects.yaml`.

## Adding a project

Copy an entry in `projects.yaml`, set `key`, `path`, `aliases`, `active: true`. Point `ledgers` at
any status docs it keeps. Set `companions` if it ships in lockstep with another repo. Then:

```bash
/next <key> init
```

The skill needs no changes.

## The two invariants

**Cross-repo work is one item.** An item spanning BIMpossible and Add-Ins is a single entry with
`projects: [bimpossible, addins]`. Mirroring it into two per-project rows is how the existing ledgers
drift apart, and is the specific failure this store exists to prevent.

**`landed` is not `live`.** Merged means merged. Live requires runtime evidence — a flag observed on,
a smoke log read, a DB row seen. Most stranded value in this workspace sits between those two states.

## Source of truth and the published mirror

**This folder is the live canonical store** — its own local git repo (`master`), and where `/next`
actually reads and writes. Every write is diffable and revertible through its history.

It is also **published as a committed mirror** in the BIMpossible workspace repo at
`F:\BIMpossible-Workspace\.tools\state` (Option B, adopted 2026-08-08), so the queue is
visible, reviewable, and recoverable in GitHub rather than only on this machine. The rule:

- A successful `/next <target> sync` writes this live store, then regenerates `QUEUE.md` from
  `queue.yaml` with `render_queue.py` and **publishes both to the mirror together** (via the
  workspace `Push-And-Verify.ps1`).
- `projects.yaml` is NOT republished: the mirror's copy was retired 2026-08-22 (it still carries
  pre-cutover `F:\AI-Dev\*` paths and is kept only as historical state). The registry is read
  from this folder alone.
- `QUEUE.md` is generated output — never hand-edited, here or in the mirror.
- Reproducibility check, from either copy:

```bash
python render_queue.py --state-dir . --generated-on <YYYY-MM-DD> --check
```

Reports `CHECK OK` when `QUEUE.md` reproduces byte-for-byte from `queue.yaml`.

## What this is not

Not an audit. It reports status and ranks work; it does not hunt defects, fix code, commit, or push.
Code-correctness questions go to `/audit` (BIMpossible web) or `/revit-functionality-audit` (Add-Ins).
UX questions go to `/revit-tool-review`.

It never writes `BIMpossible_PHASE-STATUS.md` or `BIMpossible_WAVE-STATUS.md` — those stay
owner-maintained. When they go stale it says so and drafts the row for you to paste.
