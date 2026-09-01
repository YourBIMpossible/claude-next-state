"""Tests for the two-tier /next store (queue_store.py + render_queue.py).

Run: python -m pytest test_queue_store.py -q
"""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest
import yaml

import queue_store
import render_queue
from queue_store import StoreError, load_store

HERE = Path(__file__).parent


def _item(id_, status="ready", pr=None, sha=None, **over):
    item = {
        "id": id_,
        "title": f"item {id_}",
        "projects": ["bimpossible"],
        "status": status,
        "unblocks": [],
        "blocked_by": [],
        "verification": {"level": "claimed", "by": "test", "at": "2026-08-01"},
        "source": "test fixture",
        "evidence": [],
    }
    if pr:
        item["evidence"].append({"kind": "pr", "ref": f"BIMpossible#{pr}"})
    if sha:
        item["evidence"].append({"kind": "commit", "ref": sha})
    item.update(over)
    return item


def _write_store(tmp_path, active_items, archive_items=None, archive_raw=None):
    (tmp_path / "queue.yaml").write_text(
        yaml.safe_dump({"schema_version": 1, "reconciled": {}, "items": active_items}),
        encoding="utf-8",
    )
    if archive_raw is not None:
        (tmp_path / "queue-archive.yaml").write_text(archive_raw, encoding="utf-8")
    elif archive_items is not None:
        for it in archive_items:
            it.setdefault("archived_at", "2026-08-17")
            it.setdefault("archived_reason", "test")
        (tmp_path / "queue-archive.yaml").write_text(
            yaml.safe_dump({"schema_version": 1, "items": archive_items}),
            encoding="utf-8",
        )
    (tmp_path / "projects.yaml").write_text(
        yaml.safe_dump({"projects": [{"key": "bimpossible", "active": True}]}),
        encoding="utf-8",
    )
    return tmp_path


# --- 1. no rediscovery -------------------------------------------------------

def test_archived_pr_is_known_not_rediscovered(tmp_path):
    _write_store(tmp_path, [_item("A1")], [_item("Z1", status="live", pr=187)])
    store = load_store(tmp_path)
    assert store.is_known_pr("BIMpossible#187") == [("Z1", "archive")]
    assert store.is_known_pr("bimpossible#187") == [("Z1", "archive")]  # case-insensitive
    assert store.is_known_pr("https://github.com/x/BIMpossible/pull/187") == [("Z1", "archive")]
    assert store.is_known_pr("BIMpossible#999") == []


# --- 2. archived records findable by PR, commit, and id ----------------------

def test_archived_record_findable_by_all_identities(tmp_path):
    _write_store(tmp_path, [_item("A1")], [_item("Z1", status="live", pr=42, sha="deadbeef1")])
    store = load_store(tmp_path)
    assert store.find("Z1") == ("archive", store.archived_items[0])
    assert ("Z1", "archive") in store.is_known_pr("BIMpossible#42")
    assert ("Z1", "archive") in store.is_known_commit("deadbeef1")
    assert ("Z1", "archive") in store.is_known_commit("deadbee")  # short-sha prefix


# --- 3. active behavior intact ----------------------------------------------

def test_active_items_and_render_sections(tmp_path):
    _write_store(
        tmp_path,
        [
            _item("A1", status="blocked_owner", owner_gate=True, effort="S", unblocks=["A2"]),
            _item("A2", status="ready"),
            _item("A3", status="landed"),
        ],
        [_item("Z1", status="live")],
    )
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    assert "[A1]" in out and "[A2]" in out and "[A3]" in out
    # archived live within the 30-day window still shows in the Live section...
    assert "[Z1]" in out and out.index("[Z1]") > out.index("Live (last 30 days)")
    assert "Blocked on you" in out and "Landed — not verified live" in out
    # ...but an archived live OUTSIDE the window never renders
    out_late = render_queue.build(tmp_path, date(2026, 10, 1))
    assert "[Z1]" not in out_late


