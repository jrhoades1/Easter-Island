"""Round 5 Track B: CEIPP recheck leaves the headline counts unchanged.

Counts are recomputed from the vendored Barthel pages. MockProvider
only. No Barthel number is invented.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.round5b_ceipp import (
    CEIPP_LICENCE,
    CEIPP_SOURCE,
    OUTPUT_PATH,
    build_report,
)

DOC_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "decipherment"
    / "round5b_ceipp_recheck.md"
)
NOTICE_PATH = Path(__file__).resolve().parents[1] / "data" / "decipherment" / "CEIPP_NOTICE.txt"


class TestRound5bCeippRecheck(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = MockProvider()
        self.report = build_report(self.provider)

    def test_provider_is_unused_and_no_reading_is_assigned(self) -> None:
        self.assertEqual(self.provider.get_call_history(), [])
        self.assertEqual(self.report["provider_calls"], 0)
        self.assertFalse(self.report["readings_assigned"])
        self.assertEqual(self.report["adopted_corrections"], [])
        self.assertTrue(all(not row["adopted"] for row in self.report["disagreements"]))

    def test_headline_counts_do_not_move(self) -> None:
        before = self.report["stats_before"]
        after = self.report["stats_after"]
        self.assertEqual(before, after)
        self.assertEqual(before["calendar_040"], 28)
        self.assertEqual(before["calendar_040_before_152"], 13)
        self.assertEqual(before["calendar_040_after_152"], 13)
        self.assertEqual(before["calendar_040_gaps"], [2, 6, 3, 2, 5, 3, 5])
        self.assertEqual(before["calendar_full_delimiters"], 6)
        self.assertEqual(before["calendar_152"], 1)
        self.assertEqual(before["calendar_143"], 1)
        self.assertEqual(before["gv6_phrases"], 4)
        self.assertEqual(before["gv6_handoffs"], 3)
        self.assertEqual(before["staff_pure_999"], 96)
        self.assertEqual(before["staff_076_after_999"], 91)
        self.assertEqual(before["staff_076_after_999_rate"], 91 / 96)
        self.assertEqual(before["parallel_span"], 125)
        self.assertEqual(before["parallel_matches"], 107)
        self.assertEqual(before["parallel_mismatches"], 16)
        self.assertEqual(before["parallel_bird_substitutions"], 2)
        self.assertEqual(before["corpus_bird_substitutions"], 18)

    def test_saved_record_matches_the_recomputed_report(self) -> None:
        saved = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(saved, self.report)
        self.assertEqual(saved["geometry"]["calendar_040_tall_crescents"], 28)
        self.assertEqual(saved["geometry"]["staff_999_count"], 97)
        self.assertLess(saved["geometry"]["staff_999_width_max"], 8)

    def test_ceipp_credit_is_in_the_repo(self) -> None:
        doc = DOC_PATH.read_text(encoding="utf-8")
        notice = NOTICE_PATH.read_text(encoding="utf-8")
        self.assertIn(CEIPP_LICENCE, doc)
        self.assertIn(CEIPP_LICENCE, notice)
        self.assertIn("C.E.I.P.P.", doc)
        self.assertIn(CEIPP_SOURCE.split(",")[0], notice)
        self.assertIn("non-profit", self.report["licence"]["statement"])
        self.assertEqual(self.provider.get_call_history(), [])
