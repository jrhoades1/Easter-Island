"""I's cycle-290 leftover n=4 remaining 090 076 020 forward-4-grams off-I lock.

Cycle 291 text-search lock. Uses already-vendored A–V and the
cycle-290 I sites of 3-gram 090 076 020 (all 4 I sites; each
has a next stem). Those 4 equal the cycle-289 leftover n=4
remaining I 090 076 exactly 4 share next 020 cluster (every
next 4-gram 090 076 020 010). Does not retune those 4-grams,
the 4 I sites, leftover n=4 remaining 020 (cycle 289), leftover
n=4 remaining share-one-forward-stem (cycle 288 lost), leftover
n=4 remaining sites, the leftover n=4 set, leftover extra
peels (225–287), or the already-closed leftover remaining
family. Does not vendor a new tablet. Does not scrape X. W has
no Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not
redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 237 (I 090 076 700 forward 4-grams
all I-only HOLDS 2/2 hapax 1/0), `020` instead of `700`.
Hapax is not required for the claim (cycle 237's two 4-grams
happened to be hapax). Cycle 263 I 999 090 076 previous
4-grams all I-only hapax LOST (14/0, N_not_hapax=2) is a
different lose condition; this cycle matches 237 (I-only),
not 263 (hapax). Cycle 219 I 090 076 070 forward 4-grams all
I-only lost 7/8; 090 076 070 000 leaks 1/1 on T — the lose
path analog. Cycle 290 I 090 076 020 I-only holds 4/0 extra
I=0, cycle 289 leftover n=4 remaining K=4 / G=020 all
090 076 020 010, cycle 288 unique-max G=020 K=4, cycle 223
69/3, and cycle 207 8/1 stay. Off-I T sites of 090 076 are
not this 3-gram and are not this 4-gram. Leftover n=4
remaining remaining-after-020 next stems are not locked this
cycle. Previous 4-grams of the four I sites are not locked
this cycle. Do not overwrite cycle 167/268–290. Do not
retune leftover n=4, leftover extra peels, 076-cells, or any
detector. 090 076 700, 090 076 070, leftover 076 020 010,
and 090 076 without 020 do not count.

Locks exact consecutive hits of each distinct continuing I
090 076 020 forward 4-gram on tablet I and on every other
vendored tablet A–H and J–V. Cycle 289 inventory (measure,
do not retune): all 4 I 090 076 020 sites continue 010, so
the continuing 4-gram is expected to be one distinct
090 076 020 010 with N_I=4. If a site is line-final after
020 (3-gram with no 4th token), lock that as no next 4-gram
rather than inventing one. Measured: all 4 sites have next
010; N_no_forward=0; one distinct 4-gram 090 076 020 010
with N_I=4, N_off_I=0, hapax false; Ib unpublished 0; no
off-I tablets. Shared 4th token 010 / N_I=4 does not make
the claim lose. Hapax / N_I>1 does not make the claim lose.
Claim that can lose: i_090_076_020_forward_4grams_all_i_only.
True iff every continuing I 090 076 020 forward 4-gram has
N_I ≥ 1 and N_off_I = 0 (and every I site that has a 4th
token is covered). This can lose if any 4-gram leaks off I
(same shape as cycle 219 090 076 070 000 1/1 on T). Given
2-gram 090 076 already leaks on T, this is a real lose path.
The claim is true. Do not assume the I-only result; measure.
Do not retune.

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
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_I_ONLY,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_N_OFF_I_EACH as CYCLE219_N_OFF_I_EACH,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
    TestMamariI090076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_700_forward_4grams_i_only_scoreboard import (
    STANDING_HAPAX_EACH as CYCLE237_HAPAX_EACH,
    STANDING_I_090_076_700_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE237_I_ONLY,
    STANDING_N_I_ONLY as CYCLE237_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE237_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE237_SEQUENCES,
    TestMamariI090076700Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_020010_COVERED,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_020_i_only_scoreboard import (
    GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE290_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_020_I_ONLY as CYCLE290_I_ONLY,
    STANDING_I_NEXT_4GRAMS as CYCLE290_NEXT_4GRAMS,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE290_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE290_I_SITES,
    STANDING_N_EXTRA as CYCLE290_N_EXTRA,
    STANDING_N_I as CYCLE290_N_I,
    STANDING_N_OFF_I as CYCLE290_N_OFF_I,
    extra_i_sites,
    leftover_extra_remaining_after_000_excludes_020,
    leftover_n4_remaining_020_subset,
    named_off_i_sites as cycle290_named_off_i_sites,
    TestMamariI3gram090076020IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_700_i_only_scoreboard import (
    GRAM3 as CYCLE236_GRAM3,
    STANDING_I_SITES as CYCLE236_I_SITES,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_020_scoreboard import (
    GRAM3_FORWARD,
    STANDING_G as CYCLE289_G,
    STANDING_IA12_82,
    STANDING_IA12_83,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020 as CYCLE289_CLAIM,
    STANDING_K as CYCLE289_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE289_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE289_MATCHING_SITES,
    STANDING_N_INSIDE as CYCLE289_N_INSIDE,
    STANDING_N_REMAINING_AFTER_020 as CYCLE289_N_REMAINING_AFTER_020,
    TestMamariILeftoverN4Remaining090076Forward020Scoreboard,
    leftover_n4_remaining_with_forward_020,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_SITES as CYCLE288_G_SITES,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE288_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE288_N_INSIDE,
    STANDING_N_WITH_NEXT as CYCLE288_N_WITH_NEXT,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
    leftover_n4_remaining_next_4grams,
    leftover_n4_remaining_next_stems,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_020_010_i_only_scoreboard import (
    GRAM3 as LEFTOVER_076_020_010,
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
STANDING_N_I = 4
STANDING_N_SEQUENCES = 1
STANDING_N_NO_FORWARD = 0
STANDING_CYCLE290_SITES = CYCLE290_I_SITES
STANDING_NO_FORWARD_SITES = ()
STANDING_CONTINUING_SITES = CYCLE290_I_SITES
STANDING_SEQUENCES = (("090", "076", "020", "010"),)
STANDING_PER_SITE_FORWARD_4GRAMS = CYCLE290_NEXT_4GRAMS
STANDING_NEXT_STEMS = ("010",)
STANDING_PER_SITE_NEXT_STEMS = ("010", "010", "010", "010")
STANDING_PREVIOUS_4GRAMS = CYCLE290_PREVIOUS_4GRAMS
STANDING_ROLES = ("forward",) * STANDING_N_SEQUENCES
STANDING_N_I_EACH = (4,)
STANDING_N_ON_I_EACH = (4,)
STANDING_I_SITES = (CYCLE290_I_SITES,)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,)
STANDING_OFF_I_SITES = ((),)
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = (
    tuple(4 if tablet == "I" else 0 for tablet in VENDORED_TABLETS),
)
STANDING_N_I_ONLY = 1
STANDING_N_NOT_I_ONLY = 0
STANDING_N_LEAKING = 0
STANDING_LEAKING_4GRAMS = ()
STANDING_N_EXTRA = 0
STANDING_EXTRA_I_SITES = CYCLE290_EXTRA_I_SITES
STANDING_LEFTOVER_MATCHING_SITES = CYCLE289_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS = CYCLE289_MATCHING_NEXT_4GRAMS
STANDING_SHARED_FOURTH_TOKEN = "010"
STANDING_SHARED_FOURTH_DOES_NOT_MAKE_CLAIM_LOSE = True
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_NOT_REQUIRED = True
STANDING_HAPAX_EACH = (False,)
STANDING_N_NOT_HAPAX = 1
STANDING_CLAIM = "i_090_076_020_forward_4grams_all_i_only"
STANDING_I_090_076_020_FORWARD_4GRAMS_ALL_I_ONLY = True
STANDING_I_090_076_020_FORWARD_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_090_076_020_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE237 = False
STANDING_SAME_AS_CYCLE263 = False
STANDING_SAME_AS_CYCLE288 = False
STANDING_SAME_AS_CYCLE289 = False
STANDING_SAME_AS_CYCLE290 = False
STANDING_SAME_AS_LEFTOVER_076_020_010 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE237 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE263 = False
STANDING_090_076_700_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_WITHOUT_020_DOES_NOT_COUNT = True
STANDING_076_020_010_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_090_076_070_000_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED = True
STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE290_N_I = 4
STANDING_CYCLE290_N_OFF_I = 0
STANDING_CYCLE290_N_EXTRA = 0
STANDING_CYCLE289_K = 4
STANDING_CYCLE289_G = "020"
STANDING_CYCLE288_K = 4
STANDING_CYCLE288_G = "020"
STANDING_CYCLE237_N_I_ONLY = 2
STANDING_CYCLE237_N_NOT_I_ONLY = 0


def forward_4gram_start_site(
    cycle290_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-290 I 090 076 020 site."""
    return cycle290_site


