"""I's cycle-303 leftover n=4 remaining previous-021 3-gram
021 090 076 off-I lock.

Cycle 304 text-search lock. Uses already-vendored A–V and the
cycle-303 leftover n=4 remaining I 090 076 exactly 5 share
previous 021 cluster (K_021=5 of N_inside=13;
N_remaining_after_021=8; leftover extra=56; N_I=69). Does
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
(cycle 262) or leftover extra remaining-after-999 3-gram
600 090 076 (cycle 268). Does not lock leftover n=4 remaining
previous-021 4-grams I-only this cycle (that is the next
lock if this HOLD). Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished
Ib is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Same claim-shape as cycle 268 (600 090 076 was I-only 6/0
extra I=2 after leftover extra remaining-after-999 previous-
600) and cycle 290 (090 076 020 was I-only 4/0 extra I=0
after leftover n=4 remaining exactly 4 share next 020).
Sharing previous 021 does not imply 3-gram 021 090 076 is
I-only (it can leak off I, or extra I can exist outside
leftover n=4 remaining previous-021). Extra I of this
3-gram is leftover-of-leftover, same shape as cycle 268
extra I of 600 090 076. Extra I ≠ 0 does not make the claim
lose (still I-only); still lock extra I. Cycle 207 lost:
090 076 070 is not I-only (8/1 on T). Cycle 223 lost:
090 076 is not I-only (69/3 on T). This cycle is the new
leftover n=4 remaining previous-021 3-gram 021 090 076 only.
090 076 without 021, 600 090 076, 999 090 076, 090 076 020,
and leftover n=4 remaining 021 090 076 087 do not count as
this 3-gram. Do not retune leftover n=4, leftover extra
peels, 076-cells, or any detector. Do not overwrite cycle
167/268–303. Off-I T sites of 090 076 are not this cycle
except as off-I of 021 090 076 if they match. Do not assume
the I-only result.

Locks exact consecutive hits of 021 090 076 on tablet I and
on every other vendored tablet A–H and J–V. Claim that can
lose: i_3gram_021_090_076_i_only (I hits ≥ 1 and off-I hits
== 0). True only if N_off_I == 0. Also lose if leftover n=4
remaining previous-021 no longer computes as 5, or if K_021
is no longer unique-max. Measured: Ia is exactly 5 at
Ia4[116]/Ia5[27]/Ia6[77]/Ia8[105]/Ia13[16]; Ib unpublished
0; every other vendored tablet is exact-0. Leftover n=4
remaining previous-021 5 sites (090-starts Ia4[117]/Ia5[28]/
Ia6[78]/Ia8[106]/Ia13[17]) ⊆ those I 3-gram sites
(021-starts one token earlier). Extra I = 0 (no I 021 090
076 outside leftover n=4 remaining previous-021). Extra I
of 021 090 076 overlap leftover extra I 090 076 is empty.
Nested leftover extra previous-999 overlap empty; leftover
extra remaining-after-000 extra I overlap Ia8[106] only;
remaining-after-011 overlap Ia8[106] and Ia13[17]; record,
do not fail I-only on it. The claim is true. Not an n≥8
island. Not the cycle-103 I 5-gram. Nested leftover n=4
remaining 13 / 4 / 9 / 3 / 6 / 2 / 4 / 2 / 2, cycle 302
unique-max true G=021 K=5 N_distinct=8 N=13
N_line_initial=0, cycle 303 K_021=5, cycle 288 unique-max
true G=020 K=4 share-one lost, cycle 301 090 076 607 073
1/0, cycle 224 13/56, and cycle 223 69/3 stay.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_g_nge8_scoreboard import (
    nge8_sites,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    TA_LINE_NAMES,
    load_t_sides,
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
    STANDING_I_SITES as CYCLE223_I_SITES,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_020_i_only_scoreboard import (
    GRAM3 as CYCLE290_GRAM3,
    STANDING_I_3GRAM_090_076_020_I_ONLY as CYCLE290_CLAIM,
    STANDING_N_EXTRA as CYCLE290_N_EXTRA,
    STANDING_N_I as CYCLE290_N_I,
    STANDING_N_OFF_I as CYCLE290_N_OFF_I,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_600_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE268_GRAM3,
    STANDING_I_3GRAM_600_090_076_I_ONLY as CYCLE268_CLAIM,
    STANDING_N_EXTRA as CYCLE268_N_EXTRA,
    STANDING_N_I as CYCLE268_N_I,
    STANDING_N_OFF_I as CYCLE268_N_OFF_I,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
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
    leftover_n4_remaining_previous_stems,
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
from tests.test_mamari_keiti_n9_scoreboard import (
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_s_nge6_scoreboard import (
    nge6_sites,
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
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
    load_g_k_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    SIDE_SA,
    SIDE_SB,
    load_s_sides,
)

HYPOTHESIS_I_ONLY = True
GRAM3 = GRAM3_BACKWARD
NEAR_MISS_600_090_076 = CYCLE268_GRAM3
NEAR_MISS_999_090_076 = CYCLE167_GRAM3
NEAR_MISS_090_076_020 = CYCLE290_GRAM3
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_090_076 = GRAM2
NEAR_MISS_N4_021_090_076_087 = ("021", "090", "076", "087")
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_I_HITS = 5
STANDING_IA_HITS = 5
STANDING_IB_HITS = 0
STANDING_N_ON_I = 5
STANDING_N_I = 5
STANDING_I_SITES = (
    (SIDE_IA, "Ia4", 116),
    (SIDE_IA, "Ia5", 27),
    (SIDE_IA, "Ia6", 77),
    (SIDE_IA, "Ia8", 105),
    (SIDE_IA, "Ia13", 16),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_MATCHING_SITES = CYCLE303_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_COUNT = 5
STANDING_LEFTOVER_MATCHING_PREVIOUS_4GRAMS = CYCLE303_MATCHING_PREVIOUS_4GRAMS
STANDING_LEFTOVER_3GRAM_SITES = (
    (SIDE_IA, "Ia4", 116),
    (SIDE_IA, "Ia5", 27),
    (SIDE_IA, "Ia6", 77),
    (SIDE_IA, "Ia8", 105),
    (SIDE_IA, "Ia13", 16),
)
STANDING_N_LEFTOVER = 5
STANDING_EXTRA_I_SITES = ()
STANDING_N_EXTRA = 0
STANDING_EXTRA_I_090_076_SITES = ()
STANDING_I_PREVIOUS_4GRAMS = (
    ("600", "021", "090", "076"),
    ("007", "021", "090", "076"),
    ("150", "021", "090", "076"),
    ("999", "021", "090", "076"),
    ("999", "021", "090", "076"),
)
STANDING_I_NEXT_4GRAMS = (
    ("021", "090", "076", "087"),
    ("021", "090", "076", "087"),
    ("021", "090", "076", "087"),
    ("021", "090", "076", "607"),
    ("021", "090", "076", "021"),
)
STANDING_I_SITE_ROWS = (
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia4",
        "index": 116,
        "previous_4gram": ("600", "021", "090", "076"),
        "leftover_n4_remaining_090_076_site": (SIDE_IA, "Ia4", 117),
        "in_cycle303_leftover_n4_remaining_5": True,
        "inside_leftover_extra": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia5",
        "index": 27,
        "previous_4gram": ("007", "021", "090", "076"),
        "leftover_n4_remaining_090_076_site": (SIDE_IA, "Ia5", 28),
        "in_cycle303_leftover_n4_remaining_5": True,
        "inside_leftover_extra": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia6",
        "index": 77,
        "previous_4gram": ("150", "021", "090", "076"),
        "leftover_n4_remaining_090_076_site": (SIDE_IA, "Ia6", 78),
        "in_cycle303_leftover_n4_remaining_5": True,
        "inside_leftover_extra": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia8",
        "index": 105,
        "previous_4gram": ("999", "021", "090", "076"),
        "leftover_n4_remaining_090_076_site": (SIDE_IA, "Ia8", 106),
        "in_cycle303_leftover_n4_remaining_5": True,
        "inside_leftover_extra": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia13",
        "index": 16,
        "previous_4gram": ("999", "021", "090", "076"),
        "leftover_n4_remaining_090_076_site": (SIDE_IA, "Ia13", 17),
        "in_cycle303_leftover_n4_remaining_5": True,
        "inside_leftover_extra": False,
    },
)
STANDING_OFF_I_HITS = 0
STANDING_N_OFF_I = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_OFF_I_BY_TABLET_NONZERO = {}
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_EXTRA_I_OVERLAP_LEFTOVER_EXTRA_090_076 = ()
STANDING_EXTRA_I_OVERLAP_LEFTOVER_EXTRA_090_076_COUNT = 0
STANDING_OVERLAP_DOES_NOT_LOSE = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_3gram_021_090_076_i_only"
STANDING_I_3GRAM_021_090_076_I_ONLY = True
STANDING_RESULT = "i_3gram_021_090_076_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE207_3GRAM = False
STANDING_SAME_AS_CYCLE262_3GRAM = False
STANDING_SAME_AS_CYCLE268_3GRAM = False
STANDING_SAME_AS_CYCLE290_3GRAM = False
STANDING_SAME_AS_CYCLE303 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE268 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE290 = True
STANDING_090_076_WITHOUT_021_DOES_NOT_COUNT = True
STANDING_600_090_076_DOES_NOT_COUNT = True
STANDING_999_090_076_DOES_NOT_COUNT = True
STANDING_090_076_020_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_021_090_076_087_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_4GRAMS_NOT_LOCKED = True
STANDING_DO_NOT_RELOCK_CYCLE262 = True
STANDING_DO_NOT_RELOCK_CYCLE268 = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE303_K_021 = 5
STANDING_CYCLE303_G = "021"
STANDING_CYCLE302_N_DISTINCT = 8
STANDING_NESTED_LEFTOVER_N4_REMAINING = (13, 4, 9, 3, 6, 2, 4, 2, 2)


def leftover_n4_remaining_090_076_site_for_3gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """090 076 starts one token after 021 090 076."""
    side, line, index = site
    return (side, line, index + 1)


def leftover_n4_remaining_previous_021_3gram_sites(
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining previous-021 090-starts shifted to 021-starts."""
    return tuple((side, line, index - 1) for side, line, index in leftover_matching)


