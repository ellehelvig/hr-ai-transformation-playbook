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


def _band(base_pay, historical=False, role="Compensation Analyst", level="IC3", tier="tier1"):
    """Helper. used_historical_pay_as_input is a required argument now, so every
    call site has to answer it; this keeps the happy-path tests readable while
    still forcing the answer."""
    return tool.get_band_position(role, level, tier, base_pay, used_historical_pay_as_input=historical)


def test_mid_range_pay_lands_near_p50():
    result = _band(112000)
    assert result["band_label"] == "mid-range"
    assert 45 <= result["percentile_estimate"] <= 55
    assert result["human_review_required"] is True
    assert result["refused"] is False


def test_below_range_pay_flags_retention_risk():
    result = _band(90000)
    assert result["band_label"] == "below-range"
    assert any("retention" in f.lower() for f in result["flags"])


def test_above_p90_flags_exception_process():
    result = _band(150000)
    assert result["band_label"] == "above-range"
    assert any("exception process" in f.lower() for f in result["flags"])


# ── The historical-pay guardrail must refuse, not annotate ───────────────────


def test_historical_pay_input_is_refused_with_no_market_position():
    """The one that matters most, and the one that used to be wrong.

    The previous implementation appended a BLOCKED-BY-POLICY string to `flags`
    and then returned the full band position anyway, percentile included. An
    agent that ignored one element of a list got exactly the answer the policy
    forbids. A refusal has to withhold the thing it is refusing to give."""
    result = _band(112000, historical=True)

    assert result["refused"] is True
    assert result["refusal_code"] == tool.HISTORICAL_PAY_REFUSAL_CODE
    assert result["human_review_required"] is True

    # Nothing quotable may survive the refusal.
    for leaked in (
        "percentile_estimate", "band_label", "band_low_p25", "band_mid_p50",
        "band_p75", "band_high_p90", "base_pay", "flags",
    ):
        assert leaked not in result, f"refusal payload leaked {leaked!r}"

    assert "pay-equity-governance.md" in result["reason"]
    assert "remediation" in result


def test_historical_pay_refusal_short_circuits_before_validation():
    """A refused call must not do work or reveal anything about the benchmark
    table, including whether the role exists or whether base_pay was valid."""
    unknown_role = tool.get_band_position(
        "Made Up Role", "IC99", "tier9", -5, used_historical_pay_as_input=True
    )
    assert unknown_role["refused"] is True
    assert unknown_role["refusal_code"] == tool.HISTORICAL_PAY_REFUSAL_CODE


def test_historical_pay_parameter_has_no_default():
    """The guardrail used to default to False, so it was off unless the caller
    volunteered incriminating information. Requiring the argument is what makes
    it a control rather than a suggestion, and FastMCP surfaces required
    arguments to the model on every call."""
    import inspect

    sig = inspect.signature(tool.get_band_position)
    param = sig.parameters["used_historical_pay_as_input"]
    assert param.default is inspect.Parameter.empty, (
        "used_historical_pay_as_input must stay required; a default re-disables the guardrail"
    )


# ── Percentile honesty ───────────────────────────────────────────────────────


def test_pay_outside_benchmark_range_returns_no_percentile():
    """The benchmark table holds p25, p50, p75, p90 and nothing else. The old
    code invented p1 as `p25 * 0.7` and p99 as `p90 * 1.25`, then interpolated
    into those made-up anchors and reported results like '8th percentile' that
    were artifacts of the constant. Outside the known range the honest answer
    is None plus a direction."""
    low = _band(50000)
    assert low["percentile_estimate"] is None
    assert low["band_label"] == "below-range"
    assert "outside the p25-to-p90 benchmark range" in low["percentile_estimate_note"]

    high = _band(400000)
    assert high["percentile_estimate"] is None
    assert high["band_label"] == "above-range"


def test_percentile_inside_range_is_monotonic():
    """Sanity check on the interpolation: more pay never means a lower
    percentile."""
    rows = [r for r in tool.list_known_bands()
            if r["role_family"] == "Compensation Analyst" and r["level"] == "IC3"][0]
    pays = [rows["p25"], rows["p50"], rows["p75"], rows["p90"]]
    percentiles = [_band(p)["percentile_estimate"] for p in pays]
    assert all(a <= b for a, b in zip(percentiles, percentiles[1:], strict=False)), percentiles
    assert percentiles == [25.0, 50.0, 75.0, 90.0]


def test_p75_is_exposed_not_just_used_internally():
    """p75 informs the interpolation, so a caller checking the tool's work needs
    to see it. It used to be loaded and silently discarded."""
    result = _band(112000)
    assert "band_p75" in result
    assert result["band_low_p25"] <= result["band_mid_p50"] <= result["band_p75"] <= result["band_high_p90"]


# ── Data validation ──────────────────────────────────────────────────────────


def test_malformed_band_data_fails_loudly(tmp_path, monkeypatch):
    """A missing key used to surface as a bare KeyError from inside the lookup
    loop. Comp analysts are the intended editors of comp_bands.json, so the
    error has to say which row and which key."""
    bad = tmp_path / "comp_bands.json"
    bad.write_text('{"bands": [{"role_family": "X", "level": "IC1", "location_tier": "tier1", "p25": 1}]}')
    monkeypatch.setattr(tool, "DATA_PATH", bad)
    tool._load_bands_cached.cache_clear()
    with pytest.raises(ValueError, match="missing required key"):
        tool._load_bands()


def test_non_monotonic_percentiles_rejected(tmp_path, monkeypatch):
    bad = tmp_path / "comp_bands.json"
    bad.write_text(
        '{"bands": [{"role_family": "X", "level": "IC1", "location_tier": "tier1",'
        ' "p25": 100, "p50": 90, "p75": 120, "p90": 130}]}'
    )
    monkeypatch.setattr(tool, "DATA_PATH", bad)
    tool._load_bands_cached.cache_clear()
    with pytest.raises(ValueError, match="non-monotonic"):
        tool._load_bands()


def test_unknown_role_raises_instead_of_guessing():
    with pytest.raises(tool.BandNotFoundError):
        _band(100000, role="Made Up Role", level="IC99")


def test_negative_pay_rejected():
    with pytest.raises(ValueError):
        _band(-5)


def test_human_review_required_always_true():
    """There must be no code path that turns this off -- it's a governance
    invariant, not a default. Includes the refusal path."""
    for row in tool.list_known_bands():
        result = _band(row["p50"], role=row["role_family"], level=row["level"], tier=row["location_tier"])
        assert result["human_review_required"] is True
    assert _band(112000, historical=True)["human_review_required"] is True


def test_list_known_bands_returns_all_rows():
    rows = tool.list_known_bands()
    assert len(rows) >= 10
    assert all({"role_family", "level", "location_tier", "p25", "p50", "p75", "p90"} <= row.keys() for row in rows)
