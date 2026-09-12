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
   derived from the candidate's own prior salary, the tool refuses the lookup
   outright. This encodes the playbook rule: "Using employee compensation
   history to train or fine-tune a model: Not approved." Historical pay
   reflects historical bias; a banding tool that quietly launders that number
   back into "market-aligned" is exactly the failure mode the governance doc
   warns about.

   Two things about this parameter changed after review, both because the
   original version did not do what this docstring said it did:

   - It has **no default**. It used to default to False, which meant the
     guardrail was off unless the calling agent volunteered that it had used
     prohibited input. A control that depends on the caller self-incriminating
     is not a control. Now the caller must answer the question to use the tool
     at all, and FastMCP surfaces it as a required argument, so the model sees
     it on every call.
   - It **refuses** rather than annotating. It used to append a
     BLOCKED-BY-POLICY string to `flags` and then return the full band
     position, percentile included, so "blocked" was advisory and an agent
     that ignored one list element got the answer anyway. Now the refusal path
     returns a distinct payload with no percentile, no band edges, and no
     band label. There is nothing to quote.
2. The response never returns a bare go/no-go. It always returns enough
   context (percentile, band edges, flag) for a human to make the call,
   and always carries a `human_review_required` field set to True. There is
   no code path that sets it to False. See ADOPTION-MONITORING.md for how
   that invariant gets checked in production, not just in this file.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "comp_bands.json"


class BandNotFoundError(ValueError):
    """Raised when no benchmark row matches the requested role/level/tier."""


HISTORICAL_PAY_REFUSAL_CODE = "REFUSED_HISTORICAL_PAY_INPUT"

_HISTORICAL_PAY_REFUSAL_REASON = (
    "Refused: the proposed pay was derived from the candidate's or employee's own pay "
    "history. Per 03-governance/pay-equity-governance.md, historical pay cannot be used "
    "to justify a banding decision, because it carries forward whatever bias produced "
    "that history. This tool will not return a market position for such a number. "
    "Re-derive the proposed pay from role, level, and market data only, then call again "
    "with used_historical_pay_as_input=False."
)


def _historical_pay_refusal(role_family: str, level: str, location_tier: str) -> dict:
    """The refusal payload. Deliberately carries no percentile, no band edges,
    and no band label: a refusal that still hands over the number it refused to
    bless is not a refusal. Echoes back only the non-sensitive lookup keys so
    the agent can tell which call was refused."""
    return {
        "refused": True,
        "refusal_code": HISTORICAL_PAY_REFUSAL_CODE,
        "reason": _HISTORICAL_PAY_REFUSAL_REASON,
        "role_family": role_family,
        "level": level,
        "location_tier": location_tier,
        "human_review_required": True,
        "remediation": (
            "Ask the hiring manager or comp partner for a proposed number sourced from the "
            "band itself rather than from the candidate's current or prior salary. Many "
            "jurisdictions also restrict asking for salary history at all."
        ),
    }


@dataclass
class BandPosition:
    role_family: str
    level: str
    location_tier: str
    base_pay: float
    band_low: float
    band_mid: float
    band_high: float
    band_p75: float
    percentile_estimate: float | None
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
            "refused": False,
            "band_low_p25": self.band_low,
            "band_mid_p50": self.band_mid,
            "band_p75": self.band_p75,
            "band_high_p90": self.band_high,
            "percentile_estimate": self.percentile_estimate,
            "percentile_estimate_note": (
                "Null means the pay falls outside the p25-to-p90 benchmark range, so no "
                "percentile can be estimated from the four available benchmark points. "
                "Read band_label and flags for the direction."
                if self.percentile_estimate is None
                else "Interpolated between benchmark points; precision is limited by having "
                "only p25, p50, p75, and p90."
            ),
            "band_label": self.band_label,
            "flags": self.flags,
            "human_review_required": self.human_review_required,
            "disclaimer": self.disclaimer,
        }


