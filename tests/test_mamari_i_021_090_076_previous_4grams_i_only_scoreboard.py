"""I's leftover n=4 remaining previous-021 4-grams off-I lock.

Cycle 305 text-search lock. Uses already-vendored A–V and the
cycle-303 leftover n=4 remaining I 090 076 exactly 5 share
previous 021 cluster (K_021=5 of N_inside=13;
N_remaining_after_021=8; leftover extra=56; N_I=69) after
cycle 304 3-gram 021 090 076 I-only HOLD 5/0 extra I=0. Does
not retune that leftover n=4 remaining previous-021 lock,
leftover n=4 remaining unique previous stem (cycle 302
holds), leftover n=4 remaining share-one-forward-stem
(cycle 288 lost), leftover n=4 remaining sites, the leftover
n=4 set, leftover extra peels (225–287), leftover extra
previous-999 (cycle 261 holds), leftover extra remaining-
after-999 previous 600 (cycle 267 holds), leftover n=4
remaining remaining-after-011 3-grams (cycle 300), or
remaining-after-011 extra-I 4-grams (cycle 301). Does not
re-lock leftover extra previous-999 3-gram 999 090 076
(cycle 262), leftover extra 999 090 076 previous 4-grams
(cycle 263), leftover extra remaining-after-999 3-gram
600 090 076 (cycle 268), leftover extra 600 090 076 previous
4-grams (cycle 269), or 3-gram 021 090 076 I-only (cycle
304). Does not lock leftover n=4 remaining remaining-after-
021 unique previous stem this cycle (that is after previous-
021 4-grams, analog remaining-after peel). Does not vendor a
new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new
agents. Not a meaning dictionary.

Same claim-shape as cycle 269 (600 090 076 previous 4-grams
all I-only hapax HOLD 6/0) and cycle 291 (090 076 020 forward
4-grams all I-only HOLD 4/0 not hapax). Cycle 263 leftover
extra 999 090 076 previous 4-grams I-only hapax LOST (14/0,
N_not_hapax=2) is a different lose condition; this cycle
matches 291 (I-only), not 263 (hapax). A 3-gram I-only does
not imply the previous 4-grams are I-only. Two leftover n=4
remaining previous-021 sites share 999 021 090 076, so
hapax-on-I is not expected for every 4-gram. Not all hapax
is not an automatic fail. Cycle 219 lost: 090 076 070 000
leaks 1/1 on T. Cycle 207 lost: 090 076 070 is not I-only
(8/1 on T). Cycle 223 lost: 090 076 is not I-only (69/3 on
T). This cycle is leftover n=4 remaining previous-021
4-grams, a different population from leftover extra
999 090 076 / 600 090 076 previous 4-grams. 090 076 without
021, 600 090 076, 999 090 076, 090 076 020, leftover n=4
remaining 021 090 076 087, leftover extra W 999 090 076, and
leftover extra W 600 090 076 do not count as these 4-grams.
Do not retune leftover n=4, leftover extra peels, 076-cells,
or any detector. Do not overwrite cycle 167/268–304. Off-I T
sites of 090 076 are not this cycle except as off-I of a
previous-021 4-gram if they match. Do not assume the I-only
result.

Locks exact consecutive hits of each leftover n=4 remaining
previous-021 previous 4-gram <prev> 021 090 076 on tablet I
and on every other vendored tablet A–H and J–V. Population:
leftover n=4 remaining previous-021 I 090 076 sites (cycle
303 K_021=5). For each, take the previous 4-gram. Cycle 303
listed 600 021 090 076 / 007 021 090 076 / 150 021 090 076 /
999 021 090 076 / 999 021 090 076 at Ia4[117]/Ia5[28]/
Ia6[78]/Ia8[106]/Ia13[17]. Verify from fixtures; do not
invent sites. Line-initial / no previous-of-021 is a nested
fact (cycle 302 N_line_initial=0 so all five should have a
previous token). Claim that can lose:
i_021_090_076_previous_4grams_all_i_only. True iff every
leftover n=4 remaining previous-021 4-gram is I-only
(N_off_I==0, N_I>=1). Also lose if N leftover n=4 remaining
previous-021 != 5, if a site has no previous token so the
4-gram set is incomplete relative to N=5, or if extra I of
021 090 076 is no longer 0 (that would change the 4-gram
population). Hapax is recorded, not required. Measured:
N leftover=5, N_4grams=5, N_line_initial=0, extra I=0; four
distinct 4-grams 600 021 090 076 1/0 hapax, 007 021 090 076
1/0 hapax, 150 021 090 076 1/0 hapax, 999 021 090 076 2/0
not hapax; N_i_only=4 / N_hapax_i_only=3 / N_not_hapax=1 /
N_leak_off_i=0. The claim is true (I-only, not all hapax).
Nested leftover extra previous-999 overlap empty; leftover
extra remaining-after-000 extra I overlap Ia8[106] only;
remaining-after-011 overlap Ia8[106] and Ia13[17]; record,
do not fail I-only on it. Previous 4-grams 999 021 090 076
and 600 021 090 076 do not overlap leftover extra previous-
999 / remaining-after-999 previous-600 4-grams (different
4-grams: leftover extra was 999 090 076 / 600 090 076).
Nested leftover n=4 remaining 13 / 4 / 9 / 3 / 6 / 2 / 4 /
2 / 2, cycle 302 unique-max true G=021 K=5 N_distinct=8 N=13
N_line_initial=0, cycle 303 K_021=5, cycle 304 5/0 extra
I=0, cycle 288 unique-max true G=020 K=4 share-one lost,
cycle 301 090 076 607 073 1/0, cycle 224 13/56, and cycle
223 69/3 stay.

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
from tests.test_mamari_i_090_076_020_forward_4grams_i_only_scoreboard import (
    STANDING_HAPAX_EACH as CYCLE291_HAPAX_EACH,
    STANDING_I_090_076_020_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE291_CLAIM,
    STANDING_N_I_ONLY as CYCLE291_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE291_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE291_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE291_SEQUENCES,
    TestMamariI090076020Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_021_090_076_i_only_scoreboard import (
    GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE304_EXTRA_I_SITES,
    STANDING_I_3GRAM_021_090_076_I_ONLY as CYCLE304_CLAIM,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE304_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE304_I_SITES,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE304_LEFTOVER_MATCHING_SITES,
    STANDING_N_EXTRA as CYCLE304_N_EXTRA,
    STANDING_N_I as CYCLE304_N_I,
    STANDING_N_OFF_I as CYCLE304_N_OFF_I,
    extra_i_sites,
    leftover_n4_remaining_090_076_site_for_3gram,
    leftover_n4_remaining_previous_021_subset,
    named_off_i_sites as cycle304_named_off_i_sites,
    site_previous_4gram_for_3gram,
    TestMamariI3gram021090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_600_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE268_GRAM3,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
)
from tests.test_mamari_i_600_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_600_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE269_CLAIM,
    STANDING_N_I_ONLY as CYCLE269_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE269_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE269_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE269_SEQUENCES,
    TestMamariI600090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_999_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE263_CLAIM,
    STANDING_N_I_ONLY as CYCLE263_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE263_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE263_N_NOT_I_ONLY,
    TestMamariI999090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE261_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_600_scoreboard import (
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE267_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE267_MATCHING_SITES,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE288_N_DISTINCT,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_previous_021_scoreboard import (
    GRAM3_BACKWARD,
    STANDING_G as CYCLE303_G,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021 as CYCLE303_CLAIM,
    STANDING_K_021 as CYCLE303_K_021,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE303_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE303_MATCHING_SITES,
    STANDING_NESTED_LEFTOVER_N4_REMAINING as CYCLE303_NESTED,
    STANDING_N_REMAINING_AFTER_021 as CYCLE303_N_REMAINING_AFTER_021,
    STANDING_OVERLAP_CYCLE258_EXTRA_I as CYCLE303_OVERLAP_258,
    STANDING_OVERLAP_CYCLE259_EXTRA_I as CYCLE303_OVERLAP_259,
    STANDING_OVERLAP_CYCLE261_PREVIOUS_999 as CYCLE303_OVERLAP_261,
    STANDING_OVERLAP_REMAINING_AFTER_011 as CYCLE303_OVERLAP_AFTER_011,
    leftover_n4_remaining_with_previous_021,
    TestMamariILeftoverN4Remaining090076Previous021Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE302_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE302_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_UNIQUE_PREVIOUS_STEM as CYCLE302_CLAIM,
    STANDING_K as CYCLE302_K,
    STANDING_MATCHING_SITES as CYCLE302_MATCHING_SITES,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE302_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE302_N_INSIDE,
    STANDING_N_LINE_INITIAL as CYCLE302_N_LINE_INITIAL,
    leftover_n4_remaining_g_overlap_sites,
    leftover_n4_remaining_previous_4grams,
    leftover_n4_remaining_previous_stems,
    leftover_n4_remaining_sites_with_previous,
    leftover_n4_remaining_sites_without_previous,
    TestMamariILeftoverN4Remaining090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE301_CLAIM,
    STANDING_N_I_ONLY as CYCLE301_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE301_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE301_SEQUENCES,
    TestMamariILeftoverN4Remaining090076RemainingAfter011ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_next_stem_scoreboard import (
    leftover_n4_remaining_remaining_after_011_nested_counts_hold,
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
HYPOTHESIS_ALL_I_ONLY_HAPAX = False
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
NEAR_MISS_600_090_076 = CYCLE268_GRAM3
NEAR_MISS_999_090_076 = CYCLE167_GRAM3
NEAR_MISS_090_076 = GRAM2
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_N4_021_090_076_087 = ("021", "090", "076", "087")
STANDING_LEFTOVER_SITES_PREVIOUS_021 = CYCLE303_MATCHING_SITES
STANDING_N_LEFTOVER_PREVIOUS_021 = 5
STANDING_PER_SITE_PREVIOUS_4GRAMS = CYCLE303_MATCHING_PREVIOUS_4GRAMS
STANDING_CYCLE304_SITES = CYCLE304_I_SITES


def distinct_previous_4grams(
    grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, ...], ...]:
    """First-seen distinct previous 4-grams. None (line-initial) is skipped."""
    seen: list[tuple[str, ...]] = []
    for gram in grams:
        if gram is not None and gram not in seen:
            seen.append(gram)
    return tuple(seen)


STANDING_SEQUENCES = distinct_previous_4grams(STANDING_PER_SITE_PREVIOUS_4GRAMS)
STANDING_N_SEQUENCES = 4
STANDING_N_4GRAMS = 5
STANDING_N_WITH_PREVIOUS = 5
STANDING_N_LINE_INITIAL = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_NO_PREVIOUS_SITES = ()
STANDING_PREVIOUS_STEMS = tuple(gram[0] for gram in STANDING_SEQUENCES)
STANDING_N_I_EACH = (1, 1, 1, 2)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_SEQUENCES
STANDING_HAPAX_EACH = (True, True, True, False)
STANDING_I_ONLY_EACH = (True,) * STANDING_N_SEQUENCES
STANDING_I_SITES = (
    ((SIDE_IA, "Ia4", 115),),
    ((SIDE_IA, "Ia5", 26),),
    ((SIDE_IA, "Ia6", 76),),
    (
        (SIDE_IA, "Ia8", 104),
        (SIDE_IA, "Ia13", 15),
    ),
)
STANDING_CYCLE304_SITES_BY_GRAM = (
    ((SIDE_IA, "Ia4", 116),),
    ((SIDE_IA, "Ia5", 27),),
    ((SIDE_IA, "Ia6", 77),),
    (
        (SIDE_IA, "Ia8", 105),
        (SIDE_IA, "Ia13", 16),
    ),
)
STANDING_LEFTOVER_SITES_BY_GRAM = (
    ((SIDE_IA, "Ia4", 117),),
    ((SIDE_IA, "Ia5", 28),),
    ((SIDE_IA, "Ia6", 78),),
    (
        (SIDE_IA, "Ia8", 106),
        (SIDE_IA, "Ia13", 17),
    ),
)
STANDING_ROLES = (
    "leftover_n4_remaining_previous_021",
) * STANDING_N_SEQUENCES
STANDING_NOT_HAPAX_SEQUENCES = (("999", "021", "090", "076"),)
STANDING_NOT_HAPAX_I_SITES = (
    (SIDE_IA, "Ia8", 104),
    (SIDE_IA, "Ia13", 15),
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_OFF_I_SITES = ((),) * STANDING_N_SEQUENCES
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = (
    tuple(1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS),
    tuple(1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS),
    tuple(1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS),
    tuple(2 if tablet == "I" else 0 for tablet in VENDORED_TABLETS),
)
STANDING_N_I_ONLY = 4
STANDING_N_NOT_I_ONLY = 0
STANDING_N_HAPAX = 3
STANDING_N_HAPAX_I_ONLY = 3
STANDING_N_NOT_HAPAX = 1
STANDING_N_LEAK_OFF_I = 0
STANDING_N_I_ONLY_SITES = 5
STANDING_N_NOT_I_ONLY_SITES = 0
STANDING_N_HAPAX_SITES = 3
STANDING_N_NOT_HAPAX_SITES = 2
STANDING_LEAKING_4GRAMS = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_EXTRA_I_SITES = CYCLE304_EXTRA_I_SITES
STANDING_N_EXTRA = 0
STANDING_OVERLAP_CYCLE261_PREVIOUS_999 = CYCLE303_OVERLAP_261
STANDING_OVERLAP_CYCLE258_EXTRA_I = CYCLE303_OVERLAP_258
STANDING_OVERLAP_CYCLE259_EXTRA_I = CYCLE303_OVERLAP_259
STANDING_OVERLAP_REMAINING_AFTER_011 = CYCLE303_OVERLAP_AFTER_011
STANDING_OVERLAP_4GRAM_CYCLE261 = ()
STANDING_OVERLAP_4GRAM_CYCLE267 = ()
STANDING_OVERLAP_DOES_NOT_LOSE = True
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_NOT_REQUIRED = True
STANDING_CLAIM = "i_021_090_076_previous_4grams_all_i_only"
STANDING_I_021_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY = True
STANDING_I_021_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX = False
STANDING_RESULT = "i_021_090_076_previous_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE262_3GRAM = False
STANDING_SAME_AS_CYCLE263_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE268_3GRAM = False
STANDING_SAME_AS_CYCLE269_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE291_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE303 = False
STANDING_SAME_AS_CYCLE304 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE263 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE269 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE291 = True
STANDING_090_076_WITHOUT_021_DOES_NOT_COUNT = True
STANDING_600_090_076_DOES_NOT_COUNT = True
STANDING_999_090_076_DOES_NOT_COUNT = True
STANDING_090_076_020_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_021_090_076_087_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_W_999_090_076_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_W_600_090_076_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_DO_NOT_RELOCK_CYCLE262 = True
STANDING_DO_NOT_RELOCK_CYCLE263 = True
STANDING_DO_NOT_RELOCK_CYCLE268 = True
STANDING_DO_NOT_RELOCK_CYCLE269 = True
STANDING_DO_NOT_RELOCK_CYCLE304 = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_NOT_LOCKED = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE304_N_I = 5
STANDING_CYCLE304_N_OFF_I = 0
STANDING_CYCLE304_N_EXTRA = 0
STANDING_CYCLE303_K_021 = 5
STANDING_CYCLE303_G = "021"
STANDING_CYCLE302_N_DISTINCT = 8
STANDING_NESTED_LEFTOVER_N4_REMAINING = (13, 4, 9, 3, 6, 2, 4, 2, 2)


def previous_4gram_start_site(
    leftover_site: tuple[str, str, int],
) -> tuple[str, str, int] | None:
    """Previous 4-gram starts two tokens before leftover 090 076; None if no W."""
    side, line, index = leftover_site
    if index < 2:
        return None
    return (side, line, index - 2)


def leftover_n4_remaining_090_076_site_for_4gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """090 076 starts two tokens after the previous-4 start."""
    side, line, index = site
    return (side, line, index + 2)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def sequence_is_i_only_hapax(n_i: int, n_off_i: int) -> bool:
    """True iff N_I==1 and N_off_I=0."""
    return n_i == 1 and n_off_i == 0


def leaking_4grams(
    sequences: tuple[tuple[str, ...], ...],
    n_off_i: tuple[int, ...],
) -> tuple[tuple[str, ...], ...]:
    """Distinct previous 4-grams with N_off_I>0."""
    return tuple(
        gram
        for gram, off in zip(sequences, n_off_i, strict=True)
        if off > 0
    )


def previous_4grams_overlap(
    sequences: tuple[tuple[str, ...], ...],
    other: tuple[tuple[str, ...], ...],
) -> tuple[tuple[str, ...], ...]:
    """First-seen sequences that also sit in another previous-4 inventory."""
    other_set = set(other)
    return tuple(gram for gram in sequences if gram in other_set)


def i_021_090_076_previous_4grams_all_i_only(
    leftover_n: int,
    n_4grams: int,
    n_line_initial: int,
    n_extra: int,
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    per_site_previous: tuple[tuple[str, ...] | None, ...],
    expected_leftover: int = STANDING_N_LEFTOVER_PREVIOUS_021,
    expected_extra: int = STANDING_N_EXTRA,
) -> bool:
    """True iff leftover=5, every site has a previous 4-gram, extra I=0,
    and every distinct previous 4-gram is I-only.

    Hapax is not assumed; N_I may be greater than 1. Shared
    999 021 090 076 / N_I=2 does not make the claim lose.
    Line-initial leftover previous-021 (no previous token)
    makes the 4-gram set incomplete relative to N=5 and loses.
    Extra I of 021 090 076 != 0 loses (population change).
    """
    if leftover_n != expected_leftover:
        return False
    if n_4grams != expected_leftover:
        return False
    if n_line_initial != 0:
        return False
    if n_extra != expected_extra:
        return False
    if any(gram is None for gram in per_site_previous):
        return False
    if len(per_site_previous) != expected_leftover:
        return False
    if not n_i or len(n_i) != len(n_off_i):
        return False
    return all(
        sequence_is_i_only(on, off)
        for on, off in zip(n_i, n_off_i, strict=True)
    )


def i_sites_subset_of_previous_4gram(
    leftover_site: tuple[str, str, int],
    gram_i_sites: tuple[tuple[str, str, int], ...],
) -> bool:
    """True iff the leftover site's previous-4 start is among that 4-gram's I sites."""
    start = previous_4gram_start_site(leftover_site)
    if start is None:
        return False
    return start in gram_i_sites


def site_row_as_survey(row: dict) -> dict:
    """JSON-ready per-leftover-site row (lists, not tuples)."""
    return {
        "tablet": row["tablet"],
        "side": row["side"],
        "line": row["line"],
        "index": row["index"],
        "tokens4": list(row["tokens4"]),
        "cycle304_site": list(row["cycle304_site"]),
        "leftover_n4_remaining_090_076_site": list(
            row["leftover_n4_remaining_090_076_site"]
        ),
        "previous_stem": row["previous_stem"],
        "role": row["role"],
        "in_cycle303_leftover_n4_remaining_5": row[
            "in_cycle303_leftover_n4_remaining_5"
        ],
        "inside_leftover_extra": row["inside_leftover_extra"],
        "N_I": row["N_I"],
        "N_off_I": row["N_off_I"],
        "hapax": row["hapax"],
        "i_only": row["i_only"],
        "line_initial": row["line_initial"],
    }


def _n_i_for_gram(gram: tuple[str, ...]) -> int:
    """Locked N_I for one distinct previous 4-gram."""
    return STANDING_N_I_EACH[STANDING_SEQUENCES.index(gram)]


STANDING_SITE_ROWS = tuple(
    {
        "tablet": "I",
        "side": site[0],
        "line": site[1],
        "index": site[2] - 2,
        "tokens4": gram,
        "cycle304_site": (site[0], site[1], site[2] - 1),
        "leftover_n4_remaining_090_076_site": site,
        "previous_stem": gram[0],
        "role": "leftover_n4_remaining_previous_021",
        "in_cycle303_leftover_n4_remaining_5": True,
        "inside_leftover_extra": False,
        "N_I": _n_i_for_gram(gram),
        "N_off_I": 0,
        "hapax": _n_i_for_gram(gram) == 1,
        "i_only": True,
        "line_initial": False,
    }
    for site, gram in zip(
        STANDING_LEFTOVER_SITES_PREVIOUS_021,
        STANDING_PER_SITE_PREVIOUS_4GRAMS,
        strict=True,
    )
)


class TestI021090076Previous4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on leftover n=4 remaining previous-021 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 600 090 076 / 999 090 076 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("600", "021", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[1], ("007", "021", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[2], ("150", "021", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[3], ("999", "021", "090", "076"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_SEQUENCES)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_SEQUENCES)
        self.assertEqual(
            distinct_previous_4grams(STANDING_PER_SITE_PREVIOUS_4GRAMS),
            STANDING_SEQUENCES,
        )
        self.assertEqual(
            len(STANDING_PER_SITE_PREVIOUS_4GRAMS),
            STANDING_N_LEFTOVER_PREVIOUS_021,
        )
        self.assertEqual(STANDING_PER_SITE_PREVIOUS_4GRAMS.count(STANDING_SEQUENCES[3]), 2)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[1:], GRAM3)
            self.assertEqual(gram[1:], GRAM3_BACKWARD)
            self.assertEqual(gram[2:], GRAM2)
            self.assertEqual(len(gram), STANDING_N4)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["999", "021", "090", "076", "999", "021", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[3]), 2)
        gapped = [list(STANDING_SEQUENCES[0][:2]) + ["000"] + list(STANDING_SEQUENCES[0][2:])]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_600_090_076)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076)], STANDING_SEQUENCES[3]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_N4_021_090_076_087)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([["021", "090", "076"]], STANDING_SEQUENCES[0]), 0)
        planted = ["600", "021", "090", "076"]
        self.assertEqual(site_previous_4gram_for_3gram(planted, 1, GRAM3), STANDING_SEQUENCES[0])
        self.assertEqual(site_previous_4gram(planted, 2, GRAM2), STANDING_SEQUENCES[0])
        self.assertIsNone(site_previous_4gram_for_3gram(["021", "090", "076"], 0, GRAM3))
        self.assertIsNone(site_previous_4gram(["021", "090", "076"], 1, GRAM2))
        self.assertTrue(STANDING_090_076_WITHOUT_021_DOES_NOT_COUNT)
        self.assertTrue(STANDING_600_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_020_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_021_090_076_087_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_W_999_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_W_600_090_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_zero_off_i_complete_set_and_extra_i_0(self):
        """Boolean is True only when leftover=5, complete 4-grams, extra I=0, all I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        hold_prev = STANDING_PER_SITE_PREVIOUS_4GRAMS
        self.assertTrue(
            i_021_090_076_previous_4grams_all_i_only(
                5, 5, 0, 0, hold_ones, hold_zeros, hold_prev
            )
        )
        self.assertTrue(STANDING_HAPAX_NOT_REQUIRED)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertFalse(HYPOTHESIS_ALL_I_ONLY_HAPAX)
        self.assertEqual(STANDING_HAPAX_EACH, (True, True, True, False))
        self.assertEqual(STANDING_N_NOT_HAPAX, 1)
        self.assertEqual(STANDING_N_HAPAX_I_ONLY, 3)
        leak_off = (0, 0, 0, 1)
        self.assertFalse(
            i_021_090_076_previous_4grams_all_i_only(
                5, 5, 0, 0, hold_ones, leak_off, hold_prev
            )
        )
        self.assertFalse(
            i_021_090_076_previous_4grams_all_i_only(
                4, 4, 0, 0, hold_ones, hold_zeros, hold_prev[:-1]
            )
        )
        self.assertFalse(
            i_021_090_076_previous_4grams_all_i_only(
                5, 4, 1, 0, hold_ones, hold_zeros, hold_prev[:-1] + (None,)
            )
        )
        self.assertFalse(
            i_021_090_076_previous_4grams_all_i_only(
                5, 5, 0, 1, hold_ones, hold_zeros, hold_prev
            )
        )
        shared_ok = (1, 1, 1, 2)
        self.assertTrue(
            i_021_090_076_previous_4grams_all_i_only(
                5, 5, 0, 0, shared_ok, hold_zeros, hold_prev
            )
        )
        self.assertTrue(sequence_is_i_only(2, 0))
        self.assertFalse(sequence_is_i_only_hapax(2, 0))
        self.assertTrue(sequence_is_i_only_hapax(1, 0))
        self.assertFalse(sequence_is_i_only_hapax(1, 1))
        self.assertEqual(leaking_4grams(STANDING_SEQUENCES, hold_zeros), ())
        self.assertEqual(
            leaking_4grams(STANDING_SEQUENCES, leak_off),
            (STANDING_SEQUENCES[3],),
        )
        self.assertEqual(STANDING_CLAIM, "i_021_090_076_previous_4grams_all_i_only")
        self.assertTrue(STANDING_I_021_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY)
        self.assertFalse(STANDING_I_021_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_N_LEAK_OFF_I, 0)
        self.assertEqual(STANDING_N_NOT_I_ONLY, 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_303_leftover_not_retuned(self):
        """4-grams stay the cycle-303 leftover n=4 remaining previous-021 runs."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("021", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(STANDING_PER_SITE_PREVIOUS_4GRAMS, CYCLE303_MATCHING_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_PER_SITE_PREVIOUS_4GRAMS, CYCLE304_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_LEFTOVER_SITES_PREVIOUS_021, CYCLE303_MATCHING_SITES)
        self.assertEqual(STANDING_LEFTOVER_SITES_PREVIOUS_021, CYCLE304_LEFTOVER_MATCHING_SITES)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(STANDING_EXTRA_I_SITES, ())
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_600_090_076))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_999_090_076))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_090_076_070))
        for site, gram in zip(
            STANDING_LEFTOVER_SITES_PREVIOUS_021,
            STANDING_PER_SITE_PREVIOUS_4GRAMS,
            strict=True,
        ):
            start = previous_4gram_start_site(site)
            self.assertIsNotNone(start)
            self.assertEqual(start[2], site[2] - 2)
            self.assertEqual(leftover_n4_remaining_090_076_site_for_4gram(start), site)
            self.assertEqual(gram[1:], GRAM3)
        self.assertEqual(
            previous_4grams_overlap(STANDING_SEQUENCES, CYCLE261_MATCHING_PREVIOUS_4GRAMS),
            STANDING_OVERLAP_4GRAM_CYCLE261,
        )
        self.assertEqual(
            previous_4grams_overlap(STANDING_SEQUENCES, CYCLE267_MATCHING_PREVIOUS_4GRAMS),
            STANDING_OVERLAP_4GRAM_CYCLE267,
        )
        self.assertNotIn(("999", "021", "090", "076"), CYCLE261_MATCHING_PREVIOUS_4GRAMS)
        self.assertNotIn(("600", "021", "090", "076"), CYCLE267_MATCHING_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE262_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE263_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE268_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE269_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE291_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE303)
        self.assertFalse(STANDING_SAME_AS_CYCLE304)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE263)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE269)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE291)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE262)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE263)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE268)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE269)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE304)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_NOT_LOCKED)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI021090076Previous4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 remaining previous-021 previous-4 I-only lock."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES_PREVIOUS_021
        self.by_tablet = load_vendored_by_tablet()
        self.previous_stems = leftover_n4_remaining_previous_stems(
            self.i_sides,
            CYCLE224_INSIDE_SITES,
            GRAM2,
        )
        self.leftover_matching = leftover_n4_remaining_with_previous_021(
            CYCLE224_INSIDE_SITES,
            self.previous_stems,
        )
        self.per_site_previous = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.leftover_matching,
            GRAM2,
        )
        self.line_initial = leftover_n4_remaining_sites_without_previous(
            self.leftover_matching,
            leftover_n4_remaining_previous_stems(
                self.i_sides,
                self.leftover_matching,
                GRAM2,
            ),
        )
        self.with_previous = leftover_n4_remaining_sites_with_previous(
            self.leftover_matching,
            leftover_n4_remaining_previous_stems(
                self.i_sides,
                self.leftover_matching,
                GRAM2,
            ),
        )
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
            cycle304_named_off_i_sites(gram) for gram in self.grams
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if not sequence_is_i_only(on, off)
        )
        self.n_hapax_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only_hapax(on, off)
        )
        self.n_not_hapax = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off) and not sequence_is_i_only_hapax(on, off)
        )
        self.n_leak_off_i = sum(1 for off in self.n_off_i if off)
        self.leaking = leaking_4grams(self.grams, self.n_off_i)
        self.i_3gram_sites = nge4_sites(GRAM3, self.i_sides)
        self.extra = extra_i_sites(self.i_3gram_sites, self.leftover_matching)
        self.overlap_261 = leftover_n4_remaining_g_overlap_sites(
            self.leftover_matching,
            CYCLE261_MATCHING_SITES,
        )
        self.overlap_258 = leftover_n4_remaining_g_overlap_sites(
            self.leftover_matching,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_259 = leftover_n4_remaining_g_overlap_sites(
            self.leftover_matching,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_after_011 = leftover_n4_remaining_g_overlap_sites(
            self.leftover_matching,
            CYCLE303_OVERLAP_AFTER_011,
        )
        self.overlap_4gram_261 = previous_4grams_overlap(
            self.grams,
            CYCLE261_MATCHING_PREVIOUS_4GRAMS,
        )
        self.overlap_4gram_267 = previous_4grams_overlap(
            self.grams,
            CYCLE267_MATCHING_PREVIOUS_4GRAMS,
        )
        self.claim_holds = i_021_090_076_previous_4grams_all_i_only(
            len(self.leftover_matching),
            len(self.with_previous),
            len(self.line_initial),
            len(self.extra),
            self.n_i,
            self.n_off_i,
            self.per_site_previous,
        )

    def test_tokens_and_sites_are_cycle_303_leftover_not_retuned(self):
        """4-grams stay the cycle-303 leftover previous-021 lock; cycle 304 stays 5/0."""
        self.assertEqual(GRAM3, ("021", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_SITES_PREVIOUS_021)
        self.assertEqual(self.leftover_matching, CYCLE303_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE302_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_N_LEFTOVER_PREVIOUS_021)
        self.assertEqual(STANDING_N_LEFTOVER_PREVIOUS_021, 5)
        self.assertEqual(self.per_site_previous, STANDING_PER_SITE_PREVIOUS_4GRAMS)
        self.assertEqual(self.per_site_previous, CYCLE303_MATCHING_PREVIOUS_4GRAMS)
        self.assertEqual(self.per_site_previous, CYCLE304_PREVIOUS_4GRAMS)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(len(self.line_initial), STANDING_N_LINE_INITIAL)
        self.assertEqual(len(self.with_previous), STANDING_N_4GRAMS)
        self.assertEqual(STANDING_N_4GRAMS, 5)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        if len(self.leftover_matching) != 5:
            self.fail("leftover n=4 remaining previous-021 no longer computes as 5")
        if self.leftover_matching != CYCLE303_MATCHING_SITES:
            self.fail("leftover n=4 remaining previous-021 set drifted")
        if any(gram is None for gram in self.per_site_previous):
            self.fail("a leftover previous-021 site has no previous token")
        if len(self.extra) != 0:
            self.fail("extra I of 021 090 076 is no longer 0")
        prior_304 = self.survey["i_3gram_021_090_076_i_only"]
        self.assertEqual(prior_304["cycle"], 304)
        self.assertEqual(tuple(prior_304["tokens3"]), GRAM3)
        self.assertEqual(prior_304["N_I"], CYCLE304_N_I)
        self.assertEqual(prior_304["N_I"], 5)
        self.assertEqual(prior_304["N_off_I"], CYCLE304_N_OFF_I)
        self.assertEqual(prior_304["N_off_I"], 0)
        self.assertEqual(prior_304["N_extra"], CYCLE304_N_EXTRA)
        self.assertEqual(prior_304["N_extra"], 0)
        self.assertTrue(prior_304["i_3gram_021_090_076_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_304["i_sites"]),
            STANDING_CYCLE304_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS],
            prior_304["i_previous_4grams"],
        )
        prior_303 = self.survey["i_leftover_n4_remaining_090_076_previous_021"]
        self.assertEqual(prior_303["cycle"], 303)
        self.assertEqual(prior_303["K_021"], 5)
        self.assertEqual(prior_303["G"], "021")
        self.assertEqual(prior_303["N_remaining_after_021"], 8)
        self.assertTrue(prior_303["i_leftover_n4_remaining_090_076_exactly_5_share_previous_021"])
        prior_302 = self.survey["i_leftover_n4_remaining_090_076_previous_stem"]
        self.assertEqual(prior_302["cycle"], 302)
        self.assertEqual(prior_302["G"], "021")
        self.assertEqual(prior_302["K"], 5)
        self.assertEqual(prior_302["N_inside"], 13)
        self.assertEqual(prior_302["N_line_initial"], 0)
        self.assertEqual(prior_302["N_distinct_previous_stems"], 8)
        self.assertTrue(prior_302["G_uniquely_most_frequent"])
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertTrue(prior_288["g_uniquely_most_frequent"])
        self.assertFalse(prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        prior_301 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"
        ]
        self.assertEqual(prior_301["cycle"], 301)
        self.assertEqual(prior_301["N_i_only"], 1)
        self.assertEqual(prior_301["N_not_i_only"], 0)
        self.assertEqual(tuple(prior_301["extra_i_forward_4grams"][0]), CYCLE301_SEQUENCES[0])
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertTrue(
            leftover_n4_remaining_remaining_after_011_nested_counts_hold(
                13, 4, 9, 3, 6, 2, 4, 2, 2
            )
        )
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, (13, 4, 9, 3, 6, 2, 4, 2, 2))
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, CYCLE303_NESTED)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_HAPAX_NOT_REQUIRED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE262)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE263)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE268)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE269)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE304)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertEqual(CYCLE303_K_021, 5)
        self.assertEqual(CYCLE303_N_REMAINING_AFTER_021, 8)
        self.assertEqual(CYCLE302_N_DISTINCT, 8)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_all_4grams_are_i_only_not_all_hapax_and_claim_holds(self):
        """N_i_only=4 / N_hapax_i_only=3 / N_not_hapax=1 / N_leak_off_i=0. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_hapax_i_only, STANDING_N_HAPAX_I_ONLY)
        self.assertEqual(self.n_not_hapax, STANDING_N_NOT_HAPAX)
        self.assertEqual(self.n_leak_off_i, STANDING_N_LEAK_OFF_I)
        self.assertEqual(self.n_i_only, 4)
        self.assertEqual(self.n_hapax_i_only, 3)
        self.assertEqual(self.n_not_hapax, 1)
        self.assertEqual(self.n_leak_off_i, 0)
        self.assertEqual(self.n_not_i_only, 0)
        self.assertEqual(self.leaking, STANDING_LEAKING_4GRAMS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ())
        not_hapax = tuple(
            gram
            for gram, hapax in zip(STANDING_SEQUENCES, STANDING_HAPAX_EACH, strict=True)
            if not hapax
        )
        self.assertEqual(not_hapax, STANDING_NOT_HAPAX_SEQUENCES)
        self.assertEqual(not_hapax, (("999", "021", "090", "076"),))
        for site, gram in zip(
            STANDING_LEFTOVER_SITES_PREVIOUS_021,
            STANDING_PER_SITE_PREVIOUS_4GRAMS,
            strict=True,
        ):
            start = previous_4gram_start_site(site)
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(site_previous_4gram(stems, site[2], GRAM2), gram)
            self.assertEqual(site_previous_stem(stems, site[2], GRAM2), "021")
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(tuple(stems[site[2] - 1 : site[2] + STANDING_N2]), GRAM3)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N2]), GRAM2)
            gram_sites = STANDING_I_SITES[STANDING_SEQUENCES.index(gram)]
            self.assertTrue(i_sites_subset_of_previous_4gram(site, gram_sites))
            self.assertIn(start, gram_sites)
            self.assertIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertEqual(site[0], SIDE_IA)
        self.assertTrue(leftover_n4_remaining_previous_021_subset())
        self.assertEqual(self.i_3gram_sites, CYCLE304_I_SITES)
        self.assertEqual(len(self.extra), 0)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_NOT_REQUIRED)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off, n_on in zip(
            self.hits_by_tablet,
            self.off_i,
            STANDING_N_I_EACH,
            strict=True,
        ):
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
            self.assertEqual(sum(off), 0)
            self.assertEqual(hits[VENDORED_TABLETS.index("I")], n_on)
        for tablet, *counts in zip(VENDORED_TABLETS, *self.hits_by_tablet, strict=True):
            for count, gram, n_on in zip(counts, self.grams, STANDING_N_I_EACH, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                self.assertEqual(count, n_on if tablet == "I" else 0)
        for gram, off_sites in zip(self.grams, self.off_i_sites, strict=True):
            self.assertEqual(off_sites, ())
            unused = gram
            self.assertEqual(len(unused), 4)
        t_sides = load_t_sides()
        self.assertEqual(CYCLE223_OFF_I_SITES, (
            (SIDE_TA, "Ta5", 9),
            (SIDE_TA, "Ta7", 5),
            (SIDE_TA, "Ta9", 2),
        ))
        for site, following in zip(
            CYCLE223_OFF_I_SITES,
            CYCLE223_OFF_I_FOLLOWING_3GRAMS,
            strict=True,
        ):
            side, line, index = site
            stems = t_sides[side][TA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + 2]), GRAM2)
            self.assertEqual(tuple(stems[index : index + 3]), following)
            if index >= 2:
                self.assertNotIn(
                    tuple(stems[index - 2 : index + 2]),
                    STANDING_SEQUENCES,
                )
        self.assertTrue(self.claim_holds)
        self.assertEqual(
            self.claim_holds,
            STANDING_I_021_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY,
        )
        self.assertFalse(STANDING_I_021_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_021_090_076_previous_4grams_all_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE263)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE269)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE291)
        self.assertTrue(CYCLE291_CLAIM)
        self.assertEqual(CYCLE291_N_I_ONLY, 1)
        self.assertEqual(CYCLE291_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE291_N_NOT_HAPAX, 1)
        self.assertEqual(CYCLE291_HAPAX_EACH, (False,))
        self.assertEqual(CYCLE291_SEQUENCES, (("090", "076", "020", "010"),))
        self.assertTrue(CYCLE269_CLAIM)
        self.assertEqual(CYCLE269_N_I_ONLY, 6)
        self.assertEqual(CYCLE269_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE269_N_NOT_HAPAX, 0)
        self.assertFalse(CYCLE263_CLAIM)
        self.assertEqual(CYCLE263_N_I_ONLY, 14)
        self.assertEqual(CYCLE263_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE263_N_NOT_HAPAX, 2)
        not_hapax_sites = 0
        hapax_sites = 0
        for row in STANDING_SITE_ROWS:
            self.assertEqual(row["tablet"], "I")
            self.assertFalse(row["line_initial"])
            self.assertTrue(row["i_only"])
            self.assertEqual(row["N_off_I"], 0)
            self.assertTrue(row["in_cycle303_leftover_n4_remaining_5"])
            self.assertFalse(row["inside_leftover_extra"])
            if row["hapax"]:
                hapax_sites += 1
                self.assertEqual(row["N_I"], 1)
            else:
                not_hapax_sites += 1
                self.assertEqual(row["N_I"], 2)
        self.assertEqual(hapax_sites, STANDING_N_HAPAX_SITES)
        self.assertEqual(not_hapax_sites, STANDING_N_NOT_HAPAX_SITES)
        self.assertEqual(STANDING_N_HAPAX_SITES, 3)
        self.assertEqual(STANDING_N_NOT_HAPAX_SITES, 2)
        self.assertEqual(STANDING_N_I_ONLY_SITES, 5)
        self.assertEqual(STANDING_N_NOT_I_ONLY_SITES, 0)
        shared_rows = [row for row in STANDING_SITE_ROWS if not row["hapax"]]
        self.assertEqual(len(shared_rows), 2)
        self.assertEqual(shared_rows[0]["tokens4"], ("999", "021", "090", "076"))
        self.assertEqual(shared_rows[0]["leftover_n4_remaining_090_076_site"], (SIDE_IA, "Ia8", 106))
        self.assertEqual(shared_rows[1]["leftover_n4_remaining_090_076_site"], (SIDE_IA, "Ia13", 17))
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        for n_on, locked in zip(self.n_i, STANDING_N_I_EACH, strict=True):
            if n_on != locked:
                self.fail("measured N_I drifted from the locked count")
        if self.n_leak_off_i != 0:
            self.fail("measured N_leak_off_i drifted from 0")
        if not self.claim_holds:
            self.fail("I-only claim unexpectedly lost")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_overlap_recorded_and_4grams_do_not_overlap_leftover_extra(self):
        """Previous-021 sites overlap remaining-after-011 / 258; 4-grams do not match leftover extra."""
        self.assertEqual(self.overlap_261, STANDING_OVERLAP_CYCLE261_PREVIOUS_999)
        self.assertEqual(self.overlap_261, ())
        self.assertEqual(self.overlap_258, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_258, ((SIDE_IA, "Ia8", 106),))
        self.assertEqual(self.overlap_after_011, STANDING_OVERLAP_REMAINING_AFTER_011)
        self.assertEqual(
            self.overlap_after_011,
            ((SIDE_IA, "Ia8", 106), (SIDE_IA, "Ia13", 17)),
        )
        self.assertEqual(self.overlap_4gram_261, STANDING_OVERLAP_4GRAM_CYCLE261)
        self.assertEqual(self.overlap_4gram_267, STANDING_OVERLAP_4GRAM_CYCLE267)
        self.assertEqual(self.overlap_4gram_261, ())
        self.assertEqual(self.overlap_4gram_267, ())
        for gram in CYCLE261_MATCHING_PREVIOUS_4GRAMS:
            self.assertEqual(gram[1:], ("999", "090", "076"))
            self.assertNotIn(gram, STANDING_SEQUENCES)
        for gram in CYCLE267_MATCHING_PREVIOUS_4GRAMS:
            self.assertEqual(gram[1:], ("600", "090", "076"))
            self.assertNotIn(gram, STANDING_SEQUENCES)
        for gram in CYCLE269_SEQUENCES:
            self.assertNotIn(gram, STANDING_SEQUENCES)
        for site in CYCLE261_MATCHING_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES_PREVIOUS_021)
        for site in CYCLE267_MATCHING_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES_PREVIOUS_021)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(self.claim_holds)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_304_303_302_301_291_288_269_263_224_223_still_compute(self):
        """Cycle 304 5/0 extra I=0, 303 K_021=5, 302 unique-max, 301 1/0, 291 4/0 not hapax, 288 G=020 K=4, 269 6/0 hapax, 263 14/0 N_not_hapax=2, 224 13/56, 223 69/3 stay."""
        prior_304 = TestMamariI3gram021090076IOnlyScoreboard()
        prior_304.setUp()
        prior_304.test_i_hits_are_five_on_ia_and_leftover_n4_remaining_021_is_subset()
        prior_304.test_3gram_is_zero_off_i_and_i_only()
        prior_304.test_survey_matches_computed_lock()
        self.assertEqual(prior_304.i_hits, 5)
        self.assertEqual(prior_304.off_i_hits, 0)
        self.assertEqual(len(prior_304.extra), 0)
        self.assertTrue(prior_304.claim_holds)
        self.assertTrue(CYCLE304_CLAIM)
        self.assertEqual(CYCLE304_N_I, 5)
        self.assertEqual(CYCLE304_N_OFF_I, 0)
        self.assertEqual(CYCLE304_N_EXTRA, 0)
        if prior_304.i_hits != 5 or prior_304.off_i_hits != 0 or len(prior_304.extra) != 0:
            self.fail("nested cycle 304 021 090 076 I-only 5/0 extra I=0 drifted")
        prior_303 = TestMamariILeftoverN4Remaining090076Previous021Scoreboard()
        prior_303.setUp()
        prior_303.test_counts_5_of_13_and_hypothesis_k_5_holds()
        prior_303.test_survey_matches_computed_lock()
        self.assertEqual(prior_303.k_021, 5)
        self.assertEqual(CYCLE303_G, "021")
        self.assertEqual(prior_303.n_remaining_after_021, 8)
        self.assertEqual(prior_303.matching, CYCLE303_MATCHING_SITES)
        self.assertTrue(prior_303.claim_holds)
        self.assertTrue(CYCLE303_CLAIM)
        if prior_303.k_021 != 5 or CYCLE303_G != "021" or prior_303.n_remaining_after_021 != 8:
            self.fail("nested cycle 303 leftover n=4 remaining previous-021 K_021=5 drifted")
        prior_302 = TestMamariILeftoverN4Remaining090076PreviousStemScoreboard()
        prior_302.setUp()
        prior_302.test_counts_8_distinct_previous_stems_g_021_k_5_and_claim_holds()
        prior_302.test_survey_matches_computed_lock()
        self.assertEqual(prior_302.g, "021")
        self.assertEqual(prior_302.k, 5)
        self.assertEqual(prior_302.n_inside, 13)
        self.assertEqual(prior_302.n_line_initial, 0)
        self.assertEqual(prior_302.n_distinct, 8)
        self.assertTrue(prior_302.unique)
        self.assertTrue(prior_302.claim_holds)
        self.assertTrue(CYCLE302_CLAIM)
        self.assertEqual(CYCLE302_G, "021")
        self.assertEqual(CYCLE302_K, 5)
        self.assertEqual(CYCLE302_N_INSIDE, 13)
        self.assertEqual(CYCLE302_N_LINE_INITIAL, 0)
        self.assertEqual(CYCLE302_N_DISTINCT, 8)
        self.assertTrue(CYCLE302_UNIQUE)
        if (
            prior_302.g != "021"
            or prior_302.k != 5
            or prior_302.n_inside != 13
            or prior_302.n_line_initial != 0
            or prior_302.n_distinct != 8
            or not prior_302.unique
        ):
            self.fail(
                "nested cycle 302 unique-max G=021 K=5 N=13 distinct=8 drifted"
            )
        prior_301 = TestMamariILeftoverN4Remaining090076RemainingAfter011ExtraIFwd4IOnlyScoreboard()
        prior_301.setUp()
        prior_301.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_301.test_survey_matches_computed_lock()
        self.assertEqual(prior_301.n_i_only, 1)
        self.assertEqual(prior_301.n_not_i_only, 0)
        self.assertTrue(prior_301.claim_holds)
        self.assertTrue(CYCLE301_CLAIM)
        self.assertEqual(CYCLE301_N_I_ONLY, 1)
        self.assertEqual(CYCLE301_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE301_SEQUENCES[0], ("090", "076", "607", "073"))
        if prior_301.n_i_only != 1 or prior_301.n_not_i_only != 0:
            self.fail("nested cycle 301 extra-I 4-gram 090 076 607 073 1/0 drifted")
        prior_291 = TestMamariI090076020Forward4gramsIOnlyScoreboard()
        prior_291.setUp()
        prior_291.test_each_4gram_is_four_on_i_zero_off_i_and_claim_holds()
        prior_291.test_survey_matches_computed_lock()
        self.assertEqual(prior_291.n_i_only, 1)
        self.assertEqual(prior_291.n_not_i_only, 0)
        self.assertTrue(prior_291.claim_holds)
        self.assertTrue(CYCLE291_CLAIM)
        self.assertEqual(CYCLE291_N_I_ONLY, 1)
        self.assertEqual(CYCLE291_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE291_N_NOT_HAPAX, 1)
        if prior_291.n_i_only != 1 or prior_291.n_not_i_only != 0 or not prior_291.claim_holds:
            self.fail("nested cycle 291 090 076 020 forward 4-grams 4/0 not hapax drifted")
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.n_distinct, 6)
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        if (
            prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or not prior_288.unique_max
        ):
            self.fail("nested cycle 288 leftover n=4 remaining G=020 K=4 unique-max drifted")
        prior_269 = TestMamariI600090076Previous4gramsIOnlyScoreboard()
        prior_269.setUp()
        prior_269.test_all_4grams_are_i_only_hapax_and_claim_holds()
        prior_269.test_survey_matches_computed_lock()
        self.assertEqual(prior_269.n_i_only, 6)
        self.assertEqual(prior_269.n_not_i_only, 0)
        self.assertEqual(prior_269.n_not_hapax, 0)
        self.assertTrue(prior_269.claim_holds)
        self.assertTrue(CYCLE269_CLAIM)
        self.assertEqual(CYCLE269_N_I_ONLY, 6)
        self.assertEqual(CYCLE269_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE269_N_NOT_HAPAX, 0)
        if (
            prior_269.n_i_only != 6
            or prior_269.n_not_i_only != 0
            or prior_269.n_not_hapax != 0
            or not prior_269.claim_holds
        ):
            self.fail("nested cycle 269 600 090 076 previous 4-grams 6/0 N_not_hapax=0 drifted")
        prior_263 = TestMamariI999090076Previous4gramsIOnlyScoreboard()
        prior_263.setUp()
        prior_263.test_shared_4grams_are_i_only_not_hapax_and_claim_loses()
        prior_263.test_survey_matches_computed_lock()
        self.assertEqual(prior_263.n_i_only, 14)
        self.assertEqual(prior_263.n_not_i_only, 0)
        self.assertEqual(prior_263.n_not_hapax, 2)
        self.assertFalse(prior_263.claim_holds)
        self.assertFalse(CYCLE263_CLAIM)
        self.assertEqual(CYCLE263_N_I_ONLY, 14)
        self.assertEqual(CYCLE263_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE263_N_NOT_HAPAX, 2)
        if (
            prior_263.n_i_only != 14
            or prior_263.n_not_i_only != 0
            or prior_263.n_not_hapax != 2
            or prior_263.claim_holds
        ):
            self.fail("nested cycle 263 999 090 076 previous 4-grams 14/0 N_not_hapax=2 drifted")
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
        if prior_224.n_inside != 13 or prior_224.n_leftover != 56:
            self.fail("nested cycle 224 13/56 drifted")
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
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertFalse(prior_207.claim_holds)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        self.assertEqual(STANDING_CYCLE302_N_DISTINCT, 8)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE262)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE263)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE268)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE269)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE304)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_021_NOT_LOCKED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-305 leftover n=4 remaining previous-021 4-gram I-only lock."""
        lock = self.survey["i_021_090_076_previous_4grams_i_only"]
        self.assertEqual(lock["cycle"], 305)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertFalse(lock["hypothesis_all_i_only_hapax"])
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover_n4_remaining_previous_021"], STANDING_N_LEFTOVER_PREVIOUS_021)
        self.assertEqual(lock["N_leftover_n4_remaining_previous_021"], 5)
        self.assertEqual(lock["N_4grams"], STANDING_N_4GRAMS)
        self.assertEqual(lock["N_4grams"], 5)
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["line_initial_sites"], [])
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(lock["N_I_3gram"], CYCLE304_N_I)
        self.assertEqual(lock["N_I_3gram"], 5)
        self.assertEqual(lock["N_off_I_3gram"], CYCLE304_N_OFF_I)
        self.assertEqual(lock["N_off_I_3gram"], 0)
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_remaining_previous_021_sites"]),
            STANDING_LEFTOVER_SITES_PREVIOUS_021,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle304_sites"]),
            STANDING_CYCLE304_SITES,
        )
        self.assertEqual(lock["extra_i_sites"], [])
        self.assertEqual(lock["N_distinct_4grams"], STANDING_N_SEQUENCES)
        self.assertEqual(lock["N_distinct_4grams"], 4)
        self.assertTrue(lock["not_assumed_hapax"])
        self.assertTrue(lock["hapax_not_required"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), 4)
        for row, gram, sites, cycle_sites, leftover_sites, prev, role, n_on, n_off, hapax, off_sites, hits in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_I_SITES,
            STANDING_CYCLE304_SITES_BY_GRAM,
            STANDING_LEFTOVER_SITES_BY_GRAM,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_HAPAX_EACH,
            STANDING_OFF_I_SITES,
            STANDING_HITS_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["cycle304_sites"]), cycle_sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["leftover_n4_remaining_090_076_sites"]),
                leftover_sites,
            )
            self.assertEqual(row["previous_stem"], prev)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["ia_hits"], n_on)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(row["ib_sites"], [])
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual([list(site_row) for site_row in off_sites], row["off_i_sites"])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(tuple(row["hits_by_tablet"]), hits)
            self.assertTrue(row["i_only"])
            self.assertEqual(row["hapax"], hapax)
        self.assertEqual(
            [site_row_as_survey(row) for row in STANDING_SITE_ROWS],
            lock["site_rows"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS],
            lock["per_site_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["distinct_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_NOT_HAPAX_SEQUENCES],
            lock["not_hapax_4grams"],
        )
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_hapax_i_only"], STANDING_N_HAPAX_I_ONLY)
        self.assertEqual(lock["N_not_hapax"], STANDING_N_NOT_HAPAX)
        self.assertEqual(lock["N_leak_off_i"], STANDING_N_LEAK_OFF_I)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_i_only"], 4)
        self.assertEqual(lock["N_hapax_i_only"], 3)
        self.assertEqual(lock["N_not_hapax"], 1)
        self.assertEqual(lock["N_leak_off_i"], 0)
        self.assertEqual(lock["N_i_only_sites"], STANDING_N_I_ONLY_SITES)
        self.assertEqual(lock["N_not_i_only_sites"], STANDING_N_NOT_I_ONLY_SITES)
        self.assertEqual(lock["N_hapax_sites"], STANDING_N_HAPAX_SITES)
        self.assertEqual(lock["N_not_hapax_sites"], STANDING_N_NOT_HAPAX_SITES)
        self.assertEqual(lock["N_i_only_sites"], 5)
        self.assertEqual(lock["N_not_hapax_sites"], 2)
        self.assertEqual(lock["overlap_cycle261_previous_999_sites"], [])
        self.assertEqual(
            [list(site) for site in CYCLE303_OVERLAP_258],
            lock["overlap_cycle258_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in CYCLE303_OVERLAP_259],
            lock["overlap_cycle259_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in CYCLE303_OVERLAP_AFTER_011],
            lock["overlap_remaining_after_011_sites"],
        )
        self.assertEqual(lock["overlap_4gram_cycle261_previous_999"], [])
        self.assertEqual(lock["overlap_4gram_cycle267_remaining_after_999_previous_600"], [])
        self.assertTrue(lock["overlap_does_not_lose"])
        self.assertEqual(
            list(STANDING_NESTED_LEFTOVER_N4_REMAINING),
            lock["nested_leftover_n4_remaining"],
        )
        self.assertEqual(lock["nested_cycle304_N_I"], 5)
        self.assertEqual(lock["nested_cycle304_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle304_N_extra"], 0)
        self.assertEqual(lock["nested_cycle303_G"], "021")
        self.assertEqual(lock["nested_cycle303_K_021"], 5)
        self.assertEqual(lock["nested_cycle303_N_remaining_after_021"], 8)
        self.assertEqual(lock["nested_cycle302_G"], "021")
        self.assertEqual(lock["nested_cycle302_K"], 5)
        self.assertEqual(lock["nested_cycle302_N_inside"], 13)
        self.assertEqual(lock["nested_cycle302_N_line_initial"], 0)
        self.assertEqual(lock["nested_cycle302_N_distinct_previous_stems"], 8)
        self.assertTrue(lock["nested_cycle302_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle301_N_i_only"], 1)
        self.assertEqual(lock["nested_cycle301_N_not_i_only"], 0)
        self.assertEqual(
            tuple(lock["nested_cycle301_extra_i_4gram"]),
            ("090", "076", "607", "073"),
        )
        self.assertEqual(lock["nested_cycle291_N_i_only"], 1)
        self.assertEqual(lock["nested_cycle291_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle291_N_not_hapax"], 1)
        self.assertTrue(lock["nested_cycle291_all_i_only"])
        self.assertEqual(lock["nested_cycle288_N_distinct_next_stems"], 6)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertFalse(lock["nested_cycle288_share_one_forward_stem"])
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle269_N_i_only"], 6)
        self.assertEqual(lock["nested_cycle269_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle269_N_not_hapax"], 0)
        self.assertTrue(lock["nested_cycle269_all_i_only_hapax"])
        self.assertEqual(lock["nested_cycle263_N_i_only"], 14)
        self.assertEqual(lock["nested_cycle263_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle263_N_not_hapax"], 2)
        self.assertFalse(lock["nested_cycle263_all_i_only_hapax"])
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_021_090_076_previous_4grams_all_i_only"])
        self.assertFalse(lock["i_021_090_076_previous_4grams_all_i_only_hapax"])
        self.assertEqual(
            lock["i_021_090_076_previous_4grams_all_i_only"],
            STANDING_I_021_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle262_3gram"])
        self.assertFalse(lock["same_as_cycle263_previous_4grams"])
        self.assertFalse(lock["same_as_cycle268_3gram"])
        self.assertFalse(lock["same_as_cycle269_previous_4grams"])
        self.assertFalse(lock["same_as_cycle291_forward_4grams"])
        self.assertFalse(lock["same_as_cycle303"])
        self.assertFalse(lock["same_as_cycle304"])
        self.assertTrue(lock["same_claim_shape_as_cycle263"])
        self.assertTrue(lock["same_claim_shape_as_cycle269"])
        self.assertTrue(lock["same_claim_shape_as_cycle291"])
        self.assertTrue(lock["090_076_without_021_does_not_count"])
        self.assertTrue(lock["600_090_076_does_not_count"])
        self.assertTrue(lock["999_090_076_does_not_count"])
        self.assertTrue(lock["090_076_020_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["leftover_n4_021_090_076_087_does_not_count"])
        self.assertTrue(lock["leftover_extra_w_999_090_076_does_not_count"])
        self.assertTrue(lock["leftover_extra_w_600_090_076_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["do_not_relock_cycle262"])
        self.assertTrue(lock["do_not_relock_cycle263"])
        self.assertTrue(lock["do_not_relock_cycle268"])
        self.assertTrue(lock["do_not_relock_cycle269"])
        self.assertTrue(lock["do_not_relock_cycle304"])
        self.assertTrue(lock["leftover_n4_remaining_remaining_after_021_not_locked"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_021_kept"])
        self.assertTrue(lock["standing_i_3gram_021_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_previous_021_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_previous_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_020_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_600_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_999_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_021_090_076_i_only"]["cycle"], 304)
        self.assertTrue(self.survey["i_3gram_021_090_076_i_only"]["i_3gram_021_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_021_090_076_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_3gram_021_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_021_090_076_i_only"]["N_extra"], 0)
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_021"]["cycle"],
            303,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_021"]["K_021"],
            5,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_stem"]["cycle"],
            302,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_stem"]["G"],
            "021",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_stem"]["K"],
            5,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"][
                "cycle"
            ],
            301,
        )
        self.assertEqual(self.survey["i_090_076_020_forward_4grams_i_only"]["cycle"], 291)
        self.assertTrue(
            self.survey["i_090_076_020_forward_4grams_i_only"][
                "i_090_076_020_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"], 288)
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"][
                "i_leftover_n4_remaining_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(self.survey["i_600_090_076_previous_4grams_i_only"]["cycle"], 269)
        self.assertTrue(
            self.survey["i_600_090_076_previous_4grams_i_only"][
                "i_600_090_076_previous_4grams_all_i_only_hapax"
            ]
        )
        self.assertEqual(self.survey["i_999_090_076_previous_4grams_i_only"]["cycle"], 263)
        self.assertFalse(
            self.survey["i_999_090_076_previous_4grams_i_only"][
                "i_999_090_076_previous_4grams_all_i_only_hapax"
            ]
        )
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"], 13)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI021090076Previous4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 305 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
