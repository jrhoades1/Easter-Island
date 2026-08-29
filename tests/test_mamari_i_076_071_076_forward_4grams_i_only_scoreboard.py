"""I's cycle-174 3-gram site forward 4-grams off-I lock.

Cycle 175 text-search lock. Uses already-vendored A–V and the
cycle-174 I sites of 3-gram 076 071 076 (N_I=6, all Ia:
Ia2[43] leftover 076 071 076 021, Ia3[81] inside-family
076 071 076 385, Ia13[149] leftover 076 071 076 090,
Ia13[153] leftover 076 071 076 430, Ia14[81] leftover
076 071 076 010, Ia14[166] leftover 076 071 076 011).
Does not retune those 4-grams, the leftover 3-gram, or the
leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished
Ib is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Same leftover-shape as cycle 165 (leftover forward 4-grams
of 076 020 010 all I-only hapax 1/0) and cycle 169 (leftover
999 090 076 site 4-grams both I-only hapax 1/0). Cycle 173
leftover N=5 and leftover n=4 set stay. Ia3[81] is
inside-family (999 205 076 071) and is still a real
076 071 076 hit. 071 999 and 076 076 do not count. Do not
retune.

Locks exact consecutive hits of each forward 4-gram on
tablet I and on every other vendored tablet A–H and J–V.
Hypothesis: all six are I-only. Measured: each N_I=1 at
the cycle-174 I site above; all N_off_I=0. Claim that can
lose: i_076_071_076_forward_4grams_i_only. True only if
ALL six have N_off_I=0 (and N_I>=1). The claim is true.
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
from tests.test_mamari_i_3gram_076_071_076_i_only_scoreboard import (
    GRAM3,
    STANDING_I_NEXT_4GRAMS as CYCLE174_NEXT_4GRAMS,
    STANDING_I_SITES as CYCLE174_I_SITES,
    STANDING_INSIDE_FAMILY_NEXT_4GRAM,
    STANDING_INSIDE_FAMILY_SITE,
    STANDING_LEFTOVER_MATCHING_SITES,
    STANDING_N_I as CYCLE174_N_I,
    STANDING_N_OFF_I as CYCLE174_N_OFF_I,
    TestMamariI3gram076071076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_020_010_forward_4grams_i_only_scoreboard import (
    TestMamariILeftover076020010Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    STANDING_INSIDE_FORWARD_076_NEXT_4GRAM,
    STANDING_INSIDE_FORWARD_076_SITE,
    STANDING_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE173_MATCHING_SITES,
    STANDING_N_WITH_FORWARD_076_071_076,
    TestMamariILeftover076071Forward076Scoreboard,
)
from tests.test_mamari_i_leftover_999_090_076_site_4grams_i_only_scoreboard import (
    TestMamariILeftover999090076Site4gramsIOnlyScoreboard,
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
GRAM4_021 = ("076", "071", "076", "021")
GRAM4_385 = ("076", "071", "076", "385")
GRAM4_090 = ("076", "071", "076", "090")
GRAM4_430 = ("076", "071", "076", "430")
GRAM4_010 = ("076", "071", "076", "010")
GRAM4_011 = ("076", "071", "076", "011")
STANDING_SEQUENCES = (
    GRAM4_021,
    GRAM4_385,
    GRAM4_090,
    GRAM4_430,
    GRAM4_010,
    GRAM4_011,
)
STANDING_NEXT_STEMS = ("021", "385", "090", "430", "010", "011")
STANDING_ROLES = (
    "leftover",
    "inside_family",
    "leftover",
    "leftover",
    "leftover",
    "leftover",
)
STANDING_N_I_021 = 1
STANDING_N_I_385 = 1
STANDING_N_I_090 = 1
STANDING_N_I_430 = 1
STANDING_N_I_010 = 1
STANDING_N_I_011 = 1
STANDING_N_ON_I_021 = 1
STANDING_N_ON_I_385 = 1
STANDING_N_ON_I_090 = 1
STANDING_N_ON_I_430 = 1
STANDING_N_ON_I_010 = 1
STANDING_N_ON_I_011 = 1
STANDING_I_SITES_021 = ((SIDE_IA, "Ia2", 43),)
STANDING_I_SITES_385 = ((SIDE_IA, "Ia3", 81),)
STANDING_I_SITES_090 = ((SIDE_IA, "Ia13", 149),)
STANDING_I_SITES_430 = ((SIDE_IA, "Ia13", 153),)
STANDING_I_SITES_010 = ((SIDE_IA, "Ia14", 81),)
STANDING_I_SITES_011 = ((SIDE_IA, "Ia14", 166),)
STANDING_I_SITES = (
    STANDING_I_SITES_021,
    STANDING_I_SITES_385,
    STANDING_I_SITES_090,
    STANDING_I_SITES_430,
    STANDING_I_SITES_010,
    STANDING_I_SITES_011,
)
STANDING_CYCLE174_SITES = CYCLE174_I_SITES
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_021 = 0
STANDING_N_OFF_I_385 = 0
STANDING_N_OFF_I_090 = 0
STANDING_N_OFF_I_430 = 0
STANDING_N_OFF_I_010 = 0
STANDING_N_OFF_I_011 = 0
STANDING_OFF_I_SITES_021 = ()
STANDING_OFF_I_SITES_385 = ()
STANDING_OFF_I_SITES_090 = ()
STANDING_OFF_I_SITES_430 = ()
STANDING_OFF_I_SITES_010 = ()
STANDING_OFF_I_SITES_011 = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_076_071_076_forward_4grams_i_only"
STANDING_I_076_071_076_FORWARD_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_076_071_076_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE165_LEFTOVER_4GRAMS = False
STANDING_SAME_AS_CYCLE169_SITE_4GRAMS = False
STANDING_SAME_LEFTOVER_SHAPE_AS_165_169 = True
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_SITE_INCLUDED = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def leftover_forward_4gram_start_site(
    cycle174_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-174 076 071 076 site."""
    return cycle174_site


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_076_071_076_forward_4grams_i_only(
    n_i_021: int,
    n_off_i_021: int,
    n_i_385: int,
    n_off_i_385: int,
    n_i_090: int,
    n_off_i_090: int,
    n_i_430: int,
    n_off_i_430: int,
    n_i_010: int,
    n_off_i_010: int,
    n_i_011: int,
    n_off_i_011: int,
) -> bool:
    """True iff all six forward 4-grams are I-only.

    Claim holds only if all six have N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only.
    """
    return (
        sequence_is_i_only(n_i_021, n_off_i_021)
        and sequence_is_i_only(n_i_385, n_off_i_385)
        and sequence_is_i_only(n_i_090, n_off_i_090)
        and sequence_is_i_only(n_i_430, n_off_i_430)
        and sequence_is_i_only(n_i_010, n_off_i_010)
        and sequence_is_i_only(n_i_011, n_off_i_011)
    )


