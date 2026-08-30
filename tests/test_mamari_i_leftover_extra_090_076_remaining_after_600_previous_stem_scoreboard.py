"""I's cycle-269 leftover extra remaining-after-600 previous-stem lock.

Cycle 270 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover extra I sites of 2-gram 090 076 (the 56 I
sites that do not sit inside leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover extra sites, the leftover n=4 set, or
the already-closed leftover remaining family. Does not retune
the forward peel of leftover extra I 090 076 (cycles 225–259).
Does not overwrite cycle 167's 3-gram I-only 16/0 lock. Does
not overwrite cycle 268's 3-gram I-only 6/0 lock. Does not
overwrite cycle 269's previous-4 I-only hapax lock. Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Cycle 266 leftover extra remaining-after-999 unique-max
previous stem HOLDS: G=600 K=4, distinct=33. Cycle 267 leftover
extra remaining-after-999 exactly 4 share previous 600 HOLDS;
N_remaining_after_600=37. Cycles 268–269 peeled the I 600 090
076 cluster (3-gram I-only 6/0 extra I=2; previous 4-grams all
I-only hapax 6/0). Those are previous 4-grams of I 600 090 076,
not leftover extra remaining-after-600 previous stems. Leftover
extra remaining-after-600 previous stems are not yet locked.
This cycle is the unique-max claim on leftover extra remaining-
after-600 (same claim-shape as cycle 266 remaining-after-999
unique previous stem, cycle 256 remaining-after-000 next-stem,
and cycle 234 remaining-after-001 next-stem), remaining-after-
600 instead of remaining-after-999. Do not peel a specific
remaining previous stem this cycle. Do not retune leftover
n=4. Do not retune the forward peel. Off-I T sites are not
this cycle.

Leftover extra remaining-after-600 = leftover extra I 090 076
sites whose previous token is neither 999 nor 600. For each
such site, take the previous token if any (lock line-initial /
no-previous count separately). Nested-check leftover extra
I 090 076 == 56, N_I==69, K_999==15, N_remaining_after_999==41,
K_600==4, N_remaining_after_600==37 (do not retune
223/224/260/261/266/267). Nested-check cycle 269 all-hapax
true, N_i_only==6, N_not_hapax==0 (do not retune). Measure
previous-stem frequencies among remaining-after-600 sites
that have a previous token. G = the previous stem with the
highest remaining-after-600 with-previous count. If a tie,
pick the larger Barthel id. K = that count.

Claim that can lose:
i_leftover_extra_090_076_remaining_after_600_unique_previous_stem.
True iff remaining-after-600 leftover extra I 090 076 has a
unique most frequent previous stem G with K ≥ 2 (no tie at
max K). This can lose the same way cycle 234 lost (7-way tie
at 2) and cycle 256 lost (19 hapax K=1), or hold the same
way cycle 266 held (G=600 K=4). Unique-max G/K is inventory
for a later peel if the claim holds or loses with K≥2.
Measured: N_remaining=37, N_with_previous=37, N_no_previous=0,
N_distinct=32, 5-way tie at K=2 (090/076/071/045/009),
27 hapax, G=090 by larger-id tie-break. The claim is false.
Nested cycle 269 6/0 hapax, cycle 268 6/0 extra I=2, cycle
267 K_600=4 N_remaining_after_600=37, cycle 266 unique-max
G=600 K=4 distinct=33, cycle 261 K_999=15, cycle 260 34
distinct G=999 K=15, cycle 223 69/3, and cycle 207 8/1 on T
stay. Do not assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
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
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_600_090_076_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE268_EXTRA_I_SITES,
    STANDING_I_3GRAM_600_090_076_I_ONLY as CYCLE268_CLAIM,
    STANDING_I_SITES as CYCLE268_I_SITES,
    STANDING_N_EXTRA as CYCLE268_N_EXTRA,
    STANDING_N_I as CYCLE268_N_I,
    STANDING_N_OFF_I as CYCLE268_N_OFF_I,
    TestMamariI3gram600090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_600_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_600_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE269_ALL_HAPAX,
    STANDING_N_I_ONLY as CYCLE269_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE269_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE269_N_NOT_I_ONLY,
    TestMamariI600090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    group_sites_by_previous_stem,
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999 as CYCLE261_CLAIM,
    STANDING_K_999 as CYCLE261_K_999,
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
    STANDING_N_LEFTOVER_EXTRA as CYCLE261_N_LEFTOVER_EXTRA,
    STANDING_N_REMAINING_AFTER_999 as CYCLE261_N_REMAINING_AFTER_999,
    leftover_extra_with_previous_999,
    leftover_extra_without_previous_999,
    TestMamariILeftoverExtra090076Previous999Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE260_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE260_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM as CYCLE260_SHARE_ONE,
    STANDING_K as CYCLE260_K,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE260_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE260_N_LEFTOVER,
    leftover_extra_backward_3grams,
    leftover_extra_previous_4grams,
    leftover_extra_previous_stems,
    leftover_sites_with_previous,
    leftover_sites_without_previous,
    rank_previous_stems,
    select_previous_g,
    TestMamariILeftoverExtra090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    STANDING_G as CYCLE256_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE256_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
    TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_next_stem_scoreboard import (
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE234_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G as CYCLE234_CLAIM,
    STANDING_K as CYCLE234_K,
    STANDING_N_TIED_AT_K as CYCLE234_N_TIED_AT_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_600_scoreboard import (
    STANDING_G as CYCLE267_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_EXACTLY_4_SHARE_PREVIOUS_600 as CYCLE267_CLAIM,
    STANDING_K_600 as CYCLE267_K_600,
    STANDING_MATCHING_SITES as CYCLE267_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_600 as CYCLE267_N_REMAINING_AFTER_600,
    leftover_extra_remaining_after_999_without_previous_600,
    TestMamariILeftoverExtra090076RemainingAfter999Previous600Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_999,
    STANDING_G as CYCLE266_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE266_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_UNIQUE_PREVIOUS_STEM as CYCLE266_CLAIM,
    STANDING_K as CYCLE266_K,
    STANDING_MATCHING_SITES as CYCLE266_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING as CYCLE266_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_999 as CYCLE266_N_REMAINING,
    STANDING_REMAINING_SITES as CYCLE266_REMAINING_SITES,
    leftover_extra_remaining_after_999,
    leftover_extra_remaining_after_999_nested_counts_hold,
    leftover_extra_remaining_after_999_previous_stems,
    leftover_extra_remaining_after_999_with_g,
    leftover_extra_remaining_after_999_with_previous,
    leftover_extra_remaining_after_999_without_g,
    leftover_extra_remaining_after_999_without_previous,
    select_remaining_after_999_g,
    TestMamariILeftoverExtra090076RemainingAfter999PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
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

LOCKED_PREVIOUS_STEM_999 = "999"
LOCKED_PREVIOUS_STEM_600 = "600"
LOCKED_PREVIOUS_STEMS_AFTER_600 = (
    LOCKED_PREVIOUS_STEM_999,
    LOCKED_PREVIOUS_STEM_600,
)
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_BACKWARD = ("090", "090", "076")
GRAM3_NESTED_600 = ("600", "090", "076")
GRAM3_NESTED_999 = ("999", "090", "076")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS_LEFTOVER = 56
STANDING_N_NO_PREVIOUS_LEFTOVER = 0
STANDING_K_999 = 15
STANDING_N_REMAINING_AFTER_999 = 41
STANDING_K_600 = 4
STANDING_N_REMAINING_AFTER_600 = 37
STANDING_N_WITH_PREVIOUS = 37
STANDING_N_NO_PREVIOUS = 0
STANDING_NO_PREVIOUS_SITES = ()
STANDING_N_DISTINCT_REMAINING = 32
STANDING_N_HAPAX_REMAINING = 27
STANDING_G = "090"
STANDING_K = 2
STANDING_N_WITHOUT_G = 35
STANDING_N_TIED_AT_K = 5
STANDING_TIED_STEMS = ("090", "076", "071", "045", "009")
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_REMAINING_SITES = (
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 37),
    (SIDE_IA, "Ia2", 159),
    (SIDE_IA, "Ia2", 165),
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia3", 4),
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia4", 134),
    (SIDE_IA, "Ia4", 162),
    (SIDE_IA, "Ia4", 166),
    (SIDE_IA, "Ia5", 6),
    (SIDE_IA, "Ia5", 66),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia5", 164),
    (SIDE_IA, "Ia6", 134),
    (SIDE_IA, "Ia7", 2),
    (SIDE_IA, "Ia7", 88),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia8", 120),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia10", 141),
    (SIDE_IA, "Ia12", 42),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 67),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia13", 143),
    (SIDE_IA, "Ia13", 152),
    (SIDE_IA, "Ia14", 9),
    (SIDE_IA, "Ia14", 97),
    (SIDE_IA, "Ia14", 105),
    (SIDE_IA, "Ia14", 177),
)
STANDING_REMAINING_PREVIOUS_STEMS = (
    "045",
    "048",
    "380",
    "011",
    "499",
    "045",
    "497",
    "076",
    "009",
    "036",
    "071",
    "092",
    "291",
    "522",
    "150",
    "078",
    "295",
    "000",
    "109",
    "009",
    "052",
    "099",
    "071",
    "700",
    "161",
    "010",
    "205",
    "090",
    "382",
    "386",
    "008",
    "027",
    "076",
    "724",
    "400",
    "090",
    "326",
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia12", 42),
    (SIDE_IA, "Ia14", 105),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("011", "090", "090", "076"),
    ("011", "090", "090", "076"),
)
STANDING_REMAINING_FREQUENCY = (
    (
        "090",
        2,
        ((SIDE_IA, "Ia12", 42), (SIDE_IA, "Ia14", 105)),
        (("090", "090", "076"),) * 2,
    ),
    (
        "076",
        2,
        ((SIDE_IA, "Ia2", 165), (SIDE_IA, "Ia13", 152)),
        (("076", "090", "076"),) * 2,
    ),
    (
        "071",
        2,
        ((SIDE_IA, "Ia3", 87), (SIDE_IA, "Ia7", 88)),
        (("071", "090", "076"),) * 2,
    ),
    (
        "045",
        2,
        ((SIDE_IA, "Ia1", 15), (SIDE_IA, "Ia2", 37)),
        (("045", "090", "076"),) * 2,
    ),
    (
        "009",
        2,
        ((SIDE_IA, "Ia2", 174), (SIDE_IA, "Ia5", 164)),
        (("009", "090", "076"),) * 2,
    ),
    ("724", 1, ((SIDE_IA, "Ia14", 9),), (("724", "090", "076"),)),
    ("700", 1, ((SIDE_IA, "Ia7", 137),), (("700", "090", "076"),)),
    ("522", 1, ((SIDE_IA, "Ia4", 134),), (("522", "090", "076"),)),
    ("499", 1, ((SIDE_IA, "Ia2", 14),), (("499", "090", "076"),)),
    ("497", 1, ((SIDE_IA, "Ia2", 159),), (("497", "090", "076"),)),
    ("400", 1, ((SIDE_IA, "Ia14", 97),), (("400", "090", "076"),)),
    ("386", 1, ((SIDE_IA, "Ia13", 67),), (("386", "090", "076"),)),
    ("382", 1, ((SIDE_IA, "Ia12", 150),), (("382", "090", "076"),)),
    ("380", 1, ((SIDE_IA, "Ia1", 59),), (("380", "090", "076"),)),
    ("326", 1, ((SIDE_IA, "Ia14", 177),), (("326", "090", "076"),)),
    ("295", 1, ((SIDE_IA, "Ia5", 6),), (("295", "090", "076"),)),
    ("291", 1, ((SIDE_IA, "Ia4", 121),), (("291", "090", "076"),)),
    ("205", 1, ((SIDE_IA, "Ia10", 141),), (("205", "090", "076"),)),
    ("161", 1, ((SIDE_IA, "Ia8", 120),), (("161", "090", "076"),)),
    ("150", 1, ((SIDE_IA, "Ia4", 162),), (("150", "090", "076"),)),
    ("109", 1, ((SIDE_IA, "Ia5", 127),), (("109", "090", "076"),)),
    ("099", 1, ((SIDE_IA, "Ia7", 2),), (("099", "090", "076"),)),
    ("092", 1, ((SIDE_IA, "Ia4", 84),), (("092", "090", "076"),)),
    ("078", 1, ((SIDE_IA, "Ia4", 166),), (("078", "090", "076"),)),
    ("052", 1, ((SIDE_IA, "Ia6", 134),), (("052", "090", "076"),)),
    ("048", 1, ((SIDE_IA, "Ia1", 27),), (("048", "090", "076"),)),
    ("036", 1, ((SIDE_IA, "Ia3", 4),), (("036", "090", "076"),)),
    ("027", 1, ((SIDE_IA, "Ia13", 143),), (("027", "090", "076"),)),
    ("011", 1, ((SIDE_IA, "Ia1", 96),), (("011", "090", "076"),)),
    ("010", 1, ((SIDE_IA, "Ia10", 137),), (("010", "090", "076"),)),
    ("008", 1, ((SIDE_IA, "Ia13", 135),), (("008", "090", "076"),)),
    ("000", 1, ((SIDE_IA, "Ia5", 66),), (("000", "090", "076"),)),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_extra_090_076_remaining_after_600_unique_previous_stem"
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM = False
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_600_previous_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE234 = False
STANDING_SAME_AS_CYCLE256 = False
STANDING_SAME_AS_CYCLE266 = False
STANDING_SAME_AS_CYCLE267 = False
STANDING_SAME_AS_CYCLE268 = False
STANDING_SAME_AS_CYCLE269 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE266 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE269_PREVIOUS_4GRAMS_ARE_NOT_REMAINING_AFTER_600 = True
STANDING_CYCLE268_3GRAM_IS_NOT_REMAINING_AFTER_600 = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE167_NOT_OVERWRITTEN = True
STANDING_CYCLE268_NOT_OVERWRITTEN = True
STANDING_CYCLE269_NOT_OVERWRITTEN = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL = True


def leftover_extra_remaining_after_600(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites whose previous token is neither 999 nor 600."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev not in locked_set
    )


def leftover_extra_remaining_after_600_previous_stems(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[str, ...]:
    """Previous stems of remaining-after-600 sites that have a previous token."""
    locked_set = set(locked)
    return tuple(
        prev
        for prev in previous_stems
        if prev is not None and prev not in locked_set
    )


def leftover_extra_remaining_after_600_with_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-600 leftover extra sites that have a previous token."""
    remaining = leftover_extra_remaining_after_600(sites, previous_stems, locked)
    rem_prev = tuple(
        prev
        for site, prev in zip(sites, previous_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_with_previous(remaining, rem_prev)


def leftover_extra_remaining_after_600_without_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-600 leftover extra sites with no previous token."""
    remaining = leftover_extra_remaining_after_600(sites, previous_stems, locked)
    rem_prev = tuple(
        prev
        for site, prev in zip(sites, previous_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_without_previous(remaining, rem_prev)


def leftover_extra_remaining_after_600_with_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-600 sites whose previous token is G."""
    remaining = set(leftover_extra_remaining_after_600(sites, previous_stems, locked))
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev == stem and site in remaining
    )


def leftover_extra_remaining_after_600_without_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-600 sites whose previous token is not G."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev is not None and prev not in locked_set and prev != stem
    )


