"""Round 3 Track A: word-sized units on the Great Tradition.

Sign strings only. The corpus case retrains the segmenters and the
shuffle nulls (about twenty seconds). MockProvider only. No readings.
"""

import math
import unittest

from agents.base.providers import MockProvider
from decipherment.round3_tracka import (
    DOC_PATH,
    UNITS_PATH,
    Line,
    Stem,
    Word,
    explode_hapax_chunks,
    gibbs_refine,
    greedy_segment,
    render_json,
    render_markdown,
    rule_words,
    run_round3_tracka,
    sign_cuts,
    utterances_unigram,
)

# Locks from the stem corpus and from one seeded run. Do not retune the
# segmenter to chase these.
STANDING_TOKENS = 14488
STANDING_RAW_INVENTORY = 630
STANDING_NORMALIZED_INVENTORY = 622
STANDING_REWRITE_TOKENS = 489
STANDING_REWRITES = {
    "011": 114,
    "021": 93,
    "056": 19,
    "081": 60,
    "256": 25,
    "290": 56,
    "385": 41,
    "400": 81,
}
STANDING_GT_TOKENS = 4050
STANDING_GT_LINES = 64
STANDING_GT_SIDES = ["Hr", "Hv", "Pr", "Pv", "Qr", "Qv"]
STANDING_GT_PAIRS = {"H–P": 32, "H–Q": 18, "P–Q": 19}
STANDING_INDEL_EVENTS = 128
STANDING_CUES = {
    "group_final_076": 653,
    "sign_095": 93,
    "pure_999": 96,
    "indel_cut_loci": 293,
    "sign_cut_loci": 1012,
    "union_cut_loci": 1291,
    "great_tradition_group_final_076": 15,
    "great_tradition_095": 27,
    "great_tradition_pure_999": 0,
}
STANDING_NORM_GT = {
    "compared": 1588,
    "raw_matches": 1369,
    "normalized_matches": 1410,
    "mismatches_resolved": 41,
}
STANDING_NORM_ALL = {
    "compared": 2006,
    "raw_matches": 1752,
    "normalized_matches": 1796,
    "mismatches_resolved": 44,
}
STANDING_P001 = {
    "locus_left": "Hr2:36..Hr4:0",
    "locus_right": "Qr2:0..Qr3:65",
    "span": 125,
    "parallel_sites": 117,
}
STANDING_PARALLEL_SITES = 1416
STANDING_LEXICON_UNITS = 267
STANDING_PRIMARY = "mdl_cued"
# Great Tradition count, corpus count, and whether the unit ends in 076.
STANDING_TOP_UNITS = (
    (("004", "064"), 28, 76, False),
    (("015", "022"), 17, 17, False),
    (("067", "010"), 9, 17, False),
    (("260", "001"), 8, 23, False),
    (("430", "076"), 4, 45, True),
)
STANDING_OVER_CAP = (
    (("003", "306", "003", "084", "004", "280", "200", "048", "254", "755", "003", "734", "003", "306", "003"), 15, 2),
    (("069", "162", "200", "200", "200", "052", "200", "008", "200", "001", "004", "064", "044", "004", "049", "004", "044", "004", "064", "202", "280"), 21, 2),
)
STANDING_MDL_CUED_HISTOGRAM = {
    "1": 3597,
    "2": 108,
    "3": 5,
    "4": 0,
    "5": 11,
    "6": 2,
    "7": 1,
    "8": 0,
    "9": 0,
    "10": 4,
    "11": 0,
    "12": 3,
    "13+": 4,
}
STANDING_RULES_GT_TOKENS = 334
STANDING_NULL_REACHED = 0
FORBIDDEN_KEYS = frozenset({"gloss", "phonetic", "translation", "syllable", "reading_value"})


class GuardProvider(MockProvider):
    """Fails the test if Track A asks for a completion."""

    def complete(self, messages, **kwargs):
        raise AssertionError("Track A must not request a completion")

    def complete_with_vision(self, messages, images, **kwargs):
        raise AssertionError("Track A must not request a completion")