class TestI076071076Forward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-174 forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 071 999 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM4_021, ("076", "071", "076", "021"))
        self.assertEqual(GRAM4_385, ("076", "071", "076", "385"))
        self.assertEqual(GRAM4_090, ("076", "071", "076", "090"))
        self.assertEqual(GRAM4_430, ("076", "071", "076", "430"))
        self.assertEqual(GRAM4_010, ("076", "071", "076", "010"))
        self.assertEqual(GRAM4_011, ("076", "071", "076", "011"))
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:3], GRAM3)
        adjacent = [list(GRAM4_021), list(GRAM4_385)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_021), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_385), 1)
        overlap = [["076", "071", "076", "021", "076", "071", "076", "021"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_021), 2)
        gapped = [list(GRAM4_021[:2]) + ["000"] + list(GRAM4_021[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_021), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_021), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_011), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_071_065_071_999)], GRAM4_021), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM4_385), 0)
        self.assertEqual(ngram_hit_count([["071", "999"]], GRAM4_021), 0)
        self.assertEqual(ngram_hit_count([["076", "076"]], GRAM4_385), 0)
        self.assertEqual(ngram_hit_count([["076", "071", "076"]], GRAM4_021), 0)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all six forward 4-grams are I-only."""
        provider = MockProvider()
        hold = (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
        self.assertTrue(i_076_071_076_forward_4grams_i_only(*hold))
        self.assertTrue(i_076_071_076_forward_4grams_i_only(2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0))
        lose_off = (
            (1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0),
            (1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0),
            (1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0),
            (1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0),
            (1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0),
            (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1),
        )
        for counts in lose_off:
            self.assertFalse(i_076_071_076_forward_4grams_i_only(*counts))
        lose_missing_i = (
            (0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0),
            (1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0),
            (1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0),
            (1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0),
            (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0),
            (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0),
        )
        for counts in lose_missing_i:
            self.assertFalse(i_076_071_076_forward_4grams_i_only(*counts))
        self.assertFalse(i_076_071_076_forward_4grams_i_only(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        self.assertEqual(STANDING_CLAIM, "i_076_071_076_forward_4grams_i_only")
        self.assertTrue(STANDING_I_076_071_076_FORWARD_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_076_071_076_FORWARD_4GRAMS_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_174_forwards_not_retuned(self):
        """4-grams stay the cycle-174 I-site forwards; none is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "071", "076"))
        self.assertEqual(STANDING_SEQUENCES, CYCLE174_NEXT_4GRAMS)
        self.assertEqual(STANDING_NEXT_STEMS, ("021", "385", "090", "430", "010", "011"))
        self.assertEqual(STANDING_CYCLE174_SITES, CYCLE174_I_SITES)
        self.assertNotEqual(GRAM4_021, GRAM5)
        self.assertNotEqual(GRAM4_385, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM4_021, GRAM5))
        self.assertEqual(GRAM4_385, STANDING_INSIDE_FAMILY_NEXT_4GRAM)
        self.assertEqual(GRAM4_385, STANDING_INSIDE_FORWARD_076_NEXT_4GRAM)
        leftover_forwards = (
            GRAM4_021,
            GRAM4_090,
            GRAM4_430,
            GRAM4_010,
            GRAM4_011,
        )
        self.assertEqual(leftover_forwards, STANDING_MATCHING_NEXT_4GRAMS)
        self.assertNotIn(GRAM4_385, STANDING_MATCHING_NEXT_4GRAMS)
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_071_065_071_999))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_700_076_076_053))
        for site, start in zip(
            STANDING_CYCLE174_SITES,
            (
                STANDING_I_SITES_021[0],
                STANDING_I_SITES_385[0],
                STANDING_I_SITES_090[0],
                STANDING_I_SITES_430[0],
                STANDING_I_SITES_010[0],
                STANDING_I_SITES_011[0],
            ),
            strict=True,
        ):
            self.assertEqual(leftover_forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE165_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE169_SITE_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_165_169)
        self.assertTrue(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(GRAM4_021), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI076071076Forward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture cycle-174 forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle174_sites = STANDING_CYCLE174_SITES
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
        self.claim_holds = i_076_071_076_forward_4grams_i_only(
            *sum(zip(self.n_i, self.n_off_i, strict=True), ())
        )

    def test_tokens_and_sites_are_cycle_174_lock_not_retuned(self):
        """4-grams and I sites stay the cycle-174 forward lock."""
        self.assertEqual(GRAM3, ("076", "071", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle174_sites, STANDING_CYCLE174_SITES)
        self.assertEqual(
            STANDING_CYCLE174_SITES,
            (
                (SIDE_IA, "Ia2", 43),
                (SIDE_IA, "Ia3", 81),
                (SIDE_IA, "Ia13", 149),
                (SIDE_IA, "Ia13", 153),
                (SIDE_IA, "Ia14", 81),
                (SIDE_IA, "Ia14", 166),
            ),
        )
        prior_174 = self.survey["i_3gram_076_071_076_i_only"]
        self.assertEqual(prior_174["cycle"], 174)
        self.assertEqual(tuple(prior_174["tokens3"]), GRAM3)
        self.assertEqual(prior_174["N_I"], CYCLE174_N_I)
        self.assertEqual(prior_174["N_I"], 6)
        self.assertEqual(prior_174["N_off_I"], CYCLE174_N_OFF_I)
        self.assertEqual(prior_174["N_off_I"], 0)
        self.assertTrue(prior_174["i_3gram_076_071_076_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_174["i_sites"]),
            STANDING_CYCLE174_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_174["i_next_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_174["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(tuple(prior_174["inside_family_site"]), STANDING_INSIDE_FAMILY_SITE)
        self.assertEqual(
            tuple(prior_174["inside_family_next_4gram"]),
            STANDING_INSIDE_FAMILY_NEXT_4GRAM,
        )
        prior_173 = self.survey["i_leftover_076_071_forward_076"]
        self.assertEqual(prior_173["cycle"], 173)
        self.assertEqual(prior_173["N_with_forward_076_071_076"], STANDING_N_WITH_FORWARD_076_071_076)
        self.assertEqual(prior_173["N_with_forward_076_071_076"], 5)
        self.assertTrue(prior_173["i_leftover_076_071_exactly_5_forward_076_071_076"])
        self.assertEqual(CYCLE173_MATCHING_SITES, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(STANDING_INSIDE_FORWARD_076_SITE, STANDING_INSIDE_FAMILY_SITE)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertEqual(GRAM3[:2], CYCLE171_GRAM2)
        prior_170 = self.survey["i_leftover_n4_076_071"]
        self.assertEqual(prior_170["cycle"], 170)
        self.assertTrue(prior_170["i_leftover_n4_exactly_4_contain_076_071"])
        prior_169 = self.survey["i_leftover_999_090_076_site_4grams_i_only"]
        self.assertEqual(prior_169["cycle"], 169)
        self.assertTrue(prior_169["i_leftover_999_090_076_site_4grams_i_only"])
        prior_165 = self.survey["i_leftover_076_020_010_forward_4grams_i_only"]
        self.assertEqual(prior_165["cycle"], 165)
        self.assertTrue(prior_165["i_leftover_076_020_010_forward_4grams_all_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_I=1/1/1/1/1/1, N_off_I=0/0/0/0/0/0. All I-only. Claim holds."""
        standing_on = (
            STANDING_N_I_021,
            STANDING_N_I_385,
            STANDING_N_I_090,
            STANDING_N_I_430,
            STANDING_N_I_010,
            STANDING_N_I_011,
        )
        standing_off = (
            STANDING_N_OFF_I_021,
            STANDING_N_OFF_I_385,
            STANDING_N_OFF_I_090,
            STANDING_N_OFF_I_430,
            STANDING_N_OFF_I_010,
            STANDING_N_OFF_I_011,
        )
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, standing_on)
        self.assertEqual(standing_on, (1, 1, 1, 1, 1, 1))
        self.assertEqual(self.n_off_i, standing_off)
        self.assertEqual(standing_off, (0, 0, 0, 0, 0, 0))
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        for site, start, gram, nxt, role in zip(
            STANDING_CYCLE174_SITES,
            (
                STANDING_I_SITES_021[0],
                STANDING_I_SITES_385[0],
                STANDING_I_SITES_090[0],
                STANDING_I_SITES_430[0],
                STANDING_I_SITES_010[0],
                STANDING_I_SITES_011[0],
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
            if role == "inside_family":
                self.assertEqual(start, STANDING_INSIDE_FAMILY_SITE)
                self.assertEqual(gram, STANDING_INSIDE_FAMILY_NEXT_4GRAM)
                self.assertNotIn(start, STANDING_LEFTOVER_MATCHING_SITES)
            else:
                self.assertIn(start, STANDING_LEFTOVER_MATCHING_SITES)
                self.assertIn(gram, STANDING_MATCHING_NEXT_4GRAMS)
        self.assertTrue(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
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
            i_076_071_076_forward_4grams_i_only(
                *sum(zip(self.n_i, self.n_off_i, strict=True), ())
            ),
            STANDING_I_076_071_076_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_076_071_076_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertTrue(STANDING_I_076_071_076_FORWARD_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_076_071_076_forward_4grams_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE165_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE169_SITE_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_165_169)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_174_173_171_170_169_165_103_and_w_scoreboards_still_compute(self):
        """Cycle 174 I-only, 173 leftover 5, 171/170, 169/165, 103, W stay."""
        prior_174 = TestMamariI3gram076071076IOnlyScoreboard()
        prior_174.setUp()
        prior_174.test_i_hits_are_six_on_ia()
        prior_174.test_3gram_is_zero_off_i_and_i_only()
        prior_174.test_survey_matches_computed_lock()
        prior_173 = TestMamariILeftover076071Forward076Scoreboard()
        prior_173.setUp()
        prior_173.test_counts_5_of_34_and_hypothesis_n_5_holds()
        prior_173.test_survey_matches_computed_lock()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_169 = TestMamariILeftover999090076Site4gramsIOnlyScoreboard()
        prior_169.setUp()
        prior_169.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_169.test_survey_matches_computed_lock()
        prior_165 = TestMamariILeftover076020010Forward4gramsIOnlyScoreboard()
        prior_165.setUp()
        prior_165.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_165.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-175 forward-4 I-only lock."""
        lock = self.survey["i_076_071_076_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 175)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I_3gram"], CYCLE174_N_I)
        self.assertEqual(lock["N_I_3gram"], 6)
        self.assertEqual(lock["N_off_I_3gram"], CYCLE174_N_OFF_I)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle174_sites"]),
            STANDING_CYCLE174_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], 5)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(tuple(lock["inside_family_site"]), STANDING_INSIDE_FAMILY_SITE)
        self.assertEqual(lock["inside_family_count"], 1)
        self.assertTrue(lock["inside_family_site_included"])
        self.assertEqual(
            tuple(lock["inside_family_next_4gram"]),
            STANDING_INSIDE_FAMILY_NEXT_4GRAM,
        )
        self.assertEqual(tuple(lock["per_site_next_stems"]), STANDING_NEXT_STEMS)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 6)
        standing_on = (
            STANDING_N_I_021,
            STANDING_N_I_385,
            STANDING_N_I_090,
            STANDING_N_I_430,
            STANDING_N_I_010,
            STANDING_N_I_011,
        )
        standing_off = (
            STANDING_N_OFF_I_021,
            STANDING_N_OFF_I_385,
            STANDING_N_OFF_I_090,
            STANDING_N_OFF_I_430,
            STANDING_N_OFF_I_010,
            STANDING_N_OFF_I_011,
        )
        for row, gram, site, nxt, role, sites, n_on, n_off in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CYCLE174_SITES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            standing_on,
            standing_off,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle174_site"]), site)
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
        self.assertEqual(lock["N_I_021"], STANDING_N_I_021)
        self.assertEqual(lock["N_off_I_021"], STANDING_N_OFF_I_021)
        self.assertEqual(lock["N_I_385"], STANDING_N_I_385)
        self.assertEqual(lock["N_off_I_385"], STANDING_N_OFF_I_385)
        self.assertEqual(lock["N_I_090"], STANDING_N_I_090)
        self.assertEqual(lock["N_off_I_090"], STANDING_N_OFF_I_090)
        self.assertEqual(lock["N_I_430"], STANDING_N_I_430)
        self.assertEqual(lock["N_off_I_430"], STANDING_N_OFF_I_430)
        self.assertEqual(lock["N_I_010"], STANDING_N_I_010)
        self.assertEqual(lock["N_off_I_010"], STANDING_N_OFF_I_010)
        self.assertEqual(lock["N_I_011"], STANDING_N_I_011)
        self.assertEqual(lock["N_off_I_011"], STANDING_N_OFF_I_011)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_076_071_076_forward_4grams_i_only"])
        self.assertEqual(
            lock["i_076_071_076_forward_4grams_i_only"],
            STANDING_I_076_071_076_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle165_leftover_4grams"])
        self.assertFalse(lock["same_as_cycle169_site_4grams"])
        self.assertTrue(lock["same_leftover_shape_as_cycles_165_169"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_076_071_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_076_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_leftover_999_090_076_site_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["cycle"], 174)
        self.assertTrue(
            self.survey["i_3gram_076_071_076_i_only"]["i_3gram_076_071_076_i_only"]
        )
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
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"]["i_leftover_n4_exactly_4_contain_076_071"]
        )
        self.assertEqual(
            self.survey["i_leftover_999_090_076_site_4grams_i_only"]["cycle"], 169
        )
        self.assertTrue(
            self.survey["i_leftover_999_090_076_site_4grams_i_only"][
                "i_leftover_999_090_076_site_4grams_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_020_010_forward_4grams_i_only"]["cycle"], 165
        )
        self.assertTrue(
            self.survey["i_leftover_076_020_010_forward_4grams_i_only"][
                "i_leftover_076_020_010_forward_4grams_all_i_only"
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


class TestMamariI076071076Forward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 175 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
