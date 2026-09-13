"""Verify the regulatory claims registry.

Two modes, deliberately separated.

Offline (default, runs in CI on every push): validates every claim record against
the schema, checks that ids are unique, that referenced repo files exist, that
dates parse, and that no claim has gone past its review interval. No network, so
it is fast and cannot fail because a government website is down.

Online (--online, runs on a schedule): additionally fetches each primary source
and asserts that the claim's verbatim quote still appears in it. This is the check
that turns a citation from a promise into an assertion. A hallucinated quote, a
paraphrase, or a source that changed under a claim all fail here.

Exit code is non-zero when anything fails.
"""

from __future__ import annotations

import argparse
import datetime as dt
import io
import pathlib
import re
import sys
import unicodedata

import yaml

# Upper bound on pages read from a source PDF. Connecticut PA 26-15 is 74 pages;
# an omnibus act can be several hundred. The cap exists so a malformed or
# adversarial PDF cannot spin the scheduled check forever.
MAX_PDF_PAGES = 600

REPO = pathlib.Path(__file__).resolve().parent.parent
CLAIMS_DIR = REPO / "03-governance" / "claims"

REQUIRED = [
    "id",
    "jurisdiction",
    "topic",
    "statement",
    "status",
    "primary_source",
    "asserted_in",
    "last_verified",
    "verified_by",
    "review_interval_days",
]

REQUIRED_SOURCE = ["url", "citation"]

STATUSES = {
    "in-force",
    "enacted-not-yet-effective",
    "pending",
    "stayed",
    "repealed",
    "superseded",
    "vacated",
    "withdrawn",
    "draft-guidance",
}

DATE_FIELDS = ["last_verified"]

# Characters that differ between a statute PDF, an HTML page, and a YAML file
# without the words differing. Normalized away before comparing.
TRANSLATIONS = {
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u2013": "-",
    "\u2014": "-",
    "\u2212": "-",
    "\u00a0": " ",
    "\u2009": " ",
    "\u00ad": "",
    "\ufeff": "",
}


def normalize(text: str) -> str:
    """Collapse the differences that are formatting, keep the differences that are words."""
    text = unicodedata.normalize("NFKC", text)
    for bad, good in TRANSLATIONS.items():
        text = text.replace(bad, good)
    return re.sub(r"\s+", " ", text).strip()


def normalize_for_match(text: str) -> str:
    """normalize(), plus drop hyphens entirely, for comparing a quote to extracted text.

    PDF text extraction loses the hyphen at a line break. The Connecticut act
    reads "automated employment-related decision" in the document and comes out
    of extraction as "automated employmentrelated decision" wherever that phrase
    happened to wrap. A quote copied correctly from the statute would then fail
    to match the very source it came from, which is the worst kind of check
    failure: one that reports a true claim as false and trains people to ignore
    it.

    Dropping hyphens from both sides fixes that. The cost is that this cannot
    tell "re-creation" from "recreation". For verifying that a sentence of
    statutory text appears in a statute, that trade is obviously worth making.
    """
    return re.sub(r"[-‐‑]", "", normalize(text))


# Page furniture ("Public Act No. 26-15 20 of 74") is short. Statutory body
# lines are long. A cap separates them without needing page geometry, and keeps
# the furniture stripper from eating a repeated sentence of real text.
FURNITURE_MAX_LEN = 60

# A line has to appear on this share of pages before it counts as furniture.
FURNITURE_PAGE_SHARE = 0.6

# Only lines this close to the top or bottom of a page are furniture candidates.
# Position is the strongest signal available without page geometry: a running
# header or footer is always at an edge. Without this, wildcarding the digits
# makes any short body line that differs only by a number ("body text for page
# 3", "Item 4 of 9") look like a footer and get stripped.
FURNITURE_EDGE_LINES = 3


