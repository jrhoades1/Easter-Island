"""I's cycle-265 leftover extra remaining-after-999 previous-stem lock.

Cycle 266 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover extra I sites of 2-gram 090 076 (the 56 I
sites that do not sit inside leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover extra sites, the leftover n=4 set, or
the already-closed leftover remaining family. Does not retune
the forward peel of leftover extra I 090 076 (cycles 225–259).
Does not overwrite cycle 167's 3-gram I-only 16/0 lock. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Cycle 260 lost share-one-previous-stem: 34 distinct, G=999
K=15. Cycle 261 leftover extra exactly 15 share previous 999
HOLDS; N_remaining_after_999=41. Cycles 262–265 peeled the
I 999 090 076 previous-4-gram K=2 ties (000 and 090). Those
are previous tokens of I 999 090 076, not leftover extra
remaining-after-999 previous stems. Leftover extra remaining-
after-999 previous stems are not yet locked. This cycle is
the unique-max claim on leftover extra remaining-after-999
(same claim-shape as cycle 256 remaining-after-000 next-stem
and cycle 234 remaining-after-001 next-stem), previous
direction instead of next-stem. Do not peel a specific
remaining previous stem this cycle. Do not retune leftover
n=4. Do not retune the forward peel. Off-I T sites are not
this cycle.

Leftover extra remaining-after-999 = leftover extra I 090 076
sites whose previous token is not 999. For each such site,
take the previous token if any (lock line-initial /
no-previous count separately). Nested-check leftover extra
I 090 076 == 56, N_I==69, K_999==15, N_remaining_after_999==41
(do not retune 223/224/260/261). Nested-check cycle 265
K_000==2 and cycle 264 K_090==2 (do not retune). Measure
previous-stem frequencies among remaining-after-999 sites
that have a previous token. G = the previous stem with the
highest remaining-after-999 with-previous count. If a tie,
pick the larger Barthel id. K = that count.

Claim that can lose:
i_leftover_extra_090_076_remaining_after_999_unique_previous_stem.
True iff remaining-after-999 leftover extra I 090 076 has a
unique most frequent previous stem G with K ≥ 2 (no tie at
max K). This can lose the same way cycle 234 lost (7-way tie
at 2) and cycle 256 lost (19 hapax K=1). Unique-max G/K is
inventory for a later peel if the claim loses with K≥2;
all-hapax K=1 is the other lose path. Measured: N_remaining=41,
N_with_previous=41, N_no_previous=0, N_distinct=33, unique-max
G=600 K=4 at Ia2[114]/Ia2[128]/Ia2[154]/Ia7[113]. The claim
is true. Nested cycle 265 K_000=2, cycle 264 K_090=2, cycle
263 14/0 N_not_hapax=2, cycle 262 16/0 extra I=1, cycle 261
K_999=15 N_remaining=41, cycle 260 34 distinct G=999 K=15,
cycle 256 unique-max false N_remaining11=19 K=1 G=755, cycle
223 69/3, and cycle 207 8/1 on T stay. Do not assume the
result; measure. Do not retune.

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
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_leftover_extra_previous_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE262_EXTRA_I_SITES,
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE262_CLAIM,
    STANDING_I_SITES as CYCLE262_I_SITES,
    STANDING_N_EXTRA as CYCLE262_N_EXTRA,
    STANDING_N_I as CYCLE262_N_I,
    STANDING_N_OFF_I as CYCLE262_N_OFF_I,
    TestMamariI3gram999090076LeftoverExtraPreviousIOnlyScoreboard,
)
from tests.test_mamari_i_999_090_076_previous_000_scoreboard import (
    STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_000 as CYCLE265_CLAIM,
    STANDING_K_000 as CYCLE265_K_000,
    STANDING_MATCHING_SITES as CYCLE265_MATCHING_SITES,
    TestMamariI999090076Previous000Scoreboard,
)
from tests.test_mamari_i_999_090_076_previous_090_scoreboard import (
    STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_090 as CYCLE264_CLAIM,
    STANDING_K_000 as CYCLE264_K_000,
    STANDING_K_090 as CYCLE264_K_090,
    STANDING_MATCHING_SITES as CYCLE264_MATCHING_SITES,
    TestMamariI999090076Previous090Scoreboard,
)
from tests.test_mamari_i_999_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE263_ALL_HAPAX,
    STANDING_N_I_ONLY as CYCLE263_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE263_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE263_N_NOT_I_ONLY,
    TestMamariI999090076Previous4gramsIOnlyScoreboard,
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
    STANDING_N_NO_PREVIOUS as CYCLE260_N_NO_PREVIOUS,
    STANDING_N_WITH_PREVIOUS as CYCLE260_N_WITH_PREVIOUS,
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
LOCKED_PREVIOUS_STEMS_AFTER_999 = (LOCKED_PREVIOUS_STEM_999,)
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_BACKWARD = ("600", "090", "076")
GRAM3_NESTED_999 = ("999", "090", "076")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS_LEFTOVER = 56
STANDING_N_NO_PREVIOUS_LEFTOVER = 0
STANDING_K_999 = 15
STANDING_N_REMAINING_AFTER_999 = 41
STANDING_N_WITH_PREVIOUS = 41
STANDING_N_NO_PREVIOUS = 0
STANDING_NO_PREVIOUS_SITES = ()
STANDING_N_DISTINCT_REMAINING = 33
STANDING_N_HAPAX_REMAINING = 27
STANDING_G = "600"
STANDING_K = 4
STANDING_N_WITHOUT_G = 37
STANDING_N_TIED_AT_K = 1
STANDING_TIED_STEMS = ("600",)
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_REMAINING_SITES = (
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 37),
    (SIDE_IA, "Ia2", 114),
    (SIDE_IA, "Ia2", 128),
    (SIDE_IA, "Ia2", 154),
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
    (SIDE_IA, "Ia7", 113),
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
    "600",
    "600",
    "600",
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
    "600",
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
    (SIDE_IA, "Ia2", 114),
    (SIDE_IA, "Ia2", 128),
    (SIDE_IA, "Ia2", 154),
    (SIDE_IA, "Ia7", 113),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("076", "600", "090", "076"),
    ("070", "600", "090", "076"),
    ("455", "600", "090", "076"),
    ("168", "600", "090", "076"),
)
STANDING_REMAINING_FREQUENCY = (
    (
        "600",
        4,
        (
            (SIDE_IA, "Ia2", 114),
            (SIDE_IA, "Ia2", 128),
            (SIDE_IA, "Ia2", 154),
            (SIDE_IA, "Ia7", 113),
        ),
        (("600", "090", "076"),) * 4,
    ),
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
STANDING_CLAIM = "i_leftover_extra_090_076_remaining_after_999_unique_previous_stem"
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_UNIQUE_PREVIOUS_STEM = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_999_previous_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE234 = False
STANDING_SAME_AS_CYCLE256 = False
STANDING_SAME_AS_CYCLE260 = False
STANDING_SAME_AS_CYCLE261 = False
STANDING_SAME_AS_CYCLE264 = False
STANDING_SAME_AS_CYCLE265 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE265_PREVIOUS_000_IS_NOT_REMAINING_AFTER_999 = True
STANDING_CYCLE264_PREVIOUS_090_IS_NOT_REMAINING_AFTER_999 = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE167_NOT_OVERWRITTEN = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL = True


def leftover_extra_remaining_after_999(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_999,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites whose previous token is not 999 (includes no-previous)."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev not in locked_set
    )


def leftover_extra_remaining_after_999_previous_stems(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_999,
) -> tuple[str, ...]:
    """Previous stems of remaining-after-999 sites that have a previous token."""
    locked_set = set(locked)
    return tuple(
        prev
        for prev in previous_stems
        if prev is not None and prev not in locked_set
    )


def leftover_extra_remaining_after_999_with_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_999,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-999 leftover extra sites that have a previous token."""
    remaining = leftover_extra_remaining_after_999(sites, previous_stems, locked)
    rem_prev = tuple(
        prev
        for site, prev in zip(sites, previous_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_with_previous(remaining, rem_prev)


def leftover_extra_remaining_after_999_without_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_999,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-999 leftover extra sites with no previous token."""
    remaining = leftover_extra_remaining_after_999(sites, previous_stems, locked)
    rem_prev = tuple(
        prev
        for site, prev in zip(sites, previous_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_without_previous(remaining, rem_prev)


def leftover_extra_remaining_after_999_with_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_999,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-999 sites whose previous token is G."""
    remaining = set(leftover_extra_remaining_after_999(sites, previous_stems, locked))
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev == stem and site in remaining
    )


def leftover_extra_remaining_after_999_without_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_999,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-999 sites whose previous token is not G."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev is not None and prev not in locked_set and prev != stem
    )


