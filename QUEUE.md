<!-- GENERATED — DO NOT EDIT.
Canonical producer: F:\Claude-Profile\skills\next  (surfaced at ~/.claude/skills/next).
Regenerate via render_queue.py after editing queue.yaml; never hand-edit this file.
This is a repo-local read model, not a definition of /next behavior. -->

# /next — work-item queue

Generated 2026-09-23 (synced). Anchor-first, leverage-ranked (per item-model.md). The single #1 move is chosen live by the skill from the anchor (stated focus, else roadmap order) and finalization leverage — not from dependency cone. This board is a status-grouped snapshot; within each section it orders by owner-gated+S, then effort, risk, id, with `cone` leading (deep graph). Full algorithm: `~/.claude/skills/next/reference/item-model.md`.

Scope: `all`. Watermarks: `bimpossible` = 2026-09-23 @ `3ea5fc9a` PR#697 · `addins` = 2026-09-21 @ `baa9efe` PR#155 · `workspace` = 2026-09-21 @ `647c6b1` PR#154 · `evidence-compiler` = 2026-09-16 @ `a6977c8` PR#17 · `dashboard` = 2026-09-06 @ `efdcba1` PR#22.
(pc-monitor/bim-site: no items yet — run `init` to derive.)

> **Dormant project(s):** `families` — reassessment-bound. Items scoped to them are parked; their probes are suspended (non-executable metadata) and render **SUSPENDED**, never verified. `/next` will not run or propose a command against a dormant repo.

## Blocked on you

[OPS-DEPLOY-RUNBOOK] Deploy/rollback runbook: read-only VERIFY items closed; live drill needs owner approval
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · Carried-open finding across multiple audit cycles, per BIMpossible_P…

[OPS-CLIENTDATA-REMEDIATION] Client-data remediation: quarantine delete, PDF triage, de-ID pass, DB audit
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-31 · decision-log/2026-08-05__client-data-remediation.md -- Open Items ch…

[AI-ADDINS-GLASS-APPROVE-1] Uncommitted GlassButtonProfile.Approve change breaks pinned test GlassButtonProfileTests.NonErrorConfirmsStayCobaltPrimary (3 cases) -- owner call: update the test or revert ConfirmPrimaryFor
       unblocks 0 · S · addins · VERIFIED 2026-09-21 · F:/BIMpossible-AddIns/BIMpossible.RevitLink/Shared/GlassButtonProfil…

[CHAT-GATEWAY-291-OWNER-DECISIONS] Issue #291 owner decisions: binding lifecycle after denial, persisted identity bridge, cross-firm alerting threshold (decision package prepared, awaiting three sign-offs)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-06 · BIMpossible #582 docs(#291) -- squash 5f275baa, docs-only. Adds the …

[ONBOARDING-574-FRONTEND-REBUILD] PR #574 onboarding-flag frontend rebuild (owner-gated): backend fix already live; #574 needs NO rebuild; only the separate NEXT_PUBLIC onboarding-flag flip does
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-06 · BIMpossible #584 docs(#574) -- squash 29b46518, docs-only. Checklist…

[ADDINS-LINKPDF-OPEN-DOCS-PRS-145-148] Add-Ins open LinkPDF docs/hold PRs #145-#148: #145 acceptance review (clean docs), #146 B1/B2 policy (draft), #147 Feature E proposal (needs decision), #148 B2 packer HOLD -- none touch APS writes
       unblocks 0 · S · addins · CLAIMED 2026-09-21 · BIMpossible-AddIns#145

