import importlib.util as _ilu
from pathlib import Path as _Path

import pytest

# Loaded by explicit file path -- see comp_banding/test_comp_banding.py for why.
_spec = _ilu.spec_from_file_location(f"_local_tool_{__name__}", _Path(__file__).parent / "tool.py")
tool = _ilu.module_from_spec(_spec)
import sys as _sys
_sys.modules[_spec.name] = tool
_spec.loader.exec_module(tool)

SAMPLE_INTAKE = {
    "job_title": "AI Solutions Engineer, People & Culture",
    "must_haves": ["mcp", "agent development", "python"],
    "nice_to_haves": ["compensation analysis", "change management"],
    "trainable": ["hris"],
    "disqualifiers": ["No prior hands-on AI agent building"],
    "day_in_the_life": "Pairs with SMEs to design and ship agents, monitors adoption, runs evals.",
}


def test_boolean_string_expands_known_synonyms():
    result = tool.build_boolean_string(["mcp"])
    assert "model context protocol" in result.lower()


def test_boolean_string_ands_must_haves_ors_nice_to_haves():
    result = tool.build_boolean_string(["python", "mcp"], nice_to_haves=["hris"])
    assert " AND " in result
    assert result.strip().endswith(")")


def test_unknown_skill_still_works_without_expansion():
    result = tool.build_boolean_string(["some totally new skill nobody catalogued"])
    assert "totally new skill" in result.lower()


def test_boolean_string_requires_at_least_one_must_have():
    with pytest.raises(ValueError):
        tool.build_boolean_string([])


def test_too_many_must_haves_triggers_clarifying_question():
    intake = {**SAMPLE_INTAKE, "must_haves": ["a", "b", "c", "d", "e", "f", "g", "h"]}
    questions = tool.generate_clarifying_questions(intake)
    assert any("more than" in q.lower() for q in questions)


def test_missing_disqualifiers_triggers_question():
    intake = {**SAMPLE_INTAKE, "disqualifiers": []}
    questions = tool.generate_clarifying_questions(intake)
    assert any("disqualif" in q.lower() for q in questions)


def test_missing_day_in_the_life_triggers_question():
    intake = {**SAMPLE_INTAKE, "day_in_the_life": ""}
    questions = tool.generate_clarifying_questions(intake)
    assert any("day in the life" in q.lower() for q in questions)


def test_overlapping_must_and_nice_flagged():
    intake = {**SAMPLE_INTAKE, "must_haves": ["python"], "nice_to_haves": ["python"]}
    questions = tool.generate_clarifying_questions(intake)
    assert any("both must-haves and nice-to-haves" in q for q in questions)


def test_well_formed_intake_has_fewer_questions():
    minimal_gaps = tool.generate_clarifying_questions(SAMPLE_INTAKE)
    sparse_intake = {"job_title": "Recruiter"}
    many_gaps = tool.generate_clarifying_questions(sparse_intake)
    assert len(many_gaps) > len(minimal_gaps)


def test_calibration_doc_always_flags_human_review():
    doc = tool.build_calibration_doc(SAMPLE_INTAKE)
    assert doc["human_review_required"] is True
    assert doc["boolean_string"] is not None
    assert doc["boolean_string_error"] is None


def test_calibration_doc_handles_empty_intake_gracefully():
    doc = tool.build_calibration_doc({})
    assert doc["boolean_string"] is None
    assert doc["boolean_string_error"] is not None
    assert len(doc["clarifying_questions"]) > 0