def remaining_after_999_previous_stem_counts(previous_stems: tuple[str, ...]) -> Counter:
    """Counts of previous stems among leftover extra remaining-after-999 with-previous."""
    return Counter(previous_stems)


def rank_remaining_after_999_previous_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Remaining-after-999 previous stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_remaining_after_999_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining-after-999 has no G."""
    ranked = rank_remaining_after_999_previous_stems(
        remaining_after_999_previous_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_after_999_previous_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    backward_3grams: tuple[tuple[str, ...] | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_999,
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Remaining-after-999 previous-stem frequency: highest count first, then larger id."""
    rem_sites = leftover_extra_remaining_after_999_with_previous(
        sites, previous_stems, locked
    )
    rem_stems = leftover_extra_remaining_after_999_previous_stems(
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


def remaining_after_999_previous_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_REMAINING_FREQUENCY,
) -> list[dict]:
    """Survey-shaped remaining-after-999 previous-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "previous_stem": stem,
                "count": count,
                "leftover_extra_remaining_after_999_sites": [
                    list(site) for site in sites
                ],
                "backward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def leftover_extra_remaining_after_999_nested_counts_hold(
    n_i: int,
    n_leftover: int,
    k_999: int,
    n_remaining: int,
    expected_i: int = STANDING_N_I,
    expected_leftover: int = STANDING_N_LEFTOVER,
    expected_k_999: int = STANDING_K_999,
    expected_remaining: int = STANDING_N_REMAINING_AFTER_999,
) -> bool:
    """Nested leftover extra 69/56, K_999=15, remaining-after-999=41."""
    return (
        n_i == expected_i
        and n_leftover == expected_leftover
        and k_999 == expected_k_999
        and n_remaining == expected_remaining
        and n_remaining == n_leftover - k_999
    )


def i_leftover_extra_090_076_remaining_after_999_unique_previous_stem(
    leftover_sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_999,
) -> bool:
    """True iff remaining-after-999 has a unique most frequent previous stem with K ≥ 2."""
    remaining = leftover_extra_remaining_after_999(
        leftover_sites,
        previous_stems,
        locked,
    )
    remaining_stems = leftover_extra_remaining_after_999_previous_stems(
        leftover_sites,
        previous_stems,
        locked,
    )
    if len(remaining) != STANDING_N_REMAINING_AFTER_999:
        return False
    if remaining != leftover_extra_without_previous_999(
        leftover_sites,
        previous_stems,
    ):
        return False
    gram, count, unique = select_remaining_after_999_g(remaining_stems)
    return bool(unique and gram is not None and count >= 2)


def matching_leftover_extra_remaining_after_999_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    previous_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_PREVIOUS_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining-after-999 previous-4-gram rows."""
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


