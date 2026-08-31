"""I's leftover n=4 remaining remaining-after-090-076 430 076 4-grams I-only lock.

Cycle 331 text-search lock. Uses already-vendored A–V and the
cycle-329 leftover n=4 remaining remaining-after-090-076 labeled
G=430 076 matching leftovers (exactly K=2 of N=11):
430 076 001 076 and 430 076 049 400. Does not retune that
exactly-K lock, cycle 330 2-gram 430 076 I-only LOSE, cycle
328 unique-max, cycle 222, leftover n=4 remaining I 090 076
peels (288–327), leftover extra 090 076 peels, or cycles
220–221 / 223. Does not vendor a new tablet. Does not scrape
X. W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Population (locked, do not re-derive as a new claim): leftover
n=4 remaining remaining-after-090-076 N=11 leftover 4-grams
that do not contain 090 076. Cycle 328 LOSE unique most
frequent 2-gram (5-way tie at K=2, G=430 076 largest-id).
Cycle 329 HOLD: exactly 2 of the N=11 contain contiguous
430 076, matching leftovers 430 076 001 076 and
430 076 049 400. N_remaining after peeling G=9. Cycle 330
LOSE: 2-gram 430 076 is not I-only (N_I=30, N_off_I=16
including T at Ta4[19]/Ta8[2], extra I=26, leftover matching
sites 4). Extra I ≠ 0 is recorded, not this cycle's claim.
Do not re-lock 2-gram I-only or all-I-inside-family (all-inside
is false by extra I=26; skip that analog of cycle 224). This
cycle's N=2 population is those two leftover 4-grams.

Already locked (record overlap only, do not re-lock): nested
cycle 329 exactly-2-share-430 076 and cycle 328 unique_max
false stay nested. Cycle 330 2-gram 430 076 I-only LOSE stays
nested (2-gram can leak while 4-grams do not). Cycle 222,
leftover n=4 remaining I 090 076 peels (288–327), leftover
extra 090 076 peels, cycles 220–221, cycle 223.

Same claim-shape as cycle 291 leftover n=4 remaining
090 076 020 forward 4-grams all I-only 4/0 not hapax HOLD
after cycle 290 3-gram I-only. Also analog cycle 309 leftover
n=4 remaining remaining-after-600 previous 4-grams all I-only
hapax 6/0 after a unique-stem LOSE. Hapax is not required
(cycle 309's six 4-grams happened to be hapax). Cycle 219
I 090 076 070 forward 4-grams lost 7/8; 090 076 070 000
leaks 1/1 on T — the lose-path analog. Given 2-gram 430 076
already leaks on T (cycle 330 30/16), this is a real lose
path. Do not lock leftover extra prefixes 090 430 076 006 /
700 430 076 006 (cycle 154). Do not lock independent 5-gram
430 076 006 000 076. Gv7[25] leftover 3-gram prefix
430 076 049 on G is not 430 076 049 400. Do not retune
leftover n=4, leftover extra peels, 076-cells, or any
detector. Do not assume the I-only result.

Locks exact consecutive hits of each leftover remaining-after-
090-076 4-gram that contains 430 076 on tablet I and on
every other vendored tablet A–H and J–V. Claim that can lose:
i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only.
True iff both leftover 4-grams have N_I ≥ 1 and N_off_I = 0
(N_leak=0 per 4-gram). This can lose if either leaks onto T
(or any off-I tablet). Measured: 430 076 001 076 is N_I=2 at
Ia10[103]/Ia13[156], N_off_I=0, not hapax; 430 076 049 400
is N_I=2 at Ia13[170]/Ia14[63], N_off_I=0, not hapax. Leftover
matching sites equal the I sites (4); extra I of the 4-grams
is 0. Nested cycle 330 2-gram leak stays nested, not re-locked.
The claim is true. Do not retune.

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
)
from tests.test_mamari_i_090_076_020_forward_4grams_i_only_scoreboard import (
    STANDING_HAPAX_EACH as CYCLE291_HAPAX_EACH,
    STANDING_I_090_076_020_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE291_CLAIM,
    STANDING_N_I_EACH as CYCLE291_N_I_EACH,
    STANDING_N_I_ONLY as CYCLE291_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE291_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE291_N_NOT_I_ONLY,
    STANDING_N_OFF_I_EACH as CYCLE291_N_OFF_I_EACH,
    STANDING_SEQUENCES as CYCLE291_SEQUENCES,
    TestMamariI090076020Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_CLAIM,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
    TestMamariI090076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2 as CYCLE223_GRAM2,
    STANDING_I_2GRAM_090_076_I_ONLY as CYCLE223_CLAIM,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
    i_2gram_090_076_i_only,
)
from tests.test_mamari_i_2gram_430_076_i_only_scoreboard import (
    GRAM2 as CYCLE330_GRAM2,
    STANDING_EXTRA_I_SITES as CYCLE330_EXTRA_I_SITES,
    STANDING_I_2GRAM_430_076_I_ONLY as CYCLE330_CLAIM,
    STANDING_LEFTOVER_MATCHING_COUNT as CYCLE330_LEFTOVER_MATCHING_COUNT,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE330_LEFTOVER_MATCHING_SITES,
    STANDING_N_EXTRA as CYCLE330_N_EXTRA,
    STANDING_N_I as CYCLE330_N_I,
    STANDING_N_OFF_I as CYCLE330_N_OFF_I,
    STANDING_N_T as CYCLE330_N_T,
    STANDING_OFF_I_SITES as CYCLE330_OFF_I_SITES,
    STANDING_T_SITES as CYCLE330_T_SITES,
    TestMamariI2gram430076IOnlyScoreboard,
    i_2gram_430_076_i_only,
    leftover_matching_sites as cycle330_leftover_matching_sites,
    named_off_i_sites,
)
from tests.test_mamari_i_3gram_090_076_020_i_only_scoreboard import (
    GRAM3 as CYCLE290_GRAM3,
    STANDING_I_3GRAM_090_076_020_I_ONLY as CYCLE290_CLAIM,
    STANDING_N_EXTRA as CYCLE290_N_EXTRA,
    STANDING_N_I as CYCLE290_N_I,
    STANDING_N_OFF_I as CYCLE290_N_OFF_I,
    TestMamariI3gram090076020IOnlyScoreboard,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    STANDING_I_5GRAM_999_090_076_070_000_I_ONLY as CYCLE220_I_ONLY,
    STANDING_N_I as CYCLE220_N_I,
    STANDING_N_OFF_I as CYCLE220_N_OFF_I,
    TestMamariI5gram999090076070000IOnlyScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_430,
)
from tests.test_mamari_i_leftover_090_700_430_076_006_i_only_scoreboard import (
    GRAM4_090 as CYCLE154_GRAM4_090,
    GRAM4_700 as CYCLE154_GRAM4_700,
    STANDING_I_LEFTOVER_090_700_430_076_006_BOTH_I_ONLY as CYCLE154_CLAIM,
    TestMamariILeftover090700430076006IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_999_090_076_070_remaining_5grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_999_090_076_070_REMAINING_5GRAMS_I_ONLY as CYCLE221_I_ONLY,
    STANDING_N_SEQUENCES as CYCLE221_N_SEQUENCES,
    TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_600_prev4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_PREVIOUS_4GRAMS_ALL_I_ONLY as CYCLE309_CLAIM,
    STANDING_N_HAPAX_I_ONLY as CYCLE309_N_HAPAX,
    STANDING_N_I_ONLY as CYCLE309_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE309_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE309_SEQUENCES,
    TestMamariILeftoverN4Remaining090076RemainingAfter600Prev4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_exactly2_430_076_scoreboard import (
    GRAM2 as CYCLE329_GRAM2,
    STANDING_G as CYCLE329_G,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_EXACTLY_2_SHARE_430_076 as CYCLE329_CLAIM,
    STANDING_K as CYCLE329_K,
    STANDING_MATCHING_LEFTOVERS as CYCLE329_MATCHING,
    STANDING_N as CYCLE329_N,
    STANDING_N_REMAINING as CYCLE329_N_REMAINING,
    STANDING_WITH_ROWS as CYCLE329_WITH_ROWS,
    TestMamariILeftoverN4RemainingAfter090076Exactly2430076Scoreboard,
    i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076,
    leftover_remaining_after_090_076_matching_set,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_next_2gram_scoreboard import (
    STANDING_G as CYCLE328_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE328_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_UNIQUE_MAX_2GRAM as CYCLE328_UNIQUE_MAX_CLAIM,
    STANDING_K as CYCLE328_K,
    TestMamariILeftoverN4RemainingAfter090076Next2gramScoreboard,
    i_leftover_n4_remaining_after_090_076_unique_max_2gram,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
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
from tests.test_mamari_small_santiago_gv_430_076_200_ngram_scoreboard import (
    GRAM_430_076,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

HYPOTHESIS_ALL_I_ONLY = True
GRAM2 = CYCLE329_GRAM2
GRAM4_001 = ("430", "076", "001", "076")
GRAM4_049 = ("430", "076", "049", "400")
STANDING_SEQUENCES = (GRAM4_001, GRAM4_049)
STANDING_N = 2
STANDING_N4 = 4
STANDING_N2 = 2
NEAR_MISS_090_076 = CYCLE223_GRAM2
NEAR_MISS_090_076_020 = CYCLE290_GRAM3
NEAR_MISS_090_076_020_010 = CYCLE291_SEQUENCES[0]
NEAR_MISS_090_076_070_000 = CYCLE219_LEAK_4GRAM
NEAR_MISS_076_071 = CYCLE171_GRAM2
NEAR_MISS_430_076_006_000_076 = MAXIMAL_N5_430
NEAR_MISS_090_430_076_006 = CYCLE154_GRAM4_090
NEAR_MISS_700_430_076_006 = CYCLE154_GRAM4_700
NEAR_MISS_430_076_049 = ("430", "076", "049")
STANDING_G_LEFTOVER_PREFIX_SITE = ("Gv", "Gv7", 25)
STANDING_N_I_EACH = (2, 2)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_I_SITES = (
    ((SIDE_IA, "Ia10", 103), (SIDE_IA, "Ia13", 156)),
    ((SIDE_IA, "Ia13", 170), (SIDE_IA, "Ia14", 63)),
)
STANDING_LEFTOVER_MATCHING_SITES = (
    (SIDE_IA, "Ia10", 103),
    (SIDE_IA, "Ia13", 156),
    (SIDE_IA, "Ia13", 170),
    (SIDE_IA, "Ia14", 63),
)
STANDING_LEFTOVER_MATCHING_COUNT = 4
STANDING_LEFTOVER_MATCHING_4GRAMS = (
    GRAM4_001,
    GRAM4_001,
    GRAM4_049,
    GRAM4_049,
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0, 0)
STANDING_N_LEAK_EACH = STANDING_N_OFF_I_EACH
STANDING_OFF_I_SITES = ((), ())
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_TWO_ON_I = tuple(
    2 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (
    STANDING_HITS_BY_TABLET_TWO_ON_I,
    STANDING_HITS_BY_TABLET_TWO_ON_I,
)
STANDING_N_I_ONLY = 2
STANDING_N_NOT_I_ONLY = 0
STANDING_N_LEAKING = 0
STANDING_LEAKING_4GRAMS = ()
STANDING_N_EXTRA_EACH = (0, 0)
STANDING_EXTRA_I_SITES = ((), ())
STANDING_N_EXTRA = 0
STANDING_HAPAX_EACH = (False, False)
STANDING_N_HAPAX = 0
STANDING_N_NOT_HAPAX = 2
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_NOT_REQUIRED = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only"
)
STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_430_076_4GRAMS_ALL_I_ONLY = True
STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_430_076_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_n4_remaining_after_090_076_430_076_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE154 = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE222 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE290 = False
STANDING_SAME_AS_CYCLE291 = False
STANDING_SAME_AS_CYCLE309 = False
STANDING_SAME_AS_CYCLE328 = False
STANDING_SAME_AS_CYCLE329 = False
STANDING_SAME_AS_CYCLE330 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE291 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE309 = True
STANDING_2GRAM_LEAK_DOES_NOT_COUNT = True
STANDING_090_076_DOES_NOT_COUNT = True
STANDING_090_076_020_DOES_NOT_COUNT = True
STANDING_090_076_020_010_DOES_NOT_COUNT = True
STANDING_090_076_070_000_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_430_076_006_000_076_DOES_NOT_COUNT = True
STANDING_090_430_076_006_DOES_NOT_COUNT = True
STANDING_700_430_076_006_DOES_NOT_COUNT = True
STANDING_430_076_049_PREFIX_DOES_NOT_COUNT = True
STANDING_ALL_I_INSIDE_FAMILY_IS_NOT_THIS_CYCLE = True
STANDING_CYCLE330_DOES_NOT_COUNT = True
STANDING_CYCLE329_DOES_NOT_COUNT = True
STANDING_CYCLE328_DOES_NOT_COUNT = True
STANDING_CYCLE222_DOES_NOT_COUNT = True
STANDING_I_SITE_PEEL_288_327_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_PEELS_DO_NOT_COUNT = True
STANDING_CYCLES_220_221_DO_NOT_COUNT = True
STANDING_CYCLE223_DOES_NOT_COUNT = True


def leftover_matching_4gram_sites(
    with_rows: tuple = CYCLE329_WITH_ROWS,
) -> tuple[tuple[str, str, int], ...]:
    """I leftover remaining-after-090-076 sites of the two 4-grams."""
    return tuple(site for _gram, _n, _f, sites in with_rows for site in sites)


def leftover_matching_subset(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    i_sites: tuple[tuple[tuple[str, str, int], ...], ...] = STANDING_I_SITES,
) -> bool:
    """True iff leftover matching 4-gram sites equal the union of I sites."""
    measured = set(site for sites in i_sites for site in sites)
    return set(leftover_sites) == measured


def extra_i_sites_of_4gram(
    i_sites: tuple[tuple[str, str, int], ...],
    leftover_matching: tuple[tuple[str, str, int], ...],
) -> tuple[tuple[str, str, int], ...]:
    """I 4-gram sites outside leftover remaining-after-090-076 matching sites."""
    leftover_set = set(leftover_matching)
    return tuple(site for site in i_sites if site not in leftover_set)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def leaking_4grams(
    sequences: tuple[tuple[str, ...], ...],
    n_off_i: tuple[int, ...],
) -> tuple[tuple[str, ...], ...]:
    """Distinct leftover 4-grams with N_off_I>0."""
    return tuple(
        gram
        for gram, off in zip(sequences, n_off_i, strict=True)
        if off > 0
    )


def i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    sequences: tuple[tuple[str, ...], ...] = STANDING_SEQUENCES,
    expected_n: int = STANDING_N,
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] | None = None,
) -> bool:
    """True iff both leftover remaining-after-090-076 430 076 4-grams are I-only.

    Claim holds only if the leftover inventory still has exactly those
    two matching 4-grams and every one of them has N_I>=1 and
    N_off_I=0. Hapax is not assumed; N_I may be greater than 1.
    Nested cycle 330 2-gram leak does not make this claim lose.
    """
    if leftovers is None:
        leftovers = leftover_n4_rows()
    matching = leftover_remaining_after_090_076_matching_set(leftovers)
    return (
        matching == sequences
        and len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestILeftoverN4RemainingAfter0900764300764gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on leftover remaining-after-090-076 430 076 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 2-gram / prefixes are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES, (GRAM4_001, GRAM4_049))
        self.assertEqual(STANDING_SEQUENCES, CYCLE329_MATCHING)
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:2], GRAM2)
            self.assertEqual(len(gram), STANDING_N4)
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_001), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_049), 1)
        overlap = [["430", "076", "001", "076", "430", "076", "001", "076"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_001), 2)
        two_on_i = [list(GRAM4_001)] * 2
        self.assertEqual(ngram_hit_count(two_on_i, GRAM4_001), 2)
        gapped = [list(GRAM4_001[:2]) + ["000"] + list(GRAM4_001[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_001), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_001), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], GRAM4_001), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], GRAM4_049), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], GRAM4_001), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_020_010)], GRAM4_001), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_430_076_006)], GRAM4_001), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_430_076_006)], GRAM4_049), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_430_076_049)], GRAM4_049), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_430_076_006_000_076)], GRAM4_001), 0)
        self.assertEqual(ngram_hit_count([["076", "001", "076", "430"]], GRAM4_001), 0)
        self.assertTrue(STANDING_2GRAM_LEAK_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_430_076_006_DOES_NOT_COUNT)
        self.assertTrue(STANDING_700_430_076_006_DOES_NOT_COUNT)
        self.assertTrue(STANDING_430_076_049_PREFIX_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when both leftover 4-grams are I-only."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                (2, 2), (0, 0), leftovers=leftover
            )
        )
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                (1, 1), (0, 0), leftovers=leftover
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                (2, 2), (1, 0), leftovers=leftover
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                (2, 2), (0, 1), leftovers=leftover
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                (0, 2), (0, 0), leftovers=leftover
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                (2, 0), (0, 0), leftovers=leftover
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                (2,), (0,), leftovers=leftover
            )
        )
        dropped = tuple(row for row in leftover if row[0] != GRAM4_001)
        self.assertFalse(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                (2, 2), (0, 0), leftovers=dropped
            )
        )
        self.assertTrue(sequence_is_i_only(2, 0))
        self.assertFalse(sequence_is_i_only(2, 1))
        self.assertFalse(sequence_is_i_only(0, 0))
        self.assertEqual(leaking_4grams(STANDING_SEQUENCES, (0, 0)), ())
        self.assertEqual(leaking_4grams(STANDING_SEQUENCES, (1, 0)), (GRAM4_001,))
        self.assertEqual(leaking_4grams(STANDING_SEQUENCES, (0, 2)), (GRAM4_049,))
        self.assertEqual(STANDING_CLAIM, (
            "i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only"
        ))
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_430_076_4GRAMS_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_430_076_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_equals_i_sites_and_extra_is_empty(self):
        """Leftover matching sites equal I sites; extra I of 4-grams is 0."""
        provider = MockProvider()
        self.assertTrue(
            leftover_matching_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(
            leftover_matching_4gram_sites(),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(CYCLE330_LEFTOVER_MATCHING_SITES, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(cycle330_leftover_matching_sites(), STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(
            extra_i_sites_of_4gram(STANDING_I_SITES[0], STANDING_LEFTOVER_MATCHING_SITES),
            (),
        )
        self.assertEqual(
            extra_i_sites_of_4gram(STANDING_I_SITES[1], STANDING_LEFTOVER_MATCHING_SITES),
            (),
        )
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(STANDING_N_EXTRA_EACH, (0, 0))
        planted_foreign = (SIDE_IA, "Ia99", 999)
        self.assertFalse(
            leftover_matching_subset(
                STANDING_LEFTOVER_MATCHING_SITES + (planted_foreign,),
                STANDING_I_SITES,
            )
        )
        self.assertEqual(
            extra_i_sites_of_4gram(
                STANDING_I_SITES[0] + (planted_foreign,),
                STANDING_LEFTOVER_MATCHING_SITES,
            ),
            (planted_foreign,),
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle329_matching_leftovers_not_the_2gram(self):
        """4-grams are cycle-329 matching leftovers, not 2-gram 430 076."""
        provider = MockProvider()
        self.assertEqual(GRAM2, CYCLE329_GRAM2)
        self.assertEqual(GRAM2, CYCLE329_G)
        self.assertEqual(GRAM2, CYCLE330_GRAM2)
        self.assertEqual(GRAM2, GRAM_430_076)
        self.assertNotEqual(GRAM4_001, GRAM2)
        self.assertNotEqual(GRAM4_049, GRAM2)
        self.assertNotEqual(GRAM4_001, NEAR_MISS_090_076_020_010)
        self.assertNotEqual(GRAM4_049, NEAR_MISS_090_430_076_006)
        self.assertNotEqual(GRAM4_049, NEAR_MISS_700_430_076_006)
        self.assertNotEqual(GRAM4_001, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM4_001, GRAM5))
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM4_001))
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM4_049))
        self.assertTrue(is_contiguous_substring(NEAR_MISS_430_076_049, GRAM4_049))
        self.assertFalse(is_contiguous_substring(GRAM4_049, NEAR_MISS_430_076_049))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE330)
        self.assertFalse(STANDING_SAME_AS_CYCLE329)
        self.assertFalse(STANDING_SAME_AS_CYCLE328)
        self.assertFalse(STANDING_SAME_AS_CYCLE291)
        self.assertFalse(STANDING_SAME_AS_CYCLE309)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE291)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE309)
        self.assertTrue(STANDING_CYCLE330_DOES_NOT_COUNT)
        self.assertTrue(STANDING_ALL_I_INSIDE_FAMILY_IS_NOT_THIS_CYCLE)
        self.assertEqual(len(GRAM4_001), STANDING_N4)
        self.assertLess(len(GRAM4_001), 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4RemainingAfter0900764300764gramsIOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture remaining-after-090-076 430 076 4-grams I-only. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.matching = leftover_remaining_after_090_076_matching_set(self.leftover)
        self.leftover_matching = leftover_matching_4gram_sites()
        self.by_tablet = load_vendored_by_tablet()
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in STANDING_SEQUENCES)
        self.ia_hits = tuple(
            ngram_hit_count(self.i_sides[SIDE_IA], gram) for gram in STANDING_SEQUENCES
        )
        self.i_hits = self.ia_hits
        self.extra = tuple(
            extra_i_sites_of_4gram(sites, self.leftover_matching)
            for sites in self.i_sites
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in STANDING_SEQUENCES
        )
        self.off_i_counts = tuple(
            tablet_hit_counts(self.by_tablet, gram, OFF_I_TABLETS)
            for gram in STANDING_SEQUENCES
        )
        self.off_i_hits = tuple(sum(counts) for counts in self.off_i_counts)
        self.off_i_sites = tuple(named_off_i_sites(gram) for gram in STANDING_SEQUENCES)
        self.claim_holds = i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
            self.i_hits,
            self.off_i_hits,
            leftovers=self.leftover,
        )

    def test_tokens_are_cycle_329_matching_leftovers_not_retuned(self):
        """4-grams are the cycle-329 leftover remaining matching pair."""
        self.assertEqual(self.matching, STANDING_SEQUENCES)
        self.assertEqual(self.matching, CYCLE329_MATCHING)
        self.assertEqual(GRAM2, CYCLE329_GRAM2)
        self.assertEqual(GRAM2, ("430", "076"))
        prior_329 = self.survey["i_leftover_n4_remaining_after_090_076_exactly2_430_076"]
        self.assertEqual(prior_329["cycle"], 329)
        self.assertEqual(tuple(prior_329["tokens2"]), GRAM2)
        self.assertEqual(tuple(prior_329["G"]), CYCLE329_G)
        self.assertEqual(prior_329["K"], CYCLE329_K)
        self.assertEqual(prior_329["K"], 2)
        self.assertEqual(prior_329["N"], CYCLE329_N)
        self.assertEqual(prior_329["N"], 11)
        self.assertEqual(prior_329["N_remaining"], CYCLE329_N_REMAINING)
        self.assertEqual(prior_329["N_remaining"], 9)
        measured_matching = [list(gram) for gram in CYCLE329_MATCHING]
        self.assertEqual(prior_329["matching_leftovers"], measured_matching)
        self.assertTrue(prior_329["i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076"])
        self.assertTrue(prior_329["i_vs_off_i_is_not_this_cycle"])
        self.assertNotIn("N_I", prior_329)
        self.assertNotIn("N_off_I", prior_329)
        prior_330 = self.survey["i_2gram_430_076_i_only"]
        self.assertEqual(prior_330["cycle"], 330)
        self.assertFalse(prior_330["i_2gram_430_076_i_only"])
        self.assertEqual(prior_330["N_I"], 30)
        self.assertEqual(prior_330["N_off_I"], 16)
        self.assertEqual(prior_330["N_extra"], 26)
        self.assertTrue(prior_330["leftover_4gram_i_only_is_not_this_cycle"])
        self.assertNotEqual(GRAM4_001, GRAM5)
        self.assertNotEqual(GRAM4_049, CYCLE223_GRAM2)
        self.assertFalse(is_contiguous_substring(GRAM4_001, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_CYCLE329_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE330_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_two_on_i_zero_off_i_not_hapax_and_claim_holds(self):
        """Each leftover 4-gram is 2/0 not hapax. Extra I of 4-grams is 0. HOLD."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.matching, STANDING_SEQUENCES)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.ia_hits, STANDING_N_I_EACH)
        self.assertEqual(self.i_hits, STANDING_N_I_EACH)
        self.assertEqual(self.off_i_hits, STANDING_N_OFF_I_EACH)
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, (STANDING_OFF_I_BY_TABLET,) * STANDING_N)
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 4)
        self.assertTrue(leftover_matching_subset(self.leftover_matching, self.i_sites))
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(sum(len(sites) for sites in self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(STANDING_HAPAX_EACH, (False, False))
        self.assertEqual(STANDING_N_NOT_HAPAX, 2)
        self.assertEqual(STANDING_N_HAPAX, 0)
        self.assertTrue(STANDING_HAPAX_NOT_REQUIRED)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        for gram, sites, n_on, n_off, extra, hapax, hits in zip(
            STANDING_SEQUENCES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_EXTRA_I_SITES,
            STANDING_HAPAX_EACH,
            STANDING_HITS_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), n_on)
            self.assertEqual(n_on, 2)
            self.assertEqual(n_off, 0)
            self.assertEqual(extra, ())
            self.assertFalse(hapax)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertEqual(hits, STANDING_HITS_BY_TABLET_TWO_ON_I)
            for tablet, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                if tablet == "I":
                    self.assertEqual(count, 2)
                else:
                    self.assertEqual(count, 0)
            for side, line, index in sites:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N4]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
                self.assertNotEqual(line[:2], "Ib")
                self.assertIn((side, line, index), STANDING_LEFTOVER_MATCHING_SITES)
        for site, leftover4 in zip(
            STANDING_LEFTOVER_MATCHING_SITES,
            STANDING_LEFTOVER_MATCHING_4GRAMS,
            strict=True,
        ):
            side, line, index = site
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), leftover4)
            self.assertIn(site, CYCLE330_LEFTOVER_MATCHING_SITES)
            self.assertNotIn(site, CYCLE330_EXTRA_I_SITES)
        self.assertEqual(named_off_i_sites(GRAM4_001), ())
        self.assertEqual(named_off_i_sites(GRAM4_049), ())
        self.assertEqual(leaking_4grams(STANDING_SEQUENCES, self.off_i_hits), ())
        self.assertEqual(STANDING_N_I_ONLY, 2)
        self.assertEqual(STANDING_N_NOT_I_ONLY, 0)
        self.assertEqual(STANDING_N_LEAKING, 0)
        self.assertEqual(STANDING_LEAKING_4GRAMS, ())
        self.assertEqual(
            i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only(
                self.i_hits,
                self.off_i_hits,
                leftovers=self.leftover,
            ),
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_430_076_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_430_076_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(STANDING_CLAIM, (
            "i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only"
        ))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_cycle330_2gram_still_leaks_and_is_not_relocked(self):
        """2-gram 430 076 still 30/16 including T; 4-grams do not inherit the leak."""
        self.assertFalse(CYCLE330_CLAIM)
        self.assertFalse(i_2gram_430_076_i_only(CYCLE330_N_I, CYCLE330_N_OFF_I))
        self.assertEqual(CYCLE330_N_I, 30)
        self.assertEqual(CYCLE330_N_OFF_I, 16)
        self.assertEqual(CYCLE330_N_EXTRA, 26)
        self.assertEqual(CYCLE330_LEFTOVER_MATCHING_COUNT, 4)
        self.assertEqual(CYCLE330_N_T, 2)
        self.assertEqual(CYCLE330_T_SITES, ((SIDE_TA, "Ta4", 19), (SIDE_TA, "Ta8", 2)))
        for site in CYCLE330_T_SITES:
            self.assertIn(site, CYCLE330_OFF_I_SITES)
        self.assertEqual(len(CYCLE330_OFF_I_SITES), 16)
        self.assertEqual(len(CYCLE330_EXTRA_I_SITES), 26)
        for sites in STANDING_I_SITES:
            for site in sites:
                self.assertIn(site, CYCLE330_LEFTOVER_MATCHING_SITES)
                self.assertNotIn(site, CYCLE330_EXTRA_I_SITES)
        self.assertTrue(STANDING_2GRAM_LEAK_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE330_DOES_NOT_COUNT)
        self.assertTrue(STANDING_ALL_I_INSIDE_FAMILY_IS_NOT_THIS_CYCLE)
        self.assertNotEqual(CYCLE330_N_EXTRA, 0)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_330_329_328_291_309_223_222_and_220_scoreboards_still_compute(self):
        """Cycle 330 30/16, 329 K=2, 328 unique-max lose, 291 4/0, 309 hapax 6/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, CYCLE223_GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        self.assertTrue(CYCLE222_CLAIM)
        prior_330 = TestMamariI2gram430076IOnlyScoreboard()
        prior_330.setUp()
        prior_330.test_2gram_is_sixteen_off_i_and_not_i_only()
        prior_330.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE330_N_I, 30)
        self.assertEqual(CYCLE330_N_OFF_I, 16)
        self.assertEqual(CYCLE330_N_EXTRA, 26)
        self.assertFalse(CYCLE330_CLAIM)
        self.assertFalse(i_2gram_430_076_i_only(30, 16))
        if prior_330.claim_holds:
            self.fail("nested cycle 330 2-gram 430 076 I-only 30/16 drifted")
        prior_329 = TestMamariILeftoverN4RemainingAfter090076Exactly2430076Scoreboard()
        prior_329.setUp()
        prior_329.test_remaining_after_11_exactly_2_share_430_076_holds()
        prior_329.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE329_K, 2)
        self.assertEqual(CYCLE329_G, GRAM2)
        self.assertTrue(CYCLE329_CLAIM)
        self.assertTrue(i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076(leftover))
        if not prior_329.claim_holds:
            self.fail("nested cycle 329 leftover remaining-after-090-076 exactly-2-share-430 076 drifted")
        prior_328 = TestMamariILeftoverN4RemainingAfter090076Next2gramScoreboard()
        prior_328.setUp()
        prior_328.test_remaining_after_11_unique_max_loses()
        prior_328.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE328_K, 2)
        self.assertEqual(CYCLE328_G, GRAM2)
        self.assertFalse(CYCLE328_UNIQUE)
        self.assertFalse(CYCLE328_UNIQUE_MAX_CLAIM)
        self.assertFalse(i_leftover_n4_remaining_after_090_076_unique_max_2gram(leftover))
        if prior_328.claim_holds:
            self.fail("nested cycle 328 remaining-after-090-076 unique-max drifted")
        prior_291 = TestMamariI090076020Forward4gramsIOnlyScoreboard()
        prior_291.setUp()
        prior_291.test_each_4gram_is_four_on_i_zero_off_i_and_claim_holds()
        prior_291.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE291_SEQUENCES, (("090", "076", "020", "010"),))
        self.assertEqual(CYCLE291_N_I_EACH, (4,))
        self.assertEqual(CYCLE291_N_OFF_I_EACH, (0,))
        self.assertEqual(CYCLE291_HAPAX_EACH, (False,))
        self.assertEqual(CYCLE291_N_NOT_HAPAX, 1)
        self.assertEqual(CYCLE291_N_I_ONLY, 1)
        self.assertEqual(CYCLE291_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE291_CLAIM)
        if not prior_291.claim_holds:
            self.fail("nested cycle 291 leftover n=4 remaining 090 076 020 forward 4-grams 4/0 drifted")
        prior_309 = TestMamariILeftoverN4Remaining090076RemainingAfter600Prev4IOnlyScoreboard()
        prior_309.setUp()
        prior_309.test_each_4gram_is_one_on_i_zero_off_i_no_line_initial_and_claim_holds()
        prior_309.test_survey_matches_computed_lock()
        self.assertEqual(len(CYCLE309_SEQUENCES), 6)
        self.assertEqual(CYCLE309_N_I_ONLY, 6)
        self.assertEqual(CYCLE309_N_HAPAX, 6)
        self.assertEqual(CYCLE309_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE309_CLAIM)
        if not prior_309.claim_holds:
            self.fail("nested cycle 309 leftover n=4 remaining remaining-after-600 prev4 hapax 6/0 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, CYCLE223_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, CYCLE223_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, CYCLE223_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        self.assertFalse(CYCLE223_CLAIM)
        self.assertFalse(i_2gram_090_076_i_only(69, 3))
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
        prior_290 = TestMamariI3gram090076020IOnlyScoreboard()
        prior_290.setUp()
        prior_290.test_3gram_is_zero_off_i_and_i_only()
        prior_290.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE290_N_I, 4)
        self.assertEqual(CYCLE290_N_OFF_I, 0)
        self.assertEqual(CYCLE290_N_EXTRA, 0)
        self.assertTrue(CYCLE290_CLAIM)
        if CYCLE290_N_I != 4 or CYCLE290_N_OFF_I != 0 or CYCLE290_N_EXTRA != 0:
            self.fail("nested cycle 290 leftover n=4 remaining 090 076 020 I-only 4/0 drifted")
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        prior_154 = TestMamariILeftover090700430076006IOnlyScoreboard()
        prior_154.setUp()
        prior_154.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_154.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE154_CLAIM)
        self.assertNotEqual(NEAR_MISS_090_430_076_006, GRAM4_001)
        self.assertNotEqual(NEAR_MISS_700_430_076_006, GRAM4_049)
        prior_221 = TestMamariILeftover999090076070Remaining5gramsIOnlyScoreboard()
        prior_221.setUp()
        prior_221.test_each_5gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_221.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE221_N_SEQUENCES, 4)
        self.assertTrue(CYCLE221_I_ONLY)
        if not prior_221.claim_holds:
            self.fail("nested cycle 221 remaining 5-grams 4/4 I-only drifted")
        prior_220 = TestMamariI5gram999090076070000IOnlyScoreboard()
        prior_220.setUp()
        prior_220.test_5gram_is_zero_off_i_and_i_only()
        prior_220.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE220_N_I, 1)
        self.assertEqual(CYCLE220_N_OFF_I, 0)
        self.assertTrue(CYCLE220_I_ONLY)
        if CYCLE220_N_I != 1 or CYCLE220_N_OFF_I != 0:
            self.fail("nested cycle 220 leftover 000 5-gram 1/0 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_CYCLE328_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE222_DOES_NOT_COUNT)
        self.assertTrue(STANDING_I_SITE_PEEL_288_327_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_DO_NOT_COUNT)
        self.assertTrue(STANDING_CYCLES_220_221_DO_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE223_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-331 leftover 4-gram I-only hold."""
        lock = self.survey["i_leftover_n4_remaining_after_090_076_430_076_4grams_i_only"]
        self.assertEqual(lock["cycle"], 331)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N"], STANDING_N)
        self.assertEqual(lock["N"], 2)
        self.assertEqual(lock["N_sequences"], STANDING_N)
        measured_sequences = [list(gram) for gram in STANDING_SEQUENCES]
        self.assertEqual(lock["tokens4"], measured_sequences)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(lock["leftover_matching_count"], 4)
        self.assertTrue(lock["leftover_matching_equals_i_sites"])
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 0)
        self.assertTrue(lock["not_assumed_hapax"])
        self.assertTrue(lock["hapax_not_required"])
        self.assertEqual(lock["N_not_hapax"], STANDING_N_NOT_HAPAX)
        self.assertEqual(lock["N_not_hapax"], 2)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 0)
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N)
        for row, gram, sites, n_on, n_off, extra, hapax, hits in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_EXTRA_I_SITES,
            STANDING_HAPAX_EACH,
            STANDING_HITS_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["leftover_matching_sites"]),
                sites,
            )
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_I"], 2)
            self.assertEqual(row["ia_hits"], 2)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["ib_sites"]), STANDING_IB_SITES)
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["N_leak"], 0)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["off_i_sites"]), ())
            self.assertEqual(tuple(tuple(site_row) for site_row in row["extra_i_sites"]), extra)
            self.assertEqual(row["N_extra"], 0)
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["off_i_tablets_with_hits"]), ())
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(tuple(row["hits_by_tablet"]), hits)
            self.assertTrue(row["i_only"])
            self.assertEqual(row["hapax"], hapax)
            self.assertFalse(row["hapax"])
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(lock["N_leaking"], 0)
        self.assertEqual(lock["N_leak"], 0)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only"])
        self.assertEqual(
            lock["i_leftover_n4_remaining_after_090_076_430_076_4grams_all_i_only"],
            STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_430_076_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(lock["i_leftover_n4_remaining_after_090_076_430_076_4grams_i_only"])
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_i_only"], 2)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle330_N_I"], 30)
        self.assertEqual(lock["nested_cycle330_N_off_I"], 16)
        self.assertEqual(lock["nested_cycle330_N_extra"], 26)
        self.assertEqual(lock["nested_cycle330_leftover_matching_count"], 4)
        self.assertFalse(lock["nested_cycle330_i_2gram_430_076_i_only"])
        self.assertEqual(lock["nested_cycle329_K"], 2)
        self.assertEqual(lock["nested_cycle329_N"], 11)
        self.assertEqual(lock["nested_cycle329_N_remaining"], 9)
        self.assertTrue(lock["nested_cycle329_exactly_2_share_430_076"])
        self.assertFalse(lock["nested_cycle328_unique_max"])
        self.assertEqual(lock["nested_cycle328_K"], 2)
        self.assertEqual(lock["nested_cycle291_N_i_only"], 1)
        self.assertEqual(lock["nested_cycle291_N_not_hapax"], 1)
        self.assertEqual(lock["nested_cycle309_N_i_only"], 6)
        self.assertEqual(lock["nested_cycle309_N_hapax_i_only"], 6)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle222_K"], 5)
        self.assertEqual(lock["nested_cycle222_N_remaining"], 16)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle154"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle222"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle290"])
        self.assertFalse(lock["same_as_cycle291"])
        self.assertFalse(lock["same_as_cycle309"])
        self.assertFalse(lock["same_as_cycle328"])
        self.assertFalse(lock["same_as_cycle329"])
        self.assertFalse(lock["same_as_cycle330"])
        self.assertTrue(lock["same_claim_shape_as_cycle291"])
        self.assertTrue(lock["same_claim_shape_as_cycle309"])
        self.assertTrue(lock["2gram_leak_does_not_count"])
        self.assertTrue(lock["090_076_does_not_count"])
        self.assertTrue(lock["090_076_020_does_not_count"])
        self.assertTrue(lock["090_076_020_010_does_not_count"])
        self.assertTrue(lock["090_076_070_000_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["430_076_006_000_076_does_not_count"])
        self.assertTrue(lock["090_430_076_006_does_not_count"])
        self.assertTrue(lock["700_430_076_006_does_not_count"])
        self.assertTrue(lock["430_076_049_prefix_does_not_count"])
        self.assertTrue(lock["all_i_inside_family_is_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["do_not_relock_cycle330"])
        self.assertTrue(lock["do_not_relock_cycle329"])
        self.assertTrue(lock["do_not_relock_cycle328"])
        self.assertTrue(lock["do_not_relock_cycle222"])
        self.assertTrue(lock["do_not_relock_cycles_288_327"])
        self.assertTrue(lock["do_not_relock_leftover_extra_peels"])
        self.assertTrue(lock["do_not_relock_cycles_220_221"])
        self.assertTrue(lock["do_not_relock_cycle223"])
        self.assertTrue(lock["standing_i_2gram_430_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_after_090_076_exactly2_430_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_after_090_076_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_090_076_020_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_600_prev4_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_020_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_999_090_076_070_remaining_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_5gram_999_090_076_070_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        prior_330 = self.survey["i_2gram_430_076_i_only"]
        self.assertEqual(prior_330["cycle"], 330)
        self.assertFalse(prior_330["i_2gram_430_076_i_only"])
        self.assertEqual(prior_330["N_I"], CYCLE330_N_I)
        self.assertEqual(prior_330["N_off_I"], CYCLE330_N_OFF_I)
        self.assertEqual(prior_330["N_I"], 30)
        self.assertEqual(prior_330["N_off_I"], 16)
        self.assertEqual(prior_330["N_extra"], 26)
        self.assertTrue(prior_330["leftover_4gram_i_only_is_not_this_cycle"])
        prior_329 = self.survey["i_leftover_n4_remaining_after_090_076_exactly2_430_076"]
        self.assertEqual(prior_329["cycle"], 329)
        self.assertTrue(prior_329["i_leftover_n4_remaining_after_090_076_exactly_2_share_430_076"])
        self.assertEqual(tuple(prior_329["G"]), ("430", "076"))
        self.assertEqual(prior_329["K"], 2)
        self.assertEqual(prior_329["N"], 11)
        self.assertTrue(prior_329["i_vs_off_i_is_not_this_cycle"])
        prior_328 = self.survey["i_leftover_n4_remaining_after_090_076_next_2gram"]
        self.assertEqual(prior_328["cycle"], 328)
        self.assertFalse(prior_328["i_leftover_n4_remaining_after_090_076_unique_max_2gram"])
        self.assertFalse(prior_328["unique_max"])
        self.assertEqual(prior_328["K"], 2)
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertEqual(tuple(prior_222["G"]), ("090", "076"))
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(prior_222["N_remaining"], 16)
        self.assertEqual(self.survey["i_090_076_020_forward_4grams_i_only"]["cycle"], 291)
        self.assertTrue(
            self.survey["i_090_076_020_forward_4grams_i_only"][
                "i_090_076_020_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_020_forward_4grams_i_only"]["N_i_only"], 1)
        self.assertEqual(self.survey["i_090_076_020_forward_4grams_i_only"]["N_not_hapax"], 1)
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_600_prev4_i_only"]["cycle"],
            309,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_600_prev4_i_only"][
                "i_leftover_n4_remaining_090_076_remaining_after_600_previous_4grams_all_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_600_prev4_i_only"]["N_i_only"],
            6,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], CYCLE223_N_I)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], CYCLE223_N_OFF_I)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["cycle"], 290)
        self.assertTrue(self.survey["i_3gram_090_076_020_i_only"]["i_3gram_090_076_020_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["N_I"], 4)
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_999_090_076_070_remaining_5grams_i_only"]["cycle"], 221)
        self.assertTrue(
            self.survey["i_leftover_999_090_076_070_remaining_5grams_i_only"][
                "i_leftover_999_090_076_070_remaining_5grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_5gram_999_090_076_070_000_i_only"]["cycle"], 220)
        self.assertTrue(self.survey["i_5gram_999_090_076_070_000_i_only"]["i_5gram_999_090_076_070_000_i_only"])
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


class TestMamariILeftoverN4RemainingAfter0900764300764gramsIOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 331 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
