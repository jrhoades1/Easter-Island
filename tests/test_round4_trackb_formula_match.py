"""Round 4 Track B: structural match of sign units to Rapanui formulas.

The corpus case retrains the Great Tradition segmenter and the shuffle
nulls. MockProvider only. No reading is adopted.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.round4_trackb import (
    ADOPT_FRACTION,
    CHILD_TTR_MIN,
    DOC_PATH,
    HANDOFF_MIN_LINKS,
    JSON_PATH,
    MIN_FAMILY,
    PRIMARY_PAIRS,
    SKELETON_MIN_CYCLES,
    SKELETON_TTR_MIN,
    ZIPF_SLOPE_TOLERANCE,
    best_tile_run,
    burstiness,
    histogram_l1,
    line_has_chant_tile,
    longest_handoff,
    run_round4_trackb,
)
from decipherment.track3_genealogy import chain_links, extract_strict_phrases

DOC = Path(DOC_PATH)
JSON = Path(JSON_PATH)


class TestRound4StructureHelpers(unittest.TestCase):
    """Small constructions. No corpus shuffle."""

    def test_provider_must_be_mock(self):
        with self.assertRaises(TypeError):
            run_round4_trackb(object())

    def test_burstiness_is_regular_when_gaps_are_equal(self):
        self.assertAlmostEqual(burstiness([3, 3, 3, 3]), -1.0)
        self.assertIsNone(burstiness([3]))
        uneven = burstiness([1, 1, 1, 30])
        self.assertIsNotNone(uneven)
        self.assertGreater(uneven, 0)

    def test_handoff_finds_a_three_link_chain_and_rejects_a_repeated_child(self):
        line = ["A", "b", "c", "A", "c", "d", "A", "d", "e", "A", "e", "f"]
        self.assertEqual(longest_handoff(line), 3)
        repeated = ["A", "b", "b", "A", "b", "b", "A", "b", "b", "A", "b", "c"]
        self.assertEqual(longest_handoff(repeated, CHILD_TTR_MIN), 0)
        self.assertLess(HANDOFF_MIN_LINKS, 4)

    def test_tile_needs_four_diverse_cycles(self):
        line = []
        for index in range(4):
            line.extend(["D1", f"a{index}", "D2", f"b{index}"])
        self.assertEqual(len(best_tile_run(line, "D1", "D2")), 4)
        self.assertTrue(line_has_chant_tile(line))
        copied = []
        for _index in range(4):
            copied.extend(["D1", "a", "D2", "b"])
        self.assertFalse(line_has_chant_tile(copied))
        self.assertEqual(SKELETON_MIN_CYCLES, 4)
        self.assertEqual(SKELETON_TTR_MIN, 0.75)

    def test_histogram_distance_is_zero_for_the_same_counts(self):
        from collections import Counter

        left = Counter({3: 5, 4: 1})
        self.assertEqual(histogram_l1(left, left), 0.0)
        self.assertIsNone(histogram_l1(Counter(), left))

    def test_gv6_extractor_still_chains_the_published_groups(self):
        groups = [
            "200",
            "000!",
            "280.076",
            "200",
            "280",
            "730.076",
            "200",
            "730",
            "517a.076",
            "200",
            "517a",
            "222.076",
        ]
        phrases = extract_strict_phrases(groups, "Gv6")
        self.assertEqual(len(phrases), 4)
        self.assertEqual(chain_links(phrases), 3)

    def test_thresholds_stay_at_the_preregistered_values(self):
        self.assertEqual(MIN_FAMILY, 8)
        self.assertEqual(ZIPF_SLOPE_TOLERANCE, 0.15)
        self.assertEqual(ADOPT_FRACTION, 0.05)
        self.assertEqual(len(PRIMARY_PAIRS), 14)


class TestRound4TrackB(unittest.TestCase):
    """Locked measurements. One corpus run, shared by the methods."""

    @classmethod
    def setUpClass(cls):
        cls.provider = MockProvider()
        cls.result = run_round4_trackb(cls.provider)

    def test_provider_is_unused_and_no_reading(self):
        self.assertEqual(self.provider.name, "mock")
        self.assertEqual(self.provider.get_call_history(), [])
        self.assertEqual(self.result["provider_calls"], 0)
        self.assertIsNone(self.result["reading"])
        self.assertEqual(self.result["signs"]["types"], 267)
        self.assertEqual(self.result["language"]["formula_types"], 577)
        for unit in self.result["signs"]["top"]:
            self.assertIsNone(unit["reading"])

    def test_gv6_handoff_is_the_published_one(self):
        gv6 = self.result["genealogy"]["gv6"]
        self.assertEqual(gv6["phrases"], 4)
        self.assertEqual(gv6["links"], 3)
        self.assertEqual(self.result["genealogy"]["bracket_by_side"]["Gv"]["links"], 3)
        self.assertEqual(self.result["chant"]["verses"], 48)

    def test_match_flags_follow_the_p_values(self):
        bonferroni = self.result["matches"]["bonferroni"]
        self.assertAlmostEqual(bonferroni, round(0.05 / 14, 6), places=6)
        any_match = False
        for row in self.result["matches"]["pairs"]:
            self.assertEqual(row["trials"], 400)
            if not row["tested"]:
                self.assertFalse(row["match"])
                continue
            self.assertGreaterEqual(row["sign_p"], 0.0)
            self.assertLessEqual(row["sign_p"], 1.0)
            expected = row["sign_p"] <= bonferroni and row["language_p"] <= bonferroni
            self.assertEqual(row["match"], expected)
            any_match = any_match or row["match"]
        zipf = self.result["matches"]["zipf"]
        if zipf["match"]:
            self.assertLessEqual(zipf["absolute_gap_signs_formulas"], ZIPF_SLOPE_TOLERANCE)
            self.assertLessEqual(zipf["p"], ADOPT_FRACTION)
        self.assertEqual(self.result["matches"]["any_match"], any_match or zipf["match"])

    def test_files_state_the_verdict_in_plain_english(self):
        self.assertTrue(JSON.is_file())
        self.assertTrue(DOC.is_file())
        note = DOC.read_text(encoding="utf-8")
        self.assertIn("MockProvider", note)
        self.assertIn("Verdict", note)
        if self.result["verdict_code"] == "no_match":
            self.assertIn("nothing matches", note.lower())
        if self.result["verdict_code"] == "spacing_only":
            self.assertIn("not a reading", note.lower())
            self.assertIn("do not match", note.lower())
        self.assertIn("Fischer", note)
        self.assertIn("Guy", note)
        self.assertIn("Barthel", note)
        self.assertIn("Thomson", note)
        self.assertIn(self.result["verdict"][:40], note)
        self.assertNotIn("reading is tangata", note.lower())
