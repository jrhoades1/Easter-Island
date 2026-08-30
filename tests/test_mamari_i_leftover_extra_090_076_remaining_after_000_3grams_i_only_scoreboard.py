"""I's cycle-257 leftover extra remaining-after-000 3-grams off-I lock.

Cycle 258 text-search lock. Uses already-vendored A–V and the
cycle-256 leftover extra remaining-after-000 I sites of 2-gram
090 076 (the 19 leftover extra with-next sites whose next
token is none of 070, 071, 013, 001, 700, 530, 280, 087,
011, 005, or 000). Does not retune leftover extra
remaining-after-000 unique-max (cycle 256 lost: 19 hapax,
G=755 K=1), leftover extra remaining-after-000 forward
4-grams (cycle 257 held: 19/19 hapax 1/0), leftover extra
remaining-after-005 G=000 K=2 N_remaining10=21, leftover
extra remaining-after-001 unique-max (cycle 234 lost),
leftover extra remaining 071, leftover extra forward 070,
leftover extra sites, leftover n=4, or the already-closed
leftover remaining family. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new
agents. Not a meaning dictionary.

Same claim-shape as cycle 245 (090 076 087 was I-only 5/0
extra I=3 inside leftover n=4) and cycle 207 (090 076 070
lost 8/1 on T). Cycle 256 leftover extra remaining-after-000
unique-max lost N_remaining11=19 K=1 19-way tie G=755,
cycle 257 remaining-after-000 forward 4-grams all I-only
hapax 1/0 x19, cycle 255 1/0 + line-final, cycle 254
090 076 000 I-only 2/0 extra I=0, cycle 223 69/3, and
cycle 207 8/1 stay. Nested-check leftover extra
remaining-after-000 unique-max false, N_remaining11==19,
K==1, and all 19 forward 4-grams 1/0 (do not retune cycles
256/257). 3-grams 090 076 X for those 19 X are not yet
locked. Extra I of each (sites of 090 076 X not in leftover
extra remaining-after-000) is leftover-of-leftover, same
shape as cycle 245 extra I of 090 076 087. Do not confuse
with already-locked 3-grams (070 lost; 071/013/001/700/530/
280/087/011/005/000 hold). Remaining-after-000 X is none of
those. Do not peel leftover extra I 090 076 previous stems
this cycle. Do not retune leftover n=4.

Locks exact consecutive hits of each leftover extra
remaining-after-000 3-gram 090 076 X on tablet I and on
every other vendored tablet A–H and J–V. The nineteen
3-grams: 090 076 012, 090 076 175, 090 076 755,
090 076 470, 090 076 430, 090 076 600, 090 076 384,
090 076 535, 090 076 050, 090 076 147, 090 076 090,
090 076 386, 090 076 505, 090 076 607, 090 076 057,
090 076 072, 090 076 300, 090 076 255, 090 076 670.
Measure; do not assume the stem list if nested-check
differs. Hypothesis: all 19 leftover extra
remaining-after-000 3-grams 090 076 X are I-only.
Claim that can lose:
i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only.
True iff every one of those 19 3-grams has N_I ≥ 1 and
N_off_I = 0. Extra I ≠ 0 for some X does not make the
claim lose (still I-only); still lock extra I. This can
lose if any 090 076 X leaks off I (same shape as cycle 207
090 076 070 8/1 on T). Given 2-gram 090 076 already leaks
on T, this is a real lose path. Measured: N_i_only=19 /
N_not_i_only=0; extra I total=3 (607 extra I=1 at Ia8[106]
inside leftover n=4 remaining 999 021 090 076; 057 extra
I=2 at Ia8[114]/Ia9[28] inside leftover n=4 remaining
090 076 057 600); no off-I tablets. Nested leftover extra
remaining-after-000 090 076 X site ⊆ I 090 076 X sites for
each X. The claim is true. Do not assume; measure. Do not
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
from tests.test_mamari_i_090_076_000_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE255_CLAIM,
    STANDING_N_I_ONLY as CYCLE255_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE255_N_NOT_I_ONLY,
    STANDING_IA2_174_LINE_FINAL as CYCLE255_IA2_174_LINE_FINAL,
    TestMamariI090076000Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_057600_COVERED,
    STANDING_LEFTOVER_999021_COVERED,
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
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
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
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_087_i_only_scoreboard import (
    GRAM3 as CYCLE245_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE245_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_087_I_ONLY as CYCLE245_CLAIM,
    STANDING_I_SITES as CYCLE245_I_SITES,
    STANDING_N_EXTRA as CYCLE245_N_EXTRA,
    STANDING_N_I as CYCLE245_N_I,
    STANDING_N_OFF_I as CYCLE245_N_OFF_I,
    TestMamariI3gram090076087IOnlyScoreboard,
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
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE257_CLAIM,
    STANDING_N_I_ONLY as CYCLE257_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE257_N_NOT_I_ONLY,
    STANDING_REMAINING11_NEXT_4GRAMS as CYCLE257_NEXT_4GRAMS,
    leftover_extra_remaining_after_000_continuing_sites,
    leftover_extra_remaining_after_000_line_final_sites,
    leftover_extra_remaining_after_000_next_4grams,
    TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    LOCKED_FORWARD_STEMS_AFTER_000,
    STANDING_G as CYCLE256_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE256_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
    STANDING_REMAINING11_NEXT_STEMS as CYCLE256_REMAINING11_NEXT_STEMS,
    STANDING_REMAINING11_SITES as CYCLE256_REMAINING11_SITES,
    i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem,
    leftover_extra_remaining_after_000,
    leftover_extra_remaining_after_000_nested_counts_hold,
    leftover_extra_remaining_after_000_next_stems,
    leftover_extra_remaining_after_000_with_g,
    select_remaining_after_000_g,
    TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    STANDING_MATCHING_LEFTOVERS as CYCLE222_MATCHING,
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
STANDING_REMAINING11_SITES = CYCLE256_REMAINING11_SITES
STANDING_REMAINING11_NEXT_STEMS = CYCLE256_REMAINING11_NEXT_STEMS
STANDING_SEQUENCES = tuple(
    ("090", "076", stem) for stem in STANDING_REMAINING11_NEXT_STEMS
)
STANDING_NEXT_STEMS = STANDING_REMAINING11_NEXT_STEMS
STANDING_LOCKED_3GRAM_STEMS = LOCKED_FORWARD_STEMS_AFTER_000
STANDING_ROLES = ("leftover_extra_remaining_after_000",) * STANDING_N_REMAINING11
STANDING_N_I_EACH = (
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1,
)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_I_SITES = (
    ((SIDE_IA, "Ia1", 2),),
    ((SIDE_IA, "Ia1", 15),),
    ((SIDE_IA, "Ia1", 27),),
    ((SIDE_IA, "Ia1", 59),),
    ((SIDE_IA, "Ia1", 96),),
    ((SIDE_IA, "Ia2", 14),),
    ((SIDE_IA, "Ia2", 114),),
    ((SIDE_IA, "Ia2", 128),),
    ((SIDE_IA, "Ia2", 154),),
    ((SIDE_IA, "Ia2", 165),),
    ((SIDE_IA, "Ia4", 84),),
    ((SIDE_IA, "Ia4", 121),),
    ((SIDE_IA, "Ia5", 127),),
    ((SIDE_IA, "Ia7", 137), (SIDE_IA, "Ia8", 106)),
    ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28), (SIDE_IA, "Ia9", 129)),
    ((SIDE_IA, "Ia10", 137),),
    ((SIDE_IA, "Ia12", 150),),
    ((SIDE_IA, "Ia13", 135),),
    ((SIDE_IA, "Ia14", 177),),
)
STANDING_LEFTOVER_MATCHING_SITES = tuple(
    (site,) for site in STANDING_REMAINING11_SITES
)
STANDING_EXTRA_I_SITES = (
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    ((SIDE_IA, "Ia8", 106),),
    ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28)),
    (),
    (),
    (),
    (),
)
STANDING_N_EXTRA_EACH = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0)
STANDING_N_EXTRA_TOTAL = 3
STANDING_XS_WITH_EXTRA = ("607", "057")
STANDING_I_PREVIOUS_4GRAMS = (
    (("999", "090", "076", "012"),),
    (("045", "090", "076", "175"),),
    (("048", "090", "076", "755"),),
    (("380", "090", "076", "470"),),
    (("011", "090", "076", "430"),),
    (("499", "090", "076", "600"),),
    (("600", "090", "076", "384"),),
    (("600", "090", "076", "535"),),
    (("600", "090", "076", "050"),),
    (("076", "090", "076", "147"),),
    (("092", "090", "076", "090"),),
    (("291", "090", "076", "386"),),
    (("109", "090", "076", "505"),),
    (("700", "090", "076", "607"), ("021", "090", "076", "607")),
    (("000", "090", "076", "057"), ("999", "090", "076", "057"), ("999", "090", "076", "057")),
    (("010", "090", "076", "072"),),
    (("382", "090", "076", "300"),),
    (("008", "090", "076", "255"),),
    (("326", "090", "076", "670"),),
)
STANDING_I_NEXT_4GRAMS = (
    (("090", "076", "012", "076"),),
    (("090", "076", "175", "002"),),
    (("090", "076", "755", "509"),),
    (("090", "076", "470", "700"),),
    (("090", "076", "430", "076"),),
    (("090", "076", "600", "002"),),
    (("090", "076", "384", "570"),),
    (("090", "076", "535", "076"),),
    (("090", "076", "050", "050"),),
    (("090", "076", "147", "076"),),
    (("090", "076", "090", "076"),),
    (("090", "076", "386", "202"),),
    (("090", "076", "505", "633"),),
    (("090", "076", "607", "073"), ("090", "076", "607", "755")),
    (("090", "076", "057", "600"), ("090", "076", "057", "600"), ("090", "076", "057", "240")),
    (("090", "076", "072", "205"),),
    (("090", "076", "300", "000"),),
    (("090", "076", "255", "067"),),
    (("090", "076", "670", "700"),),
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_REMAINING11
STANDING_OFF_I_SITES = ((),) * STANDING_N_REMAINING11
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET_TWO_ON_I = tuple(
    2 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET_THREE_ON_I = tuple(
    3 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_HITS_BY_TABLET_ONE_ON_I
    if n == 1
    else STANDING_HITS_BY_TABLET_TWO_ON_I
    if n == 2
    else STANDING_HITS_BY_TABLET_THREE_ON_I
    for n in STANDING_N_I_EACH
)
STANDING_N_I_ONLY = 19
STANDING_N_NOT_I_ONLY = 0
STANDING_LEAKING_3GRAMS = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_IA2_174_IS_REMAINING_AFTER_005_000_NOT_REMAINING_AFTER_000 = True
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_CLAIM = (
    "i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only"
)
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY = True
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_000_3grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE207 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE245 = False
STANDING_SAME_AS_CYCLE254 = False
STANDING_SAME_AS_CYCLE256 = False
STANDING_SAME_AS_CYCLE257 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245 = True
STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS = True
STANDING_PREVIOUS_STEMS_OF_090_076_ARE_NOT_THIS_CYCLE = True
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
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_ARE_THIS_CYCLE_ONLY_IF_MATCHING_3GRAM = True
STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE = True
STANDING_CYCLE257_N_I_ONLY = 19
STANDING_CYCLE257_N_NOT_I_ONLY = 0
STANDING_CYCLE256_N_REMAINING11 = 19
STANDING_CYCLE256_K = 1
STANDING_CYCLE256_G = "755"
STANDING_CYCLE256_UNIQUE = False
STANDING_CYCLE255_N_I_ONLY = 1
STANDING_CYCLE255_N_NOT_I_ONLY = 0
STANDING_CYCLE254_N_I = 2
STANDING_CYCLE254_N_OFF_I = 0
STANDING_CYCLE254_N_EXTRA = 0
STANDING_CYCLE245_N_I = 5
STANDING_CYCLE245_N_OFF_I = 0
STANDING_CYCLE245_N_EXTRA = 3
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE223_N_OFF_I = 3
STANDING_CYCLE207_N_I = 8
STANDING_CYCLE207_N_OFF_I = 1


def remaining_after_000_3grams(
    remaining_stems: tuple[str, ...] = STANDING_REMAINING11_NEXT_STEMS,
) -> tuple[tuple[str, ...], ...]:
    """3-grams 090 076 X for leftover extra remaining-after-000 next stems."""
    return tuple(("090", "076", stem) for stem in remaining_stems)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_REMAINING11,
) -> bool:
    """True iff every remaining-after-000 3-gram is I-only.

    Extra I does not make the claim lose. Length must stay 19.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


