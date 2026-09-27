"""Round 3 Track B: Mamari photograph versus Barthel Ca6–Ca9.

Counts are recomputed from the vendored calendar fixture and the
Commons plate. MockProvider only. No reading is assigned.
"""

from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.round3_trackb import (
    FISCHER_CA_LINES,
    GUY_STAR_690,
    OUTSIDE_040,
    PHOTO_PATH,
    PHOTO_SHA256,
    TABLET_LENGTH_MM,
    TABLET_WIDTH_MM,
    fischer_matches_barthel_html,
    run_round3_trackb,
)
from models.glyphs import GlyphCluster
from tests.test_mamari_calendar_scoreboard import fixture_line_stems, load_mamari_fixture

DOC_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "decipherment"
    / "round3_trackB_transcription_audit.md"
)
MANIFEST_PATH = (
    Path(__file__).resolve().parents[1] / "data" / "images" / "mamari" / "manifest.json"
)
CA_JPG_SHA256 = "68fdff7e3e3f60533a7d43a6a5f5efcf3655424953dff5871db45d4d68f93a84"

# Track 1 locks. Repeated here so this audit fails if its Barthel
# baseline drifts from those counts.
BARTHEL_STEMS = 101
BARTHEL_STEMS_BY_LINE = (16, 43, 40, 2)
BARTHEL_040 = 28
BARTHEL_AROUND = (13, 13)
BARTHEL_GAPS = (2, 6, 3, 2, 5, 3, 5)
BARTHEL_RUNS = ((1, 1, 6, 1, 1, 1, 2), (5, 2, 1, 5, 2))
BARTHEL_FULL_DELIMITERS = 6
BARTHEL_SHUFFLE = 0
BARTHEL_CHI = (2376887638931856, 3323951482720)

CORRECTED_STEMS = 100
CORRECTED_STEMS_BY_LINE = (16, 42, 40, 2)
CORRECTED_040 = 28
CORRECTED_AROUND = (13, 13)
CORRECTED_GAPS = (2, 6, 3, 7, 3, 5)
CORRECTED_GAPS_FAMILY = (2, 6, 3, 2, 5, 3, 5)
CORRECTED_RUNS = BARTHEL_RUNS
CORRECTED_FULL_DELIMITERS = 5
CORRECTED_FAMILY_DELIMITERS = 6
CORRECTED_SHUFFLE = 1
CORRECTED_CHI = (2378200559616000, 3290817024000)

TABLET_BBOX = (117, 68, 1862, 1251)


