"""Rebuild fictional packets; preserve the separately sourced Resolve report snapshot."""

import hashlib
import json
from pathlib import Path

from review import CRITERIA

ROOT = Path(__file__).parent / "examples"


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(value, indent=2, allow_nan=False) + "\n").encode("utf-8"))


def build(name, results, *, reported=()):
    directory = ROOT / name
    packet = {
        "schema_version": 1,
        "data_kind": "synthetic",
        "packet_id": f"fictional-{name}",
        "workflow_id": "fictional-policy-lookup",
        "source_revision": "1" * 40,
        "artifacts": [],
        "assertions": {"privacy_review": "unknown", "identity_access_review": "unknown", "technical_review": "present"},
        "reported_incidents": list(reported),
    }
    for criterion in CRITERIA:
        if criterion not in results:
            continue
        artifact = {
            "schema_version": 1,
            "data_kind": "synthetic",
            "criterion_id": criterion,
            "workflow_id": packet["workflow_id"],
            "source_revision": packet["source_revision"],
            "dataset_id": f"fictional-{criterion.replace('_', '-')}-v1",
            "method_id": "fictional-rehearsal-v1",
            "observed_on": "2026-11-02",
            "format": "checks-v1",
            "results": results[criterion],
        }
        path = directory / f"{criterion}.json"
        write_json(path, artifact)
        packet["artifacts"].append(
            {key: artifact[key] for key in ("criterion_id", "dataset_id", "method_id", "observed_on", "format")}
        )
        packet["artifacts"][-1].update(path=path.name, sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    write_json(directory / "packet.json", packet)


def main():
    passing = {
        "routing": {
            "regression": {"passed": 20, "total": 20},
            "paraphrases": {"passed": 12, "total": 12},
            "specialist_misses": 0,
        },
        "privacy": {"tested_cases": 12, "cross_user_exposures": 0},
        "review_controls": {"tested_cases": 12, "approval_bypasses": 0},
        "reviewer_capacity": {"case_count": 12, "required_review_minutes": 120, "available_review_minutes": 150},
    }
    build("ready", passing)
    build(
        "pause",
        {
            key: value
            if key != "reviewer_capacity"
            else {"case_count": 12, "required_review_minutes": 120, "available_review_minutes": 60}
            for key, value in passing.items()
            if key != "review_controls"
        },
    )
    build("stop", {**passing, "privacy": {"tested_cases": 12, "cross_user_exposures": 1}})
    build("reported-incident", {}, reported=("approval_bypass",))

    # This is a preserved public report, not newly generated evaluation or new model evidence.
    report = json.loads((ROOT / "resolve" / "published-report.json").read_text(encoding="utf-8"))
    artifact = {
        "schema_version": 1,
        "data_kind": "synthetic",
        "criterion_id": "routing",
        "workflow_id": "resolve-rules",
        "source_revision": "074246e4e026e310e16616b11b44f3fe73cd5a59",
        "dataset_id": "resolve-published-cases-v1",
        "method_id": "resolve-rules-evaluation-v1",
        "observed_on": "2026-09-24",
        "format": "resolve-rules-v1",
        "results": report,
    }
    path = ROOT / "resolve" / "routing.json"
    write_json(path, artifact)
    packet = {
        "schema_version": 1,
        "data_kind": "synthetic",
        "packet_id": "resolve-published-review",
        "workflow_id": artifact["workflow_id"],
        "source_revision": artifact["source_revision"],
        "artifacts": [
            {key: artifact[key] for key in ("criterion_id", "dataset_id", "method_id", "observed_on", "format")}
        ],
        "assertions": {},
        "reported_incidents": [],
    }
    packet["artifacts"][0].update(path=path.name, sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    write_json(ROOT / "resolve" / "packet.json", packet)


if __name__ == "__main__":
    main()