[CI-RUNTIME-P4P5-XDIST-SHADOW] CI runtime reduction phases 4/5 MERGED (#533 #536 #538 #539 #541 #543): xdist shadow evidence window OPEN from c015e6cc; promote only after >=20 runs AND >=14 days
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-16 · #533 08aa845c vitest 2 workers + happy-dom off network; #536 00ca052…

[DECIDE-WS-MIRROR-PR-146-STALE] Workspace draft PR #146 (/next mirror publish, AddIns delta 64a8a6b->320e63a) is stale vs newer mirror publishes -- close, do not merge
       unblocks 0 · S · workspace · CLAIMED 2026-09-21 · BIMpossible_Workspace#146

[OPS-1-ADDINS-AUDIT-GAP] Add-Ins/RevitLink audit dashboard card stuck stale: newer report has no severity/ID scheme to ingest
       unblocks 0 · S · workspace+addins · CLAIMED 2026-09-14 · workspace 00_Strategy/Dashboard/strategy_decisions_ledger.md row ops…

[OWNER-RELEASE-W1-9-RESIDUALS] Release W1-9 owner residuals: branch/worktree cleanup, FU1 flag-strictness, pin-split disposition
       unblocks 0 · S · bimpossible · CLAIMED 2026-09-22 · decisions/2026-09-22__release-closeout-verification-waves1-9.md

[PROD-DERIV-3] Discharge the DERIV-3 prod verification -- needs a mid-translation model and an APS upload
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-28 · 01_BuildLog/2026-08-05__hub-tenancy-migration-BLOCKED_HANDOFF.md -- …

[AUTHZ-SHADOW-WINDOW-VALIDITY] DEFERRED to pre-pilot re-entry (runbook Sec 6): shadow-window validity work only when a real pilot is prepared
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-16 · 2026-08-16 prod probe with SHADOW live: authz_decision_log holds onl…

[ADDINS-JTI-REPLAY-CROSS-PROCESS] Durable cross-process/restart replay semantics for the add-in syncAuth jti cache — only if a multi-process Revit topology becomes supported
       unblocks 0 · M · addins · CLAIMED 2026-08-23 · Distinct from ADDINS-JTI-REPLAY-PERSIST (single-process restart insi…

[ADDINS-KEYPLAN-LIVE-WRITE] Key Plan (Tool 20) live write -- owner flags A-C then first supervised write
       unblocks 0 · M · addins · VERIFIED 2026-09-10 · AddIns #110 'Key Plan (Tool 20): composite resolver, dry-run preview…

[ARCH-FIRM-ALIAS-DYNAMIC-SELECTION] Request-scoped tenant-safe alias-profile selection -- if multi-firm alias profiles are in scope
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-30 · 2026-08-30 ARCH-FIRM-ALIAS-BACKEND runtime verification scope note: …

[AUTHZ-AUDIT-ROW-SIGNING] Sign authz AuditRecord (actor_type/principal_id) at record time so audit rows are tamper-evident, matching the syncAuth attestation leg
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-21 · BIMpossible decision-log/2026-08-21__p7-hardening-followons-queued.m…

[P13-WRITE-ENGINE-INC3] Build Write Engine Increment 3, sequenced after Increment 2 ships
       unblocks 0 · M · bimpossible+addins · CLAIMED 2026-09-13 · BIMpossible_PHASE-STATUS.md, Phase 13 -- Write Engine Increment 3 na…

[P14-14G-RESIDENCY-REDACTION] Wire residency + redaction into 14g, update proposal doc §6
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-18 · BIMpossible_PHASE-STATUS.md, Phase 14 row 14g -- PLACED not ratified…

[DECIDE-DA4R-EMPTY-WORKTREE] Decide: BIMpossible worktree da4r-status-roadmap-30ceaa is an empty lane (0 ahead of main, clean, its PR #154 merged) owned by pinned session "DA4R Status Roadmap Orientation" -- retire or keep
       unblocks 0 · XS · bimpossible · VERIFIED 2026-09-12 · Drift review 2026-09-12: worktree at c654783b, 0 commits ahead of ma…

[DECIDE-WS-REVIEW-ARTIFACT-GATEA] Decide: Workspace worktree review-artifact-gatea holds 1 unpushed commit 5312cfd (review report for merged WS #154) -- push + PR, or drop the lane
       unblocks 0 · XS · workspace · VERIFIED 2026-09-14 · Drift review 2026-09-12: F:/BIMpossible-Workspace/.claude/worktrees/…

[DECIDE-WS-STALE-MIRROR-PUBLISH-PR146] Decide: draft PR #146 (state: publish /next sync mirror, addins delta 64a8a6b->320e63a) has sat open since 2026-09-11 -- update to the current canonical snapshot and merge, or close as superseded
       unblocks 0 · XS · workspace · CLAIMED 2026-09-14 · gh pr view 146 --repo YourBIMpossible/BIMpossible_Workspace (checked…

[EC-DOGFOOD-2] Continue Evidence Compiler dogfooding toward the next North Star review window
       unblocks 0 · M · evidence-compiler · VERIFIED 2026-09-16 · F:/Evidence Compiler/NORTHSTAR.md

[EC-RELEASE-1] First release PR — versioning, changelog, build verification, PyPI publish
       unblocks 0 · M · evidence-compiler · VERIFIED 2026-08-24 · Maintainer deferred first release until after real dogfooding (WORKL…

[P5-7-ELEMENT-VISUAL-PREVIEW] Run 2 feasibility spikes then build Element Visual Preview (5.7)
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-18 · BIMpossible_PHASE-STATUS.md, Phase 5 row 5.7 -- proposed, unratified…

[P15-15D-MODEL-WRITES] Build AI-assisted model writes (15d), gated on Phase 7 go-live
       unblocks 0 · L · bimpossible+addins · CLAIMED 2026-08-30 · BIMpossible_PHASE-STATUS.md, Phase 15 row 15d -- ledger states this …

[P6-CLIENTMGMT-E] Build self-serve client onboarding flow (Client-Mgmt E)
       unblocks 0 · L · bimpossible · VERIFIED 2026-09-13 · BIMpossible_PHASE-STATUS.md, Phase 6 row Client-Mgmt E -- absorbs pr…

## Landed — not verified live

[OPS-DEPLOY-2026-09-23-MERGES] Deploy merged #694 (backend restart) + #690/#688 (Refresh-Frontend) from shared checkout; verify 405 gone
       unblocks 2 · S · bimpossible · VERIFIED 2026-09-23 · 2026-09-23 delivery pass

[AUTHZ-OPTION-B-B1-ENTITLEMENT-FOUNDATION] Autodesk-first access (Option B) B1: per-user Autodesk entitlement foundation (aec/entitlement.py EntitlementCache, user/token-scoped, no firm-wide positive cache) -- PR #666 MERGED 2026-09-16, foundation only, NOT live
       unblocks 2 · M · bimpossible · VERIFIED 2026-09-21 · BIMpossible#666

[PHASE9-REOPENED-SCOPE] Phase 9 link-target RULED: cutsheets anchor to individual element (by family type)
       unblocks 1 · S · bimpossible · VERIFIED 2026-09-16 · BIMpossible_PHASE-STATUS.md row 9 (Product Data Ingestion) -- 'Reope…

[OBS-APS-PAIRING-BLOCK-METRIC] Measure background jobs blocked by the foreground-verdict-only pairing policy (demand evidence for the deferred APS service-context spike)
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-31 · IMPLEMENTED + MERGED 2026-08-31T01:55:35Z (PR#509 -> cc40768c). Stru…

[MODEL-INDEX-DELETION-RECONCILE] model_index_sync has no reconcile/tombstone pass -- index_discovered_models only ADDS rows from all-rvts; a lineage that becomes deleted/renamed in APS is never demoted, so /search/models can keep returning a model the Files view no longer lists
       unblocks 1 · M · bimpossible · VERIFIED 2026-08-24 · Surfaced 2026-08-22 by the Explore agent while root-causing WINCHEST…

[AUTHZ-OPTION-B-B2-DISCOVERY] Autodesk-first access (Option B) B2: discovery under BIMPOSSIBLE_AUTODESK_FIRST_ACCESS (default off) uses the signed-in user's own Autodesk entitlement, per-user APS caches, 401/403 invalidation, no enrollment rows -- PR #674 MERGED 2026-09-16 (supersedes #667), NOT live, flag NOT set
       unblocks 1 · L · bimpossible · VERIFIED 2026-09-21 · BIMpossible#674

[AUTHZ-INHERITANCE-P1] Authorization-Inheritance Phase 1: permission-projection foundation (spine)
       unblocks 1 · L · bimpossible · VERIFIED 2026-08-23 · BIMpossible #337 MERGED (squash b4515ba) 2026-08-15T00:06:40Z -- Pha…

[AUTHZ-SHADOW-ACTIVATE] AUTH-INH arc CLOSED 2026-08-16: foundation complete, enforcement deferred to pre-pilot validation (runbook Sec 6)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-13 · 2026-09-13 owner-run probe: `docker exec docker-backend-1 printenv B…

[AIS-RE-2-RENEW-FAIL-OPEN] AIS-RE-2 renewal fail-closed: stop assistant turn when hold renewal fails -- draft PR #694
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-23 · BIMpossible#694

[REVITLINK-OPAQUE-500-MAPPING] revit_link error mapping collapses distinct add-in refusals (NOT_SUPPORTED, DOC_NOT_FOUND, AMBIGUOUS_DOCUMENT, SYNC_FAILED) into one opaque INTERNAL_ERROR 500 with no detail
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-19 · backend/revit_link/native_adapter.py _COMMAND_ERROR_MAP (unknown cod…

[UX-SHARED-WITH-YOU-TITLE-IS-SHARE-LABEL] UX: Shared-with-you row titled with the owner's share label instead of the project name -- project_name now on the wire, label demoted to secondary metadata
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-14 · Observed 2026-09-13 ~22:30Z in the S&L grantee view: the row read "h…

[REVIT-OPEN-DOCS-POST-FIX] FE useRevitLink probe sends GET to POST-only /revit/list_open_documents (405, docs list always empty)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-23 · BIMpossible#690

[UPLOAD-DOWNLOAD-COVERAGE] Upload/download gap tests (firm-docs 413/quota/commit-cleanup/cross-firm dup, export deny) + manual smoke runbook -- draft PR #693
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-23 · 2026-09-23 ~15:40Z Chrome, app.yourbimpossible.com, TEST_ACCC_D_EL_S…

[UX-RECENTLY-OPENED-EPOCH-DATE] UX: Recently opened rendered 12/31/1969 for discovery-only models -- backend emits null for the 1970 sentinel, timeAgo guards non-positive/invalid timestamps
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-14 · Observed 2026-09-13 ~22:30Z in the S&L grantee view: Recently opened…

[AIS-RE-2-WIRE-EXTEND] AIS-RE-2 heartbeat extend() wired into assistant turn -- already merged in #684 (PR body stale)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-22 · 5689c9db

[CKA-DOC-MODEL-PR534] CKA project/private/multi-project/firm-library document model on AUTH-INH MERGED (#534); migration b7c8d9e0f1a2 applied locally; project scopes dark while gate is not ENFORCE
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible#534 MERGED 2026-09-02T02:58Z (squash 1f59bcf8): aec/firm…

[SEC-FIRMVIEW-TENANCY-280] PR#280 CLOSED as superseded by main's #276/#291 fix -- owner-directed, coverage check done
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #280 OPEN, 2 commits, 'feat(slack): tenancy enforcement …

[SLACK-GATEWAY-W1] Read-only Slack assistant gateway merged, flag-off; migration 9329a1e7be85 now on main
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #262 MERGED 2026-08-07T04:20:29Z, squash commit dd898899…

[ADDINS-PIPE-BUSY-BACKOFF] PipeServer pipe-busy listen backoff
       unblocks 0 · S · addins · VERIFIED 2026-09-10 · BIMpossible-AddIns#117

[AUTHZ-ENFORCE-KEYSTONE-PR530] Merged BIMpossible#530: AUTH-INH ENFORCE keystone + Phase 15c T5 end-to-end test (CKA Phase 18 step 1)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible#530 OPEN, READY, head 6d64390f, opened 2026-09-02T00:40Z…

[FE-UPLOAD-EXPORT-ERROR-UX] FE: SheetComposer silently skipped failed sheets -- #697 MERGED 3ea5fc9a, not yet refreshed into frontend (upload-error half dropped: live 415/409 readable)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-23 · BIMpossible#697

[FEAT-REVIT-PAIRING-COPY] Revit pairing SHIPPED as Copy/paste-only -- protocol-launch button removed after reliability rework
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-16 · BIMpossible #391 (Send-to-Revit protocol handoff + ?pair=revit deep …

[FIX-SHARE-LINK-VIEWER] Public share-link viewer page added -- every /share/<token> URL used to 404
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-08 · BIMpossible #321 (66d09f2, merged 2026-08-08) -- adds frontend/app/s…

[SEC-FIRMLITERAL-RATCHET-CI] Firm-literal CI ratchet was scanning the wrong config and passing vacuously -- fixed
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-06 · BIMpossible #279 (344164f) -- MERGED 2026-08-06; security-scan.yml R…

[SEC-GROUPS-403-ORDERING] update_group/delete_group check the global allowlist (which echoes project_id) before the firm-ownership check
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-13 · Source: named-deliverable-personal-scope-firm-gaps.md finding #5, pr…

[SEC-GROUPS-EDIT-PERM-ALIGN] Align firm-group edit-permission gating in the frontend (GRP-1, GRP-2)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-13 · BIMpossible #329 (c311e0d, merged 2026-08-08) -- GRP-1/GRP-2 firm-gr…

[ADDINS-2026-09-11-14-MERGE-COVERAGE] Add-Ins + BIMpossible + Workspace merges 2026-09-07..16 not previously indexed (dedup coverage): AddIns #123/#139/#142/#143/#144/#150/#151, BIMpossible #658, Workspace docs/remediation -- all landed, none deployed
       unblocks 0 · S · addins+bimpossible+workspace · CLAIMED 2026-09-21 · BIMpossible-AddIns#123

[ADDINS-AUDIT-0817-HARDENING] Audit-0817 hardening closeout -- pairing identity + installer/write-guard fixes (AddIns #68, #69)
       unblocks 0 · S · addins · VERIFIED 2026-08-23 · AddIns #68 'fix/audit-0817-pane-identity' MERGED 2026-08-23 -> fcfa4…

[ADDINS-HYGIENE-PASS-20260902] AddIns hygiene pass: evidence-compiler timeouts, FamilyFixer canonical root, 4 broken doc refs
       unblocks 0 · S · addins · VERIFIED 2026-09-07 · BIMpossible-AddIns#118

[AISERVER-OPENCODE-DOCS] Commit AI-Server's uncommitted opencode/local-coding-agent doc updates (PROGRAM_PLAN.md, README.md)
       unblocks 0 · S · ai-server · VERIFIED 2026-08-08 · AI-Server main 2172820 -- 'docs: document opencode local coding-agen…

[APS-PHASE12-COMPLETION-VERIFY] APS Phase 1/2 completion verification doc + 2-legged token test
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-07 · BIMpossible#603

[ARCH-BIMP-R1-ISSUE-JOIN-PROBE] R1 issue-join probe (read-only, flag-gated) + model_urn tenancy fix
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-23 · BIMpossible#360 MERGED 2026-08-23 -> b8142fca -- adds a read-only, f…

[AUTHZ-RECON-0814-P4P5-CLOSEOUT] 2026-08-14 reconciliation audit P4/P5 remediation PRs closed out (bundle)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-16 · BIMpossible#354 MERGED 2026-08-23 -> 83170620 -- 2026-08-14 reconcil…

[DOC-ALEMBIC-REFS-274] Merge #274 -- fix three surviving database/alembic/versions doc references
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · BIMpossible #274 (469173e) -- MERGED 2026-08-06 to main, by another …

[HELP-PILLAR1-SURFACE-COVERAGE-PR535] Help Pillar 1: surfaces.json manifest + coverage guards + 48 articles MERGED (#535); backend serving it since the 06:00Z restart, not smoke-checked
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible#535 MERGED 2026-09-02T03:03Z (squash bb83222a): backend/…

[HYGIENE-UNTRACKED-DOC-CONTRACT] docs-hygiene contract: untracked new docs no longer produce a false pass
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-07 · BIMpossible#604

[MODEL-INDEX-RECONCILE-NAMELESS-RVT-EDGE] model_index_sync reconcile: a discovered rvt with a valid id but momentarily missing/empty name is `continue`d before discovered_ids.add(item_id) (model_index_sync.py:93), so its live row is excluded from the discovered set and the tombstone sweep (model_index_sync.py:131-133) soft-deletes a still-present model until a later crawl returns the name and restores it
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-30 · BIMpossible#485 MERGED 2026-08-25 -> 1dba8553: 'fix(aec): support fa…

[OPS-DOGFOOD-EVIDENCE-HOOK] Gated Evidence Compiler dogfood hook landed -- preserves pre-#'docs/path-modernization-wave1' wiring, hardened
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-24 · BIMpossible#464 MERGED -> 008e76b (main). .claude/scripts/evidence-h…

[OPS-REFRESH-FRONTEND-NODEPS] Fixed: Refresh-Frontend.ps1 was silently shipping backend code + migrations on a frontend-only deploy
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #289 (5d8d559, merged 2026-08-07T05:47:09Z) -- docker co…

[P8-HUB-ACTIVATION-RUNBOOK] Write Phase 8 hub-activation runbook per OpenQuestions #5
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · WRITTEN 2026-08-18: BIMpossible_Workspace/00_Strategy/2026-08-18__Ph…

[PERF-PDP-PROXY-MISS-SENTINEL-EVICTION] Negative manifest memo shares the bounded ManifestCache and can evict real manifests
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · IMPLEMENTED 2026-08-30 (PR#504 open, commit aa1baa4e): ManifestCache…

[PERF-PDP-PROXY-PROJECT-MODEL-LIST] Bound and cache _list_project_models: two unbounded .all() queries per shared-texture miss
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · IMPLEMENTED 2026-08-30 (PR#502 open, commit 81881b1f): both queries …

[PROVIDER-REGISTRY-272] Provider key registry opened to 9 providers -- MERGED, not yet deployed
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-06 · BIMpossible #272 (79e9de5, squash) -- MERGED 2026-08-06; backend/aec…

[WINCHESTER-STALE-LINEAGE-LINK] Winchester - TEST project file list still links one TEST_Winchester_ELEC_R25.rvt entry to a dead item lineage (urn n53a4yy6RJu5fBMjDppI8A) -- Autodesk 'couldn't find this item', bounces to Autodesk sign-in
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-22 · Two links with an identical file_name in the project's file list res…

[COVERAGE-2026-09-22-BIMPOSSIBLE-PRS] Dedup coverage: BIMpossible PRs 679-683, 686, 687 (docs, superseded, gitleaks)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-22 · BIMpossible#679

[DEP-JSYAML-282] Dependabot js-yaml bumped to 4.3.2 (4.3.0->4.3.1
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #282 MERGED 2026-08-07T02:30:12Z, squash commit 5d0379d3…

[P7-RELAY-SESSION-LIFECYCLE] Customer-session relay lifecycle: the Revit add-in owns/activates the localhost relay in the signed-in session -- available when Revit starts, gone cleanly when Revit closes; no Windows service, Scheduled Task, NSSM, machine-wide secret store, or developer-only deploy path
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-08-30 · Reclassified from P7-RELAY-SERVICE-PERSIST by owner instruction 2026…

[TEAMS-GATEWAY-W1] Microsoft Teams assistant gateway MERGED (#276) flag-gated off -- carries the firm-membership + hub-isolation fix
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-07 · BIMpossible #276 MERGED 2026-08-08T02:18:43Z as 879e857 'feat(teams)…

[WFA-2026-09-14-L3-ASSISTANT-AI-CONTEXT] WFA 2026-09-14 L3: firm-scoped assistant AI-context policy -- ported into release #685 (#671 closed)
       unblocks 0 · M · bimpossible · VERIFIED 2026-09-22 · BIMpossible#685

[ADMIN-CONSOLE-NO-DOMAIN-OR-MEMBERSHIP-CONTROLS] Gap: the platform admin console cannot add a firm email domain or activate/reassign a membership -- a new client firm's first login can never link without a raw admin API call
       unblocks 0 · M · bimpossible · VERIFIED 2026-09-23 · BIMpossible#688

[APS-DISCOVERY-PAGINATE-FOLDER-CONTENTS] APS discovery: paginate folder contents before model-index tombstone reconciliation -- list_all_rvts folder-contents walk reads child.get('data') without following links.next (APS pages at 200), so a >200-item folder yields a successful-but-partial discovery set; the #466 reconcile pass then tombstones the omitted later-page models and hides them from search until re-discovered
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-24 · MERGED 2026-08-24T23:23Z: BIMpossible#474 -> squash 6a327f72 on main…

[ARCH-BIMP-PARAMSET] Activate the BIMP_ shared-parameter set END TO END -- define the set, then wire BOTH the writer (installer) and the reader to real entry points
       unblocks 0 · M · addins · VERIFIED 2026-08-30 · WRITER, dormant: BIMpossible.RevitLink/Conformance/DeliverableParame…

[AUDIT-2026-08-08-REMEDIATION] 2026-08-08 incremental audit: 25 findings resolved, CI green, report + resolution record filed
       unblocks 0 · M · bimpossible+workspace · VERIFIED 2026-09-07 · BIMpossible #324 (3116d10, merged 2026-08-08) -- H-1 slack require_i…

[AUDIT-2026-08-17-REMEDIATION] 2026-08-17 audit program CLOSED: BIMpossible remediation PRs merged, CI green, deployed
       unblocks 0 · M · bimpossible+workspace · VERIFIED 2026-08-31 · BIMpossible half of the 2026-08-17 audit remediation, all MERGED: #3…

[AUDIT-2026-08-24-REMEDIATION] 2026-08-24 audit remediation CLOSED: 4 PRs merged, deployed, CLAUDE.md rule added
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-24 · BIMpossible#467 MERGED -> 9ca63e5 (main 243fedc): shared_state boot …

[AUDIT-ESTATE56-CLOSURE-20260826] 2026-08-17 audit estate CLOSED 56->0: 2026-08-24/25/26 reconciliation across bimpossible+addins+workspace
       unblocks 0 · M · bimpossible+addins+workspace · VERIFIED 2026-09-07 · workspace 02_Reference/Audit and Scan Info/audit-closure-COMPLETE_20…

[FEAT-FAVORITES-HOME-V3] Per-user project/model favorites + Home v3 redesign SHIPPED (7-PR arc, deployed 2026-08-17)
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-17 · BIMpossible #392 (per-user pinned projects and models) -> #394 (wire…

[P15-15C-B-LIVE-READS] Session-bound live document reads (15c-B, old T1-T5), backend re-architecture pending
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-09-01 · BIMpossible_PHASE-STATUS.md, Phase 15 row 15c -- ledger's own wordin…

[SEC-PDP-G1-TEXTURE-BINDING] Design + test plan: authorized-model cdn_root acceptance for federated proxy textures (defect #5)
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-24 · BIMpossible#463 MERGED 2026-08-24 (squash) -> ac8ba6f on main. Imple…

[SEC-PDP-MODEL-INDEX-PAIRING] APS-verify the project<->item pairing recorded by _upsert_model_index / _record_model_version
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-31 · IMPLEMENTED + MERGED 2026-08-31T00:59:17Z (PR#507 -> 91822e70). Owne…

[WARM-ORIGIN-DOORGAP] Curtain-panel/unhosted doors have no origin: label them 'no location (curtain panel)' instead of deriving one
       unblocks 0 · M · bimpossible · VERIFIED 2026-09-16 · 01_BuildLog/2026-08-04__doors-join-increment1_RESULTS.md, 'Follow-up…

[R5-AECDM-PUSHDOWN] R5 AECDM query-pushdown lane MERGED -- flag-gated, read-only (PR #363)
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-17 · BIMpossible #363 MERGED (d56bd14, 2026-08-16T19:47:59Z, branch feat/…

[SEC-DATAFLOW-HARDENING-SCOPE] Backend<->Autodesk data-flow analysis + data-hardening scope doc PUBLISHED (docs-only)
       unblocks 0 · M · bimpossible · VERIFIED date-unknown · 

[SEC-PDP-SLICE0] PDP Slice 0 no-migration containment bundle MERGED -- Redis blob encryption, conversation tenancy re-check, worker fail-closed on revoked grant, ElementCache hub-key pin
       unblocks 0 · M · bimpossible · VERIFIED date-unknown · BIMpossible#448

[AUTHZ-OPTION-B-B3-CAPABILITY-ENROLLMENT] Autodesk-first access (Option B) B3: firm_allowed_* reclassified as firm capability enrollment under the flag (write=True only), enroll needs no hub-grant row, discover/available routes member-readable (own Autodesk resources), Account/Hubs UX capability wording -- PR #675 MERGED 2026-09-16 (supersedes #668), NOT live; B4+ owner-gated and flag must stay off until B4
       unblocks 0 · L · bimpossible · VERIFIED 2026-09-21 · BIMpossible#675

[AUTHZ-OPTION-B-B4-B6-WAVES-3-5-OPEN] Autodesk-first access (Option B) B4-B6 + authority policy -- merged via release #685, flag OFF
       unblocks 0 · L · bimpossible · VERIFIED 2026-09-22 · BIMpossible#685

[CKA-PILLAR2-FIRM-DOCS] Client Knowledge Assistant Pillar 2: per-firm client documents (upload, extraction, BM25 retrieval, assistant tool)
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-13 · BIMpossible #327 (46520a7, merged 2026-08-08) -- Pillar 2 v1: per-fi…

[R12-SHARE-AUTHORITY-CLOSURE] R12 cross-firm share authority: telemetry, lifecycle holes H1-H3, share-aware projection read gate
       unblocks 0 · L · bimpossible+workspace · VERIFIED 2026-09-16 · BIMpossible#605

[WFA-2026-09-14-REMEDIATION] WFA 2026-09-14 remediation: MERGED lanes only (L2 ci-docs #669, sharing #670/#672, AddIns #153 OOM hotfix + #155 L5 reliability). L3 assistant AI-context policy (#671, OPEN) split out to WFA-2026-09-14-L3-ASSISTANT-AI-CONTEXT
       unblocks 0 · L · bimpossible+addins · CLAIMED 2026-09-21 · BIMpossible#669

[CKA-PILLAR3-EXPLAINABILITY] Client Knowledge Assistant Pillar 3: client explainability (change sets, help handoff, model-health remedies, alert next-steps, Groups read parity)
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-13 · BIMpossible #326 (686b064, merged 2026-08-08) -- Pillar 3: change se…

[P17-0-CONTROL-PLANE] Build Integration Control Plane foundation (17.0), gates 17c+ expansion
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-30 · BIMpossible#500

## Next up

[ADDINS-SLOT-LEDGER] Runtime-slot handoff ledger is stale: deploys are landing without a ledger entry
       unblocks 0 · S · addins · VERIFIED 2026-08-23 · Add-Ins decision-log/2026-07-25__runtime-slot-handoff.md -- last mod…

[OPS-WORKTREE-DRIFT-REVIEW] Recurring per-repo drift review: workspace local behind-6/ahead-1 with dirty ledgers + untracked audit docs
       unblocks 0 · S · workspace+bimpossible · VERIFIED 2026-09-14 · 2026-08-07 (original): workspace carried 2 untracked docs (revitlink…

[DASH-STALENESS-BACKSLASH-ESCAPE] Sync-GraphStalenessReminder backslash-escape quadruples instead of doubles (latent, not live)
       unblocks 0 · S · dashboard · UNVERIFIED 2026-09-07 · Refresh-Dashboard.ps1 line 316, the backslash-escape replace inside …

[RECONCILE-RESIDUAL-DASHBOARD-EC-WATERMARKS] Unreconciled watermark scope: dashboard efdcba1..origin/HEAD (77 commits since 2026-09-06) and evidence-compiler a6977c8..origin/master (7 commits since 2026-09-16); watermarks deliberately NOT advanced
       unblocks 0 · S · dashboard+evidence-compiler · CLAIMED 2026-09-21 · YourBIMpossible/ai-dev-dashboard

[ADDINS-HYGIENE] Add-Ins hygiene: finish Glass rollout (conformance-PR dedup DONE 2026-08-04)
       unblocks 0 · M · addins · VERIFIED 2026-08-23 · Add-Ins #10 MERGED 2026-08-04 (squash, main 94b21ab -- Plans 1+2 con…

[P7-REVITLINK-MULTIUSER] Scale RevitLink to multi-user (RE-1 defect now fixed; RE-2 capacity limit remains)
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-08-23 · Verification Checklist item RL_P0_10 (single-pipe/single-secret cons…

[AUTODESK-FIRST-ROLLOUT-DELIVERY] Autodesk-first rollout: complete authority model, wire FE canDownload, then enable flag
       unblocks 0 · L · bimpossible · CLAIMED 2026-09-22 · decisions/2026-09-22__autodesk-first-rollout-and-download-capability…

## In flight

[AUDIT-2026-09-07-REMEDIATION] 2026-09-07 weekly audit remediation wave: Revit write-integrity + fail-open QA reads + pipe-kill-switch CI guard -- 3 merged, 2 open drafts
       unblocks 0 · L · addins · CLAIMED 2026-09-10 · Program root: Weekly Full Audit 2026-09-07. Ledger BIMpossible-Works…

[LINKPDF-ROADMAP-A-D] NORTHSTAR "Link PDF to Sheets" post-merge roadmap (Features A/B1/C1/D): per-feature review + live smoke, not yet accepted
       unblocks 0 · L · addins · CLAIMED 2026-09-12 · BIMpossible-AddIns #127 MERGED 2026-09-11 (merge commit 64a8a6b) und…

## Blocked elsewhere

[SHARED-PARAM-REGISTRY] Canonical shared-parameter registry landed (PR#174+hardening) -- generator only, nothing imports it yet
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-17 · BIMpossible #174 (41c716c, merged 2026-07-06) -- feat(shared-paramet…

[OPS-LAUNCH] Clear the Commercial Launch Prerequisites checklist before first external deployment
       unblocks 0 · L · bimpossible · CLAIMED 2026-08-31 · BIMpossible_ProgramPlan_2026-05-25.md §Commercial Launch Prerequisit…

[P13-T5-CROSSFIRM-APPROVAL] Build cross-firm approval flow (T5), depends on Client-Mgmt F
       unblocks 0 · L · bimpossible · CLAIMED 2026-08-22 · BIMpossible_PHASE-STATUS.md, Phase 13 -- proposed cross-firm-approva…

## Parked

[OPS-DIST] Add-Ins signed installer distribution -- installer pipeline proven; release package intentionally not frozen (product-timing park, owner 2026-08-31)
       unblocks 1 · L · bimpossible+addins · VERIFIED 2026-08-31 · BIMpossible_PHASE-STATUS.md §Open-in-Revit; BIMpossible_ProductionRo…

[AI-ADDINS-DEPLOY-EVIDENCE-1] 26MB untracked deploy-evidence/glass-smoke-baseline-20260913-120604/ in BIMpossible-AddIns -- decide keep/gitignore/delete
       unblocks 0 · S · addins · CLAIMED 2026-09-21 · F:/BIMpossible-AddIns/deploy-evidence/glass-smoke-baseline-20260913-…

[OPS-AIDEV-ORPHAN-TRANSCRIPTS] Delete orphan CLI transcripts under ~/.claude/projects/F--AI-Dev-BIMpossible-Workspace once the frozen-clone burn-in ends
       unblocks 0 · S · workspace · VERIFIED 2026-09-01 · Session "Workspace root path mismatch" 2026-09-01: 122 transcripts t…

[FAM-PREEXISTING-RED] Families has 1 failing test and 13 ruff errors already on HEAD
       unblocks 0 · S · families · SUSPENDED 2026-08-31 · tool/tests/test_revitlink_pipe_adapter.py::test_handle_reports_missi…
       ⏸ dormant project (families) — probes suspended (non-executable); state unverifiable until whole-repo reassessment

[OPS-REDIS-P5] Flip WEB_CONCURRENCY>1 with redis leader-lock (Wave C-1 Phase 5)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · docker/REDIS-CUTOVER.md §Next -- confirmed exists on origin/main 202…

[ADDINS-DPAPI-PREWARM] First-use DPAPI pre-warm in the add-in verifier to remove the cold-start latency on the first attestation after Revit launch
       unblocks 0 · S · addins · CLAIMED 2026-09-10 · Observed during the 2026-08-19/21 pilots as a one-time delay; not a …

[APS-BACKGROUND-VERIFICATION-PHASE-A] APS service-context feasibility spike (docs-and-repo-only) -- deferred behind blocked-job metric trigger
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-31 · Durable plan MERGED 2026-08-31 (PR#509): docs/plans/active/aps-backg…

[EC-RG-CAP-DET] Make capped ripgrep collection deterministic — packet membership varies on match-heavy repos
       unblocks 0 · M · evidence-compiler · VERIFIED 2026-08-24 · Boundary disclosed in PR#2 'Known Follow-up'; human ruled it a separ…

[CKA-DOCS-CAPABILITY-READ-MODEL] Capability-aware UI read model: expose project CONTROL, library_manager, Restricted and Financial eligibility so document controls/classification options render only where the server would permit them
       unblocks 0 · M · bimpossible · CLAIMED 2026-09-02 · #540 — client can only see is_owner + firm role; CONTROL/library_man…

[FAMILIES-DORMANT-REASSESS] Families dormant (owner ruling 2026-08-31): whole-repo reassessment gate carrying suspended probes, the retired twins contract, and 6 parked review findings
       unblocks 0 · M · workspace · CLAIMED 2026-08-31 · OWNER RULING 2026-08-31 (in-session, genuine human turn): Families i…
       ⛔ dormancy gate — governs dormant families; keeps the constraint visible without reactivating the repo

[SEC-AUDIT-HASHCHAIN] Tamper-evident hash-chain for audit tables -- deferred, gated on trigger
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-06 · 00_Strategy/2026-08-06__Multi-Tenant_Data-Isolation_Strategy_DRAFT.m…

[GATEA-APPROVAL] Gate A — approved, not started
       unblocks 0 · M · bimpossible · VERIFIED 2026-09-12 · 00_Strategy/2026-09-12__GateA_ApprovalMemo_and_BindingAddendum_Targe…

[P5-6-VISUAL-MODEL-GRAPH] Build Visual Model Graph frontend view (5.6, design doc ready)
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-18 · BIMpossible_PHASE-STATUS.md, Phase 5 row 5.6 -- ledger's own wording…

[P9-SOURCEPARSER] Build firm design-standards SourceParser when real demand appears
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-18 · BIMpossible_PHASE-STATUS.md, Phase 9 -- PLACED not ratified; ledger …

[CKA-DOC-ACTIONS-API] Backend/API slice on /firm-docs: permitted download, replace/version, archive, restore, re-placement (scope/project change). UI in #540 offers none of these because no contract exists.
       unblocks 0 · L · bimpossible · CLAIMED 2026-09-02 · #540 Known limitations section

[FEAT-REVIT-DOOR-PLACEMENT] Explore capturing door placement Revit-side (FamilyInstance.Host + panel transforms) so curtain-panel doors can join to rooms
       unblocks 0 · L · bimpossible+addins · CLAIMED 2026-08-23 · decision-log/2026-08-05__door-origin-gap-curtain-panel.md -- proves …

[OPS-CLIENT-DATA-REMEDIATION] Client-data remediation: 39 cached models, PDF sets, DB cache -- PARKED with triggers
       unblocks 0 · L · bimpossible+workspace · VERIFIED 2026-08-31 · BIMpossible/decision-log/2026-08-05__client-data-remediation.md (ano…

[RELAY-MULTITENANCY] Revit relay is globally routed -- one REVIT_RELAY_URL and one RELAY_SECRET for every firm
       unblocks 0 · L · bimpossible+addins · VERIFIED 2026-08-23 · backend/revit_link/native_adapter.py:53-57 -- one process-global REV…

[OPS-HOSTING-MIGRATION] Migrate hosting from home PC to a cheap cloud VPS (staged path toward AWS/GCP)
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-04 · 00_Strategy/design-docs/2026-07-27__hosting-migration-home-pc-to-clo…

## Live (last 30 days)

[BIMP-RESOLVE-BINDING] Verify durable model-resolve binding (RESOLVE-BIND-1) live after next backend deploy
       unblocks 3 · S · bimpossible · VERIFIED 2026-08-30 · BIMpossible#496 MERGED 2026-08-30 -> bf49d97e: durable firm-scoped m…

[ADDINS-RESOLVE-HINT-PROJECT] RevitLink relay: send hint_project_id on GET /aps/model/resolve first resolves
       unblocks 2 · S · addins · VERIFIED 2026-08-30 · BIMpossible#496

[CKA-DOCS-UI-PR540] CKA Documents placement + management UI (BIMpossible#540, follow-up #545): merged and deployed on the dev stack
       unblocks 2 · S · bimpossible · VERIFIED 2026-09-02 · https://github.com/YourBIMpossible/BIMpossible/pull/540 (draft, 4 co…

[ADDINS-SYNC-TOKEN-HANDSHAKE] Build in-process sync-token handshake in RevitLink add-in so EventDispatcher can safely allow sync_with_central over the pipe
       unblocks 2 · M · addins+bimpossible · VERIFIED 2026-08-30 · SyncWithCentralCommand.cs header comment (2026-07-16/2026-07-27 audi…

[OPS-LOCAL-BACKEND-BOOT-SEPARATE-APPROVER] Local backend crash-loops: set BIMPOSSIBLE_CHANGE_SET_REQUIRE_SEPARATE_APPROVER=1 in .env, restart
       unblocks 1 · S · bimpossible · VERIFIED 2026-09-22 · docker logs docker-backend-1 2026-09-22 21:20 PDT

[ARCH-FIRM-ALIAS-BACKEND] Firm-alias layer SHIPPED -- BIMpossible firm-literal baseline now ZERO (126 -> 21 -> 0), Add-Ins 29 -> 5
       unblocks 1 · S · bimpossible+addins · VERIFIED 2026-08-30 · BIMpossible #257 (85c3fff, MERGED 2026-08-05T23:43:21Z) -- backend/a…

[P3-8-SLICE23] Phase 3.8 slice 3 (ACC role sync) LIVE dark (deployed, flag OFF by design); slice-2 ruling resolved
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-31 · BIMpossible #275 MERGED 2026-08-17 (owner ruling: merge tonight, dar…

[ADMIN-DOMAIN-AUDIT-INACTIVE-FIRM-GUARD] Audit admin domain registration and block auto-link bootstrap against inactive firms
       unblocks 1 · S · bimpossible · VERIFIED 2026-09-01 · BIMpossible#449 DRAFT opened 2026-08-22 (fix/domain-audit-firm-guard…

[SEC-PDP-G1-VIEWER-PROXY] G1 SDK-shaped per-model Viewer proxy — viewer-token containment, staging-validated (flag OFF)
       unblocks 1 · M · bimpossible · VERIFIED 2026-09-16 · BIMpossible#456 MERGED 2026-08-23 -> 534d8038 -- authoritative proxy…

[ASSISTANT-MODEL-ROUTING-1A] AI model routing slice 1A + per-kind defaults SHIPPED and running on the local stack (#537, #542)
       unblocks 1 · M · bimpossible · VERIFIED 2026-09-02 · Anchor F:\Claude-Tools\reports\2026-09-01_ai-model-routing-plan.md (…

[DECIDE-NL-FILTER-AI-CONTEXT-CLASSIFICATION] Decide: is backend nl_filter.py a model-data AI surface under ai_context_policy (fail-closed) or an exempt query-parsing surface? (D5 open gap named in PR #661)
       unblocks 1 · XS · bimpossible · VERIFIED 2026-09-13 · PR #661 body, decision D5: "nl_filter.py is a distinct model-data ta…

[P3-8-SLICE2-DRAFT-GATING] Build slice-2 draft reader gating: owner-only visibility for is_draft memberships (owner ruling 2026-08-27)
       unblocks 1 · M · bimpossible · VERIFIED 2026-08-31 · MERGED 2026-08-30T23:12:46Z (owner-authorized squash merge): BIMposs…

[P6-CLIENTMGMT-F] Build cross-firm project sharing (Client-Mgmt F), gated on 3.12
       unblocks 1 · L · bimpossible · VERIFIED 2026-08-30 · BIMpossible_PHASE-STATUS.md, Phase 6 row Client-Mgmt F -- PLACED not…

[RELEASE-W1-9-DEPLOY] Deploy Waves 1-9 release #685 locally: backend-migrate job, restart, smoke
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-22 · BIMpossible#685

[CHAT-GATEWAY-MEMBERSHIP-291-VERIFY] Issue #291 Slack/Teams firm-membership contract re-verified on main; #577 documents the per-turn re-check transaction boundary; #291 stays open for owner policy decisions
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-05 · BIMpossible #577 docs(chat gateways) -- squash addfcedb, docstring-o…

[DOC-PHASESTATUS-191] PHASE-STATUS.md Phase 7 row already corrected -- sole #191 reference reads 'MERGED 2026-07-23'; no stale 'open' wording remains
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · BIMpossible #191 'Phase 7 Gate G2: SSA cloud-open spike (hand-run)' …

[BIMP-RELAY-ERROR-MAP-GAP] Backend _RELAY_ERROR_MAP lacks relay codes TIMEOUT / PIPE_BUSY / METHOD_NOT_ALLOWED -- they collapse to opaque 500s instead of typed 4xx/503 responses
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · Observed 2026-08-25 during P7-RELAY-SESSION-LIFECYCLE discovery: bac…

[NL-FILTER-EVAL-QUALITY] NL-filter intent-fidelity eval harness built and RUNNING WEEKLY IN CI with a live key
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-27 · BIMpossible #375 MERGED (989a2fb, 23:25Z) -- implements the BUILD NO…

[P7-SYNC-COMMENT-CRYPTO-BINDING] Sync comment crypto-binding: CLOSED BY OWNER RULING -- comment is non-authoritative collaboration metadata, no special binding required
       unblocks 0 · S · bimpossible+addins · VERIFIED 2026-08-27 · Today the token binds firm/user/document_title only (backend/revit_l…

[SEC-ASSIST-TOOLS-PERSONAL-VIEWS] FIXED+MERGED: assistant _visible_saved_view_clause personal branch now pins firm_id (PR #416)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · backend/aec/assistant_tools.py:295-309 _visible_saved_view_clause: f…

[AEC-PREWARM-TIP-PROBE-EMPTY-VERSION] E25_Nudge live tip-probe failure leaves receptacle_schedule perpetually preparing
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-16 · 2026-08-30 backend log, repeated on every poll for E25_Nudge-1800_Ow…

[BUG-GITLEAKS-HITS-COLLAPSE] Invoke-GitleaksScan collapses the whole findings array into one hit under PowerShell 5.1 - every multi-finding scan prints one System.Object[] line and HITS: 1
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · Observed 2026-08-31 while running the helper by hand before the main…

[BUG-SHARED-PROJECT-MODEL-PAGE-NO-HUB-ID] Bug: a cross-firm share recipient opening a shared model gets an empty table and an unbounded /data/elements poll loop -- the Shared-with-you link carries no hub_id
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-13 · Observed 2026-09-13 ~20:35Z during the cross-firm Smart Filter denia…

[DELIV-RECEIPT-GATE] Verify the Workspace leg of the exact-HEAD delivery receipt gate actually runs
       unblocks 0 · S · workspace+bimpossible · VERIFIED 2026-09-07 · BIMpossible_Workspace#128

[HYG-20260831-WORKSPACE-DOCS] Workspace docs-hygiene fixes (HYG-1/2/3) sit on an unpushed local branch with no PR
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · 3de8211 'fix(ci): gate docs-hygiene at PR time, not a week downstrea…

[OPS-AUDIT-UNATTENDED-ACCESS] Pre-grant Workspace + Add-Ins folder access to the scheduled weekly-audit session
       unblocks 0 · S · workspace · VERIFIED 2026-09-14 · 01_BuildLog/2026-08-31__weekly-full-audit-run.md step 1 + the report…

[R18-PROXY-MODE-FAIL-CLOSED] Harden R18: if cross-firm sharing is ON while derivative proxy mode is OFF, the byte scope is unenforced (Viewer runs on the app-level viewables:read token Autodesk serves directly). Make the unsafe combination fail closed -- boot invariant is the lowest-complexity option.
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-13 · ACTIVATION RECEIPT (owner-restarted 2026-09-13): merged SHA 9c50c190…

[R20-P310A-DISPLAY-FLAG] Owner call: was the 2026-08-15 go meant to activate the 3.10a display flag?
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-07 · F:/BIMpossible-Workspace/00_Strategy/2026-09-04__Phase3-Phase4-Needs…

[SEC-20260831-TEMP-CLONE-TOKEN-EXPOSURE] OWNER ATTENTION: live GitHub temp_clone_token committed to Workspace evidence JSON, redacted-in-tree only -- rotation/history-scrub decision needed
       unblocks 0 · S · workspace · VERIFIED 2026-09-01 · Workspace commit ecd6072 (2026-08-31, "security: redact live temp_cl…

[TEST-PYTEST-COLLECTS-NOTHING] pytest collects ZERO tests in Claude-Profile/hooks/tests and Claude-Tools/ctxcheck - green means nothing ran
       unblocks 0 · S · workspace · VERIFIED 2026-09-07 · `python -m pytest` in F:/Claude-Tools/ctxcheck reports `no tests ran…

[WRITE-ENGINE-INC2-UID] Enforce ElementType UniqueId contract for family-type staged writes
       unblocks 0 · S · bimpossible+addins · VERIFIED 2026-09-16 · Root cause + failed value: hosted change set 9c46b1f0-81a7-4d68-98d2…

[WSR-SECSCAN-LAUNCHGUARD] Run-Security-Scan.ps1 reports a stale report as a fresh one when a scanner fails to launch
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · F:/BIMpossible-Workspace/system/Run-Security-Scan.ps1 - four sequent…

[ADDINS-JTI-REPLAY-PERSIST] Persist (or TTL-bound) the add-in's process-local syncAuth jti replay cache so an add-in restart inside the 600s attestation TTL cannot re-enable a consumed attestation
       unblocks 0 · S · addins+bimpossible · VERIFIED 2026-08-31 · BIMpossible decision-log/2026-08-21__p7-hardening-followons-queued.m…

[AUTHZ-AUDIT-POISON-BATCH-FLOOD] authz shadow-audit poison row (firm_id='', principal 'service', reason 'wizard.account_read') fails UUID cast and re-queues the whole ~500-row batch every ~2s, flooding backend logs
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · aec/authz/audit.py flush_pending -- batch insert fails with psycopg2…

[DASH-DRIFT-GATE-UNTRACKED] Harden step-0b drift gate against untracked shadowing files (review finding #6)
       unblocks 0 · S · dashboard · VERIFIED 2026-09-02 · Code review 2026-08-31 finding #6 (PLAUSIBLE): Refresh-Dashboard.ps1…

[DASH-USAGE-AGENTS-REFRESH-REPAIR] Usage/Agents dashboard sources stale ~47d: scheduled refresh never invokes usage_sync.mjs / agents_sync.mjs
       unblocks 0 · S · dashboard · VERIFIED 2026-09-07 · ROOT CAUSE (2026-09-06): usage.js/agents.js carry generated=2026-07-…

[DATA-EMPTY-PERSIST-GUARD] Never persist empty categories/property/spec data version-immutably
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible #362 MERGED (0b314d8, 2026-08-16) -- never persist an em…

[EXACTLY-ONCE-579-OWNER-POLICY] PR #579 closeout DONE 2026-09-06: owner decisions applied (PT2H/PT12H kept, Weekly ExecutionTimeLimit PT4H, exhausted-window record) via PR #595 c8131efd; host tasks re-registered, zero drift
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-06 · BIMpossible #583 docs(#579) -- squash 64d95bae, docs-only. Readiness…

[OPS-AIMR1B-GITLEAKS-FIXTURE] Token-shaped model-routing fixtures cleaned up: 1b-branch fixture de-flagged (#548), #537 fixture renamed + dead fingerprint dropped (#553)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · Push-And-Verify.ps1 -GitleaksScope AllRefs 2026-09-02: POSSIBLE LEAK…

[OPS-SYNTH-AUDIT-HARDEN] Harden synthetic-concurrency-audit tooling: env-guard seeding, loopback-check host, fix schedule
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-07 · weekly-full-audit_2026-08-04.md SEC-SCRIPTS-PERF-1, CQ-SYNTH-HOST-EN…

[P8-APS-PUBLISHING-CAP] APS app publishing/production-review cap -- SETTLED: no cap blocks launch
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-25 · Owner confirmed 2026-08-25 (has been working the APS console directl…

[PUSH-SELFCHECK-BOOTSTRAP] Push-And-Verify self-check bootstrap: committed outgoing self-edits pass without -SkipSelfCheck
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · workspace 44ccf8d -- ancestor-aware stale-copy guard: on blob mismat…

[TENANCY-RAIL-SEARCH-RESOLVE] /search/models + /aps/model/resolve migrated off the ALLOWED_PROJECT_IDS rail
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible #366 MERGED (e585862, 2026-08-16) -- migrates /search/mo…

[WRITE-ENGINE-INC2] LIVE: Write Engine Increment 2 (family-type String targeting) -- Task 8 live smoke PASSED 2026-09-11 on hosted app + Revit 2026 pane (incl. #544 per-type outcome fix)
       unblocks 0 · S · bimpossible+addins · VERIFIED 2026-09-02 · BIMpossible #273 MERGED 2026-08-18T03:25Z (owner ruling 2026-08-17: …

[ADDINS-DOCS-HYGIENE-REQUIRED-CHECK] AddIns docs-hygiene is a required branch-protection check
       unblocks 0 · S · addins · VERIFIED 2026-09-07 · BIMpossible-AddIns#121

[ADDINS-NOT-SUPPORTED-PIPE-PROPAGATION] Propagate the typed NOT_SUPPORTED classification through PipeServer.cs so the add-in answers unsupported pipe methods with the typed code instead of a generic error
       unblocks 0 · S · addins+bimpossible · VERIFIED 2026-09-02 · Deferred from P7 hardening pass 2026-08-21 (BIMpossible#440 typed NO…

[ADMIN-DOMAIN-UNKNOWN-FIRM-404] Admin domain registration: return typed 404 for unknown firm instead of 409
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-13 · BIMpossible#657 (squash 3404e85a, MERGED 2026-09-13): add_domain als…

[AUDIT-20260831-CI-HYGIENE] 2026-08-31 audit closeout batch: CI/CQ/FE hygiene findings (SEC-CI-LOCAL-1, ARCH-CI-1, CQ-DOC-1, FE-2, FE-3) -- merged, live
       unblocks 0 · S · bimpossible+addins · VERIFIED 2026-09-01 · BIMpossible PR #522 (squash d27d9ef5, MERGED 2026-09-01) body -- clo…

[AUDIT-20260901-SH-CRLF-CI-FIX] CRLF-vulnerable .sh files from PR
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · BIMpossible PR #524 (squash 8aee44da, MERGED) -- "fix(firm-docs): en…

[AUTHZ-AUDIT-FIRMID-EMPTY-ROOTCAUSE] Root-cause the original producer of firm_id='' in authz audit batches (the poison quarantined by #440) and fix it at the source
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible#440 (02bd9b6) quarantines poisoned rows (AUTHZ-AUDIT-POI…

[BIMP-CLAUDEMD-POLICY-CI-20260831] CLAUDE.md policy-docs extraction + gate-sync CI selection + PR-time docs-hygiene ceilings
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · bimpossible #511 (4da2c142, MERGED 2026-08-31T20:13Z) -- extracts po…

[BIMP-P12-OPSDOCS-COMMIT] Five finished P7/P10-P12 relay ops closeout docs sit untracked in worktree bimpossible-next-f9990d (branch claude/bimpossible-next-dffbee) -- committing them trips doc-references.json (22 new unresolved: bare BIMpossible-AddIns .cs paths, relay bin/deploy artifact paths) and docs-budget.json (word ceiling, ~110.6k > 110k) simultaneously
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · Untracked files: docs/ops/2026-08-25-revit-dll-deployment-ownership-…

[CKA-DOCS-DEFAULT-SCOPE-DECISION] Default document scope on upload DECIDED: nothing preselected, Firm Library never a default (merged in #540)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · #540 UploadForm default scope firm_library

[DASH-BIMWATCH-WIRING] Wire bimwatch pipeline output into the live dashboard (index.html/data.js have zero references)
       unblocks 0 · S · dashboard · VERIFIED 2026-08-31 · 2026-08-07 session: grepped index.html and data.js in both Dashboard…

[DOC-GITLEAKS-INDETERMINATE-RECORD] gitleaks 'Indeterminate' status shipped with no decision record; a wiki page is the only synthesis that describes it
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · 9d1472d 'fix(push): never present an unverified gitleaks exit 1 as l…

[DOCS-DELIVERY-PHASE-SCORE-DOD] Delivery contract -- phase-score ledger update is part of definition-of-done
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · MERGED PR#508 (2026-08-31T01:23:13Z) -- docs(delivery): phase-score …

[DOORS-SINGLE-ROOM-BLANK-REASON] Phase 3.10b Doors: single-room door gets an explicit "(no second room)" blank reason
       unblocks 0 · S · bimpossible · CLAIMED 2026-09-07 · BIMpossible#611

[EC-HYGIENE-1] Delete merged lane branch safety/pre-sync-2026-09-06; master already synced to origin
       unblocks 0 · S · evidence-compiler · VERIFIED 2026-09-16 · evidence-compiler#17

[FIX-INHERITED-DOCS-REVITLINK-RECEIPT-662] Fix: inherited docs + Revit Link receipt test failures cleared (conftest + decision-log ref) -- #662
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-16 · BIMpossible#662 squash-MERGED 2026-09-13T18:48Z -> main 651b692a (ba…

[GITLEAKS-FIXTURE-MODEL-ROUTING-1A] Synthetic key in test_assistant_model_routing.py:463 replaced by a low-entropy dummy before #537 merged -- gitleaks blocker gone
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · Push-And-Verify on feat/cka-documents-placement-ui: gitleaks FAIL ru…

[NL-FILTER-EVAL-CRON-CONFIRM] Confirm the nl-filter-eval weekly schedule trigger actually fires (not just workflow_dispatch) -- CONFIRMED 2026-08-24
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-27 · BIMpossible#445 (dfe2a53) fixed DATABASE_URL provisioning; manual wo…

[OPS-CACHE-RECONCILE-V1] Quarantine-first cache-reconciliation worker, report-only v1
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible #364 MERGED (ed6ad70, 2026-08-16) -- cache reconciliatio…

[OPS-P7-CLOSEOUT-DOCS-PR529] Merge BIMpossible#529: land the 3 P7 relay closeout docs missing from main
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · BIMpossible#529 OPEN, READY (not draft), head 21766e6a, opened 2026-…

[OPS-PAV-GITLEAKS-PS51-EXIT] Push-And-Verify.ps1 gitleaks "failed to run" sentinel was unreachable on a launch failure (FIXED
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · Root cause: the gitleaks call sat in a try/finally with NO catch. Un…

[OPS-ROLLBACK-RETENTION-20260817] Intentional retention: rollback-20260817 image tags until deploy soak completes 2026-08-18 evening
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-13 · deploy closed live at alembic c4e7a2b91d38, 2026-08-17 ~22:00 PDT

[OPS-SLOPAUDIT-UNPUSHED] 8 slop-audit remediation commits are local-only across 5 repos - push or discard
       unblocks 0 · S · workspace+dashboard+families · CLAIMED 2026-08-31 · F:/AI-Dev/slop-audit-remediation_2026-08-31.md section 5 (full commi…
       ⏸ dormant leg (families) suspended — workspace+dashboard leg tracked live; dormant leg unverifiable until whole-repo reassessment, so the item is not fully verified

[P11-QA-HISTORY-CAPTURE-PATHS] Snapshot QA history from digest/assistant/coordination-report paths (today only warm model-health serves capture)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · PR #476 non-goals: coordination-report and digest/assistant paths ru…

[P11-QA-HISTORY-RECONCILE-PURGE] Integrate qa_analysis_runs orphan purge into cache_reconcile (models deleted from APS keep history rows until retention)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · PR #476 non-goals: retention prunes per-model depth only; nothing re…

[P13-T6-REASON-TAG] Add reason/criteria tag to approval flow (T6)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible_PHASE-STATUS.md, Phase 13 -- reason/criteria tag T6 RATI…

[P15-15C-A-CONTEXT-INJECTION] Safe Revit-context injection (15c-A), PR
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · BIMpossible PR #517 (MERGED 2026-09-01 as squash b27b25e0; was branc…

[P7-SYNC-REJECTION-AUDIT] Audit typed sync-token rejections (403 replay/expired/scope) in revit_link_request_log and carry firm_id on sync audit rows
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · 2026-08-21 pilot: replay -> 403 'Token has already been used (single…

[R18-UI-GATE-DOWNLOAD-ON-CANDOWNLOAD] Build (R18 UI b): gate the Download PDF / export / thumbnail controls on useSharedProject().canDownload, with explanatory text for view-only shares. Clarity/workflow only -- backend 404 share_view_only remains the security boundary.
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-13 · BIMpossible@f50ccb6e: useSharedProject exposes canDownload (false on…

[R18-UI-OWNER-SHARE-SCOPE-SELECT] Build (R18 UI a): owner share dialog gains a share-scope selection -- read (default) vs download (explicit opt-in) -- posting scope to the share-create/PATCH endpoints. Backend stays authoritative.
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-13 · PROMOTED blocked_owner -> in-flight 2026-09-13 under explicit owner …

[R19-INHERITANCE-PLAN-LANE] Confirm the superseded 2026-08-08 Authorization-Inheritance plan lane is dead
       unblocks 0 · S · workspace+bimpossible · VERIFIED 2026-09-07 · F:/BIMpossible-Workspace/00_Strategy/2026-09-04__Phase3-Phase4-Needs…

[ROUTER-SUPPORT-INDEX-KEY-MISMATCH] RESOLVED by PR #485: support fast-path now keys ModelIndex on the file_urn COLUMN (not item_id); regression tests pin item_id != file_urn
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · Found by Explore agent during P11 QA-history follow-ups session 2026…

[SEC-GROUPS-VIEWS-PERSONAL-SAMEFIRM-EXISTENCE-ORACLE] PATCH/DELETE groups+views: same-firm personal-scope 403 lets a colleague infer a personal group/view id exists -- possibly by design
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-16 · Surfaced by the backend-endpoint-reviewer gate during SEC-GROUPS-VIE…

[SEC-SCAN-177-TRACKING] security-scan "red on main" tracking issue #177 closed: PR-lane comments + semgrep never running on sweeps (FIXED #576)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-05 · Root cause 2026-09-05: every main sweep was green (33021258443, 3336…

[TEST-FLAKY-TEAMS-BIND-999] Flaky test de-flaked: test_bind_to_another_firms_project_is_refused no longer collides "999" with the echoed project id (FIXED #554)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · Verify-Local-CI backend DB lane 2026-09-02: FAILED tests/test_teams_…

[WAVESTATUS-CHECK-DEPLOY] Wave-Status PR-body-check MERGED live in BIMpossible + AddIns (advisory-only)
       unblocks 0 · S · bimpossible+addins · VERIFIED 2026-08-31 · BIMpossible #494 'ci: add advisory Wave-Status PR-body check' -- MER…

[ADDINS-CI-LOCALFIRST-COST] Local-first verification + installer CI cost control shipped and exercising on every PR
       unblocks 0 · S · addins · VERIFIED 2026-08-30 · AddIns #101 'Local-first verification and installer CI cost control'…

[ADDINS-HYGIENE-CCBUILD-UNTRACK] _cc_build_check build-output snapshot untracked, ignored, policy documented
       unblocks 0 · S · addins · VERIFIED 2026-08-30 · AddIns #108 'chore(hygiene): untrack _cc_build_check/ build-output s…

[ASSIST-CONVSTORE-CREATEDAT-497] Conversation-store turns stamped with created_at; test pins it (PR#497)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-30 · BIMpossible#497 (dd7c8600), merged 2026-08-30T19:56Z, CI green

[DASH-RELEASE-2026-08-31] Dashboard release wave: completion model, UX rework, refresh fixes, review fixes #1-#5
       unblocks 0 · S · dashboard · VERIFIED 2026-08-31 · ai-dev-dashboard #5 (completion model, 753882b), #6 (deploy-endpoint…

[P11-QA-HISTORY-UI-POLISH] QA history UI polish: muted history-unavailable state (today hides on fetch failure) + narrow compare payload typing; optional retention config UI
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · typescript-api-reviewer follow-ups on PR #476: hide-on-failure degra…

[AUDIT-2026-08-31-REMEDIATION] 2026-08-31 weekly audit: unguarded Alembic migrations (High) + 2 code Mediums -- FIXED, merged, live
       unblocks 0 · M · bimpossible+workspace · VERIFIED 2026-09-01 · 02_Reference/Audit and Scan Info/weekly-full-audit_2026-08-31.md (re…

[NL-FILTER-AI-CONTEXT-POLICY-WIRING] Build: put backend/aec/nl_filter.py under ai_context_policy fail-closed (owner D5 ruling 2026-09-13) -- deny model-data AI filtering unless the project policy allows it
       unblocks 0 · M · bimpossible · VERIFIED 2026-09-13 · Folded into PR #661 (branch feat/assistant-ai-context-policy) at com…

[R18-SHARE-READ-VS-BYTES] Build the explicit per-share download scope: read share is view-only, download opt-in (owner ruling 2026-09-07)
       unblocks 0 · M · bimpossible · CLAIMED 2026-09-12 · BIMpossible#654 (MERGED squash f50ccb6e 2026-09-12)

[SEC-WORKSPACE-GITLEAKS-EVIDENCE-HITS] Workspace gitleaks scan is NOT clean: 18 findings in three migration-evidence artifacts already published on origin - needs triage or an allowlist decision
       unblocks 0 · M · workspace · VERIFIED 2026-08-31 · gitleaks --source . on F:/BIMpossible-Workspace, 2026-08-31: 18 find…

[CI-POSTURE-LEAN-2026-09-11] CI cost-reduction posture (2026-09-11): heavy GitHub Actions removed; secret-scan once/PR, clean-room-ci deleted, wiring retired; enforcement moved to Verify-Local-CI.ps1
       unblocks 0 · M · bimpossible · VERIFIED 2026-09-12 · BIMpossible #637 (secret-scan once/PR, retire wiring), #652 (delete …

[DOCS-HYGIENE-ENFORCED] docs-hygiene enforced as a required check on main in both repos; the recurring Monday sweep failure is closed
       unblocks 0 · M · bimpossible+workspace · VERIFIED 2026-09-06 · BIMpossible #600 MERGED -> 0c6e2f02. docs-hygiene added to required …

[EXACTLY-ONCE-AUDIT-RELIABILITY-WORKTREE-OVERLAP] Foreign worktree .claude/worktrees/audit-reliability (branch claude/synthetic-audit-exactly-once-completion, at c8131efd) appeared 2026-09-06 after #595 merged -- confirm its owner is not re-doing the #579 closeout (ETL PT4H / exhausted-window record already on main)
       unblocks 0 · XS · bimpossible · VERIFIED 2026-09-16 · Seen in git worktree list during the 2026-09-06 closeout pass integr…

[P15-15B-EXTERNAL-DOC-INGEST] Firm-document retrieval in the Revit Assistant Pane (15b)
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-09-01 · BOTH HALVES MERGED 2026-08-31T04:22Z -- AddIns #113 (squash d09204e,…

[P3-6-SPATIAL] Build Phase 3.6 Spatial Relationship Engine v1 (architecturally unblocked)
       unblocks 0 · M · bimpossible · VERIFIED 2026-09-02 · BIMpossible_PHASE-STATUS.md Phase 3 sub-phase notes, Phase 3.6 row

[SYNC-2026-09-12-MISC-HARDENING] Standalone hardening merged before 2026-09-12 sync: assistant optimistic-rollback, relay-boundary CI allowlist, /audit skill relocate, Wave-9E dep bump (next 15.5.25 + sharp) + FE-CORRECT residuals, ctxcheck repoint off AI-Dev copy, NL-filter two-half drift monitor (ARCH-3C)
       unblocks 0 · M · bimpossible · VERIFIED 2026-09-12 · BIMpossible #626 (assistant optimistic rollback), #627 (relay bounda…

[WSCLOSEOUT-20260831-RECORDS] 2026-08-31 workspace closeout: review, authz, weekly-audit, PHASE-STATUS and slop-audit records published
       unblocks 0 · M · workspace · VERIFIED 2026-08-31 · One coherent publication wave, all ancestors of origin/main 1360a66:…

[ASSISTANT-AI-CONTEXT-POLICY] Assistant fail-closed project AI-context policy: project_configs.ai_context_policy + opaque navigation handles, Slack/Teams coverage (PR #661, MERGED + deployed 2026-09-13)
       unblocks 0 · L · bimpossible · VERIFIED 2026-09-13 · BIMpossible#661 (branch feat/assistant-ai-context-policy, head 0eb24…

[ASSISTANT-MODEL-ROUTING-1B-2] AI model routing lane COMPLETE: slice 5 LIVE 2026-09-04 (#567 cb427585 personal usage view + downgrade guard; #569 e5411f43 nl_filter on resolver); slice 4 #563 cade308f; slice 3.2 #559; #557/#558 LIVE
       unblocks 0 · L · bimpossible · VERIFIED 2026-09-04 · Anchor F:\Claude-Tools\reports\2026-09-01_ai-model-routing-plan.md (…

[WFA-2026-09-07-CODE-REMEDIATION] WFA 2026-09-07 code-repo remediation lane: firm-neutrality/raw-SQL/admin-fail-closed/hub-isolation/atomic-budget/APS-write-boundary/read-path-tenant-scope + relay CI lane
       unblocks 0 · L · bimpossible · VERIFIED 2026-09-12 · BIMpossible #619 (HYG-3/CQ-6 firm-neutrality gate), #620 (HYG-4 raw-…

[WFA-2026-09-11-CODE-REMEDIATION] WFA 2026-09-11 remediation wave (62 findings) code-repo lane: truth/logging/docs + frontend + ops/scripts + backend lanes + sessions-volume :ro migrate + SEC-1A hub fail-closed + consent multi-worker guard -- CLOSED per owner
       unblocks 0 · L · bimpossible · VERIFIED 2026-09-12 · BIMpossible #644 (audit-2026-09-11 truth/logging/docs), #645 (fronte…

[DASH-CHECKIN-CONSOLIDATION] AI-Dev dashboard daily check-in consolidation: reliable landing, delta triage, pulse, data-health, one home
       unblocks 0 · L · dashboard · VERIFIED 2026-09-06 · ai-dev-dashboard #22 SHIPPED -- squash-merged efdcba1 on origin/main…

[EC-HOOKSAFE-1] Python-native hook-safe launcher shipped to EC core; Node wrapper migrated out of BIMpossible/AddIns/Workspace/Families
       unblocks 0 · L · evidence-compiler+bimpossible+addins+workspace+families · CLAIMED 2026-08-24 · evidence-compiler#5
       ⏸ dormant leg (families) suspended — evidence-compiler+bimpossible+addins+workspace leg tracked live; dormant leg unverifiable until whole-repo reassessment, so the item is not fully verified

[P11-AC7-VERSIONED-SNAPSHOTS] Add versioned QA snapshots (Phase 11 AC7)
       unblocks 0 · L · bimpossible · VERIFIED 2026-09-16 · BIMpossible_PHASE-STATUS.md, Phase 11 -- AC7 (versioned QA snapshots…
