# P7 remote SyncWithCentral — close-out — 2026-08-21

## 1. Pilot result — **PASS**

| | |
|---|---|
| Test document | `TEST-Stanford_ES3_Lab_S&L_R26.rvt` (Revit `Document.Title` form without extension in the add-in/relay log) |
| One valid sync | `POST /revit/sync_with_central_confirmed` → 200; relay id `14cdee9b`; `revit_link_request_log` id 25, status `ok`, 8445 ms; Revit SWC completed |
| One replay rejection | Same token replayed → typed 403 `"Token has already been used (single-use)."`; no relay call, no second execution |
| Audit evidence | Row 25 readable post-deploy (ok, `error_code` NULL, `firm_id` NULL); the replay left no row at pilot time — that gap is what #443 closed (future replays write `status='rejected'`, `error_code='SYNC_TOKEN_ALREADY_USED'`) |
| Token leakage | 0 hits for token / HMAC material across backend log, relay log, add-in log, audit rows |
| Record | `F:/AI-Dev/BIMpossible/docs/decision-log/2026-08-21__p7-sync-golive-supervised-pilot.md` |

## 2. Code and merges

| Item | SHA |
|---|---|
| #442 pilot record (docs-only) | `59df132` |
| #443 rejection audit + `firm_id` | `d6368c8` |
| Prerequisite hardening #440 | `02bd9b6` |
| Prerequisite hardening #441 | `d77319a` |
| syncAuth handshake (BIMpossible #433) | `10392e74` |
| Add-Ins handshake #78 | `91a40465` |
| Add-Ins typed NOT_SUPPORTED #81 | `e98f90e` |

## 3. Deployment

| | |
|---|---|
| Migration | `d5f8b3c41e27` (`revit_link_request_log.firm_id` nullable UUID + `ix_revit_link_request_log_firm_created`) — `backend-migrate` ran `c4e7a2b91d38 -> d5f8b3c41e27`; `alembic current` = `d5f8b3c41e27 (head)` |
| Restart / health | `docker compose up -d` from `docker/`; backend, frontend, db, redis healthy; `/health` 200; frontend 200 |
| Schema | `information_schema` confirms column uuid nullable + 5 indexes incl. `firm_created`; 25 existing rows readable |
| Codes | `SYNC_TOKEN_*` codes importable in the container; `SYNC_REJECTED_STATUS == "rejected"` |
| Tests | local 210 passed / 7 skipped; Verify-Local-CI GREEN; remote `backend / pytest`, semgrep, `security-scan-summary`, gitleaks pass |
| **Runtime flag** | **OFF.** `docker-backend-1` (recreated 17:28 PDT by the #443 deploy) holds `BIMPOSSIBLE_REVIT_LINK_SYNC_ENABLED=OFF`; `feature_flag.py` accepts only `1/true/yes`, effective = False (checked in-container). Was truthy at pilot time (16:39 PDT — the sync could not have run otherwise) and was set to `OFF` in `.env` before the redeploy. Earlier close-out text claimed "=1 still effective" — that came from `grep -c` counting the line, not reading its value; corrected. No owner action needed. |

## 4. Teardown

| | |
|---|---|
| DLL | Pipe-off build restored at `%APPDATA%\Autodesk\Revit\Addins\2026\BIMpossible.RevitLink.dll` (2,616,832 B, sha256 `4fec8329…`), done with Revit closed; pipe-enabled build kept aside as `.pipeon-20260821` (not installed) |
| Relay | Stopped; `:7779` not listening |
| Revit | No `Revit.exe` process |
| Browser | No pilot tab (no tab group for this session) |
| Overrides | No test override remains |

## 5. Queue and repository state

- `P7-SYNC-GOLIVE` — `landed` / `verified`; close-out evidence (merge SHAs, teardown, flag state) attached.
- `P7-SYNC-REJECTION-AUDIT` — `landed` / `verified` (migration, deploy, tests recorded).
- Deferred follow-ons, each its own queue entry: `ADDINS-NOT-SUPPORTED-PIPE-PROPAGATION` (ready), `AUTHZ-AUDIT-FIRMID-EMPTY-ROOTCAUSE` (ready), `ADDINS-JTI-REPLAY-CROSS-PROCESS` (owner-gated, distinct from `ADDINS-JTI-REPLAY-PERSIST`), `P7-SYNC-COMMENT-CRYPTO-BINDING` (owner-gated), `ADDINS-DPAPI-PREWARM` (owner-gated).
- BIMpossible: `main` clean at `d6368c8` == `origin/main`. Pruned: local `claude/p7-golive-record`, `claude/p7-sync-rejection-audit`, worktree `.claude/worktrees/p7-sync-rejection-audit`; remote P7 branches already auto-deleted on merge (0 `p7` heads on origin).
- Add-Ins: local `main` fast-forwarded to `2d66683` == `origin/main`; worktree `.claude/worktrees/p7-golive-pipe-build` removed (no commits). Main checkout sits on `feat/batch-rename-phase1` with 1 dirty file — not this session's work, left untouched.
- Retained (not mine, observation only): BIMpossible worktrees `design-knowledge-reconciliation-0821`, `phase-5-sheets-planning-b15415`, `site-ui-design-notes-56e276` (all clean); Add-Ins worktrees `design-knowledge-reconciliation-0821`, `exciting-bassi-a29ace`, `sheet-placement-formatting-838ca2`, `.claude-review-pr78`.
- State store (`F:/AI-Dev/.tools/state`): committed this close-out's `queue.yaml`, `QUEUE.md`, and the two 2026-08-21 reports. **No remote is configured on that repo, so nothing was pushed.**

P7 remote SyncWithCentral pilot and immediate audit hardening are fully closed. Remote sync is deployed-capable but runtime-disabled by default. No active P7 operational work remains. The roadmap is ready for an owner-selected next move.