def strip_page_furniture(pages: list[str]) -> str:
    """Drop running headers and footers, then join the pages into one string.

    Why this is needed at all: a statute PDF repeats its header and footer on
    every page, and text extraction drops them into the middle of whatever
    sentence spans the page break. In the Connecticut act the sentence

        ... in violation of this subdivision. The commission or court may
        consider evidence of anti-bias testing ...

    extracts as "... in violation of this subdivision. The / Substitute Senate
    Bill No. 5 / Public Act No. 26-15 20 of 74 / commission or court may ...".
    Any quote crossing that boundary can never match, and the sentences worth
    quoting are long, so they cross boundaries often.

    A line counts as furniture when three things hold: it sits within
    FURNITURE_EDGE_LINES of the top or bottom of its page, it is short, and it
    appears on most pages with digits wildcarded so page numbers collapse
    together. All three matter, and the third alone is not enough. Wildcarding
    digits makes "Item 3 of 9" and "Item 4 of 9" the same shape, which is the
    point for footers and a hazard for body text that differs only by a number.
    Position and length are what keep the hazard contained.

    Failure is safe in both directions: over-stripping or under-stripping makes
    a quote fail to match, which surfaces to a human rather than passing a
    claim that should not have passed.
    """
    if len(pages) < 3:
        return " ".join(pages)

    def shape(line: str) -> str:
        return re.sub(r"\d+", "#", line.strip())

    def edge_candidates(page: str) -> set[str]:
        lines = [line.strip() for line in page.splitlines() if line.strip()]
        edges = lines[:FURNITURE_EDGE_LINES] + lines[-FURNITURE_EDGE_LINES:]
        return {line for line in edges if len(line) <= FURNITURE_MAX_LEN}

    seen: dict[str, int] = {}
    for page in pages:
        for line in edge_candidates(page):
            seen[shape(line)] = seen.get(shape(line), 0) + 1

    threshold = max(2, int(len(pages) * FURNITURE_PAGE_SHARE))
    furniture = {key for key, count in seen.items() if count >= threshold}

    cleaned = []
    for page in pages:
        candidates = edge_candidates(page)
        cleaned.append(
            "\n".join(
                line
                for line in page.splitlines()
                if not (line.strip() in candidates and shape(line) in furniture)
            )
        )
    return " ".join(cleaned)


def extract_pdf_text(raw: bytes, name: str, errors: list) -> str | None:
    """Extract text from a PDF body, or record an error and return None.

    Most US state legislatures publish enacted acts as PDF only. Connecticut
    does; so do Colorado, Illinois and Texas. Without this, the registry can
    never quote-anchor a state statute, which is most of the US backlog, and
    the quote check silently covers only the sources that happen to be HTML.
    """
    try:
        from pdfminer.high_level import extract_text_to_fp
        from pdfminer.layout import LAParams
    except ImportError:
        errors.append(
            f"{name}: source is a PDF but pdfminer.six is not installed. "
            "`pip install pdfminer.six`, or see requirements.txt."
        )
        return None

    pages: list[str] = []
    try:
        for page_number in range(MAX_PDF_PAGES):
            buffer = io.StringIO()
            extract_text_to_fp(
                io.BytesIO(raw), buffer, laparams=LAParams(), page_numbers=[page_number]
            )
            text = buffer.getvalue()
            if not text.strip():
                break
            pages.append(text)
    except Exception as exc:  # noqa: BLE001 - any parse failure is a check failure
        errors.append(f"{name}: could not read the PDF at this source: {type(exc).__name__}: {exc}")
        return None

    if not pages:
        errors.append(
            f"{name}: the PDF at this source produced no extractable text. "
            "It may be a scan needing OCR, in which case quote-anchor a different "
            "primary source rather than this one."
        )
        return None

    return strip_page_furniture(pages)


def parse_date(value, where: str, errors: list) -> dt.date | None:
    if isinstance(value, dt.date):
        return value
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError:
        errors.append(f"{where}: '{value}' is not an ISO date (YYYY-MM-DD)")
        return None


