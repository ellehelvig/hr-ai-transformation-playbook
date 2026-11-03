"""Offline preflight for synthetic pilot evidence. Caller assertions are not verified approvals."""

import argparse
import json
import math
from pathlib import Path


BASE_EVIDENCE = (
    "tool_data_scope", "operator_owner", "baseline", "independent_evaluation",
    "reviewer_capacity", "human_channel", "incident_owner",
)
ROLLOUT_EVIDENCE = ("identity_access_review", "privacy_review", "technical_review")
INCIDENTS = ("cross_user_exposure", "approval_bypass")
EFFORT_FIELDS = ("baseline_minutes", "preparation_minutes", "review_minutes", "rework_minutes", "escalation_minutes")
MAX_BYTES = 65536


def _object(value, allowed, label):
    if not isinstance(value, dict) or set(value) - set(allowed):
        raise ValueError(f"{label}: expected an object with only documented fields")


def _number(value):
    if type(value) not in (int, float):
        raise ValueError("effort: expected finite nonnegative numbers")
    try:
        valid = math.isfinite(value) and value >= 0
    except OverflowError:
        valid = False
    if not valid:
        raise ValueError("effort: expected finite nonnegative numbers")
    return value


def assess(payload):
    """Return advisory gaps, never permission to deploy or an employment decision."""
    _object(payload, ("schema_version", "data_kind", "stage", "evidence", "incidents", "effort"), "input")
    if type(payload.get("schema_version")) is not int or payload["schema_version"] != 1:
        raise ValueError("schema_version: expected integer 1")
    if payload.get("data_kind") != "synthetic":
        raise ValueError("data_kind: synthetic inputs only")
    stage = payload.get("stage")
    if stage not in ("rehearsal", "rollout_review"):
        raise ValueError("stage: expected rehearsal or rollout_review")
    evidence = payload.get("evidence", {})
    _object(evidence, BASE_EVIDENCE + ROLLOUT_EVIDENCE, "evidence")
    if any(value not in ("present", "missing", "unknown") for value in evidence.values()):
        raise ValueError("evidence: expected present, missing, or unknown")
    incidents = payload.get("incidents", {})
    _object(incidents, INCIDENTS, "incidents")
    if any(value not in ("clear", "reported", "unknown") for value in incidents.values()):
        raise ValueError("incidents: expected clear, reported, or unknown")

    effort = payload.get("effort")
    capacity = None
    if "effort" in payload:
        _object(effort, ("case_count",) + EFFORT_FIELDS, "effort")
        if set(effort) != {"case_count", *EFFORT_FIELDS}:
            raise ValueError("effort: supply case_count and every documented effort component")
        count = effort["case_count"]
        if type(count) is not int or count < 0:
            raise ValueError("case_count: expected a nonnegative integer")
        _number(count)
        values = {key: _number(effort[key]) for key in EFFORT_FIELDS}
        assisted = _number(sum(values[key] for key in EFFORT_FIELDS if key != "baseline_minutes"))
        try:
            capacity = count * (values["baseline_minutes"] - assisted) / 60
        except OverflowError as exc:
            raise ValueError("effort: calculation exceeds finite range") from exc
        if not math.isfinite(capacity):
            raise ValueError("effort: calculation exceeds finite range")

    required = BASE_EVIDENCE + (ROLLOUT_EVIDENCE if stage == "rollout_review" else ())
    gaps = [key for key in required if evidence.get(key) != "present"]
    unresolved = [key for key in INCIDENTS if incidents.get(key) != "clear"]
    reported = [key for key in INCIDENTS if incidents.get(key) == "reported"]
    status = "stop_affected_processing" if reported else "pause_for_evidence" if gaps or unresolved else "human_review"
    return {
        "advisory_status": status,
        "human_review_required": True,
        "authorization_granted": False,
        "evidence_gaps": gaps,
        "unresolved_incidents": unresolved,
        "reported_incidents": reported,
        "illustrative_net_capacity_hours": capacity,
        "limits": "Caller assertions only. No verification, deployment approval, savings, or headcount conclusion.",
    }


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("input: duplicate JSON keys are not allowed")
        result[key] = value
    return result


def load_input(path):
    with Path(path).open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("input: exceeds 64 KiB limit")
    try:
        return json.loads(raw, object_pairs_hook=_unique_object)
    except (json.JSONDecodeError, UnicodeDecodeError, RecursionError) as exc:
        raise ValueError("input: invalid JSON") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Local synthetic JSON file; no network or writes")
    args = parser.parse_args()
    try:
        result = assess(load_input(args.input))
    except (ValueError, OSError):
        # Avoid echoing rejected fields, contents, or paths into logs.
        parser.exit(2, "Invalid or unreadable synthetic input. Check the documented schema.\n")
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
