"""Meaningful offline checks for evidence separation and bounded local execution."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import contextlib
import io
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("aura_runtime", ROOT/"runtime/aura.py")
aura = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aura)


class ObserverRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.data = aura.read_json(ROOT/"runtime/examples/community-workshop.simulated.json")
        self.temp_root = (ROOT/".private/runtime-test-tmp").resolve()
        self.assertTrue(self.temp_root.is_relative_to(ROOT.resolve()))
        self.temp_root.mkdir(parents=True, exist_ok=True)

    def live_data(self):
        data = copy.deepcopy(self.data)
        for source in data["sources"]:
            source["local_model_permission"] = True
        return data

    @staticmethod
    def valid_transport(endpoint, model, packet, tokens, timeout):
        return {"claims": [{"text": "A tentative account based only on this packet.", "evidence_ids": packet["evidence_ids"][:1]}], "unknowns": ["Personal meaning remains for the participant to explain."], "questions": []}, min(tokens, 20)

    def test_exact_three_observers_and_separate_fourth_account(self):
        run = aura.prepare(self.data)
        self.assertEqual([p["observer_id"] for p in run["observer_packets"]], list(aura.OBSERVER_ROLES))
        self.assertEqual(run["fourth_account"]["role"], "user_meaning")
        self.assertEqual(len(run["fourth_account"]["records"]), 2)
        all_packet_ids = {e for p in run["observer_packets"] for e in p["evidence_ids"]}
        self.assertNotIn("E-participant-meaning", all_packet_ids)
        self.assertNotIn("E-participant-correction", all_packet_ids)

    def test_whole_world_information_is_not_in_attention_or_narrator(self):
        run = aura.prepare(self.data)
        packets = {p["observer_id"]: p for p in run["observer_packets"]}
        self.assertIn("Room B", packets["environment"]["prompt"])
        self.assertNotIn("Room B", packets["character_attention"]["prompt"])
        self.assertNotIn("Room B", packets["narrator"]["prompt"])
        self.assertEqual(packets["character_attention"]["evidence_ids"], ["E-attention-invitation"])

    def test_source_labels_and_cross_stream_references_cannot_leak_context(self):
        self.data["sources"][1]["label"] = "SECRET ROOM B LOCATION"
        self.data["sources"][1]["locator"] = "secret-world-fact"
        self.data["evidence"][1]["derived_from"] = ["E-world-room"]
        attention = aura.prepare(self.data)["observer_packets"][1]
        self.assertNotIn("SECRET ROOM B LOCATION", attention["prompt"])
        self.assertNotIn("secret-world-fact", attention["prompt"])
        self.assertNotIn("E-world-room", attention["prompt"])
        self.assertEqual(attention["payload"]["evidence"][0]["unavailable_reference_counts"]["derived_from"], 1)

    def test_conflict_correction_unknown_and_original_are_retained(self):
        run = aura.prepare(self.data)
        by_id = {e["id"]: e for e in run["original_evidence"]}
        self.assertIn("E-narrator-inference", by_id)
        self.assertEqual(by_id["E-participant-correction"]["supersedes"], ["E-narrator-inference"])
        self.assertEqual(run["unknowns"][0]["id"], "E-narrator-unknown")
        self.assertEqual(len(run["comparison_ledger"]), 2)
        self.assertIn("Tentative", by_id["E-narrator-inference"]["text"])

    def test_simulation_cannot_enter_real_records(self):
        self.data["record_mode"] = "real"
        with self.assertRaisesRegex(aura.ValidationError, "Simulation"):
            aura.prepare(self.data)

    def test_simulation_taint_cannot_be_laundered_through_derivation(self):
        self.data["evidence"][3]["is_simulated"] = False
        with self.assertRaisesRegex(aura.ValidationError, "Simulation provenance"):
            aura.prepare(self.data)

    def test_derived_claim_cannot_be_measured(self):
        self.data["evidence"][3]["evidence_class"] = "measured"
        with self.assertRaisesRegex(aura.ValidationError, "cannot become measured"):
            aura.prepare(self.data)

    def test_unknown_sources_and_future_corrections_rejected(self):
        bad = copy.deepcopy(self.data)
        bad["evidence"][0]["source_ids"] = ["MISSING"]
        with self.assertRaises(aura.ValidationError):
            aura.prepare(bad)
        bad = copy.deepcopy(self.data)
        bad["evidence"][0]["supersedes"] = ["E-participant-correction"]
        with self.assertRaisesRegex(aura.ValidationError, "earlier evidence"):
            aura.prepare(bad)

    def test_demo_is_deterministic_and_never_calls_network(self):
        with patch.object(aura, "build_opener", side_effect=AssertionError("Network must not be used")):
            first = aura.prepare(self.data, execute_mock=True)
            second = aura.prepare(self.data, execute_mock=True)
        self.assertEqual(first, second)
        self.assertFalse(first["network_used"])
        self.assertEqual(first["external_actions_executed"], [])
        self.assertTrue(all(t["allowed_tools"] == [] for t in first["swarm"]["tasks"]))
        self.assertTrue(all(a["status"] == "not_executed" for a in first["proposed_action_queue"]))
        self.assertEqual(first["swarm"]["completed_tasks"], 4)

    def test_swarm_budget_stops_dependencies_without_fake_completion(self):
        self.data["budget"]["max_swarm_tasks"] = 2
        run = aura.prepare(self.data, execute_mock=True)
        self.assertEqual(run["swarm"]["completed_tasks"], 2)
        self.assertEqual([t["status"] for t in run["swarm"]["tasks"]], ["completed_simulation", "completed_simulation", "budget_stopped", "budget_stopped"])
        self.assertNotIn("output", run["swarm"]["tasks"][2])

    def test_prompt_budget_prevents_model_calls(self):
        data = self.live_data()
        data["budget"]["max_prompt_chars"] = 1
        calls = []
        run = aura.run_local(data, "local-test", transport=lambda *args: calls.append(args))
        self.assertEqual(calls, [])
        self.assertFalse(run["network_used"])
        self.assertTrue(all(p["status"] == "budget_stopped" for p in run["observer_packets"]))

    def test_local_model_requires_explicit_source_permission(self):
        with self.assertRaisesRegex(aura.ValidationError, "local_model_permission"):
            aura.run_local(self.data, "local-test", transport=self.valid_transport)

    def test_local_model_derived_only_and_budget_stops(self):
        data = self.live_data()
        data["budget"]["max_model_calls"] = 1
        run = aura.run_local(data, "local-test", transport=self.valid_transport)
        self.assertEqual(run["local_model"]["calls"], 1)
        results = run["local_model"]["results"]
        self.assertEqual(results[0]["claims"][0]["evidence_class"], "derived")
        self.assertTrue(results[0]["claims"][0]["is_simulated"])
        self.assertEqual(results[1]["status"], "budget_stopped")
        self.assertEqual(run["export_permission"], "none")

    def test_local_model_cross_stream_citation_is_rejected(self):
        def adversarial(endpoint, model, packet, tokens, timeout):
            return {"claims": [{"text": "I know an inaccessible detail", "evidence_ids": ["E-participant-meaning"]}], "unknowns": [], "questions": []}, 4
        run = aura.run_local(self.live_data(), "local-test", transport=adversarial)
        self.assertTrue(all(r["status"] == "rejected_or_failed" for r in run["local_model"]["results"]))
        self.assertEqual(run["local_model"]["response_tokens_reserved_or_used"], 1536)

    def test_remote_cloud_and_redirect_endpoints_are_rejected(self):
        for endpoint in ["https://example.com", "http://127.0.0.1.evil.test", "http://127.0.0.1:11434/api/chat", "http://user:pass@localhost", "file:///tmp/model", "http://localhost/?redirect=x"]:
            with self.subTest(endpoint=endpoint):
                with self.assertRaises(aura.ValidationError):
                    aura.normalize_endpoint(endpoint)
        self.assertEqual(aura.normalize_endpoint("http://localhost:11434"), "http://127.0.0.1:11434")
        with self.assertRaises(aura.ValidationError):
            aura.run_local(self.live_data(), "model:cloud", transport=self.valid_transport)
        with self.assertRaises(aura.ValidationError):
            aura.NoRedirect().redirect_request(None, None, 302, "redirect", {}, "https://example.com")

    def test_unsupported_fields_and_duplicate_json_keys_are_rejected(self):
        self.data["execute_shell"] = "anything"
        with self.assertRaisesRegex(aura.ValidationError, "unsupported"):
            aura.prepare(self.data)
        with tempfile.TemporaryDirectory(dir=self.temp_root) as tmp:
            path = Path(tmp)/"bad.json"
            path.write_text('{"schema":1,"schema":2}', encoding="utf8")
            with self.assertRaisesRegex(aura.ValidationError, "Duplicate JSON"):
                aura.read_json(path)

    def test_existing_run_is_not_overwritten(self):
        with tempfile.TemporaryDirectory(dir=self.temp_root) as tmp:
            path = Path(tmp)/"run.json"
            aura.write_json(path, {"first": True})
            with self.assertRaises(aura.ValidationError):
                aura.write_json(path, {"first": False})
            self.assertEqual(json.loads(path.read_text()), {"first": True})

    def test_cli_invalid_input_returns_error_without_output(self):
        with tempfile.TemporaryDirectory(dir=self.temp_root) as tmp:
            source = Path(tmp)/"invalid.json"
            output = Path(tmp)/"should-not-exist.json"
            source.write_text('{"schema":"unsupported"}', encoding="utf8")
            errors = io.StringIO()
            with contextlib.redirect_stderr(errors):
                status = aura.main(["prepare", "--input", str(source), "--output", str(output)])
            self.assertEqual(status, 2)
            self.assertIn("Aura input/run error", errors.getvalue())
            self.assertFalse(output.exists())

    def test_real_evidence_can_be_prepared_without_becoming_measurement(self):
        real = {"schema": aura.INPUT_SCHEMA, "scenario_id": "actual-note", "title": "Participant's own note", "record_mode": "real", "sources": [{"id": "S-real", "label": "Own observation", "kind": "self_report", "locator": "private-note", "captured_at": "2026-11-10"}], "evidence": [{"id": "E-real", "stream": "user_meaning", "claim_kind": "self_report", "evidence_class": "reported", "is_simulated": False, "text": "I need to check which invitation I read.", "source_ids": ["S-real"], "observed_at": "2026-11-10"}]}
        run = aura.prepare(real)
        self.assertFalse(run["is_simulation"])
        self.assertEqual(run["fourth_account"]["records"][0]["evidence_class"], "reported")
        self.assertTrue(all(not p["evidence_ids"] for p in run["observer_packets"]))


if __name__ == "__main__":
    unittest.main()
