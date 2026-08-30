"""I's cycle-254 leftover extra remaining-after-005 090 076 000 forward-4-grams off-I lock.

Cycle 255 text-search lock. Uses already-vendored A–V and the
cycle-254 I sites of 3-gram 090 076 000 (all 2 I sites). Extra
I sites = 0, so this is leftover extra remaining-after-005
000 4-grams for the one site that continues. Does not retune
those 4-grams, the 2 I sites, leftover extra remaining-after-005
G=000 K=2 N_remaining10=21, leftover extra remaining-after-011
005, leftover extra remaining-after-087 011, leftover extra
remaining-after-280 087, leftover extra remaining-after-530
280, leftover extra remaining-after-700 530, leftover extra
remaining-after-001 700, leftover extra remaining-after-001
unique-max (cycle 234 lost), leftover extra remaining-after-013
001, leftover extra remaining-after-071 013, leftover extra
remaining 071, leftover extra forward 070, leftover extra
sites, leftover n=4, or the already-closed leftover remaining
family. Does not vendor a new tablet. Does not scrape X. W has
no Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not
redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 219 (I 090 076 070 forward 4-grams
all I-only lost 7/8; 090 076 070 000 leaks 1/1 on T), cycle
252 (I 090 076 005 forward 4-grams all I-only hapax 1/0 x2),
cycle 249 (I 090 076 011 forward 4-grams 4/4 extra I=2), and
cycle 243 (I 090 076 280 forward 4-grams all I-only hapax
1/0 x2). Cycle 254 I 090 076 000 I-only holds 2/0 extra I=0,
cycle 253 leftover extra remaining-after-005 K=2 / G=000
N_remaining10=21, cycle 252 2/2 hapax, cycle 219 7/8 lose on
T 000, and cycle 223 69/3 stay. Off-I T sites of 090 076 are
not this 3-gram and are not this 4-gram. Do not count
090 076 070 000 as this 4-gram. Leftover extra remaining
after 000 is not locked this cycle. Previous 4-grams of the
two I sites are not locked this cycle. Nested-check Ia2[174]
has next token 000 and no following token on that line (next
4-gram is None). Do not invent a 4-gram for a line-final
site. Nested-check leftover extra remaining-after-005
continuing site is 090 076 000 076 at Ia10[141]; measure, do
not assume. 090 076 005, 090 076 011, 090 076 087,
090 076 280, 090 076 530, 090 076 700, 090 076 001,
090 076 013, 090 076 070, 090 076 071, and 090 076 without
000 do not count. Do not retune leftover n=4, 076-cells, or
any detector.

Locks exact consecutive hits of each continuing I 090 076 000
forward 4-gram on tablet I and on every other vendored tablet
A–H and J–V. Nested-check leftover extra remaining-after-005
pair next 4-grams are None / 090 076 000 076; measure, do not
assume those next tokens. Do not assume hapax; count each
from fixtures. Hypothesis: the one continuing 4-gram is
I-only and Ia2[174] has no next 4-gram. Measured: N_I=1 at
Ia10[141]; N_off_I=0; Ia2[174] line-final. Claim that can
lose: i_090_076_000_forward_4grams_all_i_only. True iff every
continuing I site's forward 4-gram has N_I ≥ 1 and N_off_I = 0,
and Ia2[174] has no next 4-gram. This can lose if
090 076 000 076 (or any other continuing 4-gram) leaks off I
(same shape as cycle 219 090 076 070 000 1/1 on T), or if
Ia2[174] is not line-final. Extra I = 0, so this is leftover
extra remaining-after-005 000 4-grams for the one site that
continues. Do not assume the I-only result; measure. Do not
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
from tests.test_mamari_i_090_076_005_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_005_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE252_CLAIM,
    STANDING_N_I_ONLY as CYCLE252_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE252_N_NOT_I_ONLY,
    TestMamariI090076005Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_CLAIM,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_N_OFF_I_EACH as CYCLE219_N_OFF_I_EACH,
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
    GRAM2,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_000_i_only_scoreboard import (
    GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE254_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_000_I_ONLY as CYCLE254_I_ONLY,
    STANDING_I_NEXT_4GRAMS as CYCLE254_NEXT_4GRAMS,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE254_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE254_I_SITES,
    STANDING_IA2_174_HAS_FOLLOWING_TOKEN as CYCLE254_IA2_174_HAS_FOLLOWING,
    STANDING_IA2_174_HAS_NO_NEXT_4GRAM as CYCLE254_IA2_174_HAS_NO_NEXT_4GRAM,
    STANDING_IA2_174_LINE_FINAL as CYCLE254_IA2_174_LINE_FINAL,
    STANDING_IA2_174_NEXT_TOKEN as CYCLE254_IA2_174_NEXT_TOKEN,
    STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS as CYCLE254_LEFTOVER_MATCHING_NEXT_4GRAMS,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE254_LEFTOVER_MATCHING_SITES,
    STANDING_N_EXTRA as CYCLE254_N_EXTRA,
    STANDING_N_I as CYCLE254_N_I,
    STANDING_N_OFF_I as CYCLE254_N_OFF_I,
    extra_i_sites,
    leftover_extra_remaining_after_005_000_subset,
    named_off_i_sites as cycle254_named_off_i_sites,
    TestMamariI3gram090076000IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_005_i_only_scoreboard import (
    GRAM3 as CYCLE251_GRAM3,
    STANDING_I_SITES as CYCLE251_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_011_i_only_scoreboard import (
    GRAM3 as CYCLE248_GRAM3,
    STANDING_I_SITES as CYCLE248_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_013_i_only_scoreboard import (
    GRAM3 as CYCLE229_GRAM3,
    STANDING_I_SITES as CYCLE229_I_SITES,
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
    STANDING_I_SITES as CYCLE195_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_087_i_only_scoreboard import (
    GRAM3 as CYCLE245_GRAM3,
    STANDING_I_SITES as CYCLE245_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_280_i_only_scoreboard import (
    GRAM3 as CYCLE242_GRAM3,
    STANDING_I_SITES as CYCLE242_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_530_i_only_scoreboard import (
    GRAM3 as CYCLE239_GRAM3,
    STANDING_I_SITES as CYCLE239_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_700_i_only_scoreboard import (
    GRAM3 as CYCLE236_GRAM3,
    STANDING_I_SITES as CYCLE236_I_SITES,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    GRAM5 as CYCLE220_GRAM5,
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
    STANDING_MATCHING_SITES as CYCLE226_MATCHING_SITES,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_IA2_174,
    STANDING_IA2_174_NEXT_STEM,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
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
    GRAM3_FORWARD,
    STANDING_G as CYCLE253_G,
    STANDING_IA14_140,
    STANDING_IA14_140_NEXT_4GRAM,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000 as CYCLE253_CLAIM,
    STANDING_K as CYCLE253_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE253_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE253_MATCHING_SITES,
    STANDING_N_REMAINING10 as CYCLE253_N_REMAINING10,
    leftover_extra_remaining_after_005,
    leftover_extra_remaining_after_005_with_000,
    TestMamariILeftoverExtra090076RemainingAfter005Fwd000Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_011_fwd005_scoreboard import (
    leftover_extra_remaining_after_011,
    leftover_extra_remaining_after_011_with_005,
    leftover_extra_remaining_after_011_without_005,
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
STANDING_N_SEQUENCES = 1
STANDING_N_NO_FORWARD = 1
STANDING_CYCLE254_SITES = CYCLE254_I_SITES
STANDING_NO_FORWARD_SITES = ((SIDE_IA, "Ia2", 174),)
STANDING_CONTINUING_SITES = ((SIDE_IA, "Ia10", 141),)
STANDING_SEQUENCES = (("090", "076", "000", "076"),)
STANDING_PER_SITE_FORWARD_4GRAMS = CYCLE254_NEXT_4GRAMS
STANDING_NEXT_STEMS = ("076",)
STANDING_PREVIOUS_4GRAMS = CYCLE254_PREVIOUS_4GRAMS
STANDING_ROLES = ("forward",) * STANDING_N_SEQUENCES
STANDING_N_I_EACH = (1,) * STANDING_N_SEQUENCES
STANDING_N_ON_I_EACH = (1,) * STANDING_N_SEQUENCES
STANDING_I_SITES = tuple((site,) for site in STANDING_CONTINUING_SITES)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_SEQUENCES
STANDING_OFF_I_SITES = ((),)
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (STANDING_HITS_BY_TABLET_ONE_ON_I,) * STANDING_N_SEQUENCES
STANDING_N_I_ONLY = 1
STANDING_N_NOT_I_ONLY = 0
STANDING_N_EXTRA = 0
STANDING_EXTRA_I_SITES = CYCLE254_EXTRA_I_SITES
STANDING_LEFTOVER_MATCHING_SITES = CYCLE254_LEFTOVER_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS = CYCLE254_LEFTOVER_MATCHING_NEXT_4GRAMS
STANDING_IA2_174_LINE_FINAL = True
STANDING_IA2_174_NEXT_TOKEN = "000"
STANDING_IA2_174_HAS_FOLLOWING_TOKEN = False
STANDING_IA2_174_HAS_NO_NEXT_4GRAM = True
STANDING_IA14_140_IS_NOT_090_076_000 = True
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_EACH = True
STANDING_CLAIM = "i_090_076_000_forward_4grams_all_i_only"
STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY = True
STANDING_I_090_076_000_FORWARD_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_090_076_000_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE220 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE252 = False
STANDING_SAME_AS_CYCLE253 = False
STANDING_SAME_AS_CYCLE254 = False
STANDING_SAME_AS_LEFTOVER_EXTRA_REMAINING_AFTER_005_000_4GRAMS_ALONE = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE252 = True
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
STANDING_090_076_WITHOUT_000_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_090_076_070_000_DOES_NOT_COUNT = True
STANDING_999_090_076_070_000_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE = True
STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE254_N_I = 2
STANDING_CYCLE254_N_OFF_I = 0
STANDING_CYCLE254_N_EXTRA = 0
STANDING_CYCLE253_K = 2
STANDING_CYCLE253_G = "000"
STANDING_CYCLE253_N_REMAINING10 = 21
STANDING_CYCLE252_N_I_ONLY = 2
STANDING_CYCLE252_N_NOT_I_ONLY = 0


def forward_4gram_start_site(
    cycle254_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the cycle-254 I 090 076 000 site."""
    return cycle254_site


