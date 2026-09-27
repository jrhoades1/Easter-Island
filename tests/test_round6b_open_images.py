"""Round 6 Track B: open-image survey leaves the headline counts unchanged.

MockProvider only. No Barthel number is invented. No photograph is committed.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.round6b_open_images import (
    CLASS_CC_BY,
    CLASS_CC0,
    OUTPUT_PATH,
    build_report,
)

DOC_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "decipherment"
    / "round6b_open_images.md"
)


class TestRound6bOpenImages(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = MockProvider()
        self.report = build_report(self.provider)

    def test_provider_is_unused_and_no_reading_is_assigned(self) -> None:
        self.assertEqual(self.provider.get_call_history(), [])
        self.assertEqual(self.report["provider_calls"], 0)
        self.assertFalse(self.report["readings_assigned"])
        self.assertEqual(self.report["adopted_corrections"], [])
        self.assertEqual(self.report["disagreements"], [])
        self.assertFalse(self.report["recheck"]["performed"])
        self.assertFalse(self.report["images_committed"])

    def test_no_holder_stated_cc0_or_cc_by_frame_was_sharp_enough(self) -> None:
        codes = [row["code"] for row in self.report["objects"]]
        self.assertEqual(codes, list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        for row in self.report["objects"]:
            self.assertFalse(row["rechecked"])
            self.assertFalse(row["cc0_or_cc_by"])
            self.assertFalse(row["sharp_enough_for_sign_detail"])
            self.assertNotIn(row["license_class"], {CLASS_CC0, CLASS_CC_BY})

    def test_headline_counts_do_not_move(self) -> None:
        before = self.report["stats_before"]
        after = self.report["stats_after"]
        self.assertEqual(before, after)
        self.assertEqual(before["calendar_040"], 28)
        self.assertEqual(before["calendar_040_before_152"], 13)
        self.assertEqual(before["calendar_040_after_152"], 13)
        self.assertEqual(before["calendar_040_gaps"], [2, 6, 3, 2, 5, 3, 5])
        self.assertEqual(before["calendar_full_delimiters"], 6)
        self.assertEqual(before["gv6_phrases"], 4)
        self.assertEqual(before["gv6_handoffs"], 3)
        self.assertEqual(before["staff_pure_999"], 96)
        self.assertEqual(before["staff_076_after_999"], 91)
        self.assertEqual(before["parallel_span"], 125)
        self.assertEqual(before["parallel_matches"], 107)
        self.assertEqual(before["parallel_mismatches"], 16)
        self.assertEqual(before["parallel_bird_substitutions"], 2)
        self.assertEqual(before["corpus_bird_substitutions"], 18)

    def test_saved_record_matches_the_recomputed_report(self) -> None:
        saved = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(saved, self.report)

    def test_holder_statements_are_quoted_in_the_note(self) -> None:
        doc = DOC_PATH.read_text(encoding="utf-8")
        by_code = {row["code"]: row for row in self.report["objects"]}
        self.assertIn("Claudia Obrocki CC BY-NC-SA 4.0", doc)
        self.assertIn(by_code["O"]["license_as_stated"], doc)
        self.assertIn("All Rights Reserved", doc)
        self.assertIn("all rights reserved", doc.lower())
        self.assertIn("There are restrictions for re-using this media.", doc)
        self.assertIn("private purposes", doc)
        self.assertIn("MockProvider", doc)
        self.assertEqual(self.provider.get_call_history(), [])
