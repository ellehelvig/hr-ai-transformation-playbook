"""Structure checks for the HR function and starter skills: sections, worked example, and test cases.

These checks do not run any skill against a model. They confirm that every
function skill carries the parts an agent and a reviewer rely on, and that its
test cases are laid out the way `claude plugin eval` reads them.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

SKILLS_DIR = Path(__file__).resolve().parent.parent / "11-skills"
FUNCTION_SKILLS = sorted(p for p in SKILLS_DIR.glob("function-*") if p.is_dir())
STARTER_SKILLS = [SKILLS_DIR / "hr-ai-readiness-assessment", SKILLS_DIR / "hr-ai-first-use-case-picker"]
STRUCTURED_SKILLS = FUNCTION_SKILLS + STARTER_SKILLS
ALL_SKILLS = sorted(p for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").is_file())

REQUIRED_SECTIONS = [
    "## Inputs",
    "## Tools and connectors",
    "## By maturity stage",
    "## Steps",
    "## Decision rights",
    "## Guardrails",
    "## Regulation map",
    "## Metrics a CHRO tracks",
    "## Output format",
    "## Worked example",
    "## Tests",
    "## Sources",
]
AGENT_ROLES = {"Does alone", "Drafts for sign-off", "Refuses and routes"}
CASE_NAME = re.compile(r"^[a-z][a-z0-9-]*$")
GRADER_HEADER = re.compile(r"\A---\ntype: llm\nfocus: trace\nweight: 1\n---\n\n\S")


def _section(text: str, heading: str) -> str:
    """Text from a required heading up to the next required heading.

    Required headings are used as the boundaries, so the ## lines inside the
    fenced output template do not cut a section short.
    """
    start = text.index(heading) + len(heading)
    later = REQUIRED_SECTIONS[REQUIRED_SECTIONS.index(heading) + 1:]
    ends = [text.index(h, start) for h in later if h in text[start:]]
    return text[start: min(ends)] if ends else text[start:]


def test_there_are_seventeen_function_skills_and_two_starter_skills():
    assert len(FUNCTION_SKILLS) == 17
    assert all((skill / "SKILL.md").is_file() for skill in STARTER_SKILLS)


def test_every_skill_has_a_maturity_stage_section():
    stages = ("Start (Levels 0 to 1)", "Pilot (Level 2)", "Scale (Level 3)", "Embed (Levels 4 to 5)")
    for skill in ALL_SKILLS:
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        assert "## By maturity stage" in text, f"{skill.name}: no maturity section"
        section = text.split("## By maturity stage", 1)[1].split("\n## ", 1)[0]
        assert all(stage in section for stage in stages), f"{skill.name}: missing a stage row"
        assert "transformation-roadmap-template.md" in section, f"{skill.name}: maturity scale not linked"


def test_every_function_skill_has_the_required_sections_in_order():
    for skill in STRUCTURED_SKILLS:
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        front = yaml.safe_load(text.split("---")[1])
        assert front["name"] == skill.name, f"{skill.name}: name does not match folder"
        assert len(front["description"]) <= 1024, f"{skill.name}: description over 1,024 characters"
        assert len(text.splitlines()) < 500, f"{skill.name}: SKILL.md over 500 lines"
        positions = []
        for heading in REQUIRED_SECTIONS:
            assert heading in text, f"{skill.name}: missing {heading}"
            positions.append(text.index(heading))
        assert positions == sorted(positions), f"{skill.name}: sections out of order"

        rights = _section(text, "## Decision rights")
        roles = {cell.strip() for row in rights.splitlines() if row.startswith("|") for cell in row.split("|")}
        assert roles & AGENT_ROLES == AGENT_ROLES, f"{skill.name}: decision rights need all three agent roles"
        assert "### Refuse and route" in rights, f"{skill.name}: no refuse-and-route list"

        metrics = _section(text, "## Metrics a CHRO tracks")
        metric_rows = [r for r in metrics.splitlines() if r.startswith("|") and "---" not in r][1:]
        assert 2 <= len(metric_rows) <= 3, f"{skill.name}: needs two or three metrics"

        assert "## Audit trail" in _section(text, "## Output format"), f"{skill.name}: no audit trail block"
        assert "(EXAMPLE.md)" in _section(text, "## Worked example"), f"{skill.name}: example not linked"


def test_every_function_skill_has_a_synthetic_worked_example():
    for skill in STRUCTURED_SKILLS:
        example = skill / "EXAMPLE.md"
        assert example.is_file(), f"{skill.name}: no EXAMPLE.md"
        text = example.read_text(encoding="utf-8")
        assert "synthetic" in text.lower(), f"{skill.name}: example not labeled synthetic"
        assert len(text.split()) <= 600, f"{skill.name}: example too long"


def test_every_function_skill_has_three_loadable_test_cases():
    for skill in STRUCTURED_SKILLS:
        cases = sorted(p for p in (skill / "evals").iterdir() if p.is_dir())
        assert len(cases) == 3, f"{skill.name}: expected three test cases"
        for case in cases:
            label = f"{skill.name}/{case.name}"
            assert CASE_NAME.match(case.name), f"{label}: bad case name"

            prompt = (case / "prompt.md").read_text(encoding="utf-8")
            assert prompt.startswith("---\n"), f"{label}: prompt.md has no settings block"
            settings_text, body = prompt[4:].split("\n---\n", 1)
            settings = yaml.safe_load(settings_text)
            assert set(settings) <= {"tags", "max_turns", "timeout_seconds", "allowed_tools"}, label
            assert body.strip(), f"{label}: empty prompt"

            meta = yaml.safe_load((case / "case.yaml").read_text(encoding="utf-8"))
            assert meta["schema_version"] == "1.1", label
            assert meta["name"] == case.name, label
            assert meta["expected_outcome"].strip(), label

            graders = sorted((case / "graders").glob("*.md"))
            assert 3 <= len(graders) <= 4, f"{label}: expected three or four graders"
            for grader in graders:
                assert GRADER_HEADER.match(grader.read_text(encoding="utf-8")), f"{grader}: bad header"


def _adverse_impact():
    import importlib.util

    path = SKILLS_DIR / "fairness-audit-prep" / "scripts" / "adverse_impact.py"
    spec = importlib.util.spec_from_file_location("adverse_impact", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["adverse_impact"] = module
    spec.loader.exec_module(module)
    return module


def test_fisher_exact_matches_a_known_value():
    # Classic 2x2 table [[1, 9], [11, 3]]: two-sided p = 0.0027594...
    assert abs(_adverse_impact().fisher_exact_two_sided(1, 9, 11, 3) - 0.0027594) < 1e-6


def test_impact_ratio_flags_a_group_under_four_fifths():
    rows = [
        {"group": "A", "considered": "120", "selected": "48"},
        {"group": "B", "considered": "80", "selected": "20"},
    ]
    results = {r.group: r for r in _adverse_impact().analyze(rows)}
    assert results["A"].impact_ratio == 1.0 and not results["A"].flagged
    assert abs(results["B"].impact_ratio - 0.625) < 1e-9 and results["B"].flagged


def test_adverse_impact_rejects_impossible_counts():
    import pytest

    with pytest.raises(ValueError):
        _adverse_impact().analyze(
            [{"group": "A", "considered": "10", "selected": "11"}, {"group": "B", "considered": "5", "selected": "1"}]
        )