class TestRound3TrackBAudit(unittest.TestCase):
    """Photograph, published corrections, and the calendar counts."""

    def setUp(self):
        self.provider = MockProvider()
        self.report = run_round3_trackb(self.provider)

    def test_provider_is_required_and_never_called(self):
        with self.assertRaises(TypeError):
            run_round3_trackb(object())
        self.assertEqual(self.report.provider_calls, 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_photograph_hash_and_tablet_bounds(self):
        self.assertTrue(PHOTO_PATH.is_file())
        self.assertEqual(self.report.photo_sha256, PHOTO_SHA256)
        self.assertEqual(self.report.photo_pixels, (2040, 1424))
        self.assertEqual(self.report.tablet_bbox, TABLET_BBOX)
        _x, _y, width, height = self.report.tablet_bbox
        photo_aspect = width / height
        wood_aspect = TABLET_LENGTH_MM / TABLET_WIDTH_MM
        self.assertLess(abs(photo_aspect - wood_aspect) / wood_aspect, 0.01)
        self.assertLess(width / TABLET_LENGTH_MM, 8)

    def test_every_calendar_code_is_illegible_on_the_photograph(self):
        self.assertEqual(len(self.report.judgments), 75)
        self.assertTrue(all(row.photo == "illegible" for row in self.report.judgments))
        counts = Counter(row.status for row in self.report.judgments)
        self.assertEqual(counts["unconfirmed"], 66)
        self.assertEqual(counts["disputed"], 7)
        self.assertEqual(counts["corrected"], 2)
        adopted = [row for row in self.report.judgments if row.adopted]
        self.assertEqual(
            [(row.line, row.barthel, row.proposed) for row in adopted],
            [("Ca7", "044.040", "078.040"), ("Ca7", "600.390.041", "*690.041")],
        )
        disputed = [row for row in self.report.judgments if row.status == "disputed"]
        self.assertTrue(all(row.proposed is None and row.adopted is False for row in disputed))
        self.assertEqual(
            [(row.line, row.index, row.barthel) for row in disputed],
            [
                ("Ca6", 3, "670"),
                ("Ca7", 9, "670"),
                ("Ca7", 18, "670"),
                ("Ca7", 27, "670y"),
                ("Ca8", 6, "670"),
                ("Ca8", 14, "670"),
                ("Ca8", 25, "670"),
            ],
        )

    def test_fischer_numeric_page_matches_barthel(self):
        self.assertEqual(set(FISCHER_CA_LINES), {6, 7, 8, 9})
        self.assertTrue(fischer_matches_barthel_html())

    def test_barthel_baseline_matches_track1(self):
        fixture = tuple(tuple(line) for line in fixture_line_stems(load_mamari_fixture()))
        self.assertEqual(self.report.barthel_lines, fixture)
        self.assertEqual(self.report.measure("stems").barthel, BARTHEL_STEMS)
        self.assertEqual(self.report.measure("stems_by_line").barthel, BARTHEL_STEMS_BY_LINE)
        self.assertEqual(self.report.measure("040").barthel, BARTHEL_040)
        self.assertEqual(self.report.measure("040_around_152").barthel, BARTHEL_AROUND)
        self.assertEqual(self.report.measure("040_gaps").barthel, BARTHEL_GAPS)
        self.assertEqual(self.report.measure("runs_around_152").barthel, BARTHEL_RUNS)
        self.assertEqual(self.report.measure("exact_full_delimiters").barthel, BARTHEL_FULL_DELIMITERS)
        self.assertEqual(self.report.measure("shuffle_kokore_hits").barthel, BARTHEL_SHUFFLE)
        self.assertEqual(self.report.measure("chi_square").barthel, BARTHEL_CHI)
        self.assertEqual(self.report.measure("outside_040").barthel, OUTSIDE_040)

    def test_adopted_correction_changes_segmentation_not_crescents(self):
        corrected = self.report
        self.assertEqual(corrected.measure("stems").corrected, CORRECTED_STEMS)
        self.assertEqual(corrected.measure("stems_by_line").corrected, CORRECTED_STEMS_BY_LINE)
        self.assertEqual(corrected.measure("040").corrected, CORRECTED_040)
        self.assertEqual(corrected.measure("040_around_152").corrected, CORRECTED_AROUND)
        self.assertEqual(corrected.measure("040_around_152_family").corrected, CORRECTED_AROUND)
        self.assertEqual(corrected.measure("040_gaps").corrected, CORRECTED_GAPS)
        self.assertEqual(corrected.measure("040_gaps_family").corrected, CORRECTED_GAPS_FAMILY)
        self.assertEqual(corrected.measure("runs_around_152").corrected, CORRECTED_RUNS)
        self.assertEqual(corrected.measure("exact_full_delimiters").corrected, CORRECTED_FULL_DELIMITERS)
        self.assertEqual(corrected.measure("family_full_delimiters").corrected, CORRECTED_FAMILY_DELIMITERS)
        self.assertEqual(corrected.measure("shuffle_kokore_hits").corrected, CORRECTED_SHUFFLE)
        self.assertEqual(corrected.measure("chi_square").corrected, CORRECTED_CHI)
        self.assertEqual(corrected.measure("stem_044").corrected, 0)
        self.assertEqual(corrected.measure("stem_078").corrected, 8)
        self.assertEqual(corrected.measure("stem_600").corrected, 1)
        self.assertEqual(corrected.measure("stem_390").corrected, 7)
        self.assertEqual(corrected.measure("stem_star690").corrected, 1)
        flat = [stem for line in corrected.corrected_lines for stem in line]
        self.assertNotIn("690", flat)
        self.assertIn(GUY_STAR_690, flat)
        self.assertEqual(corrected.measure("outside_040").corrected, OUTSIDE_040)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_cataloger_ids_stay_off_the_barthel_numbers(self):
        """The parked image track emits G-ids. This audit does not map them."""
        self.assertEqual(GlyphCluster.generate_id(1), "G001")
        self.assertFalse(GlyphCluster.generate_id(1).isdigit())

    def test_uncommitted_tracings_are_hashed_not_vendored(self):
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        rows = manifest["not_committed"]
        self.assertTrue(all(row["committed"] is False for row in rows))
        by_file = {row["file"]: row for row in rows}
        self.assertEqual(by_file["ca.jpg"]["sha256"], CA_JPG_SHA256)
        barthel_ca7 = next(
            row for row in rows if row["kind"] == "barthel_tracing" and row["file"] == "Ca0701.png"
        )
        self.assertEqual(barthel_ca7["pixels"], [522, 74])
        self.assertEqual(barthel_ca7["sha256"], "1446d6208480df3a88de95f5baccf63f729a3e0c4448fa0a2d17a214c1e85f58")
        self.assertIn("non-profit", barthel_ca7["license"])
        image_dir = PHOTO_PATH.parent
        committed = {path.name for path in image_dir.iterdir()}
        self.assertIn("rongorongo_c-a_mamari.jpg", committed)
        self.assertNotIn("Ca0701.png", committed)
        self.assertNotIn("ca.jpg", committed)

    def test_doc_records_the_locked_counts(self):
        text = DOC_PATH.read_text(encoding="utf-8")
        self.assertIn("illegible", text)
        self.assertIn("28", text)
        self.assertIn("13", text)
        self.assertIn("*690", text)
        self.assertIn("MockProvider", text)
        self.assertIn(PHOTO_SHA256, text)
