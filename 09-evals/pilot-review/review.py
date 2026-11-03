"""Offline review of version-bound synthetic evidence. No deployment authorization."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import stat
import sys
from datetime import UTC, date, datetime
from html import escape
from pathlib import Path, PurePosixPath

POLICY = "synthetic-pilot-review-v1"
CRITERIA = ("routing", "privacy", "review_controls", "reviewer_capacity")
MAX_AGE_DAYS = 30
MAX_BYTES = 262144
MAX_CASES = 1000000
STATUSES = ("pause", "stop", "eligible_for_human_review")
INCIDENTS = ("cross_user_exposure", "approval_bypass")
ASSERTIONS = ("privacy_review", "identity_access_review", "technical_review")
SLUG = re.compile(r"[a-z][a-z0-9-]{0,63}\Z")
REVISION = re.compile(r"[a-f0-9]{40}\Z")
SHA256 = re.compile(r"[a-f0-9]{64}\Z")


class PacketError(ValueError):
    """An invalid packet, artifact, or review record. Never include input text."""


def object_fields(value, required, optional=()):
    if not isinstance(value, dict) or not set(required) <= value.keys():
        raise PacketError("Required fields are missing.")
    if set(value) - set(required) - set(optional):
        raise PacketError("Undeclared fields are not accepted.")


def token(value, pattern=SLUG):
    if not isinstance(value, str) or not pattern.fullmatch(value):
        raise PacketError("Invalid identifier.")
    return value


def calendar_date(value):
    if not isinstance(value, str):
        raise PacketError("Invalid date.")
    try:
        result = date.fromisoformat(value)
    except ValueError as exc:
        raise PacketError("Invalid date.") from exc
    if result.isoformat() != value:
        raise PacketError("Use an ISO calendar date.")
    return result


def count(value, minimum=0):
    if type(value) is not int or not minimum <= value <= MAX_CASES:
        raise PacketError("Invalid case count.")
    return value


def minutes(value):
    if type(value) not in (int, float) or not 0 <= value <= 1000000000 or not math.isfinite(value):
        raise PacketError("Invalid workload measurement.")
    return value


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PacketError("Duplicate JSON keys are not accepted.")
        result[key] = value
    return result


def decode(raw):
    def reject_constant(_value):
        raise PacketError("Non-finite JSON values are not accepted.")

    try:
        result = json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject_constant)
        pending = [(result, 0)]
        while pending:
            value, depth = pending.pop()
            if depth > 32:
                raise PacketError("Evidence nesting exceeds the contract limit.")
            if isinstance(value, dict):
                pending.extend((child, depth + 1) for child in value.values())
            elif isinstance(value, list):
                pending.extend((child, depth + 1) for child in value)
        return result
    except (ValueError, UnicodeDecodeError, RecursionError) as exc:
        raise PacketError("Invalid JSON evidence.") from exc


def read_regular(path):
    """Bound reads and reject devices, pipes, and final symlinks where supported."""
    flags = os.O_RDONLY | getattr(os, "O_NONBLOCK", 0) | getattr(os, "O_NOFOLLOW", 0)
    if path.is_symlink():
        raise PacketError("Symlinks are not accepted.")
    descriptor = os.open(path, flags)
    with os.fdopen(descriptor, "rb") as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise PacketError("Evidence must be a regular file.")
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise PacketError("Evidence exceeds the size limit.")
    return raw


def artifact_path(root, relative):
    if not isinstance(relative, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]{0,180}\.json", relative):
        raise PacketError("Invalid artifact path.")
    pure = PurePosixPath(relative)
    if pure.is_absolute() or pure.as_posix() != relative or any(part in (".", "..") for part in relative.split("/")):
        raise PacketError("Artifact paths must remain inside the packet directory.")
    current = root
    for part in pure.parts:
        current = current / part
        if current.is_symlink():
            raise PacketError("Artifact symlinks are not accepted.")
    if not current.resolve().is_relative_to(root):
        raise PacketError("Artifact paths must remain inside the packet directory.")
    return current


def validate_packet(packet, root):
    object_fields(
        packet,
        ("schema_version", "data_kind", "packet_id", "workflow_id", "source_revision", "artifacts"),
        ("assertions", "reported_incidents"),
    )
    if type(packet["schema_version"]) is not int or packet["schema_version"] != 1:
        raise PacketError("Unsupported packet schema.")
    if packet["data_kind"] != "synthetic":
        raise PacketError("Fictional evidence only.")
    for key in ("packet_id", "workflow_id"):
        token(packet[key])
    token(packet["source_revision"], REVISION)
    if not isinstance(packet["artifacts"], list) or len(packet["artifacts"]) > len(CRITERIA):
        raise PacketError("Invalid artifact collection.")
    seen_ids, seen_paths = set(), set()
    for ref in packet["artifacts"]:
        object_fields(ref, ("criterion_id", "path", "sha256", "format", "dataset_id", "method_id", "observed_on"))
        if ref["criterion_id"] not in CRITERIA or ref["format"] not in ("checks-v1", "resolve-rules-v1"):
            raise PacketError("Unknown evidence contract.")
        if ref["format"] == "resolve-rules-v1" and ref["criterion_id"] != "routing":
            raise PacketError("Resolve reports supply routing evidence only.")
        artifact_path(root, ref["path"])
        if ref["criterion_id"] in seen_ids or ref["path"] in seen_paths:
            raise PacketError("Duplicate evidence references.")
        seen_ids.add(ref["criterion_id"])
        seen_paths.add(ref["path"])
        token(ref["sha256"], SHA256)
        token(ref["dataset_id"])
        token(ref["method_id"])
        calendar_date(ref["observed_on"])
    assertions = packet.get("assertions", {})
    object_fields(assertions, (), ASSERTIONS)
    if any(value not in ("present", "missing", "unknown") for value in assertions.values()):
        raise PacketError("Unknown assertion state.")
    incidents = packet.get("reported_incidents", [])
    if not isinstance(incidents, list) or any(item not in INCIDENTS for item in incidents):
        raise PacketError("Unknown reported incident.")
    if len(incidents) != len(set(incidents)):
        raise PacketError("Duplicate reported incidents.")


def suite(result):
    object_fields(result, ("passed", "total"))
    total, passed = count(result["total"], 1), count(result["passed"])
    if passed > total:
        raise PacketError("Contradictory evaluation counts.")
    return passed, total


def resolve_results(result, observed_on):
    """Reconcile the preserved report before interpreting its routing counts."""
    object_fields(
        result,
        (
            "generated_at",
            "suite_version",
            "total",
            "passed",
            "pass_rate",
            "metrics",
            "categories",
            "failures",
            "holdout",
        ),
    )
    if result["suite_version"] != "1.0.0" or not isinstance(result["generated_at"], str):
        raise PacketError("Unsupported Resolve report version.")
    try:
        generated = datetime.fromisoformat(result["generated_at"])
    except ValueError as exc:
        raise PacketError("Invalid Resolve observation date.") from exc
    if generated.tzinfo is None or generated.astimezone(UTC).date() != calendar_date(observed_on):
        raise PacketError("Resolve observation date contradicts its report.")
    baseline = {key: result[key] for key in ("passed", "total")}
    passed, total = suite(baseline)
    rate = result["pass_rate"]
    if type(rate) not in (int, float) or not math.isfinite(rate) or abs(rate - passed / total * 100) > 0.001:
        raise PacketError("Contradictory baseline rate.")
    if not isinstance(result["failures"], list) or len(result["failures"]) != total - passed:
        raise PacketError("Contradictory baseline failures.")
    if not isinstance(result["categories"], dict) or not 1 <= len(result["categories"]) <= 100:
        raise PacketError("Invalid baseline categories.")
    categories = [suite(entry) for entry in result["categories"].values()]
    if sum(entry[0] for entry in categories) != passed or sum(entry[1] for entry in categories) != total:
        raise PacketError("Baseline categories contradict the summary.")
    holdout = result["holdout"]
    object_fields(holdout, ("total", "passed", "miss_types", "cases"))
    suite({key: holdout[key] for key in ("passed", "total")})
    if not isinstance(holdout["cases"], list) or len(holdout["cases"]) != holdout["total"]:
        raise PacketError("Contradictory paraphrase denominator.")
    passed_cases, misses, specialist_misses, case_ids = 0, {}, 0, set()
    for case in holdout["cases"]:
        object_fields(
            case,
            ("id", "category", "request", "expected_status", "actual_status", "actual_intent", "passed", "miss_type"),
        )
        if not isinstance(case["id"], str) or case["id"] in case_ids or type(case["passed"]) is not bool:
            raise PacketError("Invalid paraphrase case.")
        case_ids.add(case["id"])
        if case["passed"] and case["actual_status"] != case["expected_status"]:
            raise PacketError("A successful case contradicts its routing status.")
        passed_cases += case["passed"]
        if not case["passed"]:
            if not isinstance(case["miss_type"], str):
                raise PacketError("Invalid miss classification.")
            misses[case["miss_type"]] = misses.get(case["miss_type"], 0) + 1
            specialist_misses += case["category"] in ("protected_workplace_concern", "legal_escalation")
    if passed_cases != holdout["passed"] or misses != holdout["miss_types"]:
        raise PacketError("Paraphrase summaries contradict case results.")
    return {
        "regression": baseline,
        "paraphrases": {key: holdout[key] for key in ("passed", "total")},
        "specialist_misses": specialist_misses,
    }


def observations(criterion, result):
    """Compute outcomes from typed observations, never from a supplied pass label."""
    if criterion == "routing":
        object_fields(result, ("regression", "paraphrases", "specialist_misses"))
        regression, paraphrases = suite(result["regression"]), suite(result["paraphrases"])
        missed = count(result["specialist_misses"])
        if missed > paraphrases[1] - paraphrases[0]:
            raise PacketError("Specialist misses exceed failed paraphrase cases.")
        passed = regression[0] == regression[1] and paraphrases[0] == paraphrases[1] and missed == 0
        metrics = {
            "regression": f"{regression[0]}/{regression[1]}",
            "paraphrases": f"{paraphrases[0]}/{paraphrases[1]}",
            "specialist_misses": missed,
        }
        return passed, False, metrics
    if criterion in ("privacy", "review_controls"):
        field = "cross_user_exposures" if criterion == "privacy" else "approval_bypasses"
        object_fields(result, ("tested_cases", field))
        tested, failures = count(result["tested_cases"], 1), count(result[field])
        if failures > tested:
            raise PacketError("Incident count exceeds tested cases.")
        return failures == 0, failures > 0, {"tested_cases": tested, field: failures}
    object_fields(result, ("case_count", "required_review_minutes", "available_review_minutes"))
    cases = count(result["case_count"], 1)
    required, available = minutes(result["required_review_minutes"]), minutes(result["available_review_minutes"])
    if required == 0:
        raise PacketError("Required human review effort cannot be zero.")
    return (
        available >= required,
        False,
        {"case_count": cases, "required_review_minutes": required, "available_review_minutes": available},
    )


def inspect_artifact(packet, ref, root, as_of):
    row = {key: ref[key] for key in ("criterion_id", "path", "dataset_id", "method_id", "observed_on")}
    row.update(
        declared_sha256=ref["sha256"],
        actual_sha256=None,
        status="invalid",
        reason="invalid_artifact",
        metrics={},
        critical_incident=False,
        checks_passed=None,
    )
    try:
        raw = read_regular(artifact_path(root, ref["path"]))
        row["actual_sha256"] = hashlib.sha256(raw).hexdigest()
        if row["actual_sha256"] != ref["sha256"]:
            row["reason"] = "hash_mismatch"
            return row
        artifact = decode(raw)
        object_fields(
            artifact,
            (
                "schema_version",
                "data_kind",
                "criterion_id",
                "workflow_id",
                "source_revision",
                "dataset_id",
                "method_id",
                "observed_on",
                "format",
                "results",
            ),
        )
        if type(artifact["schema_version"]) is not int or artifact["schema_version"] != 1:
            return row
        if artifact["data_kind"] != "synthetic":
            return row
        bindings = {key: packet[key] for key in ("workflow_id", "source_revision")}
        bindings.update({key: ref[key] for key in ("criterion_id", "dataset_id", "method_id", "observed_on", "format")})
        if any(artifact[key] != expected for key, expected in bindings.items()):
            row["reason"] = "binding_mismatch"
            return row
        result = (
            resolve_results(artifact["results"], ref["observed_on"])
            if ref["format"] == "resolve-rules-v1"
            else artifact["results"]
        )
        passed, critical, metrics = observations(ref["criterion_id"], result)
        row.update(metrics=metrics, critical_incident=critical, checks_passed=passed)
        age = (as_of - calendar_date(ref["observed_on"])).days
        if age < 0:
            row.update(status="invalid", reason="future_observation")
        elif age > MAX_AGE_DAYS:
            row.update(status="stale", reason="older_than_policy_limit" if passed else "stale_and_failed_checks")
        else:
            row.update(
                status="passed" if passed else "failed", reason="checks_satisfied" if passed else "failed_checks"
            )
    except FileNotFoundError:
        row.update(status="missing", reason="missing_file")
    except (OSError, PacketError, TypeError, OverflowError):
        # Do not repeat raw file contents, personal text, or caller paths in errors.
        row.update(status="invalid", reason="invalid_artifact")
    return row


def assess(path, as_of=None):
    as_of = as_of or datetime.now(UTC).date()
    if not isinstance(as_of, date) or isinstance(as_of, datetime):
        raise PacketError("Invalid review date.")
    path = Path(path)
    raw = read_regular(path)
    packet, root = decode(raw), path.parent.resolve()
    validate_packet(packet, root)
    refs = {ref["criterion_id"]: ref for ref in packet["artifacts"]}
    rows = []
    for criterion in CRITERIA:
        if criterion in refs:
            rows.append(inspect_artifact(packet, refs[criterion], root, as_of))
        else:
            rows.append(
                {
                    "criterion_id": criterion,
                    "status": "missing",
                    "reason": "missing_reference",
                    "metrics": {},
                    "critical_incident": False,
                }
            )
    blockers = [
        {"criterion_id": row["criterion_id"], "reason": row["reason"]} for row in rows if row["status"] != "passed"
    ]
    incidents = packet.get("reported_incidents", [])
    critical = bool(incidents) or any(row["critical_incident"] for row in rows)
    decision = "stop" if critical else "pause" if blockers else "eligible_for_human_review"
    report = {
        "schema_version": 1,
        "policy_id": POLICY,
        "data_kind": "synthetic",
        "packet_id": packet["packet_id"],
        "workflow_id": packet["workflow_id"],
        "source_revision": packet["source_revision"],
        "packet_sha256": hashlib.sha256(raw).hexdigest(),
        "as_of": as_of.isoformat(),
        "max_age_days": MAX_AGE_DAYS,
        "decision": decision,
        "artifacts": rows,
        "blockers": blockers,
        "caller_assertions": {key: packet.get("assertions", {}).get(key, "unknown") for key in ASSERTIONS},
        "caller_reported_incidents": incidents,
        "authorization_granted": False,
        "production_hold": True,
        "limits": "Local synthetic evidence only. Hashes identify bytes, not truth, independence, or approval.",
    }
    report["review_digest"] = hashlib.sha256(json.dumps(report, sort_keys=True, allow_nan=False).encode()).hexdigest()
    return report


def make_record(report, reviewer, disposition):
    if not isinstance(reviewer, str) or not re.fullmatch(r"reviewer-[0-9]{2}", reviewer):
        raise PacketError("Use a fictional reviewer identifier.")
    if disposition not in STATUSES:
        raise PacketError("Invalid proposed disposition.")
    if report["decision"] == "stop" and disposition != "stop":
        raise PacketError("A record cannot clear a stop.")
    if report["decision"] == "pause" and disposition == "eligible_for_human_review":
        raise PacketError("A record cannot clear required evidence gaps.")
    return {
        "schema_version": 1,
        "policy_id": POLICY,
        "data_kind": "synthetic",
        "packet_id": report["packet_id"],
        "source_revision": report["source_revision"],
        "as_of": report["as_of"],
        "packet_sha256": report["packet_sha256"],
        "review_digest": report["review_digest"],
        "reviewer_id": reviewer,
        "proposed_disposition": disposition,
        "simulated_identity": True,
        "editable_record": True,
        "authorization_granted": False,
        "production_hold": True,
    }


def verify_record(report, record):
    if not isinstance(record, dict):
        raise PacketError("Invalid review record.")
    expected = make_record(report, record.get("reviewer_id"), record.get("proposed_disposition"))
    # JSON booleans and integer values must retain their types, not merely compare equal.
    if json.dumps(record, sort_keys=True) != json.dumps(expected, sort_keys=True):
        raise PacketError("The record does not match this evidence version and review date.")
    return {
        "record_matches": True,
        "simulated_identity": True,
        "editable_record": True,
        "authorization_granted": False,
        "production_hold": True,
        "proposed_disposition": record["proposed_disposition"],
    }


def markdown(report):
    lines = [
        "# Synthetic HR AI pilot review",
        "",
        f"**Proposed disposition: {report['decision']}**",
        "",
        "Production hold: yes. Deployment authorization: no.",
        "",
        f"Workflow: `{report['workflow_id']}`. Source revision: `{report['source_revision']}`.",
        f"As of: {report['as_of']}. Policy: `{POLICY}`. Maximum evidence age: {MAX_AGE_DAYS} days.",
        "",
        "| Criterion | Status | Finding | Observations |",
        "|---|---|---|---|",
    ]
    for row in report["artifacts"]:
        values = "; ".join(f"{key}: {value}" for key, value in row["metrics"].items()) or "No valid observations"
        lines.append(f"| {row['criterion_id']} | {row['status']} | {row['reason']} | {values} |")
    lines.extend(["", "## Caller assertions, not verified approvals", ""])
    lines.extend(f"- {key}: {value}" for key, value in report["caller_assertions"].items())
    lines.extend(
        [
            "",
            f"Caller-reported fictional incidents: {', '.join(report['caller_reported_incidents']) or 'none'}.",
            "",
            "## Evidence identity",
            "",
            f"Packet SHA-256: `{report['packet_sha256']}`.",
            f"Review digest: `{report['review_digest']}`.",
            "",
        ]
    )
    for row in report["artifacts"]:
        if "path" in row:
            lines.extend(
                [
                    f"- {row['criterion_id']}: `{row['path']}`; dataset `{row['dataset_id']}`; "
                    f"method `{row['method_id']}`; observed {row['observed_on']}.",
                    f"  Declared SHA-256: `{row['declared_sha256']}`; read SHA-256: "
                    f"`{row['actual_sha256'] or 'unavailable'}`.",
                ]
            )
    lines.extend(
        [
            "",
            "## Limits and next action",
            "",
            report["limits"],
            "A person must inspect the source evidence, methods, ownership, access, and legal scope "
            "before any real use.",
            "Stop and pause findings require correction and fresh review. An eligible result only queues human review.",
            "A typed reviewer ID and editable JSON file do not verify identity or protect an audit trail.",
            "",
        ]
    )
    return "\n".join(lines)


def html_report(report):
    cards = []
    identities = []
    for row in report["artifacts"]:
        label = escape(row["criterion_id"].replace("_", " "))
        reason = escape(row["reason"].replace("_", " "))
        metrics = "".join(
            f"<dt>{escape(key.replace('_', ' '))}</dt><dd>{escape(str(value))}</dd>"
            for key, value in row["metrics"].items()
        )
        cards.append(
            f'<article><p class="tag">{label}</p><h3>{escape(row["status"])}</h3>'
            f"<p>{reason}</p><dl>{metrics or 'No valid observations available.'}</dl></article>"
        )
        if "path" in row:
            identities.append(
                f"<li><b>{label}</b>: {escape(row['path'])}<br>"
                f"Dataset: {escape(row['dataset_id'])}. Method: {escape(row['method_id'])}.<br>"
                f"Observed: {escape(row['observed_on'])}.<br>"
                f"Declared SHA-256: {escape(row['declared_sha256'])}<br>"
                f"Read SHA-256: {escape(row['actual_sha256'] or 'unavailable')}</li>"
            )
    assertions = "".join(
        f"<li>{escape(key.replace('_', ' '))}: <b>{escape(value)}</b></li>"
        for key, value in report["caller_assertions"].items()
    )
    incidents = escape(", ".join(report["caller_reported_incidents"]) or "none")
    return f"""<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'">
