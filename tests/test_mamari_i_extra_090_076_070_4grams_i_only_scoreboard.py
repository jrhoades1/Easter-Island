"""I's cycle-207 extra 090 076 070 4-grams off-I lock.

Cycle 209 text-search lock. Uses already-vendored A–V and the
cycle-207 extra I sites of 3-gram 090 076 070 (the 3 I sites
that are not leftover n=4 999 090 076 070). Local previous
4-grams: 036 090 076 070 at Ia3[3], 161 090 076 070 at
Ia8[119], 400 090 076 070 at Ia14[96]. Does not retune those
4-grams, the leftover 3-gram, or the leftover n=4 set. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 169 (leftover 999 090 076 site
4-grams both I-only hapax 1/0) and cycle 175 (076 071 076
forward 4-grams all I-only hapax 1/0). Cycle 208 holds:
leftover 4-gram 999 090 076 070 I-only 5/0. Cycle 207 lost:
3-gram 090 076 070 is not I-only (8/1 on T). Cycle 206
lost: 2-gram 076 070 is not I-only (19/5). Cycle 205 holds:
exactly 1 leftover n=4 maximal contains consecutive 076 070.
Do not include leftover 999 090 076 070 (already locked
cycle 208). Do not include the T leak 059 090 076 070
(already off-I). 090 076 071 prefixes are a different
3-gram. Do not retune. Do not assume the I-only result.

Locks exact consecutive hits of each extra 4-gram on tablet
I and on every other vendored tablet A–H and J–V.
Hypothesis: all three are I-only. Measured: each N_I=1 at
the 4-gram start one token before the cycle-207 extra site;
all N_off_I=0. Claim that can lose:
i_extra_090_076_070_4grams_i_only. True only if ALL three
have N_off_I=0 (and N_I>=1). The claim is true. Do not
assume hapax; measure. Do not retune.

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
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_PREVIOUS_4GRAM as CYCLE207_OFF_I_PREVIOUS_4GRAM,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
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
from tests.test_mamari_i_4gram_999_090_076_070_i_only_scoreboard import (
    GRAM4 as CYCLE208_GRAM4,
    STANDING_I_4GRAM_999_090_076_070_I_ONLY as CYCLE208_I_ONLY,
    STANDING_I_SITES as CYCLE208_I_SITES,
    STANDING_N_I as CYCLE208_N_I,
    STANDING_N_OFF_I as CYCLE208_N_OFF_I,
    TestMamariI4gram999090076070IOnlyScoreboard,
)
from tests.test_mamari_i_076_071_076_forward_4grams_i_only_scoreboard import (
    TestMamariI076071076Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_999_090_076_site_4grams_i_only_scoreboard import (
    TestMamariILeftover999090076Site4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    GRAM2 as CYCLE205_GRAM2,
    NEAR_MISS_700_076_076_053,
    NEAR_MISS_999_090_076_071,
    STANDING_MATCHING_LEFTOVERS,
    TestMamariILeftoverN4076070Scoreboard,
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
GRAM4_036 = ("036", "090", "076", "070")
GRAM4_161 = ("161", "090", "076", "070")
GRAM4_400 = ("400", "090", "076", "070")
STANDING_SEQUENCES = (GRAM4_036, GRAM4_161, GRAM4_400)
STANDING_PREVIOUS_STEMS = ("036", "161", "400")
NEAR_MISS_999_090_076_070 = CYCLE208_GRAM4
NEAR_MISS_059_090_076_070 = CYCLE207_OFF_I_PREVIOUS_4GRAM
NEAR_MISS_090_076_071 = CYCLE195_GRAM3
STANDING_N_SEQUENCES = 3
STANDING_CYCLE207_EXTRA_SITES = CYCLE207_EXTRA_I_SITES
STANDING_N_I_036 = 1
STANDING_N_I_161 = 1
STANDING_N_I_400 = 1
STANDING_N_ON_I_036 = 1
STANDING_N_ON_I_161 = 1
STANDING_N_ON_I_400 = 1
STANDING_I_SITES_036 = ((SIDE_IA, "Ia3", 3),)
STANDING_I_SITES_161 = ((SIDE_IA, "Ia8", 119),)
STANDING_I_SITES_400 = ((SIDE_IA, "Ia14", 96),)
STANDING_I_SITES = (
    STANDING_I_SITES_036,
    STANDING_I_SITES_161,
    STANDING_I_SITES_400,
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_036 = 0
STANDING_N_OFF_I_161 = 0
STANDING_N_OFF_I_400 = 0
STANDING_OFF_I_SITES_036 = ()
STANDING_OFF_I_SITES_161 = ()
STANDING_OFF_I_SITES_400 = ()
STANDING_OFF_I_SITES = (
    STANDING_OFF_I_SITES_036,
    STANDING_OFF_I_SITES_161,
    STANDING_OFF_I_SITES_400,
)
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_CLAIM = "i_extra_090_076_070_4grams_i_only"
STANDING_I_EXTRA_090_076_070_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_extra_090_076_070_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE169_SITE_4GRAMS = False
STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE208_4GRAM = False
STANDING_SAME_CLAIM_SHAPE_AS_169_175 = True
STANDING_999_090_076_070_DOES_NOT_COUNT = True
STANDING_059_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
PREV_OFFSET = 1


def extra_previous_4gram_start_site(
    extra_3gram_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Previous 4-gram starts one stem before extra 090 076 070."""
    side, line, index = extra_3gram_site
    return (side, line, index - PREV_OFFSET)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_extra_090_076_070_4grams_i_only(
    n_i_036: int,
    n_off_i_036: int,
    n_i_161: int,
    n_off_i_161: int,
    n_i_400: int,
    n_off_i_400: int,
) -> bool:
    """True iff all three extra 090 076 070 4-grams are I-only.

    Claim holds only if every gram has N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only. Hapax is not
    assumed; N_I may be greater than 1.
    """
    return (
        sequence_is_i_only(n_i_036, n_off_i_036)
        and sequence_is_i_only(n_i_161, n_off_i_161)
        and sequence_is_i_only(n_i_400, n_off_i_400)
    )


