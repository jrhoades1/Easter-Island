"""I's leftover n=4 remaining remaining-after-021 previous-stem lock.

Cycle 306 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–287), leftover n=4 remaining
forward peel (288–301), leftover n=4 remaining unique
previous stem (cycle 302 holds), leftover n=4 remaining
exactly 5 share previous 021 (cycle 303), 3-gram 021 090 076
I-only (cycle 304), leftover n=4 remaining previous-021
4-grams (cycle 305), leftover extra remaining-after-600
unique previous stem (cycle 270 lost), leftover extra
remaining-after-999 unique previous stem (cycle 266 holds),
leftover extra previous-999 (cycle 261), leftover extra
remaining-after-000 extra I (cycles 258/259), leftover extra
remaining-after-009 unique previous stem (cycle 284 lost),
or remaining-after-011 extra-I 4-grams (cycle 301). Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Cycle 305 leftover n=4 remaining previous-021 4-grams all
I-only HOLDS: N leftover=5, N_4grams=5, extra I of
021 090 076 = 0, N_i_only=4 / N_hapax_i_only=3 /
N_not_hapax=1 / N_leak_off_i=0. Those are previous 4-grams
of leftover n=4 remaining I 021 090 076, not leftover n=4
remaining remaining-after-021 previous stems. Cycle 303
leftover n=4 remaining I 090 076 exactly 5 share previous
021 HOLDS; N_remaining_after_021 = 8. Previous-021 4-grams
I-only does not lock remaining-after-021 previous stems.
That is the claim that can lose. Analog: cycle 269 leftover
extra 600 090 076 previous 4-grams I-only hapax HOLD then
cycle 270 leftover extra remaining-after-600 unique previous
stem LOST (5-way tie at K=2). Cycle 291 leftover n=4
remaining 090 076 020 forward 4-grams I-only not hapax HOLD
then cycle 292 leftover n=4 remaining remaining-after-020
unique next stem HOLD (G=087 K=3). Cycle 266 leftover extra
remaining-after-999 unique previous stem HOLD (G=600 K=4).
Do not peel leftover n=4 remaining 999 021 090 076 previous-
of-999 this cycle (the remaining-after-021 unique-max is
the leftover claim after previous-021 4-grams, matching
cycle 270/292). Do not peel a specific remaining-after-021
stem this cycle. Off-I T sites are not this cycle. 076 071
and 076 070 do not count as this 2-gram. Leftover extra
sites do not count as leftover n=4 remaining.

Leftover n=4 remaining remaining-after-021 = leftover n=4
remaining I 090 076 sites whose previous token is not 021.
Cycle 302 N leftover n=4 remaining = 13, cycle 303 K_021 = 5,
N_remaining_after_021 = 8. Verify from fixtures the same
way as cycle 302/303; do not invent sites. For each such
site, take the previous token if any (lock line-initial /
no-previous count separately). Line-initial / no previous
token is a nested fact (cycle 302 N_line_initial=0). Nested-
check leftover n=4 remaining N_inside==13, N_line_initial==0,
K_021==5, N_remaining_after_021==8 (do not retune
224/288/302/303). Nested leftover n=4 remaining 13 / 4 / 9 /
3 / 6 / 2 / 4 / 2 / 2 still computes (do not retune
288–297). Nested-check cycle 305 previous-021 4-grams
N_i_only==4 N_hapax==3 N_not_hapax==1 N_leak==0 (do not
retune). Count previous-stem frequencies among remaining-
after-021 sites that have a previous token. G = the previous
stem with the highest remaining-after-021 with-previous
count. If a tie, pick the larger Barthel id. K = that count.

Claim that can lose:
i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem.
True iff remaining-after-021 leftover n=4 remaining I
090 076 has a unique most frequent previous stem G with
K ≥ 2 (no tie at max K) and N_remaining_after_021 == 8.
This can lose the same way cycle 270 lost (5-way tie at
K=2, G=090) and cycle 284 lost (27 hapax G=724 K=1), or
hold the same way cycle 266 held (G=600 K=4) and cycle
292 held (G=087 K=3). Unique-max G/K is inventory for a
later peel if the claim holds or loses with K≥2. Measured:
N_remaining_after_021=8, N_with_previous=8,
N_line_initial=0, N_distinct=7, unique-max G=600 K=2 at
Ia2[107]/Ia14[54]. The claim is true. Nested leftover extra
previous-999 G-site overlap empty; leftover extra remaining-
after-000 extra I G-site overlap empty; remaining-after-011
(Ia8[106]/Ia13[17]) are previous-021 so not in remaining-
after-021; remaining-after-021 overlap leftover extra
remaining-after-000 extra I is Ia8[114]/Ia9[28]; record,
do not fail unique-max on it. Nested cycle 305 4-grams
I-only N_not_hapax=1, cycle 304 5/0 extra I=0, cycle 303
K_021=5, cycle 302 unique-max true G=021 K=5 N_distinct=8
N=13 N_line_initial=0, cycle 301 090 076 607 073 1/0,
cycle 288 unique-max false G=020 K=4, cycle 224 13/56, and
cycle 223 69/3 stay. Do not assume the result; measure.
Do not retune.

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
    STANDING_N_NOT_HAPAX as CYCLE305_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE305_N_NOT_I_ONLY,
    TestMamariI021090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_600011_COVERED,
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
    site_backward_3gram,
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
    STANDING_EXTRA_I_BY_X as CYCLE259_EXTRA_I_BY_X,
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_N_I_ONLY as CYCLE259_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE259_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_prev_stem_scoreboard import (
    STANDING_G as CYCLE284_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE284_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_UNIQUE_PREVIOUS_STEM as CYCLE284_CLAIM,
    STANDING_K as CYCLE284_K,
    STANDING_N_HAPAX_REMAINING as CYCLE284_N_HAPAX,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_stem_scoreboard import (
    STANDING_G as CYCLE270_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE270_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE270_CLAIM,
    STANDING_K as CYCLE270_K,
    STANDING_N_TIED_AT_K as CYCLE270_N_TIED,
    STANDING_TIED_STEMS as CYCLE270_TIED_STEMS,
    TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_stem_scoreboard import (
    STANDING_G as CYCLE266_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE266_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_UNIQUE_PREVIOUS_STEM as CYCLE266_CLAIM,
    STANDING_K as CYCLE266_K,
    STANDING_MATCHING_SITES as CYCLE266_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING as CYCLE266_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_999 as CYCLE266_N_REMAINING,
    TestMamariILeftoverExtra090076RemainingAfter999PreviousStemScoreboard,
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
    GRAM3_BACKWARD as GRAM3_NESTED_021,
    STANDING_G as CYCLE303_G,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_5_SHARE_PREVIOUS_021 as CYCLE303_CLAIM,
    STANDING_K_021 as CYCLE303_K_021,
    STANDING_MATCHING_SITES as CYCLE303_MATCHING_SITES,
    STANDING_NESTED_LEFTOVER_N4_REMAINING as CYCLE303_NESTED,
    STANDING_N_REMAINING_AFTER_021 as CYCLE303_N_REMAINING_AFTER_021,
    STANDING_REMAINING_AFTER_021_SITES as CYCLE303_REMAINING_AFTER_021_SITES,
    leftover_n4_remaining_with_previous_021,
    leftover_n4_remaining_without_previous_021,
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
    leftover_n4_remaining_backward_3grams,
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
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_scoreboard import (
    STANDING_G as CYCLE292_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE292_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_UNIQUE_NEXT_STEM as CYCLE292_CLAIM,
    STANDING_K as CYCLE292_K,
    STANDING_N_DISTINCT as CYCLE292_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_020 as CYCLE292_N_REMAINING,
    TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_057_forward_011_scoreboard import (
    STANDING_REMAINING_AFTER_011_SITES as CYCLE297_REMAINING_AFTER_011_SITES,
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

LOCKED_PREVIOUS_STEM_021 = "021"
LOCKED_PREVIOUS_STEMS = (LOCKED_PREVIOUS_STEM_021,)
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_BACKWARD = ("600", "090", "076")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS_INSIDE = 13
STANDING_N_LINE_INITIAL_INSIDE = 0
STANDING_K_021 = 5
STANDING_N_REMAINING_AFTER_021 = 8
STANDING_N_WITH_PREVIOUS = 8
STANDING_N_LINE_INITIAL = 0
STANDING_N_NO_PREVIOUS = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_NO_PREVIOUS_SITES = ()
STANDING_N_DISTINCT = 7
STANDING_N_HAPAX = 6
STANDING_G = "600"
STANDING_K = 2
STANDING_N_WITHOUT_G = 6
STANDING_N_TIED_AT_K = 1
STANDING_TIED_STEMS = ("600",)
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_REMAINING_SITES = CYCLE303_REMAINING_AFTER_021_SITES
STANDING_REMAINING_PREVIOUS_STEMS = (
    "600",
    "591",
    "076",
    "090",
    "000",
    "999",
    "008",
    "600",
)
STANDING_MATCHING_SITES = STANDING_LEFTOVER_600011_COVERED
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("071", "600", "090", "076"),
    ("175", "600", "090", "076"),
)
STANDING_REMAINING_FREQUENCY = (
    (
        "600",
        2,
        STANDING_MATCHING_SITES,
        (("600", "090", "076"),) * 2,
    ),
    ("999", 1, ((SIDE_IA, "Ia9", 28),), (("999", "090", "076"),)),
    ("591", 1, ((SIDE_IA, "Ia2", 119),), (("591", "090", "076"),)),
    ("090", 1, ((SIDE_IA, "Ia5", 143),), (("090", "090", "076"),)),
    ("076", 1, ((SIDE_IA, "Ia4", 86),), (("076", "090", "076"),)),
    ("008", 1, ((SIDE_IA, "Ia12", 83),), (("008", "090", "076"),)),
    ("000", 1, ((SIDE_IA, "Ia8", 114),), (("000", "090", "076"),)),
)
STANDING_OVERLAP_CYCLE261_PREVIOUS_999 = ()
STANDING_OVERLAP_CYCLE258_EXTRA_I = ()
STANDING_OVERLAP_CYCLE259_EXTRA_I = ()
STANDING_OVERLAP_REMAINING_AFTER_011 = ()
STANDING_OVERLAP_REMAINING_AFTER_021_CYCLE259_EXTRA_I = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
)
STANDING_OVERLAP_DOES_NOT_LOSE = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem"
)
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE266 = False
STANDING_SAME_AS_CYCLE270 = False
STANDING_SAME_AS_CYCLE284 = False
STANDING_SAME_AS_CYCLE292 = False
STANDING_SAME_AS_CYCLE302 = False
STANDING_SAME_AS_CYCLE303 = False
STANDING_SAME_AS_CYCLE304 = False
STANDING_SAME_AS_CYCLE305 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE266 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE270 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE284 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_DO_NOT_PEEL_PREVIOUS_OF_999 = True
STANDING_CYCLE305_4GRAMS_ARE_021_CLUSTER_NOT_REMAINING_AFTER_021 = True
STANDING_CYCLE304_3GRAM_IS_NOT_REMAINING_AFTER_021 = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_600_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_UNIQUE_PREVIOUS_STEM_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_4GRAMS_IS_NOT_THIS_CYCLE = True
STANDING_3GRAM_021_090_076_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL = True
STANDING_NESTED_LEFTOVER_N4_REMAINING = (13, 4, 9, 3, 6, 2, 4, 2, 2)


def leftover_n4_remaining_remaining_after_021(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites whose previous token is not 021 (includes line-initial)."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev not in locked_set
    )


def leftover_n4_remaining_remaining_after_021_previous_stems(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> tuple[str, ...]:
    """Previous stems of remaining-after-021 sites that have a previous token."""
    locked_set = set(locked)
    return tuple(
        prev
        for prev in previous_stems
        if prev is not None and prev not in locked_set
    )


def leftover_n4_remaining_remaining_after_021_with_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-021 leftover n=4 remaining sites that have a previous token."""
    remaining = leftover_n4_remaining_remaining_after_021(sites, previous_stems, locked)
    rem_prev = tuple(
        prev
        for site, prev in zip(sites, previous_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_with_previous(remaining, rem_prev)


def leftover_n4_remaining_remaining_after_021_without_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-021 leftover n=4 remaining sites with no previous token."""
    remaining = leftover_n4_remaining_remaining_after_021(sites, previous_stems, locked)
    rem_prev = tuple(
        prev
        for site, prev in zip(sites, previous_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_without_previous(remaining, rem_prev)


def leftover_n4_remaining_remaining_after_021_with_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-021 sites whose previous token is G."""
    remaining = set(leftover_n4_remaining_remaining_after_021(sites, previous_stems, locked))
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev == stem and site in remaining
    )


def leftover_n4_remaining_remaining_after_021_without_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-021 sites whose previous token is not G."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev is not None and prev not in locked_set and prev != stem
    )


