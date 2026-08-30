"""I's cycle-179 leftover 3-gram 076 071 090 off-I lock.

Cycle 180 text-search lock. Uses already-vendored A–V and the
cycle-179 leftover forward 3-gram 076 071 090 (the n=3 run
shared by leftover 076 071 sites Ia1[86] 076 071 090 606,
Ia3[85] 076 071 090 076, and Ia12[19] 076 071 090 047).
Does not retune that 3-gram, those leftover sites, or the
leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished
Ib is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Same claim-shape as cycle 177 (076 071 600 was I-only 4/0),
cycle 174 (076 071 076 was I-only 6/0), cycle 171 (076 071
was I-only 43/0), cycle 167 (999 090 076 was I-only 16/0),
cycle 160 (076 020 010 was I-only 12/0), and cycle 141
(076 010 079 was I-only 8/0). This cycle is the new leftover
3-gram 076 071 090 only. 071 999 (071 065 071 999) does not
count. 076 076 (700 076 076 053) does not. Do not retune
076 071 600, 076 071 076, 076 071, 999 090 076, 076 020 010,
or 076 010 079. Cycle 179 leftover N=3 and leftover n=4 set
stay. Do not assume the I-only result. Include any
inside-family 076 071 site that also has this 3-gram:
leftover n=4 maximal 076 071 090 999 at Ia7[166] and
Ia14[136] (cycle 172 inside-family) count as real I hits
because they are consecutive 076 071 090.

Locks exact consecutive hits of 076 071 090 on tablet I
and on every other vendored tablet A–H and J–V. Claim that
can lose: i_3gram_076_071_090_i_only (I hits ≥ 1 and
off-I hits == 0). True only if N_off_I == 0. Ia is exactly
5 at Ia1[86]/Ia3[85]/Ia7[166]/Ia12[19]/Ia14[136] (three
leftover matching sites plus inside-family Ia7[166] and
Ia14[136] 076 071 090 999); Ib unpublished 0; every other
vendored tablet is exact-0. Not an n≥8 island. Not the
cycle-103 I 5-gram.

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
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_inside_family_scoreboard import (
    LEFTOVER_N4_090999,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_090999_COVERED,
    STANDING_LEFTOVER_SITES,
    TestMamariI2gram076071InsideFamilyScoreboard,
)
from tests.test_mamari_i_076_071_600_forward_4grams_i_only_scoreboard import (
    TestMamariI076071600Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_076_071_076_forward_4grams_i_only_scoreboard import (
    TestMamariI076071076Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_3gram_076_071_076_i_only_scoreboard import (
    GRAM3 as CYCLE174_GRAM3,
    TestMamariI3gram076071076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_076_071_600_i_only_scoreboard import (
    GRAM3 as CYCLE177_GRAM3,
    TestMamariI3gram076071600IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    TestMamariILeftover076071Forward076Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_090_scoreboard import (
    GRAM3_FORWARD,
    STANDING_INSIDE_FORWARD_090_NEXT_4GRAM,
    STANDING_INSIDE_FORWARD_090_SITES,
    STANDING_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE179_MATCHING_SITES,
    STANDING_N_WITH_FORWARD_076_071_090,
    TestMamariILeftover076071Forward090Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_600_scoreboard import (
    TestMamariILeftover076071Forward600Scoreboard,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    GRAM2 as CYCLE170_GRAM2,
    NEAR_MISS_071_065_071_999,
    NEAR_MISS_700_076_076_053,
    TestMamariILeftoverN4076071Scoreboard,
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
GRAM3 = GRAM3_FORWARD
STANDING_N3 = 3
STANDING_I_HITS = 5
STANDING_IA_HITS = 5
STANDING_IB_HITS = 0
STANDING_N_ON_I = 5
STANDING_N_I = 5
STANDING_I_SITES = (
    (SIDE_IA, "Ia1", 86),
    (SIDE_IA, "Ia3", 85),
    (SIDE_IA, "Ia7", 166),
    (SIDE_IA, "Ia12", 19),
    (SIDE_IA, "Ia14", 136),
)
STANDING_LEFTOVER_MATCHING_SITES = CYCLE179_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_COUNT = 3
STANDING_INSIDE_FAMILY_SITES = STANDING_INSIDE_FORWARD_090_SITES
STANDING_INSIDE_FAMILY_COUNT = 2
STANDING_INSIDE_FAMILY_NEXT_4GRAM = STANDING_INSIDE_FORWARD_090_NEXT_4GRAM
STANDING_INSIDE_FAMILY_NEXT_4GRAMS = (
    STANDING_INSIDE_FORWARD_090_NEXT_4GRAM,
    STANDING_INSIDE_FORWARD_090_NEXT_4GRAM,
)
STANDING_INSIDE_FAMILY_SITE_INCLUDED = True
STANDING_I_NEXT_4GRAMS = (
    ("076", "071", "090", "606"),
    ("076", "071", "090", "076"),
    ("076", "071", "090", "999"),
    ("076", "071", "090", "047"),
    ("076", "071", "090", "999"),
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
STANDING_CLAIM = "i_3gram_076_071_090_i_only"
STANDING_I_3GRAM_076_071_090_I_ONLY = True
STANDING_RESULT = "i_3gram_076_071_090_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE141_3GRAM = False
STANDING_SAME_AS_CYCLE160_3GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE171_2GRAM = False
STANDING_SAME_AS_CYCLE174_3GRAM = False
STANDING_SAME_AS_CYCLE177_3GRAM = False
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_SITES_CHECKED = True


def i_3gram_076_071_090_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


class TestI3gram076071090IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-179 leftover 3-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. 071 999 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "071", "090"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["076", "071", "090", "071", "090"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 1)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_071_065_071_999)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["071", "999"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "076"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "071"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "071", "076"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "071", "600"]], GRAM3), 0)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0."""
        provider = MockProvider()
        self.assertTrue(i_3gram_076_071_090_i_only(1, 0))
        self.assertTrue(i_3gram_076_071_090_i_only(5, 0))
        self.assertFalse(i_3gram_076_071_090_i_only(1, 1))
        self.assertFalse(i_3gram_076_071_090_i_only(0, 0))
        self.assertFalse(i_3gram_076_071_090_i_only(0, 5))
        self.assertEqual(STANDING_CLAIM, "i_3gram_076_071_090_i_only")
        self.assertTrue(STANDING_I_3GRAM_076_071_090_I_ONLY)
        self.assertEqual(
            STANDING_I_3GRAM_076_071_090_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_cycle179_leftover_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-179 leftover, not 071 999, 076 076, or the priors."""
        provider = MockProvider()
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM3[:2], CYCLE171_GRAM2)
        self.assertEqual(GRAM3[:2], CYCLE170_GRAM2)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, CYCLE174_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE177_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE160_GRAM3)
        self.assertNotEqual(GRAM3, ("076", "010", "079"))
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE141_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE160_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE174_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE177_3GRAM)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertLess(len(GRAM3), 8)
        for leftover in STANDING_MATCHING_NEXT_4GRAMS:
            self.assertTrue(is_contiguous_substring(GRAM3, leftover))
        self.assertTrue(
            is_contiguous_substring(GRAM3, STANDING_INSIDE_FAMILY_NEXT_4GRAM)
        )
        self.assertEqual(STANDING_INSIDE_FAMILY_NEXT_4GRAM, LEFTOVER_N4_090999)
        self.assertEqual(STANDING_INSIDE_FAMILY_NEXT_4GRAM, ("076", "071", "090", "999"))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_071_065_071_999))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_700_076_076_053))
        self.assertTrue(is_contiguous_substring(("071", "999"), NEAR_MISS_071_065_071_999))
        self.assertTrue(is_contiguous_substring(("076", "076"), NEAR_MISS_700_076_076_053))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram076071090IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 3-gram 076 071 090 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM3, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM3)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM3, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM3, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.claim_holds = i_3gram_076_071_090_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_179_leftover_not_retuned(self):
        """3-gram is the cycle-179 leftover lock, not a new inventory."""
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM3, ("076", "071", "090"))
        prior_179 = self.survey["i_leftover_076_071_forward_090"]
        self.assertEqual(prior_179["cycle"], 179)
        self.assertEqual(tuple(prior_179["forward_3gram"]), GRAM3)
        self.assertEqual(prior_179["N_with_forward_076_071_090"], 3)
        self.assertEqual(prior_179["N_without"], 31)
        self.assertEqual(prior_179["N_leftover"], 34)
        measured_matching = [list(site) for site in CYCLE179_MATCHING_SITES]
        self.assertEqual(
            [list(site) for site in prior_179["matching_leftover_sites"]],
            measured_matching,
        )
        self.assertTrue(prior_179["i_leftover_076_071_exactly_3_forward_076_071_090"])
        self.assertTrue(prior_179["071_999_does_not_count"])
        self.assertTrue(prior_179["076_076_does_not_count"])
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, CYCLE177_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE174_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE160_GRAM3)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(STANDING_N_WITH_FORWARD_076_071_090, 3)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_five_on_ia(self):
        """3-gram is 5 on Ia (3 leftover + Ia7[166]/Ia14[136]); Ib unpublished 0."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 5)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 5)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 5)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM3, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM3), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        leftover_in_i = tuple(
            site for site in STANDING_I_SITES if site in STANDING_LEFTOVER_SITES
        )
        inside_in_i = tuple(
            site for site in STANDING_I_SITES if site in STANDING_INSIDE_SITES
        )
        self.assertEqual(leftover_in_i, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(len(leftover_in_i), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 3)
        self.assertEqual(inside_in_i, STANDING_INSIDE_FAMILY_SITES)
        self.assertEqual(inside_in_i, STANDING_LEFTOVER_090999_COVERED)
        self.assertEqual(len(inside_in_i), STANDING_INSIDE_FAMILY_COUNT)
        self.assertEqual(STANDING_INSIDE_FAMILY_COUNT, 2)
        self.assertTrue(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
        self.assertTrue(STANDING_INSIDE_FAMILY_SITES_CHECKED)
        self.assertEqual(
            STANDING_INSIDE_FAMILY_NEXT_4GRAMS,
            (
                STANDING_INSIDE_FAMILY_NEXT_4GRAM,
                STANDING_INSIDE_FAMILY_NEXT_4GRAM,
            ),
        )
        for site in STANDING_INSIDE_FAMILY_SITES:
            self.assertIn(site, STANDING_I_SITES)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N3]
            self.assertEqual(tuple(stems), GRAM3)
            self.assertEqual(side, SIDE_IA)
        for (side, line, index), nxt in zip(
            STANDING_I_SITES,
            STANDING_I_NEXT_4GRAMS,
            strict=True,
        ):
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), nxt)
            self.assertEqual(nxt[:3], GRAM3)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia1", 86),
                (SIDE_IA, "Ia3", 85),
                (SIDE_IA, "Ia7", 166),
                (SIDE_IA, "Ia12", 19),
                (SIDE_IA, "Ia14", 136),
            ),
        )
        leftover_next = tuple(
            nxt
            for site, nxt in zip(STANDING_I_SITES, STANDING_I_NEXT_4GRAMS, strict=True)
            if site in STANDING_LEFTOVER_MATCHING_SITES
        )
        inside_next = tuple(
            nxt
            for site, nxt in zip(STANDING_I_SITES, STANDING_I_NEXT_4GRAMS, strict=True)
            if site in STANDING_INSIDE_FAMILY_SITES
        )
        self.assertEqual(leftover_next, STANDING_MATCHING_NEXT_4GRAMS)
        self.assertEqual(inside_next, STANDING_INSIDE_FAMILY_NEXT_4GRAMS)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_zero_off_i_and_i_only(self):
        """3-gram is 0 on A–H and J–V. Ia has exactly 5. W is not a tablet."""
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
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM3))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 5)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(
            i_3gram_076_071_090_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_3GRAM_076_071_090_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_076_071_090_I_ONLY,
        )
        self.assertTrue(STANDING_I_3GRAM_076_071_090_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_3gram_076_071_090_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE141_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE160_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE174_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE177_3GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_179_178_177_176_175_174_173_172_171_170_167_160_141_103_and_w_scoreboards_still_compute(self):
        """Cycle 179 leftover 3, 178/177 I-only, 176/175/174/173/172/171/170, 167/160/141, 103, W stay."""
        prior_179 = TestMamariILeftover076071Forward090Scoreboard()
        prior_179.setUp()
        prior_179.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_179.test_survey_matches_computed_lock()
        prior_178 = TestMamariI076071600Forward4gramsIOnlyScoreboard()
        prior_178.setUp()
        prior_178.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_178.test_survey_matches_computed_lock()
        prior_177 = TestMamariI3gram076071600IOnlyScoreboard()
        prior_177.setUp()
        prior_177.test_3gram_is_zero_off_i_and_i_only()
        prior_177.test_survey_matches_computed_lock()
        prior_176 = TestMamariILeftover076071Forward600Scoreboard()
        prior_176.setUp()
        prior_176.test_counts_4_of_34_and_hypothesis_n_4_holds()
        prior_176.test_survey_matches_computed_lock()
        prior_175 = TestMamariI076071076Forward4gramsIOnlyScoreboard()
        prior_175.setUp()
        prior_175.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_175.test_survey_matches_computed_lock()
        prior_174 = TestMamariI3gram076071076IOnlyScoreboard()
        prior_174.setUp()
        prior_174.test_3gram_is_zero_off_i_and_i_only()
        prior_174.test_survey_matches_computed_lock()
        prior_173 = TestMamariILeftover076071Forward076Scoreboard()
        prior_173.setUp()
        prior_173.test_counts_5_of_34_and_hypothesis_n_5_holds()
        prior_173.test_survey_matches_computed_lock()
        prior_172 = TestMamariI2gram076071InsideFamilyScoreboard()
        prior_172.setUp()
        prior_172.test_forty_three_sites_split_9_inside_34_leftover_and_claim_loses()
        prior_172.test_survey_matches_computed_lock()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-180 3-gram I-only lock."""
        lock = self.survey["i_3gram_076_071_090_i_only"]
        self.assertEqual(lock["cycle"], 180)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 5)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            [list(gram) for gram in STANDING_I_NEXT_4GRAMS],
            lock["i_next_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(lock["leftover_matching_count"], 3)
        self.assertEqual(
            [list(site) for site in STANDING_INSIDE_FAMILY_SITES],
            lock["inside_family_sites"],
        )
        self.assertEqual(lock["inside_family_count"], STANDING_INSIDE_FAMILY_COUNT)
        self.assertEqual(lock["inside_family_count"], 2)
        self.assertTrue(lock["inside_family_site_included"])
        self.assertTrue(lock["inside_family_sites_checked"])
        self.assertEqual(
            [list(gram) for gram in STANDING_INSIDE_FAMILY_NEXT_4GRAMS],
            lock["inside_family_next_4grams"],
        )
        self.assertEqual(
            tuple(lock["inside_family_next_4gram"]),
            STANDING_INSIDE_FAMILY_NEXT_4GRAM,
        )
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
        self.assertTrue(lock["i_3gram_076_071_090_i_only"])
        self.assertEqual(
            lock["i_3gram_076_071_090_i_only"],
            STANDING_I_3GRAM_076_071_090_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle141_3gram"])
        self.assertFalse(lock["same_as_cycle160_3gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle171_2gram"])
        self.assertFalse(lock["same_as_cycle174_3gram"])
        self.assertFalse(lock["same_as_cycle177_3gram"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_090_unchanged"])
        self.assertTrue(lock["standing_i_076_071_600_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_076_071_600_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_600_unchanged"])
        self.assertTrue(lock["standing_i_076_071_076_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_076_071_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_076_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
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
        self.assertEqual(self.survey["i_leftover_076_071_forward_090"]["cycle"], 179)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_090"][
                "i_leftover_076_071_exactly_3_forward_076_071_090"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_forward_090"]["N_with_forward_076_071_090"],
            3,
        )
        self.assertEqual(self.survey["i_leftover_076_071_forward_090"]["N_without"], 31)
        self.assertEqual(self.survey["i_076_071_600_forward_4grams_i_only"]["cycle"], 178)
        self.assertTrue(
            self.survey["i_076_071_600_forward_4grams_i_only"][
                "i_076_071_600_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_076_071_600_i_only"]["cycle"], 177)
        self.assertTrue(
            self.survey["i_3gram_076_071_600_i_only"]["i_3gram_076_071_600_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_076_071_600_i_only"]["N_I"], 4)
        self.assertEqual(self.survey["i_3gram_076_071_600_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_076_071_forward_600"]["cycle"], 176)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_600"][
                "i_leftover_076_071_exactly_4_forward_076_071_600"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_forward_600"]["N_with_forward_076_071_600"],
            4,
        )
        self.assertEqual(self.survey["i_076_071_076_forward_4grams_i_only"]["cycle"], 175)
        self.assertTrue(
            self.survey["i_076_071_076_forward_4grams_i_only"][
                "i_076_071_076_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["cycle"], 174)
        self.assertTrue(self.survey["i_3gram_076_071_076_i_only"]["i_3gram_076_071_076_i_only"])
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_076_071_forward_076"]["cycle"], 173)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_076"][
                "i_leftover_076_071_exactly_5_forward_076_071_076"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_forward_076"]["N_with_forward_076_071_076"],
            5,
        )
        self.assertEqual(self.survey["i_leftover_076_071_forward_076"]["N_without"], 29)
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["cycle"], 172)
        self.assertFalse(
            self.survey["i_2gram_076_071_inside_family"][
                "i_2gram_076_071_all_inside_leftover_n4_family"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"][
                "i_leftover_n4_exactly_4_contain_076_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["N_with_076_071"], 4)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(
            self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
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


class TestMamariI3gram076071090IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 180 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
