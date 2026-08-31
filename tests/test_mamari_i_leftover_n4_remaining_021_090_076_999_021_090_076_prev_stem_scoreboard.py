"""I's leftover n=4 remaining 021 090 076 4-gram 999 021 090 076
previous-stem lock.

Cycle 319 text-search lock. Uses already-vendored A–V and the
cycle-305 leftover n=4 remaining previous-021 4-grams I-only
not-hapax pair of 999 021 090 076 (Ia8[106] and Ia13[17]; 090
at the named index). Does not retune leftover n=4 remaining
previous-021 4-grams I-only (cycle 305 holds: N_i_only=4 /
N_hapax_i_only=3 / N_not_hapax=1 / N_leak=0; 600/007/150 hapax
1/0; 999 021 090 076 2/0 not hapax), 3-gram 021 090 076 I-only
(cycle 304 holds: 5/0 extra I=0), leftover n=4 remaining
exactly 5 share previous 021 (cycle 303 holds), leftover n=4
remaining unique previous stem (cycle 302 holds: G=021 K=5),
leftover n=4 remaining remaining-after-011 (cycles 298–301),
leftover extra remaining-after-000 extra I (cycles 258/259),
leftover n=4 remaining remaining-after-600 (cycles 308–318),
or leftover n=4 remaining remaining-after-021 unique previous
G=600 K=2 (cycles 306–307; a different population, not
previous-021). Does not vendor a new tablet. Does not scrape
X. W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Population (locked, do not re-derive as a new claim): leftover
n=4 remaining I 090 076 sites that share previous 021 (cycle
303 HOLD): Ia4[117], Ia5[28], Ia6[78], Ia8[106], Ia13[17].
3-gram 021 090 076 I-only 5/0 extra I=0 (cycle 304). Those
sites' previous 4-grams are all I-only (cycle 305 HOLD):
600/007/150 hapax 1/0; 999 021 090 076 2/0 not hapax at
Ia8[106] and Ia13[17]. This cycle's N=2 population is exactly
those two not-hapax sites: Ia8[106] and Ia13[17], previous
4-gram 999 021 090 076 (090 at the named index). Unique-max
previous stem = the token immediately before 999.

Already locked on these same two sites (do not re-lock; record
overlap only): forward leftover n=4 remaining remaining-after-
011 (cycles 298–301): Ia8[106] 090 076 607 755, Ia13[17]
090 076 021 020; 3-grams I-only extra I=1 of 090 076 607;
extra-I 4-gram 090 076 607 073 at Ia7[137]. Ia8[106] overlaps
leftover extra remaining-after-000 extra I (cycles 258/259).
Leftover n=4 remaining remaining-after-600 is exhausted both
directions (cycles 308–318). Cycle 318 HOLD: extra I of
090 076 057 is 1 at Ia9[129], extra-I 4-gram 090 076 057 240
I-only hapax 1/0. Leftover n=4 remaining remaining-after-021
unique previous G=600 K=2 (cycles 306–307) is a different
population (not previous-021).

Analog: cycle 302 leftover n=4 remaining I 090 076 unique
previous stem; cycle 306 leftover n=4 remaining remaining-
after-021 unique previous stem; cycle 308 leftover n=4
remaining remaining-after-600 unique previous stem (LOSE,
6-way hapax). Same claim-shape as those unique-max previous-
stem locks; leftover n=4 remaining 021 090 076 4-gram
999 021 090 076 previous-of-999 instead of those populations.

For each of the two not-hapax 999 021 090 076 sites, take the
token immediately before 999 if any (lock line-initial / no-
previous count separately). Line-initial / no previous token
is N_line_initial, not a stem. Nested-check leftover n=4
remaining N_inside==13, N_line_initial==0, K_021==5,
N_remaining_after_021==8, cycle 305 N_i_only==4 N_hapax==3
N_not_hapax==1 N_leak==0, cycle 304 5/0 extra I=0 (do not
retune 224/288/302/303/304/305). Nested leftover n=4 remaining
13 / 4 / 9 / 3 / 6 / 2 / 4 / 2 / 2 still computes (do not
retune 288–297). Count previous-of-999 frequencies among the
N=2 sites that have a previous token. G = the previous stem
with the highest with-previous count. If a tie, pick the
larger Barthel id. K = that count.

Claim that can lose:
i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem.
True iff unique_max is true (one previous stem strictly
outcounts every other among the N=2 sites that have a
previous token) and N==2 and both previous 4-grams are
999 021 090 076. LOSE on a tie or hapax pile (unique_max
false). Empty remainder does not lose HOLD. Unique-max G/K
is inventory for a later peel if the claim holds or loses
with K≥2. Measured: N=2, N_with_previous=2,
N_line_initial=0, N_distinct=2, unique-max false, G=720
K=1 (2-way hapax 720×1 at Ia8[106], 076×1 at Ia13[17]),
N_remaining after peeling G=1. Previous 5-grams
720 999 021 090 076 and 076 999 021 090 076. The claim is
false. Nested leftover-extra / remaining-after-011 overlap:
remaining-after-011 exact equality Ia8[106]/Ia13[17]; leftover
extra remaining-after-000 extra I overlap Ia8[106] only;
record, do not fail unique-max on it. Nested cycle 305
4-grams I-only N_not_hapax=1, cycle 304 5/0 extra I=0, cycle
303 K_021=5, cycle 302 unique-max true G=021 K=5 N_distinct=8
N=13 N_line_initial=0, cycle 301 090 076 607 073 1/0, cycle
308 unique-max previous false G=999 K=1 N_distinct=6, cycle
306 unique-max G=600 K=2, cycle 318 extra I of 090 076 057
1/0 at Ia9[129], cycle 288 unique-max false G=020 K=4, cycle
224 13/56, and cycle 223 69/3 stay. Do not assume the result;
measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_021_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_021_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY as CYCLE305_CLAIM,
    STANDING_N_HAPAX_I_ONLY as CYCLE305_N_HAPAX,
    STANDING_N_I_ONLY as CYCLE305_N_I_ONLY,
    STANDING_N_LEAK_OFF_I as CYCLE305_N_LEAK,
    STANDING_N_NOT_HAPAX as CYCLE305_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE305_N_NOT_I_ONLY,
    STANDING_NOT_HAPAX_I_SITES as CYCLE305_NOT_HAPAX_I_SITES,
    STANDING_NOT_HAPAX_SEQUENCES as CYCLE305_NOT_HAPAX_SEQUENCES,
    TestMamariI021090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_I as CYCLE224_N_I,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
    leftover_local_4grams,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_OFF_I,
    STANDING_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_021_090_076_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE304_EXTRA_I_SITES,
    STANDING_I_3GRAM_021_090_076_I_ONLY as CYCLE304_CLAIM,
    STANDING_N_EXTRA as CYCLE304_N_EXTRA,
    STANDING_N_I as CYCLE304_N_I,
    STANDING_N_OFF_I as CYCLE304_N_OFF_I,
    TestMamariI3gram021090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    group_sites_by_previous_stem,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999 as CYCLE261_CLAIM,
    STANDING_K_999 as CYCLE261_K_999,
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_999 as CYCLE261_N_REMAINING_AFTER_999,
    TestMamariILeftoverExtra090076Previous999Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    leftover_sites_with_previous,
    leftover_sites_without_previous,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_N_I_ONLY as CYCLE259_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE259_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE288_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE288_N_INSIDE,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_previous_021_scoreboard import (
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
    STANDING_K_011,
    STANDING_K_020,
    STANDING_K_057,
    STANDING_K_087,
    STANDING_N_REMAINING_AFTER_011,
    STANDING_N_REMAINING_AFTER_020,
    STANDING_N_REMAINING_AFTER_057,
    STANDING_N_REMAINING_AFTER_087,
    leftover_n4_remaining_remaining_after_011_nested_counts_hold,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_021_previous_600_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_EXACTLY_2_SHARE_PREVIOUS_600 as CYCLE307_CLAIM,
    STANDING_K_600 as CYCLE307_K_600,
    STANDING_MATCHING_SITES as CYCLE307_MATCHING_SITES,
    TestMamariILeftoverN4Remaining090076RemainingAfter021Previous600Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem_scoreboard import (
    STANDING_G as CYCLE306_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE306_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM as CYCLE306_CLAIM,
    STANDING_K as CYCLE306_K,
    STANDING_N_DISTINCT as CYCLE306_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_021 as CYCLE306_N_REMAINING,
    TestMamariILeftoverN4Remaining090076RemainingAfter021PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_057_forward_011_scoreboard import (
    STANDING_REMAINING_AFTER_011_SITES as CYCLE297_REMAINING_AFTER_011_SITES,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem_scoreboard import (
    STANDING_G as CYCLE308_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE308_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE308_CLAIM,
    STANDING_K as CYCLE308_K,
    STANDING_N_DISTINCT as CYCLE308_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_600 as CYCLE308_N_REMAINING,
    TestMamariILeftoverN4Remaining090076RemainingAfter600PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_600_remaining_after_020_extra_i_fwd4_090_076_057_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_600_REMAINING_AFTER_020_EXTRA_I_FWD4_090_076_057_ALL_I_ONLY as CYCLE318_CLAIM,
    TestMamariILeftoverN4Remaining090076RemainingAfter600RemainingAfter020ExtraIFwd4090076057IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    barthel_id,
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
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

LOCKED_PREVIOUS_4GRAM = ("999", "021", "090", "076")
LOCKED_PREVIOUS_STEM_021 = "021"
GRAM4_PREV = LOCKED_PREVIOUS_4GRAM
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N5 = 5
GRAM3_BACKWARD = ("021", "090", "076")
GRAM5_PREV_G = ("720", "999", "021", "090", "076")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS_INSIDE = 13
STANDING_N_LINE_INITIAL_INSIDE = 0
STANDING_K_021 = 5
STANDING_N_REMAINING_AFTER_021 = 8
STANDING_N_NOT_HAPAX_4GRAM = 1
STANDING_N = 2
STANDING_N_WITH_PREVIOUS = 2
STANDING_N_LINE_INITIAL = 0
STANDING_N_NO_PREVIOUS = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_NO_PREVIOUS_SITES = ()
STANDING_N_DISTINCT = 2
STANDING_N_HAPAX = 2
STANDING_G = "720"
STANDING_K = 1
STANDING_N_WITHOUT_G = 1
STANDING_N_TIED_AT_K = 2
STANDING_TIED_STEMS = ("720", "076")
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_SITES = (
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia13", 17),
)
STANDING_PREVIOUS_STEMS = (
    "720",
    "076",
)
STANDING_PREVIOUS_4GRAMS = (
    ("999", "021", "090", "076"),
    ("999", "021", "090", "076"),
)
STANDING_PREVIOUS_5GRAMS = (
    ("720", "999", "021", "090", "076"),
    ("076", "999", "021", "090", "076"),
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia8", 106),
)
STANDING_MATCHING_PREVIOUS_5GRAMS = (
    ("720", "999", "021", "090", "076"),
)
STANDING_REMAINING_AFTER_G_SITES = (
    (SIDE_IA, "Ia13", 17),
)
STANDING_REMAINING_AFTER_G_PREVIOUS_5GRAMS = (
    ("076", "999", "021", "090", "076"),
)
STANDING_FREQUENCY = (
    (
        "720",
        1,
        ((SIDE_IA, "Ia8", 106),),
        (("720", "999", "021", "090", "076"),),
    ),
    (
        "076",
        1,
        ((SIDE_IA, "Ia13", 17),),
        (("076", "999", "021", "090", "076"),),
    ),
)
STANDING_OVERLAP_CYCLE261_PREVIOUS_999 = ()
STANDING_OVERLAP_CYCLE258_EXTRA_I = ((SIDE_IA, "Ia8", 106),)
STANDING_OVERLAP_CYCLE259_EXTRA_I = ((SIDE_IA, "Ia8", 106),)
STANDING_OVERLAP_REMAINING_AFTER_011 = (
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia13", 17),
)
STANDING_OVERLAP_REMAINING_AFTER_011_EQUALS_POPULATION = True
STANDING_OVERLAP_CYCLE306_G_600 = ()
STANDING_OVERLAP_CYCLE307_PREVIOUS_600 = ()
STANDING_OVERLAP_CYCLE308_REMAINING_AFTER_600 = ()
STANDING_OVERLAP_CYCLE318_EXTRA_I = ()
STANDING_OVERLAP_DOES_NOT_LOSE = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem"
)
STANDING_I_LEFTOVER_N4_REMAINING_021_090_076_999_021_090_076_UNIQUE_PREVIOUS_STEM = False
STANDING_RESULT = "i_leftover_n4_remaining_021_090_076_999_021_090_076_prev_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE302 = False
STANDING_SAME_AS_CYCLE303 = False
STANDING_SAME_AS_CYCLE304 = False
STANDING_SAME_AS_CYCLE305 = False
STANDING_SAME_AS_CYCLE306 = False
STANDING_SAME_AS_CYCLE307 = False
STANDING_SAME_AS_CYCLE308 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE302 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE306 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE308 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_DO_NOT_RELOCK_CYCLE305 = True
STANDING_DO_NOT_RELOCK_CYCLE304 = True
STANDING_DO_NOT_RELOCK_CYCLES_302_303 = True
STANDING_DO_NOT_RELOCK_CYCLES_298_301 = True
STANDING_DO_NOT_RELOCK_CYCLES_258_259 = True
STANDING_DO_NOT_RELOCK_CYCLES_308_318 = True
STANDING_CYCLE305_4GRAMS_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE304_3GRAM_IS_NOT_THIS_CYCLE = True
STANDING_CYCLE306_REMAINING_AFTER_021_IS_NOT_THIS_POPULATION = True
STANDING_CYCLE308_REMAINING_AFTER_600_IS_NOT_THIS_POPULATION = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_PREVIOUS_999_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_UNIQUE_PREVIOUS_STEM_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_4GRAMS_IS_NOT_THIS_CYCLE = True
STANDING_3GRAM_021_090_076_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL = True
STANDING_EMPTY_REMAINDER_DOES_NOT_LOSE = True
STANDING_NESTED_LEFTOVER_N4_REMAINING = (13, 4, 9, 3, 6, 2, 4, 2, 2)


def site_previous_of_999_stem(
    stems: list[str],
    index: int,
    gram4: tuple[str, ...] = LOCKED_PREVIOUS_4GRAM,
    gram2: tuple[str, ...] = GRAM2,
) -> str | None:
    """Token immediately before 999 in 999 021 090 076; None if missing."""
    if tuple(stems[index : index + len(gram2)]) != gram2:
        return None
    if index < 2:
        return None
    if tuple(stems[index - 2 : index + len(gram2)]) != gram4:
        return None
    if index < 3:
        return None
    return stems[index - 3]


def site_previous_5gram(
    stems: list[str],
    index: int,
    gram4: tuple[str, ...] = LOCKED_PREVIOUS_4GRAM,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str, ...] | None:
    """Previous 5-gram <prev> 999 021 090 076; None if missing."""
    prev = site_previous_of_999_stem(stems, index, gram4, gram2)
    if prev is None:
        return None
    return (prev,) + gram4


def leftover_n4_remaining_999_021_090_076_sites(
    sites: tuple[tuple[str, str, int], ...],
    previous_4grams: tuple[tuple[str, ...] | None, ...],
    gram4: tuple[str, ...] = LOCKED_PREVIOUS_4GRAM,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining I 090 076 sites whose previous 4-gram is 999 021 090 076."""
    return tuple(
        site
        for site, prev4 in zip(sites, previous_4grams, strict=True)
        if prev4 == gram4
    )