def site_forward_4gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """090 076 020 Y if a next stem exists; None at end-of-line."""
    n3 = len(gram3)
    if tuple(stems[index : index + n3]) != gram3:
        return None
    next_index = index + n3
    if next_index >= len(stems):
        return None
    return tuple(stems[index : index + n3 + 1])


def i_090_076_020_forward_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_CYCLE290_SITES,
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
    """I 090 076 020 sites that have no next stem after the 3-gram."""
    return tuple(
        site
        for site, gram in zip(sites, forwards, strict=True)
        if gram is None
    )


def i_sites_with_forward(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """I 090 076 020 sites that continue after the 3-gram."""
    return tuple(
        site
        for site, gram in zip(sites, forwards, strict=True)
        if gram is not None
    )


def distinct_continuing_forward_4grams(
    forwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, ...], ...]:
    """Distinct continuing forward 4-grams in first-seen order."""
    seen: set[tuple[str, ...]] = set()
    out: list[tuple[str, ...]] = []
    for gram in forwards:
        if gram is not None and gram not in seen:
            seen.add(gram)
            out.append(gram)
    return tuple(out)


def continuing_sites_covered(
    forwards: tuple[tuple[str, ...] | None, ...],
    sequences: tuple[tuple[str, ...], ...],
) -> bool:
    """True iff every I site that has a 4th token is in sequences."""
    seq_set = set(sequences)
    return all(gram is None or gram in seq_set for gram in forwards)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def leaking_4grams(
    sequences: tuple[tuple[str, ...], ...],
    n_off_i: tuple[int, ...],
) -> tuple[tuple[str, ...], ...]:
    """Distinct continuing 4-grams with N_off_I>0."""
    return tuple(
        gram
        for gram, off in zip(sequences, n_off_i, strict=True)
        if off > 0
    )


