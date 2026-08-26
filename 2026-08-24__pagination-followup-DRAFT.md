# Pagination follow-up — DRAFT (not yet filed; awaiting owner approval)

Ready to file as either a GitHub issue or a `queue.yaml` item. Content is identical; pick the sink.

---

**Title:** APS discovery: paginate folder contents before model-index tombstone reconciliation

**Severity:** correctness / latent (bites projects with any single ACC folder holding >200 children)
**Introduced by:** pre-existing (unpaginated walk predates #466); **made impactful by:** PR #466's tombstone reconcile
**Area:** `backend/aps/router.py` (folder-contents walk), `backend/aec/model_index_sync.py` (reconcile consumer)

## Problem
`backend/aps/router.py` `list_all_rvts` walks `data/v1/projects/{pid}/folders/{id}/contents` and reads
`child.get("data")` ([router.py:667-670](backend/aps/router.py:667)) **without following `links.next`**.
APS paginates folder contents at 200 items. A folder with >200 children therefore returns a
**successful-but-partial** result. PR #466's reconcile pass (`index_discovered_models`) treats any
`item_id` absent from that partial set as deleted, tombstones it (`deleted_at` set), and excludes it
from `/search/models`, `/search/model-counts`, and the model picker. Because the omitted models sit
on later pages, they never re-enter `discovered_ids` on subsequent crawls either, so the restore path
never fires — they stay hidden until pagination is fixed. Rows are soft-deleted (recoverable), not
lost.

Note the safe half already holds: a **hard** crawl failure (any `_authed_get` raises mid-walk)
propagates out of `_all_rvts_cache.get_or_compute` before `index_discovered_models` is called, so a
failed crawl does **not** tombstone. The gap is specifically the *silent partial* — HTTP 200 with a
truncated page.

## Acceptance criteria
- [ ] Follow `links.next` for **every** `folders/{id}/contents` response until the cursor is exhausted (root folder walk and the recursive `collect` subfolder walk both).
- [ ] Preserve existing traversal semantics, duplicate handling, and any cycle/visited protection (do not regress `_is_dead_lineage` filtering or path construction).
- [ ] Guarantee reconciliation never receives a partial project discovery set: either the crawl returns the complete lineage set or it raises (which already skips reconcile) — never a truncated success.
- [ ] Add a multi-page fixture where an `.rvt` item appears only on page 2 (`links.next` present on page 1).
- [ ] Add a regression test asserting a later-page model is **not** tombstoned after a crawl+reconcile.
- [ ] Preserve safe failure semantics: a failed/invalid crawl must **skip** reconciliation for that project (current behavior), never be treated as an empty project (which tombstones all).
- [ ] No changes to `sdk_proxy.py` / `proxy_router.py` unless later evidence requires them.

## Out of scope
- The `deleted_at` schema/index and the reconcile logic themselves (correct as shipped in #466).
- Any change to search egress guards.

## Evidence
- Unpaginated read: [backend/aps/router.py:667-670](backend/aps/router.py:667) and the top-level walk [router.py:705-718](backend/aps/router.py:705).
- Paginated precedent already in the same file (fields walk): [router.py:346-365](backend/aps/router.py:346) — mirror this `offset += 200` / `links.next` pattern.
- Reconcile consumer: `index_discovered_models` in `backend/aec/model_index_sync.py` (docstring already warns callers must pass "a real, successfully-fetched all-rvts result, never a partial/error-path list").