def _line(groups: list[list[str]], side: str = "Hr") -> Line:
    stems: list[Stem] = []
    index = 0
    for group in groups:
        for offset, raw in enumerate(group):
            stems.append(
                Stem(
                    side=side,
                    tablet=side[0],
                    line=f"{side}1",
                    line_number=1,
                    index=index,
                    offset=offset,
                    raw=raw,
                    normalized=raw,
                    group_final=offset == len(group) - 1,
                    group_len=len(group),
                )
            )
            index += 1
    return Line(side, side[0], f"{side}1", tuple(stems))


def _words(result: dict) -> list[tuple[str, ...]]:
    return [word.signs for utterance in result["utterances"] for word in utterance]


class TestRuleCuts(unittest.TestCase):
    def test_group_final_076_and_095_split_the_chunk(self):
        line = _line([["600", "076"], ["003"], ["095"], ["006"]])
        words = rule_words([line], sign_cuts([line]))
        self.assertEqual(
            [word.signs for utterance in words for word in utterance],
            [("600", "076"), ("003",), ("095",), ("006",)],
        )

    def test_076_inside_a_group_is_not_a_cut(self):
        line = _line([["076", "001"]])
        self.assertEqual(sign_cuts([line]), set())
        words = rule_words([line], sign_cuts([line]))
        self.assertEqual(
            [word.signs for utterance in words for word in utterance],
            [("076", "001")],
        )


class TestUnsupervisedToys(unittest.TestCase):
    def test_mdl_merges_a_repeated_bigram(self):
        signs = ["200", "300"] * 8
        line = _line([[sign] for sign in signs])
        result = greedy_segment(
            utterances_unigram([line]),
            objective="mdl",
            alphabet=2,
            verify=True,
        )
        self.assertEqual(result["rounds"], 1)
        self.assertEqual(_words(result), [("200", "300")] * 8)
        self.assertAlmostEqual(result["score"], 3 * math.log2(3), places=6)

    def test_explode_opens_a_hapax_and_keeps_a_repeat(self):
        unique = [Word(("001", "002", "003"), (("Hr", 0), ("Hr", 1), ("Hr", 2)))]
        repeat_a = [Word(("004", "005"), (("Hr", 3), ("Hr", 4)))]
        repeat_b = [Word(("004", "005"), (("Pr", 0), ("Pr", 1)))]
        exploded = explode_hapax_chunks([unique, repeat_a, repeat_b])
        self.assertEqual([word.signs for word in exploded[0]], [("001",), ("002",), ("003",)])
        self.assertEqual(exploded[1][0].signs, ("004", "005"))
        self.assertEqual(exploded[2][0].signs, ("004", "005"))

    def test_gibbs_same_seed_matches(self):
        signs = ["200", "300"] * 6
        line = _line([[sign] for sign in signs])
        start = utterances_unigram([line])
        first = gibbs_refine(start, alphabet=50, seed=0, sweeps=3)
        second = gibbs_refine(start, alphabet=50, seed=0, sweeps=3)
        self.assertEqual(_words(first), _words(second))
        self.assertEqual(first["seed"], 0)

    def test_rejects_a_provider_that_is_not_mock(self):
        with self.assertRaises(TypeError):
            run_round3_tracka(object())  # type: ignore[arg-type]


