"""
comp_banding.tool
==================

A deterministic comp-banding helper for a Compensation Analyst copilot.

Design intent (read this before you extend it):

This is deliberately NOT an LLM call. Banding math should be reproducible,
auditable, and identical for the same inputs every time -- that is a
governance requirement, not a style preference (see
03-governance/pay-equity-governance.md in the main playbook). The calling
agent (Claude, or whatever orchestrates this MCP server) is responsible for
the parts that genuinely need judgment: explaining the result to a manager
in plain language, drafting an offer narrative, flagging edge cases for a
human. This module is responsible for the arithmetic and the guardrails,
and nothing else.

Two guardrails are load-bearing, not decorative:

1. `used_historical_pay_as_input` -- if a caller says the proposed pay was
   derived from the candidate's own prior salary, the tool refuses to bless
   it as market-aligned. This encodes the playbook rule: "Using employee
   compensation history to train or fine-tune a model: Not approved."
   Historical pay reflects historical bias; a banding tool that quietly
   launders that number back into "market-aligned" is exactly the failure
   mode the governance doc warns about.
2. The response never returns a bare go/no-go. It always returns enough
   context (percentile, band edges, flag) for a human to make the call,
   and always carries a `human_review_required` field set to True. There is
   no code path that sets it to False. See ADOPTION-MONITORING.md for how
   that invariant gets checked in production, not just in this file.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "comp_bands.json"


class BandNotFoundError(ValueError):
    """Raised when no benchmark row matches the requested role/level/tier."""


@dataclass
class BandPosition:
    role_family: str
    level: str
    location_tier: str
    base_pay: float
    band_low: float
    band_mid: float
    band_high: float
    percentile_estimate: float
    band_label: str
    flags: list[str] = field(default_factory=list)
    human_review_required: bool = True
    disclaimer: str = (
        "Advisory only. This tool estimates market position from illustrative "
        "benchmark data; it does not set pay. A comp analyst or People "
        "Partner makes the final call, per the playbook's human-review-gate "
        "policy."
    )

    def to_dict(self) -> dict:
        return {
            "role_family": self.role_family,
            "level": self.level,
            "location_tier": self.location_tier,
            "base_pay": self.base_pay,
            "band_low_p25": self.band_low,
            "band_mid_p50": self.band_mid,
            "band_high_p90": self.band_high,
            "percentile_estimate": self.percentile_estimate,
            "band_label": self.band_label,
            "flags": self.flags,
            "human_review_required": self.human_review_required,
            "disclaimer": self.disclaimer,
        }


def _load_bands() -> list[dict]:
    with open(DATA_PATH) as f:
        payload = json.load(f)
    return payload["bands"]


def _interpolate_percentile(base_pay: float, p25: float, p50: float, p75: float, p90: float) -> float:
    """Piecewise-linear percentile estimate. Clamped to [1, 99] outside the
    known points rather than extrapolated, because linear extrapolation past
    p90 or below p25 gets misleading fast and this number gets quoted in
    conversations with candidates -- better to say '99th+' than invent 140."""
    points = [(1.0, p25 * 0.7), (25.0, p25), (50.0, p50), (75.0, p75), (90.0, p90), (99.0, p90 * 1.25)]
    if base_pay <= points[0][1]:
        return 1.0
    if base_pay >= points[-1][1]:
        return 99.0
    for (pct_a, pay_a), (pct_b, pay_b) in zip(points, points[1:], strict=False):
        if pay_a <= base_pay <= pay_b:
            if pay_b == pay_a:
                return pct_a
            frac = (base_pay - pay_a) / (pay_b - pay_a)
            return round(pct_a + frac * (pct_b - pct_a), 1)
    return 50.0


def _label_for(percentile: float) -> str:
    if percentile < 25:
        return "below-range"
    if percentile < 50:
        return "low-range"
    if percentile < 75:
        return "mid-range"
    if percentile < 90:
        return "high-range"
    return "above-range"


def get_band_position(
    role_family: str,
    level: str,
    location_tier: str,
    base_pay: float,
    used_historical_pay_as_input: bool = False,
) -> dict:
    """Look up market position for a proposed base pay against illustrative
    benchmark bands.

    Raises BandNotFoundError if role_family/level/location_tier has no
    benchmark row -- callers (including the calling agent) must not
    silently fall back to a "closest match"; an unmatched role should be
    surfaced for a human to source real benchmark data, not guessed at.
    """
    if base_pay <= 0:
        raise ValueError("base_pay must be positive")

    for row in _load_bands():
        if (
            row["role_family"].lower() == role_family.lower()
            and row["level"].lower() == level.lower()
            and row["location_tier"].lower() == location_tier.lower()
        ):
            percentile = _interpolate_percentile(base_pay, row["p25"], row["p50"], row["p75"], row["p90"])
            flags: list[str] = []

            if used_historical_pay_as_input:
                flags.append(
                    "BLOCKED-BY-POLICY: proposed pay was derived from the candidate's/employee's "
                    "own historical pay. Per pay-equity-governance.md this cannot be used to "
                    "justify a banding decision -- historical pay carries forward historical bias. "
                    "Re-derive the proposed number from role/level/market data only, then re-run."
                )

            if percentile < 25:
                flags.append("Below p25: retention and equity risk if this is an existing employee.")
            if percentile >= 90:
                flags.append("At or above p90: route through your above-band exception process.")

            return BandPosition(
                role_family=row["role_family"],
                level=row["level"],
                location_tier=row["location_tier"],
                base_pay=base_pay,
                band_low=row["p25"],
                band_mid=row["p50"],
                band_high=row["p90"],
                percentile_estimate=percentile,
                band_label=_label_for(percentile),
                flags=flags,
            ).to_dict()

    known = sorted({f"{r['role_family']} / {r['level']} / {r['location_tier']}" for r in _load_bands()})
    raise BandNotFoundError(
        f"No benchmark row for role_family={role_family!r}, level={level!r}, "
        f"location_tier={location_tier!r}. Known combinations: {known}"
    )


def list_known_bands() -> list[dict]:
    """Return the raw benchmark table so an agent can tell a user what's covered
    before attempting a lookup, instead of trial-and-erroring role names."""
    return _load_bands()
