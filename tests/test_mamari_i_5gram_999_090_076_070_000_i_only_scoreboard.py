"""I's leftover 5-gram 999 090 076 070 000 off-I lock.

Cycle 220 text-search lock. Uses already-vendored A–V and the
cycle-208 leftover 4-gram 999 090 076 070 plus the cycle-219
leak site Ia14[140] / leftover site Ia14[139]. Does not
retune that 5-gram, the leftover n=4 set, or the cycle-219
forward-4 inventory. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished Ib
is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Same claim-shape as cycle 208 (999 090 076 070 was I-only
5/0 vs 090 076 070 leaking 8/1). Cycle 219 lost: I
090 076 070 forward 4-grams I-only 7/8; leak
090 076 070 000 on T Ta9[2]. Cycle 207 lost: 090 076 070
I-only 8/1 on T. Cycle 206 lost: 076 070 I-only 19/5.
Cycle 171 holds: 076 071 I-only 43/0. This cycle is the
leftover 5-gram 999 090 076 070 000 only.
090 076 070 000 without leading 999 does not count as this
5-gram (the T leak is 059 090 076 070 000, a different
5-gram). 999 090 076 070 without trailing 000 is a
different 4-gram. Do not retune the leftover n=4 set. Do
not assume the I-only result.

Locks exact consecutive hits of 999 090 076 070 000 on
tablet I and on every other vendored tablet A–H and J–V.
Claim that can lose: i_5gram_999_090_076_070_000_i_only
(I hits ≥ 1 and off-I hits == 0). True only if N_off_I == 0
and N_I >= 1. Measured: Ia is exactly 1 at Ia14[139]; Ib
unpublished 0; off-I is 0. The one I site sits inside
leftover n=4 999 090 076 070; extra is 0. The claim is
true. Not an n≥8 island. Not the cycle-103 I 5-gram.

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
    STANDING_I_3GRAM_090_076_070_I_ONLY as CYCLE207_I_ONLY,
    STANDING_LEFTOVER_3GRAM_SITES as CYCLE207_LEFTOVER_3GRAM_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_PREVIOUS_4GRAM as CYCLE207_OFF_I_PREVIOUS_4GRAM,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
    leftover_contained_3gram_sites as cycle207_leftover_3gram_sites,
    named_off_i_sites as cycle207_named_off_i_sites,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
)
from tests.test_mamari_i_4gram_999_090_076_070_i_only_scoreboard import (
    GRAM4 as CYCLE208_GRAM4,
    STANDING_I_4GRAM_999_090_076_070_I_ONLY as CYCLE208_I_ONLY,
    STANDING_I_SITES as CYCLE208_I_SITES,
    STANDING_LEFTOVER_4GRAM_SITES as CYCLE208_LEFTOVER_4GRAM_SITES,
    STANDING_N_I as CYCLE208_N_I,
    STANDING_N_OFF_I as CYCLE208_N_OFF_I,
    TestMamariI4gram999090076070IOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_I_ONLY,
    STANDING_N_I_EACH as CYCLE219_N_I_EACH,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_N_OFF_I_EACH as CYCLE219_N_OFF_I_EACH,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
    STANDING_OFF_I_SITES_000 as CYCLE219_OFF_I_SITES,
    TestMamariI090076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    GRAM2 as CYCLE205_GRAM2,
    NEAR_MISS_700_076_076_053,
    NEAR_MISS_999_090_076_071,
    STANDING_MATCHING_LEFTOVERS,
    STANDING_WITH_ROWS,
    TestMamariILeftoverN4076070Scoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5 as CYCLE103_GRAM5,
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
GRAM5 = ("999", "090", "076", "070", "000")
NEAR_MISS_090_076_070_000 = CYCLE219_LEAK_4GRAM
NEAR_MISS_999_090_076_070 = CYCLE208_GRAM4
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_076_070 = CYCLE206_GRAM2
NEAR_MISS_999_090_076 = CYCLE167_GRAM3
NEAR_MISS_059_090_076_070 = CYCLE207_OFF_I_PREVIOUS_4GRAM
NEAR_MISS_059_090_076_070_000 = ("059", "090", "076", "070", "000")
NEAR_MISS_999_090_076_070_499 = ("999", "090", "076", "070", "499")
NEAR_MISS_999_090_076_070_600 = ("999", "090", "076", "070", "600")
NEAR_MISS_999_090_076_070_027 = ("999", "090", "076", "070", "027")
NEAR_MISS_999_090_076_070_532 = ("999", "090", "076", "070", "532")
STANDING_N5 = 5
STANDING_I_HITS = 1
STANDING_IA_HITS = 1
STANDING_IB_HITS = 0
STANDING_N_ON_I = 1
STANDING_N_I = 1
STANDING_I_SITES = ((SIDE_IA, "Ia14", 139),)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_N4 = STANDING_MATCHING_LEFTOVERS[0]
STANDING_LEFTOVER_N4_SITES = STANDING_WITH_ROWS[0][3]
STANDING_LEFTOVER_NEXT_STEMS = ("499", "600", "027", "532", "000")
STANDING_LEFTOVER_5GRAM_SITES = ((SIDE_IA, "Ia14", 139),)
STANDING_N_INSIDE_LEFTOVER = 1
STANDING_EXTRA_I_SITES = ()
STANDING_N_EXTRA = 0
STANDING_OFF_I_HITS = 0
STANDING_N_OFF_I = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_OFF_I_BY_TABLET_NONZERO = {}
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
STANDING_CLAIM = "i_5gram_999_090_076_070_000_i_only"
STANDING_I_5GRAM_999_090_076_070_000_I_ONLY = True
STANDING_RESULT = "i_5gram_999_090_076_070_000_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE208_4GRAM = False
STANDING_SAME_AS_CYCLE219_LEAK_4GRAM = False
STANDING_SAME_AS_CYCLE207_3GRAM = False
STANDING_SAME_AS_CYCLE206_2GRAM = False
STANDING_SAME_AS_CYCLE171_2GRAM = False
STANDING_090_076_070_000_WITHOUT_999_DOES_NOT_COUNT = True
STANDING_999_090_076_070_WITHOUT_000_DOES_NOT_COUNT = True
STANDING_059_090_076_070_000_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def i_5gram_999_090_076_070_000_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


def leftover_contained_5gram_sites(
    leftover_n4_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_N4_SITES,
    i_sides: dict[str, list[list[str]]] | None = None,
    gram5: tuple[str, ...] = GRAM5,
) -> tuple[tuple[str, str, int], ...]:
    """5-gram starts at leftover n=4 999 090 076 070 only when next is 000."""
    sides = i_sides if i_sides is not None else load_i_sides()
    hits = []
    for side, line, index in leftover_n4_sites:
        stems = sides[side][IA_LINE_NAMES.index(line)]
        if tuple(stems[index : index + len(gram5)]) == gram5:
            hits.append((side, line, index))
    return tuple(hits)


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_5gram: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_5GRAM_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 999 090 076 070 000 sites that are not leftover n=4 + trailing 000."""
    leftover_set = set(leftover_5gram)
    return tuple(site for site in i_sites if site not in leftover_set)


