"""I's leftover n=5 remaining remaining-after-090-076 remaining-after-430-076 remaining-after-076-020 remaining-after-076-010 leftover 5-grams I-only lock.

Cycle 414 text-search lock. Uses already-vendored A–V and the
cycle-340 leftover n=4 remaining remaining-after-090-076
remaining-after-430-076 remaining-after-076-020 remaining-
after-076-010 leftover 4-grams (N=5, all I-only extra I=0).
Leftover 5-grams remaining of that family after leftover-2
peels (090 076, 430 076, 076 020, 076 010, nested 076 006 /
076 011): leftover-4 remaining plus one extra I token at
leftover matching leftover-4 sites of leftover 4-grams that
do not contain those leftover-2 peels. Nested leftover-2
matches (076 006, 076 011) stay peeled as leftover 2-grams
(cycle 349). Do not re-peel leftover matching leftover-2 of
leftover 5-grams=18. Does not retune leftover n=4, leftover
3-gram I-only (cycle 341 extra I=5), leftover 2-gram I-only
(cycle 349 LOSE 9/6 extra I=116), extra-I previous-3-gram
5-grams (cycle 413 HOLD extra I=0), extra-I previous-3-gram
4-grams (cycle 412 HOLD extra I=1), previous 3-grams (cycle
411 HOLD extra I=2), or leftover 4-gram I-only (cycle 340
extra I=0). Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a
meaning dictionary. Do not peel labeled G with exactly-1-share.
Do not launch extra-I peels. Do not launch next/prev N of
leftover 5-grams.

Population (locked, do not re-derive as a new claim): leftover
n=4 remaining remaining-after-090-076 remaining-after-430-076
remaining-after-076-020 remaining-after-076-010 leftover
4-grams 028 076 011 076 / 071 999 604 076 / 202 076 006 055 /
076 999 029 076 / 700 076 076 053 (cycle 340 HOLD extra I=0,
leftover matching leftover-4 sites=11). Leftover 4-grams that
contain leftover-2 peels 076 011 / 076 006 stay peeled
(028 076 011 076, 202 076 006 055). Remaining leftover
4-grams after leftover-2 peels: 071 999 604 076 /
076 999 029 076 / 700 076 076 053 (leftover matching leftover-4
sites=6). Leftover 5-grams remaining = leftover-4 remaining
plus one extra I token (next or previous) at those leftover
matching leftover-4 sites. The twelve leftover 5-grams (all
hapax I-only extra I=0):
071 999 604 076 460 leftover matching Ia1[63];
700 071 999 604 076 leftover matching Ia1[62];
071 999 604 076 000 leftover matching Ia9[3];
065 071 999 604 076 leftover matching Ia9[2];
076 999 029 076 022 leftover matching Ia8[30];
070 076 999 029 076 leftover matching Ia8[29];
076 999 029 076 048 leftover matching Ia10[144];
000 076 999 029 076 leftover matching Ia10[143];
700 076 076 053 720 leftover matching Ia8[167];
087 700 076 076 053 leftover matching Ia8[166];
700 076 076 053 177 leftover matching Ia9[32];
600 700 076 076 053 leftover matching Ia9[31].
N leftover 5-grams=12 leftover matching leftover-5 remaining
sites=12 (complete) N_distinct=12 N_i_only=12 N_leak=0
N_hapax=12 N_not_hapax=0 extra I of leftover 5-grams=0
leftover matching leftover-4 of leftover 5-grams=6 leftover
matching leftover-3 of leftover 5-grams=12 leftover matching
leftover-2 of leftover 5-grams=18 (nested cycle 349). Nested
leftover remaining-after-076-010 4grams / 3grams / 413 / 412 /
411 / 349 / 340 stay nested.

Already locked (record overlap only, do not re-lock): nested
leftover remaining-after-076-010 4grams / 3grams / extra-I
prev3-tokens 5grams (413) / extra-I prev3-tokens 4grams (412) /
prev3-tokens (411) / leftover 2-grams (349) / leftover 4-grams
(340) stay nested and unchanged in meaning.

Same claim-shape as cycle 340 leftover remaining-after-076-010
leftover 4-grams all I-only extra I=0 HOLD. Hapax of the
5-grams is not required (this cycle's leftover 5-grams
happened to be hapax). Extra I ≠ 0 would be recorded, not
this cycle's claim; extra-I peel is closed (extra I=0). Do
not retune leftover n=4. Nested leftover-2 matches stay
peeled. Do not peel labeled G with exactly-1-share.

Locks exact consecutive hits of each leftover remaining-
after-076-010 leftover 5-gram on tablet I and on every other
vendored tablet A–H and J–V. Claim that can lose:
i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only.
True iff all twelve leftover 5-grams have N_I ≥ 1 and
N_off_I = 0 (N_leak=0 per 5-gram) and leftover matching
leftover-5 remaining sites=12 (complete). This can lose if
any leaks onto T (or any off-I tablet) or if the leftover-5
remaining set is incomplete. Measured: every leftover 5-gram
N_I=1 N_off_I=0 N_leak=0 hapax leftover matching leftover-5
remaining sites=12 extra I=0. The claim is true. Do not
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
from tests.test_mamari_i_2gram_076_010_i_only_scoreboard import (
    named_off_i_sites,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_2grams_i_only_scoreboard import (
    STANDING_CLAIM as CYCLE349_CLAIM,
    STANDING_N_I_ONLY as CYCLE349_N_I_ONLY,
    STANDING_N_LEAK as CYCLE349_N_LEAK,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760102gramsIOnlyScoreboard,
    leftover_matching_2gram_sites_each,
    leftover_remaining_2grams,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_3GRAMS_ALL_I_ONLY as CYCLE341_CLAIM,
    STANDING_N_EXTRA as CYCLE341_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE341_N_I_ONLY,
    STANDING_N_LEAK as CYCLE341_N_LEAK,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760103gramsIOnlyScoreboard,
    leftover_matching_3gram_sites_each,
    leftover_remaining_3grams,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_i_only_scoreboard import (
    GRAM4_028,
    GRAM4_071,
    GRAM4_076,
    GRAM4_202,
    GRAM4_700,
    STANDING_I_LEFTOVER_N4_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_4GRAMS_ALL_I_ONLY as CYCLE340_CLAIM,
    STANDING_LEFTOVER_MATCHING_COUNT as CYCLE340_LEFTOVER_MATCHING_COUNT,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE340_LEFTOVER_MATCHING,
    STANDING_N as CYCLE340_N,
    STANDING_N_EXTRA as CYCLE340_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE340_N_I_ONLY,
    STANDING_SEQUENCES as CYCLE340_SEQUENCES,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760104gramsIOnlyScoreboard,
    i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_all_i_only,
    leftover_matching_4gram_sites,
    leftover_remaining_grams,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_prev3_tokens_4grams_i_only_scoreboard import (
    STANDING_CLAIM as CYCLE412_CLAIM,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraIPrev3Tokens4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_prev3_tokens_5grams_i_only_scoreboard import (
    STANDING_CLAIM as CYCLE413_CLAIM,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraIPrev3Tokens5gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_next_2gram_scoreboard import (
    leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010,
)
from tests.test_mamari_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_prev3_tokens_i_only_scoreboard import (
    STANDING_CLAIM as CYCLE411_CLAIM,
    TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Prev3TokensIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    leftover_n4_family_counts_hold,
    leftover_n4_rows,
    leftover_remaining_n4,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
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
NESTED_LEFTOVER2_PEELS = (("076", "006"), ("076", "011"))
NEAR_MISS_090_076 = ("090", "076")
NEAR_MISS_430_076 = ("430", "076")
NEAR_MISS_076_020 = ("076", "020")
NEAR_MISS_076_010 = ("076", "010")
GRAM5_071_FWD_IA1 = ("071", "999", "604", "076", "460")
GRAM5_071_PREV_IA1 = ("700", "071", "999", "604", "076")
GRAM5_071_FWD_IA9 = ("071", "999", "604", "076", "000")
GRAM5_071_PREV_IA9 = ("065", "071", "999", "604", "076")
GRAM5_076_FWD_IA8 = ("076", "999", "029", "076", "022")
GRAM5_076_PREV_IA8 = ("070", "076", "999", "029", "076")
GRAM5_076_FWD_IA10 = ("076", "999", "029", "076", "048")
GRAM5_076_PREV_IA10 = ("000", "076", "999", "029", "076")
GRAM5_700_FWD_IA8 = ("700", "076", "076", "053", "720")
GRAM5_700_PREV_IA8 = ("087", "700", "076", "076", "053")
GRAM5_700_FWD_IA9 = ("700", "076", "076", "053", "177")
GRAM5_700_PREV_IA9 = ("600", "700", "076", "076", "053")
STANDING_SEQUENCES = (
    GRAM5_071_FWD_IA1,
    GRAM5_071_PREV_IA1,
    GRAM5_071_FWD_IA9,
    GRAM5_071_PREV_IA9,
    GRAM5_076_FWD_IA8,
    GRAM5_076_PREV_IA8,
    GRAM5_076_FWD_IA10,
    GRAM5_076_PREV_IA10,
    GRAM5_700_FWD_IA8,
    GRAM5_700_PREV_IA8,
    GRAM5_700_FWD_IA9,
    GRAM5_700_PREV_IA9,
)
STANDING_PARENT_4GRAMS = (
    GRAM4_071,
    GRAM4_071,
    GRAM4_071,
    GRAM4_071,
    GRAM4_076,
    GRAM4_076,
    GRAM4_076,
    GRAM4_076,
    GRAM4_700,
    GRAM4_700,
    GRAM4_700,
    GRAM4_700,
)
STANDING_ROLES = (
    "next",
    "prev",
    "next",
    "prev",
    "next",
    "prev",
    "next",
    "prev",
    "next",
    "prev",
    "next",
    "prev",
)
STANDING_N = 12
STANDING_N4_REMAINING_AFTER_LEFTOVER2 = 3
STANDING_N4 = 4
STANDING_N5 = 5
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N_I_EACH = (1,) * STANDING_N
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_I_SITES = (
    ((SIDE_IA, "Ia1", 63),),
    ((SIDE_IA, "Ia1", 62),),
    ((SIDE_IA, "Ia9", 3),),
    ((SIDE_IA, "Ia9", 2),),
    ((SIDE_IA, "Ia8", 30),),
    ((SIDE_IA, "Ia8", 29),),
    ((SIDE_IA, "Ia10", 144),),
    ((SIDE_IA, "Ia10", 143),),
    ((SIDE_IA, "Ia8", 167),),
    ((SIDE_IA, "Ia8", 166),),
    ((SIDE_IA, "Ia9", 32),),
    ((SIDE_IA, "Ia9", 31),),
)
STANDING_LEFTOVER_MATCHING_SITES = (
    (SIDE_IA, "Ia1", 63),
    (SIDE_IA, "Ia1", 62),
    (SIDE_IA, "Ia9", 3),
    (SIDE_IA, "Ia9", 2),
    (SIDE_IA, "Ia8", 30),
    (SIDE_IA, "Ia8", 29),
    (SIDE_IA, "Ia10", 144),
    (SIDE_IA, "Ia10", 143),
    (SIDE_IA, "Ia8", 167),
    (SIDE_IA, "Ia8", 166),
    (SIDE_IA, "Ia9", 32),
    (SIDE_IA, "Ia9", 31),
)
STANDING_LEFTOVER_MATCHING_COUNT = 12
STANDING_LEFTOVER_MATCHING_5GRAMS = STANDING_SEQUENCES
STANDING_LEFTOVER_MATCHING_LEFTOVER4_SITES = (
    (SIDE_IA, "Ia1", 63),
    (SIDE_IA, "Ia9", 3),
    (SIDE_IA, "Ia8", 30),
    (SIDE_IA, "Ia10", 144),
    (SIDE_IA, "Ia8", 167),
    (SIDE_IA, "Ia9", 32),
)
STANDING_LEFTOVER_MATCHING_LEFTOVER4 = 6
STANDING_LEFTOVER_MATCHING_LEFTOVER3_SITES = (
    (SIDE_IA, "Ia1", 63),
    (SIDE_IA, "Ia1", 64),
    (SIDE_IA, "Ia9", 3),
    (SIDE_IA, "Ia9", 4),
    (SIDE_IA, "Ia8", 30),
    (SIDE_IA, "Ia8", 31),
    (SIDE_IA, "Ia10", 144),
    (SIDE_IA, "Ia10", 145),
    (SIDE_IA, "Ia8", 167),
    (SIDE_IA, "Ia8", 168),
    (SIDE_IA, "Ia9", 32),
    (SIDE_IA, "Ia9", 33),
)
STANDING_LEFTOVER_MATCHING_LEFTOVER3 = 12
STANDING_LEFTOVER_MATCHING_LEFTOVER2_SITES = (
    (SIDE_IA, "Ia1", 63),
    (SIDE_IA, "Ia1", 64),
    (SIDE_IA, "Ia1", 65),
    (SIDE_IA, "Ia9", 3),
    (SIDE_IA, "Ia9", 4),
    (SIDE_IA, "Ia9", 5),
    (SIDE_IA, "Ia8", 30),
    (SIDE_IA, "Ia8", 31),
    (SIDE_IA, "Ia8", 32),
    (SIDE_IA, "Ia10", 144),
    (SIDE_IA, "Ia10", 145),
    (SIDE_IA, "Ia10", 146),
    (SIDE_IA, "Ia8", 167),
    (SIDE_IA, "Ia8", 168),
    (SIDE_IA, "Ia8", 169),
    (SIDE_IA, "Ia9", 32),
    (SIDE_IA, "Ia9", 33),
    (SIDE_IA, "Ia9", 34),
)
STANDING_LEFTOVER_MATCHING_LEFTOVER2 = 18
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N
STANDING_N_LEAK_EACH = STANDING_N_OFF_I_EACH
STANDING_OFF_I_SITES = ((),) * STANDING_N
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (STANDING_HITS_BY_TABLET_ONE_ON_I,) * STANDING_N
STANDING_N_I_ONLY = 12
STANDING_N_NOT_I_ONLY = 0
STANDING_N_LEAKING = 0
STANDING_N_LEAK = 0
STANDING_N_DISTINCT = 12
STANDING_LEAKING_5GRAMS = ()
STANDING_N_EXTRA_EACH = (0,) * STANDING_N
STANDING_EXTRA_I_SITES = ((),) * STANDING_N
STANDING_N_EXTRA = 0
STANDING_HAPAX_EACH = (True,) * STANDING_N
STANDING_N_HAPAX = 12
STANDING_N_NOT_HAPAX = 0
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_NOT_REQUIRED = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = (
    "i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only"
)
STANDING_I_LEFTOVER_N5_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_ALL_I_ONLY = (
    True
)
STANDING_I_LEFTOVER_N5_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_5GRAMS_I_ONLY = (
    True
)
STANDING_RESULT = (
    "i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_5grams_i_only"
)
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_CYCLE340 = False
STANDING_SAME_AS_CYCLE341 = False
STANDING_SAME_AS_CYCLE349 = False
STANDING_SAME_AS_CYCLE411 = False
STANDING_SAME_AS_CYCLE412 = False
STANDING_SAME_AS_CYCLE413 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE340 = True
STANDING_LABELED_G_DOES_NOT_COUNT = True
STANDING_PEEL_LABELED_G_IS_TAUTOLOGY = True
STANDING_ALL_I_INSIDE_FAMILY_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_REPEEL_LEFTOVER2 = True
STANDING_DO_NOT_LAUNCH_EXTRA_I_PEELS = True
STANDING_DO_NOT_LAUNCH_NEXT_PREV_N = True
STANDING_CYCLE413_DOES_NOT_COUNT = True
STANDING_CYCLE412_DOES_NOT_COUNT = True
STANDING_CYCLE411_DOES_NOT_COUNT = True
STANDING_CYCLE349_DOES_NOT_COUNT = True
STANDING_CYCLE341_DOES_NOT_COUNT = True
STANDING_CYCLE340_DOES_NOT_COUNT = True


def leftover_4grams_remaining_after_leftover2_peels(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] | None = None,
) -> tuple[tuple[tuple[str, ...], int, int, tuple], ...]:
    """Leftover remaining-after-076-010 4-grams that do not contain leftover-2 peels."""
    remaining = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
        leftovers
    )
    return tuple(
        row
        for row in remaining
        if not any(is_contiguous_substring(peel, row[0]) for peel in NESTED_LEFTOVER2_PEELS)
    )


def leftover_remaining_5grams(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] | None = None,
    i_sides: dict | None = None,
) -> tuple[tuple[str, ...], ...]:
    """Leftover-4 remaining plus one extra I token at leftover matching leftover-4 sites."""
    if i_sides is None:
        i_sides = load_i_sides()
    remaining = leftover_4grams_remaining_after_leftover2_peels(leftovers)
    out: list[tuple[str, ...]] = []
    for _gram4, _n, _f, sites in remaining:
        for side, line, index in sites:
            stems = i_sides[side][IA_LINE_NAMES.index(line)]
            out.append(tuple(stems[index : index + STANDING_N5]))
            out.append(tuple(stems[index - 1 : index + STANDING_N4]))
    return tuple(out)


def leftover_matching_5gram_sites(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] | None = None,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching leftover-5 remaining sites of leftover-4 remaining plus extra I token."""
    remaining = leftover_4grams_remaining_after_leftover2_peels(leftovers)
    out: list[tuple[str, str, int]] = []
    for _gram4, _n, _f, sites in remaining:
        for side, line, index in sites:
            out.append((side, line, index))
            out.append((side, line, index - 1))
    return tuple(out)


