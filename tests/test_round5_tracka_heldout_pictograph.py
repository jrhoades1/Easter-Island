"""Round 5 Track A: held-out pictograph confirmation.

The plan in docs/decipherment/round5a_preregistration.md was committed
before the scores. MockProvider only. No reading is adopted.
"""

from __future__ import annotations

import random
import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.round4_tracka import _r1_words
from decipherment.round5_tracka import (
    ALPHA,
    BIRD_LABEL_SEED,
    BIRD_SIGN_SEED,
    CLOSED_CLASS,
    EXPECTED_DISCOVERY,
    EXPECTED_HELDOUT,
    MIN_POOL,
    NOUN_MAP_SEED,
    REBUS_SHUFFLE_SEED,
    ROUND4_FAMILY_IDS,
    SIGN_ORDER,
    STEMMA_EDGES,
    TRIALS,
    TWO_APART_SEED,
    block_shuffle,
    frequency_bin,
    holm_adjust,
    mixed_word_hits,
    render_round5_tracka,
    run_round5_tracka,
    split_tablets,
    write_round5_outputs,
    _significant_passages,
)
from decipherment.round2_trackb import load_lines

DOC_PATH = Path(__file__).resolve().parents[1] / "docs" / "decipherment" / "round5a_heldout_pictograph.md"
JSON_PATH = Path(__file__).resolve().parents[1] / "data" / "decipherment" / "round5a_heldout_pictograph.json"
PLAN_PATH = Path(__file__).resolve().parents[1] / "docs" / "decipherment" / "round5a_preregistration.md"


class PlanConstantTests(unittest.TestCase):
    def test_seeds_match_the_committed_plan(self):
        self.assertEqual(TRIALS, 500)
        self.assertEqual(ALPHA, 0.05)
        self.assertEqual(MIN_POOL, 8)
        self.assertEqual(
            (REBUS_SHUFFLE_SEED, NOUN_MAP_SEED, TWO_APART_SEED, BIRD_LABEL_SEED, BIRD_SIGN_SEED),
            (50, 51, 52, 53, 54),
        )
        self.assertEqual(EXPECTED_DISCOVERY, ("A", "B", "C", "E", "G", "H", "K", "P", "Q", "R"))
        self.assertEqual(EXPECTED_HELDOUT, ("D", "F", "I", "J", "L", "M", "N", "O", "S", "T", "U", "V", "W"))
        self.assertEqual(SIGN_ORDER, ("006", "040", "143", "152", "200", "600", "680", "700"))
        self.assertEqual(STEMMA_EDGES, (("G", "K"), ("H", "P"), ("H", "Q"), ("P", "Q")))
        text = PLAN_PATH.read_text(encoding="utf-8")
        self.assertIn("committed before the held-out counts", text)
        self.assertIn("r5_rebus_sign_shuffle", text)
        self.assertIn("r5_two_apart_sign_shuffle", text)

    def test_r1_is_the_round4_map(self):
        words = _r1_words()
        self.assertEqual(
            words,
            {
                "040": "marama",
                "143": "rakau",
                "152": "omotohi",
                "200": "tangata",
                "600": "manu",
                "680": "makohe",
                "700": "ika",
                "006": "rima",
            },
        )

    def test_closed_class_covers_particles_and_pronouns(self):
        for word in ("te", "ki", "au", "koe", "ia", "hoki", "ina"):
            self.assertIn(word, CLOSED_CLASS)
        self.assertNotIn("manu", CLOSED_CLASS)
        self.assertNotIn("tangata", CLOSED_CLASS)

    def test_frequency_bins(self):
        self.assertEqual(frequency_bin(0), 0)
        self.assertEqual(frequency_bin(20), 1)
        self.assertEqual(frequency_bin(21), 2)
        self.assertEqual(frequency_bin(100), 2)
        self.assertEqual(frequency_bin(101), 3)
        self.assertEqual(frequency_bin(300), 3)
        self.assertEqual(frequency_bin(301), 4)


def _runs(row: list[str]) -> list[list[str]]:
    runs: list[list[str]] = []
    for stem in row:
        if runs and runs[-1][-1] == stem:
            runs[-1].append(stem)
        else:
            runs.append([stem])
    return runs