def leftover_extra_remaining_after_000_3gram_subset(
    leftover_site: tuple[str, str, int],
    i_sites: tuple[tuple[str, str, int], ...],
) -> bool:
    """True iff leftover extra remaining-after-000 site ⊆ I 090 076 X."""
    return leftover_site in i_sites


def leftover_extra_remaining_after_000_3grams_subset_all(
    leftover_sites: tuple[tuple[str, str, int], ...],
    i_sites_each: tuple[tuple[tuple[str, str, int], ...], ...],
) -> bool:
    """True iff every remaining-after-000 site sits in its I 3-gram sites."""
    if len(leftover_sites) != len(i_sites_each):
        return False
    return all(
        leftover_extra_remaining_after_000_3gram_subset(site, sites)
        for site, sites in zip(leftover_sites, i_sites_each, strict=True)
    )


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...],
    leftover_matching: tuple[tuple[str, str, int], ...],
) -> tuple[tuple[str, str, int], ...]:
    """I 090 076 X sites that are not leftover extra remaining-after-000."""
    leftover_set = set(leftover_matching)
    return tuple(site for site in i_sites if site not in leftover_set)


class TestILeftoverExtra090076RemainingAfter0003gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-000 3-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. Locked 070/000 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "012"))
        self.assertEqual(STANDING_SEQUENCES[2], ("090", "076", "755"))
        self.assertEqual(STANDING_SEQUENCES[13], ("090", "076", "607"))
        self.assertEqual(STANDING_SEQUENCES[14], ("090", "076", "057"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("090", "076", "670"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_REMAINING11)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_REMAINING11)
        self.assertEqual(remaining_after_000_3grams(), STANDING_SEQUENCES)
        for gram, nxt in zip(STANDING_SEQUENCES, STANDING_NEXT_STEMS, strict=True):
            self.assertEqual(gram[:2], GRAM2)
            self.assertEqual(gram[2], nxt)
            self.assertEqual(len(gram), STANDING_N3)
            self.assertNotIn(nxt, STANDING_LOCKED_3GRAM_STEMS)
            self.assertNotEqual(gram, CYCLE207_GRAM3)
            self.assertNotEqual(gram, CYCLE254_GRAM3)
            self.assertNotEqual(gram, CYCLE245_GRAM3)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["090", "076", "012", "090", "076", "012"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [list(STANDING_SEQUENCES[0][:2]) + ["006"] + list(STANDING_SEQUENCES[0][2:])]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE207_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "070"]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "000"]], STANDING_SEQUENCES[0]), 0)
        planted = ["999", "090", "076", "012"]
        self.assertEqual(site_forward_3gram(planted, 1, GRAM2), STANDING_SEQUENCES[0])
        no_next = ["087", "078", "090", "076"]
        self.assertIsNone(site_forward_3gram(no_next, 2, GRAM2))
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_000_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_3gram(self):
        """Boolean is True only when all remaining-after-000 3-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only(
                hold_ones,
                hold_zeros,
            )
        )
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only(
                (3,) + hold_ones[1:],
                hold_zeros,
            )
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only(
                hold_ones,
                tuple(lose_off),
            )
        )
        lose_off_mid = list(hold_zeros)
        lose_off_mid[14] = 1
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only(
                hold_ones,
                tuple(lose_off_mid),
            )
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only(
                tuple(lose_missing_i),
                hold_zeros,
            )
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only((), ())
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only(
                hold_ones[:-1],
                hold_zeros[:-1],
            )
        )
        self.assertTrue(STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertEqual(STANDING_N_EXTRA_TOTAL, 3)
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertFalse(CYCLE207_GRAM3[2] in STANDING_NEXT_STEMS)
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(CYCLE207_N_OFF_I, 1)
        self.assertTrue(CYCLE245_CLAIM)
        self.assertEqual(CYCLE245_N_EXTRA, 3)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_be_nonempty(self):
        """Remaining-after-000 site ⊆ I sites; extra I can be nonempty."""
        provider = MockProvider()
        self.assertTrue(
            leftover_extra_remaining_after_000_3grams_subset_all(
                STANDING_REMAINING11_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(STANDING_N_EXTRA_EACH[13], 1)
        self.assertEqual(STANDING_N_EXTRA_EACH[14], 2)
        self.assertEqual(sum(STANDING_N_EXTRA_EACH), STANDING_N_EXTRA_TOTAL)
        self.assertEqual(
            extra_i_sites(STANDING_I_SITES[13], STANDING_LEFTOVER_MATCHING_SITES[13]),
            STANDING_EXTRA_I_SITES[13],
        )
        self.assertEqual(
            extra_i_sites(STANDING_I_SITES[14], STANDING_LEFTOVER_MATCHING_SITES[14]),
            STANDING_EXTRA_I_SITES[14],
        )
        self.assertEqual(STANDING_EXTRA_I_SITES[13], ((SIDE_IA, "Ia8", 106),))
        self.assertEqual(
            STANDING_EXTRA_I_SITES[14],
            ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28)),
        )
        self.assertIn(STANDING_EXTRA_I_SITES[13][0], CYCLE224_INSIDE_SITES)
        self.assertIn(STANDING_EXTRA_I_SITES[13][0], STANDING_LEFTOVER_999021_COVERED)
        for site in STANDING_EXTRA_I_SITES[14]:
            self.assertIn(site, CYCLE224_INSIDE_SITES)
            self.assertIn(site, STANDING_LEFTOVER_057600_COVERED)
        planted_extra = STANDING_REMAINING11_SITES + ((SIDE_IA, "Ia1", 0),)
        planted_sites = STANDING_I_SITES + (((SIDE_IA, "Ia1", 0),),)
        self.assertFalse(
            leftover_extra_remaining_after_000_3grams_subset_all(
                planted_extra,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(len(planted_sites), 20)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-000 3-gram off-I lock. Mock only."""

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
        self.grams = remaining_after_000_3grams(self.remaining11_stems)
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
        self.leftover_matching = tuple(
            leftover_extra_remaining_after_000_with_g(
                self.leftover_sites,
                self.next_stems,
                stem,
            )
            for stem in self.remaining11_stems
        )
        self.extra = tuple(
            extra_i_sites(sites, matching)
            for sites, matching in zip(
                self.i_sites,
                self.leftover_matching,
                strict=True,
            )
        )
        self.n_extra = tuple(len(row) for row in self.extra)
        self.g, self.k, self.unique = select_remaining_after_000_g(
            self.remaining11_stems
        )
        self.unique_max = i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem(
            self.leftover_sites,
            self.next_stems,
        )
        self.claim_holds = (
            i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only(
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
        """3-grams stay the cycle-256 remaining-after-000 X. Nested 19/K=1/G=755 stay."""
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
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(self.per_site_next_4grams, CYCLE257_NEXT_4GRAMS)
        self.assertEqual(self.line_final, ())
        self.assertEqual(len(self.grams), STANDING_N_REMAINING11)
        self.assertTrue(all(stem is not None for stem in self.remaining11_stems))
        self.assertTrue(all(gram is not None for gram in self.per_site_next_4grams))
        self.assertNotIn(STANDING_IA2_174, self.remaining11)
        self.assertTrue(
            leftover_extra_remaining_after_000_nested_counts_hold(
                56, 55, 1, 8, 47, 6, 41, 5, 36, 3, 33, 2, 31, 2, 29, 2, 27, 2, 25, 2, 23, 2, 21, 2, 19,
            )
        )
        for nxt in self.remaining11_stems:
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS_AFTER_000)
        prior_257 = self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"]
        self.assertEqual(prior_257["cycle"], 257)
        self.assertEqual(prior_257["N_i_only"], 19)
        self.assertEqual(prior_257["N_not_i_only"], 0)
        self.assertTrue(prior_257["i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE257_CLAIM)
        self.assertEqual(CYCLE257_N_I_ONLY, 19)
        self.assertEqual(CYCLE257_N_NOT_I_ONLY, 0)
        prior_256 = self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]
        self.assertEqual(prior_256["cycle"], 256)
        self.assertEqual(prior_256["N_remaining11"], 19)
        self.assertEqual(prior_256["K"], 1)
        self.assertEqual(prior_256["G"], "755")
        self.assertFalse(prior_256["G_uniquely_most_frequent"])
        self.assertFalse(prior_256["i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem"])
        prior_255 = self.survey["i_090_076_000_forward_4grams_i_only"]
        self.assertEqual(prior_255["cycle"], 255)
        self.assertEqual(prior_255["N_i_only"], 1)
        self.assertEqual(prior_255["N_not_i_only"], 0)
        self.assertTrue(prior_255["ia2_174_line_final"])
        prior_254 = self.survey["i_3gram_090_076_000_i_only"]
        self.assertEqual(prior_254["cycle"], 254)
        self.assertEqual(prior_254["N_I"], 2)
        self.assertEqual(prior_254["N_off_I"], 0)
        self.assertEqual(prior_254["N_extra"], 0)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_3gram_lock_extra_i_and_claim_holds(self):
        """Each remaining-after-000 3-gram is I-only. Extra I=3 does not lose."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(self.n_extra, STANDING_N_EXTRA_EACH)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(sum(self.n_extra), STANDING_N_EXTRA_TOTAL)
        self.assertEqual(STANDING_N_EXTRA_TOTAL, 3)
        self.assertEqual(self.leaking, STANDING_LEAKING_3GRAMS)
        self.assertEqual(self.leaking, ())
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_i_only, 19)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_not_i_only, 0)
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from 0")
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked remaining-after-000 3-grams")
        if self.leaking:
            self.fail("measured remaining-after-000 3-grams leaked off I")
        if self.extra != STANDING_EXTRA_I_SITES:
            self.fail("extra I leftover-of-leftover sites drifted")
        self.assertTrue(
            leftover_extra_remaining_after_000_3grams_subset_all(
                self.remaining11,
                self.i_sites,
            )
        )
        for site, gram, nxt, role, sites, matching, extra, n_on, n_off, n_ex, prevs, nexts in zip(
            STANDING_REMAINING11_SITES,
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_LEFTOVER_MATCHING_SITES,
            STANDING_EXTRA_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_N_EXTRA_EACH,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(matching, (site,))
            self.assertIn(site, sites)
            self.assertEqual(extra_i_sites(sites, matching), extra)
            self.assertEqual(len(extra), n_ex)
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N3]), gram)
            self.assertEqual(stems[site[2] + STANDING_N2], nxt)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N2]), GRAM2)
            self.assertEqual(site_forward_3gram(stems, site[2], GRAM2), gram)
            self.assertEqual(site_next_4gram(stems, site[2], GRAM2), nexts[sites.index(site)])
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS_AFTER_000)
            self.assertEqual(role, "leftover_extra_remaining_after_000")
            self.assertGreaterEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            for i_site, prev4, nxt4 in zip(sites, prevs, nexts, strict=True):
                line = line_stems_for_site(self.i_sides, i_site)
                idx = i_site[2]
                self.assertEqual(tuple(line[idx : idx + STANDING_N3]), gram)
                self.assertEqual(tuple(line[idx - 1 : idx + STANDING_N3]), prev4)
                self.assertEqual(site_next_4gram(line, idx, GRAM2), nxt4)
                if i_site != site:
                    self.assertIn(i_site, CYCLE224_INSIDE_SITES)
                    self.assertNotIn(i_site, STANDING_LEFTOVER_SITES)
        self.assertEqual(STANDING_XS_WITH_EXTRA, ("607", "057"))
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE224_INSIDE_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), STANDING_LEFTOVER_999021_COVERED)
        self.assertIn(("999", "021", "090", "076"), CYCLE222_MATCHING)
        self.assertIn(("090", "076", "057", "600"), CYCLE222_MATCHING)
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        if not self.claim_holds:
            self.fail("measured remaining-after-000 3-grams are not all I-only")
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off, n_on in zip(self.hits_by_tablet, self.off_i, self.n_i, strict=True):
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
            self.assertEqual(hits[VENDORED_TABLETS.index("I")], n_on)
            self.assertEqual(sum(hits) - n_on, 0)
        t_sides = load_t_sides()
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
            self.assertNotIn(following, STANDING_SEQUENCES)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertEqual(
            i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only(
                self.n_i,
                self.n_off_i,
            ),
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_IA2_174_IS_REMAINING_AFTER_005_000_NOT_REMAINING_AFTER_000)
        self.assertFalse(STANDING_SAME_AS_CYCLE207)
        self.assertFalse(STANDING_SAME_AS_CYCLE245)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_257_256_255_254_245_223_and_207_still_compute(self):
        """Cycle 257 19/19, 256 unique-max lose 19/K=1/G=755, 255 1/0, 254 2/0, 245 5/0 extra I=3, 223 69/3, 207 8/1 stay."""
        prior_257 = TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard()
        prior_257.setUp()
        prior_257.test_each_4gram_is_one_on_i_zero_off_i_no_line_final_and_claim_holds()
        prior_257.test_survey_matches_computed_lock()
        self.assertEqual(prior_257.n_i_only, 19)
        self.assertEqual(prior_257.n_not_i_only, 0)
        self.assertTrue(prior_257.claim_holds)
        self.assertTrue(CYCLE257_CLAIM)
        if prior_257.n_i_only != 19 or prior_257.n_not_i_only != 0:
            self.fail("nested cycle 257 remaining-after-000 forward 4-grams 19/19 hapax drifted")
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
        self.assertEqual(prior_254.off_i_hits, CYCLE254_N_OFF_I)
        self.assertEqual(len(prior_254.extra), CYCLE254_N_EXTRA)
        self.assertEqual(prior_254.extra, CYCLE254_EXTRA_I_SITES)
        self.assertTrue(prior_254.claim_holds)
        self.assertTrue(CYCLE254_CLAIM)
        if prior_254.i_hits != 2 or prior_254.off_i_hits != 0 or prior_254.extra:
            self.fail("nested cycle 254 090 076 000 I-only 2/0 extra I=0 drifted")
        prior_245 = TestMamariI3gram090076087IOnlyScoreboard()
        prior_245.setUp()
        prior_245.test_i_hits_are_five_on_ia_and_leftover_extra_087_is_subset()
        prior_245.test_3gram_is_zero_off_i_and_i_only()
        prior_245.test_survey_matches_computed_lock()
        self.assertEqual(prior_245.i_hits, CYCLE245_N_I)
        self.assertEqual(prior_245.off_i_hits, CYCLE245_N_OFF_I)
        self.assertEqual(len(prior_245.extra), CYCLE245_N_EXTRA)
        self.assertEqual(prior_245.extra, CYCLE245_EXTRA_I_SITES)
        self.assertTrue(prior_245.claim_holds)
        self.assertTrue(CYCLE245_CLAIM)
        if prior_245.i_hits != 5 or prior_245.off_i_hits != 0 or len(prior_245.extra) != 3:
            self.fail("nested cycle 245 090 076 087 I-only 5/0 extra I=3 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, CYCLE223_N_I)
        self.assertEqual(prior_223.off_i_hits, CYCLE223_N_OFF_I)
        self.assertEqual(prior_223.off_i_sites, CYCLE223_OFF_I_SITES)
        self.assertEqual(len(CYCLE223_I_SITES), 69)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_sites, CYCLE207_OFF_I_SITES)
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
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-258 remaining-after-000 3-gram I-only lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]
        self.assertEqual(lock["cycle"], 258)
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
            lock["remaining_after_000_3grams"],
        )
        self.assertTrue(lock["ia2_174_is_remaining_after_005_000_not_remaining_after_000"])
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_REMAINING11)
        for row, gram, site, nxt, role, sites, matching, extra, n_on, n_off, n_ex, prevs, nexts in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_REMAINING11_SITES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_LEFTOVER_MATCHING_SITES,
            STANDING_EXTRA_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_N_EXTRA_EACH,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens3"]), gram)
            self.assertEqual(tuple(row["cycle256_site"]), site)
            self.assertEqual(row["next_stem"], nxt)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["ia_hits"], n_on)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["leftover_extra_remaining_after_000_sites"]),
                matching,
            )
            self.assertTrue(row["leftover_extra_remaining_after_000_subset_of_i_sites"])
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["extra_i_sites"]),
                extra,
            )
            self.assertEqual(row["N_extra"], n_ex)
            self.assertEqual(
                [list(gram4) for gram4 in prevs],
                row["i_previous_4grams"],
            )
            self.assertEqual(
                [list(gram4) for gram4 in nexts],
                row["i_next_4grams"],
            )
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(row["off_i_tablets_with_hits"], [])
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertTrue(row["i_only"])
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(tuple(lock["N_extra_each"]), STANDING_N_EXTRA_EACH)
        self.assertEqual(lock["N_extra_total"], 3)
        self.assertEqual(tuple(lock["xs_with_extra"]), STANDING_XS_WITH_EXTRA)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only"]
        )
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]
        )
        self.assertEqual(lock["N_i_only"], 19)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["leaking_3grams"], [])
        self.assertEqual(lock["off_i_tablets_with_hits"], [])
        self.assertTrue(lock["extra_i_does_not_make_claim_lose"])
        self.assertEqual(lock["nested_cycle257_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle257_N_not_i_only"], 0)
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
        self.assertEqual(lock["nested_cycle245_N_I"], 5)
        self.assertEqual(lock["nested_cycle245_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle245_N_extra"], 3)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(tuple(lock["nested_cycle207_off_i_sites"][0]), CYCLE207_OFF_I_SITES[0])
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle207"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle245"])
        self.assertFalse(lock["same_as_cycle254"])
        self.assertFalse(lock["same_as_cycle256"])
        self.assertFalse(lock["same_as_cycle257"])
        self.assertTrue(lock["same_claim_shape_as_cycle207"])
        self.assertTrue(lock["same_claim_shape_as_cycle245"])
        self.assertTrue(lock["do_not_peel_leftover_extra_i_previous_stems"])
        self.assertTrue(lock["previous_stems_of_090_076_are_not_this_cycle"])
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
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_are_this_cycle_only_if_matching_3gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_000_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_000_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_087_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"]["cycle"],
            257,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]["cycle"],
            256,
        )
        self.assertEqual(self.survey["i_3gram_090_076_000_i_only"]["cycle"], 254)
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["cycle"], 245)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 258 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