class TestCorpusSegmentation(unittest.TestCase):
    result: dict

    @classmethod
    def setUpClass(cls):
        cls.result = run_round3_tracka(GuardProvider())

    def test_outputs_match_the_committed_artifacts(self):
        self.assertEqual(render_json(self.result), UNITS_PATH.read_text(encoding="utf-8"))
        self.assertEqual(render_markdown(self.result), DOC_PATH.read_text(encoding="utf-8"))

    def test_corpus_and_normalization_locks(self):
        result = self.result
        self.assertEqual(result["provider"], "MockProvider")
        self.assertEqual(result["provider_calls"], 0)
        self.assertFalse(result["readings_assigned"])
        self.assertTrue(result["unread"])
        self.assertEqual(result["primary_segmenter"], STANDING_PRIMARY)
        corpus = result["corpus"]
        self.assertEqual(corpus["tokens"], STANDING_TOKENS)
        self.assertEqual(corpus["raw_inventory"], STANDING_RAW_INVENTORY)
        self.assertEqual(corpus["normalized_inventory"], STANDING_NORMALIZED_INVENTORY)
        self.assertEqual(corpus["rewrite_tokens"], STANDING_REWRITE_TOKENS)
        self.assertEqual(corpus["rewrites"], STANDING_REWRITES)
        gt = result["great_tradition"]
        self.assertEqual(gt["tokens"], STANDING_GT_TOKENS)
        self.assertEqual(gt["lines"], STANDING_GT_LINES)
        self.assertEqual(gt["sides"], STANDING_GT_SIDES)
        self.assertEqual(result["cues"]["indel_events"], STANDING_INDEL_EVENTS)
        for key, expected in STANDING_CUES.items():
            self.assertEqual(result["cues"][key], expected, key)
        passages = result["passages"]
        self.assertEqual(passages["significant"], 99)
        self.assertEqual(passages["great_tradition_pairs"], STANDING_GT_PAIRS)
        self.assertEqual(passages["p001"], STANDING_P001)
        self.assertEqual(passages["normalization_great_tradition"], STANDING_NORM_GT)
        self.assertEqual(passages["normalization_all"], STANDING_NORM_ALL)

    def test_segmenter_and_null_locks(self):
        result = self.result
        mdl = result["segmenters"]["mdl_cued"]
        self.assertEqual(mdl["rounds"], 138)
        self.assertEqual(mdl["great_tradition"]["length"]["tokens"], 3735)
        self.assertEqual(mdl["great_tradition"]["length"]["histogram"], STANDING_MDL_CUED_HISTOGRAM)
        self.assertEqual(mdl["corpus"]["frequency"]["repeated_multisign_types"], 49)
        rules = result["segmenters"]["rules"]
        self.assertEqual(rules["rounds"], 0)
        self.assertEqual(rules["great_tradition"]["length"]["tokens"], STANDING_RULES_GT_TOKENS)
        self.assertEqual(result["segmenters"]["gibbs"]["gibbs_flips"], 0)
        self.assertEqual(result["segmenters"]["gibbs"]["gibbs_sites"], 14211)
        self.assertEqual(result["segmenters"]["gibbs_cued"]["gibbs_flips"], 0)
        for name in ("mdl", "mdl_cued", "dp", "dp_cued"):
            for statistic in ("repeated_multisign_types", "code_per_sign"):
                self.assertEqual(
                    result["nulls"][name][statistic]["null_reached"],
                    STANDING_NULL_REACHED,
                    f"{name} {statistic}",
                )
        for name, block in result["parallel_agreement"].items():
            gt = block["great_tradition"]
            self.assertEqual(gt["sites"], STANDING_PARALLEL_SITES, name)
            self.assertEqual(gt["null_ge"], 0, name)
            self.assertEqual(block["p001"]["sites"], 117, name)

    def test_lexicon_is_unread_sign_strings(self):
        lexicon = self.result["lexicon"]
        self.assertEqual(lexicon["segmenter"], STANDING_PRIMARY)
        self.assertEqual(lexicon["units"], STANDING_LEXICON_UNITS)
        self.assertEqual(lexicon["consensus_units"], STANDING_LEXICON_UNITS)
        self.assertEqual(lexicon["ends_with_076"], 2)
        items = lexicon["items"]
        self.assertTrue(all(item["reading"] is None for item in items))
        by_signs = {tuple(item["signs"]): item for item in items}
        for signs, count, corpus_count, ends in STANDING_TOP_UNITS:
            item = by_signs[signs]
            self.assertEqual(item["count"], count, signs)
            self.assertEqual(item["corpus_count"], corpus_count, signs)
            self.assertEqual(item["ends_with_076"], ends, signs)
        over = {
            tuple(item["signs"]): item
            for item in items
            if item["length"] > 12
        }
        self.assertEqual(len(over), len(STANDING_OVER_CAP))
        for signs, length, count in STANDING_OVER_CAP:
            self.assertEqual(over[signs]["length"], length)
            self.assertEqual(over[signs]["count"], count)
        self._assert_no_reading_keys(self.result)

    def test_note_states_the_f1_and_cap_limits(self):
        note = DOC_PATH.read_text(encoding="utf-8")
        self.assertIn("cuts at nearly every site", note)
        self.assertIn("longer than the merge cap of 12", note)
        self.assertIn("`076` alone", note)

    def _assert_no_reading_keys(self, value: object) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                self.assertNotIn(key, FORBIDDEN_KEYS)
                self._assert_no_reading_keys(child)
        elif isinstance(value, list):
            for child in value:
                self._assert_no_reading_keys(child)
