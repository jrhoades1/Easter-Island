"""I's cycle-177 3-gram site forward 4-grams off-I lock.

Cycle 178 text-search lock. Uses already-vendored A–V and the
cycle-177 I sites of 3-gram 076 071 600 (N_I=4, all Ia, no
inside-family extras: Ia2[104] leftover 076 071 600 090,
Ia2[169] leftover 076 071 600 009, Ia9[10] leftover
076 071 600 999, Ia14[106] leftover 076 071 600 053).
Those four ARE the cycle-176 leftover matching sites. Does
not retune those 4-grams, the leftover 3-gram, or the leftover
n=4 set. Does not vendor a new tablet. Does not scrape X. W
has no Barthel (cycle 100); skip W. Unpublished Ib is 0. Does
not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same leftover-shape as cycle 175 (076 071 076 forward 4-grams
all I-only hapax 1/0). Cycle 176 leftover N=4 and leftover
n=4 set stay. 071 999 and 076 076 do not count. Do not
retune.

Locks exact consecutive hits of each forward 4-gram on
tablet I and on every other vendored tablet A–H and J–V.
Hypothesis: all four are I-only. Measured: each N_I=1 at
the cycle-177 I site above; all N_off_I=0. Claim that can
lose: i_076_071_600_forward_4grams_i_only. True only if
ALL four have N_off_I=0 (and N_I>=1). The claim is true.
Do not assume hapax; measure. Do not retune.

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
from tests.test_mamari_i_3gram_076_071_600_i_only_scoreboard import (
    GRAM3,
    STANDING_I_NEXT_4GRAMS as CYCLE177_NEXT_4GRAMS,
    STANDING_I_SITES as CYCLE177_I_SITES,
    STANDING_INSIDE_FAMILY_COUNT,
    STANDING_INSIDE_FAMILY_SITES,
    STANDING_LEFTOVER_MATCHING_SITES,
    STANDING_N_I as CYCLE177_N_I,
    STANDING_N_OFF_I as CYCLE177_N_OFF_I,
    TestMamariI3gram076071600IOnlyScoreboard,
)
from tests.test_mamari_i_076_071_076_forward_4grams_i_only_scoreboard import (
    TestMamariI076071076Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_600_scoreboard import (
    STANDING_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE176_MATCHING_SITES,
    STANDING_N_WITH_FORWARD_076_071_600,
    TestMamariILeftover076071Forward600Scoreboard,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    NEAR_MISS_071_065_071_999,
    NEAR_MISS_700_076_076_053,
    TestMamariILeftoverN4076071Scoreboard,
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

HYPOTHESIS_ALL_I_ONLY = True
STANDING_N3 = 3
STANDING_N4 = 4
GRAM4_090 = ("076", "071", "600", "090")
GRAM4_009 = ("076", "071", "600", "009")
GRAM4_999 = ("076", "071", "600", "999")
GRAM4_053 = ("076", "071", "600", "053")
STANDING_SEQUENCES = (
    GRAM4_090,
    GRAM4_009,
    GRAM4_999,
    GRAM4_053,
)
STANDING_NEXT_STEMS = ("090", "009", "999", "053")
STANDING_ROLES = (
    "leftover",
    "leftover",
    "leftover",
    "leftover",
)
STANDING_N_I_090 = 1
STANDING_N_I_009 = 1
STANDING_N_I_999 = 1
STANDING_N_I_053 = 1
STANDING_N_ON_I_090 = 1
STANDING_N_ON_I_009 = 1
STANDING_N_ON_I_999 = 1
STANDING_N_ON_I_053 = 1
STANDING_I_SITES_090 = ((SIDE_IA, "Ia2", 104),)
STANDING_I_SITES_009 = ((SIDE_IA, "Ia2", 169),)
STANDING_I_SITES_999 = ((SIDE_IA, "Ia9", 10),)
STANDING_I_SITES_053 = ((SIDE_IA, "Ia14", 106),)
STANDING_I_SITES = (
    STANDING_I_SITES_090,
    STANDING_I_SITES_009,
    STANDING_I_SITES_999,
    STANDING_I_SITES_053,
)
STANDING_CYCLE177_SITES = CYCLE177_I_SITES
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_090 = 0
STANDING_N_OFF_I_009 = 0
STANDING_N_OFF_I_999 = 0
STANDING_N_OFF_I_053 = 0
STANDING_OFF_I_SITES_090 = ()
STANDING_OFF_I_SITES_009 = ()
STANDING_OFF_I_SITES_999 = ()
STANDING_OFF_I_SITES_053 = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_076_071_600_forward_4grams_i_only"
STANDING_I_076_071_600_FORWARD_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_076_071_600_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS = False
STANDING_SAME_LEFTOVER_SHAPE_AS_175 = True
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_SITE_INCLUDED = False
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def leftover_forward_4gram_start_site(
    cycle177_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-177 076 071 600 site."""
    return cycle177_site


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_076_071_600_forward_4grams_i_only(
    n_i_090: int,
    n_off_i_090: int,
    n_i_009: int,
    n_off_i_009: int,
    n_i_999: int,
    n_off_i_999: int,
    n_i_053: int,
    n_off_i_053: int,
) -> bool:
    """True iff all four forward 4-grams are I-only.

    Claim holds only if all four have N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only.
    """
    return (
        sequence_is_i_only(n_i_090, n_off_i_090)
        and sequence_is_i_only(n_i_009, n_off_i_009)
        and sequence_is_i_only(n_i_999, n_off_i_999)
        and sequence_is_i_only(n_i_053, n_off_i_053)
    )


