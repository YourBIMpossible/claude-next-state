# Migration 2026-08-17 — two-tier store (queue.yaml + queue-archive.yaml)

Why: queue.yaml had grown to 267,717 bytes / 2,814 lines for 100 items — no longer hand-editable
in practice. Closed items could not simply be deleted because reconciliation dedups discovered
PRs/commits against every visible item; removal would cause merged work to be "rediscovered".

## Before → after

| | before | after |
|---|---|---|
| queue.yaml | 267,717 B / 2,814 lines / 100 items | 128,556 B / 1,497 lines / 57 items |
| queue-archive.yaml | — | 126,992 B / 43 items |
| `reconciled:` block | ~20 KB (9 syncs of diary comments) | structured watermark values only |

Active statuses after: landed 26 · ready 12 · blocked_owner 9 · parked 7 · blocked_dep 2 · live 1.
Archived: live 41 · dropped 2. Combined ids: 100 (complete — verified by loader).

## Decisions

- **`landed` stays active** (26 items). item-model.md defines it as actionable stranded value
  ("verify it"); archiving would hide exactly what the model exists to surface.
- **`live` archives regardless of age.** A 30-day-age rule was tried first and matched only 2
  items, because sync refreshes `verification.at` on every confirm. The QUEUE.md
  "Live (last 30 days)" section now renders from both tiers, so recent go-lives stay visible.
- **OPS-TENANCY-DOC (live) intentionally retained in active** — referenced by an active item's
  `blocked_by`; the hold rule keeps dependency resolution one-tier-local for active reads.
- **Records moved verbatim** (evidence/verification prose intact) + `archived_at`,
  `archived_reason`, `source_queue_version`.
- Cone/ranking math runs over the union of both tiers → archiving cannot change active ranking.
- Bare `PR#N` evidence refs (repo-ambiguous) are indexed under the item's `projects` keys.
- Removed `reconciled:` diary preserved in git history (`git log -p queue.yaml`, pre-d1c7ea6).

## Validation (all run 2026-08-17, in-lane)

```
python queue_store.py                              → OK — active 57 · archive 43 · ids 100 · exit 0
python render_queue.py --generated-on 2026-08-17 --check
                                                   → CHECK OK, byte-identical before AND after migration
python -m pytest test_queue_store.py -q            → 18 passed
python queue_store.py --known-pr BIMpossible#244   → KNOWN (archive) — archived PR not rediscoverable
python queue_store.py --known-commit fa865d6       → KNOWN (archive)
second-pass eligibility dry-run                    → candidates: NONE (idempotent)
```

Known pre-existing defect (reported, not fixed here): SEC-APSISO-TESTS-ENROLLMENT-EXPLICIT
missing `unblocks`/`source` — predates migration, carried into archive verbatim.

## Do not

- Do not delete archive records — they are the anti-rediscovery index.
- Do not edit archive records during sync. Reopen = new active item with `follow_up_of`.
- Do not write sync narrative into `reconciled:` — commit message / sync report instead.
