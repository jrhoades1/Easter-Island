"""Round 4 Track C: petroglyph parallels. MockProvider only.

Counts are recomputed from the vendored Barthel pages. No reading is adopted.
"""

from __future__ import annotations

import ast
import json
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.barthel_corpus import load_located_sides
from decipherment.inventories import encode_token
from decipherment.round4_trackc import (
    ADOPTED_MATCHES,
    JSON_PATH,
    MIN_COUNT,
    UNNUMBERED,
    render_round4_trackc,
    run_round4_trackc,
)

DOC_PATH = Path(__file__).resolve().parents[1] / "docs" / "decipherment" / "round4_trackC_petroglyphs.md"


def _direct_stem_count(stem: str) -> int:
    total = 0
    for side in load_located_sides():
        for _line_no, tokens in side.lines:
            for token in tokens:
                total += encode_token(token, "stem").count(stem)
    return total


def _direct_surface_count(surface: str) -> int:
    total = 0
    for side in load_located_sides():
        for _line_no, tokens in side.lines:
            for token in tokens:
                for form in encode_token(token, "surface"):
                    if form == surface or (form.startswith("V") and form[1:] == surface):
                        total += 1
    return total


class TestRound4TrackC(unittest.TestCase):
    """One corpus run. Readings stay null."""

    @classmethod
    def setUpClass(cls):
        cls.provider = MockProvider()
        cls.result = run_round4_trackc(cls.provider)
        cls.note = render_round4_trackc(cls.result)

    def test_provider_must_be_mock(self):
        with self.assertRaises(TypeError):
            run_round4_trackc(object())

    def test_provider_is_unused_and_no_reading(self):
        self.assertEqual(self.provider.name, "mock")
        self.assertEqual(self.provider.get_call_history(), [])
        self.assertEqual(self.result["provider_calls"], 0)
        self.assertIsNone(self.result["reading"])
        self.assertEqual(self.result["supported_lexical_readings"], [])

    def test_every_adopted_sign_is_cited_and_unread(self):
        cited = set()
        for match in ADOPTED_MATCHES:
            self.assertTrue(match["citation"].strip())
            self.assertIsNotNone(match["barthel_signs"])
            cited.update(match["barthel_signs"])
        self.assertEqual(set(self.result["signs"]), cited)
        for row in self.result["signs"].values():
            self.assertIsNone(row["reading"])
            self.assertIsNone(row["lexical_reading"])

    def test_unnumbered_motifs_are_not_tested(self):
        for row in UNNUMBERED:
            self.assertIsNone(row["barthel_signs"])
            self.assertTrue(row["citation"].strip())
        self.assertIsNone(self.result["inscribed_reimiro"]["rei_miro_1"]["implication"])
        self.assertIsNone(self.result["inscribed_reimiro"]["rei_miro_2"]["implication"])
        self.assertIsNone(self.result["inscribed_reimiro"]["rei_miro_1"]["reading"])

    def test_vendored_counts_match_a_direct_scan(self):
        for stem in ("074", "660", "680", "007"):
            self.assertEqual(self.result["signs"][stem]["stem_count"], _direct_stem_count(stem))
        self.assertEqual(self.result["signs"]["700b"]["stem_count"], _direct_surface_count("700b"))
        self.assertNotIn("700", self.result["signs"])
        wider = self.result["stem_700_not_cited"]
        self.assertEqual(wider["stem_count"], _direct_stem_count("700"))
        self.assertIsNone(wider["concentration"])
        self.assertIsNone(wider["lexical_reading"])
        self.assertGreater(wider["stem_count"], self.result["signs"]["700b"]["stem_count"])

    def test_rare_signs_keep_a_null_confirmatory_test(self):
        for row in self.result["signs"].values():
            if row["stem_count"] < MIN_COUNT:
                self.assertIsNone(row["concentration"])
                self.assertIn(row["distribution_status"], {"absent", "not_tested"})
        for sign in ("700b", "721", "733", "513", "550"):
            self.assertIsNone(self.result["signs"][sign]["concentration"])

    def test_published_counts_are_not_overwritten(self):
        by_id = {match["match_id"]: match for match in self.result["adopted_matches"]}
        self.assertEqual(by_id["orongo_house_44_gourd"]["published_count"]["074"]["count"], 94)
        self.assertEqual(by_id["orongo_house_40_long_beak"]["published_count"]["660"]["count"], 29)
        self.assertEqual(by_id["mata_ngarau_two_headed_bird"]["published_count"]["680"]["count"], 23)

    def test_note_states_the_limit(self):
        self.assertIn("No sign gains a word", self.note)
        self.assertIn("reading", self.note)
        self.assertIn("null", self.note)
        self.assertNotIn("glyph 51 as a supported", self.note)

    def test_saved_files_match_this_run(self):
        self.assertEqual(DOC_PATH.read_text(encoding="utf-8"), self.note)
        saved = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        self.assertIsNone(saved["reading"])
        self.assertEqual(saved["supported_lexical_readings"], [])
        self.assertEqual(saved["corpus_tokens"], self.result["corpus_tokens"])
        for sign, row in self.result["signs"].items():
            self.assertEqual(saved["signs"][sign]["stem_count"], row["stem_count"])
            self.assertEqual(saved["signs"][sign]["distribution_status"], row["distribution_status"])
            self.assertIsNone(saved["signs"][sign]["reading"])

    def test_module_does_not_assign_a_gloss(self):
        source = Path(__file__).resolve().parents[1] / "decipherment" / "round4_trackc.py"
        tree = ast.parse(source.read_text(encoding="utf-8"))
        assigned = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in {"reading", "gloss"}:
                        assigned.append(node)
        self.assertEqual(assigned, [])