def remaining_after_600_previous_stem_counts(previous_stems: tuple[str, ...]) -> Counter:
    """Counts of previous stems among leftover extra remaining-after-600 with-previous."""
    return Counter(previous_stems)


def rank_remaining_after_600_previous_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Remaining-after-600 previous stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_remaining_after_600_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining-after-600 has no G."""
    ranked = rank_remaining_after_600_previous_stems(
        remaining_after_600_previous_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_after_600_previous_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    backward_3grams: tuple[tuple[str, ...] | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Remaining-after-600 previous-stem frequency: highest count first, then larger id."""
    rem_sites = leftover_extra_remaining_after_600_with_previous(
        sites, previous_stems, locked
    )
    rem_stems = leftover_extra_remaining_after_600_previous_stems(
        sites, previous_stems, locked
    )
    locked_set = set(locked)
    rem_grams = tuple(
        gram
        for prev, gram in zip(previous_stems, backward_3grams, strict=True)
        if prev is not None and prev not in locked_set
    )
    first_seen = group_sites_by_previous_stem(rem_sites, rem_stems)
    grams_by_stem: dict[str, list[tuple[str, ...]]] = {
        stem: [] for stem, _ in first_seen
    }
    for prev, gram in zip(rem_stems, rem_grams, strict=True):
        if gram is not None:
            grams_by_stem[prev].append(gram)
    rows = tuple(
        (stem, len(stem_sites), stem_sites, tuple(grams_by_stem[stem]))
        for stem, stem_sites in first_seen
    )
    return tuple(sorted(rows, key=lambda row: (-row[1], -barthel_id(row[0]))))