def load_claims(errors: list) -> list:
    if not CLAIMS_DIR.is_dir():
        errors.append(f"missing claims directory: {CLAIMS_DIR}")
        return []
    claims = []
    for path in sorted(CLAIMS_DIR.glob("*.yml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{path.name}: will not parse as YAML: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path.name}: top level must be a mapping")
            continue
        data["_path"] = path
        claims.append(data)
    return claims


def check_schema(claims: list, errors: list) -> None:
    seen = {}
    today = dt.datetime.now(tz=dt.timezone.utc).date()

    for claim in claims:
        name = claim["_path"].name

        for field in REQUIRED:
            if field not in claim or claim[field] in (None, "", []):
                errors.append(f"{name}: missing required field '{field}'")

        claim_id = claim.get("id")
        if claim_id:
            if claim_id in seen:
                errors.append(f"{name}: duplicate id '{claim_id}', also in {seen[claim_id]}")
            seen[claim_id] = name
            if claim["_path"].stem != claim_id:
                errors.append(f"{name}: filename should match id '{claim_id}'")

        status = claim.get("status")
        if status and status not in STATUSES:
            errors.append(f"{name}: status '{status}' is not one of {sorted(STATUSES)}")

        source = claim.get("primary_source")
        if isinstance(source, dict):
            for field in REQUIRED_SOURCE:
                if not source.get(field):
                    errors.append(f"{name}: primary_source is missing '{field}'")
            url = str(source.get("url", ""))
            if url and not url.startswith("https://"):
                errors.append(f"{name}: primary_source.url must be https")
            quote = source.get("quote")
            if quote:
                if len(normalize(str(quote))) < 25:
                    errors.append(f"{name}: primary_source.quote is too short to be evidence")
                if not source.get("retrieved"):
                    errors.append(f"{name}: a quote needs a 'retrieved' date")
                else:
                    parse_date(source["retrieved"], f"{name}: primary_source.retrieved", errors)
        elif source is not None:
            errors.append(f"{name}: primary_source must be a mapping")

        for field in DATE_FIELDS:
            value = claim.get(field)
            if value and value != "never":
                parse_date(value, f"{name}: {field}", errors)

        for ref in claim.get("asserted_in") or []:
            if not (REPO / str(ref)).exists():
                errors.append(f"{name}: asserted_in points at a file that does not exist: {ref}")

        interval = claim.get("review_interval_days")
        if interval is not None and not isinstance(interval, int):
            errors.append(f"{name}: review_interval_days must be an integer")

        blob = yaml.safe_dump(
            {k: v for k, v in claim.items() if k != "_path"}, allow_unicode=True
        )
        if "\u2014" in blob or "\u2013" in blob:
            errors.append(f"{name}: contains an em dash or en dash")

        verified = claim.get("last_verified")
        if verified == "never":
            continue
        if verified and isinstance(interval, int):
            date = parse_date(verified, f"{name}: last_verified", errors)
            if date:
                if date > today:
                    errors.append(f"{name}: last_verified is in the future")
                age = (today - date).days
                if age > interval:
                    errors.append(
                        f"{name}: last verified {age} days ago, review interval is {interval}. "
                        "Re-check the primary source and update last_verified."
                    )


def check_sources_online(claims: list, errors: list) -> None:
    import urllib.error
    import urllib.request

    for claim in claims:
        name = claim["_path"].name
        source = claim.get("primary_source")
        if not isinstance(source, dict):
            continue
        url = source.get("url")
        quote = source.get("quote")
        if not url or not quote:
            continue

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": (
                    "hr-ai-transformation-playbook claim verifier "
                    "(+https://github.com/ellehelvig/hr-ai-transformation-playbook)"
                )
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                raw = response.read()
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            errors.append(f"{name}: could not fetch {url}: {exc}")
            continue

        # Detect PDF by magic bytes rather than by a .pdf suffix on the URL.
        # Legislature sites serve PDFs from extensionless and query-string URLs
        # often enough that trusting the suffix would miss them, and a
        # misdetected PDF fails as "quote not found", which reads as a bad claim
        # rather than as an unsupported format.
        if raw[:5] == b"%PDF-":
            text = extract_pdf_text(raw, name, errors)
            if text is None:
                continue
        else:
            try:
                text = raw.decode("utf-8", errors="replace")
            except UnicodeDecodeError:
                errors.append(f"{name}: could not decode {url}")
                continue

            text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", text)
            text = re.sub(r"(?s)<[^>]+>", " ", text)
            text = (
                text.replace("&nbsp;", " ")
                .replace("&amp;", "&")
                .replace("&quot;", '"')
                .replace("&#39;", "'")
                .replace("&lt;", "<")
                .replace("&gt;", ">")
            )

        if normalize_for_match(str(quote)) not in normalize_for_match(text):
            errors.append(
                f"{name}: the quote no longer appears in {url}. "
                "Either the source changed or the quote is wrong. Do not merge "
                "content resting on this claim until a human has read the source."
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--online",
        action="store_true",
        help="also fetch every primary source and verify its quote verbatim",
    )
    args = parser.parse_args()

    errors: list = []
    claims = load_claims(errors)
    check_schema(claims, errors)
    if args.online and claims:
        check_sources_online(claims, errors)

    anchored = [
        c
        for c in claims
        if isinstance(c.get("primary_source"), dict) and c["primary_source"].get("quote")
    ]
    verified = [c for c in claims if c.get("last_verified") not in (None, "never")]
    print(f"Checked {len(claims)} claim records in 03-governance/claims/")
    print(f"  anchored to a verbatim primary-source quote: {len(anchored)}/{len(claims)}")
    print(f"  verified by a human at least once:           {len(verified)}/{len(claims)}")
    if args.online:
        print("Online mode: every primary source fetched and every quote compared.")

    if errors:
        print("\nFAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("All claim records valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