def leftover_matching_leftover4_of_leftover5(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] | None = None,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching leftover-4 sites of leftover 4-grams remaining after leftover-2 peels."""
    remaining = leftover_4grams_remaining_after_leftover2_peels(leftovers)
    return tuple(site for _gram, _n, _f, sites in remaining for site in sites)


def leftover_matching_leftover3_of_leftover5(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] | None = None,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching leftover-3 sites of leftover 4-grams remaining after leftover-2 peels."""
    remaining = leftover_4grams_remaining_after_leftover2_peels(leftovers)
    out: list[tuple[str, str, int]] = []
    for _gram, _n, _f, sites in remaining:
        for side, line, index in sites:
            out.append((side, line, index))
            out.append((side, line, index + 1))
    return tuple(out)


def leftover_matching_leftover2_of_leftover5(
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] | None = None,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover matching leftover-2 sites of leftover 4-grams remaining after leftover-2 peels."""
    remaining = leftover_4grams_remaining_after_leftover2_peels(leftovers)
    out: list[tuple[str, str, int]] = []
    for _gram, _n, _f, sites in remaining:
        for side, line, index in sites:
            out.append((side, line, index))
            out.append((side, line, index + 1))
            out.append((side, line, index + 2))
    return tuple(out)


def leftover_matching_subset(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    i_sites: tuple[tuple[tuple[str, str, int], ...], ...] = STANDING_I_SITES,
) -> bool:
    """True iff leftover matching leftover-5 remaining sites equal the union of I sites."""
    measured = set(site for sites in i_sites for site in sites)
    return set(leftover_sites) == measured


def extra_i_sites_of_5gram(
    i_sites: tuple[tuple[str, str, int], ...],
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 5-gram sites outside leftover matching leftover-5 remaining sites."""
    leftover_set = set(leftover_matching)
    return tuple(site for site in i_sites if site not in leftover_set)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def leaking_5grams(
    sequences: tuple[tuple[str, ...], ...],
    n_off_i: tuple[int, ...],
) -> tuple[tuple[str, ...], ...]:
    """Distinct leftover 5-grams with N_off_I>0."""
    return tuple(
        gram
        for gram, off in zip(sequences, n_off_i, strict=True)
        if off > 0
    )