class TestI076071600Forward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-177 forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 071 999 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM4_090, ("076", "071", "600", "090"))
        self.assertEqual(GRAM4_009, ("076", "071", "600", "009"))
        self.assertEqual(GRAM4_999, ("076", "071", "600", "999"))
        self.assertEqual(GRAM4_053, ("076", "071", "600", "053"))
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:3], GRAM3)
        adjacent = [list(GRAM4_090), list(GRAM4_009)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_090), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_009), 1)
        overlap = [["076", "071", "600", "090", "076", "071", "600", "090"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_090), 2)
        gapped = [list(GRAM4_090[:2]) + ["000"] + list(GRAM4_090[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_053), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_071_065_071_999)], GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM4_009), 0)
        self.assertEqual(ngram_hit_count([["071", "999"]], GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([["076", "076"]], GRAM4_009), 0)
        self.assertEqual(ngram_hit_count([["076", "071", "600"]], GRAM4_090), 0)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all four forward 4-grams are I-only."""
        provider = MockProvider()
        hold = (1, 0, 1, 0, 1, 0, 1, 0)
        self.assertTrue(i_076_071_600_forward_4grams_i_only(*hold))
        self.assertTrue(i_076_071_600_forward_4grams_i_only(2, 0, 1, 0, 1, 0, 1, 0))
        lose_off = (
            (1, 1, 1, 0, 1, 0, 1, 0),
            (1, 0, 1, 1, 1, 0, 1, 0),
            (1, 0, 1, 0, 1, 1, 1, 0),
            (1, 0, 1, 0, 1, 0, 1, 1),
        )
        for counts in lose_off:
            self.assertFalse(i_076_071_600_forward_4grams_i_only(*counts))
        lose_missing_i = (
            (0, 0, 1, 0, 1, 0, 1, 0),
            (1, 0, 0, 0, 1, 0, 1, 0),
            (1, 0, 1, 0, 0, 0, 1, 0),
            (1, 0, 1, 0, 1, 0, 0, 0),
        )
        for counts in lose_missing_i:
            self.assertFalse(i_076_071_600_forward_4grams_i_only(*counts))
        self.assertFalse(i_076_071_600_forward_4grams_i_only(0, 0, 0, 0, 0, 0, 0, 0))
        self.assertEqual(STANDING_CLAIM, "i_076_071_600_forward_4grams_i_only")
        self.assertTrue(STANDING_I_076_071_600_FORWARD_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_076_071_600_FORWARD_4GRAMS_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_177_forwards_not_retuned(self):
        """4-grams stay the cycle-177 I-site forwards; none is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "071", "600"))
        self.assertEqual(STANDING_SEQUENCES, CYCLE177_NEXT_4GRAMS)
        self.assertEqual(STANDING_NEXT_STEMS, ("090", "009", "999", "053"))
        self.assertEqual(STANDING_CYCLE177_SITES, CYCLE177_I_SITES)
        self.assertNotEqual(GRAM4_090, GRAM5)
        self.assertNotEqual(GRAM4_009, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM4_090, GRAM5))
        leftover_forwards = (
            GRAM4_090,
            GRAM4_009,
            GRAM4_999,
            GRAM4_053,
        )
        self.assertEqual(leftover_forwards, STANDING_MATCHING_NEXT_4GRAMS)
        self.assertEqual(STANDING_INSIDE_FAMILY_SITES, ())
        self.assertEqual(STANDING_INSIDE_FAMILY_COUNT, 0)
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_071_065_071_999))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_700_076_076_053))
        for site, start in zip(
            STANDING_CYCLE177_SITES,
            (
                STANDING_I_SITES_090[0],
                STANDING_I_SITES_009[0],
                STANDING_I_SITES_999[0],
                STANDING_I_SITES_053[0],
            ),
            strict=True,
        ):
            self.assertEqual(leftover_forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_175)
        self.assertFalse(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(GRAM4_090), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI076071600Forward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture cycle-177 forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle177_sites = STANDING_CYCLE177_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.grams = STANDING_SEQUENCES
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in self.grams)
        self.n_i = tuple(
            ngram_hit_count(self.i_sides[SIDE_IA], gram) + STANDING_IB_HITS
            for gram in self.grams
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in self.grams
        )
        self.off_i = tuple(
            tablet_hit_counts(self.by_tablet, gram, OFF_I_TABLETS)
            for gram in self.grams
        )
        self.n_off_i = tuple(sum(row) for row in self.off_i)
        self.claim_holds = i_076_071_600_forward_4grams_i_only(
            *sum(zip(self.n_i, self.n_off_i, strict=True), ())
        )

    def test_tokens_and_sites_are_cycle_177_lock_not_retuned(self):
        """4-grams and I sites stay the cycle-177 forward lock."""
        self.assertEqual(GRAM3, ("076", "071", "600"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle177_sites, STANDING_CYCLE177_SITES)
        self.assertEqual(
            STANDING_CYCLE177_SITES,
            (
                (SIDE_IA, "Ia2", 104),
                (SIDE_IA, "Ia2", 169),
                (SIDE_IA, "Ia9", 10),
                (SIDE_IA, "Ia14", 106),
            ),
        )
        prior_177 = self.survey["i_3gram_076_071_600_i_only"]
        self.assertEqual(prior_177["cycle"], 177)
        self.assertEqual(tuple(prior_177["tokens3"]), GRAM3)
        self.assertEqual(prior_177["N_I"], CYCLE177_N_I)
        self.assertEqual(prior_177["N_I"], 4)
        self.assertEqual(prior_177["N_off_I"], CYCLE177_N_OFF_I)
        self.assertEqual(prior_177["N_off_I"], 0)
        self.assertTrue(prior_177["i_3gram_076_071_600_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_177["i_sites"]),
            STANDING_CYCLE177_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_177["i_next_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_177["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(prior_177["inside_family_count"], 0)
        self.assertEqual(prior_177["inside_family_sites"], [])
        prior_176 = self.survey["i_leftover_076_071_forward_600"]
        self.assertEqual(prior_176["cycle"], 176)
        self.assertEqual(prior_176["N_with_forward_076_071_600"], STANDING_N_WITH_FORWARD_076_071_600)
        self.assertEqual(prior_176["N_with_forward_076_071_600"], 4)
        self.assertTrue(prior_176["i_leftover_076_071_exactly_4_forward_076_071_600"])
        self.assertEqual(CYCLE176_MATCHING_SITES, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(CYCLE176_MATCHING_SITES, STANDING_CYCLE177_SITES)
        prior_175 = self.survey["i_076_071_076_forward_4grams_i_only"]
        self.assertEqual(prior_175["cycle"], 175)
        self.assertTrue(prior_175["i_076_071_076_forward_4grams_i_only"])
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertEqual(GRAM3[:2], CYCLE171_GRAM2)
        prior_170 = self.survey["i_leftover_n4_076_071"]
        self.assertEqual(prior_170["cycle"], 170)
        self.assertTrue(prior_170["i_leftover_n4_exactly_4_contain_076_071"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_I=1/1/1/1, N_off_I=0/0/0/0. All I-only. Claim holds."""
        standing_on = (
            STANDING_N_I_090,
            STANDING_N_I_009,
            STANDING_N_I_999,
            STANDING_N_I_053,
        )
        standing_off = (
            STANDING_N_OFF_I_090,
            STANDING_N_OFF_I_009,
            STANDING_N_OFF_I_999,
            STANDING_N_OFF_I_053,
        )
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, standing_on)
        self.assertEqual(standing_on, (1, 1, 1, 1))
        self.assertEqual(self.n_off_i, standing_off)
        self.assertEqual(standing_off, (0, 0, 0, 0))
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        for site, start, gram, nxt, role in zip(
            STANDING_CYCLE177_SITES,
            (
                STANDING_I_SITES_090[0],
                STANDING_I_SITES_009[0],
                STANDING_I_SITES_999[0],
                STANDING_I_SITES_053[0],
            ),
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            strict=True,
        ):
            self.assertEqual(leftover_forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2] + STANDING_N3], nxt)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N3]), GRAM3)
            self.assertNotEqual(gram, GRAM5)
            self.assertEqual(role, "leftover")
            self.assertIn(start, STANDING_LEFTOVER_MATCHING_SITES)
            self.assertIn(gram, STANDING_MATCHING_NEXT_4GRAMS)
        self.assertFalse(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
        self.assertEqual(STANDING_INSIDE_FAMILY_COUNT, 0)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off in zip(self.hits_by_tablet, self.off_i, strict=True):
            self.assertEqual(hits, STANDING_HITS_BY_TABLET_ONE_ON_I)
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
        for tablet, *counts in zip(
            VENDORED_TABLETS,
            *self.hits_by_tablet,
            strict=True,
        ):
            for count, gram in zip(counts, self.grams, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                self.assertEqual(count, 1 if tablet == "I" else 0)
        self.assertEqual(
            i_076_071_600_forward_4grams_i_only(
                *sum(zip(self.n_i, self.n_off_i, strict=True), ())
            ),
            STANDING_I_076_071_600_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_076_071_600_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertTrue(STANDING_I_076_071_600_FORWARD_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_076_071_600_forward_4grams_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_175)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_177_176_175_171_170_103_and_w_scoreboards_still_compute(self):
        """Cycle 177 I-only, 176 leftover 4, 175/171/170, 103, W stay."""
        prior_177 = TestMamariI3gram076071600IOnlyScoreboard()
        prior_177.setUp()
        prior_177.test_i_hits_are_four_on_ia()
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
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-178 forward-4 I-only lock."""
        lock = self.survey["i_076_071_600_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 178)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I_3gram"], CYCLE177_N_I)
        self.assertEqual(lock["N_I_3gram"], 4)
        self.assertEqual(lock["N_off_I_3gram"], CYCLE177_N_OFF_I)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle177_sites"]),
            STANDING_CYCLE177_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(lock["inside_family_sites"], [])
        self.assertEqual(lock["inside_family_count"], 0)
        self.assertFalse(lock["inside_family_site_included"])
        self.assertEqual(tuple(lock["per_site_next_stems"]), STANDING_NEXT_STEMS)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 4)
        standing_on = (
            STANDING_N_I_090,
            STANDING_N_I_009,
            STANDING_N_I_999,
            STANDING_N_I_053,
        )
        standing_off = (
            STANDING_N_OFF_I_090,
            STANDING_N_OFF_I_009,
            STANDING_N_OFF_I_999,
            STANDING_N_OFF_I_053,
        )
        for row, gram, site, nxt, role, sites, n_on, n_off in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CYCLE177_SITES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            standing_on,
            standing_off,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle177_site"]), site)
            self.assertEqual(row["next_stem"], nxt)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_I"], 1)
            self.assertEqual(row["ia_hits"], 1)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["ib_sites"]),
                STANDING_IB_SITES,
            )
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(
                tuple(row["hits_by_tablet"]),
                STANDING_HITS_BY_TABLET_ONE_ON_I,
            )
            self.assertTrue(row["i_only"])
        self.assertEqual(lock["N_I_090"], STANDING_N_I_090)
        self.assertEqual(lock["N_off_I_090"], STANDING_N_OFF_I_090)
        self.assertEqual(lock["N_I_009"], STANDING_N_I_009)
        self.assertEqual(lock["N_off_I_009"], STANDING_N_OFF_I_009)
        self.assertEqual(lock["N_I_999"], STANDING_N_I_999)
        self.assertEqual(lock["N_off_I_999"], STANDING_N_OFF_I_999)
        self.assertEqual(lock["N_I_053"], STANDING_N_I_053)
        self.assertEqual(lock["N_off_I_053"], STANDING_N_OFF_I_053)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_076_071_600_forward_4grams_i_only"])
        self.assertEqual(
            lock["i_076_071_600_forward_4grams_i_only"],
            STANDING_I_076_071_600_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle175_forward_4grams"])
        self.assertTrue(lock["same_leftover_shape_as_cycle_175"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_076_071_600_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_600_unchanged"])
        self.assertTrue(lock["standing_i_076_071_076_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
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
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"]["i_leftover_n4_exactly_4_contain_076_071"]
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


class TestMamariI076071600Forward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 178 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