def test_cones_stable_across_archiving(tmp_path):
    """Moving a closed item to archive must not change active ranking (union cone math)."""
    active_all = [
        _item("A1", unblocks=["L1"]),
        _item("L1", status="live", unblocks=["L2"]),
        _item("L2", status="live"),
    ]
    _write_store(tmp_path, active_all)
    before = render_queue.build(tmp_path, date(2026, 8, 17))

    tmp2 = tmp_path / "after"
    tmp2.mkdir()
    _write_store(
        tmp2,
        [_item("A1", unblocks=["L1"])],
        [_item("L1", status="live", unblocks=["L2"]), _item("L2", status="live")],
    )
    after = render_queue.build(tmp2, date(2026, 8, 17))
    # A1's cone (2, through the archive) identical; no dangling-defect banner appears.
    assert "unblocks 2" in before and "unblocks 2" in after
    assert "dangling" not in after


# --- 4/5. duplicate identity ------------------------------------------------

def test_duplicate_id_across_tiers_rejected(tmp_path):
    _write_store(tmp_path, [_item("X1")], [_item("X1", status="live")])
    with pytest.raises(StoreError, match="duplicate item id 'X1'"):
        load_store(tmp_path)


def test_duplicate_id_within_tier_rejected(tmp_path):
    _write_store(tmp_path, [_item("X1"), _item("X1")])
    with pytest.raises(StoreError, match="duplicate item id 'X1'"):
        load_store(tmp_path)


def test_shared_pr_across_tiers_is_many_to_many_not_error(tmp_path):
    """Canonical rule: PR identity is many-to-many; 'known' = present in combined index."""
    _write_store(tmp_path, [_item("A1", pr=100)], [_item("Z1", status="live", pr=100)])
    store = load_store(tmp_path)
    assert set(store.is_known_pr("BIMpossible#100")) == {("A1", "active"), ("Z1", "archive")}


# --- 6. malformed archive fails safely --------------------------------------

def test_malformed_archive_yaml_fails(tmp_path):
    _write_store(tmp_path, [_item("A1")], archive_raw="items: [::not yaml::")
    with pytest.raises(StoreError, match="not valid YAML"):
        load_store(tmp_path)


def test_archive_invalid_status_fails(tmp_path):
    _write_store(tmp_path, [_item("A1")], [_item("Z1", status="ready")])
    with pytest.raises(StoreError, match="not an allowed archived status"):
        load_store(tmp_path)


def test_archive_missing_metadata_fails(tmp_path):
    bad = _item("Z1", status="live")
    (tmp_path / "queue-archive.yaml").write_text(
        yaml.safe_dump({"schema_version": 1, "items": [bad]}), encoding="utf-8"
    )
    _write_store(tmp_path, [_item("A1")])  # writes queue.yaml/projects.yaml, keeps archive file
    with pytest.raises(StoreError, match="archived_at"):
        load_store(tmp_path)


def test_schema_version_mismatch_fails(tmp_path):
    _write_store(tmp_path, [_item("A1")])
    (tmp_path / "queue-archive.yaml").write_text(
        yaml.safe_dump({"schema_version": 2, "items": []}), encoding="utf-8"
    )
    with pytest.raises(StoreError, match="schema_version mismatch"):
        load_store(tmp_path)


def test_active_bad_status_fails(tmp_path):
    _write_store(tmp_path, [_item("A1", status="done")])
    with pytest.raises(StoreError, match="outside the closed vocabulary"):
        load_store(tmp_path)


# --- 7. missing archive = backward compatible -------------------------------

def test_missing_archive_backward_compatible(tmp_path):
    _write_store(tmp_path, [_item("A1")])
    store = load_store(tmp_path)
    assert store.archived_items == []
    assert render_queue.build(tmp_path, date(2026, 8, 17))


# --- 8. archive immutability contract ---------------------------------------

def test_soft_required_fields_reported_not_fatal(tmp_path):
    item = _item("A1")
    del item["unblocks"], item["source"]
    _write_store(tmp_path, [item])
    store = load_store(tmp_path)
    assert any("A1" in d for d in store.defects)


# --- 9. reopen linkage -------------------------------------------------------

