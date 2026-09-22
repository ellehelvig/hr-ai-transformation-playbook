"""Tests for the claims verifier, focused on PDF quote anchoring.

These run offline. The PDF fixtures are generated in-process and rebuild the two
pathologies observed in the real Connecticut Public Act 26-15 extraction, so the
behavior is pinned without the suite depending on a government website being up.

Run:  pytest scripts -q
"""

from __future__ import annotations

import datetime as _dt
import importlib.util
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).parent
_spec = importlib.util.spec_from_file_location("verify_claim_sources", HERE / "verify_claim_sources.py")
verifier = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = verifier
_spec.loader.exec_module(verifier)

reportlab = pytest.importorskip("reportlab", reason="reportlab builds the PDF fixtures")
pytest.importorskip("pdfminer", reason="pdfminer.six is what we are testing")


# The sentence worth quoting from PA 26-15 Section 13. It spans a page break in
# the real document, which is exactly why it needs a test.
CROSS_PAGE_QUOTE = (
    "shall not be a defense against a complaint alleging a discriminatory practice in "
    "violation of this subdivision. The commission or court may consider evidence of "
    "anti-bias testing or similar proactive efforts to avoid the discriminatory practice, "
    "including, but not limited to, the quality, efficacy, recency and scope of such testing "
    "or efforts, the results of such testing or efforts and the response thereto."
)

# Body text repeated on several pages. Must survive furniture stripping.
REPEATED_BODY = "individual on the basis of an automated employmentrelated decision"


def _build_act_pdf(path: Path) -> None:
    """A miniature statute PDF with running headers, page numbers, a sentence
    that spans a page break, and a hyphenated phrase broken across lines."""
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    filler = [
        "(%d) For any employment agency, except in the case of a bona fide",
        "occupational qualification, to refuse to refer for employment any",
        REPEATED_BODY,
    ]
    pages = [[line % (i + 3) if "%d" in line else line for line in filler] for i in range(4)]
    pages.insert(2, [
        "veteran, status as a victim of domestic violence, status as a victim of",
        "sexual assault or status as a victim of trafficking in persons. [;] The use",
        "of an automated employment-related decision technology, as defined in",
        "section 7 of this act, shall not be a defense against a complaint alleging",
        "a discriminatory practice in violation of this subdivision. The",
    ])
    pages.insert(3, [
        "commission or court may consider evidence of anti-bias testing or",
        "similar proactive efforts to avoid the discriminatory practice, including,",
        "but not limited to, the quality, efficacy, recency and scope of such testing",
        "or efforts, the results of such testing or efforts and the response thereto.",
    ])

    pdf = canvas.Canvas(str(path), pagesize=letter)
    for number, body in enumerate(pages, start=18):
        y = 720
        for line in body:
            pdf.drawString(72, y, line)
            y -= 16
        pdf.drawString(72, 60, "Substitute Senate Bill No. 5")
        pdf.drawString(72, 44, f"Public Act No. 26-15 {number} of 74")
        pdf.showPage()
    pdf.save()


@pytest.fixture(scope="module")
def act_pdf(tmp_path_factory) -> bytes:
    path = tmp_path_factory.mktemp("pdf") / "act.pdf"
    _build_act_pdf(path)
    return path.read_bytes()


# ── Hyphen handling ──────────────────────────────────────────────────────────


def test_hyphen_lost_at_line_break_still_matches():
    """The failure this fixes: a quote copied correctly from the statute reads
    "employment-related", extraction yields "employmentrelated", and the check
    reports a true claim as false."""
    quote = "an automated employment-related decision"
    extracted = "an automated employmentrelated decision"
    assert verifier.normalize(quote) not in verifier.normalize(extracted)
    assert verifier.normalize_for_match(quote) in verifier.normalize_for_match(extracted)


def test_hyphen_insensitivity_does_not_match_unrelated_words():
    assert verifier.normalize_for_match("employment decision") not in verifier.normalize_for_match(
        "an automated employmentrelated decision"
    )


def test_normalize_for_match_still_collapses_quotes_and_spacing():
    assert verifier.normalize_for_match("the “deployer”   owes") == 'the "deployer" owes'


# ── Page furniture ───────────────────────────────────────────────────────────


