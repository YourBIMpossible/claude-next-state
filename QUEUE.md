<!-- GENERATED from queue.yaml. Do not hand-edit — edit queue.yaml, then regenerate. -->

# /next — work-item queue

Generated 2026-08-04 (synced). Ranked by critical path (transitive `unblocks` cone), tiebreak:
owner-gated+S effort, then effort, then risk, then id. Full algorithm:
`~/.claude/skills/next/reference/item-model.md`.

Scope: `all`. Watermarks: `bimpossible` = 2026-08-04 @ `2eb20c3` PR#241 · `addins` = 2026-08-04 @ `19c5ddd` PR#48 · `workspace` = 2026-08-04 @ `0dcd968`. (ai-server/dashboard/families/pc-monitor:
no items yet — run `init` to derive.)

## Blocked on you

[P3-10A-GOLIVE] Supervised owner flag-flip: go-live Cross-Model Room Join (Phase 3.10a)
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible_PHASE-STATUS.md Phase 3 sub-

[P7-SYNC-GOLIVE] Supervised owner flag-flip: go-live Revit Link sync re-enable (Phase 7 step 2)
       unblocks 0 · S · bimpossible+addins · CLAIMED 2026-08-04 · BIMpossible#187

[OD-DECISIONS] Decide OD3 (fire-alarm schedule owner) and OD4 (OSS reuse triage)
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-04 · BIMpossible_ProductionRoadmap_2026-07-26

## Landed — not verified live

[OPS-SYNTH-AUDIT-HARDEN] Harden synthetic-concurrency-audit tooling: env-guard seeding, loopback-check host, fix schedule
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible PR#239

[DOC-LEDGER-HYGIENE] Retire stale NEXT.md: superseded banner applied, commit pending
       unblocks 0 · S · bimpossible+workspace · VERIFIED 2026-08-04 · 2026-08-04: SUPERSEDED banner applied to 00_Strategy/NEXT.md

## Next up

[OPS-RESIDENCY-DOC] Write and publish a data residency/retention policy
       unblocks 1 · S · bimpossible · CLAIMED 2026-08-04 · BIMpossible_ProgramPlan_2026-05-25.md §C

[OPS-TENANCY-DOC] Document and verify the multi-tenant data-isolation strategy
       unblocks 1 · M · bimpossible · VERIFIED 2026-08-04 · BIMpossible PR#231

[P3-8-SLICE23] Build Phase 3.8 slices 2-3 -- is_draft reader gating + ACC sync endpoint
       unblocks 1 · M · bimpossible · CLAIMED 2026-08-04 · slice 1 migrations e6f7a8b9c0d1

[OPS-DIST] Code-sign Add-Ins + ship a real installer, including the Open-in-Revit opener
       unblocks 1 · L · bimpossible+addins · CLAIMED 2026-08-04 · BIMpossible_PHASE-STATUS.md §Open-in-Rev

[OPS-DEPLOY-RUNBOOK] Walk the deploy/rollback runbook draft on the prod host; fill VERIFY blanks
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-04 · BIMpossible_ProductionRoadmap_2026-07-26

[SEC-DEP-EXEC] Execute Dependabot PR triage: close 201+235, merge 139/179/180, 237 solo, park 200
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · gh pr list 2026-08-04

[ADDINS-HYGIENE] Add-Ins hygiene: finish Glass rollout, dedupe 3 conformance PRs (secret-scan gate now added)
       unblocks 0 · M · addins · VERIFIED 2026-08-04 · Add-Ins #10

[P7-REVITLINK-MULTIUSER] Scale RevitLink to multi-user (RE-1 defect now fixed; RE-2 capacity limit remains)
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-08-04 · Add-Ins PR#46

[P3-6-SPATIAL] Build Phase 3.6 Spatial Relationship Engine v1 (architecturally unblocked)
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-04 · BIMpossible_PHASE-STATUS.md Phase 3 sub-

## In flight

[WRITE-ENGINE-INC1] Run Task 8 live smoke, then land Write Engine Increment-1 (draft PRs #232 + AddIns #49)
       unblocks 1 · L · bimpossible+addins · VERIFIED 2026-08-04 · BIMpossible PR#232 draft 'Write Engine Increment 1 - typed v

[ADDINS-PANE-PR45] Land Add-Ins PR#45 -- Assistant pane header dock fix (branch checked out locally)
       unblocks 0 · S · addins · VERIFIED 2026-08-04 · Add-Ins PR#45 'fix(revitlink): dock Assistant pane header to

[WS-NEXT-VERSIONING] Version /next skill + store + session docs into workspace repo (branch + draft PR)
       unblocks 0 · S · workspace · VERIFIED 2026-08-04 · 2026-08-04__ProductionQueue_Session_Find

## Blocked elsewhere

[WRITE-ENGINE-SHIPVEHICLE] Decide Write Engine ship vehicle -- own phase/wave or Phase 13 sub-increment
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-04 · BIMpossible_ProductionRoadmap_2026-07-26

[P3-10B-DOORS] Build Doors schedule slice once the 3.10a pipeline runs live
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-04 · BIMpossible_PHASE-STATUS.md Phase 3.10b 

[OPS-LAUNCH] Clear the Commercial Launch Prerequisites checklist before first external deployment
       unblocks 0 · L · bimpossible · CLAIMED 2026-08-04 · BIMpossible_ProgramPlan_2026-05-25.md §C

## Parked

[OPS-REDIS-P5] Flip WEB_CONCURRENCY>1 with redis leader-lock (Wave C-1 Phase 5)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · docker/REDIS-CUTOVER.md; 2026-08-04 clou

[OPS-HOSTING-MIGRATION] Migrate hosting from home PC to a cheap cloud VPS (staged path toward AWS/GCP)
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-04 · design-docs/2026-07-27__hosting-migratio

## Live (last 30 days)

[P13-T4-REFUSAL] Live-test Apply-Changes refusal paths -- non-cloud file, expired pane pairing
       unblocks 2 · S · bimpossible+addins · VERIFIED 2026-08-04 · addins main cfb4cc1

[RE-WIZ-POLL-2] Fix wizard provisioning poll: retry transient HTTP errors like its sibling loop does
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible PR#239

[SEC-BRACE-2] Bump brace-expansion override to 5.0.9 -- new HIGH GHSA-rgw5-rvv9-x895
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · gh api dependabot/alerts 2026-08-04: alert #3 OPEN HIGH, bra

[SEC-DEPENDABOT-CI] Decide the CI Actions merge policy (unreviewed third-party Action can merge to main)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible PR#242 MERGED f8b022f 2026-08-04

