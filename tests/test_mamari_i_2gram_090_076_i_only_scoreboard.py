"""I's cycle-222 leftover remaining 2-gram 090 076 off-I lock.

Cycle 223 text-search lock. Uses already-vendored A–V and the
cycle-222 leftover remaining 2-gram 090 076 (G of leftover n=4
remaining; K=5 of N_remaining=16). Does not retune that 2-gram
or the leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished Ib
is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Same claim-shape as cycle 171 (076 071 was I-only 43/0),
cycle 167 (999 090 076 was I-only 16/0), cycle 206 (076 070
lost 19/5), and cycle 207 (090 076 070 lost 8/1). Cycle 52
already locked 69 on Ia among eight early fixtures; this
cycle is the dedicated A–V lock. This cycle is the new
leftover remaining 2-gram 090 076 only. 090 076 070 is a
different 3-gram (already lost 8/1). 090 076 071 is a
different 3-gram (already I-only 6/0). 999 090 076 is a
different 3-gram (already I-only 16/0). 076 070 is a
different 2-gram (already lost 19/5). Do not retune leftover
n=4, 076-cells, or any detector. Do not lock I-only of
leftover 4-grams this cycle. Do not assume the I-only result.

Locks exact consecutive hits of 090 076 on tablet I and on
every other vendored tablet A–H and J–V. Claim that can lose:
i_2gram_090_076_i_only (I hits ≥ 1 and off-I hits == 0).
True only if N_off_I == 0. Measured: Ia is exactly 69; Ib
unpublished 0; off-I is 3 on T (Ta5[9], Ta7[5], Ta9[2]).
Ta9[2] is the cycle-207 3-gram 090 076 070 leak (still 8/1;
do not retune). Ta5[9] 090 076 010 and Ta7[5] 090 076 126
are extra T leaks, not that 3-gram. The claim is false. Not
an n≥8 island. Not the cycle-103 I 5-gram. Nested cycle 222
leftover remaining K=5 / G=090 076 / N_remaining=16, cycle
207 8/1, cycle 167 16/0, and cycle 171 43/0 stay.

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
from tests.test_mamari_i_2gram_076_070_i_only_scoreboard import (
    GRAM2 as CYCLE206_GRAM2,
    STANDING_N_I as CYCLE206_N_I,
    STANDING_N_OFF_I as CYCLE206_N_OFF_I,
    TestMamariI2gram076070IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
    i_3gram_090_076_070_i_only,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
    TestMamariI3gram090076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE222_MATCHING,
    STANDING_N_REMAINING as CYCLE222_N_REMAINING,
    TestMamariILeftoverN4RemainingNext2gramScoreboard,
    i_leftover_n4_remaining_exactly_5_contain_090_076,
    leftover_n4_family_counts_hold,
    leftover_n4_rows,
    leftover_remaining_n4,
    leftover_remaining_with_g,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
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
    GRAM_090_076,
    STANDING_090_076_HITS,
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
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
    load_g_k_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    SIDE_SA,
    SIDE_SB,
    load_s_sides,
)

HYPOTHESIS_I_ONLY = True
GRAM2 = CYCLE222_GRAM2
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_090_076_071 = CYCLE195_GRAM3
NEAR_MISS_999_090_076 = CYCLE167_GRAM3
NEAR_MISS_076_070 = CYCLE206_GRAM2
NEAR_MISS_076_071 = CYCLE171_GRAM2
STANDING_N2 = 2
STANDING_I_HITS = 69
STANDING_IA_HITS = 69
STANDING_IB_HITS = 0
STANDING_N_ON_I = 69
STANDING_N_I = 69
STANDING_I_SITES = (
    (SIDE_IA, "Ia1", 2),
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 10),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 37),
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia2", 114),
    (SIDE_IA, "Ia2", 119),
    (SIDE_IA, "Ia2", 128),
    (SIDE_IA, "Ia2", 154),
    (SIDE_IA, "Ia2", 159),
    (SIDE_IA, "Ia2", 165),
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia3", 4),
    (SIDE_IA, "Ia3", 37),
    (SIDE_IA, "Ia3", 71),
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 86),
    (SIDE_IA, "Ia4", 112),
    (SIDE_IA, "Ia4", 117),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia4", 134),
    (SIDE_IA, "Ia4", 154),
    (SIDE_IA, "Ia4", 162),
    (SIDE_IA, "Ia4", 166),
    (SIDE_IA, "Ia5", 2),
    (SIDE_IA, "Ia5", 6),
    (SIDE_IA, "Ia5", 23),
    (SIDE_IA, "Ia5", 28),
    (SIDE_IA, "Ia5", 66),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia5", 143),
    (SIDE_IA, "Ia5", 164),
    (SIDE_IA, "Ia6", 78),
    (SIDE_IA, "Ia6", 92),
    (SIDE_IA, "Ia6", 134),
    (SIDE_IA, "Ia7", 2),
    (SIDE_IA, "Ia7", 68),
    (SIDE_IA, "Ia7", 88),
    (SIDE_IA, "Ia7", 113),
    (SIDE_IA, "Ia7", 129),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia8", 120),
    (SIDE_IA, "Ia9", 28),
    (SIDE_IA, "Ia9", 129),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia10", 141),
    (SIDE_IA, "Ia12", 42),
    (SIDE_IA, "Ia12", 47),
    (SIDE_IA, "Ia12", 83),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 17),
    (SIDE_IA, "Ia13", 67),
    (SIDE_IA, "Ia13", 109),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia13", 143),
    (SIDE_IA, "Ia13", 152),
    (SIDE_IA, "Ia14", 9),
    (SIDE_IA, "Ia14", 54),
    (SIDE_IA, "Ia14", 97),
    (SIDE_IA, "Ia14", 105),
    (SIDE_IA, "Ia14", 140),
    (SIDE_IA, "Ia14", 177),
)
STANDING_IB_SITES = ()
STANDING_OFF_I_HITS = 3
STANDING_N_OFF_I = 3
STANDING_OFF_I_SITES = (
    (SIDE_TA, "Ta5", 9),
    (SIDE_TA, "Ta7", 5),
    (SIDE_TA, "Ta9", 2),
)
STANDING_OFF_I_PREVIOUS_4GRAMS = (
    ("090", "090", "076", "010"),
    ("076", "090", "076", "126"),
    ("059", "090", "076", "070"),
)
STANDING_OFF_I_FOLLOWING_3GRAMS = (
    ("090", "076", "010"),
    ("090", "076", "126"),
    ("090", "076", "070"),
)
STANDING_CYCLE207_OFF_I_SITE = (SIDE_TA, "Ta9", 2)
STANDING_N_OFF_I_FROM_CYCLE207 = 1
STANDING_N_OFF_I_EXTRA = 2
STANDING_OFF_I_TABLETS_WITH_HITS = ("T",)
STANDING_OFF_I_BY_TABLET_NONZERO = {"T": 3}
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
STANDING_CLAIM = "i_2gram_090_076_i_only"
STANDING_I_2GRAM_090_076_I_ONLY = False
STANDING_RESULT = "i_2gram_090_076_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = False
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE171_2GRAM = False
STANDING_SAME_AS_CYCLE195_3GRAM = False
STANDING_SAME_AS_CYCLE206_2GRAM = False
STANDING_SAME_AS_CYCLE207_3GRAM = False
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_999_090_076_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_CYCLE52_IA_HITS = 69


def i_2gram_090_076_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


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


class TestI2gram090076IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-222 leftover remaining 2-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 2-gram counts; a gap is not a hit. Longer 3-grams are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM2, GRAM_090_076)
        adjacent = [list(GRAM2), list(GRAM2)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM2), 2)
        overlap = [["090", "076", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM2), 2)
        gapped = [list(GRAM2[:1]) + ["006"] + list(GRAM2[1:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM2), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_070)], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_071)], GRAM2), 0)
        self.assertEqual(ngram_hit_count([["076", "090"]], GRAM2), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM2), 1)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_071)], GRAM2), 1)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076)], GRAM2), 1)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Measured 69/3 loses."""
        provider = MockProvider()
        self.assertTrue(i_2gram_090_076_i_only(1, 0))
        self.assertTrue(i_2gram_090_076_i_only(69, 0))
        self.assertFalse(i_2gram_090_076_i_only(69, 3))
        self.assertFalse(i_2gram_090_076_i_only(1, 1))
        self.assertFalse(i_2gram_090_076_i_only(0, 0))
        self.assertFalse(i_2gram_090_076_i_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "i_2gram_090_076_i_only")
        self.assertFalse(STANDING_I_2GRAM_090_076_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertNotEqual(
            STANDING_I_2GRAM_090_076_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_2gram_is_cycle222_g_not_the_cycle_103_5gram(self):
        """2-gram is cycle-222 G, not 090 076 070, 076 071, or the 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertNotEqual(GRAM2, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE206_GRAM2)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM2, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N2, 2)
        self.assertLess(len(GRAM2), 8)
        for leftover in CYCLE222_MATCHING:
            self.assertTrue(is_contiguous_substring(GRAM2, leftover))
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_090_076_070))
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_090_076_071))
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_999_090_076))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_076_070))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_076_071))
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI2gram090076IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover remaining 2-gram 090 076 off-I lock. Mock only."""

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
        self.claim_holds = i_2gram_090_076_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_222_g_not_retuned(self):
        """2-gram is the cycle-222 leftover remaining G, not a new inventory."""
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertEqual(tuple(prior_222["tokens2"]), GRAM2)
        self.assertEqual(tuple(prior_222["G"]), CYCLE222_G)
        self.assertEqual(prior_222["K"], CYCLE222_K)
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(prior_222["N_remaining"], CYCLE222_N_REMAINING)
        self.assertEqual(prior_222["N_remaining"], 16)
        measured_matching = [list(gram) for gram in CYCLE222_MATCHING]
        self.assertEqual(prior_222["matching_leftovers"], measured_matching)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertTrue(prior_222["i_vs_off_i_is_not_this_cycle"])
        self.assertNotIn("N_I", prior_222)
        self.assertNotIn("N_off_I", prior_222)
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertNotEqual(GRAM2, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertFalse(is_contiguous_substring(GRAM2, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(STANDING_I_HITS, STANDING_090_076_HITS[-1])
        self.assertEqual(STANDING_090_076_HITS[-1], STANDING_CYCLE52_IA_HITS)
        self.assertEqual(STANDING_CYCLE52_IA_HITS, 69)
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_sixty_nine_on_ia(self):
        """2-gram is 69 on Ia; Ib unpublished 0. N_I must not drift."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 69)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 69)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM2, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM2), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N2]
            self.assertEqual(tuple(stems), GRAM2)
            self.assertEqual(side, SIDE_IA)
            self.assertNotEqual(line[:2], "Ib")
        self.assertEqual(
            STANDING_I_SITES[:3],
            ((SIDE_IA, "Ia1", 2), (SIDE_IA, "Ia1", 15), (SIDE_IA, "Ia1", 27)),
        )
        self.assertEqual(
            STANDING_I_SITES[5],
            (SIDE_IA, "Ia2", 10),
        )
        self.assertEqual(
            STANDING_I_SITES[68],
            (SIDE_IA, "Ia14", 177),
        )
        for site in CYCLE207_I_SITES:
            self.assertIn(site, STANDING_I_SITES)
        self.assertFalse(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_2gram_is_three_off_i_and_not_i_only(self):
        """2-gram is 3 off-I (T Ta5[9]/Ta7[5]/Ta9[2]). Ia has exactly 69. Claim loses."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, STANDING_N_OFF_I)
        self.assertEqual(STANDING_N_OFF_I, 3)
        self.assertNotEqual(STANDING_N_OFF_I, 0)
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(len(STANDING_OFF_I_SITES), STANDING_N_OFF_I)
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ("T",))
        self.assertEqual(STANDING_OFF_I_BY_TABLET_NONZERO, {"T": 3})
        self.assertEqual(STANDING_N_OFF_I_FROM_CYCLE207 + STANDING_N_OFF_I_EXTRA, 3)
        self.assertIn(STANDING_CYCLE207_OFF_I_SITE, STANDING_OFF_I_SITES)
        self.assertEqual(CYCLE207_OFF_I_SITES, (STANDING_CYCLE207_OFF_I_SITE,))
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM2))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 69)
            elif tablet in STANDING_OFF_I_BY_TABLET_NONZERO:
                self.assertEqual(count, STANDING_OFF_I_BY_TABLET_NONZERO[tablet])
            else:
                self.assertEqual(count, 0)
        gk = load_g_k_sides()
        self.assertEqual(ngram_hit_count(gk[SIDE_GR], GRAM2), 0)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], GRAM2), 0)
        s_sides = load_s_sides()
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], GRAM2), 0)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], GRAM2), 0)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM2), 3)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE207_GRAM3), 1)
        for (side, line, index), prev4, follow3 in zip(
            STANDING_OFF_I_SITES,
            STANDING_OFF_I_PREVIOUS_4GRAMS,
            STANDING_OFF_I_FOLLOWING_3GRAMS,
            strict=True,
        ):
            stems = t_sides[side][TA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N2]), prev4)
            self.assertEqual(tuple(stems[index : index + 3]), follow3)
        self.assertEqual(
            STANDING_OFF_I_FOLLOWING_3GRAMS[2],
            CYCLE207_GRAM3,
        )
        self.assertNotEqual(STANDING_OFF_I_FOLLOWING_3GRAMS[0], CYCLE207_GRAM3)
        self.assertNotEqual(STANDING_OFF_I_FOLLOWING_3GRAMS[1], CYCLE207_GRAM3)
        self.assertEqual(
            i_2gram_090_076_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_2GRAM_090_076_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_2GRAM_090_076_I_ONLY,
        )
        self.assertFalse(self.claim_holds)
        self.assertFalse(STANDING_I_2GRAM_090_076_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_2gram_090_076_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertTrue(STANDING_LEFTOVER_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_222_207_171_and_167_scoreboards_still_compute(self):
        """Cycle 222 K=5 / G=090 076, 207 8/1, 171 43/0, 167 16/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        self.assertTrue(CYCLE222_CLAIM)
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertEqual(prior_207.off_i_sites, CYCLE207_OFF_I_SITES)
        self.assertFalse(prior_207.claim_holds)
        self.assertFalse(i_3gram_090_076_070_i_only(8, 1))
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE167_N_I, 16)
        self.assertEqual(CYCLE167_N_OFF_I, 0)
        self.assertEqual(CYCLE167_GRAM3, ("999", "090", "076"))
        if CYCLE167_N_I != 16 or CYCLE167_N_OFF_I != 0:
            self.fail("nested cycle 167 16/0 drifted")
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_195 = TestMamariI3gram090076071IOnlyScoreboard()
        prior_195.setUp()
        prior_195.test_3gram_is_zero_off_i_and_i_only()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-223 2-gram I-only loss."""
        lock = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(lock["cycle"], 223)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(lock["N_off_I"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in lock["off_i_sites"]),
            STANDING_OFF_I_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["off_i_previous_4grams"]),
            STANDING_OFF_I_PREVIOUS_4GRAMS,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["off_i_following_3grams"]),
            STANDING_OFF_I_FOLLOWING_3GRAMS,
        )
        self.assertEqual(
            tuple(lock["cycle207_off_i_site"]),
            STANDING_CYCLE207_OFF_I_SITE,
        )
        self.assertEqual(lock["N_off_I_from_cycle207"], STANDING_N_OFF_I_FROM_CYCLE207)
        self.assertEqual(lock["N_off_I_extra"], STANDING_N_OFF_I_EXTRA)
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
        self.assertFalse(lock["i_2gram_090_076_i_only"])
        self.assertEqual(
            lock["i_2gram_090_076_i_only"],
            STANDING_I_2GRAM_090_076_I_ONLY,
        )
        self.assertFalse(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle171_2gram"])
        self.assertFalse(lock["same_as_cycle195_3gram"])
        self.assertFalse(lock["same_as_cycle206_2gram"])
        self.assertFalse(lock["same_as_cycle207_3gram"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["999_090_076_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["leftover_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertEqual(tuple(prior_222["G"]), ("090", "076"))
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(prior_222["N_remaining"], 16)
        self.assertTrue(prior_222["i_vs_off_i_is_not_this_cycle"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], CYCLE207_N_I)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], CYCLE207_N_OFF_I)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in self.survey["i_3gram_090_076_070_i_only"]["off_i_sites"]),
            CYCLE207_OFF_I_SITES,
        )
        self.assertEqual(tuple(self.survey["i_3gram_090_076_070_i_only"]["tokens3"]), CYCLE207_GRAM3)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], CYCLE206_N_I)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], CYCLE206_N_OFF_I)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(
            self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["cycle"], 195)
        self.assertTrue(
            self.survey["i_3gram_090_076_071_i_only"]["i_3gram_090_076_071_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_off_I"], 0)
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


class TestMamariI2gram090076IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 223 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