def remaining_after_600_previous_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_REMAINING_FREQUENCY,
) -> list[dict]:
    """Survey-shaped remaining-after-600 previous-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "previous_stem": stem,
                "count": count,
                "leftover_extra_remaining_after_600_sites": [
                    list(site) for site in sites
                ],
                "backward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def leftover_extra_remaining_after_600_nested_counts_hold(
    n_i: int,
    n_leftover: int,
    k_999: int,
    n_remaining_after_999: int,
    k_600: int,
    n_remaining: int,
    expected_i: int = STANDING_N_I,
    expected_leftover: int = STANDING_N_LEFTOVER,
    expected_k_999: int = STANDING_K_999,
    expected_remaining_999: int = STANDING_N_REMAINING_AFTER_999,
    expected_k_600: int = STANDING_K_600,
    expected_remaining: int = STANDING_N_REMAINING_AFTER_600,
) -> bool:
    """Nested leftover extra 69/56, K_999=15, remaining-after-999=41, K_600=4, remaining-after-600=37."""
    return (
        n_i == expected_i
        and n_leftover == expected_leftover
        and k_999 == expected_k_999
        and n_remaining_after_999 == expected_remaining_999
        and k_600 == expected_k_600
        and n_remaining == expected_remaining
        and n_remaining_after_999 == n_leftover - k_999
        and n_remaining == n_remaining_after_999 - k_600
    )


def i_leftover_extra_090_076_remaining_after_600_unique_previous_stem(
    leftover_sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_600,
) -> bool:
    """True iff remaining-after-600 has a unique most frequent previous stem with K ≥ 2."""
    remaining = leftover_extra_remaining_after_600(
        leftover_sites,
        previous_stems,
        locked,
    )
    remaining_stems = leftover_extra_remaining_after_600_previous_stems(
        leftover_sites,
        previous_stems,
        locked,
    )
    if len(remaining) != STANDING_N_REMAINING_AFTER_600:
        return False
    if remaining != leftover_extra_remaining_after_999_without_previous_600(
        leftover_sites,
        previous_stems,
    ):
        return False
    gram, count, unique = select_remaining_after_600_g(remaining_stems)
    return bool(unique and gram is not None and count >= 2)


def matching_leftover_extra_remaining_after_600_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    previous_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_PREVIOUS_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining-after-600 previous-4-gram rows."""
    rows = []
    for (side, line, index), prev_gram in zip(
        leftover_sites,
        previous_4grams,
        strict=True,
    ):
        rows.append(
            {
                "tablet": "I",
                "side": side,
                "line": line,
                "index": index,
                "previous_4gram": list(prev_gram),
                "backward_3gram": list(prev_gram[1:]),
            }
        )
    return rows


