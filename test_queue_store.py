"""Tests for the two-tier /next store (queue_store.py + render_queue.py).

Run: python -m pytest test_queue_store.py -q
"""

from __future__ import annotations

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


# --- real store sanity -------------------------------------------------------

def test_real_store_loads_and_renders():
    """The actual live store in this worktree must validate and reproduce QUEUE.md."""
    store = load_store(HERE)
    assert len(store.ids) == len(store.active_items) + len(store.archived_items)
    text = render_queue.build(HERE, date(2026, 8, 24))
    assert (HERE / "QUEUE.md").read_text(encoding="utf-8") == text
