"""I's cycle-229 090 076 013 forward-4-grams off-I lock.

Cycle 230 text-search lock. Uses already-vendored A–V and the
cycle-229 I sites of 3-gram 090 076 013 (all 5 I sites; each
has a next stem). Does not retune those 4-grams, the 5 I
sites, leftover extra remaining-after-071 G=013 K=5, leftover
extra remaining 071, leftover extra forward 070, leftover
extra sites, the leftover n=4 set, or the already-closed
leftover remaining family. Does not vendor a new tablet. Does
not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Same claim-shape as cycle 219 (I 090 076 070 forward 4-grams
all I-only lost 7/8; 090 076 070 000 leaks 1/1 on T). Cycle
229 I 090 076 013 I-only holds 5/0, cycle 228 leftover extra
remaining-after-071 K=5 / G=013, cycle 227 6/071, cycle 226
8/070, cycle 223 69/3, cycle 195 6/0, and cycle 171 43/0
stay. Off-I T sites of 090 076 are not this 3-gram and are
not these 4-grams. Leftover extra remaining after 013 is not
locked this cycle. Previous 4-grams of the five I sites are
not locked this cycle. 090 076 070, 090 076 071, and
090 076 without 013 do not count. Do not retune leftover n=4,
076-cells, or any detector.

Locks exact consecutive hits of each I 090 076 013 forward
4-gram on tablet I and on every other vendored tablet A–H
and J–V. The five 4-grams: 090 076 013 073, 090 076 013 291,
090 076 013 076, 090 076 013 070, 090 076 013 755.
Do not assume hapax; count each from fixtures. Hypothesis:
all five are I-only. Measured: each N_I=1 at the cycle-229
I site; all N_off_I=0. Claim that can lose:
i_090_076_013_forward_4grams_all_i_only.
True only if ALL five have N_off_I=0 and N_I>=1. The claim
is true. Do not assume the I-only result; measure. Do not
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
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_013_i_only_scoreboard import (
    GRAM3,
    STANDING_I_3GRAM_090_076_013_I_ONLY as CYCLE229_I_ONLY,
    STANDING_I_NEXT_4GRAMS as CYCLE229_NEXT_4GRAMS,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE229_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE229_I_SITES,
    STANDING_N_I as CYCLE229_N_I,
    STANDING_N_OFF_I as CYCLE229_N_OFF_I,
    extra_i_sites,
    leftover_extra_remaining_after_071_013_subset,
    named_off_i_sites as cycle229_named_off_i_sites,
    TestMamariI3gram090076013IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
    STANDING_I_3GRAM_090_076_071_I_ONLY as CYCLE195_CLAIM,
    STANDING_I_SITES as CYCLE195_I_SITES,
    STANDING_N_I as CYCLE195_N_I,
    STANDING_N_OFF_I as CYCLE195_N_OFF_I,
    TestMamariI3gram090076071IOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_I_ONLY,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_N_OFF_I_EACH as CYCLE219_N_OFF_I_EACH,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_070_scoreboard import (
    STANDING_G as CYCLE226_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070 as CYCLE226_CLAIM,
    STANDING_K as CYCLE226_K,
    STANDING_MATCHING_SITES as CYCLE226_MATCHING_SITES,
    TestMamariILeftoverExtra090076Forward070Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_071_next_stem_scoreboard import (
    GRAM3_FORWARD,
    STANDING_G as CYCLE228_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G as CYCLE228_CLAIM,
    STANDING_K as CYCLE228_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE228_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE228_MATCHING_SITES,
    STANDING_N_REMAINING2 as CYCLE228_N_REMAINING2,
    leftover_extra_remaining_after_071,
    leftover_extra_remaining_after_071_with_g,
    TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    STANDING_G as CYCLE227_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071 as CYCLE227_CLAIM,
    STANDING_K as CYCLE227_K,
    STANDING_MATCHING_SITES as CYCLE227_MATCHING_SITES,
    TestMamariILeftoverExtra090076RemainingNextStemScoreboard,
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
STANDING_N_I = 5
STANDING_N_SEQUENCES = 5
STANDING_SEQUENCES = CYCLE229_NEXT_4GRAMS
STANDING_CYCLE229_SITES = CYCLE229_I_SITES
STANDING_NEXT_STEMS = (
    "073",
    "291",
    "076",
    "070",
    "755",
)
STANDING_PREVIOUS_4GRAMS = CYCLE229_PREVIOUS_4GRAMS
STANDING_ROLES = ("forward",) * STANDING_N_SEQUENCES
STANDING_N_I_EACH = (1,) * STANDING_N_SEQUENCES
STANDING_N_ON_I_EACH = (1,) * STANDING_N_SEQUENCES
STANDING_I_SITES = tuple((site,) for site in STANDING_CYCLE229_SITES)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_SEQUENCES
STANDING_OFF_I_SITES = ((), (), (), (), ())
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (STANDING_HITS_BY_TABLET_ONE_ON_I,) * STANDING_N_SEQUENCES
STANDING_N_I_ONLY = 5
STANDING_N_NOT_I_ONLY = 0
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_EACH = True
STANDING_CLAIM = "i_090_076_013_forward_4grams_all_i_only"
STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY = True
STANDING_I_090_076_013_FORWARD_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_090_076_013_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE228 = False
STANDING_SAME_AS_CYCLE229 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_090_076_WITHOUT_013_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_013_IS_NOT_THIS_CYCLE = True
STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE228_K = 5
STANDING_CYCLE228_G = "013"
STANDING_CYCLE229_N_I = 5
STANDING_CYCLE229_N_OFF_I = 0


def forward_4gram_start_site(
    cycle229_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-229 I 090 076 013 site."""
    return cycle229_site