@lru_cache(maxsize=1)
def _load_bands_cached(mtime_ns: int) -> tuple[dict, ...]:
    """Parse the benchmark table once. Keyed on the file's mtime so editing
    comp_bands.json during a session still takes effect, which matters because
    the enablement path for this tool is a comp analyst opening that JSON and
    pasting in their own survey data. Returns a tuple of dicts; callers treat
    it as read-only."""
    with open(DATA_PATH) as f:
        payload = json.load(f)
    bands = payload["bands"]
    required = {"role_family", "level", "location_tier", "p25", "p50", "p75", "p90"}
    for i, row in enumerate(bands):
        missing = required - row.keys()
        if missing:
            raise ValueError(
                f"comp_bands.json row {i} is missing required key(s): {sorted(missing)}. "
                f"Every row needs {sorted(required)}."
            )
        if not (row["p25"] <= row["p50"] <= row["p75"] <= row["p90"]):
            raise ValueError(
                f"comp_bands.json row {i} ({row['role_family']} / {row['level']} / "
                f"{row['location_tier']}) has non-monotonic percentiles: "
                f"p25={row['p25']}, p50={row['p50']}, p75={row['p75']}, p90={row['p90']}. "
                "Percentiles must be non-decreasing, otherwise interpolation is meaningless."
            )
    return tuple(bands)


def _load_bands() -> list[dict]:
    return list(_load_bands_cached(DATA_PATH.stat().st_mtime_ns))


def _interpolate_percentile(
    base_pay: float, p25: float, p50: float, p75: float, p90: float
) -> float | None:
    """Piecewise-linear percentile estimate between known benchmark points, or
    None when the pay sits outside them.

    Returns None rather than a number below p25 or above p90. The previous
    version anchored the ends at `p25 * 0.7` for the 1st percentile and
    `p90 * 1.25` for the 99th, then interpolated into those anchors. Those two
    multipliers were invented. They have no basis in the benchmark data, which
    contains only p25, p50, p75, and p90, and they produced confident-looking
    numbers like "8th percentile" that were artifacts of the constant 0.7.

    That mattered because, as the module docstring notes, this number gets
    quoted in conversations with candidates. Saying "below p25, outside the
    benchmark range" is honest and equally actionable. Saying "8th percentile"
    invents precision the data cannot support. Callers must handle None; the
    band_label and flags still tell them which direction it fell.
    """
    points = [(25.0, p25), (50.0, p50), (75.0, p75), (90.0, p90)]
    if base_pay < p25 or base_pay > p90:
        return None
    for (pct_a, pay_a), (pct_b, pay_b) in zip(points, points[1:], strict=True):
        if pay_a <= base_pay <= pay_b:
            if pay_b == pay_a:
                return pct_a
            frac = (base_pay - pay_a) / (pay_b - pay_a)
            return round(pct_a + frac * (pct_b - pct_a), 1)
    return None


def _label_for(percentile: float | None, base_pay: float, p25: float, p90: float) -> str:
    """Label the position. Handles the None percentile that
    _interpolate_percentile now returns for pay outside p25..p90 by using the
    band edges directly, which is where the label came from in substance
    anyway."""
    if percentile is None:
        return "below-range" if base_pay < p25 else "above-range"
    if percentile < 50:
        return "low-range"
    if percentile < 75:
        return "mid-range"
    return "high-range"


def get_band_position(
    role_family: str,
    level: str,
    location_tier: str,
    base_pay: float,
    used_historical_pay_as_input: bool,
) -> dict:
    """Look up market position for a proposed base pay against illustrative
    benchmark bands.

    `used_historical_pay_as_input` is required, not optional. Answer it
    honestly: True if the proposed number was derived in any part from the
    person's current or prior salary. True returns a refusal with no market
    position in it.

    Raises BandNotFoundError if role_family/level/location_tier has no
    benchmark row -- callers (including the calling agent) must not
    silently fall back to a "closest match"; an unmatched role should be
    surfaced for a human to source real benchmark data, not guessed at.
    """
    # Checked before the band lookup and before base_pay validation, so a
    # refused call never touches benchmark data and never reveals whether the
    # role/level combination exists.
    if used_historical_pay_as_input:
        return _historical_pay_refusal(role_family, level, location_tier)

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

            # Flag off the band edges, not off the percentile. The percentile is
            # None outside p25..p90, which is exactly where these two flags need
            # to fire, so keying them to the percentile would silently drop the
            # flags in the only cases that warrant escalation.
            if base_pay < row["p25"]:
                flags.append("Below p25: retention and equity risk if this is an existing employee.")
            if base_pay > row["p90"]:
                flags.append("At or above p90: route through your above-band exception process.")

            return BandPosition(
                role_family=row["role_family"],
                level=row["level"],
                location_tier=row["location_tier"],
                base_pay=base_pay,
                band_low=row["p25"],
                band_mid=row["p50"],
                band_p75=row["p75"],
                band_high=row["p90"],
                percentile_estimate=percentile,
                band_label=_label_for(percentile, base_pay, row["p25"], row["p90"]),
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