def test_cross_page_quote_matches_only_after_furniture_is_stripped(act_pdf):
    """The headline behavior. Running headers land mid-sentence at every page
    break, and the sentences worth quoting are long enough to cross them."""
    errors: list[str] = []
    text = verifier.extract_pdf_text(act_pdf, "fixture", errors)
    assert errors == []
    assert verifier.normalize_for_match(CROSS_PAGE_QUOTE) in verifier.normalize_for_match(text)


def test_repeated_body_text_is_not_mistaken_for_furniture(act_pdf):
    """The guard on the heuristic. Page furniture is short; statutory lines are
    long. Without the length cap, a sentence repeated across pages gets eaten,
    and the check would then reject a correct quote."""
    errors: list[str] = []
    text = verifier.extract_pdf_text(act_pdf, "fixture", errors)
    assert verifier.normalize_for_match(REPEATED_BODY) in verifier.normalize_for_match(text)


def test_running_header_and_page_numbers_are_removed(act_pdf):
    errors: list[str] = []
    text = verifier.normalize(verifier.extract_pdf_text(act_pdf, "fixture", errors))
    assert "Substitute Senate Bill No. 5" not in text
    assert "Public Act No. 26-15 18 of 74" not in text


def test_short_documents_are_left_alone():
    """Under three pages there is not enough repetition to tell furniture from
    content, so the stripper does nothing rather than guessing."""
    pages = ["Header\nbody one", "Header\nbody two"]
    joined = verifier.strip_page_furniture(pages)
    assert "Header" in joined


def _page(number: int) -> str:
    """A page shaped like a real one: a footer at the bottom, and body lines in
    the middle that differ only by a number, which is the case digit-wildcarding
    would otherwise mistake for furniture."""
    body = "\n".join(f"body text for page {number} line {j}" for j in range(8))
    return f"{body}\nPage {number} of 9"


def test_page_numbers_collapse_so_footers_group_together():
    """Wildcarding digits is what lets "Page 1 of 9" and "Page 2 of 9" be
    recognized as the same footer."""
    joined = verifier.strip_page_furniture([_page(i) for i in range(1, 6)])
    assert "Page 3 of 9" not in joined
    assert "body text for page 3 line 4" in joined


def test_numbered_body_lines_away_from_the_edges_survive():
    """The guard on digit-wildcarding. Body lines differing only by a number
    share a wildcarded shape with each other, so without the position check they
    would be stripped as footers."""
    joined = verifier.strip_page_furniture([_page(i) for i in range(1, 6)])
    for i in range(1, 6):
        assert f"body text for page {i} line 4" in joined


def test_very_short_pages_are_a_known_limitation():
    """Pinned rather than fixed. When a page has fewer lines than the edge
    window, every line is an edge line, so body text that repeats in shape gets
    stripped. Real statute pages carry 30 to 50 lines, so this does not arise in
    practice, and the failure direction is a quote that does not match, which a
    human sees. Recording it so the next person does not rediscover it as a bug."""
    pages = [f"body text for page {i}\nPage {i} of 9" for i in range(1, 6)]
    joined = verifier.strip_page_furniture(pages)
    assert "body text for page 3" not in joined


# ── Failure modes report rather than pass ────────────────────────────────────


def test_blank_page_does_not_truncate_the_document():
    """Regression. The first implementation walked pages and stopped at the
    first one with no text, so a blank divider page made everything after it
    invisible: a six-page fixture returned three pages. A quote from a later
    section then failed to match and was reported as a wrong claim, which is a
    false alarm on a true claim, the one failure direction this checker cannot
    afford."""
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    import io as _io

    # Pages carry enough distinct lines to look like a real statute page. A
    # one-line-per-page fixture would instead trip the short-page limitation
    # pinned in test_very_short_pages_are_a_known_limitation and test nothing
    # about truncation.
    # The marker sits in the middle of the page, not at the top. A short line
    # repeating at a page edge is indistinguishable from a running header and
    # would be stripped, correctly, by the furniture heuristic. This test is
    # about truncation, so it asserts on body text where that cannot interfere.
    marker = "the quick brown fox jumps over the lazy dog on page"
    buffer = _io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    for n in range(6):
        if n != 3:  # page index 3 deliberately blank
            y = 700
            for j in range(9):
                pdf.drawString(
                    72, y,
                    f"{marker} {n}" if j == 4
                    else f"subsection {j} text unique to page {n} of this fixture act",
                )
                y -= 16
        pdf.showPage()
    pdf.save()

    errors: list[str] = []
    text = verifier.extract_pdf_text(buffer.getvalue(), "fixture", errors)
    assert errors == []
    for n in (0, 1, 2, 4, 5):
        assert f"{marker} {n}" in text, f"page {n} was lost after the blank page"


