"""Round 2 Track C: parallel passages and substitution classes.

Sign ids only. The corpus case reruns the shuffle nulls (about two seconds).
MockProvider only. No readings.
"""

import unittest

from agents.base.providers import MockProvider
from decipherment.track_c_parallels import (
    DOC_PATH,
    JSON_PATH,
    SideText,
    align_window,
    find_passages,
    load_side_texts,
    render_json,
    render_markdown,
    run_track_c,
    smith_waterman,
)
from tests.test_mamari_hpq_triple_n8_scoreboard import STANDING_MAXIMALS
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    STANDING_COMBINED_TOKENS,
)

# Locks from the vendored Barthel stem sample. Track 2 reports the same
# 14488 tokens and 630 types. Do not retune these to chase a class.
STANDING_SIDES = 36
STANDING_TOKENS = 14488
STANDING_INVENTORY = 630
STANDING_NULL_MAX = 0
STANDING_NULL_TRIALS = 24
STANDING_SIGNIFICANT = 99
STANDING_CANDIDATES = 99
STANDING_PUBLISHED = {"H–P": 32, "H–Q": 18, "P–Q": 19, "G–K": 6, "A–R": 0}
STANDING_ABSENT = ("A–R",)
STANDING_STAFF_PARTNERS = ()
STANDING_SPROAT = ("Hr2:36..Hr4:0", "Qr2:0..Qr3:65", 125, 195)
STANDING_CLASSES = (
    ("S01", "600", ("400", "600"), 9),
    ("S02", "002", ("002", "021"), 7),
    ("S03", "001", ("001", "011"), 6),
    ("S04", "254", ("254", "256"), 6),
    ("S05", "084", ("056", "084"), 5),
    ("S06", "008", ("008", "081"), 4),
    ("S07", "280", ("280", "290"), 4),
    ("S08", "381", ("381", "385"), 3),
)
STANDING_MERGE = {
    "001": "001",
    "002": "002",
    "008": "008",
    "011": "001",
    "021": "002",
    "056": "084",
    "081": "008",
    "084": "084",
    "254": "254",
    "256": "254",
    "280": "280",
    "290": "280",
    "381": "381",
    "385": "381",
    "400": "600",
    "600": "600",
}
STANDING_HAND = ("absent", 0, False)
STANDING_HAPAX_PAIRS = 122
STANDING_FAMILY_MAX = 6
STANDING_INDEL = ("095", "003", "006", 4, "systematic")
STANDING_SYSTEMATIC_INDELS = 1
STANDING_LIGATURE_SIGNIFICANT = 55
STANDING_LIGATURE_RECOVERED = ("H–P", "H–Q", "P–Q", "G–K")
STANDING_LIGATURE_ABSENT = ("A–R",)
STANDING_LIGATURE_CLASS = ("S01", ("002", "021"))


class GuardProvider(MockProvider):
    """Fails the test if Track C asks for a completion."""

    def complete(self, messages, **kwargs):
        raise AssertionError("Track C must not request a completion")

    def complete_with_vision(self, messages, images, **kwargs):
        raise AssertionError("Track C must not request a completion")


def _contains(sequence: tuple[str, ...], gram: tuple[str, ...]) -> bool:
    width = len(gram)
    return any(sequence[index : index + width] == gram for index in range(len(sequence) - width + 1))


def _slice(texts: dict[str, SideText], passage: dict, side: str) -> tuple[str, ...] | None:
    if passage["left"]["side"] == side:
        node = passage["left"]
    elif passage["right"]["side"] == side:
        node = passage["right"]
    else:
        return None
    return texts[side].signs[node["start"] : node["end"]]


class TestSmithWaterman(unittest.TestCase):
    def test_identical_path_scores_two_per_sign(self):
        signs = ["001", "002", "003", "004"]
        score, start_a, end_a, start_b, end_b, columns = smith_waterman(signs, signs)
        self.assertEqual(score, 8)
        self.assertEqual((start_a, end_a, start_b, end_b), (0, 4, 0, 4))
        self.assertEqual(columns, [(sign, sign) for sign in signs])

    def test_one_substitution_stays_on_the_diagonal(self):
        left = ["001", "002", "003", "004"]
        right = ["001", "009", "003", "004"]
        _score, _sa, _ea, _sb, _eb, columns = smith_waterman(left, right)
        self.assertEqual(columns, list(zip(left, right)))

    def test_internal_gap(self):
        _score, _sa, _ea, _sb, _eb, columns = smith_waterman(
            ["001", "002", "003"],
            ["001", "003"],
        )
        self.assertEqual(columns, [("001", "001"), ("002", None), ("003", "003")])


