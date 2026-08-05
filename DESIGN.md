# `/next` — design record

Written 2026-07-26. The spec for the skill at `~/.claude/skills/next/`.

## Problem

Answering "where is this project at, and what should I do next" cost a long, argumentative session
every time, and produced a different answer each run. Root causes, from reading the actual artifacts:

1. **The ledgers are write-only archives.** `BIMpossible_PHASE-STATUS.md` carries ~900-word paragraphs
   inside single table cells and a six-deep `Prior: (Prior: (Prior:` header chain. Every fact is in
   there, which is precisely why nothing can be found. Any reader pointed at that file re-pays the
   full interpretation cost on every run.
2. **No cross-repo view.** Phase 13 T4 and Phase 15 span BIMpossible and BIMpossible-AddIns in
   lockstep PRs; the Dashboard renders from a third repo. No artifact spanned them, so status
   fragmented at exactly the seams where work actually crosses.
3. **Every existing tool is an audit, not a status.** `/audit`, `/revit-functionality-audit`,
   `/converge-review` hunt defects. Asked "where are we", they return a defect hunt — hence the
   re-wording and convincing.
4. **Stranded finished value is invisible.** A large class of work is built, merged, CI-green, and
   sitting behind a flag or an unrun supervised step. No artifact surfaced that as a class.

## Decision

A durable, minimal, cross-repo work-item store with **live verification on read**, plus fan-out as an
explicitly-invoked deep mode only.

Routes considered:

- **A — read-only reporter.** Rejected: re-pays interpretation cost every run and drifts in output
  quality run to run, which is the original complaint.
- **B — durable queue + live verification.** Chosen.
- **C — parallel fan-out every run.** Rejected as a default (slow, expensive, wrong for a routine
  check); retained as `all deep`.

## Decisions of record

| Decision | Rationale |
|---|---|
| Invocation is `/next`, not `/state` | The intent is a decision, not a snapshot. "state" survives as the store's name and report label. |
| Ranking primary axis = **critical path** (transitive `unblocks` cone) | Chosen by the owner over owner-gated-first, nearest-done, and risk-first. Those three survive as ordered tiebreakers. |
| Ranking is auditable, not inferred | Every item declares `unblocks` explicitly. An item with an empty cone can never rank #1. |
| **Cross-repo work items**, not per-repo rows | The pain is lockstep work across repos. Mirrored rows drift apart — that is the failure being designed out. Registry stays project-based; the board is a derived roll-up. |
| **Structured canonical store, markdown as a derived view** | "One line per item" as the canonical shape would have forced prose re-parsing on sync. Items carry machine-readable fields; display sections are computed from `status` and rank, never stored. |
| Central storage, one file | Low noise, one writer, survives worktree churn. Per-repo queues were the alternative — more faithful, more commit noise. |
| Store is never trusted alone | Deterministic facts are re-probed on every read. Without this the store becomes a second stale ledger, which would be strictly worse than no store. |
| Contradictions surfaced, never resolved | Silent resolution is how ledgers acquire confident wrong answers. |
| Owner ledgers are read-only to this skill | `PHASE-STATUS` / `WAVE-STATUS` are owner-maintained by their own rules. Staleness gets reported and a row gets drafted; the paste stays human. |
| v1 `sync` writes directly | Interactive propose→confirm deferred to v2 — write-flow UX is where these tools get messy first, and the cycle should be proven before adding a gate. Version history makes writes revertible. |
| No fixing, committing, pushing, defect-hunting | Those are `/audit`, `/revit-functionality-audit`, `/converge-review`, `/code-review`. Scope creep here would recreate problem 3. |

## The one distinction that carries the most weight

`landed` (merged) versus `live` (verified running, with named runtime evidence). Every source ledger
blurs these, and the blur is where finished-but-unearning work hides. The status vocabulary keeps
them separate and the reconcile procedure requires runtime evidence — not merge evidence — to cross
between them.

## Deferred to v2

- Interactive propose→confirm on `sync` writes.
- Automatic staleness nudges (scheduled/unattended runs).
- Rendering the board into the Dashboard.
- Effort estimates derived from history rather than hand-set `S/M/L`.

## Open at time of writing

- `F:\AI-Dev\Dashboard` and `F:\AI-Dev\Dashboard-auto` share one origin (`ai-dev-dashboard`). Two
  working copies of one repo. Which is canonical is unresolved; flagged in `projects.yaml`.
- The store is unversioned. `README.md` carries the one-liner to `git init` it; deliberately not run
  automatically, given the workspace's repo-sprawl guardrails.
- No project has been reconciled yet. `queue.yaml` is empty by design — the first `init` is the
  first real test of the model.
