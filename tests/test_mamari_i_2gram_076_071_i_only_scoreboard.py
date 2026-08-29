"""I's cycle-170 leftover 2-gram 076 071 off-I lock.

Cycle 171 text-search lock. Uses already-vendored A–V and the
cycle-170 leftover 2-gram 076 071 (the n=2 run shared by
leftover n=4 maximals 999 090 076 071, 999 205 076 071,
076 071 009 090, and 076 071 090 999). Does not retune that
2-gram or the leftover n=4 set. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same claim-shape as cycle 167 (999 090 076 was I-only 16/0),
cycle 160 (076 020 010 was I-only 12/0), and cycle 141
(076 010 079 was I-only 8/0). This cycle is the new leftover
2-gram 076 071 only. 071 999 (071 065 071 999) does not
count. 076 076 (700 076 076 053) does not. Do not retune
999 090 076, 076 020 010, or 076 010 079. Cycle 52 already
locked 43 on Ia among eight early fixtures; this cycle is
the dedicated A–V lock. Do not assume the I-only result.

Locks exact consecutive hits of 076 071 on tablet I and
on every other vendored tablet A–H and J–V. Claim that can
lose: i_2gram_076_071_i_only (I hits ≥ 1 and off-I hits
== 0). True only if N_off_I == 0. Ia is exactly 43; Ib
unpublished 0; every other vendored tablet is exact-0. Not
an n≥8 island. Not the cycle-103 I 5-gram.

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
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    GRAM2 as CYCLE170_GRAM2,
    NEAR_MISS_071_065_071_999,
    NEAR_MISS_700_076_076_053,
    STANDING_MATCHING_LEFTOVERS,
    TestMamariILeftoverN4076071Scoreboard,
)
from tests.test_mamari_i_leftover_n4_999_090_076_scoreboard import (
    STANDING_MATCHING_LEFTOVERS as CYCLE166_MATCHING_LEFTOVERS,
)
from tests.test_mamari_i_leftover_n4_independent_n5_n3_overlap_scoreboard import (
    TestMamariILeftoverN4IndependentN5N3OverlapScoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_010_079_i_only_scoreboard import (
    TestMamariIOverlap3gram076010079IOnlyScoreboard,
)
from tests.test_mamari_i_overlap_3gram_076_020_010_i_only_scoreboard import (
    GRAM3 as CYCLE160_GRAM3,
    TestMamariIOverlap3gram076020010IOnlyScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    GRAM_076_071,
    STANDING_076_071_HITS,
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    OFF_I_TABLETS,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
    load_vendored_by_tablet,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

HYPOTHESIS_I_ONLY = True
GRAM2 = CYCLE170_GRAM2
STANDING_N2 = 2
STANDING_I_HITS = 43
STANDING_IA_HITS = 43
STANDING_IB_HITS = 0
STANDING_N_ON_I = 43
STANDING_N_I = 43
STANDING_I_SITES = (
    (SIDE_IA, "Ia1", 86),
    (SIDE_IA, "Ia1", 163),
    (SIDE_IA, "Ia2", 43),
    (SIDE_IA, "Ia2", 51),
    (SIDE_IA, "Ia2", 104),
    (SIDE_IA, "Ia2", 169),
    (SIDE_IA, "Ia3", 13),
    (SIDE_IA, "Ia3", 53),
    (SIDE_IA, "Ia3", 81),
    (SIDE_IA, "Ia3", 85),
    (SIDE_IA, "Ia3", 110),
    (SIDE_IA, "Ia3", 133),
    (SIDE_IA, "Ia3", 147),
    (SIDE_IA, "Ia4", 155),
    (SIDE_IA, "Ia5", 3),
    (SIDE_IA, "Ia5", 24),
    (SIDE_IA, "Ia5", 67),
    (SIDE_IA, "Ia5", 79),
    (SIDE_IA, "Ia5", 134),
    (SIDE_IA, "Ia5", 161),
    (SIDE_IA, "Ia6", 117),
    (SIDE_IA, "Ia7", 32),
    (SIDE_IA, "Ia7", 48),
    (SIDE_IA, "Ia7", 166),
    (SIDE_IA, "Ia8", 27),
    (SIDE_IA, "Ia9", 10),
    (SIDE_IA, "Ia12", 6),
    (SIDE_IA, "Ia12", 19),
    (SIDE_IA, "Ia12", 59),
    (SIDE_IA, "Ia12", 63),
    (SIDE_IA, "Ia12", 71),
    (SIDE_IA, "Ia13", 44),
    (SIDE_IA, "Ia13", 54),
    (SIDE_IA, "Ia13", 92),
    (SIDE_IA, "Ia13", 101),
    (SIDE_IA, "Ia13", 114),
    (SIDE_IA, "Ia13", 128),
    (SIDE_IA, "Ia13", 149),
    (SIDE_IA, "Ia13", 153),
    (SIDE_IA, "Ia14", 81),
    (SIDE_IA, "Ia14", 106),
    (SIDE_IA, "Ia14", 136),
    (SIDE_IA, "Ia14", 166),
)
STANDING_IB_SITES = ()
STANDING_OFF_I_HITS = 0
STANDING_N_OFF_I = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_2gram_076_071_i_only"
STANDING_I_2GRAM_076_071_I_ONLY = True
STANDING_RESULT = "i_2gram_076_071_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE141_3GRAM = False
STANDING_SAME_AS_CYCLE160_3GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_SHARED_WITH_CYCLE166_FAMILY = (("999", "090", "076", "071"),)


def i_2gram_076_071_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


class TestI2gram076071IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-170 leftover 2-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 2-gram counts; a gap is not a hit. 071 999 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(GRAM2, CYCLE170_GRAM2)
        self.assertEqual(GRAM2, GRAM_076_071)
        adjacent = [list(GRAM2), list(GRAM2)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM2), 2)
        overlap = [["076", "071", "076", "071"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM2), 2)
        gapped = [list(GRAM2[:1]) + ["006"] + list(GRAM2[1:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM2), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_071_065_071_999)], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM2), 0)
        self.assertEqual(ngram_hit_count([["071", "999"]], GRAM2), 0)
        self.assertEqual(ngram_hit_count([["076", "076"]], GRAM2), 0)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0."""
        provider = MockProvider()
        self.assertTrue(i_2gram_076_071_i_only(1, 0))
        self.assertTrue(i_2gram_076_071_i_only(43, 0))
        self.assertFalse(i_2gram_076_071_i_only(1, 1))
        self.assertFalse(i_2gram_076_071_i_only(0, 0))
        self.assertFalse(i_2gram_076_071_i_only(0, 43))
        self.assertEqual(STANDING_CLAIM, "i_2gram_076_071_i_only")
        self.assertTrue(STANDING_I_2GRAM_076_071_I_ONLY)
        self.assertEqual(
            STANDING_I_2GRAM_076_071_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_2gram_is_cycle170_leftover_not_the_cycle_103_5gram(self):
        """2-gram is the cycle-170 leftover, not 071 999, 076 076, or the 3-grams."""
        provider = MockProvider()
        self.assertEqual(GRAM2, CYCLE170_GRAM2)
        self.assertNotEqual(GRAM2, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE160_GRAM3)
        self.assertNotEqual(GRAM2, ("076", "010", "079"))
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM2, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE141_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE160_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N2, 2)
        self.assertLess(len(GRAM2), 8)
        for leftover in STANDING_MATCHING_LEFTOVERS:
            self.assertTrue(is_contiguous_substring(GRAM2, leftover))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_071_065_071_999))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertTrue(is_contiguous_substring(("071", "999"), NEAR_MISS_071_065_071_999))
        self.assertTrue(is_contiguous_substring(("076", "076"), NEAR_MISS_700_076_076_053))
        shared = set(STANDING_MATCHING_LEFTOVERS) & set(CYCLE166_MATCHING_LEFTOVERS)
        self.assertEqual(shared, set(STANDING_SHARED_WITH_CYCLE166_FAMILY))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI2gram076071IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 2-gram 076 071 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM2)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM2, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM2, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.claim_holds = i_2gram_076_071_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_170_leftover_not_retuned(self):
        """2-gram is the cycle-170 leftover lock, not a new inventory."""
        self.assertEqual(GRAM2, CYCLE170_GRAM2)
        self.assertEqual(GRAM2, ("076", "071"))
        prior_170 = self.survey["i_leftover_n4_076_071"]
        self.assertEqual(prior_170["cycle"], 170)
        self.assertEqual(tuple(prior_170["tokens2"]), GRAM2)
        self.assertEqual(prior_170["N_with_076_071"], 4)
        self.assertEqual(prior_170["N_without_076_071"], 23)
        measured_matching = [list(gram) for gram in STANDING_MATCHING_LEFTOVERS]
        self.assertEqual(prior_170["matching_leftovers"], measured_matching)
        self.assertTrue(prior_170["i_leftover_n4_exactly_4_contain_076_071"])
        self.assertTrue(prior_170["071_999_does_not_count"])
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertNotEqual(GRAM2, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE160_GRAM3)
        self.assertFalse(is_contiguous_substring(GRAM2, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(STANDING_I_HITS, STANDING_076_071_HITS[-1])
        self.assertEqual(STANDING_076_071_HITS[-1], 43)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_forty_three_on_ia(self):
        """2-gram is 43 on Ia; Ib unpublished 0."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 43)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 43)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 43)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM2, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM2), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N2]
            self.assertEqual(tuple(stems), GRAM2)
            self.assertEqual(side, SIDE_IA)
        self.assertEqual(
            STANDING_I_SITES[:3],
            ((SIDE_IA, "Ia1", 86), (SIDE_IA, "Ia1", 163), (SIDE_IA, "Ia2", 43)),
        )
        self.assertEqual(
            STANDING_I_SITES[13],
            (SIDE_IA, "Ia4", 155),
        )
        self.assertEqual(
            STANDING_I_SITES[42],
            (SIDE_IA, "Ia14", 166),
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_2gram_is_zero_off_i_and_i_only(self):
        """2-gram is 0 on A–H and J–V. Ia has exactly 43. W is not a tablet."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, STANDING_N_OFF_I)
        self.assertEqual(STANDING_N_OFF_I, 0)
        self.assertEqual(STANDING_OFF_I_SITES, ())
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM2))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 43)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(
            i_2gram_076_071_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_2GRAM_076_071_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_2GRAM_076_071_I_ONLY,
        )
        self.assertTrue(STANDING_I_2GRAM_076_071_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_2gram_076_071_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE141_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE160_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_170_167_160_159_141_103_and_w_scoreboards_still_compute(self):
        """Cycle 170 leftover, 167/160/141 I-only, 159 n≥3, 103 I-only, and W stay."""
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        prior_160 = TestMamariIOverlap3gram076020010IOnlyScoreboard()
        prior_160.setUp()
        prior_160.test_3gram_is_zero_off_i_and_i_only()
        prior_160.test_survey_matches_computed_lock()
        prior_159 = TestMamariILeftoverN4IndependentN5N3OverlapScoreboard()
        prior_159.setUp()
        prior_159.test_counts_5_of_27_and_hypothesis_n_5_holds()
        prior_159.test_survey_matches_computed_lock()
        prior_141 = TestMamariIOverlap3gram076010079IOnlyScoreboard()
        prior_141.setUp()
        prior_141.test_3gram_is_zero_off_i_and_i_only()
        prior_141.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-171 2-gram I-only lock."""
        lock = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(lock["cycle"], 171)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 43)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(lock["N_off_I"], 0)
        self.assertEqual(
            [list(site) for site in STANDING_OFF_I_SITES],
            lock["off_i_sites"],
        )
        self.assertEqual(tuple(lock["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(lock["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_2gram_076_071_i_only"])
        self.assertEqual(
            lock["i_2gram_076_071_i_only"],
            STANDING_I_2GRAM_076_071_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle141_3gram"])
        self.assertFalse(lock["same_as_cycle160_3gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_020_010_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_independent_n5_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"][
                "i_leftover_n4_exactly_4_contain_076_071"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_076_071"]["N_with_076_071"],
            4,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_076_071"]["N_without_076_071"],
            23,
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(
            self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_999_090_076"]["cycle"], 166)
        self.assertTrue(
            self.survey["i_leftover_n4_999_090_076"][
                "i_leftover_n4_exactly_7_contain_999_090_076"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_999_090_076"]["N_with_999_090_076"],
            7,
        )
        self.assertEqual(self.survey["i_leftover_n4_independent_n5_n3_overlap"]["cycle"], 159)
        self.assertTrue(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"][
                "i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"]["N_with_n3plus_overlap"],
            5,
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_i_only"]["cycle"], 160)
        self.assertTrue(
            self.survey["i_overlap_3gram_076_020_010_i_only"][
                "i_overlap_3gram_076_020_010_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_i_only"]["N_on_I"], 12)
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["cycle"], 141)
        self.assertTrue(
            self.survey["i_overlap_3gram_076_010_079_i_only"][
                "i_overlap_3gram_076_010_079_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["N_on_I"], 8)
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["N_off_I"], 0)
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


class TestMamariI2gram076071IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 171 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
