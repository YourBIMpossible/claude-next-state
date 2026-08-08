<!-- GENERATED from queue.yaml. Do not hand-edit — edit queue.yaml, then regenerate. -->

# /next — work-item queue

Generated 2026-08-07 (synced). Ranked by critical path (transitive `unblocks` cone), tiebreak:
owner-gated+S effort, then effort, then risk, then id. Full algorithm:
`~/.claude/skills/next/reference/item-model.md`.

Scope: `all`. Watermarks: `bimpossible` = 2026-08-07 @ `0fdf6e0` PR#317 · `addins` = 2026-08-07 @ `5160510` PR#61 · `workspace` = 2026-08-07 @ `11b79ec` PR#38. (ai-server/dashboard/families/pc-monitor:
no items yet — run `init` to derive.)

## Blocked on you

[HUB-TENANCY-GOLIVE] Seed firm->hub binding, migrate to head (NOT e0f1a2b3c4d5 -- 4 revisions behind), restart backend, run both tenancy smokes
       unblocks 2 · S · bimpossible · CONTRADICTED 2026-08-07 · BIMpossible #264 (90088f0), #265 (1fe6010), #266 (84c94c2), #267 (718…

[FE-3-10-FLAG] Rebuild the frontend with NEXT_PUBLIC_BIMPOSSIBLE_PHASE3_10_ENABLED=1 so room-join and door columns are visible
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-06 · frontend/Dockerfile:34-35 on origin/main -- ARG NEXT_PUBLIC_BIMPOSSIB…