class TestI5gram999090076070000IOnlyHelpers(unittest.TestCase):
    """Helpers on leftover 5-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 5-gram counts; a gap is not a hit. Near-miss grams are not."""
        provider = MockProvider()
        self.assertEqual(GRAM5, ("999", "090", "076", "070", "000"))
        adjacent = [list(GRAM5), list(GRAM5)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM5), 2)
        overlap = [["999", "090", "076", "070", "000", "999", "090", "076", "070", "000"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM5), 2)
        gapped = [list(GRAM5[:2]) + ["006"] + list(GRAM5[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM5), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070_000)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_070)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_070)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_071)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_059_090_076_070)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_059_090_076_070_000)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_070_499)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_070_600)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_070_027)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_070_532)], GRAM5), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE103_GRAM5)], GRAM5), 0)
        self.assertTrue(STANDING_090_076_070_000_WITHOUT_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_070_WITHOUT_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_059_090_076_070_000_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Measured 1/0 holds."""
        provider = MockProvider()
        self.assertTrue(i_5gram_999_090_076_070_000_i_only(1, 0))
        self.assertTrue(i_5gram_999_090_076_070_000_i_only(2, 0))
        self.assertFalse(i_5gram_999_090_076_070_000_i_only(1, 1))
        self.assertFalse(i_5gram_999_090_076_070_000_i_only(5, 1))
        self.assertFalse(i_5gram_999_090_076_070_000_i_only(0, 0))
        self.assertFalse(i_5gram_999_090_076_070_000_i_only(0, 1))
        self.assertEqual(STANDING_CLAIM, "i_5gram_999_090_076_070_000_i_only")
        self.assertTrue(STANDING_I_5GRAM_999_090_076_070_000_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(
            STANDING_I_5GRAM_999_090_076_070_000_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_5gram_is_leftover_plus_000_not_the_cycle_103_5gram(self):
        """5-gram is leftover 4-gram + 000, not the T leak or cycle-103 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM5, ("999", "090", "076", "070", "000"))
        self.assertEqual(GRAM5[:4], STANDING_LEFTOVER_N4)
        self.assertEqual(GRAM5[:4], CYCLE208_GRAM4)
        self.assertEqual(GRAM5[1:], NEAR_MISS_090_076_070_000)
        self.assertNotEqual(GRAM5, CYCLE103_GRAM5)
        self.assertNotEqual(GRAM5, CYCLE208_GRAM4)
        self.assertNotEqual(GRAM5, CYCLE219_LEAK_4GRAM)
        self.assertNotEqual(GRAM5, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM5, CYCLE206_GRAM2)
        self.assertNotEqual(GRAM5, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM5, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM5, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM5, NEAR_MISS_059_090_076_070_000)
        self.assertNotEqual(GRAM5, NEAR_MISS_999_090_076_071)
        self.assertEqual(CYCLE103_GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM5, CYCLE103_GRAM5))
        self.assertFalse(is_contiguous_substring(CYCLE103_GRAM5, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE208_4GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219_LEAK_4GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertEqual(len(GRAM5), STANDING_N5)
        self.assertEqual(STANDING_N5, 5)
        self.assertLess(len(GRAM5), 8)
        for leftover in STANDING_MATCHING_LEFTOVERS:
            self.assertTrue(is_contiguous_substring(leftover, GRAM5))
            self.assertEqual(leftover, CYCLE208_GRAM4)
        self.assertTrue(is_contiguous_substring(CYCLE208_GRAM4, GRAM5))
        self.assertTrue(is_contiguous_substring(CYCLE207_GRAM3, GRAM5))
        self.assertTrue(is_contiguous_substring(CYCLE206_GRAM2, GRAM5))
        self.assertTrue(is_contiguous_substring(CYCLE167_GRAM3, GRAM5))
        self.assertTrue(is_contiguous_substring(CYCLE219_LEAK_4GRAM, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM5, CYCLE208_GRAM4))
        self.assertFalse(is_contiguous_substring(NEAR_MISS_059_090_076_070_000, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM5, NEAR_MISS_059_090_076_070_000))
        self.assertEqual(GRAM5[1:4], CYCLE207_GRAM3)
        self.assertEqual(GRAM5[2:4], CYCLE206_GRAM2)
        self.assertEqual(GRAM5[:3], CYCLE167_GRAM3)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_vs_extra_split_can_fail(self):
        """The one I site sits inside leftover n=4 + 000; extra is 0."""
        provider = MockProvider()
        leftover_5gram = leftover_contained_5gram_sites()
        extra = extra_i_sites()
        self.assertEqual(leftover_5gram, STANDING_LEFTOVER_5GRAM_SITES)
        self.assertEqual(extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(leftover_5gram), STANDING_N_INSIDE_LEFTOVER)
        self.assertEqual(len(extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(
            STANDING_N_INSIDE_LEFTOVER + STANDING_N_EXTRA,
            STANDING_N_I,
        )
        self.assertEqual(
            tuple(sorted(leftover_5gram + extra)),
            tuple(sorted(STANDING_I_SITES)),
        )
        planted = extra_i_sites(STANDING_I_SITES, ())
        self.assertNotEqual(planted, extra)
        self.assertEqual(len(planted), STANDING_N_I)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI5gram999090076070000IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 5-gram 999 090 076 070 000 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM5, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM5)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM5, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM5, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.off_i_sites = cycle207_named_off_i_sites(GRAM5)
        self.leftover_5gram = leftover_contained_5gram_sites(
            STANDING_LEFTOVER_N4_SITES,
            self.i_sides,
        )
        self.extra = extra_i_sites(self.i_sites, self.leftover_5gram)
        self.claim_holds = i_5gram_999_090_076_070_000_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_leftover_plus_000_not_retuned(self):
        """5-gram is leftover 4-gram + 000, not a new inventory."""
        self.assertEqual(GRAM5, ("999", "090", "076", "070", "000"))
        self.assertEqual(GRAM5[:4], STANDING_LEFTOVER_N4)
        prior_208 = self.survey["i_4gram_999_090_076_070_i_only"]
        self.assertEqual(prior_208["cycle"], 208)
        self.assertEqual(tuple(prior_208["tokens4"]), CYCLE208_GRAM4)
        self.assertEqual(prior_208["N_I"], CYCLE208_N_I)
        self.assertEqual(prior_208["N_I"], 5)
        self.assertEqual(prior_208["N_off_I"], CYCLE208_N_OFF_I)
        self.assertEqual(prior_208["N_off_I"], 0)
        self.assertTrue(prior_208["i_4gram_999_090_076_070_i_only"])
        prior_205 = self.survey["i_leftover_n4_076_070"]
        self.assertEqual(prior_205["cycle"], 205)
        self.assertEqual(prior_205["N_with_076_070"], 1)
        self.assertEqual(prior_205["N_without_076_070"], 26)
        measured_matching = [list(gram) for gram in STANDING_MATCHING_LEFTOVERS]
        self.assertEqual(prior_205["matching_leftovers"], measured_matching)
        self.assertTrue(prior_205["i_leftover_n4_exactly_1_contain_076_070"])
        self.assertEqual(STANDING_LEFTOVER_N4, ("999", "090", "076", "070"))
        self.assertEqual(STANDING_LEFTOVER_N4_SITES, STANDING_WITH_ROWS[0][3])
        self.assertEqual(STANDING_LEFTOVER_N4_SITES, CYCLE208_I_SITES)
        self.assertEqual(STANDING_LEFTOVER_N4_SITES, CYCLE208_LEFTOVER_4GRAM_SITES)
        self.assertNotEqual(GRAM5, CYCLE103_GRAM5)
        self.assertNotEqual(GRAM5, CYCLE208_GRAM4)
        self.assertNotEqual(GRAM5, CYCLE219_LEAK_4GRAM)
        self.assertNotEqual(GRAM5, CYCLE207_GRAM3)
        self.assertFalse(is_contiguous_substring(GRAM5, CYCLE103_GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_one_on_ia14(self):
        """5-gram is 1 on Ia14[139]; Ib unpublished 0. N_I must not drift."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 1)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 1)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 1)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        if self.i_hits != STANDING_N_I:
            self.fail("measured N_I drifted from the locked 1")
        self.assertEqual(nge4_sites(GRAM5, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM5), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N5]), GRAM5)
            self.assertEqual(tuple(stems[index : index + 4]), CYCLE208_GRAM4)
            self.assertEqual(tuple(stems[index + 1 : index + 5]), CYCLE219_LEAK_4GRAM)
            self.assertEqual(side, SIDE_IA)
        self.assertEqual(STANDING_I_SITES[0], (SIDE_IA, "Ia14", 139))
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_vs_extra_on_i(self):
        """The one I site sits inside leftover 999 090 076 070 000; extra is 0."""
        self.assertEqual(self.leftover_5gram, STANDING_LEFTOVER_5GRAM_SITES)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.leftover_5gram), STANDING_N_INSIDE_LEFTOVER)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_INSIDE_LEFTOVER, 1)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(
            leftover_contained_5gram_sites(STANDING_LEFTOVER_N4_SITES, self.i_sides),
            STANDING_LEFTOVER_5GRAM_SITES,
        )
        self.assertEqual(STANDING_LEFTOVER_5GRAM_SITES, STANDING_I_SITES)
        leftover_set = set(STANDING_LEFTOVER_5GRAM_SITES)
        leftover_next = []
        for side, line, index in STANDING_LEFTOVER_N4_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + 4]), STANDING_LEFTOVER_N4)
            next_stem = stems[index + 4]
            leftover_next.append(next_stem)
            window5 = tuple(stems[index : index + 5])
            if next_stem == "000":
                self.assertEqual(window5, GRAM5)
                self.assertIn((side, line, index), leftover_set)
            else:
                self.assertNotEqual(window5, GRAM5)
                self.assertNotIn((side, line, index), leftover_set)
        self.assertEqual(tuple(leftover_next), STANDING_LEFTOVER_NEXT_STEMS)
        self.assertEqual(STANDING_LEFTOVER_NEXT_STEMS.count("000"), 1)
        self.assertEqual(STANDING_LEFTOVER_N4_SITES[4], (SIDE_IA, "Ia14", 139))
        for site in STANDING_LEFTOVER_5GRAM_SITES:
            self.assertIn(site, STANDING_I_SITES)
            self.assertIn(site, STANDING_LEFTOVER_N4_SITES)
        self.assertEqual(STANDING_EXTRA_I_SITES, ())
        leftover_3gram = cycle207_leftover_3gram_sites(STANDING_LEFTOVER_N4_SITES)
        self.assertEqual(leftover_3gram, CYCLE207_LEFTOVER_3GRAM_SITES)
        self.assertIn((SIDE_IA, "Ia14", 140), set(CYCLE207_LEFTOVER_3GRAM_SITES))
        leak_site = (SIDE_IA, "Ia14", 140)
        leak_stems = self.i_sides[SIDE_IA][IA_LINE_NAMES.index("Ia14")]
        self.assertEqual(tuple(leak_stems[140:144]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(tuple(leak_stems[139:144]), GRAM5)
        self.assertEqual(leak_site, (SIDE_IA, "Ia14", 140))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_5gram_is_zero_off_i_and_i_only(self):
        """5-gram is 0 off-I. Ia has exactly 1. Claim holds."""
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
        if self.off_i_hits != 0:
            self.fail("measured N_off_I drifted from the locked 0")
        if self.i_hits != 1:
            self.fail("measured N_I drifted from the locked 1")
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(len(STANDING_OFF_I_SITES), STANDING_N_OFF_I)
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ())
        self.assertEqual(STANDING_OFF_I_BY_TABLET_NONZERO, {})
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM5))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 1)
            else:
                self.assertEqual(count, 0)
        gk = load_g_k_sides()
        self.assertEqual(ngram_hit_count(gk[SIDE_GR], GRAM5), 0)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], GRAM5), 0)
        s_sides = load_s_sides()
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], GRAM5), 0)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], GRAM5), 0)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM5), 0)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE219_LEAK_4GRAM), 1)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE207_GRAM3), 1)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE208_GRAM4), 0)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], NEAR_MISS_059_090_076_070_000), 1)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], CYCLE206_GRAM2), 2)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], CYCLE206_GRAM2), 1)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE206_GRAM2), 2)
        for side, line, index in CYCLE207_OFF_I_SITES:
            stems = t_sides[side][TA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + 3]), CYCLE207_GRAM3)
            self.assertEqual(
                tuple(stems[index : index + 4]),
                CYCLE219_LEAK_4GRAM,
            )
            self.assertEqual(
                tuple(stems[index - 1 : index + 4]),
                NEAR_MISS_059_090_076_070_000,
            )
            self.assertNotEqual(
                tuple(stems[index - 1 : index + 4]),
                GRAM5,
            )
            self.assertNotEqual(
                tuple(stems[index - 1 : index + 3]),
                CYCLE208_GRAM4,
            )
        self.assertEqual(CYCLE219_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertEqual(CYCLE207_OFF_I_SITES, CYCLE219_OFF_I_SITES)
        ta9 = t_sides[SIDE_TA][TA_LINE_NAMES.index("Ta9")]
        self.assertEqual(tuple(ta9[1:6]), NEAR_MISS_059_090_076_070_000)
        self.assertEqual(tuple(ta9[2:6]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(tuple(ta9[2:5]), CYCLE207_GRAM3)
        gv3 = gk[SIDE_GV][GV_LINE_NAMES.index("Gv3")]
        self.assertEqual(tuple(gv3[33:35]), CYCLE206_GRAM2)
        self.assertNotEqual(tuple(gv3[31:36]), GRAM5)
        gv4 = gk[SIDE_GV][GV_LINE_NAMES.index("Gv4")]
        self.assertEqual(tuple(gv4[1:3]), CYCLE206_GRAM2)
        self.assertNotEqual(tuple(gv4[0:5]), GRAM5)
        sb8 = s_sides[SIDE_SB][SB_LINE_NAMES.index("Sb8")]
        self.assertEqual(tuple(sb8[17:19]), CYCLE206_GRAM2)
        self.assertNotEqual(tuple(sb8[15:20]), GRAM5)
        self.assertEqual(
            i_5gram_999_090_076_070_000_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_5GRAM_999_090_076_070_000_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_5GRAM_999_090_076_070_000_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_5GRAM_999_090_076_070_000_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_5gram_999_090_076_070_000_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM5, CYCLE103_GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE208_4GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219_LEAK_4GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertFalse(CYCLE207_I_ONLY)
        self.assertTrue(CYCLE208_I_ONLY)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_219_208_207_206_and_171_scoreboards_still_compute(self):
        """Cycle 219 leak 1/1, 208 5/0, 207 8/1, 206 19/5, 171 43/0 stay."""
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        prior_219.test_survey_matches_computed_lock()
        self.assertEqual(prior_219.n_i, CYCLE219_N_I_EACH)
        self.assertEqual(prior_219.n_off_i, CYCLE219_N_OFF_I_EACH)
        self.assertEqual(CYCLE219_N_I_EACH, (1,) * 8)
        self.assertEqual(CYCLE219_N_OFF_I_EACH, (0, 0, 0, 0, 0, 0, 0, 1))
        self.assertEqual(prior_219.n_i[-1], 1)
        self.assertEqual(prior_219.n_off_i[-1], 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertEqual(CYCLE219_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertEqual(prior_219.off_i_sites[-1], CYCLE219_OFF_I_SITES)
        self.assertFalse(prior_219.claim_holds)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        if prior_219.n_i[-1] != 1 or prior_219.n_off_i[-1] != 1:
            self.fail("nested cycle 219 leak 090 076 070 000 1/1 drifted")
        prior_208 = TestMamariI4gram999090076070IOnlyScoreboard()
        prior_208.setUp()
        prior_208.test_4gram_is_zero_off_i_and_i_only()
        prior_208.test_survey_matches_computed_lock()
        self.assertEqual(prior_208.i_hits, CYCLE208_N_I)
        self.assertEqual(prior_208.i_hits, 5)
        self.assertEqual(prior_208.off_i_hits, CYCLE208_N_OFF_I)
        self.assertEqual(prior_208.off_i_hits, 0)
        self.assertTrue(prior_208.claim_holds)
        self.assertTrue(CYCLE208_I_ONLY)
        if prior_208.i_hits != 5 or prior_208.off_i_hits != 0:
            self.fail("nested cycle 208 leftover 4-gram 5/0 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertFalse(prior_207.claim_holds)
        self.assertFalse(CYCLE207_I_ONLY)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 8/1 drifted")
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        self.assertEqual(prior_206.i_hits, CYCLE206_N_I)
        self.assertEqual(prior_206.i_hits, 19)
        self.assertEqual(prior_206.off_i_hits, CYCLE206_N_OFF_I)
        self.assertEqual(prior_206.off_i_hits, 5)
        if prior_206.i_hits != 19 or prior_206.off_i_hits != 5:
            self.fail("nested cycle 206 19/5 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-220 5-gram I-only hold."""
        lock = self.survey["i_5gram_999_090_076_070_000_i_only"]
        self.assertEqual(lock["cycle"], 220)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens5"]), GRAM5)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 1)
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
            tuple(tuple(row) for row in lock["leftover_5gram_sites"]),
            STANDING_LEFTOVER_5GRAM_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertEqual(lock["N_inside_leftover"], STANDING_N_INSIDE_LEFTOVER)
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(tuple(lock["leftover_n4"]), STANDING_LEFTOVER_N4)
        self.assertEqual(tuple(lock["leftover_next_stems"]), STANDING_LEFTOVER_NEXT_STEMS)
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(lock["N_off_I"], 0)
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
        self.assertTrue(lock["i_5gram_999_090_076_070_000_i_only"])
        self.assertEqual(
            lock["i_5gram_999_090_076_070_000_i_only"],
            STANDING_I_5GRAM_999_090_076_070_000_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle208_4gram"])
        self.assertFalse(lock["same_as_cycle219_leak_4gram"])
        self.assertFalse(lock["same_as_cycle207_3gram"])
        self.assertFalse(lock["same_as_cycle206_2gram"])
        self.assertFalse(lock["same_as_cycle171_2gram"])
        self.assertTrue(lock["090_076_070_000_without_999_does_not_count"])
        self.assertTrue(lock["999_090_076_070_without_000_does_not_count"])
        self.assertTrue(lock["059_090_076_070_000_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        prior_219 = self.survey["i_090_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_219["cycle"], 219)
        self.assertFalse(prior_219["i_090_076_070_forward_4grams_i_only"])
        self.assertEqual(prior_219["N_i_only"], 7)
        self.assertEqual(prior_219["N_not_i_only"], 1)
        self.assertEqual(tuple(prior_219["N_I_each"]), CYCLE219_N_I_EACH)
        self.assertEqual(tuple(prior_219["N_off_I_each"]), CYCLE219_N_OFF_I_EACH)
        self.assertEqual(tuple(prior_219["off_i_forward_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(prior_219["sequences"][-1]["N_I"], 1)
        self.assertEqual(prior_219["sequences"][-1]["N_off_I"], 1)
        self.assertFalse(prior_219["sequences"][-1]["i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_219["sequences"][-1]["off_i_sites"]),
            CYCLE219_OFF_I_SITES,
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"][
                "i_4gram_999_090_076_070_i_only"
            ]
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], CYCLE207_N_I)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], CYCLE207_N_OFF_I)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], CYCLE206_N_I)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], CYCLE206_N_OFF_I)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
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
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            CYCLE103_GRAM5,
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


class TestMamariI5gram999090076070000IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 220 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