def remaining_after_021_previous_stem_counts(previous_stems: tuple[str, ...]) -> Counter:
    """Counts of previous stems among leftover n=4 remaining remaining-after-021 with-previous."""
    return Counter(previous_stems)


def rank_remaining_after_021_previous_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Remaining-after-021 previous stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_remaining_after_021_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining-after-021 has no G."""
    ranked = rank_remaining_after_021_previous_stems(
        remaining_after_021_previous_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_after_021_previous_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    backward_3grams: tuple[tuple[str, ...] | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Remaining-after-021 previous-stem frequency: highest count first, then larger id."""
    rem_sites = leftover_n4_remaining_remaining_after_021_with_previous(
        sites, previous_stems, locked
    )
    rem_stems = leftover_n4_remaining_remaining_after_021_previous_stems(
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


def remaining_after_021_previous_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_REMAINING_FREQUENCY,
) -> list[dict]:
    """Survey-shaped remaining-after-021 previous-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "previous_stem": stem,
                "count": count,
                "leftover_n4_remaining_remaining_after_021_sites": [
                    list(site) for site in sites
                ],
                "backward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def leftover_n4_remaining_remaining_after_021_nested_counts_hold(
    n_inside: int,
    n_line_initial_inside: int,
    k_021: int,
    n_remaining: int,
    expected_inside: int = STANDING_N_INSIDE,
    expected_line_initial_inside: int = STANDING_N_LINE_INITIAL_INSIDE,
    expected_k_021: int = STANDING_K_021,
    expected_remaining: int = STANDING_N_REMAINING_AFTER_021,
) -> bool:
    """Nested leftover n=4 remaining 13/0/5/8."""
    return (
        n_inside == expected_inside
        and n_line_initial_inside == expected_line_initial_inside
        and k_021 == expected_k_021
        and n_remaining == expected_remaining
        and n_remaining == n_inside - k_021
        and n_line_initial_inside == 0
    )


def i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem(
    inside_sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS,
) -> bool:
    """True iff remaining-after-021 has a unique most frequent previous stem with K ≥ 2."""
    remaining = leftover_n4_remaining_remaining_after_021(
        inside_sites,
        previous_stems,
        locked,
    )
    remaining_stems = leftover_n4_remaining_remaining_after_021_previous_stems(
        inside_sites,
        previous_stems,
        locked,
    )
    if len(remaining) != STANDING_N_REMAINING_AFTER_021:
        return False
    if remaining != leftover_n4_remaining_without_previous_021(
        inside_sites,
        previous_stems,
    ):
        return False
    gram, count, unique = select_remaining_after_021_g(remaining_stems)
    return bool(unique and gram is not None and count >= 2)


def matching_leftover_n4_remaining_remaining_after_021_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    previous_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_PREVIOUS_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover n=4 remaining remaining-after-021 previous-4-gram rows."""
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


