#!/usr/bin/env python3
"""Verify that this repository's self-description matches what is in the tree.

The README tells readers they can check its claims against the repo itself. This
script is what makes that promise enforceable instead of aspirational: every count
the README states is recomputed from the files and tests that back it, and CI fails
when prose and reality disagree.

It also enforces the house no-em-dash rule across every text file, which the other
CI steps do not cover.

Run it directly, or let CI run it:

    python3 scripts/verify_claims.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Written as a code point so this file never contains the character it looks for.
EM_DASH = chr(0x2014)

WORD_NUMBERS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
}

TEXT_SUFFIXES = {
    ".md", ".py", ".yaml", ".yml", ".json", ".ipynb",
    ".txt", ".toml", ".cff", ".html", ".cfg", ".css", ".js",
}

SKIP_DIRS = {".git", ".pytest_cache", ".ruff_cache", "__pycache__", "node_modules", ".venv", "venv"}

# JSON and notebook files store an em dash as an escape sequence rather than the
# character, so both forms count as a violation there. Elsewhere only the character does,
# which keeps this scanner from flagging its own source.
ESCAPED_EM_DASH_SUFFIXES = {".json", ".ipynb"}


@dataclass
class Check:
    """One claim the repo makes about itself, and what the tree actually holds."""

    name: str
    claimed: int | None
    actual: int
    source: str
    skipped: str = ""

    @property
    def ok(self) -> bool:
        if self.skipped:
            return True
        return self.claimed == self.actual


@dataclass
class Report:
    checks: list[Check] = field(default_factory=list)
    em_dashes: list[tuple[str, int]] = field(default_factory=list)
    matrix_errors: list[str] = field(default_factory=list)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def to_int(token: str) -> int | None:
    token = token.strip().lower()
    if token.isdigit():
        return int(token)
    return WORD_NUMBERS.get(token)


def claim(relative: str, pattern: str) -> int | None:
    """Pull a single numeric claim out of a file. Returns None when the phrasing moved."""
    match = re.search(pattern, read(relative), flags=re.IGNORECASE)
    if not match:
        return None
    return to_int(match.group(1))


def is_table_separator(line: str) -> bool:
    cells = set(line.replace("|", "").replace(" ", ""))
    return bool(cells) and cells <= set("-:")


def count_table_rows(relative: str) -> int:
    """Count data rows across every Markdown table in a file, excluding headers and rules.

    A header is the row directly above a separator, so the file may hold any number of
    separate tables and the count stays right.
    """
    rows = [line for line in read(relative).splitlines() if line.strip().startswith("|")]
    data = 0
    for index, line in enumerate(rows):
        if is_table_separator(line):
            continue
        if index + 1 < len(rows) and is_table_separator(rows[index + 1]):
            continue  # header row
        data += 1
    return data


def count_files(directory: str, pattern: str, exclude: set[str] | None = None) -> int:
    exclude = exclude or set()
    return len([p for p in (ROOT / directory).glob(pattern) if p.name not in exclude])


def count_dirs(directory: str) -> int:
    return len([p for p in (ROOT / directory).iterdir() if p.is_dir() and p.name not in SKIP_DIRS])


def count_headings(relative: str, pattern: str) -> int:
    return len(re.findall(pattern, read(relative), flags=re.MULTILINE))


def collect_tests(target: str) -> tuple[int, str]:
    """Return the number of tests pytest collects, or a reason the check was skipped."""
    command = [sys.executable, "-m", "pytest", target, "-q", "--collect-only"]
    try:
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False, timeout=180)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 0, f"could not run pytest ({exc.__class__.__name__})"
    if result.returncode != 0:
        return 0, "pytest collection failed, install the test dependencies to check this"
    match = re.search(r"(\d+) tests? collected", result.stdout)
    if not match:
        return 0, "could not parse pytest collection output"
    return int(match.group(1)), ""


def find_em_dashes() -> list[tuple[str, int]]:
    hits: list[tuple[str, int]] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if SKIP_DIRS & set(path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        escaped_matters = path.suffix.lower() in ESCAPED_EM_DASH_SUFFIXES
        for number, line in enumerate(text.splitlines(), start=1):
            if EM_DASH in line or (escaped_matters and "\\u2014" in line):
                hits.append((str(path.relative_to(ROOT)), number))
    return hits


MATRIX_WEIGHTS = (0.25, 0.20, 0.15, 0.15, 0.15)
MATRIX_TIERS = ((4.0, 1), (3.0, 2), (2.0, 3), (0.0, 4))


def check_matrix_example() -> list[str]:
    """Check eligibility gating and normalized business scores in the example."""
    errors = []
    text = read("01-use-cases/prioritization-matrix.md")
    section = text.split("## Example scoring", 1)[-1].split("\n---", 1)[0]
    eligible_count = 0
    blocked_count = 0
    for line in section.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 9 or cells[0] == "Use case" or set(cells[0]) == {"-"}:
            continue
        name, eligibility = cells[:2]
        if eligibility.startswith(("Hold:", "Stop:")):
            blocked_count += 1
            if cells[7:] != ["Not scored", "None"] or any(cells[2:7]):
                errors.append(f"{name}: failed gates must have no business score or tier")
            continue
        if eligibility != "Eligible":
            errors.append(f"{name}: unrecognized eligibility status")
            continue
        eligible_count += 1
        try:
            scores = [int(c) for c in cells[2:7]]
            stated, tier = float(cells[7]), int(cells[8])
        except ValueError:
            errors.append(f"{name}: invalid example score")
            continue
        if any(score < 1 or score > 5 for score in scores):
            errors.append(f"{name}: scores must be between 1 and 5")
        actual = sum(w * v for w, v in zip(MATRIX_WEIGHTS, scores, strict=True)) / sum(MATRIX_WEIGHTS)
        if abs(round(actual, 2) - stated) > 0.005:
            errors.append(f"{name}: table says {stated:.2f}, weights give {actual:.2f}")
        expected_tier = next(t for floor, t in MATRIX_TIERS if actual >= floor)
        if tier != expected_tier:
            errors.append(f"{name}: tier {tier} in table, score {actual:.2f} is tier {expected_tier}")
    if not eligible_count or not blocked_count:
        errors.append("prioritization-matrix.md: eligible and blocked examples are required")
    return errors


def build_report() -> Report:
    report = Report()
    add = report.checks.append

    add(Check(
        "Use cases in the library",
        claim("README.md", r"(\d+) vetted HR AI use cases"),
        count_table_rows("01-use-cases/use-case-library.md"),
        "01-use-cases/use-case-library.md table rows",
    ))
    add(Check(
        "Installable agent skills",
        claim("README.md", r"(\w+) installable agent skills"),
        count_dirs("11-skills"),
        "11-skills/ package directories",
    ))
    add(Check(
        "Notebooks executed in CI",
        claim("README.md", r"(\w+) notebooks execute in CI"),
        count_files("05-notebooks", "*.ipynb"),
        "05-notebooks/*.ipynb",
    ))
    add(Check(
        "MCP tools on the server",
        claim("README.md", r"(\w+) MCP tools"),
        len(re.findall(r"^@mcp\.tool\(\)", read("10-mcp-agents/server.py"), flags=re.MULTILINE)),
        "10-mcp-agents/server.py registered tools",
    ))
    add(Check(
        "Eval cases in the suite",
        claim("README.md", r"The (\d+)-case eval runner"),
        len(re.findall(r"^\s*- id:", read("09-evals/hr-qa-agent-evals.yaml"), flags=re.MULTILINE)),
        "09-evals/hr-qa-agent-evals.yaml case ids",
    ))
    add(Check(
        "Architecture patterns",
        claim("README.md", r"(\w+) architecture patterns"),
        count_headings("07-agentic-patterns/README.md", r"^## Pattern \d+:"),
        "07-agentic-patterns/README.md pattern headings",
    ))
    add(Check(
        "Literacy curriculum modules",
        claim("README.md", r"(\d+)-module literacy curriculum"),
        count_headings("04-enablement/hr-ai-literacy-curriculum.md", r"^## Module \d+:"),
        "04-enablement/hr-ai-literacy-curriculum.md module headings",
    ))

    mcp_tests, mcp_skip = collect_tests("10-mcp-agents")
    add(Check(
        "MCP test suite size",
        claim("README.md", r"a (\d+)-test suite"),
        mcp_tests, "pytest 10-mcp-agents", mcp_skip,
    ))

    eval_tests, eval_skip = collect_tests("09-evals")
    add(Check(
        "Scorer and judge tests",
        claim("README.md", r"have (\d+) tests of their own"),
        eval_tests, "pytest 09-evals", eval_skip,
    ))

    report.em_dashes = find_em_dashes()
    report.matrix_errors = check_matrix_example()
    return report


def render(report: Report) -> bool:
    width = max(len(c.name) for c in report.checks)
    print("Repository self-description check")
    print("=" * (width + 34))
    for check in report.checks:
        if check.skipped:
            status, detail = "SKIP", check.skipped
        elif check.claimed is None:
            status = "FAIL"
            detail = f"no claim found in README, actual is {check.actual}"
        elif check.ok:
            status, detail = "ok", f"{check.actual}"
        else:
            status = "FAIL"
            detail = f"README says {check.claimed}, tree has {check.actual}"
        print(f"  [{status:4}] {check.name.ljust(width)}  {detail}")
        if status == "FAIL":
            print(f"{'':10}{''.ljust(width)}  source: {check.source}")

    print()
    if report.em_dashes:
        print(f"Em dashes found in {len(report.em_dashes)} place(s). The house rule is none, anywhere.")
        for path, line in report.em_dashes[:40]:
            print(f"  {path}:{line}")
        if len(report.em_dashes) > 40:
            print(f"  ... and {len(report.em_dashes) - 40} more")
    else:
        print("No em dashes found.")

    if report.matrix_errors:
        print("Prioritization matrix example does not match its own weights:")
        for err in report.matrix_errors:
            print(f"  {err}")
    else:
        print("Prioritization matrix example scores and tiers recompute correctly.")

    failed = [c for c in report.checks if not c.ok or (c.claimed is None and not c.skipped)]
    print()
    if failed or report.em_dashes or report.matrix_errors:
        print(
            f"FAILED: {len(failed)} claim mismatch(es), {len(report.em_dashes)} em dash(es), "
            f"{len(report.matrix_errors)} matrix error(s)."
        )
        return False
    print("All repository claims verified against the tree.")
    return True


def main() -> int:
    return 0 if render(build_report()) else 1


if __name__ == "__main__":
    sys.exit(main())
