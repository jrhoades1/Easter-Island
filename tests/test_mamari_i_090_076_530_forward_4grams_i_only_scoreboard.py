"""I's cycle-239 090 076 530 forward-4-grams off-I lock.

Cycle 240 text-search lock. Uses already-vendored A–V and the
cycle-239 I sites of 3-gram 090 076 530 (all 2 I sites; each
has a next stem). Does not retune those 4-grams, the 2 I
sites, leftover extra remaining-after-700 G=530 K=2
N_remaining5=31, leftover extra remaining-after-001 unique-max
(cycle 234 lost), leftover extra remaining-after-001 700,
leftover extra remaining-after-013 001, leftover extra
remaining-after-071 013, leftover extra remaining 071,
leftover extra forward 070, leftover extra sites, the leftover
n=4 set, or the already-closed leftover remaining family. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 219 (I 090 076 070 forward 4-grams
all I-only lost 7/8; 090 076 070 000 leaks 1/1 on T), cycle
233 (I 090 076 001 forward 4-grams all I-only hapax 1/0 x3),
and cycle 237 (I 090 076 700 forward 4-grams all I-only hapax
1/0 x2). Cycle 239 I 090 076 530 I-only holds 2/0, cycle 238
leftover extra remaining-after-700 K=2 / G=530 N_remaining5=31,
cycle 237 2/0 hapax, cycle 236 2/0, cycle 234 7-way tie at 2,
cycle 233 3/0 hapax, cycle 232 3/0, cycle 223 69/3, cycle 195
6/0, and cycle 171 43/0 stay. Off-I T sites of 090 076 are
not this 3-gram and are not these 4-grams. Leftover extra
remaining after 530 is not locked this cycle. Previous
4-grams of the two I sites are not locked this cycle. The
other five tied stems (280/087/011/005/000) are not locked.
090 after 530 is a different 4-gram from leftover extra
090 076 itself. 090 076 700, 090 076 001, 090 076 013,
090 076 070, 090 076 071, and 090 076 without 530 do not
count. Do not retune leftover n=4, 076-cells, or any
detector.

Locks exact consecutive hits of each I 090 076 530 forward
4-gram on tablet I and on every other vendored tablet A–H
and J–V. The two 4-grams: 090 076 530 090, 090 076 530 499.
Do not assume hapax; count each from fixtures. Hypothesis:
all two are I-only. Measured: each N_I=1 at the cycle-239
I site; all N_off_I=0. Claim that can lose:
i_090_076_530_forward_4grams_all_i_only.
True only if ALL two have N_off_I=0 and N_I>=1. The claim
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
from tests.test_mamari_i_3gram_090_076_001_i_only_scoreboard import (
    GRAM3 as CYCLE232_GRAM3,
    STANDING_I_3GRAM_090_076_001_I_ONLY as CYCLE232_CLAIM,
    STANDING_I_SITES as CYCLE232_I_SITES,
    STANDING_N_I as CYCLE232_N_I,
    STANDING_N_OFF_I as CYCLE232_N_OFF_I,
    TestMamariI3gram090076001IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_013_i_only_scoreboard import (
    GRAM3 as CYCLE229_GRAM3,
    STANDING_I_3GRAM_090_076_013_I_ONLY as CYCLE229_CLAIM,
    STANDING_I_SITES as CYCLE229_I_SITES,
    STANDING_N_I as CYCLE229_N_I,
    STANDING_N_OFF_I as CYCLE229_N_OFF_I,
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
from tests.test_mamari_i_3gram_090_076_530_i_only_scoreboard import (
    GRAM3,
    STANDING_I_3GRAM_090_076_530_I_ONLY as CYCLE239_I_ONLY,
    STANDING_I_NEXT_4GRAMS as CYCLE239_NEXT_4GRAMS,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE239_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE239_I_SITES,
    STANDING_N_I as CYCLE239_N_I,
    STANDING_N_OFF_I as CYCLE239_N_OFF_I,
    extra_i_sites,
    leftover_extra_remaining_after_700_530_subset,
    named_off_i_sites as cycle239_named_off_i_sites,
    TestMamariI3gram090076530IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_700_i_only_scoreboard import (
    GRAM3 as CYCLE236_GRAM3,
    STANDING_I_3GRAM_090_076_700_I_ONLY as CYCLE236_I_ONLY,
    STANDING_I_SITES as CYCLE236_I_SITES,
    STANDING_N_I as CYCLE236_N_I,
    STANDING_N_OFF_I as CYCLE236_N_OFF_I,
    TestMamariI3gram090076700IOnlyScoreboard,
)
from tests.test_mamari_i_090_076_001_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_001_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE233_I_ONLY,
    STANDING_N_I_ONLY as CYCLE233_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE233_N_NOT_I_ONLY,
    TestMamariI090076001Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_013_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_013_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE230_I_ONLY,
    STANDING_N_I_ONLY as CYCLE230_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE230_N_NOT_I_ONLY,
    STANDING_N_OFF_I_EACH as CYCLE230_N_OFF_I_EACH,
    TestMamariI090076013Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_I_ONLY,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_N_OFF_I_EACH as CYCLE219_N_OFF_I_EACH,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
)
from tests.test_mamari_i_090_076_700_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_700_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE237_I_ONLY,
    STANDING_N_I_ONLY as CYCLE237_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE237_N_NOT_I_ONLY,
    TestMamariI090076700Forward4gramsIOnlyScoreboard,
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
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_fwd700_scoreboard import (
    STANDING_G as CYCLE235_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_2_SHARE_700 as CYCLE235_CLAIM,
    STANDING_K as CYCLE235_K,
    STANDING_MATCHING_SITES as CYCLE235_MATCHING_SITES,
    STANDING_N_REMAINING4 as CYCLE235_N_REMAINING4,
    STANDING_OTHER_TIED_STEMS as CYCLE235_OTHER_TIED_STEMS,
    TestMamariILeftoverExtra090076RemainingAfter001Fwd700Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_next_stem_scoreboard import (
    STANDING_G as CYCLE234_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE234_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G as CYCLE234_CLAIM,
    STANDING_K as CYCLE234_K,
    STANDING_N_DISTINCT_REMAINING4 as CYCLE234_N_DISTINCT_REMAINING4,
    STANDING_N_REMAINING4 as CYCLE234_N_REMAINING4,
    STANDING_N_TIED_AT_K as CYCLE234_N_TIED_AT_K,
    STANDING_TIED_STEMS as CYCLE234_TIED_STEMS,
    leftover_extra_remaining_after_001,
    TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_013_next_stem_scoreboard import (
    STANDING_G as CYCLE231_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_013_EXACTLY_K_SHARE_G as CYCLE231_CLAIM,
    STANDING_K as CYCLE231_K,
    TestMamariILeftoverExtra090076RemainingAfter013NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_071_next_stem_scoreboard import (
    STANDING_G as CYCLE228_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G as CYCLE228_CLAIM,
    STANDING_K as CYCLE228_K,
    TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_700_fwd530_scoreboard import (
    GRAM3_FORWARD,
    STANDING_G as CYCLE238_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_700_EXACTLY_2_SHARE_530 as CYCLE238_CLAIM,
    STANDING_K as CYCLE238_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE238_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE238_MATCHING_SITES,
    STANDING_N_REMAINING5 as CYCLE238_N_REMAINING5,
    leftover_extra_remaining_after_700,
    leftover_extra_remaining_after_700_with_530,
    TestMamariILeftoverExtra090076RemainingAfter700Fwd530Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    STANDING_G as CYCLE227_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071 as CYCLE227_CLAIM,
    STANDING_K as CYCLE227_K,
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
STANDING_N_I = 2
STANDING_N_SEQUENCES = 2
STANDING_SEQUENCES = CYCLE239_NEXT_4GRAMS
STANDING_CYCLE239_SITES = CYCLE239_I_SITES
STANDING_NEXT_STEMS = (
    "090",
    "499",
)
STANDING_PREVIOUS_4GRAMS = CYCLE239_PREVIOUS_4GRAMS
STANDING_ROLES = ("forward",) * STANDING_N_SEQUENCES
STANDING_N_I_EACH = (1,) * STANDING_N_SEQUENCES
STANDING_N_ON_I_EACH = (1,) * STANDING_N_SEQUENCES
STANDING_I_SITES = tuple((site,) for site in STANDING_CYCLE239_SITES)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_SEQUENCES
STANDING_OFF_I_SITES = ((), ())
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (STANDING_HITS_BY_TABLET_ONE_ON_I,) * STANDING_N_SEQUENCES
STANDING_N_I_ONLY = 2
STANDING_N_NOT_I_ONLY = 0
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_EACH = True
STANDING_CLAIM = "i_090_076_530_forward_4grams_all_i_only"
STANDING_I_090_076_530_FORWARD_4GRAMS_ALL_I_ONLY = True
STANDING_I_090_076_530_FORWARD_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_090_076_530_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE230 = False
STANDING_SAME_AS_CYCLE233 = False
STANDING_SAME_AS_CYCLE236 = False
STANDING_SAME_AS_CYCLE237 = False
STANDING_SAME_AS_CYCLE238 = False
STANDING_SAME_AS_CYCLE239 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE230 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE233 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE237 = True
STANDING_090_076_700_DOES_NOT_COUNT = True
STANDING_090_076_001_DOES_NOT_COUNT = True
STANDING_090_076_013_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_090_076_WITHOUT_530_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_090_AFTER_530_IS_NOT_LEFTOVER_EXTRA_090_076 = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_530_IS_NOT_THIS_CYCLE = True
STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE = True
STANDING_OTHER_TIED_STEMS_NOT_LOCKED = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_OTHER_TIED_STEMS = ("280", "087", "011", "005", "000")
STANDING_CYCLE238_K = 2
STANDING_CYCLE238_G = "530"
STANDING_CYCLE238_N_REMAINING5 = 31
STANDING_CYCLE239_N_I = 2
STANDING_CYCLE239_N_OFF_I = 0


def forward_4gram_start_site(
    cycle239_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-239 I 090 076 530 site."""
    return cycle239_site


