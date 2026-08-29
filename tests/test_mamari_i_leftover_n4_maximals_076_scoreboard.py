"""I's cycle-136 leftover n=4 maximals vs stem 076.

Cycle 137 text-search lock. Uses already-vendored A–V and the
cycle-136 leftover n=4 maximal set (27 independent n=4 grams
that are not substrings of the four I 5-grams). Does not vendor
a new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning dictionary.

For each leftover n=4 maximal, whether the gram contains token
076 (Santiago staff formulaic glyph). Hypothesis: all 27
contain at least one 076. Measured: 26 of 27 do. The exception
is 071 065 071 999 at Ia9[1]/Ia9[56]. Claim that can lose:
i_leftover_n4_maximals_all_contain_076. The claim is false.
Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    STANDING_HYPOTHESIZED_N5,
    STANDING_LEFTOVER_N4_COUNT,
    STANDING_MAXIMALS,
    STANDING_N,
    TestMamariIIndependentNge4MaximalsScoreboard,
    leftover_n4_rows,
)
from tests.test_mamari_i_nge4_scoreboard import (
    STANDING_INDEPENDENT,
    STANDING_INDEPENDENT_COUNT,
    TestMamariINge4Scoreboard,
    nge4_sites,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_076_inventory_scoreboard import STEM_076
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HYPOTHESIS_ALL_CONTAIN_076 = True
STANDING_LEFTOVER_N = 27
STANDING_WITH_076 = 26
STANDING_WITHOUT_076 = 1
EXCEPTION_GRAM = (
    "071",
    "065",
    "071",
    "999",
)
EXCEPTION_SITES = (("Ia", "Ia9", 1), ("Ia", "Ia9", 56))
STANDING_EXCEPTIONS = (
    (EXCEPTION_GRAM, 4, 2, EXCEPTION_SITES),
)
STANDING_LEFTOVER = (
    (("999", "090", "076", "070"), 4, 5, (("Ia", "Ia2", 9), ("Ia", "Ia4", 111), ("Ia", "Ia7", 67), ("Ia", "Ia7", 128), ("Ia", "Ia14", 139))),
    (("090", "076", "020", "010"), 4, 4, (("Ia", "Ia2", 119), ("Ia", "Ia4", 86), ("Ia", "Ia5", 143), ("Ia", "Ia12", 83))),
    (("028", "076", "011", "076"), 4, 3, (("Ia", "Ia1", 136), ("Ia", "Ia4", 125), ("Ia", "Ia14", 78))),
    (("021", "090", "076", "087"), 4, 3, (("Ia", "Ia4", 116), ("Ia", "Ia5", 27), ("Ia", "Ia6", 77))),
    (("999", "090", "076", "071"), 4, 3, (("Ia", "Ia4", 153), ("Ia", "Ia5", 1), ("Ia", "Ia5", 22))),
    (("071", "999", "604", "076"), 4, 2, (("Ia", "Ia1", 63), ("Ia", "Ia9", 3))),
    (("600", "090", "076", "011"), 4, 2, (("Ia", "Ia2", 106), ("Ia", "Ia14", 53))),
    (("076", "020", "010", "050"), 4, 2, (("Ia", "Ia2", 120), ("Ia", "Ia14", 110))),
    (("000", "999", "090", "076"), 4, 2, (("Ia", "Ia3", 35), ("Ia", "Ia5", 0))),
    (("999", "090", "076", "013"), 4, 2, (("Ia", "Ia3", 36), ("Ia", "Ia6", 91))),
    (("999", "205", "076", "071"), 4, 2, (("Ia", "Ia3", 51), ("Ia", "Ia3", 79))),
    (("999", "090", "076", "005"), 4, 2, (("Ia", "Ia3", 70), ("Ia", "Ia13", 108))),
    (("076", "010", "079", "090"), 4, 2, (("Ia", "Ia5", 110), ("Ia", "Ia5", 139))),
    (("072", "076", "010", "079"), 4, 2, (("Ia", "Ia5", 138), ("Ia", "Ia13", 71))),
    (("076", "071", "009", "090"), 4, 2, (("Ia", "Ia5", 161), ("Ia", "Ia12", 71))),
    (("202", "076", "006", "055"), 4, 2, (("Ia", "Ia6", 48), ("Ia", "Ia12", 119))),
    (("076", "071", "090", "999"), 4, 2, (("Ia", "Ia7", 166), ("Ia", "Ia14", 136))),
    (("076", "999", "029", "076"), 4, 2, (("Ia", "Ia8", 30), ("Ia", "Ia10", 144))),
    (("999", "021", "090", "076"), 4, 2, (("Ia", "Ia8", 104), ("Ia", "Ia13", 15))),
    (("090", "076", "057", "600"), 4, 2, (("Ia", "Ia8", 114), ("Ia", "Ia9", 28))),
    (("700", "076", "076", "053"), 4, 2, (("Ia", "Ia8", 167), ("Ia", "Ia9", 32))),
    (("071", "065", "071", "999"), 4, 2, (("Ia", "Ia9", 1), ("Ia", "Ia9", 56))),
    (("999", "090", "076", "057"), 4, 2, (("Ia", "Ia9", 27), ("Ia", "Ia9", 128))),
    (("430", "076", "001", "076"), 4, 2, (("Ia", "Ia10", 103), ("Ia", "Ia13", 156))),
    (("053", "076", "020", "010"), 4, 2, (("Ia", "Ia12", 0), ("Ia", "Ia14", 109))),
    (("090", "999", "090", "076"), 4, 2, (("Ia", "Ia12", 45), ("Ia", "Ia14", 138))),
    (("430", "076", "049", "400"), 4, 2, (("Ia", "Ia13", 170), ("Ia", "Ia14", 63))),
)
STANDING_CONTAINS_076 = (
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_maximals_all_contain_076"
STANDING_I_LEFTOVER_N4_MAXIMALS_ALL_CONTAIN_076 = False
STANDING_RESULT = "i_leftover_n4_maximals_076"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def gram_contains_076(
    gram: tuple[str, ...],
    stem: str = STEM_076,
) -> bool:
    """True iff the gram contains at least one token 076."""
    return stem in gram


def leftover_with_076(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    stem: str = STEM_076,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 maximals that contain stem 076."""
    return tuple(row for row in rows if stem in row[0])