class TestILeftoverExtra090076RemainingAfter600PreviousStemHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-600 previous stems. No CV, no LLM."""

    def test_remaining_after_600_requires_previous_neither_999_nor_600(self):
        """Remaining-after-600 excludes previous 999 and 600; line-initial is remaining."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("090", "090", "076"))
        self.assertEqual(GRAM3_NESTED_600, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_999, ("999", "090", "076"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS_AFTER_600, ("999", "600"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS_AFTER_999, ("999",))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_090 = ["011", "090", "090", "076"]
        self.assertEqual(site_previous_stem(has_090, 2, GRAM2), "090")
        self.assertEqual(site_backward_3gram(has_090, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_090, 2, GRAM2),
            ("011", "090", "090", "076"),
        )
        has_600 = ["076", "600", "090", "076", "011"]
        self.assertEqual(site_previous_stem(has_600, 2, GRAM2), "600")
        self.assertNotEqual(site_previous_stem(has_600, 2, GRAM2), "090")
        has_999 = ["000", "999", "090", "076"]
        self.assertEqual(site_previous_stem(has_999, 2, GRAM2), "999")
        self.assertNotEqual(site_previous_stem(has_999, 2, GRAM2), "090")
        line_initial = ["090", "076", "012"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 4),
        )
        planted_stems = ("090", "999", "600", None, "045")
        rem = leftover_extra_remaining_after_600(planted_sites, planted_stems)
        self.assertEqual(
            rem,
            (planted_sites[0], planted_sites[3], planted_sites[4]),
        )
        self.assertEqual(
            leftover_extra_remaining_after_600_previous_stems(
                planted_sites, planted_stems
            ),
            ("090", "045"),
        )
        self.assertEqual(
            leftover_extra_remaining_after_600_with_previous(
                planted_sites, planted_stems
            ),
            (planted_sites[0], planted_sites[4]),
        )
        self.assertEqual(
            leftover_extra_remaining_after_600_without_previous(
                planted_sites, planted_stems
            ),
            (planted_sites[3],),
        )
        self.assertEqual(
            leftover_extra_remaining_after_600_with_g(planted_sites, planted_stems),
            (planted_sites[0],),
        )
        self.assertNotIn(planted_sites[1], rem)
        self.assertNotIn(planted_sites[2], rem)
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_previous_stem(mismatch_071, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE269_PREVIOUS_4GRAMS_ARE_NOT_REMAINING_AFTER_600)
        self.assertTrue(STANDING_CYCLE268_3GRAM_IS_NOT_REMAINING_AFTER_600)
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_can_fail(self):
        """Boolean is True only when remaining=37 and some G has unique K≥2."""
        provider = MockProvider()
        leftover = STANDING_LEFTOVER_SITES
        stems = leftover_extra_previous_stems(load_i_sides(), leftover, GRAM2)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_unique_previous_stem(
                leftover,
                stems,
            )
        )
        rem = leftover_extra_remaining_after_600(leftover, stems)
        rem_stems = leftover_extra_remaining_after_600_previous_stems(leftover, stems)
        self.assertEqual(len(rem), STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(len(rem), 37)
        self.assertEqual(rem, STANDING_REMAINING_SITES)
        self.assertEqual(rem_stems, STANDING_REMAINING_PREVIOUS_STEMS)
        g, k, unique = select_remaining_after_600_g(rem_stems)
        self.assertEqual(g, "090")
        self.assertEqual(k, 2)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        empty_stems = ("999",) * len(leftover)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_unique_previous_stem(
                leftover,
                empty_stems,
            )
        )
        unique_stems = list(stems)
        for i, site in enumerate(leftover):
            if site == (SIDE_IA, "Ia1", 27):
                unique_stems[i] = "090"
        unique_planted = tuple(unique_stems)
        uniq_g, uniq_k, uniq_unique = select_remaining_after_600_g(
            leftover_extra_remaining_after_600_previous_stems(leftover, unique_planted)
        )
        self.assertEqual(uniq_g, "090")
        self.assertEqual(uniq_k, 3)
        self.assertTrue(uniq_unique)
        self.assertEqual(
            len(leftover_extra_remaining_after_600(leftover, unique_planted)),
            37,
        )
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_600_unique_previous_stem(
                leftover,
                unique_planted,
            )
        )
        hapax_stems = list(stems)
        replacements = {
            (SIDE_IA, "Ia14", 105): "801",
            (SIDE_IA, "Ia13", 152): "802",
            (SIDE_IA, "Ia7", 88): "803",
            (SIDE_IA, "Ia2", 37): "804",
            (SIDE_IA, "Ia5", 164): "805",
        }
        for i, site in enumerate(leftover):
            if site in replacements:
                hapax_stems[i] = replacements[site]
        hapax = tuple(hapax_stems)
        hap_g, hap_k, hap_unique = select_remaining_after_600_g(
            leftover_extra_remaining_after_600_previous_stems(leftover, hapax)
        )
        self.assertEqual(hap_k, 1)
        self.assertFalse(hap_unique)
        self.assertEqual(len(leftover_extra_remaining_after_600(leftover, hapax)), 37)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_unique_previous_stem(
                leftover,
                hapax,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_600_unique_previous_stem",
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(2 + 35, 37)
        self.assertEqual(
            STANDING_K_600 + STANDING_N_REMAINING_AFTER_600,
            STANDING_N_REMAINING_AFTER_999,
        )
        self.assertEqual(4 + 37, 41)
        self.assertEqual(STANDING_K_999 + STANDING_N_REMAINING_AFTER_999, STANDING_N_LEFTOVER)
        self.assertEqual(15 + 41, 56)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal remaining-after-600 counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"090": 2, "076": 2, "045": 2})
        ranked = rank_remaining_after_600_previous_stems(counts)
        self.assertEqual(ranked[0], ("090", 2))
        self.assertEqual(ranked[1], ("076", 2))
        self.assertEqual(ranked[2], ("045", 2))
        self.assertEqual(select_remaining_after_600_g(("090", "045", "090", "045"))[0], "090")
        self.assertFalse(select_remaining_after_600_g(("090", "045", "090", "045"))[2])
        self.assertEqual(select_remaining_after_600_g(("090", "090", "045"))[0], "090")
        self.assertTrue(select_remaining_after_600_g(("090", "090", "045"))[2])
        self.assertEqual(select_remaining_after_600_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE266)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE266)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertTrue(CYCLE266_UNIQUE)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-600 previous-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.previous_stems = leftover_extra_previous_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.backwards = leftover_extra_backward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.previous_4grams = leftover_extra_previous_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.share_999 = leftover_extra_with_previous_999(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_after_999 = leftover_extra_remaining_after_999(
            self.leftover_sites,
            self.previous_stems,
        )
        self.share_600 = leftover_extra_remaining_after_999_with_g(
            self.leftover_sites,
            self.previous_stems,
            "600",
        )
        self.remaining = leftover_extra_remaining_after_600(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_stems = leftover_extra_remaining_after_600_previous_stems(
            self.leftover_sites,
            self.previous_stems,
        )
        self.with_previous = leftover_extra_remaining_after_600_with_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.no_previous = leftover_extra_remaining_after_600_without_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.matching = leftover_extra_remaining_after_600_with_g(
            self.leftover_sites,
            self.previous_stems,
        )
        self.without = leftover_extra_remaining_after_600_without_g(
            self.leftover_sites,
            self.previous_stems,
        )
        self.frequency = remaining_after_600_previous_stem_frequency_table(
            self.leftover_sites,
            self.previous_stems,
            self.backwards,
        )
        self.matching_previous_4grams = leftover_extra_previous_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = CYCLE224_N_INSIDE
        self.n_leftover = len(self.leftover_sites)
        self.n_leftover_extra = self.n_leftover
        self.k_999 = len(self.share_999)
        self.n_remaining_after_999 = len(self.remaining_after_999)
        self.k_600 = len(self.share_600)
        self.n_remaining = len(self.remaining)
        self.n_with_previous = len(self.with_previous)
        self.n_no_previous = len(self.no_previous)
        self.n_distinct = len(self.frequency)
        self.g, self.k, self.unique = select_remaining_after_600_g(self.remaining_stems)
        self.n_without = len(self.without)
        self.claim_holds = i_leftover_extra_090_076_remaining_after_600_unique_previous_stem(
            self.leftover_sites,
            self.previous_stems,
        )

    def test_tokens_and_nested_leftover_extra_56_69_k999_15_k600_4_not_retuned(self):
        """2-gram and leftover extra 56 / N_I=69 / K_999=15 / K_600=4 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("090", "090", "076"))
        self.assertEqual(GRAM3_NESTED_600, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_999, ("999", "090", "076"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE260_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        prior_269 = self.survey["i_600_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_269["cycle"], 269)
        self.assertEqual(prior_269["N_i_only"], 6)
        self.assertEqual(prior_269["N_not_i_only"], 0)
        self.assertEqual(prior_269["N_not_hapax"], 0)
        self.assertTrue(prior_269["i_600_090_076_previous_4grams_all_i_only_hapax"])
        self.assertTrue(CYCLE269_ALL_HAPAX)
        self.assertEqual(CYCLE269_N_I_ONLY, 6)
        self.assertEqual(CYCLE269_N_NOT_HAPAX, 0)
        prior_268 = self.survey["i_3gram_600_090_076_i_only"]
        self.assertEqual(prior_268["cycle"], 268)
        self.assertEqual(prior_268["N_I"], 6)
        self.assertEqual(prior_268["N_off_I"], 0)
        self.assertEqual(prior_268["N_extra"], 2)
        self.assertTrue(prior_268["i_3gram_600_090_076_i_only"])
        prior_267 = self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]
        self.assertEqual(prior_267["cycle"], 267)
        self.assertEqual(prior_267["K_600"], 4)
        self.assertEqual(prior_267["N_remaining_after_600"], 37)
        self.assertTrue(
            prior_267[
                "i_leftover_extra_090_076_remaining_after_999_exactly_4_share_previous_600"
            ]
        )
        self.assertTrue(CYCLE267_CLAIM)
        self.assertEqual(CYCLE267_K_600, 4)
        self.assertEqual(CYCLE267_N_REMAINING_AFTER_600, 37)
        prior_266 = self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]
        self.assertEqual(prior_266["cycle"], 266)
        self.assertEqual(prior_266["G"], "600")
        self.assertEqual(prior_266["K"], 4)
        self.assertEqual(prior_266["N_distinct_remaining"], 33)
        self.assertTrue(prior_266["G_uniquely_most_frequent"])
        self.assertTrue(
            prior_266["i_leftover_extra_090_076_remaining_after_999_unique_previous_stem"]
        )
        self.assertTrue(CYCLE266_CLAIM)
        self.assertEqual(CYCLE266_G, "600")
        self.assertEqual(CYCLE266_K, 4)
        self.assertEqual(CYCLE266_N_DISTINCT, 33)
        prior_261 = self.survey["i_leftover_extra_090_076_previous_999"]
        self.assertEqual(prior_261["cycle"], 261)
        self.assertEqual(prior_261["K_999"], 15)
        self.assertEqual(prior_261["N_remaining_after_999"], 41)
        self.assertTrue(prior_261["i_leftover_extra_090_076_exactly_15_share_previous_999"])
        self.assertTrue(CYCLE261_CLAIM)
        self.assertEqual(CYCLE261_K_999, 15)
        self.assertEqual(CYCLE261_N_REMAINING_AFTER_999, 41)
        prior_260 = self.survey["i_leftover_extra_090_076_previous_stem"]
        self.assertEqual(prior_260["cycle"], 260)
        self.assertEqual(prior_260["N_distinct_previous_stems"], 34)
        self.assertEqual(prior_260["G"], "999")
        self.assertEqual(prior_260["K"], 15)
        self.assertFalse(prior_260["i_leftover_extra_090_076_share_one_previous_stem"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertTrue(prior_167["i_3gram_999_090_076_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE268_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE269_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_37_remaining_g_090_k_2_five_way_tie_and_hypothesis_loses(self):
        """N_remaining=37, N_distinct=32, G=090 K=2 five-way tie. Claim loses."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.k_999, STANDING_K_999)
        self.assertEqual(STANDING_K_999, 15)
        self.assertEqual(self.share_999, CYCLE261_MATCHING_SITES)
        if self.k_999 != 15:
            self.fail("nested cycle 261 K_999 drifted from 15")
        self.assertEqual(self.n_remaining_after_999, STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(STANDING_N_REMAINING_AFTER_999, 41)
        self.assertEqual(self.remaining_after_999, CYCLE266_REMAINING_SITES)
        self.assertEqual(self.k_600, STANDING_K_600)
        self.assertEqual(STANDING_K_600, 4)
        self.assertEqual(self.share_600, CYCLE267_MATCHING_SITES)
        self.assertEqual(self.share_600, CYCLE266_MATCHING_SITES)
        if self.k_600 != 4:
            self.fail("nested cycle 267 K_600 drifted from 4")
        self.assertTrue(
            leftover_extra_remaining_after_600_nested_counts_hold(
                self.n_i,
                self.n_leftover,
                self.k_999,
                self.n_remaining_after_999,
                self.k_600,
                self.n_remaining,
            )
        )
        self.assertTrue(
            leftover_extra_remaining_after_999_nested_counts_hold(
                self.n_i,
                self.n_leftover,
                self.k_999,
                self.n_remaining_after_999,
            )
        )
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(STANDING_N_REMAINING_AFTER_600, 37)
        self.assertEqual(self.n_remaining, CYCLE267_N_REMAINING_AFTER_600)
        self.assertEqual(self.n_remaining, self.n_remaining_after_999 - self.k_600)
        self.assertEqual(41 - 4, 37)
        if self.n_remaining != 37:
            self.fail("measured N_remaining_after_600 drifted from 37")
        if self.n_remaining != self.n_remaining_after_999 - self.k_600:
            self.fail("leftover extra remaining-after-600 filter disagrees with nested 41−4")
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_PREVIOUS_STEMS)
        self.assertEqual(len(self.remaining), len(self.remaining_stems))
        self.assertEqual(
            self.remaining,
            leftover_extra_remaining_after_999_without_previous_600(
                self.leftover_sites,
                self.previous_stems,
            ),
        )
        self.assertEqual(
            self.remaining,
            leftover_extra_remaining_after_999_without_g(
                self.leftover_sites,
                self.previous_stems,
                "600",
            ),
        )
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 37)
        self.assertEqual(self.n_no_previous, STANDING_N_NO_PREVIOUS)
        self.assertEqual(STANDING_N_NO_PREVIOUS, 0)
        self.assertEqual(self.no_previous, STANDING_NO_PREVIOUS_SITES)
        self.assertEqual(self.n_with_previous + self.n_no_previous, self.n_remaining)
        self.assertEqual(37 + 0, 37)
        for site in self.share_999:
            self.assertNotIn(site, self.remaining)
        for site in self.share_600:
            self.assertNotIn(site, self.remaining)
        for site in CYCLE267_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
        for site in CYCLE266_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING, 32)
        self.assertEqual(self.frequency, STANDING_REMAINING_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "090")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 2)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "090")
        self.assertEqual(self.frequency[0][1], 2)
        tied = tuple(stem for stem, count, _sites, _grams in self.frequency if count == 2)
        self.assertEqual(tied, STANDING_TIED_STEMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 5)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX_REMAINING)
        self.assertEqual(STANDING_N_HAPAX_REMAINING, 27)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 35)
        self.assertEqual(self.k + self.n_without, self.n_remaining)
        self.assertEqual(2 + 35, 37)
        leftover_g, leftover_k, leftover_unique = select_previous_g(self.previous_stems)
        self.assertEqual(leftover_g, "999")
        self.assertEqual(leftover_k, 15)
        self.assertTrue(leftover_unique)
        leftover_ranked = rank_previous_stems(
            Counter(stem for stem in self.previous_stems if stem is not None)
        )
        self.assertEqual(leftover_ranked[0], ("999", 15))
        self.assertEqual(leftover_ranked[1], ("600", 4))
        rem999_g, rem999_k, rem999_unique = select_remaining_after_999_g(
            leftover_extra_remaining_after_999_previous_stems(
                self.leftover_sites,
                self.previous_stems,
            )
        )
        self.assertEqual(rem999_g, "600")
        self.assertEqual(rem999_k, 4)
        self.assertTrue(rem999_unique)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_600_unique_previous_stem(
                self.leftover_sites,
                self.previous_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM,
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE266)
        self.assertFalse(STANDING_SAME_AS_CYCLE267)
        self.assertFalse(STANDING_SAME_AS_CYCLE268)
        self.assertFalse(STANDING_SAME_AS_CYCLE269)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE266)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_CYCLE269_PREVIOUS_4GRAMS_ARE_NOT_REMAINING_AFTER_600)
        self.assertTrue(STANDING_CYCLE268_3GRAM_IS_NOT_REMAINING_AFTER_600)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertTrue(CYCLE266_CLAIM)
        self.assertTrue(CYCLE267_CLAIM)
        self.assertTrue(CYCLE268_CLAIM)
        self.assertTrue(CYCLE269_ALL_HAPAX)
        self.assertFalse(CYCLE256_CLAIM)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertEqual(CYCLE266_N_DISTINCT, 33)
        self.assertEqual(CYCLE256_N_REMAINING11, 19)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertEqual(CYCLE234_K, 2)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_remaining_after_600_g_is_090_by_tie_break(self):
        """Tie-break G=090 is two leftover extra remaining-after-600 sites."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_previous_4grams, STANDING_MATCHING_PREVIOUS_4GRAMS)
        expected = tuple(
            zip(STANDING_MATCHING_SITES, STANDING_MATCHING_PREVIOUS_4GRAMS, strict=True)
        )
        for (site, prev4), (want_site, want_prev) in zip(
            zip(self.matching, self.matching_previous_4grams, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N2]), GRAM3_BACKWARD)
            self.assertEqual(stems[index - 1], "090")
            self.assertEqual(site_previous_stem(stems, index, GRAM2), "090")
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), GRAM3_BACKWARD)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), want_prev)
            self.assertEqual(prev4, want_prev)
            self.assertEqual(site, want_site)
            self.assertEqual(prev4[1:], GRAM3_BACKWARD)
            self.assertEqual(len(prev4), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_REMAINING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE261_MATCHING_SITES)
            self.assertNotIn(site, CYCLE267_MATCHING_SITES)
            self.assertNotIn(site, CYCLE266_MATCHING_SITES)
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            prev = site_previous_stem(stems, index, GRAM2)
            self.assertIsNotNone(prev)
            self.assertNotEqual(prev, "090")
            self.assertNotEqual(prev, "600")
            self.assertNotEqual(prev, "999")
            self.assertIn(site, STANDING_REMAINING_SITES)
        for site in self.share_999:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE261_MATCHING_SITES)
        for site in self.share_600:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE267_MATCHING_SITES)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, prev4, _nxt4), want in zip(
            local,
            STANDING_MATCHING_PREVIOUS_4GRAMS,
            strict=True,
        ):
            self.assertEqual(prev4, want)
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_269_268_267_266_261_260_223_and_207_still_compute(self):
        """Cycle 269 6/0 hapax, 268 6/0 extra I=2, 267 K_600=4/37, 266 G=600 K=4 distinct=33, 261 K_999=15, 260 34/999/15, 223 69/3, 207 8/1 stay."""
        prior_269 = TestMamariI600090076Previous4gramsIOnlyScoreboard()
        prior_269.setUp()
        prior_269.test_all_4grams_are_i_only_hapax_and_claim_holds()
        prior_269.test_survey_matches_computed_lock()
        self.assertEqual(prior_269.n_i_only, 6)
        self.assertEqual(prior_269.n_not_i_only, 0)
        self.assertEqual(prior_269.n_not_hapax, 0)
        self.assertTrue(prior_269.claim_holds)
        self.assertTrue(CYCLE269_ALL_HAPAX)
        self.assertEqual(CYCLE269_N_I_ONLY, 6)
        self.assertEqual(CYCLE269_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE269_N_NOT_HAPAX, 0)
        if (
            prior_269.n_i_only != 6
            or prior_269.n_not_i_only != 0
            or prior_269.n_not_hapax != 0
            or not prior_269.claim_holds
        ):
            self.fail("nested cycle 269 6/0 hapax drifted")
        prior_268 = TestMamariI3gram600090076IOnlyScoreboard()
        prior_268.setUp()
        prior_268.test_i_hits_are_six_on_ia_and_leftover_extra_600_is_subset()
        prior_268.test_3gram_is_zero_off_i_and_i_only()
        prior_268.test_survey_matches_computed_lock()
        self.assertEqual(prior_268.i_hits, 6)
        self.assertEqual(prior_268.off_i_hits, 0)
        self.assertEqual(prior_268.i_sites, CYCLE268_I_SITES)
        self.assertEqual(len(prior_268.extra), 2)
        self.assertEqual(prior_268.extra, CYCLE268_EXTRA_I_SITES)
        self.assertEqual(CYCLE268_N_I, 6)
        self.assertEqual(CYCLE268_N_OFF_I, 0)
        self.assertEqual(CYCLE268_N_EXTRA, 2)
        self.assertTrue(CYCLE268_CLAIM)
        if prior_268.i_hits != 6 or prior_268.off_i_hits != 0 or len(prior_268.extra) != 2:
            self.fail("nested cycle 268 600 090 076 leftover extra previous I-only 6/0 extra I=2 drifted")
        prior_267 = TestMamariILeftoverExtra090076RemainingAfter999Previous600Scoreboard()
        prior_267.setUp()
        prior_267.test_counts_4_of_41_and_hypothesis_k_4_holds()
        prior_267.test_survey_matches_computed_lock()
        self.assertEqual(prior_267.k_600, 4)
        self.assertEqual(prior_267.n_remaining_after_600, 37)
        self.assertTrue(prior_267.claim_holds)
        self.assertTrue(CYCLE267_CLAIM)
        self.assertEqual(CYCLE267_K_600, 4)
        self.assertEqual(CYCLE267_N_REMAINING_AFTER_600, 37)
        self.assertEqual(CYCLE267_G, "600")
        if (
            prior_267.k_600 != 4
            or prior_267.n_remaining_after_600 != 37
            or not prior_267.claim_holds
        ):
            self.fail(
                "nested cycle 267 leftover extra remaining-after-999 previous-600 "
                "K_600=4 N_remaining_after_600=37 drifted"
            )
        prior_266 = TestMamariILeftoverExtra090076RemainingAfter999PreviousStemScoreboard()
        prior_266.setUp()
        prior_266.test_counts_41_remaining_g_600_k_4_and_hypothesis_holds()
        prior_266.test_survey_matches_computed_lock()
        self.assertEqual(prior_266.g, "600")
        self.assertEqual(prior_266.k, 4)
        self.assertEqual(prior_266.n_remaining, 41)
        self.assertEqual(prior_266.n_distinct, 33)
        self.assertTrue(prior_266.unique)
        self.assertTrue(prior_266.claim_holds)
        self.assertTrue(CYCLE266_CLAIM)
        self.assertEqual(CYCLE266_G, "600")
        self.assertEqual(CYCLE266_K, 4)
        self.assertEqual(CYCLE266_N_REMAINING, 41)
        self.assertEqual(CYCLE266_N_DISTINCT, 33)
        if (
            prior_266.g != "600"
            or prior_266.k != 4
            or prior_266.n_remaining != 41
            or prior_266.n_distinct != 33
            or not prior_266.unique
            or not prior_266.claim_holds
        ):
            self.fail(
                "nested cycle 266 unique-max G=600 K=4 N_remaining=41 distinct=33 drifted"
            )
        prior_261 = TestMamariILeftoverExtra090076Previous999Scoreboard()
        prior_261.setUp()
        prior_261.test_counts_15_of_56_and_hypothesis_k_15_holds()
        prior_261.test_survey_matches_computed_lock()
        self.assertEqual(prior_261.k_999, 15)
        self.assertEqual(prior_261.n_remaining_after_999, 41)
        self.assertEqual(prior_261.n_leftover_extra, 56)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertEqual(CYCLE261_K_999, 15)
        self.assertEqual(CYCLE261_N_REMAINING_AFTER_999, 41)
        self.assertEqual(CYCLE261_N_LEFTOVER_EXTRA, 56)
        if (
            prior_261.k_999 != 15
            or prior_261.n_remaining_after_999 != 41
            or prior_261.n_leftover_extra != 56
        ):
            self.fail("nested cycle 261 leftover extra previous-999 K_999=15 N_remaining=41 drifted")
        prior_260 = TestMamariILeftoverExtra090076PreviousStemScoreboard()
        prior_260.setUp()
        prior_260.test_counts_34_distinct_previous_stems_and_claim_loses()
        prior_260.test_survey_matches_computed_lock()
        self.assertEqual(prior_260.n_distinct, 34)
        self.assertEqual(CYCLE260_G, "999")
        self.assertEqual(CYCLE260_K, 15)
        self.assertTrue(CYCLE260_UNIQUE)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertEqual(CYCLE260_N_LEFTOVER, 56)
        if prior_260.n_distinct != 34 or CYCLE260_G != "999" or CYCLE260_K != 15:
            self.fail("nested cycle 260 34 distinct G=999 K=15 drifted")
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
        self.assertFalse(CYCLE256_UNIQUE)
        if (
            prior_256.n_remaining11 != 19
            or prior_256.k != 1
            or prior_256.g != "755"
            or prior_256.unique
        ):
            self.fail("nested cycle 256 unique-max false N_remaining11=19 K=1 G=755 drifted")
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
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(prior_167.i_hits, 16)
        self.assertEqual(prior_167.off_i_hits, 0)
        self.assertTrue(CYCLE167_CLAIM)
        self.assertEqual(CYCLE167_N_I, 16)
        self.assertEqual(CYCLE167_N_OFF_I, 0)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE268_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE269_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-270 leftover extra remaining-after-600 lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]
        self.assertEqual(lock["cycle"], 270)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(tuple(lock["backward_3gram"]), ("090", "090", "076"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(
            tuple(lock["locked_previous_stems_after_600"]),
            LOCKED_PREVIOUS_STEMS_AFTER_600,
        )
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_previous_leftover"], STANDING_N_WITH_PREVIOUS_LEFTOVER)
        self.assertEqual(lock["N_no_previous_leftover"], STANDING_N_NO_PREVIOUS_LEFTOVER)
        self.assertEqual(lock["K_999"], STANDING_K_999)
        self.assertEqual(lock["K_999"], 15)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_999_sites"]),
            CYCLE261_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_999"], STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(lock["N_remaining_after_999"], 41)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_999_sites"]),
            CYCLE266_REMAINING_SITES,
        )
        self.assertEqual(lock["K_600"], STANDING_K_600)
        self.assertEqual(lock["K_600"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_600_sites"]),
            CYCLE267_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_600"], STANDING_N_REMAINING_AFTER_600)
        self.assertEqual(lock["N_remaining_after_600"], 37)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_600_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_600_previous_stems"]),
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 37)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(lock["N_distinct_remaining"], STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(lock["N_distinct_remaining"], 32)
        self.assertEqual(lock["N_hapax_remaining"], STANDING_N_HAPAX_REMAINING)
        self.assertEqual(lock["N_hapax_remaining"], 27)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "090")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 5)
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 35)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_600_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_after_600_local_4grams"],
            matching_leftover_extra_remaining_after_600_local_4gram_rows(),
        )
        self.assertEqual(
            lock["remaining_after_600_previous_stem_frequency"],
            remaining_after_600_previous_stem_frequency_rows(),
        )
        self.assertEqual(lock["nested_cycle269_N_i_only"], 6)
        self.assertEqual(lock["nested_cycle269_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle269_N_not_hapax"], 0)
        self.assertTrue(lock["nested_cycle269_all_i_only_hapax"])
        self.assertEqual(lock["nested_cycle268_N_I"], 6)
        self.assertEqual(lock["nested_cycle268_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle268_N_extra"], 2)
        self.assertEqual(lock["nested_cycle267_K_600"], 4)
        self.assertEqual(lock["nested_cycle267_N_remaining_after_600"], 37)
        self.assertEqual(lock["nested_cycle266_G"], "600")
        self.assertEqual(lock["nested_cycle266_K"], 4)
        self.assertEqual(lock["nested_cycle266_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle266_N_distinct_remaining"], 33)
        self.assertTrue(lock["nested_cycle266_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle261_K_999"], 15)
        self.assertEqual(lock["nested_cycle261_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle260_N_distinct_previous_stems"], 34)
        self.assertEqual(lock["nested_cycle260_G"], "999")
        self.assertEqual(lock["nested_cycle260_K"], 15)
        self.assertFalse(lock["nested_cycle260_share_one_previous_stem"])
        self.assertEqual(lock["nested_cycle256_N_remaining11"], 19)
        self.assertEqual(lock["nested_cycle256_K"], 1)
        self.assertEqual(lock["nested_cycle256_G"], "755")
        self.assertFalse(lock["nested_cycle256_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["nested_cycle234_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_extra_090_076_remaining_after_600_unique_previous_stem"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle234"])
        self.assertFalse(lock["same_as_cycle256"])
        self.assertFalse(lock["same_as_cycle266"])
        self.assertFalse(lock["same_as_cycle267"])
        self.assertFalse(lock["same_as_cycle268"])
        self.assertFalse(lock["same_as_cycle269"])
        self.assertTrue(lock["same_claim_shape_as_cycle234"])
        self.assertTrue(lock["same_claim_shape_as_cycle256"])
        self.assertTrue(lock["same_claim_shape_as_cycle266"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["cycle269_previous_4grams_are_not_remaining_after_600"])
        self.assertTrue(lock["cycle268_3gram_is_not_remaining_after_600"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle167_not_overwritten"])
        self.assertTrue(lock["cycle268_not_overwritten"])
        self.assertTrue(lock["cycle269_not_overwritten"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["g_k_is_inventory_for_later_peel"])
        self.assertTrue(lock["raw_stems_090_kept"])
        self.assertTrue(lock["standing_i_600_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_600_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_600_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_600_090_076_previous_4grams_i_only"]["cycle"], 269)
        self.assertEqual(self.survey["i_600_090_076_previous_4grams_i_only"]["N_i_only"], 6)
        self.assertEqual(self.survey["i_600_090_076_previous_4grams_i_only"]["N_not_hapax"], 0)
        self.assertTrue(
            self.survey["i_600_090_076_previous_4grams_i_only"][
                "i_600_090_076_previous_4grams_all_i_only_hapax"
            ]
        )
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["cycle"], 268)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_extra"], 2)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["cycle"],
            267,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"]["K_600"],
            4,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_600"][
                "N_remaining_after_600"
            ],
            37,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]["cycle"],
            266,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]["G"],
            "600",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]["K"],
            4,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"][
                "N_distinct_remaining"
            ],
            33,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"][
                "i_leftover_extra_090_076_remaining_after_999_unique_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["cycle"], 261)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["K_999"], 15)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_previous_999"]["N_remaining_after_999"],
            41,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_stem"]["cycle"], 260)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
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


class TestMamariILeftoverExtra090076RemainingAfter600PreviousStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 270 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