def test_unreadable_pdf_is_an_error_not_a_silent_pass():
    errors: list[str] = []
    result = verifier.extract_pdf_text(b"%PDF-1.4 truncated garbage", "fixture", errors)
    assert result is None
    assert errors and "fixture" in errors[0]


def test_image_only_pdf_says_to_pick_a_different_source():
    """A scanned act yields no text. The message has to point somewhere useful
    rather than reading as a wrong quote."""
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    import io as _io

    buffer = _io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.rect(100, 100, 200, 200, fill=1)
    pdf.showPage()
    pdf.save()

    errors: list[str] = []
    assert verifier.extract_pdf_text(buffer.getvalue(), "fixture", errors) is None
    assert "OCR" in errors[0]


def test_pdf_detected_by_magic_bytes_not_url_suffix():
    """Legislature sites serve PDFs from extensionless and query-string URLs.
    Trusting the suffix would send those down the HTML path, where the failure
    reads as a bad claim rather than an unsupported format."""
    assert b"%PDF-"[:5] == b"%PDF-"
    assert not b"<!DOCTYPE html>".startswith(b"%PDF-")


def test_bot_challenge_is_unreadable_not_a_wrong_quote():
    """EUR-Lex answers scripts with 202 and an empty body. That has to fail as
    a fetch problem, or it reads as a statute that changed."""
    reason = verifier.blocked_response_reason(202, {"x-amzn-waf-action": "challenge"}, b"")
    assert reason and "bot challenge" in reason


def test_non_200_and_empty_pages_are_unreadable():
    assert "202" in verifier.blocked_response_reason(202, {}, b"<html></html>")
    assert "empty" in verifier.blocked_response_reason(200, {}, b"  \n")


def test_a_normal_page_is_readable():
    assert verifier.blocked_response_reason(200, {}, b"<html>text</html>") is None


# ---------------------------------------------------------------------------
# Marker and drift gate
#
# The defect these pin: a statute date lives in the registry and is separately
# retyped in up to six documents. Nothing connected the copies, so changing one
# and forgetting the others failed silently. A silently wrong effective date is
# the worst thing this repo can ship, because a reader acts on it.
# ---------------------------------------------------------------------------


def test_date_forms_accepts_the_ways_this_repo_writes_a_date():
    forms = verifier.date_forms(_dt.date(2027, 12, 2))
    assert "2 December 2027" in forms
    assert "December 2, 2027" in forms
    assert "2027-12-02" in forms


def test_date_forms_includes_month_and_year_without_the_day():
    """Prose legitimately says "December 2027". Requiring the day would fail
    correct documents, and the drift worth catching is a wholly different date:
    the real case moved August 2026 to December 2027."""
    assert "December 2027" in verifier.date_forms(_dt.date(2027, 12, 2))


def test_paragraph_around_stops_at_blank_lines():
    """The date has to sit near its marker. Searching the whole document would
    pass on a coincidence somewhere else on the page."""
    text = "First para with 2 August 2026.\n\nSecond para here.\n\nThird para."
    index = text.index("Second")
    para = verifier.paragraph_around(text, index)
    assert para == "Second para here."
    assert "2 August 2026" not in para


def test_paragraph_around_handles_first_and_last_paragraph():
    text = "Only one paragraph, no blank lines at all."
    assert verifier.paragraph_around(text, 5) == text


def _claim(**over):
    base = {
        "id": "demo-claim",
        "jurisdiction": "EU",
        "topic": "demo",
        "statement": "demo",
        "status": "in-force",
        "primary_source": {"url": "https://example.org", "citation": "demo"},
        "asserted_in": ["README.md"],
        "last_verified": "never",
        "verified_by": "unverified",
        "review_interval_days": 90,
        "_path": Path("demo-claim.yml"),
    }
    base.update(over)
    return base