def leftover_without_076(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...] = STANDING_LEFTOVER,
    stem: str = STEM_076,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover n=4 maximals that do not contain stem 076."""
    return tuple(row for row in rows if stem not in row[0])


def i_leftover_n4_maximals_all_contain_076(
    rows: tuple[tuple[tuple[str, ...], int, int, tuple], ...],
    stem: str = STEM_076,
) -> bool:
    """True iff every leftover n=4 maximal contains stem 076.

    An empty leftover set is false here (the cycle-136 leftover
    set must be present and every member must contain 076).
    """
    return bool(rows) and all(stem in gram for gram, _n, _f, _s in rows)


class TestILeftoverN4Maximals076Helpers(unittest.TestCase):
    """Helpers on cycle-136 leftover tokens. No CV, no LLM."""

    def test_contains_076_and_all_contain_can_fail(self):
        """26 leftovers with 076 hold the claim; the full 27 lose."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N)
        self.assertEqual(STANDING_LEFTOVER_N, STANDING_LEFTOVER_N4_COUNT)
        self.assertEqual(STEM_076, "076")
        self.assertTrue(gram_contains_076(("071", "999", "604", "076")))
        self.assertTrue(gram_contains_076(("076", "010", "079", "090")))
        self.assertTrue(gram_contains_076(("700", "076", "076", "053")))
        self.assertFalse(gram_contains_076(EXCEPTION_GRAM))
        self.assertFalse(gram_contains_076(("071", "065", "071", "999")))
        self.assertFalse(i_leftover_n4_maximals_all_contain_076(()))
        with_076 = leftover_with_076(leftover)
        without_076 = leftover_without_076(leftover)
        self.assertEqual(len(with_076), STANDING_WITH_076)
        self.assertEqual(len(without_076), STANDING_WITHOUT_076)
        self.assertTrue(i_leftover_n4_maximals_all_contain_076(with_076))
        self.assertFalse(i_leftover_n4_maximals_all_contain_076(without_076))
        self.assertFalse(i_leftover_n4_maximals_all_contain_076(leftover))
        self.assertEqual(without_076, STANDING_EXCEPTIONS)
        self.assertEqual(without_076[0][0], EXCEPTION_GRAM)
        self.assertEqual(without_076[0][3], EXCEPTION_SITES)
        self.assertEqual(tuple(STEM_076 in gram for gram, _n, _f, _s in leftover), STANDING_CONTAINS_076)
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_maximals_all_contain_076")
        self.assertFalse(STANDING_I_LEFTOVER_N4_MAXIMALS_ALL_CONTAIN_076)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_N4_MAXIMALS_ALL_CONTAIN_076,
            HYPOTHESIS_ALL_CONTAIN_076,
        )
        self.assertEqual(STANDING_WITH_076 + STANDING_WITHOUT_076, STANDING_LEFTOVER_N)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftovers_are_n4_maximals_not_5gram_substrings(self):
        """Cycle-136 leftover set: 27 n=4 maximals outside the four 5-grams."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        maximal_n4 = tuple(row for row in STANDING_MAXIMALS if row[1] == 4)
        self.assertEqual(len(maximal_n4), STANDING_LEFTOVER_N)
        self.assertEqual(
            {gram for gram, _n, _f, _s in leftover},
            {gram for gram, _n, _f, _s in maximal_n4},
        )
        for gram, n, _freq, _sites in leftover:
            self.assertEqual(n, 4)
            self.assertEqual(len(gram), 4)
            for five in STANDING_HYPOTHESIZED_N5:
                self.assertFalse(is_contiguous_substring(gram, five))
        self.assertIn(EXCEPTION_GRAM, {gram for gram, _n, _f, _s in leftover})
        self.assertNotIn(GRAM5, {gram for gram, _n, _f, _s in leftover})
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Maximals076Scoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 maximals vs 076. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.with_076 = leftover_with_076(self.leftover)
        self.without_076 = leftover_without_076(self.leftover)
        self.claim_holds = i_leftover_n4_maximals_all_contain_076(self.leftover)

    def test_tokens_are_cycle_136_leftover_not_invented(self):
        """Leftover set is the cycle-136 lock, not a new inventory."""
        self.assertEqual(self.leftover, STANDING_LEFTOVER)
        self.assertEqual(leftover_n4_rows(), STANDING_LEFTOVER)
        self.assertEqual(len(STANDING_LEFTOVER), STANDING_LEFTOVER_N)
        self.assertEqual(STANDING_LEFTOVER_N, 27)
        self.assertEqual(STANDING_LEFTOVER_N4_COUNT, 27)
        prior = TestMamariIIndependentNge4MaximalsScoreboard()
        prior.setUp()
        self.assertEqual(len(prior.maximals), STANDING_N)
        self.assertEqual(STANDING_N, 31)
        leftover_tokens = {gram for gram, _n, _f, _s in STANDING_LEFTOVER}
        maximal_n4 = {gram for gram, n, _f, _s in prior.maximals if n == 4}
        self.assertEqual(leftover_tokens, maximal_n4)
        self.assertEqual(len(STANDING_INDEPENDENT), STANDING_INDEPENDENT_COUNT)
        self.assertEqual(STANDING_INDEPENDENT_COUNT, 39)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertFalse(
            self.survey["i_independent_nge4_maximals"]["i_independent_nge4_has_exactly_4_maximals"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertEqual(self.survey["i_repeating_nge4"]["independent_count"], 39)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_26_of_27_and_hypothesis_all_contain_loses(self):
        """26 leftovers contain 076; 1 does not. Claim is false."""
        self.assertEqual(len(self.leftover), STANDING_LEFTOVER_N)
        self.assertEqual(len(self.with_076), STANDING_WITH_076)
        self.assertEqual(len(self.without_076), STANDING_WITHOUT_076)
        self.assertEqual(STANDING_WITH_076, 26)
        self.assertEqual(STANDING_WITHOUT_076, 1)
        self.assertEqual(STANDING_LEFTOVER_N, STANDING_WITH_076 + STANDING_WITHOUT_076)
        self.assertTrue(HYPOTHESIS_ALL_CONTAIN_076)
        self.assertFalse(i_leftover_n4_maximals_all_contain_076(self.leftover))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_MAXIMALS_ALL_CONTAIN_076,
        )
        self.assertFalse(STANDING_I_LEFTOVER_N4_MAXIMALS_ALL_CONTAIN_076)
        self.assertEqual(STANDING_CLAIM, "i_leftover_n4_maximals_all_contain_076")
        self.assertEqual(
            tuple(STEM_076 in gram for gram, _n, _f, _s in self.leftover),
            STANDING_CONTAINS_076,
        )
        self.assertEqual(sum(1 for flag in STANDING_CONTAINS_076 if flag), STANDING_WITH_076)
        self.assertEqual(
            sum(1 for flag in STANDING_CONTAINS_076 if not flag),
            STANDING_WITHOUT_076,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_exception_is_071_065_071_999_at_ia9(self):
        """The only leftover without 076 is 071 065 071 999 at Ia9."""
        self.assertEqual(self.without_076, STANDING_EXCEPTIONS)
        self.assertEqual(len(STANDING_EXCEPTIONS), 1)
        gram, n, freq, sites = STANDING_EXCEPTIONS[0]
        self.assertEqual(gram, EXCEPTION_GRAM)
        self.assertEqual(n, 4)
        self.assertEqual(freq, 2)
        self.assertEqual(sites, EXCEPTION_SITES)
        self.assertFalse(gram_contains_076(gram))
        self.assertNotIn(STEM_076, gram)
        for other, _n, _f, _s in self.with_076:
            self.assertTrue(gram_contains_076(other))
            self.assertIn(STEM_076, other)
            self.assertNotEqual(other, EXCEPTION_GRAM)
        self.assertIn(EXCEPTION_GRAM, {g for g, _n, _f, _s in self.leftover})
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_sites_on_i(self):
        """Leftover I sites; Ib unpublished; each site matches the locked stems."""
        self.assertEqual(self.leftover, STANDING_LEFTOVER)
        for gram, n, freq, sites in self.leftover:
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), freq)
            for side, line, index in sites:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + n]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
        self.assertEqual(
            nge4_sites(EXCEPTION_GRAM, self.i_sides),
            EXCEPTION_SITES,
        )
        self.assertEqual(
            STANDING_EXCEPTIONS[0][3],
            (("Ia", "Ia9", 1), ("Ia", "Ia9", 56)),
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_136_135_103_and_w_scoreboards_still_compute(self):
        """Cycle 136 maximals, 135 I n≥4, 103 I-only, and W stay."""
        prior_136 = TestMamariIIndependentNge4MaximalsScoreboard()
        prior_136.setUp()
        prior_136.test_n_is_31_and_hypothesis_n_4_loses()
        prior_136.test_survey_matches_computed_lock()
        prior_135 = TestMamariINge4Scoreboard()
        prior_135.setUp()
        prior_135.test_counts_and_hypothesis_all_substrings_loses()
        prior_135.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-137 leftover 076 lock."""
        lock = self.survey["i_leftover_n4_maximals_076"]
        self.assertEqual(lock["cycle"], 137)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_contain_076"])
        self.assertEqual(lock["hypothesis_all_contain_076"], HYPOTHESIS_ALL_CONTAIN_076)
        self.assertEqual(lock["leftover_n4_count"], STANDING_LEFTOVER_N)
        self.assertEqual(lock["with_076_count"], STANDING_WITH_076)
        self.assertEqual(lock["without_076_count"], STANDING_WITHOUT_076)
        self.assertEqual(lock["stem"], STEM_076)
        measured_leftovers = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
                "contains_076": STEM_076 in tokens,
            }
            for tokens, n, freq, sites in STANDING_LEFTOVER
        ]
        self.assertEqual(lock["leftovers"], measured_leftovers)
        measured_exceptions = [
            {
                "tokens": list(tokens),
                "n": n,
                "freq": freq,
                "sites": [list(site) for site in sites],
            }
            for tokens, n, freq, sites in STANDING_EXCEPTIONS
        ]
        self.assertEqual(lock["exceptions"], measured_exceptions)
        self.assertEqual(tuple(lock["contains_076"]), STANDING_CONTAINS_076)
        self.assertEqual(
            tuple(lock["exception_tokens"]),
            EXCEPTION_GRAM,
        )
        self.assertEqual(
            [list(site) for site in EXCEPTION_SITES],
            lock["exception_sites"],
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_n4_maximals_all_contain_076"])
        self.assertEqual(
            lock["i_leftover_n4_maximals_all_contain_076"],
            STANDING_I_LEFTOVER_N4_MAXIMALS_ALL_CONTAIN_076,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_independent_nge4_maximals_unchanged"])
        self.assertTrue(lock["standing_i_repeating_nge4_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["maximal_count"], 31)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertFalse(
            self.survey["i_independent_nge4_maximals"]["i_independent_nge4_has_exactly_4_maximals"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertFalse(
            self.survey["i_repeating_nge4"]["i_repeating_nge4_all_substrings_of_i_5gram"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["independent_count"], 39)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_n"], 5)
        self.assertEqual(self.survey["n_repeating_nge5"]["cycle"], 134)
        self.assertTrue(self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"])
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"], 5)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN4Maximals076ImageSnapshot(unittest.TestCase):
    """Cycle 137 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
