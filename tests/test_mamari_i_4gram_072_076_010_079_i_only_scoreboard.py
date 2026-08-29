"""I's cycle-144 leftover minority backward 4-gram off-I lock.

Cycle 148 text-search lock. Uses already-vendored A–V and the
cycle-144 leftover minority backward 4-gram 072 076 010 079
at leftover site Ia5[139]. Does not retune that 4-gram or
that site. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Locks exact consecutive hits of 072 076 010 079 on tablet I
and on every other vendored tablet A–H and J–V. Claim that
can lose: i_4gram_072_076_010_079_is_i_only (I hits ≥ 2 and
off-I hits == 0). Ia is exactly 2 at Ia5[138]/Ia13[71]; Ib
unpublished 0; every other vendored tablet is exact-0. The
4-gram starts one stem before leftover Ia5[139]. Not an
n≥8 island. Not the cycle-103 I 5-gram. Not the cycle-144
majority 071 076 010 079.

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
    MAXIMAL_N5_010,
)
from tests.test_mamari_i_leftover_076_010_079_backward_4gram_scoreboard import (
    STANDING_BACKWARD_4GRAM_071,
    STANDING_BACKWARD_4GRAM_072,
    TestMamariILeftover076010079Backward4gramScoreboard,
)
from tests.test_mamari_i_leftover_backward_5grams_i_only_scoreboard import (
    TestMamariILeftoverBackward5gramsIOnlyScoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_010_079_i_only_scoreboard import (
    GRAM3,
    TestMamariIOverlap3gram076010079IOnlyScoreboard,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    STANDING_LEFTOVER_SITES,
    line_stems_for_site,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    OFF_I_TABLETS,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    is_i_only,
    load_i_sides,
    load_vendored_by_tablet,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

HYPOTHESIS_I_ONLY = True
GRAM4 = STANDING_BACKWARD_4GRAM_072
STANDING_N4 = 4
STANDING_LEFTOVER_SITE = (SIDE_IA, "Ia5", 139)
LEFTOVER_TO_4GRAM_OFFSET = 1
STANDING_I_HITS = 2
STANDING_IA_HITS = 2
STANDING_IB_HITS = 0
STANDING_N_ON_I = 2
STANDING_I_SITES = (
    (SIDE_IA, "Ia5", 138),
    (SIDE_IA, "Ia13", 71),
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
STANDING_CLAIM = "i_4gram_072_076_010_079_is_i_only"
STANDING_I_4GRAM_072_076_010_079_IS_I_ONLY = True
STANDING_RESULT = "i_4gram_072_076_010_079_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_MAJORITY_071 = False


def leftover_4gram_start_site(
    leftover_site: tuple[str, str, int] = STANDING_LEFTOVER_SITE,
) -> tuple[str, str, int]:
    """4-gram starts one stem before leftover 076 010 079."""
    side, line, index = leftover_site
    return (side, line, index - LEFTOVER_TO_4GRAM_OFFSET)


def i_4gram_072_076_010_079_is_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 2 and off-I hits == 0."""
    return is_i_only(i_hits, off_i_hits)


