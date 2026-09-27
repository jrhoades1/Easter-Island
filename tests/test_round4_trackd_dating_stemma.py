"""Round 4 Track D: dating and the copying tree.

Sign ids and cited physical facts only. MockProvider only. No readings.
The corpus case rebuilds the Track C passages and the bootstraps.
"""

import unittest

from agents.base.providers import MockProvider
from decipherment.round4_trackd import (
    BOOTSTRAP_REPLICATES,
    DOC_PATH,
    JSON_PATH,
    TREE_MIN_COLUMNS,
    neighbor_joining,
    newick,
    p_distance,
    render_json,
    render_markdown,
    run_round4_trackd,
    spearman,
    write_outputs,
)


class GuardProvider(MockProvider):
    """Fails the test if Track D asks for a completion."""

    def complete(self, messages, **kwargs):
        raise AssertionError("Track D must not request a completion")

    def complete_with_vision(self, messages, images, **kwargs):
        raise AssertionError("Track D must not request a completion")


class TestNeighborJoining(unittest.TestCase):
    def test_three_taxa_draw_the_shorter_pair_together(self):
        labels = ("H", "P", "Q")
        distances = {("H", "P"): 0.10, ("H", "Q"): 0.30, ("P", "Q"): 0.30}
        tree = neighbor_joining(labels, distances)
        text = newick(tree, {})
        # H and P are the short pair, so they share a parenthesis.
        self.assertTrue(text.startswith("((H:0.05,P:0.05)") or "(H:0.05,P:0.05)" in text)

    def test_spearman_of_reversed_ranks_is_negative(self):
        self.assertAlmostEqual(spearman((1, 2, 3), (3, 2, 1)), -1.0)

    def test_p_distance_counts_a_gap(self):
        self.assertEqual(p_distance({"columns": 4, "differences": 1}), 0.25)


class TestRound4TrackD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_round4_trackd(GuardProvider())

    def test_provider_is_unused_and_no_reading_is_assigned(self):
        self.assertEqual(self.result["provider"], "MockProvider")
        self.assertEqual(self.result["provider_calls"], 0)
        self.assertFalse(self.result["readings_assigned"])
        blob = render_json(self.result)
        self.assertNotIn('"reading":', blob)

    def test_uses_the_ninety_nine_track_c_passages(self):
        self.assertEqual(self.result["passages"], 99)
        self.assertGreater(self.result["deduped_columns"], 99)
        self.assertEqual(self.result["tree_min_columns"], TREE_MIN_COLUMNS)
        self.assertEqual(self.result["tree_labels"], ["G", "H", "K", "P", "Q"])
        gt = self.result["great_tradition"]
        self.assertGreater(gt["triple_sites"], 0)
        self.assertGreater(gt["triple_sign_sites"], 0)
        self.assertEqual(gt["distance_closest_pair"], "H–Q")
        self.assertEqual(gt["exclusive_agreement_closest"], "H–Q")
        self.assertEqual(gt["distance_bootstrap_support"]["H–Q"], 0.663)
        self.assertEqual(gt["column_bootstrap_support"]["H–Q"], 0.679)

    def test_separate_traditions_are_not_glued(self):
        stemma = self.result["stemma"]
        newicks = stemma["newicks"]
        self.assertGreaterEqual(len(newicks), 2)
        joined = " ".join(newicks)
        self.assertIn("H", joined)
        self.assertIn("P", joined)
        self.assertIn("Q", joined)
        self.assertIn("G", joined)
        self.assertIn("K", joined)
        for text in newicks:
            has_gt = any(tablet in text for tablet in ("H", "P", "Q"))
            has_gk = any(tablet in text for tablet in ("G", "K"))
            self.assertFalse(has_gt and has_gk)
        imputed = {tuple(pair) for pair in stemma["imputed_pairs"]}
        self.assertNotIn(("G", "H"), imputed)
        for row in self.result["distances"]:
            self.assertNotEqual(row["p_distance"], 1.5)

    def test_catalog_cites_ferrara_orliac_and_covers_every_letter(self):
        codes = [row["code"] for row in self.result["catalog"]]
        self.assertEqual(codes, list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        by_code = {row["code"]: row for row in self.result["catalog"]}
        echancree = by_code["D"]["radiocarbon"]
        self.assertIn("1493", echancree)
        self.assertIn("1509", echancree)
        self.assertIn("474", echancree)
        self.assertIn("Ferrara", by_code["D"]["radiocarbon_citation"])
        self.assertIn("Podocarpus", by_code["P"]["wood"])
        self.assertIn("Orliac 2007", by_code["P"]["wood_citation"])
        self.assertIn("80±40", by_code["Q"]["radiocarbon"])
        self.assertIn("Thespesia", by_code["O"]["wood"])
        self.assertIn("117±14", by_code["O"]["radiocarbon"])
        self.assertTrue(by_code["D"]["in_transcription"])
        self.assertFalse(by_code["W"]["in_transcription"])

    def test_bootstrap_supports_are_fractions(self):
        gt = self.result["great_tradition"]
        self.assertIn(gt["distance_closest_pair"], {"H–P", "H–Q", "P–Q", "unresolved"})
        self.assertIn(gt["exclusive_agreement_closest"], {"H–P", "H–Q", "P–Q", "unresolved"})
        for support in gt["distance_bootstrap_support"].values():
            self.assertGreaterEqual(support, 0.0)
            self.assertLessEqual(support, 1.0)
        votes = sum(gt["distance_bootstrap_votes"].values())
        self.assertEqual(votes, BOOTSTRAP_REPLICATES)
        self.assertIn("(", self.result["stemma"]["newick"])
        for row in self.result["stemma"]["bipartitions"]:
            self.assertGreaterEqual(row["support"], 0.0)
            self.assertLessEqual(row["support"], 1.0)

    def test_form_and_substitution_tests_stay_inside_unit_interval(self):
        forms = self.result["form_test"]
        for name in ("H", "P", "Q"):
            rate = forms["aligned_rates"][name]["ligature_rate"]
            self.assertGreaterEqual(rate, 0.0)
            self.assertLessEqual(rate, 1.0)
        direction = self.result["substitution_direction"]
        self.assertGreaterEqual(direction["singleton_has_rarer"], 0)
        self.assertGreaterEqual(direction["singleton_has_commoner"], 0)
        self.assertTrue(direction["hypothesis"].startswith("HYPOTHESIS"))
        self.assertGreater(len(self.result["systematic_pairs"]), 0)

    def test_outputs_roundtrip(self):
        text = render_markdown(self.result)
        self.assertIn("MockProvider", text)
        self.assertIn("1493–1509", text)
        self.assertIn(self.result["great_tradition"]["distance_closest_pair"], text)
        self.assertNotIn("copulated", text.lower())
        payload = render_json(self.result)
        self.assertIn('"readings_assigned": false', payload)
        write_outputs(self.result)
        self.assertTrue(JSON_PATH.is_file())
        self.assertTrue(DOC_PATH.is_file())
