# Anchor — queue-archive-two-tier (2026-08-17)

Job: two-tier /next store. queue.yaml = active + minimal watermark; queue-archive.yaml =
closed-item provenance used for dedup; reconciliation consults both. Mandate: user prompt
2026-08-17 ("/next Queue Store — One-Pass Resolution").

Lane: `.tools/state` worktree `.claude/worktrees/queue-archive`, branch `queue-archive-two-tier`.
Repo is LOCAL-ONLY (no remote) → no push/PR possible; merge to master at the end is the
"ship" step. Skill docs live in F:\Claude-Profile\skills\next (separate repo, own commit).

## Pre-work done
- Pre-existing uncommitted 2026-08-17 workspace sync checkpointed as-is on master (3598d15).
- Code surface mapped: render_queue.py is the ONLY code; reconcile is skill-markdown procedure.
  Only structured fields of `reconciled:` are read (render_queue.py:151-157, reconcile.md schema).

## Phases
- A: compact `reconciled:` to structured values only. Done-criterion: render --check OK, isolated commit.
- B: queue_store.py loader/validator (active+archive union, dup ID/PR indexes, fail-loud,
  archive-optional back-compat); render_queue.py consumes it; cones computed over UNION,
  sections rendered from active only (preserves ranking exactly). Skill reference docs updated.
- C: pytest suite (test_queue_store.py) — no-rediscovery, dup rejection, malformed/missing archive,
  render consistency, archive immutability contract.
- D: migrate. ELIGIBILITY (decided, repo-semantics over prompt wording): archive `dropped` (always)
  and `live` with verification.at older than 30 days (outside QUEUE.md live window) AND not in any
  active item's blocked_by. `landed` stays ACTIVE — item-model.md defines it as actionable
  ("yes — verify it"); archiving it would hide stranded value, the model's core concern.
- E: docs (README/DESIGN/skill refs), migration note, merge lane→master, workspace mirror publish
  is a PUSH → leave to owner or existing Push-And-Verify path; flag if not done.

## Decisions + why
- landed NOT archived (see D). Prompt counted landed as inactive; item-model.md contradicts; prompt
  says code/skill semantics win.
- Cone math over union of both stores so archiving never changes ranking of active items.
- Archived refs in active unblocks are NOT dangling; validator resolves against combined index.

## Gotchas
- .gitattributes LF pinning exists only in the MIRROR repo, not here; local git warns LF→CRLF — harmless.
- Auto-mode classifier blocked a chained verify+commit Bash; split verify and commit into separate calls.

## Next entry point
Phase A in the worktree: edit queue.yaml reconciled block.