<title>Synthetic HR AI pilot review</title>
<style>body{{margin:0;background:#f5f7fb;color:#172033;font:16px/1.6 system-ui}}
main{{max-width:1080px;margin:32px auto;padding:24px}}header{{border-top:4px solid #5140b5}}
.tag{{color:#086779}}h1{{font-size:2rem;line-height:1.2}}.decision{{background:#fff;border:1px solid #73809b;
border-radius:12px;padding:20px;overflow-wrap:anywhere}}.cards{{display:grid;grid-template-columns:1fr 1fr;gap:16px;
margin:24px 0}}article{{background:#fff;border:1px solid #d0d6e0;border-radius:12px;padding:20px}}
article h3{{margin:0}}dl{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}dd{{margin:0;font-weight:600}}
.identity{{overflow-wrap:anywhere;font:13px/1.8 ui-monospace,monospace}}li{{margin-bottom:12px}}
@media(max-width:600px){{main{{padding:16px;margin:0}}.cards{{grid-template-columns:1fr}}}}</style>
<main><header><p class="tag">FICTIONAL DATA / EVIDENCE REVIEW</p>
<h1>What does this pilot evidence support?</h1></header>
<section class="decision"><h2>{escape(report["decision"].replace("_", " "))}</h2>
<p>Production hold stays in place. No deployment authorization is granted.</p>
<p>{len(report["blockers"])} required criterion findings. Review date: {report["as_of"]}.</p>
<p>Workflow: {escape(report["workflow_id"])}<br>Source revision: {escape(report["source_revision"])}</p></section>
<p>Local artifact contents are inspected. Experimental truth, independence, and approvals are not verified.</p>
<div class="cards">{"".join(cards)}</div>
<h2>Caller assertions, not verified approvals</h2><ul>{assertions}</ul>
<p>Caller-reported fictional incidents: {incidents}.</p>
<h2>Before any next step</h2><p>A person must inspect the source evidence, methods, ownership, access, and legal scope.
An eligible result only queues human review. Fix pause/stop findings and obtain a fresh review.</p>
<p>The four criteria and {MAX_AGE_DAYS}-day age limit are demonstration policy choices, not legal thresholds.
A typed reviewer ID and editable JSON file do not verify identity or protect an audit trail.</p>
<details class="identity"><summary>Artifact identity and provenance limits</summary>
<p>Policy: {POLICY}. Packet SHA-256: {report["packet_sha256"]}. Review digest: {report["review_digest"]}.</p>
<ul>{"".join(identities)}</ul><p>{escape(report["limits"])}</p></details></main></html>\n"""


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("review", "record", "verify-record"):
        child = sub.add_parser(command)
        child.add_argument("packet")
        child.add_argument("--as-of", help="ISO date; defaults to the current UTC date")
        if command == "review":
            child.add_argument("--format", choices=("markdown", "json", "html"), default="markdown")
        elif command == "record":
            child.add_argument("--reviewer", required=True)
            child.add_argument("--disposition", choices=STATUSES, required=True)
        else:
            child.add_argument("record")
    args = parser.parse_args(argv)
    try:
        report = assess(args.packet, calendar_date(args.as_of) if args.as_of else None)
        if args.command == "review":
            if args.format == "markdown":
                output = markdown(report)
            elif args.format == "html":
                output = html_report(report)
            else:
                output = json.dumps(report, indent=2, allow_nan=False)
            code = 0 if report["decision"] == "eligible_for_human_review" else 1
        elif args.command == "record":
            output = json.dumps(make_record(report, args.reviewer, args.disposition), indent=2)
            code = 0
        else:
            output = json.dumps(verify_record(report, decode(read_regular(Path(args.record)))), indent=2)
            code = 0
    except (PacketError, OSError, TypeError, OverflowError):
        print("Invalid or unreadable synthetic evidence. Check the documented contract.", file=sys.stderr)
        return 2
    print(output)
    return code


if __name__ == "__main__":
    sys.exit(main())
