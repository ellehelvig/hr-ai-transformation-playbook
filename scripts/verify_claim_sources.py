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
import pathlib
import re
import sys
import unicodedata

import yaml

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

        if normalize(str(quote)) not in normalize(text):
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
