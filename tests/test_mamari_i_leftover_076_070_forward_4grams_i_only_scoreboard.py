"""I's cycle-216 leftover 2-gram forward-4-grams off-I lock.

Cycle 217 text-search lock. Uses already-vendored A–V and the
cycle-216 leftover I sites of 2-gram 076 070 (the I sites that
are not 090-prefixed 090 076 070). Does not retune those
4-grams, the leftover 11, the leftover n=4 set, or the
cycle-216 next-stem inventory. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same leftover-shape as cycle 189 (leftover 076 071 remaining
forward 4-grams all I-only hapax 1/0) and cycle 215 (leftover
076 070 remaining previous 4-grams all I-only hapax 1/0 x8).
Cycle 216 leftover share-one-forward-stem lost N_leftover=11 /
N_distinct=11, cycle 215 remaining previous 4-grams 8/8 I-only,
cycle 210 leftover share-one-previous-stem lost N_leftover=11
N_distinct=9, cycle 206 076 070 19/5 loss, and cycle 171
076 071 I-only 43/0 stay. Leftover = I 076 070 sites that are
NOT 090 076 070. Off-I 076 070 is not leftover. 076 071 is a
different 2-gram. Do not retune the leftover n=4 set.

Locks exact consecutive hits of each leftover forward 4-gram
on tablet I and on every other vendored tablet A–H and J–V.
The eleven 4-grams: 076 070 449 449, 076 070 560 072,
076 070 600 090, 076 070 430 061, 076 070 146 490,
076 070 305 999, 076 070 073 064, 076 070 701 214,
076 070 091 430, 076 070 076 670, 076 070 027 090.
Do not assume hapax; count each from fixtures. Hypothesis:
all eleven are I-only. Measured: each N_I=1 at the cycle-216
leftover site; all N_off_I=0. Claim that can lose:
i_leftover_076_070_forward_4grams_i_only.
True only if ALL eleven have N_off_I=0 and N_I>=1. The
claim is true. Do not assume hapax; measure. Do not retune.

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
from tests.test_mamari_i_2gram_076_070_i_only_scoreboard import (
    GRAM2 as CYCLE206_GRAM2,
    STANDING_I_SITES as CYCLE206_I_SITES,
    STANDING_N_I as CYCLE206_N_I,
    STANDING_N_OFF_I as CYCLE206_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE206_OFF_I_SITES,
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
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_forward_stem_scoreboard import (
    STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM as CYCLE216_SHARE_ONE,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE216_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE216_N_LEFTOVER,
    STANDING_N_NO_FORWARD as CYCLE216_N_NO_FORWARD,
    STANDING_PER_SITE_FORWARD_3GRAMS as CYCLE216_FORWARD_3GRAMS,
    STANDING_PER_SITE_NEXT_4GRAMS as CYCLE216_NEXT_4GRAMS,
    STANDING_PER_SITE_NEXT_STEMS as CYCLE216_NEXT_STEMS,
    leftover_forward_3grams,
    leftover_next_4grams,
    leftover_sites_without_forward,
    TestMamariILeftover076070ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_076_070_previous_stem_scoreboard import (
    GRAM2,
    PREFIXED_STEM,
    STANDING_I_LEFTOVER_076_070_SHARE_ONE_PREVIOUS_STEM as CYCLE210_SHARE_ONE,
    STANDING_LEFTOVER_SITES,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE210_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE210_N_LEFTOVER,
    STANDING_PREFIXED_I_SITES,
    TestMamariILeftover076070PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_076_070_remaining_previous_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_4GRAMS_I_ONLY as CYCLE215_I_ONLY,
    STANDING_N_I_EACH as CYCLE215_N_I_EACH,
    STANDING_N_OFF_I_EACH as CYCLE215_N_OFF_I_EACH,
    STANDING_N_REMAINING as CYCLE215_N_REMAINING,
    TestMamariILeftover076070RemainingPrevious4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    leftover_sites_without_forward as leftover_sites_without_forward_071,
    site_next_4gram,
    TestMamariILeftover076071Forward076Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_remaining_forward_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_I_ONLY as CYCLE189_I_ONLY,
    TestMamariILeftover076071RemainingForward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    NEAR_MISS_700_076_076_053,
    NEAR_MISS_999_090_076_071,
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
PREFIXED_3GRAM = CYCLE207_GRAM3
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_LEFTOVER = 11
STANDING_SEQUENCES = CYCLE216_NEXT_4GRAMS
STANDING_LEFTOVER_FORWARD_SITES = STANDING_LEFTOVER_SITES
STANDING_NEXT_STEMS = CYCLE216_NEXT_STEMS
STANDING_ROLES = ("leftover",) * STANDING_N_LEFTOVER
STANDING_N_I_EACH = (1,) * STANDING_N_LEFTOVER
STANDING_N_ON_I_EACH = (1,) * STANDING_N_LEFTOVER
STANDING_I_SITES = tuple((site,) for site in STANDING_LEFTOVER_FORWARD_SITES)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_LEFTOVER
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_EACH = True
STANDING_CLAIM = "i_leftover_076_070_forward_4grams_i_only"
STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_076_070_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE189_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE215_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE216 = False
STANDING_SAME_AS_CYCLE210 = False
STANDING_SAME_LEFTOVER_SHAPE_AS_189_AND_215 = True
STANDING_090_PREFIXED_DOES_NOT_COUNT = True
STANDING_OFF_I_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LOCKED_CLUSTER_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_PREVIOUS_SIDE_CLOSED = True


def leftover_forward_4gram_start_site(
    leftover_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-216 leftover 076 070 site."""
    return leftover_site


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_076_070_forward_4grams_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_LEFTOVER,
) -> bool:
    """True iff all 11 leftover forward 4-grams are I-only.

    Claim holds only if every gram has N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only. Hapax is not
    assumed; N_I may be greater than 1. Length must stay 11.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestILeftover076070Forward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-216 leftover forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 076 071 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("076", "070", "449", "449"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("076", "070", "027", "090"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_LEFTOVER)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:2], GRAM2)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["076", "070", "449", "449", "076", "070", "449", "449"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [list(STANDING_SEQUENCES[0][:2]) + ["000"] + list(STANDING_SEQUENCES[0][2:])]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(
            ngram_hit_count([list(NEAR_MISS_999_090_076_071)], STANDING_SEQUENCES[0]),
            0,
        )
        self.assertEqual(
            ngram_hit_count([list(NEAR_MISS_700_076_076_053)], STANDING_SEQUENCES[-1]),
            0,
        )
        self.assertEqual(ngram_hit_count([["076", "071"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["076", "076"]], STANDING_SEQUENCES[-1]), 0)
        self.assertEqual(ngram_hit_count([["076", "070", "449"]], STANDING_SEQUENCES[0]), 0)
        planted = ["099", "571", "076", "070", "449", "449"]
        self.assertEqual(site_next_4gram(planted, 2, GRAM2), STANDING_SEQUENCES[0])
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all 11 leftover forward 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_076_070_forward_4grams_i_only(hold_ones, hold_zeros)
        )
        self.assertTrue(
            i_leftover_076_070_forward_4grams_i_only(
                (2,) + hold_ones[1:],
                hold_zeros,
            )
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_leftover_076_070_forward_4grams_i_only(
                hold_ones,
                tuple(lose_off),
            )
        )
        lose_off_mid = list(hold_zeros)
        lose_off_mid[5] = 1
        self.assertFalse(
            i_leftover_076_070_forward_4grams_i_only(
                hold_ones,
                tuple(lose_off_mid),
            )
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_leftover_076_070_forward_4grams_i_only(
                tuple(lose_missing_i),
                hold_zeros,
            )
        )
        self.assertFalse(i_leftover_076_070_forward_4grams_i_only((), ()))
        self.assertFalse(
            i_leftover_076_070_forward_4grams_i_only(
                hold_ones[:-1],
                hold_zeros[:-1],
            )
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_070_forward_4grams_i_only")
        self.assertTrue(STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_216_leftover_forwards_not_retuned(self):
        """4-grams stay the cycle-216 leftover forwards; none is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM2, CYCLE206_GRAM2)
        self.assertEqual(STANDING_SEQUENCES, CYCLE216_NEXT_4GRAMS)
        self.assertEqual(STANDING_NEXT_STEMS, CYCLE216_NEXT_STEMS)
        self.assertEqual(STANDING_LEFTOVER_FORWARD_SITES, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE216_N_LEFTOVER)
        self.assertEqual(CYCLE216_N_LEFTOVER, 11)
        self.assertEqual(CYCLE216_N_DISTINCT, 11)
        self.assertEqual(len(set(STANDING_NEXT_STEMS)), 11)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_999_090_076_071))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_700_076_076_053))
            self.assertNotEqual(gram[:3], PREFIXED_3GRAM)
            self.assertNotEqual(gram[:2], CYCLE171_GRAM2)
        for site, start in zip(
            STANDING_LEFTOVER_FORWARD_SITES,
            (sites[0] for sites in STANDING_I_SITES),
            strict=True,
        ):
            self.assertEqual(leftover_forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE189_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE215_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE216)
        self.assertFalse(STANDING_SAME_AS_CYCLE210)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_189_AND_215)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_PREVIOUS_SIDE_CLOSED)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076070Forward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 076 070 forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_FORWARD_SITES
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
        self.measured_leftover_next_4grams = leftover_next_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.forwards = leftover_forward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.no_forward = leftover_sites_without_forward(
            self.leftover_sites,
            self.forwards,
        )
        self.claim_holds = i_leftover_076_070_forward_4grams_i_only(
            self.n_i,
            self.n_off_i,
        )

    def test_tokens_and_sites_are_cycle_216_leftover_not_retuned(self):
        """4-grams and I sites stay the cycle-216 leftover forward lock."""
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM2, CYCLE206_GRAM2)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_FORWARD_SITES)
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.measured_leftover_next_4grams, STANDING_SEQUENCES)
        self.assertEqual(self.measured_leftover_next_4grams, CYCLE216_NEXT_4GRAMS)
        self.assertEqual(self.no_forward, ())
        self.assertEqual(self.forwards, CYCLE216_FORWARD_3GRAMS)
        prior_216 = self.survey["i_leftover_076_070_forward_stem"]
        self.assertEqual(prior_216["cycle"], 216)
        self.assertEqual(prior_216["N_leftover"], CYCLE216_N_LEFTOVER)
        self.assertEqual(prior_216["N_leftover"], 11)
        self.assertEqual(prior_216["N_distinct_next_stems"], CYCLE216_N_DISTINCT)
        self.assertEqual(prior_216["N_distinct_next_stems"], 11)
        self.assertEqual(prior_216["N_no_forward"], CYCLE216_N_NO_FORWARD)
        self.assertEqual(prior_216["N_no_forward"], 0)
        self.assertFalse(prior_216["i_leftover_076_070_share_one_forward_stem"])
        self.assertFalse(CYCLE216_SHARE_ONE)
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_216["per_site_next_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_216["leftover_sites"]),
            STANDING_LEFTOVER_FORWARD_SITES,
        )
        self.assertEqual(tuple(prior_216["per_site_next_stems"]), STANDING_NEXT_STEMS)
        prior_215 = self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"]
        self.assertEqual(prior_215["cycle"], 215)
        self.assertTrue(prior_215["i_leftover_076_070_remaining_previous_4grams_i_only"])
        self.assertTrue(CYCLE215_I_ONLY)
        self.assertEqual(prior_215["N_remaining"], CYCLE215_N_REMAINING)
        self.assertEqual(prior_215["N_remaining"], 8)
        self.assertEqual(tuple(prior_215["N_I_each"]), CYCLE215_N_I_EACH)
        self.assertEqual(tuple(prior_215["N_off_I_each"]), CYCLE215_N_OFF_I_EACH)
        self.assertEqual(prior_215["N_i_only"], 8)
        self.assertEqual(prior_215["N_not_i_only"], 0)
        prior_210 = self.survey["i_leftover_076_070_previous_stem"]
        self.assertEqual(prior_210["cycle"], 210)
        self.assertEqual(prior_210["N_leftover"], CYCLE210_N_LEFTOVER)
        self.assertEqual(prior_210["N_leftover"], 11)
        self.assertEqual(prior_210["N_distinct_previous_stems"], CYCLE210_N_DISTINCT)
        self.assertEqual(prior_210["N_distinct_previous_stems"], 9)
        self.assertFalse(prior_210["i_leftover_076_070_share_one_previous_stem"])
        self.assertFalse(CYCLE210_SHARE_ONE)
        prior_206 = self.survey["i_2gram_076_070_i_only"]
        self.assertEqual(prior_206["cycle"], 206)
        self.assertFalse(prior_206["i_2gram_076_070_i_only"])
        self.assertEqual(prior_206["N_I"], CYCLE206_N_I)
        self.assertEqual(prior_206["N_I"], 19)
        self.assertEqual(prior_206["N_off_I"], CYCLE206_N_OFF_I)
        self.assertEqual(prior_206["N_off_I"], 5)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], CYCLE171_N_I)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], CYCLE171_N_OFF_I)
        self.assertEqual(prior_171["N_off_I"], 0)
        prior_189 = self.survey["i_leftover_076_071_remaining_forward_4grams_i_only"]
        self.assertEqual(prior_189["cycle"], 189)
        self.assertTrue(prior_189["i_leftover_076_071_remaining_forward_4grams_i_only"])
        self.assertTrue(CYCLE189_I_ONLY)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_PREVIOUS_SIDE_CLOSED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """Each leftover forward 4-gram is N_I=1, N_off_I=0. All I-only. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (1,) * STANDING_N_LEFTOVER)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0,) * STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(STANDING_OFF_I_SITES, ())
        self.assertEqual(len(self.grams), STANDING_N_LEFTOVER)
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from 0")
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked leftover hapax")
        for site, start, gram, nxt, role, sites, n_on, n_off in zip(
            STANDING_LEFTOVER_FORWARD_SITES,
            (row[0] for row in STANDING_I_SITES),
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            strict=True,
        ):
            self.assertEqual(leftover_forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
            self.assertEqual(sites, (start,))
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2] + STANDING_N2], nxt)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N2]), GRAM2)
            self.assertEqual(site_next_4gram(stems, start[2], GRAM2), gram)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram[:3], PREFIXED_3GRAM)
            self.assertEqual(role, "leftover")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertNotIn(site, STANDING_PREFIXED_I_SITES)
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        for n_on, locked in zip(self.n_i, STANDING_N_I_EACH, strict=True):
            if n_on != locked:
                self.fail("measured N_I drifted from the locked count")
        if not self.claim_holds:
            self.fail("measured leftover forward 4-grams are not all I-only")
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_EACH)
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
            i_leftover_076_070_forward_4grams_i_only(
                self.n_i,
                self.n_off_i,
            ),
            STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_070_forward_4grams_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE189_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE215_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE216)
        self.assertFalse(STANDING_SAME_AS_CYCLE210)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_189_AND_215)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LOCKED_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_PREVIOUS_SIDE_CLOSED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        for site in STANDING_PREFIXED_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_FORWARD_SITES)
        for site in CYCLE206_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_FORWARD_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_216_215_210_206_and_171_scoreboards_still_compute(self):
        """Cycle 216 11/11, 215 8/8, 210 11/9, 206 19/5, 171 43/0 stay."""
        prior_216 = TestMamariILeftover076070ForwardStemScoreboard()
        prior_216.setUp()
        prior_216.test_counts_11_distinct_next_stems_and_claim_loses()
        prior_216.test_survey_matches_computed_lock()
        self.assertEqual(prior_216.n_leftover, CYCLE216_N_LEFTOVER)
        self.assertEqual(prior_216.n_leftover, 11)
        self.assertEqual(prior_216.n_distinct, CYCLE216_N_DISTINCT)
        self.assertEqual(prior_216.n_distinct, 11)
        self.assertFalse(prior_216.claim_holds)
        self.assertFalse(CYCLE216_SHARE_ONE)
        if prior_216.n_leftover != 11 or prior_216.n_distinct != 11:
            self.fail("nested cycle 216 leftover/distinct drifted")
        prior_215 = TestMamariILeftover076070RemainingPrevious4gramsIOnlyScoreboard()
        prior_215.setUp()
        prior_215.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_215.test_survey_matches_computed_lock()
        self.assertEqual(prior_215.n_i, CYCLE215_N_I_EACH)
        self.assertEqual(prior_215.n_off_i, CYCLE215_N_OFF_I_EACH)
        self.assertTrue(prior_215.claim_holds)
        self.assertTrue(CYCLE215_I_ONLY)
        self.assertEqual(CYCLE215_N_REMAINING, 8)
        self.assertEqual(sum(CYCLE215_N_I_EACH), 8)
        self.assertEqual(sum(CYCLE215_N_OFF_I_EACH), 0)
        prior_210 = TestMamariILeftover076070PreviousStemScoreboard()
        prior_210.setUp()
        prior_210.test_counts_9_distinct_previous_stems_and_claim_loses()
        prior_210.test_survey_matches_computed_lock()
        self.assertEqual(prior_210.n_leftover, CYCLE210_N_LEFTOVER)
        self.assertEqual(prior_210.n_leftover, 11)
        self.assertEqual(prior_210.n_distinct, CYCLE210_N_DISTINCT)
        self.assertEqual(prior_210.n_distinct, 9)
        self.assertFalse(prior_210.claim_holds)
        if prior_210.n_leftover != 11 or prior_210.n_distinct != 9:
            self.fail("nested cycle 210 leftover/distinct drifted")
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        self.assertEqual(prior_206.i_hits, 19)
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
        prior_189 = TestMamariILeftover076071RemainingForward4gramsIOnlyScoreboard()
        prior_189.setUp()
        prior_189.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_189.test_survey_matches_computed_lock()
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        prior_173 = TestMamariILeftover076071Forward076Scoreboard()
        prior_173.setUp()
        prior_173.test_counts_5_of_34_and_hypothesis_n_5_holds()
        prior_173.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        unused = leftover_sites_without_forward_071
        self.assertTrue(callable(unused))
        self.assertEqual(PREFIXED_STEM, "090")
        self.assertEqual(len(CYCLE206_I_SITES), 19)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-217 leftover-forward-4 I-only lock."""
        lock = self.survey["i_leftover_076_070_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 217)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], CYCLE206_N_I)
        self.assertEqual(lock["N_I"], 19)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 11)
        self.assertEqual(lock["N_leftover"], CYCLE216_N_LEFTOVER)
        self.assertEqual(lock["N_distinct_next_stems"], CYCLE216_N_DISTINCT)
        self.assertEqual(lock["N_distinct_next_stems"], 11)
        self.assertEqual(lock["N_no_forward"], CYCLE216_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_FORWARD_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["leftover_next_4grams"],
        )
        self.assertEqual(tuple(lock["leftover_next_stems"]), STANDING_NEXT_STEMS)
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_LEFTOVER)
        for row, gram, site, nxt, role, sites, n_on, n_off in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_LEFTOVER_FORWARD_SITES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle216_site"]), site)
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
            self.assertTrue(row["hapax"])
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_076_070_forward_4grams_i_only"])
        self.assertEqual(
            lock["i_leftover_076_070_forward_4grams_i_only"],
            STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertEqual(lock["N_i_only"], 11)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle189_forward_4grams"])
        self.assertFalse(lock["same_as_cycle215_previous_4grams"])
        self.assertFalse(lock["same_as_cycle216"])
        self.assertFalse(lock["same_as_cycle210"])
        self.assertTrue(lock["same_leftover_shape_as_cycle_189_and_215"])
        self.assertTrue(lock["090_prefixed_does_not_count"])
        self.assertTrue(lock["off_i_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["locked_cluster_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["previous_side_closed"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_076_070_forward_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_076_070_remaining_previous_4grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_076_070_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_076_071_remaining_forward_4grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_076_070_forward_stem"]["cycle"], 216)
        self.assertEqual(self.survey["i_leftover_076_070_forward_stem"]["N_leftover"], 11)
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_stem"]["N_distinct_next_stems"],
            11,
        )
        self.assertFalse(
            self.survey["i_leftover_076_070_forward_stem"][
                "i_leftover_076_070_share_one_forward_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"]["cycle"],
            215,
        )
        self.assertTrue(
            self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"][
                "i_leftover_076_070_remaining_previous_4grams_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"][
                "N_i_only"
            ],
            8,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"][
                "N_not_i_only"
            ],
            0,
        )
        self.assertEqual(self.survey["i_leftover_076_070_previous_stem"]["cycle"], 210)
        self.assertEqual(self.survey["i_leftover_076_070_previous_stem"]["N_leftover"], 11)
        self.assertEqual(
            self.survey["i_leftover_076_070_previous_stem"]["N_distinct_previous_stems"],
            9,
        )
        self.assertFalse(
            self.survey["i_leftover_076_070_previous_stem"][
                "i_leftover_076_070_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_forward_4grams_i_only"]["cycle"],
            189,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_remaining_forward_4grams_i_only"][
                "i_leftover_076_071_remaining_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"][
                "i_leftover_n4_exactly_1_contain_076_070"
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


class TestMamariILeftover076070Forward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 217 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
