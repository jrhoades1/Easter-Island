"""I's cycle-205 leftover 2-gram 076 070 off-I lock.

Cycle 206 text-search lock. Uses already-vendored A–V and the
cycle-205 leftover 2-gram 076 070 (the n=2 run inside leftover
n=4 maximal 999 090 076 070). Does not retune that 2-gram or
the leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished Ib
is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Same claim-shape as cycle 171 (076 071 was I-only 43/0),
cycle 167 (999 090 076 was I-only 16/0), cycle 160
(076 020 010 was I-only 12/0), and cycle 141 (076 010 079
was I-only 8/0). This cycle is the new leftover 2-gram
076 070 only. 076 071 (999 090 076 071) does not count.
076 076 (700 076 076 053) does not. Do not retune 076 071,
999 090 076, 076 020 010, or 076 010 079. Do not assume
the I-only result.

Locks exact consecutive hits of 076 070 on tablet I and on
every other vendored tablet A–H and J–V. Claim that can lose:
i_2gram_076_070_i_only (I hits ≥ 1 and off-I hits == 0).
True only if N_off_I == 0. Measured: Ia is exactly 19; Ib
unpublished 0; off-I is 5 on G (2), S (1), and T (2). The
claim is false. Not an n≥8 island. Not the cycle-103 I
5-gram. Five of the 19 I sites sit inside leftover n=4
999 090 076 070; the other 14 are extra.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_g_nge8_scoreboard import (
    nge8_sites,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    TA_LINE_NAMES,
    load_t_sides,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    GRAM2 as CYCLE205_GRAM2,
    NEAR_MISS_700_076_076_053,
    NEAR_MISS_999_090_076_071,
    STANDING_MATCHING_LEFTOVERS,
    STANDING_WITH_ROWS,
    TestMamariILeftoverN4076070Scoreboard,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    TestMamariILeftoverN4076071Scoreboard,
)
from tests.test_mamari_i_leftover_n4_999_090_076_scoreboard import (
    STANDING_MATCHING_LEFTOVERS as CYCLE166_MATCHING_LEFTOVERS,
    TestMamariILeftoverN4999090076Scoreboard,
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
from tests.test_mamari_keiti_n9_scoreboard import (
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_s_nge6_scoreboard import (
    nge6_sites,
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
from tests.test_mamari_small_santiago_gv_scoreboard import GV_LINE_NAMES
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
    load_g_k_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    SB_LINE_NAMES,
    SIDE_SA,
    SIDE_SB,
    load_s_sides,
)

HYPOTHESIS_I_ONLY = True
GRAM2 = CYCLE205_GRAM2
STANDING_N2 = 2
STANDING_I_HITS = 19
STANDING_IA_HITS = 19
STANDING_IB_HITS = 0
STANDING_N_ON_I = 19
STANDING_N_I = 19
STANDING_I_SITES = (
    (SIDE_IA, "Ia1", 79),
    (SIDE_IA, "Ia1", 141),
    (SIDE_IA, "Ia2", 11),
    (SIDE_IA, "Ia2", 125),
    (SIDE_IA, "Ia3", 5),
    (SIDE_IA, "Ia3", 123),
    (SIDE_IA, "Ia4", 113),
    (SIDE_IA, "Ia5", 61),
    (SIDE_IA, "Ia6", 144),
    (SIDE_IA, "Ia7", 63),
    (SIDE_IA, "Ia7", 69),
    (SIDE_IA, "Ia7", 130),
    (SIDE_IA, "Ia8", 121),
    (SIDE_IA, "Ia8", 172),
    (SIDE_IA, "Ia9", 120),
    (SIDE_IA, "Ia13", 120),
    (SIDE_IA, "Ia13", 140),
    (SIDE_IA, "Ia14", 98),
    (SIDE_IA, "Ia14", 141),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_N4 = STANDING_MATCHING_LEFTOVERS[0]
STANDING_LEFTOVER_N4_SITES = STANDING_WITH_ROWS[0][3]
STANDING_LEFTOVER_2GRAM_SITES = (
    (SIDE_IA, "Ia2", 11),
    (SIDE_IA, "Ia4", 113),
    (SIDE_IA, "Ia7", 69),
    (SIDE_IA, "Ia7", 130),
    (SIDE_IA, "Ia14", 141),
)
STANDING_N_INSIDE_LEFTOVER = 5
STANDING_EXTRA_I_SITES = (
    (SIDE_IA, "Ia1", 79),
    (SIDE_IA, "Ia1", 141),
    (SIDE_IA, "Ia2", 125),
    (SIDE_IA, "Ia3", 5),
    (SIDE_IA, "Ia3", 123),
    (SIDE_IA, "Ia5", 61),
    (SIDE_IA, "Ia6", 144),
    (SIDE_IA, "Ia7", 63),
    (SIDE_IA, "Ia8", 121),
    (SIDE_IA, "Ia8", 172),
    (SIDE_IA, "Ia9", 120),
    (SIDE_IA, "Ia13", 120),
    (SIDE_IA, "Ia13", 140),
    (SIDE_IA, "Ia14", 98),
)
STANDING_N_EXTRA = 14
STANDING_OFF_I_HITS = 5
STANDING_N_OFF_I = 5
STANDING_OFF_I_SITES = (
    (SIDE_GV, "Gv3", 33),
    (SIDE_GV, "Gv4", 1),
    (SIDE_SB, "Sb8", 17),
    (SIDE_TA, "Ta2", 10),
    (SIDE_TA, "Ta9", 3),
)
STANDING_OFF_I_TABLETS_WITH_HITS = ("G", "S", "T")
STANDING_OFF_I_BY_TABLET_NONZERO = {"G": 2, "S": 1, "T": 2}
STANDING_OFF_I_BY_TABLET = tuple(
    STANDING_OFF_I_BY_TABLET_NONZERO.get(tablet, 0) for tablet in OFF_I_TABLETS
)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS
    if tablet == "I"
    else STANDING_OFF_I_BY_TABLET_NONZERO.get(tablet, 0)
    for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_2gram_076_070_i_only"
STANDING_I_2GRAM_076_070_I_ONLY = False
STANDING_RESULT = "i_2gram_076_070_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = False
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE141_3GRAM = False
STANDING_SAME_AS_CYCLE160_3GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE171_2GRAM = False
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_SHARED_WITH_CYCLE166_FAMILY = (("999", "090", "076", "070"),)


def i_2gram_076_070_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


def leftover_contained_2gram_sites(
    leftover_n4_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_N4_SITES,
    offset: int = 2,
) -> tuple[tuple[str, str, int], ...]:
    """076 070 starts two tokens after leftover n=4 999 090 076 070."""
    return tuple((side, line, index + offset) for side, line, index in leftover_n4_sites)


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_2gram: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_2GRAM_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 076 070 sites that do not sit inside leftover n=4 999 090 076 070."""
    leftover_set = set(leftover_2gram)
    return tuple(site for site in i_sites if site not in leftover_set)