[OPS-BACKUP-RESTORE-DRILL] -VerifyRestore proven live (147/147 rows); RPO/RTO table + named restore operator still open
       unblocks 1 · S · bimpossible+workspace · VERIFIED 2026-08-07 · 01_BuildLog/2026-08-05__product-risk-assessment.md finding W4/W5 (ori…

[P3-8-SLICE23] Merge Phase 3.8 slice 3 (ACC role sync); slice 2 still needs one owner ruling
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #275 OPEN DRAFT, head feat/phase38-draft-gating-and-acc-s…

[P7-SYNC-GOLIVE] Supervised owner flag-flip: go-live Revit Link sync re-enable (Phase 7 step 2)
       unblocks 0 · S · bimpossible+addins · CLAIMED 2026-08-04 · BIMpossible#187 (2936c32f) + AddIns#11 (be4d6a8f), lockstep, both mer…

[OPS-CLIENTDATA-REMEDIATION] Client-data remediation: quarantine delete, PDF triage, de-ID pass, DB audit
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-07 · decision-log/2026-08-05__client-data-remediation.md -- Open Items che…

[OPS-LOCAL-SIGNIN-AUTHLOOP] Local sign-in auth-loops, so no signed-in UI can be visually verified before it ships
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-06 · 01_BuildLog/2026-08-05__product-risk-assessment.md -- the local .env …

[WRITE-ENGINE-INC2] Merge Write Engine Increment 2 -- both halves built, CI green, awaiting owner merge decision
       unblocks 0 · S · bimpossible+addins · VERIFIED 2026-08-07 · BIMpossible #273 OPEN DRAFT, head feat/write-engine-increment2-typepa…

[OD-DECISIONS] Decide OD3 (fire-alarm schedule owner) and OD4 (OSS reuse triage)
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-04 · 02_Reference/Audit and Scan Info/BIMpossible_Verification_Checklist.m…

[PROD-DERIV-3] Discharge the DERIV-3 prod verification -- needs a mid-translation model and an APS upload
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-06 · 01_BuildLog/2026-08-05__hub-tenancy-migration-BLOCKED_HANDOFF.md -- '…

## Landed — not verified live

[SEC-ASSIST-FIRMVIEW] Merge #278 -- scope the assistant briefing's firm-view count to the caller's firm
       unblocks 2 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #278 MERGED 2026-08-07T04:44:03Z, squash commit 5190a4a41…

[POST-268-FOLLOWUPS] Merge the three post-#268 follow-up PRs -- reviewed, three-lane green, awaiting checks
       unblocks 2 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #269 (1887583), #270 (f6f0044), #271 (428889c) -- all MER…

[OPS-RESIDENCY-DOC] Data residency/retention policy PUBLISHED -- /data-policy page live, bs-5 closed
       unblocks 1 · S · bimpossible · CLAIMED 2026-08-04 · BIMpossible_ProgramPlan_2026-05-25.md, Commercial Launch Prerequisite…

[OPS-TENANCY-DOC] Write the multi-tenant data-isolation strategy doc (audit's required TEST already shipped in PR#243)
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible_ProgramPlan_2026-05-25.md, Commercial Launch Prerequisite…

[ARCH-FIRM-ALIAS-BACKEND] Firm-alias layer SHIPPED -- BIMpossible firm-literal baseline now ZERO (126 -> 21 -> 0), Add-Ins 29 -> 5
       unblocks 1 · S · bimpossible+addins · VERIFIED 2026-08-06 · BIMpossible #257 (85c3fff, MERGED 2026-08-05T23:43:21Z) -- backend/ae…

[SEC-GROUPS-DELIVERABLE-FIRM] Cross-firm NamedDeliverable IDOR in groups.py category derivation -- fixed and merged
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · backend/aec/groups.py:195-231 (_validate_members_and_compute_categori…

[SEC-GROUPS-PERSONAL-LISTING] list_groups personal-group cross-firm leak -- CONFIRMED and LANDED via PR #290 (independent parallel session won the race; see verification.by)
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-07 · backend/aec/groups.py:318-329 (list_groups, personal query) filtered …

[SEC-VIEWS-PERSONAL-LISTING] list_views' personal-views query has the same missing-firm_id gap as the fixed list_groups bug
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · backend/aec/views.py:207-218 (list_views, GET /data/views) -- persona…

[SEC-FIRMVIEW-TENANCY-280] PR#280 CLOSED as superseded by main's #276/#291 fix -- owner-directed, coverage check done
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #280 OPEN, 2 commits, 'feat(slack): tenancy enforcement f…

[SLACK-GATEWAY-W1] Read-only Slack assistant gateway merged, flag-off; migration 9329a1e7be85 now on main
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #262 MERGED 2026-08-07T04:20:29Z, squash commit dd898899e…

[OPS-SYNTH-AUDIT-HARDEN] Harden synthetic-concurrency-audit tooling: env-guard seeding, loopback-check host, fix schedule
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · weekly-full-audit_2026-08-04.md SEC-SCRIPTS-PERF-1, CQ-SYNTH-HOST-ENV…

[SEC-FIRMLITERAL-RATCHET-CI] Firm-literal CI ratchet was scanning the wrong config and passing vacuously -- fixed
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-06 · BIMpossible #279 (344164f) -- MERGED 2026-08-06; security-scan.yml RA…

[SEC-GROUPS-403-ORDERING] update_group/delete_group check the global allowlist (which echoes project_id) before the firm-ownership check
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-07 · Source: named-deliverable-personal-scope-firm-gaps.md finding #5, pro…

[SEC-GROUPS-PERSONAL-INDEX-FIRMID] uix_named_deliverables_personal_name_group unique index omits firm_id -- confirmed write-path only, not data corruption
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · Source: named-deliverable-personal-scope-firm-gaps.md finding #4, pro…

[SEC-VIEWS-PERSONAL-INDEX-FIRMID] uix_saved_views_personal_name (personal views/leaves unique index) omits firm_id -- same reassigned-user 409 dead-end as the groups sibling
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · CONFIRMED by direct read 2026-08-07 while fixing SEC-GROUPS-PERSONAL-…

[TENANCY-PROBE-281] Tenancy invariant now covers flag-gated routers; /probe hub isolation fixed, 41 routes triaged
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #281 MERGED 2026-08-07T02:48:19Z, squash commit 36412c9c9…

[DOC-ALEMBIC-REFS-274] Merge #274 -- fix three surviving database/alembic/versions doc references
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #274 (469173e) -- MERGED 2026-08-06 to main, by another s…

[OPS-REFRESH-FRONTEND-NODEPS] Fixed: Refresh-Frontend.ps1 was silently shipping backend code + migrations on a frontend-only deploy
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #289 (5d8d559, merged 2026-08-07T05:47:09Z) -- docker com…

[PROVIDER-REGISTRY-272] Provider key registry opened to 9 providers -- MERGED, not yet deployed
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-06 · BIMpossible #272 (79e9de5, squash) -- MERGED 2026-08-06; backend/aec/…

[SEC-GROUPS-VIEWS-404-EXISTENCE-ORACLE] PATCH/DELETE groups+views: nonexistent id returns 404 but cross-firm id returns 403 -- status-code existence oracle
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · Surfaced by the backend-endpoint-reviewer gate during SEC-GROUPS-403-…

[DEP-JSYAML-282] Dependabot js-yaml 4.3.0 -> 4.3.1 merged (GHSA-5p4m-2wfm-xmqj, dev-only transitive)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #282 MERGED 2026-08-07T02:30:12Z, squash commit 5d0379d32…

[OPS-NEUTRALITY-CLOSEOUT-D6] Neutrality + remediation closeout MERGED (#297); D-6 compare-mode soak running, owner go/no-go due 2026-08-15
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-07 · BIMpossible #297 (2332646) MERGED 2026-08-07 -- 'feat(closeout): reco…

[SEC-GROUPS-VIEWS-HUB-ISOLATION] groups.py + views.py routes check only the global project allowlist, never per-firm hub isolation
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-07 · Source: parallel session's memory record named-deliverable-personal-s…

[TEAMS-GATEWAY-W1] Microsoft Teams assistant gateway MERGED (#276) flag-gated off -- carries the firm-membership + hub-isolation fix
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-07 · BIMpossible #276 MERGED 2026-08-08T02:18:43Z as 879e857 'feat(teams):…

[WARM-ORIGIN-DOORGAP] Curtain-panel/unhosted doors have no origin: label them 'no location (curtain panel)' instead of deriving one
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-06 · 01_BuildLog/2026-08-04__doors-join-increment1_RESULTS.md, 'Follow-ups…

## Next up

[OPS-DIST] Code-sign Add-Ins + ship a real installer, including the Open-in-Revit opener
       unblocks 1 · L · bimpossible+addins · CLAIMED 2026-08-04 · BIMpossible_PHASE-STATUS.md §Open-in-Revit; BIMpossible_ProductionRoa…

[OPS-DEPLOY-RUNBOOK] Walk the deploy/rollback runbook draft on the prod host; fill VERIFY blanks
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-04 · Carried-open finding across multiple audit cycles, per BIMpossible_Pr…

[SEC-ASSIST-TOOLS-PERSONAL-VIEWS] Assistant's _visible_saved_view_clause personal branch has no firm_id scope -- feeds tool_list_saved_views + tool_describe_saved_view
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-07 · backend/aec/assistant_tools.py:295-309 _visible_saved_view_clause: fi…

[SEC-ASSIST-PERSONAL-VIEWCOUNT] Assistant briefing's personal_views count is the unfixed half of the SEC-ASSIST-FIRMVIEW function
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-07 · backend/aec/assistant_context.py:172-178 (_assemble_project_context) …

[ADDINS-SLOT-LEDGER] Runtime-slot handoff ledger is stale: deploys are landing without a ledger entry
       unblocks 0 · S · addins · VERIFIED 2026-08-06 · Add-Ins decision-log/2026-07-25__runtime-slot-handoff.md -- last modi…

[AISERVER-OPENCODE-DOCS] Commit AI-Server's uncommitted opencode/local-coding-agent doc updates (PROGRAM_PLAN.md, README.md)
       unblocks 0 · S · ai-server · CLAIMED 2026-08-07 · 2026-08-07 close: git status on F:/AI-Dev/AI-Server shows M CLAUDE.md…

[DEP-TRIAGE-2026-08] Nine Dependabot PRs open and waiting -- five are Action bumps the auto-merge policy deliberately holds for review
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · Open as of 2026-08-07 night (gh pr list, all non-draft): github-actio…

[OPS-WORKTREE-DRIFT-REVIEW] Per-repo drift ownership review: workspace uncommitted docs + .tools/state edits, BIMpossible behind-5 + dirty tree
       unblocks 0 · S · workspace+bimpossible · CLAIMED 2026-08-07 · Observed 2026-08-07 sync pass: workspace main carries 2 untracked d…

[TAILWIND-V4-VERIFY] Verify Tailwind v4 migration (#284) live in prod -- Docker image is baked, merge alone doesn't ship it
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-07 · BIMpossible #284 (89f1222, merged 2026-08-07T04:51:18Z) -- replaces p…

[DASH-BIMWATCH-WIRING] Wire bimwatch pipeline output into the live dashboard (index.html/data.js have zero references)
       unblocks 0 · S · dashboard · CLAIMED 2026-08-07 · 2026-08-07 session: grepped index.html and data.js in both Dashboard …

[SEC-GROUPS-VIEWS-PERSONAL-SAMEFIRM-EXISTENCE-ORACLE] PATCH/DELETE groups+views: same-firm personal-scope 403 lets a colleague infer a personal group/view id exists -- possibly by design
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-07 · Surfaced by the backend-endpoint-reviewer gate during SEC-GROUPS-VIEW…

[ADDINS-HYGIENE] Add-Ins hygiene: finish Glass rollout (conformance-PR dedup DONE 2026-08-04)
       unblocks 0 · M · addins · VERIFIED 2026-08-06 · Add-Ins #10 MERGED 2026-08-04 (squash, main 94b21ab -- Plans 1+2 conf…

[ARCH-BIMP-PARAMSET] Activate the BIMP_ shared-parameter set END TO END -- define the set, then wire BOTH the writer (installer) and the reader to real entry points
       unblocks 0 · M · addins · VERIFIED 2026-08-07 · WRITER, dormant: BIMpossible.RevitLink/Conformance/DeliverableParamet…

[P7-REVITLINK-MULTIUSER] Scale RevitLink to multi-user (RE-1 defect now fixed; RE-2 capacity limit remains)
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-08-04 · Verification Checklist item RL_P0_10 (single-pipe/single-secret const…

[P3-6-SPATIAL] Build Phase 3.6 Spatial Relationship Engine v1 (architecturally unblocked)
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-04 · BIMpossible_PHASE-STATUS.md Phase 3 sub-phase notes, Phase 3.6 row

## Blocked elsewhere

[OPS-LAUNCH] Clear the Commercial Launch Prerequisites checklist before first external deployment
       unblocks 0 · L · bimpossible · CLAIMED 2026-08-04 · BIMpossible_ProgramPlan_2026-05-25.md §Commercial Launch Prerequisite…

## Parked

[OPS-REDIS-P5] Flip WEB_CONCURRENCY>1 with redis leader-lock (Wave C-1 Phase 5)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · docker/REDIS-CUTOVER.md §Next -- confirmed exists on origin/main 2026…

[SEC-AUDIT-HASHCHAIN] Tamper-evident hash-chain for audit tables -- deferred, gated on trigger
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-06 · 00_Strategy/2026-08-06__Multi-Tenant_Data-Isolation_Strategy_DRAFT.md…

[FEAT-REVIT-DOOR-PLACEMENT] Explore capturing door placement Revit-side (FamilyInstance.Host + panel transforms) so curtain-panel doors can join to rooms
       unblocks 0 · L · bimpossible+addins · CLAIMED 2026-08-05 · decision-log/2026-08-05__door-origin-gap-curtain-panel.md -- proves A…

[OPS-CLIENT-DATA-REMEDIATION] Client-data remediation: 39 cached models, PDF sets, DB cache -- PARKED with triggers
       unblocks 0 · L · bimpossible+workspace · VERIFIED 2026-08-07 · BIMpossible/decision-log/2026-08-05__client-data-remediation.md (anot…

[RELAY-MULTITENANCY] Revit relay is globally routed -- one REVIT_RELAY_URL and one RELAY_SECRET for every firm
       unblocks 0 · L · bimpossible+addins · VERIFIED 2026-08-06 · backend/revit_link/native_adapter.py:53-57 -- one process-global REVI…

[OPS-HOSTING-MIGRATION] Migrate hosting from home PC to a cheap cloud VPS (staged path toward AWS/GCP)
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-04 · 00_Strategy/design-docs/2026-07-27__hosting-migration-home-pc-to-clou…

## Live (last 30 days)

[P13-T4-REFUSAL] Live-test Apply-Changes refusal paths -- non-cloud file, expired pane pairing
       unblocks 2 · S · bimpossible+addins · VERIFIED 2026-08-04 · addins main cfb4cc1 (T4 apply core); BIMpossible PR#229 b19674c + Add…

[P3-10A-GOLIVE] Cross-Model Room Join LIVE -- rollout flag DELETED, path unconditional (PR#244)
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-06 · BIMpossible_PHASE-STATUS.md Phase 3 sub-phase notes, Phase 3.10a row

[WRITE-ENGINE-INC1] Write Engine Increment-1 -- SHIPPED: Task 8 smoke passed, #232 + AddIns #49 merged lockstep
       unblocks 1 · L · bimpossible+addins · VERIFIED 2026-08-04 · 00_Strategy/design-docs/2026-07-26__write-engine-increment1_typed-val…

[WRITE-ENGINE-SHIPVEHICLE] Write Engine ship vehicle DECIDED: Phase 13 sub-increment (platform track reserved for later)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible_PHASE-STATUS.md row 13.1 (placed 2026-08-04 AM): 'ships a…

[RE-WIZ-POLL-2] Fix wizard provisioning poll: retry transient HTTP errors like its sibling loop does
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible PR#239 (68bb596, merged 2026-08-04) -- _await_project_act…

[SEC-BRACE-2] Bump brace-expansion override to 5.0.9 -- new HIGH GHSA-rgw5-rvv9-x895
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · gh api dependabot/alerts 2026-08-04: alert #3 OPEN HIGH, brace-expans…

[SEC-DEP-EXEC] Dependabot PR triage EXECUTED: closed 201+235, parked 200, merged 179/180/237 (redis smoked); 139 auto-merging
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · 00_Strategy/2026-08-04__ProductionQueue_Session_Findings.md §2 -- per…

[SEC-DEPENDABOT-CI] Decide the CI Actions merge policy (unreviewed third-party Action can merge to main)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible PR#242 MERGED f8b022f 2026-08-04 -- github_actions ecosys…

[ADDINS-PANE-PR45] Land Add-Ins PR#45 -- Assistant pane header dock fix (branch checked out locally)
       unblocks 0 · S · addins · VERIFIED 2026-08-06 · Add-Ins PR#45 'fix(revitlink): dock Assistant pane header to Top, com…

[DOC-DOCINDEX-DEFECTS-24] docindex: code root drops silently in a worktree; sub-chunk line attribution duplicates results
       unblocks 0 · S · workspace · VERIFIED 2026-08-07 · tools/docindex/docindex.config.json:34 -- code root path '../BIMpossi…

[DOC-LEDGER-HYGIENE] Retire stale NEXT.md: superseded banner applied, commit pending
       unblocks 0 · S · bimpossible+workspace · VERIFIED 2026-08-06 · 00_Strategy/NEXT.md header, read 2026-07-26: 'Updated 2026-07-10', pr…

[WS-NEXT-VERSIONING] Version /next skill + store + session docs into workspace repo (branch + draft PR)
       unblocks 0 · S · workspace · VERIFIED 2026-08-07 · 2026-08-04__ProductionQueue_Session_Findings.md §3 -- cloud session p…

[P3-10B-DOORS] Doors room-pair slice LIVE on main -- Increment 1 merged (PR#253); direction is Increment 2
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-06 · BIMpossible PR#253 'feat(3.10b): doors resolve to the room PAIR they …