class TestIExtra0900760704gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-207 extra previous 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. Leftover / T leak / 071 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM4_036, ("036", "090", "076", "070"))
        self.assertEqual(GRAM4_161, ("161", "090", "076", "070"))
        self.assertEqual(GRAM4_400, ("400", "090", "076", "070"))
        self.assertEqual(STANDING_SEQUENCES, CYCLE207_EXTRA_PREVIOUS_4GRAMS)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[1:], CYCLE207_GRAM3)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["036", "090", "076", "070", "036", "090", "076", "070"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_036), 2)
        gapped = [list(GRAM4_036[:2]) + ["000"] + list(GRAM4_036[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_036), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_036), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_070)], GRAM4_036), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_059_090_076_070)], GRAM4_161), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_071)], GRAM4_400), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_071)], GRAM4_036), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM4_161), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE207_GRAM3)], GRAM4_036), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE206_GRAM2)], GRAM4_161), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "071"]], GRAM4_400), 0)
        self.assertTrue(STANDING_999_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_059_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all three extra 4-grams are I-only."""
        provider = MockProvider()
        self.assertTrue(i_extra_090_076_070_4grams_i_only(1, 0, 1, 0, 1, 0))
        self.assertTrue(i_extra_090_076_070_4grams_i_only(2, 0, 1, 0, 1, 0))
        self.assertFalse(i_extra_090_076_070_4grams_i_only(1, 1, 1, 0, 1, 0))
        self.assertFalse(i_extra_090_076_070_4grams_i_only(1, 0, 1, 1, 1, 0))
        self.assertFalse(i_extra_090_076_070_4grams_i_only(1, 0, 1, 0, 1, 1))
        self.assertFalse(i_extra_090_076_070_4grams_i_only(0, 0, 1, 0, 1, 0))
        self.assertFalse(i_extra_090_076_070_4grams_i_only(1, 0, 0, 0, 1, 0))
        self.assertFalse(i_extra_090_076_070_4grams_i_only(1, 0, 1, 0, 0, 0))
        self.assertFalse(i_extra_090_076_070_4grams_i_only(0, 0, 0, 0, 0, 0))
        self.assertFalse(i_extra_090_076_070_4grams_i_only(1, 1, 1, 1, 1, 1))
        self.assertEqual(STANDING_CLAIM, "i_extra_090_076_070_4grams_i_only")
        self.assertTrue(STANDING_I_EXTRA_090_076_070_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(
            STANDING_I_EXTRA_090_076_070_4GRAMS_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_207_extra_previous_not_retuned(self):
        """4-grams stay the cycle-207 extra previous locals; leftover / T leak are not."""
        provider = MockProvider()
        self.assertEqual(CYCLE207_GRAM3, ("090", "076", "070"))
        self.assertEqual(STANDING_SEQUENCES, CYCLE207_EXTRA_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_CYCLE207_EXTRA_SITES, CYCLE207_EXTRA_I_SITES)
        self.assertEqual(
            STANDING_CYCLE207_EXTRA_SITES,
            (
                (SIDE_IA, "Ia3", 4),
                (SIDE_IA, "Ia8", 120),
                (SIDE_IA, "Ia14", 97),
            ),
        )
        self.assertNotEqual(GRAM4_036, CYCLE208_GRAM4)
        self.assertNotEqual(GRAM4_161, CYCLE208_GRAM4)
        self.assertNotEqual(GRAM4_400, CYCLE208_GRAM4)
        self.assertNotEqual(GRAM4_036, NEAR_MISS_059_090_076_070)
        self.assertNotEqual(GRAM4_161, NEAR_MISS_059_090_076_070)
        self.assertNotEqual(GRAM4_400, NEAR_MISS_059_090_076_070)
        self.assertNotEqual(GRAM4_036, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(CYCLE208_GRAM4, STANDING_MATCHING_LEFTOVERS[0])
        family = set(STANDING_MATCHING_LEFTOVERS)
        for gram in STANDING_SEQUENCES:
            self.assertNotIn(gram, family)
            self.assertTrue(is_contiguous_substring(CYCLE207_GRAM3, gram))
            self.assertTrue(is_contiguous_substring(CYCLE206_GRAM2, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(CYCLE195_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE171_GRAM2, gram))
        for extra_site, start in zip(
            STANDING_CYCLE207_EXTRA_SITES,
            (
                STANDING_I_SITES_036[0],
                STANDING_I_SITES_161[0],
                STANDING_I_SITES_400[0],
            ),
            strict=True,
        ):
            self.assertEqual(extra_previous_4gram_start_site(extra_site), start)
        planted = extra_previous_4gram_start_site((SIDE_IA, "Ia3", 4))
        self.assertEqual(planted, (SIDE_IA, "Ia3", 3))
        self.assertNotEqual(planted, (SIDE_IA, "Ia3", 4))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE169_SITE_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE208_4GRAM)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_169_175)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(GRAM4_036), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariIExtra0900760704gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture extra 090 076 070 4-gram off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle207_extra = STANDING_CYCLE207_EXTRA_SITES
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
        self.off_i_sites = tuple(
            cycle207_named_off_i_sites(gram) for gram in self.grams
        )
        self.claim_holds = i_extra_090_076_070_4grams_i_only(
            *sum(zip(self.n_i, self.n_off_i, strict=True), ())
        )

    def test_tokens_and_sites_are_cycle_207_extra_not_retuned(self):
        """4-grams and extra I sites stay the cycle-207 previous lock."""
        self.assertEqual(CYCLE207_GRAM3, ("090", "076", "070"))
        self.assertEqual(self.cycle207_extra, STANDING_CYCLE207_EXTRA_SITES)
        self.assertEqual(STANDING_SEQUENCES, CYCLE207_EXTRA_PREVIOUS_4GRAMS)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(tuple(prior_207["tokens3"]), CYCLE207_GRAM3)
        self.assertEqual(prior_207["N_I"], CYCLE207_N_I)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], CYCLE207_N_OFF_I)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertFalse(CYCLE207_I_ONLY)
        self.assertEqual(
            tuple(tuple(row) for row in prior_207["extra_i_sites"]),
            STANDING_CYCLE207_EXTRA_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_207["extra_previous_4grams"],
        )
        prior_208 = self.survey["i_4gram_999_090_076_070_i_only"]
        self.assertEqual(prior_208["cycle"], 208)
        self.assertEqual(tuple(prior_208["tokens4"]), CYCLE208_GRAM4)
        self.assertEqual(prior_208["N_I"], CYCLE208_N_I)
        self.assertEqual(prior_208["N_I"], 5)
        self.assertEqual(prior_208["N_off_I"], CYCLE208_N_OFF_I)
        self.assertEqual(prior_208["N_off_I"], 0)
        self.assertTrue(prior_208["i_4gram_999_090_076_070_i_only"])
        self.assertTrue(CYCLE208_I_ONLY)
        self.assertEqual(
            tuple(tuple(row) for row in prior_208["i_sites"]),
            CYCLE208_I_SITES,
        )
        prior_205 = self.survey["i_leftover_n4_076_070"]
        self.assertEqual(prior_205["cycle"], 205)
        self.assertEqual(tuple(prior_205["tokens2"]), CYCLE205_GRAM2)
        self.assertEqual(prior_205["N_with_076_070"], 1)
        self.assertEqual(prior_205["N_without_076_070"], 26)
        self.assertTrue(prior_205["i_leftover_n4_exactly_1_contain_076_070"])
        self.assertEqual(STANDING_MATCHING_LEFTOVERS[0], CYCLE208_GRAM4)
        for gram in STANDING_SEQUENCES:
            self.assertNotEqual(gram, CYCLE208_GRAM4)
            self.assertNotEqual(gram, NEAR_MISS_059_090_076_070)
            self.assertNotEqual(gram, CYCLE195_GRAM3)
            self.assertNotEqual(gram, GRAM5)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_I=1/1/1, N_off_I=0/0/0. All I-only. Claim holds."""
        standing_on = (STANDING_N_I_036, STANDING_N_I_161, STANDING_N_I_400)
        standing_off = (STANDING_N_OFF_I_036, STANDING_N_OFF_I_161, STANDING_N_OFF_I_400)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, standing_on)
        self.assertEqual(standing_on, (1, 1, 1))
        self.assertEqual(self.n_off_i, standing_off)
        self.assertEqual(standing_off, (0, 0, 0))
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        for extra_site, start, gram, prev in zip(
            STANDING_CYCLE207_EXTRA_SITES,
            (
                STANDING_I_SITES_036[0],
                STANDING_I_SITES_161[0],
                STANDING_I_SITES_400[0],
            ),
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
            strict=True,
        ):
            self.assertEqual(extra_previous_4gram_start_site(extra_site), start)
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2]], prev)
            self.assertEqual(
                tuple(stems[extra_site[2] : extra_site[2] + STANDING_N3]),
                CYCLE207_GRAM3,
            )
            self.assertEqual(tuple(stems[start[2] + 1 : start[2] + 4]), CYCLE207_GRAM3)
            self.assertNotEqual(gram, CYCLE208_GRAM4)
            self.assertNotEqual(gram, NEAR_MISS_059_090_076_070)
            self.assertNotEqual(gram, GRAM5)
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
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE207_GRAM3), 1)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], CYCLE208_GRAM4), 0)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], gram), 0)
        for side, line, index in CYCLE207_OFF_I_SITES:
            stems = t_sides[side][TA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), CYCLE207_GRAM3)
            self.assertEqual(
                tuple(stems[index - 1 : index + STANDING_N3]),
                NEAR_MISS_059_090_076_070,
            )
            self.assertNotIn(
                tuple(stems[index - 1 : index + STANDING_N3]),
                STANDING_SEQUENCES,
            )
        self.assertEqual(
            i_extra_090_076_070_4grams_i_only(
                *sum(zip(self.n_i, self.n_off_i, strict=True), ())
            ),
            STANDING_I_EXTRA_090_076_070_4GRAMS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_EXTRA_090_076_070_4GRAMS_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_EXTRA_090_076_070_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_extra_090_076_070_4grams_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE169_SITE_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE208_4GRAM)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_169_175)
        self.assertTrue(STANDING_999_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_059_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_208_207_206_205_and_171_scoreboards_still_compute(self):
        """Cycle 208 5/0 hold, 207 8/1 loss, 206 19/5 loss, 205 leftover-1, 171 43/0 stay."""
        prior_208 = TestMamariI4gram999090076070IOnlyScoreboard()
        prior_208.setUp()
        prior_208.test_4gram_is_zero_off_i_and_i_only()
        prior_208.test_survey_matches_computed_lock()
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
        prior_169 = TestMamariILeftover999090076Site4gramsIOnlyScoreboard()
        prior_169.setUp()
        prior_169.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_169.test_survey_matches_computed_lock()
        prior_175 = TestMamariI076071076Forward4gramsIOnlyScoreboard()
        prior_175.setUp()
        prior_175.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_175.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-209 extra 4-gram I-only hold."""
        lock = self.survey["i_extra_090_076_070_4grams_i_only"]
        self.assertEqual(lock["cycle"], 209)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), CYCLE207_GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_sequences"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_I_3gram"], CYCLE207_N_I)
        self.assertEqual(lock["N_I_3gram"], 8)
        self.assertEqual(lock["N_off_I_3gram"], CYCLE207_N_OFF_I)
        self.assertEqual(lock["N_off_I_3gram"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle207_extra_sites"]),
            STANDING_CYCLE207_EXTRA_SITES,
        )
        self.assertEqual(lock["N_extra"], 3)
        self.assertEqual(tuple(lock["previous_stems"]), STANDING_PREVIOUS_STEMS)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 3)
        standing_on = (STANDING_N_I_036, STANDING_N_I_161, STANDING_N_I_400)
        standing_off = (STANDING_N_OFF_I_036, STANDING_N_OFF_I_161, STANDING_N_OFF_I_400)
        standing_off_sites = (
            STANDING_OFF_I_SITES_036,
            STANDING_OFF_I_SITES_161,
            STANDING_OFF_I_SITES_400,
        )
        for row, gram, extra_site, start, prev, sites, n_on, n_off, off_sites in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CYCLE207_EXTRA_SITES,
            (
                STANDING_I_SITES_036[0],
                STANDING_I_SITES_161[0],
                STANDING_I_SITES_400[0],
            ),
            STANDING_PREVIOUS_STEMS,
            STANDING_I_SITES,
            standing_on,
            standing_off,
            standing_off_sites,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle207_extra_site"]), extra_site)
            self.assertEqual(tuple(row["i_4gram_start"]), start)
            self.assertEqual(row["previous_stem"], prev)
            self.assertEqual(row["role"], "extra")
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
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["off_i_sites"]),
                off_sites,
            )
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(
                tuple(row["hits_by_tablet"]),
                STANDING_HITS_BY_TABLET_ONE_ON_I,
            )
            self.assertTrue(row["i_only"])
        self.assertEqual(lock["N_I_036"], STANDING_N_I_036)
        self.assertEqual(lock["N_off_I_036"], STANDING_N_OFF_I_036)
        self.assertEqual(lock["N_I_161"], STANDING_N_I_161)
        self.assertEqual(lock["N_off_I_161"], STANDING_N_OFF_I_161)
        self.assertEqual(lock["N_I_400"], STANDING_N_I_400)
        self.assertEqual(lock["N_off_I_400"], STANDING_N_OFF_I_400)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_extra_090_076_070_4grams_i_only"])
        self.assertEqual(
            lock["i_extra_090_076_070_4grams_i_only"],
            STANDING_I_EXTRA_090_076_070_4GRAMS_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["not_assumed_hapax"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle169_site_4grams"])
        self.assertFalse(lock["same_as_cycle175_forward_4grams"])
        self.assertFalse(lock["same_as_cycle208_4gram"])
        self.assertTrue(lock["same_claim_shape_as_cycles_169_175"])
        self.assertTrue(lock["999_090_076_070_does_not_count"])
        self.assertTrue(lock["059_090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_999_090_076_site_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_076_071_076_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"]["i_4gram_999_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
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
        self.assertEqual(
            self.survey["i_leftover_999_090_076_site_4grams_i_only"]["cycle"], 169
        )
        self.assertTrue(
            self.survey["i_leftover_999_090_076_site_4grams_i_only"][
                "i_leftover_999_090_076_site_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_076_071_076_forward_4grams_i_only"]["cycle"], 175)
        self.assertTrue(
            self.survey["i_076_071_076_forward_4grams_i_only"][
                "i_076_071_076_forward_4grams_i_only"
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


class TestMamariIExtra0900760704gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 209 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
