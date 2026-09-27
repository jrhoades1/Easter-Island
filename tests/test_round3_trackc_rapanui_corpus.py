"""Round 3 Track C: larger old-Rapanui corpus and the rerun language tests.

Counts are recomputed from the vendored texts. MockProvider only.
No reading is adopted.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.old_rapanui import (
    cv_syllables_mapped,
    extract_metoro_lines,
    lexicon_headwords,
    load_churchill_headwords,
    primary_running_lines,
)
from decipherment.round2_trackb import build_lexicon
from decipherment.round3_trackc import render_round3_trackc, run_round3_trackc

DOC_PATH = Path(__file__).resolve().parents[1] / "docs" / "decipherment" / "round3_trackC_rapanui_corpus.md"
SOURCES_PATH = Path(__file__).resolve().parents[1] / "data" / "rapanui" / "SOURCES.md"

RUNNING_SOURCES = {"thomson_1891", "metoro_jaussen", "routledge_1919"}


class TestOldRapanuiUnits(unittest.TestCase):
    """Loader and spelling rules. No sign-corpus shuffle."""

    def test_provider_must_be_mock(self):
        with self.assertRaises(TypeError):
            run_round3_trackc(object())

    def test_tagata_maps_to_the_same_syllables_as_tangata(self):
        self.assertEqual(cv_syllables_mapped("tagata"), ("ta", "nga", "ta"))
        self.assertEqual(cv_syllables_mapped("tangata"), ("ta", "nga", "ta"))
        self.assertIsNone(cv_syllables_mapped("man"))

    def test_churchill_list_is_lexicon_not_running_text(self):
        headwords = load_churchill_headwords()
        self.assertEqual(len(headwords), 2182)
        self.assertEqual(sum(1 for item in headwords if item.thomson), 111)
        self.assertEqual(sum(1 for item in headwords if item.geiseler), 25)
        words = {item.word for item in headwords}
        for probe in ("tagata", "poki", "ure", "marama", "atua", "henua", "ragi", "haka"):
            self.assertIn(probe, words)
        for leak in ("child", "bird", "water", "yes", "hieroglyphs", "rongorongo"):
            self.assertNotIn(leak, words)
        running = primary_running_lines()
        self.assertTrue(RUNNING_SOURCES.issuperset({row.source for row in running}))
        lexicon_words = {item.word for item in lexicon_headwords()}
        running_tokens = [word for row in running for word in row.words]
        self.assertGreater(len(lexicon_words), 0)
        self.assertNotEqual(set(running_tokens), lexicon_words)

    def test_metoro_lines_drop_the_html_header(self):
        lines = extract_metoro_lines()
        self.assertEqual(len(lines), 82)
        tokens = [word.lower() for row in lines for word in row.words]
        self.assertNotIn("hieroglyphs", tokens)
        self.assertNotIn("show", tokens)
        elliptical = [row for row in lines if row.elliptical]
        self.assertTrue(elliptical)
        self.assertTrue(all(row.line_id[0].upper() in {"C", "E"} for row in elliptical))

    def test_round2_open_list_stays_the_published_size(self):
        lexicon, _forms, targets = build_lexicon()
        syllable_types = {piece for word in lexicon for piece in word}
        self.assertEqual(len(lexicon), 656)
        self.assertEqual(len(targets), 48)
        self.assertEqual(len(syllable_types), 54)


class TestRound3TrackC(unittest.TestCase):
    """Locked measurements. One corpus run, shared by the methods."""

    @classmethod
    def setUpClass(cls):
        cls.provider = MockProvider()
        cls.result = run_round3_trackc(cls.provider)
        cls.note = render_round3_trackc(cls.result)

    def test_provider_is_unused_and_no_reading(self):
        self.assertEqual(self.provider.name, "mock")
        self.assertEqual(self.provider.get_call_history(), [])
        self.assertEqual(self.result["provider_calls"], 0)
        self.assertIsNone(self.result["reading"])
        self.assertEqual(self.result["trackB"]["adopted_readings"], [])

    def test_thomson_reproduction_is_the_round1_sample(self):
        sample = self.result["thomson_round1_reproduction"]
        self.assertEqual(sample["orthography"], "strict")
        self.assertEqual(sample["syllables"], 3400)
        self.assertEqual(sample["words"], 1591)
        self.assertEqual(sample["words_rejected"], 54)

    def test_primary_sample_counts(self):
        corpus = self.result["corpus"]
        track2 = self.result["track2"]
        self.assertEqual(corpus["metoro_lines"], 82)
        self.assertEqual(corpus["churchill_headwords"], 2182)
        self.assertEqual(corpus["churchill_thomson_mark"], 111)
        self.assertEqual(corpus["churchill_geiseler_mark"], 25)
        self.assertEqual(corpus["syllable_tokens"], 30203)
        self.assertEqual(corpus["cv_word_tokens"], 16198)
        self.assertEqual(corpus["cv_words_rejected"], 115)
        self.assertEqual(track2["syllables"]["tokens"], 30203)
        self.assertEqual(track2["syllables"]["inventory"], 50)
        self.assertEqual(track2["words"]["tokens"], 16198)
        self.assertEqual(track2["words"]["inventory"], 1098)
        self.assertEqual(track2["stem_tokens"], 14488)
        self.assertEqual(track2["stem_types"], 630)
        self.assertEqual(track2["verdict"]["label"], "mixed")
        sensitive = track2["sensitivity_without_elliptical"]
        self.assertEqual(sensitive["label"], "mixed")
        self.assertEqual(sensitive["syllable_tokens"], 21713)
        self.assertEqual(sensitive["word_tokens"], 11843)

    def test_scheme_labels_and_closed_gate(self):
        by_id = {row["id"]: row for row in self.result["trackA"]["schemes"]}
        self.assertEqual(by_id["stem"]["track2_label"], "mixed")
        self.assertEqual(by_id["barthel_suffix_only"]["track2_label"], "logographic")
        self.assertEqual(by_id["barthel_suffix_only"]["round2_label"], "mixed")
        self.assertEqual(by_id["barthel_families"]["track2_label"], "logographic")
        self.assertEqual(by_id["barthel_families"]["round2_label"], "mixed")
        self.assertEqual(by_id["pozdniakov_2007"]["track2_label"], "mixed")
        self.assertFalse(self.result["trackA"]["any_gate"])
        self.assertTrue(all(not row["gate_passes"] for row in by_id.values()))
        self.assertIsNone(self.result["track2"]["alignment"])

    def test_crib_does_not_clear_the_target_gate(self):
        track_b = self.result["trackB"]
        self.assertEqual(track_b["windows"], 81)
        self.assertEqual(track_b["open_lexicon"], 2843)
        self.assertEqual(track_b["targets"], 48)
        self.assertEqual(track_b["syllable_types"], 55)
        by_name = {row["name"]: row for row in track_b["hypotheses"]}
        for name in ("H1", "H2", "H3", "H4"):
            self.assertEqual(by_name[name]["crib_hits"], 0)
            self.assertFalse(by_name[name]["adopted"])
        h1 = by_name["H1"]
        self.assertEqual(h1["open_hits"], 68)
        self.assertEqual(h1["permutation_ge"], 46)
        self.assertEqual(h1["random_ge"], 5)
        self.assertEqual(h1["phrase_hits"], 33)
        self.assertEqual(h1["phrase_permutation_ge"], 6)
        self.assertEqual(h1["phrase_permutation_trials"], 120)
        self.assertTrue(h1["phrase_survives"])
        self.assertEqual(
            h1["phrase_shapes"],
            [{"phrase": "tangata tangata", "count": 25}, {"phrase": "tangata ure", "count": 8}],
        )
        self.assertEqual(by_name["H2"]["phrase_hits"], 42)
        self.assertEqual(by_name["H2"]["phrase_permutation_ge"], 18)
        self.assertFalse(by_name["H2"]["phrase_survives"])

    def test_formula_null_and_word_length(self):
        primary = self.result["word_length"]["primary"]
        self.assertEqual(primary["tokens"], 16198)
        self.assertEqual(primary["full_reduplications"], 461)
        self.assertEqual(primary["histogram"]["1"], 6459)
        self.assertEqual(primary["histogram"]["2"], 6637)
        widths = self.result["formulae"]["widths"]
        self.assertEqual(widths["2"]["types"], 723)
        self.assertEqual(widths["3"]["types"], 577)
        self.assertEqual(widths["3"]["top"][0], ("ki te henua", 87))
        self.assertEqual(widths["4"]["types"], 241)
        self.assertEqual(widths["5"]["types"], 70)
        self.assertEqual(widths["6"]["types"], 21)
        null = self.result["formulae"]["null"]
        self.assertEqual(null["observed_types"], 577)
        self.assertEqual(null["ge"], 0)
        self.assertEqual(null["trials"], 200)
        self.assertTrue(null["beats_null"])

    def test_note_and_sources_record_the_boundary(self):
        note = self.note
        self.assertIn("still not a reading", note)
        self.assertIn("30203", note)
        self.assertIn("16198", note)
        self.assertIn("tangata tangata", note)
        self.assertIn("reading` is None", note)
        self.assertIn("mapped_letters", note)
        self.assertIn("barthel_suffix_only", note)
        written = DOC_PATH.read_text(encoding="utf-8")
        self.assertEqual(written, note)
        sources = SOURCES_PATH.read_text(encoding="utf-8")
        self.assertIn("Métraux", sources)
        self.assertIn("catechism", sources)
        self.assertIn("Englert", sources)
        rule_ids = [rule["id"] for rule in self.result["normalization_rules"]]
        self.assertIn("mapped_letters", rule_ids)
        self.assertIn("streams", rule_ids)
