"""Round 4 Track A: cited pictographs, class co-occurrence, rebus nulls.

Counts are recomputed from the vendored Barthel pages and the Rapanui
corpus. MockProvider only. No invented sign number. No adopted translation.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.round4_tracka import (
    ADOPT_FRACTION,
    CONTEXT_NAMES,
    HAND_ALIAS,
    OMITTED,
    PAIR_SEED,
    PAIR_TRIALS,
    PICTOGRAPHS,
    REBUS_SEED_R1,
    REBUS_SEED_R2,
    REBUS_TRIALS,
    SLOT_SEED,
    SLOT_TRIALS,
    TESTABLE_CLASSES,
    class_of,
    render_round4_tracka,
    run_round4_tracka,
    write_round4_outputs,
)

DOC_PATH = Path(__file__).resolve().parents[1] / "docs" / "decipherment" / "round4a_pictograph_rebus.md"
JSON_PATH = Path(__file__).resolve().parents[1] / "data" / "decipherment" / "round4a_pictograph_rebus.json"

WORD_LABELS = {"", "HYPOTHESIS", "published_hypothesis", "contested"}


class PictographTableTests(unittest.TestCase):
    """The table is a citation list. These checks do not shuffle the corpus."""

    def test_every_row_has_a_source_and_a_legal_word_label(self):
        stems = [row.stem for row in PICTOGRAPHS]
        self.assertEqual(len(stems), len(set(stems)))
        for row in PICTOGRAPHS:
            self.assertGreater(len(row.source), 40, row.stem)
            self.assertIn(row.word_label, WORD_LABELS)
            self.assertEqual(len(row.stem), 3)
            self.assertTrue(row.stem.isdigit())
            if row.word_label == "":
                self.assertEqual(row.word, "")
            else:
                self.assertNotEqual(row.word, "")

    def test_canoe_and_turtle_are_not_given_a_sign(self):
        pictures = {item["picture"] for item in OMITTED}
        self.assertIn("canoe", pictures)
        self.assertIn("sea turtle", pictures)
        self.assertNotIn("280", {row.stem for row in PICTOGRAPHS})

    def test_class_overrides(self):
        self.assertIsNone(class_of("042"))
        self.assertEqual(class_of("040"), "moon")
        self.assertEqual(class_of("041"), "moon")
        self.assertEqual(class_of("143"), "moon")
        self.assertEqual(class_of("152"), "moon")
        self.assertEqual(class_of("760"), "lizard")
        self.assertEqual(class_of("730"), "sea")
        self.assertEqual(class_of("700"), "sea")
        self.assertEqual(class_of("400"), "bird")
        self.assertEqual(class_of("409"), "bird")
        self.assertEqual(class_of("410"), None)
        self.assertEqual(class_of("600"), "bird")
        self.assertEqual(class_of("200"), "human")
        self.assertEqual(class_of("300"), "human_gaping")
        self.assertEqual(class_of("006"), "hand")
        self.assertEqual(class_of("064"), "hand")
        self.assertEqual(class_of("001"), None)
        self.assertEqual(class_of("076"), None)
        self.assertEqual(class_of("067"), "plant")
        self.assertEqual(HAND_ALIAS, {"064": "006"})

    def test_provider_must_be_mock(self):
        with self.assertRaises(TypeError):
            run_round4_tracka(object())


class Round4TrackARunTests(unittest.TestCase):
    """One corpus run. The gates were fixed in the module before this count."""

    @classmethod
    def setUpClass(cls):
        cls.result = run_round4_tracka(MockProvider())
        write_round4_outputs(cls.result)

    def test_preregistered_constants(self):
        self.assertEqual((PAIR_TRIALS, PAIR_SEED), (500, 40))
        self.assertEqual((SLOT_TRIALS, SLOT_SEED), (500, 41))
        self.assertEqual((REBUS_TRIALS, REBUS_SEED_R1, REBUS_SEED_R2), (500, 42, 43))
        self.assertEqual(ADOPT_FRACTION, 0.05)
        self.assertEqual(CONTEXT_NAMES, ("calendar", "gv6", "parallels"))
        self.assertEqual(TESTABLE_CLASSES, ("moon", "hand", "bird", "sea", "human", "human_gaping"))

    def test_provider_and_no_translation_claim(self):
        self.assertEqual(self.result["provider"], "mock")
        self.assertEqual(self.result["provider_calls"], 0)
        self.assertEqual(self.result["reading"], "R1")
        note = render_round4_tracka(self.result)
        self.assertIn("Nothing here is a translation of a tablet.", note)
        self.assertIn("Gv6 has 0 mapped windows.", note)

    def test_neighbor_gate_fails_and_two_apart_is_secondary(self):
        semantic = self.result["semantic_cooccurrence"]
        self.assertEqual(semantic["observed"], 303)
        self.assertEqual(semantic["null_ge"], 389)
        self.assertFalse(semantic["holds"])
        self.assertEqual(semantic["step2"]["observed"], 394)
        self.assertEqual(semantic["step2"]["null_ge"], 0)
        self.assertFalse(semantic["step2"]["gated"])
        self.assertTrue(semantic["step2"]["holds_if_it_were_gated"])
        by_name = {item["class"]: item for item in semantic["step2"]["by_class"]}
        self.assertEqual(by_name["bird"]["null_ge"], 0)
        self.assertEqual(by_name["human"]["null_ge"], 0)
        self.assertGreater(by_name["sea"]["null_fraction"], 0.05)
        outside = self.result["semantic_cooccurrence_calendar_removed"]
        self.assertEqual(outside["observed"], 301)
        self.assertFalse(outside["holds"])
        self.assertEqual(outside["step2"]["null_ge"], 0)

    def test_cross_hundred_signal_is_the_bird_pairing(self):
        slots = self.result["parallel_slots"]
        cross = slots["cross_hundred"]
        self.assertEqual(slots["alignment"]["passages"], 99)
        self.assertEqual(cross["observed"], 18)
        self.assertEqual(cross["classified_pairs"], 34)
        self.assertEqual(cross["null_ge"], 23)
        self.assertTrue(cross["holds"])
        self.assertEqual(self.result["cross_hundred_by_class"], {"bird": 18})
        signs = {tuple(item["signs"]) for item in self.result["cross_hundred_pairs"]}
        self.assertIn(("400", "600"), signs)
        for pair in signs:
            self.assertTrue(pair[0].startswith("4") or pair[1].startswith("4"))
            self.assertTrue(pair[0].startswith("6") or pair[1].startswith("6"))

    def test_rebus_rates(self):
        r1 = self.result["rebus_r1"]
        r2 = self.result["rebus_r2"]
        self.assertEqual(r1["windows"], 85)
        self.assertEqual(r1["hits"], 44)
        self.assertEqual(r1["null_ge"], 4)
        self.assertEqual(r1["diverse_hits"], 15)
        self.assertEqual(r1["diverse_null_ge"], 15)
        self.assertTrue(r1["adopted"])
        contexts = {item["context"]: item for item in r1["contexts"]}
        self.assertEqual(contexts["calendar"]["hits"], 16)
        self.assertEqual(contexts["calendar"]["diverse_hits"], 0)
        self.assertFalse(contexts["calendar"]["holds_bonferroni"])
        self.assertEqual(contexts["gv6"]["windows"], 0)
        self.assertEqual(contexts["parallels"]["hits"], 28)
        self.assertEqual(contexts["parallels"]["null_ge"], 8)
        self.assertTrue(contexts["parallels"]["holds_bonferroni"])
        self.assertEqual(r2["hits"], 46)
        self.assertEqual(r2["null_ge"], 6)
        self.assertFalse(r2["adopted"])
        phrases = [item["groups"] for item in self.result["gv6_phrases_r1"] if item["kind"] == "strict"]
        self.assertEqual(len(phrases), 4)

    def test_written_report_matches_the_run(self):
        self.assertTrue(JSON_PATH.is_file())
        self.assertTrue(DOC_PATH.is_file())
        text = DOC_PATH.read_text(encoding="utf-8")
        self.assertIn("fraction 0.778", text)
        self.assertIn("fraction 0.008", text)
        self.assertIn("fraction 0.046", text)
        self.assertIn("fraction 0.000", text)
        self.assertIn("HYPOTHESIS", text)
        self.assertNotIn("honu", text.split("sea turtle")[0])
