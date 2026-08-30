"""I's cycle-256 leftover extra remaining-after-000 forward-4-grams off-I lock.

Cycle 257 text-search lock. Uses already-vendored A–V and the
cycle-256 leftover extra remaining-after-000 I sites of 2-gram
090 076 (the 19 leftover extra with-next sites whose next
token is none of 070, 071, 013, 001, 700, 530, 280, 087,
011, 005, or 000). Does not retune those 4-grams, leftover
extra remaining-after-000 unique-max (cycle 256 lost: 19
hapax, G=755 K=1), leftover extra remaining-after-005 G=000
K=2 N_remaining10=21, leftover extra remaining-after-001
unique-max (cycle 234 lost), leftover extra remaining 071,
leftover extra forward 070, leftover extra sites, leftover
n=4, or the already-closed leftover remaining family. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 217 (leftover 076 070 forward
4-grams all I-only hapax 1/0 x11) and cycle 255 (I 090 076
000 continuing forward 4-grams all I-only hapax 1/0 plus
Ia2[174] line-final). Cycle 256 leftover extra
remaining-after-000 unique-max lost N_remaining11=19 K=1
19-way tie G=755, cycle 255 1/0 + line-final, cycle 254
090 076 000 I-only 2/0 extra I=0, cycle 253 leftover extra
remaining-after-005 K=2 / G=000 N_remaining10=21, cycle 234
7-way tie at 2, cycle 223 69/3, and cycle 217 11/11 hapax
stay. Nested-check leftover extra remaining-after-000
unique-max false, N_remaining11==19, K==1, 19 distinct next
stems, G=755 (do not retune cycle 256). Nested-check each
remaining-after-000 site has a next token. If a site is
line-final after the next stem (3-gram 090 076 X with no
4th token), lock that as no next 4-gram rather than
inventing one; that site then does not count as a 4-gram
hapax. Measure; do not assume all 19 have a 4th token.
Do not peel a specific remaining-after-000 stem this cycle.
Do not lock previous 4-grams of 090 076 000. Off-I T sites
are this cycle only as off-I of a remaining-after-000
4-gram if they match. 090 076 000, 090 076 005, 090 076
011, 090 076 087, 090 076 280, 090 076 530, 090 076 700,
090 076 001, 090 076 013, 090 076 070, and 090 076 071 do
not count. Do not retune leftover n=4, 076-cells, or any
detector.

Locks exact consecutive hits of each continuing leftover
extra remaining-after-000 forward 4-gram on tablet I and on
every other vendored tablet A–H and J–V. The nineteen
4-grams: 090 076 012 076, 090 076 175 002, 090 076 755 509,
090 076 470 700, 090 076 430 076, 090 076 600 002,
090 076 384 570, 090 076 535 076, 090 076 050 050,
090 076 147 076, 090 076 090 076, 090 076 386 202,
090 076 505 633, 090 076 607 073, 090 076 057 240,
090 076 072 205, 090 076 300 000, 090 076 255 067,
090 076 670 700. Do not assume hapax; count each from
fixtures. Hypothesis: all continuing remaining-after-000
forward 4-grams are I-only. Measured: each N_I=1 at the
cycle-256 remaining-after-000 site; all N_off_I=0; no
remaining-after-000 site is line-final after its next stem
(all 19 have a 4th token). Ia2[174] is remaining-after-005
000 (line-final), not remaining-after-000. Claim that can
lose: i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only.
True iff every continuing remaining-after-000 forward
4-gram has N_I ≥ 1 and N_off_I = 0 (hapax 1/0 expected
given K=1). This can lose if any leaks off I (same shape
as cycle 219 090 076 070 000 1/1 on T). The claim is true.
Do not assume hapax; measure. Do not retune.

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
from tests.test_mamari_i_090_076_000_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE255_CLAIM,
    STANDING_N_I_ONLY as CYCLE255_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE255_N_NOT_I_ONLY,
    STANDING_IA2_174_LINE_FINAL as CYCLE255_IA2_174_LINE_FINAL,
    STANDING_SEQUENCES as CYCLE255_SEQUENCES,
    TestMamariI090076000Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_CLAIM,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
    TestMamariI090076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES as CYCLE223_I_SITES,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_000_i_only_scoreboard import (
    GRAM3 as CYCLE254_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE254_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_000_I_ONLY as CYCLE254_CLAIM,
    STANDING_I_SITES as CYCLE254_I_SITES,
    STANDING_N_EXTRA as CYCLE254_N_EXTRA,
    STANDING_N_I as CYCLE254_N_I,
    STANDING_N_OFF_I as CYCLE254_N_OFF_I,
    TestMamariI3gram090076000IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE217_CLAIM,
    STANDING_N_I_EACH as CYCLE217_N_I_EACH,
    STANDING_N_LEFTOVER as CYCLE217_N_LEFTOVER,
    STANDING_N_OFF_I_EACH as CYCLE217_N_OFF_I_EACH,
    TestMamariILeftover076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_forward_stem_scoreboard import (
    STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM as CYCLE216_SHARE_ONE,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE216_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE216_N_LEFTOVER,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_IA2_174,
    leftover_extra_forward_3grams,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    LOCKED_FORWARD_STEMS_AFTER_000,
    STANDING_G as CYCLE256_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE256_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_DISTINCT_REMAINING11 as CYCLE256_N_DISTINCT,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
    STANDING_REMAINING11_NEXT_STEMS as CYCLE256_REMAINING11_NEXT_STEMS,
    STANDING_REMAINING11_SITES as CYCLE256_REMAINING11_SITES,
    STANDING_TIED_STEMS as CYCLE256_TIED_STEMS,
    i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem,
    leftover_extra_remaining_after_000,
    leftover_extra_remaining_after_000_nested_counts_hold,
    leftover_extra_remaining_after_000_next_stems,
    select_remaining_after_000_g,
    TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_next_stem_scoreboard import (
    STANDING_G as CYCLE234_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE234_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G as CYCLE234_CLAIM,
    STANDING_K as CYCLE234_K,
    STANDING_N_REMAINING4 as CYCLE234_N_REMAINING4,
    STANDING_N_TIED_AT_K as CYCLE234_N_TIED_AT_K,
    STANDING_TIED_STEMS as CYCLE234_TIED_STEMS,
    leftover_extra_remaining_after_001,
    TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_005_fwd000_scoreboard import (
    STANDING_G as CYCLE253_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000 as CYCLE253_CLAIM,
    STANDING_K as CYCLE253_K,
    STANDING_MATCHING_SITES as CYCLE253_MATCHING_SITES,
    STANDING_N_REMAINING10 as CYCLE253_N_REMAINING10,
    leftover_extra_remaining_after_005,
    leftover_extra_remaining_after_005_with_000,
    TestMamariILeftoverExtra090076RemainingAfter005Fwd000Scoreboard,
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
STANDING_N_I = 69
STANDING_N_LEFTOVER = 56
STANDING_N_REMAINING11 = 19
STANDING_N_DISTINCT_REMAINING11 = 19
STANDING_N_CONTINUING = 19
STANDING_N_NO_FORWARD = 0
STANDING_N_LINE_FINAL = 0
STANDING_REMAINING11_SITES = CYCLE256_REMAINING11_SITES
STANDING_REMAINING11_NEXT_STEMS = CYCLE256_REMAINING11_NEXT_STEMS
STANDING_REMAINING11_NEXT_4GRAMS = (
    ("090", "076", "012", "076"),
    ("090", "076", "175", "002"),
    ("090", "076", "755", "509"),
    ("090", "076", "470", "700"),
    ("090", "076", "430", "076"),
    ("090", "076", "600", "002"),
    ("090", "076", "384", "570"),
    ("090", "076", "535", "076"),
    ("090", "076", "050", "050"),
    ("090", "076", "147", "076"),
    ("090", "076", "090", "076"),
    ("090", "076", "386", "202"),
    ("090", "076", "505", "633"),
    ("090", "076", "607", "073"),
    ("090", "076", "057", "240"),
    ("090", "076", "072", "205"),
    ("090", "076", "300", "000"),
    ("090", "076", "255", "067"),
    ("090", "076", "670", "700"),
)
STANDING_SEQUENCES = STANDING_REMAINING11_NEXT_4GRAMS
STANDING_CONTINUING_SITES = STANDING_REMAINING11_SITES
STANDING_LINE_FINAL_SITES = ()
STANDING_NO_FORWARD_SITES = ()
STANDING_NEXT_STEMS = STANDING_REMAINING11_NEXT_STEMS
STANDING_ROLES = ("leftover_extra_remaining_after_000",) * STANDING_N_CONTINUING
STANDING_N_I_EACH = (1,) * STANDING_N_CONTINUING
STANDING_N_ON_I_EACH = (1,) * STANDING_N_CONTINUING
STANDING_I_SITES = tuple((site,) for site in STANDING_CONTINUING_SITES)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_CONTINUING
STANDING_OFF_I_SITES = ((),) * STANDING_N_CONTINUING
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (STANDING_HITS_BY_TABLET_ONE_ON_I,) * STANDING_N_CONTINUING
STANDING_N_I_ONLY = 19
STANDING_N_NOT_I_ONLY = 0
STANDING_LEAKING_4GRAMS = ()
STANDING_IA2_174_IS_REMAINING_AFTER_005_000_NOT_REMAINING_AFTER_000 = True
STANDING_ALL_REMAINING11_HAVE_NEXT_TOKEN = True
STANDING_ALL_REMAINING11_HAVE_FOURTH_TOKEN = True
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_EACH = True
STANDING_CLAIM = (
    "i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only"
)
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY = True
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE217 = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE234 = False
STANDING_SAME_AS_CYCLE253 = False
STANDING_SAME_AS_CYCLE254 = False
STANDING_SAME_AS_CYCLE255 = False
STANDING_SAME_AS_CYCLE256 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE217 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_PREVIOUS_4GRAMS_OF_090_076_000_ARE_NOT_THIS_CYCLE = True
STANDING_090_076_000_DOES_NOT_COUNT = True
STANDING_090_076_005_DOES_NOT_COUNT = True
STANDING_090_076_011_DOES_NOT_COUNT = True
STANDING_090_076_087_DOES_NOT_COUNT = True
STANDING_090_076_280_DOES_NOT_COUNT = True
STANDING_090_076_530_DOES_NOT_COUNT = True
STANDING_090_076_700_DOES_NOT_COUNT = True
STANDING_090_076_001_DOES_NOT_COUNT = True
STANDING_090_076_013_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_090_076_070_000_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_ARE_THIS_CYCLE_ONLY_IF_MATCHING_4GRAM = True
STANDING_CYCLE256_N_REMAINING11 = 19
STANDING_CYCLE256_K = 1
STANDING_CYCLE256_G = "755"
STANDING_CYCLE256_UNIQUE = False
STANDING_CYCLE255_N_I_ONLY = 1
STANDING_CYCLE255_N_NOT_I_ONLY = 0
STANDING_CYCLE254_N_I = 2
STANDING_CYCLE254_N_OFF_I = 0
STANDING_CYCLE254_N_EXTRA = 0
STANDING_CYCLE253_K = 2
STANDING_CYCLE253_G = "000"
STANDING_CYCLE253_N_REMAINING10 = 21
STANDING_CYCLE234_N_REMAINING4 = 33
STANDING_CYCLE234_N_TIED_AT_K = 7
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE223_N_OFF_I = 3
STANDING_CYCLE217_N_I_ONLY = 11
STANDING_CYCLE217_N_NOT_I_ONLY = 0


def leftover_forward_4gram_start_site(
    remaining_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-256 remaining-after-000 site."""
    return remaining_site