def test_reopen_via_follow_up_of(tmp_path):
    """Reopen = NEW active item with follow_up_of; archive record untouched and both load."""
    _write_store(
        tmp_path,
        [_item("A1-REOPEN", follow_up_of="Z1")],
        [_item("Z1", status="live", pr=55)],
    )
    store = load_store(tmp_path)
    assert store.find("A1-REOPEN")[0] == "active"
    assert store.find("Z1")[0] == "archive"
    assert store.active_items[0]["follow_up_of"] == "Z1"
    assert ("Z1", "archive") in store.is_known_pr("BIMpossible#55")


# --- 10. CLI probes ----------------------------------------------------------

def test_cli_validate_and_probes(tmp_path):
    _write_store(tmp_path, [_item("A1", pr=77)], [_item("Z1", status="dropped", sha="abc1234def")])
    script = str(HERE / "queue_store.py")
    ok = subprocess.run([sys.executable, script, "--state-dir", str(tmp_path)],
                        capture_output=True, text=True)
    assert ok.returncode == 0 and "OK" in ok.stdout
    known = subprocess.run([sys.executable, script, "--state-dir", str(tmp_path),
                            "--known-pr", "BIMpossible#77"], capture_output=True, text=True)
    assert known.returncode == 0
    unknown = subprocess.run([sys.executable, script, "--state-dir", str(tmp_path),
                              "--known-pr", "BIMpossible#78"], capture_output=True, text=True)
    assert unknown.returncode == 2


def test_bare_pr_ref_indexed_under_projects(tmp_path):
    """'PR#244' with no repo name must be findable by the item's project key."""
    it = _item("Z1", status="live")
    it["evidence"] = [{"kind": "pr", "ref": "PR#244 squash fa865d6"}]
    _write_store(tmp_path, [_item("A1")], [it])
    store = load_store(tmp_path)
    assert ("Z1", "archive") in store.is_known_pr("bimpossible#244")
    assert ("Z1", "archive") in store.is_known_pr("PR#244")
    assert ("Z1", "archive") in store.is_known_commit("fa865d6")


# --- resolved (ranking) cone vs display cone --------------------------------
# The renderer keeps two distinct cone counts: the DISPLAY cone (`unblocks N`,
# inclusive of dangling ids per item-model.md) and the RANKING cone (resolved
# nodes only), which alone decides graph shape and cone ordering. A dangling edge
# must inflate the first and never the second.

def test_cone_size_splits_display_from_rank():
    """Unit-level proof of the split: display counts an unknown id; rank does not."""
    unblocks = {"A": ["B", "GHOST"], "B": ["C"], "C": []}
    display, rank, cycles, dangling = render_queue.cone_size("A", unblocks)
    assert display == 3          # B, C, GHOST — inclusive `unblocks N`
    assert rank == 2             # B, C — resolved nodes only
    assert dangling == ["GHOST"]
    assert cycles == []


def test_flat_graph_survives_dangling_unblock(tmp_path):
    """Two dangling unblocks ids must not inflate a flat graph into 'deep' and
    reorder by cone — the exact regression this fix targets."""
    _write_store(tmp_path, [
        _item("A1", status="ready"),
        _item("Z1", status="ready", unblocks=["GHOST1", "GHOST2"]),
    ])
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    assert "this store is flat today" in out            # flat regime, on resolved edges
    assert out.index("[A1]") < out.index("[Z1]")        # id order, not cone order
    assert "Z1` dangling unblocks ids: GHOST1, GHOST2" in out  # defect still surfaced


def test_deep_graph_from_resolved_edges(tmp_path):
    """A real resolved chain (A→B→C) is deep; resolved cone leads intra-section order."""
    _write_store(tmp_path, [
        _item("A1", status="ready", unblocks=["B1"]),
        _item("B1", status="ready", unblocks=["C1"]),
        _item("C1", status="ready"),
    ])
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    assert "cone` leading (deep graph)" in out
    # A1 rank cone 2 > B1 1 > C1 0 → cone-descending within "Next up"
    assert out.index("[A1]") < out.index("[B1]") < out.index("[C1]")


