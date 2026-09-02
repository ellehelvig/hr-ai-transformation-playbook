"""
resume_screen.tool
====================

A bias-mitigated JD-to-resume evidence comparison tool.

This closes a specific, named gap: the main playbook's use-case-library.md
lists "Resume screening and scoring" as high-impact, high-risk, with
mitigation status "None yet." This module is that mitigation, built the way
the governance doc requires it to be built.

The load-bearing design decision: **this tool never produces a score, a
rank, or a recommendation.** Every public function's return schema is
tested (see test_resume_screen.py::test_output_never_contains_a_score) to
guarantee no numeric "match %" or "fit score" field can appear, on purpose
or by accident, in any return value. That is not a missing feature. Scoring
resumes is exactly the failure mode the governance playbook flags as
"bias amplification": a single number launders a hundred small judgment
calls into something that looks objective and isn't. What this tool does
instead:

1. Extracts the stated requirements from a JD (deterministic parsing, not
   an LLM guessing at "what the manager probably meant").
2. For each requirement, reports whether the resume text contains direct
   evidence, partial/adjacent evidence, or none, and shows the evidence
   line so a human can check the tool's work.
3. Separately lints the JD's own language for gendered-coded wording and
   protected-class-proxy phrases (things like "digital native" or "culture
   fit"), because a bias-mitigated screen that only looks at the resume and
   ignores a biased job ad is solving half the problem.

The calling agent's job is to turn this evidence into something a recruiter
reads (a summary, a set of validation questions) -- this module's job is to
make sure that summary is built on visible, checkable evidence rather than
a black-box score.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "bias_terms.json"

_STOPWORDS = {
    "the", "and", "for", "with", "you", "your", "our", "a", "an", "to", "of",
    "in", "on", "is", "are", "will", "be", "or", "as", "at", "by", "this",
    "that", "we", "us", "it", "its", "their", "they", "who", "have", "has",
    "including", "etc", "years", "year", "experience", "ability", "skills",
}


def _load_bias_terms() -> dict:
    with open(DATA_PATH) as f:
        return json.load(f)


def extract_requirements(jd_text: str) -> list[str]:
    """Pull requirement-shaped lines out of a JD.

    Deterministic on purpose: looks for bulleted/dashed lines (the format
    almost every real JD, including the one this was built against, actually
    uses) rather than asking a model to decide what counts as a requirement.
    Falls back to sentence-splitting only if no bullets are found at all, so
    it degrades instead of returning nothing for a plain-paragraph JD.
    """
    bullet_lines = [
        line.strip(" \t-*••").strip()
        for line in jd_text.splitlines()
        if re.match(r"^\s*[-*•]\s+\S", line)
    ]
    bullet_lines = [line for line in bullet_lines if len(line) > 8]
    if bullet_lines:
        return bullet_lines

    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", jd_text) if len(s.strip()) > 12]
    return sentences


def _keywords(text: str, min_len: int = 4) -> set[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z\-]+", text.lower())
    return {w for w in words if len(w) >= min_len and w not in _STOPWORDS}


def _evidence_for_requirement(requirement: str, resume_lines: list[str]) -> dict:
    req_keywords = _keywords(requirement)
    if not req_keywords:
        return {"requirement": requirement, "status": "no_evidence_found", "evidence_line": None, "matched_terms": []}

    # Coverage against the whole resume (a requirement's keywords rarely all
    # land in one bullet; a resume paraphrases, it doesn't quote the JD back).
    # We still track the single best-matching line separately so a human has
    # something concrete to check the tool's work against.
    whole_resume_keywords = set()
    for line in resume_lines:
        whole_resume_keywords |= _keywords(line)
    overall_overlap = req_keywords & whole_resume_keywords
    coverage = len(overall_overlap) / len(req_keywords) if req_keywords else 0.0

    best_line = None
    best_line_overlap: set[str] = set()
    for line in resume_lines:
        line_keywords = _keywords(line)
        overlap = req_keywords & line_keywords
        if len(overlap) > len(best_line_overlap):
            best_line_overlap = overlap
            best_line = line

    if coverage >= 0.4:
        status = "evidence_found"
    elif coverage > 0:
        status = "partial_evidence_unconfirmed"
    else:
        status = "no_evidence_found"

    return {
        "requirement": requirement,
        "status": status,
        "evidence_line": best_line if best_line_overlap else None,
        "matched_terms": sorted(overall_overlap),
    }


def compare_to_resume(jd_text: str, resume_text: str) -> dict:
    """Map each JD requirement to evidence (or its absence) in a resume.

    Returns per-requirement evidence plus counts. Deliberately no aggregate
    score. `unconfirmed_count` and `no_evidence_count` exist so an agent can
    say "6 of 9 requirements need validation with the candidate" without a
    single number standing in for "should we move forward."
    """
    requirements = extract_requirements(jd_text)
    resume_lines = [l.strip() for l in resume_text.splitlines() if l.strip()]

    results = [_evidence_for_requirement(req, resume_lines) for req in requirements]

    return {
        "requirement_count": len(results),
        "evidence": results,
        "evidence_found_count": sum(1 for r in results if r["status"] == "evidence_found"),
        "partial_evidence_count": sum(1 for r in results if r["status"] == "partial_evidence_unconfirmed"),
        "no_evidence_count": sum(1 for r in results if r["status"] == "no_evidence_found"),
        "human_review_required": True,
        "note": (
            "This is an evidence map, not a score or a recommendation. 'No evidence found' "
            "means the resume text doesn't mention it, not that the candidate lacks it -- "
            "confirm gaps with the candidate before screening anyone out. See "
            "03-governance/ai-use-policy.md, principle 3."
        ),
    }


def lint_bias_language(text: str) -> dict:
    """Scan JD (or any HR-facing) text for gendered-coded wording and
    protected-class-proxy phrases. Returns matches with severity, doesn't
    auto-edit the text -- rewriting someone's JD without them seeing the
    diff is its own kind of failure mode."""
    terms = _load_bias_terms()
    lowered = text.lower()

    def _find(term_list: list[str], category: str, severity: str) -> list[dict]:
        hits = []
        for term in term_list:
            if re.search(r"\b" + re.escape(term) + r"\b", lowered):
                hits.append({"term": term, "category": category, "severity": severity})
        return hits

    matches = (
        _find(terms["masculine_coded"], "gendered_wording_masculine", "advisory")
        + _find(terms["feminine_coded"], "gendered_wording_feminine", "advisory")
        + _find(terms["protected_class_proxy"], "protected_class_proxy", "high")
    )

    return {
        "matches": matches,
        "high_severity_count": sum(1 for m in matches if m["severity"] == "high"),
        "advisory_count": sum(1 for m in matches if m["severity"] == "advisory"),
        "note": (
            "Advisory-severity hits are gendered-coded wording research links to skewed "
            "applicant pools (Gaucher, Friesen & Kay 2011), not a legal violation -- reword "
            "at your discretion. High-severity hits are phrases that proxy for a protected "
            "characteristic (age, national origin, etc.) and should almost always be removed "
            "or routed to Legal before the req goes live."
        ),
    }


def screen_candidate(jd_text: str, resume_text: str) -> dict:
    """Convenience wrapper: evidence comparison plus a JD bias lint in one call."""
    return {
        "evidence_comparison": compare_to_resume(jd_text, resume_text),
        "jd_language_check": lint_bias_language(jd_text),
        "human_review_required": True,
    }
