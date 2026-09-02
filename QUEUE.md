<!-- GENERATED — DO NOT EDIT.
Canonical producer: F:\Claude-Profile\skills\next  (surfaced at ~/.claude/skills/next).
Regenerate via render_queue.py after editing queue.yaml; never hand-edit this file.
This is a repo-local read model, not a definition of /next behavior. -->

# /next — work-item queue

Generated 2026-09-01 (synced). Anchor-first, leverage-ranked (per item-model.md). The single #1 move is chosen live by the skill from the anchor (stated focus, else roadmap order) and finalization leverage — not from dependency cone. This board is a status-grouped snapshot; within each section it orders by owner-gated+S, then effort, risk, id, with `cone` leading (deep graph). Full algorithm: `~/.claude/skills/next/reference/item-model.md`.

Scope: `all`. Watermarks: `bimpossible` = 2026-09-01 @ `b7158ed8` PR#532 · `addins` = 2026-08-31 @ `d09204e` PR#115 · `workspace` = 2026-09-01 @ `9a8afb8` PR#112 · `evidence-compiler` = 2026-08-24 @ `0ef747e7533c7cf714888076f3df6f06dd028b84` PR#5 · `dashboard` = 2026-08-31 @ `387eefb` PR#10.
(pc-monitor: no items yet — run `init` to derive.)

> **Dormant project(s):** `families` — reassessment-bound. Items scoped to them are parked; their probes are suspended (non-executable metadata) and render **SUSPENDED**, never verified. `/next` will not run or propose a command against a dormant repo.

## Blocked on you

[CKA-DOCS-UI-PR540] Owner review of draft BIMpossible#540 (CKA Documents placement + management UI): upload defaults, reclassification, inaccessible-linked-project disclosure; then authorize remote CI / merge
       unblocks 2 · S · bimpossible · VERIFIED 2026-09-02 · https://github.com/YourBIMpossible/BIMpossible/pull/540 (draft, 4 co…

[OPS-DEPLOY-RUNBOOK] Deploy/rollback runbook: read-only VERIFY items closed; live drill needs owner approval
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · Carried-open finding across multiple audit cycles, per BIMpossible_P…

[OPS-CLIENTDATA-REMEDIATION] Client-data remediation: quarantine delete, PDF triage, de-ID pass, DB audit
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-31 · decision-log/2026-08-05__client-data-remediation.md -- Open Items ch…

[WARM-ORIGIN-ALLABSENT-ANOMALY] Investigate per-model AEC-DM warm gap: six model versions show 100% origin_absent across all door rows
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · 2026-08-24 probe: mvs 1329 (4/4), 1335 (1128/1128), 1336 (496/496), …

[ADDINS-DPAPI-PREWARM] First-use DPAPI pre-warm in the add-in verifier to remove the cold-start latency on the first attestation after Revit launch
       unblocks 0 · S · addins · CLAIMED 2026-08-23 · Observed during the 2026-08-19/21 pilots as a one-time delay; not a …