def leftover_n4_remaining_previous_021_subset(
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff leftover n=4 remaining previous-021 5 sites ⊆ I 021 090 076."""
    return set(
        leftover_n4_remaining_previous_021_3gram_sites(leftover_matching)
    ).issubset(set(i_sites))


def leftover_3gram_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 021 090 076 sites whose 090 076 is leftover n=4 remaining previous-021."""
    leftover_set = set(leftover_matching)
    return tuple(
        site
        for site in i_sites
        if leftover_n4_remaining_090_076_site_for_3gram(site) in leftover_set
    )


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 021 090 076 sites that are not leftover n=4 remaining previous-021."""
    leftover_set = set(leftover_matching)
    return tuple(
        site
        for site in i_sites
        if leftover_n4_remaining_090_076_site_for_3gram(site) not in leftover_set
    )


def extra_i_090_076_sites(
    extra: tuple[tuple[str, str, int], ...] = STANDING_EXTRA_I_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """090-starts of extra I 021 090 076."""
    return tuple(leftover_n4_remaining_090_076_site_for_3gram(site) for site in extra)


def extra_i_overlap_leftover_extra_090_076(
    extra_090: tuple[tuple[str, str, int], ...] = STANDING_EXTRA_I_090_076_SITES,
    leftover_extra: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """Extra I 090-starts of 021 090 076 that sit in leftover extra I 090 076."""
    leftover_set = set(leftover_extra)
    return tuple(site for site in extra_090 if site in leftover_set)


def site_previous_4gram_for_3gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """W 021 090 076 if a previous stem exists; None at start-of-line."""
    if tuple(stems[index : index + len(gram3)]) != gram3:
        return None
    if index < 1:
        return None
    return tuple(stems[index - 1 : index + len(gram3)])


def i_3gram_021_090_076_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0. Extra I does not lose."""
    return i_hits >= 1 and off_i_hits == 0


def named_off_i_sites(
    gram: tuple[str, ...] = GRAM3,
) -> tuple[tuple[str, str, int], ...]:
    """Named (side, line, index) hits on G, S, and T. Search only."""
    gk = load_g_k_sides()
    g_sites = nge8_sites(gram, gk)
    s_sites = nge6_sites(gram, load_s_sides())
    t = load_t_sides()
    t_sites = tuple(
        site_tuple(hit)
        for hit in named_side_hits(t[SIDE_TA], TA_LINE_NAMES, SIDE_TA, gram)
    )
    return g_sites + s_sites + t_sites


def i_site_row_as_survey(row: dict) -> dict:
    """JSON-ready site row (lists, not tuples)."""
    return {
        "tablet": row["tablet"],
        "side": row["side"],
        "line": row["line"],
        "index": row["index"],
        "previous_4gram": list(row["previous_4gram"]),
        "leftover_n4_remaining_090_076_site": list(row["leftover_n4_remaining_090_076_site"]),
        "in_cycle303_leftover_n4_remaining_5": row["in_cycle303_leftover_n4_remaining_5"],
        "inside_leftover_extra": row["inside_leftover_extra"],
    }


class TestI3gram021090076IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-303 leftover n=4 remaining previous-021 3-gram."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. 090 076 / 600 090 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("021", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["021", "090", "076", "021", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 2)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_600_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_020)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["600", "090", "076"]], GRAM3), 0)
        self.assertTrue(STANDING_090_076_WITHOUT_021_DOES_NOT_COUNT)
        self.assertTrue(STANDING_600_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_020_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_021_090_076_087_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Extra I does not lose."""
        provider = MockProvider()
        self.assertTrue(i_3gram_021_090_076_i_only(1, 0))
        self.assertTrue(i_3gram_021_090_076_i_only(5, 0))
        self.assertFalse(i_3gram_021_090_076_i_only(5, 1))
        self.assertFalse(i_3gram_021_090_076_i_only(1, 1))
        self.assertFalse(i_3gram_021_090_076_i_only(0, 0))
        self.assertFalse(i_3gram_021_090_076_i_only(0, 1))
        self.assertEqual(STANDING_CLAIM, "i_3gram_021_090_076_i_only")
        self.assertTrue(STANDING_I_3GRAM_021_090_076_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(
            STANDING_I_3GRAM_021_090_076_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertTrue(STANDING_I_3GRAM_021_090_076_I_ONLY)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_fail(self):
        """Leftover n=4 remaining previous-021 ⊆ I sites; extra can be nonempty."""
        provider = MockProvider()
        self.assertTrue(
            leftover_n4_remaining_previous_021_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(
            leftover_n4_remaining_previous_021_3gram_sites(),
            STANDING_LEFTOVER_3GRAM_SITES,
        )
        self.assertEqual(leftover_3gram_sites(), STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(extra_i_sites(), STANDING_EXTRA_I_SITES)
        self.assertEqual(len(extra_i_sites()), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(STANDING_N_LEFTOVER + STANDING_N_EXTRA, STANDING_N_I)
        self.assertEqual(extra_i_090_076_sites(), STANDING_EXTRA_I_090_076_SITES)
        self.assertEqual(
            extra_i_overlap_leftover_extra_090_076(),
            STANDING_EXTRA_I_OVERLAP_LEFTOVER_EXTRA_090_076,
        )
        planted_extra = STANDING_I_SITES + ((SIDE_IA, "Ia1", 0),)
        self.assertFalse(
            leftover_n4_remaining_previous_021_subset(
                STANDING_LEFTOVER_MATCHING_SITES + ((SIDE_IA, "Ia1", 1),),
                STANDING_I_SITES,
            )
        )
        self.assertEqual(len(extra_i_sites(planted_extra)), 1)
        dropped = STANDING_I_SITES[1:]
        self.assertFalse(
            leftover_n4_remaining_previous_021_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                dropped,
            )
        )
        planted_extra_090 = ((SIDE_IA, "Ia1", 2),)
        self.assertEqual(
            extra_i_overlap_leftover_extra_090_076(
                planted_extra_090,
                STANDING_LEFTOVER_SITES,
            ),
            planted_extra_090,
        )
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_cycle303_leftover_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-303 leftover n=4 remaining previous G, not priors."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("021", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3[1:], GRAM2)
        self.assertEqual(GRAM3[0], CYCLE303_G)
        self.assertNotEqual(GRAM3, CYCLE268_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE290_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, GRAM2)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertTrue(is_contiguous_substring(GRAM3, NEAR_MISS_N4_021_090_076_087))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE262_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE268_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE290_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE303)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE268)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE290)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        self.assertLess(len(GRAM3), 8)
        for prev4 in STANDING_I_PREVIOUS_4GRAMS:
            self.assertTrue(is_contiguous_substring(GRAM3, prev4))
        for nxt4 in STANDING_I_NEXT_4GRAMS:
            self.assertTrue(is_contiguous_substring(GRAM3, nxt4))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_600_090_076))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_020))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_070))
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM3))
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_4GRAMS_NOT_LOCKED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE262)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE268)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram021090076IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 remaining previous-021 3-gram off-I lock."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM3, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM3)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM3, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM3, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.off_i_sites = named_off_i_sites(GRAM3)
        self.previous_stems = leftover_n4_remaining_previous_stems(
            self.i_sides,
            CYCLE224_INSIDE_SITES,
            GRAM2,
        )
        self.leftover_matching = leftover_n4_remaining_with_previous_021(
            CYCLE224_INSIDE_SITES,
            self.previous_stems,
        )
        self.leftover = leftover_3gram_sites(self.i_sites, self.leftover_matching)
        self.extra = extra_i_sites(self.i_sites, self.leftover_matching)
        self.extra_090 = extra_i_090_076_sites(self.extra)
        self.extra_overlap_leftover_extra = extra_i_overlap_leftover_extra_090_076(
            self.extra_090,
            STANDING_LEFTOVER_SITES,
        )
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
        self.claim_holds = i_3gram_021_090_076_i_only(
            self.i_hits,
            self.off_i_hits,
        )
        self.previous_4grams = tuple(
            site_previous_4gram_for_3gram(
                line_stems_for_site(self.i_sides, site),
                site[2],
                GRAM3,
            )
            for site in self.i_sites
        )
        self.leftover_n4_remaining_090_076_sites = tuple(
            leftover_n4_remaining_090_076_site_for_3gram(site) for site in self.leftover
        )

    def test_tokens_are_cycle_303_leftover_not_retuned(self):
        """3-gram is the cycle-303 leftover n=4 remaining previous G, not a new inventory."""
        self.assertEqual(GRAM3, ("021", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3[1:], GRAM2)
        self.assertEqual(GRAM3[0], "021")
        prior_303 = self.survey["i_leftover_n4_remaining_090_076_previous_021"]
        self.assertEqual(prior_303["cycle"], 303)
        self.assertEqual(tuple(prior_303["backward_3gram"]), GRAM3)
        self.assertEqual(prior_303["G"], "021")
        self.assertEqual(prior_303["K"], 5)
        self.assertEqual(prior_303["K_021"], 5)
        self.assertEqual(prior_303["N_remaining_after_021"], 8)
        self.assertEqual(prior_303["N_inside"], 13)
        self.assertEqual(prior_303["N_leftover_extra"], 56)
        self.assertEqual(prior_303["N_I"], 69)
        self.assertEqual(CYCLE303_G, "021")
        self.assertEqual(CYCLE303_K_021, 5)
        self.assertEqual(CYCLE303_N_REMAINING_AFTER_021, 8)
        self.assertTrue(CYCLE303_CLAIM)
        self.assertTrue(
            prior_303["i_leftover_n4_remaining_090_076_exactly_5_share_previous_021"]
        )
        measured_matching = [list(site) for site in CYCLE303_MATCHING_SITES]
        self.assertEqual(
            [list(site) for site in prior_303["matching_leftover_n4_remaining_sites"]],
            measured_matching,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE303_MATCHING_PREVIOUS_4GRAMS],
            prior_303["matching_previous_4grams"],
        )
        self.assertEqual(self.leftover_matching, CYCLE303_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE303_K_021)
        self.assertEqual(STANDING_CYCLE303_K_021, 5)
        self.assertEqual(STANDING_CYCLE303_G, "021")
        if (
            len(self.leftover_matching) != 5
            or CYCLE303_G != "021"
            or CYCLE303_K_021 != 5
            or CYCLE303_N_REMAINING_AFTER_021 != 8
        ):
            self.fail(
                "leftover n=4 remaining previous-021 no longer computes as 5"
            )
        prior_302 = self.survey["i_leftover_n4_remaining_090_076_previous_stem"]
        self.assertEqual(prior_302["cycle"], 302)
        self.assertEqual(prior_302["G"], "021")
        self.assertEqual(prior_302["K"], 5)
        self.assertEqual(prior_302["N_inside"], 13)
        self.assertEqual(prior_302["N_line_initial"], 0)
        self.assertEqual(prior_302["N_distinct_previous_stems"], 8)
        self.assertTrue(prior_302["G_uniquely_most_frequent"])
        self.assertTrue(prior_302["i_leftover_n4_remaining_090_076_unique_previous_stem"])
        if (
            prior_302["G"] != "021"
            or prior_302["K"] != 5
            or prior_302["N_inside"] != 13
            or prior_302["N_line_initial"] != 0
            or prior_302["N_distinct_previous_stems"] != 8
            or not prior_302["G_uniquely_most_frequent"]
        ):
            self.fail(
                "K_021 is no longer unique-max G=021 K=5 N=13 distinct=8"
            )
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["N_distinct_next_stems"], 6)
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
        self.assertEqual(CYCLE301_SEQUENCES[0], ("090", "076", "607", "073"))
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
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_4GRAMS_NOT_LOCKED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE262)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE268)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_five_on_ia_and_leftover_n4_remaining_021_is_subset(self):
        """3-gram is 5 on Ia; Ib 0. Leftover n=4 remaining previous-021 is those 5."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 5)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 5)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 5)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM3, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM3), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE303_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE302_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 5)
        self.assertTrue(
            leftover_n4_remaining_previous_021_subset(
                self.leftover_matching,
                self.i_sites,
            )
        )
        self.assertEqual(self.leftover, STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(self.leftover, STANDING_I_SITES)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.leftover), STANDING_N_LEFTOVER)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER, 5)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(STANDING_N_LEFTOVER + STANDING_N_EXTRA, STANDING_N_I)
        self.assertEqual(self.leftover_n4_remaining_090_076_sites, CYCLE303_MATCHING_SITES)
        self.assertEqual(self.extra_090, STANDING_EXTRA_I_090_076_SITES)
        self.assertEqual(
            self.extra_overlap_leftover_extra,
            STANDING_EXTRA_I_OVERLAP_LEFTOVER_EXTRA_090_076,
        )
        self.assertEqual(self.extra_overlap_leftover_extra, ())
        self.assertEqual(STANDING_EXTRA_I_OVERLAP_LEFTOVER_EXTRA_090_076_COUNT, 0)
        if self.i_hits != 5:
            self.fail("measured N_I drifted from 5")
        if self.leftover_matching != CYCLE303_MATCHING_SITES:
            self.fail("leftover n=4 remaining previous-021 set drifted")
        if len(self.leftover_matching) != 5:
            self.fail("leftover n=4 remaining previous-021 no longer computes as 5")
        if not leftover_n4_remaining_previous_021_subset(
            self.leftover_matching,
            self.i_sites,
        ):
            self.fail(
                "leftover n=4 remaining previous-021 5 sites "
                "not subset of I 021 090 076"
            )
        if self.extra != STANDING_EXTRA_I_SITES:
            self.fail("extra I 021 090 076 leftover-of-leftover sites drifted")
        leftover_set = set(STANDING_LEFTOVER_3GRAM_SITES)
        for (side, line, index), prev4, nxt4, row in zip(
            STANDING_I_SITES,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            STANDING_I_SITE_ROWS,
            strict=True,
        ):
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N3]), prev4)
            self.assertEqual(tuple(stems[index : index + STANDING_N4]), nxt4)
            self.assertEqual(
                site_previous_4gram_for_3gram(stems, index, GRAM3),
                prev4,
            )
            self.assertEqual(side, SIDE_IA)
            site = (side, line, index)
            gram2_site = leftover_n4_remaining_090_076_site_for_3gram(site)
            self.assertEqual((row["side"], row["line"], row["index"]), site)
            self.assertEqual(row["previous_4gram"], prev4)
            self.assertEqual(tuple(row["leftover_n4_remaining_090_076_site"]), gram2_site)
            self.assertIn(site, leftover_set)
            self.assertIn(gram2_site, CYCLE224_INSIDE_SITES)
            self.assertIn(gram2_site, CYCLE303_MATCHING_SITES)
            self.assertNotIn(gram2_site, STANDING_LEFTOVER_SITES)
            self.assertTrue(row["in_cycle303_leftover_n4_remaining_5"])
            self.assertFalse(row["inside_leftover_extra"])
            self.assertNotIn(site, CYCLE207_I_SITES)
        self.assertEqual(self.previous_4grams, STANDING_I_PREVIOUS_4GRAMS)
        self.assertEqual(self.previous_4grams, CYCLE303_MATCHING_PREVIOUS_4GRAMS)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        self.assertEqual(self.overlap_261, CYCLE303_OVERLAP_261)
        self.assertEqual(self.overlap_261, ())
        self.assertEqual(self.overlap_258, CYCLE303_OVERLAP_258)
        self.assertEqual(self.overlap_259, CYCLE303_OVERLAP_259)
        self.assertEqual(self.overlap_258, ((SIDE_IA, "Ia8", 106),))
        self.assertEqual(self.overlap_after_011, CYCLE303_OVERLAP_AFTER_011)
        self.assertEqual(
            self.overlap_after_011,
            ((SIDE_IA, "Ia8", 106), (SIDE_IA, "Ia13", 17)),
        )
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_4GRAMS_NOT_LOCKED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_zero_off_i_and_i_only(self):
        """3-gram is 0 on A–H and J–V. Ia has exactly 5. T 090 076 is not this 3-gram."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, STANDING_N_OFF_I)
        self.assertEqual(STANDING_N_OFF_I, 0)
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(STANDING_OFF_I_SITES, ())
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ())
        self.assertEqual(STANDING_OFF_I_BY_TABLET_NONZERO, {})
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM3))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 5)
            else:
                self.assertEqual(count, 0)
        gk = load_g_k_sides()
        self.assertEqual(ngram_hit_count(gk[SIDE_GR], GRAM3), 0)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], GRAM3), 0)
        s_sides = load_s_sides()
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], GRAM3), 0)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], GRAM3), 0)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM3), 0)
        self.assertEqual(named_off_i_sites(GRAM3), ())
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
            if index >= 1:
                self.assertNotEqual(tuple(stems[index - 1 : index + 2]), GRAM3)
            self.assertNotIn(site, STANDING_I_SITES)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        ta9 = t_sides[SIDE_TA][TA_LINE_NAMES.index("Ta9")]
        self.assertEqual(tuple(ta9[2:5]), CYCLE207_GRAM3)
        self.assertNotEqual(tuple(ta9[2:5]), GRAM3)
        if len(ta9) >= 5:
            self.assertNotEqual(tuple(ta9[1:4]), GRAM3)
        self.assertEqual(
            i_3gram_021_090_076_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_3GRAM_021_090_076_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_021_090_076_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_3GRAM_021_090_076_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_3gram_021_090_076_i_only")
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertTrue(self.claim_holds)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE262_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE268_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE290_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE303)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE268)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE290)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        if self.off_i_hits != 0:
            self.fail("measured N_off_I drifted from 0")
        if self.i_hits != STANDING_N_I:
            self.fail("measured N_I drifted from the locked count")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_303_302_301_288_224_223_still_compute(self):
        """Cycle 303 K_021=5, 302 unique-max G=021 K=5, 301 1/0, 288 G=020 K=4, 224 13/56, 223 69/3 stay."""
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
        self.assertTrue(prior_303.unique)
        if (
            prior_303.k_021 != 5
            or CYCLE303_G != "021"
            or prior_303.n_remaining_after_021 != 8
            or not prior_303.unique
            or prior_303.g != "021"
        ):
            self.fail(
                "nested cycle 303 leftover n=4 remaining previous-021 "
                "K_021=5 unique-max drifted"
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
        unused_223 = CYCLE223_I_SITES
        self.assertEqual(len(unused_223), 69)
        self.assertEqual(CYCLE268_N_I, 6)
        self.assertEqual(CYCLE268_N_OFF_I, 0)
        self.assertEqual(CYCLE268_N_EXTRA, 2)
        self.assertTrue(CYCLE268_CLAIM)
        self.assertEqual(CYCLE290_N_I, 4)
        self.assertEqual(CYCLE290_N_OFF_I, 0)
        self.assertEqual(CYCLE290_N_EXTRA, 0)
        self.assertTrue(CYCLE290_CLAIM)
        self.assertEqual(STANDING_CYCLE302_N_DISTINCT, 8)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_021_4GRAMS_NOT_LOCKED)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE262)
        self.assertTrue(STANDING_DO_NOT_RELOCK_CYCLE268)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-304 leftover n=4 remaining previous-021 3-gram I-only lock."""
        lock = self.survey["i_3gram_021_090_076_i_only"]
        self.assertEqual(lock["cycle"], 304)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 5)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_remaining_previous_021_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(
            lock["leftover_n4_remaining_previous_021_count"],
            STANDING_LEFTOVER_MATCHING_COUNT,
        )
        self.assertEqual(lock["leftover_n4_remaining_previous_021_count"], 5)
        self.assertTrue(lock["leftover_n4_remaining_previous_021_subset_of_i_sites"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_3gram_sites"]),
            STANDING_LEFTOVER_3GRAM_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 5)
        self.assertEqual(lock["extra_i_sites"], [])
        self.assertEqual(lock["N_extra"], 0)
        self.assertEqual(lock["extra_i_090_076_sites"], [])
        self.assertEqual(lock["extra_i_overlap_leftover_extra_090_076_sites"], [])
        self.assertEqual(lock["extra_i_overlap_leftover_extra_090_076_count"], 0)
        self.assertEqual(
            [list(gram) for gram in STANDING_I_PREVIOUS_4GRAMS],
            lock["i_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_I_NEXT_4GRAMS],
            lock["i_next_4grams"],
        )
        self.assertEqual(
            [i_site_row_as_survey(row) for row in STANDING_I_SITE_ROWS],
            lock["i_site_rows"],
        )
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(lock["N_off_I"], 0)
        self.assertEqual(
            [list(site) for site in STANDING_OFF_I_SITES],
            lock["off_i_sites"],
        )
        self.assertEqual(tuple(lock["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(lock["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(
            tuple(lock["off_i_tablets_with_hits"]),
            STANDING_OFF_I_TABLETS_WITH_HITS,
        )
        self.assertEqual(
            lock["off_i_by_tablet_nonzero"],
            STANDING_OFF_I_BY_TABLET_NONZERO,
        )
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
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
        self.assertTrue(lock["overlap_does_not_lose"])
        self.assertEqual(
            list(STANDING_NESTED_LEFTOVER_N4_REMAINING),
            lock["nested_leftover_n4_remaining"],
        )
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
        self.assertEqual(lock["nested_cycle288_N_distinct_next_stems"], 6)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertFalse(lock["nested_cycle288_share_one_forward_stem"])
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle268_N_I"], 6)
        self.assertEqual(lock["nested_cycle268_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle268_N_extra"], 2)
        self.assertEqual(lock["nested_cycle290_N_I"], 4)
        self.assertEqual(lock["nested_cycle290_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle290_N_extra"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_3gram_021_090_076_i_only"])
        self.assertEqual(
            lock["i_3gram_021_090_076_i_only"],
            STANDING_I_3GRAM_021_090_076_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle207_3gram"])
        self.assertFalse(lock["same_as_cycle262_3gram"])
        self.assertFalse(lock["same_as_cycle268_3gram"])
        self.assertFalse(lock["same_as_cycle290_3gram"])
        self.assertFalse(lock["same_as_cycle303"])
        self.assertTrue(lock["same_claim_shape_as_cycle268"])
        self.assertTrue(lock["same_claim_shape_as_cycle290"])
        self.assertTrue(lock["090_076_without_021_does_not_count"])
        self.assertTrue(lock["600_090_076_does_not_count"])
        self.assertTrue(lock["999_090_076_does_not_count"])
        self.assertTrue(lock["090_076_020_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["leftover_n4_021_090_076_087_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_n4_remaining_previous_021_4grams_not_locked"])
        self.assertTrue(lock["do_not_relock_cycle262"])
        self.assertTrue(lock["do_not_relock_cycle268"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_021_kept"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_previous_021_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_previous_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_previous_021"]["cycle"],
            303,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_previous_021"][
                "i_leftover_n4_remaining_090_076_exactly_5_share_previous_021"
            ]
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
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"][
                "N_i_only"
            ],
            1,
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"], 288)
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"][
                "i_leftover_n4_remaining_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["G"], "020")
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["K"], 4)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["g_uniquely_most_frequent"]
        )
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"], 13)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
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


class TestMamariI3gram021090076IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 304 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