def test_flat_graph_cone_does_not_override_tiebreak(tmp_path):
    """On a flat graph a dangling-inflated DISPLAY cone must not reorder items;
    the finalization tail (owner-gated+S, effort, risk, id) governs."""
    _write_store(tmp_path, [
        _item("A1", status="ready", owner_gate=True, effort="S"),
        _item("B1", status="ready", effort="M", unblocks=["GHOST1", "GHOST2"]),
    ])
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    assert "this store is flat today" in out
    # A1 wins on owner-gated+S; B1's display cone of 2 (all dangling) does not pull it up.
    assert out.index("[A1]") < out.index("[B1]")
    assert "unblocks 2" in out                          # B1's inclusive display cone still shown


def test_display_cone_and_defect_preserved(tmp_path):
    """Dangling refs stay visible: inclusive `unblocks N` on the line AND a defect
    note. The fix removes them from RANKING, never from the operator's view."""
    _write_store(tmp_path, [
        _item("A1", status="ready", unblocks=["B1", "GHOST"]),
        _item("B1", status="ready"),
    ])
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    assert "[A1] item A1" in out and "unblocks 2" in out   # display cone = B1 + GHOST
    assert "Data defects found while ranking" in out
    assert "A1` dangling unblocks ids: GHOST" in out


def test_banner_is_anchor_first(tmp_path):
    """Banner reflects anchor-first policy with a stable, dateless item-model.md reference."""
    _write_store(tmp_path, [_item("A1", status="ready")])
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    assert "Anchor-first, leverage-ranked (per item-model.md)" in out
    assert "critical path" not in out.lower()   # obsolete cone-first framing is gone
    assert "2026-08-30" not in out              # no frozen policy date baked into output


def _write_projects(tmp_path, projects):
    (tmp_path / "projects.yaml").write_text(
        yaml.safe_dump({"projects": projects}), encoding="utf-8"
    )


# --- Outcome D: commit_index harvests ONLY declared commit evidence, shape-guarded ---
# The parser must index a git commit id when (and only when) it is asserted as commit/PR
# identity AND is commit-shaped (7–40 hex, != 32). MD5 provenance (32 hex), blob/tree object
# shas (40 hex, but only ever in prose), and incidental hex in narrative must never be
# mistaken for a commit — that false-positive is what poisoned dedup.

def test_commit_index_indexes_real_shas_from_commit_evidence(tmp_path):
    """7–40-char SHAs in kind: commit evidence are indexed and prefix-matchable both ways."""
    it = _item("A1", status="live")
    it["evidence"] = [
        {"kind": "commit", "ref": "abc1234 fix thing"},                          # 7-char abbrev
        {"kind": "commit", "ref": "0123456789abcdef0123456789abcdef01234567"},   # 40-char full
    ]
    _write_store(tmp_path, [_item("A0")], [it])
    store = load_store(tmp_path)
    assert ("A1", "archive") in store.is_known_commit("abc1234")
    assert ("A1", "archive") in store.is_known_commit("abc12")     # shorter probe prefix
    assert ("A1", "archive") in store.is_known_commit("0123456789abcdef0123456789abcdef01234567")
    assert ("A1", "archive") in store.is_known_commit("0123456")   # abbrev of the full sha


def test_commit_index_rejects_md5_even_in_commit_evidence(tmp_path):
    """A 32-hex MD5 is never a git abbreviation (a full SHA-1 is 40), so it is rejected by
    shape even when it sits inside a kind: commit ref. This is the provenance-hash fix."""
    it = _item("A1", status="live")
    it["evidence"] = [{"kind": "commit", "ref": "af8996536aa8b442fa2093023a99567a provenance md5"}]
    _write_store(tmp_path, [_item("A0")], [it])
    store = load_store(tmp_path)
    assert store.is_known_commit("af8996536aa8b442fa2093023a99567a") == []


def test_commit_index_ignores_blob_sha_in_prose(tmp_path):
    """A 40-char blob/tree object sha in narrative (kind: log) is excluded structurally —
    commit ids come only from kind: commit|pr evidence, never free prose."""
    it = _item("A1", status="live")
    it["evidence"] = [
        {"kind": "log", "ref": "shared LF blob d85fb68a82db76e46f3c1f0bcac59e05f8d5ecc7 across the pair"},
    ]
    _write_store(tmp_path, [_item("A0")], [it])
    store = load_store(tmp_path)
    assert store.is_known_commit("d85fb68a82db76e46f3c1f0bcac59e05f8d5ecc7") == []


