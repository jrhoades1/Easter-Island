"""I's cycle-157 leftover prefix 4-grams off-I lock.

Cycle 158 text-search lock. Uses already-vendored A–V and the
cycle-157 leftover prefix 4-grams of independent 5-gram
400 070 076 020 010 (023 400 070 076 at Ia13[84],
077 400 070 076 at Ia14[125]). Does not retune those
4-grams, the independent 5-gram, or those I sites. Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

This closes the previous-stem leftover of the last of the
four independent I n=5 maximals (cycles 136/139). Nearby
leftover n=4 maximal 053 076 020 010 at Ia12[0]/Ia14[109]
is context only; do not retune.

Locks exact consecutive hits of each leftover prefix 4-gram
on tablet I and on every other vendored tablet A–H and J–V.
Hypothesis: both are I-only (N_on_I>=1 and N_off_I=0).
Measured: 023 400 070 076 N_on_I=1 at Ia13[84];
077 400 070 076 N_on_I=1 at Ia14[125]; both N_off_I=0.
Claim that can lose: i_leftover_023_077_400_070_076_both_i_only.
True only if both have N_on_I>=1 and N_off_I=0. The claim
is true. Do not retune.

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
from tests.test_mamari_i_independent_400_070_076_020_010_previous_stem_scoreboard import (
    LEFTOVER_N4_053,
    STANDING_I_SITES as STANDING_CYCLE157_SITES,
    STANDING_PER_SITE_PREVIOUS,
    STEM_023,
    STEM_077,
    TestMamariIIndependent400070076020010PreviousStemScoreboard,
)
from tests.test_mamari_i_independent_n5_076_scoreboard import (
    TestMamariIIndependentN5076Scoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
    MAXIMAL_N5_011,
    MAXIMAL_N5_400,
    MAXIMAL_N5_430,
)
from tests.test_mamari_i_leftover_090_700_430_076_006_i_only_scoreboard import (
    leftover_prefix_4gram_start_site,
)
from tests.test_mamari_i_leftover_633_006_076_011_090_i_only_scoreboard import (
    GRAM4_006 as CYCLE156_GRAM4_006,
    GRAM4_633 as CYCLE156_GRAM4_633,
    TestMamariILeftover633006076011090IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    STANDING_LEFTOVER,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
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
    load_i_sides,
    load_vendored_by_tablet,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

HYPOTHESIS_BOTH_I_ONLY = True
STANDING_N4 = 4
GRAM5_INDEPENDENT = MAXIMAL_N5_400
GRAM4_023 = (STEM_023, "400", "070", "076")
GRAM4_077 = (STEM_077, "400", "070", "076")
STANDING_SEQUENCES = (GRAM4_023, GRAM4_077)
STANDING_N_ON_I_023 = 1
STANDING_N_ON_I_077 = 1
STANDING_I_SITES_023 = ((SIDE_IA, "Ia13", 84),)
STANDING_I_SITES_077 = ((SIDE_IA, "Ia14", 125),)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_023 = 0
STANDING_N_OFF_I_077 = 0
STANDING_OFF_I_SITES_023 = ()
STANDING_OFF_I_SITES_077 = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_023 = tuple(
    STANDING_N_ON_I_023 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET_077 = tuple(
    STANDING_N_ON_I_077 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_023_077_400_070_076_both_i_only"
STANDING_I_LEFTOVER_023_077_400_070_076_BOTH_I_ONLY = True
STANDING_RESULT = "i_leftover_023_077_400_070_076_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE154_LEFTOVER_4GRAMS = False
STANDING_SAME_AS_CYCLE156_LEFTOVER_4GRAMS = False
STANDING_SAME_AS_INDEPENDENT_N5_430 = False
STANDING_SAME_AS_INDEPENDENT_N5_011 = False
STANDING_SAME_AS_INDEPENDENT_N5_010 = False
STANDING_LEFTOVER_N4_053_SITES = (("Ia", "Ia12", 0), ("Ia", "Ia14", 109))


def sequence_is_i_only(n_on_i: int, n_off_i: int) -> bool:
    """True iff N_on_I>=1 and N_off_I=0."""
    return n_on_i >= 1 and n_off_i == 0


def i_leftover_023_077_400_070_076_both_i_only(
    n_on_i_023: int,
    n_off_i_023: int,
    n_on_i_077: int,
    n_off_i_077: int,
) -> bool:
    """True iff both leftover prefix 4-grams are I-only."""
    return sequence_is_i_only(n_on_i_023, n_off_i_023) and sequence_is_i_only(
        n_on_i_077, n_off_i_077
    )


class TestILeftover023077400070076IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-157 leftover prefix 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4_023, ("023", "400", "070", "076"))
        self.assertEqual(GRAM4_077, ("077", "400", "070", "076"))
        self.assertEqual(GRAM4_023[1:], GRAM5_INDEPENDENT[:3])
        self.assertEqual(GRAM4_077[1:], GRAM5_INDEPENDENT[:3])
        adjacent = [list(GRAM4_023), list(GRAM4_077)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_023), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_077), 1)
        overlap = [["023", "400", "070", "076", "023", "400", "070", "076"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_023), 2)
        gapped = [list(GRAM4_023[:2]) + ["000"] + list(GRAM4_023[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_023), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_023), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_077), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_both_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when both leftover 4-grams are I-only."""
        provider = MockProvider()
        self.assertTrue(i_leftover_023_077_400_070_076_both_i_only(1, 0, 1, 0))
        self.assertTrue(i_leftover_023_077_400_070_076_both_i_only(2, 0, 1, 0))
        self.assertFalse(i_leftover_023_077_400_070_076_both_i_only(1, 1, 1, 0))
        self.assertFalse(i_leftover_023_077_400_070_076_both_i_only(1, 0, 1, 1))
        self.assertFalse(i_leftover_023_077_400_070_076_both_i_only(0, 0, 1, 0))
        self.assertFalse(i_leftover_023_077_400_070_076_both_i_only(1, 0, 0, 0))
        self.assertFalse(i_leftover_023_077_400_070_076_both_i_only(0, 0, 0, 0))
        self.assertFalse(i_leftover_023_077_400_070_076_both_i_only(1, 1, 1, 1))
        self.assertEqual(STANDING_CLAIM, "i_leftover_023_077_400_070_076_both_i_only")
        self.assertTrue(STANDING_I_LEFTOVER_023_077_400_070_076_BOTH_I_ONLY)
        self.assertEqual(
            STANDING_I_LEFTOVER_023_077_400_070_076_BOTH_I_ONLY,
            HYPOTHESIS_BOTH_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_157_leftovers_not_retuned(self):
        """4-grams stay the cycle-157 pair; neither is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM4_023, (STEM_023, "400", "070", "076"))
        self.assertEqual(GRAM4_077, (STEM_077, "400", "070", "076"))
        self.assertEqual(STANDING_SEQUENCES, (GRAM4_023, GRAM4_077))
        self.assertNotEqual(GRAM4_023, GRAM5)
        self.assertNotEqual(GRAM4_077, GRAM5)
        self.assertNotEqual(GRAM4_023, GRAM5_INDEPENDENT)
        self.assertNotEqual(GRAM4_077, GRAM5_INDEPENDENT)
        self.assertNotEqual(GRAM4_023, CYCLE156_GRAM4_633)
        self.assertNotEqual(GRAM4_077, CYCLE156_GRAM4_006)
        self.assertNotEqual(GRAM4_023, MAXIMAL_N5_430)
        self.assertNotEqual(GRAM4_077, MAXIMAL_N5_011)
        self.assertNotEqual(GRAM4_023, MAXIMAL_N5_010)
        self.assertNotEqual(GRAM4_077, LEFTOVER_N4_053)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(GRAM5_INDEPENDENT, ("400", "070", "076", "020", "010"))
        self.assertEqual(CYCLE156_GRAM4_633, ("633", "076", "011", "090"))
        self.assertEqual(CYCLE156_GRAM4_006, ("006", "076", "011", "090"))
        self.assertEqual(MAXIMAL_N5_430, ("430", "076", "006", "000", "076"))
        self.assertEqual(MAXIMAL_N5_011, ("076", "011", "090", "090", "076"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertEqual(LEFTOVER_N4_053, ("053", "076", "020", "010"))
        leftover_053 = [
            row for row in STANDING_LEFTOVER if row[0] == LEFTOVER_N4_053
        ]
        self.assertEqual(len(leftover_053), 1)
        self.assertEqual(
            leftover_053[0],
            (LEFTOVER_N4_053, 4, 2, STANDING_LEFTOVER_N4_053_SITES),
        )
        self.assertTrue(is_contiguous_substring(GRAM4_023[1:], GRAM5_INDEPENDENT))
        self.assertTrue(is_contiguous_substring(GRAM4_077[1:], GRAM5_INDEPENDENT))
        self.assertFalse(is_contiguous_substring(GRAM4_023, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM4_077, GRAM5))
        self.assertEqual(
            leftover_prefix_4gram_start_site((SIDE_IA, "Ia13", 85)),
            (SIDE_IA, "Ia13", 84),
        )
        self.assertEqual(
            leftover_prefix_4gram_start_site((SIDE_IA, "Ia14", 126)),
            (SIDE_IA, "Ia14", 125),
        )
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE154_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE156_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5_430)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5_011)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5_010)
        self.assertEqual(len(GRAM4_023), STANDING_N4)
        self.assertEqual(len(GRAM4_077), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover023077400070076IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover prefix-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle157_sites = STANDING_CYCLE157_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.i_sites_023 = nge4_sites(GRAM4_023, self.i_sides)
        self.i_sites_077 = nge4_sites(GRAM4_077, self.i_sides)
        self.n_on_i_023 = ngram_hit_count(self.i_sides[SIDE_IA], GRAM4_023) + STANDING_IB_HITS
        self.n_on_i_077 = ngram_hit_count(self.i_sides[SIDE_IA], GRAM4_077) + STANDING_IB_HITS
        self.hits_by_tablet_023 = tablet_hit_counts(
            self.by_tablet, GRAM4_023, VENDORED_TABLETS
        )
        self.hits_by_tablet_077 = tablet_hit_counts(
            self.by_tablet, GRAM4_077, VENDORED_TABLETS
        )
        self.off_i_023 = tablet_hit_counts(self.by_tablet, GRAM4_023, OFF_I_TABLETS)
        self.off_i_077 = tablet_hit_counts(self.by_tablet, GRAM4_077, OFF_I_TABLETS)
        self.n_off_i_023 = sum(self.off_i_023)
        self.n_off_i_077 = sum(self.off_i_077)
        self.claim_holds = i_leftover_023_077_400_070_076_both_i_only(
            self.n_on_i_023,
            self.n_off_i_023,
            self.n_on_i_077,
            self.n_off_i_077,
        )

    def test_tokens_and_sites_are_cycle_157_lock_not_retuned(self):
        """4-grams and I sites stay the cycle-157 leftover previous stems."""
        self.assertEqual(GRAM5_INDEPENDENT, MAXIMAL_N5_400)
        self.assertEqual(GRAM5_INDEPENDENT, ("400", "070", "076", "020", "010"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(GRAM4_023, ("023", "400", "070", "076"))
        self.assertEqual(GRAM4_077, ("077", "400", "070", "076"))
        self.assertEqual(self.cycle157_sites, STANDING_CYCLE157_SITES)
        self.assertEqual(
            STANDING_CYCLE157_SITES,
            (
                (SIDE_IA, "Ia13", 85),
                (SIDE_IA, "Ia14", 126),
            ),
        )
        self.assertEqual(STANDING_PER_SITE_PREVIOUS, (STEM_023, STEM_077))
        prior_157 = self.survey["i_independent_400_070_076_020_010_previous_stem"]
        self.assertEqual(prior_157["cycle"], 157)
        self.assertEqual(tuple(prior_157["tokens5"]), GRAM5_INDEPENDENT)
        self.assertEqual(prior_157["N_sites"], 2)
        self.assertEqual(prior_157["N_with_previous"], 2)
        self.assertEqual(prior_157["N_distinct_previous_stems"], 2)
        self.assertEqual(tuple(prior_157["per_site_previous_stems"]), (STEM_023, STEM_077))
        self.assertEqual(
            tuple(tuple(row) for row in prior_157["i_sites"]),
            STANDING_CYCLE157_SITES,
        )
        self.assertFalse(
            prior_157["i_independent_400_070_076_020_010_share_one_previous_stem"]
        )
        prior_156 = self.survey["i_leftover_633_006_076_011_090_i_only"]
        self.assertEqual(prior_156["cycle"], 156)
        self.assertTrue(prior_156["i_leftover_633_006_076_011_090_both_i_only"])
        self.assertEqual(tuple(prior_156["sequences"][0]["tokens4"]), CYCLE156_GRAM4_633)
        self.assertEqual(tuple(prior_156["sequences"][1]["tokens4"]), CYCLE156_GRAM4_006)
        prior_154 = self.survey["i_leftover_090_700_430_076_006_i_only"]
        self.assertEqual(prior_154["cycle"], 154)
        self.assertTrue(prior_154["i_leftover_090_700_430_076_006_both_i_only"])
        prior_139 = self.survey["i_independent_n5_maximals_076"]
        self.assertEqual(prior_139["cycle"], 139)
        self.assertTrue(prior_139["i_independent_n5_maximals_all_contain_076"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_on_I=1/1, N_off_I=0/0. Both I-only. Claim holds."""
        self.assertEqual(self.i_sites_023, STANDING_I_SITES_023)
        self.assertEqual(self.i_sites_077, STANDING_I_SITES_077)
        self.assertEqual(self.n_on_i_023, STANDING_N_ON_I_023)
        self.assertEqual(STANDING_N_ON_I_023, 1)
        self.assertEqual(self.n_on_i_077, STANDING_N_ON_I_077)
        self.assertEqual(STANDING_N_ON_I_077, 1)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(
            leftover_prefix_4gram_start_site(STANDING_CYCLE157_SITES[0]),
            STANDING_I_SITES_023[0],
        )
        self.assertEqual(
            leftover_prefix_4gram_start_site(STANDING_CYCLE157_SITES[1]),
            STANDING_I_SITES_077[0],
        )
        for site, want_gram, prev in (
            (STANDING_I_SITES_023[0], GRAM4_023, STEM_023),
            (STANDING_I_SITES_077[0], GRAM4_077, STEM_077),
        ):
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N4]), want_gram)
            self.assertEqual(stems[site[2]], prev)
            self.assertEqual(
                tuple(stems[site[2] + 1 : site[2] + 6]),
                GRAM5_INDEPENDENT,
            )
            self.assertNotEqual(want_gram, GRAM5)
            self.assertNotEqual(want_gram, GRAM5_INDEPENDENT)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet_023, STANDING_HITS_BY_TABLET_023)
        self.assertEqual(self.hits_by_tablet_077, STANDING_HITS_BY_TABLET_077)
        self.assertEqual(self.off_i_023, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_077, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.n_off_i_023, STANDING_N_OFF_I_023)
        self.assertEqual(self.n_off_i_077, STANDING_N_OFF_I_077)
        self.assertEqual(STANDING_N_OFF_I_023, 0)
        self.assertEqual(STANDING_N_OFF_I_077, 0)
        self.assertEqual(STANDING_OFF_I_SITES_023, ())
        self.assertEqual(STANDING_OFF_I_SITES_077, ())
        for tablet, count_023, count_077 in zip(
            VENDORED_TABLETS,
            self.hits_by_tablet_023,
            self.hits_by_tablet_077,
            strict=True,
        ):
            self.assertEqual(count_023, ngram_hit_count(self.by_tablet[tablet], GRAM4_023))
            self.assertEqual(count_077, ngram_hit_count(self.by_tablet[tablet], GRAM4_077))
            if tablet == "I":
                self.assertEqual(count_023, 1)
                self.assertEqual(count_077, 1)
            else:
                self.assertEqual(count_023, 0)
                self.assertEqual(count_077, 0)
        self.assertEqual(
            i_leftover_023_077_400_070_076_both_i_only(
                self.n_on_i_023,
                self.n_off_i_023,
                self.n_on_i_077,
                self.n_off_i_077,
            ),
            STANDING_I_LEFTOVER_023_077_400_070_076_BOTH_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_023_077_400_070_076_BOTH_I_ONLY,
        )
        self.assertTrue(STANDING_I_LEFTOVER_023_077_400_070_076_BOTH_I_ONLY)
        self.assertTrue(HYPOTHESIS_BOTH_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_leftover_023_077_400_070_076_both_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE154_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE156_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5_430)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5_011)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5_010)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_157_156_139_103_and_w_scoreboards_still_compute(self):
        """Cycle 157 previous-stem, 156 I-only, 139 076, 103 I-only, W stay."""
        prior_157 = TestMamariIIndependent400070076020010PreviousStemScoreboard()
        prior_157.setUp()
        prior_157.test_two_distinct_previous_stems_and_claim_loses()
        prior_157.test_survey_matches_computed_lock()
        prior_156 = TestMamariILeftover633006076011090IOnlyScoreboard()
        prior_156.setUp()
        prior_156.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_156.test_survey_matches_computed_lock()
        prior_139 = TestMamariIIndependentN5076Scoreboard()
        prior_139.setUp()
        prior_139.test_counts_4_of_4_and_hypothesis_all_contain_holds()
        prior_139.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-158 leftover 4-gram I-only lock."""
        lock = self.survey["i_leftover_023_077_400_070_076_i_only"]
        self.assertEqual(lock["cycle"], 158)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_both_i_only"])
        self.assertEqual(lock["hypothesis_both_i_only"], HYPOTHESIS_BOTH_I_ONLY)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["tokens5"]), GRAM5_INDEPENDENT)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle157_sites"]),
            STANDING_CYCLE157_SITES,
        )
        self.assertEqual(tuple(lock["per_site_previous_stems"]), STANDING_PER_SITE_PREVIOUS)
        self.assertEqual(lock["N_distinct_previous_stems"], 2)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 2)
        row_023, row_077 = rows
        self.assertEqual(tuple(row_023["tokens4"]), GRAM4_023)
        self.assertEqual(tuple(row_077["tokens4"]), GRAM4_077)
        self.assertEqual(tuple(row_023["cycle157_site"]), STANDING_CYCLE157_SITES[0])
        self.assertEqual(tuple(row_077["cycle157_site"]), STANDING_CYCLE157_SITES[1])
        self.assertEqual(row_023["previous_stem"], STEM_023)
        self.assertEqual(row_077["previous_stem"], STEM_077)
        self.assertEqual(row_023["N_on_I"], STANDING_N_ON_I_023)
        self.assertEqual(row_077["N_on_I"], STANDING_N_ON_I_077)
        self.assertEqual(row_023["N_on_I"], 1)
        self.assertEqual(row_077["N_on_I"], 1)
        self.assertEqual(row_023["ia_hits"], 1)
        self.assertEqual(row_077["ia_hits"], 1)
        self.assertEqual(row_023["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(row_077["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(site) for site in row_023["i_sites"]),
            STANDING_I_SITES_023,
        )
        self.assertEqual(
            tuple(tuple(site) for site in row_077["i_sites"]),
            STANDING_I_SITES_077,
        )
        self.assertEqual(tuple(tuple(site) for site in row_023["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(tuple(tuple(site) for site in row_077["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(row_023["N_off_I"], STANDING_N_OFF_I_023)
        self.assertEqual(row_077["N_off_I"], STANDING_N_OFF_I_077)
        self.assertEqual(row_023["N_off_I"], 0)
        self.assertEqual(row_077["N_off_I"], 0)
        self.assertEqual(row_023["off_i_sites"], [])
        self.assertEqual(row_077["off_i_sites"], [])
        self.assertEqual(tuple(row_023["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(row_077["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(row_023["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(row_077["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(row_023["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(row_077["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(row_023["hits_by_tablet"]), STANDING_HITS_BY_TABLET_023)
        self.assertEqual(tuple(row_077["hits_by_tablet"]), STANDING_HITS_BY_TABLET_077)
        self.assertTrue(row_023["i_only"])
        self.assertTrue(row_077["i_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_023_077_400_070_076_both_i_only"])
        self.assertEqual(
            lock["i_leftover_023_077_400_070_076_both_i_only"],
            STANDING_I_LEFTOVER_023_077_400_070_076_BOTH_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle154_leftover_4grams"])
        self.assertFalse(lock["same_as_cycle156_leftover_4grams"])
        self.assertFalse(lock["same_as_independent_n5_430"])
        self.assertFalse(lock["same_as_independent_n5_011"])
        self.assertFalse(lock["same_as_independent_n5_010"])
        self.assertEqual(tuple(lock["leftover_n4_053_076_020_010"]), LEFTOVER_N4_053)
        self.assertEqual(
            tuple(tuple(site) for site in lock["leftover_n4_053_sites"]),
            STANDING_LEFTOVER_N4_053_SITES,
        )
        self.assertTrue(lock["leftover_n4_053_context_only"])
        self.assertTrue(lock["last_of_four_independent_n5_leftover_closed"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_independent_400_070_076_020_010_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_633_006_076_011_090_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_independent_076_011_090_090_076_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_090_700_430_076_006_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_independent_430_076_006_000_076_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_4gram_630_076_010_079_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_independent_076_010_079_006_700_preceded_072_unchanged"]
        )
        self.assertTrue(lock["standing_i_072_forward_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_072_076_010_079_forward_5gram_unchanged"])
        self.assertTrue(lock["standing_i_4gram_072_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_backward_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_inside_two_5grams_unchanged"])
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
            self.survey["i_independent_400_070_076_020_010_previous_stem"]["cycle"],
            157,
        )
        self.assertFalse(
            self.survey["i_independent_400_070_076_020_010_previous_stem"][
                "i_independent_400_070_076_020_010_share_one_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_633_006_076_011_090_i_only"]["cycle"], 156
        )
        self.assertTrue(
            self.survey["i_leftover_633_006_076_011_090_i_only"][
                "i_leftover_633_006_076_011_090_both_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_independent_076_011_090_090_076_previous_stem"]["cycle"],
            155,
        )
        self.assertFalse(
            self.survey["i_independent_076_011_090_090_076_previous_stem"][
                "i_independent_076_011_090_090_076_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_090_700_430_076_006_i_only"]["cycle"], 154)
        self.assertTrue(
            self.survey["i_leftover_090_700_430_076_006_i_only"][
                "i_leftover_090_700_430_076_006_both_i_only"
            ]
        )
        self.assertEqual(self.survey["i_independent_n5_maximals_076"]["cycle"], 139)
        self.assertTrue(
            self.survey["i_independent_n5_maximals_076"][
                "i_independent_n5_maximals_all_contain_076"
            ]
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
        self.assertTrue(
            self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"]
        )
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(
            self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"]
        )
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(
            self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"],
            5,
        )
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftover023077400070076IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 158 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