def site_forward_4gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """090 076 530 X if a next stem exists; None at end-of-line."""
    n3 = len(gram3)
    if tuple(stems[index : index + n3]) != gram3:
        return None
    next_index = index + n3
    if next_index >= len(stems):
        return None
    return tuple(stems[index : index + n3 + 1])


def i_090_076_530_forward_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_CYCLE239_SITES,
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
    """I 090 076 530 sites that have no next stem after the 3-gram."""
    return tuple(
        site
        for site, gram in zip(sites, forwards, strict=True)
        if gram is None
    )


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_090_076_530_forward_4grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_SEQUENCES,
) -> bool:
    """True iff all 2 I 090 076 530 forward 4-grams are I-only.

    Claim holds only if every gram has N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only. Hapax is not
    assumed; N_I may be greater than 1. Length must stay 2.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestI090076530Forward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-239 I 090 076 530 forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 700 / 001 / 013 / 070 / 071 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "530", "090"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("090", "076", "530", "499"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_SEQUENCES)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:3], GRAM3)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["090", "076", "530", "090", "090", "076", "530", "090"]]
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
        self.assertEqual(ngram_hit_count([list(CYCLE229_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE232_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE236_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "530"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "700", "011"]], STANDING_SEQUENCES[0]), 0)
        planted = ["090", "090", "076", "530", "090"]
        self.assertEqual(site_forward_4gram(planted, 1, GRAM3), STANDING_SEQUENCES[0])
        self.assertEqual(site_next_4gram(planted, 1, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_forward_3gram(planted, 1, GRAM2), GRAM3)
        self.assertTrue(STANDING_090_076_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_001_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_013_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_530_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_AFTER_530_IS_NOT_LEFTOVER_EXTRA_090_076)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all 2 forward 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(i_090_076_530_forward_4grams_all_i_only(hold_ones, hold_zeros))
        self.assertTrue(
            i_090_076_530_forward_4grams_all_i_only((2,) + hold_ones[1:], hold_zeros)
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_090_076_530_forward_4grams_all_i_only(hold_ones, tuple(lose_off))
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_090_076_530_forward_4grams_all_i_only(tuple(lose_missing_i), hold_zeros)
        )
        self.assertFalse(i_090_076_530_forward_4grams_all_i_only((), ()))
        self.assertFalse(
            i_090_076_530_forward_4grams_all_i_only(hold_ones[:-1], hold_zeros[:-1])
        )
        self.assertEqual(STANDING_CLAIM, "i_090_076_530_forward_4grams_all_i_only")
        self.assertTrue(STANDING_I_090_076_530_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_090_076_530_FORWARD_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_090_076_530_FORWARD_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_N_OFF_I_EACH[-1], 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertTrue(CYCLE230_I_ONLY)
        self.assertEqual(CYCLE230_N_I_ONLY, 5)
        self.assertEqual(CYCLE230_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE230_N_OFF_I_EACH, (0, 0, 0, 0, 0))
        self.assertTrue(CYCLE233_I_ONLY)
        self.assertEqual(CYCLE233_N_I_ONLY, 3)
        self.assertEqual(CYCLE233_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE237_I_ONLY)
        self.assertEqual(CYCLE237_N_I_ONLY, 2)
        self.assertEqual(CYCLE237_N_NOT_I_ONLY, 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_239_forwards_not_retuned(self):
        """4-grams stay the cycle-239 I forwards; leftover / 700 / 001 / 013 / 070 / 071 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "530"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(STANDING_SEQUENCES, CYCLE239_NEXT_4GRAMS)
        self.assertEqual(STANDING_SEQUENCES, CYCLE238_MATCHING_NEXT_4GRAMS)
        self.assertEqual(STANDING_CYCLE239_SITES, CYCLE239_I_SITES)
        self.assertEqual(STANDING_CYCLE239_SITES, CYCLE238_MATCHING_SITES)
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE239_N_I)
        self.assertEqual(CYCLE239_N_I, 2)
        self.assertEqual(CYCLE239_N_OFF_I, 0)
        self.assertEqual(len(set(STANDING_NEXT_STEMS)), 2)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(CYCLE195_GRAM3, ("090", "076", "071"))
        self.assertEqual(CYCLE207_GRAM3, ("090", "076", "070"))
        self.assertEqual(CYCLE229_GRAM3, ("090", "076", "013"))
        self.assertEqual(CYCLE232_GRAM3, ("090", "076", "001"))
        self.assertEqual(CYCLE236_GRAM3, ("090", "076", "700"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(CYCLE195_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE207_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE229_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE232_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE236_GRAM3, gram))
            self.assertNotEqual(gram[:3], CYCLE195_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE207_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE229_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE232_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE236_GRAM3)
            self.assertNotEqual(gram[:2], CYCLE171_GRAM2)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram, GRAM2)
            self.assertNotEqual(gram, ("090", "076"))
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "530", "090"))
        self.assertEqual(STANDING_SEQUENCES[0][:2], GRAM2)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM2)
        self.assertTrue(STANDING_090_AFTER_530_IS_NOT_LEFTOVER_EXTRA_090_076)
        for site, start in zip(
            STANDING_CYCLE239_SITES,
            (sites[0] for sites in STANDING_I_SITES),
            strict=True,
        ):
            self.assertEqual(forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE230)
        self.assertFalse(STANDING_SAME_AS_CYCLE233)
        self.assertFalse(STANDING_SAME_AS_CYCLE236)
        self.assertFalse(STANDING_SAME_AS_CYCLE237)
        self.assertFalse(STANDING_SAME_AS_CYCLE238)
        self.assertFalse(STANDING_SAME_AS_CYCLE239)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE230)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE233)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE237)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_530_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_090_AFTER_530_IS_NOT_LEFTOVER_EXTRA_090_076)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI090076530Forward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture I 090 076 530 forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle239_sites = STANDING_CYCLE239_SITES
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
            cycle239_named_off_i_sites(gram) for gram in self.grams
        )
        self.measured_forwards = i_090_076_530_forward_4grams(
            self.i_sides,
            self.cycle239_sites,
            GRAM3,
        )
        self.no_forward = i_sites_without_forward(
            self.cycle239_sites,
            self.measured_forwards,
        )
        self.next_stems = leftover_extra_next_stems(
            self.i_sides,
            STANDING_LEFTOVER_SITES,
            GRAM2,
        )
        self.remaining4 = leftover_extra_remaining_after_001(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.remaining5 = leftover_extra_remaining_after_700(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.leftover_matching = leftover_extra_remaining_after_700_with_530(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
            CYCLE238_G,
        )
        self.leftover_matching_next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.leftover_matching,
            GRAM2,
        )
        self.extra = extra_i_sites(self.cycle239_sites, self.leftover_matching)
        self.n3_i = ngram_hit_count(self.i_sides[SIDE_IA], GRAM3) + STANDING_IB_HITS
        self.n3_off_i = sum(tablet_hit_counts(self.by_tablet, GRAM3, OFF_I_TABLETS))
        self.claim_holds = i_090_076_530_forward_4grams_all_i_only(
            self.n_i,
            self.n_off_i,
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = STANDING_N_SEQUENCES - self.n_i_only

    def test_tokens_and_sites_are_cycle_239_forwards_not_retuned(self):
        """4-grams and I sites stay the cycle-239 forward lock. Nested 2/0 must hold."""
        self.assertEqual(GRAM3, ("090", "076", "530"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle239_sites, STANDING_CYCLE239_SITES)
        self.assertEqual(self.cycle239_sites, CYCLE239_I_SITES)
        self.assertEqual(self.cycle239_sites, CYCLE238_MATCHING_SITES)
        self.assertEqual(self.measured_forwards, STANDING_SEQUENCES)
        self.assertEqual(self.measured_forwards, CYCLE239_NEXT_4GRAMS)
        self.assertEqual(self.measured_forwards, CYCLE238_MATCHING_NEXT_4GRAMS)
        self.assertEqual(self.leftover_matching_next_4grams, STANDING_SEQUENCES)
        self.assertEqual(self.no_forward, ())
        self.assertEqual(self.n3_i, STANDING_CYCLE239_N_I)
        self.assertEqual(self.n3_i, 2)
        self.assertEqual(self.n3_off_i, STANDING_CYCLE239_N_OFF_I)
        self.assertEqual(self.n3_off_i, 0)
        self.assertEqual(self.leftover_matching, CYCLE238_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE239_I_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE238_K)
        self.assertEqual(STANDING_CYCLE238_K, 2)
        self.assertEqual(STANDING_CYCLE238_G, "530")
        self.assertEqual(CYCLE238_G, "530")
        self.assertEqual(CYCLE238_K, 2)
        self.assertEqual(len(self.remaining5), CYCLE238_N_REMAINING5)
        self.assertEqual(len(self.remaining5), 31)
        self.assertEqual(len(self.remaining4), CYCLE234_N_REMAINING4)
        self.assertEqual(len(self.remaining4), 33)
        self.assertTrue(
            leftover_extra_remaining_after_700_530_subset(
                self.leftover_matching,
                self.cycle239_sites,
            )
        )
        self.assertEqual(self.extra, ())
        if self.n3_i != 2 or self.n3_off_i != 0:
            self.fail("nested cycle 239 090 076 530 I-only 2/0 drifted")
        if len(self.leftover_matching) != 2 or CYCLE238_G != "530":
            self.fail("nested cycle 238 leftover extra remaining-after-700 G=530 K=2 drifted")
        if self.extra:
            self.fail("extra I 090 076 530 sites appeared; leftover of leftover is not this cycle")
        prior_239 = self.survey["i_3gram_090_076_530_i_only"]
        self.assertEqual(prior_239["cycle"], 239)
        self.assertEqual(prior_239["N_I"], CYCLE239_N_I)
        self.assertEqual(prior_239["N_I"], 2)
        self.assertEqual(prior_239["N_off_I"], CYCLE239_N_OFF_I)
        self.assertEqual(prior_239["N_off_I"], 0)
        self.assertTrue(prior_239["i_3gram_090_076_530_i_only"])
        self.assertTrue(CYCLE239_I_ONLY)
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_239["i_next_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_239["i_sites"]),
            STANDING_CYCLE239_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PREVIOUS_4GRAMS],
            prior_239["i_previous_4grams"],
        )
        prior_238 = self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"]
        self.assertEqual(prior_238["cycle"], 238)
        self.assertEqual(prior_238["G"], "530")
        self.assertEqual(prior_238["K"], 2)
        self.assertEqual(prior_238["N_remaining5"], 31)
        self.assertTrue(prior_238["i_leftover_extra_090_076_remaining_after_700_exactly_2_share_530"])
        self.assertTrue(CYCLE238_CLAIM)
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_238["matching_next_4grams"],
        )
        prior_237 = self.survey["i_090_076_700_forward_4grams_i_only"]
        self.assertEqual(prior_237["cycle"], 237)
        self.assertTrue(prior_237["i_090_076_700_forward_4grams_all_i_only"])
        self.assertEqual(prior_237["N_i_only"], 2)
        self.assertEqual(prior_237["N_not_i_only"], 0)
        self.assertTrue(CYCLE237_I_ONLY)
        prior_236 = self.survey["i_3gram_090_076_700_i_only"]
        self.assertEqual(prior_236["cycle"], 236)
        self.assertEqual(prior_236["N_I"], CYCLE236_N_I)
        self.assertEqual(prior_236["N_I"], 2)
        self.assertEqual(prior_236["N_off_I"], CYCLE236_N_OFF_I)
        self.assertEqual(prior_236["N_off_I"], 0)
        self.assertTrue(prior_236["i_3gram_090_076_700_i_only"])
        self.assertTrue(CYCLE236_I_ONLY)
        prior_234 = self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]
        self.assertEqual(prior_234["cycle"], 234)
        self.assertEqual(prior_234["N_remaining4"], 33)
        self.assertEqual(prior_234["N_distinct_remaining4"], 26)
        self.assertEqual(prior_234["N_tied_at_K"], 7)
        self.assertFalse(prior_234["G_uniquely_most_frequent"])
        self.assertFalse(prior_234["i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G"])
        prior_233 = self.survey["i_090_076_001_forward_4grams_i_only"]
        self.assertEqual(prior_233["cycle"], 233)
        self.assertTrue(prior_233["i_090_076_001_forward_4grams_all_i_only"])
        self.assertEqual(prior_233["N_i_only"], 3)
        self.assertEqual(prior_233["N_not_i_only"], 0)
        self.assertTrue(CYCLE233_I_ONLY)
        prior_232 = self.survey["i_3gram_090_076_001_i_only"]
        self.assertEqual(prior_232["cycle"], 232)
        self.assertEqual(prior_232["N_I"], CYCLE232_N_I)
        self.assertEqual(prior_232["N_I"], 3)
        self.assertEqual(prior_232["N_off_I"], CYCLE232_N_OFF_I)
        self.assertEqual(prior_232["N_off_I"], 0)
        self.assertTrue(prior_232["i_3gram_090_076_001_i_only"])
        self.assertTrue(CYCLE232_CLAIM)
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
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_530_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(CYCLE235_OTHER_TIED_STEMS, ("530", "280", "087", "011", "005", "000"))
        self.assertEqual(STANDING_OTHER_TIED_STEMS, ("280", "087", "011", "005", "000"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """Each forward 4-gram is 1/0. All two I-only. Claim holds."""
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
            self.fail("measured N_off_I drifted from the locked 2/0")
        for site, start, gram, nxt, prev4, role, sites, n_on, n_off, off_sites in zip(
            STANDING_CYCLE239_SITES,
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
            self.assertNotEqual(gram[:3], CYCLE229_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE232_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE236_GRAM3)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram, GRAM2)
            self.assertEqual(role, "forward")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertEqual(off_sites, ())
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, CYCLE238_MATCHING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE226_MATCHING_SITES)
            self.assertNotIn(site, CYCLE229_I_SITES)
            self.assertNotIn(site, CYCLE232_I_SITES)
            self.assertNotIn(site, CYCLE236_I_SITES)
            self.assertNotIn(site, CYCLE195_I_SITES)
        if self.n_i_only != STANDING_N_I_ONLY:
            self.fail("measured N_i_only drifted from 2")
        if self.n_not_i_only != STANDING_N_NOT_I_ONLY:
            self.fail("measured N_not_i_only drifted from 0")
        if not self.claim_holds:
            self.fail("measured forward 4-grams are not all I-only")
        self.assertEqual(self.n_i_only, 2)
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
            self.assertEqual(cycle239_named_off_i_sites(gram), ())
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
        self.assertNotEqual(tuple(ta9[2:6]), STANDING_SEQUENCES[0])
        self.assertEqual(
            i_090_076_530_forward_4grams_all_i_only(self.n_i, self.n_off_i),
            STANDING_I_090_076_530_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_090_076_530_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_090_076_530_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_090_076_530_FORWARD_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_090_076_530_forward_4grams_all_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE230)
        self.assertFalse(STANDING_SAME_AS_CYCLE233)
        self.assertFalse(STANDING_SAME_AS_CYCLE236)
        self.assertFalse(STANDING_SAME_AS_CYCLE237)
        self.assertFalse(STANDING_SAME_AS_CYCLE238)
        self.assertFalse(STANDING_SAME_AS_CYCLE239)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE230)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE233)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE237)
        self.assertTrue(STANDING_090_076_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_001_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_013_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_530_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_AFTER_530_IS_NOT_LEFTOVER_EXTRA_090_076)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_530_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_239_238_237_236_234_233_232_223_195_and_171_still_compute(self):
        """Cycle 239 2/0, 238 K=2/G=530, 237 2/0 hapax, 236 2/0, 234 7-way tie, 233 3/0 hapax, 232 3/0, 223 69/3, 195 6/0, 171 43/0 stay."""
        prior_239 = TestMamariI3gram090076530IOnlyScoreboard()
        prior_239.setUp()
        prior_239.test_i_hits_are_two_on_ia_and_equal_leftover_extra_530()
        prior_239.test_3gram_is_zero_off_i_and_i_only()
        prior_239.test_survey_matches_computed_lock()
        self.assertEqual(prior_239.i_hits, CYCLE239_N_I)
        self.assertEqual(prior_239.i_hits, 2)
        self.assertEqual(prior_239.off_i_hits, CYCLE239_N_OFF_I)
        self.assertEqual(prior_239.off_i_hits, 0)
        self.assertEqual(prior_239.i_sites, CYCLE239_I_SITES)
        self.assertTrue(prior_239.claim_holds)
        self.assertTrue(CYCLE239_I_ONLY)
        if prior_239.i_hits != 2 or prior_239.off_i_hits != 0:
            self.fail("nested cycle 239 090 076 530 I-only 2/0 drifted")
        prior_238 = TestMamariILeftoverExtra090076RemainingAfter700Fwd530Scoreboard()
        prior_238.setUp()
        prior_238.test_counts_2_of_31_and_hypothesis_k_2_holds()
        prior_238.test_survey_matches_computed_lock()
        self.assertEqual(prior_238.k, 2)
        self.assertEqual(CYCLE238_G, "530")
        self.assertEqual(prior_238.n_remaining5, 31)
        self.assertEqual(prior_238.matching, CYCLE238_MATCHING_SITES)
        self.assertEqual(prior_238.matching_next_4grams, STANDING_SEQUENCES)
        self.assertTrue(prior_238.claim_holds)
        self.assertTrue(CYCLE238_CLAIM)
        if prior_238.k != 2 or CYCLE238_G != "530" or prior_238.n_remaining5 != 31:
            self.fail("nested cycle 238 leftover extra remaining-after-700 G=530 K=2 drifted")
        prior_237 = TestMamariI090076700Forward4gramsIOnlyScoreboard()
        prior_237.setUp()
        prior_237.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_237.test_survey_matches_computed_lock()
        self.assertEqual(prior_237.n_i_only, 2)
        self.assertEqual(prior_237.n_not_i_only, 0)
        self.assertTrue(prior_237.claim_holds)
        self.assertTrue(CYCLE237_I_ONLY)
        self.assertEqual(CYCLE237_N_I_ONLY, 2)
        self.assertEqual(CYCLE237_N_NOT_I_ONLY, 0)
        if prior_237.n_i_only != 2 or prior_237.n_not_i_only != 0:
            self.fail("nested cycle 237 090 076 700 forward 4-grams 2/0 hapax drifted")
        prior_236 = TestMamariI3gram090076700IOnlyScoreboard()
        prior_236.setUp()
        prior_236.test_i_hits_are_two_on_ia_and_equal_leftover_extra_700()
        prior_236.test_3gram_is_zero_off_i_and_i_only()
        prior_236.test_survey_matches_computed_lock()
        self.assertEqual(prior_236.i_hits, CYCLE236_N_I)
        self.assertEqual(prior_236.i_hits, 2)
        self.assertEqual(prior_236.off_i_hits, CYCLE236_N_OFF_I)
        self.assertEqual(prior_236.off_i_hits, 0)
        self.assertEqual(prior_236.i_sites, CYCLE236_I_SITES)
        self.assertTrue(prior_236.claim_holds)
        self.assertTrue(CYCLE236_I_ONLY)
        if prior_236.i_hits != 2 or prior_236.off_i_hits != 0:
            self.fail("nested cycle 236 090 076 700 I-only 2/0 drifted")
        prior_235 = TestMamariILeftoverExtra090076RemainingAfter001Fwd700Scoreboard()
        prior_235.setUp()
        prior_235.test_counts_2_of_33_and_hypothesis_k_2_holds()
        prior_235.test_survey_matches_computed_lock()
        self.assertEqual(prior_235.k, 2)
        self.assertEqual(prior_235.g, "700")
        self.assertEqual(prior_235.n_remaining4, 33)
        self.assertEqual(prior_235.matching, CYCLE235_MATCHING_SITES)
        self.assertTrue(prior_235.claim_holds)
        self.assertTrue(CYCLE235_CLAIM)
        if prior_235.k != 2 or prior_235.g != "700" or prior_235.n_remaining4 != 33:
            self.fail("nested cycle 235 leftover extra remaining-after-001 G=700 K=2 drifted")
        prior_234 = TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard()
        prior_234.setUp()
        prior_234.test_counts_33_remaining4_g_700_k_2_and_hypothesis_loses()
        prior_234.test_survey_matches_computed_lock()
        self.assertEqual(prior_234.n_remaining4, 33)
        self.assertEqual(prior_234.n_distinct_remaining4, 26)
        self.assertEqual(prior_234.k, 2)
        self.assertEqual(CYCLE234_G, "700")
        self.assertFalse(prior_234.unique)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(prior_234.claim_holds)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertEqual(CYCLE234_N_REMAINING4, 33)
        self.assertEqual(CYCLE234_N_DISTINCT_REMAINING4, 26)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertEqual(CYCLE234_TIED_STEMS, ("700", "530", "280", "087", "011", "005", "000"))
        if (
            prior_234.n_remaining4 != 33
            or prior_234.n_distinct_remaining4 != 26
            or prior_234.k != 2
            or prior_234.unique
        ):
            self.fail("nested cycle 234 leftover extra remaining-after-001 7-way tie at 2 drifted")
        prior_233 = TestMamariI090076001Forward4gramsIOnlyScoreboard()
        prior_233.setUp()
        prior_233.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_233.test_survey_matches_computed_lock()
        self.assertEqual(prior_233.n_i_only, 3)
        self.assertEqual(prior_233.n_not_i_only, 0)
        self.assertTrue(prior_233.claim_holds)
        self.assertTrue(CYCLE233_I_ONLY)
        self.assertEqual(CYCLE233_N_I_ONLY, 3)
        self.assertEqual(CYCLE233_N_NOT_I_ONLY, 0)
        if prior_233.n_i_only != 3 or prior_233.n_not_i_only != 0:
            self.fail("nested cycle 233 090 076 001 forward 4-grams 3/0 hapax drifted")
        prior_232 = TestMamariI3gram090076001IOnlyScoreboard()
        prior_232.setUp()
        prior_232.test_i_hits_are_three_on_ia_and_equal_leftover_extra_001()
        prior_232.test_3gram_is_zero_off_i_and_i_only()
        prior_232.test_survey_matches_computed_lock()
        self.assertEqual(prior_232.i_hits, CYCLE232_N_I)
        self.assertEqual(prior_232.i_hits, 3)
        self.assertEqual(prior_232.off_i_hits, CYCLE232_N_OFF_I)
        self.assertEqual(prior_232.off_i_hits, 0)
        self.assertEqual(prior_232.i_sites, CYCLE232_I_SITES)
        self.assertTrue(prior_232.claim_holds)
        self.assertTrue(CYCLE232_CLAIM)
        if prior_232.i_hits != 3 or prior_232.off_i_hits != 0:
            self.fail("nested cycle 232 090 076 001 I-only 3/0 drifted")
        prior_231 = TestMamariILeftoverExtra090076RemainingAfter013NextStemScoreboard()
        prior_231.setUp()
        prior_231.test_counts_36_remaining3_g_001_k_3_and_hypothesis_holds()
        self.assertEqual(CYCLE231_K, 3)
        self.assertEqual(CYCLE231_G, "001")
        self.assertTrue(CYCLE231_CLAIM)
        prior_230 = TestMamariI090076013Forward4gramsIOnlyScoreboard()
        prior_230.setUp()
        prior_230.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        self.assertEqual(prior_230.n_i_only, 5)
        self.assertEqual(prior_230.n_not_i_only, 0)
        self.assertTrue(prior_230.claim_holds)
        self.assertTrue(CYCLE230_I_ONLY)
        if prior_230.n_i_only != 5 or prior_230.n_not_i_only != 0:
            self.fail("nested cycle 230 090 076 013 forward 4-grams 5/0 hapax drifted")
        prior_229 = TestMamariI3gram090076013IOnlyScoreboard()
        prior_229.setUp()
        prior_229.test_i_hits_are_five_on_ia_and_equal_leftover_extra_013()
        prior_229.test_3gram_is_zero_off_i_and_i_only()
        self.assertEqual(prior_229.i_hits, CYCLE229_N_I)
        self.assertEqual(prior_229.i_hits, 5)
        self.assertEqual(prior_229.off_i_hits, CYCLE229_N_OFF_I)
        self.assertEqual(prior_229.off_i_hits, 0)
        self.assertTrue(prior_229.claim_holds)
        self.assertTrue(CYCLE229_CLAIM)
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
        prior_226 = TestMamariILeftoverExtra090076Forward070Scoreboard()
        prior_226.setUp()
        prior_226.test_counts_8_of_56_and_hypothesis_k_8_holds()
        self.assertEqual(CYCLE226_K, 8)
        self.assertEqual(CYCLE226_G, "070")
        self.assertTrue(CYCLE226_CLAIM)
        prior_227 = TestMamariILeftoverExtra090076RemainingNextStemScoreboard()
        prior_227.setUp()
        prior_227.test_counts_47_remaining_g_071_k_6_and_hypothesis_holds()
        self.assertEqual(CYCLE227_K, 6)
        self.assertEqual(CYCLE227_G, "071")
        self.assertTrue(CYCLE227_CLAIM)
        prior_228 = TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard()
        prior_228.setUp()
        prior_228.test_counts_41_remaining2_g_013_k_5_and_hypothesis_holds()
        self.assertEqual(CYCLE228_K, 5)
        self.assertEqual(CYCLE228_G, "013")
        self.assertTrue(CYCLE228_CLAIM)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE235_OTHER_TIED_STEMS, ("530", "280", "087", "011", "005", "000"))
        self.assertEqual(STANDING_OTHER_TIED_STEMS, ("280", "087", "011", "005", "000"))
        self.assertTrue(STANDING_OTHER_TIED_STEMS_NOT_LOCKED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-240 I-forward-4 I-only hold."""
        lock = self.survey["i_090_076_530_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 240)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 2)
        self.assertEqual(lock["N_I"], CYCLE239_N_I)
        self.assertEqual(lock["N_sequences"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_CYCLE239_SITES,
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
            STANDING_CYCLE239_SITES,
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
            self.assertEqual(tuple(row["cycle239_site"]), site)
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
        self.assertTrue(lock["i_090_076_530_forward_4grams_all_i_only"])
        self.assertEqual(
            lock["i_090_076_530_forward_4grams_all_i_only"],
            STANDING_I_090_076_530_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(lock["i_090_076_530_forward_4grams_i_only"])
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_i_only"], 2)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle239_N_I"], 2)
        self.assertEqual(lock["nested_cycle239_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle238_G"], STANDING_CYCLE238_G)
        self.assertEqual(lock["nested_cycle238_G"], "530")
        self.assertEqual(lock["nested_cycle238_K"], STANDING_CYCLE238_K)
        self.assertEqual(lock["nested_cycle238_K"], 2)
        self.assertEqual(lock["nested_cycle238_N_remaining5"], 31)
        self.assertEqual(lock["nested_cycle237_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle237_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle236_N_I"], 2)
        self.assertEqual(lock["nested_cycle236_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle234_N_remaining4"], 33)
        self.assertEqual(lock["nested_cycle234_N_distinct_remaining4"], 26)
        self.assertEqual(lock["nested_cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["nested_cycle234_G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["nested_cycle234_tied_stems_at_K"]), CYCLE234_TIED_STEMS)
        self.assertEqual(lock["nested_cycle233_N_i_only"], 3)
        self.assertEqual(lock["nested_cycle233_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle232_N_I"], 3)
        self.assertEqual(lock["nested_cycle232_N_off_I"], 0)
        self.assertEqual(tuple(lock["other_tied_stems"]), STANDING_OTHER_TIED_STEMS)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle230"])
        self.assertFalse(lock["same_as_cycle233"])
        self.assertFalse(lock["same_as_cycle236"])
        self.assertFalse(lock["same_as_cycle237"])
        self.assertFalse(lock["same_as_cycle238"])
        self.assertFalse(lock["same_as_cycle239"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["same_claim_shape_as_cycle230"])
        self.assertTrue(lock["same_claim_shape_as_cycle233"])
        self.assertTrue(lock["same_claim_shape_as_cycle237"])
        self.assertTrue(lock["090_076_700_does_not_count"])
        self.assertTrue(lock["090_076_001_does_not_count"])
        self.assertTrue(lock["090_076_013_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["090_076_without_530_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["090_after_530_is_not_leftover_extra_090_076"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_530_is_not_this_cycle"])
        self.assertTrue(lock["previous_4grams_are_not_this_cycle"])
        self.assertTrue(lock["other_tied_stems_not_locked"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_090_076_530_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_700_fwd530_unchanged"])
        self.assertTrue(lock["standing_i_090_076_700_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_700_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_fwd700_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_001_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_001_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_013_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_013_forward_4grams_i_only_unchanged"])
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
        self.assertEqual(self.survey["i_3gram_090_076_530_i_only"]["cycle"], 239)
        self.assertTrue(self.survey["i_3gram_090_076_530_i_only"]["i_3gram_090_076_530_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_530_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_090_076_530_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"]["cycle"],
            238,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"][
                "i_leftover_extra_090_076_remaining_after_700_exactly_2_share_530"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"]["G"],
            "530",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"]["K"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_700_fwd530"]["N_remaining5"],
            31,
        )
        self.assertEqual(self.survey["i_090_076_700_forward_4grams_i_only"]["cycle"], 237)
        self.assertTrue(
            self.survey["i_090_076_700_forward_4grams_i_only"][
                "i_090_076_700_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_700_forward_4grams_i_only"]["N_i_only"], 2)
        self.assertEqual(self.survey["i_090_076_700_forward_4grams_i_only"]["N_not_i_only"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_700_i_only"]["cycle"], 236)
        self.assertTrue(self.survey["i_3gram_090_076_700_i_only"]["i_3gram_090_076_700_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_700_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_090_076_700_i_only"]["N_off_I"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]["cycle"],
            234,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"][
                "i_leftover_extra_090_076_remaining_after_001_exactly_K_share_G"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]["N_remaining4"],
            33,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]["N_tied_at_K"],
            7,
        )
        self.assertEqual(self.survey["i_090_076_001_forward_4grams_i_only"]["cycle"], 233)
        self.assertTrue(
            self.survey["i_090_076_001_forward_4grams_i_only"][
                "i_090_076_001_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_001_forward_4grams_i_only"]["N_i_only"], 3)
        self.assertEqual(self.survey["i_090_076_001_forward_4grams_i_only"]["N_not_i_only"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_001_i_only"]["cycle"], 232)
        self.assertTrue(self.survey["i_3gram_090_076_001_i_only"]["i_3gram_090_076_001_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_001_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_001_i_only"]["N_off_I"], 0)
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


class TestMamariI090076530Forward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 240 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