def site_forward_4gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """090 076 013 X if a next stem exists; None at end-of-line."""
    n3 = len(gram3)
    if tuple(stems[index : index + n3]) != gram3:
        return None
    next_index = index + n3
    if next_index >= len(stems):
        return None
    return tuple(stems[index : index + n3 + 1])


def i_090_076_013_forward_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_CYCLE229_SITES,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site forward 4-gram or None for the locked I sites."""
    return tuple(
        site_forward_4gram(line_stems_for_site(i_sides, site), site[2], gram3)
        for site in sites
    )


def i_sites_without_forward(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """I 090 076 013 sites that have no next stem after the 3-gram."""
    return tuple(
        site
        for site, gram in zip(sites, forwards, strict=True)
        if gram is None
    )


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_090_076_013_forward_4grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_SEQUENCES,
) -> bool:
    """True iff all 5 I 090 076 013 forward 4-grams are I-only.

    Claim holds only if every gram has N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only. Hapax is not
    assumed; N_I may be greater than 1. Length must stay 5.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestI090076013Forward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-229 I 090 076 013 forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 070 / 071 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "013", "073"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("090", "076", "013", "755"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_SEQUENCES)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:3], GRAM3)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["090", "076", "013", "073", "090", "076", "013", "073"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [
            list(STANDING_SEQUENCES[0][:2])
            + ["000"]
            + list(STANDING_SEQUENCES[0][2:])
        ]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE207_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE195_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "013"]], STANDING_SEQUENCES[0]), 0)
        planted = ["999", "090", "076", "013", "073", "090"]
        self.assertEqual(site_forward_4gram(planted, 1, GRAM3), STANDING_SEQUENCES[0])
        self.assertEqual(site_next_4gram(planted, 1, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_forward_3gram(planted, 1, GRAM2), GRAM3)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_013_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all 5 forward 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(i_090_076_013_forward_4grams_all_i_only(hold_ones, hold_zeros))
        self.assertTrue(
            i_090_076_013_forward_4grams_all_i_only((2,) + hold_ones[1:], hold_zeros)
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_090_076_013_forward_4grams_all_i_only(hold_ones, tuple(lose_off))
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_090_076_013_forward_4grams_all_i_only(tuple(lose_missing_i), hold_zeros)
        )
        self.assertFalse(i_090_076_013_forward_4grams_all_i_only((), ()))
        self.assertFalse(
            i_090_076_013_forward_4grams_all_i_only(hold_ones[:-1], hold_zeros[:-1])
        )
        self.assertEqual(STANDING_CLAIM, "i_090_076_013_forward_4grams_all_i_only")
        self.assertTrue(STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_090_076_013_FORWARD_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_N_OFF_I_EACH[-1], 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_229_forwards_not_retuned(self):
        """4-grams stay the cycle-229 I forwards; leftover / 070 / 071 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "013"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(STANDING_SEQUENCES, CYCLE229_NEXT_4GRAMS)
        self.assertEqual(STANDING_SEQUENCES, CYCLE228_MATCHING_NEXT_4GRAMS)
        self.assertEqual(STANDING_CYCLE229_SITES, CYCLE229_I_SITES)
        self.assertEqual(STANDING_CYCLE229_SITES, CYCLE228_MATCHING_SITES)
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE229_N_I)
        self.assertEqual(CYCLE229_N_I, 5)
        self.assertEqual(CYCLE229_N_OFF_I, 0)
        self.assertEqual(len(set(STANDING_NEXT_STEMS)), 5)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(CYCLE195_GRAM3, ("090", "076", "071"))
        self.assertEqual(CYCLE207_GRAM3, ("090", "076", "070"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(CYCLE195_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE207_GRAM3, gram))
            self.assertNotEqual(gram[:3], CYCLE195_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE207_GRAM3)
            self.assertNotEqual(gram[:2], CYCLE171_GRAM2)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
        for site, start in zip(
            STANDING_CYCLE229_SITES,
            (sites[0] for sites in STANDING_I_SITES),
            strict=True,
        ):
            self.assertEqual(forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE228)
        self.assertFalse(STANDING_SAME_AS_CYCLE229)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_013_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI090076013Forward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture I 090 076 013 forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle229_sites = STANDING_CYCLE229_SITES
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
            cycle229_named_off_i_sites(gram) for gram in self.grams
        )
        self.measured_forwards = i_090_076_013_forward_4grams(
            self.i_sides,
            self.cycle229_sites,
            GRAM3,
        )
        self.no_forward = i_sites_without_forward(
            self.cycle229_sites,
            self.measured_forwards,
        )
        self.next_stems = leftover_extra_next_stems(
            self.i_sides,
            STANDING_LEFTOVER_SITES,
            GRAM2,
        )
        self.remaining2 = leftover_extra_remaining_after_071(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.leftover_matching = leftover_extra_remaining_after_071_with_g(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
            CYCLE228_G,
        )
        self.leftover_matching_next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.leftover_matching,
            GRAM2,
        )
        self.extra = extra_i_sites(self.cycle229_sites, self.leftover_matching)
        self.n3_i = ngram_hit_count(self.i_sides[SIDE_IA], GRAM3) + STANDING_IB_HITS
        self.n3_off_i = sum(tablet_hit_counts(self.by_tablet, GRAM3, OFF_I_TABLETS))
        self.claim_holds = i_090_076_013_forward_4grams_all_i_only(
            self.n_i,
            self.n_off_i,
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = STANDING_N_SEQUENCES - self.n_i_only

    def test_tokens_and_sites_are_cycle_229_forwards_not_retuned(self):
        """4-grams and I sites stay the cycle-229 forward lock. Nested 5/0 must hold."""
        self.assertEqual(GRAM3, ("090", "076", "013"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle229_sites, STANDING_CYCLE229_SITES)
        self.assertEqual(self.cycle229_sites, CYCLE229_I_SITES)
        self.assertEqual(self.cycle229_sites, CYCLE228_MATCHING_SITES)
        self.assertEqual(self.measured_forwards, STANDING_SEQUENCES)
        self.assertEqual(self.measured_forwards, CYCLE229_NEXT_4GRAMS)
        self.assertEqual(self.measured_forwards, CYCLE228_MATCHING_NEXT_4GRAMS)
        self.assertEqual(self.leftover_matching_next_4grams, STANDING_SEQUENCES)
        self.assertEqual(self.no_forward, ())
        self.assertEqual(self.n3_i, STANDING_CYCLE229_N_I)
        self.assertEqual(self.n3_i, 5)
        self.assertEqual(self.n3_off_i, STANDING_CYCLE229_N_OFF_I)
        self.assertEqual(self.n3_off_i, 0)
        self.assertEqual(self.leftover_matching, CYCLE228_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE229_I_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE228_K)
        self.assertEqual(STANDING_CYCLE228_K, 5)
        self.assertEqual(STANDING_CYCLE228_G, "013")
        self.assertEqual(CYCLE228_G, "013")
        self.assertEqual(CYCLE228_K, 5)
        self.assertEqual(len(self.remaining2), CYCLE228_N_REMAINING2)
        self.assertEqual(len(self.remaining2), 41)
        self.assertTrue(
            leftover_extra_remaining_after_071_013_subset(
                self.leftover_matching,
                self.cycle229_sites,
            )
        )
        self.assertEqual(self.extra, ())
        if self.n3_i != 5 or self.n3_off_i != 0:
            self.fail("nested cycle 229 090 076 013 I-only 5/0 drifted")
        if len(self.leftover_matching) != 5 or CYCLE228_G != "013":
            self.fail("nested cycle 228 leftover extra remaining-after-071 G=013 K=5 drifted")
        if self.extra:
            self.fail("extra I 090 076 013 sites appeared; leftover of leftover is not this cycle")
        prior_229 = self.survey["i_3gram_090_076_013_i_only"]
        self.assertEqual(prior_229["cycle"], 229)
        self.assertEqual(prior_229["N_I"], CYCLE229_N_I)
        self.assertEqual(prior_229["N_I"], 5)
        self.assertEqual(prior_229["N_off_I"], CYCLE229_N_OFF_I)
        self.assertEqual(prior_229["N_off_I"], 0)
        self.assertTrue(prior_229["i_3gram_090_076_013_i_only"])
        self.assertTrue(CYCLE229_I_ONLY)
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_229["i_next_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_229["i_sites"]),
            STANDING_CYCLE229_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PREVIOUS_4GRAMS],
            prior_229["i_previous_4grams"],
        )
        prior_228 = self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]
        self.assertEqual(prior_228["cycle"], 228)
        self.assertEqual(prior_228["G"], "013")
        self.assertEqual(prior_228["K"], 5)
        self.assertEqual(prior_228["N_remaining2"], 41)
        self.assertTrue(prior_228["i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G"])
        self.assertTrue(CYCLE228_CLAIM)
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_228["matching_next_4grams"],
        )
        prior_227 = self.survey["i_leftover_extra_090_076_remaining_next_stem"]
        self.assertEqual(prior_227["cycle"], 227)
        self.assertEqual(prior_227["G"], "071")
        self.assertEqual(prior_227["K"], 6)
        self.assertTrue(prior_227["i_leftover_extra_090_076_remaining_exactly_6_share_071"])
        prior_226 = self.survey["i_leftover_extra_090_076_forward_070"]
        self.assertEqual(prior_226["cycle"], 226)
        self.assertEqual(prior_226["G"], "070")
        self.assertEqual(prior_226["K"], 8)
        self.assertTrue(prior_226["i_leftover_extra_090_076_exactly_8_share_forward_070"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_219 = self.survey["i_090_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_219["cycle"], 219)
        self.assertFalse(prior_219["i_090_076_070_forward_4grams_i_only"])
        self.assertEqual(prior_219["N_i_only"], 7)
        self.assertEqual(prior_219["N_not_i_only"], 1)
        self.assertFalse(CYCLE219_I_ONLY)
        prior_195 = self.survey["i_3gram_090_076_071_i_only"]
        self.assertEqual(prior_195["cycle"], 195)
        self.assertEqual(prior_195["N_I"], 6)
        self.assertEqual(prior_195["N_off_I"], 0)
        self.assertTrue(prior_195["i_3gram_090_076_071_i_only"])
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_013_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """Each forward 4-gram is 1/0. All five I-only. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (1,) * STANDING_N_SEQUENCES)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0,) * STANDING_N_SEQUENCES)
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(len(self.grams), STANDING_N_SEQUENCES)
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked hapax")
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from the locked 5/0")
        for site, start, gram, nxt, prev4, role, sites, n_on, n_off, off_sites in zip(
            STANDING_CYCLE229_SITES,
            (row[0] for row in STANDING_I_SITES),
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            STANDING_PREVIOUS_4GRAMS,
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
            self.assertEqual(tuple(stems[start[2] - 1 : start[2] + STANDING_N3]), prev4)
            self.assertEqual(site_forward_4gram(stems, start[2], GRAM3), gram)
            self.assertEqual(site_next_4gram(stems, start[2], GRAM2), gram)
            self.assertEqual(site_forward_3gram(stems, start[2], GRAM2), GRAM3)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram[:3], CYCLE195_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE207_GRAM3)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertEqual(role, "forward")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertEqual(off_sites, ())
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, CYCLE228_MATCHING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE226_MATCHING_SITES)
            self.assertNotIn(site, CYCLE227_MATCHING_SITES)
            self.assertNotIn(site, CYCLE195_I_SITES)
        if self.n_i_only != STANDING_N_I_ONLY:
            self.fail("measured N_i_only drifted from 5")
        if self.n_not_i_only != STANDING_N_NOT_I_ONLY:
            self.fail("measured N_not_i_only drifted from 0")
        if not self.claim_holds:
            self.fail("measured forward 4-grams are not all I-only")
        self.assertEqual(self.n_i_only, 5)
        self.assertEqual(self.n_not_i_only, 0)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_EACH)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off, expected_hits in zip(
            self.hits_by_tablet,
            self.off_i,
            STANDING_HITS_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(hits, expected_hits)
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
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
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM3), 0)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], gram), 0)
            self.assertEqual(cycle229_named_off_i_sites(gram), ())
        self.assertEqual(CYCLE223_OFF_I_SITES, (
            (SIDE_TA, "Ta5", 9),
            (SIDE_TA, "Ta7", 5),
            (SIDE_TA, "Ta9", 2),
        ))
        self.assertEqual(
            CYCLE223_OFF_I_FOLLOWING_3GRAMS,
            (("090", "076", "010"), ("090", "076", "126"), ("090", "076", "070")),
        )
        for site, following in zip(
            CYCLE223_OFF_I_SITES,
            CYCLE223_OFF_I_FOLLOWING_3GRAMS,
            strict=True,
        ):
            side, line, index = site
            stems = t_sides[side][TA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + 2]), GRAM2)
            self.assertEqual(tuple(stems[index : index + 3]), following)
            self.assertNotEqual(following, GRAM3)
            for gram in STANDING_SEQUENCES:
                self.assertNotEqual(tuple(stems[index : index + STANDING_N4]), gram)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        ta9 = t_sides[SIDE_TA][TA_LINE_NAMES.index("Ta9")]
        self.assertEqual(tuple(ta9[2:6]), CYCLE219_LEAK_4GRAM)
        self.assertNotEqual(tuple(ta9[2:6]), STANDING_SEQUENCES[3])
        self.assertEqual(
            i_090_076_013_forward_4grams_all_i_only(self.n_i, self.n_off_i),
            STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_090_076_013_FORWARD_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_090_076_013_forward_4grams_all_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE228)
        self.assertFalse(STANDING_SAME_AS_CYCLE229)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_013_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_013_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_229_228_227_226_223_195_and_171_still_compute(self):
        """Cycle 229 5/0, 228 K=5/G=013, 227 6/071, 226 8/070, 223 69/3, 195 6/0, 171 43/0 stay."""
        prior_229 = TestMamariI3gram090076013IOnlyScoreboard()
        prior_229.setUp()
        prior_229.test_i_hits_are_five_on_ia_and_equal_leftover_extra_013()
        prior_229.test_3gram_is_zero_off_i_and_i_only()
        prior_229.test_survey_matches_computed_lock()
        self.assertEqual(prior_229.i_hits, CYCLE229_N_I)
        self.assertEqual(prior_229.i_hits, 5)
        self.assertEqual(prior_229.off_i_hits, CYCLE229_N_OFF_I)
        self.assertEqual(prior_229.off_i_hits, 0)
        self.assertEqual(prior_229.i_sites, CYCLE229_I_SITES)
        self.assertTrue(prior_229.claim_holds)
        self.assertTrue(CYCLE229_I_ONLY)
        if prior_229.i_hits != 5 or prior_229.off_i_hits != 0:
            self.fail("nested cycle 229 090 076 013 I-only 5/0 drifted")
        prior_228 = TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard()
        prior_228.setUp()
        prior_228.test_counts_41_remaining2_g_013_k_5_and_hypothesis_holds()
        prior_228.test_survey_matches_computed_lock()
        self.assertEqual(prior_228.k, 5)
        self.assertEqual(prior_228.g, "013")
        self.assertEqual(prior_228.n_remaining2, 41)
        self.assertEqual(prior_228.matching, CYCLE228_MATCHING_SITES)
        self.assertEqual(prior_228.matching_next_4grams, STANDING_SEQUENCES)
        self.assertTrue(prior_228.claim_holds)
        self.assertTrue(CYCLE228_CLAIM)
        if prior_228.k != 5 or prior_228.g != "013" or prior_228.n_remaining2 != 41:
            self.fail("nested cycle 228 leftover extra remaining-after-071 G=013 K=5 drifted")
        prior_227 = TestMamariILeftoverExtra090076RemainingNextStemScoreboard()
        prior_227.setUp()
        prior_227.test_counts_47_remaining_g_071_k_6_and_hypothesis_holds()
        prior_227.test_survey_matches_computed_lock()
        self.assertEqual(prior_227.k, 6)
        self.assertEqual(CYCLE227_G, "071")
        self.assertEqual(CYCLE227_K, 6)
        self.assertEqual(prior_227.matching, CYCLE227_MATCHING_SITES)
        self.assertTrue(prior_227.claim_holds)
        self.assertTrue(CYCLE227_CLAIM)
        if prior_227.k != 6 or CYCLE227_G != "071":
            self.fail("nested cycle 227 leftover extra remaining 6/071 drifted")
        prior_226 = TestMamariILeftoverExtra090076Forward070Scoreboard()
        prior_226.setUp()
        prior_226.test_counts_8_of_56_and_hypothesis_k_8_holds()
        prior_226.test_survey_matches_computed_lock()
        self.assertEqual(prior_226.k, 8)
        self.assertEqual(CYCLE226_G, "070")
        self.assertEqual(CYCLE226_K, 8)
        self.assertEqual(prior_226.matching, CYCLE226_MATCHING_SITES)
        self.assertTrue(prior_226.claim_holds)
        self.assertTrue(CYCLE226_CLAIM)
        if prior_226.k != 8 or CYCLE226_G != "070":
            self.fail("nested cycle 226 leftover extra 8/070 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, CYCLE223_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, CYCLE223_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, CYCLE223_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertFalse(prior_207.claim_holds)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_195 = TestMamariI3gram090076071IOnlyScoreboard()
        prior_195.setUp()
        prior_195.test_i_hits_are_six_on_ia()
        prior_195.test_3gram_is_zero_off_i_and_i_only()
        prior_195.test_survey_matches_computed_lock()
        self.assertEqual(prior_195.i_hits, CYCLE195_N_I)
        self.assertEqual(prior_195.i_hits, 6)
        self.assertEqual(prior_195.off_i_hits, CYCLE195_N_OFF_I)
        self.assertEqual(prior_195.off_i_hits, 0)
        self.assertEqual(prior_195.i_sites, CYCLE195_I_SITES)
        self.assertTrue(prior_195.claim_holds)
        self.assertTrue(CYCLE195_CLAIM)
        if prior_195.i_hits != 6 or prior_195.off_i_hits != 0:
            self.fail("nested cycle 195 090 076 071 I-only 6/0 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-230 I-forward-4 I-only hold."""
        lock = self.survey["i_090_076_013_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 230)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 5)
        self.assertEqual(lock["N_I"], CYCLE229_N_I)
        self.assertEqual(lock["N_sequences"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_CYCLE229_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["per_site_forward_4grams"],
        )
        self.assertEqual(tuple(lock["per_site_next_stems"]), STANDING_NEXT_STEMS)
        self.assertEqual(
            [list(gram) for gram in STANDING_PREVIOUS_4GRAMS],
            lock["i_previous_4grams"],
        )
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_SEQUENCES)
        for row, gram, site, nxt, role, sites, n_on, n_off, off_sites, hits in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CYCLE229_SITES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_OFF_I_SITES,
            STANDING_HITS_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle229_site"]), site)
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
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["off_i_sites"]),
                off_sites,
            )
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["off_i_tablets_with_hits"]), ())
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(tuple(row["hits_by_tablet"]), hits)
            self.assertTrue(row["i_only"])
            self.assertTrue(row["hapax"])
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_090_076_013_forward_4grams_all_i_only"])
        self.assertEqual(
            lock["i_090_076_013_forward_4grams_all_i_only"],
            STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(lock["i_090_076_013_forward_4grams_i_only"])
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_i_only"], 5)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle229_N_I"], 5)
        self.assertEqual(lock["nested_cycle229_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle228_G"], STANDING_CYCLE228_G)
        self.assertEqual(lock["nested_cycle228_G"], "013")
        self.assertEqual(lock["nested_cycle228_K"], STANDING_CYCLE228_K)
        self.assertEqual(lock["nested_cycle228_K"], 5)
        self.assertEqual(lock["nested_cycle228_N_remaining2"], 41)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle228"])
        self.assertFalse(lock["same_as_cycle229"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["090_076_without_013_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_013_is_not_this_cycle"])
        self.assertTrue(lock["previous_4grams_are_not_this_cycle"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_090_076_013_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_071_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_070_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_090_076_013_i_only"]["cycle"], 229)
        self.assertTrue(self.survey["i_3gram_090_076_013_i_only"]["i_3gram_090_076_013_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_013_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_3gram_090_076_013_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["cycle"],
            228,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"][
                "i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["G"],
            "013",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["K"],
            5,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["N_remaining2"],
            41,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["cycle"], 227)
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["G"], "071")
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["K"], 6)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["cycle"], 226)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["G"], "070")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["K"], 8)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_090_076_070_forward_4grams_i_only"]["cycle"], 219)
        self.assertFalse(
            self.survey["i_090_076_070_forward_4grams_i_only"][
                "i_090_076_070_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_070_forward_4grams_i_only"]["N_i_only"], 7)
        self.assertEqual(self.survey["i_090_076_070_forward_4grams_i_only"]["N_not_i_only"], 1)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["cycle"], 195)
        self.assertTrue(self.survey["i_3gram_090_076_071_i_only"]["i_3gram_090_076_071_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
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


class TestMamariI090076013Forward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 230 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
