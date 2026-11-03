"""Evidence-boundary regressions. All examples and mutations are fictional."""

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "09-evals" / "pilot-review"
SPEC = importlib.util.spec_from_file_location("pilot_review", TOOL / "review.py")
review = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(review)
AS_OF = date(2026, 11, 3)


class EvidenceReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(TOOL / "examples" / "ready", self.root / "ready")
        self.packet = self.root / "ready" / "packet.json"

    def document(self):
        return json.loads(self.packet.read_text(encoding="utf-8"))

    def write(self, value):
        self.packet.write_text(json.dumps(value), encoding="utf-8")

    def mutate_artifact(self, criterion, change):
        packet = self.document()
        ref = next(ref for ref in packet["artifacts"] if ref["criterion_id"] == criterion)
        path = self.packet.parent / ref["path"]
        artifact = json.loads(path.read_text(encoding="utf-8"))
        change(artifact)
        path.write_text(json.dumps(artifact), encoding="utf-8")
        ref["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.write(packet)

    def assess(self):
        return review.assess(self.packet, AS_OF)

    def test_all_examples_have_expected_dispositions_and_never_authorize(self):
        for name, disposition in (
            ("ready", "eligible_for_human_review"),
            ("pause", "pause"),
            ("stop", "stop"),
            ("reported-incident", "stop"),
            ("resolve", "pause"),
        ):
            with self.subTest(name=name):
                report = review.assess(TOOL / "examples" / name / "packet.json", AS_OF)
                self.assertEqual(report["decision"], disposition)
                self.assertIs(report["authorization_granted"], False)
                self.assertIs(report["production_hold"], True)

    def test_resolve_snapshot_keeps_failures_and_original_observation_date(self):
        snapshot = (TOOL / "examples/resolve/published-report.json").read_bytes()
        self.assertEqual(
            hashlib.sha256(snapshot).hexdigest(),
            "d05c639ab7c424aff0fecc5c6a8cd53e17ee184d8d78aa6efa50bca3d548c114",
        )
        report = review.assess(TOOL / "examples/resolve/packet.json", AS_OF)
        row = report["artifacts"][0]
        self.assertEqual(row["metrics"], {"regression": "60/60", "paraphrases": "0/16", "specialist_misses": 5})
        self.assertEqual(row["observed_on"], "2026-09-24")
        self.assertEqual(row["status"], "stale")
        self.assertIs(row["checks_passed"], False)
        self.assertEqual(len(report["blockers"]), 4)

    def test_missing_criterion_and_missing_file_both_pause(self):
        packet = self.document()
        packet["artifacts"] = packet["artifacts"][1:]
        self.write(packet)
        (self.packet.parent / "privacy.json").unlink()
        report = self.assess()
        self.assertEqual(report["decision"], "pause")
        self.assertEqual([row["status"] for row in report["artifacts"][:2]], ["missing", "missing"])

    def test_modified_bytes_cannot_use_declared_old_hash(self):
        path = self.packet.parent / "routing.json"
        path.write_bytes(path.read_bytes() + b" ")
        row = self.assess()["artifacts"][0]
        self.assertEqual(row["reason"], "hash_mismatch")
        self.assertEqual(row["metrics"], {})

    def test_binding_changes_cannot_yield_eligible_report_even_with_new_hash(self):
        for key, value in (
            ("source_revision", "2" * 40),
            ("workflow_id", "other-workflow"),
            ("dataset_id", "other-dataset"),
            ("method_id", "other-method"),
            ("observed_on", "2026-11-01"),
            ("criterion_id", "privacy"),
            ("format", "resolve-rules-v1"),
        ):
            with self.subTest(key=key):
                original_packet = self.document()
                original = (self.packet.parent / "routing.json").read_bytes()
                self.mutate_artifact("routing", lambda artifact, k=key, v=value: artifact.update({k: v}))
                self.assertEqual(self.assess()["artifacts"][0]["reason"], "binding_mismatch")
                (self.packet.parent / "routing.json").write_bytes(original)
                self.write(original_packet)

    def test_dates_block_future_and_stale_evidence_with_boundary_inclusive(self):
        for as_of, expected in (
            (date(2026, 11, 1), "pause"),
            (date(2026, 12, 2), "eligible_for_human_review"),
            (date(2026, 12, 3), "pause"),
        ):
            with self.subTest(as_of=as_of):
                self.assertEqual(review.assess(self.packet, as_of)["decision"], expected)

    def test_present_assertions_do_not_clear_failed_evidence(self):
        packet = self.document()
        packet["assertions"] = dict.fromkeys(review.ASSERTIONS, "present")
        self.write(packet)
        self.mutate_artifact("reviewer_capacity", lambda a: a["results"].update(available_review_minutes=0))
        self.assertEqual(self.assess()["decision"], "pause")

    def test_zero_denominator_contradictory_counts_and_boolean_counts_pause(self):
        for values in ({"passed": 0, "total": 0}, {"passed": 13, "total": 12}, {"passed": True, "total": 12}):
            with self.subTest(values=values):
                self.mutate_artifact("routing", lambda a, v=values: a["results"].update(paraphrases=v))
                self.assertEqual(self.assess()["decision"], "pause")
                self.assertEqual(self.assess()["artifacts"][0]["status"], "invalid")

    def test_specialist_misses_cannot_exceed_failed_cases(self):
        self.mutate_artifact("routing", lambda a: a["results"].update(specialist_misses=1))
        self.assertEqual(self.assess()["artifacts"][0]["status"], "invalid")

    def test_failing_paraphrases_pause_despite_perfect_regression(self):
        self.mutate_artifact("routing", lambda a: a["results"].update(paraphrases={"passed": 11, "total": 12}))
        self.assertEqual(self.assess()["decision"], "pause")
        self.assertIs(self.assess()["artifacts"][0]["checks_passed"], False)

    def test_invalid_workload_values_do_not_become_capacity_passes(self):
        for value in (True, -1, float("inf"), float("nan"), "150", None, 10**400):
            with self.subTest(value_type=type(value).__name__):
                self.mutate_artifact(
                    "reviewer_capacity", lambda a, v=value: a["results"].update(available_review_minutes=v)
                )
                self.assertEqual(self.assess()["decision"], "pause")

    def test_zero_required_review_effort_is_invalid(self):
        self.mutate_artifact("reviewer_capacity", lambda a: a["results"].update(required_review_minutes=0))
        self.assertEqual(self.assess()["artifacts"][3]["status"], "invalid")

    def test_exposure_or_bypass_stops_even_with_other_evidence_missing(self):
        for criterion, field in (("privacy", "cross_user_exposures"), ("review_controls", "approval_bypasses")):
            with self.subTest(criterion=criterion):
                shutil.copytree(TOOL / "examples/ready", self.packet.parent, dirs_exist_ok=True)
                self.mutate_artifact(criterion, lambda a, f=field: a["results"].update({f: 1}))
                packet = self.document()
                packet["artifacts"] = [ref for ref in packet["artifacts"] if ref["criterion_id"] == criterion]
                self.write(packet)
                self.assertEqual(self.assess()["decision"], "stop")

    def test_stale_incident_evidence_does_not_clear_a_stop(self):
        self.mutate_artifact("privacy", lambda a: a["results"].update(cross_user_exposures=1))
        self.assertEqual(review.assess(self.packet, date(2026, 12, 3))["decision"], "stop")

    def test_reported_incident_overrides_missing_artifacts(self):
        packet = self.document()
        packet.update(artifacts=[], reported_incidents=["approval_bypass"])
        self.write(packet)
        self.assertEqual(self.assess()["decision"], "stop")

    def test_unknown_schema_fields_and_real_data_kind_are_rejected(self):
        for key, value in (
            ("schema_version", True),
            ("schema_version", 2),
            ("data_kind", "real"),
            ("employee_name", "FICTIONAL_PRIVATE_SENTINEL"),
            ("assertions", {"privacy_review": "approved"}),
        ):
            with self.subTest(key=key):
                packet = copy.deepcopy(self.document())
                original = self.packet.read_bytes()
                packet[key] = value
                self.write(packet)
                with self.assertRaises(review.PacketError):
                    self.assess()
                self.packet.write_bytes(original)

    def test_duplicate_criteria_paths_and_unsupported_formats_rejected(self):
        original = self.document()
        for change in (
            lambda p: p["artifacts"].append(copy.deepcopy(p["artifacts"][0])),
            lambda p: p["artifacts"][1].update(path=p["artifacts"][0]["path"]),
            lambda p: p["artifacts"][0].update(format="external-url"),
        ):
            packet = copy.deepcopy(original)
            change(packet)
            self.write(packet)
            with self.assertRaises(review.PacketError):
                self.assess()

    def test_path_traversal_absolute_urls_and_windows_paths_rejected(self):
        original = self.document()
        for path in (
            "../outside.json",
            "/tmp/outside.json",
            "https://example.invalid/evidence.json",
            "C:/outside.json",
            "sub\\outside.json",
            "sub/../routing.json",
            "sub//routing.json",
        ):
            with self.subTest(path=path):
                packet = copy.deepcopy(original)
                packet["artifacts"][0]["path"] = path
                self.write(packet)
                with self.assertRaises(review.PacketError):
                    self.assess()

    def test_symlinked_artifact_is_rejected(self):
        path = self.packet.parent / "linked.json"
        try:
            path.symlink_to(self.packet.parent / "routing.json")
        except OSError:
            self.skipTest("This system does not permit creating test symlinks")
        packet = self.document()
        packet["artifacts"][0]["path"] = path.name
        self.write(packet)
        with self.assertRaises(review.PacketError):
            self.assess()

    @unittest.skipUnless(hasattr(os, "mkfifo"), "Named pipe regression requires POSIX")
    def test_named_pipe_is_rejected_without_waiting_for_a_writer(self):
        path = self.root / "pipe.json"
        os.mkfifo(path)
        with self.assertRaises(review.PacketError):
            review.read_regular(path)

    def test_duplicate_json_deep_json_and_size_limits(self):
        for raw in (b'{"a":1,"a":2}', b"[" * 2000 + b"0" + b"]" * 2000, b'{"a":NaN}', b"\xff"):
            with self.subTest(raw_length=len(raw)), self.assertRaises(review.PacketError):
                review.decode(raw)
        self.packet.write_bytes(b" " * (review.MAX_BYTES + 1))
        with self.assertRaises(review.PacketError):
            self.assess()

    def test_malformed_artifact_and_unknown_keys_pause_without_echo(self):
        self.mutate_artifact("routing", lambda a: a.update(employee="FICTIONAL_PRIVATE_SENTINEL"))
        report = self.assess()
        self.assertEqual(report["decision"], "pause")
        self.assertNotIn("FICTIONAL_PRIVATE_SENTINEL", json.dumps(report))

    def test_record_matches_only_same_packet_artifacts_date_and_policy(self):
        report = self.assess()
        record = review.make_record(report, "reviewer-01", "eligible_for_human_review")
        self.assertIs(review.verify_record(report, record)["record_matches"], True)
        self.assertIs(review.verify_record(report, record)["authorization_granted"], False)
        for other in (review.assess(self.packet, date(2026, 11, 4)), {**report, "review_digest": "0" * 64}):
            with self.assertRaises(review.PacketError):
                review.verify_record(other, record)
        self.mutate_artifact("reviewer_capacity", lambda a: a["results"].update(available_review_minutes=160))
        with self.assertRaises(review.PacketError):
            review.verify_record(self.assess(), record)

    def test_record_cannot_claim_authorization_or_authenticated_identity(self):
        report = self.assess()
        original = review.make_record(report, "reviewer-01", "pause")
        for key, value in (
            ("authorization_granted", True),
            ("production_hold", False),
            ("simulated_identity", False),
            ("editable_record", False),
            ("schema_version", True),
            ("unknown_field", "fictional"),
        ):
            with self.subTest(key=key):
                record = {**original, key: value}
                with self.assertRaises(review.PacketError):
                    review.verify_record(report, record)

    def test_no_disposition_clears_missing_evidence_or_stop(self):
        for name, disposition in (
            ("pause", "eligible_for_human_review"),
            ("stop", "pause"),
            ("stop", "eligible_for_human_review"),
            ("ready", "approved"),
        ):
            with self.subTest(name=name, disposition=disposition):
                report = review.assess(TOOL / "examples" / name / "packet.json", AS_OF)
                with self.assertRaises(review.PacketError):
                    review.make_record(report, "reviewer-01", disposition)

    def test_real_names_cannot_be_used_as_reviewer_ids(self):
        with self.assertRaises(review.PacketError):
            review.make_record(self.assess(), "Fictional Person", "pause")

    def test_resolve_adapter_rejects_contradictory_counts_and_false_recency(self):
        shutil.copytree(TOOL / "examples/resolve", self.packet.parent, dirs_exist_ok=True)
        original_packet = self.document()
        original_artifact = (self.packet.parent / "routing.json").read_bytes()
        changes = (
            lambda a: a["results"]["holdout"].update(passed=16),
            lambda a: a["results"]["categories"].pop(next(iter(a["results"]["categories"]))),
            lambda a: a["results"].update(pass_rate=0),
            lambda a: a["results"].update(generated_at="2026-11-02T00:00:00+00:00"),
            lambda a: a["results"]["holdout"]["cases"][0].update(passed=True),
        )
        for change in changes:
            self.write(original_packet)
            (self.packet.parent / "routing.json").write_bytes(original_artifact)
            self.mutate_artifact("routing", change)
            self.assertEqual(self.assess()["artifacts"][0]["status"], "invalid")

    def test_html_escapes_content_and_uses_no_remote_dependencies(self):
        report = self.assess()
        report["workflow_id"] = '<script>alert("fictional")</script>'
        html = review.html_report(report)
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
        self.assertNotIn("<script src", html)
        self.assertIn("default-src 'none'", html)

    def test_cli_exit_codes_reports_and_simulated_record_cycle(self):
        def cli(*args):
            return subprocess.run(
                [sys.executable, str(TOOL / "review.py"), *args], capture_output=True, text=True, check=False
            )

        before = {path: path.read_bytes() for path in self.packet.parent.iterdir()}
        result = cli("review", str(self.packet), "--as-of", "2026-11-03", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIs(json.loads(result.stdout)["authorization_granted"], False)
        for name in ("pause", "stop", "resolve"):
            result = cli("review", str(TOOL / "examples" / name / "packet.json"), "--as-of", "2026-11-03")
            self.assertEqual(result.returncode, 1, result.stderr)
        record = cli(
            "record",
            str(self.packet),
            "--as-of",
            "2026-11-03",
            "--reviewer",
            "reviewer-01",
            "--disposition",
            "eligible_for_human_review",
        )
        self.assertEqual(record.returncode, 0, record.stderr)
        record_path = self.root / "record.json"
        record_path.write_text(record.stdout, encoding="utf-8")
        checked = cli("verify-record", str(self.packet), str(record_path), "--as-of", "2026-11-03")
        self.assertEqual(checked.returncode, 0, checked.stderr)
        self.assertIs(json.loads(checked.stdout)["record_matches"], True)
        self.assertEqual(before, {path: path.read_bytes() for path in self.packet.parent.iterdir()})
        self.packet.write_text('{"name":"FICTIONAL_PRIVATE_SENTINEL"}', encoding="utf-8")
        invalid = cli("review", str(self.packet), "--as-of", "2026-11-03")
        self.assertEqual(invalid.returncode, 2)
        self.assertEqual(invalid.stdout, "")
        self.assertNotIn("FICTIONAL_PRIVATE_SENTINEL", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