def site_forward_4gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """090 076 000 X if a next stem exists; None at end-of-line."""
    n3 = len(gram3)
    if tuple(stems[index : index + n3]) != gram3:
        return None
    next_index = index + n3
    if next_index >= len(stems):
        return None
    return tuple(stems[index : index + n3 + 1])


def i_090_076_000_forward_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_CYCLE254_SITES,
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
    """I 090 076 000 sites that have no next stem after the 3-gram."""
    return tuple(
        site
        for site, gram in zip(sites, forwards, strict=True)
        if gram is None
    )


def i_sites_with_forward(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """I 090 076 000 sites that continue after the 3-gram."""
    return tuple(
        site
        for site, gram in zip(sites, forwards, strict=True)
        if gram is not None
    )


def continuing_forward_4grams(
    forwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, ...], ...]:
    """Distinct-preserving continuing forward 4-grams (Nones dropped)."""
    return tuple(gram for gram in forwards if gram is not None)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_090_076_000_forward_4grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    ia2_174_has_no_next_4gram: bool,
    expected_n: int = STANDING_N_SEQUENCES,
) -> bool:
    """True iff every continuing I 090 076 000 forward 4-gram is I-only
    and Ia2[174] has no next 4-gram.

    Claim holds only if every continuing gram has N_off_I=0 and
    N_I>=1, length stays the continuing count, and the
    line-final site is not given an invented 4-gram. Hapax is
    not assumed; N_I may be greater than 1. Extra I = 0, so
    leftover extra remaining-after-005 000 4-grams for the one
    continuing site are this claim.
    """
    return (
        ia2_174_has_no_next_4gram
        and len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestI090076000Forward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-254 I 090 076 000 forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 070 000 / 005 / 011 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "000", "076"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_SEQUENCES)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_SEQUENCES)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[:3], GRAM3)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["090", "076", "000", "076", "090", "076", "000", "076"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [
            list(STANDING_SEQUENCES[0][:2])
            + ["006"]
            + list(STANDING_SEQUENCES[0][2:])
        ]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE207_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE195_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE251_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE248_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE220_GRAM5)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "000"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "070", "000"]], STANDING_SEQUENCES[0]), 0)
        planted = ["205", "090", "076", "000", "076"]
        self.assertEqual(site_forward_4gram(planted, 1, GRAM3), STANDING_SEQUENCES[0])
        self.assertEqual(site_next_4gram(planted, 1, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_forward_3gram(planted, 1, GRAM2), GRAM3)
        line_final = ["009", "090", "076", "000"]
        self.assertIsNone(site_forward_4gram(line_final, 1, GRAM3))
        self.assertIsNone(site_next_4gram(line_final, 1, GRAM2))
        self.assertEqual(site_forward_3gram(line_final, 1, GRAM2), GRAM3)
        self.assertTrue(STANDING_090_076_005_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_011_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_087_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_280_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_530_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_001_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_013_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_070_000_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_zero_off_i_and_ia2_174_line_final(self):
        """Boolean is True only when the continuing 4-gram is I-only and Ia2[174] is line-final."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_090_076_000_forward_4grams_all_i_only(hold_ones, hold_zeros, True)
        )
        self.assertTrue(
            i_090_076_000_forward_4grams_all_i_only((2,), hold_zeros, True)
        )
        self.assertFalse(
            i_090_076_000_forward_4grams_all_i_only(hold_ones, hold_zeros, False)
        )
        self.assertFalse(
            i_090_076_000_forward_4grams_all_i_only(hold_ones, (1,), True)
        )
        self.assertFalse(
            i_090_076_000_forward_4grams_all_i_only((0,), hold_zeros, True)
        )
        self.assertFalse(i_090_076_000_forward_4grams_all_i_only((), (), True))
        self.assertFalse(
            i_090_076_000_forward_4grams_all_i_only(hold_ones + (1,), hold_zeros + (0,), True)
        )
        self.assertEqual(STANDING_CLAIM, "i_090_076_000_forward_4grams_all_i_only")
        self.assertTrue(STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_090_076_000_FORWARD_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_IA2_174_HAS_NO_NEXT_4GRAM)
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_N_OFF_I_EACH[-1], 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertTrue(CYCLE252_CLAIM)
        self.assertEqual(CYCLE252_N_I_ONLY, 2)
        self.assertEqual(CYCLE252_N_NOT_I_ONLY, 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_254_forwards_not_retuned(self):
        """4-grams stay the cycle-254 I forwards; leftover / 005 / 070 000 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "000"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(STANDING_PER_SITE_FORWARD_4GRAMS, CYCLE254_NEXT_4GRAMS)
        self.assertEqual(STANDING_PER_SITE_FORWARD_4GRAMS, CYCLE253_MATCHING_NEXT_4GRAMS)
        self.assertEqual(STANDING_PER_SITE_FORWARD_4GRAMS, CYCLE254_LEFTOVER_MATCHING_NEXT_4GRAMS)
        self.assertEqual(STANDING_CYCLE254_SITES, CYCLE254_I_SITES)
        self.assertEqual(STANDING_CYCLE254_SITES, CYCLE253_MATCHING_SITES)
        self.assertEqual(STANDING_CYCLE254_SITES, CYCLE254_LEFTOVER_MATCHING_SITES)
        self.assertEqual(len(STANDING_CYCLE254_SITES), CYCLE254_N_I)
        self.assertEqual(CYCLE254_N_I, 2)
        self.assertEqual(CYCLE254_N_OFF_I, 0)
        self.assertEqual(CYCLE254_N_EXTRA, 0)
        self.assertEqual(STANDING_EXTRA_I_SITES, ())
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertIsNone(STANDING_PER_SITE_FORWARD_4GRAMS[0])
        self.assertEqual(STANDING_PER_SITE_FORWARD_4GRAMS[1], STANDING_SEQUENCES[0])
        self.assertEqual(STANDING_NO_FORWARD_SITES, ((SIDE_IA, "Ia2", 174),))
        self.assertEqual(STANDING_CONTINUING_SITES, ((SIDE_IA, "Ia10", 141),))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_SEQUENCES)
        self.assertEqual(STANDING_N_SEQUENCES, 1)
        self.assertEqual(STANDING_N_NO_FORWARD, 1)
        self.assertEqual(len(set(STANDING_NEXT_STEMS)), 1)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(CYCLE220_GRAM5, ("999", "090", "076", "070", "000"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertFalse(is_contiguous_substring(CYCLE195_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE207_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE251_GRAM3, gram))
            self.assertFalse(is_contiguous_substring(CYCLE248_GRAM3, gram))
            self.assertNotEqual(gram[:3], CYCLE195_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE207_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE229_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE236_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE239_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE242_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE245_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE248_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE251_GRAM3)
            self.assertNotEqual(gram[:2], CYCLE171_GRAM2)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram, CYCLE220_GRAM5)
            self.assertNotEqual(gram, GRAM2)
        self.assertEqual(STANDING_SEQUENCES[0][:2], GRAM2)
        self.assertEqual(forward_4gram_start_site(STANDING_CONTINUING_SITES[0]), STANDING_I_SITES[0][0])
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE220)
        self.assertFalse(STANDING_SAME_AS_CYCLE223)
        self.assertFalse(STANDING_SAME_AS_CYCLE252)
        self.assertFalse(STANDING_SAME_AS_CYCLE253)
        self.assertFalse(STANDING_SAME_AS_CYCLE254)
        self.assertTrue(STANDING_SAME_AS_LEFTOVER_EXTRA_REMAINING_AFTER_005_000_4GRAMS_ALONE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE252)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI090076000Forward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture I 090 076 000 forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle254_sites = STANDING_CYCLE254_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.measured_forwards = i_090_076_000_forward_4grams(
            self.i_sides,
            self.cycle254_sites,
            GRAM3,
        )
        self.no_forward = i_sites_without_forward(
            self.cycle254_sites,
            self.measured_forwards,
        )
        self.continuing = i_sites_with_forward(
            self.cycle254_sites,
            self.measured_forwards,
        )
        self.grams = continuing_forward_4grams(self.measured_forwards)
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
            cycle254_named_off_i_sites(gram) for gram in self.grams
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
        self.remaining9 = leftover_extra_remaining_after_011(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.share_005 = leftover_extra_remaining_after_011_with_005(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.remaining10 = leftover_extra_remaining_after_005(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.leftover_matching = leftover_extra_remaining_after_005_with_000(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.leftover_matching_next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.leftover_matching,
            GRAM2,
        )
        self.extra = extra_i_sites(self.cycle254_sites, self.leftover_matching)
        self.n3_i = ngram_hit_count(self.i_sides[SIDE_IA], GRAM3) + STANDING_IB_HITS
        self.n3_off_i = sum(tablet_hit_counts(self.by_tablet, GRAM3, OFF_I_TABLETS))
        ia2 = self.i_sides[SIDE_IA][IA_LINE_NAMES.index("Ia2")]
        self.ia2_174_has_no_next_4gram = (
            site_forward_4gram(ia2, 174, GRAM3) is None
        )
        self.claim_holds = i_090_076_000_forward_4grams_all_i_only(
            self.n_i,
            self.n_off_i,
            self.ia2_174_has_no_next_4gram,
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = STANDING_N_SEQUENCES - self.n_i_only

    def test_tokens_and_sites_are_cycle_254_forwards_not_retuned(self):
        """4-grams and I sites stay the cycle-254 forward lock. Nested 2/0 extra I=0 must hold."""
        self.assertEqual(GRAM3, ("090", "076", "000"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle254_sites, STANDING_CYCLE254_SITES)
        self.assertEqual(self.cycle254_sites, CYCLE254_I_SITES)
        self.assertEqual(self.cycle254_sites, CYCLE253_MATCHING_SITES)
        self.assertEqual(self.measured_forwards, STANDING_PER_SITE_FORWARD_4GRAMS)
        self.assertEqual(self.measured_forwards, CYCLE254_NEXT_4GRAMS)
        self.assertEqual(self.measured_forwards, CYCLE253_MATCHING_NEXT_4GRAMS)
        self.assertEqual(self.leftover_matching_next_4grams, STANDING_PER_SITE_FORWARD_4GRAMS)
        self.assertEqual(self.no_forward, STANDING_NO_FORWARD_SITES)
        self.assertEqual(self.continuing, STANDING_CONTINUING_SITES)
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(len(self.no_forward), STANDING_N_NO_FORWARD)
        self.assertEqual(STANDING_N_NO_FORWARD, 1)
        self.assertEqual(len(self.grams), STANDING_N_SEQUENCES)
        self.assertEqual(STANDING_N_SEQUENCES, 1)
        self.assertEqual(self.n3_i, STANDING_CYCLE254_N_I)
        self.assertEqual(self.n3_i, 2)
        self.assertEqual(self.n3_off_i, STANDING_CYCLE254_N_OFF_I)
        self.assertEqual(self.n3_off_i, 0)
        self.assertEqual(self.leftover_matching, CYCLE253_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE254_I_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE253_K)
        self.assertEqual(STANDING_CYCLE253_K, 2)
        self.assertEqual(STANDING_CYCLE253_G, "000")
        self.assertEqual(CYCLE253_G, "000")
        self.assertEqual(CYCLE253_K, 2)
        self.assertEqual(len(self.remaining10), CYCLE253_N_REMAINING10)
        self.assertEqual(len(self.remaining10), 21)
        self.assertEqual(len(self.remaining9), 23)
        self.assertEqual(len(self.share_005), 2)
        self.assertEqual(len(self.remaining4), CYCLE234_N_REMAINING4)
        self.assertEqual(len(self.remaining4), 33)
        self.assertEqual(
            self.remaining10,
            leftover_extra_remaining_after_011_without_005(
                STANDING_LEFTOVER_SITES,
                self.next_stems,
            ),
        )
        self.assertTrue(
            leftover_extra_remaining_after_005_000_subset(
                self.leftover_matching,
                self.cycle254_sites,
            )
        )
        self.assertEqual(self.extra, ())
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        if self.n3_i != 2 or self.n3_off_i != 0 or self.extra:
            self.fail("nested cycle 254 090 076 000 I-only 2/0 extra I=0 drifted")
        if (
            len(self.leftover_matching) != 2
            or CYCLE253_G != "000"
            or len(self.remaining10) != 21
        ):
            self.fail("nested cycle 253 leftover extra remaining-after-005 G=000 K=2 drifted")
        if self.extra:
            self.fail("extra I 090 076 000 leftover-of-leftover sites appeared")
        prior_254 = self.survey["i_3gram_090_076_000_i_only"]
        self.assertEqual(prior_254["cycle"], 254)
        self.assertEqual(prior_254["N_I"], CYCLE254_N_I)
        self.assertEqual(prior_254["N_I"], 2)
        self.assertEqual(prior_254["N_off_I"], CYCLE254_N_OFF_I)
        self.assertEqual(prior_254["N_off_I"], 0)
        self.assertEqual(prior_254["N_extra"], 0)
        self.assertTrue(prior_254["i_3gram_090_076_000_i_only"])
        self.assertTrue(CYCLE254_I_ONLY)
        self.assertEqual(
            [None if gram is None else list(gram) for gram in STANDING_PER_SITE_FORWARD_4GRAMS],
            prior_254["i_next_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_254["i_sites"]),
            STANDING_CYCLE254_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PREVIOUS_4GRAMS],
            prior_254["i_previous_4grams"],
        )
        self.assertTrue(prior_254["ia2_174_has_no_next_4gram"])
        prior_253 = self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]
        self.assertEqual(prior_253["cycle"], 253)
        self.assertEqual(prior_253["G"], "000")
        self.assertEqual(prior_253["K"], 2)
        self.assertEqual(prior_253["N_remaining10"], 21)
        self.assertTrue(prior_253["i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"])
        self.assertTrue(CYCLE253_CLAIM)
        self.assertEqual(
            [None if gram is None else list(gram) for gram in STANDING_PER_SITE_FORWARD_4GRAMS],
            prior_253["matching_next_4grams"],
        )
        prior_252 = self.survey["i_090_076_005_forward_4grams_i_only"]
        self.assertEqual(prior_252["cycle"], 252)
        self.assertTrue(prior_252["i_090_076_005_forward_4grams_all_i_only"])
        self.assertEqual(prior_252["N_i_only"], 2)
        self.assertEqual(prior_252["N_not_i_only"], 0)
        self.assertTrue(CYCLE252_CLAIM)
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
        self.assertFalse(CYCLE219_CLAIM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_ia2_174_line_final_and_claim_holds(self):
        """Continuing 4-gram is 1/0. Ia2[174] has no next 4-gram. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (1,))
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0,))
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(len(self.grams), STANDING_N_SEQUENCES)
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked hapax")
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from the locked 1/0")
        if self.no_forward != STANDING_NO_FORWARD_SITES:
            self.fail("measured line-final I 090 076 000 set drifted")
        if not self.ia2_174_has_no_next_4gram:
            self.fail("Ia2[174] is not line-final; invented a next 4-gram")
        for site, start, gram, nxt, role, sites, n_on, n_off, off_sites in zip(
            STANDING_CONTINUING_SITES,
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
            self.assertEqual(
                tuple(stems[start[2] - 1 : start[2] + STANDING_N3]),
                STANDING_PREVIOUS_4GRAMS[1],
            )
            self.assertEqual(site_forward_4gram(stems, start[2], GRAM3), gram)
            self.assertEqual(site_next_4gram(stems, start[2], GRAM2), gram)
            self.assertEqual(site_forward_3gram(stems, start[2], GRAM2), GRAM3)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram[:3], CYCLE195_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE207_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE251_GRAM3)
            self.assertNotEqual(gram[:3], CYCLE248_GRAM3)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram, CYCLE220_GRAM5)
            self.assertNotEqual(gram, GRAM2)
            self.assertEqual(role, "forward")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertEqual(off_sites, ())
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, CYCLE253_MATCHING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE226_MATCHING_SITES)
            self.assertNotIn(site, CYCLE229_I_SITES)
            self.assertNotIn(site, CYCLE236_I_SITES)
            self.assertNotIn(site, CYCLE239_I_SITES)
            self.assertNotIn(site, CYCLE242_I_SITES)
            self.assertNotIn(site, CYCLE245_I_SITES)
            self.assertNotIn(site, CYCLE248_I_SITES)
            self.assertNotIn(site, CYCLE251_I_SITES)
            self.assertNotIn(site, CYCLE195_I_SITES)
            self.assertNotEqual(site, STANDING_IA14_140)
            self.assertNotEqual(site, STANDING_IA2_174)
        ia2 = self.i_sides[SIDE_IA][IA_LINE_NAMES.index("Ia2")]
        self.assertEqual(tuple(ia2[174:177]), GRAM3)
        self.assertEqual(len(ia2), 177)
        self.assertEqual(ia2[176], STANDING_IA2_174_NEXT_TOKEN)
        self.assertEqual(STANDING_IA2_174_NEXT_STEM, "000")
        self.assertEqual(CYCLE254_IA2_174_NEXT_TOKEN, "000")
        self.assertTrue(STANDING_IA2_174_LINE_FINAL)
        self.assertTrue(CYCLE254_IA2_174_LINE_FINAL)
        self.assertFalse(STANDING_IA2_174_HAS_FOLLOWING_TOKEN)
        self.assertFalse(CYCLE254_IA2_174_HAS_FOLLOWING)
        self.assertTrue(STANDING_IA2_174_HAS_NO_NEXT_4GRAM)
        self.assertTrue(CYCLE254_IA2_174_HAS_NO_NEXT_4GRAM)
        self.assertIsNone(site_forward_4gram(ia2, 174, GRAM3))
        self.assertIsNone(site_next_4gram(ia2, 174, GRAM2))
        self.assertEqual(site_forward_3gram(ia2, 174, GRAM2), GRAM3)
        self.assertEqual(STANDING_NO_FORWARD_SITES[0], STANDING_IA2_174)
        self.assertIn(STANDING_IA2_174, self.no_forward)
        self.assertNotIn(STANDING_IA2_174, self.continuing)
        ia14 = self.i_sides[SIDE_IA][IA_LINE_NAMES.index("Ia14")]
        self.assertEqual(tuple(ia14[140:144]), STANDING_IA14_140_NEXT_4GRAM)
        self.assertEqual(tuple(ia14[140:144]), CYCLE219_LEAK_4GRAM)
        self.assertNotEqual(tuple(ia14[140:143]), GRAM3)
        self.assertTrue(STANDING_IA14_140_IS_NOT_090_076_000)
        self.assertNotIn(STANDING_IA14_140, STANDING_CYCLE254_SITES)
        if self.n_i_only != STANDING_N_I_ONLY:
            self.fail("measured N_i_only drifted from 1")
        if self.n_not_i_only != STANDING_N_NOT_I_ONLY:
            self.fail("measured N_not_i_only drifted from 0")
        if not self.claim_holds:
            self.fail("measured continuing forward 4-grams are not all I-only or Ia2[174] is not line-final")
        self.assertEqual(self.n_i_only, 1)
        self.assertEqual(self.n_not_i_only, 0)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_EACH)
        self.assertTrue(STANDING_SAME_AS_LEFTOVER_EXTRA_REMAINING_AFTER_005_000_4GRAMS_ALONE)
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
            self.assertEqual(cycle254_named_off_i_sites(gram), ())
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
        self.assertNotEqual(tuple(ta9[2:5]), GRAM3)
        self.assertEqual(
            i_090_076_000_forward_4grams_all_i_only(
                self.n_i,
                self.n_off_i,
                self.ia2_174_has_no_next_4gram,
            ),
            STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_090_076_000_FORWARD_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_090_076_000_forward_4grams_all_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE220)
        self.assertFalse(STANDING_SAME_AS_CYCLE223)
        self.assertFalse(STANDING_SAME_AS_CYCLE252)
        self.assertFalse(STANDING_SAME_AS_CYCLE253)
        self.assertFalse(STANDING_SAME_AS_CYCLE254)
        self.assertTrue(STANDING_SAME_AS_LEFTOVER_EXTRA_REMAINING_AFTER_005_000_4GRAMS_ALONE)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE252)
        self.assertTrue(STANDING_090_076_005_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_011_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_087_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_280_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_530_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_001_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_013_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[9], "Ia10")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_254_253_252_219_and_223_still_compute(self):
        """Cycle 254 2/0 extra I=0, 253 K=2/G=000 N_remaining10=21, 252 2/2 hapax, 219 7/8 lose on T 000, 223 69/3 stay."""
        prior_254 = TestMamariI3gram090076000IOnlyScoreboard()
        prior_254.setUp()
        prior_254.test_i_hits_are_two_on_ia_and_equal_leftover_extra_000()
        prior_254.test_3gram_is_zero_off_i_and_i_only()
        prior_254.test_survey_matches_computed_lock()
        self.assertEqual(prior_254.i_hits, CYCLE254_N_I)
        self.assertEqual(prior_254.i_hits, 2)
        self.assertEqual(prior_254.off_i_hits, CYCLE254_N_OFF_I)
        self.assertEqual(prior_254.off_i_hits, 0)
        self.assertEqual(prior_254.i_sites, CYCLE254_I_SITES)
        self.assertEqual(prior_254.extra, CYCLE254_EXTRA_I_SITES)
        self.assertEqual(len(prior_254.extra), CYCLE254_N_EXTRA)
        self.assertEqual(CYCLE254_N_EXTRA, 0)
        self.assertTrue(prior_254.claim_holds)
        self.assertTrue(CYCLE254_I_ONLY)
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
        self.assertEqual(prior_253.matching_next_4grams, STANDING_PER_SITE_FORWARD_4GRAMS)
        self.assertTrue(prior_253.claim_holds)
        self.assertTrue(CYCLE253_CLAIM)
        if prior_253.k != 2 or CYCLE253_G != "000" or prior_253.n_remaining10 != 21:
            self.fail("nested cycle 253 leftover extra remaining-after-005 G=000 K=2 drifted")
        prior_252 = TestMamariI090076005Forward4gramsIOnlyScoreboard()
        prior_252.setUp()
        prior_252.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_252.test_survey_matches_computed_lock()
        self.assertEqual(prior_252.n_i_only, 2)
        self.assertEqual(prior_252.n_not_i_only, 0)
        self.assertTrue(prior_252.claim_holds)
        self.assertTrue(CYCLE252_CLAIM)
        self.assertEqual(CYCLE252_N_I_ONLY, 2)
        self.assertEqual(CYCLE252_N_NOT_I_ONLY, 0)
        if prior_252.n_i_only != 2 or prior_252.n_not_i_only != 0:
            self.fail("nested cycle 252 090 076 005 forward 4-grams 2/2 hapax drifted")
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
        self.assertEqual(CYCLE234_TIED_STEMS[-1], "000")
        if (
            prior_234.n_remaining4 != 33
            or prior_234.k != 2
            or prior_234.unique
        ):
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
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        prior_219.test_survey_matches_computed_lock()
        self.assertEqual(prior_219.n_i_only, 7)
        self.assertEqual(prior_219.n_not_i_only, 1)
        self.assertFalse(prior_219.claim_holds)
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        if prior_219.n_i_only != 7 or prior_219.n_not_i_only != 1:
            self.fail("nested cycle 219 090 076 070 forward 4-grams 7/8 lose on T 000 drifted")
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
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_PREVIOUS_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-255 I-forward-4 I-only hold."""
        lock = self.survey["i_090_076_000_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 255)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 2)
        self.assertEqual(lock["N_I"], CYCLE254_N_I)
        self.assertEqual(lock["N_sequences"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_sequences"], 1)
        self.assertEqual(lock["N_no_forward"], STANDING_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_CYCLE254_SITES,
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
            [None if gram is None else list(gram) for gram in STANDING_PER_SITE_FORWARD_4GRAMS],
            lock["per_site_forward_4grams"],
        )
        self.assertEqual(tuple(lock["per_site_next_stems"]), (None, "076"))
        self.assertEqual(tuple(lock["continuing_next_stems"]), STANDING_NEXT_STEMS)
        self.assertEqual(
            [list(gram) for gram in STANDING_PREVIOUS_4GRAMS],
            lock["i_previous_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_extra_remaining_after_005_000_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(
            [None if gram is None else list(gram) for gram in STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS],
            lock["leftover_extra_remaining_after_005_000_next_4grams"],
        )
        self.assertEqual(lock["extra_i_sites"], [])
        self.assertEqual(lock["N_extra"], 0)
        self.assertTrue(lock["ia2_174_line_final"])
        self.assertEqual(lock["ia2_174_next_token"], "000")
        self.assertFalse(lock["ia2_174_has_following_token"])
        self.assertTrue(lock["ia2_174_has_no_next_4gram"])
        self.assertTrue(lock["ia14_140_is_not_090_076_000"])
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_SEQUENCES)
        for row, gram, site, nxt, role, sites, n_on, n_off, off_sites, hits in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CONTINUING_SITES,
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
            self.assertEqual(tuple(row["cycle254_site"]), site)
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
        self.assertTrue(lock["i_090_076_000_forward_4grams_all_i_only"])
        self.assertEqual(
            lock["i_090_076_000_forward_4grams_all_i_only"],
            STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(lock["i_090_076_000_forward_4grams_i_only"])
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_i_only"], 1)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle254_N_I"], 2)
        self.assertEqual(lock["nested_cycle254_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle254_N_extra"], 0)
        self.assertEqual(lock["nested_cycle253_G"], STANDING_CYCLE253_G)
        self.assertEqual(lock["nested_cycle253_G"], "000")
        self.assertEqual(lock["nested_cycle253_K"], STANDING_CYCLE253_K)
        self.assertEqual(lock["nested_cycle253_K"], 2)
        self.assertEqual(lock["nested_cycle253_N_remaining10"], 21)
        self.assertEqual(lock["nested_cycle252_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle252_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle234_N_remaining4"], 33)
        self.assertEqual(lock["nested_cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["nested_cycle234_G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["nested_cycle234_tied_stems_at_K"]), CYCLE234_TIED_STEMS)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle219_N_i_only"], 7)
        self.assertEqual(lock["nested_cycle219_N_not_i_only"], 1)
        self.assertEqual(tuple(lock["nested_cycle219_leak_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle171_N_I"], 43)
        self.assertEqual(lock["nested_cycle171_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle220"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle252"])
        self.assertFalse(lock["same_as_cycle253"])
        self.assertFalse(lock["same_as_cycle254"])
        self.assertTrue(lock["same_as_leftover_extra_remaining_after_005_000_4grams_alone"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["same_claim_shape_as_cycle252"])
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
        self.assertTrue(lock["090_076_without_000_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["090_076_070_000_does_not_count"])
        self.assertTrue(lock["999_090_076_070_000_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_000_is_not_this_cycle"])
        self.assertTrue(lock["previous_4grams_are_not_this_cycle"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_090_076_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_005_fwd000_unchanged"])
        self.assertTrue(lock["standing_i_090_076_005_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_090_076_000_i_only"]["cycle"], 254)
        self.assertTrue(self.survey["i_3gram_090_076_000_i_only"]["i_3gram_090_076_000_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_000_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_090_076_000_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_000_i_only"]["N_extra"], 0)
        self.assertTrue(self.survey["i_3gram_090_076_000_i_only"]["ia2_174_has_no_next_4gram"])
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["cycle"],
            253,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"][
                "i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["G"],
            "000",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["K"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["N_remaining10"],
            21,
        )
        self.assertEqual(self.survey["i_090_076_005_forward_4grams_i_only"]["cycle"], 252)
        self.assertTrue(
            self.survey["i_090_076_005_forward_4grams_i_only"][
                "i_090_076_005_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_005_forward_4grams_i_only"]["N_i_only"], 2)
        self.assertEqual(self.survey["i_090_076_005_forward_4grams_i_only"]["N_not_i_only"], 0)
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
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI090076000Forward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 255 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