class TestPlantedPassage(unittest.TestCase):
    def test_finder_keeps_a_ten_sign_parallel_with_one_substitution(self):
        core = [f"{index:03d}" for index in range(1, 11)]
        altered = core[:4] + ["099"] + core[5:]
        left = SideText("A", "Aa", "mem", tuple(["900"] * 4 + core + ["800"] * 4), (("Aa1", 0, 18),))
        right = SideText(
            "B",
            "Ba",
            "mem",
            tuple(["700"] * 3 + altered + ["600"] * 3),
            (("Ba1", 0, 16),),
        )
        found = find_passages((left, right))
        self.assertEqual(len(found), 1)
        passage = found[0]
        self.assertEqual(passage.matches, 9)
        self.assertEqual(passage.mismatches, 1)
        self.assertGreaterEqual(passage.span, 8)
        self.assertIn(("005", "099"), passage.columns)

    def test_window_keeps_two_exact_islands_inside_a_looser_trace(self):
        # Ten matches, six mismatches, ten matches. The whole trace is under
        # 0.80 identity. Each island still clears the gate.
        island = [f"{index:03d}" for index in range(1, 11)]
        noise_a = ["111", "222", "333", "444", "555", "666"]
        noise_b = ["777", "888", "101", "202", "303", "404"]
        left = SideText("A", "Aa", "mem", tuple(island + noise_a + island), (("Aa1", 0, 26),))
        right = SideText("B", "Ba", "mem", tuple(island + noise_b + island), (("Ba1", 0, 26),))
        found = align_window(left, right, 0, 26, 0, 26)
        self.assertGreaterEqual(len(found), 2)
        covered = [item for item in found if item.matches >= 10 and item.mismatches == 0]
        self.assertGreaterEqual(len(covered), 2)


