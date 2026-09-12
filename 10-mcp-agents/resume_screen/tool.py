"""
resume_screen.tool
====================

A bias-mitigated JD-to-resume evidence comparison tool.

This closes a specific, named gap: the main playbook's use-case-library.md
lists "Resume screening and scoring" as high-impact, high-risk, with
mitigation status "None yet." This module is that mitigation, built the way
the governance doc requires it to be built.

The load-bearing design decision: **this tool emits no single number
representing candidate fitness, and never ranks candidates against each
other.** Scoring resumes is the failure mode the governance playbook flags as
"bias amplification": a single number launders a hundred small judgment calls
into something that looks objective and isn't.

Note the precise wording, which is narrower than what this docstring used to
claim. It used to say the tool "never produces a score," enforced by a test
asserting no field name matches /score|rank|fit_percent/. That test passes and
the guarantee does not hold, because the response carries per-status counts and
a requirement count, and dividing one by the other yields a match percentage.
No schema can stop an agent from doing arithmetic. The enforceable subset now
lives in ENFORCED_GUARANTEES, each item verified behaviorally in
test_resume_screen.py, and what a schema cannot prevent lives in
KNOWN_LIMITATIONS. Both ship in every response.

What this tool does:

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
from functools import lru_cache
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "bias_terms.json"
TECHNICAL_TERMS_PATH = Path(__file__).parent / "data" / "technical_terms.json"

_STOPWORDS = {
    "the", "and", "for", "with", "you", "your", "our", "a", "an", "to", "of",
    "in", "on", "is", "are", "will", "be", "or", "as", "at", "by", "this",
    "that", "we", "us", "it", "its", "their", "they", "who", "have", "has",
    "including", "etc", "years", "year", "experience", "ability", "skills",
}


@lru_cache(maxsize=1)
def _load_bias_terms() -> dict:
    with open(DATA_PATH) as f:
        return json.load(f)


@lru_cache(maxsize=1)
def _load_technical_terms() -> tuple[frozenset[str], tuple[str, ...]]:
    """Short and punctuated technical tokens that bypass the length floor.

    Returns (short_terms, punctuated_patterns). Punctuated terms are returned
    as a length-sorted tuple so longer terms match first: without that,
    scanning for "c#" inside "c#/.net" is fine, but scanning for "c" before
    "c++" would consume the "c" and leave "++" unmatched.
    """
    with open(TECHNICAL_TERMS_PATH) as f:
        payload = json.load(f)
    short = frozenset(t.lower() for t in payload["short_technical_terms"])
    punctuated = tuple(
        sorted((t.lower() for t in payload["punctuated_technical_terms"]), key=len, reverse=True)
    )
    return short, punctuated


def extract_requirements(jd_text: str) -> list[str]:
    """Pull requirement-shaped lines out of a JD.

    Deterministic on purpose: looks for bulleted/dashed lines (the format
    almost every real JD, including the one this was built against, actually
    uses) rather than asking a model to decide what counts as a requirement.
    Falls back to sentence-splitting only if no bullets are found at all, so
    it degrades instead of returning nothing for a plain-paragraph JD.
    """
    bullet_lines = [
        line.lstrip(" \t-*•").strip()
        for line in jd_text.splitlines()
        if re.match(r"^\s*[-*•]\s+\S", line)
    ]
    bullet_lines = [line for line in bullet_lines if len(line) > 8]
    if bullet_lines:
        return bullet_lines

    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", jd_text) if len(s.strip()) > 12]
    return sentences


def _keywords(text: str, min_len: int = 4) -> set[str]:
    """Extract comparable terms from text.

    Ordinary words need `min_len` characters, because 2 and 3 character English
    words are noise. Technical tokens are exempt, in two passes:

    1. Punctuated terms (c++, c#, .net, ci/cd, node.js) are matched first and
       removed from the text, because the general word regex cannot represent
       them: `[a-zA-Z][a-zA-Z\\-]+` reads "c++" as nothing and "node.js" as two
       separate words.
    2. Short alphabetic terms on the allowlist (sql, aws, mcp, go, r, ai) are
       kept even though they fall under the floor.

    Without these exemptions the extractor silently dropped every technical
    acronym, and a resume reading "built SQL pipelines on AWS" produced zero
    matches against a JD requiring "experience with SQL and AWS". A screening
    tool that reports no evidence for a qualified candidate is worse than no
    tool, so this is a correctness fix, not a tuning preference. See
    data/technical_terms.json to extend the lists.
    """
    short_terms, punctuated_terms = _load_technical_terms()
    lowered = text.lower()

    found: set[str] = set()

    # Pass 1: punctuated technical terms, longest first, consuming as we go.
    for term in punctuated_terms:
        pattern = r"(?<![\w.#+/-])" + re.escape(term) + r"(?![\w.#+/-])"
        if re.search(pattern, lowered):
            found.add(term)
            lowered = re.sub(pattern, " ", lowered)

    # Pass 2: ordinary words, with the allowlist exempt from the length floor.
    words = re.findall(r"[a-zA-Z][a-zA-Z\-]*", lowered)
    for word in words:
        if word in _STOPWORDS:
            continue
        if len(word) >= min_len or word in short_terms:
            found.add(word)

    return found


# Confirmed-evidence threshold
# ---------------------------------
# A requirement counts as confirmed when at least this share of its comparable
# terms appear somewhere in the resume. 0.4 is a deliberate choice, not a tuned
# value, and it is set by the shape of the inputs rather than by optimization:
# a typical requirement bullet yields 4 to 6 comparable terms after stopwords,
# and a resume paraphrases rather than quoting the JD back, so demanding a
# majority overlap produces false "no evidence" on genuine matches. At 0.4 a
# 5-term requirement needs 2 terms present.
#
# This number decides whether a human sees "confirmed" or "needs validation",
# so treat it as a governed parameter: if you change it, re-run
# test_threshold_behavior_is_documented and update the number here and in
# ENABLEMENT.md together. It has not been validated against labeled screening
# outcomes, and it should be before this tool informs a real req. Recording
# that gap is the point of this comment.
CONFIRMED_EVIDENCE_THRESHOLD = 0.4

# What this tool actually enforces, versus what it merely encourages
# -------------------------------------------------------------------
# These two lists are returned in every response on purpose. The original
# version of this module claimed the tool "never produces a score" and backed
# that with a test asserting no field NAME matches /score|rank|fit_percent/.
# That test passes, and the guarantee still does not hold: the response carries
# evidence_found_count and requirement_count, so any calling agent divides one
# by the other and has a match percentage in a single step. Field-name
# filtering cannot prevent arithmetic.
#
# So the claim is now split. ENFORCED_GUARANTEES are properties the test suite
# verifies behaviorally. KNOWN_LIMITATIONS are the things a schema cannot
# prevent, stated plainly and shipped in the payload so the agent consuming
# this tool sees them at call time rather than in a docstring nobody reads.
# An honest limitation beats an unenforceable promise.
ENFORCED_GUARANTEES = (
    "No field in this response holds a single number representing candidate fitness.",
    "No response ranks or compares one candidate against another; each call sees one resume.",
    "Every requirement carries a status and, where matched, the evidence line it came from, "
    "so a human can check the tool's work.",
    "human_review_required is True on every code path.",
    "A requirement with no comparable terms is reported as not assessable, never as missing evidence.",
)

KNOWN_LIMITATIONS = (
    "The per-status counts can be divided into a percentage. Treat any such ratio as a "
    "workload estimate for validation, never as a fitness score, and do not surface it to a "
    "hiring manager as one. This constraint lives in your agent instructions and reviewer "
    "training, not in this schema.",
    "Matching is keyword overlap, so candidates who echo the job description's vocabulary "
    "match more readily than candidates who describe equivalent work in different words. "
    "That disadvantages career changers and non-native English speakers. This bias has not "
    "been measured. Do not present output as bias-free; present it as evidence to check.",
    f"The confirmed-evidence threshold ({CONFIRMED_EVIDENCE_THRESHOLD}) is reasoned, not "
    "validated against labeled screening outcomes.",
)


def _evidence_for_requirement(requirement: str, resume_lines: list[str]) -> dict:
    req_keywords = _keywords(requirement)
    if not req_keywords:
        # No comparable terms at all. This is usually a duration or quantity
        # requirement ("5+ years of experience", "a bachelor's degree or
        # equivalent") where every word is a stopword. Reporting
        # "no_evidence_found" here was wrong and actively misleading: it reads
        # as "the candidate lacks this" when the truth is "keyword matching
        # cannot answer this question at all." Say that instead.
        return {
            "requirement": requirement,
            "status": "not_assessable_by_this_tool",
            "evidence_line": None,
            "matched_terms": [],
            "reason": (
                "This requirement has no comparable terms after removing common words, "
                "so it is usually a duration, quantity, or credential requirement. "
                "Keyword evidence matching cannot verify it. A human must check it directly."
            ),
        }

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

    if coverage >= CONFIRMED_EVIDENCE_THRESHOLD:
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
    resume_lines = [line.strip() for line in resume_text.splitlines() if line.strip()]

    results = [_evidence_for_requirement(req, resume_lines) for req in requirements]

    return {
        "requirement_count": len(results),
        "evidence": results,
        "evidence_found_count": sum(1 for r in results if r["status"] == "evidence_found"),
        "partial_evidence_count": sum(1 for r in results if r["status"] == "partial_evidence_unconfirmed"),
        "no_evidence_count": sum(1 for r in results if r["status"] == "no_evidence_found"),
        "not_assessable_count": sum(1 for r in results if r["status"] == "not_assessable_by_this_tool"),
        "human_review_required": True,
        "enforced_guarantees": list(ENFORCED_GUARANTEES),
        "known_limitations": list(KNOWN_LIMITATIONS),
        "note": (
            "This is an evidence map, not a recommendation. 'No evidence found' means the "
            "resume text doesn't mention it, not that the candidate lacks it, and "
            "'not assessable by this tool' means keyword matching cannot answer the question "
            "at all. Confirm both with the candidate before screening anyone out. See "
            "03-governance/ai-use-policy.md, principle 3, and read known_limitations before "
            "presenting any of this to a hiring manager."
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