class ShuffleAndHolmTests(unittest.TestCase):
    def test_block_shuffle_keeps_adjacent_repeats(self):
        row = ["040", "040", "200", "600", "600", "600"]
        shuffled = block_shuffle(row, random.Random(0))
        self.assertEqual(sorted(shuffled), sorted(row))
        self.assertIn(["040", "040"], _runs(shuffled))
        self.assertIn(["600", "600", "600"], _runs(shuffled))

    def test_mixed_hits_drop_repeats_and_doubled_words(self):
        shapes = {("ma", "nu", "i", "ka")}
        formulae = {2: {}, 3: {}, 4: {}}
        words = {"600": "manu", "700": "ika", "006": "rima"}
        syllables = {"600": ("ma", "nu"), "700": ("i", "ka"), "006": ("ri", "ma")}
        windows = [
            ("600", "600"),
            ("600", "700"),
            ("006", "006", "700"),
            ("200", "200"),
        ]
        # 200 is not in words; the scorer assumes every sign in a window is mapped.
        windows = [gram for gram in windows if all(sign in words for sign in gram)]
        scored = mixed_word_hits(windows, words, syllables, shapes, formulae)
        self.assertEqual(scored["pure_sign_repeats"], 1)
        self.assertEqual(scored["doubled_word_windows"], 1)
        self.assertEqual(scored["eligible_windows"], 1)
        self.assertEqual(scored["hits"], 1)
        self.assertEqual(scored["examples"][0]["phrase"], "manu ika")

    def test_holm_running_maximum(self):
        rows = [
            {"id": "b", "p_add_one": 0.03},
            {"id": "a", "p_add_one": 0.01},
            {"id": "c", "p_add_one": 0.04},
        ]
        adjusted = {row["id"]: row for row in holm_adjust(rows, alpha=0.05)}
        self.assertAlmostEqual(adjusted["a"]["holm_p"], 0.03)
        self.assertAlmostEqual(adjusted["b"]["holm_p"], 0.06)
        self.assertAlmostEqual(adjusted["c"]["holm_p"], 0.06)
        self.assertTrue(adjusted["a"]["survives_holm"])
        self.assertFalse(adjusted["b"]["survives_holm"])
        self.assertEqual(adjusted["a"]["holm_rank"], 1)

    def test_split_matches_the_published_components(self):
        passages = _significant_passages()
        tablets = [line.tablet for line in load_lines()]
        split = split_tablets(passages, tablets)
        self.assertEqual(split["discovery"], EXPECTED_DISCOVERY)
        self.assertEqual(split["heldout"], EXPECTED_HELDOUT)
        self.assertEqual(split["shared_passage_ids"], [])
        self.assertEqual(split["split_stemma_edges"], [])
        self.assertIn("I", split["heldout"])
        self.assertNotIn("G", split["heldout"])
        self.assertNotIn("H", split["heldout"])

    def test_provider_must_be_mock(self):
        with self.assertRaises(TypeError):
            run_round5_tracka(object())


class Round5RunTests(unittest.TestCase):
    """One held-out run. The gates were frozen in the plan before this count."""

    @classmethod
    def setUpClass(cls):
        cls.result = run_round5_tracka(MockProvider())
        write_round5_outputs(cls.result)

    def test_no_translation_and_mock_only(self):
        self.assertEqual(self.result["provider"], "mock")
        self.assertEqual(self.result["provider_calls"], 0)
        self.assertIsNone(self.result["reading"])
        self.assertIn(self.result["package"], ("survives", "dies"))
        note = render_round5_tracka(self.result)
        self.assertIn("Nothing here is a translation of a tablet.", note)
        self.assertIn("HYPOTHESIS", note)

    def test_family_contains_the_pre_registered_ids(self):
        ids = [row["id"] for row in self.result["family"]]
        for required in ROUND4_FAMILY_IDS:
            self.assertIn(required, ids)
        self.assertIn("r5_rebus_sign_shuffle", ids)
        self.assertIn("r5_rebus_noun_map", ids)
        self.assertIn("r5_two_apart_sign_shuffle", ids)
        self.assertEqual(len(ids), len(set(ids)))
        ranks = [row["holm_rank"] for row in self.result["family"]]
        self.assertEqual(sorted(ranks), list(range(1, len(ranks) + 1)))

    def test_verdict_follows_the_holm_rule(self):
        by_id = {row["id"]: row for row in self.result["family"]}
        rebus = (
            by_id["r5_rebus_sign_shuffle"]["survives_holm"]
            and by_id["r5_rebus_noun_map"]["survives_holm"]
        )
        two_apart = by_id["r5_two_apart_sign_shuffle"]["survives_holm"]
        bird = self.result["verdict"]["bird"]
        if self.result["bird"]["available"]:
            self.assertIn("r5_bird_label_shuffle", by_id)
            self.assertIn("r5_bird_sign_shuffle", by_id)
            bird_ok = (
                by_id["r5_bird_label_shuffle"]["survives_holm"]
                and by_id["r5_bird_sign_shuffle"]["survives_holm"]
            )
            self.assertEqual(bird, "survives" if bird_ok else "dies")
        else:
            self.assertEqual(bird, "not_tested")
            self.assertNotIn("r5_bird_label_shuffle", by_id)
        package = "survives" if rebus and two_apart and bird != "dies" else "dies"
        self.assertEqual(self.result["package"], package)
        self.assertEqual(self.result["verdict"]["rebus"], "survives" if rebus else "dies")
        self.assertEqual(self.result["verdict"]["two_apart"], "survives" if two_apart else "dies")

    def test_exclusions_and_effect_sizes_are_present(self):
        observed = self.result["rebus"]["observed"]
        self.assertGreaterEqual(observed["mapped_windows"], observed["eligible_windows"])
        self.assertEqual(
            observed["mapped_windows"],
            observed["eligible_windows"] + observed["pure_sign_repeats"] + observed["doubled_word_windows"],
        )
        for block in (
            self.result["rebus"]["sign_shuffle"],
            self.result["rebus"]["noun_map"],
            self.result["two_apart"],
        ):
            self.assertEqual(block["trials"], TRIALS)
            self.assertGreaterEqual(block["p_add_one"], 1 / (TRIALS + 1))
            if block["null_sd"] > 0:
                expected = (block["observed"] - block["null_mean"]) / block["null_sd"]
                self.assertAlmostEqual(block["effect_size"], expected)
        for row in self.result["rebus"]["pools"]:
            self.assertGreaterEqual(row["pool_size"], 1)

    def test_written_report_matches_the_run(self):
        self.assertTrue(JSON_PATH.is_file())
        self.assertTrue(DOC_PATH.is_file())
        text = DOC_PATH.read_text(encoding="utf-8")
        self.assertIn(f"The pictograph package **{self.result['package']}**.", text)
        self.assertIn("Nothing here is a translation of a tablet.", text)
        self.assertIn("HYPOTHESIS", text)
