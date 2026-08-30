"""I's cycle-205 leftover 4-gram 999 090 076 070 off-I lock.

Cycle 208 text-search lock. Uses already-vendored A–V and the
cycle-205 leftover n=4 maximal 999 090 076 070. Does not
retune that 4-gram or the leftover n=4 set. Does not vendor
a new tablet. Does not scrape X. W has no Barthel (cycle
100); skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8
or G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Same claim-shape as cycle 167 (999 090 076 was I-only 16/0)
and cycle 171 (076 071 was I-only 43/0). Cycle 207 lost:
3-gram 090 076 070 is not I-only (8/1 on T). Cycle 206 lost:
2-gram 076 070 is not I-only (19/5). Cycle 205 holds: exactly
1 leftover n=4 maximal contains consecutive 076 070
(999 090 076 070, freq 5). This cycle is that leftover
4-gram only. 090 076 070 without leading 999 does not count
as this 4-gram (cycle 207 T leak is 059 090 076 070).
999 090 076 071 is a different 4-gram. Do not retune
090 076 070, 076 070, 999 090 076, or 076 071. Do not
assume the I-only result.

Locks exact consecutive hits of 999 090 076 070 on tablet I
and on every other vendored tablet A–H and J–V. Claim that
can lose: i_4gram_999_090_076_070_i_only (I hits ≥ 1 and
off-I hits == 0). True only if N_off_I == 0. Measured: Ia
is exactly 5; Ib unpublished 0; off-I is 0. The claim is
true. Not an n≥8 island. Not the cycle-103 I 5-gram. All 5
I sites sit inside leftover n=4 999 090 076 070; extra is 0.

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
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE207_EXTRA_I_SITES,
    STANDING_EXTRA_PREVIOUS_4GRAMS as CYCLE207_EXTRA_PREVIOUS_4GRAMS,
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
    TestMamariI3gram090076071IOnlyScoreboard,
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
GRAM4 = ("999", "090", "076", "070")
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_076_070 = CYCLE206_GRAM2
NEAR_MISS_999_090_076 = CYCLE167_GRAM3
NEAR_MISS_059_090_076_070 = CYCLE207_OFF_I_PREVIOUS_4GRAM
STANDING_N4 = 4
STANDING_I_HITS = 5
STANDING_IA_HITS = 5
STANDING_IB_HITS = 0
STANDING_N_ON_I = 5
STANDING_N_I = 5
STANDING_I_SITES = (
    (SIDE_IA, "Ia2", 9),
    (SIDE_IA, "Ia4", 111),
    (SIDE_IA, "Ia7", 67),
    (SIDE_IA, "Ia7", 128),
    (SIDE_IA, "Ia14", 139),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_N4 = STANDING_MATCHING_LEFTOVERS[0]
STANDING_LEFTOVER_N4_SITES = STANDING_WITH_ROWS[0][3]
STANDING_LEFTOVER_4GRAM_SITES = (
    (SIDE_IA, "Ia2", 9),
    (SIDE_IA, "Ia4", 111),
    (SIDE_IA, "Ia7", 67),
    (SIDE_IA, "Ia7", 128),
    (SIDE_IA, "Ia14", 139),
)
STANDING_N_INSIDE_LEFTOVER = 5
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
STANDING_CLAIM = "i_4gram_999_090_076_070_i_only"
STANDING_I_4GRAM_999_090_076_070_I_ONLY = True
STANDING_RESULT = "i_4gram_999_090_076_070_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE171_2GRAM = False
STANDING_SAME_AS_CYCLE195_3GRAM = False
STANDING_SAME_AS_CYCLE206_2GRAM = False
STANDING_SAME_AS_CYCLE207_3GRAM = False
STANDING_090_076_070_WITHOUT_999_DOES_NOT_COUNT = True
STANDING_999_090_076_071_DOES_NOT_COUNT = True
STANDING_059_090_076_070_DOES_NOT_COUNT = True


def i_4gram_999_090_076_070_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


def leftover_contained_4gram_sites(
    leftover_n4_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_N4_SITES,
    offset: int = 0,
) -> tuple[tuple[str, str, int], ...]:
    """999 090 076 070 starts at leftover n=4 999 090 076 070 (offset 0)."""
    return tuple((side, line, index + offset) for side, line, index in leftover_n4_sites)


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_4gram: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_4GRAM_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 999 090 076 070 sites that are not leftover n=4 999 090 076 070."""
    leftover_set = set(leftover_4gram)
    return tuple(site for site in i_sites if site not in leftover_set)


