# `/next` store

Backing store for the `/next` skill (`~/.claude/skills/next/`). Answers "where is this at" and
"what should I do now" without re-sifting the ledgers every session.

## Files

| File | Role |
|---|---|
| `projects.yaml` | Registry. What projects exist, where they live, how to probe them. Hand-edited. |
| `queue.yaml` | **Canonical** work-item store. Hand-editable and machine-written. |
| `QUEUE.md` | Generated human view. Do not hand-edit — regenerated on every write. |
| `DESIGN.md` | Why this exists and what it deliberately does not do. |

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

## Version history (recommended, not done for you)

This folder is not a git repo. The judgment accumulated in `queue.yaml` is the expensive part of this
system and is worth versioning. To do it — deliberately left for you to run, given the workspace's
repo-sprawl guardrails:

```bash
git -C "F:/AI-Dev/.tools/state" init && git -C "F:/AI-Dev/.tools/state" add -A && git -C "F:/AI-Dev/.tools/state" commit -m "next: initial store"
```

Local only, no remote needed. Alternative: include this folder in the existing `_backups` routine.

## What this is not

Not an audit. It reports status and ranks work; it does not hunt defects, fix code, commit, or push.
Code-correctness questions go to `/audit` (BIMpossible web) or `/revit-functionality-audit` (Add-Ins).
UX questions go to `/revit-tool-review`.

It never writes `BIMpossible_PHASE-STATUS.md` or `BIMpossible_WAVE-STATUS.md` — those stay
owner-maintained. When they go stale it says so and drafts the row for you to paste.
