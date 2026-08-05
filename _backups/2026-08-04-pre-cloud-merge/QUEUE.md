<!-- GENERATED from queue.yaml. Do not hand-edit — edit queue.yaml, then regenerate. -->

# /next — work-item queue

Generated 2026-07-27 (synced). Ranked by critical path (transitive `unblocks` cone), tiebreak:
owner-gated+S effort, then effort, then risk, then id. Full algorithm:
`~/.claude/skills/next/reference/item-model.md`.

Scope: `bimpossible`. Watermark: `reconciled.bimpossible` = 2026-07-27, commit `ff42ac3`, PR #231.

## Since the last read (2026-07-26 → 2026-07-27)

A full weekly-audit cycle ran and closed out (`weekly-full-audit_2026-07-27.md`, 12 Human-Review
findings, resolved via BIMpossible PR#231 + Add-Ins PR#46). Folded into the store:

- **RE-1 (High, carried 3 cycles) — CLOSED.** Fixed inside `P7-REVITLINK-MULTIUSER`; risk 4→2, title
  updated. Remaining scope is pure capacity work (RE-2/OPS-C1), not a live defect.
- **Dependabot HIGH alerts — CLOSED.** `SEC-DEPENDABOT-CI` retitled to what's actually left: the CI
  Actions merge-policy decision, untouched by this cycle.
- **Add-Ins secret-scan gate — CLOSED.** `ADDINS-HYGIENE` retitled; Glass rollout + conformance-PR
  dedup remain, untouched by this cycle.
- **`OPS-TENANCY-DOC` gained real evidence**, not just a documentation gap: `SEC-MEMBERSHIP-1` found
  a live isolation divergence, bounded to single-tenancy as an interim fix — the audit names the exact
  test still needed to close it for real.

**#1 move unchanged** — none of this touches Phase 3.10a.

## #1 move

**[P3-10A-GOLIVE]** Supervised owner flag-flip: go-live Cross-Model Room Join (Phase 3.10a) —
**needs the owner, not a build session.** Functionally proven 2026-07-15 (real warm-pipeline run:
1,239 footprints + 14,873 origins from 0; AC-1/2/3 pass); both flags still OFF. Closes by: a
supervised flag-flip on a test model, capturing AC-3 timing.

## Blocked on you

```
[P3-10A-GOLIVE] Supervised owner flag-flip: go-live Cross-Model Room Join (Phase 3.10a)
                unblocks 1 · S · bimpossible · CLAIMED 2026-07-26 · PHASE-STATUS.md Phase 3.10a

[P7-SYNC-GOLIVE] Supervised owner flag-flip: go-live Revit Link sync re-enable (Phase 7 step 2)
                 unblocks 0 · S · bimpossible+addins · CLAIMED 2026-07-26 · PR#187+AddIns#11, flag confirmed in code

[DOC-LEDGER-HYGIENE] Decide: retire or refresh stale NEXT.md against the new Roadmap doc
                     unblocks 0 · S · bimpossible+workspace · VERIFIED 2026-07-26 · NEXT.md header read live (2026-07-10)

[OD-DECISIONS] Decide OD3 (fire-alarm schedule owner) and OD4 (OSS reuse triage)
               unblocks 0 · S · bimpossible · CLAIMED 2026-07-26 · Verification Checklist standing rule
```

## Next up

```
[P13-T4-REFUSAL] Live-test Apply-Changes refusal paths -- non-cloud file, expired pane pairing
                 unblocks 1 · S · bimpossible+addins · VERIFIED 2026-07-26 · T4-live-smoke_RESULTS.md §5

[OPS-RESIDENCY-DOC] Write and publish a data residency/retention policy
                    unblocks 1 · S · bimpossible · CLAIMED 2026-07-26 · ProgramPlan checklist item 3

[OPS-TENANCY-DOC] Document and verify the multi-tenant data-isolation strategy
                  unblocks 1 · M · bimpossible · VERIFIED 2026-07-27 · SEC-MEMBERSHIP-1 (PR#231) + ProgramPlan item 1

[P3-8-SLICE23] Build Phase 3.8 slices 2-3 -- is_draft reader gating + ACC sync endpoint
               unblocks 1 · M · bimpossible · CLAIMED 2026-07-26 · PHASE-STATUS.md Phase 3.8; ProgramPlan item 4

[OPS-DIST] Code-sign Add-Ins + ship a real installer, including the Open-in-Revit opener
           unblocks 1 · L · bimpossible+addins · CLAIMED 2026-07-26 · PHASE-STATUS.md §Open-in-Revit

[OPS-DEPLOY-RUNBOOK] Formalize CI-driven deploy and a documented rollback procedure
                     unblocks 0 · S · bimpossible · CLAIMED 2026-07-26 · carried-open audit finding

[SEC-DEPENDABOT-CI] Decide the CI Actions merge policy (Dependabot HIGH alerts now closed)
                    unblocks 0 · S · bimpossible · VERIFIED 2026-07-27 · PR#231 SEC-NPMALERT-1, alerts at zero

[ADDINS-HYGIENE] Add-Ins hygiene: finish Glass rollout, dedupe 3 conformance PRs (secret-scan gate now added)
                 unblocks 0 · M · addins · VERIFIED 2026-07-27 · Add-Ins PR#46 SEC-ADDINS-NOSCAN-1

[P7-REVITLINK-MULTIUSER] Scale RevitLink to multi-user (RE-1 defect now fixed; RE-2 capacity limit remains)
                         unblocks 0 · M · bimpossible+addins · VERIFIED 2026-07-27 · Add-Ins PR#46 (RE-1 closed)

[P3-6-SPATIAL] Build Phase 3.6 Spatial Relationship Engine v1 (architecturally unblocked)
               unblocks 0 · M · bimpossible · CLAIMED 2026-07-26 · PHASE-STATUS.md Phase 3 sub-phase notes
```

## Blocked elsewhere

```
[P3-10B-DOORS] Build Doors schedule slice once the 3.10a pipeline runs live
               unblocks 0 · M · bimpossible · CLAIMED 2026-07-26 · blocked_by P3-10A-GOLIVE

[WRITE-ENGINE-INC1] Execute Write Engine typed-values + type-params Increment-1 (7 tasks + live smoke)
                    unblocks 0 · L · bimpossible · CLAIMED 2026-07-26 · blocked_by P13-T4-REFUSAL (sequencing judgment, not a hard block)

[OPS-LAUNCH] Clear the Commercial Launch Prerequisites checklist before first external deployment
             unblocks 0 · L · bimpossible · CLAIMED 2026-07-26 · blocked_by OPS-DIST, P3-8-SLICE23, OPS-TENANCY-DOC, OPS-RESIDENCY-DOC
```

---

No items currently in `landed`, `in_flight`, `parked`, or `live` (last 30 days) — by design, this
store only tracks actionable/gated work, not the full already-live capability catalog (that catalog
lives at `BIMpossible_ProductionRoadmap_2026-07-26.md` §1). The weekly-audit cycle itself is not
mirrored here — it has its own tracking in `02_Reference/Audit and Scan Info/`; only findings that
bore on an existing item were folded in.