[CKA-DOCS-DEFAULT-SCOPE-DECISION] Owner decision: default document scope on upload (#540 defaults to Firm Library; alternatives Private or Project)
       unblocks 0 · S · bimpossible · CLAIMED 2026-09-02 · #540 UploadForm default scope firm_library

[OPS-1-ADDINS-AUDIT-GAP] Add-Ins/RevitLink audit dashboard card stuck stale: newer report has no severity/ID scheme to ingest
       unblocks 0 · S · workspace+addins · CLAIMED 2026-08-31 · workspace 00_Strategy/Dashboard/strategy_decisions_ledger.md row ops…

[PROD-DERIV-3] Discharge the DERIV-3 prod verification -- needs a mid-translation model and an APS upload
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-28 · 01_BuildLog/2026-08-05__hub-tenancy-migration-BLOCKED_HANDOFF.md -- …

[AUTHZ-SHADOW-WINDOW-VALIDITY] DEFERRED to pre-pilot re-entry (runbook Sec 6): shadow-window validity work only when a real pilot is prepared
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-16 · 2026-08-16 prod probe with SHADOW live: authz_decision_log holds onl…

[ADDINS-JTI-REPLAY-CROSS-PROCESS] Durable cross-process/restart replay semantics for the add-in syncAuth jti cache — only if a multi-process Revit topology becomes supported
       unblocks 0 · M · addins · CLAIMED 2026-08-23 · Distinct from ADDINS-JTI-REPLAY-PERSIST (single-process restart insi…

[ADDINS-KEYPLAN-LIVE-WRITE] Key Plan (Tool 20) live write -- owner flags A-C then first supervised write
       unblocks 0 · M · addins · VERIFIED 2026-08-31 · AddIns #110 'Key Plan (Tool 20): composite resolver, dry-run preview…

[ARCH-FIRM-ALIAS-DYNAMIC-SELECTION] Request-scoped tenant-safe alias-profile selection -- if multi-firm alias profiles are in scope
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-30 · 2026-08-30 ARCH-FIRM-ALIAS-BACKEND runtime verification scope note: …

[AUTHZ-AUDIT-ROW-SIGNING] Sign authz AuditRecord (actor_type/principal_id) at record time so audit rows are tamper-evident, matching the syncAuth attestation leg
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-21 · BIMpossible decision-log/2026-08-21__p7-hardening-followons-queued.m…

[P13-WRITE-ENGINE-INC3] Build Write Engine Increment 3, sequenced after Increment 2 ships
       unblocks 0 · M · bimpossible+addins · CLAIMED 2026-08-23 · BIMpossible_PHASE-STATUS.md, Phase 13 -- Write Engine Increment 3 na…

[P14-14G-RESIDENCY-REDACTION] Wire residency + redaction into 14g, update proposal doc §6
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-18 · BIMpossible_PHASE-STATUS.md, Phase 14 row 14g -- PLACED not ratified…

[EC-RELEASE-1] First release PR — versioning, changelog, build verification, PyPI publish
       unblocks 0 · M · evidence-compiler · VERIFIED 2026-08-24 · Maintainer deferred first release until after real dogfooding (WORKL…

[P5-7-ELEMENT-VISUAL-PREVIEW] Run 2 feasibility spikes then build Element Visual Preview (5.7)
       unblocks 0 · M · bimpossible · CLAIMED 2026-08-18 · BIMpossible_PHASE-STATUS.md, Phase 5 row 5.7 -- proposed, unratified…

[P15-15D-MODEL-WRITES] Build AI-assisted model writes (15d), gated on Phase 7 go-live
       unblocks 0 · L · bimpossible+addins · CLAIMED 2026-08-30 · BIMpossible_PHASE-STATUS.md, Phase 15 row 15d -- ledger states this …

[P6-CLIENTMGMT-E] Build self-serve client onboarding flow (Client-Mgmt E)
       unblocks 0 · L · bimpossible · CLAIMED 2026-08-18 · BIMpossible_PHASE-STATUS.md, Phase 6 row Client-Mgmt E -- absorbs pr…

## Landed — not verified live

[PHASE9-REOPENED-SCOPE] Phase 9 link-target RULED: cutsheets anchor to individual element (by family type)
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-30 · BIMpossible_PHASE-STATUS.md row 9 (Product Data Ingestion) -- 'Reope…

[OBS-APS-PAIRING-BLOCK-METRIC] Measure background jobs blocked by the foreground-verdict-only pairing policy (demand evidence for the deferred APS service-context spike)
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-31 · IMPLEMENTED + MERGED 2026-08-31T01:55:35Z (PR#509 -> cc40768c). Stru…

[SEC-PDP-G1-VIEWER-PROXY] G1 SDK-shaped per-model Viewer proxy — viewer-token containment, staging-validated (flag OFF)
       unblocks 1 · M · bimpossible · VERIFIED 2026-08-27 · BIMpossible#456 MERGED 2026-08-23 -> 534d8038 -- authoritative proxy…

[MODEL-INDEX-DELETION-RECONCILE] model_index_sync has no reconcile/tombstone pass -- index_discovered_models only ADDS rows from all-rvts; a lineage that becomes deleted/renamed in APS is never demoted, so /search/models can keep returning a model the Files view no longer lists
       unblocks 1 · M · bimpossible · VERIFIED 2026-08-24 · Surfaced 2026-08-22 by the Explore agent while root-causing WINCHEST…

[AUTHZ-INHERITANCE-P1] Authorization-Inheritance Phase 1: permission-projection foundation (spine)
       unblocks 1 · L · bimpossible · VERIFIED 2026-08-23 · BIMpossible #337 MERGED (squash b4515ba) 2026-08-15T00:06:40Z -- Pha…

[AUTHZ-SHADOW-ACTIVATE] AUTH-INH arc CLOSED 2026-08-16: foundation complete, enforcement deferred to pre-pilot validation (runbook Sec 6)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-16 · NORTHSTAR guardrail #1 (owner 'go' AND ratified revocation window, p…

[REVITLINK-OPAQUE-500-MAPPING] revit_link error mapping collapses distinct add-in refusals (NOT_SUPPORTED, DOC_NOT_FOUND, AMBIGUOUS_DOCUMENT, SYNC_FAILED) into one opaque INTERNAL_ERROR 500 with no detail
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-19 · backend/revit_link/native_adapter.py _COMMAND_ERROR_MAP (unknown cod…

[AEC-PREWARM-TIP-PROBE-EMPTY-VERSION] E25_Nudge live tip-probe failure leaves receptacle_schedule perpetually preparing
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · 2026-08-30 backend log, repeated on every poll for E25_Nudge-1800_Ow…

[SEC-FIRMVIEW-TENANCY-280] PR#280 CLOSED as superseded by main's #276/#291 fix -- owner-directed, coverage check done
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #280 OPEN, 2 commits, 'feat(slack): tenancy enforcement …

[SLACK-GATEWAY-W1] Read-only Slack assistant gateway merged, flag-off; migration 9329a1e7be85 now on main
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #262 MERGED 2026-08-07T04:20:29Z, squash commit dd898899…

[AUTHZ-ENFORCE-KEYSTONE-PR530] Merge BIMpossible#530: AUTH-INH ENFORCE keystone + Phase 15c T5 end-to-end test (CKA Phase 18 step 1)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · BIMpossible#530 OPEN, READY, head 6d64390f, opened 2026-09-02T00:40Z…

[DASH-DRIFT-GATE-UNTRACKED] Harden step-0b drift gate against untracked shadowing files (review finding #6)
       unblocks 0 · S · dashboard · VERIFIED 2026-08-31 · Code review 2026-08-31 finding #6 (PLAUSIBLE): Refresh-Dashboard.ps1…

[FEAT-REVIT-PAIRING-COPY] Revit pairing SHIPPED as Copy/paste-only -- protocol-launch button removed after reliability rework
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · BIMpossible #391 (Send-to-Revit protocol handoff + ?pair=revit deep …

[FIX-SHARE-LINK-VIEWER] Public share-link viewer page added -- every /share/<token> URL used to 404
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-08 · BIMpossible #321 (66d09f2, merged 2026-08-08) -- adds frontend/app/s…

[OPS-SYNTH-AUDIT-HARDEN] Harden synthetic-concurrency-audit tooling: env-guard seeding, loopback-check host, fix schedule
       unblocks 0 · S · bimpossible · CONTRADICTED 2026-09-01 · weekly-full-audit_2026-08-04.md SEC-SCRIPTS-PERF-1, CQ-SYNTH-HOST-EN…
       ⚠ both readings unresolved — STORE: guard wiring exercised on the next Monday run, exitCode 0/1 never 2. LIVE 2026-09-01: 2026-08-31 run exited 2 (wrapper container-recreate error…

[SEC-FIRMLITERAL-RATCHET-CI] Firm-literal CI ratchet was scanning the wrong config and passing vacuously -- fixed
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-06 · BIMpossible #279 (344164f) -- MERGED 2026-08-06; security-scan.yml R…

[SEC-GROUPS-403-ORDERING] update_group/delete_group check the global allowlist (which echoes project_id) before the firm-ownership check
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-07 · Source: named-deliverable-personal-scope-firm-gaps.md finding #5, pr…

[SEC-GROUPS-EDIT-PERM-ALIGN] Align firm-group edit-permission gating in the frontend (GRP-1, GRP-2)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-13 · BIMpossible #329 (c311e0d, merged 2026-08-08) -- GRP-1/GRP-2 firm-gr…

[WRITE-ENGINE-INC2] Write Engine Increment 2 MERGED dark -- BIMpossible #273 + AddIns #54 both landed 2026-08-17
       unblocks 0 · S · bimpossible+addins · VERIFIED 2026-09-02 · BIMpossible #273 MERGED 2026-08-18T03:25Z (owner ruling 2026-08-17: …

[ADDINS-AUDIT-0817-HARDENING] Audit-0817 hardening closeout -- pairing identity + installer/write-guard fixes (AddIns #68, #69)
       unblocks 0 · S · addins · VERIFIED 2026-08-23 · AddIns #68 'fix/audit-0817-pane-identity' MERGED 2026-08-23 -> fcfa4…

[AISERVER-OPENCODE-DOCS] Commit AI-Server's uncommitted opencode/local-coding-agent doc updates (PROGRAM_PLAN.md, README.md)
       unblocks 0 · S · ai-server · VERIFIED 2026-08-08 · AI-Server main 2172820 -- 'docs: document opencode local coding-agen…

[ARCH-BIMP-R1-ISSUE-JOIN-PROBE] R1 issue-join probe (read-only, flag-gated) + model_urn tenancy fix
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-23 · BIMpossible#360 MERGED 2026-08-23 -> b8142fca -- adds a read-only, f…

[AUTHZ-RECON-0814-P4P5-CLOSEOUT] 2026-08-14 reconciliation audit P4/P5 remediation PRs closed out (bundle)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-23 · BIMpossible#354 MERGED 2026-08-23 -> 83170620 -- 2026-08-14 reconcil…

[DOC-ALEMBIC-REFS-274] Merge #274 -- fix three surviving database/alembic/versions doc references
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · BIMpossible #274 (469173e) -- MERGED 2026-08-06 to main, by another …

[MODEL-INDEX-RECONCILE-NAMELESS-RVT-EDGE] model_index_sync reconcile: a discovered rvt with a valid id but momentarily missing/empty name is `continue`d before discovered_ids.add(item_id) (model_index_sync.py:93), so its live row is excluded from the discovered set and the tombstone sweep (model_index_sync.py:131-133) soft-deletes a still-present model until a later crawl returns the name and restores it
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-30 · BIMpossible#485 MERGED 2026-08-25 -> 1dba8553: 'fix(aec): support fa…

[OPS-DOGFOOD-EVIDENCE-HOOK] Gated Evidence Compiler dogfood hook landed -- preserves pre-#'docs/path-modernization-wave1' wiring, hardened
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-24 · BIMpossible#464 MERGED -> 008e76b (main). .claude/scripts/evidence-h…

[OPS-REFRESH-FRONTEND-NODEPS] Fixed: Refresh-Frontend.ps1 was silently shipping backend code + migrations on a frontend-only deploy
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #289 (5d8d559, merged 2026-08-07T05:47:09Z) -- docker co…

[P8-HUB-ACTIVATION-RUNBOOK] Write Phase 8 hub-activation runbook per OpenQuestions #5
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-18 · WRITTEN 2026-08-18: BIMpossible_Workspace/00_Strategy/2026-08-18__Ph…

[PERF-PDP-PROXY-MISS-SENTINEL-EVICTION] Negative manifest memo shares the bounded ManifestCache and can evict real manifests
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · IMPLEMENTED 2026-08-30 (PR#504 open, commit aa1baa4e): ManifestCache…

[PERF-PDP-PROXY-PROJECT-MODEL-LIST] Bound and cache _list_project_models: two unbounded .all() queries per shared-texture miss
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · IMPLEMENTED 2026-08-30 (PR#502 open, commit 81881b1f): both queries …

[PROVIDER-REGISTRY-272] Provider key registry opened to 9 providers -- MERGED, not yet deployed
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-06 · BIMpossible #272 (79e9de5, squash) -- MERGED 2026-08-06; backend/aec…

[SEC-GROUPS-VIEWS-PERSONAL-SAMEFIRM-EXISTENCE-ORACLE] PATCH/DELETE groups+views: same-firm personal-scope 403 lets a colleague infer a personal group/view id exists -- possibly by design
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · Surfaced by the backend-endpoint-reviewer gate during SEC-GROUPS-VIE…

[WINCHESTER-STALE-LINEAGE-LINK] Winchester - TEST project file list still links one TEST_Winchester_ELEC_R25.rvt entry to a dead item lineage (urn n53a4yy6RJu5fBMjDppI8A) -- Autodesk 'couldn't find this item', bounces to Autodesk sign-in
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-22 · Two links with an identical file_name in the project's file list res…

[DEP-JSYAML-282] Dependabot js-yaml 4.3.0 -> 4.3.1 merged (GHSA-5p4m-2wfm-xmqj, dev-only transitive)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · BIMpossible #282 MERGED 2026-08-07T02:30:12Z, squash commit 5d0379d3…

[P7-RELAY-SESSION-LIFECYCLE] Customer-session relay lifecycle: the Revit add-in owns/activates the localhost relay in the signed-in session -- available when Revit starts, gone cleanly when Revit closes; no Windows service, Scheduled Task, NSSM, machine-wide secret store, or developer-only deploy path
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-08-30 · Reclassified from P7-RELAY-SERVICE-PERSIST by owner instruction 2026…

[TEAMS-GATEWAY-W1] Microsoft Teams assistant gateway MERGED (#276) flag-gated off -- carries the firm-membership + hub-isolation fix
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-07 · BIMpossible #276 MERGED 2026-08-08T02:18:43Z as 879e857 'feat(teams)…

[APS-DISCOVERY-PAGINATE-FOLDER-CONTENTS] APS discovery: paginate folder contents before model-index tombstone reconciliation -- list_all_rvts folder-contents walk reads child.get('data') without following links.next (APS pages at 200), so a >200-item folder yields a successful-but-partial discovery set; the #466 reconcile pass then tombstones the omitted later-page models and hides them from search until re-discovered
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-24 · MERGED 2026-08-24T23:23Z: BIMpossible#474 -> squash 6a327f72 on main…

[ARCH-BIMP-PARAMSET] Activate the BIMP_ shared-parameter set END TO END -- define the set, then wire BOTH the writer (installer) and the reader to real entry points
       unblocks 0 · M · addins · VERIFIED 2026-08-30 · WRITER, dormant: BIMpossible.RevitLink/Conformance/DeliverableParame…

[AUDIT-2026-08-08-REMEDIATION] 2026-08-08 incremental audit: 25 findings resolved, CI green, report + resolution record filed
       unblocks 0 · M · bimpossible+workspace · VERIFIED 2026-08-31 · BIMpossible #324 (3116d10, merged 2026-08-08) -- H-1 slack require_i…

[AUDIT-2026-08-17-REMEDIATION] 2026-08-17 audit program CLOSED: BIMpossible remediation PRs merged, CI green, deployed
       unblocks 0 · M · bimpossible+workspace · VERIFIED 2026-08-31 · BIMpossible half of the 2026-08-17 audit remediation, all MERGED: #3…

[AUDIT-2026-08-24-REMEDIATION] 2026-08-24 audit remediation CLOSED: 4 PRs merged, deployed, CLAUDE.md rule added
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-24 · BIMpossible#467 MERGED -> 9ca63e5 (main 243fedc): shared_state boot …

[AUDIT-ESTATE56-CLOSURE-20260826] 2026-08-17 audit estate CLOSED 56->0: 2026-08-24/25/26 reconciliation across bimpossible+addins+workspace
       unblocks 0 · M · bimpossible+addins+workspace · VERIFIED 2026-08-31 · workspace 02_Reference/Audit and Scan Info/audit-closure-COMPLETE_20…

[FEAT-FAVORITES-HOME-V3] Per-user project/model favorites + Home v3 redesign SHIPPED (7-PR arc, deployed 2026-08-17)
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-17 · BIMpossible #392 (per-user pinned projects and models) -> #394 (wire…

[P15-15C-B-LIVE-READS] Session-bound live document reads (15c-B, old T1-T5), backend re-architecture pending
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-09-01 · BIMpossible_PHASE-STATUS.md, Phase 15 row 15c -- ledger's own wordin…

[SEC-PDP-G1-TEXTURE-BINDING] Design + test plan: authorized-model cdn_root acceptance for federated proxy textures (defect #5)
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-24 · BIMpossible#463 MERGED 2026-08-24 (squash) -> ac8ba6f on main. Imple…

[SEC-PDP-MODEL-INDEX-PAIRING] APS-verify the project<->item pairing recorded by _upsert_model_index / _record_model_version
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-31 · IMPLEMENTED + MERGED 2026-08-31T00:59:17Z (PR#507 -> 91822e70). Owne…

[WARM-ORIGIN-DOORGAP] Curtain-panel/unhosted doors have no origin: label them 'no location (curtain panel)' instead of deriving one
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-24 · 01_BuildLog/2026-08-04__doors-join-increment1_RESULTS.md, 'Follow-up…

[R5-AECDM-PUSHDOWN] R5 AECDM query-pushdown lane MERGED -- flag-gated, read-only (PR #363)
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-17 · BIMpossible #363 MERGED (d56bd14, 2026-08-16T19:47:59Z, branch feat/…

[SEC-DATAFLOW-HARDENING-SCOPE] Backend<->Autodesk data-flow analysis + data-hardening scope doc PUBLISHED (docs-only)
       unblocks 0 · M · bimpossible · VERIFIED date-unknown · 

[SEC-PDP-SLICE0] PDP Slice 0 no-migration containment bundle MERGED -- Redis blob encryption, conversation tenancy re-check, worker fail-closed on revoked grant, ElementCache hub-key pin
       unblocks 0 · M · bimpossible · VERIFIED date-unknown · BIMpossible#448

[CKA-PILLAR2-FIRM-DOCS] Client Knowledge Assistant Pillar 2: per-firm client documents (upload, extraction, BM25 retrieval, assistant tool)
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-13 · BIMpossible #327 (46520a7, merged 2026-08-08) -- Pillar 2 v1: per-fi…

[CKA-PILLAR3-EXPLAINABILITY] Client Knowledge Assistant Pillar 3: client explainability (change sets, help handoff, model-health remedies, alert next-steps, Groups read parity)
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-13 · BIMpossible #326 (686b064, merged 2026-08-08) -- Pillar 3: change se…

[P17-0-CONTROL-PLANE] Build Integration Control Plane foundation (17.0), gates 17c+ expansion
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-30 · BIMpossible#500

[P11-AC7-VERSIONED-SNAPSHOTS] Add versioned QA snapshots (Phase 11 AC7)
       unblocks 0 · L · bimpossible · VERIFIED 2026-08-24 · BIMpossible_PHASE-STATUS.md, Phase 11 -- AC7 (versioned QA snapshots…

## Next up

[EC-DOGFOOD-2] Continue Evidence Compiler dogfooding toward the next North Star review window
       unblocks 1 · M · evidence-compiler · VERIFIED 2026-08-24 · F:/Evidence Compiler/DOGFOOD_LOG.md

[OPS-AUDIT-UNATTENDED-ACCESS] Pre-grant Workspace + Add-Ins folder access to the scheduled weekly-audit session
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · 01_BuildLog/2026-08-31__weekly-full-audit-run.md step 1 + the report…

[TEST-PYTEST-COLLECTS-NOTHING] pytest collects ZERO tests in Claude-Profile/hooks/tests and Claude-Tools/ctxcheck - green means nothing ran
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · `python -m pytest` in F:/Claude-Tools/ctxcheck reports `no tests ran…

[ADDINS-SLOT-LEDGER] Runtime-slot handoff ledger is stale: deploys are landing without a ledger entry
       unblocks 0 · S · addins · VERIFIED 2026-08-23 · Add-Ins decision-log/2026-07-25__runtime-slot-handoff.md -- last mod…

[OPS-WORKTREE-DRIFT-REVIEW] Recurring per-repo drift review: workspace local behind-6/ahead-1 with dirty ledgers + untracked audit docs
       unblocks 0 · S · workspace+bimpossible · VERIFIED 2026-08-31 · 2026-08-07 (original): workspace carried 2 untracked docs (revitlink…

[ADMIN-DOMAIN-UNKNOWN-FIRM-404] Admin domain registration: return typed 404 for unknown firm instead of 409
       unblocks 0 · S · bimpossible · CLAIMED 2026-09-01 · Observed during BIMpossible#449 review: POST /admin/domains/{firm_id…

[EC-HYGIENE-1] Pull main checkout master to 345e1c7; delete merged lane branches (#1, #2 heads)
       unblocks 0 · S · evidence-compiler · VERIFIED 2026-08-24 · Live probe 2026-08-24: local master at 8bc555b, origin/master at 345…

[GITLEAKS-FIXTURE-MODEL-ROUTING-1A] Narrow gitleaks fixture/allowlist correction for synthetic key in backend/tests/test_assistant_model_routing.py:463 on feat/ai-model-routing-slice1a — owned by that branch's session (blocked Push-And-Verify from other branches 2026-09-02)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · Push-And-Verify on feat/cka-documents-placement-ui: gitleaks FAIL ru…

[OPS-ROLLBACK-RETENTION-20260817] Intentional retention: rollback-20260817 image tags until deploy soak completes 2026-08-18 evening
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-30 · deploy closed live at alembic c4e7a2b91d38, 2026-08-17 ~22:00 PDT

[ADDINS-HYGIENE] Add-Ins hygiene: finish Glass rollout (conformance-PR dedup DONE 2026-08-04)
       unblocks 0 · M · addins · VERIFIED 2026-08-23 · Add-Ins #10 MERGED 2026-08-04 (squash, main 94b21ab -- Plans 1+2 con…

[P7-REVITLINK-MULTIUSER] Scale RevitLink to multi-user (RE-1 defect now fixed; RE-2 capacity limit remains)
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-08-23 · Verification Checklist item RL_P0_10 (single-pipe/single-secret cons…

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

[FAM-PREEXISTING-RED] Families has 1 failing test and 13 ruff errors already on HEAD
       unblocks 0 · S · families · SUSPENDED 2026-08-31 · tool/tests/test_revitlink_pipe_adapter.py::test_handle_reports_missi…
       ⏸ dormant project (families) — probes suspended (non-executable); state unverifiable until whole-repo reassessment

[OPS-REDIS-P5] Flip WEB_CONCURRENCY>1 with redis leader-lock (Wave C-1 Phase 5)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · docker/REDIS-CUTOVER.md §Next -- confirmed exists on origin/main 202…

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

[HUB-TENANCY-GOLIVE] Seed firm->hub binding, migrate to HEAD via backend-migrate (never a hand-pinned revision), restart backend, run both tenancy smokes
       unblocks 2 · S · bimpossible · VERIFIED 2026-08-16 · BIMpossible #264 (90088f0), #265 (1fe6010), #266 (84c94c2), #267 (71…

[P3-12-TENANCY-REVISIT] Re-rule 3.12 tenancy row-isolation call for multi-firm project sharing
       unblocks 2 · S · bimpossible · VERIFIED 2026-08-20 · BIMpossible_PHASE-STATUS.md, Phase 3 row 3.12 -- RATIFIED 2026-08-18…

[SEC-ASSIST-FIRMVIEW] Merge #278 -- scope the assistant briefing's firm-view count to the caller's firm
       unblocks 2 · S · bimpossible · VERIFIED 2026-08-17 · BIMpossible #278 MERGED 2026-08-07T04:44:03Z, squash commit 5190a4a4…

[P13-T4-REFUSAL] Live-test Apply-Changes refusal paths -- non-cloud file, expired pane pairing
       unblocks 2 · S · bimpossible+addins · VERIFIED 2026-08-04 · addins main cfb4cc1 (T4 apply core); BIMpossible PR#229 b19674c + Ad…

[ADDINS-RESOLVE-HINT-PROJECT] RevitLink relay: send hint_project_id on GET /aps/model/resolve first resolves
       unblocks 2 · S · addins · VERIFIED 2026-08-30 · BIMpossible#496

[POST-268-FOLLOWUPS] Merge the three post-#268 follow-up PRs -- reviewed, three-lane green, awaiting checks
       unblocks 2 · S · bimpossible · VERIFIED 2026-08-18 · BIMpossible #269 (1887583), #270 (f6f0044), #271 (428889c) -- all ME…

[ADDINS-SYNC-TOKEN-HANDSHAKE] Build in-process sync-token handshake in RevitLink add-in so EventDispatcher can safely allow sync_with_central over the pipe
       unblocks 2 · M · addins+bimpossible · VERIFIED 2026-08-30 · SyncWithCentralCommand.cs header comment (2026-07-16/2026-07-27 audi…

[FE-3-10-FLAG] Phase 3.10 UI flag baked ON -- room-join/door columns LIVE in prod (PR#359 + rebuild + browser smoke)
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-16 · frontend/Dockerfile:34-35 on origin/main -- ARG NEXT_PUBLIC_BIMPOSSI…

[P3-10A-GOLIVE] Cross-Model Room Join LIVE -- rollout flag DELETED, path unconditional (PR#244)
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-06 · BIMpossible_PHASE-STATUS.md Phase 3 sub-phase notes, Phase 3.10a row

[OPS-BACKUP-RESTORE-DRILL] -VerifyRestore proven live (147/147 rows); RPO/RTO table + named restore operator still open
       unblocks 1 · S · bimpossible+workspace · VERIFIED 2026-08-17 · 01_BuildLog/2026-08-05__product-risk-assessment.md finding W4/W5 (or…

[OPS-RESIDENCY-SITE-DEPLOY] Deploy data-policy page to yourbimpossible.com -- DEPLOYED + VERIFIED LIVE 2026-08-27
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-23 · F:\BIMpossible-Site\site\dist\data-policy\index.html -- astro build …

[OPS-RESIDENCY-DOC] Data residency/retention policy PUBLISHED -- /data-policy page live, bs-5 closed
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible_ProgramPlan_2026-05-25.md, Commercial Launch Prerequisit…

[OPS-TENANCY-DOC] Write the multi-tenant data-isolation strategy doc (audit's required TEST already shipped in PR#243)
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-17 · BIMpossible_ProgramPlan_2026-05-25.md, Commercial Launch Prerequisit…

[P7-SYNC-GOLIVE] Supervised owner flag-flip: go-live Revit Link sync re-enable (Phase 7 step 2)
       unblocks 1 · S · bimpossible+addins · VERIFIED 2026-08-23 · CUTOVER PASS 2026-08-25 -- LIVE and verified, stays on (unlike pilot…

[ARCH-FIRM-ALIAS-BACKEND] Firm-alias layer SHIPPED -- BIMpossible firm-literal baseline now ZERO (126 -> 21 -> 0), Add-Ins 29 -> 5
       unblocks 1 · S · bimpossible+addins · VERIFIED 2026-08-30 · BIMpossible #257 (85c3fff, MERGED 2026-08-05T23:43:21Z) -- backend/a…

[OPS-ADMIN-HOST-SPLIT] Option C admin-hostname split live: founder surface on admin.yourbimpossible.com only
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-16 · BIMpossible #367 MERGED (736b2d6, 2026-08-16) -- Option C middleware…

[P3-8-SLICE23] Phase 3.8 slice 3 (ACC role sync) LIVE dark (deployed, flag OFF by design); slice-2 ruling resolved
       unblocks 1 · S · bimpossible · VERIFIED 2026-08-31 · BIMpossible #275 MERGED 2026-08-17 (owner ruling: merge tonight, dar…

[ADMIN-DOMAIN-AUDIT-INACTIVE-FIRM-GUARD] Audit admin domain registration and block auto-link bootstrap against inactive firms
       unblocks 1 · S · bimpossible · VERIFIED 2026-09-01 · BIMpossible#449 DRAFT opened 2026-08-22 (fix/domain-audit-firm-guard…

[P3-8-SLICE2-DRAFT-GATING] Build slice-2 draft reader gating: owner-only visibility for is_draft memberships (owner ruling 2026-08-27)
       unblocks 1 · M · bimpossible · VERIFIED 2026-08-31 · MERGED 2026-08-30T23:12:46Z (owner-authorized squash merge): BIMposs…

[WRITE-ENGINE-INC1] Write Engine Increment-1 -- SHIPPED: Task 8 smoke passed, #232 + AddIns #49 merged lockstep
       unblocks 1 · L · bimpossible+addins · VERIFIED 2026-08-04 · 00_Strategy/design-docs/2026-07-26__write-engine-increment1_typed-va…

[ENROLL-TENANCY-LAYER] Client/project enrollment tenancy layer (E1-E5) — enforcement LIVE (flag ON)
       unblocks 1 · L · bimpossible · VERIFIED 2026-08-17 · BIMpossible #333 MERGED (squash 593a4fb) 2026-08-14T23:33:38Z -- cli…

[P6-CLIENTMGMT-F] Build cross-firm project sharing (Client-Mgmt F), gated on 3.12
       unblocks 1 · L · bimpossible · VERIFIED 2026-08-30 · BIMpossible_PHASE-STATUS.md, Phase 6 row Client-Mgmt F -- PLACED not…

[DOC-PHASESTATUS-191] PHASE-STATUS.md Phase 7 row already corrected -- sole #191 reference reads 'MERGED 2026-07-23'; no stale 'open' wording remains
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · BIMpossible #191 'Phase 7 Gate G2: SSA cloud-open spike (hand-run)' …

[P3-DUCTS-PIPES-DECISION] Decide ducts/pipes parameter-write scope for Phase 3 write-back
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-20 · BIMpossible_PHASE-STATUS.md, Phase 3.10b sub-note -- DECIDED 2026-08…

[BIMP-RELAY-ERROR-MAP-GAP] Backend _RELAY_ERROR_MAP lacks relay codes TIMEOUT / PIPE_BUSY / METHOD_NOT_ALLOWED -- they collapse to opaque 500s instead of typed 4xx/503 responses
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · Observed 2026-08-25 during P7-RELAY-SESSION-LIFECYCLE discovery: bac…

[NL-FILTER-EVAL-QUALITY] NL-filter intent-fidelity eval harness built and RUNNING WEEKLY IN CI with a live key
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-27 · BIMpossible #375 MERGED (989a2fb, 23:25Z) -- implements the BUILD NO…

[OD-DECISIONS] Decide OD3 (fire-alarm schedule owner) and OD4 (OSS reuse triage)
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-18 · 02_Reference/Audit and Scan Info/BIMpossible_Verification_Checklist.…

[P7-SYNC-COMMENT-CRYPTO-BINDING] Sync comment crypto-binding: CLOSED BY OWNER RULING -- comment is non-authoritative collaboration metadata, no special binding required
       unblocks 0 · S · bimpossible+addins · VERIFIED 2026-08-27 · Today the token binds firm/user/document_title only (backend/revit_l…

[WRITE-ENGINE-SHIPVEHICLE] Write Engine ship vehicle DECIDED: Phase 13 sub-increment (platform track reserved for later)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible_PHASE-STATUS.md row 13.1 (placed 2026-08-04 AM): 'ships …

[SEC-ASSIST-TOOLS-PERSONAL-VIEWS] FIXED+MERGED: assistant _visible_saved_view_clause personal branch now pins firm_id (PR #416)
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · backend/aec/assistant_tools.py:295-309 _visible_saved_view_clause: f…

[SEC-GROUPS-DELIVERABLE-FIRM] Cross-firm NamedDeliverable IDOR in groups.py category derivation -- fixed and merged
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · backend/aec/groups.py:195-231 (_validate_members_and_compute_categor…

[SEC-GROUPS-PERSONAL-LISTING] list_groups personal-group cross-firm leak -- CONFIRMED and LANDED via PR #290 (independent parallel session won the race; see verification.by)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · backend/aec/groups.py:318-329 (list_groups, personal query) filtered…

[SEC-VIEWS-PERSONAL-LISTING] list_views' personal-views query has the same missing-firm_id gap as the fixed list_groups bug
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · backend/aec/views.py:207-218 (list_views, GET /data/views) -- person…

[BUG-GITLEAKS-HITS-COLLAPSE] Invoke-GitleaksScan collapses the whole findings array into one hit under PowerShell 5.1 - every multi-finding scan prints one System.Object[] line and HITS: 1
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · Observed 2026-08-31 while running the helper by hand before the main…

[HYG-20260831-WORKSPACE-DOCS] Workspace docs-hygiene fixes (HYG-1/2/3) sit on an unpushed local branch with no PR
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · 3de8211 'fix(ci): gate docs-hygiene at PR time, not a week downstrea…

[RE-WIZ-POLL-2] Fix wizard provisioning poll: retry transient HTTP errors like its sibling loop does
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible PR#239 (68bb596, merged 2026-08-04) -- _await_project_ac…

[SEC-20260831-TEMP-CLONE-TOKEN-EXPOSURE] OWNER ATTENTION: live GitHub temp_clone_token committed to Workspace evidence JSON, redacted-in-tree only -- rotation/history-scrub decision needed
       unblocks 0 · S · workspace · VERIFIED 2026-09-01 · Workspace commit ecd6072 (2026-08-31, "security: redact live temp_cl…

[SEC-ASSIST-PERSONAL-VIEWCOUNT] Assistant briefing's personal_views count is the unfixed half of the SEC-ASSIST-FIRMVIEW function
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · backend/aec/assistant_context.py:172-178 (_assemble_project_context)…

[SEC-BRACE-2] Bump brace-expansion override to 5.0.9 -- new HIGH GHSA-rgw5-rvv9-x895
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · gh api dependabot/alerts 2026-08-04: alert #3 OPEN HIGH, brace-expan…

[WSR-SECSCAN-LAUNCHGUARD] Run-Security-Scan.ps1 reports a stale report as a fresh one when a scanner fails to launch
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · F:/BIMpossible-Workspace/system/Run-Security-Scan.ps1 - four sequent…

[ADDINS-JTI-REPLAY-PERSIST] Persist (or TTL-bound) the add-in's process-local syncAuth jti replay cache so an add-in restart inside the 600s attestation TTL cannot re-enable a consumed attestation
       unblocks 0 · S · addins+bimpossible · VERIFIED 2026-08-31 · BIMpossible decision-log/2026-08-21__p7-hardening-followons-queued.m…

[APS-TOKEN-REFRESH-CLASSIFY] Classify APS/auth token-refresh failures instead of leaking 500s (_authed_get, remaining paths, AEC worker)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · BIMpossible #334 (e0577ad) -- token-refresh failures in _authed_get …

[AUTHZ-AUDIT-POISON-BATCH-FLOOD] authz shadow-audit poison row (firm_id='', principal 'service', reason 'wizard.account_read') fails UUID cast and re-queues the whole ~500-row batch every ~2s, flooding backend logs
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · aec/authz/audit.py flush_pending -- batch insert fails with psycopg2…

[DATA-EMPTY-PERSIST-GUARD] Never persist empty categories/property/spec data version-immutably
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible #362 MERGED (0b314d8, 2026-08-16) -- never persist an em…

[DEP-TRIAGE-2026-08] Dependabot triage: CLOSED BY OWNER RULING 2026-08-21 -- all 6 held PRs closed under the dependency-update policy
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-18 · STILL OPEN as of 2026-08-17 (gh pr view, live): github-actions -- #3…

[OPS-DEPLOY-STACK-REFRESH-20260817] Deploy tonight's merged main to the local stack -- images/DB stale vs main 130ba49
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-17 · BIMpossible#415 #416 #417 #418 #419 (+#273 #275) all MERGED; main ti…

[P8-APS-PUBLISHING-CAP] APS app publishing/production-review cap -- SETTLED: no cap blocks launch
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-25 · Owner confirmed 2026-08-25 (has been working the APS console directl…

[PUSH-SELFCHECK-BOOTSTRAP] Push-And-Verify self-check bootstrap: committed outgoing self-edits pass without -SkipSelfCheck
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · workspace 44ccf8d -- ancestor-aware stale-copy guard: on blob mismat…

[RAIL-RETIRE-FINAL] ALLOWED_PROJECT_IDS / guard.py allowlist subsystem retired end-to-end (PRs #371, #374)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · BIMpossible #371 MERGED (9b851ff, 2026-08-16T20:24:50Z) -- migrates …

[SEC-DEP-EXEC] Dependabot PR triage EXECUTED: closed 201+235, parked 200, merged 179/180/237 (redis smoked); 139 auto-merging
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-07 · 00_Strategy/2026-08-04__ProductionQueue_Session_Findings.md §2 -- pe…

[SEC-DEPENDABOT-CI] Decide the CI Actions merge policy (unreviewed third-party Action can merge to main)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-04 · BIMpossible PR#242 MERGED f8b022f 2026-08-04 -- github_actions ecosy…

[SEC-GROUPS-PERSONAL-INDEX-FIRMID] uix_named_deliverables_personal_name_group unique index omits firm_id -- confirmed write-path only, not data corruption
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · Source: named-deliverable-personal-scope-firm-gaps.md finding #4, pr…

[SEC-VIEWS-PERSONAL-INDEX-FIRMID] uix_saved_views_personal_name (personal views/leaves unique index) omits firm_id -- same reassigned-user 409 dead-end as the groups sibling
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · CONFIRMED by direct read 2026-08-07 while fixing SEC-GROUPS-PERSONAL…

[SHARE-V2-CELL-FREEZE] Share v2 snapshots freeze display-formatted cell values, not raw metric values (SHARE-V2-DEF-1)
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · BIMpossible #336 (22b6f4e, merged 2026-08-08) -- SHARE-V2-DEF-1: the…

[TAILWIND-V4-VERIFY] Verify Tailwind v4 migration (#284) live in prod -- Docker image is baked, merge alone doesn't ship it
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-18 · BIMpossible #284 (89f1222, merged 2026-08-07T04:51:18Z) -- replaces …

[TENANCY-PROBE-281] Tenancy invariant now covers flag-gated routers; /probe hub isolation fixed, 41 routes triaged
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · BIMpossible #281 MERGED 2026-08-07T02:48:19Z, squash commit 36412c9c…

[TENANCY-RAIL-SEARCH-RESOLVE] /search/models + /aps/model/resolve migrated off the ALLOWED_PROJECT_IDS rail
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible #366 MERGED (e585862, 2026-08-16) -- migrates /search/mo…

[ADDINS-BRANCH-PROTECT] Protect Add-Ins main: require PRs + firm-literals/test/gitleaks checks, strict up-to-date
       unblocks 0 · S · addins · VERIFIED 2026-08-08 · Applied 2026-08-08 via gh api PUT repos/YourBIMpossible/BIMpossible-…

[ADDINS-DEP-SCAN] Add deterministic NuGet dependency-vulnerability check to Add-Ins CI, gate it, add its check name to branch protection
       unblocks 0 · S · addins · VERIFIED 2026-08-08 · Verified 2026-08-08: Add-Ins security-scan.yml is a single gitleaks …

[ADDINS-NOT-SUPPORTED-PIPE-PROPAGATION] Propagate the typed NOT_SUPPORTED classification through PipeServer.cs so the add-in answers unsupported pipe methods with the typed code instead of a generic error
       unblocks 0 · S · addins+bimpossible · VERIFIED 2026-09-02 · Deferred from P7 hardening pass 2026-08-21 (BIMpossible#440 typed NO…

[ADDINS-PANE-PR45] Land Add-Ins PR#45 -- Assistant pane header dock fix (branch checked out locally)
       unblocks 0 · S · addins · VERIFIED 2026-08-06 · Add-Ins PR#45 'fix(revitlink): dock Assistant pane header to Top, co…

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

[CI-DRAFT-GATING] CI cost/draft-gating live: drafts skip expensive CI, superseded runs cancel, auto-draft-on-red reverted
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-13 · BIMpossible #342 (4956b45) -- expensive CI + security scans skip on …

[DASH-BIMWATCH-WIRING] Wire bimwatch pipeline output into the live dashboard (index.html/data.js have zero references)
       unblocks 0 · S · dashboard · VERIFIED 2026-08-31 · 2026-08-07 session: grepped index.html and data.js in both Dashboard…

[DOC-DOCINDEX-DEFECTS-24] docindex: code root drops silently in a worktree; sub-chunk line attribution duplicates results
       unblocks 0 · S · workspace · VERIFIED 2026-08-07 · tools/docindex/docindex.config.json:34 -- code root path '../BIMposs…

[DOC-GITLEAKS-INDETERMINATE-RECORD] gitleaks 'Indeterminate' status shipped with no decision record; a wiki page is the only synthesis that describes it
       unblocks 0 · S · workspace · VERIFIED 2026-08-31 · 9d1472d 'fix(push): never present an unverified gitleaks exit 1 as l…

[DOC-LEDGER-HYGIENE] Retire stale NEXT.md: superseded banner applied, commit pending
       unblocks 0 · S · bimpossible+workspace · VERIFIED 2026-08-06 · 00_Strategy/NEXT.md header, read 2026-07-26: 'Updated 2026-07-10', p…

[DOCS-DELIVERY-PHASE-SCORE-DOD] Delivery contract -- phase-score ledger update is part of definition-of-done
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · MERGED PR#508 (2026-08-31T01:23:13Z) -- docs(delivery): phase-score …

[NL-FILTER-EVAL-CRON-CONFIRM] Confirm the nl-filter-eval weekly schedule trigger actually fires (not just workflow_dispatch) -- CONFIRMED 2026-08-24
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-27 · BIMpossible#445 (dfe2a53) fixed DATABASE_URL provisioning; manual wo…

[OPS-CACHE-RECONCILE-V1] Quarantine-first cache-reconciliation worker, report-only v1
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-02 · BIMpossible #364 MERGED (ed6ad70, 2026-08-16) -- cache reconciliatio…

[OPS-CF-RECORD-CONSOLIDATION] Option C session ended: both CF Access docs committed to main; Access-memory fold is the residual
       unblocks 0 · S · workspace · VERIFIED 2026-08-17 · Two untracked docs in the workspace main tree (2026-08-16): 00_Strat…

[OPS-CLOSEOUT-WANDER-20260817] Closeout wander triage: stale CLAUDE.md backend-mount note; REVIT_LINK_SYNC env=1 confirm; leaked bk-localci pairs
       unblocks 0 · S · bimpossible · CLAIMED 2026-08-17 · observed 2026-08-17 closeout session 67df33a5

[OPS-P7-CLOSEOUT-DOCS-PR529] Merge BIMpossible#529: land the 3 P7 relay closeout docs missing from main
       unblocks 0 · S · bimpossible · VERIFIED 2026-09-01 · BIMpossible#529 OPEN, READY (not draft), head 21766e6a, opened 2026-…

[OPS-SLOPAUDIT-UNPUSHED] 8 slop-audit remediation commits are local-only across 5 repos - push or discard
       unblocks 0 · S · workspace+dashboard+families · PARTIAL 2026-08-31 · F:/AI-Dev/slop-audit-remediation_2026-08-31.md section 5 (full commi…
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

[ROUTER-SUPPORT-INDEX-KEY-MISMATCH] RESOLVED by PR #485: support fast-path now keys ModelIndex on the file_urn COLUMN (not item_id); regression tests pin item_id != file_urn
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-31 · Found by Explore agent during P11 QA-history follow-ups session 2026…

[SEC-GROUPS-VIEWS-404-EXISTENCE-ORACLE] PATCH/DELETE groups+views: nonexistent id returns 404 but cross-firm id returns 403 -- status-code existence oracle
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · Surfaced by the backend-endpoint-reviewer gate during SEC-GROUPS-403…

[TEST-OPS-HYGIENE] Test/ops hygiene: app-boot tripwire, post-deploy identity smoke script, flaky prefs test fixed
       unblocks 0 · S · bimpossible · VERIFIED 2026-08-17 · BIMpossible #339 (e516a0d) -- app-boot smoke tripwire that fails CI …

[WAVESTATUS-CHECK-DEPLOY] Wave-Status PR-body-check MERGED live in BIMpossible + AddIns (advisory-only)
       unblocks 0 · S · bimpossible+addins · VERIFIED 2026-08-31 · BIMpossible #494 'ci: add advisory Wave-Status PR-body check' -- MER…

[WS-NEXT-VERSIONING] Version /next skill + store + session docs into workspace repo (branch + draft PR)
       unblocks 0 · S · workspace · VERIFIED 2026-08-07 · 2026-08-04__ProductionQueue_Session_Findings.md §3 -- cloud session …

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

[SEC-GROUPS-VIEWS-HUB-ISOLATION] groups.py + views.py routes check only the global project allowlist, never per-firm hub isolation
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-17 · Source: parallel session's memory record named-deliverable-personal-…

[SEC-WORKSPACE-GITLEAKS-EVIDENCE-HITS] Workspace gitleaks scan is NOT clean: 18 findings in three migration-evidence artifacts already published on origin - needs triage or an allowlist decision
       unblocks 0 · M · workspace · VERIFIED 2026-08-31 · gitleaks --source . on F:/BIMpossible-Workspace, 2026-08-31: 18 find…

[CKA-PILLAR1-HELP-CORPUS] Client Knowledge Assistant Pillar 1: BM25 help ranker + how-to corpus, waves 1-4 shipped
       unblocks 0 · M · bimpossible+workspace · VERIFIED 2026-08-17 · BIMpossible #320 (f8791ec) -- ports the docindex BM25 ranker into ba…

[WIZARD-NEWPROJECT-SETUP] New-Project-Setup wizard hardened -- keep-alive-safe provision (#387) + approved fixes wave (#388: combobox, address/client, dup-number advisory, schedule/value/timezone, Option A session-cached consent)
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-17 · BIMpossible #387 (squash b12ef36, merged 2026-08-17) -- fix(wizard):…

[ADDINS-TDD-CENSUS] Measure Add-Ins logic in the /tdd-excluded Revit-API-bound glue zone vs extracted tested cores
       unblocks 0 · M · addins · VERIFIED 2026-08-08 · Anti-slop coverage plan sec.3: /tdd explicitly excludes Revit-API-bo…

[P15-15B-EXTERNAL-DOC-INGEST] Firm-document retrieval in the Revit Assistant Pane (15b)
       unblocks 0 · M · bimpossible+addins · VERIFIED 2026-09-01 · BOTH HALVES MERGED 2026-08-31T04:22Z -- AddIns #113 (squash d09204e,…

[P3-10B-DOORS] Doors room-pair slice LIVE on main -- Increment 1 merged (PR#253); direction is Increment 2
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-06 · BIMpossible PR#253 'feat(3.10b): doors resolve to the room PAIR they…

[P3-6-SPATIAL] Build Phase 3.6 Spatial Relationship Engine v1 (architecturally unblocked)
       unblocks 0 · M · bimpossible · VERIFIED 2026-09-02 · BIMpossible_PHASE-STATUS.md Phase 3 sub-phase notes, Phase 3.6 row

[SLOP-AUDIT-SKILL] Repo-agnostic on-demand slop-audit skill: silent-catch census, counter-integrity, tested-but-dead
       unblocks 0 · M · claude-profile+workspace · VERIFIED 2026-08-08 · Anti-slop coverage plan sec.2: PC-Monitor, Finance-Dashboard, Presea…

[WSCLOSEOUT-20260831-RECORDS] 2026-08-31 workspace closeout: review, authz, weekly-audit, PHASE-STATUS and slop-audit records published
       unblocks 0 · M · workspace · VERIFIED 2026-08-31 · One coherent publication wave, all ancestors of origin/main 1360a66:…

[SEC-APSISO-TESTS-ENROLLMENT-EXPLICIT] Make /aps + /data hub-isolation test suites enrollment-explicit (no flag-lane dependence)
       unblocks 0 · M · bimpossible · VERIFIED 2026-08-17 · BIMpossible #390 (e9a424e, merged 2026-08-17) -- enrollment-explicit…

[EC-HOOKSAFE-1] Python-native hook-safe launcher shipped to EC core; Node wrapper migrated out of BIMpossible/AddIns/Workspace/Families
       unblocks 0 · L · evidence-compiler+bimpossible+addins+workspace+families · PARTIAL 2026-08-24 · evidence-compiler#5
       ⏸ dormant leg (families) suspended — evidence-compiler+bimpossible+addins+workspace leg tracked live; dormant leg unverifiable until whole-repo reassessment, so the item is not fully verified