def test_commit_index_ignores_hexlike_in_verification_prose(tmp_path):
    """Hex-like identifiers in verification.by (free prose) never enter the commit index,
    even when commit-shaped — prose is PR-scanned only, not commit-scanned."""
    it = _item("A1", status="live")
    it["evidence"] = []
    it["verification"] = {
        "level": "claimed",
        "by": "temp cache key deadbeef1 written by the run; not a commit",
        "at": "2026-08-01",
    }
    _write_store(tmp_path, [_item("A0")], [it])
    store = load_store(tmp_path)
    assert store.is_known_commit("deadbeef1") == []


def test_commit_index_positive_and_negative_together(tmp_path):
    """Intentional detection: a real commit and an MD5 in the same commit evidence — only
    the commit is known, the MD5 stays invisible to dedup."""
    it = _item("A1", status="live")
    it["evidence"] = [
        {"kind": "commit", "ref": "b98c71a restored the probe"},
        {"kind": "commit", "ref": "md5 af8996536aa8b442fa2093023a99567a"},
    ]
    _write_store(tmp_path, [_item("A0")], [it])
    store = load_store(tmp_path)
    assert ("A1", "archive") in store.is_known_commit("b98c71a")
    assert store.is_known_commit("af8996536aa8b442fa2093023a99567a") == []


# --- Outcome A/E: dormancy enforcement --------------------------------------
# A dormant project's item can never (a) carry a runnable probe, (b) rank as actionable/#1,
# or (c) render as verified from prior evidence. Enforced deterministically, not by convention.

def test_load_dormant_reads_flag(tmp_path):
    _write_store(tmp_path, [_item("A1")])
    _write_projects(tmp_path, [
        {"key": "bimpossible", "active": True},
        {"key": "families", "active": False, "dormant": True},
    ])
    assert queue_store.load_dormant(tmp_path) == {"families"}


# Dormant-target map: key -> normalized checkout-path token (what load_dormant_targets returns).
FAM_TARGETS = {"families": "f:/bimpossible-families"}


def test_dormancy_defect_flags_runnable_probe_on_dormant_item(tmp_path):
    item = _item("F1", status="parked", projects=["families"],
                 live_check=["cd F:/BIMpossible-Families && python -m pytest -q"])
    assert queue_store.dormancy_defects([item], FAM_TARGETS)


def test_dormancy_no_defect_when_live_check_empty(tmp_path):
    item = _item("F1", status="parked", projects=["families"], live_check=[])
    assert queue_store.dormancy_defects([item], FAM_TARGETS) == []


def test_dormancy_exempts_governance_item_scoped_to_live_project(tmp_path):
    """A workspace-scoped gate that only references a dormant repo via affects_projects is
    exempt — it may run its own (workspace) probe; the ban is on commands against the dormant repo."""
    gate = _item("GATE", status="parked", projects=["workspace"], affects_projects=["families"],
                 live_check=["git -C F:/BIMpossible-Workspace status -sb"])
    assert queue_store.dormancy_defects([gate], FAM_TARGETS) == []


def test_load_dormant_targets_maps_key_to_normalized_path(tmp_path):
    _write_projects(tmp_path, [
        {"key": "workspace", "active": True},
        {"key": "families", "active": False, "dormant": True,
         "path": "F:\\BIMpossible-Families"},
    ])
    targets = queue_store.load_dormant_targets(tmp_path)
    assert targets == {"families": "f:/bimpossible-families"}


def test_dormancy_flags_mixed_scope_command_targeting_dormant(tmp_path):
    """A mixed [workspace, families] item whose live_check names the dormant checkout path is a
    violation — the dormant leg must not be probed even though the item also has a live leg."""
    item = _item("MIX", status="ready", projects=["workspace", "families"],
                 live_check=[
                     "git -C F:/BIMpossible-Workspace log --oneline origin/main..main",
                     "git -C F:\\BIMpossible-Families status -sb",
                 ])
    defects = queue_store.dormancy_defects([item], FAM_TARGETS)
    assert defects and "MIX" in defects[0] and "families" in defects[0]