class TestTrackCCorpus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_track_c(GuardProvider())
        cls.stem = cls.result["stem"]
        cls.texts = {side.side: side for side in load_side_texts("stem")}

    def test_provider_guard_and_no_readings(self):
        self.assertEqual(self.result["provider"], "MockProvider")
        self.assertFalse(self.result["readings_assigned"])
        self.assertEqual(self.result["primary_encoding"], "stem")
        blob = render_json(self.result)
        self.assertIn('"readings_assigned": false', blob)
        self.assertNotIn('"reading":', blob)
        self.assertNotIn('"gloss":', blob)
        self.assertNotIn("translation", blob)

    def test_rejects_a_non_mock_provider(self):
        with self.assertRaises(TypeError):
            run_track_c(provider=object())  # type: ignore[arg-type]

    def test_corpus_matches_track2_stem_sample(self):
        corpus = self.stem["corpus"]
        self.assertEqual(corpus["side_count"], STANDING_SIDES)
        self.assertEqual(corpus["tokens"], STANDING_TOKENS)
        self.assertEqual(corpus["inventory"], STANDING_INVENTORY)
        self.assertEqual(len(corpus["sides"]), STANDING_SIDES)

    def test_null_and_passage_counts(self):
        self.assertEqual(self.stem["null"]["max_score"], STANDING_NULL_MAX)
        self.assertEqual(len(self.stem["null"]["scores"]), STANDING_NULL_TRIALS)
        self.assertEqual(set(self.stem["null"]["scores"]), {0})
        self.assertEqual(self.stem["significant_passages"], STANDING_SIGNIFICANT)
        self.assertEqual(self.stem["candidate_passages"], STANDING_CANDIDATES)
        self.assertTrue(all(passage["significant"] for passage in self.stem["passages"]))

    def test_sproat_anchor_and_published_pairs(self):
        comparison = self.stem["published_comparison"]
        self.assertEqual(comparison["published_passage_counts"], STANDING_PUBLISHED)
        self.assertEqual(tuple(comparison["published_absent"]), STANDING_ABSENT)
        self.assertEqual(tuple(comparison["staff_i_partners"]), STANDING_STAFF_PARTNERS)
        head = self.stem["passages"][0]
        locus = (head["left"]["locus"], head["right"]["locus"], head["span"], head["score"])
        self.assertEqual(head["id"], "P001")
        self.assertEqual(locus, STANDING_SPROAT)
        self.assertEqual(head["publication_label"], "H–Q")

    def test_locked_hpq_islands_and_gk_17gram_sit_inside_passages(self):
        for tokens, _n, _fh, _fp, _fq, *sites in STANDING_MAXIMALS:
            sides = tuple(site[0] for site in sites)
            self.assertTrue(
                self._shared(tokens, sides),
                tokens,
            )
        self.assertTrue(self._shared(STANDING_COMBINED_TOKENS, ("Gr", "Kr")))

    def _shared(self, gram: tuple[str, ...], sides: tuple[str, ...]) -> bool:
        for index, left in enumerate(sides):
            for right in sides[index + 1 :]:
                for passage in self.stem["passages"]:
                    pair = {passage["left"]["side"], passage["right"]["side"]}
                    if pair != {left, right}:
                        continue
                    left_slice = _slice(self.texts, passage, left)
                    right_slice = _slice(self.texts, passage, right)
                    if left_slice and right_slice and _contains(left_slice, gram) and _contains(right_slice, gram):
                        return True
        return False

    def test_substitution_classes_and_merge_table(self):
        subs = self.stem["substitutions"]
        classes = tuple(
            (item["id"], item["representative"], tuple(item["members"]), item["pair_count"])
            for item in subs["classes"]
        )
        self.assertEqual(classes, STANDING_CLASSES)
        self.assertEqual(self.result["merge_table"], STANDING_MERGE)
        self.assertEqual(subs["merge_table"], STANDING_MERGE)
        self.assertFalse(any(item["wide"] for item in subs["classes"]))
        hand = subs["hand_pair_006_064"]
        self.assertEqual((hand["kind"], hand["observed_count"], hand["in_systematic_class"]), STANDING_HAND)
        self.assertEqual(subs["hapax_pairs"], STANDING_HAPAX_PAIRS)
        self.assertEqual(subs["family_max_count"], STANDING_FAMILY_MAX)
        systematic = [row for row in subs["pairs"] if row["kind"] == "systematic"]
        self.assertEqual(len(systematic), len(STANDING_CLASSES))
        above = [row for row in systematic if row["above_family_max"]]
        self.assertEqual([(row["a"], row["b"]) for row in above], [("400", "600"), ("002", "021")])

    def test_only_one_indel_pattern_is_systematic(self):
        indels = self.stem["indels"]
        systematic = [row for row in indels["patterns"] if row["kind"] == "systematic"]
        self.assertEqual(len(systematic), STANDING_SYSTEMATIC_INDELS)
        row = systematic[0]
        self.assertEqual(
            (row["sign"], row["left_neighbor"], row["right_neighbor"], row["count"], row["kind"]),
            STANDING_INDEL,
        )

    def test_ligature_option_still_finds_hpq_and_gk(self):
        ligature = self.result["ligature_atomic"]
        comparison = ligature["published_comparison"]
        self.assertEqual(ligature["significant_passages"], STANDING_LIGATURE_SIGNIFICANT)
        self.assertEqual(ligature["null"]["max_score"], 0)
        self.assertEqual(tuple(comparison["published_recovered"]), STANDING_LIGATURE_RECOVERED)
        self.assertEqual(tuple(comparison["published_absent"]), STANDING_LIGATURE_ABSENT)
        classes = ligature["substitutions"]["classes"]
        self.assertEqual(len(classes), 1)
        self.assertEqual((classes[0]["id"], tuple(classes[0]["members"])), STANDING_LIGATURE_CLASS)
        self.assertTrue(ligature["decompose_ligatures"] is False)
        self.assertTrue(self.stem["decompose_ligatures"] is True)

    def test_written_report_and_json_match_the_run(self):
        self.assertEqual(JSON_PATH.read_text(encoding="utf-8"), render_json(self.result))
        self.assertEqual(DOC_PATH.read_text(encoding="utf-8"), render_markdown(self.result))
        text = DOC_PATH.read_text(encoding="utf-8")
        self.assertIn("assigns no readings", text)
        self.assertIn("Hr2:36", text)
        self.assertIn("095", text)
        self.assertIn("400", text)
        self.assertIn("Comparison with the Track A cited merges", text)
        self.assertIn("abstract_56_and_84", text)
        self.assertIn("hand_digit_4_to_6", text)
        self.assertIn("gaping_mouth_to_bird", text)
        self.assertIn("horley_one_to_one", text)


if __name__ == "__main__":
    unittest.main()
