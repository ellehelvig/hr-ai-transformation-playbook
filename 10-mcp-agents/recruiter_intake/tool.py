"""
recruiter_intake.tool
=======================

Turns a raw hiring-manager intake into a structured role calibration: skill
buckets, a working Boolean search string, and clarifying questions for the
gaps the intake left open. This closes the "hiring manager intake" workflow
gap: recruiters currently rebuild this by hand per req, which is exactly
the kind of repeated, mechanical translation work an agent should own so
the recruiter's time goes to the parts that need judgment (the actual
sourcing and candidate conversations).

Design note on scope: this module does the structuring and the Boolean
string generation, both deterministic, testable, and independent of any
one candidate's data. It does NOT draft outreach messages or make sourcing
decisions, those need real judgment about a real market and belong with
the calling agent (and ultimately the recruiter), not hardcoded here.
"""

from __future__ import annotations

import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "skill_synonyms.json"


def _load_synonyms() -> dict:
    with open(DATA_PATH) as f:
        return json.load(f)


def _boolean_term(skill: str, synonyms: dict) -> str:
    """Build one OR-clause for a skill, expanding known synonyms. Unknown
    skills still work, just without expansion, so the tool never blocks on
    a skill it hasn't seen before."""
    key = skill.strip().lower()
    variants = [skill.strip()] + synonyms.get(key, [])
    quoted = [f'"{v}"' if " " in v else v for v in variants]
    if len(quoted) == 1:
        return quoted[0]
    return "(" + " OR ".join(quoted) + ")"


def build_boolean_string(must_haves: list[str], nice_to_haves: list[str] | None = None) -> str:
    """AND together must-haves (each internally OR'd with synonyms); nice-to-haves
    are appended as an OR'd optional block rather than ANDed in, an optional
    skill that's ANDed into the query is the single most common way a Boolean
    string accidentally filters out a perfectly good candidate."""
    synonyms = _load_synonyms()
    if not must_haves:
        raise ValueError("build_boolean_string requires at least one must-have skill")

    must_clause = " AND ".join(_boolean_term(s, synonyms) for s in must_haves)
    if nice_to_haves:
        nice_clause = " OR ".join(_boolean_term(s, synonyms) for s in nice_to_haves)
        return f"{must_clause} AND ({nice_clause})"
    return must_clause


def generate_clarifying_questions(intake: dict) -> list[str]:
    """Rule-based gap detection on a raw intake payload. Every question here
    maps to a real failure mode we've seen: too many 'must haves' silently
    filters out strong candidates, a missing disqualifier list means the
    recruiter improvises one per candidate, and so on."""
    questions: list[str] = []

    must_haves = intake.get("must_haves") or []
    nice_to_haves = intake.get("nice_to_haves") or []
    trainable = intake.get("trainable") or []
    disqualifiers = intake.get("disqualifiers") or []
    day_in_the_life = (intake.get("day_in_the_life") or "").strip()

    if len(must_haves) > 6:
        questions.append(
            f"You listed {len(must_haves)} must-haves. More than ~6 non-negotiables usually "
            "means some of these are actually nice-to-haves or trainable, which skill can this "
            "person NOT do on day one without it being disqualifying?"
        )
    if not must_haves:
        questions.append("No must-have skills were listed, what's truly non-negotiable for this role?")
    if not disqualifiers:
        questions.append(
            "No disqualifiers listed. Is there anything that should auto-exclude a candidate "
            "regardless of their skills (e.g., a licensing requirement, a background check flag)?"
        )
    if not trainable:
        questions.append(
            "No trainable skills listed, are any of the nice-to-haves things a strong hire could "
            "pick up in their first 90 days? Naming these widens the sourcing pool."
        )
    if not day_in_the_life:
        questions.append(
            "No 'day in the life' description provided. This is what turns into role-learning "
            "material for the recruiting team, a few sentences on a typical week would help."
        )
    overlap = set(s.lower() for s in must_haves) & set(s.lower() for s in nice_to_haves)
    if overlap:
        questions.append(
            f"These appear in both must-haves and nice-to-haves: {sorted(overlap)}. Pick one list."
        )

    return questions


def build_calibration_doc(intake: dict) -> dict:
    """Full calibration output: skill buckets, Boolean string, clarifying
    questions, all in one payload ready to hand to a recruiter."""
    must_haves = intake.get("must_haves") or []
    nice_to_haves = intake.get("nice_to_haves") or []
    trainable = intake.get("trainable") or []

    boolean_string = None
    boolean_error = None
    try:
        boolean_string = build_boolean_string(must_haves, nice_to_haves)
    except ValueError as e:
        boolean_error = str(e)

    return {
        "job_title": intake.get("job_title", "(untitled)"),
        "skill_buckets": {
            "must_have": must_haves,
            "nice_to_have": nice_to_haves,
            "trainable": trainable,
        },
        "disqualifiers": intake.get("disqualifiers") or [],
        "day_in_the_life": intake.get("day_in_the_life", ""),
        "boolean_string": boolean_string,
        "boolean_string_error": boolean_error,
        "clarifying_questions": generate_clarifying_questions(intake),
        "human_review_required": True,
        "note": (
            "Recruiter validates the Boolean string against a live search before using it, and "
            "confirms this calibration with the hiring manager before sourcing begins. This "
            "document is a hypothesis to validate, not a finished spec."
        ),
    }