def leftover_n4_remaining_999_021_090_076_previous_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_SITES,
    gram4: tuple[str, ...] = LOCKED_PREVIOUS_4GRAM,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str | None, ...]:
    """Per-site token immediately before 999, or None if line-initial."""
    return tuple(
        site_previous_of_999_stem(
            line_stems_for_site(i_sides, site), site[2], gram4, gram2
        )
        for site in sites
    )


def leftover_n4_remaining_999_021_090_076_previous_5grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_SITES,
    gram4: tuple[str, ...] = LOCKED_PREVIOUS_4GRAM,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site previous 5-gram or None for the locked N=2 sites."""
    return tuple(
        site_previous_5gram(line_stems_for_site(i_sides, site), site[2], gram4, gram2)
        for site in sites
    )


def leftover_n4_remaining_999_021_090_076_with_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """N=2 999 021 090 076 sites that have a token before 999."""
    return leftover_sites_with_previous(sites, previous_stems)


def leftover_n4_remaining_999_021_090_076_without_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """N=2 999 021 090 076 sites with no token before 999."""
    return leftover_sites_without_previous(sites, previous_stems)


def leftover_n4_remaining_999_021_090_076_with_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """N=2 sites whose token before 999 is G."""
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev == stem
    )


def leftover_n4_remaining_999_021_090_076_without_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """N=2 sites whose token before 999 is not G (includes line-initial)."""
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev != stem
    )


def remaining_999_021_090_076_previous_stem_counts(
    previous_stems: tuple[str, ...],
) -> Counter:
    """Counts of previous-of-999 stems among N=2 with-previous sites."""
    return Counter(previous_stems)


def rank_999_021_090_076_previous_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Previous-of-999 stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_999_021_090_076_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty with-previous has no G."""
    ranked = rank_999_021_090_076_previous_stems(
        remaining_999_021_090_076_previous_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_999_021_090_076_previous_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    previous_5grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Previous-of-999 frequency: highest count first, then larger id."""
    with_prev = leftover_n4_remaining_999_021_090_076_with_previous(
        sites, previous_stems
    )
    stems = tuple(prev for prev in previous_stems if prev is not None)
    grams = tuple(gram for gram in previous_5grams if gram is not None)
    first_seen = group_sites_by_previous_stem(with_prev, stems)
    grams_by_stem: dict[str, list[tuple[str, ...]]] = {
        stem: [] for stem, _ in first_seen
    }
    for prev, gram in zip(stems, grams, strict=True):
        grams_by_stem[prev].append(gram)
    rows = tuple(
        (stem, len(stem_sites), stem_sites, tuple(grams_by_stem[stem]))
        for stem, stem_sites in first_seen
    )
    return tuple(sorted(rows, key=lambda row: (-row[1], -barthel_id(row[0]))))


def remaining_999_021_090_076_previous_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_FREQUENCY,
) -> list[dict]:
    """Survey-shaped previous-of-999 frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "previous_stem": stem,
                "count": count,
                "leftover_n4_remaining_021_090_076_999_021_090_076_sites": [
                    list(site) for site in sites
                ],
                "previous_5grams": [list(gram) for gram in grams],
            }
        )
    return rows


