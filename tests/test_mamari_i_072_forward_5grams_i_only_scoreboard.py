"""I's cycle-149 leftover forward 5-grams off-I lock.

Cycle 150 text-search lock. Uses already-vendored A–V and the
cycle-149 leftover forward 5-grams of I-only 4-gram
072 076 010 079 (072 076 010 079 090 at Ia5[138],
072 076 010 079 006 at Ia13[71]). Does not retune those
5-grams or those I sites. Does not vendor a new tablet. Does
not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Locks exact consecutive hits of each leftover forward 5-gram
on tablet I and on every other vendored tablet A–H and J–V.
Hypothesis: both are I-only (0 exact matches on A–H and J–V).
Measured: 072 076 010 079 090 N_on_I=1 at Ia5[138];
072 076 010 079 006 N_on_I=1 at Ia13[71]; both N_off_I=0.
Claim that can lose: i_072_forward_5grams_both_i_only. True
only if both have N_off_I=0. The claim is true. Do not retune.

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
from tests.test_mamari_i_4gram_072_076_010_079_forward_5gram_scoreboard import (
    STANDING_DISTINCT_FORWARD_5GRAMS,
    STANDING_FORWARD_5GRAM_006,
    STANDING_FORWARD_5GRAM_090,
    STANDING_INDEPENDENT_N5_SITE,
    STANDING_N_DISTINCT_FORWARD_5GRAMS,
    TestMamariI4gram072076010079Forward5gramScoreboard,
    i_site_forward_5grams,
)
from tests.test_mamari_i_4gram_072_076_010_079_i_only_scoreboard import (
    GRAM4,
    STANDING_I_SITES,
    STANDING_N_ON_I,
    TestMamariI4gram072076010079IOnlyScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
)
from tests.test_mamari_i_leftover_076_010_079_forward_4gram_scoreboard import (
    STANDING_FORWARD_4GRAM_090,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_010_079_i_only_scoreboard import (
    GRAM3,
    TestMamariIOverlap3gram076010079IOnlyScoreboard,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    line_stems_for_site,
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
    load_i_sides,
    load_vendored_by_tablet,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

HYPOTHESIS_BOTH_I_ONLY = True
STANDING_N5 = 5
GRAM5_090 = STANDING_FORWARD_5GRAM_090
GRAM5_006 = STANDING_FORWARD_5GRAM_006
STANDING_SEQUENCES = (GRAM5_090, GRAM5_006)
STANDING_N_ON_I_090 = 1
STANDING_N_ON_I_006 = 1
STANDING_I_SITES_090 = ((SIDE_IA, "Ia5", 138),)
STANDING_I_SITES_006 = ((SIDE_IA, "Ia13", 71),)
STANDING_CYCLE149_SITES = STANDING_I_SITES
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_090 = 0
STANDING_N_OFF_I_006 = 0
STANDING_OFF_I_SITES_090 = ()
STANDING_OFF_I_SITES_006 = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_090 = tuple(
    STANDING_N_ON_I_090 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET_006 = tuple(
    STANDING_N_ON_I_006 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_072_forward_5grams_both_i_only"
STANDING_I_072_FORWARD_5GRAMS_BOTH_I_ONLY = True
STANDING_RESULT = "i_072_forward_5grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_INDEPENDENT_N5 = False


def i_072_forward_5grams_both_i_only(
    n_off_i_090: int,
    n_off_i_006: int,
) -> bool:
    """True iff both leftover forward 5-grams have N_off_I=0."""
    return n_off_i_090 == 0 and n_off_i_006 == 0


class TestI072Forward5gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-149 leftover forward 5-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 5-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM5_090, ("072", "076", "010", "079", "090"))
        self.assertEqual(GRAM5_006, ("072", "076", "010", "079", "006"))
        self.assertEqual(GRAM5_090[:4], GRAM4)
        self.assertEqual(GRAM5_006[:4], GRAM4)
        adjacent = [list(GRAM5_090), list(GRAM5_006)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM5_090), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM5_006), 1)
        overlap = [["072", "076", "010", "079", "090", "072", "076", "010", "079", "090"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM5_090), 2)
        gapped = [list(GRAM5_090[:2]) + ["006"] + list(GRAM5_090[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM5_090), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM5_090), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM5_006), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_both_i_only_requires_zero_off_i_for_each_5gram(self):
        """Boolean is True only when both leftover 5-grams have N_off_I=0."""
        provider = MockProvider()
        self.assertTrue(i_072_forward_5grams_both_i_only(0, 0))
        self.assertFalse(i_072_forward_5grams_both_i_only(1, 0))
        self.assertFalse(i_072_forward_5grams_both_i_only(0, 1))
        self.assertFalse(i_072_forward_5grams_both_i_only(1, 1))
        self.assertFalse(i_072_forward_5grams_both_i_only(2, 0))
        self.assertEqual(STANDING_CLAIM, "i_072_forward_5grams_both_i_only")
        self.assertTrue(STANDING_I_072_FORWARD_5GRAMS_BOTH_I_ONLY)
        self.assertEqual(
            STANDING_I_072_FORWARD_5GRAMS_BOTH_I_ONLY,
            HYPOTHESIS_BOTH_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_5grams_are_cycle_149_leftovers_not_the_cycle_103_5gram(self):
        """5-grams stay the cycle-149 pair; neither is 999 071 076 010 079."""
        provider = MockProvider()
        self.assertEqual(GRAM5_090, STANDING_FORWARD_5GRAM_090)
        self.assertEqual(GRAM5_006, STANDING_FORWARD_5GRAM_006)
        self.assertEqual(STANDING_SEQUENCES, STANDING_DISTINCT_FORWARD_5GRAMS)
        self.assertNotEqual(GRAM5_090, GRAM5)
        self.assertNotEqual(GRAM5_006, GRAM5)
        self.assertNotEqual(GRAM5_090, MAXIMAL_N5_010)
        self.assertNotEqual(GRAM5_006, MAXIMAL_N5_010)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertEqual(GRAM5_090[1:4], GRAM3)
        self.assertEqual(GRAM5_006[1:], MAXIMAL_N5_010[:4])
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5)
        self.assertEqual(len(GRAM5_090), STANDING_N5)
        self.assertEqual(len(GRAM5_006), STANDING_N5)
        self.assertLess(STANDING_N5, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI072Forward5gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover forward-5 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle149_sites = STANDING_CYCLE149_SITES
        self.forwards = i_site_forward_5grams(self.i_sides, self.cycle149_sites)
        self.by_tablet = load_vendored_by_tablet()
        self.i_sites_090 = nge4_sites(GRAM5_090, self.i_sides)
        self.i_sites_006 = nge4_sites(GRAM5_006, self.i_sides)
        self.n_on_i_090 = ngram_hit_count(self.i_sides[SIDE_IA], GRAM5_090) + STANDING_IB_HITS
        self.n_on_i_006 = ngram_hit_count(self.i_sides[SIDE_IA], GRAM5_006) + STANDING_IB_HITS
        self.hits_by_tablet_090 = tablet_hit_counts(
            self.by_tablet, GRAM5_090, VENDORED_TABLETS
        )
        self.hits_by_tablet_006 = tablet_hit_counts(
            self.by_tablet, GRAM5_006, VENDORED_TABLETS
        )
        self.off_i_090 = tablet_hit_counts(self.by_tablet, GRAM5_090, OFF_I_TABLETS)
        self.off_i_006 = tablet_hit_counts(self.by_tablet, GRAM5_006, OFF_I_TABLETS)
        self.n_off_i_090 = sum(self.off_i_090)
        self.n_off_i_006 = sum(self.off_i_006)
        self.claim_holds = i_072_forward_5grams_both_i_only(
            self.n_off_i_090,
            self.n_off_i_006,
        )

    def test_tokens_and_sites_are_cycle_149_lock_not_retuned(self):
        """5-grams and I sites stay the cycle-149 lock."""
        self.assertEqual(GRAM4, ("072", "076", "010", "079"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(GRAM5_090, ("072", "076", "010", "079", "090"))
        self.assertEqual(GRAM5_006, ("072", "076", "010", "079", "006"))
        self.assertEqual(self.cycle149_sites, STANDING_I_SITES)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia5", 138),
                (SIDE_IA, "Ia13", 71),
            ),
        )
        self.assertEqual(STANDING_N_ON_I, 2)
        self.assertEqual(self.forwards, (GRAM5_090, GRAM5_006))
        prior_149 = self.survey["i_4gram_072_076_010_079_forward_5gram"]
        self.assertEqual(prior_149["cycle"], 149)
        self.assertEqual(prior_149["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(prior_149["N_distinct_forward_5grams"], 2)
        self.assertEqual(STANDING_N_DISTINCT_FORWARD_5GRAMS, 2)
        self.assertEqual(
            tuple(tuple(row) for row in prior_149["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_149["distinct_forward_5grams"]),
            STANDING_SEQUENCES,
        )
        self.assertFalse(prior_149["i_4gram_072_076_010_079_share_one_forward_5gram"])
        prior_148 = self.survey["i_4gram_072_076_010_079_i_only"]
        self.assertEqual(prior_148["cycle"], 148)
        self.assertEqual(prior_148["N_on_I"], 2)
        self.assertEqual(prior_148["N_off_I"], 0)
        self.assertTrue(prior_148["i_4gram_072_076_010_079_is_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_5gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_on_I=1/1, N_off_I=0/0. Both I-only. Claim holds."""
        self.assertEqual(self.i_sites_090, STANDING_I_SITES_090)
        self.assertEqual(self.i_sites_006, STANDING_I_SITES_006)
        self.assertEqual(self.n_on_i_090, STANDING_N_ON_I_090)
        self.assertEqual(STANDING_N_ON_I_090, 1)
        self.assertEqual(self.n_on_i_006, STANDING_N_ON_I_006)
        self.assertEqual(STANDING_N_ON_I_006, 1)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(STANDING_I_SITES_090[0], STANDING_I_SITES[0])
        self.assertEqual(STANDING_I_SITES_006[0], STANDING_I_SITES[1])
        for site, want_gram in (
            (STANDING_I_SITES_090[0], GRAM5_090),
            (STANDING_I_SITES_006[0], GRAM5_006),
        ):
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(tuple(stems[site[2] : site[2] + 4]), GRAM4)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N5]), want_gram)
            self.assertNotEqual(want_gram, GRAM5)
            self.assertNotEqual(want_gram, MAXIMAL_N5_010)
        ia13_stems = line_stems_for_site(self.i_sides, STANDING_I_SITES_006[0])
        ia13_index = STANDING_I_SITES_006[0][2]
        self.assertEqual(STANDING_I_SITES_006[0][2] + 1, STANDING_INDEPENDENT_N5_SITE[2])
        self.assertEqual(
            tuple(ia13_stems[ia13_index + 1 : ia13_index + 6]),
            MAXIMAL_N5_010,
        )
        ia5_stems = line_stems_for_site(self.i_sides, STANDING_I_SITES_090[0])
        ia5_index = STANDING_I_SITES_090[0][2]
        self.assertEqual(
            tuple(ia5_stems[ia5_index + 1 : ia5_index + 5]),
            STANDING_FORWARD_4GRAM_090,
        )
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet_090, STANDING_HITS_BY_TABLET_090)
        self.assertEqual(self.hits_by_tablet_006, STANDING_HITS_BY_TABLET_006)
        self.assertEqual(self.off_i_090, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_006, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.n_off_i_090, STANDING_N_OFF_I_090)
        self.assertEqual(self.n_off_i_006, STANDING_N_OFF_I_006)
        self.assertEqual(STANDING_N_OFF_I_090, 0)
        self.assertEqual(STANDING_N_OFF_I_006, 0)
        self.assertEqual(STANDING_OFF_I_SITES_090, ())
        self.assertEqual(STANDING_OFF_I_SITES_006, ())
        for tablet, count_090, count_006 in zip(
            VENDORED_TABLETS,
            self.hits_by_tablet_090,
            self.hits_by_tablet_006,
            strict=True,
        ):
            self.assertEqual(count_090, ngram_hit_count(self.by_tablet[tablet], GRAM5_090))
            self.assertEqual(count_006, ngram_hit_count(self.by_tablet[tablet], GRAM5_006))
            if tablet == "I":
                self.assertEqual(count_090, 1)
                self.assertEqual(count_006, 1)
            else:
                self.assertEqual(count_090, 0)
                self.assertEqual(count_006, 0)
        self.assertEqual(
            i_072_forward_5grams_both_i_only(self.n_off_i_090, self.n_off_i_006),
            STANDING_I_072_FORWARD_5GRAMS_BOTH_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_072_FORWARD_5GRAMS_BOTH_I_ONLY,
        )
        self.assertTrue(STANDING_I_072_FORWARD_5GRAMS_BOTH_I_ONLY)
        self.assertTrue(HYPOTHESIS_BOTH_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_072_forward_5grams_both_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_149_148_147_141_103_and_w_scoreboards_still_compute(self):
        """Cycle 149 forward-5, 148 I-only, 147 I-only, 141, 103, W stay."""
        prior_149 = TestMamariI4gram072076010079Forward5gramScoreboard()
        prior_149.setUp()
        prior_149.test_two_i_sites_have_two_distinct_forwards_and_claim_loses()
        prior_149.test_survey_matches_computed_lock()
        prior_148 = TestMamariI4gram072076010079IOnlyScoreboard()
        prior_148.setUp()
        prior_148.test_i_hits_are_two_on_ia_including_leftover_start()
        prior_148.test_4gram_is_zero_off_i_and_i_only()
        prior_148.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-150 leftover 5-gram I-only lock."""
        lock = self.survey["i_072_forward_5grams_i_only"]
        self.assertEqual(lock["cycle"], 150)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_both_i_only"])
        self.assertEqual(lock["hypothesis_both_i_only"], HYPOTHESIS_BOTH_I_ONLY)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["N_on_I_4gram"], STANDING_N_ON_I)
        self.assertEqual(lock["N_on_I_4gram"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle149_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_distinct_forward_5grams"], 2)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 2)
        row_090, row_006 = rows
        self.assertEqual(tuple(row_090["tokens5"]), GRAM5_090)
        self.assertEqual(tuple(row_006["tokens5"]), GRAM5_006)
        self.assertEqual(tuple(row_090["cycle149_site"]), STANDING_I_SITES[0])
        self.assertEqual(tuple(row_006["cycle149_site"]), STANDING_I_SITES[1])
        self.assertEqual(row_090["N_on_I"], STANDING_N_ON_I_090)
        self.assertEqual(row_006["N_on_I"], STANDING_N_ON_I_006)
        self.assertEqual(row_090["N_on_I"], 1)
        self.assertEqual(row_006["N_on_I"], 1)
        self.assertEqual(row_090["ia_hits"], 1)
        self.assertEqual(row_006["ia_hits"], 1)
        self.assertEqual(row_090["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(row_006["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(site) for site in row_090["i_sites"]),
            STANDING_I_SITES_090,
        )
        self.assertEqual(
            tuple(tuple(site) for site in row_006["i_sites"]),
            STANDING_I_SITES_006,
        )
        self.assertEqual(tuple(tuple(site) for site in row_090["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(tuple(tuple(site) for site in row_006["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(row_090["N_off_I"], STANDING_N_OFF_I_090)
        self.assertEqual(row_006["N_off_I"], STANDING_N_OFF_I_006)
        self.assertEqual(row_090["N_off_I"], 0)
        self.assertEqual(row_006["N_off_I"], 0)
        self.assertEqual(row_090["off_i_sites"], [])
        self.assertEqual(row_006["off_i_sites"], [])
        self.assertEqual(tuple(row_090["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(row_006["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(row_090["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(row_006["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(row_090["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(row_006["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(row_090["hits_by_tablet"]), STANDING_HITS_BY_TABLET_090)
        self.assertEqual(tuple(row_006["hits_by_tablet"]), STANDING_HITS_BY_TABLET_006)
        self.assertTrue(row_090["i_only"])
        self.assertTrue(row_006["i_only"])
        self.assertEqual(
            tuple(lock["independent_n5_site_after_ia13"]),
            STANDING_INDEPENDENT_N5_SITE,
        )
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_072_forward_5grams_both_i_only"])
        self.assertEqual(
            lock["i_072_forward_5grams_both_i_only"],
            STANDING_I_072_FORWARD_5GRAMS_BOTH_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_independent_n5"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_4gram_072_076_010_079_forward_5gram_unchanged"])
        self.assertTrue(lock["standing_i_4gram_072_076_010_079_i_only_unchanged"])
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
        self.assertEqual(
            self.survey["i_4gram_072_076_010_079_forward_5gram"]["cycle"],
            149,
        )
        self.assertFalse(
            self.survey["i_4gram_072_076_010_079_forward_5gram"][
                "i_4gram_072_076_010_079_share_one_forward_5gram"
            ]
        )
        self.assertEqual(
            self.survey["i_4gram_072_076_010_079_forward_5gram"][
                "N_distinct_forward_5grams"
            ],
            2,
        )
        self.assertEqual(self.survey["i_4gram_072_076_010_079_i_only"]["cycle"], 148)
        self.assertTrue(
            self.survey["i_4gram_072_076_010_079_i_only"][
                "i_4gram_072_076_010_079_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_4gram_072_076_010_079_i_only"]["N_on_I"], 2)
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
        self.assertEqual(self.survey["i_leftover_076_010_079_forward_4gram"]["cycle"], 143)
        self.assertFalse(
            self.survey["i_leftover_076_010_079_forward_4gram"][
                "i_leftover_076_010_079_share_one_forward_4gram"
            ]
        )
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


class TestMamariI072Forward5gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 150 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