def named_off_i_sites(
    gram: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, str, int], ...]:
    """Named (side, line, index) hits on G, S, and T. Search only."""
    gk = load_g_k_sides()
    g_sites = nge8_sites(gram, gk)
    s_sites = nge6_sites(gram, load_s_sides())
    t = load_t_sides()
    t_sites = tuple(
        site_tuple(hit)
        for hit in named_side_hits(t[SIDE_TA], TA_LINE_NAMES, SIDE_TA, gram)
    )
    return g_sites + s_sites + t_sites


class TestI2gram076070IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-205 leftover 2-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 2-gram counts; a gap is not a hit. 076 071 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM2, CYCLE205_GRAM2)
        adjacent = [list(GRAM2), list(GRAM2)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM2), 2)
        overlap = [["076", "070", "076", "070"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM2), 2)
        gapped = [list(GRAM2[:1]) + ["006"] + list(GRAM2[1:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM2), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_071)], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM2), 0)
        self.assertEqual(ngram_hit_count([["076", "071"]], GRAM2), 0)
        self.assertEqual(ngram_hit_count([["076", "076"]], GRAM2), 0)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Measured 19/5 loses."""
        provider = MockProvider()
        self.assertTrue(i_2gram_076_070_i_only(1, 0))
        self.assertTrue(i_2gram_076_070_i_only(19, 0))
        self.assertFalse(i_2gram_076_070_i_only(19, 5))
        self.assertFalse(i_2gram_076_070_i_only(1, 1))
        self.assertFalse(i_2gram_076_070_i_only(0, 0))
        self.assertFalse(i_2gram_076_070_i_only(0, 5))
        self.assertEqual(STANDING_CLAIM, "i_2gram_076_070_i_only")
        self.assertFalse(STANDING_I_2GRAM_076_070_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertNotEqual(
            STANDING_I_2GRAM_076_070_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_2gram_is_cycle205_leftover_not_the_cycle_103_5gram(self):
        """2-gram is the cycle-205 leftover, not 076 071, 076 076, or the 3-grams."""
        provider = MockProvider()
        self.assertEqual(GRAM2, CYCLE205_GRAM2)
        self.assertNotEqual(GRAM2, ("076", "071"))
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
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N2, 2)
        self.assertLess(len(GRAM2), 8)
        for leftover in STANDING_MATCHING_LEFTOVERS:
            self.assertTrue(is_contiguous_substring(GRAM2, leftover))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_999_090_076_071))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertTrue(is_contiguous_substring(("076", "071"), NEAR_MISS_999_090_076_071))
        self.assertTrue(is_contiguous_substring(("076", "076"), NEAR_MISS_700_076_076_053))
        shared = set(STANDING_MATCHING_LEFTOVERS) & set(CYCLE166_MATCHING_LEFTOVERS)
        self.assertEqual(shared, set(STANDING_SHARED_WITH_CYCLE166_FAMILY))
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_vs_extra_split_can_fail(self):
        """Five I sites sit inside leftover n=4; the other 14 are extra."""
        provider = MockProvider()
        leftover_2gram = leftover_contained_2gram_sites()
        extra = extra_i_sites()
        self.assertEqual(leftover_2gram, STANDING_LEFTOVER_2GRAM_SITES)
        self.assertEqual(extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(leftover_2gram), STANDING_N_INSIDE_LEFTOVER)
        self.assertEqual(len(extra), STANDING_N_EXTRA)
        self.assertEqual(
            STANDING_N_INSIDE_LEFTOVER + STANDING_N_EXTRA,
            STANDING_N_I,
        )
        self.assertEqual(
            tuple(sorted(leftover_2gram + extra)),
            tuple(sorted(STANDING_I_SITES)),
        )
        planted = leftover_2gram + ((SIDE_IA, "Ia1", 0),)
        self.assertNotEqual(extra_i_sites(STANDING_I_SITES, planted), extra)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI2gram076070IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 2-gram 076 070 off-I lock. Mock only."""

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
        self.off_i_sites = named_off_i_sites(GRAM2)
        self.leftover_2gram = leftover_contained_2gram_sites()
        self.extra = extra_i_sites(self.i_sites, self.leftover_2gram)
        self.claim_holds = i_2gram_076_070_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_205_leftover_not_retuned(self):
        """2-gram is the cycle-205 leftover lock, not a new inventory."""
        self.assertEqual(GRAM2, CYCLE205_GRAM2)
        self.assertEqual(GRAM2, ("076", "070"))
        prior_205 = self.survey["i_leftover_n4_076_070"]
        self.assertEqual(prior_205["cycle"], 205)
        self.assertEqual(tuple(prior_205["tokens2"]), GRAM2)
        self.assertEqual(prior_205["N_with_076_070"], 1)
        self.assertEqual(prior_205["N_without_076_070"], 26)
        measured_matching = [list(gram) for gram in STANDING_MATCHING_LEFTOVERS]
        self.assertEqual(prior_205["matching_leftovers"], measured_matching)
        self.assertTrue(prior_205["i_leftover_n4_exactly_1_contain_076_070"])
        self.assertTrue(prior_205["076_071_does_not_count"])
        self.assertEqual(STANDING_LEFTOVER_N4, ("999", "090", "076", "070"))
        self.assertEqual(STANDING_LEFTOVER_N4_SITES, STANDING_WITH_ROWS[0][3])
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertNotEqual(GRAM2, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE160_GRAM3)
        self.assertNotEqual(GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_nineteen_on_ia(self):
        """2-gram is 19 on Ia; Ib unpublished 0. N_I must not drift."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 19)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 19)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 19)
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
            ((SIDE_IA, "Ia1", 79), (SIDE_IA, "Ia1", 141), (SIDE_IA, "Ia2", 11)),
        )
        self.assertEqual(
            STANDING_I_SITES[6],
            (SIDE_IA, "Ia4", 113),
        )
        self.assertEqual(
            STANDING_I_SITES[18],
            (SIDE_IA, "Ia14", 141),
        )
        self.assertFalse(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_vs_extra_on_i(self):
        """Five I sites sit inside leftover 999 090 076 070; 14 are extra."""
        self.assertEqual(self.leftover_2gram, STANDING_LEFTOVER_2GRAM_SITES)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.leftover_2gram), STANDING_N_INSIDE_LEFTOVER)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_INSIDE_LEFTOVER, 5)
        self.assertEqual(STANDING_N_EXTRA, 14)
        self.assertEqual(
            leftover_contained_2gram_sites(STANDING_LEFTOVER_N4_SITES),
            STANDING_LEFTOVER_2GRAM_SITES,
        )
        leftover_set = set(STANDING_LEFTOVER_2GRAM_SITES)
        for side, line, index in STANDING_LEFTOVER_N4_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), STANDING_LEFTOVER_N4)
            self.assertIn((side, line, index + 2), leftover_set)
        for site in STANDING_LEFTOVER_2GRAM_SITES:
            self.assertIn(site, STANDING_I_SITES)
        for site in STANDING_EXTRA_I_SITES:
            self.assertIn(site, STANDING_I_SITES)
            self.assertNotIn(site, leftover_set)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_2gram_is_five_off_i_and_not_i_only(self):
        """2-gram is 5 off-I (G 2, S 1, T 2). Ia has exactly 19. Claim loses."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, STANDING_N_OFF_I)
        self.assertEqual(STANDING_N_OFF_I, 5)
        self.assertNotEqual(STANDING_N_OFF_I, 0)
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(len(STANDING_OFF_I_SITES), STANDING_N_OFF_I)
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ("G", "S", "T"))
        self.assertEqual(STANDING_OFF_I_BY_TABLET_NONZERO, {"G": 2, "S": 1, "T": 2})
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM2))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 19)
            elif tablet in STANDING_OFF_I_BY_TABLET_NONZERO:
                self.assertEqual(count, STANDING_OFF_I_BY_TABLET_NONZERO[tablet])
            else:
                self.assertEqual(count, 0)
        gk = load_g_k_sides()
        self.assertEqual(ngram_hit_count(gk[SIDE_GR], GRAM2), 0)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], GRAM2), 2)
        s_sides = load_s_sides()
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], GRAM2), 0)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], GRAM2), 1)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM2), 2)
        for side, line, index in STANDING_OFF_I_SITES:
            if side == SIDE_GV:
                stems = gk[side][GV_LINE_NAMES.index(line)][index : index + STANDING_N2]
            elif side == SIDE_SB:
                stems = s_sides[side][SB_LINE_NAMES.index(line)][index : index + STANDING_N2]
            else:
                stems = t_sides[side][TA_LINE_NAMES.index(line)][index : index + STANDING_N2]
            self.assertEqual(tuple(stems), GRAM2)
        self.assertEqual(
            i_2gram_076_070_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_2GRAM_076_070_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_2GRAM_076_070_I_ONLY,
        )
        self.assertFalse(self.claim_holds)
        self.assertFalse(STANDING_I_2GRAM_076_070_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_2gram_076_070_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE141_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE160_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_205_171_170_166_and_w_scoreboards_still_compute(self):
        """Cycle 205 leftover-1, 171 I-only 43/0, 170 leftover-4, 166 leftover-7 stay."""
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_166 = TestMamariILeftoverN4999090076Scoreboard()
        prior_166.setUp()
        prior_166.test_counts_7_of_27_and_hypothesis_n_7_holds()
        prior_166.test_survey_matches_computed_lock()
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_160 = TestMamariIOverlap3gram076020010IOnlyScoreboard()
        prior_160.setUp()
        prior_160.test_3gram_is_zero_off_i_and_i_only()
        prior_141 = TestMamariIOverlap3gram076010079IOnlyScoreboard()
        prior_141.setUp()
        prior_141.test_3gram_is_zero_off_i_and_i_only()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-206 2-gram I-only loss."""
        lock = self.survey["i_2gram_076_070_i_only"]
        self.assertEqual(lock["cycle"], 206)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 19)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_sites"]),
            STANDING_LEFTOVER_N4_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_2gram_sites"]),
            STANDING_LEFTOVER_2GRAM_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertEqual(lock["N_inside_leftover"], STANDING_N_INSIDE_LEFTOVER)
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(tuple(lock["leftover_n4"]), STANDING_LEFTOVER_N4)
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(lock["N_off_I"], 5)
        self.assertEqual(
            tuple(tuple(row) for row in lock["off_i_sites"]),
            STANDING_OFF_I_SITES,
        )
        self.assertEqual(tuple(lock["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(lock["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(
            tuple(lock["off_i_tablets_with_hits"]),
            STANDING_OFF_I_TABLETS_WITH_HITS,
        )
        self.assertEqual(
            lock["off_i_by_tablet_nonzero"],
            STANDING_OFF_I_BY_TABLET_NONZERO,
        )
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_2gram_076_070_i_only"])
        self.assertEqual(
            lock["i_2gram_076_070_i_only"],
            STANDING_I_2GRAM_076_070_I_ONLY,
        )
        self.assertFalse(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle141_3gram"])
        self.assertFalse(lock["same_as_cycle160_3gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle171_2gram"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_999_090_076_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_020_010_i_only_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"][
                "i_leftover_n4_exactly_1_contain_076_070"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["N_with_076_070"], 1)
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["N_without_076_070"], 26)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"]["i_leftover_n4_exactly_4_contain_076_071"]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["N_with_076_071"], 4)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["N_without_076_071"], 23)
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
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(
            self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
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


class TestMamariI2gram076070IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 206 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