def matching_leftover_n4_remaining_999_021_090_076_local_5gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    previous_5grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_PREVIOUS_5GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover n=4 remaining 999 021 090 076 previous-5-gram rows."""
    rows = []
    for (side, line, index), prev_gram in zip(
        leftover_sites,
        previous_5grams,
        strict=True,
    ):
        rows.append(
            {
                "tablet": "I",
                "side": side,
                "line": line,
                "index": index,
                "previous_5gram": list(prev_gram),
                "previous_4gram": list(prev_gram[1:]),
            }
        )
    return rows


def leftover_n4_remaining_999_021_090_076_nested_counts_hold(
    n_inside: int,
    n_line_initial_inside: int,
    k_021: int,
    n_remaining: int,
    n_not_hapax: int,
    n_population: int,
    expected_inside: int = STANDING_N_INSIDE,
    expected_line_initial_inside: int = STANDING_N_LINE_INITIAL_INSIDE,
    expected_k_021: int = STANDING_K_021,
    expected_remaining: int = STANDING_N_REMAINING_AFTER_021,
    expected_not_hapax: int = STANDING_N_NOT_HAPAX_4GRAM,
    expected_population: int = STANDING_N,
) -> bool:
    """Nested leftover n=4 remaining 13/0/5/8 plus cycle-305 not-hapax N=2."""
    return (
        n_inside == expected_inside
        and n_line_initial_inside == expected_line_initial_inside
        and k_021 == expected_k_021
        and n_remaining == expected_remaining
        and n_remaining == n_inside - k_021
        and n_not_hapax == expected_not_hapax
        and n_population == expected_population
        and n_line_initial_inside == 0
    )


def i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    previous_4grams: tuple[tuple[str, ...] | None, ...],
    gram4: tuple[str, ...] = LOCKED_PREVIOUS_4GRAM,
    expected_n: int = STANDING_N,
) -> bool:
    """True iff N=2 999 021 090 076 sites have a unique most frequent previous-of-999."""
    if sites != STANDING_SITES:
        return False
    if len(sites) != expected_n:
        return False
    if any(prev4 != gram4 for prev4 in previous_4grams):
        return False
    with_prev = leftover_n4_remaining_999_021_090_076_with_previous(
        sites, previous_stems
    )
    stems = tuple(prev for prev in previous_stems if prev is not None)
    if len(with_prev) != len(stems):
        return False
    gram, count, unique = select_999_021_090_076_g(stems)
    return bool(unique and gram is not None and count >= 2)


class TestILeftoverN4Remaining021090076999021090076PrevStemHelpers(unittest.TestCase):
    """Helpers on leftover n=4 remaining 999 021 090 076 previous-of-999. No CV, no LLM."""

    def test_previous_of_999_requires_999_021_090_076(self):
        """Previous-of-999 is the token before 999; line-initial is no-previous."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("021", "090", "076"))
        self.assertEqual(LOCKED_PREVIOUS_4GRAM, ("999", "021", "090", "076"))
        self.assertEqual(GRAM5_PREV_G, ("720", "999", "021", "090", "076"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(len(LOCKED_PREVIOUS_4GRAM), STANDING_N4)
        self.assertEqual(len(GRAM5_PREV_G), STANDING_N5)
        has_720 = ["720", "999", "021", "090", "076"]
        self.assertEqual(site_previous_stem(has_720, 3, GRAM2), "021")
        self.assertEqual(site_previous_4gram(has_720, 3, GRAM2), LOCKED_PREVIOUS_4GRAM)
        self.assertEqual(site_previous_of_999_stem(has_720, 3), "720")
        self.assertEqual(site_previous_5gram(has_720, 3), GRAM5_PREV_G)
        has_076 = ["076", "999", "021", "090", "076"]
        self.assertEqual(site_previous_of_999_stem(has_076, 3), "076")
        self.assertEqual(
            site_previous_5gram(has_076, 3),
            ("076", "999", "021", "090", "076"),
        )
        no_prev = ["999", "021", "090", "076"]
        self.assertEqual(site_previous_4gram(no_prev, 2, GRAM2), LOCKED_PREVIOUS_4GRAM)
        self.assertIsNone(site_previous_of_999_stem(no_prev, 2))
        self.assertIsNone(site_previous_5gram(no_prev, 2))
        not_999 = ["600", "021", "090", "076"]
        self.assertEqual(site_previous_stem(not_999, 2, GRAM2), "021")
        self.assertIsNone(site_previous_of_999_stem(not_999, 2))
        mismatch_071 = ["720", "999", "021", "076", "071"]
        self.assertIsNone(site_previous_of_999_stem(mismatch_071, 3))
        planted_sites = (
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 8),
            (SIDE_IA, "Ia1", 13),
        )
        planted_stems = ("720", None, "076")
        self.assertEqual(
            leftover_n4_remaining_999_021_090_076_with_previous(
                planted_sites, planted_stems
            ),
            (planted_sites[0], planted_sites[2]),
        )
        self.assertEqual(
            leftover_n4_remaining_999_021_090_076_without_previous(
                planted_sites, planted_stems
            ),
            (planted_sites[1],),
        )
        self.assertEqual(
            leftover_n4_remaining_999_021_090_076_with_g(planted_sites, planted_stems),
            (planted_sites[0],),
        )
        self.assertEqual(
            leftover_n4_remaining_999_021_090_076_without_g(planted_sites, planted_stems),
            (planted_sites[1], planted_sites[2]),
        )
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE305_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_CYCLE304_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_can_fail(self):
        """Boolean is True only when N=2 and some G has unique K≥2."""
        provider = MockProvider()
        sites = STANDING_SITES
        i_sides = load_i_sides()
        stems = leftover_n4_remaining_999_021_090_076_previous_stems(i_sides, sites)
        prev4 = leftover_n4_remaining_previous_4grams(i_sides, sites, GRAM2)
        self.assertFalse(
            i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem(
                sites,
                stems,
                prev4,
            )
        )
        self.assertEqual(stems, STANDING_PREVIOUS_STEMS)
        self.assertEqual(prev4, STANDING_PREVIOUS_4GRAMS)
        g, k, unique = select_999_021_090_076_g(tuple(s for s in stems if s is not None))
        self.assertEqual(g, "720")
        self.assertEqual(k, 1)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        hold_stems = ("720", "720")
        hold_g, hold_k, hold_unique = select_999_021_090_076_g(hold_stems)
        self.assertEqual(hold_g, "720")
        self.assertEqual(hold_k, 2)
        self.assertTrue(hold_unique)
        self.assertTrue(
            i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem(
                sites,
                hold_stems,
                prev4,
            )
        )
        empty_stems = (None, None)
        self.assertFalse(
            i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem(
                sites,
                empty_stems,
                prev4,
            )
        )
        wrong_4 = (("600", "021", "090", "076"), LOCKED_PREVIOUS_4GRAM)
        self.assertFalse(
            i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem(
                sites,
                hold_stems,
                wrong_4,
            )
        )
        wrong_n = (sites[0],)
        self.assertFalse(
            i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem(
                wrong_n,
                ("720",),
                (LOCKED_PREVIOUS_4GRAM,),
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem",
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_021_090_076_999_021_090_076_UNIQUE_PREVIOUS_STEM
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N)
        self.assertEqual(1 + 1, 2)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_EMPTY_REMAINDER_DOES_NOT_LOSE)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal previous-of-999 counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"720": 1, "076": 1})
        ranked = rank_999_021_090_076_previous_stems(counts)
        self.assertEqual(ranked[0], ("720", 1))
        self.assertEqual(ranked[1], ("076", 1))
        self.assertEqual(select_999_021_090_076_g(("720", "076"))[0], "720")
        self.assertFalse(select_999_021_090_076_g(("720", "076"))[2])
        self.assertEqual(select_999_021_090_076_g(("720", "720"))[0], "720")
        self.assertTrue(select_999_021_090_076_g(("720", "720"))[2])
        self.assertEqual(select_999_021_090_076_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE302)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE306)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE308)
        self.assertFalse(STANDING_SAME_AS_CYCLE302)
        self.assertFalse(STANDING_SAME_AS_CYCLE306)
        self.assertFalse(STANDING_SAME_AS_CYCLE308)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining021090076999021090076PrevStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining 999 021 090 076 previous-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.inside_sites = STANDING_INSIDE_SITES
        self.inside_previous_4grams = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.inside_previous_stems = leftover_n4_remaining_previous_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.share_021 = leftover_n4_remaining_with_previous_021(
            self.inside_sites,
            self.inside_previous_stems,
        )
        self.sites = leftover_n4_remaining_999_021_090_076_sites(
            self.inside_sites,
            self.inside_previous_4grams,
        )
        self.previous_stems = leftover_n4_remaining_999_021_090_076_previous_stems(
            self.i_sides,
            self.sites,
        )
        self.previous_4grams = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.sites,
            GRAM2,
        )
        self.previous_5grams = leftover_n4_remaining_999_021_090_076_previous_5grams(
            self.i_sides,
            self.sites,
        )
        self.with_previous = leftover_n4_remaining_999_021_090_076_with_previous(
            self.sites,
            self.previous_stems,
        )
        self.line_initial = leftover_n4_remaining_999_021_090_076_without_previous(
            self.sites,
            self.previous_stems,
        )
        self.matching = leftover_n4_remaining_999_021_090_076_with_g(
            self.sites,
            self.previous_stems,
        )
        self.without = leftover_n4_remaining_999_021_090_076_without_g(
            self.sites,
            self.previous_stems,
        )
        self.frequency = remaining_999_021_090_076_previous_stem_frequency_table(
            self.sites,
            self.previous_stems,
            self.previous_5grams,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover_extra = len(STANDING_LEFTOVER_SITES)
        self.n_with_previous_inside = len(
            leftover_n4_remaining_sites_with_previous(
                self.inside_sites,
                self.inside_previous_stems,
            )
        )
        self.n_line_initial_inside = len(
            leftover_n4_remaining_sites_without_previous(
                self.inside_sites,
                self.inside_previous_stems,
            )
        )
        self.k_021 = len(self.share_021)
        self.n = len(self.sites)
        self.n_with_previous = len(self.with_previous)
        self.n_line_initial = len(self.line_initial)
        self.n_distinct = len(self.frequency)
        self.g, self.k, self.unique = select_999_021_090_076_g(
            tuple(prev for prev in self.previous_stems if prev is not None)
        )
        self.n_without = len(self.without)
        self.overlap_261 = leftover_n4_remaining_g_overlap_sites(
            self.sites,
            CYCLE261_MATCHING_SITES,
        )
        self.overlap_258 = leftover_n4_remaining_g_overlap_sites(
            self.sites,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_259 = leftover_n4_remaining_g_overlap_sites(
            self.sites,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_after_011 = leftover_n4_remaining_g_overlap_sites(
            self.sites,
            CYCLE297_REMAINING_AFTER_011_SITES,
        )
        self.overlap_306 = leftover_n4_remaining_g_overlap_sites(
            self.sites,
            CYCLE307_MATCHING_SITES,
        )
        self.claim_holds = (
            i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem(
                self.sites,
                self.previous_stems,
                self.previous_4grams,
            )
        )

    def test_tokens_and_nested_leftover_n4_remaining_13_5_8_not_retuned(self):
        """2-gram and leftover n=4 remaining 13/0/5/8 stay the cycle-303/302/224 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("021", "090", "076"))
        self.assertEqual(LOCKED_PREVIOUS_4GRAM, ("999", "021", "090", "076"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(len(STANDING_INSIDE_SITES), STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE224_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE288_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE302_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_318 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_600_remaining_after_020_extra_i_fwd4_090_076_057_i_only"
        ]
        self.assertEqual(prior_318["cycle"], 318)
        self.assertTrue(
            prior_318[
                "i_leftover_n4_remaining_090_076_remaining_after_600_remaining_after_020_extra_i_fwd4_090_076_057_all_i_only"
            ]
        )
        self.assertTrue(CYCLE318_CLAIM)
        prior_308 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem"
        ]
        self.assertEqual(prior_308["cycle"], 308)
        self.assertEqual(prior_308["G"], "999")
        self.assertEqual(prior_308["K"], 1)
        self.assertFalse(prior_308["G_uniquely_most_frequent"])
        self.assertFalse(CYCLE308_CLAIM)
        self.assertEqual(CYCLE308_G, "999")
        self.assertEqual(CYCLE308_K, 1)
        self.assertEqual(CYCLE308_N_DISTINCT, 6)
        self.assertFalse(CYCLE308_UNIQUE)
        prior_306 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem"
        ]
        self.assertEqual(prior_306["cycle"], 306)
        self.assertEqual(prior_306["G"], "600")
        self.assertEqual(prior_306["K"], 2)
        self.assertTrue(prior_306["G_uniquely_most_frequent"])
        self.assertTrue(CYCLE306_CLAIM)
        self.assertEqual(CYCLE306_G, "600")
        self.assertEqual(CYCLE306_K, 2)
        self.assertEqual(CYCLE306_N_DISTINCT, 7)
        self.assertTrue(CYCLE306_UNIQUE)
        prior_305 = self.survey["i_021_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_305["cycle"], 305)
        self.assertEqual(prior_305["N_i_only"], 4)
        self.assertEqual(prior_305["N_hapax_i_only"], 3)
        self.assertEqual(prior_305["N_not_hapax"], 1)
        self.assertEqual(prior_305["N_not_i_only"], 0)
        self.assertTrue(prior_305["i_021_090_076_previous_4grams_all_i_only"])
        self.assertTrue(CYCLE305_CLAIM)
        self.assertEqual(CYCLE305_N_I_ONLY, 4)
        self.assertEqual(CYCLE305_N_HAPAX, 3)
        self.assertEqual(CYCLE305_N_NOT_HAPAX, 1)
        self.assertEqual(CYCLE305_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE305_N_LEAK, 0)
        self.assertEqual(CYCLE305_NOT_HAPAX_SEQUENCES, (LOCKED_PREVIOUS_4GRAM,))
        prior_304 = self.survey["i_3gram_021_090_076_i_only"]
        self.assertEqual(prior_304["cycle"], 304)
        self.assertEqual(prior_304["N_I"], 5)
        self.assertEqual(prior_304["N_off_I"], 0)
        self.assertEqual(prior_304["N_extra"], 0)
        self.assertTrue(prior_304["i_3gram_021_090_076_i_only"])
        self.assertTrue(CYCLE304_CLAIM)
        self.assertEqual(CYCLE304_N_I, 5)
        self.assertEqual(CYCLE304_N_OFF_I, 0)
        self.assertEqual(CYCLE304_N_EXTRA, 0)
        prior_303 = self.survey["i_leftover_n4_remaining_090_076_previous_021"]
        self.assertEqual(prior_303["cycle"], 303)
        self.assertEqual(prior_303["K_021"], 5)
        self.assertEqual(prior_303["N_remaining_after_021"], 8)
        self.assertTrue(
            prior_303["i_leftover_n4_remaining_090_076_exactly_5_share_previous_021"]
        )
        self.assertTrue(CYCLE303_CLAIM)
        self.assertEqual(CYCLE303_G, "021")
        self.assertEqual(CYCLE303_K_021, 5)
        self.assertEqual(CYCLE303_N_REMAINING_AFTER_021, 8)
        prior_302 = self.survey["i_leftover_n4_remaining_090_076_previous_stem"]
        self.assertEqual(prior_302["cycle"], 302)
        self.assertEqual(prior_302["G"], "021")
        self.assertEqual(prior_302["K"], 5)
        self.assertEqual(prior_302["N_inside"], 13)
        self.assertEqual(prior_302["N_line_initial"], 0)
        self.assertEqual(prior_302["N_distinct_previous_stems"], 8)
        self.assertTrue(prior_302["G_uniquely_most_frequent"])
        self.assertTrue(prior_302["i_leftover_n4_remaining_090_076_unique_previous_stem"])
        self.assertTrue(CYCLE302_CLAIM)
        self.assertEqual(CYCLE302_G, "021")
        self.assertEqual(CYCLE302_K, 5)
        self.assertEqual(CYCLE302_N_INSIDE, 13)
        self.assertEqual(CYCLE302_N_LINE_INITIAL, 0)
        self.assertEqual(CYCLE302_N_DISTINCT, 8)
        self.assertTrue(CYCLE302_UNIQUE)
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertTrue(prior_288["g_uniquely_most_frequent"])
        self.assertFalse(prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        prior_301 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"
        ]
        self.assertEqual(prior_301["cycle"], 301)
        self.assertEqual(prior_301["N_i_only"], 1)
        self.assertEqual(prior_301["N_not_i_only"], 0)
        self.assertEqual(tuple(prior_301["extra_i_forward_4grams"][0]), CYCLE301_SEQUENCES[0])
        self.assertEqual(CYCLE301_SEQUENCES[0], ("090", "076", "607", "073"))
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_I"], 69)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(prior_224["i_090_076_all_inside_leftover_n4_remaining_family"])
        self.assertFalse(CYCLE224_ALL_INSIDE)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertTrue(
            leftover_n4_remaining_remaining_after_011_nested_counts_hold(
                13, 4, 9, 3, 6, 2, 4, 2, 2
            )
        )
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, (13, 4, 9, 3, 6, 2, 4, 2, 2))
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, CYCLE303_NESTED)
        self.assertEqual(STANDING_K_020, 4)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(STANDING_K_087, 3)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(STANDING_K_057, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, 4)
        self.assertEqual(STANDING_K_011, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_011, 2)
        unused_224_n = CYCLE224_N_I
        self.assertEqual(unused_224_n, 69)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE305)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE304)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLES_302_303)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLES_298_301)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLES_258_259)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLES_308_318)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE306_REMAINING_AFTER_021_IS_NOT_THIS_POPULATION)
        self.assertTrue(STANDING_CYCLE308_REMAINING_AFTER_600_IS_NOT_THIS_POPULATION)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_2_sites_g_720_k_1_two_way_hapax_and_hypothesis_loses(self):
        """N=2, N_line_initial=0, N_distinct=2, G=720 K=1 unique-max false. Claim loses."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_previous_inside, STANDING_N_WITH_PREVIOUS_INSIDE)
        self.assertEqual(STANDING_N_WITH_PREVIOUS_INSIDE, 13)
        self.assertEqual(self.n_line_initial_inside, STANDING_N_LINE_INITIAL_INSIDE)
        self.assertEqual(STANDING_N_LINE_INITIAL_INSIDE, CYCLE302_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_LINE_INITIAL_INSIDE, 0)
        self.assertEqual(self.k_021, STANDING_K_021)
        self.assertEqual(STANDING_K_021, CYCLE303_K_021)
        self.assertEqual(STANDING_K_021, 5)
        self.assertEqual(self.share_021, CYCLE303_MATCHING_SITES)
        self.assertTrue(
            leftover_n4_remaining_999_021_090_076_nested_counts_hold(
                self.n_inside,
                self.n_line_initial_inside,
                self.k_021,
                STANDING_N_REMAINING_AFTER_021,
                CYCLE305_N_NOT_HAPAX,
                self.n,
            )
        )
        self.assertEqual(self.n, STANDING_N)
        self.assertEqual(STANDING_N, 2)
        if self.n != 2:
            self.fail("measured N of 999 021 090 076 leftover n=4 remaining drifted from 2")
        self.assertEqual(self.sites, STANDING_SITES)
        self.assertEqual(self.sites, CYCLE303_OVERLAP_AFTER_011)
        self.assertEqual(self.sites, CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertEqual(self.previous_stems, STANDING_PREVIOUS_STEMS)
        self.assertEqual(self.previous_4grams, STANDING_PREVIOUS_4GRAMS)
        self.assertEqual(self.previous_5grams, STANDING_PREVIOUS_5GRAMS)
        self.assertEqual(len(self.sites), len(self.previous_stems))
        for prev4 in self.previous_4grams:
            self.assertEqual(prev4, LOCKED_PREVIOUS_4GRAM)
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 2)
        self.assertEqual(self.n_line_initial, STANDING_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertEqual(self.n_line_initial, STANDING_N_NO_PREVIOUS)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertEqual(self.n_with_previous + self.n_line_initial, self.n)
        self.assertEqual(2 + 0, 2)
        for site in self.sites:
            self.assertIn(site, CYCLE303_MATCHING_SITES)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE307_MATCHING_SITES)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT)
        self.assertEqual(STANDING_N_DISTINCT, 2)
        self.assertEqual(self.frequency, STANDING_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "720")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 1)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "720")
        self.assertEqual(self.frequency[0][1], 1)
        self.assertEqual(self.frequency[1][0], "076")
        self.assertEqual(self.frequency[1][1], 1)
        self.assertEqual(self.frequency[0][1], self.frequency[1][1])
        tied = tuple(stem for stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(tied, STANDING_TIED_STEMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 2)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX)
        self.assertEqual(STANDING_N_HAPAX, 2)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 1)
        self.assertEqual(self.k + self.n_without, self.n)
        self.assertEqual(1 + 1, 2)
        self.assertFalse(
            i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem(
                self.sites,
                self.previous_stems,
                self.previous_4grams,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_021_090_076_999_021_090_076_UNIQUE_PREVIOUS_STEM,
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_021_090_076_999_021_090_076_UNIQUE_PREVIOUS_STEM
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.without, STANDING_REMAINING_AFTER_G_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE302)
        self.assertFalse(STANDING_SAME_AS_CYCLE303)
        self.assertFalse(STANDING_SAME_AS_CYCLE304)
        self.assertFalse(STANDING_SAME_AS_CYCLE305)
        self.assertFalse(STANDING_SAME_AS_CYCLE306)
        self.assertFalse(STANDING_SAME_AS_CYCLE307)
        self.assertFalse(STANDING_SAME_AS_CYCLE308)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE302)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE306)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE308)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_CYCLE305_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_CYCLE304_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL)
        self.assertTrue(CYCLE302_CLAIM)
        self.assertTrue(CYCLE303_CLAIM)
        self.assertTrue(CYCLE304_CLAIM)
        self.assertTrue(CYCLE305_CLAIM)
        self.assertTrue(CYCLE306_CLAIM)
        self.assertTrue(CYCLE307_CLAIM)
        self.assertFalse(CYCLE308_CLAIM)
        self.assertTrue(CYCLE318_CLAIM)
        self.assertEqual(CYCLE306_G, "600")
        self.assertEqual(CYCLE306_K, 2)
        self.assertEqual(CYCLE306_N_REMAINING, 8)
        self.assertEqual(CYCLE306_N_DISTINCT, 7)
        self.assertTrue(CYCLE306_UNIQUE)
        self.assertEqual(CYCLE307_K_600, 2)
        self.assertEqual(CYCLE308_G, "999")
        self.assertEqual(CYCLE308_K, 1)
        self.assertEqual(CYCLE308_N_REMAINING, 6)
        self.assertEqual(CYCLE308_N_DISTINCT, 6)
        self.assertFalse(CYCLE308_UNIQUE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_sites_and_previous_5grams_from_fixtures(self):
        """Ia8[106] is 720 999 021 090 076; Ia13[17] is 076 999 021 090 076."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        expected = tuple(
            zip(STANDING_SITES, STANDING_PREVIOUS_5GRAMS, strict=True)
        )
        for (site, prev5), (want_site, want_prev) in zip(
            zip(self.sites, self.previous_5grams, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N2]), GRAM3_BACKWARD)
            self.assertEqual(stems[index - 1], "021")
            self.assertEqual(stems[index - 2], "999")
            self.assertEqual(site_previous_stem(stems, index, GRAM2), "021")
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), LOCKED_PREVIOUS_4GRAM)
            self.assertEqual(site_previous_of_999_stem(stems, index), want_prev[0])
            self.assertEqual(site_previous_5gram(stems, index), want_prev)
            self.assertEqual(prev5, want_prev)
            self.assertEqual(site, want_site)
            self.assertEqual(prev5[1:], LOCKED_PREVIOUS_4GRAM)
            self.assertEqual(len(prev5), STANDING_N5)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, CYCLE303_MATCHING_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE307_MATCHING_SITES)
        self.assertEqual(self.previous_5grams[0], GRAM5_PREV_G)
        self.assertEqual(self.previous_stems[0], "720")
        self.assertEqual(self.previous_stems[1], "076")
        local = leftover_local_4grams(self.i_sides, STANDING_SITES, GRAM2)
        for (_site, prev4, _nxt4), want in zip(
            local,
            STANDING_PREVIOUS_4GRAMS,
            strict=True,
        ):
            self.assertEqual(prev4, want)
        self.assertEqual(
            leftover_n4_remaining_g_overlap_sites(
                self.sites, CYCLE297_REMAINING_AFTER_011_SITES
            ),
            STANDING_OVERLAP_REMAINING_AFTER_011,
        )
        self.assertTrue(STANDING_OVERLAP_REMAINING_AFTER_011_EQUALS_POPULATION)
        self.assertEqual(self.overlap_after_011, STANDING_SITES)
        self.assertEqual(self.overlap_258, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_261, STANDING_OVERLAP_CYCLE261_PREVIOUS_999)
        self.assertEqual(self.overlap_306, STANDING_OVERLAP_CYCLE306_G_600)
        self.assertEqual(CYCLE303_OVERLAP_258, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(CYCLE303_OVERLAP_259, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(CYCLE303_OVERLAP_261, STANDING_OVERLAP_CYCLE261_PREVIOUS_999)
        self.assertEqual(CYCLE303_OVERLAP_AFTER_011, STANDING_OVERLAP_REMAINING_AFTER_011)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE259_EXTRA_I_SITES)
        self.assertNotIn((SIDE_IA, "Ia13", 17), CYCLE259_EXTRA_I_SITES)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(STANDING_EMPTY_REMAINDER_DOES_NOT_LOSE)
        unused_ia = IA_LINE_NAMES
        self.assertIn("Ia8", unused_ia)
        self.assertIn("Ia13", unused_ia)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_overlap_recorded_does_not_fail_unique_max(self):
        """Remaining-after-011 equality and leftover-extra Ia8[106] do not decide unique-max."""
        self.assertEqual(self.overlap_after_011, STANDING_SITES)
        self.assertEqual(self.overlap_after_011, CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertEqual(self.overlap_258, ((SIDE_IA, "Ia8", 106),))
        self.assertEqual(self.overlap_259, ((SIDE_IA, "Ia8", 106),))
        self.assertEqual(self.overlap_261, ())
        self.assertEqual(self.overlap_306, ())
        self.assertNotEqual(self.sites, CYCLE307_MATCHING_SITES)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertFalse(self.unique)
        self.assertFalse(self.claim_holds)
        self.assertEqual(CYCLE304_EXTRA_I_SITES, ())
        self.assertEqual(CYCLE305_NOT_HAPAX_I_SITES[0][2], 104)
        self.assertEqual(CYCLE305_NOT_HAPAX_I_SITES[1][2], 15)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_prior_cycles_stay(self):
        """Cycles 305/304/303/302/301/288/306/308/318/224/223 stay; no LLM."""
        prior_305 = TestMamariI021090076Previous4gramsIOnlyScoreboard()
        prior_305.setUp()
        prior_305.test_all_4grams_are_i_only_not_all_hapax_and_claim_holds()
        prior_305.test_survey_matches_computed_lock()
        self.assertEqual(prior_305.n_i_only, 4)
        self.assertEqual(prior_305.n_not_hapax, 1)
        self.assertEqual(prior_305.n_not_i_only, 0)
        self.assertTrue(prior_305.claim_holds)
        self.assertTrue(CYCLE305_CLAIM)
        if prior_305.n_i_only != 4 or prior_305.n_not_hapax != 1:
            self.fail("nested cycle 305 previous-021 4-grams I-only N_i_only=4 N_not_hapax=1 drifted")
        prior_304 = TestMamariI3gram021090076IOnlyScoreboard()
        prior_304.setUp()
        prior_304.test_3gram_is_zero_off_i_and_i_only()
        prior_304.test_survey_matches_computed_lock()
        self.assertEqual(prior_304.i_hits, 5)
        self.assertEqual(prior_304.off_i_hits, 0)
        self.assertEqual(prior_304.extra, ())
        self.assertTrue(CYCLE304_CLAIM)
        self.assertEqual(CYCLE304_N_I, 5)
        self.assertEqual(CYCLE304_N_OFF_I, 0)
        self.assertEqual(CYCLE304_N_EXTRA, 0)
        if prior_304.i_hits != 5 or prior_304.off_i_hits != 0 or prior_304.extra:
            self.fail("nested cycle 304 021 090 076 I-only 5/0 extra I=0 drifted")
        prior_303 = TestMamariILeftoverN4Remaining090076Previous021Scoreboard()
        prior_303.setUp()
        prior_303.test_counts_5_of_13_and_hypothesis_k_5_holds()
        prior_303.test_survey_matches_computed_lock()
        self.assertEqual(prior_303.k_021, 5)
        self.assertEqual(prior_303.n_remaining_after_021, 8)
        self.assertEqual(prior_303.matching, CYCLE303_MATCHING_SITES)
        self.assertEqual(self.share_021, prior_303.matching)
        self.assertTrue(prior_303.claim_holds)
        self.assertTrue(CYCLE303_CLAIM)
        if (
            prior_303.k_021 != 5
            or prior_303.n_remaining_after_021 != 8
            or not prior_303.claim_holds
        ):
            self.fail(
                "nested cycle 303 leftover n=4 remaining exactly 5 share 021 / N_remaining=8 drifted"
            )
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
        if (
            prior_302.g != "021"
            or prior_302.k != 5
            or prior_302.n_inside != 13
            or prior_302.n_distinct != 8
            or not prior_302.unique
            or not prior_302.claim_holds
        ):
            self.fail(
                "nested cycle 302 unique-max G=021 K=5 N=13 N_line_initial=0 distinct=8 drifted"
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
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.n_inside, 13)
        self.assertEqual(prior_288.n_distinct, 6)
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        if (
            prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or not prior_288.unique_max
            or prior_288.claim_holds
        ):
            self.fail("nested cycle 288 share-one-forward lost 6 distinct G=020 K=4 unique-max drifted")
        prior_306 = TestMamariILeftoverN4Remaining090076RemainingAfter021PreviousStemScoreboard()
        prior_306.setUp()
        prior_306.test_counts_8_remaining_g_600_k_2_and_hypothesis_holds()
        prior_306.test_survey_matches_computed_lock()
        self.assertEqual(prior_306.g, "600")
        self.assertEqual(prior_306.k, 2)
        self.assertTrue(prior_306.unique)
        self.assertTrue(prior_306.claim_holds)
        self.assertTrue(CYCLE306_CLAIM)
        if prior_306.g != "600" or prior_306.k != 2 or not prior_306.unique:
            self.fail("nested cycle 306 remaining-after-021 unique-max true G=600 K=2 drifted")
        prior_307 = TestMamariILeftoverN4Remaining090076RemainingAfter021Previous600Scoreboard()
        prior_307.setUp()
        prior_307.test_counts_2_of_8_and_hypothesis_k_2_holds()
        prior_307.test_survey_matches_computed_lock()
        self.assertEqual(prior_307.k_600, 2)
        self.assertTrue(prior_307.claim_holds)
        self.assertTrue(CYCLE307_CLAIM)
        if prior_307.k_600 != 2 or not prior_307.claim_holds:
            self.fail("nested cycle 307 remaining-after-021 exactly 2 share 600 drifted")
        prior_308 = TestMamariILeftoverN4Remaining090076RemainingAfter600PreviousStemScoreboard()
        prior_308.setUp()
        prior_308.test_counts_6_remaining_all_hapax_g_999_k_1_and_hypothesis_loses()
        prior_308.test_survey_matches_computed_lock()
        self.assertEqual(prior_308.g, "999")
        self.assertEqual(prior_308.k, 1)
        self.assertFalse(prior_308.unique)
        self.assertFalse(prior_308.claim_holds)
        self.assertFalse(CYCLE308_CLAIM)
        if prior_308.g != "999" or prior_308.k != 1 or prior_308.unique:
            self.fail("nested cycle 308 remaining-after-600 unique-max false G=999 K=1 drifted")
        prior_318 = TestMamariILeftoverN4Remaining090076RemainingAfter600RemainingAfter020ExtraIFwd4090076057IOnlyScoreboard()
        prior_318.setUp()
        prior_318.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_318.test_survey_matches_computed_lock()
        self.assertTrue(prior_318.claim_holds)
        self.assertTrue(CYCLE318_CLAIM)
        if not prior_318.claim_holds:
            self.fail("nested cycle 318 remaining-after-600 remaining-after-020 extra-I 4-grams drifted")
        prior_261 = TestMamariILeftoverExtra090076Previous999Scoreboard()
        prior_261.setUp()
        prior_261.test_counts_15_of_56_and_hypothesis_k_15_holds()
        prior_261.test_survey_matches_computed_lock()
        self.assertEqual(prior_261.k_999, 15)
        self.assertEqual(prior_261.n_remaining_after_999, 41)
        self.assertTrue(CYCLE261_CLAIM)
        if prior_261.k_999 != 15 or prior_261.n_remaining_after_999 != 41:
            self.fail("nested cycle 261 leftover extra previous-999 K_999=15 N_remaining=41 drifted")
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_259.test_survey_matches_computed_lock()
        self.assertEqual(prior_259.n_i_only, 2)
        self.assertEqual(prior_259.n_not_i_only, 0)
        self.assertTrue(prior_259.claim_holds)
        self.assertTrue(CYCLE259_CLAIM)
        self.assertEqual(CYCLE259_N_I_ONLY, 2)
        self.assertEqual(CYCLE259_N_NOT_I_ONLY, 0)
        if prior_259.n_i_only != 2 or prior_259.n_not_i_only != 0:
            self.fail("nested cycle 259 leftover extra remaining-after-000 extra-I 4-grams 2/0 drifted")
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
        self.assertEqual(prior_223.i_hits, STANDING_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, STANDING_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, STANDING_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        unused_303_prev4 = CYCLE303_MATCHING_PREVIOUS_4GRAMS
        self.assertEqual(unused_303_prev4.count(LOCKED_PREVIOUS_4GRAM), 2)
        unused_261 = CYCLE261_K_999
        self.assertEqual(unused_261, 15)
        unused_261_rem = CYCLE261_N_REMAINING_AFTER_999
        self.assertEqual(unused_261_rem, 41)
        unused_gram5 = GRAM5
        self.assertEqual(len(unused_gram5), 5)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-319 leftover n=4 remaining 999 021 090 076 lock."""
        lock = self.survey[
            "i_leftover_n4_remaining_021_090_076_999_021_090_076_prev_stem"
        ]
        self.assertEqual(lock["cycle"], 319)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(tuple(lock["backward_3gram"]), ("021", "090", "076"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(tuple(lock["previous_4gram"]), LOCKED_PREVIOUS_4GRAM)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_with_previous_inside"], STANDING_N_WITH_PREVIOUS_INSIDE)
        self.assertEqual(lock["N_with_previous_inside"], 13)
        self.assertEqual(lock["N_line_initial_inside"], STANDING_N_LINE_INITIAL_INSIDE)
        self.assertEqual(lock["N_line_initial_inside"], 0)
        self.assertEqual(lock["K_021"], STANDING_K_021)
        self.assertEqual(lock["K_021"], 5)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_021_sites"]),
            CYCLE303_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_021"], STANDING_N_REMAINING_AFTER_021)
        self.assertEqual(lock["N_remaining_after_021"], 8)
        self.assertEqual(lock["N_not_hapax_4gram"], STANDING_N_NOT_HAPAX_4GRAM)
        self.assertEqual(lock["N"], STANDING_N)
        self.assertEqual(lock["N"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_remaining_021_090_076_999_021_090_076_sites"]),
            STANDING_SITES,
        )
        self.assertEqual(
            tuple(lock["previous_of_999_stems"]),
            STANDING_PREVIOUS_STEMS,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PREVIOUS_4GRAMS],
            lock["previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PREVIOUS_5GRAMS],
            lock["previous_5grams"],
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 2)
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["line_initial_sites"], [])
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 2)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 2)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "720")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 1)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 2)
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 1)
        self.assertEqual(
            tuple(
                tuple(row)
                for row in lock["matching_leftover_n4_remaining_021_090_076_999_021_090_076_sites"]
            ),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_5GRAMS],
            lock["matching_previous_5grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_021_090_076_999_021_090_076_local_5grams"],
            matching_leftover_n4_remaining_999_021_090_076_local_5gram_rows(),
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_G_sites"]),
            STANDING_REMAINING_AFTER_G_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_REMAINING_AFTER_G_PREVIOUS_5GRAMS],
            lock["remaining_after_G_previous_5grams"],
        )
        self.assertEqual(
            lock["previous_of_999_stem_frequency"],
            remaining_999_021_090_076_previous_stem_frequency_rows(),
        )
        self.assertEqual(lock["overlap_cycle261_previous_999_sites"], [])
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE258_EXTRA_I],
            lock["overlap_cycle258_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE259_EXTRA_I],
            lock["overlap_cycle259_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_REMAINING_AFTER_011],
            lock["overlap_remaining_after_011_sites"],
        )
        self.assertTrue(lock["overlap_remaining_after_011_equals_population"])
        self.assertEqual(lock["overlap_cycle306_G_600_sites"], [])
        self.assertEqual(lock["overlap_cycle307_previous_600_sites"], [])
        self.assertEqual(lock["overlap_cycle308_remaining_after_600_sites"], [])
        self.assertEqual(lock["overlap_cycle318_extra_i_sites"], [])
        self.assertTrue(lock["overlap_does_not_lose"])
        self.assertEqual(
            list(STANDING_NESTED_LEFTOVER_N4_REMAINING),
            lock["nested_leftover_n4_remaining"],
        )
        self.assertEqual(lock["nested_cycle305_N_i_only"], 4)
        self.assertEqual(lock["nested_cycle305_N_hapax_i_only"], 3)
        self.assertEqual(lock["nested_cycle305_N_not_hapax"], 1)
        self.assertEqual(lock["nested_cycle305_N_not_i_only"], 0)
        self.assertTrue(lock["nested_cycle305_previous_4grams_all_i_only"])
        self.assertEqual(lock["nested_cycle304_N_I"], 5)
        self.assertEqual(lock["nested_cycle304_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle304_N_extra"], 0)
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
        self.assertEqual(lock["nested_cycle288_N_distinct_next_stems"], 6)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertFalse(lock["nested_cycle288_share_one_forward_stem"])
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle306_G"], "600")
        self.assertEqual(lock["nested_cycle306_K"], 2)
        self.assertTrue(lock["nested_cycle306_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle307_K_600"], 2)
        self.assertEqual(lock["nested_cycle308_G"], "999")
        self.assertEqual(lock["nested_cycle308_K"], 1)
        self.assertEqual(lock["nested_cycle308_N_distinct"], 6)
        self.assertFalse(lock["nested_cycle308_G_uniquely_most_frequent"])
        self.assertTrue(lock["nested_cycle318_extra_i_fwd4_all_i_only"])
        self.assertEqual(lock["nested_cycle261_K_999"], 15)
        self.assertEqual(lock["nested_cycle261_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle259_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle259_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(
            lock["i_leftover_n4_remaining_021_090_076_999_021_090_076_unique_previous_stem"]
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle302"])
        self.assertFalse(lock["same_as_cycle303"])
        self.assertFalse(lock["same_as_cycle304"])
        self.assertFalse(lock["same_as_cycle305"])
        self.assertFalse(lock["same_as_cycle306"])
        self.assertFalse(lock["same_as_cycle307"])
        self.assertFalse(lock["same_as_cycle308"])
        self.assertTrue(lock["same_claim_shape_as_cycle302"])
        self.assertTrue(lock["same_claim_shape_as_cycle306"])
        self.assertTrue(lock["same_claim_shape_as_cycle308"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["do_not_relock_cycle305"])
        self.assertTrue(lock["do_not_relock_cycle304"])
        self.assertTrue(lock["do_not_relock_cycles_302_303"])
        self.assertTrue(lock["do_not_relock_cycles_298_301"])
        self.assertTrue(lock["do_not_relock_cycles_258_259"])
        self.assertTrue(lock["do_not_relock_cycles_308_318"])
        self.assertTrue(lock["cycle305_4grams_are_not_this_cycle"])
        self.assertTrue(lock["cycle304_3gram_is_not_this_cycle"])
        self.assertTrue(lock["cycle306_remaining_after_021_is_not_this_population"])
        self.assertTrue(lock["cycle308_remaining_after_600_is_not_this_population"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_extra_previous_999_is_not_this_cycle"])
        self.assertTrue(
            lock["leftover_n4_remaining_unique_previous_stem_is_not_this_cycle"]
        )
        self.assertTrue(lock["leftover_n4_remaining_previous_021_is_not_this_cycle"])
        self.assertTrue(
            lock["leftover_n4_remaining_previous_021_4grams_is_not_this_cycle"]
        )
        self.assertTrue(lock["3gram_021_090_076_is_not_this_cycle"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["g_k_is_inventory_for_later_peel"])
        self.assertTrue(lock["empty_remainder_does_not_lose"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_021_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_021_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_previous_021_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_previous_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_600_remaining_after_020_extra_i_fwd4_090_076_057_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_021_090_076_previous_4grams_i_only"]["cycle"], 305)
        self.assertTrue(
            self.survey["i_021_090_076_previous_4grams_i_only"][
                "i_021_090_076_previous_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_021_090_076_previous_4grams_i_only"]["N_i_only"], 4)
        self.assertEqual(self.survey["i_021_090_076_previous_4grams_i_only"]["N_not_hapax"], 1)
        self.assertEqual(self.survey["i_3gram_021_090_076_i_only"]["cycle"], 304)
        self.assertTrue(self.survey["i_3gram_021_090_076_i_only"]["i_3gram_021_090_076_i_only"])
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
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem"][
                "cycle"
            ],
            306,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem"][
                "cycle"
            ],
            308,
        )
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_600_previous_stem"][
                "i_leftover_n4_remaining_090_076_remaining_after_600_unique_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey[
                "i_leftover_n4_remaining_090_076_remaining_after_600_remaining_after_020_extra_i_fwd4_090_076_057_i_only"
            ]["cycle"],
            318,
        )
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"], 13)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
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


class TestMamariILeftoverN4Remaining021090076999021090076PrevStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 319 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