def test_dormancy_no_defect_mixed_scope_command_targets_only_live(tmp_path):
    """Mixed scope is fine as long as no live_check command names the dormant repo: the live-leg
    probes stay runnable, the dormant leg is simply carried (and rendered suspended elsewhere)."""
    item = _item("MIX", status="ready", projects=["workspace", "families"],
                 live_check=[
                     "git -C F:/BIMpossible-Workspace log --oneline origin/main..main",
                     "gh pr view 5 --repo YourBIMpossible/evidence-compiler --json state",
                 ])
    assert queue_store.dormancy_defects([item], FAM_TARGETS) == []


def test_dormancy_active_only_item_never_flagged(tmp_path):
    """An item with no dormant leg is out of the gate entirely, whatever its live_check says."""
    item = _item("ACT", status="ready", projects=["workspace", "bimpossible"],
                 live_check=["git -C F:/BIMpossible-Workspace status -sb"])
    assert queue_store.dormancy_defects([item], FAM_TARGETS) == []


def test_cli_hard_fails_on_dormant_runnable_probe(tmp_path):
    fam = _item("F1", status="parked", projects=["families"],
                live_check=["cd F:/BIMpossible-Families && python -m pytest -q"])
    _write_store(tmp_path, [_item("A1"), fam])
    _write_projects(tmp_path, [
        {"key": "bimpossible", "active": True},
        {"key": "families", "active": False, "dormant": True,
         "path": "F:\\BIMpossible-Families"},
    ])
    script = str(HERE / "queue_store.py")
    res = subprocess.run([sys.executable, script, "--state-dir", str(tmp_path)],
                         capture_output=True, text=True)
    assert res.returncode == 1
    assert "dormancy violation" in res.stderr


def test_cli_hard_fails_on_mixed_scope_dormant_targeting_command(tmp_path):
    """End-to-end: the validator rejects a mixed-scope item whose live_check names the dormant
    checkout — the bypass the all-dormant-only gate used to wave through."""
    mix = _item("MIX", status="ready", projects=["workspace", "families"],
                live_check=[
                    "git -C F:/BIMpossible-Workspace status -sb",
                    "git -C F:/BIMpossible-Families log --oneline",
                ])
    _write_store(tmp_path, [_item("A1"), mix])
    _write_projects(tmp_path, [
        {"key": "workspace", "active": True},
        {"key": "bimpossible", "active": True},
        {"key": "families", "active": False, "dormant": True,
         "path": "F:\\BIMpossible-Families"},
    ])
    script = str(HERE / "queue_store.py")
    res = subprocess.run([sys.executable, script, "--state-dir", str(tmp_path)],
                         capture_output=True, text=True)
    assert res.returncode == 1
    assert "dormancy violation" in res.stderr and "MIX" in res.stderr


def test_render_marks_dormant_item_suspended_and_discloses(tmp_path):
    """A dormant-scoped item renders SUSPENDED (never verified from stale evidence), carries the
    suspended-probes marker, and the board discloses the dormant-project constraint."""
    fam = _item("F1", status="parked", projects=["families"], live_check=[])
    fam["verification"] = {"level": "verified", "by": "stale prior evidence", "at": "2026-08-01"}
    _write_store(tmp_path, [_item("A1", status="ready"), fam])
    _write_projects(tmp_path, [
        {"key": "bimpossible", "active": True},
        {"key": "families", "active": False, "dormant": True},
    ])
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    assert "Dormant project(s):" in out and "`families`" in out
    assert "[F1]" in out and "SUSPENDED" in out
    assert "probes suspended" in out
    assert "VERIFIED" not in out          # the stale verified badge is overridden, never shown


