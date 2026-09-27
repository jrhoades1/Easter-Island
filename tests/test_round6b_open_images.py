"""Round 6 Track B: open-image survey leaves the headline counts unchanged.

Licenses in the record are the ones written into the survey module from
holder pages. MockProvider only. No Barthel number is invented.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.round6b_open_images import (
    DISAGREEMENT_FIELDS,
    DOC_PATH,
    OUTPUT_PATH,
    build_report,
)

README_PATH = Path(__file__).resolve().parents[1] / "docs" / "decipherment" / "README.md"


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
        self.assertEqual(self.report["disagreement_record_fields"], DISAGREEMENT_FIELDS)
        self.assertIn("adopted", DISAGREEMENT_FIELDS)
        self.assertFalse(self.report["images_committed"])
        self.assertEqual(self.report["images_downloaded_for_recheck"], [])

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

    def test_corpus_and_the_named_objects(self) -> None:
        signs = [row["sign"] for row in self.report["objects"]]
        self.assertEqual(signs, list("ABCDEFGHIJKLMNOPQRSTUVWXY"))
        by_sign = {row["sign"]: row for row in self.report["objects"]}
        self.assertEqual(by_sign["O"]["holder_license"], "CC BY-NC-SA 4.0")
        self.assertFalse(by_sign["O"]["open_cc0_or_cc_by"])
        self.assertFalse(by_sign["O"]["used_for_sign_recheck"])
        self.assertEqual(by_sign["G"]["holder_license"], "CC0 1.0")
        self.assertTrue(by_sign["G"]["open_cc0_or_cc_by"])
        self.assertFalse(by_sign["G"]["used_for_sign_recheck"])
        self.assertEqual(by_sign["H"]["holder_license"], "CC0 1.0")
        self.assertFalse(by_sign["H"]["used_for_sign_recheck"])
        self.assertEqual(by_sign["I"]["holder_license"], "CC BY-NC-SA 4.0")
        self.assertFalse(by_sign["I"]["open_cc0_or_cc_by"])
        self.assertEqual(by_sign["R"]["holder_license"], "Not determined")
        self.assertEqual(by_sign["S"]["holder_license"], "Not determined")
        self.assertFalse(by_sign["C"]["used_for_sign_recheck"])
        self.assertTrue(all(not row["used_for_sign_recheck"] for row in self.report["objects"]))
        self.assertTrue(all(not row["images_committed"] for row in self.report["objects"]))

    def test_berlin_and_santiago_addresses_are_in_the_record_and_the_note(self) -> None:
        berlin = self.report["contacts"]["berlin"]["emails"]
        santiago = self.report["contacts"]["santiago"]["emails"]
        self.assertEqual(berlin["photo_archive"], "photo-em@smb.spk-berlin.de")
        self.assertEqual(berlin["object_record_and_general_research"], "em@smb.spk-berlin.de")
        self.assertEqual(santiago["collections_administrator"], "yasna.sepulveda@mnhn.gob.cl")
        self.assertEqual(santiago["curatorial_head"], "cristian.becker@mnhn.gob.cl")
        doc = DOC_PATH.read_text(encoding="utf-8")
        for address in (
            "photo-em@smb.spk-berlin.de",
            "em@smb.spk-berlin.de",
            "yasna.sepulveda@mnhn.gob.cl",
            "cristian.becker@mnhn.gob.cl",
            "veronica.silva@mnhn.gob.cl",
            "francisco.garrido@mnhn.gob.cl",
            "julieta.elizaga@mnhn.gob.cl",
            "guillermo.castillo@mnhn.gob.cl",
            "comunicaciones@mnhn.gob.cl",
        ):
            self.assertIn(address, doc)
            blob = json.dumps(self.report)
            self.assertIn(address, blob)
        readme = README_PATH.read_text(encoding="utf-8")
        self.assertIn("round6b_open_images.md", readme)
        self.assertIn("CC BY-NC-SA 4.0", doc)
        self.assertIn("Not determined", doc)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_saved_record_matches_the_recomputed_report(self) -> None:
        saved = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(saved, self.report)
