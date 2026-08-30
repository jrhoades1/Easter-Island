"""I's cycle-218 090 076 070 forward-4-grams off-I lock.

Cycle 219 text-search lock. Uses already-vendored A–V and the
cycle-218 I sites of 3-gram 090 076 070 (all 8 I sites; each
has a next stem). Does not retune those 4-grams, the 8 I
sites, the leftover n=4 set, or the already-closed leftover
076 070 that is not 090 076 070. Does not vendor a new
tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or
G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Same claim-shape as cycle 217 (leftover 076 070 forward
4-grams all I-only hapax 1/0 x11). Cycle 218 I 090 076 070
share-one-forward-stem lost N_I=8 / N_distinct=8, cycle 217
leftover forward 4-grams 11/11 I-only, cycle 208 leftover
4-gram 999 090 076 070 I-only 5/0, cycle 207 090 076 070 8/1
loss, and cycle 171 076 071 I-only 43/0 stay. Off-I
090 076 070 (Ta9[2] 059 090 076 070) is not one of the 8 I
sites. Leftover 076 070 that is not 090 076 070 is a
different leftover (already closed). 090 076 071 is a
different 3-gram. Do not retune the leftover n=4 set.

Locks exact consecutive hits of each I 090 076 070 forward
4-gram on tablet I and on every other vendored tablet A–H
and J–V. The eight 4-grams: 090 076 070 499, 090 076 070 200,
090 076 070 600, 090 076 070 027, 090 076 070 532,
090 076 070 071, 090 076 070 073, 090 076 070 000.
Do not assume hapax; count each from fixtures. Hypothesis:
all eight are I-only. Measured: each N_I=1 at the cycle-218
I site; seven N_off_I=0; 090 076 070 000 is N_off_I=1 on T
(Ta9[2]). Claim that can lose:
i_090_076_070_forward_4grams_i_only.
True only if ALL eight have N_off_I=0 and N_I>=1. The
claim is false (7/8). Do not assume the I-only result;
measure. Do not retune.

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
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3,
    STANDING_I_3GRAM_090_076_070_I_ONLY as CYCLE207_I_ONLY,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_PREVIOUS_4GRAM as CYCLE207_OFF_I_PREVIOUS_4GRAM,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
    named_off_i_sites as cycle207_named_off_i_sites,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
)
from tests.test_mamari_i_4gram_999_090_076_070_i_only_scoreboard import (
    GRAM4 as CYCLE208_GRAM4,
    STANDING_I_4GRAM_999_090_076_070_I_ONLY as CYCLE208_I_ONLY,
    STANDING_N_I as CYCLE208_N_I,
    STANDING_N_OFF_I as CYCLE208_N_OFF_I,
    TestMamariI4gram999090076070IOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_stem_scoreboard import (
    STANDING_I_090_076_070_SHARE_ONE_FORWARD_STEM as CYCLE218_SHARE_ONE,
    STANDING_I_SITES as CYCLE218_I_SITES,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE218_N_DISTINCT,
    STANDING_N_I as CYCLE218_N_I,
    STANDING_N_NO_FORWARD as CYCLE218_N_NO_FORWARD,
    STANDING_PER_SITE_FORWARD_4GRAMS as CYCLE218_FORWARD_4GRAMS,
    STANDING_PER_SITE_NEXT_5GRAMS as CYCLE218_NEXT_5GRAMS,
    STANDING_PER_SITE_NEXT_STEMS as CYCLE218_NEXT_STEMS,
    i_090_076_070_forward_4grams,
    i_090_076_070_next_5grams,
    i_sites_without_forward,
    site_forward_4gram,
    site_next_5gram,
    TestMamariI090076070ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE217_I_ONLY,
    STANDING_N_I_EACH as CYCLE217_N_I_EACH,
    STANDING_N_LEFTOVER as CYCLE217_N_LEFTOVER,
    STANDING_N_OFF_I_EACH as CYCLE217_N_OFF_I_EACH,
    TestMamariILeftover076070Forward4gramsIOnlyScoreboard,
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
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N5 = 5
STANDING_N_I = 8
STANDING_N_SEQUENCES = 8
STANDING_SEQUENCES = CYCLE218_FORWARD_4GRAMS
STANDING_CYCLE218_SITES = CYCLE218_I_SITES
STANDING_NEXT_STEMS = CYCLE218_NEXT_STEMS
STANDING_ROLES = ("forward",) * STANDING_N_SEQUENCES
STANDING_N_I_EACH = (1,) * STANDING_N_SEQUENCES
STANDING_N_ON_I_EACH = (1,) * STANDING_N_SEQUENCES
STANDING_I_SITES = tuple((site,) for site in STANDING_CYCLE218_SITES)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0, 0, 0, 0, 0, 0, 0, 1)
STANDING_OFF_I_SITES_000 = ((SIDE_TA, "Ta9", 2),)
STANDING_OFF_I_SITES = (
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    STANDING_OFF_I_SITES_000,
)
STANDING_OFF_I_PREVIOUS_4GRAM = CYCLE207_OFF_I_PREVIOUS_4GRAM
STANDING_OFF_I_FORWARD_4GRAM = ("090", "076", "070", "000")
STANDING_OFF_I_BY_TABLET_ZERO = (0,) * len(OFF_I_TABLETS)
STANDING_OFF_I_BY_TABLET_000 = tuple(
    1 if tablet == "T" else 0 for tablet in OFF_I_TABLETS
)
STANDING_OFF_I_BY_TABLET = (
    STANDING_OFF_I_BY_TABLET_ZERO,
    STANDING_OFF_I_BY_TABLET_ZERO,
    STANDING_OFF_I_BY_TABLET_ZERO,
    STANDING_OFF_I_BY_TABLET_ZERO,
    STANDING_OFF_I_BY_TABLET_ZERO,
    STANDING_OFF_I_BY_TABLET_ZERO,
    STANDING_OFF_I_BY_TABLET_ZERO,
    STANDING_OFF_I_BY_TABLET_000,
)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET_000 = tuple(
    1 if tablet in ("I", "T") else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (
    STANDING_HITS_BY_TABLET_ONE_ON_I,
    STANDING_HITS_BY_TABLET_ONE_ON_I,
    STANDING_HITS_BY_TABLET_ONE_ON_I,
    STANDING_HITS_BY_TABLET_ONE_ON_I,
    STANDING_HITS_BY_TABLET_ONE_ON_I,
    STANDING_HITS_BY_TABLET_ONE_ON_I,
    STANDING_HITS_BY_TABLET_ONE_ON_I,
    STANDING_HITS_BY_TABLET_000,
)
STANDING_N_I_ONLY = 7
STANDING_N_NOT_I_ONLY = 1
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_EACH = True
STANDING_CLAIM = "i_090_076_070_forward_4grams_i_only"
STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY = False
STANDING_RESULT = "i_090_076_070_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = False
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE217 = False
STANDING_SAME_AS_CYCLE218 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE217 = True
STANDING_OFF_I_3GRAM_DOES_NOT_COUNT_AS_I_SITE = True
STANDING_LEFTOVER_076_070_NOT_090_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_076_070_SIDES_CLOSED = True


def forward_4gram_start_site(
    cycle218_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-218 I 090 076 070 site."""
    return cycle218_site


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_090_076_070_forward_4grams_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_SEQUENCES,
) -> bool:
    """True iff all 8 I 090 076 070 forward 4-grams are I-only.

    Claim holds only if every gram has N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only. Hapax is not
    assumed; N_I may be greater than 1. Length must stay 8.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestI090076070Forward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-218 I 090 076 070 forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 071 / leftover 076 070 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "070", "499"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("090", "076", "070", "000"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_SEQUENCES)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:3], GRAM3)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["090", "076", "070", "499", "090", "076", "070", "499"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [
            list(STANDING_SEQUENCES[0][:2])
            + ["000"]
            + list(STANDING_SEQUENCES[0][2:])
        ]
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
        self.assertEqual(ngram_hit_count([list(CYCLE195_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["076", "070", "449", "449"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(
            ngram_hit_count([list(STANDING_OFF_I_PREVIOUS_4GRAM)], STANDING_OFF_I_FORWARD_4GRAM),
            0,
        )
        t_forward = ["059", "090", "076", "070", "000"]
        self.assertEqual(ngram_hit_count([t_forward], STANDING_OFF_I_FORWARD_4GRAM), 1)
        self.assertEqual(ngram_hit_count([t_forward], STANDING_OFF_I_PREVIOUS_4GRAM), 1)
        planted = ["999", "090", "076", "070", "499", "090"]
        self.assertEqual(site_forward_4gram(planted, 1, GRAM3), STANDING_SEQUENCES[0])
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_076_070_NOT_090_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all 8 forward 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = (0,) * STANDING_N_SEQUENCES
        self.assertTrue(i_090_076_070_forward_4grams_i_only(hold_ones, hold_zeros))
        self.assertTrue(
            i_090_076_070_forward_4grams_i_only((2,) + hold_ones[1:], hold_zeros)
        )
        self.assertFalse(
            i_090_076_070_forward_4grams_i_only(hold_ones, STANDING_N_OFF_I_EACH)
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_090_076_070_forward_4grams_i_only(hold_ones, tuple(lose_off))
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_090_076_070_forward_4grams_i_only(tuple(lose_missing_i), hold_zeros)
        )
        self.assertFalse(i_090_076_070_forward_4grams_i_only((), ()))
        self.assertFalse(
            i_090_076_070_forward_4grams_i_only(hold_ones[:-1], hold_zeros[:-1])
        )
        self.assertEqual(STANDING_CLAIM, "i_090_076_070_forward_4grams_i_only")
        self.assertFalse(STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY)
        self.assertNotEqual(
            STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_218_forwards_not_retuned(self):
        """4-grams stay the cycle-218 I forwards; leftover / 071 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "070"))
        self.assertEqual(STANDING_SEQUENCES, CYCLE218_FORWARD_4GRAMS)
        self.assertEqual(STANDING_NEXT_STEMS, CYCLE218_NEXT_STEMS)
        self.assertEqual(STANDING_CYCLE218_SITES, CYCLE218_I_SITES)
        self.assertEqual(STANDING_CYCLE218_SITES, CYCLE207_I_SITES)
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE218_N_I)
        self.assertEqual(CYCLE218_N_I, 8)
        self.assertEqual(CYCLE218_N_DISTINCT, 8)
        self.assertEqual(len(set(STANDING_NEXT_STEMS)), 8)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(CYCLE195_GRAM3, ("090", "076", "071"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(CYCLE195_GRAM3, gram))
            self.assertNotEqual(gram[:3], CYCLE195_GRAM3)
            self.assertNotEqual(gram[:2], CYCLE171_GRAM2)
            self.assertNotEqual(gram, CYCLE208_GRAM4)
        for site, start in zip(
            STANDING_CYCLE218_SITES,
            (sites[0] for sites in STANDING_I_SITES),
            strict=True,
        ):
            self.assertEqual(forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE217)
        self.assertFalse(STANDING_SAME_AS_CYCLE218)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE217)
        self.assertTrue(STANDING_OFF_I_3GRAM_DOES_NOT_COUNT_AS_I_SITE)
        self.assertTrue(STANDING_LEFTOVER_076_070_NOT_090_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI090076070Forward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture I 090 076 070 forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle218_sites = STANDING_CYCLE218_SITES
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
        self.measured_forwards = i_090_076_070_forward_4grams(
            self.i_sides,
            self.cycle218_sites,
            GRAM3,
        )
        self.next_5grams = i_090_076_070_next_5grams(
            self.i_sides,
            self.cycle218_sites,
            GRAM3,
        )
        self.no_forward = i_sites_without_forward(
            self.cycle218_sites,
            tuple(gram[3] if gram else None for gram in self.measured_forwards),
        )
        self.claim_holds = i_090_076_070_forward_4grams_i_only(
            self.n_i,
            self.n_off_i,
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = STANDING_N_SEQUENCES - self.n_i_only

    def test_tokens_and_sites_are_cycle_218_forwards_not_retuned(self):
        """4-grams and I sites stay the cycle-218 forward lock. Nested 8 must hold."""
        self.assertEqual(GRAM3, ("090", "076", "070"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle218_sites, STANDING_CYCLE218_SITES)
        self.assertEqual(self.cycle218_sites, CYCLE218_I_SITES)
        self.assertEqual(self.cycle218_sites, CYCLE207_I_SITES)
        self.assertEqual(self.measured_forwards, STANDING_SEQUENCES)
        self.assertEqual(self.measured_forwards, CYCLE218_FORWARD_4GRAMS)
        self.assertEqual(self.no_forward, ())
        self.assertEqual(self.next_5grams, CYCLE218_NEXT_5GRAMS)
        prior_218 = self.survey["i_090_076_070_forward_stem"]
        self.assertEqual(prior_218["cycle"], 218)
        self.assertEqual(prior_218["N_I"], CYCLE218_N_I)
        self.assertEqual(prior_218["N_I"], 8)
        self.assertEqual(prior_218["N_distinct_next_stems"], CYCLE218_N_DISTINCT)
        self.assertEqual(prior_218["N_distinct_next_stems"], 8)
        self.assertEqual(prior_218["N_no_forward"], CYCLE218_N_NO_FORWARD)
        self.assertEqual(prior_218["N_no_forward"], 0)
        self.assertFalse(prior_218["i_090_076_070_share_one_forward_stem"])
        self.assertFalse(CYCLE218_SHARE_ONE)
        if prior_218["N_I"] != 8 or prior_218["N_distinct_next_stems"] != 8:
            self.fail("nested cycle 218 N_I=8 / N_distinct=8 drifted")
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_218["per_site_forward_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_218["i_sites"]),
            STANDING_CYCLE218_SITES,
        )
        self.assertEqual(tuple(prior_218["per_site_next_stems"]), STANDING_NEXT_STEMS)
        prior_217 = self.survey["i_leftover_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_217["cycle"], 217)
        self.assertTrue(prior_217["i_leftover_076_070_forward_4grams_i_only"])
        self.assertTrue(CYCLE217_I_ONLY)
        self.assertEqual(prior_217["N_leftover"], CYCLE217_N_LEFTOVER)
        self.assertEqual(prior_217["N_leftover"], 11)
        self.assertEqual(tuple(prior_217["N_I_each"]), CYCLE217_N_I_EACH)
        self.assertEqual(tuple(prior_217["N_off_I_each"]), CYCLE217_N_OFF_I_EACH)
        self.assertEqual(prior_217["N_i_only"], 11)
        self.assertEqual(prior_217["N_not_i_only"], 0)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], CYCLE207_N_I)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], CYCLE207_N_OFF_I)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertFalse(CYCLE207_I_ONLY)
        prior_208 = self.survey["i_4gram_999_090_076_070_i_only"]
        self.assertEqual(prior_208["cycle"], 208)
        self.assertTrue(prior_208["i_4gram_999_090_076_070_i_only"])
        self.assertTrue(CYCLE208_I_ONLY)
        self.assertEqual(prior_208["N_I"], CYCLE208_N_I)
        self.assertEqual(prior_208["N_I"], 5)
        self.assertEqual(prior_208["N_off_I"], CYCLE208_N_OFF_I)
        self.assertEqual(prior_208["N_off_I"], 0)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], CYCLE171_N_I)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], CYCLE171_N_OFF_I)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_3GRAM_DOES_NOT_COUNT_AS_I_SITE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_076_070_SIDES_CLOSED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_lock_and_claim_loses_on_000(self):
        """Seven 4-grams are 1/0; 090 076 070 000 is 1/1 on T. Claim loses."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (1,) * STANDING_N_SEQUENCES)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0, 0, 0, 0, 0, 0, 0, 1))
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(len(self.grams), STANDING_N_SEQUENCES)
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked hapax")
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from the locked 7/8 split")
        for site, start, gram, nxt, role, sites, n_on, n_off, off_sites in zip(
            STANDING_CYCLE218_SITES,
            (row[0] for row in STANDING_I_SITES),
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_OFF_I_SITES,
            strict=True,
        ):
            self.assertEqual(forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
            self.assertEqual(sites, (start,))
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2] + STANDING_N3], nxt)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N3]), GRAM3)
            self.assertEqual(site_forward_4gram(stems, start[2], GRAM3), gram)
            self.assertEqual(
                site_next_5gram(stems, start[2], GRAM3)[:4],
                gram,
            )
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram[:3], CYCLE195_GRAM3)
            self.assertEqual(role, "forward")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0 if gram != STANDING_OFF_I_FORWARD_4GRAM else 1)
            self.assertEqual(sequence_is_i_only(n_on, n_off), n_off == 0)
            self.assertNotIn(site, CYCLE207_OFF_I_SITES)
            self.assertEqual(off_sites, STANDING_OFF_I_SITES_000 if n_off else ())
        if self.n_i_only != STANDING_N_I_ONLY:
            self.fail("measured N_i_only drifted from 7")
        if self.n_not_i_only != STANDING_N_NOT_I_ONLY:
            self.fail("measured N_not_i_only drifted from 1")
        if self.claim_holds:
            self.fail("measured forward 4-grams are not all I-only")
        self.assertEqual(self.n_i_only, 7)
        self.assertEqual(self.n_not_i_only, 1)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_EACH)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off, expected_hits, expected_off in zip(
            self.hits_by_tablet,
            self.off_i,
            STANDING_HITS_BY_TABLET,
            STANDING_OFF_I_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(hits, expected_hits)
            self.assertEqual(off, expected_off)
        for tablet, *counts in zip(
            VENDORED_TABLETS,
            *self.hits_by_tablet,
            strict=True,
        ):
            for count, gram, expected in zip(
                counts,
                self.grams,
                (row[VENDORED_TABLETS.index(tablet)] for row in STANDING_HITS_BY_TABLET),
                strict=True,
            ):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                self.assertEqual(count, expected)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM3), 1)
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], STANDING_OFF_I_FORWARD_4GRAM), 1)
        for gram in STANDING_SEQUENCES[:-1]:
            self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], gram), 0)
        off_side, off_line, off_index = STANDING_OFF_I_SITES_000[0]
        off_stems = t_sides[off_side][TA_LINE_NAMES.index(off_line)]
        self.assertEqual(
            tuple(off_stems[off_index : off_index + STANDING_N4]),
            STANDING_OFF_I_FORWARD_4GRAM,
        )
        self.assertEqual(
            tuple(off_stems[off_index : off_index + STANDING_N3]),
            GRAM3,
        )
        self.assertEqual(
            tuple(off_stems[off_index - 1 : off_index + STANDING_N3]),
            STANDING_OFF_I_PREVIOUS_4GRAM,
        )
        self.assertEqual(STANDING_OFF_I_PREVIOUS_4GRAM, ("059", "090", "076", "070"))
        self.assertEqual(CYCLE207_OFF_I_SITES, STANDING_OFF_I_SITES_000)
        self.assertNotIn(CYCLE207_OFF_I_SITES[0], STANDING_CYCLE218_SITES)
        self.assertEqual(
            i_090_076_070_forward_4grams_i_only(self.n_i, self.n_off_i),
            STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertFalse(self.claim_holds)
        self.assertFalse(STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_090_076_070_forward_4grams_i_only")
        self.assertFalse(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE217)
        self.assertFalse(STANDING_SAME_AS_CYCLE218)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE217)
        self.assertTrue(STANDING_OFF_I_3GRAM_DOES_NOT_COUNT_AS_I_SITE)
        self.assertTrue(STANDING_LEFTOVER_076_070_NOT_090_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_076_070_SIDES_CLOSED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, CYCLE195_GRAM3)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_218_217_207_208_and_171_scoreboards_still_compute(self):
        """Cycle 218 8/8, 217 11/11, 207 8/1, 208 5/0, 171 43/0 stay."""
        prior_218 = TestMamariI090076070ForwardStemScoreboard()
        prior_218.setUp()
        prior_218.test_counts_8_distinct_next_stems_and_claim_loses()
        prior_218.test_survey_matches_computed_lock()
        self.assertEqual(prior_218.n_i, CYCLE218_N_I)
        self.assertEqual(prior_218.n_i, 8)
        self.assertEqual(prior_218.n_distinct, CYCLE218_N_DISTINCT)
        self.assertEqual(prior_218.n_distinct, 8)
        self.assertFalse(prior_218.claim_holds)
        self.assertFalse(CYCLE218_SHARE_ONE)
        if prior_218.n_i != 8 or prior_218.n_distinct != 8:
            self.fail("nested cycle 218 N_I=8 / N_distinct=8 drifted")
        prior_217 = TestMamariILeftover076070Forward4gramsIOnlyScoreboard()
        prior_217.setUp()
        prior_217.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_217.test_survey_matches_computed_lock()
        self.assertEqual(prior_217.n_i, CYCLE217_N_I_EACH)
        self.assertEqual(prior_217.n_off_i, CYCLE217_N_OFF_I_EACH)
        self.assertTrue(prior_217.claim_holds)
        self.assertTrue(CYCLE217_I_ONLY)
        self.assertEqual(CYCLE217_N_LEFTOVER, 11)
        self.assertEqual(sum(CYCLE217_N_I_EACH), 11)
        self.assertEqual(sum(CYCLE217_N_OFF_I_EACH), 0)
        if sum(CYCLE217_N_I_EACH) != 11 or sum(CYCLE217_N_OFF_I_EACH) != 0:
            self.fail("nested cycle 217 leftover forward 4-grams 11/11 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 8/1 drifted")
        prior_208 = TestMamariI4gram999090076070IOnlyScoreboard()
        prior_208.setUp()
        prior_208.test_4gram_is_zero_off_i_and_i_only()
        prior_208.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE208_N_I, 5)
        self.assertEqual(CYCLE208_N_OFF_I, 0)
        self.assertTrue(CYCLE208_I_ONLY)
        if CYCLE208_N_I != 5 or CYCLE208_N_OFF_I != 0:
            self.fail("nested cycle 208 5/0 drifted")
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
        """CORPUS_SURVEY.json records the cycle-219 I-forward-4 I-only loss."""
        lock = self.survey["i_090_076_070_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 219)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 8)
        self.assertEqual(lock["N_I"], CYCLE218_N_I)
        self.assertEqual(lock["N_I"], CYCLE207_N_I)
        self.assertEqual(lock["N_sequences"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_distinct_next_stems"], CYCLE218_N_DISTINCT)
        self.assertEqual(lock["N_distinct_next_stems"], 8)
        self.assertEqual(lock["N_no_forward"], CYCLE218_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_CYCLE218_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["per_site_forward_4grams"],
        )
        self.assertEqual(tuple(lock["per_site_next_stems"]), STANDING_NEXT_STEMS)
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_SEQUENCES)
        for row, gram, site, nxt, role, sites, n_on, n_off, off_sites, hits, off_by in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CYCLE218_SITES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_OFF_I_SITES,
            STANDING_HITS_BY_TABLET,
            STANDING_OFF_I_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle218_site"]), site)
            self.assertEqual(tuple(row["i_4gram_start"]), site)
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
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["off_i_sites"]),
                off_sites,
            )
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), off_by)
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(tuple(row["hits_by_tablet"]), hits)
            self.assertEqual(row["i_only"], n_off == 0)
            self.assertTrue(row["hapax"])
        self.assertEqual(rows[-1]["N_off_I"], 1)
        self.assertFalse(rows[-1]["i_only"])
        self.assertEqual(
            tuple(tuple(site_row) for site_row in rows[-1]["off_i_sites"]),
            STANDING_OFF_I_SITES_000,
        )
        self.assertEqual(
            tuple(rows[-1]["off_i_previous_4gram"]),
            STANDING_OFF_I_PREVIOUS_4GRAM,
        )
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_090_076_070_forward_4grams_i_only"])
        self.assertEqual(
            lock["i_090_076_070_forward_4grams_i_only"],
            STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY,
        )
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_i_only"], 7)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], 1)
        self.assertEqual(
            tuple(lock["off_i_previous_4gram"]),
            STANDING_OFF_I_PREVIOUS_4GRAM,
        )
        self.assertEqual(
            tuple(lock["off_i_forward_4gram"]),
            STANDING_OFF_I_FORWARD_4GRAM,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertFalse(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle217"])
        self.assertFalse(lock["same_as_cycle218"])
        self.assertTrue(lock["same_claim_shape_as_cycle217"])
        self.assertTrue(lock["off_i_3gram_does_not_count_as_i_site"])
        self.assertTrue(lock["leftover_076_070_not_090_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_076_070_sides_closed"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_090_076_070_forward_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_076_070_forward_4grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
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
        self.assertEqual(self.survey["i_090_076_070_forward_stem"]["cycle"], 218)
        self.assertEqual(self.survey["i_090_076_070_forward_stem"]["N_I"], 8)
        self.assertEqual(
            self.survey["i_090_076_070_forward_stem"]["N_distinct_next_stems"],
            8,
        )
        self.assertFalse(
            self.survey["i_090_076_070_forward_stem"][
                "i_090_076_070_share_one_forward_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_4grams_i_only"]["cycle"],
            217,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_4grams_i_only"]["N_i_only"],
            11,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_4grams_i_only"]["N_not_i_only"],
            0,
        )
        self.assertTrue(
            self.survey["i_leftover_076_070_forward_4grams_i_only"][
                "i_leftover_076_070_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertFalse(
            self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_off_I"], 0)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"][
                "i_4gram_999_090_076_070_i_only"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
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


class TestMamariI090076070Forward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 219 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
