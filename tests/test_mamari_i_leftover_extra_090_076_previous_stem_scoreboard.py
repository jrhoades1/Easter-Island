"""I's cycle-224 leftover extra 2-gram previous-stem lock.

Cycle 260 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover extra I sites of 2-gram 090 076 (the 56 I
sites that do not sit inside leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover extra sites, the leftover n=4 set, or
the already-closed leftover remaining family. Does not retune
the forward peel of leftover extra I 090 076 (cycles 225–259).
Does not peel leftover-of-leftover extra I this cycle. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

For each leftover extra I site, record the previous token
immediately before 090 076 when it exists (the Y in Y 090 076;
backward 3-gram Y 090 076, and previous 4-gram X Y 090 076 when
it exists). Sites with no previous token (line-initial) are
N_no_previous, not a shared stem. Nested-assert N_I=69 /
N_inside=13 / N_leftover=56 from cycle 224; do not retune
cycles 223/224. Nested-check cycle 225: share-one-forward-stem
false, 30 distinct next stems, G=070 K=8 (do not retune).
Off-I T sites are not this cycle. I-only of leftover extra
4-grams is leftover-of-leftover for a later cycle. 076 071
and 076 070 do not count as this 2-gram. Inside-family sites
do not count as leftover extra.

Claim that can lose:
i_leftover_extra_090_076_share_one_previous_stem. True only if
N_with_previous>=2 and N_distinct==1. Measured: N_leftover=56,
N_leftover_extra=56, N_with_previous=56, N_no_previous=0,
N_distinct=34, most frequent previous stem G=999 K=15 (report;
the claim is share-one, not exactly-K). Unique-max G/K is
inventory for a later peel; unique-max alone does not make
this claim true (cycle 225 had unique-max G=070 K=8 and still
LOST share-one-forward-stem). The claim is false. Same
claim-shape as cycle 225 (leftover extra 090 076
share-one-forward-stem lost, N_distinct=30), previous
direction instead of forward. Nested cycle 259 extra-I 4-grams
2/0, cycle 258 19/19 extra I=3, cycle 257 19/19 hapax, cycle
256 unique-max false N_remaining11=19 K=1 G=755, cycle 223
69/3, and cycle 207 8/1 stay. Do not assume the result;
measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from collections import Counter

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_I as CYCLE224_N_I,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
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
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    group_sites_by_previous_stem,
    leftover_sites_with_backward,
    leftover_sites_without_backward,
    previous_stem_frequency_table,
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE225_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_K as CYCLE225_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE225_N_LEFTOVER,
    STANDING_N_NO_NEXT as CYCLE225_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE225_N_WITH_NEXT,
    TestMamariILeftoverExtra090076ForwardStemScoreboard,
    leftover_extra_next_stems,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_N_I_ONLY as CYCLE259_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE259_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    STANDING_N_EXTRA_TOTAL as CYCLE258_N_EXTRA_TOTAL,
    STANDING_N_I_ONLY as CYCLE258_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE258_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE257_CLAIM,
    STANDING_N_I_ONLY as CYCLE257_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE257_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    STANDING_G as CYCLE256_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE256_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
    TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard,
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

HYPOTHESIS_SHARE_ONE = True
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS = 56
STANDING_N_NO_PREVIOUS = 0
STANDING_NO_PREVIOUS_SITES = ()
STANDING_PER_SITE_PREVIOUS_STEMS = (
    "999",
    "045",
    "048",
    "380",
    "011",
    "999",
    "499",
    "045",
    "600",
    "600",
    "600",
    "497",
    "076",
    "009",
    "036",
    "999",
    "999",
    "071",
    "092",
    "999",
    "291",
    "522",
    "999",
    "150",
    "078",
    "999",
    "295",
    "999",
    "000",
    "109",
    "009",
    "999",
    "052",
    "099",
    "999",
    "071",
    "600",
    "999",
    "700",
    "161",
    "999",
    "010",
    "205",
    "090",
    "999",
    "382",
    "386",
    "999",
    "008",
    "027",
    "076",
    "724",
    "400",
    "090",
    "999",
    "326",
)

STANDING_PER_SITE_BACKWARD_3GRAMS = tuple(
    ((stem, "090", "076") if stem is not None else None)
    for stem in STANDING_PER_SITE_PREVIOUS_STEMS
)


STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN = (
    "999",
    "045",
    "048",
    "380",
    "011",
    "499",
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
    "052",
    "099",
    "700",
    "161",
    "010",
    "205",
    "090",
    "382",
    "386",
    "008",
    "027",
    "724",
    "400",
    "326",
)

STANDING_G_SITES = (
    (SIDE_IA, "Ia1", 2),
    (SIDE_IA, "Ia2", 10),
    (SIDE_IA, "Ia3", 37),
    (SIDE_IA, "Ia3", 71),
    (SIDE_IA, "Ia4", 112),
    (SIDE_IA, "Ia4", 154),
    (SIDE_IA, "Ia5", 2),
    (SIDE_IA, "Ia5", 23),
    (SIDE_IA, "Ia6", 92),
    (SIDE_IA, "Ia7", 68),
    (SIDE_IA, "Ia7", 129),
    (SIDE_IA, "Ia9", 129),
    (SIDE_IA, "Ia12", 47),
    (SIDE_IA, "Ia13", 109),
    (SIDE_IA, "Ia14", 140),
)

STANDING_PER_SITE_PREVIOUS_4GRAMS = (
    ("602", "999", "090", "076"),
    ("093", "045", "090", "076"),
    ("027", "048", "090", "076"),
    ("380", "380", "090", "076"),
    ("076", "011", "090", "076"),
    ("070", "999", "090", "076"),
    ("070", "499", "090", "076"),
    ("061", "045", "090", "076"),
    ("076", "600", "090", "076"),
    ("070", "600", "090", "076"),
    ("455", "600", "090", "076"),
    ("050", "497", "090", "076"),
    ("076", "076", "090", "076"),
    ("009", "009", "090", "076"),
    ("061", "036", "090", "076"),
    ("000", "999", "090", "076"),
    ("499", "999", "090", "076"),
    ("076", "071", "090", "076"),
    ("090", "092", "090", "076"),
    ("060", "999", "090", "076"),
    ("087", "291", "090", "076"),
    ("460", "522", "090", "076"),
    ("254", "999", "090", "076"),
    ("010", "150", "090", "076"),
    ("087", "078", "090", "076"),
    ("000", "999", "090", "076"),
    ("071", "295", "090", "076"),
    ("381", "999", "090", "076"),
    ("490", "000", "090", "076"),
    ("090", "109", "090", "076"),
    ("071", "009", "090", "076"),
    ("023", "999", "090", "076"),
    ("055", "052", "090", "076"),
    ("000", "099", "090", "076"),
    ("064", "999", "090", "076"),
    ("092", "071", "090", "076"),
    ("168", "600", "090", "076"),
    ("518", "999", "090", "076"),
    ("670", "700", "090", "076"),
    ("076", "161", "090", "076"),
    ("075", "999", "090", "076"),
    ("208", "010", "090", "076"),
    ("072", "205", "090", "076"),
    ("011", "090", "090", "076"),
    ("090", "999", "090", "076"),
    ("071", "382", "090", "076"),
    ("011", "386", "090", "076"),
    ("700", "999", "090", "076"),
    ("727", "008", "090", "076"),
    ("070", "027", "090", "076"),
    ("071", "076", "090", "076"),
    ("724", "724", "090", "076"),
    ("007", "400", "090", "076"),
    ("011", "090", "090", "076"),
    ("090", "999", "090", "076"),
    ("600", "326", "090", "076"),
)

STANDING_PREVIOUS_STEM_FREQUENCY = (
    (
        "999",
        15,
        (
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia2", 10),
            (SIDE_IA, "Ia3", 37),
            (SIDE_IA, "Ia3", 71),
            (SIDE_IA, "Ia4", 112),
            (SIDE_IA, "Ia4", 154),
            (SIDE_IA, "Ia5", 2),
            (SIDE_IA, "Ia5", 23),
            (SIDE_IA, "Ia6", 92),
            (SIDE_IA, "Ia7", 68),
            (SIDE_IA, "Ia7", 129),
            (SIDE_IA, "Ia9", 129),
            (SIDE_IA, "Ia12", 47),
            (SIDE_IA, "Ia13", 109),
            (SIDE_IA, "Ia14", 140),
        ),
        (("999", "090", "076"),) * 15,
    ),
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
        "045",
        2,
        (
            (SIDE_IA, "Ia1", 15),
            (SIDE_IA, "Ia2", 37),
        ),
        (("045", "090", "076"),) * 2,
    ),
    (
        "076",
        2,
        (
            (SIDE_IA, "Ia2", 165),
            (SIDE_IA, "Ia13", 152),
        ),
        (("076", "090", "076"),) * 2,
    ),
    (
        "009",
        2,
        (
            (SIDE_IA, "Ia2", 174),
            (SIDE_IA, "Ia5", 164),
        ),
        (("009", "090", "076"),) * 2,
    ),
    (
        "071",
        2,
        (
            (SIDE_IA, "Ia3", 87),
            (SIDE_IA, "Ia7", 88),
        ),
        (("071", "090", "076"),) * 2,
    ),
    (
        "090",
        2,
        (
            (SIDE_IA, "Ia12", 42),
            (SIDE_IA, "Ia14", 105),
        ),
        (("090", "090", "076"),) * 2,
    ),
    (
        "048",
        1,
        ((SIDE_IA, "Ia1", 27),),
        (("048", "090", "076"),),
    ),
    (
        "380",
        1,
        ((SIDE_IA, "Ia1", 59),),
        (("380", "090", "076"),),
    ),
    (
        "011",
        1,
        ((SIDE_IA, "Ia1", 96),),
        (("011", "090", "076"),),
    ),
    (
        "499",
        1,
        ((SIDE_IA, "Ia2", 14),),
        (("499", "090", "076"),),
    ),
    (
        "497",
        1,
        ((SIDE_IA, "Ia2", 159),),
        (("497", "090", "076"),),
    ),
    (
        "036",
        1,
        ((SIDE_IA, "Ia3", 4),),
        (("036", "090", "076"),),
    ),
    (
        "092",
        1,
        ((SIDE_IA, "Ia4", 84),),
        (("092", "090", "076"),),
    ),
    (
        "291",
        1,
        ((SIDE_IA, "Ia4", 121),),
        (("291", "090", "076"),),
    ),
    (
        "522",
        1,
        ((SIDE_IA, "Ia4", 134),),
        (("522", "090", "076"),),
    ),
    (
        "150",
        1,
        ((SIDE_IA, "Ia4", 162),),
        (("150", "090", "076"),),
    ),
    (
        "078",
        1,
        ((SIDE_IA, "Ia4", 166),),
        (("078", "090", "076"),),
    ),
    (
        "295",
        1,
        ((SIDE_IA, "Ia5", 6),),
        (("295", "090", "076"),),
    ),
    (
        "000",
        1,
        ((SIDE_IA, "Ia5", 66),),
        (("000", "090", "076"),),
    ),
    (
        "109",
        1,
        ((SIDE_IA, "Ia5", 127),),
        (("109", "090", "076"),),
    ),
    (
        "052",
        1,
        ((SIDE_IA, "Ia6", 134),),
        (("052", "090", "076"),),
    ),
    (
        "099",
        1,
        ((SIDE_IA, "Ia7", 2),),
        (("099", "090", "076"),),
    ),
    (
        "700",
        1,
        ((SIDE_IA, "Ia7", 137),),
        (("700", "090", "076"),),
    ),
    (
        "161",
        1,
        ((SIDE_IA, "Ia8", 120),),
        (("161", "090", "076"),),
    ),
    (
        "010",
        1,
        ((SIDE_IA, "Ia10", 137),),
        (("010", "090", "076"),),
    ),
    (
        "205",
        1,
        ((SIDE_IA, "Ia10", 141),),
        (("205", "090", "076"),),
    ),
    (
        "382",
        1,
        ((SIDE_IA, "Ia12", 150),),
        (("382", "090", "076"),),
    ),
    (
        "386",
        1,
        ((SIDE_IA, "Ia13", 67),),
        (("386", "090", "076"),),
    ),
    (
        "008",
        1,
        ((SIDE_IA, "Ia13", 135),),
        (("008", "090", "076"),),
    ),
    (
        "027",
        1,
        ((SIDE_IA, "Ia13", 143),),
        (("027", "090", "076"),),
    ),
    (
        "724",
        1,
        ((SIDE_IA, "Ia14", 9),),
        (("724", "090", "076"),),
    ),
    (
        "400",
        1,
        ((SIDE_IA, "Ia14", 97),),
        (("400", "090", "076"),),
    ),
    (
        "326",
        1,
        ((SIDE_IA, "Ia14", 177),),
        (("326", "090", "076"),),
    ),
)


STANDING_N_DISTINCT_PREVIOUS_STEMS = 34
STANDING_N_HAPAX_PREVIOUS_STEMS = 27
STANDING_G = "999"
STANDING_K = 15
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_extra_090_076_share_one_previous_stem"
STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM = False
STANDING_RESULT = "i_leftover_extra_090_076_previous_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE225 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE225 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_OF_LEFTOVER_EXTRA_I_IS_NOT_THIS_CYCLE = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_UNIQUE_MAX_ALONE_DOES_NOT_MAKE_CLAIM_TRUE = True
STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL = True
STANDING_CYCLE259_N_I_ONLY = 2
STANDING_CYCLE259_N_NOT_I_ONLY = 0
STANDING_CYCLE258_N_I_ONLY = 19
STANDING_CYCLE258_N_NOT_I_ONLY = 0
STANDING_CYCLE258_N_EXTRA = 3
STANDING_CYCLE257_N_I_ONLY = 19
STANDING_CYCLE257_N_NOT_I_ONLY = 0
STANDING_CYCLE256_N_REMAINING11 = 19
STANDING_CYCLE256_K = 1
STANDING_CYCLE256_G = "755"
STANDING_CYCLE256_UNIQUE = False
STANDING_CYCLE225_N_DISTINCT = 30
STANDING_CYCLE225_G = "070"
STANDING_CYCLE225_K = 8
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE223_N_OFF_I = 3
STANDING_CYCLE207_N_I = 8
STANDING_CYCLE207_N_OFF_I = 1


def leftover_extra_previous_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str | None, ...]:
    """Per-site previous stem or None for the locked leftover extra sites."""
    return tuple(
        site_previous_stem(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_extra_backward_3grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site backward 3-gram or None for the locked leftover extra sites."""
    return tuple(
        site_backward_3gram(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_extra_previous_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site previous 4-gram or None for the locked leftover extra sites."""
    return tuple(
        site_previous_4gram(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_sites_with_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites that have a previous stem before 090 076."""
    return leftover_sites_with_backward(sites, previous_stems)


def leftover_sites_without_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites that are line-initial (no previous token)."""
    return leftover_sites_without_backward(sites, previous_stems)


def previous_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_PREVIOUS_STEM_FREQUENCY,
) -> list[dict]:
    """Survey-shaped previous-stem frequency table, highest count first."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "previous_stem": stem,
                "count": count,
                "leftover_sites": [list(site) for site in sites],
                "backward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def rank_previous_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Previous stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_previous_g(
    previous_stems: tuple[str | None, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Unique-max else largest-id."""
    ranked = rank_previous_stems(
        Counter(stem for stem in previous_stems if stem is not None)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def i_leftover_extra_090_076_share_one_previous_stem(
    n_distinct_previous_stems: int,
    n_with_previous: int,
) -> bool:
    """True iff N_distinct==1 and N_with_previous>=2."""
    return n_distinct_previous_stems == 1 and n_with_previous >= 2


class TestILeftoverExtra090076PreviousStemHelpers(unittest.TestCase):
    """Helpers on leftover extra I 090 076 previous stems. No CV, no LLM."""

    def test_previous_requires_stem_before_2gram(self):
        """A previous stem is a 3-gram; line-initial is no-previous."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N3, STANDING_N2 + 1)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_999 = ["602", "999", "090", "076", "012", "076"]
        self.assertEqual(site_previous_stem(has_999, 2, GRAM2), "999")
        self.assertEqual(
            site_backward_3gram(has_999, 2, GRAM2),
            ("999", "090", "076"),
        )
        self.assertEqual(
            site_previous_4gram(has_999, 2, GRAM2),
            ("602", "999", "090", "076"),
        )
        line_initial = ["090", "076", "012"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(line_initial, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(line_initial, 0, GRAM2))
        one_token_before = ["999", "090", "076"]
        self.assertEqual(site_previous_stem(one_token_before, 1, GRAM2), "999")
        self.assertEqual(
            site_backward_3gram(one_token_before, 1, GRAM2),
            ("999", "090", "076"),
        )
        self.assertIsNone(site_previous_4gram(one_token_before, 1, GRAM2))
        mismatch_071 = ["999", "076", "071", "090"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_one_distinct_and_at_least_two_with_previous(self):
        """Boolean is True only when N_distinct=1 and N_with_previous>=2."""
        provider = MockProvider()
        self.assertTrue(i_leftover_extra_090_076_share_one_previous_stem(1, 2))
        self.assertTrue(i_leftover_extra_090_076_share_one_previous_stem(1, 56))
        self.assertFalse(i_leftover_extra_090_076_share_one_previous_stem(34, 56))
        self.assertFalse(i_leftover_extra_090_076_share_one_previous_stem(30, 55))
        self.assertFalse(i_leftover_extra_090_076_share_one_previous_stem(2, 56))
        self.assertFalse(i_leftover_extra_090_076_share_one_previous_stem(1, 1))
        self.assertFalse(i_leftover_extra_090_076_share_one_previous_stem(1, 0))
        self.assertFalse(i_leftover_extra_090_076_share_one_previous_stem(0, 0))
        self.assertEqual(STANDING_CLAIM, "i_leftover_extra_090_076_share_one_previous_stem")
        self.assertFalse(STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(STANDING_N_DISTINCT_PREVIOUS_STEMS, 34)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 56)
        self.assertEqual(STANDING_G, "999")
        self.assertEqual(STANDING_K, 15)
        self.assertTrue(STANDING_UNIQUE_MAX_ALONE_DOES_NOT_MAKE_CLAIM_TRUE)
        self.assertEqual(provider.get_call_history(), [])

    def test_frequency_table_sorts_highest_count_first_and_skips_none(self):
        """Frequency table is count-desc; no-previous sites are omitted."""
        provider = MockProvider()
        sites = STANDING_LEFTOVER_SITES[:6]
        prev = ("999", "045", "999", "600", None, "999")
        grams = (
            ("999", "090", "076"),
            ("045", "090", "076"),
            ("999", "090", "076"),
            ("600", "090", "076"),
            None,
            ("999", "090", "076"),
        )
        table = previous_stem_frequency_table(sites, prev, grams)
        self.assertEqual(table[0][0], "999")
        self.assertEqual(table[0][1], 3)
        self.assertEqual(table[1][0], "045")
        self.assertEqual(table[1][1], 1)
        self.assertEqual(table[2][0], "600")
        self.assertEqual(table[2][1], 1)
        self.assertEqual(len(table), 3)
        self.assertEqual(leftover_sites_without_previous(sites, prev), (sites[4],))
        self.assertEqual(
            leftover_sites_with_previous(sites, prev),
            (sites[0], sites[1], sites[2], sites[3], sites[5]),
        )
        shared = ("999",) * 6
        shared_grams = (("999", "090", "076"),) * 6
        shared_table = previous_stem_frequency_table(sites, shared, shared_grams)
        self.assertEqual(len(shared_table), 1)
        self.assertEqual(shared_table[0][0], "999")
        self.assertEqual(shared_table[0][1], 6)
        g, k, unique = select_previous_g(("070", "071", "070"))
        self.assertEqual(g, "070")
        self.assertEqual(k, 2)
        self.assertTrue(unique)
        tied = select_previous_g(("070", "071"))
        self.assertEqual(tied[0], "071")
        self.assertEqual(tied[1], 1)
        self.assertFalse(tied[2])
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076PreviousStemScoreboard(unittest.TestCase):
    """Cited-fixture leftover extra 090 076 previous-stem lock. Mock only."""

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
        self.with_previous = leftover_sites_with_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.no_previous = leftover_sites_without_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.first_seen = group_sites_by_previous_stem(
            self.leftover_sites,
            self.previous_stems,
        )
        self.frequency = previous_stem_frequency_table(
            self.leftover_sites,
            self.previous_stems,
            self.backwards,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = CYCLE224_N_INSIDE
        self.n_leftover = len(self.leftover_sites)
        self.n_leftover_extra = self.n_leftover
        self.n_with_previous = len(self.with_previous)
        self.n_no_previous = len(self.no_previous)
        self.n_distinct = len(self.first_seen)
        self.g, self.k, self.unique = select_previous_g(self.previous_stems)
        self.claim_holds = i_leftover_extra_090_076_share_one_previous_stem(
            self.n_distinct,
            self.n_with_previous,
        )

    def test_tokens_and_sites_are_cycle_224_leftover_extra_not_retuned(self):
        """2-gram and leftover extra 56 stay the cycle-224/223/225 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_i, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_I"], 69)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(prior_224["i_090_076_all_inside_leftover_n4_remaining_family"])
        self.assertFalse(CYCLE224_ALL_INSIDE)
        self.assertEqual(
            tuple(tuple(row) for row in prior_224["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_224["inside_sites"]),
            CYCLE224_INSIDE_SITES,
        )
        prior_225 = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(prior_225["cycle"], 225)
        self.assertFalse(prior_225["i_leftover_extra_090_076_share_one_forward_stem"])
        self.assertFalse(CYCLE225_SHARE_ONE)
        self.assertEqual(prior_225["N_distinct_next_stems"], 30)
        self.assertEqual(prior_225["N_distinct_next_stems"], CYCLE225_N_DISTINCT)
        self.assertEqual(prior_225["G"], "070")
        self.assertEqual(prior_225["G"], CYCLE225_G)
        self.assertEqual(prior_225["K"], 8)
        self.assertEqual(prior_225["K"], CYCLE225_K)
        self.assertEqual(prior_225["N_leftover"], 56)
        self.assertEqual(prior_225["N_with_next"], 55)
        self.assertEqual(prior_225["N_no_next"], 1)
        if (
            prior_225["N_distinct_next_stems"] != 30
            or prior_225["G"] != "070"
            or prior_225["K"] != 8
            or prior_225["i_leftover_extra_090_076_share_one_forward_stem"]
        ):
            self.fail("nested cycle 225 30 distinct G=070 K=8 share-one-forward lost drifted")
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_OF_LEFTOVER_EXTRA_I_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        unused = leftover_extra_next_stems
        self.assertTrue(callable(unused))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_34_distinct_previous_stems_and_claim_loses(self):
        """N_leftover_extra=56, N_with_previous=56, N_distinct=34, G=999 K=15. Claim loses."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 56)
        self.assertEqual(self.n_no_previous, STANDING_N_NO_PREVIOUS)
        self.assertEqual(STANDING_N_NO_PREVIOUS, 0)
        self.assertEqual(self.no_previous, STANDING_NO_PREVIOUS_SITES)
        self.assertEqual(STANDING_NO_PREVIOUS_SITES, ())
        self.assertEqual(self.n_with_previous + self.n_no_previous, self.n_leftover)
        self.assertEqual(56 + 0, 56)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_PREVIOUS_STEMS)
        self.assertEqual(STANDING_N_DISTINCT_PREVIOUS_STEMS, 34)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "999")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 15)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertGreater(STANDING_K, STANDING_PREVIOUS_STEM_FREQUENCY[1][1])
        if self.n_distinct != 1:
            self.assertFalse(
                i_leftover_extra_090_076_share_one_previous_stem(
                    self.n_distinct,
                    self.n_with_previous,
                )
            )
        self.assertNotEqual(self.n_distinct, 1)
        self.assertFalse(
            i_leftover_extra_090_076_share_one_previous_stem(
                self.n_distinct,
                self.n_with_previous,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM,
        )
        self.assertFalse(STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(STANDING_CLAIM, "i_leftover_extra_090_076_share_one_previous_stem")
        self.assertEqual(self.previous_stems, STANDING_PER_SITE_PREVIOUS_STEMS)
        self.assertEqual(self.backwards, STANDING_PER_SITE_BACKWARD_3GRAMS)
        self.assertEqual(self.previous_4grams, STANDING_PER_SITE_PREVIOUS_4GRAMS)
        self.assertEqual(
            tuple(stem for stem, _sites in self.first_seen),
            STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN,
        )
        self.assertEqual(len(STANDING_PREVIOUS_STEM_FREQUENCY), 34)
        self.assertEqual(STANDING_N_HAPAX_PREVIOUS_STEMS, 27)
        hapax = tuple(row for row in self.frequency if row[1] == 1)
        self.assertEqual(len(hapax), STANDING_N_HAPAX_PREVIOUS_STEMS)
        self.assertEqual(
            sum(count for _stem, count, _sites, _grams in self.frequency),
            56,
        )
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE225)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE225)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_OF_LEFTOVER_EXTRA_I_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_UNIQUE_MAX_ALONE_DOES_NOT_MAKE_CLAIM_TRUE)
        self.assertTrue(STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_frequency_table_and_unique_max_g_999_k_15(self):
        """G=999 K=15 is unique-max inventory; all leftover extra sites have a previous token."""
        self.assertEqual(self.frequency, STANDING_PREVIOUS_STEM_FREQUENCY)
        counts = [row[1] for row in self.frequency]
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertEqual(counts[0], 15)
        self.assertEqual(self.frequency[0][0], "999")
        self.assertEqual(self.frequency[0][2], STANDING_G_SITES)
        self.assertEqual(len(STANDING_G_SITES), 15)
        self.assertEqual(self.g, "999")
        self.assertEqual(self.k, 15)
        self.assertTrue(self.unique)
        for site, prev, bwd3, prev4 in zip(
            STANDING_LEFTOVER_SITES,
            STANDING_PER_SITE_PREVIOUS_STEMS,
            STANDING_PER_SITE_BACKWARD_3GRAMS,
            STANDING_PER_SITE_PREVIOUS_4GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(site_previous_stem(stems, index, GRAM2), prev)
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), bwd3)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), prev4)
            self.assertIsNotNone(prev)
            self.assertGreater(index, 0)
            self.assertEqual(stems[index - 1], prev)
            self.assertEqual(bwd3, (prev, "090", "076"))
            self.assertIsNotNone(prev4)
            self.assertEqual(prev4[1:], bwd3)
            self.assertEqual(prev4[2:], GRAM2)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
        for stem, count, sites, grams in STANDING_PREVIOUS_STEM_FREQUENCY:
            self.assertEqual(len(sites), count)
            self.assertEqual(len(grams), count)
            for site, gram3 in zip(sites, grams, strict=True):
                self.assertEqual(gram3[0], stem)
                self.assertEqual(gram3[1:], GRAM2)
                self.assertIn(site, STANDING_LEFTOVER_SITES)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_259_258_257_256_225_223_and_207_still_compute(self):
        """Cycle 259 2/0, 258 19/19 extra I=3, 257 19/19, 256 19/K=1/G=755, 225 30/070/8, 223 69/3, 207 8/1 stay."""
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_259.test_survey_matches_computed_lock()
        self.assertEqual(prior_259.n_i_only, 2)
        self.assertEqual(prior_259.n_not_i_only, 0)
        self.assertTrue(prior_259.claim_holds)
        self.assertTrue(CYCLE259_CLAIM)
        if prior_259.n_i_only != 2 or prior_259.n_not_i_only != 0:
            self.fail("nested cycle 259 extra-I 4-grams 2/0 drifted")
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_258.test_survey_matches_computed_lock()
        self.assertEqual(prior_258.n_i_only, 19)
        self.assertEqual(prior_258.n_not_i_only, 0)
        self.assertEqual(sum(prior_258.n_extra), 3)
        self.assertTrue(prior_258.claim_holds)
        self.assertTrue(CYCLE258_CLAIM)
        if (
            prior_258.n_i_only != 19
            or prior_258.n_not_i_only != 0
            or sum(prior_258.n_extra) != 3
        ):
            self.fail("nested cycle 258 remaining-after-000 3-grams 19/19 extra I=3 drifted")
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
        prior_225 = TestMamariILeftoverExtra090076ForwardStemScoreboard()
        prior_225.setUp()
        prior_225.test_counts_30_distinct_next_stems_and_claim_loses()
        prior_225.test_survey_matches_computed_lock()
        self.assertEqual(prior_225.n_leftover, CYCLE225_N_LEFTOVER)
        self.assertEqual(prior_225.n_leftover, 56)
        self.assertEqual(prior_225.n_with_next, CYCLE225_N_WITH_NEXT)
        self.assertEqual(prior_225.n_no_next, CYCLE225_N_NO_NEXT)
        self.assertEqual(prior_225.n_distinct, CYCLE225_N_DISTINCT)
        self.assertEqual(prior_225.n_distinct, 30)
        self.assertEqual(prior_225.g, CYCLE225_G)
        self.assertEqual(prior_225.g, "070")
        self.assertEqual(prior_225.k, CYCLE225_K)
        self.assertEqual(prior_225.k, 8)
        self.assertFalse(prior_225.claim_holds)
        self.assertFalse(CYCLE225_SHARE_ONE)
        if (
            prior_225.n_distinct != 30
            or prior_225.g != "070"
            or prior_225.k != 8
            or prior_225.claim_holds
        ):
            self.fail("nested cycle 225 share-one-forward lost 30 distinct G=070 K=8 drifted")
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
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_OF_LEFTOVER_EXTRA_I_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-260 leftover extra previous-stem lock."""
        lock = self.survey["i_leftover_extra_090_076_previous_stem"]
        self.assertEqual(lock["cycle"], 260)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_one_previous_stem"])
        self.assertEqual(
            lock["hypothesis_share_one_previous_stem"],
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 56)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(
            lock["N_distinct_previous_stems"],
            STANDING_N_DISTINCT_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_distinct_previous_stems"], 34)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "999")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 15)
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["G_sites"]),
            STANDING_G_SITES,
        )
        self.assertEqual(
            tuple(lock["distinct_previous_stems"]),
            STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN,
        )
        self.assertEqual(
            list(STANDING_PER_SITE_PREVIOUS_STEMS),
            lock["per_site_previous_stems"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_PER_SITE_BACKWARD_3GRAMS],
            lock["per_site_backward_3grams"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS],
            lock["per_site_previous_4grams"],
        )
        self.assertEqual(
            lock["previous_stem_frequency"],
            previous_stem_frequency_rows(STANDING_PREVIOUS_STEM_FREQUENCY),
        )
        self.assertEqual(len(lock["previous_stem_frequency"]), 34)
        self.assertEqual(lock["previous_stem_frequency"][0]["previous_stem"], "999")
        self.assertEqual(lock["previous_stem_frequency"][0]["count"], 15)
        self.assertEqual(lock["N_hapax_previous_stems"], STANDING_N_HAPAX_PREVIOUS_STEMS)
        self.assertEqual(lock["N_hapax_previous_stems"], 27)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_extra_090_076_share_one_previous_stem"])
        self.assertEqual(
            lock["i_leftover_extra_090_076_share_one_previous_stem"],
            STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM,
        )
        self.assertEqual(lock["nested_cycle259_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle259_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle258_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle258_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle258_N_extra"], 3)
        self.assertEqual(lock["nested_cycle257_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle257_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle256_N_remaining11"], 19)
        self.assertEqual(lock["nested_cycle256_K"], 1)
        self.assertEqual(lock["nested_cycle256_G"], "755")
        self.assertFalse(lock["nested_cycle256_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle225_N_distinct_next_stems"], 30)
        self.assertEqual(lock["nested_cycle225_G"], "070")
        self.assertEqual(lock["nested_cycle225_K"], 8)
        self.assertFalse(lock["nested_cycle225_share_one_forward_stem"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle225"])
        self.assertTrue(lock["same_claim_shape_as_cycle225"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["leftover_of_leftover_extra_i_is_not_this_cycle"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["unique_max_alone_does_not_make_claim_true"])
        self.assertTrue(lock["g_k_is_inventory_for_later_peel"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["cycle"], 225)
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_forward_stem"][
                "i_leftover_extra_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_forward_stem"]["N_distinct_next_stems"],
            30,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["G"], "070")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["K"], 8)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]["cycle"],
            259,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]["cycle"],
            258,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"]["cycle"],
            257,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]["cycle"],
            256,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
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


class TestMamariILeftoverExtra090076PreviousStemImageSnapshot(unittest.TestCase):
    """Cycle 260 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