def i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    sequences: tuple[tuple[str, ...], ...] = STANDING_SEQUENCES,
    expected_n: int = STANDING_N,
    leftovers: tuple[tuple[tuple[str, ...], int, int, tuple], ...] | None = None,
    i_sides: dict | None = None,
) -> bool:
    """True iff all twelve leftover remaining-after-076-010 leftover 5-grams are I-only.

    Claim holds only if leftover-4 remaining plus one extra I token still
    yields exactly those twelve leftover 5-grams and every one of them
    has N_I>=1 and N_off_I=0. Hapax is not assumed. Nested leftover-2
    peels stay nested. Extra I of leftover 5-grams is recorded, not this
    claim.
    """
    remaining_grams = leftover_remaining_5grams(leftovers, i_sides)
    return (
        remaining_grams == sequences
        and len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestILeftoverN5RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760105gramsIOnlyHelpers(
    unittest.TestCase
):
    """Helpers on leftover remaining-after-076-010 leftover 5-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 5-gram counts; a gap is not a hit. Leftover-2 peels are not."""
        provider = MockProvider()
        self.assertEqual(leftover_remaining_5grams(), STANDING_SEQUENCES)
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N)
        self.assertEqual(STANDING_N_DISTINCT, 12)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(len(gram), STANDING_N5)
            self.assertFalse(is_contiguous_substring(NEAR_MISS_090_076, gram))
            self.assertFalse(is_contiguous_substring(NEAR_MISS_430_076, gram))
            self.assertFalse(is_contiguous_substring(NEAR_MISS_076_020, gram))
            self.assertFalse(is_contiguous_substring(NEAR_MISS_076_010, gram))
            self.assertFalse(is_contiguous_substring(NESTED_LEFTOVER2_PEELS[0], gram))
            self.assertFalse(is_contiguous_substring(NESTED_LEFTOVER2_PEELS[1], gram))
        remaining4 = leftover_4grams_remaining_after_leftover2_peels()
        self.assertEqual(
            tuple(gram for gram, _n, _f, _sites in remaining4),
            (GRAM4_071, GRAM4_076, GRAM4_700),
        )
        self.assertEqual(len(remaining4), STANDING_N4_REMAINING_AFTER_LEFTOVER2)
        self.assertNotIn(GRAM4_028, tuple(gram for gram, _n, _f, _sites in remaining4))
        self.assertNotIn(GRAM4_202, tuple(gram for gram, _n, _f, _sites in remaining4))
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        self.assertEqual(ngram_hit_count(adjacent, GRAM5_071_FWD_IA1), 1)
        gapped = [list(GRAM5_071_FWD_IA1[:2]) + ["000"] + list(GRAM5_071_FWD_IA1[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM5_071_FWD_IA1), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM5_071_FWD_IA1), 0)
        self.assertTrue(STANDING_DO_NOT_REPEEL_LEFTOVER2)
        self.assertTrue(STANDING_LABELED_G_DOES_NOT_COUNT)
        self.assertTrue(STANDING_PEEL_LABELED_G_IS_TAUTOLOGY)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_5gram(self):
        """Boolean is True only when all twelve leftover 5-grams are I-only."""
        provider = MockProvider()
        leftover = leftover_n4_rows()
        hold_ones = (1,) * STANDING_N
        hold_zeros = (0,) * STANDING_N
        self.assertTrue(
            i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only(
                hold_ones, hold_zeros, leftovers=leftover
            )
        )
        leak = (1,) + (0,) * (STANDING_N - 1)
        self.assertFalse(
            i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only(
                hold_ones, leak, leftovers=leftover
            )
        )
        missing = (0,) + (1,) * (STANDING_N - 1)
        self.assertFalse(
            i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only(
                missing, hold_zeros, leftovers=leftover
            )
        )
        self.assertFalse(
            i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only(
                hold_ones[:-1], hold_zeros[:-1], leftovers=leftover
            )
        )
        self.assertTrue(sequence_is_i_only(1, 0))
        self.assertFalse(sequence_is_i_only(1, 1))
        self.assertFalse(sequence_is_i_only(0, 0))
        self.assertEqual(leaking_5grams(STANDING_SEQUENCES, hold_zeros), ())
        self.assertEqual(
            leaking_5grams(STANDING_SEQUENCES, leak),
            (GRAM5_071_FWD_IA1,),
        )
        self.assertEqual(STANDING_CLAIM, (
            "i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only"
        ))
        self.assertTrue(
            STANDING_I_LEFTOVER_N5_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_N5_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_equals_i_sites_and_extra_is_empty(self):
        """Leftover matching leftover-5 remaining sites equal I sites; extra I is 0."""
        provider = MockProvider()
        self.assertTrue(
            leftover_matching_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(
            leftover_matching_5gram_sites(),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 12)
        self.assertEqual(
            leftover_matching_leftover4_of_leftover5(),
            STANDING_LEFTOVER_MATCHING_LEFTOVER4_SITES,
        )
        self.assertEqual(STANDING_LEFTOVER_MATCHING_LEFTOVER4, 6)
        self.assertEqual(
            leftover_matching_leftover3_of_leftover5(),
            STANDING_LEFTOVER_MATCHING_LEFTOVER3_SITES,
        )
        self.assertEqual(STANDING_LEFTOVER_MATCHING_LEFTOVER3, 12)
        self.assertEqual(
            leftover_matching_leftover2_of_leftover5(),
            STANDING_LEFTOVER_MATCHING_LEFTOVER2_SITES,
        )
        self.assertEqual(STANDING_LEFTOVER_MATCHING_LEFTOVER2, 18)
        for sites in STANDING_I_SITES:
            self.assertEqual(
                extra_i_sites_of_5gram(sites, STANDING_LEFTOVER_MATCHING_SITES),
                (),
            )
        self.assertEqual(STANDING_N_EXTRA, 0)
        planted_foreign = (SIDE_IA, "Ia99", 999)
        self.assertFalse(
            leftover_matching_subset(
                STANDING_LEFTOVER_MATCHING_SITES + (planted_foreign,),
                STANDING_I_SITES,
            )
        )
        self.assertEqual(
            extra_i_sites_of_5gram(
                STANDING_I_SITES[0] + (planted_foreign,),
                STANDING_LEFTOVER_MATCHING_SITES,
            ),
            (planted_foreign,),
        )
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN5RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760105gramsIOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover remaining-after-076-010 leftover 5-grams I-only. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover = leftover_n4_rows()
        self.remaining_after = leftover_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010(
            self.leftover
        )
        self.remaining_4grams = leftover_remaining_grams(self.leftover)
        self.remaining_4grams_after_leftover2 = leftover_4grams_remaining_after_leftover2_peels(
            self.leftover
        )
        self.remaining_grams = leftover_remaining_5grams(self.leftover, self.i_sides)
        self.leftover_matching = leftover_matching_5gram_sites(self.leftover)
        self.leftover_matching_leftover4 = leftover_matching_leftover4_of_leftover5(self.leftover)
        self.leftover_matching_leftover3 = leftover_matching_leftover3_of_leftover5(self.leftover)
        self.leftover_matching_leftover2 = leftover_matching_leftover2_of_leftover5(self.leftover)
        self.by_tablet = load_vendored_by_tablet()
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in STANDING_SEQUENCES)
        self.ia_hits = tuple(
            ngram_hit_count(self.i_sides[SIDE_IA], gram) for gram in STANDING_SEQUENCES
        )
        self.i_hits = self.ia_hits
        self.extra = tuple(
            extra_i_sites_of_5gram(sites, self.leftover_matching)
            for sites in self.i_sites
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in STANDING_SEQUENCES
        )
        self.off_i_counts = tuple(
            tablet_hit_counts(self.by_tablet, gram, OFF_I_TABLETS)
            for gram in STANDING_SEQUENCES
        )
        self.off_i_hits = tuple(sum(counts) for counts in self.off_i_counts)
        self.off_i_sites = tuple(named_off_i_sites(gram) for gram in STANDING_SEQUENCES)
        self.claim_holds = i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only(
            self.i_hits,
            self.off_i_hits,
            leftovers=self.leftover,
            i_sides=self.i_sides,
        )

    def test_tokens_are_leftover_5grams_remaining_after_leftover2_peels(self):
        """5-grams are leftover-4 remaining plus one extra I token after leftover-2 peels."""
        self.assertEqual(self.remaining_grams, STANDING_SEQUENCES)
        self.assertEqual(self.remaining_4grams, CYCLE340_SEQUENCES)
        self.assertEqual(len(self.remaining_after), CYCLE340_N)
        self.assertEqual(len(self.remaining_after), 5)
        self.assertEqual(
            tuple(gram for gram, _n, _f, _sites in self.remaining_4grams_after_leftover2),
            (GRAM4_071, GRAM4_076, GRAM4_700),
        )
        self.assertEqual(len(self.remaining_4grams_after_leftover2), 3)
        prior_340 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_i_only"
        ]
        self.assertEqual(prior_340["cycle"], 340)
        self.assertTrue(
            prior_340[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_all_i_only"
            ]
        )
        self.assertEqual(prior_340["N_extra"], 0)
        self.assertEqual(prior_340["leftover_matching_count"], 11)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_CYCLE340_DOES_NOT_COUNT)
        self.assertTrue(STANDING_DO_NOT_REPEEL_LEFTOVER2)
        self.assertTrue(STANDING_PEEL_LABELED_G_IS_TAUTOLOGY)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_5gram_is_i_only_hapax_extra_zero_and_claim_holds(self):
        """Each leftover 5-gram is I-only hapax. Extra I of 5-grams is 0. HOLD."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.remaining_grams, STANDING_SEQUENCES)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.ia_hits, STANDING_N_I_EACH)
        self.assertEqual(self.i_hits, STANDING_N_I_EACH)
        self.assertEqual(self.off_i_hits, STANDING_N_OFF_I_EACH)
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, (STANDING_OFF_I_BY_TABLET,) * STANDING_N)
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 12)
        self.assertTrue(leftover_matching_subset(self.leftover_matching, self.i_sites))
        self.assertEqual(self.leftover_matching_leftover4, STANDING_LEFTOVER_MATCHING_LEFTOVER4_SITES)
        self.assertEqual(len(self.leftover_matching_leftover4), STANDING_LEFTOVER_MATCHING_LEFTOVER4)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_LEFTOVER4, 6)
        self.assertEqual(self.leftover_matching_leftover3, STANDING_LEFTOVER_MATCHING_LEFTOVER3_SITES)
        self.assertEqual(len(self.leftover_matching_leftover3), STANDING_LEFTOVER_MATCHING_LEFTOVER3)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_LEFTOVER3, 12)
        self.assertEqual(self.leftover_matching_leftover2, STANDING_LEFTOVER_MATCHING_LEFTOVER2_SITES)
        self.assertEqual(len(self.leftover_matching_leftover2), STANDING_LEFTOVER_MATCHING_LEFTOVER2)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_LEFTOVER2, 18)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(sum(len(sites) for sites in self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(STANDING_HAPAX_EACH, (True,) * STANDING_N)
        self.assertEqual(STANDING_N_HAPAX, 12)
        self.assertEqual(STANDING_N_NOT_HAPAX, 0)
        self.assertTrue(STANDING_HAPAX_NOT_REQUIRED)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        for gram, sites, n_on, n_off, extra, hapax, hits in zip(
            STANDING_SEQUENCES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_EXTRA_I_SITES,
            STANDING_HAPAX_EACH,
            STANDING_HITS_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(nge4_sites(gram, self.i_sides), sites)
            self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], gram), n_on)
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertEqual(extra, ())
            self.assertTrue(hapax)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            for tablet, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                if tablet == "I":
                    self.assertEqual(count, n_on)
                else:
                    self.assertEqual(count, 0)
            for side, line, index in sites:
                stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N5]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_IA)
                self.assertNotEqual(line[:2], "Ib")
                self.assertIn((side, line, index), STANDING_LEFTOVER_MATCHING_SITES)
        for site, leftover5 in zip(
            STANDING_LEFTOVER_MATCHING_SITES,
            STANDING_LEFTOVER_MATCHING_5GRAMS,
            strict=True,
        ):
            side, line, index = site
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N5]
            self.assertEqual(tuple(stems), leftover5)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(named_off_i_sites(gram), ())
        self.assertEqual(leaking_5grams(STANDING_SEQUENCES, self.off_i_hits), ())
        self.assertEqual(STANDING_N_I_ONLY, 12)
        self.assertEqual(STANDING_N_NOT_I_ONLY, 0)
        self.assertEqual(STANDING_N_LEAKING, 0)
        self.assertEqual(STANDING_N_LEAK, 0)
        self.assertEqual(STANDING_LEAKING_5GRAMS, ())
        self.assertEqual(
            i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only(
                self.i_hits,
                self.off_i_hits,
                leftovers=self.leftover,
                i_sides=self.i_sides,
            ),
            STANDING_I_LEFTOVER_N5_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N5_REMAINING_AFTER_090_076_REMAINING_AFTER_430_076_REMAINING_AFTER_076_020_REMAINING_AFTER_076_010_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_EXTRA_I_PEELS)
        self.assertTrue(STANDING_DO_NOT_LAUNCH_NEXT_PREV_N)
        self.assertEqual(STANDING_CLAIM, (
            "i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only"
        ))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_leftover2_matches_stay_peeled(self):
        """Nested leftover-2 matches 076 006 / 076 011 stay peeled as leftover 2-grams."""
        remaining4 = leftover_remaining_grams(self.leftover)
        self.assertEqual(remaining4, CYCLE340_SEQUENCES)
        self.assertIn(GRAM4_028, remaining4)
        self.assertIn(GRAM4_202, remaining4)
        self.assertTrue(is_contiguous_substring(NESTED_LEFTOVER2_PEELS[1], GRAM4_028))
        self.assertTrue(is_contiguous_substring(NESTED_LEFTOVER2_PEELS[0], GRAM4_202))
        remaining_after_peels = leftover_4grams_remaining_after_leftover2_peels(self.leftover)
        remaining_grams4 = tuple(gram for gram, _n, _f, _sites in remaining_after_peels)
        self.assertNotIn(GRAM4_028, remaining_grams4)
        self.assertNotIn(GRAM4_202, remaining_grams4)
        for gram in self.remaining_grams:
            self.assertFalse(is_contiguous_substring(NESTED_LEFTOVER2_PEELS[0], gram))
            self.assertFalse(is_contiguous_substring(NESTED_LEFTOVER2_PEELS[1], gram))
        self.assertEqual(STANDING_LEFTOVER_MATCHING_LEFTOVER2, 18)
        self.assertTrue(STANDING_DO_NOT_REPEEL_LEFTOVER2)
        self.assertTrue(STANDING_CYCLE349_DOES_NOT_COUNT)
        self.assertFalse(CYCLE349_CLAIM)
        self.assertEqual(CYCLE349_N_I_ONLY, 9)
        self.assertEqual(CYCLE349_N_LEAK, 6)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_413_412_411_349_341_340_scoreboards_still_compute(self):
        """Nested leftover remaining-after-076-010 4grams / 3grams / 413 / 412 / 411 / 349 / 340 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        prior_413 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraIPrev3Tokens5gramsIOnlyScoreboard()
        )
        prior_413.setUp()
        prior_413.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE413_CLAIM)
        if not prior_413.claim_holds:
            self.fail("nested cycle 413 leftover remaining-after-076-010 extra-I previous-3-gram 5-grams drifted")
        prior_412 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010ExtraIPrev3Tokens4gramsIOnlyScoreboard()
        )
        prior_412.setUp()
        prior_412.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE412_CLAIM)
        if not prior_412.claim_holds:
            self.fail("nested cycle 412 leftover remaining-after-076-010 extra-I previous-3-gram 4-grams drifted")
        prior_411 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter076010Prev3TokensIOnlyScoreboard()
        )
        prior_411.setUp()
        prior_411.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE411_CLAIM)
        if not prior_411.claim_holds:
            self.fail("nested cycle 411 leftover remaining-after-076-010 previous 3-grams tokens I-only drifted")
        prior_349 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760102gramsIOnlyScoreboard()
        )
        prior_349.setUp()
        prior_349.test_survey_matches_computed_lock()
        self.assertFalse(CYCLE349_CLAIM)
        if prior_349.claim_holds:
            self.fail("nested cycle 349 leftover remaining-after-076-010 leftover 2-grams drifted")
        prior_341 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760103gramsIOnlyScoreboard()
        )
        prior_341.setUp()
        prior_341.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE341_CLAIM)
        self.assertEqual(CYCLE341_N_I_ONLY, 10)
        self.assertEqual(CYCLE341_N_LEAK, 0)
        self.assertEqual(CYCLE341_N_EXTRA, 5)
        if not prior_341.claim_holds:
            self.fail("nested cycle 341 leftover remaining-after-076-010 leftover 3-grams drifted")
        prior_340 = (
            TestMamariILeftoverN4RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760104gramsIOnlyScoreboard()
        )
        prior_340.setUp()
        prior_340.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE340_CLAIM)
        self.assertEqual(CYCLE340_N_I_ONLY, 5)
        self.assertEqual(CYCLE340_N_EXTRA, 0)
        self.assertEqual(CYCLE340_LEFTOVER_MATCHING_COUNT, 11)
        self.assertTrue(
            i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_all_i_only(
                (3, 2, 2, 2, 2), (0, 0, 0, 0, 0)
            )
        )
        if not prior_340.claim_holds:
            self.fail("nested cycle 340 leftover remaining-after-076-010 leftover 4-grams drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_CYCLE413_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE412_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE411_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE349_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE341_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE340_DOES_NOT_COUNT)
        self.assertEqual(leftover_remaining_3grams(), leftover_remaining_3grams(leftover))
        self.assertEqual(leftover_remaining_2grams(), leftover_remaining_2grams(leftover))
        self.assertEqual(len(leftover_matching_3gram_sites_each()), 10)
        self.assertEqual(len(leftover_matching_2gram_sites_each()), 15)
        self.assertEqual(leftover_matching_4gram_sites(), CYCLE340_LEFTOVER_MATCHING)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-414 leftover 5-gram I-only hold."""
        lock = self.survey[STANDING_RESULT]
        self.assertEqual(lock["cycle"], 414)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N"], STANDING_N)
        self.assertEqual(lock["N"], 12)
        self.assertEqual(lock["N_sequences"], STANDING_N)
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_4grams_leftover"], CYCLE340_N)
        self.assertEqual(lock["N_4grams_remaining_after_leftover2"], STANDING_N4_REMAINING_AFTER_LEFTOVER2)
        measured_sequences = [list(gram) for gram in STANDING_SEQUENCES]
        self.assertEqual(lock["tokens5"], measured_sequences)
        self.assertEqual(
            tuple(tuple(site_row) for site_row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(lock["leftover_matching_count"], 12)
        self.assertEqual(lock["leftover_matching_leftover5_remaining_sites"], lock["leftover_matching_sites"])
        self.assertTrue(lock["leftover_matching_equals_i_sites"])
        self.assertEqual(lock["leftover_matching_leftover4"], STANDING_LEFTOVER_MATCHING_LEFTOVER4)
        self.assertEqual(lock["leftover_matching_leftover4"], 6)
        self.assertEqual(lock["leftover_matching_leftover3"], STANDING_LEFTOVER_MATCHING_LEFTOVER3)
        self.assertEqual(lock["leftover_matching_leftover3"], 12)
        self.assertEqual(lock["leftover_matching_leftover2"], STANDING_LEFTOVER_MATCHING_LEFTOVER2)
        self.assertEqual(lock["leftover_matching_leftover2"], 18)
        self.assertEqual(
            tuple(tuple(site_row) for site_row in lock["leftover_matching_leftover4_sites"]),
            STANDING_LEFTOVER_MATCHING_LEFTOVER4_SITES,
        )
        self.assertEqual(
            tuple(tuple(site_row) for site_row in lock["leftover_matching_leftover3_sites"]),
            STANDING_LEFTOVER_MATCHING_LEFTOVER3_SITES,
        )
        self.assertEqual(
            tuple(tuple(site_row) for site_row in lock["leftover_matching_leftover2_sites"]),
            STANDING_LEFTOVER_MATCHING_LEFTOVER2_SITES,
        )
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 0)
        self.assertEqual(lock["N_extra_of_5grams"], 0)
        self.assertTrue(lock["not_assumed_hapax"])
        self.assertTrue(lock["hapax_not_required"])
        self.assertEqual(lock["N_not_hapax"], STANDING_N_NOT_HAPAX)
        self.assertEqual(lock["N_not_hapax"], 0)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 12)
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N)
        for row, gram, sites, n_on, n_off, extra, hapax, hits, parent4, role in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_EXTRA_I_SITES,
            STANDING_HAPAX_EACH,
            STANDING_HITS_BY_TABLET,
            STANDING_PARENT_4GRAMS,
            STANDING_ROLES,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens5"]), gram)
            self.assertEqual(tuple(row["parent_4gram"]), parent4)
            self.assertEqual(row["role"], role)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["leftover_matching_sites"]),
                sites,
            )
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_I"], 1)
            self.assertEqual(row["ia_hits"], n_on)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["ib_sites"]), STANDING_IB_SITES)
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["N_leak"], 0)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["off_i_sites"]), ())
            self.assertEqual(tuple(tuple(site_row) for site_row in row["extra_i_sites"]), extra)
            self.assertEqual(row["N_extra"], 0)
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["off_i_tablets_with_hits"]), ())
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(tuple(row["hits_by_tablet"]), hits)
            self.assertTrue(row["i_only"])
            self.assertEqual(row["hapax"], hapax)
            self.assertTrue(row["hapax"])
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(tuple(lock["hapax_each"]), STANDING_HAPAX_EACH)
        self.assertEqual(lock["leaking_5grams"], [])
        self.assertEqual(lock["N_leaking"], 0)
        self.assertEqual(lock["N_leak"], 0)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock[
                "i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_all_i_only"
            ]
        )
        self.assertTrue(
            lock[
                "i_leftover_n5_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_5grams_i_only"
            ]
        )
        self.assertEqual(lock["N_i_only"], STANDING_N_I_ONLY)
        self.assertEqual(lock["N_i_only"], 12)
        self.assertEqual(lock["N_not_i_only"], STANDING_N_NOT_I_ONLY)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertTrue(lock["nested_cycle413_extra_i_prev3_tokens_5grams_all_i_only"])
        self.assertTrue(lock["nested_cycle412_extra_i_prev3_tokens_4grams_all_i_only"])
        self.assertTrue(lock["nested_cycle411_previous_3grams_tokens_all_i_only"])
        self.assertFalse(lock["nested_cycle349_2grams_all_i_only"])
        self.assertEqual(lock["nested_cycle349_N_i_only"], 9)
        self.assertEqual(lock["nested_cycle349_N_leak"], 6)
        self.assertEqual(lock["nested_cycle349_N_extra"], 116)
        self.assertTrue(lock["nested_cycle341_3grams_all_i_only"])
        self.assertEqual(lock["nested_cycle341_N_extra"], 5)
        self.assertTrue(lock["nested_cycle340_4grams_all_i_only"])
        self.assertEqual(lock["nested_cycle340_N_extra"], 0)
        self.assertEqual(lock["nested_cycle340_N_i_only"], 5)
        self.assertEqual(lock["nested_cycle340_leftover_matching_count"], 11)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_cycle340"])
        self.assertFalse(lock["same_as_cycle341"])
        self.assertFalse(lock["same_as_cycle349"])
        self.assertFalse(lock["same_as_cycle411"])
        self.assertFalse(lock["same_as_cycle412"])
        self.assertFalse(lock["same_as_cycle413"])
        self.assertTrue(lock["same_claim_shape_as_cycle340"])
        self.assertTrue(lock["labeled_G_does_not_count"])
        self.assertTrue(lock["peel_labeled_G_is_tautology"])
        self.assertTrue(lock["do_not_peel_labeled_g_exactly_1_share"])
        self.assertTrue(lock["do_not_repeel_leftover2"])
        self.assertTrue(lock["do_not_launch_extra_i_peels"])
        self.assertTrue(lock["do_not_launch_next_prev_n_of_leftover_5grams"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_n5_set_not_retuned"])
        self.assertTrue(lock["do_not_relock_cycle413"])
        self.assertTrue(lock["do_not_relock_cycle412"])
        self.assertTrue(lock["do_not_relock_cycle411"])
        self.assertTrue(lock["do_not_relock_cycle349"])
        self.assertTrue(lock["do_not_relock_cycle341"])
        self.assertTrue(lock["do_not_relock_cycle340"])
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_prev3_tokens_5grams_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_prev3_tokens_4grams_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_prev3_tokens_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_2grams_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_3grams_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_i_only_unchanged"
            ]
        )
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        prior_413 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_prev3_tokens_5grams_i_only"
        ]
        self.assertEqual(prior_413["cycle"], 413)
        self.assertTrue(
            prior_413[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_prev3_tokens_5grams_all_i_only"
            ]
        )
        prior_412 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_extra_i_prev3_tokens_4grams_i_only"
        ]
        self.assertEqual(prior_412["cycle"], 412)
        prior_411 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_prev3_tokens_i_only"
        ]
        self.assertEqual(prior_411["cycle"], 411)
        prior_349 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_2grams_i_only"
        ]
        self.assertEqual(prior_349["cycle"], 349)
        self.assertFalse(
            prior_349[
                "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_2grams_all_i_only"
            ]
        )
        prior_341 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_3grams_i_only"
        ]
        self.assertEqual(prior_341["cycle"], 341)
        prior_340 = self.survey[
            "i_leftover_n4_remaining_after_090_076_remaining_after_430_076_remaining_after_076_020_remaining_after_076_010_4grams_i_only"
        ]
        self.assertEqual(prior_340["cycle"], 340)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN5RemainingAfter090076RemainingAfter430076RemainingAfter076020RemainingAfter0760105gramsIOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 414 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