def i_090_076_020_forward_4grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    forwards: tuple[tuple[str, ...] | None, ...] = STANDING_PER_SITE_FORWARD_4GRAMS,
    sequences: tuple[tuple[str, ...], ...] = STANDING_SEQUENCES,
    expected_n: int = STANDING_N_SEQUENCES,
) -> bool:
    """True iff every continuing I 090 076 020 forward 4-gram is I-only
    and every I site that has a 4th token is covered.

    Claim holds only if every distinct continuing gram has
    N_off_I=0 and N_I>=1, length stays the distinct count, and
    no continuing site is left without its 4-gram. Hapax is
    not assumed; N_I may be greater than 1. Shared 4th token
    010 / N_I=4 does not make the claim lose.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and continuing_sites_covered(forwards, sequences)
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestI090076020Forward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-290 I 090 076 020 forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 700 / 070 / 076 020 010 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "020", "010"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_SEQUENCES)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_SEQUENCES)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:3], GRAM3)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["090", "076", "020", "010", "090", "076", "020", "010"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        four_on_i = [list(STANDING_SEQUENCES[0])] * 4
        self.assertEqual(ngram_hit_count(four_on_i, STANDING_SEQUENCES[0]), 4)
        gapped = [
            list(STANDING_SEQUENCES[0][:2])
            + ["000"]
            + list(STANDING_SEQUENCES[0][2:])
        ]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE207_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE236_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(LEFTOVER_076_020_010)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "020"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["076", "020", "010", "090"]], STANDING_SEQUENCES[0]), 0)
        planted = ["591", "090", "076", "020", "010", "090"]
        self.assertEqual(site_forward_4gram(planted, 1, GRAM3), STANDING_SEQUENCES[0])
        self.assertEqual(site_next_4gram(planted, 1, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_forward_3gram(planted, 1, GRAM2), GRAM3)
        self.assertIsNone(site_forward_4gram(["090", "076", "020"], 0, GRAM3))
        self.assertTrue(STANDING_090_076_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_020_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_020_010_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all distinct continuing 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        hold_forwards = STANDING_PER_SITE_FORWARD_4GRAMS
        self.assertTrue(
            i_090_076_020_forward_4grams_all_i_only(hold_ones, hold_zeros)
        )
        self.assertTrue(
            i_090_076_020_forward_4grams_all_i_only((1,), hold_zeros)
        )
        self.assertTrue(STANDING_SHARED_FOURTH_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertTrue(STANDING_HAPAX_NOT_REQUIRED)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(STANDING_HAPAX_EACH, (False,))
        self.assertEqual(STANDING_N_NOT_HAPAX, 1)
        lose_off = (1,)
        self.assertFalse(
            i_090_076_020_forward_4grams_all_i_only(hold_ones, lose_off)
        )
        self.assertFalse(
            i_090_076_020_forward_4grams_all_i_only((0,), hold_zeros)
        )
        self.assertFalse(i_090_076_020_forward_4grams_all_i_only((), ()))
        uncovered = hold_forwards[:-1] + (("090", "076", "020", "999"),)
        self.assertFalse(
            i_090_076_020_forward_4grams_all_i_only(
                hold_ones,
                hold_zeros,
                uncovered,
                STANDING_SEQUENCES,
            )
        )
        self.assertEqual(leaking_4grams(STANDING_SEQUENCES, hold_zeros), ())
        self.assertEqual(
            leaking_4grams(STANDING_SEQUENCES, lose_off),
            STANDING_SEQUENCES,
        )
        self.assertEqual(STANDING_CLAIM, "i_090_076_020_forward_4grams_all_i_only")
        self.assertTrue(STANDING_I_090_076_020_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_090_076_020_FORWARD_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_090_076_020_FORWARD_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_N_OFF_I_EACH[-1], 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertTrue(CYCLE237_I_ONLY)
        self.assertEqual(CYCLE237_N_I_ONLY, 2)
        self.assertEqual(CYCLE237_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE237_HAPAX_EACH)
        self.assertEqual(len(CYCLE237_SEQUENCES), 2)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_290_forwards_not_retuned(self):
        """4-grams stay the cycle-290 I forwards; leftover / 700 / 070 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "020"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(STANDING_SEQUENCES, (("090", "076", "020", "010"),))
        self.assertEqual(STANDING_CYCLE290_SITES, CYCLE290_I_SITES)
        self.assertEqual(STANDING_CYCLE290_SITES, CYCLE289_MATCHING_SITES)
        self.assertEqual(STANDING_PER_SITE_FORWARD_4GRAMS, CYCLE290_NEXT_4GRAMS)
        self.assertEqual(STANDING_PER_SITE_FORWARD_4GRAMS, CYCLE289_MATCHING_NEXT_4GRAMS)
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE290_N_I - 3)
        self.assertEqual(CYCLE290_N_I, 4)
        self.assertEqual(CYCLE290_N_OFF_I, 0)
        self.assertEqual(CYCLE290_N_EXTRA, 0)
        self.assertEqual(STANDING_SHARED_FOURTH_TOKEN, "010")
        self.assertEqual(len(set(STANDING_PER_SITE_NEXT_STEMS)), 1)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(CYCLE236_GRAM3, ("090", "076", "700"))
        self.assertEqual(CYCLE207_GRAM3, ("090", "076", "070"))
        self.assertEqual(LEFTOVER_076_020_010, ("076", "020", "010"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(CYCLE236_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE207_GRAM3, gram))
            self.assertTrue(is_contiguous_substring(LEFTOVER_076_020_010, gram))
            self.assertNotEqual(gram[:3], CYCLE236_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE207_GRAM3)
            self.assertNotEqual(gram[:3], LEFTOVER_076_020_010)
            self.assertEqual(gram[:2], GRAM2)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
        for site in STANDING_CYCLE290_SITES:
            self.assertEqual(forward_4gram_start_site(site), site)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE223)
        self.assertFalse(STANDING_SAME_AS_CYCLE237)
        self.assertFalse(STANDING_SAME_AS_CYCLE263)
        self.assertFalse(STANDING_SAME_AS_CYCLE288)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE290)
        self.assertFalse(STANDING_SAME_AS_LEFTOVER_076_020_010)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE237)
        self.assertFalse(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE263)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI090076020Forward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture I 090 076 020 forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle290_sites = STANDING_CYCLE290_SITES
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
            cycle290_named_off_i_sites(gram) for gram in self.grams
        )
        self.measured_forwards = i_090_076_020_forward_4grams(
            self.i_sides,
            self.cycle290_sites,
            GRAM3,
        )
        self.no_forward = i_sites_without_forward(
            self.cycle290_sites,
            self.measured_forwards,
        )
        self.continuing = i_sites_with_forward(
            self.cycle290_sites,
            self.measured_forwards,
        )
        self.distinct = distinct_continuing_forward_4grams(self.measured_forwards)
        self.next_stems = leftover_n4_remaining_next_stems(
            self.i_sides,
            CYCLE224_INSIDE_SITES,
            GRAM2,
        )
        self.leftover_matching = leftover_n4_remaining_with_forward_020(
            CYCLE224_INSIDE_SITES,
            self.next_stems,
        )
        self.leftover_matching_next_4grams = leftover_n4_remaining_next_4grams(
            self.i_sides,
            self.leftover_matching,
            GRAM2,
        )
        self.extra = extra_i_sites(self.cycle290_sites, self.leftover_matching)
        self.n3_i = ngram_hit_count(self.i_sides[SIDE_IA], GRAM3) + STANDING_IB_HITS
        self.n3_off_i = sum(tablet_hit_counts(self.by_tablet, GRAM3, OFF_I_TABLETS))
        self.claim_holds = i_090_076_020_forward_4grams_all_i_only(
            self.n_i,
            self.n_off_i,
            self.measured_forwards,
            self.distinct,
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = STANDING_N_SEQUENCES - self.n_i_only
        self.leaking = leaking_4grams(self.grams, self.n_off_i)

    def test_tokens_and_sites_are_cycle_290_forwards_not_retuned(self):
        """4-grams and I sites stay the cycle-290 forward lock. Nested 4/0 must hold."""
        self.assertEqual(GRAM3, ("090", "076", "020"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle290_sites, STANDING_CYCLE290_SITES)
        self.assertEqual(self.cycle290_sites, CYCLE290_I_SITES)
        self.assertEqual(self.cycle290_sites, CYCLE289_MATCHING_SITES)
        self.assertEqual(self.cycle290_sites, CYCLE288_G_SITES)
        self.assertEqual(self.cycle290_sites, STANDING_LEFTOVER_020010_COVERED)
        self.assertEqual(self.measured_forwards, STANDING_PER_SITE_FORWARD_4GRAMS)
        self.assertEqual(self.measured_forwards, CYCLE290_NEXT_4GRAMS)
        self.assertEqual(self.measured_forwards, CYCLE289_MATCHING_NEXT_4GRAMS)
        self.assertEqual(self.leftover_matching_next_4grams, STANDING_PER_SITE_FORWARD_4GRAMS)
        self.assertEqual(self.no_forward, STANDING_NO_FORWARD_SITES)
        self.assertEqual(self.continuing, STANDING_CONTINUING_SITES)
        self.assertEqual(self.distinct, STANDING_SEQUENCES)
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(len(self.no_forward), STANDING_N_NO_FORWARD)
        self.assertEqual(STANDING_N_NO_FORWARD, 0)
        self.assertEqual(len(self.grams), STANDING_N_SEQUENCES)
        self.assertEqual(STANDING_N_SEQUENCES, 1)
        self.assertEqual(self.n3_i, STANDING_CYCLE290_N_I)
        self.assertEqual(self.n3_i, 4)
        self.assertEqual(self.n3_off_i, STANDING_CYCLE290_N_OFF_I)
        self.assertEqual(self.n3_off_i, 0)
        self.assertEqual(self.leftover_matching, CYCLE289_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE290_I_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE289_K)
        self.assertEqual(STANDING_CYCLE289_K, 4)
        self.assertEqual(STANDING_CYCLE289_G, "020")
        self.assertEqual(CYCLE289_G, "020")
        self.assertEqual(CYCLE289_K, 4)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertTrue(
            leftover_n4_remaining_020_subset(
                self.leftover_matching,
                self.cycle290_sites,
            )
        )
        if self.n3_i != 4 or self.n3_off_i != 0 or self.extra:
            self.fail("nested cycle 290 090 076 020 I-only 4/0 extra I=0 drifted")
        if len(self.leftover_matching) != 4 or CYCLE289_G != "020":
            self.fail("nested cycle 289 leftover n=4 remaining G=020 K=4 drifted")
        for nxt4 in self.leftover_matching_next_4grams:
            if nxt4 != ("090", "076", "020", "010"):
                self.fail("nested cycle 289 matching next 4-grams drifted from 090 076 020 010")
        prior_290 = self.survey["i_3gram_090_076_020_i_only"]
        self.assertEqual(prior_290["cycle"], 290)
        self.assertEqual(prior_290["N_I"], CYCLE290_N_I)
        self.assertEqual(prior_290["N_I"], 4)
        self.assertEqual(prior_290["N_off_I"], CYCLE290_N_OFF_I)
        self.assertEqual(prior_290["N_off_I"], 0)
        self.assertEqual(prior_290["N_extra"], 0)
        self.assertTrue(prior_290["i_3gram_090_076_020_i_only"])
        self.assertTrue(CYCLE290_I_ONLY)
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_FORWARD_4GRAMS],
            prior_290["i_next_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_290["i_sites"]),
            STANDING_CYCLE290_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PREVIOUS_4GRAMS],
            prior_290["i_previous_4grams"],
        )
        prior_289 = self.survey["i_leftover_n4_remaining_090_076_forward_020"]
        self.assertEqual(prior_289["cycle"], 289)
        self.assertEqual(prior_289["G"], "020")
        self.assertEqual(prior_289["K"], 4)
        self.assertEqual(prior_289["N_inside"], 13)
        self.assertEqual(prior_289["N_remaining_after_020"], 9)
        self.assertTrue(prior_289["i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"])
        self.assertTrue(CYCLE289_CLAIM)
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_FORWARD_4GRAMS],
            prior_289["matching_next_4grams"],
        )
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["N_inside"], 13)
        self.assertEqual(prior_288["N_with_next"], 13)
        self.assertEqual(prior_288["N_distinct_next_stems"], 6)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertTrue(prior_288["g_uniquely_most_frequent"])
        self.assertFalse(prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        prior_237 = self.survey["i_090_076_700_forward_4grams_i_only"]
        self.assertEqual(prior_237["cycle"], 237)
        self.assertTrue(prior_237["i_090_076_700_forward_4grams_all_i_only"])
        self.assertEqual(prior_237["N_i_only"], 2)
        self.assertEqual(prior_237["N_not_i_only"], 0)
        self.assertTrue(CYCLE237_I_ONLY)
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
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_four_on_i_zero_off_i_and_claim_holds(self):
        """One distinct 4-gram is 4/0, not hapax. All I-only. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (4,))
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0,))
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(self.leaking, STANDING_LEAKING_4GRAMS)
        self.assertEqual(STANDING_N_LEAKING, 0)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(len(self.grams), STANDING_N_SEQUENCES)
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked 4/0")
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from the locked 4/0")
        if self.leaking:
            self.fail("a continuing 4-gram leaked off I")
        gram = STANDING_SEQUENCES[0]
        nxt = STANDING_NEXT_STEMS[0]
        sites = STANDING_I_SITES[0]
        self.assertEqual(gram, ("090", "076", "020", "010"))
        self.assertEqual(nxt, STANDING_SHARED_FOURTH_TOKEN)
        self.assertEqual(sites, STANDING_CYCLE290_SITES)
        self.assertEqual(len(sites), 4)
        for site, start, per_site, prev4, per_next in zip(
            STANDING_CYCLE290_SITES,
            STANDING_CONTINUING_SITES,
            STANDING_PER_SITE_FORWARD_4GRAMS,
            STANDING_PREVIOUS_4GRAMS,
            STANDING_PER_SITE_NEXT_STEMS,
            strict=True,
        ):
            self.assertEqual(forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), per_site)
            self.assertEqual(stems[start[2] + STANDING_N3], nxt)
            self.assertEqual(stems[start[2] + STANDING_N3], per_next)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N3]), GRAM3)
            self.assertEqual(tuple(stems[start[2] - 1 : start[2] + STANDING_N3]), prev4)
            self.assertEqual(site_forward_4gram(stems, start[2], GRAM3), gram)
            self.assertEqual(site_next_4gram(stems, start[2], GRAM2), gram)
            self.assertEqual(site_forward_3gram(stems, start[2], GRAM2), GRAM3)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram[:3], CYCLE236_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE207_GRAM3)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram[:3], LEFTOVER_076_020_010)
            self.assertIn(site, STANDING_CYCLE290_SITES)
            self.assertIn(site, CYCLE289_MATCHING_SITES)
            self.assertIn(site, CYCLE288_G_SITES)
            self.assertIn(site, STANDING_LEFTOVER_020010_COVERED)
            self.assertIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE236_I_SITES)
        self.assertEqual(
            STANDING_CYCLE290_SITES,
            (
                (SIDE_IA, "Ia2", 119),
                (SIDE_IA, "Ia4", 86),
                (SIDE_IA, "Ia5", 143),
                (SIDE_IA, "Ia12", 83),
            ),
        )
        self.assertIn(STANDING_IA12_83, STANDING_CYCLE290_SITES)
        self.assertEqual(STANDING_IA12_83, (SIDE_IA, "Ia12", 83))
        self.assertEqual(STANDING_IA12_82, (SIDE_IA, "Ia12", 82))
        self.assertTrue(sequence_is_i_only(4, 0))
        self.assertFalse(STANDING_HAPAX_EACH[0])
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_NOT_REQUIRED)
        self.assertTrue(STANDING_SHARED_FOURTH_DOES_NOT_MAKE_CLAIM_LOSE)
        if self.n_i_only != STANDING_N_I_ONLY:
            self.fail("measured N_i_only drifted from 1")
        if self.n_not_i_only != STANDING_N_NOT_I_ONLY:
            self.fail("measured N_not_i_only drifted from 0")
        if not self.claim_holds:
            self.fail("measured forward 4-grams are not all I-only")
        self.assertEqual(self.n_i_only, 1)
        self.assertEqual(self.n_not_i_only, 0)
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
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet[0], strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
            if tablet == "I":
                self.assertEqual(count, 4)
            else:
                self.assertEqual(count, 0)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM3), 0)
        for seq in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], seq), 0)
            self.assertEqual(cycle290_named_off_i_sites(seq), ())
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
            for seq in STANDING_SEQUENCES:
                self.assertNotEqual(tuple(stems[index : index + STANDING_N4]), seq)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        ta9 = t_sides[SIDE_TA][TA_LINE_NAMES.index("Ta9")]
        self.assertEqual(tuple(ta9[2:6]), CYCLE219_LEAK_4GRAM)
        self.assertNotEqual(tuple(ta9[2:6]), STANDING_SEQUENCES[0])
        self.assertEqual(
            i_090_076_020_forward_4grams_all_i_only(
                self.n_i,
                self.n_off_i,
                self.measured_forwards,
                self.distinct,
            ),
            STANDING_I_090_076_020_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_090_076_020_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_090_076_020_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_090_076_020_FORWARD_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_090_076_020_forward_4grams_all_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE223)
        self.assertFalse(STANDING_SAME_AS_CYCLE237)
        self.assertFalse(STANDING_SAME_AS_CYCLE263)
        self.assertFalse(STANDING_SAME_AS_CYCLE288)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE290)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE237)
        self.assertFalse(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE263)
        self.assertTrue(STANDING_090_076_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_020_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_020_010_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_290_289_288_237_223_and_219_still_compute(self):
        """Cycle 290 4/0 extra I=0, 289 K=4 all 010, 288 unique-max G=020 K=4, 237 2/2 hapax, 223 69/3, 219 T leak stay."""
        prior_290 = TestMamariI3gram090076020IOnlyScoreboard()
        prior_290.setUp()
        prior_290.test_i_hits_are_four_on_ia_and_equal_leftover_n4_remaining_020()
        prior_290.test_3gram_is_zero_off_i_and_i_only()
        prior_290.test_survey_matches_computed_lock()
        self.assertEqual(prior_290.i_hits, CYCLE290_N_I)
        self.assertEqual(prior_290.i_hits, 4)
        self.assertEqual(prior_290.off_i_hits, CYCLE290_N_OFF_I)
        self.assertEqual(prior_290.off_i_hits, 0)
        self.assertEqual(prior_290.i_sites, CYCLE290_I_SITES)
        self.assertEqual(prior_290.extra, ())
        self.assertTrue(prior_290.claim_holds)
        self.assertTrue(CYCLE290_I_ONLY)
        if prior_290.i_hits != 4 or prior_290.off_i_hits != 0 or prior_290.extra:
            self.fail("nested cycle 290 090 076 020 I-only 4/0 extra I=0 drifted")
        prior_289 = TestMamariILeftoverN4Remaining090076Forward020Scoreboard()
        prior_289.setUp()
        prior_289.test_counts_4_of_13_and_hypothesis_k_4_holds()
        prior_289.test_survey_matches_computed_lock()
        self.assertEqual(prior_289.k, 4)
        self.assertEqual(CYCLE289_G, "020")
        self.assertEqual(prior_289.n_inside, 13)
        self.assertEqual(prior_289.matching, CYCLE289_MATCHING_SITES)
        self.assertEqual(prior_289.matching_next_4grams, CYCLE289_MATCHING_NEXT_4GRAMS)
        for nxt4 in prior_289.matching_next_4grams:
            self.assertEqual(nxt4, ("090", "076", "020", "010"))
        self.assertTrue(prior_289.claim_holds)
        self.assertTrue(CYCLE289_CLAIM)
        if prior_289.k != 4 or CYCLE289_G != "020" or prior_289.n_inside != 13:
            self.fail("nested cycle 289 leftover n=4 remaining G=020 K=4 drifted")
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.n_inside, 13)
        self.assertEqual(prior_288.n_with_next, 13)
        self.assertEqual(prior_288.n_distinct, 6)
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_INSIDE, 13)
        self.assertEqual(CYCLE288_N_WITH_NEXT, 13)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        if (
            prior_288.n_inside != 13
            or prior_288.n_with_next != 13
            or prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or not prior_288.unique_max
        ):
            self.fail("nested cycle 288 leftover n=4 remaining unique-max G=020 K=4 drifted")
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
        self.assertTrue(CYCLE237_HAPAX_EACH)
        if prior_237.n_i_only != 2 or prior_237.n_not_i_only != 0:
            self.fail("nested cycle 237 090 076 700 forward 4-grams 2/2 hapax drifted")
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
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        prior_219.test_survey_matches_computed_lock()
        self.assertFalse(prior_219.claim_holds)
        self.assertFalse(CYCLE219_I_ONLY)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        if prior_219.n_i_only != 7 or prior_219.n_not_i_only != 1:
            self.fail("nested cycle 219 090 076 070 forward 4-grams T leak drifted")
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
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(leftover_extra_remaining_after_000_excludes_020())
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-291 I-forward-4 I-only hold."""
        lock = self.survey["i_090_076_020_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 291)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 4)
        self.assertEqual(lock["N_I"], CYCLE290_N_I)
        self.assertEqual(lock["N_sequences"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_sequences"], 1)
        self.assertEqual(lock["N_no_forward"], STANDING_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_CYCLE290_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_forward_sites"]),
            STANDING_NO_FORWARD_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["continuing_sites"]),
            STANDING_CONTINUING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_FORWARD_4GRAMS],
            lock["per_site_forward_4grams"],
        )
        self.assertEqual(tuple(lock["per_site_next_stems"]), STANDING_PER_SITE_NEXT_STEMS)
        self.assertEqual(tuple(lock["continuing_next_stems"]), STANDING_NEXT_STEMS)
        self.assertEqual(lock["shared_fourth_token"], STANDING_SHARED_FOURTH_TOKEN)
        self.assertEqual(lock["shared_fourth_token"], "010")
        self.assertTrue(lock["shared_fourth_does_not_make_claim_lose"])
        self.assertEqual(
            [list(gram) for gram in STANDING_PREVIOUS_4GRAMS],
            lock["i_previous_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_remaining_020_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS],
            lock["leftover_n4_remaining_020_next_4grams"],
        )
        self.assertEqual(lock["extra_i_sites"], [])
        self.assertEqual(lock["N_extra"], 0)
        self.assertTrue(lock["not_assumed_hapax"])
        self.assertTrue(lock["hapax_not_required"])
        self.assertEqual(lock["N_not_hapax"], STANDING_N_NOT_HAPAX)
        self.assertEqual(lock["N_not_hapax"], 1)
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_SEQUENCES)
        for row, gram, nxt, role, sites, n_on, n_off, off_sites, hits, hapax in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_OFF_I_SITES,
            STANDING_HITS_BY_TABLET,
            STANDING_HAPAX_EACH,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["cycle290_sites"]),
                sites,
            )
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["i_4gram_starts"]),
                sites,
            )
            self.assertEqual(row["next_stem"], nxt)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_I"], 4)
            self.assertEqual(row["ia_hits"], 4)
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
            self.assertEqual(row["hapax"], hapax)
            self.assertFalse(row["hapax"])
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(lock["N_leaking"], 0)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_090_076_020_forward_4grams_all_i_only"])
        self.assertEqual(
            lock["i_090_076_020_forward_4grams_all_i_only"],
            STANDING_I_090_076_020_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(lock["i_090_076_020_forward_4grams_i_only"])
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_i_only"], 1)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle290_N_I"], 4)
        self.assertEqual(lock["nested_cycle290_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle290_N_extra"], 0)
        self.assertEqual(lock["nested_cycle289_G"], STANDING_CYCLE289_G)
        self.assertEqual(lock["nested_cycle289_G"], "020")
        self.assertEqual(lock["nested_cycle289_K"], STANDING_CYCLE289_K)
        self.assertEqual(lock["nested_cycle289_K"], 4)
        self.assertEqual(lock["nested_cycle289_N_inside"], 13)
        self.assertEqual(lock["nested_cycle289_N_remaining_after_020"], 9)
        self.assertEqual(lock["nested_cycle288_N_inside"], 13)
        self.assertEqual(lock["nested_cycle288_N_with_next"], 13)
        self.assertEqual(lock["nested_cycle288_N_distinct_next_stems"], 6)
        self.assertEqual(lock["nested_cycle288_G"], STANDING_CYCLE288_G)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], STANDING_CYCLE288_K)
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle237_N_i_only"], STANDING_CYCLE237_N_I_ONLY)
        self.assertEqual(lock["nested_cycle237_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle237_N_not_i_only"], STANDING_CYCLE237_N_NOT_I_ONLY)
        self.assertEqual(lock["nested_cycle237_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle219_N_i_only"], 7)
        self.assertEqual(lock["nested_cycle219_N_not_i_only"], 1)
        self.assertEqual(tuple(lock["nested_cycle219_leak_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle237"])
        self.assertFalse(lock["same_as_cycle263"])
        self.assertFalse(lock["same_as_cycle288"])
        self.assertFalse(lock["same_as_cycle289"])
        self.assertFalse(lock["same_as_cycle290"])
        self.assertFalse(lock["same_as_leftover_076_020_010"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["same_claim_shape_as_cycle237"])
        self.assertFalse(lock["same_claim_shape_as_cycle263"])
        self.assertTrue(lock["090_076_700_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_without_020_does_not_count"])
        self.assertTrue(lock["076_020_010_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["090_076_070_000_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["leftover_n4_remaining_remaining_after_020_next_stems_not_locked"])
        self.assertTrue(lock["previous_4grams_are_not_this_cycle"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_090_076_020_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_020_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_700_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["cycle"], 290)
        self.assertTrue(self.survey["i_3gram_090_076_020_i_only"]["i_3gram_090_076_020_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["N_I"], 4)
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_020_i_only"]["N_extra"], 0)
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"]["cycle"],
            289,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"][
                "i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"]["G"],
            "020",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"]["K"],
            4,
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"], 288)
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"][
                "i_leftover_n4_remaining_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["G"], "020")
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["K"], 4)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["g_uniquely_most_frequent"]
        )
        self.assertEqual(self.survey["i_090_076_700_forward_4grams_i_only"]["cycle"], 237)
        self.assertTrue(
            self.survey["i_090_076_700_forward_4grams_i_only"][
                "i_090_076_700_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_700_forward_4grams_i_only"]["N_i_only"], 2)
        self.assertEqual(self.survey["i_090_076_700_forward_4grams_i_only"]["N_not_i_only"], 0)
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
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
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


class TestMamariI090076020Forward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 291 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
