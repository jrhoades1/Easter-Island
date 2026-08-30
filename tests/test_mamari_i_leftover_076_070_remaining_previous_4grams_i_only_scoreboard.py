"""I's cycle-214 leftover remaining previous-4-grams off-I lock.

Cycle 215 text-search lock. Uses already-vendored A–V and the
cycle-214 remaining 8 leftover 076 070 sites (the leftover
sites whose previous stem is not 720). Does not retune those
4-grams, the leftover 11, the cycle-211 leftover-3 previous
720 cluster, or the leftover n=4 set. Does not vendor a new
tablet. Does not scrape X. W has no Barthel (cycle 100); skip
W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same leftover-shape as cycle 204 (leftover 076 071 remaining
previous 4-grams all I-only hapax 1/0, 24/24). Cycle 214
remaining-8-distinct, cycle 213 previous-4 hapax 1/0 x3,
cycle 212 720 076 070 I-only 3/0, cycle 211 leftover N_share=3
/ N_leftover=11, and cycle 171 076 071 I-only 43/0 stay.
Already-locked 720 cluster 4-grams (069 720 076 070,
053 720 076 070, 999 720 076 070) do not count. Leftover =
I 076 070 sites that are NOT 090 076 070. Off-I 076 070 is
not leftover. 076 071 is a different 2-gram. Do not retune
the leftover n=4 set.

Locks exact consecutive hits of each remaining leftover
previous 4-gram on tablet I and on every other vendored
tablet A–H and J–V. The eight 4-grams: 099 571 076 070,
076 295 076 070, 050 048 076 070, 093 205 076 070,
090 099 076 070, 053 029 076 070, 600 604 076 070,
067 606 076 070. Do not assume hapax; count each from
fixtures. Hypothesis: all eight are I-only. Measured: each
N_I=1 at the previous-4 start two tokens before the
cycle-214 remaining leftover site; all N_off_I=0. Claim
that can lose:
i_leftover_076_070_remaining_previous_4grams_i_only.
True only if ALL eight have N_off_I=0 and N_I>=1. The
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
    TestMamariI2gram076070IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_I_SITES as CYCLE171_I_SITES,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_720_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE212_GRAM3,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE212_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE212_I_SITES,
    STANDING_N_I as CYCLE212_N_I,
    STANDING_N_OFF_I as CYCLE212_N_OFF_I,
    TestMamariI3gram720076070IOnlyScoreboard,
)
from tests.test_mamari_i_720_076_070_previous_4grams_i_only_scoreboard import (
    STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY as CYCLE213_I_ONLY,
    STANDING_N_I_053 as CYCLE213_N_I_053,
    STANDING_N_I_069 as CYCLE213_N_I_069,
    STANDING_N_I_999 as CYCLE213_N_I_999,
    STANDING_N_OFF_I_053 as CYCLE213_N_OFF_I_053,
    STANDING_N_OFF_I_069 as CYCLE213_N_OFF_I_069,
    STANDING_N_OFF_I_999 as CYCLE213_N_OFF_I_999,
    STANDING_SEQUENCES as CYCLE213_SEQUENCES,
    TestMamariI720076070Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_previous_720_scoreboard import (
    GRAM3_BACKWARD,
    STEM_720,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE211_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE211_MATCHING_SITES,
    STANDING_N_LEFTOVER as CYCLE211_N_LEFTOVER,
    STANDING_N_SHARE as CYCLE211_N_SHARE,
    STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
    STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
    STANDING_WITHOUT_SITES as CYCLE211_WITHOUT_SITES,
    TestMamariILeftover076070Previous720Scoreboard,
)
from tests.test_mamari_i_leftover_076_070_previous_stem_scoreboard import (
    GRAM2,
    STANDING_LEFTOVER_SITES,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE210_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE210_N_LEFTOVER,
    STANDING_PREFIXED_I_SITES,
    TestMamariILeftover076070PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_076_070_remaining_previous_stems_distinct_scoreboard import (
    STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_STEMS_DISTINCT,
    STANDING_N_DISTINCT_REMAINING as CYCLE214_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE214_N_LEFTOVER,
    STANDING_N_REMAINING as CYCLE214_N_REMAINING,
    STANDING_N_SHARE_720 as CYCLE214_N_SHARE,
    STANDING_REMAINING_PREVIOUS_4GRAMS as CYCLE214_PREVIOUS_4GRAMS,
    STANDING_REMAINING_PREVIOUS_STEMS as CYCLE214_PREVIOUS_STEMS,
    STANDING_REMAINING_SITES as CYCLE214_REMAINING_SITES,
    TestMamariILeftover076070RemainingPreviousStemsDistinctScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    leftover_previous_4grams,
    leftover_sites_without_backward,
    leftover_previous_stems,
    site_previous_4gram,
)
from tests.test_mamari_i_leftover_076_071_remaining_previous_4grams_i_only_scoreboard import (
    TestMamariILeftover076071RemainingPrevious4gramsIOnlyScoreboard,
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
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_REMAINING = 8
STANDING_SEQUENCES = CYCLE214_PREVIOUS_4GRAMS
STANDING_REMAINING_SITES = CYCLE214_REMAINING_SITES
STANDING_PREVIOUS_STEMS = CYCLE214_PREVIOUS_STEMS
STANDING_ROLES = ("leftover",) * STANDING_N_REMAINING
STANDING_N_I_EACH = (1,) * STANDING_N_REMAINING
STANDING_N_ON_I_EACH = (1,) * STANDING_N_REMAINING
STANDING_I_SITES = tuple(
    ((side, line, index - 2),) for side, line, index in STANDING_REMAINING_SITES
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_REMAINING
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_EACH = True
STANDING_CLAIM = "i_leftover_076_070_remaining_previous_4grams_i_only"
STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_076_070_remaining_previous_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE204_REMAINING_4GRAMS = False
STANDING_SAME_AS_CYCLE213_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE212 = False
STANDING_SAME_AS_CYCLE211 = False
STANDING_SAME_AS_CYCLE214 = False
STANDING_SAME_LEFTOVER_SHAPE_AS_204 = True
STANDING_720_CLUSTER_DOES_NOT_COUNT = True
STANDING_090_PREFIXED_DOES_NOT_COUNT = True
STANDING_OFF_I_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LOCKED_CLUSTER_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def leftover_previous_4gram_start_site(
    remaining_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Previous 4-gram starts two tokens before the cycle-214 leftover site."""
    side, line, index = remaining_site
    return (side, line, index - 2)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_076_070_remaining_previous_4grams_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_REMAINING,
) -> bool:
    """True iff all 8 remaining leftover previous 4-grams are I-only.

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


class TestILeftover076070RemainingPrevious4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-214 remaining leftover previous 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 076 071 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("099", "571", "076", "070"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("067", "606", "076", "070"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_REMAINING)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[2:], GRAM2)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["099", "571", "076", "070", "099", "571", "076", "070"]]
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
        self.assertEqual(ngram_hit_count([["571", "076", "070"]], STANDING_SEQUENCES[0]), 0)
        planted = ["099", "571", "076", "070", "010", "660"]
        self.assertEqual(site_previous_4gram(planted, 2, GRAM2), STANDING_SEQUENCES[0])
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all 8 remaining previous 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_076_070_remaining_previous_4grams_i_only(
                hold_ones, hold_zeros
            )
        )
        self.assertTrue(
            i_leftover_076_070_remaining_previous_4grams_i_only(
                (2,) + hold_ones[1:],
                hold_zeros,
            )
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_leftover_076_070_remaining_previous_4grams_i_only(
                hold_ones,
                tuple(lose_off),
            )
        )
        lose_off_mid = list(hold_zeros)
        lose_off_mid[4] = 1
        self.assertFalse(
            i_leftover_076_070_remaining_previous_4grams_i_only(
                hold_ones,
                tuple(lose_off_mid),
            )
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_leftover_076_070_remaining_previous_4grams_i_only(
                tuple(lose_missing_i),
                hold_zeros,
            )
        )
        self.assertFalse(
            i_leftover_076_070_remaining_previous_4grams_i_only((), ())
        )
        self.assertFalse(
            i_leftover_076_070_remaining_previous_4grams_i_only(
                hold_ones[:-1],
                hold_zeros[:-1],
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_076_070_remaining_previous_4grams_i_only",
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_4GRAMS_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_214_remaining_previous_not_retuned(self):
        """4-grams stay the cycle-214 remaining leftover previouss; none is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(STANDING_SEQUENCES, CYCLE214_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_PREVIOUS_STEMS, CYCLE214_PREVIOUS_STEMS)
        self.assertEqual(STANDING_REMAINING_SITES, CYCLE214_REMAINING_SITES)
        self.assertEqual(STANDING_REMAINING_SITES, CYCLE211_WITHOUT_SITES)
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE214_N_REMAINING)
        self.assertEqual(CYCLE214_N_REMAINING, 8)
        self.assertEqual(CYCLE214_N_DISTINCT, 8)
        self.assertEqual(len(set(STANDING_PREVIOUS_STEMS)), 8)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        locked_grams = set(CYCLE211_MATCHING_PREVIOUS_4GRAMS)
        locked_stems = {STEM_720}
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_999_090_076_071))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_700_076_076_053))
            self.assertNotIn(gram[1], locked_stems)
            self.assertNotIn(gram, locked_grams)
            self.assertNotEqual(gram[2:], CYCLE171_GRAM2)
        for gram in CYCLE213_SEQUENCES:
            self.assertNotIn(gram, STANDING_SEQUENCES)
            self.assertIn(gram, locked_grams)
        for site, start in zip(
            STANDING_REMAINING_SITES,
            (sites[0] for sites in STANDING_I_SITES),
            strict=True,
        ):
            self.assertEqual(leftover_previous_4gram_start_site(site), start)
            self.assertEqual(start[2], site[2] - 2)
        self.assertEqual(
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
            STANDING_SEQUENCES[4],
        )
        self.assertEqual(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_REMAINING_SITES[4])
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE204_REMAINING_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE213_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE212)
        self.assertFalse(STANDING_SAME_AS_CYCLE211)
        self.assertFalse(STANDING_SAME_AS_CYCLE214)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_204)
        self.assertTrue(STANDING_720_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LOCKED_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076070RemainingPrevious4gramsIOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture cycle-214 remaining-previous-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.remaining_sites = STANDING_REMAINING_SITES
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
        self.measured_remaining_previous_4grams = leftover_previous_4grams(
            self.i_sides,
            self.remaining_sites,
            GRAM2,
        )
        self.previous = leftover_previous_stems(
            self.i_sides,
            self.remaining_sites,
            GRAM2,
        )
        self.no_backward = leftover_sites_without_backward(
            self.remaining_sites,
            self.previous,
        )
        self.claim_holds = i_leftover_076_070_remaining_previous_4grams_i_only(
            self.n_i,
            self.n_off_i,
        )

    def test_tokens_and_sites_are_cycle_214_remaining_not_retuned(self):
        """4-grams and I sites stay the cycle-214 remaining leftover lock."""
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM2, CYCLE206_GRAM2)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.remaining_sites, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining_sites, CYCLE214_REMAINING_SITES)
        self.assertEqual(self.remaining_sites, CYCLE211_WITHOUT_SITES)
        self.assertEqual(self.measured_remaining_previous_4grams, STANDING_SEQUENCES)
        self.assertEqual(
            self.measured_remaining_previous_4grams, CYCLE214_PREVIOUS_4GRAMS
        )
        self.assertEqual(self.no_backward, ())
        prior_214 = self.survey["i_leftover_076_070_remaining_previous_stems_distinct"]
        self.assertEqual(prior_214["cycle"], 214)
        self.assertEqual(prior_214["N_leftover"], CYCLE214_N_LEFTOVER)
        self.assertEqual(prior_214["N_leftover"], 11)
        self.assertEqual(prior_214["N_share_720"], CYCLE214_N_SHARE)
        self.assertEqual(prior_214["N_share_720"], 3)
        self.assertEqual(prior_214["N_remaining"], CYCLE214_N_REMAINING)
        self.assertEqual(prior_214["N_remaining"], 8)
        self.assertEqual(
            prior_214["N_distinct_remaining_previous_stems"],
            CYCLE214_N_DISTINCT,
        )
        self.assertEqual(prior_214["N_distinct_remaining_previous_stems"], 8)
        self.assertEqual(prior_214["N_distinct_remaining"], 8)
        self.assertEqual(prior_214["N_no_backward"], 0)
        self.assertTrue(
            prior_214["i_leftover_076_070_remaining_previous_stems_distinct"]
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_STEMS_DISTINCT)
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_214["remaining_previous_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_214["remaining_leftover_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(prior_214["remaining_previous_stems"]),
            STANDING_PREVIOUS_STEMS,
        )
        prior_213 = self.survey["i_720_076_070_previous_4grams_i_only"]
        self.assertEqual(prior_213["cycle"], 213)
        self.assertTrue(prior_213["i_720_076_070_previous_4grams_i_only"])
        self.assertTrue(CYCLE213_I_ONLY)
        self.assertEqual(prior_213["N_I_069"], CYCLE213_N_I_069)
        self.assertEqual(prior_213["N_off_I_069"], CYCLE213_N_OFF_I_069)
        self.assertEqual(prior_213["N_I_053"], CYCLE213_N_I_053)
        self.assertEqual(prior_213["N_off_I_053"], CYCLE213_N_OFF_I_053)
        self.assertEqual(prior_213["N_I_999"], CYCLE213_N_I_999)
        self.assertEqual(prior_213["N_off_I_999"], CYCLE213_N_OFF_I_999)
        self.assertEqual(prior_213["N_I_069"], 1)
        self.assertEqual(prior_213["N_off_I_069"], 0)
        self.assertEqual(prior_213["N_I_053"], 1)
        self.assertEqual(prior_213["N_off_I_053"], 0)
        self.assertEqual(prior_213["N_I_999"], 1)
        self.assertEqual(prior_213["N_off_I_999"], 0)
        self.assertEqual(
            [list(gram) for gram in CYCLE213_SEQUENCES],
            [row["tokens4"] for row in prior_213["sequences"]],
        )
        prior_212 = self.survey["i_3gram_720_076_070_i_only"]
        self.assertEqual(prior_212["cycle"], 212)
        self.assertEqual(tuple(prior_212["tokens3"]), CYCLE212_GRAM3)
        self.assertEqual(prior_212["N_I"], CYCLE212_N_I)
        self.assertEqual(prior_212["N_I"], 3)
        self.assertEqual(prior_212["N_off_I"], CYCLE212_N_OFF_I)
        self.assertEqual(prior_212["N_off_I"], 0)
        self.assertTrue(prior_212["i_3gram_720_076_070_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_212["i_sites"]),
            CYCLE212_I_SITES,
        )
        prior_211 = self.survey["i_leftover_076_070_previous_720"]
        self.assertEqual(prior_211["cycle"], 211)
        self.assertEqual(tuple(prior_211["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(prior_211["N_share"], CYCLE211_N_SHARE)
        self.assertEqual(prior_211["N_share"], 3)
        self.assertEqual(prior_211["N_leftover"], CYCLE211_N_LEFTOVER)
        self.assertEqual(prior_211["N_leftover"], 11)
        self.assertTrue(prior_211["i_leftover_076_070_previous_720"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_211["matching_leftover_sites"]),
            CYCLE211_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_211["without_sites"]),
            CYCLE211_WITHOUT_SITES,
        )
        prior_210 = self.survey["i_leftover_076_070_previous_stem"]
        self.assertEqual(prior_210["cycle"], 210)
        self.assertEqual(prior_210["N_leftover"], CYCLE210_N_LEFTOVER)
        self.assertEqual(prior_210["N_leftover"], 11)
        self.assertEqual(prior_210["N_distinct_previous_stems"], CYCLE210_N_DISTINCT)
        self.assertEqual(prior_210["N_distinct_previous_stems"], 9)
        self.assertFalse(prior_210["i_leftover_076_070_share_one_previous_stem"])
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
        prior_204 = self.survey["i_leftover_076_071_remaining_previous_4grams_i_only"]
        self.assertEqual(prior_204["cycle"], 204)
        self.assertTrue(prior_204["i_leftover_076_071_remaining_previous_4grams_all_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """Each remaining leftover previous 4-gram is N_I=1, N_off_I=0. All I-only. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (1,) * STANDING_N_REMAINING)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0,) * STANDING_N_REMAINING)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(STANDING_OFF_I_SITES, ())
        self.assertEqual(len(self.grams), STANDING_N_REMAINING)
        locked_stems = {STEM_720}
        locked_grams = set(CYCLE211_MATCHING_PREVIOUS_4GRAMS)
        for site, start, gram, prev, role, sites, n_on, n_off in zip(
            STANDING_REMAINING_SITES,
            (row[0] for row in STANDING_I_SITES),
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            strict=True,
        ):
            self.assertEqual(leftover_previous_4gram_start_site(site), start)
            self.assertEqual(sites, (start,))
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2] + 1], prev)
            self.assertEqual(tuple(stems[start[2] + 2 : start[2] + STANDING_N4]), GRAM2)
            self.assertEqual(site_previous_4gram(stems, site[2], GRAM2), gram)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotIn(gram, locked_grams)
            self.assertEqual(role, "leftover")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertNotIn(prev, locked_stems)
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
            i_leftover_076_070_remaining_previous_4grams_i_only(
                self.n_i,
                self.n_off_i,
            ),
            STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_4GRAMS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_4GRAMS_I_ONLY,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_076_070_remaining_previous_4grams_i_only",
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE204_REMAINING_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE213_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE212)
        self.assertFalse(STANDING_SAME_AS_CYCLE211)
        self.assertFalse(STANDING_SAME_AS_CYCLE214)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_204)
        self.assertTrue(STANDING_720_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LOCKED_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        for n_on, locked in zip(self.n_i, STANDING_N_I_EACH, strict=True):
            if n_on != locked:
                self.fail("measured N_I drifted from the locked count")
        if not self.claim_holds:
            self.fail("measured remaining previous 4-grams are not all I-only")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_214_213_212_211_and_171_scoreboards_still_compute(self):
        """Cycle 214 8/8, 213 hapax 1/0 x3, 212 3/0, 211 N_share=3/11, 171 43/0 stay."""
        prior_214 = TestMamariILeftover076070RemainingPreviousStemsDistinctScoreboard()
        prior_214.setUp()
        prior_214.test_counts_8_remaining_all_distinct_and_claim_holds()
        prior_214.test_remaining_sites_inventory_and_disjoint_from_720_cluster()
        prior_214.test_survey_matches_computed_lock()
        self.assertEqual(prior_214.n_remaining, 8)
        self.assertEqual(prior_214.n_distinct, 8)
        self.assertEqual(prior_214.n_leftover, 11)
        self.assertTrue(prior_214.claim_holds)
        self.assertEqual(CYCLE214_N_REMAINING, 8)
        self.assertEqual(CYCLE214_N_DISTINCT, 8)
        self.assertEqual(set(self.remaining_sites), set(prior_214.remaining_sites))
        prior_213 = TestMamariI720076070Previous4gramsIOnlyScoreboard()
        prior_213.setUp()
        prior_213.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_213.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE213_N_I_069, 1)
        self.assertEqual(CYCLE213_N_OFF_I_069, 0)
        self.assertEqual(CYCLE213_N_I_053, 1)
        self.assertEqual(CYCLE213_N_OFF_I_053, 0)
        self.assertEqual(CYCLE213_N_I_999, 1)
        self.assertEqual(CYCLE213_N_OFF_I_999, 0)
        self.assertTrue(CYCLE213_I_ONLY)
        prior_212 = TestMamariI3gram720076070IOnlyScoreboard()
        prior_212.setUp()
        prior_212.test_i_hits_are_three_on_ia_all_leftover()
        prior_212.test_3gram_is_zero_off_i_and_i_only()
        prior_212.test_survey_matches_computed_lock()
        self.assertEqual(prior_212.i_hits, 3)
        self.assertEqual(prior_212.off_i_hits, 0)
        self.assertEqual(prior_212.i_sites, CYCLE212_I_SITES)
        self.assertEqual(CYCLE212_N_I, 3)
        self.assertEqual(CYCLE212_N_OFF_I, 0)
        prior_211 = TestMamariILeftover076070Previous720Scoreboard()
        prior_211.setUp()
        prior_211.test_counts_3_of_11_and_hypothesis_n_3_holds()
        prior_211.test_survey_matches_computed_lock()
        self.assertEqual(prior_211.n_share, 3)
        self.assertEqual(prior_211.n_leftover, 11)
        self.assertEqual(CYCLE211_N_SHARE, 3)
        self.assertEqual(CYCLE211_N_LEFTOVER, 11)
        self.assertEqual(prior_211.with_sites, CYCLE211_MATCHING_SITES)
        self.assertEqual(prior_211.without_sites, self.remaining_sites)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(len(prior_171.i_sites), 43)
        self.assertEqual(prior_171.i_sites, CYCLE171_I_SITES)
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_210 = TestMamariILeftover076070PreviousStemScoreboard()
        prior_210.setUp()
        prior_210.test_counts_9_distinct_previous_stems_and_claim_loses()
        prior_210.test_survey_matches_computed_lock()
        self.assertEqual(prior_210.n_distinct, CYCLE210_N_DISTINCT)
        self.assertEqual(prior_210.n_leftover, CYCLE210_N_LEFTOVER)
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        self.assertEqual(prior_206.i_hits, 19)
        self.assertEqual(prior_206.off_i_hits, 5)
        prior_204 = TestMamariILeftover076071RemainingPrevious4gramsIOnlyScoreboard()
        prior_204.setUp()
        prior_204.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_204.test_survey_matches_computed_lock()
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-215 remaining-previous-4 I-only lock."""
        lock = self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"]
        self.assertEqual(lock["cycle"], 215)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover"], CYCLE214_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 11)
        self.assertEqual(lock["N_share_720"], CYCLE214_N_SHARE)
        self.assertEqual(lock["N_share_720"], 3)
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 8)
        self.assertEqual(
            lock["N_distinct_remaining_previous_stems"],
            CYCLE214_N_DISTINCT,
        )
        self.assertEqual(lock["N_distinct_remaining_previous_stems"], 8)
        self.assertEqual(lock["N_no_backward"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_leftover_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["remaining_previous_4grams"],
        )
        self.assertEqual(
            tuple(lock["remaining_previous_stems"]),
            STANDING_PREVIOUS_STEMS,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE211_MATCHING_PREVIOUS_4GRAMS],
            lock["excluded_720_cluster_4grams"],
        )
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_REMAINING)
        for row, gram, site, prev, role, sites, n_on, n_off in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_REMAINING_SITES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle214_site"]), site)
            self.assertEqual(row["previous_stem"], prev)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_I"], 1)
            self.assertEqual(row["ia_hits"], 1)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["i_sites"]), sites
            )
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
        self.assertTrue(lock["i_leftover_076_070_remaining_previous_4grams_i_only"])
        self.assertEqual(
            lock["i_leftover_076_070_remaining_previous_4grams_i_only"],
            STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_4GRAMS_I_ONLY,
        )
        self.assertEqual(lock["N_i_only"], 8)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle204_remaining_4grams"])
        self.assertFalse(lock["same_as_cycle213_previous_4grams"])
        self.assertFalse(lock["same_as_cycle212"])
        self.assertFalse(lock["same_as_cycle211"])
        self.assertFalse(lock["same_as_cycle214"])
        self.assertTrue(lock["same_leftover_shape_as_cycle_204"])
        self.assertTrue(lock["720_cluster_does_not_count"])
        self.assertTrue(lock["090_prefixed_does_not_count"])
        self.assertTrue(lock["off_i_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["locked_cluster_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_076_070_remaining_previous_stems_distinct_unchanged"]
        )
        self.assertTrue(lock["standing_i_720_076_070_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_720_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_070_previous_720_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_070_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_076_071_remaining_previous_4grams_i_only_unchanged"]
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
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_stems_distinct"]["cycle"],
            214,
        )
        self.assertTrue(
            self.survey["i_leftover_076_070_remaining_previous_stems_distinct"][
                "i_leftover_076_070_remaining_previous_stems_distinct"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_stems_distinct"][
                "N_remaining"
            ],
            8,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_stems_distinct"][
                "N_distinct_remaining_previous_stems"
            ],
            8,
        )
        self.assertEqual(self.survey["i_720_076_070_previous_4grams_i_only"]["cycle"], 213)
        self.assertTrue(
            self.survey["i_720_076_070_previous_4grams_i_only"][
                "i_720_076_070_previous_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["cycle"], 212)
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_076_070_previous_720"]["cycle"], 211)
        self.assertEqual(self.survey["i_leftover_076_070_previous_720"]["N_share"], 3)
        self.assertEqual(self.survey["i_leftover_076_070_previous_720"]["N_leftover"], 11)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_previous_4grams_i_only"]["cycle"],
            204,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_remaining_previous_4grams_i_only"][
                "i_leftover_076_071_remaining_previous_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"]["i_leftover_n4_exactly_1_contain_076_070"]
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


class TestMamariILeftover076070RemainingPrevious4gramsIOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 215 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
