"""I's cycle-271 leftover extra remaining-after-600 previous-090
3-gram 090 090 076 off-I lock.

Cycle 272 text-search lock. Uses already-vendored A–V and the
cycle-271 leftover extra remaining-after-600 previous-090
cluster (K_090=2 of N_remaining_after_090=35; leftover extra=56;
N_I=69). Does not retune that leftover extra remaining-after-600
previous-090 lock, leftover extra remaining-after-600 unique
previous stem (cycle 270 lost), leftover extra remaining-after-999
previous-600 (cycle 267 holds), leftover extra previous-999
(cycle 261 holds), leftover extra share-one-previous-stem
(cycle 260 lost), leftover extra share-one-forward-stem
(cycle 225 lost), leftover extra sites, the leftover n=4 set,
or the already-closed leftover remaining family. Does not
retune the forward peel of leftover extra I 090 076 (cycles
225–259). Does not peel leftover extra remaining-after-090 /
remaining 076/071/045/009 this cycle. Does not retune leftover
n=4. Does not overwrite cycle 167's 3-gram I-only 16/0 lock.
Does not overwrite cycle 268's 3-gram I-only 6/0 lock. Does
not overwrite cycle 271's leftover extra remaining-after-600
previous-090 lock. Does not retune cycle 248's 090 076 011
I-only 4/0 extra I=2 or peel 011. Does not vendor a new
tablet. Does not scrape X. W has no Barthel (cycle 100); skip
W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same claim-shape as cycle 212 (720 076 070 was I-only 3/0
after leftover previous-720) and cycle 268 (600 090 076 was
I-only 6/0 extra I=2 after leftover extra remaining-after-999
previous-600). Extra I of this 3-gram is leftover-of-leftover,
same shape as cycle 245 extra I of 090 076 087 and cycle 268
extra I of 600 090 076. Cycle 207 lost: 090 076 070 is not
I-only (8/1 on T). Cycle 223 lost: 090 076 is not I-only
(69/3 on T). T leaks of 090 076 are a real lose path for
090 090 076. Cycle 167 already owns 999 090 076 I-only 16/0;
this cycle is the new leftover extra remaining-after-600
previous-090 3-gram 090 090 076 only. 090 076 without the
leading 090, 999 090 076, 600 090 076, 720 076 070,
090 076 070, 090 076 011, leftover n=4 remaining
090 076 020 010, and leftover n=4 remaining 600 090 076 011
do not count as this 3-gram. Cycle 264 K_090=2 of I
999 090 076 at Ia12[46]/Ia14[139] is a different cluster.
Both leftover extra remaining-after-600 previous-090 sites
have previous 4-gram 011 090 090 076; related to 011
leftover-of-leftover, do not retune 248 or peel 011. Do not
retune leftover n=4, 076-cells, or any detector. Do not lock
leftover extra remaining-after-090. Off-I T sites of 090 076
are this cycle only as off-I of 090 090 076 if they match.
Do not assume the I-only result.

Locks exact consecutive hits of 090 090 076 on tablet I and
on every other vendored tablet A–H and J–V. Claim that can
lose: i_3gram_090_090_076_i_only (I hits ≥ 1 and off-I hits
== 0). True only if N_off_I == 0. Extra I ≠ 0 does not make
the claim lose (still I-only); still lock extra I. Measured:
Ia is exactly 3 at Ia5[142]/Ia12[41]/Ia14[104]; Ib unpublished
0; off-I is 1 on T (Ta5[8]). Leftover extra remaining-after-600
previous-090 2 sites (090-starts Ia12[42]/Ia14[105]) ⊆ those
I 3-gram sites (090-starts one token earlier). Extra I = 1
at Ia5[142] (090-start Ia5[143] sits inside leftover n=4
remaining 090 076 020 010; leftover of leftover, not locked
as remaining-after-090). The claim is false. Not an n≥8
island. Not the cycle-103 I 5-gram. Nested leftover extra
remaining-after-600 previous-090 K_090=2 / N_remaining_after_090=35,
leftover extra==56, N_I==69, cycle 271 both previous 4-grams
011 090 090 076, cycle 270 unique-max false 5-way K=2 G=090,
cycle 268 6/0 extra I=2, cycle 264 K_090=2 of I 999 090 076,
cycle 248 4/0 extra I=2, cycle 223 69/3, and cycle 207 8/1
on T stay.

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
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES as CYCLE223_I_SITES,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
    STANDING_OFF_I_PREVIOUS_4GRAMS as CYCLE223_OFF_I_PREVIOUS_4GRAMS,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_011_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE248_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_011_I_ONLY as CYCLE248_CLAIM,
    STANDING_N_EXTRA as CYCLE248_N_EXTRA,
    STANDING_N_I as CYCLE248_N_I,
    STANDING_N_OFF_I as CYCLE248_N_OFF_I,
    TestMamariI3gram090076011IOnlyScoreboard,
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
    STANDING_I_3GRAM_090_076_087_I_ONLY as CYCLE245_CLAIM,
    STANDING_N_EXTRA as CYCLE245_N_EXTRA,
    STANDING_N_I as CYCLE245_N_I,
    STANDING_N_OFF_I as CYCLE245_N_OFF_I,
    TestMamariI3gram090076087IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_600_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE268_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE268_EXTRA_I_SITES,
    STANDING_I_3GRAM_600_090_076_I_ONLY as CYCLE268_CLAIM,
    STANDING_I_SITES as CYCLE268_I_SITES,
    STANDING_N_EXTRA as CYCLE268_N_EXTRA,
    STANDING_N_I as CYCLE268_N_I,
    STANDING_N_OFF_I as CYCLE268_N_OFF_I,
    TestMamariI3gram600090076IOnlyScoreboard,
    named_off_i_sites,
)
from tests.test_mamari_i_3gram_720_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE212_GRAM3,
    STANDING_I_3GRAM_720_076_070_I_ONLY as CYCLE212_CLAIM,
    STANDING_I_SITES as CYCLE212_I_SITES,
    STANDING_N_I as CYCLE212_N_I,
    STANDING_N_OFF_I as CYCLE212_N_OFF_I,
    TestMamariI3gram720076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_I_SITES as CYCLE167_I_SITES,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_999_090_076_previous_090_scoreboard import (
    STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_090 as CYCLE264_CLAIM,
    STANDING_K_090 as CYCLE264_K_090,
    STANDING_MATCHING_SITES as CYCLE264_MATCHING_SITES,
    TestMamariI999090076Previous090Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    leftover_extra_previous_stems,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_090_scoreboard import (
    GRAM3_BACKWARD,
    STANDING_G as CYCLE271_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_EXACTLY_2_SHARE_PREVIOUS_090 as CYCLE271_CLAIM,
    STANDING_K_090 as CYCLE271_K_090,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE271_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE271_MATCHING_SITES,
    STANDING_N_LEFTOVER_EXTRA as CYCLE271_N_LEFTOVER_EXTRA,
    STANDING_N_REMAINING_AFTER_090 as CYCLE271_N_REMAINING_AFTER_090,
    leftover_extra_remaining_after_600_with_previous_090,
    TestMamariILeftoverExtra090076RemainingAfter600Previous090Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_stem_scoreboard import (
    STANDING_G as CYCLE270_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE270_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE270_CLAIM,
    STANDING_K as CYCLE270_K,
    STANDING_MATCHING_SITES as CYCLE270_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING as CYCLE270_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_600 as CYCLE270_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE270_N_TIED_AT_K,
    STANDING_TIED_STEMS as CYCLE270_TIED_STEMS,
    TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    STANDING_MATCHING_LEFTOVERS as CYCLE222_MATCHING_LEFTOVERS,
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
NEAR_MISS_999_090_076 = CYCLE167_GRAM3
NEAR_MISS_600_090_076 = CYCLE268_GRAM3
NEAR_MISS_720_076_070 = CYCLE212_GRAM3
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_090_076 = GRAM2
NEAR_MISS_N4_090_076_020_010 = ("090", "076", "020", "010")
NEAR_MISS_N4_600_090_076_011 = ("600", "090", "076", "011")
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_I_HITS = 3
STANDING_IA_HITS = 3
STANDING_IB_HITS = 0
STANDING_N_ON_I = 3
STANDING_N_I = 3
STANDING_I_SITES = (
    (SIDE_IA, "Ia5", 142),
    (SIDE_IA, "Ia12", 41),
    (SIDE_IA, "Ia14", 104),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_MATCHING_SITES = CYCLE271_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_COUNT = 2
STANDING_LEFTOVER_MATCHING_PREVIOUS_4GRAMS = CYCLE271_MATCHING_PREVIOUS_4GRAMS
STANDING_LEFTOVER_3GRAM_SITES = (
    (SIDE_IA, "Ia12", 41),
    (SIDE_IA, "Ia14", 104),
)
STANDING_N_LEFTOVER = 2
STANDING_EXTRA_I_SITES = (
    (SIDE_IA, "Ia5", 142),
)
STANDING_N_EXTRA = 1
STANDING_EXTRA_I_090_076_SITES = (
    (SIDE_IA, "Ia5", 143),
)
STANDING_I_PREVIOUS_4GRAMS = (
    ("079", "090", "090", "076"),
    ("011", "090", "090", "076"),
    ("011", "090", "090", "076"),
)
STANDING_I_NEXT_4GRAMS = (
    ("090", "090", "076", "020"),
    ("090", "090", "076", "530"),
    ("090", "090", "076", "071"),
)
STANDING_I_SITE_ROWS = (
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia5",
        "index": 142,
        "previous_4gram": ("079", "090", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia5", 143),
        "in_cycle271_leftover_extra_2": False,
        "inside_leftover_n4_remaining": True,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia12",
        "index": 41,
        "previous_4gram": ("011", "090", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia12", 42),
        "in_cycle271_leftover_extra_2": True,
        "inside_leftover_n4_remaining": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia14",
        "index": 104,
        "previous_4gram": ("011", "090", "090", "076"),
        "leftover_extra_090_076_site": (SIDE_IA, "Ia14", 105),
        "in_cycle271_leftover_extra_2": True,
        "inside_leftover_n4_remaining": False,
    },
)
STANDING_OFF_I_HITS = 1
STANDING_N_OFF_I = 1
STANDING_OFF_I_SITES = (
    (SIDE_TA, "Ta5", 8),
)
STANDING_OFF_I_PREVIOUS_4GRAM = ("090", "090", "090", "076")
STANDING_OFF_I_NEXT_4GRAM = ("090", "090", "076", "010")
STANDING_OFF_I_TABLETS_WITH_HITS = ("T",)
STANDING_OFF_I_BY_TABLET_NONZERO = {"T": 1}
STANDING_OFF_I_BY_TABLET = tuple(
    STANDING_OFF_I_BY_TABLET_NONZERO.get(tablet, 0) for tablet in OFF_I_TABLETS
)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS
    if tablet == "I"
    else STANDING_OFF_I_BY_TABLET_NONZERO.get(tablet, 0)
    for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_3gram_090_090_076_i_only"
STANDING_I_3GRAM_090_090_076_I_ONLY = False
STANDING_RESULT = "i_3gram_090_090_076_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = False
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE212_3GRAM = False
STANDING_SAME_AS_CYCLE245_3GRAM = False
STANDING_SAME_AS_CYCLE248_3GRAM = False
STANDING_SAME_AS_CYCLE264 = False
STANDING_SAME_AS_CYCLE268_3GRAM = False
STANDING_SAME_AS_CYCLE271 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE212 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245_EXTRA_I = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE268 = True
STANDING_090_076_WITHOUT_LEADING_090_DOES_NOT_COUNT = True
STANDING_999_090_076_DOES_NOT_COUNT = True
STANDING_600_090_076_DOES_NOT_COUNT = True
STANDING_720_076_070_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_011_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_090_076_020_010_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_600_090_076_011_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_090_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_REMAINING_AFTER_090 = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_CYCLE167_NOT_OVERWRITTEN = True
STANDING_CYCLE248_NOT_RETUNED = True
STANDING_CYCLE268_NOT_OVERWRITTEN = True
STANDING_CYCLE271_NOT_OVERWRITTEN = True
STANDING_CYCLE264_IS_DIFFERENT_CLUSTER = True
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE271_K_090 = 2
STANDING_CYCLE271_G = "090"
STANDING_CYCLE271_N_REMAINING_AFTER_090 = 35
STANDING_CYCLE271_N_LEFTOVER_EXTRA = 56


def leftover_extra_090_076_site_for_3gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """090 076 starts one token after 090 090 076."""
    side, line, index = site
    return (side, line, index + 1)


def leftover_extra_remaining_after_600_previous_090_3gram_sites(
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-600 previous-090 090-starts shifted to 3-gram starts."""
    return tuple((side, line, index - 1) for side, line, index in leftover_matching)