class TestILeftoverN4Remaining090076RemainingAfter021PreviousStemHelpers(
    unittest.TestCase
):
    """Helpers on leftover n=4 remaining remaining-after-021 previous stems. No CV, no LLM."""

    def test_remaining_after_021_requires_previous_not_021(self):
        """Remaining-after-021 excludes previous 021; line-initial is remaining, no-previous."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_021, ("021", "090", "076"))
        self.assertEqual(LOCKED_PREVIOUS_STEMS, ("021",))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_BACKWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_600 = ["071", "600", "090", "076"]
        self.assertEqual(site_previous_stem(has_600, 2, GRAM2), "600")
        self.assertEqual(site_backward_3gram(has_600, 2, GRAM2), GRAM3_BACKWARD)
        self.assertEqual(
            site_previous_4gram(has_600, 2, GRAM2),
            ("071", "600", "090", "076"),
        )
        has_021 = ["600", "021", "090", "076"]
        self.assertEqual(site_previous_stem(has_021, 2, GRAM2), "021")
        self.assertNotEqual(site_previous_stem(has_021, 2, GRAM2), "600")
        line_initial = ["090", "076", "011"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
        )
        planted_stems = ("600", "021", None, "999")
        rem = leftover_n4_remaining_remaining_after_021(planted_sites, planted_stems)
        self.assertEqual(rem, (planted_sites[0], planted_sites[2], planted_sites[3]))
        self.assertEqual(
            leftover_n4_remaining_remaining_after_021_previous_stems(
                planted_sites, planted_stems
            ),
            ("600", "999"),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_021_with_previous(
                planted_sites, planted_stems
            ),
            (planted_sites[0], planted_sites[3]),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_021_without_previous(
                planted_sites, planted_stems
            ),
            (planted_sites[2],),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_021_with_g(
                planted_sites, planted_stems
            ),
            (planted_sites[0],),
        )
        self.assertNotIn(planted_sites[1], rem)
        mismatch_071 = ["021", "076", "071", "090"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        mismatch_070 = ["021", "076", "070", "090"]
        self.assertIsNone(site_previous_stem(mismatch_070, 1, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE305_4GRAMS_ARE_021_CLUSTER_NOT_REMAINING_AFTER_021)
        self.assertTrue(STANDING_CYCLE304_3GRAM_IS_NOT_REMAINING_AFTER_021)
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_can_fail(self):
        """Boolean is True only when remaining=8 and some G has unique K≥2."""
        provider = MockProvider()
        inside = STANDING_INSIDE_SITES
        stems = leftover_n4_remaining_previous_stems(load_i_sides(), inside, GRAM2)
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem(
                inside,
                stems,
            )
        )
        rem = leftover_n4_remaining_remaining_after_021(inside, stems)
        rem_stems = leftover_n4_remaining_remaining_after_021_previous_stems(
            inside, stems
        )
        self.assertEqual(len(rem), STANDING_N_REMAINING_AFTER_021)
        self.assertEqual(len(rem), 8)
        self.assertEqual(rem, STANDING_REMAINING_SITES)
        self.assertEqual(rem_stems, STANDING_REMAINING_PREVIOUS_STEMS)
        g, k, unique = select_remaining_after_021_g(rem_stems)
        self.assertEqual(g, "600")
        self.assertEqual(k, 2)
        self.assertTrue(unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        empty_stems = ("021",) * len(inside)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem(
                inside,
                empty_stems,
            )
        )
        tie_stems = list(stems)
        demote = {(SIDE_IA, "Ia2", 119): "600"}
        for i, site in enumerate(inside):
            if site in demote:
                tie_stems[i] = demote[site]
        tied = tuple(tie_stems)
        tied_g, tied_k, tied_unique = select_remaining_after_021_g(
            leftover_n4_remaining_remaining_after_021_previous_stems(inside, tied)
        )
        self.assertEqual(tied_g, "600")
        self.assertEqual(tied_k, 3)
        self.assertTrue(tied_unique)
        hapax_stems = list(stems)
        replacements = {(SIDE_IA, "Ia14", 54): "801"}
        for i, site in enumerate(inside):
            if site in replacements:
                hapax_stems[i] = replacements[site]
        hapax = tuple(hapax_stems)
        hap_g, hap_k, hap_unique = select_remaining_after_021_g(
            leftover_n4_remaining_remaining_after_021_previous_stems(inside, hapax)
        )
        self.assertEqual(hap_k, 1)
        self.assertFalse(hap_unique)
        self.assertEqual(
            len(leftover_n4_remaining_remaining_after_021(inside, hapax)),
            8,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem(
                inside,
                hapax,
            )
        )
        two_way = list(stems)
        two_way_map = {(SIDE_IA, "Ia9", 28): "591"}
        for i, site in enumerate(inside):
            if site in two_way_map:
                two_way[i] = two_way_map[site]
        two = tuple(two_way)
        two_g, two_k, two_unique = select_remaining_after_021_g(
            leftover_n4_remaining_remaining_after_021_previous_stems(inside, two)
        )
        self.assertEqual(two_g, "600")
        self.assertEqual(two_k, 2)
        self.assertFalse(two_unique)
        self.assertEqual(
            len(leftover_n4_remaining_remaining_after_021(inside, two)),
            8,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem(
                inside,
                two,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM
        )
        self.assertEqual(
            STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING_AFTER_021
        )
        self.assertEqual(2 + 6, 8)
        self.assertEqual(
            STANDING_K_021 + STANDING_N_REMAINING_AFTER_021, STANDING_N_INSIDE
        )
        self.assertEqual(5 + 8, 13)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_PEEL_PREVIOUS_OF_999)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal remaining-after-021 counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"600": 2, "999": 1, "591": 1})
        ranked = rank_remaining_after_021_previous_stems(counts)
        self.assertEqual(ranked[0], ("600", 2))
        self.assertEqual(ranked[1], ("999", 1))
        self.assertEqual(ranked[2], ("591", 1))
        self.assertEqual(
            select_remaining_after_021_g(("600", "999", "600", "999"))[0], "999"
        )
        self.assertFalse(select_remaining_after_021_g(("600", "999", "600", "999"))[2])
        self.assertEqual(select_remaining_after_021_g(("600", "600", "999"))[0], "600")
        self.assertTrue(select_remaining_after_021_g(("600", "600", "999"))[2])
        self.assertEqual(select_remaining_after_021_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE266)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE270)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE284)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE266)
        self.assertFalse(STANDING_SAME_AS_CYCLE270)
        self.assertFalse(STANDING_SAME_AS_CYCLE284)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertTrue(CYCLE266_UNIQUE)
        self.assertFalse(CYCLE270_UNIQUE)
        self.assertFalse(CYCLE284_UNIQUE)
        self.assertTrue(CYCLE292_UNIQUE)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter021PreviousStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining remaining-after-021 previous-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.inside_sites = STANDING_INSIDE_SITES
        self.previous_stems = leftover_n4_remaining_previous_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.backwards = leftover_n4_remaining_backward_3grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.previous_4grams = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.with_previous_inside = leftover_n4_remaining_sites_with_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.line_initial_inside = leftover_n4_remaining_sites_without_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.share_021 = leftover_n4_remaining_with_previous_021(
            self.inside_sites,
            self.previous_stems,
        )
        self.remaining = leftover_n4_remaining_remaining_after_021(
            self.inside_sites,
            self.previous_stems,
        )
        self.remaining_stems = leftover_n4_remaining_remaining_after_021_previous_stems(
            self.inside_sites,
            self.previous_stems,
        )
        self.with_previous = leftover_n4_remaining_remaining_after_021_with_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.line_initial = leftover_n4_remaining_remaining_after_021_without_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.matching = leftover_n4_remaining_remaining_after_021_with_g(
            self.inside_sites,
            self.previous_stems,
        )
        self.without = leftover_n4_remaining_remaining_after_021_without_g(
            self.inside_sites,
            self.previous_stems,
        )
        self.frequency = remaining_after_021_previous_stem_frequency_table(
            self.inside_sites,
            self.previous_stems,
            self.backwards,
        )
        self.matching_previous_4grams = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover_extra = len(STANDING_LEFTOVER_SITES)
        self.n_with_previous_inside = len(self.with_previous_inside)
        self.n_line_initial_inside = len(self.line_initial_inside)
        self.k_021 = len(self.share_021)
        self.n_remaining = len(self.remaining)
        self.n_with_previous = len(self.with_previous)
        self.n_line_initial = len(self.line_initial)
        self.n_distinct = len(self.frequency)
        self.g, self.k, self.unique = select_remaining_after_021_g(self.remaining_stems)
        self.n_without = len(self.without)
        self.overlap_261 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE261_MATCHING_SITES,
        )
        self.overlap_258 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_259 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_after_011 = leftover_n4_remaining_g_overlap_sites(
            self.remaining,
            CYCLE297_REMAINING_AFTER_011_SITES,
        )
        self.overlap_remaining_259 = leftover_n4_remaining_g_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_SITES,
        )
        self.claim_holds = (
            i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem(
                self.inside_sites,
                self.previous_stems,
            )
        )

    def test_tokens_and_nested_leftover_n4_remaining_13_5_8_not_retuned(self):
        """2-gram and leftover n=4 remaining 13/0/5/8 stay the cycle-303/302/224 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_BACKWARD, ("600", "090", "076"))
        self.assertEqual(GRAM3_NESTED_021, ("021", "090", "076"))
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
        self.assertTrue(STANDING_DO_NOT_PEEL_PREVIOUS_OF_999)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_600_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_UNIQUE_PREVIOUS_STEM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_4GRAMS_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_3GRAM_021_090_076_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_8_remaining_g_600_k_2_and_hypothesis_holds(self):
        """N_remaining=8, N_line_initial=0, N_distinct=7, G=600 K=2 unique-max. Claim holds."""
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
            leftover_n4_remaining_remaining_after_021_nested_counts_hold(
                self.n_inside,
                self.n_line_initial_inside,
                self.k_021,
                self.n_remaining,
            )
        )
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_021)
        self.assertEqual(STANDING_N_REMAINING_AFTER_021, 8)
        self.assertEqual(STANDING_N_REMAINING_AFTER_021, CYCLE303_N_REMAINING_AFTER_021)
        self.assertEqual(self.n_remaining, self.n_inside - self.k_021)
        self.assertEqual(13 - 5, 8)
        if self.n_remaining != 8:
            self.fail("measured N_remaining_after_021 drifted from 8")
        if self.n_remaining != self.n_inside - self.k_021:
            self.fail(
                "leftover n=4 remaining remaining-after-021 filter disagrees with nested 13−5"
            )
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE303_REMAINING_AFTER_021_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_PREVIOUS_STEMS)
        self.assertEqual(len(self.remaining), len(self.remaining_stems))
        self.assertEqual(
            self.remaining,
            leftover_n4_remaining_without_previous_021(
                self.inside_sites,
                self.previous_stems,
            ),
        )
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 8)
        self.assertEqual(self.n_line_initial, STANDING_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertEqual(self.n_line_initial, STANDING_N_NO_PREVIOUS)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertEqual(self.n_with_previous + self.n_line_initial, self.n_remaining)
        self.assertEqual(8 + 0, 8)
        for site in self.share_021:
            self.assertNotIn(site, self.remaining)
        for site in CYCLE297_REMAINING_AFTER_011_SITES:
            self.assertNotIn(site, self.remaining)
            self.assertIn(site, CYCLE303_MATCHING_SITES)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT)
        self.assertEqual(STANDING_N_DISTINCT, 7)
        self.assertEqual(self.frequency, STANDING_REMAINING_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "600")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 2)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "600")
        self.assertEqual(self.frequency[0][1], 2)
        self.assertGreater(self.frequency[0][1], self.frequency[1][1])
        tied = tuple(stem for stem, count, _sites, _grams in self.frequency if count == 2)
        self.assertEqual(tied, STANDING_TIED_STEMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 1)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX)
        self.assertEqual(STANDING_N_HAPAX, 6)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 6)
        self.assertEqual(self.k + self.n_without, self.n_remaining)
        self.assertEqual(2 + 6, 8)
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem(
                self.inside_sites,
                self.previous_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_021_UNIQUE_PREVIOUS_STEM
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching, STANDING_LEFTOVER_600011_COVERED)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE266)
        self.assertFalse(STANDING_SAME_AS_CYCLE270)
        self.assertFalse(STANDING_SAME_AS_CYCLE284)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE302)
        self.assertFalse(STANDING_SAME_AS_CYCLE303)
        self.assertFalse(STANDING_SAME_AS_CYCLE304)
        self.assertFalse(STANDING_SAME_AS_CYCLE305)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE266)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE270)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE284)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_CYCLE305_4GRAMS_ARE_021_CLUSTER_NOT_REMAINING_AFTER_021)
        self.assertTrue(STANDING_CYCLE304_3GRAM_IS_NOT_REMAINING_AFTER_021)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL)
        self.assertTrue(CYCLE302_CLAIM)
        self.assertTrue(CYCLE303_CLAIM)
        self.assertTrue(CYCLE304_CLAIM)
        self.assertTrue(CYCLE305_CLAIM)
        self.assertTrue(CYCLE266_CLAIM)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertFalse(CYCLE284_CLAIM)
        self.assertTrue(CYCLE292_CLAIM)
        self.assertEqual(CYCLE266_G, "600")
        self.assertEqual(CYCLE266_K, 4)
        self.assertEqual(CYCLE266_N_REMAINING, 41)
        self.assertEqual(CYCLE266_N_DISTINCT, 33)
        self.assertTrue(CYCLE266_UNIQUE)
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        self.assertEqual(CYCLE270_N_TIED, 5)
        self.assertEqual(CYCLE270_TIED_STEMS, ("090", "076", "071", "045", "009"))
        self.assertFalse(CYCLE270_UNIQUE)
        self.assertEqual(CYCLE284_G, "724")
        self.assertEqual(CYCLE284_K, 1)
        self.assertEqual(CYCLE284_N_HAPAX, 27)
        self.assertFalse(CYCLE284_UNIQUE)
        self.assertEqual(CYCLE292_G, "087")
        self.assertEqual(CYCLE292_K, 3)
        self.assertEqual(CYCLE292_N_REMAINING, 9)
        self.assertEqual(CYCLE292_N_DISTINCT, 5)
        self.assertTrue(CYCLE292_UNIQUE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_n4_remaining_remaining_after_021_sites_share_600(self):
        """Two leftover n=4 remaining remaining-after-021 sites are 600 090 076."""
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
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, STANDING_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE303_MATCHING_SITES)
            self.assertNotIn(site, CYCLE297_REMAINING_AFTER_011_SITES)
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            prev = site_previous_stem(stems, index, GRAM2)
            self.assertIsNotNone(prev)
            self.assertNotEqual(prev, "600")
            self.assertNotEqual(prev, "021")
            self.assertIn(site, STANDING_REMAINING_SITES)
        for site in self.share_021:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE303_MATCHING_SITES)
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, prev4, _nxt4), want in zip(
            local,
            STANDING_MATCHING_PREVIOUS_4GRAMS,
            strict=True,
        ):
            self.assertEqual(prev4, want)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_PEEL_PREVIOUS_OF_999)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_overlap_g_sites_empty_remaining_after_021_has_258_259(self):
        """G sites do not overlap leftover extra previous-999 / remaining-after-000 extra I / remaining-after-011."""
        self.assertEqual(self.overlap_261, STANDING_OVERLAP_CYCLE261_PREVIOUS_999)
        self.assertEqual(self.overlap_261, ())
        self.assertEqual(self.overlap_258, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_258, ())
        self.assertEqual(self.overlap_after_011, STANDING_OVERLAP_REMAINING_AFTER_011)
        self.assertEqual(self.overlap_after_011, ())
        self.assertEqual(
            self.overlap_remaining_259,
            STANDING_OVERLAP_REMAINING_AFTER_021_CYCLE259_EXTRA_I,
        )
        self.assertEqual(
            self.overlap_remaining_259,
            ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28)),
        )
        self.assertIn((SIDE_IA, "Ia8", 114), CYCLE259_EXTRA_I_SITES)
        self.assertIn((SIDE_IA, "Ia9", 28), CYCLE259_EXTRA_I_SITES)
        self.assertIn((SIDE_IA, "Ia8", 114), CYCLE259_EXTRA_I_BY_X["057"])
        self.assertIn((SIDE_IA, "Ia9", 28), CYCLE259_EXTRA_I_BY_X["057"])
        self.assertNotIn((SIDE_IA, "Ia8", 106), self.remaining)
        self.assertNotIn((SIDE_IA, "Ia13", 17), self.remaining)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE303_MATCHING_SITES)
        self.assertIn((SIDE_IA, "Ia13", 17), CYCLE303_MATCHING_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE297_REMAINING_AFTER_011_SITES)
        self.assertIn((SIDE_IA, "Ia13", 17), CYCLE297_REMAINING_AFTER_011_SITES)
        for site in CYCLE261_MATCHING_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.matching)
            self.assertNotIn(site, self.remaining)
        for site in CYCLE266_MATCHING_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.matching)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(self.claim_holds)
        self.assertEqual(CYCLE261_K_999, 15)
        self.assertEqual(CYCLE261_N_REMAINING_AFTER_999, 41)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertEqual(len(CYCLE259_EXTRA_I_SITES), 3)
        self.assertEqual(CYCLE259_N_I_ONLY, 2)
        self.assertEqual(CYCLE259_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE259_CLAIM)
        extra_i_not_previous_021 = leftover_n4_remaining_g_overlap_sites(
            CYCLE259_EXTRA_I_SITES,
            self.remaining,
        )
        self.assertEqual(extra_i_not_previous_021, self.overlap_remaining_259)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_305_304_303_302_301_288_270_266_224_223_still_compute(self):
        """Cycle 305 4/3/1/0, 304 5/0 extra I=0, 303 K_021=5/8, 302 G=021 K=5, 301 1/0, 288 G=020 K=4, 270 5-way tie, 266 G=600 K=4, 224 13/56, 223 69/3 stay."""
        prior_305 = TestMamariI021090076Previous4gramsIOnlyScoreboard()
        prior_305.setUp()
        prior_305.test_all_4grams_are_i_only_not_all_hapax_and_claim_holds()
        prior_305.test_survey_matches_computed_lock()
        self.assertEqual(prior_305.n_i_only, 4)
        self.assertEqual(prior_305.n_hapax_i_only, 3)
        self.assertEqual(prior_305.n_not_hapax, 1)
        self.assertEqual(prior_305.n_not_i_only, 0)
        self.assertTrue(prior_305.claim_holds)
        self.assertTrue(CYCLE305_CLAIM)
        self.assertEqual(CYCLE305_N_I_ONLY, 4)
        self.assertEqual(CYCLE305_N_HAPAX, 3)
        self.assertEqual(CYCLE305_N_NOT_HAPAX, 1)
        self.assertEqual(CYCLE305_N_NOT_I_ONLY, 0)
        if (
            prior_305.n_i_only != 4
            or prior_305.n_hapax_i_only != 3
            or prior_305.n_not_hapax != 1
            or prior_305.n_not_i_only != 0
            or not prior_305.claim_holds
        ):
            self.fail("nested cycle 305 previous-021 4-grams I-only N_i_only=4 N_hapax=3 N_not_hapax=1 N_leak=0 drifted")
        prior_304 = TestMamariI3gram021090076IOnlyScoreboard()
        prior_304.setUp()
        prior_304.test_i_hits_are_five_on_ia_and_leftover_n4_remaining_021_is_subset()
        prior_304.test_3gram_is_zero_off_i_and_i_only()
        prior_304.test_survey_matches_computed_lock()
        self.assertEqual(prior_304.i_hits, 5)
        self.assertEqual(prior_304.off_i_hits, 0)
        self.assertEqual(len(prior_304.extra), 0)
        self.assertEqual(prior_304.extra, CYCLE304_EXTRA_I_SITES)
        self.assertTrue(prior_304.claim_holds)
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
        self.assertEqual(self.remaining, prior_303.without)
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
        prior_270 = TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard()
        prior_270.setUp()
        prior_270.test_counts_37_remaining_g_090_k_2_five_way_tie_and_hypothesis_loses()
        prior_270.test_survey_matches_computed_lock()
        self.assertEqual(prior_270.g, "090")
        self.assertEqual(prior_270.k, 2)
        self.assertFalse(prior_270.unique)
        self.assertFalse(prior_270.claim_holds)
        self.assertFalse(CYCLE270_CLAIM)
        if prior_270.g != "090" or prior_270.k != 2 or prior_270.unique:
            self.fail("nested cycle 270 leftover extra remaining-after-600 unique-max false G=090 K=2 5-way tie drifted")
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
        if (
            prior_266.g != "600"
            or prior_266.k != 4
            or prior_266.n_remaining != 41
            or prior_266.n_distinct != 33
            or not prior_266.unique
        ):
            self.fail("nested cycle 266 unique-max G=600 K=4 N_remaining=41 distinct=33 drifted")
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
        if prior_259.n_i_only != 2 or prior_259.n_not_i_only != 0:
            self.fail("nested cycle 259 leftover extra remaining-after-000 extra-I 4-grams 2/0 drifted")
        prior_292 = TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard()
        prior_292.setUp()
        prior_292.test_counts_9_remaining_g_087_k_3_and_hypothesis_holds()
        prior_292.test_survey_matches_computed_lock()
        self.assertEqual(prior_292.g, "087")
        self.assertEqual(prior_292.k, 3)
        self.assertEqual(prior_292.n_remaining, 9)
        self.assertEqual(prior_292.n_distinct, 5)
        self.assertTrue(prior_292.unique)
        self.assertTrue(prior_292.claim_holds)
        self.assertTrue(CYCLE292_CLAIM)
        if (
            prior_292.g != "087"
            or prior_292.k != 3
            or prior_292.n_remaining != 9
            or not prior_292.unique
        ):
            self.fail("nested cycle 292 leftover n=4 remaining remaining-after-020 unique next stem G=087 K=3 drifted")
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
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-306 leftover n=4 remaining remaining-after-021 lock."""
        lock = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_021_previous_stem"
        ]
        self.assertEqual(lock["cycle"], 306)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["backward_3gram"]), GRAM3_BACKWARD)
        self.assertEqual(tuple(lock["backward_3gram"]), ("600", "090", "076"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_previous_stems"]), LOCKED_PREVIOUS_STEMS)
        self.assertEqual(tuple(lock["locked_previous_stems"]), ("021",))
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
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_021_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_021_previous_stems"]),
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 8)
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["line_initial_sites"], [])
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 7)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 6)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "600")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertTrue(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 1)
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 6)
        self.assertEqual(
            tuple(
                tuple(row)
                for row in lock["matching_leftover_n4_remaining_remaining_after_021_sites"]
            ),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_remaining_after_021_local_4grams"],
            matching_leftover_n4_remaining_remaining_after_021_local_4gram_rows(),
        )
        self.assertEqual(
            lock["remaining_after_021_previous_stem_frequency"],
            remaining_after_021_previous_stem_frequency_rows(),
        )
        self.assertEqual(lock["overlap_cycle261_previous_999_sites"], [])
        self.assertEqual(lock["overlap_cycle258_extra_i_sites"], [])
        self.assertEqual(lock["overlap_cycle259_extra_i_sites"], [])
        self.assertEqual(lock["overlap_remaining_after_011_sites"], [])
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_REMAINING_AFTER_021_CYCLE259_EXTRA_I],
            lock["overlap_remaining_after_021_cycle259_extra_i_sites"],
        )
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
        self.assertEqual(lock["nested_cycle292_G"], "087")
        self.assertEqual(lock["nested_cycle292_K"], 3)
        self.assertTrue(lock["nested_cycle292_unique_next_stem"])
        self.assertEqual(lock["nested_cycle270_G"], "090")
        self.assertEqual(lock["nested_cycle270_K"], 2)
        self.assertEqual(lock["nested_cycle270_N_tied_at_K"], 5)
        self.assertFalse(lock["nested_cycle270_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle266_G"], "600")
        self.assertEqual(lock["nested_cycle266_K"], 4)
        self.assertTrue(lock["nested_cycle266_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle284_G"], "724")
        self.assertEqual(lock["nested_cycle284_K"], 1)
        self.assertFalse(lock["nested_cycle284_G_uniquely_most_frequent"])
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
        self.assertTrue(
            lock["i_leftover_n4_remaining_090_076_remaining_after_021_unique_previous_stem"]
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle266"])
        self.assertFalse(lock["same_as_cycle270"])
        self.assertFalse(lock["same_as_cycle284"])
        self.assertFalse(lock["same_as_cycle292"])
        self.assertFalse(lock["same_as_cycle302"])
        self.assertFalse(lock["same_as_cycle303"])
        self.assertFalse(lock["same_as_cycle304"])
        self.assertFalse(lock["same_as_cycle305"])
        self.assertTrue(lock["same_claim_shape_as_cycle266"])
        self.assertTrue(lock["same_claim_shape_as_cycle270"])
        self.assertTrue(lock["same_claim_shape_as_cycle284"])
        self.assertTrue(lock["same_claim_shape_as_cycle292"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["do_not_peel_previous_of_999"])
        self.assertTrue(lock["cycle305_4grams_are_021_cluster_not_remaining_after_021"])
        self.assertTrue(lock["cycle304_3gram_is_not_remaining_after_021"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_extra_remaining_after_600_is_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_remaining_after_999_is_not_this_cycle"])
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
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_999_previous_stem_unchanged"]
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
            self.survey["i_leftover_n4_remaining_090_076_previous_021"][
                "N_remaining_after_021"
            ],
            8,
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
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_previous_stem"][
                "i_leftover_n4_remaining_090_076_unique_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"][
                "cycle"
            ],
            301,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"],
            288,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"][
                "cycle"
            ],
            292,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "cycle"
            ],
            270,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "i_leftover_extra_090_076_remaining_after_600_unique_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_999_previous_stem"][
                "cycle"
            ],
            266,
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


class TestMamariILeftoverN4Remaining090076RemainingAfter021PreviousStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 306 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
