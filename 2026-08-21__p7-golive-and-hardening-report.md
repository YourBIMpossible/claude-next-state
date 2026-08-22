# P7 go-live + hardening/roadmap report — 2026-08-21

## 1. P7-SYNC-GOLIVE — **PASS**

| | |
|---|---|
| Result | Exactly one authorized remote SyncWithCentral end-to-end; one replay → typed 403; no second sync; no token material in any log or audit row |
| Revisions | Backend `b33fa9b` (bind-mounted main); Add-in DLL from Add-Ins main `ae464ec` (pipe-enabled build, sha256 `b43bd4aa…`); relay `revit-relay/relay.py` @ b33fa9b |
| Evidence | `F:\AI-Dev\BIMpossible\docs\decision-log\2026-08-21__p7-sync-golive-supervised-pilot.md` (full timeline); `revit-relay/relay.log` 16:39–16:40 PDT; `revit_link_request_log` row id=25 (ok, 8445 ms); replay 403 `"Token has already been used (single-use)."` with no relay call and no audit row |
| Flag final state | `BIMPOSSIBLE_REVIT_LINK_SYNC_ENABLED=1` **still set in `docker-backend-1`** — lives in `.env` (human-only). Owner must unset + restart backend. Repo default remains OFF; no release-policy change. |
| Relay / Chrome | Relay process stopped; pilot browser tab closed |
| Queue | `P7-SYNC-GOLIVE` → `landed`, verification `verified` (evidence above) |
| Record | Decision log + `INDEX.md` → [#442](https://github.com/YourBIMpossible/BIMpossible/pull/442) (draft, `b4ef5a9`, docs-only) |

## 2. Hardening — shipped earlier this session (merged)

| PR | What |
|---|---|
| [#440](https://github.com/YourBIMpossible/BIMpossible/pull/440) `02bd9b6` | authz audit-poison quarantine, typed NOT_SUPPORTED mapping, non-JSON error bodies |
| [#441](https://github.com/YourBIMpossible/BIMpossible/pull/441) `d77319a` | remaining hardening items + follow-on decision log (`decision-log/2026-08-21__p7-hardening-followons-queued.md`) |
| Add-Ins [#81](https://github.com/YourBIMpossible/BIMpossible-AddIns/pull/81) | add-in side typed error propagation |

## 3. Next code-only item — built this session

**[#443](https://github.com/YourBIMpossible/BIMpossible/pull/443)** (draft, `1db29c9`, branch `claude/p7-sync-rejection-audit`) — P7-SYNC-REJECTION-AUDIT
- `SyncTokenError` family → typed `.code` (`SYNC_TOKEN_ALREADY_USED`, `_EXPIRED`, `_SCOPE_MISMATCH`, `_BAD_SIGNATURE`, `_MALFORMED`, `_SECRET_MISSING`)
- Router audits rejections as `status="rejected"` rows after every gate; never the token; degrade-don't-block
- `revit_link_request_log.firm_id` (nullable UUID, migration `d5f8b3c41e27`, idempotent/reversible, ORM index declared); `_coerce_firm_id` → NULL on garbage
- Tests: 5 new (replay audited + no second execute + token absent; audit failure keeps 403; secret-missing code; DB-lane firm_id persist + `''`→NULL; coerce unit)
- Gates: `backend-endpoint-reviewer` PASS, `migration-reviewer` PASS (drift finding fixed in-PR)
- `.\Verify-Local-CI.ps1 -BaseRef origin/main` → **LOCAL CI GREEN**
- Deploy: carries a migration → full-stack deploy (`docker compose up -d --build` from `docker/`), not a frontend refresh
- Queue: `P7-SYNC-REJECTION-AUDIT` → `in_flight` with PR ref

## 4. Merge order
1. #442 (docs only) — any time
2. #443 — after CI green; deploy with migrate
3. Nothing else pending from this session

## 5. Roadmap re-rank (post go-live)
Ready code-only, in order: **P7-SYNC-REJECTION-AUDIT (in flight #443)** → P7-REVITLINK-MULTIUSER (M) → P15-15B (M) → P11-AC7 (M).
Owner-gated / blocked: P15-15D-MODEL-WRITES (risk 3, L — now unblocked by the pilot, needs go), INC3 (no scope), P13-T5 (← P6-CLIENTMGMT-F), P15-15C (hub cutover gate), P5-7 (owner spikes).

## 6. Decision card — owner-only, one pass

| # | Decision | Default if silent |
|---|---|---|
| 1 | Unset `BIMPOSSIBLE_REVIT_LINK_SYNC_ENABLED` in `.env`, restart backend, confirm `docker exec docker-backend-1 env \| grep SYNC_ENABLED` is empty | **Must do** — flag is currently ON |
| 2 | Restore pipe-off DLL: with Revit 2026 closed, replace `%APPDATA%\Autodesk\Revit\Addins\2026\BIMpossible.RevitLink.dll` with `…dll.pipeoff-20260821` | Must do before next Revit session |
| 3 | Merge #442 then #443 | Merge both |
| 4 | P15-15D-MODEL-WRITES go/no-go (risk 3, L) — pilot removed its blocker | Stay parked; next code item is P7-REVITLINK-MULTIUSER |
| 5 | INC3 — define scope or retire | Retire if no scope by next sync |
| 6 | AUTHZ-AUDIT-ROW-SIGNING — HMAC scheme choice (server-key vs per-firm) | Server-key, rotate via env |
| 7 | ADDINS-JTI-REPLAY-PERSIST — persist JTI cache vs keep process-local TTL 600 s | Keep TTL; persist only if multi-process add-in host appears |
| 8 | P13-T5 waits on P6-CLIENTMGMT-F — schedule F? | Not before hosting migration |
| 9 | P15-15C hub cutover date | No date → stays blocked |
| 10 | P5-7 spikes — which first | None until 4–9 settle |

## 7. Assumed
- Pilot drove the modal's exact two-call sequence from the app origin under the owner's session (web button hidden by `SHOW_LEGACY_REVIT_SYNC=false`); recorded in the decision log as the accepted alternative.
- Flag was already ON at session start (expected OFF) — noted, not changed.

## 8. Left-Flags
- `revit_link_request_log.firm_id` has no reader yet; any future per-firm read must filter fail-closed on NULL + `require_active_membership` (migration-reviewer note).
- Add-in does not log sync acceptance to `log.txt`; add-in evidence = relay ok + Revit result.