def test_render_shows_dormancy_gate_marker(tmp_path):
    """A live-scoped governance item that governs a dormant repo via affects_projects shows the
    gate marker and triggers the board disclosure, without being marked SUSPENDED itself."""
    gate = _item("GATE", status="parked", projects=["workspace"], affects_projects=["families"])
    _write_store(tmp_path, [_item("A1", status="ready"), gate])
    _write_projects(tmp_path, [
        {"key": "workspace", "active": True},
        {"key": "families", "active": False, "dormant": True},
    ])
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    assert "dormancy gate" in out
    assert "Dormant project(s):" in out
    gate_block = out[out.index("[GATE]"):]
    assert "SUSPENDED" not in gate_block.split("\n\n")[0]   # gate is scoped to a live project


def test_render_mixed_scope_downgrades_verified_to_partial(tmp_path):
    """A mixed [workspace, families] item that stored VERIFIED (on its live leg) must NOT render a
    whole-item VERIFIED badge — the dormant leg is unprobed, so the item renders PARTIAL and carries
    the suspended-leg marker. The active leg stays visible and the item is not marked SUSPENDED."""
    mix = _item("MIX", status="ready", projects=["workspace", "families"],
                live_check=["git -C F:/BIMpossible-Workspace status -sb"])
    mix["verification"] = {"level": "verified", "by": "workspace leg pushed", "at": "2026-08-30"}
    _write_store(tmp_path, [_item("A1", status="ready"), mix])
    _write_projects(tmp_path, [
        {"key": "workspace", "active": True},
        {"key": "families", "active": False, "dormant": True,
         "path": "F:\\BIMpossible-Families"},
    ])
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    mix_block = out[out.index("[MIX]"):].split("\n\n")[0]
    assert "PARTIAL" in mix_block
    assert "VERIFIED" not in mix_block          # never fully verified off the live leg alone
    assert "SUSPENDED" not in mix_block         # active leg is still tracked, not suspended
    assert "dormant leg" in mix_block and "families" in mix_block
    assert "Dormant project(s):" in out         # board still discloses the constraint


def test_render_and_validation_agree_on_mixed_scope(tmp_path):
    """Renderer and store-validation agree: a mixed item with only live-targeting commands passes
    validation (no dormancy defect) AND renders as not-fully-verified. One truth, two surfaces."""
    mix = _item("MIX", status="ready", projects=["workspace", "families"],
                live_check=["git -C F:/BIMpossible-Workspace status -sb"])
    mix["verification"] = {"level": "verified", "by": "workspace leg", "at": "2026-08-30"}
    _write_projects(tmp_path, [
        {"key": "workspace", "active": True},
        {"key": "families", "active": False, "dormant": True,
         "path": "F:\\BIMpossible-Families"},
    ])
    assert queue_store.dormancy_defects([mix], queue_store.load_dormant_targets(tmp_path)) == []
    _write_store(tmp_path, [_item("A1", status="ready"), mix])
    _write_projects(tmp_path, [
        {"key": "workspace", "active": True},
        {"key": "families", "active": False, "dormant": True,
         "path": "F:\\BIMpossible-Families"},
    ])
    out = render_queue.build(tmp_path, date(2026, 8, 17))
    mix_block = out[out.index("[MIX]"):].split("\n\n")[0]
    assert "PARTIAL" in mix_block and "VERIFIED" not in mix_block


def test_dormant_item_status_is_not_actionable(tmp_path):
    """Structural proof it cannot be #1: a dormant item is parked, and parked is outside the
    actionable set the ranker draws the #1 move from."""
    assert "parked" not in render_queue.ACTIONABLE_STATUSES


# --- real store sanity -------------------------------------------------------

def test_real_store_loads_and_renders():
    """The actual live store in this worktree must validate and reproduce QUEUE.md.

    The generation date is the one run-dependent input, so read it back from the file's
    own header rather than hard-coding it — otherwise this test rots the moment QUEUE.md
    is regenerated on a later day, which has nothing to do with what it means to verify.
    """
    store = load_store(HERE)
    assert len(store.ids) == len(store.active_items) + len(store.archived_items)
    existing = (HERE / "QUEUE.md").read_text(encoding="utf-8")
    stamp = re.search(r"Generated (\d{4}-\d{2}-\d{2})", existing)
    assert stamp, "QUEUE.md is missing its 'Generated <date>' header line"
    text = render_queue.build(HERE, date.fromisoformat(stamp.group(1)))
    assert existing == text
