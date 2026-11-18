"""Selection rates, impact ratios, and an exact test from group counts.

Input is a CSV of aggregate counts, one row per group, with the columns
group, considered, selected. No individual records go in, and nothing is
written anywhere. Output is a Markdown table for the analyst.

The impact ratio compares each group's selection rate with the highest
group rate. A ratio under 0.80 is the screening flag described in the
Uniform Guidelines, 29 CFR 1607.4(D). It is a rule of thumb, not a legal
finding: the same provision says small differences can matter in large
samples and large differences may not be significant in small ones. So the
script also reports a two-sided Fisher exact p-value for each group against
the highest-rate group. People Analytics or counsel interprets the result.

Usage: python adverse_impact.py counts.csv
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from math import comb
from pathlib import Path

FOUR_FIFTHS = 0.80


@dataclass
class GroupResult:
    group: str
    considered: int
    selected: int
    rate: float
    impact_ratio: float
    p_value: float
    flagged: bool


def fisher_exact_two_sided(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact p-value for the 2x2 table [[a, b], [c, d]]."""
    row1, row2, col1 = a + b, c + d, a + c
    total = row1 + row2
    denom = comb(total, col1)

    def prob(x: int) -> float:
        return comb(row1, x) * comb(row2, col1 - x) / denom

    observed = prob(a)
    low, high = max(0, col1 - row2), min(row1, col1)
    p = sum(prob(x) for x in range(low, high + 1) if prob(x) <= observed * (1 + 1e-9))
    return min(1.0, p)


def analyze(rows: list[dict[str, str]]) -> list[GroupResult]:
    counts = []
    for row in rows:
        considered, selected = int(row["considered"]), int(row["selected"])
        if considered <= 0 or not 0 <= selected <= considered:
            raise ValueError(f"group {row['group']!r}: need 0 <= selected <= considered and considered > 0")
        counts.append((row["group"].strip(), considered, selected))
    if len(counts) < 2:
        raise ValueError("need at least two groups")

    ref_group, ref_n, ref_sel = max(counts, key=lambda c: c[2] / c[1])
    ref_rate = ref_sel / ref_n
    if ref_rate == 0:
        raise ValueError("no group has any selections, so impact ratios are undefined")

    results = []
    for group, n, sel in counts:
        rate = sel / n
        ratio = rate / ref_rate
        p = 1.0 if group == ref_group else fisher_exact_two_sided(sel, n - sel, ref_sel, ref_n - ref_sel)
        results.append(GroupResult(group, n, sel, rate, ratio, p, ratio < FOUR_FIFTHS))
    return results


def to_markdown(results: list[GroupResult]) -> str:
    lines = [
        "| Group | Considered | Selected | Selection rate | Impact ratio | Under 0.80 | Fisher p vs highest |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in results:
        lines.append(
            f"| {r.group} | {r.considered} | {r.selected} | {r.rate:.3f} | {r.impact_ratio:.2f} | "
            f"{'yes' if r.flagged else 'no'} | {r.p_value:.3f} |"
        )
    lines.append("")
    lines.append(
        "Screening output only. A flag is a reason to look, not a finding. "
        "People Analytics or counsel interprets the result before anyone acts on it."
    )
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[-1])
        return 2
    with Path(argv[1]).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    print(to_markdown(analyze(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
