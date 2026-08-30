"""I's cycle-200 leftover 3-gram 099 076 071 off-I lock.

Cycle 201 text-search lock. Uses already-vendored A–V and the
cycle-200 leftover previous 3-gram 099 076 071 (the n=3 run
shared by leftover 076 071 sites Ia6[117] 430 099 076 071
and Ia12[6] 019 099 076 071). Does not retune that 3-gram,
those leftover sites, or the leftover n=4 set. Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 198 (604 076 071 was I-only 2/0),
cycle 195 (090 076 071 was I-only 6/0), cycle 192
(700 076 071 was I-only 3/0), cycle 186 (076 071 061 was
I-only 2/0), cycle 183 (076 071 700 was I-only 3/0), cycle
180 (076 071 090 was I-only 5/0), cycle 177 (076 071 600
was I-only 4/0), cycle 174 (076 071 076 was I-only 6/0),
cycle 171 (076 071 was I-only 43/0), cycle 167
(999 090 076 was I-only 16/0), cycle 160 (076 020 010 was
I-only 12/0), and cycle 141 (076 010 079 was I-only 8/0).
This cycle is the new leftover previous 3-gram 099 076 071
only. 071 999 (071 065 071 999) does not count. 076 076
(700 076 076 053) does not. Cycle 191 leftover 700 076 071
does not. Cycle 194 leftover 090 076 071 does not. Cycle
197 leftover 604 076 071 does not. Near-miss Ia1[163]
090 700 076 071 does not (the previous stem is 700).
Cycle 191's near-miss Ia9[10] 700 604 076 071 does not
(the previous stem is 604). 099 076 not followed by 071
does not. Do not retune 604 076 071, 090 076 071,
700 076 071, 076 071, 999 090 076, 076 020 010, or
076 010 079. Cycle 200 leftover N=2, cycle 197 leftover
N=2, cycle 194 leftover N=3, cycle 191 leftover N=3,
cycle 190 N_distinct=28, cycle 172 leftover N=34, and
leftover n=4 set stay. Do not assume the I-only result.
Include any inside-family 076 071 site that also has this
3-gram, if one exists (none does; cycle 200 already
measured that).

Locks exact consecutive hits of 099 076 071 on tablet I
and on every other vendored tablet A–H and J–V. Claim that
can lose: i_3gram_099_076_071_i_only (I hits ≥ 1 and
off-I hits == 0). True only if N_off_I == 0. Ia is exactly
2 at Ia6[116]/Ia12[5] (the two leftover-2 / leftover-34
076 071 sites; no inside-family 076 071 site has this
3-gram; no extra I hits); Ib unpublished 0; every other
vendored tablet is exact-0. Not an n≥8 island. Not the
cycle-103 I 5-gram.

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
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_I_SITES as CYCLE171_I_SITES,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_inside_family_scoreboard import (
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_LEFTOVER as CYCLE172_N_LEFTOVER,
    TestMamariI2gram076071InsideFamilyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
    TestMamariI3gram090076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_604_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE198_GRAM3,
    TestMamariI3gram604076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_700_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE192_GRAM3,
    TestMamariI3gram700076071IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_090_scoreboard import (
    GRAM3_BACKWARD as CYCLE194_GRAM3_BACKWARD,
    STANDING_MATCHING_SITES as CYCLE194_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_090_076_071 as CYCLE194_N_WITH,
    TestMamariILeftover076071Previous090Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_099_scoreboard import (
    GRAM3_BACKWARD,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE200_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE200_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_099_076_071 as CYCLE200_N_WITH,
    STANDING_NEAR_MISS_CYCLE191_090_700_PREVIOUS_4GRAM,
    STANDING_NEAR_MISS_CYCLE191_090_700_SITE,
    TestMamariILeftover076071Previous099Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_604_scoreboard import (
    GRAM3_BACKWARD as CYCLE197_GRAM3_BACKWARD,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE197_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE197_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_604_076_071 as CYCLE197_N_WITH,
    STANDING_NEAR_MISS_FORWARD_604_NEXT_4GRAMS,
    STANDING_NEAR_MISS_FORWARD_604_SITES,
    TestMamariILeftover076071Previous604Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_700_scoreboard import (
    GRAM3_BACKWARD as CYCLE191_GRAM3_BACKWARD,
    STANDING_MATCHING_SITES as CYCLE191_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_700_076_071 as CYCLE191_N_WITH,
    STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
    STANDING_NEAR_MISS_LEFTOVER_700_604_SITE,
    TestMamariILeftover076071Previous700Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE190_N_DISTINCT,
    STANDING_N_NO_BACKWARD as CYCLE190_N_NO_BACKWARD,
    STANDING_N_WITH_BACKWARD as CYCLE190_N_WITH_BACKWARD,
    site_previous_4gram,
    TestMamariILeftover076071PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    GRAM2 as CYCLE170_GRAM2,
    NEAR_MISS_071_065_071_999,
    NEAR_MISS_700_076_076_053,
    TestMamariILeftoverN4076071Scoreboard,
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

HYPOTHESIS_I_ONLY = True
GRAM3 = GRAM3_BACKWARD
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_I_HITS = 2
STANDING_IA_HITS = 2
STANDING_IB_HITS = 0
STANDING_N_ON_I = 2
STANDING_N_I = 2
STANDING_I_SITES = (
    (SIDE_IA, "Ia6", 116),
    (SIDE_IA, "Ia12", 5),
)
STANDING_LEFTOVER_MATCHING_SITES = CYCLE200_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_COUNT = 2
STANDING_LEFTOVER_MATCHING_3GRAM_SITES = (
    (SIDE_IA, "Ia6", 116),
    (SIDE_IA, "Ia12", 5),
)
STANDING_LEFTOVER_34_SITES = CYCLE200_MATCHING_SITES
STANDING_LEFTOVER_34_COUNT = 2
STANDING_INSIDE_FAMILY_SITES = ()
STANDING_INSIDE_FAMILY_COUNT = 0
STANDING_INSIDE_FAMILY_3GRAM_SITES = ()
STANDING_INSIDE_FAMILY_PREVIOUS_4GRAMS = ()
STANDING_INSIDE_FAMILY_SITE_INCLUDED = False
STANDING_EXTRA_I_SITES = ()
STANDING_EXTRA_I_COUNT = 0
STANDING_I_PREVIOUS_4GRAMS = (
    ("430", "099", "076", "071"),
    ("019", "099", "076", "071"),
)
STANDING_I_SITE_ROWS = (
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia6",
        "index": 116,
        "previous_4gram": ("430", "099", "076", "071"),
        "leftover_076_071_site": (SIDE_IA, "Ia6", 117),
        "in_cycle200_leftover_2": True,
        "in_cycle197_leftover_2": False,
        "in_cycle194_leftover_3": False,
        "in_cycle191_leftover_3": False,
        "in_cycle172_leftover_34": True,
        "inside_family": False,
        "inside_leftover_n4_maximal": False,
        "role": "leftover",
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia12",
        "index": 5,
        "previous_4gram": ("019", "099", "076", "071"),
        "leftover_076_071_site": (SIDE_IA, "Ia12", 6),
        "in_cycle200_leftover_2": True,
        "in_cycle197_leftover_2": False,
        "in_cycle194_leftover_3": False,
        "in_cycle191_leftover_3": False,
        "in_cycle172_leftover_34": True,
        "inside_family": False,
        "inside_leftover_n4_maximal": False,
        "role": "leftover",
    },
)
STANDING_IB_SITES = ()
STANDING_OFF_I_HITS = 0
STANDING_N_OFF_I = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_NEAR_MISS_099_076_NOT_071_SITES = (
    (SIDE_IA, "Ia2", 99),
    (SIDE_IA, "Ia5", 45),
    (SIDE_IA, "Ia5", 60),
    (SIDE_IA, "Ia7", 93),
    (SIDE_IA, "Ia13", 179),
)
STANDING_NEAR_MISS_099_076_NOT_071_NEXT = (
    ("099", "076", "724"),
    ("099", "076", "522"),
    ("099", "076", "070"),
    ("099", "076", "532"),
    ("099", "076", "530"),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_3gram_099_076_071_i_only"
STANDING_I_3GRAM_099_076_071_I_ONLY = True
STANDING_RESULT = "i_3gram_099_076_071_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE141_3GRAM = False
STANDING_SAME_AS_CYCLE160_3GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE171_2GRAM = False
STANDING_SAME_AS_CYCLE174_3GRAM = False
STANDING_SAME_AS_CYCLE177_3GRAM = False
STANDING_SAME_AS_CYCLE180_3GRAM = False
STANDING_SAME_AS_CYCLE183_3GRAM = False
STANDING_SAME_AS_CYCLE186_3GRAM = False
STANDING_SAME_AS_CYCLE191 = False
STANDING_SAME_AS_CYCLE192 = False
STANDING_SAME_AS_CYCLE194 = False
STANDING_SAME_AS_CYCLE195 = False
STANDING_SAME_AS_CYCLE197 = False
STANDING_SAME_AS_CYCLE198 = False
STANDING_SAME_AS_CYCLE200 = False
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_NEAR_MISS_090_700_DOES_NOT_COUNT = True
STANDING_NEAR_MISS_700_604_DOES_NOT_COUNT = True
STANDING_NEAR_MISS_099_076_NOT_071_DOES_NOT_COUNT = True
STANDING_CYCLE191_PREVIOUS_700_DOES_NOT_COUNT = True
STANDING_CYCLE194_PREVIOUS_090_DOES_NOT_COUNT = True
STANDING_CYCLE197_PREVIOUS_604_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_SITES_CHECKED = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_DISJOINT_FROM_CYCLE197_LEFTOVER_2 = True
STANDING_DISJOINT_FROM_CYCLE194_LEFTOVER_3 = True
STANDING_DISJOINT_FROM_CYCLE191_LEFTOVER_3 = True
STANDING_N_NO_BACKWARD = 0


def leftover_076_071_site_for_3gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """076 071 start one token after 099 076 071."""
    side, line, index = site
    return (side, line, index + 1)


def site_previous_4gram_for_3gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """W 099 076 071 if a previous stem exists; None at start-of-line."""
    if tuple(stems[index : index + len(gram3)]) != gram3:
        return None
    if index < 1:
        return None
    return tuple(stems[index - 1 : index + len(gram3)])


def i_3gram_099_076_071_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


def i_site_row_as_survey(row: dict) -> dict:
    """JSON-ready site row (lists, not tuples)."""
    return {
        "tablet": row["tablet"],
        "side": row["side"],
        "line": row["line"],
        "index": row["index"],
        "previous_4gram": list(row["previous_4gram"]),
        "leftover_076_071_site": list(row["leftover_076_071_site"]),
        "in_cycle200_leftover_2": row["in_cycle200_leftover_2"],
        "in_cycle197_leftover_2": row["in_cycle197_leftover_2"],
        "in_cycle194_leftover_3": row["in_cycle194_leftover_3"],
        "in_cycle191_leftover_3": row["in_cycle191_leftover_3"],
        "in_cycle172_leftover_34": row["in_cycle172_leftover_34"],
        "inside_family": row["inside_family"],
        "inside_leftover_n4_maximal": row["inside_leftover_n4_maximal"],
        "role": row["role"],
    }


class TestI3gram099076071IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-200 leftover previous 3-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. 071 999 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("099", "076", "071"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["099", "076", "071", "076", "071"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 1)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_071_065_071_999)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["071", "999"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "076"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "071"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["700", "076", "071"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "071"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["604", "076", "071"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["099", "076", "724"]], GRAM3), 0)
        self.assertEqual(
            ngram_hit_count(
                [list(STANDING_NEAR_MISS_CYCLE191_090_700_PREVIOUS_4GRAM)],
                GRAM3,
            ),
            0,
        )
        self.assertEqual(
            ngram_hit_count(
                [list(STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM)],
                GRAM3,
            ),
            0,
        )
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_NEAR_MISS_090_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_NEAR_MISS_700_604_DOES_NOT_COUNT)
        self.assertTrue(STANDING_NEAR_MISS_099_076_NOT_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE191_PREVIOUS_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE194_PREVIOUS_090_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE197_PREVIOUS_604_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_previous_4gram_requires_stem_before_3gram(self):
        """Previous 4-gram is W 099 076 071; start-of-line is none."""
        provider = MockProvider()
        has_prev = ["430", "099", "076", "071", "632"]
        self.assertEqual(
            site_previous_4gram_for_3gram(has_prev, 1, GRAM3),
            ("430", "099", "076", "071"),
        )
        start_of_line = ["099", "076", "071", "632"]
        self.assertIsNone(site_previous_4gram_for_3gram(start_of_line, 0, GRAM3))
        mismatch = ["099", "076", "070"]
        self.assertIsNone(site_previous_4gram_for_3gram(mismatch, 0, GRAM3))
        near_miss = list(STANDING_NEAR_MISS_CYCLE191_090_700_PREVIOUS_4GRAM)
        self.assertIsNone(site_previous_4gram_for_3gram(near_miss, 1, GRAM3))
        cycle191_near = list(STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM)
        self.assertIsNone(site_previous_4gram_for_3gram(cycle191_near, 1, GRAM3))
        self.assertEqual(
            leftover_076_071_site_for_3gram((SIDE_IA, "Ia6", 116)),
            (SIDE_IA, "Ia6", 117),
        )
        self.assertEqual(
            leftover_076_071_site_for_3gram((SIDE_IA, "Ia12", 5)),
            (SIDE_IA, "Ia12", 6),
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0."""
        provider = MockProvider()
        self.assertTrue(i_3gram_099_076_071_i_only(1, 0))
        self.assertTrue(i_3gram_099_076_071_i_only(2, 0))
        self.assertFalse(i_3gram_099_076_071_i_only(1, 1))
        self.assertFalse(i_3gram_099_076_071_i_only(0, 0))
        self.assertFalse(i_3gram_099_076_071_i_only(0, 2))
        self.assertFalse(i_3gram_099_076_071_i_only(2, 1))
        self.assertEqual(STANDING_CLAIM, "i_3gram_099_076_071_i_only")
        self.assertTrue(STANDING_I_3GRAM_099_076_071_I_ONLY)
        self.assertEqual(
            STANDING_I_3GRAM_099_076_071_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_cycle200_leftover_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-200 leftover previous run, not 071 999, 076 076, or the priors."""
        provider = MockProvider()
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3[1:], CYCLE171_GRAM2)
        self.assertEqual(GRAM3[1:], CYCLE170_GRAM2)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, CYCLE191_GRAM3_BACKWARD)
        self.assertNotEqual(GRAM3, CYCLE192_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE194_GRAM3_BACKWARD)
        self.assertNotEqual(GRAM3, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE197_GRAM3_BACKWARD)
        self.assertNotEqual(GRAM3, CYCLE198_GRAM3)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE141_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE160_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE174_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE177_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE180_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE183_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE186_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE191)
        self.assertFalse(STANDING_SAME_AS_CYCLE192)
        self.assertFalse(STANDING_SAME_AS_CYCLE194)
        self.assertFalse(STANDING_SAME_AS_CYCLE195)
        self.assertFalse(STANDING_SAME_AS_CYCLE197)
        self.assertFalse(STANDING_SAME_AS_CYCLE198)
        self.assertFalse(STANDING_SAME_AS_CYCLE200)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        self.assertLess(len(GRAM3), 8)
        for leftover in CYCLE200_MATCHING_PREVIOUS_4GRAMS:
            self.assertTrue(is_contiguous_substring(GRAM3, leftover))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_071_065_071_999))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_700_076_076_053))
        self.assertFalse(
            is_contiguous_substring(
                GRAM3,
                STANDING_NEAR_MISS_CYCLE191_090_700_PREVIOUS_4GRAM,
            )
        )
        self.assertFalse(
            is_contiguous_substring(
                GRAM3,
                STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
            )
        )
        for nxt in STANDING_NEAR_MISS_FORWARD_604_NEXT_4GRAMS:
            self.assertFalse(is_contiguous_substring(GRAM3, nxt))
        for nxt in STANDING_NEAR_MISS_099_076_NOT_071_NEXT:
            self.assertFalse(is_contiguous_substring(GRAM3, nxt))
        self.assertTrue(is_contiguous_substring(("071", "999"), NEAR_MISS_071_065_071_999))
        self.assertTrue(is_contiguous_substring(("076", "076"), NEAR_MISS_700_076_076_053))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram099076071IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 3-gram 099 076 071 off-I lock. Mock only."""

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
        self.claim_holds = i_3gram_099_076_071_i_only(
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
        self.leftover_076_071_sites = tuple(
            leftover_076_071_site_for_3gram(site) for site in self.i_sites
        )

    def test_tokens_are_cycle_200_leftover_not_retuned(self):
        """3-gram is the cycle-200 leftover previous lock, not a new inventory."""
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3, ("099", "076", "071"))
        prior_200 = self.survey["i_leftover_076_071_previous_099"]
        self.assertEqual(prior_200["cycle"], 200)
        self.assertEqual(tuple(prior_200["backward_3gram"]), GRAM3)
        self.assertEqual(prior_200["N_with_previous_099_076_071"], 2)
        self.assertEqual(prior_200["N_without"], 32)
        self.assertEqual(prior_200["N_leftover"], 34)
        self.assertEqual(prior_200["N_no_backward"], 0)
        measured_matching = [list(site) for site in CYCLE200_MATCHING_SITES]
        self.assertEqual(
            [list(site) for site in prior_200["matching_leftover_sites"]],
            measured_matching,
        )
        self.assertTrue(prior_200["i_leftover_076_071_exactly_2_previous_099_076_071"])
        self.assertTrue(prior_200["071_999_does_not_count"])
        self.assertTrue(prior_200["076_076_does_not_count"])
        self.assertTrue(prior_200["inside_family_does_not_count"])
        self.assertTrue(prior_200["disjoint_from_cycle191_leftover_3"])
        self.assertTrue(prior_200["disjoint_from_cycle194_leftover_3"])
        self.assertTrue(prior_200["disjoint_from_cycle197_leftover_2"])
        prior_197 = self.survey["i_leftover_076_071_previous_604"]
        self.assertEqual(prior_197["cycle"], 197)
        self.assertEqual(prior_197["N_with_previous_604_076_071"], 2)
        self.assertEqual(prior_197["N_without"], 32)
        self.assertEqual(prior_197["N_leftover"], 34)
        self.assertTrue(prior_197["i_leftover_076_071_exactly_2_previous_604_076_071"])
        prior_194 = self.survey["i_leftover_076_071_previous_090"]
        self.assertEqual(prior_194["cycle"], 194)
        self.assertEqual(prior_194["N_with_previous_090_076_071"], 3)
        self.assertEqual(prior_194["N_without"], 31)
        self.assertEqual(prior_194["N_leftover"], 34)
        self.assertTrue(prior_194["i_leftover_076_071_exactly_3_previous_090_076_071"])
        prior_191 = self.survey["i_leftover_076_071_previous_700"]
        self.assertEqual(prior_191["cycle"], 191)
        self.assertEqual(prior_191["N_with_previous_700_076_071"], 3)
        self.assertEqual(prior_191["N_without"], 31)
        self.assertEqual(prior_191["N_leftover"], 34)
        self.assertTrue(prior_191["i_leftover_076_071_exactly_3_previous_700_076_071"])
        prior_190 = self.survey["i_leftover_076_071_previous_stem"]
        self.assertEqual(prior_190["cycle"], 190)
        self.assertEqual(prior_190["N_distinct_previous_stems"], 28)
        self.assertFalse(prior_190["i_leftover_076_071_share_one_previous_stem"])
        prior_172 = self.survey["i_2gram_076_071_inside_family"]
        self.assertEqual(prior_172["cycle"], 172)
        self.assertEqual(prior_172["N_leftover"], 34)
        self.assertFalse(prior_172["i_2gram_076_071_all_inside_leftover_n4_family"])
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, CYCLE191_GRAM3_BACKWARD)
        self.assertNotEqual(GRAM3, CYCLE192_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE194_GRAM3_BACKWARD)
        self.assertNotEqual(GRAM3, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE197_GRAM3_BACKWARD)
        self.assertNotEqual(GRAM3, CYCLE198_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(CYCLE200_N_WITH, 2)
        self.assertEqual(CYCLE197_N_WITH, 2)
        self.assertEqual(CYCLE194_N_WITH, 3)
        self.assertEqual(CYCLE191_N_WITH, 3)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_two_on_ia(self):
        """3-gram is 2 on Ia (2 leftover-2/leftover-34, 0 inside-family); Ib 0."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 2)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 2)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 2)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM3, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM3), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        leftover2_in_i = tuple(
            leftover_076_071_site_for_3gram(site)
            for site in STANDING_I_SITES
            if leftover_076_071_site_for_3gram(site) in CYCLE200_MATCHING_SITES
        )
        leftover34_in_i = tuple(
            leftover_076_071_site_for_3gram(site)
            for site in STANDING_I_SITES
            if leftover_076_071_site_for_3gram(site) in STANDING_LEFTOVER_SITES
        )
        inside_in_i = tuple(
            leftover_076_071_site_for_3gram(site)
            for site in STANDING_I_SITES
            if leftover_076_071_site_for_3gram(site) in STANDING_INSIDE_SITES
        )
        extra_in_i = tuple(
            leftover_076_071_site_for_3gram(site)
            for site in STANDING_I_SITES
            if leftover_076_071_site_for_3gram(site) not in CYCLE200_MATCHING_SITES
            and leftover_076_071_site_for_3gram(site) not in STANDING_INSIDE_SITES
        )
        self.assertEqual(leftover2_in_i, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(leftover2_in_i, CYCLE200_MATCHING_SITES)
        self.assertEqual(len(leftover2_in_i), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 2)
        self.assertEqual(leftover34_in_i, STANDING_LEFTOVER_34_SITES)
        self.assertEqual(leftover34_in_i, CYCLE200_MATCHING_SITES)
        self.assertEqual(len(leftover34_in_i), STANDING_LEFTOVER_34_COUNT)
        self.assertEqual(STANDING_LEFTOVER_34_COUNT, 2)
        self.assertEqual(inside_in_i, STANDING_INSIDE_FAMILY_SITES)
        self.assertEqual(len(inside_in_i), STANDING_INSIDE_FAMILY_COUNT)
        self.assertEqual(STANDING_INSIDE_FAMILY_COUNT, 0)
        self.assertFalse(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
        self.assertTrue(STANDING_INSIDE_FAMILY_SITES_CHECKED)
        self.assertEqual(STANDING_INSIDE_FAMILY_PREVIOUS_4GRAMS, ())
        self.assertEqual(STANDING_INSIDE_FAMILY_3GRAM_SITES, ())
        self.assertEqual(extra_in_i, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(extra_in_i), STANDING_EXTRA_I_COUNT)
        self.assertEqual(STANDING_EXTRA_I_COUNT, 0)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), CYCLE172_N_LEFTOVER)
        self.assertEqual(CYCLE172_N_LEFTOVER, 34)
        self.assertEqual(
            tuple(
                leftover_076_071_site_for_3gram(site)
                for site in STANDING_LEFTOVER_MATCHING_3GRAM_SITES
            ),
            CYCLE200_MATCHING_SITES,
        )
        self.assertEqual(self.leftover_076_071_sites, CYCLE200_MATCHING_SITES)
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, STANDING_I_SITES)
            self.assertNotIn(leftover_076_071_site_for_3gram(site), STANDING_I_SITES)
            self.assertNotIn(site, self.leftover_076_071_sites)
        for site in STANDING_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            gram2_site = leftover_076_071_site_for_3gram(site)
            self.assertIn(gram2_site, STANDING_LEFTOVER_SITES)
            self.assertIn(gram2_site, CYCLE200_MATCHING_SITES)
            self.assertNotIn(gram2_site, STANDING_INSIDE_SITES)
            self.assertNotIn(gram2_site, CYCLE191_MATCHING_SITES)
            self.assertNotIn(gram2_site, CYCLE194_MATCHING_SITES)
            self.assertNotIn(gram2_site, CYCLE197_MATCHING_SITES)
        self.assertTrue(STANDING_DISJOINT_FROM_CYCLE191_LEFTOVER_3)
        self.assertTrue(STANDING_DISJOINT_FROM_CYCLE194_LEFTOVER_3)
        self.assertTrue(STANDING_DISJOINT_FROM_CYCLE197_LEFTOVER_2)
        self.assertEqual(
            set(CYCLE200_MATCHING_SITES) & set(CYCLE191_MATCHING_SITES),
            set(),
        )
        self.assertEqual(
            set(CYCLE200_MATCHING_SITES) & set(CYCLE194_MATCHING_SITES),
            set(),
        )
        self.assertEqual(
            set(CYCLE200_MATCHING_SITES) & set(CYCLE197_MATCHING_SITES),
            set(),
        )
        for site in CYCLE191_MATCHING_SITES:
            self.assertNotIn(site, self.leftover_076_071_sites)
        for site in CYCLE194_MATCHING_SITES:
            self.assertNotIn(site, self.leftover_076_071_sites)
        for site in CYCLE197_MATCHING_SITES:
            self.assertNotIn(site, self.leftover_076_071_sites)
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N3]
            self.assertEqual(tuple(stems), GRAM3)
            self.assertEqual(side, SIDE_IA)
        for (side, line, index), prev4 in zip(
            STANDING_I_SITES,
            STANDING_I_PREVIOUS_4GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, (side, line, index))
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N3]), prev4)
            self.assertEqual(prev4[1:], GRAM3)
            self.assertEqual(
                site_previous_4gram_for_3gram(stems, index, GRAM3),
                prev4,
            )
            self.assertEqual(
                site_previous_4gram(stems, index + 1, CYCLE171_GRAM2),
                prev4,
            )
        self.assertEqual(self.previous_4grams, STANDING_I_PREVIOUS_4GRAMS)
        self.assertEqual(self.previous_4grams, CYCLE200_MATCHING_PREVIOUS_4GRAMS)
        self.assertNotIn(None, self.previous_4grams)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia6", 116),
                (SIDE_IA, "Ia12", 5),
            ),
        )
        for row, site, prev4 in zip(
            STANDING_I_SITE_ROWS,
            STANDING_I_SITES,
            STANDING_I_PREVIOUS_4GRAMS,
            strict=True,
        ):
            self.assertEqual((row["side"], row["line"], row["index"]), site)
            self.assertEqual(row["previous_4gram"], prev4)
            self.assertEqual(
                tuple(row["leftover_076_071_site"]),
                leftover_076_071_site_for_3gram(site),
            )
            self.assertTrue(row["in_cycle200_leftover_2"])
            self.assertTrue(row["in_cycle172_leftover_34"])
            self.assertFalse(row["in_cycle197_leftover_2"])
            self.assertFalse(row["in_cycle194_leftover_3"])
            self.assertFalse(row["in_cycle191_leftover_3"])
            self.assertFalse(row["inside_family"])
            self.assertFalse(row["inside_leftover_n4_maximal"])
            self.assertEqual(row["role"], "leftover")
        near_stems = line_stems_for_site(
            self.i_sides,
            STANDING_NEAR_MISS_CYCLE191_090_700_SITE,
        )
        near_index = STANDING_NEAR_MISS_CYCLE191_090_700_SITE[2]
        self.assertEqual(
            site_previous_4gram(near_stems, near_index, CYCLE171_GRAM2),
            STANDING_NEAR_MISS_CYCLE191_090_700_PREVIOUS_4GRAM,
        )
        self.assertNotEqual(
            tuple(near_stems[near_index - 1 : near_index + 2]),
            GRAM3,
        )
        self.assertNotIn(STANDING_NEAR_MISS_CYCLE191_090_700_SITE, STANDING_I_SITES)
        self.assertEqual(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, (SIDE_IA, "Ia9", 10))
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, self.leftover_076_071_sites)
        cycle191_near_stems = line_stems_for_site(
            self.i_sides,
            STANDING_NEAR_MISS_LEFTOVER_700_604_SITE,
        )
        cycle191_near_index = STANDING_NEAR_MISS_LEFTOVER_700_604_SITE[2]
        self.assertEqual(
            site_previous_4gram(
                cycle191_near_stems,
                cycle191_near_index,
                CYCLE171_GRAM2,
            ),
            STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
        )
        self.assertNotEqual(
            tuple(cycle191_near_stems[cycle191_near_index - 1 : cycle191_near_index + 2]),
            GRAM3,
        )
        for site, nxt in zip(
            STANDING_NEAR_MISS_FORWARD_604_SITES,
            STANDING_NEAR_MISS_FORWARD_604_NEXT_4GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N4]), nxt)
            self.assertEqual(nxt[3], "604")
            self.assertEqual(nxt[:2], CYCLE171_GRAM2)
            self.assertNotIn(site, self.leftover_076_071_sites)
            self.assertNotEqual(
                tuple(stems[index - 1 : index + 2]) if index >= 1 else (),
                GRAM3,
            )
        for site, nxt in zip(
            STANDING_NEAR_MISS_099_076_NOT_071_SITES,
            STANDING_NEAR_MISS_099_076_NOT_071_NEXT,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + 3]), nxt)
            self.assertEqual(nxt[:2], ("099", "076"))
            self.assertNotEqual(nxt[2], "071")
            self.assertNotIn(site, STANDING_I_SITES)
            self.assertNotEqual(tuple(stems[index : index + 3]), GRAM3)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        if self.i_hits != 2:
            self.fail("measured N_I drifted from 2")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_zero_off_i_and_i_only(self):
        """3-gram is 0 on A–H and J–V. Ia has exactly 2. W is not a tablet."""
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
        self.assertEqual(STANDING_OFF_I_SITES, ())
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM3))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 2)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(
            i_3gram_099_076_071_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_3GRAM_099_076_071_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_099_076_071_I_ONLY,
        )
        self.assertTrue(STANDING_I_3GRAM_099_076_071_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_3gram_099_076_071_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE141_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE160_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE174_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE177_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE180_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE183_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE186_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE191)
        self.assertFalse(STANDING_SAME_AS_CYCLE192)
        self.assertFalse(STANDING_SAME_AS_CYCLE194)
        self.assertFalse(STANDING_SAME_AS_CYCLE195)
        self.assertFalse(STANDING_SAME_AS_CYCLE197)
        self.assertFalse(STANDING_SAME_AS_CYCLE198)
        self.assertFalse(STANDING_SAME_AS_CYCLE200)
        if self.off_i_hits != 0:
            self.fail("measured N_off_I drifted from 0")
        if self.i_hits != STANDING_N_I:
            self.fail("measured N_I drifted from the locked count")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_200_197_194_191_172_171_scoreboards_still_compute(self):
        """Cycle 200 leftover-2, 197 leftover-2, 194 leftover-3, 191 leftover-3, 172 leftover-34, and 171 I-only 43/0 stay."""
        prior_200 = TestMamariILeftover076071Previous099Scoreboard()
        prior_200.setUp()
        prior_200.test_counts_2_of_34_and_hypothesis_n_2_holds()
        prior_200.test_survey_matches_computed_lock()
        self.assertEqual(prior_200.n_with, 2)
        self.assertEqual(prior_200.n_leftover, 34)
        self.assertEqual(CYCLE200_N_WITH, 2)
        self.assertEqual(prior_200.with_sites, CYCLE200_MATCHING_SITES)
        prior_197 = TestMamariILeftover076071Previous604Scoreboard()
        prior_197.setUp()
        prior_197.test_counts_2_of_34_and_hypothesis_n_2_holds()
        prior_197.test_survey_matches_computed_lock()
        self.assertEqual(prior_197.n_with, 2)
        self.assertEqual(prior_197.n_leftover, 34)
        self.assertEqual(CYCLE197_N_WITH, 2)
        self.assertEqual(prior_197.with_sites, CYCLE197_MATCHING_SITES)
        self.assertEqual(
            set(prior_200.with_sites) & set(prior_197.with_sites),
            set(),
        )
        prior_194 = TestMamariILeftover076071Previous090Scoreboard()
        prior_194.setUp()
        prior_194.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_194.test_survey_matches_computed_lock()
        self.assertEqual(prior_194.n_with, 3)
        self.assertEqual(prior_194.n_leftover, 34)
        self.assertEqual(CYCLE194_N_WITH, 3)
        self.assertEqual(prior_194.with_sites, CYCLE194_MATCHING_SITES)
        self.assertEqual(
            set(prior_200.with_sites) & set(prior_194.with_sites),
            set(),
        )
        prior_191 = TestMamariILeftover076071Previous700Scoreboard()
        prior_191.setUp()
        prior_191.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_191.test_survey_matches_computed_lock()
        self.assertEqual(prior_191.n_with, 3)
        self.assertEqual(prior_191.n_leftover, 34)
        self.assertEqual(CYCLE191_N_WITH, 3)
        self.assertEqual(prior_191.with_sites, CYCLE191_MATCHING_SITES)
        self.assertEqual(
            set(prior_200.with_sites) & set(prior_191.with_sites),
            set(),
        )
        prior_172 = TestMamariI2gram076071InsideFamilyScoreboard()
        prior_172.setUp()
        prior_172.test_forty_three_sites_split_9_inside_34_leftover_and_claim_loses()
        prior_172.test_survey_matches_computed_lock()
        self.assertEqual(prior_172.n_leftover, 34)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(len(prior_171.i_sites), 43)
        self.assertEqual(prior_171.i_sites, CYCLE171_I_SITES)
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_198 = TestMamariI3gram604076071IOnlyScoreboard()
        prior_198.setUp()
        prior_198.test_3gram_is_zero_off_i_and_i_only()
        prior_198.test_survey_matches_computed_lock()
        prior_195 = TestMamariI3gram090076071IOnlyScoreboard()
        prior_195.setUp()
        prior_195.test_3gram_is_zero_off_i_and_i_only()
        prior_195.test_survey_matches_computed_lock()
        prior_192 = TestMamariI3gram700076071IOnlyScoreboard()
        prior_192.setUp()
        prior_192.test_3gram_is_zero_off_i_and_i_only()
        prior_192.test_survey_matches_computed_lock()
        prior_190 = TestMamariILeftover076071PreviousStemScoreboard()
        prior_190.setUp()
        prior_190.test_counts_28_distinct_previous_stems_and_claim_loses()
        prior_190.test_survey_matches_computed_lock()
        self.assertEqual(prior_190.n_distinct, 28)
        self.assertEqual(prior_190.n_leftover, 34)
        self.assertEqual(CYCLE190_N_DISTINCT, 28)
        self.assertEqual(CYCLE190_N_WITH_BACKWARD, 34)
        self.assertEqual(CYCLE190_N_NO_BACKWARD, 0)
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-201 3-gram I-only lock."""
        lock = self.survey["i_3gram_099_076_071_i_only"]
        self.assertEqual(lock["cycle"], 201)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 2)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            [list(gram) for gram in STANDING_I_PREVIOUS_4GRAMS],
            lock["i_previous_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(lock["leftover_matching_count"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_3gram_sites"]),
            STANDING_LEFTOVER_MATCHING_3GRAM_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_34_sites"]),
            STANDING_LEFTOVER_34_SITES,
        )
        self.assertEqual(lock["leftover_34_count"], STANDING_LEFTOVER_34_COUNT)
        self.assertEqual(lock["leftover_34_count"], 2)
        self.assertEqual(lock["inside_family_sites"], [])
        self.assertEqual(lock["inside_family_count"], STANDING_INSIDE_FAMILY_COUNT)
        self.assertEqual(lock["inside_family_count"], 0)
        self.assertFalse(lock["inside_family_site_included"])
        self.assertTrue(lock["inside_family_sites_checked"])
        self.assertEqual(lock["inside_family_3gram_sites"], [])
        self.assertEqual(lock["inside_family_previous_4grams"], [])
        self.assertEqual(lock["extra_i_sites"], [])
        self.assertEqual(lock["extra_i_count"], 0)
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
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(
            tuple(lock["near_miss_cycle191_090_700_site"]),
            STANDING_NEAR_MISS_CYCLE191_090_700_SITE,
        )
        self.assertEqual(
            tuple(lock["near_miss_cycle191_090_700_previous_4gram"]),
            STANDING_NEAR_MISS_CYCLE191_090_700_PREVIOUS_4GRAM,
        )
        self.assertEqual(
            [list(site) for site in STANDING_NEAR_MISS_FORWARD_604_SITES],
            lock["near_miss_forward_604_sites"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_NEAR_MISS_FORWARD_604_NEXT_4GRAMS],
            lock["near_miss_forward_604_next_4grams"],
        )
        self.assertEqual(
            tuple(lock["cycle191_near_miss_700_604_site"]),
            STANDING_NEAR_MISS_LEFTOVER_700_604_SITE,
        )
        self.assertEqual(
            tuple(lock["cycle191_near_miss_700_604_previous_4gram"]),
            STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
        )
        self.assertEqual(
            [list(site) for site in STANDING_NEAR_MISS_099_076_NOT_071_SITES],
            lock["near_miss_099_076_not_071_sites"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_NEAR_MISS_099_076_NOT_071_NEXT],
            lock["near_miss_099_076_not_071_next"],
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_3gram_099_076_071_i_only"])
        self.assertEqual(
            lock["i_3gram_099_076_071_i_only"],
            STANDING_I_3GRAM_099_076_071_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle141_3gram"])
        self.assertFalse(lock["same_as_cycle160_3gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle171_2gram"])
        self.assertFalse(lock["same_as_cycle174_3gram"])
        self.assertFalse(lock["same_as_cycle177_3gram"])
        self.assertFalse(lock["same_as_cycle180_3gram"])
        self.assertFalse(lock["same_as_cycle183_3gram"])
        self.assertFalse(lock["same_as_cycle186_3gram"])
        self.assertFalse(lock["same_as_cycle191"])
        self.assertFalse(lock["same_as_cycle192"])
        self.assertFalse(lock["same_as_cycle194"])
        self.assertFalse(lock["same_as_cycle195"])
        self.assertFalse(lock["same_as_cycle197"])
        self.assertFalse(lock["same_as_cycle198"])
        self.assertFalse(lock["same_as_cycle200"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["near_miss_090_700_does_not_count"])
        self.assertTrue(lock["near_miss_700_604_does_not_count"])
        self.assertTrue(lock["near_miss_099_076_not_071_does_not_count"])
        self.assertTrue(lock["cycle191_previous_700_does_not_count"])
        self.assertTrue(lock["cycle194_previous_090_does_not_count"])
        self.assertTrue(lock["cycle197_previous_604_does_not_count"])
        self.assertTrue(lock["disjoint_from_cycle191_leftover_3"])
        self.assertTrue(lock["disjoint_from_cycle194_leftover_3"])
        self.assertTrue(lock["disjoint_from_cycle197_leftover_2"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_099_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_604_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_090_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_700_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_604_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_700_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_076_071_previous_099"]["cycle"], 200)
        self.assertTrue(
            self.survey["i_leftover_076_071_previous_099"][
                "i_leftover_076_071_exactly_2_previous_099_076_071"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_099"]["N_with_previous_099_076_071"],
            2,
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_099"]["N_without"], 32)
        self.assertEqual(self.survey["i_leftover_076_071_previous_099"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_leftover_076_071_previous_604"]["cycle"], 197)
        self.assertTrue(
            self.survey["i_leftover_076_071_previous_604"][
                "i_leftover_076_071_exactly_2_previous_604_076_071"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_604"]["N_with_previous_604_076_071"],
            2,
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_604"]["N_without"], 32)
        self.assertEqual(self.survey["i_leftover_076_071_previous_604"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_leftover_076_071_previous_090"]["cycle"], 194)
        self.assertTrue(
            self.survey["i_leftover_076_071_previous_090"][
                "i_leftover_076_071_exactly_3_previous_090_076_071"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_090"]["N_with_previous_090_076_071"],
            3,
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_090"]["N_without"], 31)
        self.assertEqual(self.survey["i_leftover_076_071_previous_090"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_leftover_076_071_previous_700"]["cycle"], 191)
        self.assertTrue(
            self.survey["i_leftover_076_071_previous_700"][
                "i_leftover_076_071_exactly_3_previous_700_076_071"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_700"]["N_with_previous_700_076_071"],
            3,
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_700"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_leftover_076_071_previous_stem"]["cycle"], 190)
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_stem"]["N_distinct_previous_stems"],
            28,
        )
        self.assertFalse(
            self.survey["i_leftover_076_071_previous_stem"][
                "i_leftover_076_071_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["cycle"], 172)
        self.assertFalse(
            self.survey["i_2gram_076_071_inside_family"][
                "i_2gram_076_071_all_inside_leftover_n4_family"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["N_inside"], 9)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_604_076_071_i_only"]["cycle"], 198)
        self.assertTrue(
            self.survey["i_3gram_604_076_071_i_only"]["i_3gram_604_076_071_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_604_076_071_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_604_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["cycle"], 195)
        self.assertTrue(
            self.survey["i_3gram_090_076_071_i_only"]["i_3gram_090_076_071_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_700_076_071_i_only"]["cycle"], 192)
        self.assertTrue(
            self.survey["i_3gram_700_076_071_i_only"]["i_3gram_700_076_071_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_700_076_071_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_700_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"][
                "i_leftover_n4_exactly_4_contain_076_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["N_with_076_071"], 4)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_n"], 5)
        self.assertEqual(self.survey["n_repeating_nge5"]["cycle"], 134)
        self.assertTrue(self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"])
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"], 5)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI3gram099076071IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 201 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
