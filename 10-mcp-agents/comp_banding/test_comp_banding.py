import importlib.util as _ilu
import sys as _sys
from pathlib import Path as _Path

import pytest

# Loaded by explicit file path (not `import tool`) so this test suite is safe
# to run either standalone (`cd comp_banding && pytest`) or all together from
# the repo root (`pytest` at 10-mcp-agents/) -- every folder here has its own
# tool.py, and a bare `from tool import ...` collides across them under
# Python's module cache once more than one is imported in the same process.
_spec = _ilu.spec_from_file_location(f"_local_tool_{__name__}", _Path(__file__).parent / "tool.py")
tool = _ilu.module_from_spec(_spec)
_sys.modules[_spec.name] = tool
_spec.loader.exec_module(tool)


def test_mid_range_pay_lands_near_p50():
    result = tool.get_band_position("Compensation Analyst", "IC3", "tier1", 112000)
    assert result["band_label"] == "mid-range"
    assert 45 <= result["percentile_estimate"] <= 55
    assert result["human_review_required"] is True


def test_below_range_pay_flags_retention_risk():
    result = tool.get_band_position("Compensation Analyst", "IC3", "tier1", 90000)
    assert result["band_label"] == "below-range"
    assert any("retention" in f.lower() for f in result["flags"])


def test_above_p90_flags_exception_process():
    result = tool.get_band_position("Compensation Analyst", "IC3", "tier1", 150000)
    assert result["percentile_estimate"] >= 90
    assert any("exception process" in f.lower() for f in result["flags"])


def test_historical_pay_input_is_blocked_not_silently_allowed():
    """This is the one that matters most: the tool must never quietly bless
    a number derived from someone's own pay history."""
    result = tool.get_band_position(
        "Compensation Analyst", "IC3", "tier1", 112000, used_historical_pay_as_input=True
    )
    assert any(f.startswith("BLOCKED-BY-POLICY") for f in result["flags"])


def test_unknown_role_raises_instead_of_guessing():
    with pytest.raises(tool.BandNotFoundError):
        tool.get_band_position("Made Up Role", "IC99", "tier1", 100000)


def test_negative_pay_rejected():
    with pytest.raises(ValueError):
        tool.get_band_position("Compensation Analyst", "IC3", "tier1", -5)


def test_human_review_required_always_true():
    """There must be no code path that turns this off -- it's a governance
    invariant, not a default."""
    for row in tool.list_known_bands():
        result = tool.get_band_position(row["role_family"], row["level"], row["location_tier"], row["p50"])
        assert result["human_review_required"] is True


def test_list_known_bands_returns_all_rows():
    rows = tool.list_known_bands()
    assert len(rows) >= 10
    assert all({"role_family", "level", "location_tier", "p25", "p50", "p75", "p90"} <= row.keys() for row in rows)
