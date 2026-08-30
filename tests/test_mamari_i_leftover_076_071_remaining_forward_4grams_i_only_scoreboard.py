"""I's cycle-188 leftover remaining next-4-grams off-I lock.

Cycle 189 text-search lock. Uses already-vendored A–V and the
cycle-188 remaining 17 leftover 076 071 sites (the leftover
sites whose next stem is not in {076, 600, 090, 700, 061}).
Does not retune those 4-grams, the leftover 34, or the
leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished
Ib is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Same leftover-shape as cycle 187 (076 071 061 forward
4-grams all I-only hapax 1/0), cycle 184 (076 071 700
forward 4-grams all I-only hapax 1/0), cycle 181 (076 071
090 forward 4-grams all I-only 1/0 x3 + 2/0), cycle 178
(076 071 600 forward 4-grams all I-only hapax 1/0), and
cycle 175 (076 071 076 forward 4-grams all I-only hapax
1/0). Cycle 188 remaining-17-distinct, cycle 172 leftover
N=34, and leftover n=4 set stay. 071 999 and 076 076 do
not count. Do not retune.

Locks exact consecutive hits of each remaining leftover
forward 4-gram on tablet I and on every other vendored
tablet A–H and J–V. The seventeen 4-grams: 076 071 010 660,
076 071 274 604, 076 071 018 049, 076 071 202 604,
076 071 004 004, 076 071 078 999, 076 071 496 999,
076 071 632 670, 076 071 183 430, 076 071 071 076,
076 071 070 076, 076 071 513 001, 076 071 607 208,
076 071 002 536, 076 071 729 073, 076 071 021 090,
076 071 670 009. Do not assume hapax; count each from
fixtures. Hypothesis: all seventeen are I-only. Measured:
each N_I=1 at the cycle-188 remaining leftover site; all
N_off_I=0. Claim that can lose:
i_leftover_076_071_remaining_forward_4grams_all_i_only.
True only if ALL seventeen have N_off_I=0 (and N_I>=1).
The claim is true. Do not assume hapax; measure. Do not
retune.

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
    GRAM2,
    STANDING_I_SITES as CYCLE171_I_SITES,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_inside_family_scoreboard import (
    STANDING_LEFTOVER_SITES as CYCLE172_LEFTOVER_SITES,
    STANDING_N_LEFTOVER as CYCLE172_N_LEFTOVER,
    TestMamariI2gram076071InsideFamilyScoreboard,
)
from tests.test_mamari_i_076_071_061_forward_4grams_i_only_scoreboard import (
    TestMamariI076071061Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_076_071_076_forward_4grams_i_only_scoreboard import (
    TestMamariI076071076Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_076_071_090_forward_4grams_i_only_scoreboard import (
    TestMamariI076071090Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_076_071_600_forward_4grams_i_only_scoreboard import (
    TestMamariI076071600Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_076_071_700_forward_4grams_i_only_scoreboard import (
    TestMamariI076071700Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    leftover_forward_3grams,
    leftover_next_4grams,
    leftover_sites_without_forward,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_076_071_remaining_next_stems_distinct_scoreboard import (
    STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT,
    STANDING_N_DISTINCT_REMAINING_NEXT_STEMS as CYCLE188_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE188_N_LEFTOVER,
    STANDING_N_LOCKED_CLUSTER as CYCLE188_N_LOCKED,
    STANDING_N_NO_FORWARD as CYCLE188_N_NO_FORWARD,
    STANDING_N_REMAINING as CYCLE188_N_REMAINING,
    STANDING_REMAINING_NEXT_4GRAMS as CYCLE188_NEXT_4GRAMS,
    STANDING_REMAINING_NEXT_STEMS as CYCLE188_NEXT_STEMS,
    STANDING_REMAINING_SITES as CYCLE188_REMAINING_SITES,
    TestMamariILeftover076071RemainingNextStemsDistinctScoreboard,
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
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_REMAINING = 17
STANDING_SEQUENCES = CYCLE188_NEXT_4GRAMS
STANDING_REMAINING_SITES = CYCLE188_REMAINING_SITES
STANDING_NEXT_STEMS = CYCLE188_NEXT_STEMS
STANDING_ROLES = ("leftover",) * STANDING_N_REMAINING
STANDING_N_I_EACH = (1,) * STANDING_N_REMAINING
STANDING_N_ON_I_EACH = (1,) * STANDING_N_REMAINING
STANDING_I_SITES = tuple((site,) for site in STANDING_REMAINING_SITES)
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
STANDING_CLAIM = "i_leftover_076_071_remaining_forward_4grams_all_i_only"
STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_ALL_I_ONLY = True
STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_076_071_remaining_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE178_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE181_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE184_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE187_FORWARD_4GRAMS = False
STANDING_SAME_LEFTOVER_SHAPE_AS_175_178_181_184_187 = True
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LOCKED_CLUSTER_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def leftover_forward_4gram_start_site(
    remaining_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-188 remaining leftover site."""
    return remaining_site


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_076_071_remaining_forward_4grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_REMAINING,
) -> bool:
    """True iff all 17 remaining leftover forward 4-grams are I-only.

    Claim holds only if every gram has N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only. Hapax is not
    assumed; N_I may be greater than 1. Length must stay 17.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestILeftover076071RemainingForward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-188 remaining leftover 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 071 999 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("076", "071", "010", "660"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("076", "071", "670", "009"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_REMAINING)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:2], GRAM2)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["076", "071", "010", "660", "076", "071", "010", "660"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [list(STANDING_SEQUENCES[0][:2]) + ["000"] + list(STANDING_SEQUENCES[0][2:])]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_071_065_071_999)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], STANDING_SEQUENCES[-1]), 0)
        self.assertEqual(ngram_hit_count([["071", "999"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["076", "076"]], STANDING_SEQUENCES[-1]), 0)
        self.assertEqual(ngram_hit_count([["076", "071", "010"]], STANDING_SEQUENCES[0]), 0)
        planted = ["147", "076", "076", "071", "010", "660"]
        self.assertEqual(site_next_4gram(planted, 2, GRAM2), STANDING_SEQUENCES[0])
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all 17 remaining forward 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_076_071_remaining_forward_4grams_all_i_only(hold_ones, hold_zeros)
        )
        self.assertTrue(
            i_leftover_076_071_remaining_forward_4grams_all_i_only(
                (2,) + hold_ones[1:],
                hold_zeros,
            )
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_leftover_076_071_remaining_forward_4grams_all_i_only(
                hold_ones,
                tuple(lose_off),
            )
        )
        lose_off_mid = list(hold_zeros)
        lose_off_mid[8] = 1
        self.assertFalse(
            i_leftover_076_071_remaining_forward_4grams_all_i_only(
                hold_ones,
                tuple(lose_off_mid),
            )
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_leftover_076_071_remaining_forward_4grams_all_i_only(
                tuple(lose_missing_i),
                hold_zeros,
            )
        )
        self.assertFalse(
            i_leftover_076_071_remaining_forward_4grams_all_i_only((), ())
        )
        self.assertFalse(
            i_leftover_076_071_remaining_forward_4grams_all_i_only(
                hold_ones[:-1],
                hold_zeros[:-1],
            )
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_remaining_forward_4grams_all_i_only")
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_188_remaining_forwards_not_retuned(self):
        """4-grams stay the cycle-188 remaining leftover forwards; none is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(STANDING_SEQUENCES, CYCLE188_NEXT_4GRAMS)
        self.assertEqual(STANDING_NEXT_STEMS, CYCLE188_NEXT_STEMS)
        self.assertEqual(STANDING_REMAINING_SITES, CYCLE188_REMAINING_SITES)
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE188_N_REMAINING)
        self.assertEqual(CYCLE188_N_REMAINING, 17)
        self.assertEqual(CYCLE188_N_DISTINCT, 17)
        self.assertEqual(len(set(STANDING_NEXT_STEMS)), 17)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_071_065_071_999))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_700_076_076_053))
            self.assertNotIn(gram[2], {"076", "600", "090", "700", "061"})
        for site, start in zip(
            STANDING_REMAINING_SITES,
            (sites[0] for sites in STANDING_I_SITES),
            strict=True,
        ):
            self.assertEqual(leftover_forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE178_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE181_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE184_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE187_FORWARD_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_175_178_181_184_187)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LOCKED_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076071RemainingForward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture cycle-188 remaining-forward-4 off-I lock. Mock only."""

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
        self.measured_remaining_next_4grams = leftover_next_4grams(
            self.i_sides,
            self.remaining_sites,
            GRAM2,
        )
        self.forwards = leftover_forward_3grams(
            self.i_sides,
            self.remaining_sites,
            GRAM2,
        )
        self.no_forward = leftover_sites_without_forward(
            self.remaining_sites,
            self.forwards,
        )
        self.claim_holds = i_leftover_076_071_remaining_forward_4grams_all_i_only(
            self.n_i,
            self.n_off_i,
        )

    def test_tokens_and_sites_are_cycle_188_remaining_not_retuned(self):
        """4-grams and I sites stay the cycle-188 remaining leftover lock."""
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.remaining_sites, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining_sites, CYCLE188_REMAINING_SITES)
        self.assertEqual(self.measured_remaining_next_4grams, STANDING_SEQUENCES)
        self.assertEqual(self.measured_remaining_next_4grams, CYCLE188_NEXT_4GRAMS)
        self.assertEqual(self.no_forward, ())
        prior_188 = self.survey["i_leftover_076_071_remaining_next_stems_distinct"]
        self.assertEqual(prior_188["cycle"], 188)
        self.assertEqual(prior_188["N_leftover"], CYCLE188_N_LEFTOVER)
        self.assertEqual(prior_188["N_leftover"], 34)
        self.assertEqual(prior_188["N_locked_cluster"], CYCLE188_N_LOCKED)
        self.assertEqual(prior_188["N_locked_cluster"], 17)
        self.assertEqual(prior_188["N_remaining"], CYCLE188_N_REMAINING)
        self.assertEqual(prior_188["N_remaining"], 17)
        self.assertEqual(prior_188["N_distinct_remaining_next_stems"], CYCLE188_N_DISTINCT)
        self.assertEqual(prior_188["N_distinct_remaining_next_stems"], 17)
        self.assertEqual(prior_188["N_no_forward"], CYCLE188_N_NO_FORWARD)
        self.assertEqual(prior_188["N_no_forward"], 0)
        self.assertTrue(prior_188["i_leftover_076_071_remaining_next_stems_all_distinct"])
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT)
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_188["remaining_next_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_188["remaining_leftover_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(tuple(prior_188["remaining_next_stems"]), STANDING_NEXT_STEMS)
        prior_172 = self.survey["i_2gram_076_071_inside_family"]
        self.assertEqual(prior_172["cycle"], 172)
        self.assertEqual(prior_172["N_leftover"], CYCLE172_N_LEFTOVER)
        self.assertEqual(prior_172["N_leftover"], 34)
        self.assertEqual(CYCLE188_N_LEFTOVER, CYCLE172_N_LEFTOVER)
        self.assertEqual(
            tuple(tuple(row) for row in prior_172["leftover_sites"]),
            CYCLE172_LEFTOVER_SITES,
        )
        self.assertFalse(prior_172["i_2gram_076_071_all_inside_leftover_n4_family"])
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], CYCLE171_N_I)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], CYCLE171_N_OFF_I)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertEqual(GRAM2[:2], GRAM2)
        prior_187 = self.survey["i_076_071_061_forward_4grams_i_only"]
        self.assertEqual(prior_187["cycle"], 187)
        self.assertTrue(prior_187["i_076_071_061_forward_4grams_i_only"])
        prior_184 = self.survey["i_076_071_700_forward_4grams_i_only"]
        self.assertEqual(prior_184["cycle"], 184)
        self.assertTrue(prior_184["i_076_071_700_forward_4grams_i_only"])
        prior_181 = self.survey["i_076_071_090_forward_4grams_i_only"]
        self.assertEqual(prior_181["cycle"], 181)
        self.assertTrue(prior_181["i_076_071_090_forward_4grams_i_only"])
        prior_178 = self.survey["i_076_071_600_forward_4grams_i_only"]
        self.assertEqual(prior_178["cycle"], 178)
        self.assertTrue(prior_178["i_076_071_600_forward_4grams_i_only"])
        prior_175 = self.survey["i_076_071_076_forward_4grams_i_only"]
        self.assertEqual(prior_175["cycle"], 175)
        self.assertTrue(prior_175["i_076_071_076_forward_4grams_i_only"])
        prior_170 = self.survey["i_leftover_n4_076_071"]
        self.assertEqual(prior_170["cycle"], 170)
        self.assertTrue(prior_170["i_leftover_n4_exactly_4_contain_076_071"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """Each remaining leftover 4-gram is N_I=1, N_off_I=0. All I-only. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (1,) * STANDING_N_REMAINING)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0,) * STANDING_N_REMAINING)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(len(self.grams), STANDING_N_REMAINING)
        for site, start, gram, nxt, role, sites, n_on, n_off in zip(
            STANDING_REMAINING_SITES,
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
            self.assertNotEqual(gram, GRAM5)
            self.assertEqual(role, "leftover")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertNotIn(nxt, {"076", "600", "090", "700", "061"})
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
            i_leftover_076_071_remaining_forward_4grams_all_i_only(
                self.n_i,
                self.n_off_i,
            ),
            STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_remaining_forward_4grams_all_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE178_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE181_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE184_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE187_FORWARD_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_175_178_181_184_187)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LOCKED_CLUSTER_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_188_172_171_and_sibling_i_only_scoreboards_still_compute(self):
        """Cycle 188 remaining-17, 172 leftover-34, 171 I-only 43/0, sibling leftover I-only stay."""
        prior_188 = TestMamariILeftover076071RemainingNextStemsDistinctScoreboard()
        prior_188.setUp()
        prior_188.test_counts_17_of_34_remaining_all_distinct_and_claim_holds()
        prior_188.test_remaining_sites_next_4grams_and_disjoint_from_locked_clusters()
        prior_188.test_survey_matches_computed_lock()
        prior_172 = TestMamariI2gram076071InsideFamilyScoreboard()
        prior_172.setUp()
        prior_172.test_forty_three_sites_split_9_inside_34_leftover_and_claim_loses()
        prior_172.test_survey_matches_computed_lock()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        prior_187 = TestMamariI076071061Forward4gramsIOnlyScoreboard()
        prior_187.setUp()
        prior_187.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_187.test_survey_matches_computed_lock()
        prior_184 = TestMamariI076071700Forward4gramsIOnlyScoreboard()
        prior_184.setUp()
        prior_184.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_184.test_survey_matches_computed_lock()
        prior_181 = TestMamariI076071090Forward4gramsIOnlyScoreboard()
        prior_181.setUp()
        prior_181.test_each_4gram_is_i_only_and_claim_holds()
        prior_181.test_survey_matches_computed_lock()
        prior_178 = TestMamariI076071600Forward4gramsIOnlyScoreboard()
        prior_178.setUp()
        prior_178.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_178.test_survey_matches_computed_lock()
        prior_175 = TestMamariI076071076Forward4gramsIOnlyScoreboard()
        prior_175.setUp()
        prior_175.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_175.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-189 remaining-forward-4 I-only lock."""
        lock = self.survey["i_leftover_076_071_remaining_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 189)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover"], CYCLE172_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 34)
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 17)
        self.assertEqual(lock["N_distinct_remaining_next_stems"], CYCLE188_N_DISTINCT)
        self.assertEqual(lock["N_distinct_remaining_next_stems"], 17)
        self.assertEqual(lock["N_no_forward"], CYCLE188_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_leftover_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["remaining_next_4grams"],
        )
        self.assertEqual(tuple(lock["remaining_next_stems"]), STANDING_NEXT_STEMS)
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_REMAINING)
        for row, gram, site, nxt, role, sites, n_on, n_off in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_REMAINING_SITES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle188_site"]), site)
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
        self.assertTrue(lock["i_leftover_076_071_remaining_forward_4grams_all_i_only"])
        self.assertTrue(lock["i_leftover_076_071_remaining_forward_4grams_i_only"])
        self.assertEqual(
            lock["i_leftover_076_071_remaining_forward_4grams_all_i_only"],
            STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle175_forward_4grams"])
        self.assertFalse(lock["same_as_cycle178_forward_4grams"])
        self.assertFalse(lock["same_as_cycle181_forward_4grams"])
        self.assertFalse(lock["same_as_cycle184_forward_4grams"])
        self.assertFalse(lock["same_as_cycle187_forward_4grams"])
        self.assertTrue(lock["same_leftover_shape_as_cycle_175_178_181_184_187"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["locked_cluster_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_076_071_remaining_next_stems_distinct_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_076_071_061_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_076_071_700_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_076_071_090_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_076_071_600_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_076_071_076_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_next_stems_distinct"]["cycle"],
            188,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_remaining_next_stems_distinct"][
                "i_leftover_076_071_remaining_next_stems_all_distinct"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_next_stems_distinct"]["N_remaining"],
            17,
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_next_stems_distinct"][
                "N_distinct_remaining_next_stems"
            ],
            17,
        )
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["cycle"], 172)
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["N_leftover"], 34)
        self.assertFalse(
            self.survey["i_2gram_076_071_inside_family"][
                "i_2gram_076_071_all_inside_leftover_n4_family"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_076_071_061_forward_4grams_i_only"]["cycle"], 187)
        self.assertTrue(
            self.survey["i_076_071_061_forward_4grams_i_only"][
                "i_076_071_061_forward_4grams_i_only"
            ]
        )
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


class TestMamariILeftover076071RemainingForward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 189 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