def leftover_extra_remaining_after_000_next_4grams(
    leftover_sites: tuple[tuple[str, str, int], ...],
    leftover_next_4grams: tuple[tuple[str, ...] | None, ...],
    leftover_next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_000,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per remaining-after-000 site next 4-gram or None if line-final after X."""
    locked_set = set(locked)
    return tuple(
        gram
        for nxt, gram in zip(leftover_next_stems, leftover_next_4grams, strict=True)
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_000_line_final_sites(
    leftover_sites: tuple[tuple[str, str, int], ...],
    leftover_next_4grams: tuple[tuple[str, ...] | None, ...],
    leftover_next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_000,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-000 sites with a next stem and no 4th token."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt, gram in zip(
            leftover_sites,
            leftover_next_stems,
            leftover_next_4grams,
            strict=True,
        )
        if nxt is not None and nxt not in locked_set and gram is None
    )


def leftover_extra_remaining_after_000_continuing_sites(
    leftover_sites: tuple[tuple[str, str, int], ...],
    leftover_next_4grams: tuple[tuple[str, ...] | None, ...],
    leftover_next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS_AFTER_000,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-000 sites that continue to a 4th token."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt, gram in zip(
            leftover_sites,
            leftover_next_stems,
            leftover_next_4grams,
            strict=True,
        )
        if nxt is not None and nxt not in locked_set and gram is not None
    )


def continuing_forward_4grams(
    per_site_next_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, ...], ...]:
    """Distinct-preserving continuing remaining-after-000 forward 4-grams."""
    return tuple(gram for gram in per_site_next_4grams if gram is not None)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_CONTINUING,
) -> bool:
    """True iff every continuing remaining-after-000 forward 4-gram is I-only.

    Claim holds only if every continuing gram has N_off_I=0 and
    N_I>=1. Hapax is not assumed; N_I may be greater than 1.
    Line-final remaining-after-000 sites (no 4th token) do not
    count as 4-gram hapax and are not invented. Length must stay
    the continuing count.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestILeftoverExtra090076RemainingAfter000Fwd4IOnlyHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-000 forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 000 / 070 000 / 076 070 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "012", "076"))
        self.assertEqual(STANDING_SEQUENCES[2], ("090", "076", "755", "509"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("090", "076", "670", "700"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_CONTINUING)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_CONTINUING)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:2], GRAM2)
            self.assertEqual(len(gram), STANDING_N4)
            self.assertNotEqual(gram[:3], CYCLE254_GRAM3)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram, CYCLE255_SEQUENCES[0])
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["090", "076", "012", "076", "090", "076", "012", "076"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [
            list(STANDING_SEQUENCES[0][:2])
            + ["006"]
            + list(STANDING_SEQUENCES[0][2:])
        ]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE254_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "000"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["076", "070", "449", "449"]], STANDING_SEQUENCES[0]), 0)
        planted = ["999", "090", "076", "012", "076"]
        self.assertEqual(site_next_4gram(planted, 1, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_forward_3gram(planted, 1, GRAM2), ("090", "076", "012"))
        line_final_after_x = ["999", "090", "076", "012"]
        self.assertEqual(site_forward_3gram(line_final_after_x, 1, GRAM2), ("090", "076", "012"))
        self.assertIsNone(site_next_4gram(line_final_after_x, 1, GRAM2))
        no_next = ["087", "078", "090", "076"]
        self.assertIsNone(site_forward_3gram(no_next, 2, GRAM2))
        self.assertIsNone(site_next_4gram(no_next, 2, GRAM2))
        self.assertTrue(STANDING_090_076_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all continuing remaining-after-000 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only(
                hold_ones,
                hold_zeros,
            )
        )
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only(
                (2,) + hold_ones[1:],
                hold_zeros,
            )
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only(
                hold_ones,
                tuple(lose_off),
            )
        )
        lose_off_mid = list(hold_zeros)
        lose_off_mid[10] = 1
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only(
                hold_ones,
                tuple(lose_off_mid),
            )
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only(
                tuple(lose_missing_i),
                hold_zeros,
            )
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only((), ())
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only(
                hold_ones[:-1],
                hold_zeros[:-1],
            )
        )
        self.assertEqual(STANDING_CLAIM, STANDING_CLAIM)
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertTrue(CYCLE217_CLAIM)
        self.assertEqual(CYCLE217_N_LEFTOVER, 11)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_256_remaining_after_000_forwards_not_retuned(self):
        """4-grams stay the cycle-256 remaining-after-000 forwards; 000 / 070 000 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(STANDING_REMAINING11_SITES, CYCLE256_REMAINING11_SITES)
        self.assertEqual(STANDING_REMAINING11_NEXT_STEMS, CYCLE256_REMAINING11_NEXT_STEMS)
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE256_N_REMAINING11)
        self.assertEqual(CYCLE256_N_REMAINING11, 19)
        self.assertEqual(CYCLE256_N_DISTINCT, 19)
        self.assertEqual(CYCLE256_G, "755")
        self.assertEqual(CYCLE256_K, 1)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertFalse(CYCLE256_CLAIM)
        self.assertEqual(len(set(STANDING_NEXT_STEMS)), 19)
        self.assertEqual(len(set(STANDING_SEQUENCES)), 19)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        for gram, nxt in zip(STANDING_SEQUENCES, STANDING_NEXT_STEMS, strict=True):
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertEqual(gram[2], nxt)
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS_AFTER_000)
            self.assertNotEqual(gram[:3], CYCLE254_GRAM3)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram, CYCLE255_SEQUENCES[0])
            self.assertNotEqual(gram[:2], CYCLE171_GRAM2)
        for site, start in zip(
            STANDING_CONTINUING_SITES,
            (sites[0] for sites in STANDING_I_SITES),
            strict=True,
        ):
            self.assertEqual(leftover_forward_4gram_start_site(site), start)
            self.assertEqual(site, start)
        self.assertEqual(STANDING_LINE_FINAL_SITES, ())
        self.assertEqual(STANDING_N_NO_FORWARD, 0)
        self.assertNotIn(STANDING_IA2_174, STANDING_REMAINING11_SITES)
        self.assertEqual(STANDING_IA2_174, (SIDE_IA, "Ia2", 174))
        self.assertTrue(STANDING_IA2_174_IS_REMAINING_AFTER_005_000_NOT_REMAINING_AFTER_000)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE217)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_000_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE255)
        self.assertFalse(STANDING_SAME_AS_CYCLE217)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-000 forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.next_stems = leftover_extra_next_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.leftover_next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.forwards = leftover_extra_forward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.remaining11 = leftover_extra_remaining_after_000(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining11_stems = leftover_extra_remaining_after_000_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.per_site_next_4grams = leftover_extra_remaining_after_000_next_4grams(
            self.leftover_sites,
            self.leftover_next_4grams,
            self.next_stems,
        )
        self.line_final = leftover_extra_remaining_after_000_line_final_sites(
            self.leftover_sites,
            self.leftover_next_4grams,
            self.next_stems,
        )
        self.continuing = leftover_extra_remaining_after_000_continuing_sites(
            self.leftover_sites,
            self.leftover_next_4grams,
            self.next_stems,
        )
        self.grams = continuing_forward_4grams(self.per_site_next_4grams)
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
        self.g, self.k, self.unique = select_remaining_after_000_g(
            self.remaining11_stems
        )
        self.unique_max = i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining10 = leftover_extra_remaining_after_005(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_000 = leftover_extra_remaining_after_005_with_000(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining4 = leftover_extra_remaining_after_001(
            self.leftover_sites,
            self.next_stems,
        )
        self.claim_holds = (
            i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only(
                self.n_i,
                self.n_off_i,
            )
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = len(self.grams) - self.n_i_only
        self.leaking = tuple(
            gram
            for gram, on, off in zip(self.grams, self.n_i, self.n_off_i, strict=True)
            if not sequence_is_i_only(on, off)
        )

    def test_tokens_and_sites_are_cycle_256_remaining_after_000_not_retuned(self):
        """4-grams stay the cycle-256 remaining-after-000 lock. Nested 19/K=1/G=755 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(self.leftover_sites), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.remaining11, STANDING_REMAINING11_SITES)
        self.assertEqual(self.remaining11, CYCLE256_REMAINING11_SITES)
        self.assertEqual(self.remaining11_stems, STANDING_REMAINING11_NEXT_STEMS)
        self.assertEqual(len(self.remaining11), STANDING_N_REMAINING11)
        self.assertEqual(STANDING_N_REMAINING11, 19)
        self.assertEqual(len(set(self.remaining11_stems)), STANDING_N_DISTINCT_REMAINING11)
        self.assertEqual(self.g, CYCLE256_G)
        self.assertEqual(self.g, "755")
        self.assertEqual(self.k, CYCLE256_K)
        self.assertEqual(self.k, 1)
        self.assertFalse(self.unique)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertFalse(self.unique_max)
        self.assertFalse(CYCLE256_CLAIM)
        if (
            len(self.remaining11) != 19
            or self.k != 1
            or self.g != "755"
            or self.unique
            or self.unique_max
        ):
            self.fail("nested cycle 256 unique-max false N_remaining11=19 K=1 G=755 drifted")
        self.assertEqual(self.per_site_next_4grams, STANDING_REMAINING11_NEXT_4GRAMS)
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(self.continuing, STANDING_CONTINUING_SITES)
        self.assertEqual(self.line_final, STANDING_LINE_FINAL_SITES)
        self.assertEqual(self.line_final, ())
        self.assertEqual(len(self.grams), STANDING_N_CONTINUING)
        self.assertEqual(STANDING_N_CONTINUING, 19)
        self.assertEqual(len(self.line_final), STANDING_N_LINE_FINAL)
        self.assertEqual(STANDING_N_LINE_FINAL, 0)
        self.assertTrue(all(stem is not None for stem in self.remaining11_stems))
        self.assertTrue(all(gram is not None for gram in self.per_site_next_4grams))
        self.assertNotIn(STANDING_IA2_174, self.remaining11)
        self.assertIn(STANDING_IA2_174, self.share_000)
        self.assertEqual(self.share_000, CYCLE253_MATCHING_SITES)
        self.assertEqual(self.share_000, CYCLE254_I_SITES)
        self.assertEqual(len(self.remaining10), CYCLE253_N_REMAINING10)
        self.assertEqual(len(self.remaining10), 21)
        self.assertEqual(len(self.remaining4), CYCLE234_N_REMAINING4)
        self.assertEqual(len(self.remaining4), 33)
        self.assertTrue(
            leftover_extra_remaining_after_000_nested_counts_hold(
                56,
                55,
                1,
                8,
                47,
                6,
                41,
                5,
                36,
                3,
                33,
                2,
                31,
                2,
                29,
                2,
                27,
                2,
                25,
                2,
                23,
                2,
                21,
                2,
                19,
            )
        )
        prior_256 = self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]
        self.assertEqual(prior_256["cycle"], 256)
        self.assertEqual(prior_256["N_remaining11"], 19)
        self.assertEqual(prior_256["K"], 1)
        self.assertEqual(prior_256["G"], "755")
        self.assertFalse(prior_256["G_uniquely_most_frequent"])
        self.assertFalse(prior_256["i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_256["remaining_after_000_sites"]),
            STANDING_REMAINING11_SITES,
        )
        self.assertEqual(
            tuple(prior_256["remaining_after_000_next_stems"]),
            STANDING_REMAINING11_NEXT_STEMS,
        )
        self.assertTrue(prior_256["ia2_174_is_remaining_after_005_000_not_remaining_after_000"])
        prior_255 = self.survey["i_090_076_000_forward_4grams_i_only"]
        self.assertEqual(prior_255["cycle"], 255)
        self.assertEqual(prior_255["N_i_only"], 1)
        self.assertEqual(prior_255["N_not_i_only"], 0)
        self.assertTrue(prior_255["ia2_174_line_final"])
        self.assertTrue(prior_255["i_090_076_000_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE255_CLAIM)
        self.assertEqual(CYCLE255_N_I_ONLY, 1)
        self.assertEqual(CYCLE255_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE255_IA2_174_LINE_FINAL)
        prior_254 = self.survey["i_3gram_090_076_000_i_only"]
        self.assertEqual(prior_254["cycle"], 254)
        self.assertEqual(prior_254["N_I"], 2)
        self.assertEqual(prior_254["N_off_I"], 0)
        self.assertEqual(prior_254["N_extra"], 0)
        self.assertTrue(prior_254["i_3gram_090_076_000_i_only"])
        self.assertTrue(CYCLE254_CLAIM)
        prior_253 = self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]
        self.assertEqual(prior_253["cycle"], 253)
        self.assertEqual(prior_253["G"], "000")
        self.assertEqual(prior_253["K"], 2)
        self.assertEqual(prior_253["N_remaining10"], 21)
        self.assertTrue(prior_253["i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"])
        self.assertTrue(CYCLE253_CLAIM)
        prior_234 = self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]
        self.assertEqual(prior_234["cycle"], 234)
        self.assertEqual(prior_234["N_remaining4"], 33)
        self.assertEqual(prior_234["N_tied_at_K"], 7)
        self.assertFalse(prior_234["G_uniquely_most_frequent"])
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertEqual(CYCLE234_G, "700")
        self.assertEqual(CYCLE234_K, 2)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertEqual(CYCLE234_TIED_STEMS[-1], "000")
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_217 = self.survey["i_leftover_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_217["cycle"], 217)
        self.assertTrue(prior_217["i_leftover_076_070_forward_4grams_i_only"])
        self.assertEqual(prior_217["N_i_only"], 11)
        self.assertEqual(prior_217["N_not_i_only"], 0)
        self.assertTrue(CYCLE217_CLAIM)
        prior_219 = self.survey["i_090_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_219["cycle"], 219)
        self.assertFalse(prior_219["i_090_076_070_forward_4grams_i_only"])
        self.assertEqual(prior_219["N_i_only"], 7)
        self.assertEqual(prior_219["N_not_i_only"], 1)
        self.assertFalse(CYCLE219_CLAIM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_000_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_no_line_final_and_claim_holds(self):
        """Each remaining-after-000 forward 4-gram is N_I=1, N_off_I=0. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (1,) * STANDING_N_CONTINUING)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0,) * STANDING_N_CONTINUING)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.line_final, ())
        self.assertEqual(self.leaking, STANDING_LEAKING_4GRAMS)
        self.assertEqual(self.leaking, ())
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_i_only, 19)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_not_i_only, 0)
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from 0")
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked remaining-after-000 hapax")
        if self.line_final:
            self.fail("measured line-final remaining-after-000 set drifted from empty")
        if self.leaking:
            self.fail("measured remaining-after-000 forward 4-grams leaked off I")
        for site, start, gram, nxt, role, sites, n_on, n_off in zip(
            STANDING_CONTINUING_SITES,
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
            self.assertGreater(len(stems), start[2] + 3)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram[:3], CYCLE254_GRAM3)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS_AFTER_000)
            self.assertEqual(role, "leftover_extra_remaining_after_000")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        for n_on, locked in zip(self.n_i, STANDING_N_I_EACH, strict=True):
            if n_on != locked:
                self.fail("measured N_I drifted from the locked count")
        if not self.claim_holds:
            self.fail("measured remaining-after-000 forward 4-grams are not all I-only")
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_EACH)
        self.assertTrue(STANDING_ALL_REMAINING11_HAVE_NEXT_TOKEN)
        self.assertTrue(STANDING_ALL_REMAINING11_HAVE_FOURTH_TOKEN)
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
            i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only(
                self.n_i,
                self.n_off_i,
            ),
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY
        )
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, STANDING_CLAIM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE217)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE217)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_090_076_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_IA2_174_IS_REMAINING_AFTER_005_000_NOT_REMAINING_AFTER_000)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        for site in CYCLE254_I_SITES:
            self.assertNotIn(site, STANDING_REMAINING11_SITES)
        for site in CYCLE223_OFF_I_SITES:
            self.assertNotIn(site, STANDING_REMAINING11_SITES)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[9], "Ia10")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_256_255_254_253_234_223_and_217_still_compute(self):
        """Cycle 256 unique-max lose 19/K=1/G=755, 255 1/0 + line-final, 254 2/0, 253 21/2/000, 234 7-way, 223 69/3, 217 11/11 stay."""
        prior_256 = TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard()
        prior_256.setUp()
        prior_256.test_counts_19_remaining11_all_hapax_g_755_k_1_and_hypothesis_loses()
        prior_256.test_survey_matches_computed_lock()
        self.assertEqual(prior_256.n_remaining11, 19)
        self.assertEqual(prior_256.k, 1)
        self.assertEqual(prior_256.g, "755")
        self.assertFalse(prior_256.unique)
        self.assertFalse(prior_256.claim_holds)
        self.assertFalse(CYCLE256_CLAIM)
        self.assertEqual(CYCLE256_N_REMAINING11, 19)
        self.assertEqual(CYCLE256_K, 1)
        self.assertEqual(CYCLE256_G, "755")
        self.assertEqual(tuple(CYCLE256_TIED_STEMS), tuple(CYCLE256_TIED_STEMS))
        if (
            prior_256.n_remaining11 != 19
            or prior_256.k != 1
            or prior_256.g != "755"
            or prior_256.unique
        ):
            self.fail("nested cycle 256 unique-max false N_remaining11=19 K=1 G=755 drifted")
        prior_255 = TestMamariI090076000Forward4gramsIOnlyScoreboard()
        prior_255.setUp()
        prior_255.test_each_4gram_is_one_on_i_zero_off_i_ia2_174_line_final_and_claim_holds()
        prior_255.test_survey_matches_computed_lock()
        self.assertEqual(prior_255.n_i_only, 1)
        self.assertEqual(prior_255.n_not_i_only, 0)
        self.assertTrue(prior_255.claim_holds)
        self.assertTrue(CYCLE255_CLAIM)
        self.assertTrue(CYCLE255_IA2_174_LINE_FINAL)
        if prior_255.n_i_only != 1 or prior_255.n_not_i_only != 0:
            self.fail("nested cycle 255 090 076 000 forward 4-grams 1/0 + line-final drifted")
        prior_254 = TestMamariI3gram090076000IOnlyScoreboard()
        prior_254.setUp()
        prior_254.test_i_hits_are_two_on_ia_and_equal_leftover_extra_000()
        prior_254.test_3gram_is_zero_off_i_and_i_only()
        prior_254.test_survey_matches_computed_lock()
        self.assertEqual(prior_254.i_hits, CYCLE254_N_I)
        self.assertEqual(prior_254.i_hits, 2)
        self.assertEqual(prior_254.off_i_hits, CYCLE254_N_OFF_I)
        self.assertEqual(prior_254.off_i_hits, 0)
        self.assertEqual(len(prior_254.extra), CYCLE254_N_EXTRA)
        self.assertEqual(len(prior_254.extra), 0)
        self.assertEqual(prior_254.extra, CYCLE254_EXTRA_I_SITES)
        self.assertEqual(prior_254.i_sites, CYCLE254_I_SITES)
        self.assertTrue(prior_254.claim_holds)
        self.assertTrue(CYCLE254_CLAIM)
        if prior_254.i_hits != 2 or prior_254.off_i_hits != 0 or prior_254.extra:
            self.fail("nested cycle 254 090 076 000 I-only 2/0 extra I=0 drifted")
        prior_253 = TestMamariILeftoverExtra090076RemainingAfter005Fwd000Scoreboard()
        prior_253.setUp()
        prior_253.test_counts_2_of_21_and_hypothesis_k_2_holds()
        prior_253.test_survey_matches_computed_lock()
        self.assertEqual(prior_253.k, 2)
        self.assertEqual(CYCLE253_G, "000")
        self.assertEqual(prior_253.n_remaining10, 21)
        self.assertEqual(prior_253.matching, CYCLE253_MATCHING_SITES)
        self.assertTrue(prior_253.claim_holds)
        self.assertTrue(CYCLE253_CLAIM)
        if prior_253.k != 2 or CYCLE253_G != "000" or prior_253.n_remaining10 != 21:
            self.fail("nested cycle 253 leftover extra remaining-after-005 G=000 K=2 drifted")
        prior_234 = TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard()
        prior_234.setUp()
        prior_234.test_counts_33_remaining4_g_700_k_2_and_hypothesis_loses()
        prior_234.test_survey_matches_computed_lock()
        self.assertEqual(prior_234.n_remaining4, 33)
        self.assertEqual(prior_234.k, 2)
        self.assertEqual(CYCLE234_G, "700")
        self.assertFalse(prior_234.unique)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(prior_234.claim_holds)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertEqual(CYCLE234_N_REMAINING4, 33)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        if prior_234.n_remaining4 != 33 or prior_234.k != 2 or prior_234.unique:
            self.fail("nested cycle 234 leftover extra remaining-after-001 7-way tie at 2 drifted")
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
        self.assertEqual(len(CYCLE223_I_SITES), 69)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_217 = TestMamariILeftover076070Forward4gramsIOnlyScoreboard()
        prior_217.setUp()
        prior_217.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_217.test_survey_matches_computed_lock()
        self.assertEqual(prior_217.n_i, CYCLE217_N_I_EACH)
        self.assertEqual(prior_217.n_off_i, CYCLE217_N_OFF_I_EACH)
        self.assertTrue(prior_217.claim_holds)
        self.assertTrue(CYCLE217_CLAIM)
        self.assertEqual(CYCLE217_N_LEFTOVER, 11)
        self.assertEqual(CYCLE216_N_LEFTOVER, 11)
        self.assertEqual(CYCLE216_N_DISTINCT, 11)
        self.assertFalse(CYCLE216_SHARE_ONE)
        if sum(CYCLE217_N_I_EACH) != 11 or sum(CYCLE217_N_OFF_I_EACH) != 0:
            self.fail("nested cycle 217 leftover 076 070 forward 4-grams 11/11 hapax drifted")
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        prior_219.test_survey_matches_computed_lock()
        self.assertEqual(prior_219.n_i_only, 7)
        self.assertEqual(prior_219.n_not_i_only, 1)
        self.assertFalse(prior_219.claim_holds)
        self.assertFalse(CYCLE219_CLAIM)
        if prior_219.n_i_only != 7 or prior_219.n_not_i_only != 1:
            self.fail("nested cycle 219 090 076 070 forward 4-grams 7/8 lose on T 000 drifted")
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
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_OF_090_076_000_ARE_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-257 remaining-after-000 forward-4 I-only lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"]
        self.assertEqual(lock["cycle"], 257)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(lock["N_remaining11"], STANDING_N_REMAINING11)
        self.assertEqual(lock["N_remaining11"], 19)
        self.assertEqual(lock["N_distinct_remaining11"], STANDING_N_DISTINCT_REMAINING11)
        self.assertEqual(lock["N_distinct_remaining11"], 19)
        self.assertEqual(lock["N_continuing"], STANDING_N_CONTINUING)
        self.assertEqual(lock["N_continuing"], 19)
        self.assertEqual(lock["N_no_forward"], STANDING_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(lock["N_line_final"], STANDING_N_LINE_FINAL)
        self.assertEqual(lock["N_line_final"], 0)
        self.assertEqual(lock["K"], 1)
        self.assertEqual(lock["G"], "755")
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertFalse(lock["i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem"])
        self.assertEqual(
            tuple(lock["locked_forward_stems_after_000"]),
            LOCKED_FORWARD_STEMS_AFTER_000,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_000_sites"]),
            STANDING_REMAINING11_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_000_next_stems"]),
            STANDING_REMAINING11_NEXT_STEMS,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["remaining_after_000_next_4grams"],
        )
        self.assertEqual(lock["line_final_remaining_after_000_sites"], [])
        self.assertEqual(
            tuple(tuple(row) for row in lock["continuing_sites"]),
            STANDING_CONTINUING_SITES,
        )
        self.assertTrue(lock["all_remaining11_have_next_token"])
        self.assertTrue(lock["all_remaining11_have_fourth_token"])
        self.assertTrue(lock["ia2_174_is_remaining_after_005_000_not_remaining_after_000"])
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_CONTINUING)
        for row, gram, site, nxt, role, sites, n_on, n_off in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CONTINUING_SITES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle256_site"]), site)
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
            self.assertEqual(row["off_i_tablets_with_hits"], [])
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
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
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only"]
        )
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_000_forward_4grams_i_only"]
        )
        self.assertEqual(lock["N_i_only"], 19)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(lock["nested_cycle256_N_remaining11"], 19)
        self.assertEqual(lock["nested_cycle256_K"], 1)
        self.assertEqual(lock["nested_cycle256_G"], "755")
        self.assertFalse(lock["nested_cycle256_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle255_N_i_only"], 1)
        self.assertEqual(lock["nested_cycle255_N_not_i_only"], 0)
        self.assertTrue(lock["nested_cycle255_ia2_174_line_final"])
        self.assertEqual(lock["nested_cycle254_N_I"], 2)
        self.assertEqual(lock["nested_cycle254_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle254_N_extra"], 0)
        self.assertEqual(lock["nested_cycle253_G"], "000")
        self.assertEqual(lock["nested_cycle253_K"], 2)
        self.assertEqual(lock["nested_cycle253_N_remaining10"], 21)
        self.assertEqual(lock["nested_cycle234_N_remaining4"], 33)
        self.assertEqual(lock["nested_cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["nested_cycle234_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle219_N_i_only"], 7)
        self.assertEqual(lock["nested_cycle219_N_not_i_only"], 1)
        self.assertEqual(tuple(lock["nested_cycle219_leak_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(lock["nested_cycle217_N_i_only"], 11)
        self.assertEqual(lock["nested_cycle217_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle171_N_I"], 43)
        self.assertEqual(lock["nested_cycle171_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle217"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle234"])
        self.assertFalse(lock["same_as_cycle253"])
        self.assertFalse(lock["same_as_cycle254"])
        self.assertFalse(lock["same_as_cycle255"])
        self.assertFalse(lock["same_as_cycle256"])
        self.assertTrue(lock["same_claim_shape_as_cycle217"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["previous_4grams_of_090_076_000_are_not_this_cycle"])
        self.assertTrue(lock["090_076_000_does_not_count"])
        self.assertTrue(lock["090_076_005_does_not_count"])
        self.assertTrue(lock["090_076_011_does_not_count"])
        self.assertTrue(lock["090_076_087_does_not_count"])
        self.assertTrue(lock["090_076_280_does_not_count"])
        self.assertTrue(lock["090_076_530_does_not_count"])
        self.assertTrue(lock["090_076_700_does_not_count"])
        self.assertTrue(lock["090_076_001_does_not_count"])
        self.assertTrue(lock["090_076_013_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["090_076_070_000_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_are_this_cycle_only_if_matching_4gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_000_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_000_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_005_fwd000_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_001_next_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]["cycle"],
            256,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"][
                "N_remaining11"
            ],
            19,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"][
                "i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem"
            ]
        )
        self.assertEqual(self.survey["i_090_076_000_forward_4grams_i_only"]["cycle"], 255)
        self.assertTrue(
            self.survey["i_090_076_000_forward_4grams_i_only"][
                "i_090_076_000_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_090_076_000_i_only"]["cycle"], 254)
        self.assertTrue(self.survey["i_3gram_090_076_000_i_only"]["i_3gram_090_076_000_i_only"])
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["cycle"],
            253,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_4grams_i_only"]["cycle"],
            217,
        )
        self.assertTrue(
            self.survey["i_leftover_076_070_forward_4grams_i_only"][
                "i_leftover_076_070_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 257 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