def leftover_extra_remaining_after_600_previous_090_subset(
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff leftover extra remaining-after-600 previous-090 2 sites ⊆ I 090 090 076."""
    return set(
        leftover_extra_remaining_after_600_previous_090_3gram_sites(leftover_matching)
    ).issubset(set(i_sites))


def leftover_3gram_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 090 090 076 sites whose 090 076 is leftover extra remaining-after-600 previous-090."""
    leftover_set = set(leftover_matching)
    return tuple(
        site
        for site in i_sites
        if leftover_extra_090_076_site_for_3gram(site) in leftover_set
    )


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 090 090 076 sites that are not leftover extra remaining-after-600 previous-090."""
    leftover_set = set(leftover_matching)
    return tuple(
        site
        for site in i_sites
        if leftover_extra_090_076_site_for_3gram(site) not in leftover_set
    )


def site_previous_4gram_for_3gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """W 090 090 076 if a previous stem exists; None at start-of-line."""
    if tuple(stems[index : index + len(gram3)]) != gram3:
        return None
    if index < 1:
        return None
    return tuple(stems[index - 1 : index + len(gram3)])


def i_3gram_090_090_076_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0. Extra I does not lose."""
    return i_hits >= 1 and off_i_hits == 0


def i_site_row_as_survey(row: dict) -> dict:
    """JSON-ready site row (lists, not tuples)."""
    return {
        "tablet": row["tablet"],
        "side": row["side"],
        "line": row["line"],
        "index": row["index"],
        "previous_4gram": list(row["previous_4gram"]),
        "leftover_extra_090_076_site": list(row["leftover_extra_090_076_site"]),
        "in_cycle271_leftover_extra_2": row["in_cycle271_leftover_extra_2"],
        "inside_leftover_n4_remaining": row["inside_leftover_n4_remaining"],
    }


class TestI3gram090090076IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-271 leftover extra remaining-after-600 previous-090 3-gram."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. 090 076 / 600 090 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["090", "090", "076", "090", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 2)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_600_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_720_076_070)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["600", "090", "076"]], GRAM3), 0)
        self.assertTrue(STANDING_090_076_WITHOUT_LEADING_090_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_600_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_720_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_011_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_090_076_020_010_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_600_090_076_011_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Extra I does not lose."""
        provider = MockProvider()
        self.assertTrue(i_3gram_090_090_076_i_only(1, 0))
        self.assertTrue(i_3gram_090_090_076_i_only(2, 0))
        self.assertTrue(i_3gram_090_090_076_i_only(3, 0))
        self.assertFalse(i_3gram_090_090_076_i_only(3, 1))
        self.assertFalse(i_3gram_090_090_076_i_only(1, 1))
        self.assertFalse(i_3gram_090_090_076_i_only(0, 0))
        self.assertFalse(i_3gram_090_090_076_i_only(0, 1))
        self.assertEqual(STANDING_CLAIM, "i_3gram_090_090_076_i_only")
        self.assertFalse(STANDING_I_3GRAM_090_090_076_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertNotEqual(
            STANDING_I_3GRAM_090_090_076_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertNotEqual(STANDING_N_EXTRA, 0)
        self.assertFalse(STANDING_I_3GRAM_090_090_076_I_ONLY)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_fail(self):
        """Leftover extra previous-090 ⊆ I sites; extra is nonempty leftover-of-leftover."""
        provider = MockProvider()
        self.assertTrue(
            leftover_extra_remaining_after_600_previous_090_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(
            leftover_extra_remaining_after_600_previous_090_3gram_sites(),
            STANDING_LEFTOVER_3GRAM_SITES,
        )
        self.assertEqual(leftover_3gram_sites(), STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(extra_i_sites(), STANDING_EXTRA_I_SITES)
        self.assertEqual(len(extra_i_sites()), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertEqual(STANDING_N_LEFTOVER + STANDING_N_EXTRA, STANDING_N_I)
        self.assertEqual(
            leftover_extra_090_076_site_for_3gram(STANDING_EXTRA_I_SITES[0]),
            STANDING_EXTRA_I_090_076_SITES[0],
        )
        planted_extra = STANDING_I_SITES + ((SIDE_IA, "Ia1", 0),)
        self.assertFalse(
            leftover_extra_remaining_after_600_previous_090_subset(
                STANDING_LEFTOVER_MATCHING_SITES + ((SIDE_IA, "Ia1", 1),),
                STANDING_I_SITES,
            )
        )
        self.assertEqual(len(extra_i_sites(planted_extra)), 2)
        dropped = tuple(
            site
            for site in STANDING_I_SITES
            if site != STANDING_LEFTOVER_3GRAM_SITES[0]
        )
        self.assertFalse(
            leftover_extra_remaining_after_600_previous_090_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                dropped,
            )
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_cycle271_leftover_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-271 leftover extra previous G, not priors."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3[1:], GRAM2)
        self.assertEqual(GRAM3[0], CYCLE271_G)
        self.assertNotEqual(GRAM3, CYCLE167_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE268_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE212_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, GRAM2)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_N4_090_076_020_010))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_N4_600_090_076_011))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE212_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE245_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE248_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE264)
        self.assertFalse(STANDING_SAME_AS_CYCLE268_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE271)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE212)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245_EXTRA_I)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE268)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        self.assertLess(len(GRAM3), 8)
        for prev4 in STANDING_I_PREVIOUS_4GRAMS:
            self.assertTrue(is_contiguous_substring(GRAM3, prev4))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_720_076_070))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_070))
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM3))
        self.assertIn(NEAR_MISS_N4_090_076_020_010, CYCLE222_MATCHING_LEFTOVERS)
        self.assertIn(NEAR_MISS_N4_600_090_076_011, CYCLE222_MATCHING_LEFTOVERS)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_090_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_090)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram090090076IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover extra remaining-after-600 previous-090 3-gram off-I lock."""

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
        self.previous_stems = leftover_extra_previous_stems(
            self.i_sides,
            STANDING_LEFTOVER_SITES,
            GRAM2,
        )
        self.leftover_matching = leftover_extra_remaining_after_600_with_previous_090(
            STANDING_LEFTOVER_SITES,
            self.previous_stems,
        )
        self.leftover = leftover_3gram_sites(self.i_sites, self.leftover_matching)
        self.extra = extra_i_sites(self.i_sites, self.leftover_matching)
        self.claim_holds = i_3gram_090_090_076_i_only(
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
        self.leftover_extra_090_076_sites = tuple(
            leftover_extra_090_076_site_for_3gram(site) for site in self.leftover
        )

    def test_tokens_are_cycle_271_leftover_not_retuned(self):
        """3-gram is the cycle-271 leftover extra previous G, not a new inventory."""
        self.assertEqual(GRAM3, ("090", "090", "076"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3[1:], GRAM2)
        self.assertEqual(GRAM3[0], "090")
        prior_271 = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]
        self.assertEqual(prior_271["cycle"], 271)
        self.assertEqual(tuple(prior_271["backward_3gram"]), GRAM3)
        self.assertEqual(prior_271["G"], "090")
        self.assertEqual(prior_271["K"], 2)
        self.assertEqual(prior_271["K_090"], 2)
        self.assertEqual(prior_271["N_remaining_after_090"], 35)
        self.assertEqual(prior_271["N_leftover_extra"], 56)
        self.assertEqual(prior_271["N_I"], 69)
        self.assertEqual(CYCLE271_G, "090")
        self.assertEqual(CYCLE271_K_090, 2)
        self.assertEqual(CYCLE271_N_REMAINING_AFTER_090, 35)
        self.assertEqual(CYCLE271_N_LEFTOVER_EXTRA, 56)
        self.assertTrue(CYCLE271_CLAIM)
        self.assertTrue(
            prior_271[
                "i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090"
            ]
        )
        measured_matching = [list(site) for site in CYCLE271_MATCHING_SITES]
        self.assertEqual(
            [list(site) for site in prior_271["matching_leftover_extra_remaining_after_600_sites"]],
            measured_matching,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE271_MATCHING_PREVIOUS_4GRAMS],
            prior_271["matching_previous_4grams"],
        )
        self.assertEqual(
            CYCLE271_MATCHING_PREVIOUS_4GRAMS,
            (("011", "090", "090", "076"), ("011", "090", "090", "076")),
        )
        self.assertEqual(self.leftover_matching, CYCLE271_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE271_K_090)
        self.assertEqual(STANDING_CYCLE271_K_090, 2)
        self.assertEqual(STANDING_CYCLE271_G, "090")
        self.assertEqual(STANDING_CYCLE271_N_REMAINING_AFTER_090, 35)
        self.assertEqual(STANDING_CYCLE271_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(STANDING_CYCLE223_N_I, 69)
        if (
            len(self.leftover_matching) != 2
            or CYCLE271_G != "090"
            or CYCLE271_K_090 != 2
            or CYCLE271_N_REMAINING_AFTER_090 != 35
            or CYCLE271_N_LEFTOVER_EXTRA != 56
            or CYCLE223_N_I != 69
        ):
            self.fail(
                "nested leftover extra remaining-after-600 previous-090 "
                "K_090=2 N_remaining_after_090=35 leftover extra=56 N_I=69 drifted"
            )
        prior_270 = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]
        self.assertEqual(prior_270["cycle"], 270)
        self.assertEqual(prior_270["G"], "090")
        self.assertEqual(prior_270["K"], 2)
        self.assertEqual(prior_270["N_remaining_after_600"], 37)
        self.assertFalse(prior_270["G_uniquely_most_frequent"])
        self.assertEqual(tuple(prior_270["tied_stems_at_K"]), CYCLE270_TIED_STEMS)
        self.assertEqual(prior_270["N_tied_at_K"], 5)
        self.assertFalse(
            prior_270["i_leftover_extra_090_076_remaining_after_600_unique_previous_stem"]
        )
        if (
            prior_270["G"] != "090"
            or prior_270["K"] != 2
            or prior_270["N_remaining_after_600"] != 37
            or prior_270["G_uniquely_most_frequent"]
            or prior_270["N_tied_at_K"] != 5
        ):
            self.fail(
                "nested cycle 270 unique-max false 5-way K=2 G=090 drifted"
            )
        prior_268 = self.survey["i_3gram_600_090_076_i_only"]
        self.assertEqual(prior_268["cycle"], 268)
        self.assertEqual(prior_268["N_I"], 6)
        self.assertEqual(prior_268["N_off_I"], 0)
        self.assertEqual(prior_268["N_extra"], 2)
        self.assertTrue(prior_268["i_3gram_600_090_076_i_only"])
        prior_264 = self.survey["i_999_090_076_previous_090"]
        self.assertEqual(prior_264["cycle"], 264)
        self.assertEqual(prior_264["K_090"], 2)
        self.assertTrue(prior_264["i_999_090_076_exactly_2_share_previous_090"])
        self.assertNotEqual(CYCLE264_MATCHING_SITES, CYCLE271_MATCHING_SITES)
        prior_248 = self.survey["i_3gram_090_076_011_i_only"]
        self.assertEqual(prior_248["cycle"], 248)
        self.assertEqual(prior_248["N_I"], 4)
        self.assertEqual(prior_248["N_off_I"], 0)
        self.assertEqual(prior_248["N_extra"], 2)
        self.assertTrue(prior_248["i_3gram_090_076_011_i_only"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_212 = self.survey["i_3gram_720_076_070_i_only"]
        self.assertEqual(prior_212["cycle"], 212)
        self.assertEqual(prior_212["N_I"], 3)
        self.assertEqual(prior_212["N_off_I"], 0)
        self.assertTrue(prior_212["i_3gram_720_076_070_i_only"])
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertTrue(prior_167["i_3gram_999_090_076_i_only"])
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_090_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_REMAINING_AFTER_090)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE248_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE268_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE271_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE264_IS_DIFFERENT_CLUSTER)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_three_on_ia_and_leftover_extra_090_is_subset(self):
        """3-gram is 3 on Ia; Ib 0. Leftover extra previous-090 is 2 of those 3."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 3)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 3)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 3)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM3, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM3), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE271_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE270_MATCHING_SITES)
        self.assertNotEqual(self.leftover, STANDING_I_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 2)
        self.assertTrue(
            leftover_extra_remaining_after_600_previous_090_subset(
                self.leftover_matching,
                self.i_sites,
            )
        )
        self.assertEqual(self.leftover, STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.leftover), STANDING_N_LEFTOVER)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER, 2)
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertEqual(STANDING_N_LEFTOVER + STANDING_N_EXTRA, STANDING_N_I)
        self.assertEqual(self.leftover_extra_090_076_sites, CYCLE271_MATCHING_SITES)
        if self.i_hits != 3:
            self.fail("measured N_I drifted from 3")
        if self.leftover_matching != CYCLE271_MATCHING_SITES:
            self.fail("leftover extra remaining-after-600 previous-090 set drifted")
        if not leftover_extra_remaining_after_600_previous_090_subset(
            self.leftover_matching,
            self.i_sites,
        ):
            self.fail(
                "leftover extra remaining-after-600 previous-090 2 sites "
                "not subset of I 090 090 076"
            )
        if self.extra != STANDING_EXTRA_I_SITES:
            self.fail("extra I 090 090 076 leftover-of-leftover sites drifted")
        leftover_set = set(STANDING_LEFTOVER_3GRAM_SITES)
        extra_set = set(STANDING_EXTRA_I_SITES)
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
            gram2_site = leftover_extra_090_076_site_for_3gram(site)
            self.assertEqual((row["side"], row["line"], row["index"]), site)
            self.assertEqual(row["previous_4gram"], prev4)
            self.assertEqual(tuple(row["leftover_extra_090_076_site"]), gram2_site)
            if site in leftover_set:
                self.assertIn(gram2_site, STANDING_LEFTOVER_SITES)
                self.assertIn(gram2_site, CYCLE271_MATCHING_SITES)
                self.assertNotIn(gram2_site, CYCLE224_INSIDE_SITES)
                self.assertTrue(row["in_cycle271_leftover_extra_2"])
                self.assertFalse(row["inside_leftover_n4_remaining"])
                self.assertEqual(prev4, ("011", "090", "090", "076"))
            else:
                self.assertIn(site, extra_set)
                self.assertIn(gram2_site, CYCLE224_INSIDE_SITES)
                self.assertNotIn(gram2_site, STANDING_LEFTOVER_SITES)
                self.assertNotIn(gram2_site, CYCLE271_MATCHING_SITES)
                self.assertFalse(row["in_cycle271_leftover_extra_2"])
                self.assertTrue(row["inside_leftover_n4_remaining"])
                self.assertEqual(nxt4, ("090", "090", "076", "020"))
            self.assertNotIn(site, CYCLE268_I_SITES)
            self.assertNotIn(site, CYCLE212_I_SITES)
            self.assertNotIn(site, CYCLE207_I_SITES)
            self.assertNotIn(site, CYCLE167_I_SITES)
            self.assertNotIn(site, CYCLE264_MATCHING_SITES)
            self.assertNotIn(gram2_site, CYCLE264_MATCHING_SITES)
        self.assertEqual(self.previous_4grams, STANDING_I_PREVIOUS_4GRAMS)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        self.assertEqual(STANDING_EXTRA_I_SITES, ((SIDE_IA, "Ia5", 142),))
        self.assertEqual(STANDING_EXTRA_I_090_076_SITES, ((SIDE_IA, "Ia5", 143),))
        for gram2_site in STANDING_EXTRA_I_090_076_SITES:
            self.assertIn(gram2_site, CYCLE223_I_SITES)
            self.assertIn(gram2_site, CYCLE224_INSIDE_SITES)
        self.assertFalse(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_090_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_one_off_i_and_not_i_only(self):
        """3-gram is 1 on T and 0 on A–H and J–S/U–V. Ia has exactly 3. Claim loses."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, STANDING_N_OFF_I)
        self.assertEqual(STANDING_N_OFF_I, 1)
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(STANDING_OFF_I_SITES, ((SIDE_TA, "Ta5", 8),))
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ("T",))
        self.assertEqual(STANDING_OFF_I_BY_TABLET_NONZERO, {"T": 1})
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM3))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 3)
            elif tablet == "T":
                self.assertEqual(count, 1)
            else:
                self.assertEqual(count, 0)
        gk = load_g_k_sides()
        self.assertEqual(ngram_hit_count(gk[SIDE_GR], GRAM3), 0)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], GRAM3), 0)
        s_sides = load_s_sides()
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], GRAM3), 0)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], GRAM3), 0)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM3), 1)
        self.assertEqual(named_off_i_sites(GRAM3), STANDING_OFF_I_SITES)
        ta5 = t_sides[SIDE_TA][TA_LINE_NAMES.index("Ta5")]
        self.assertEqual(tuple(ta5[8:11]), GRAM3)
        self.assertEqual(tuple(ta5[7:11]), STANDING_OFF_I_PREVIOUS_4GRAM)
        self.assertEqual(tuple(ta5[8:12]), STANDING_OFF_I_NEXT_4GRAM)
        self.assertEqual(CYCLE223_OFF_I_SITES, (
            (SIDE_TA, "Ta5", 9),
            (SIDE_TA, "Ta7", 5),
            (SIDE_TA, "Ta9", 2),
        ))
        self.assertEqual(
            CYCLE223_OFF_I_FOLLOWING_3GRAMS,
            (("090", "076", "010"), ("090", "076", "126"), ("090", "076", "070")),
        )
        self.assertEqual(
            CYCLE223_OFF_I_PREVIOUS_4GRAMS[0],
            STANDING_OFF_I_NEXT_4GRAM,
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
            if site == (SIDE_TA, "Ta5", 9):
                self.assertEqual(tuple(stems[index - 1 : index + 2]), GRAM3)
                self.assertEqual((side, line, index - 1), STANDING_OFF_I_SITES[0])
            else:
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
            i_3gram_090_090_076_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_3GRAM_090_090_076_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_090_090_076_I_ONLY,
        )
        self.assertFalse(self.claim_holds)
        self.assertFalse(STANDING_I_3GRAM_090_090_076_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_3gram_090_090_076_i_only")
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE212_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE245_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE248_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE264)
        self.assertFalse(STANDING_SAME_AS_CYCLE268_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE271)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE212)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245_EXTRA_I)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE268)
        if self.off_i_hits != 1:
            self.fail("measured N_off_I drifted from 1")
        if self.i_hits != STANDING_N_I:
            self.fail("measured N_I drifted from the locked count")
        if self.off_i_sites != STANDING_OFF_I_SITES:
            self.fail("off-I T site of 090 090 076 drifted")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_271_270_268_264_248_223_207_and_w_still_compute(self):
        """Cycle 271 K=2/35, 270 5-way lose, 268 6/0 extra I=2, 264 K_090=2, 248 4/0 extra I=2, 223 69/3, 207 8/1 stay."""
        prior_271 = TestMamariILeftoverExtra090076RemainingAfter600Previous090Scoreboard()
        prior_271.setUp()
        prior_271.test_counts_2_of_37_and_hypothesis_k_2_holds()
        prior_271.test_survey_matches_computed_lock()
        self.assertEqual(prior_271.k_090, 2)
        self.assertEqual(CYCLE271_G, "090")
        self.assertEqual(prior_271.n_remaining_after_090, 35)
        self.assertEqual(prior_271.n_leftover_extra, 56)
        self.assertEqual(prior_271.matching, CYCLE271_MATCHING_SITES)
        self.assertEqual(
            prior_271.matching_previous_4grams,
            (("011", "090", "090", "076"), ("011", "090", "090", "076")),
        )
        self.assertTrue(prior_271.claim_holds)
        self.assertTrue(CYCLE271_CLAIM)
        if (
            prior_271.k_090 != 2
            or CYCLE271_G != "090"
            or prior_271.n_remaining_after_090 != 35
            or prior_271.n_leftover_extra != 56
        ):
            self.fail(
                "nested cycle 271 leftover extra remaining-after-600 previous-090 "
                "K_090=2 N_remaining_after_090=35 drifted"
            )
        prior_270 = TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard()
        prior_270.setUp()
        prior_270.test_counts_37_remaining_g_090_k_2_five_way_tie_and_hypothesis_loses()
        prior_270.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE270_N_DISTINCT, 32)
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        self.assertEqual(CYCLE270_N_REMAINING, 37)
        self.assertEqual(CYCLE270_N_TIED_AT_K, 5)
        self.assertEqual(CYCLE270_TIED_STEMS, ("090", "076", "071", "045", "009"))
        self.assertFalse(prior_270.unique)
        self.assertFalse(prior_270.claim_holds)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertFalse(CYCLE270_UNIQUE)
        if (
            prior_270.n_remaining != 37
            or CYCLE270_G != "090"
            or CYCLE270_K != 2
            or prior_270.unique
            or CYCLE270_N_TIED_AT_K != 5
        ):
            self.fail("nested cycle 270 unique-max false 5-way K=2 G=090 drifted")
        prior_268 = TestMamariI3gram600090076IOnlyScoreboard()
        prior_268.setUp()
        prior_268.test_3gram_is_zero_off_i_and_i_only()
        prior_268.test_survey_matches_computed_lock()
        self.assertEqual(prior_268.i_hits, CYCLE268_N_I)
        self.assertEqual(prior_268.i_hits, 6)
        self.assertEqual(prior_268.off_i_hits, CYCLE268_N_OFF_I)
        self.assertEqual(prior_268.off_i_hits, 0)
        self.assertEqual(CYCLE268_N_EXTRA, 2)
        self.assertEqual(prior_268.extra, CYCLE268_EXTRA_I_SITES)
        self.assertTrue(prior_268.claim_holds)
        self.assertTrue(CYCLE268_CLAIM)
        if prior_268.i_hits != 6 or prior_268.off_i_hits != 0 or CYCLE268_N_EXTRA != 2:
            self.fail("nested cycle 268 600 090 076 I-only 6/0 extra I=2 drifted")
        prior_264 = TestMamariI999090076Previous090Scoreboard()
        prior_264.setUp()
        prior_264.test_counts_exactly_2_share_previous_090_and_hypothesis_holds()
        prior_264.test_survey_matches_computed_lock()
        self.assertEqual(prior_264.k_090, 2)
        self.assertEqual(prior_264.matching, CYCLE264_MATCHING_SITES)
        self.assertEqual(CYCLE264_MATCHING_SITES, ((SIDE_IA, "Ia12", 46), (SIDE_IA, "Ia14", 139)))
        self.assertTrue(prior_264.claim_holds)
        self.assertTrue(CYCLE264_CLAIM)
        self.assertEqual(CYCLE264_K_090, 2)
        self.assertNotEqual(prior_264.matching, CYCLE271_MATCHING_SITES)
        if prior_264.k_090 != 2:
            self.fail("nested cycle 264 K_090=2 drifted")
        prior_248 = TestMamariI3gram090076011IOnlyScoreboard()
        prior_248.setUp()
        prior_248.test_3gram_is_zero_off_i_and_i_only()
        prior_248.test_survey_matches_computed_lock()
        self.assertEqual(prior_248.i_hits, CYCLE248_N_I)
        self.assertEqual(prior_248.off_i_hits, CYCLE248_N_OFF_I)
        self.assertEqual(CYCLE248_N_EXTRA, 2)
        self.assertEqual(CYCLE248_N_I, 4)
        self.assertEqual(CYCLE248_N_OFF_I, 0)
        self.assertTrue(prior_248.claim_holds)
        self.assertTrue(CYCLE248_CLAIM)
        if prior_248.i_hits != 4 or prior_248.off_i_hits != 0 or CYCLE248_N_EXTRA != 2:
            self.fail("nested cycle 248 090 076 011 I-only 4/0 extra I=2 drifted")
        unused_248 = CYCLE248_EXTRA_I_SITES
        self.assertEqual(len(unused_248), 2)
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
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertFalse(prior_207.claim_holds)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_212 = TestMamariI3gram720076070IOnlyScoreboard()
        prior_212.setUp()
        prior_212.test_3gram_is_zero_off_i_and_i_only()
        prior_212.test_survey_matches_computed_lock()
        self.assertEqual(prior_212.i_hits, CYCLE212_N_I)
        self.assertEqual(prior_212.off_i_hits, CYCLE212_N_OFF_I)
        self.assertTrue(prior_212.claim_holds)
        self.assertTrue(CYCLE212_CLAIM)
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(prior_167.i_hits, CYCLE167_N_I)
        self.assertEqual(prior_167.i_hits, 16)
        self.assertEqual(prior_167.off_i_hits, CYCLE167_N_OFF_I)
        self.assertEqual(prior_167.off_i_hits, 0)
        self.assertEqual(prior_167.i_sites, CYCLE167_I_SITES)
        self.assertTrue(prior_167.claim_holds)
        self.assertTrue(CYCLE167_CLAIM)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
        prior_245 = TestMamariI3gram090076087IOnlyScoreboard()
        prior_245.setUp()
        prior_245.test_3gram_is_zero_off_i_and_i_only()
        prior_245.test_survey_matches_computed_lock()
        self.assertEqual(prior_245.i_hits, CYCLE245_N_I)
        self.assertEqual(prior_245.off_i_hits, CYCLE245_N_OFF_I)
        self.assertEqual(CYCLE245_N_EXTRA, 3)
        self.assertTrue(prior_245.claim_holds)
        self.assertTrue(CYCLE245_CLAIM)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_090_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE248_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE268_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE271_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-272 leftover extra previous-090 3-gram I-only lose."""
        lock = self.survey["i_3gram_090_090_076_i_only"]
        self.assertEqual(lock["cycle"], 272)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 3)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_extra_remaining_after_600_previous_090_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(
            lock["leftover_extra_remaining_after_600_previous_090_count"],
            STANDING_LEFTOVER_MATCHING_COUNT,
        )
        self.assertEqual(lock["leftover_extra_remaining_after_600_previous_090_count"], 2)
        self.assertTrue(lock["leftover_extra_remaining_after_600_previous_090_subset_of_i_sites"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_3gram_sites"]),
            STANDING_LEFTOVER_3GRAM_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_090_076_sites"]),
            STANDING_EXTRA_I_090_076_SITES,
        )
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
        self.assertEqual(lock["N_off_I"], 1)
        self.assertEqual(
            [list(site) for site in STANDING_OFF_I_SITES],
            lock["off_i_sites"],
        )
        self.assertEqual(tuple(lock["off_i_previous_4gram"]), STANDING_OFF_I_PREVIOUS_4GRAM)
        self.assertEqual(tuple(lock["off_i_next_4gram"]), STANDING_OFF_I_NEXT_4GRAM)
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
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_3gram_090_090_076_i_only"])
        self.assertEqual(
            lock["i_3gram_090_090_076_i_only"],
            STANDING_I_3GRAM_090_090_076_I_ONLY,
        )
        self.assertFalse(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle212_3gram"])
        self.assertFalse(lock["same_as_cycle245_3gram"])
        self.assertFalse(lock["same_as_cycle248_3gram"])
        self.assertFalse(lock["same_as_cycle264"])
        self.assertFalse(lock["same_as_cycle268_3gram"])
        self.assertFalse(lock["same_as_cycle271"])
        self.assertTrue(lock["same_claim_shape_as_cycle212"])
        self.assertTrue(lock["same_claim_shape_as_cycle245_extra_i"])
        self.assertTrue(lock["same_claim_shape_as_cycle268"])
        self.assertTrue(lock["090_076_without_leading_090_does_not_count"])
        self.assertTrue(lock["999_090_076_does_not_count"])
        self.assertTrue(lock["600_090_076_does_not_count"])
        self.assertTrue(lock["720_076_070_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_011_does_not_count"])
        self.assertTrue(lock["leftover_n4_090_076_020_010_does_not_count"])
        self.assertTrue(lock["leftover_n4_600_090_076_011_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_090_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_remaining_after_090"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["cycle167_not_overwritten"])
        self.assertTrue(lock["cycle248_not_retuned"])
        self.assertTrue(lock["cycle268_not_overwritten"])
        self.assertTrue(lock["cycle271_not_overwritten"])
        self.assertTrue(lock["cycle264_is_different_cluster"])
        self.assertTrue(lock["raw_stems_090_kept"])
        self.assertEqual(lock["nested_cycle271_K_090"], 2)
        self.assertEqual(lock["nested_cycle271_N_remaining_after_090"], 35)
        self.assertEqual(lock["nested_cycle271_N_leftover_extra"], 56)
        self.assertEqual(lock["nested_cycle271_N_I"], 69)
        self.assertEqual(
            [list(gram) for gram in CYCLE271_MATCHING_PREVIOUS_4GRAMS],
            lock["nested_cycle271_matching_previous_4grams"],
        )
        self.assertFalse(lock["nested_cycle270_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle270_G"], "090")
        self.assertEqual(lock["nested_cycle270_K"], 2)
        self.assertEqual(lock["nested_cycle270_N_tied_at_K"], 5)
        self.assertEqual(tuple(lock["nested_cycle270_tied_stems_at_K"]), CYCLE270_TIED_STEMS)
        self.assertEqual(lock["nested_cycle268_N_I"], 6)
        self.assertEqual(lock["nested_cycle268_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle268_N_extra"], 2)
        self.assertEqual(lock["nested_cycle264_K_090"], 2)
        self.assertTrue(lock["nested_cycle264_exactly_2_share_previous_090"])
        self.assertTrue(lock["nested_cycle264_is_different_cluster"])
        self.assertEqual(lock["nested_cycle248_N_I"], 4)
        self.assertEqual(lock["nested_cycle248_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle248_N_extra"], 2)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle212_N_I"], 3)
        self.assertEqual(lock["nested_cycle212_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_090_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_3gram_600_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_999_090_076_previous_090_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_011_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_720_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_087_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]["cycle"],
            271,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"][
                "i_leftover_extra_090_076_remaining_after_600_exactly_2_share_previous_090"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"]["K_090"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_090"][
                "N_remaining_after_090"
            ],
            35,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["cycle"],
            270,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"][
                "i_leftover_extra_090_076_remaining_after_600_unique_previous_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]["G"],
            "090",
        )
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["cycle"], 268)
        self.assertTrue(self.survey["i_3gram_600_090_076_i_only"]["i_3gram_600_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_600_090_076_i_only"]["N_extra"], 2)
        self.assertEqual(self.survey["i_999_090_076_previous_090"]["cycle"], 264)
        self.assertEqual(self.survey["i_999_090_076_previous_090"]["K_090"], 2)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["cycle"], 248)
        self.assertTrue(self.survey["i_3gram_090_076_011_i_only"]["i_3gram_090_076_011_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_extra"], 2)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["cycle"], 212)
        self.assertTrue(self.survey["i_3gram_720_076_070_i_only"]["i_3gram_720_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI3gram090090076IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 272 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