class TestI4gram999090076070IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-205 leftover 4-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. Near-miss 4-grams are not."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("999", "090", "076", "070"))
        adjacent = [list(GRAM4), list(GRAM4)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4), 2)
        overlap = [["999", "090", "076", "070", "999", "090", "076", "070"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4), 2)
        gapped = [list(GRAM4[:2]) + ["006"] + list(GRAM4[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM4), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_070)], GRAM4), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076)], GRAM4), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_071)], GRAM4), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM4), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_059_090_076_070)], GRAM4), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "070"]], GRAM4), 0)
        self.assertEqual(ngram_hit_count([["076", "070"]], GRAM4), 0)
        for extra4 in CYCLE207_EXTRA_PREVIOUS_4GRAMS:
            self.assertEqual(ngram_hit_count([list(extra4)], GRAM4), 0)
            self.assertNotEqual(extra4, GRAM4)
        self.assertTrue(STANDING_090_076_070_WITHOUT_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_059_090_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Measured 5/0 holds."""
        provider = MockProvider()
        self.assertTrue(i_4gram_999_090_076_070_i_only(1, 0))
        self.assertTrue(i_4gram_999_090_076_070_i_only(5, 0))
        self.assertFalse(i_4gram_999_090_076_070_i_only(5, 1))
        self.assertFalse(i_4gram_999_090_076_070_i_only(1, 1))
        self.assertFalse(i_4gram_999_090_076_070_i_only(0, 0))
        self.assertFalse(i_4gram_999_090_076_070_i_only(0, 1))
        self.assertEqual(STANDING_CLAIM, "i_4gram_999_090_076_070_i_only")
        self.assertTrue(STANDING_I_4GRAM_999_090_076_070_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(
            STANDING_I_4GRAM_999_090_076_070_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4gram_is_cycle205_leftover_not_the_cycle_103_5gram(self):
        """4-gram is the cycle-205 leftover, not 090 076 070, 076 070, or 999 090 076."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("999", "090", "076", "070"))
        self.assertEqual(GRAM4, STANDING_LEFTOVER_N4)
        self.assertNotEqual(GRAM4, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM4, CYCLE206_GRAM2)
        self.assertNotEqual(GRAM4, CYCLE205_GRAM2)
        self.assertNotEqual(GRAM4, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM4, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM4, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM4, GRAM5)
        self.assertNotEqual(GRAM4, NEAR_MISS_999_090_076_071)
        self.assertNotEqual(GRAM4, NEAR_MISS_059_090_076_070)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM4, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertEqual(len(GRAM4), STANDING_N4)
        self.assertEqual(STANDING_N4, 4)
        self.assertLess(len(GRAM4), 8)
        for leftover in STANDING_MATCHING_LEFTOVERS:
            self.assertTrue(is_contiguous_substring(GRAM4, leftover))
            self.assertEqual(GRAM4, leftover)
        self.assertFalse(is_contiguous_substring(GRAM4, NEAR_MISS_999_090_076_071))
        self.assertFalse(is_contiguous_substring(GRAM4, NEAR_MISS_700_076_076_053))
        self.assertTrue(is_contiguous_substring(CYCLE206_GRAM2, GRAM4))
        self.assertTrue(is_contiguous_substring(CYCLE207_GRAM3, GRAM4))
        self.assertTrue(is_contiguous_substring(CYCLE167_GRAM3, GRAM4))
        self.assertEqual(GRAM4[1:], CYCLE207_GRAM3)
        self.assertEqual(GRAM4[:3], CYCLE167_GRAM3)
        self.assertEqual(GRAM4[2:], CYCLE206_GRAM2)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_vs_extra_split_can_fail(self):
        """All 5 I sites sit inside leftover n=4; extra is 0."""
        provider = MockProvider()
        leftover_4gram = leftover_contained_4gram_sites()
        extra = extra_i_sites()
        self.assertEqual(leftover_4gram, STANDING_LEFTOVER_4GRAM_SITES)
        self.assertEqual(extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(leftover_4gram), STANDING_N_INSIDE_LEFTOVER)
        self.assertEqual(len(extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(
            STANDING_N_INSIDE_LEFTOVER + STANDING_N_EXTRA,
            STANDING_N_I,
        )
        self.assertEqual(
            tuple(sorted(leftover_4gram + extra)),
            tuple(sorted(STANDING_I_SITES)),
        )
        planted = extra_i_sites(STANDING_I_SITES, ())
        self.assertNotEqual(planted, extra)
        self.assertEqual(len(planted), STANDING_N_I)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI4gram999090076070IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 4-gram 999 090 076 070 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM4, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM4)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM4, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM4, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.off_i_sites = cycle207_named_off_i_sites(GRAM4)
        self.leftover_4gram = leftover_contained_4gram_sites()
        self.extra = extra_i_sites(self.i_sites, self.leftover_4gram)
        self.claim_holds = i_4gram_999_090_076_070_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_205_leftover_not_retuned(self):
        """4-gram is the cycle-205 leftover lock, not a new inventory."""
        self.assertEqual(GRAM4, ("999", "090", "076", "070"))
        self.assertEqual(GRAM4, STANDING_LEFTOVER_N4)
        prior_205 = self.survey["i_leftover_n4_076_070"]
        self.assertEqual(prior_205["cycle"], 205)
        self.assertEqual(tuple(prior_205["tokens2"]), CYCLE205_GRAM2)
        self.assertEqual(prior_205["N_with_076_070"], 1)
        self.assertEqual(prior_205["N_without_076_070"], 26)
        measured_matching = [list(gram) for gram in STANDING_MATCHING_LEFTOVERS]
        self.assertEqual(prior_205["matching_leftovers"], measured_matching)
        self.assertTrue(prior_205["i_leftover_n4_exactly_1_contain_076_070"])
        self.assertTrue(prior_205["076_071_does_not_count"])
        self.assertEqual(STANDING_LEFTOVER_N4, ("999", "090", "076", "070"))
        self.assertEqual(STANDING_LEFTOVER_N4_SITES, STANDING_WITH_ROWS[0][3])
        self.assertNotEqual(GRAM4, GRAM5)
        self.assertNotEqual(GRAM4, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM4, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM4, CYCLE206_GRAM2)
        self.assertNotEqual(GRAM4, CYCLE207_GRAM3)
        self.assertFalse(is_contiguous_substring(GRAM4, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_five_on_ia(self):
        """4-gram is 5 on Ia; Ib unpublished 0. N_I must not drift."""
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
        self.assertEqual(nge4_sites(GRAM4, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM4), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N4]), GRAM4)
            self.assertEqual(side, SIDE_IA)
        self.assertEqual(
            STANDING_I_SITES[:3],
            ((SIDE_IA, "Ia2", 9), (SIDE_IA, "Ia4", 111), (SIDE_IA, "Ia7", 67)),
        )
        self.assertEqual(
            STANDING_I_SITES[4],
            (SIDE_IA, "Ia14", 139),
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_vs_extra_on_i(self):
        """All 5 I sites sit inside leftover 999 090 076 070; extra is 0."""
        self.assertEqual(self.leftover_4gram, STANDING_LEFTOVER_4GRAM_SITES)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.leftover_4gram), STANDING_N_INSIDE_LEFTOVER)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_INSIDE_LEFTOVER, 5)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(
            leftover_contained_4gram_sites(STANDING_LEFTOVER_N4_SITES),
            STANDING_LEFTOVER_4GRAM_SITES,
        )
        self.assertEqual(STANDING_LEFTOVER_4GRAM_SITES, STANDING_LEFTOVER_N4_SITES)
        self.assertEqual(STANDING_LEFTOVER_4GRAM_SITES, STANDING_I_SITES)
        leftover_set = set(STANDING_LEFTOVER_4GRAM_SITES)
        for side, line, index in STANDING_LEFTOVER_N4_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), STANDING_LEFTOVER_N4)
            self.assertIn((side, line, index), leftover_set)
        for site in STANDING_LEFTOVER_4GRAM_SITES:
            self.assertIn(site, STANDING_I_SITES)
        self.assertEqual(STANDING_EXTRA_I_SITES, ())
        leftover_3gram = cycle207_leftover_3gram_sites(STANDING_LEFTOVER_N4_SITES)
        self.assertEqual(leftover_3gram, CYCLE207_LEFTOVER_3GRAM_SITES)
        for side, line, index in STANDING_LEFTOVER_N4_SITES:
            self.assertIn((side, line, index + 1), set(CYCLE207_LEFTOVER_3GRAM_SITES))
        for site, prev4 in zip(
            CYCLE207_EXTRA_I_SITES,
            CYCLE207_EXTRA_PREVIOUS_4GRAMS,
            strict=True,
        ):
            self.assertNotIn(site, leftover_set)
            side, line, index = site
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index - 1 : index + 3]), prev4)
            self.assertNotEqual(prev4, STANDING_LEFTOVER_N4)
            self.assertEqual(tuple(stems[index : index + 3]), CYCLE207_GRAM3)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_4gram_is_zero_off_i_and_i_only(self):
        """4-gram is 0 off-I. Ia has exactly 5. Claim holds."""
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
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(len(STANDING_OFF_I_SITES), STANDING_N_OFF_I)
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ())
        self.assertEqual(STANDING_OFF_I_BY_TABLET_NONZERO, {})
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM4))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 5)
            else:
                self.assertEqual(count, 0)
        gk = load_g_k_sides()
        self.assertEqual(ngram_hit_count(gk[SIDE_GR], GRAM4), 0)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], GRAM4), 0)
        s_sides = load_s_sides()
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], GRAM4), 0)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], GRAM4), 0)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM4), 0)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE207_GRAM3), 1)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], CYCLE206_GRAM2), 2)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], CYCLE206_GRAM2), 1)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE206_GRAM2), 2)
        for side, line, index in CYCLE207_OFF_I_SITES:
            stems = t_sides[side][TA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + 3]), CYCLE207_GRAM3)
            self.assertEqual(
                tuple(stems[index - 1 : index + 3]),
                CYCLE207_OFF_I_PREVIOUS_4GRAM,
            )
            self.assertNotEqual(
                tuple(stems[index - 1 : index + 3]),
                GRAM4,
            )
        gv3 = gk[SIDE_GV][GV_LINE_NAMES.index("Gv3")]
        self.assertEqual(tuple(gv3[33:35]), CYCLE206_GRAM2)
        self.assertNotEqual(tuple(gv3[31:35]), GRAM4)
        gv4 = gk[SIDE_GV][GV_LINE_NAMES.index("Gv4")]
        self.assertEqual(tuple(gv4[1:3]), CYCLE206_GRAM2)
        self.assertNotEqual(tuple(gv4[0:4]), GRAM4)
        sb8 = s_sides[SIDE_SB][SB_LINE_NAMES.index("Sb8")]
        self.assertEqual(tuple(sb8[17:19]), CYCLE206_GRAM2)
        self.assertNotEqual(tuple(sb8[15:19]), GRAM4)
        ta2 = t_sides[SIDE_TA][TA_LINE_NAMES.index("Ta2")]
        self.assertEqual(tuple(ta2[10:12]), CYCLE206_GRAM2)
        self.assertNotEqual(tuple(ta2[8:12]), GRAM4)
        self.assertEqual(
            i_4gram_999_090_076_070_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_4GRAM_999_090_076_070_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_4GRAM_999_090_076_070_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_4GRAM_999_090_076_070_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_4gram_999_090_076_070_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM4, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(CYCLE207_I_ONLY)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_207_206_205_171_and_167_scoreboards_still_compute(self):
        """Cycle 207 8/1 loss, 206 19/5 loss, 205 leftover-1, 171 I-only 43/0, 167 I-only 16/0 stay."""
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-208 4-gram I-only hold."""
        lock = self.survey["i_4gram_999_090_076_070_i_only"]
        self.assertEqual(lock["cycle"], 208)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], STANDING_N4)
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
            tuple(tuple(row) for row in lock["leftover_n4_sites"]),
            STANDING_LEFTOVER_N4_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_4gram_sites"]),
            STANDING_LEFTOVER_4GRAM_SITES,
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
        self.assertTrue(lock["i_4gram_999_090_076_070_i_only"])
        self.assertEqual(
            lock["i_4gram_999_090_076_070_i_only"],
            STANDING_I_4GRAM_999_090_076_070_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle171_2gram"])
        self.assertFalse(lock["same_as_cycle195_3gram"])
        self.assertFalse(lock["same_as_cycle206_2gram"])
        self.assertFalse(lock["same_as_cycle207_3gram"])
        self.assertTrue(lock["090_076_070_without_999_does_not_count"])
        self.assertTrue(lock["999_090_076_071_does_not_count"])
        self.assertTrue(lock["059_090_076_070_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
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


class TestMamariI4gram999090076070IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 208 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