class TestILeftoverExtra090076RemainingAfter999PreviousStemHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-999 previous stems. No CV, no LLM."""

    def test_remaining_after_999_requires_previous_not_999(self):
        """Remaining-after-999 excludes previous 999; line-initial is remaining, no-previous."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_999, ("999", "090", "076"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS_AFTER_999, ("999",))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_600 = ["076", "600", "090", "076", "011"]
        self.assertEqual(site_previous_stem(has_600, 2, GRAM2), "600")
        self.assertEqual(site_backward_3gram(has_600, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_600, 2, GRAM2),
            ("076", "600", "090", "076"),
        )
        has_999 = ["000", "999", "090", "076"]
        self.assertEqual(site_previous_stem(has_999, 2, GRAM2), "999")
        self.assertNotEqual(site_previous_stem(has_999, 2, GRAM2), "600")
        line_initial = ["090", "076", "012"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
        )
        planted_stems = ("600", "999", None, "045")
        rem = leftover_extra_remaining_after_999(planted_sites, planted_stems)
        self.assertEqual(rem, (planted_sites[0], planted_sites[2], planted_sites[3]))
        self.assertEqual(
            leftover_extra_remaining_after_999_previous_stems(
                planted_sites, planted_stems
            ),
            ("600", "045"),
        )
        self.assertEqual(
            leftover_extra_remaining_after_999_with_previous(
                planted_sites, planted_stems
            ),
            (planted_sites[0], planted_sites[3]),
        )
        self.assertEqual(
            leftover_extra_remaining_after_999_without_previous(
                planted_sites, planted_stems
            ),
            (planted_sites[2],),
        )
        self.assertEqual(
            leftover_extra_remaining_after_999_with_g(planted_sites, planted_stems),
            (planted_sites[0],),
        )
        self.assertNotIn(planted_sites[1], rem)
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_previous_stem(mismatch_071, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE265_PREVIOUS_000_IS_NOT_REMAINING_AFTER_999)
        self.assertTrue(STANDING_CYCLE264_PREVIOUS_090_IS_NOT_REMAINING_AFTER_999)
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_can_fail(self):
        """Boolean is True only when remaining=41 and some G has unique K≥2."""
        provider = MockProvider()
        leftover = STANDING_LEFTOVER_SITES
        stems = leftover_extra_previous_stems(load_i_sides(), leftover, GRAM2)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_999_unique_previous_stem(
                leftover,
                stems,
            )
        )
        rem = leftover_extra_remaining_after_999(leftover, stems)
        rem_stems = leftover_extra_remaining_after_999_previous_stems(leftover, stems)
        self.assertEqual(len(rem), STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(len(rem), 41)
        self.assertEqual(rem, STANDING_REMAINING_SITES)
        self.assertEqual(rem_stems, STANDING_REMAINING_PREVIOUS_STEMS)
        g, k, unique = select_remaining_after_999_g(rem_stems)
        self.assertEqual(g, "600")
        self.assertEqual(k, 4)
        self.assertTrue(unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        empty_stems = ("999",) * len(leftover)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_999_unique_previous_stem(
                leftover,
                empty_stems,
            )
        )
        tie_stems = list(stems)
        demote = ((SIDE_IA, "Ia1", 27), (SIDE_IA, "Ia1", 59))
        for i, site in enumerate(leftover):
            if site in demote:
                tie_stems[i] = "045"
        tied = tuple(tie_stems)
        tied_g, tied_k, tied_unique = select_remaining_after_999_g(
            leftover_extra_remaining_after_999_previous_stems(leftover, tied)
        )
        self.assertEqual(tied_g, "600")
        self.assertEqual(tied_k, 4)
        self.assertFalse(tied_unique)
        self.assertEqual(len(leftover_extra_remaining_after_999(leftover, tied)), 41)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_999_unique_previous_stem(
                leftover,
                tied,
            )
        )
        hapax_stems = list(stems)
        replacements = {
            (SIDE_IA, "Ia2", 128): "801",
            (SIDE_IA, "Ia2", 154): "802",
            (SIDE_IA, "Ia7", 113): "803",
            (SIDE_IA, "Ia2", 37): "804",
            (SIDE_IA, "Ia13", 152): "805",
            (SIDE_IA, "Ia5", 164): "806",
            (SIDE_IA, "Ia7", 88): "807",
            (SIDE_IA, "Ia14", 105): "808",
        }
        for i, site in enumerate(leftover):
            if site in replacements:
                hapax_stems[i] = replacements[site]
        hapax = tuple(hapax_stems)
        hap_g, hap_k, hap_unique = select_remaining_after_999_g(
            leftover_extra_remaining_after_999_previous_stems(leftover, hapax)
        )
        self.assertEqual(hap_k, 1)
        self.assertFalse(hap_unique)
        self.assertEqual(len(leftover_extra_remaining_after_999(leftover, hapax)), 41)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_999_unique_previous_stem(
                leftover,
                hapax,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_999_unique_previous_stem",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_UNIQUE_PREVIOUS_STEM
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(4 + 37, 41)
        self.assertEqual(STANDING_K_999 + STANDING_N_REMAINING_AFTER_999, STANDING_N_LEFTOVER)
        self.assertEqual(15 + 41, 56)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal remaining-after-999 counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"600": 4, "090": 2, "045": 2})
        ranked = rank_remaining_after_999_previous_stems(counts)
        self.assertEqual(ranked[0], ("600", 4))
        self.assertEqual(ranked[1], ("090", 2))
        self.assertEqual(ranked[2], ("045", 2))
        self.assertEqual(select_remaining_after_999_g(("600", "045", "600", "045"))[0], "600")
        self.assertFalse(select_remaining_after_999_g(("600", "045", "600", "045"))[2])
        self.assertEqual(select_remaining_after_999_g(("600", "600", "045"))[0], "600")
        self.assertTrue(select_remaining_after_999_g(("600", "600", "045"))[2])
        self.assertEqual(select_remaining_after_999_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter999PreviousStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-999 previous-stem lock. Mock only."""

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
        self.remaining = leftover_extra_remaining_after_999(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_stems = leftover_extra_remaining_after_999_previous_stems(
            self.leftover_sites,
            self.previous_stems,
        )
        self.with_previous = leftover_extra_remaining_after_999_with_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.no_previous = leftover_extra_remaining_after_999_without_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.matching = leftover_extra_remaining_after_999_with_g(
            self.leftover_sites,
            self.previous_stems,
        )
        self.without = leftover_extra_remaining_after_999_without_g(
            self.leftover_sites,
            self.previous_stems,
        )
        self.frequency = remaining_after_999_previous_stem_frequency_table(
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
        self.n_remaining = len(self.remaining)
        self.n_with_previous = len(self.with_previous)
        self.n_no_previous = len(self.no_previous)
        self.n_distinct = len(self.frequency)
        self.g, self.k, self.unique = select_remaining_after_999_g(self.remaining_stems)
        self.n_without = len(self.without)
        self.claim_holds = i_leftover_extra_090_076_remaining_after_999_unique_previous_stem(
            self.leftover_sites,
            self.previous_stems,
        )

    def test_tokens_and_nested_leftover_extra_56_69_k999_15_not_retuned(self):
        """2-gram and leftover extra 56 / N_I=69 / K_999=15 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("600", "090", "076"))
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
        prior_265 = self.survey["i_999_090_076_previous_000"]
        self.assertEqual(prior_265["cycle"], 265)
        self.assertEqual(prior_265["K_000"], 2)
        self.assertEqual(prior_265["K_090"], 2)
        self.assertTrue(prior_265["i_999_090_076_exactly_2_share_previous_000"])
        self.assertTrue(CYCLE265_CLAIM)
        self.assertEqual(CYCLE265_K_000, 2)
        prior_264 = self.survey["i_999_090_076_previous_090"]
        self.assertEqual(prior_264["cycle"], 264)
        self.assertEqual(prior_264["K_090"], 2)
        self.assertEqual(prior_264["K_000"], 2)
        self.assertTrue(prior_264["i_999_090_076_exactly_2_share_previous_090"])
        self.assertTrue(CYCLE264_CLAIM)
        self.assertEqual(CYCLE264_K_090, 2)
        self.assertEqual(CYCLE264_K_000, 2)
        prior_263 = self.survey["i_999_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_263["cycle"], 263)
        self.assertEqual(prior_263["N_i_only"], 14)
        self.assertEqual(prior_263["N_not_i_only"], 0)
        self.assertEqual(prior_263["N_not_hapax"], 2)
        self.assertFalse(prior_263["i_999_090_076_previous_4grams_all_i_only_hapax"])
        prior_262 = self.survey["i_3gram_999_090_076_leftover_extra_previous_i_only"]
        self.assertEqual(prior_262["cycle"], 262)
        self.assertEqual(prior_262["N_I"], 16)
        self.assertEqual(prior_262["N_off_I"], 0)
        self.assertEqual(prior_262["N_extra"], 1)
        self.assertTrue(prior_262["i_3gram_999_090_076_i_only"])
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
        prior_256 = self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]
        self.assertEqual(prior_256["cycle"], 256)
        self.assertEqual(prior_256["N_remaining11"], 19)
        self.assertEqual(prior_256["K"], 1)
        self.assertEqual(prior_256["G"], "755")
        self.assertFalse(prior_256["G_uniquely_most_frequent"])
        self.assertFalse(prior_256["i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem"])
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_41_remaining_g_600_k_4_and_hypothesis_holds(self):
        """N_remaining=41, N_distinct=33, G=600 K=4 unique. Claim holds."""
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
        self.assertTrue(
            leftover_extra_remaining_after_999_nested_counts_hold(
                self.n_i,
                self.n_leftover,
                self.k_999,
                self.n_remaining,
            )
        )
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_999)
        self.assertEqual(STANDING_N_REMAINING_AFTER_999, 41)
        self.assertEqual(self.n_remaining, CYCLE261_N_REMAINING_AFTER_999)
        self.assertEqual(self.n_remaining, self.n_leftover - self.k_999)
        self.assertEqual(56 - 15, 41)
        if self.n_remaining != 41:
            self.fail("measured N_remaining_after_999 drifted from 41")
        if self.n_remaining != self.n_leftover - self.k_999:
            self.fail("leftover extra remaining-after-999 filter disagrees with nested 56−15")
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_PREVIOUS_STEMS)
        self.assertEqual(len(self.remaining), len(self.remaining_stems))
        self.assertEqual(
            self.remaining,
            leftover_extra_without_previous_999(
                self.leftover_sites,
                self.previous_stems,
            ),
        )
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 41)
        self.assertEqual(self.n_no_previous, STANDING_N_NO_PREVIOUS)
        self.assertEqual(STANDING_N_NO_PREVIOUS, 0)
        self.assertEqual(self.no_previous, STANDING_NO_PREVIOUS_SITES)
        self.assertEqual(self.n_with_previous + self.n_no_previous, self.n_remaining)
        self.assertEqual(41 + 0, 41)
        for site in self.share_999:
            self.assertNotIn(site, self.remaining)
        for site in CYCLE265_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
        for site in CYCLE264_MATCHING_SITES:
            self.assertNotIn(site, self.remaining)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING, 33)
        self.assertEqual(self.frequency, STANDING_REMAINING_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "600")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 4)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "600")
        self.assertEqual(self.frequency[0][1], 4)
        tied = tuple(stem for stem, count, _sites, _grams in self.frequency if count == 4)
        self.assertEqual(tied, STANDING_TIED_STEMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 1)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX_REMAINING)
        self.assertEqual(STANDING_N_HAPAX_REMAINING, 27)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 37)
        self.assertEqual(self.k + self.n_without, self.n_remaining)
        self.assertEqual(4 + 37, 41)
        leftover_g, leftover_k, leftover_unique = select_previous_g(self.previous_stems)
        self.assertEqual(leftover_g, "999")
        self.assertEqual(leftover_k, 15)
        self.assertTrue(leftover_unique)
        leftover_ranked = rank_previous_stems(
            Counter(stem for stem in self.previous_stems if stem is not None)
        )
        self.assertEqual(leftover_ranked[0], ("999", 15))
        self.assertEqual(leftover_ranked[1], ("600", 4))
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_999_unique_previous_stem(
                self.leftover_sites,
                self.previous_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_UNIQUE_PREVIOUS_STEM,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_UNIQUE_PREVIOUS_STEM
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE260)
        self.assertFalse(STANDING_SAME_AS_CYCLE261)
        self.assertFalse(STANDING_SAME_AS_CYCLE264)
        self.assertFalse(STANDING_SAME_AS_CYCLE265)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_CYCLE265_PREVIOUS_000_IS_NOT_REMAINING_AFTER_999)
        self.assertTrue(STANDING_CYCLE264_PREVIOUS_090_IS_NOT_REMAINING_AFTER_999)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertTrue(CYCLE262_CLAIM)
        self.assertFalse(CYCLE263_ALL_HAPAX)
        self.assertTrue(CYCLE264_CLAIM)
        self.assertTrue(CYCLE265_CLAIM)
        self.assertFalse(CYCLE256_CLAIM)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertEqual(CYCLE256_N_REMAINING11, 19)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertEqual(CYCLE234_K, 2)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_remaining_after_999_g_is_600(self):
        """Unique-max G=600 is four leftover extra remaining-after-999 sites."""
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
            self.assertEqual(stems[index - 1], "600")
            self.assertEqual(site_previous_stem(stems, index, GRAM2), "600")
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
            self.assertNotIn(site, CYCLE265_MATCHING_SITES)
            self.assertNotIn(site, CYCLE264_MATCHING_SITES)
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            prev = site_previous_stem(stems, index, GRAM2)
            self.assertIsNotNone(prev)
            self.assertNotEqual(prev, "600")
            self.assertNotEqual(prev, "999")
            self.assertIn(site, STANDING_REMAINING_SITES)
        for site in self.share_999:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE261_MATCHING_SITES)
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
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_265_264_263_262_261_260_256_223_and_207_still_compute(self):
        """Cycle 265 K_000=2, 264 K_090=2, 263 14/0 N_not_hapax=2, 262 16/0 extra I=1, 261 15/41, 260 34/999/15, 256 19/K=1/G=755, 223 69/3, 207 8/1 stay."""
        prior_265 = TestMamariI999090076Previous000Scoreboard()
        prior_265.setUp()
        prior_265.test_counts_exactly_2_share_previous_000_and_hypothesis_holds()
        prior_265.test_survey_matches_computed_lock()
        self.assertEqual(prior_265.k_000, 2)
        self.assertEqual(prior_265.matching, CYCLE265_MATCHING_SITES)
        self.assertTrue(prior_265.claim_holds)
        self.assertTrue(CYCLE265_CLAIM)
        if prior_265.k_000 != 2 or not prior_265.claim_holds:
            self.fail("nested cycle 265 K_000=2 drifted")
        prior_264 = TestMamariI999090076Previous090Scoreboard()
        prior_264.setUp()
        prior_264.test_counts_exactly_2_share_previous_090_and_hypothesis_holds()
        prior_264.test_survey_matches_computed_lock()
        self.assertEqual(prior_264.k_090, 2)
        self.assertEqual(prior_264.k_000, 2)
        self.assertEqual(prior_264.matching, CYCLE264_MATCHING_SITES)
        self.assertTrue(prior_264.claim_holds)
        self.assertTrue(CYCLE264_CLAIM)
        self.assertEqual(CYCLE264_K_090, 2)
        self.assertEqual(CYCLE264_K_000, 2)
        if prior_264.k_090 != 2 or prior_264.k_000 != 2:
            self.fail("nested cycle 264 K_090=2 / K_000=2 drifted")
        prior_263 = TestMamariI999090076Previous4gramsIOnlyScoreboard()
        prior_263.setUp()
        prior_263.test_shared_4grams_are_i_only_not_hapax_and_claim_loses()
        prior_263.test_survey_matches_computed_lock()
        self.assertEqual(prior_263.n_i_only, 14)
        self.assertEqual(prior_263.n_not_i_only, 0)
        self.assertEqual(prior_263.n_not_hapax, 2)
        self.assertFalse(prior_263.claim_holds)
        self.assertFalse(CYCLE263_ALL_HAPAX)
        self.assertEqual(CYCLE263_N_I_ONLY, 14)
        self.assertEqual(CYCLE263_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE263_N_NOT_HAPAX, 2)
        if (
            prior_263.n_i_only != 14
            or prior_263.n_not_i_only != 0
            or prior_263.n_not_hapax != 2
            or prior_263.claim_holds
        ):
            self.fail("nested cycle 263 14/0 N_not_hapax=2 drifted")
        prior_262 = TestMamariI3gram999090076LeftoverExtraPreviousIOnlyScoreboard()
        prior_262.setUp()
        prior_262.test_i_hits_are_sixteen_on_ia_and_leftover_extra_999_is_subset()
        prior_262.test_3gram_is_zero_off_i_and_i_only()
        prior_262.test_survey_matches_computed_lock()
        self.assertEqual(prior_262.i_hits, 16)
        self.assertEqual(prior_262.off_i_hits, 0)
        self.assertEqual(prior_262.i_sites, CYCLE262_I_SITES)
        self.assertEqual(len(prior_262.extra), 1)
        self.assertEqual(prior_262.extra, CYCLE262_EXTRA_I_SITES)
        self.assertEqual(CYCLE262_N_I, 16)
        self.assertEqual(CYCLE262_N_OFF_I, 0)
        self.assertEqual(CYCLE262_N_EXTRA, 1)
        self.assertTrue(CYCLE262_CLAIM)
        if prior_262.i_hits != 16 or prior_262.off_i_hits != 0 or len(prior_262.extra) != 1:
            self.fail("nested cycle 262 999 090 076 leftover extra previous I-only 16/0 extra I=1 drifted")
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
        self.assertEqual(CYCLE260_N_WITH_PREVIOUS, 56)
        self.assertEqual(CYCLE260_N_NO_PREVIOUS, 0)
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-266 leftover extra remaining-after-999 lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"]
        self.assertEqual(lock["cycle"], 266)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(tuple(lock["backward_3gram"]), ("600", "090", "076"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(
            tuple(lock["locked_previous_stems_after_999"]),
            LOCKED_PREVIOUS_STEMS_AFTER_999,
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
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_999_previous_stems"]),
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 41)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(lock["N_distinct_remaining"], STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(lock["N_distinct_remaining"], 33)
        self.assertEqual(lock["N_hapax_remaining"], STANDING_N_HAPAX_REMAINING)
        self.assertEqual(lock["N_hapax_remaining"], 27)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "600")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 4)
        self.assertTrue(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 1)
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 37)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_999_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_after_999_local_4grams"],
            matching_leftover_extra_remaining_after_999_local_4gram_rows(),
        )
        self.assertEqual(
            lock["remaining_after_999_previous_stem_frequency"],
            remaining_after_999_previous_stem_frequency_rows(),
        )
        self.assertEqual(lock["nested_cycle265_K_000"], 2)
        self.assertTrue(lock["nested_cycle265_exactly_2_share_previous_000"])
        self.assertEqual(lock["nested_cycle264_K_090"], 2)
        self.assertTrue(lock["nested_cycle264_exactly_2_share_previous_090"])
        self.assertEqual(lock["nested_cycle263_N_i_only"], 14)
        self.assertEqual(lock["nested_cycle263_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle263_N_not_hapax"], 2)
        self.assertFalse(lock["nested_cycle263_all_i_only_hapax"])
        self.assertEqual(lock["nested_cycle262_N_I"], 16)
        self.assertEqual(lock["nested_cycle262_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle262_N_extra"], 1)
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
        self.assertTrue(lock["i_leftover_extra_090_076_remaining_after_999_unique_previous_stem"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle234"])
        self.assertFalse(lock["same_as_cycle256"])
        self.assertFalse(lock["same_as_cycle260"])
        self.assertFalse(lock["same_as_cycle261"])
        self.assertFalse(lock["same_as_cycle264"])
        self.assertFalse(lock["same_as_cycle265"])
        self.assertTrue(lock["same_claim_shape_as_cycle234"])
        self.assertTrue(lock["same_claim_shape_as_cycle256"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["cycle265_previous_000_is_not_remaining_after_999"])
        self.assertTrue(lock["cycle264_previous_090_is_not_remaining_after_999"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle167_not_overwritten"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["g_k_is_inventory_for_later_peel"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_999_090_076_previous_000_unchanged"])
        self.assertTrue(lock["standing_i_999_090_076_previous_090_unchanged"])
        self.assertTrue(lock["standing_i_999_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_leftover_extra_previous_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_999_090_076_previous_000"]["cycle"], 265)
        self.assertEqual(self.survey["i_999_090_076_previous_000"]["K_000"], 2)
        self.assertEqual(self.survey["i_999_090_076_previous_090"]["cycle"], 264)
        self.assertEqual(self.survey["i_999_090_076_previous_090"]["K_090"], 2)
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


class TestMamariILeftoverExtra090076RemainingAfter999PreviousStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 266 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