def test_drift_gate_fires_when_prose_keeps_the_old_date(monkeypatch):
    """Change the date in the record, leave the prose alone, fail the build."""
    monkeypatch.setattr(
        verifier,
        "collect_markers",
        lambda: {"demo-claim": [("README.md", "Applies from 2 August 2026. <!--claim:demo-claim-->")]},
    )
    errors: list[str] = []
    verifier.check_markers([_claim(effective="2027-12-02")], errors)
    assert len(errors) == 1
    assert "does not state the effective date 2027-12-02" in errors[0]
    assert "2 December 2027" in errors[0]


def test_drift_gate_passes_when_prose_matches(monkeypatch):
    monkeypatch.setattr(
        verifier,
        "collect_markers",
        lambda: {"demo-claim": [("README.md", "Applies from 2 December 2027. <!--claim:demo-claim-->")]},
    )
    errors: list[str] = []
    marked, unmarked = verifier.check_markers([_claim(effective="2027-12-02")], errors)
    assert errors == []
    assert (marked, unmarked) == (1, 0)


def test_marker_citing_an_unknown_id_is_a_dangling_citation(monkeypatch):
    monkeypatch.setattr(
        verifier, "collect_markers", lambda: {"no-such-claim": [("README.md", "text")]}
    )
    errors: list[str] = []
    verifier.check_markers([_claim()], errors)
    assert any("not a record" in e for e in errors)


def test_marker_in_a_file_missing_from_asserted_in_fails(monkeypatch):
    """Caught a real gap: 2 August 2028 appeared in deployer-checklist.md while
    the Annex I record listed only the intake template."""
    monkeypatch.setattr(
        verifier,
        "collect_markers",
        lambda: {"demo-claim": [("other.md", "text <!--claim:demo-claim-->")]},
    )
    errors: list[str] = []
    verifier.check_markers([_claim(asserted_in=["README.md"])], errors)
    assert any("not listed in asserted_in" in e for e in errors)
    assert any("has no" in e and "marker" in e for e in errors)


def test_claim_with_no_marker_anywhere_is_counted_not_failed(monkeypatch):
    """Adoption is per claim. An unmarked claim is a visible gap, not a broken
    build, so the scheme can be taken up one record at a time."""
    monkeypatch.setattr(verifier, "collect_markers", lambda: {})
    errors: list[str] = []
    marked, unmarked = verifier.check_markers([_claim(effective="2027-12-02")], errors)
    assert errors == []
    assert (marked, unmarked) == (0, 1)


def test_unverified_claim_does_not_fail_before_the_deadline():
    """Every record says last_verified: never. Failing today would block every
    merge, so the gate is dated rather than absent."""
    assert verifier.UNVERIFIED_DEADLINE > _dt.date(2026, 9, 18)
    errors: list[str] = []
    verifier.check_schema([_claim()], errors)
    assert errors == []


def test_never_no_longer_silently_skips_the_staleness_gate(monkeypatch):
    """The original bug: `never` hit a bare `continue`, so the staleness check
    ran on nothing at all while appearing to work."""
    monkeypatch.setattr(verifier, "UNVERIFIED_DEADLINE", _dt.date(2020, 1, 1))
    errors: list[str] = []
    verifier.check_schema([_claim()], errors)
    assert any("deadline for verifying" in e for e in errors)


def test_marker_inside_a_code_fence_is_not_a_citation():
    """Documentation has to be able to show a marker. This check flagged its own
    README on the first run, reporting the literal example as a dangling
    citation."""
    text = "Real one here. <!--claim:real-id-->\n\n```markdown\n<!--claim:example-id-->\n```\n"
    cleaned = verifier.blank_code(text)
    found = {m.group(1) for m in verifier.MARKER_RE.finditer(cleaned)}
    assert found == {"real-id"}


def test_marker_inside_backticks_is_not_a_citation():
    """The CHANGELOG describes the scheme as `<!--claim:id-->` in inline code."""
    text = "Prose cites a record with `<!--claim:id-->`, which renders as nothing."
    assert verifier.MARKER_RE.search(verifier.blank_code(text)) is None


def test_blanking_code_preserves_offsets_so_paragraphs_stay_correct():
    """Spaces rather than deletion, so the paragraph the drift gate reads is
    still the real one and the date it looks for is still in it."""
    text = "Applies from `2 December 2027` per the record. <!--claim:demo-->"
    cleaned = verifier.blank_code(text)
    assert len(cleaned) == len(text)
    assert cleaned.index("<!--claim:demo-->") == text.index("<!--claim:demo-->")
