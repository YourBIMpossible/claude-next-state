# Evidence ledger (owner-adopted 2026-08-08)

Every observed friction event gets ONE structured entry below, using this format.
This is the sensor: no watcher, daemon, hook, dashboard, or new runtime tool —
structured entries + thresholds decide whether a frustration earns a build.

```
- Date:
- Signal: retrieval-miss | docs-drift | permission-block | context-overflow | repeated-manual-step
- Exact task / query:
- What existing tool was tried:
- Result and cost:
- Repeat count:
- Candidate response:
- Threshold to build:
```

Build thresholds (explicit — do not build below them):
- **ctxdex / ctxpack:** same retrieval/context-assembly miss ×3, each with a concrete artifact that should have been found.
- **ctxcheck:** same drift category in 2 projects, or recurring after a prior repair.
- **Permission rule:** `gh pr view` blocked in 3 separate sessions AND the installed engine proven to enforce parsed executable + constrained argv rules (see claude-profile notes/2026-08-07-permission-allowlist-proposal.md).
- **MCP:** a CLI interaction requires repeated structured copy/paste or argument reconstruction across clients.
- **Embeddings / vector retrieval:** FTS + metadata filtering fails on recorded real queries — never hypothetical semantic-search scenarios.

# Ledger entries

```
- Date: 2026-08-07
- Signal: permission-block
- Exact task / query: `gh pr view 5` during ctxdex PR review (read-only, blocked by auto-mode classifier)
- What existing tool was tried: Bash gh; workaround was git log / web
- Result and cost: one approval round-trip; ~1 min + flow break
- Repeat count: 1 session
- Candidate response: single parsed-argv allow rule for `gh pr view` only
- Threshold to build: blocked in 3 separate sessions + engine proven to enforce parsed argv rules
```

# Queue

- ~~2026-08-07 (ctxdex closeout): auto-mode classifier blocks benign/read-only Bash~~ RESOLVED as proposal-only 2026-08-07: audit record at claude-profile `notes/2026-08-07-permission-allowlist-proposal.md` — deferred by owner ruling, no settings change; revisit only if block frequency grows.
- ~~2026-08-07 (substrate review): BUILD ctxcheck~~ DONE 2026-08-07: built at F:\AI-Dev\.tools\ctxcheck (commit 7951f87, 42/42 tests); live runs clean on claude-profile, BIMpossible 4 doc-rot WARNs (ARCHITECTURE.md `aec/` ×2 + 02_Reference path; CI-GATES.md 00_Strategy path) — prose fixes belong to a BIMpossible session, not here.
- ~~2026-08-07 (deploy gap)~~ DONE 2026-08-07 release sync: main checkout on master @ 03194f3, hook verified live; rule recorded in claude-profile notes/MAINTENANCE.md.
- 2026-08-07 (ctxdex gate): Bearer + connection-string content patterns are the likeliest false-positive sources in the manual-ingest secret gate — when the missed-query/refused-ingest log starts, seed it with this note before tuning any pattern.
- 2026-08-07 (workflow-fix closeout): Dashboard Toolkit tab (toolkitView() in F:\AI-Dev\Dashboard\index.html ~line 2835, hand-curated) may still list the retired "Sync Dashboard" GitHub Actions workflow (dashboard-sync.yml deleted from BIMpossible_Workspace 2026-08-07, commit 11b79ec) — verify and drop the entry if present.
- 2026-08-07 (dashboard dead-code closeout): F:\AI-Dev\Dashboard docs still describe the retired GitHub Models prose sync — REFRESH-SPEC.md ("sync_dashboard.py — soft prose only" section) plus docs/superpowers/specs/2026-07-04-local-dashboard-monitor-design.md and docs/superpowers/plans/2026-07-04-local-dashboard-monitor.md; prose-only cleanup, code already removed (e1961c9).

- 2026-08-07 (PR #317 reviewer, cosmetic): delete_group firm-default guard returns 409 (backend/aec/groups.py:~568) while delete_view's returns 403 (backend/aec/views.py:~506) -- pre-existing status-code inconsistency, no security impact; align when next touching either route. [WANDER-317-DELETE-GUARD-CODE]
- 2026-08-08 (branch-cleanup closeout): 4 merged PRs still hold their branch, left alone because a concurrent session was actively pushing to both repos at the time — BIMpossible #277 `claude/competent-kalam-977348`; Workspace #20 `claude/drift-stale-correction`, #21 `claude/session-handoff-notes`, #22 `claude/revert-session-handoff-notes`. Sweep them once that session is quiet, using the 4 checks in memory `squash-merge-branch-cleanup-checks` (`--merged`/plain `diff` both lie under squash merge). [WANDER-LINGERING-MERGED-BRANCHES]
- 2026-08-08 (/next sync): QUEUE.md was hand-rendered every prior sync; this one generated it deterministically from queue.yaml via a script written to the session scratchpad (`render_queue.py` — implements item-model.md's cone ranking + section rules, reports cycles/dangling ids). The scratchpad is session-scoped, so the script dies with it and the next sync hand-renders again into a different shape. RESOLVED 2026-08-08 same day, owner-directed: landed as .tools/state/render_queue.py (local store commit) + workspace draft PR #41; --check verified byte-for-byte against 492e33b. [WANDER-QUEUE-RENDERER]
- 2026-08-08 (Wave 30 dashboard refresh): Refresh-Dashboard.ps1 ran green overall but sync_activity.py aborted — gh_commits() returned None -> AttributeError at sync_activity.py:74 (build_patch line 99), so activity/lastActivity dates were NOT refreshed that run; waves/phases/DAG/graph-metrics rendered fine. Looks like a transient gh API/rate-limit empty response. Watch the next scheduled refresh; investigate only if it recurs. [WANDER-SYNCACTIVITY-GHNONE]

- Date: 2026-08-17
- Signal: permission-block
- Exact task / query: overnight closeout mandated a local-stack deploy; `docker compose up -d --build`, `start-local.ps1 -Rebuild`, and `Refresh-Frontend.ps1` were all denied by the session permission classifier
- What existing tool was tried: all three sanctioned deploy paths, then stopped per denial guidance
- Result and cost: deploy prepared but not executed; owner must run one command (queue item OPS-DEPLOY-STACK-REFRESH-20260817)
- Repeat count: 1
- Candidate response: settings Bash allow-rule for the repo deploy scripts (start-local.ps1 / Refresh-Frontend.ps1)
- Threshold to build: per ledger rules -- blocked in 3 separate sessions