class TestI4gram072IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-144 leftover minority tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("072", "076", "010", "079"))
        self.assertEqual(GRAM4, STANDING_BACKWARD_4GRAM_072)
        adjacent = [list(GRAM4), list(GRAM4)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4), 2)
        overlap = [["072", "076", "010", "079", "072", "076", "010", "079"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4), 2)
        gapped = [list(GRAM4[:2]) + ["006"] + list(GRAM4[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_2_and_zero_off_i(self):
        """Boolean is True only when I ≥ 2 and off-I is 0."""
        provider = MockProvider()
        self.assertTrue(i_4gram_072_076_010_079_is_i_only(2, 0))
        self.assertTrue(i_4gram_072_076_010_079_is_i_only(3, 0))
        self.assertFalse(i_4gram_072_076_010_079_is_i_only(2, 1))
        self.assertFalse(i_4gram_072_076_010_079_is_i_only(1, 0))
        self.assertFalse(i_4gram_072_076_010_079_is_i_only(0, 0))
        self.assertFalse(i_4gram_072_076_010_079_is_i_only(0, 2))
        self.assertEqual(STANDING_CLAIM, "i_4gram_072_076_010_079_is_i_only")
        self.assertTrue(STANDING_I_4GRAM_072_076_010_079_IS_I_ONLY)
        self.assertEqual(
            STANDING_I_4GRAM_072_076_010_079_IS_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_minority_4gram_is_cycle144_leftover_not_the_cycle_103_5gram(self):
        """4-gram is the cycle-144 minority leftover, not 999 071 076 010 079."""
        provider = MockProvider()
        self.assertEqual(GRAM4, STANDING_BACKWARD_4GRAM_072)
        self.assertNotEqual(GRAM4, STANDING_BACKWARD_4GRAM_071)
        self.assertNotEqual(GRAM4, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(GRAM4[1:], GRAM3)
        self.assertTrue(is_contiguous_substring(GRAM3, GRAM4))
        self.assertFalse(is_contiguous_substring(GRAM4, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM4, MAXIMAL_N5_010))
        self.assertEqual(
            leftover_4gram_start_site((SIDE_IA, "Ia5", 139)),
            (SIDE_IA, "Ia5", 138),
        )
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_MAJORITY_071)
        self.assertEqual(len(GRAM4), STANDING_N4)
        self.assertEqual(STANDING_N4, 4)
        self.assertLess(len(GRAM4), 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI4gram072076010079IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover minority 4-gram off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_site = STANDING_LEFTOVER_SITE
        self.i_sites = nge4_sites(GRAM4, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM4)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM4, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM4, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.claim_holds = i_4gram_072_076_010_079_is_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_and_site_are_cycle_144_minority_not_retuned(self):
        """4-gram and leftover Ia5[139] stay the cycle-144 minority lock."""
        self.assertEqual(GRAM4, STANDING_BACKWARD_4GRAM_072)
        self.assertEqual(GRAM4, ("072", "076", "010", "079"))
        self.assertEqual(GRAM3, ("076", "010", "079"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertEqual(self.leftover_site, STANDING_LEFTOVER_SITE)
        self.assertEqual(STANDING_LEFTOVER_SITE, (SIDE_IA, "Ia5", 139))
        self.assertEqual(STANDING_LEFTOVER_SITES[0], STANDING_LEFTOVER_SITE)
        prior_144 = self.survey["i_leftover_076_010_079_backward_4gram"]
        self.assertEqual(prior_144["cycle"], 144)
        self.assertEqual(tuple(prior_144["distinct_backward_4grams"][0]), GRAM4)
        self.assertEqual(
            tuple(tuple(row) for row in prior_144["sites_per_backward_4gram"][0]["sites"]),
            (STANDING_LEFTOVER_SITE,),
        )
        self.assertEqual(prior_144["N_distinct_backward_4grams"], 2)
        self.assertFalse(prior_144["i_leftover_076_010_079_share_one_backward_4gram"])
        prior_147 = self.survey["i_leftover_backward_5grams_i_only"]
        self.assertEqual(prior_147["cycle"], 147)
        self.assertTrue(prior_147["i_leftover_backward_5grams_both_i_only"])
        prior_145 = self.survey["i_4gram_071_076_010_079_inside_cycle103"]
        self.assertEqual(prior_145["cycle"], 145)
        self.assertEqual(tuple(prior_145["tokens4"]), STANDING_BACKWARD_4GRAM_071)
        self.assertNotEqual(tuple(prior_145["tokens4"]), GRAM4)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_two_on_ia_including_leftover_start(self):
        """4-gram is 2 on Ia at Ia5[138]/Ia13[71]; Ib unpublished 0."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 2)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, 2)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM4, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM4), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(
            leftover_4gram_start_site(STANDING_LEFTOVER_SITE),
            STANDING_I_SITES[0],
        )
        leftover_stems = line_stems_for_site(self.i_sides, STANDING_LEFTOVER_SITE)
        leftover_index = STANDING_LEFTOVER_SITE[2]
        self.assertEqual(
            tuple(leftover_stems[leftover_index : leftover_index + 3]),
            GRAM3,
        )
        self.assertEqual(
            tuple(leftover_stems[leftover_index - 1 : leftover_index + 3]),
            GRAM4,
        )
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N4]
            self.assertEqual(tuple(stems), GRAM4)
            self.assertEqual(side, SIDE_IA)
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_4gram_is_zero_off_i_and_i_only(self):
        """4-gram is 0 on A–H and J–V. Ia has exactly 2. W is not a tablet."""
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
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM4))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 2)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(
            i_4gram_072_076_010_079_is_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_4GRAM_072_076_010_079_IS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_4GRAM_072_076_010_079_IS_I_ONLY,
        )
        self.assertTrue(STANDING_I_4GRAM_072_076_010_079_IS_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_4gram_072_076_010_079_is_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM4, GRAM5)
        self.assertNotEqual(GRAM4, STANDING_BACKWARD_4GRAM_071)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_MAJORITY_071)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_147_144_141_103_and_w_scoreboards_still_compute(self):
        """Cycle 147 I-only, 144 backward-4, 141 I-only, 103, W stay."""
        prior_147 = TestMamariILeftoverBackward5gramsIOnlyScoreboard()
        prior_147.setUp()
        prior_147.test_each_5gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_147.test_survey_matches_computed_lock()
        prior_144 = TestMamariILeftover076010079Backward4gramScoreboard()
        prior_144.setUp()
        prior_144.test_three_leftovers_have_two_distinct_backwards_and_claim_loses()
        prior_144.test_survey_matches_computed_lock()
        prior_141 = TestMamariIOverlap3gram076010079IOnlyScoreboard()
        prior_141.setUp()
        prior_141.test_i_hits_are_eight_on_ia()
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
        """CORPUS_SURVEY.json records the cycle-148 minority 4-gram I-only lock."""
        lock = self.survey["i_4gram_072_076_010_079_i_only"]
        self.assertEqual(lock["cycle"], 148)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["leftover_site"]), STANDING_LEFTOVER_SITE)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
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
        self.assertTrue(lock["i_4gram_072_076_010_079_is_i_only"])
        self.assertEqual(
            lock["i_4gram_072_076_010_079_is_i_only"],
            STANDING_I_4GRAM_072_076_010_079_IS_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_majority_071"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_backward_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_071_076_010_079_backward_5gram_unchanged"])
        self.assertTrue(lock["standing_i_4gram_071_076_010_079_inside_cycle103_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_backward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_forward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_inside_two_5grams_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_independent_n5_cycle103_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_independent_n5_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_exception_n4_071_065_071_999_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
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
        self.assertEqual(self.survey["i_leftover_backward_5grams_i_only"]["cycle"], 147)
        self.assertTrue(
            self.survey["i_leftover_backward_5grams_i_only"][
                "i_leftover_backward_5grams_both_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_071_076_010_079_backward_5gram"]["cycle"],
            146,
        )
        self.assertEqual(
            self.survey["i_4gram_071_076_010_079_inside_cycle103"]["cycle"],
            145,
        )
        self.assertFalse(
            self.survey["i_4gram_071_076_010_079_inside_cycle103"][
                "i_4gram_071_076_010_079_all_inside_cycle103_5gram"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_010_079_backward_4gram"]["cycle"], 144)
        self.assertFalse(
            self.survey["i_leftover_076_010_079_backward_4gram"][
                "i_leftover_076_010_079_share_one_backward_4gram"
            ]
        )
        self.assertEqual(
            tuple(
                self.survey["i_leftover_076_010_079_backward_4gram"][
                    "distinct_backward_4grams"
                ][0]
            ),
            GRAM4,
        )
        self.assertEqual(self.survey["i_leftover_076_010_079_forward_4gram"]["cycle"], 143)
        self.assertEqual(self.survey["i_overlap_3gram_inside_two_5grams"]["cycle"], 142)
        self.assertFalse(
            self.survey["i_overlap_3gram_inside_two_5grams"][
                "i_overlap_3gram_076_010_079_all_inside_two_5grams"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["cycle"], 141)
        self.assertTrue(
            self.survey["i_overlap_3gram_076_010_079_i_only"][
                "i_overlap_3gram_076_010_079_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["N_on_I"], 8)
        self.assertEqual(self.survey["i_independent_n5_cycle103_n3_overlap"]["cycle"], 140)
        self.assertFalse(
            self.survey["i_independent_n5_cycle103_n3_overlap"][
                "i_independent_n5_share_no_n3plus_with_cycle103_5gram"
            ]
        )
        self.assertEqual(self.survey["i_independent_n5_maximals_076"]["cycle"], 139)
        self.assertTrue(
            self.survey["i_independent_n5_maximals_076"][
                "i_independent_n5_maximals_all_contain_076"
            ]
        )
        self.assertEqual(self.survey["i_exception_n4_071_065_071_999_i_only"]["cycle"], 138)
        self.assertTrue(
            self.survey["i_exception_n4_071_065_071_999_i_only"][
                "i_exception_n4_071_065_071_999_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_maximals_076"]["cycle"], 137)
        self.assertFalse(
            self.survey["i_leftover_n4_maximals_076"]["i_leftover_n4_maximals_all_contain_076"]
        )
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["maximal_count"], 31)
        self.assertFalse(
            self.survey["i_independent_nge4_maximals"]["i_independent_nge4_has_exactly_4_maximals"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertFalse(
            self.survey["i_repeating_nge4"]["i_repeating_nge4_all_substrings_of_i_5gram"]
        )
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


class TestMamariI4gram072076010079IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 148 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
