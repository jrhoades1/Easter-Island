"""I's cycle-211 leftover 3-gram 720 076 070 off-I lock.

Cycle 212 text-search lock. Uses already-vendored A–V and the
cycle-211 leftover previous 3-gram 720 076 070 (the n=3 run
shared by leftover I 076 070 sites Ia7[63] 069 720 076 070,
Ia8[172] 053 720 076 070, and Ia9[120] 999 720 076 070).
Does not retune that 3-gram, those leftover sites, the
cycle-207 8 I 090 076 070 sites, or the leftover n=4 set.
Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not
redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 192 (700 076 071 was I-only 3/0)
and cycle 207 (090 076 070 I-only lost 8/1). Cycle 211 holds:
leftover I 076 070 exactly 3 share previous 720 076 070
(N_share=3, N_leftover=11). Cycle 210 lost: leftover 076 070
share-one-previous-stem (11 leftover, 9 distinct). Cycle 206
lost: 076 070 is not I-only (19/5). Cycle 171 holds: 076 071
is I-only (43/0). This cycle is the new leftover previous
3-gram 720 076 070 only. Leftover = I 076 070 sites that are
NOT 090 076 070. 720 076 071 is a different 3-gram. 090 076 070
is a different 3-gram (already lost 8/1). 700 076 071 is a
different 3-gram. Do not retune 076 070, 090 076 070,
720 076 071, 700 076 071, or the leftover n=4 set. Do not
assume the I-only result.

Locks exact consecutive hits of 720 076 070 on tablet I and
on every other vendored tablet A–H and J–V. Claim that can
lose: i_3gram_720_076_070_i_only (I hits ≥ 1 and off-I hits
== 0). True only if N_off_I == 0. Measured: Ia is exactly 3
at Ia7[62]/Ia8[171]/Ia9[119] (all leftover; extra=0); Ib
unpublished 0; every other vendored tablet is exact-0. The
claim is true. Not an n≥8 island. Not the cycle-103 I 5-gram.

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
from tests.test_mamari_i_2gram_076_070_i_only_scoreboard import (
    GRAM2 as CYCLE206_GRAM2,
    STANDING_N_I as CYCLE206_N_I,
    STANDING_N_OFF_I as CYCLE206_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE206_OFF_I_SITES,
    TestMamariI2gram076070IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_700_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE192_GRAM3,
    STANDING_I_3GRAM_700_076_071_I_ONLY as CYCLE192_I_ONLY,
    STANDING_N_I as CYCLE192_N_I,
    STANDING_N_OFF_I as CYCLE192_N_OFF_I,
    TestMamariI3gram700076071IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_previous_720_scoreboard import (
    GRAM3_BACKWARD,
    STANDING_I_LEFTOVER_076_070_PREVIOUS_720 as CYCLE211_CLAIM,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE211_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE211_MATCHING_SITES,
    STANDING_N_LEFTOVER as CYCLE211_N_LEFTOVER,
    STANDING_N_SHARE as CYCLE211_N_SHARE,
    STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
    STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
    TestMamariILeftover076070Previous720Scoreboard,
)
from tests.test_mamari_i_leftover_076_070_previous_stem_scoreboard import (
    STANDING_LEFTOVER_SITES,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE210_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE210_N_LEFTOVER,
    STANDING_PREFIXED_I_SITES,
    TestMamariILeftover076070PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    GRAM2 as CYCLE205_GRAM2,
    NEAR_MISS_700_076_076_053,
    NEAR_MISS_999_090_076_071,
    STANDING_MATCHING_LEFTOVERS as CYCLE205_MATCHING_LEFTOVERS,
    TestMamariILeftoverN4076070Scoreboard,
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
    load_g_k_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    load_s_sides,
)

HYPOTHESIS_I_ONLY = True
GRAM3 = GRAM3_BACKWARD
NEAR_MISS_720_076_071 = ("720", "076", "071")
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_700_076_071 = CYCLE192_GRAM3
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_I_HITS = 3
STANDING_IA_HITS = 3
STANDING_IB_HITS = 0
STANDING_N_ON_I = 3
STANDING_N_I = 3
STANDING_I_SITES = (
    (SIDE_IA, "Ia7", 62),
    (SIDE_IA, "Ia8", 171),
    (SIDE_IA, "Ia9", 119),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_076_070_SITES = CYCLE211_MATCHING_SITES
STANDING_N_LEFTOVER_076_070 = CYCLE211_N_LEFTOVER
STANDING_LEFTOVER_3GRAM_SITES = (
    (SIDE_IA, "Ia7", 62),
    (SIDE_IA, "Ia8", 171),
    (SIDE_IA, "Ia9", 119),
)
STANDING_N_LEFTOVER = 3
STANDING_EXTRA_I_SITES = ()
STANDING_N_EXTRA = 0
STANDING_I_PREVIOUS_4GRAMS = (
    ("069", "720", "076", "070"),
    ("053", "720", "076", "070"),
    ("999", "720", "076", "070"),
)
STANDING_I_SITE_ROWS = (
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia7",
        "index": 62,
        "previous_4gram": ("069", "720", "076", "070"),
        "leftover_076_070_site": (SIDE_IA, "Ia7", 63),
        "in_cycle211_leftover_3": True,
        "in_cycle210_leftover_11": True,
        "prefixed_090_076_070": False,
        "inside_leftover_n4_maximal": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia8",
        "index": 171,
        "previous_4gram": ("053", "720", "076", "070"),
        "leftover_076_070_site": (SIDE_IA, "Ia8", 172),
        "in_cycle211_leftover_3": True,
        "in_cycle210_leftover_11": True,
        "prefixed_090_076_070": False,
        "inside_leftover_n4_maximal": False,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia9",
        "index": 119,
        "previous_4gram": ("999", "720", "076", "070"),
        "leftover_076_070_site": (SIDE_IA, "Ia9", 120),
        "in_cycle211_leftover_3": True,
        "in_cycle210_leftover_11": True,
        "prefixed_090_076_070": False,
        "inside_leftover_n4_maximal": False,
    },
)
STANDING_OFF_I_HITS = 0
STANDING_N_OFF_I = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_OFF_I_BY_TABLET_NONZERO = {}
STANDING_OFF_I_BY_TABLET = tuple(
    STANDING_OFF_I_BY_TABLET_NONZERO.get(tablet, 0) for tablet in OFF_I_TABLETS
)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_3gram_720_076_070_i_only"
STANDING_I_3GRAM_720_076_070_I_ONLY = True
STANDING_RESULT = "i_3gram_720_076_070_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE192_3GRAM = False
STANDING_SAME_AS_CYCLE207_3GRAM = False
STANDING_SAME_AS_CYCLE206_2GRAM = False
STANDING_SAME_AS_CYCLE171_2GRAM = False
STANDING_SAME_AS_CYCLE211 = False
STANDING_720_076_071_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_700_076_071_DOES_NOT_COUNT = True
STANDING_076_070_WITHOUT_720_DOES_NOT_COUNT = True
STANDING_PREFIXED_090_DOES_NOT_COUNT = True
STANDING_NEAR_MISS_090_099_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def leftover_076_070_site_for_3gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """076 070 starts one token after 720 076 070."""
    side, line, index = site
    return (side, line, index + 1)


def leftover_3gram_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_076_070: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 720 076 070 sites whose 076 070 is leftover (not 090 076 070)."""
    leftover_set = set(leftover_076_070)
    return tuple(
        site
        for site in i_sites
        if leftover_076_070_site_for_3gram(site) in leftover_set
    )


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_076_070: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 720 076 070 sites that are not leftover I 076 070."""
    leftover_set = set(leftover_076_070)
    return tuple(
        site
        for site in i_sites
        if leftover_076_070_site_for_3gram(site) not in leftover_set
    )


def site_previous_4gram_for_3gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """W 720 076 070 if a previous stem exists; None at start-of-line."""
    if tuple(stems[index : index + len(gram3)]) != gram3:
        return None
    if index < 1:
        return None
    return tuple(stems[index - 1 : index + len(gram3)])


def i_3gram_720_076_070_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
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
        "leftover_076_070_site": list(row["leftover_076_070_site"]),
        "in_cycle211_leftover_3": row["in_cycle211_leftover_3"],
        "in_cycle210_leftover_11": row["in_cycle210_leftover_11"],
        "prefixed_090_076_070": row["prefixed_090_076_070"],
        "inside_leftover_n4_maximal": row["inside_leftover_n4_maximal"],
    }


class TestI3gram720076070IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-211 leftover previous 3-gram tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. 720 076 071 / 090 076 070 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("720", "076", "070"))
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["720", "076", "070", "720", "076", "070"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 2)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_720_076_071)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_071)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_071)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "070"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["720", "076", "071"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "070"]], GRAM3), 0)
        self.assertTrue(STANDING_720_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_700_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_WITHOUT_720_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_previous_4gram_requires_stem_before_3gram(self):
        """Previous 4-gram is W 720 076 070; start-of-line is none."""
        provider = MockProvider()
        has_prev = ["069", "720", "076", "070", "720", "076"]
        self.assertEqual(
            site_previous_4gram_for_3gram(has_prev, 1, GRAM3),
            ("069", "720", "076", "070"),
        )
        start_of_line = ["720", "076", "070", "010"]
        self.assertIsNone(site_previous_4gram_for_3gram(start_of_line, 0, GRAM3))
        mismatch = ["720", "076", "071"]
        self.assertIsNone(site_previous_4gram_for_3gram(mismatch, 0, GRAM3))
        near_miss = list(STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM)
        self.assertIsNone(site_previous_4gram_for_3gram(near_miss, 1, GRAM3))
        self.assertEqual(
            leftover_076_070_site_for_3gram((SIDE_IA, "Ia7", 62)),
            (SIDE_IA, "Ia7", 63),
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Measured 3/0 holds."""
        provider = MockProvider()
        self.assertTrue(i_3gram_720_076_070_i_only(1, 0))
        self.assertTrue(i_3gram_720_076_070_i_only(3, 0))
        self.assertFalse(i_3gram_720_076_070_i_only(3, 1))
        self.assertFalse(i_3gram_720_076_070_i_only(1, 1))
        self.assertFalse(i_3gram_720_076_070_i_only(0, 0))
        self.assertFalse(i_3gram_720_076_070_i_only(0, 1))
        self.assertEqual(STANDING_CLAIM, "i_3gram_720_076_070_i_only")
        self.assertTrue(STANDING_I_3GRAM_720_076_070_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(
            STANDING_I_3GRAM_720_076_070_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_cycle211_leftover_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-211 leftover previous run, not 720 076 071 or 090 076 070."""
        provider = MockProvider()
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3, ("720", "076", "070"))
        self.assertEqual(GRAM3[1:], CYCLE206_GRAM2)
        self.assertEqual(GRAM3[1:], CYCLE205_GRAM2)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE192_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, CYCLE206_GRAM2)
        self.assertNotEqual(GRAM3, NEAR_MISS_720_076_071)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM3, CYCLE205_MATCHING_LEFTOVERS[0]))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE192_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE211)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        self.assertLess(len(GRAM3), 8)
        for leftover in CYCLE211_MATCHING_PREVIOUS_4GRAMS:
            self.assertTrue(is_contiguous_substring(GRAM3, leftover))
        self.assertFalse(
            is_contiguous_substring(
                GRAM3,
                STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
            )
        )
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_999_090_076_071))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_700_076_076_053))
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_vs_extra_split_can_fail(self):
        """All three I sites are leftover; extra is empty. A planted extra loses."""
        provider = MockProvider()
        leftover = leftover_3gram_sites()
        extra = extra_i_sites()
        self.assertEqual(leftover, STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(leftover), STANDING_N_LEFTOVER)
        self.assertEqual(len(extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER + STANDING_N_EXTRA, STANDING_N_I)
        self.assertEqual(
            tuple(sorted(leftover + extra)),
            tuple(sorted(STANDING_I_SITES)),
        )
        planted_leftover = tuple(
            site
            for site in STANDING_LEFTOVER_SITES
            if site != STANDING_LEFTOVER_076_070_SITES[0]
        )
        planted_extra = extra_i_sites(STANDING_I_SITES, planted_leftover)
        self.assertNotEqual(planted_extra, extra)
        self.assertEqual(len(planted_extra), 1)
        self.assertEqual(planted_extra, (STANDING_I_SITES[0],))
        self.assertTrue(STANDING_PREFIXED_090_DOES_NOT_COUNT)
        self.assertTrue(STANDING_NEAR_MISS_090_099_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram720076070IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 3-gram 720 076 070 off-I lock. Mock only."""

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
        self.leftover = leftover_3gram_sites(self.i_sites, STANDING_LEFTOVER_SITES)
        self.extra = extra_i_sites(self.i_sites, STANDING_LEFTOVER_SITES)
        self.claim_holds = i_3gram_720_076_070_i_only(
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
        self.leftover_076_070_sites = tuple(
            leftover_076_070_site_for_3gram(site) for site in self.i_sites
        )

    def test_tokens_are_cycle_211_leftover_not_retuned(self):
        """3-gram is the cycle-211 leftover previous lock, not a new inventory."""
        self.assertEqual(GRAM3, GRAM3_BACKWARD)
        self.assertEqual(GRAM3, ("720", "076", "070"))
        prior_211 = self.survey["i_leftover_076_070_previous_720"]
        self.assertEqual(prior_211["cycle"], 211)
        self.assertEqual(tuple(prior_211["backward_3gram"]), GRAM3)
        self.assertEqual(prior_211["N_share"], 3)
        self.assertEqual(prior_211["N_leftover"], 11)
        self.assertEqual(prior_211["N_share"], CYCLE211_N_SHARE)
        self.assertEqual(prior_211["N_leftover"], CYCLE211_N_LEFTOVER)
        self.assertEqual(prior_211["N_with_previous_720_076_070"], 3)
        self.assertEqual(prior_211["N_without"], 8)
        self.assertEqual(prior_211["N_no_backward"], 0)
        measured_matching = [list(site) for site in CYCLE211_MATCHING_SITES]
        self.assertEqual(
            [list(site) for site in prior_211["matching_leftover_sites"]],
            measured_matching,
        )
        self.assertTrue(prior_211["i_leftover_076_070_previous_720"])
        self.assertTrue(CYCLE211_CLAIM)
        prior_210 = self.survey["i_leftover_076_070_previous_stem"]
        self.assertEqual(prior_210["cycle"], 210)
        self.assertEqual(prior_210["N_leftover"], 11)
        self.assertEqual(prior_210["N_distinct_previous_stems"], 9)
        self.assertEqual(prior_210["N_distinct_previous_stems"], CYCLE210_N_DISTINCT)
        self.assertFalse(prior_210["i_leftover_076_070_share_one_previous_stem"])
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        prior_206 = self.survey["i_2gram_076_070_i_only"]
        self.assertEqual(prior_206["cycle"], 206)
        self.assertFalse(prior_206["i_2gram_076_070_i_only"])
        self.assertEqual(prior_206["N_I"], 19)
        self.assertEqual(prior_206["N_off_I"], 5)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE192_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, NEAR_MISS_720_076_071)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(CYCLE211_N_SHARE, 3)
        self.assertEqual(CYCLE211_N_LEFTOVER, 11)
        self.assertEqual(CYCLE210_N_LEFTOVER, 11)
        self.assertEqual(CYCLE210_N_DISTINCT, 9)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_three_on_ia_all_leftover(self):
        """3-gram is 3 on Ia (3 leftover, 0 extra); Ib unpublished 0. N_I must not drift."""
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
        self.assertEqual(self.leftover, STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.leftover), STANDING_N_LEFTOVER)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER, 3)
        self.assertEqual(STANDING_N_EXTRA, 0)
        self.assertEqual(STANDING_N_LEFTOVER + STANDING_N_EXTRA, STANDING_N_I)
        self.assertEqual(self.leftover_076_070_sites, CYCLE211_MATCHING_SITES)
        self.assertEqual(self.leftover_076_070_sites, STANDING_LEFTOVER_076_070_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_076_070)
        self.assertEqual(STANDING_N_LEFTOVER_076_070, 11)
        for site in STANDING_PREFIXED_I_SITES:
            self.assertNotIn(site, STANDING_I_SITES)
            self.assertNotIn(leftover_076_070_site_for_3gram(site), STANDING_I_SITES)
        for site in CYCLE207_I_SITES:
            self.assertNotIn(site, STANDING_I_SITES)
        for site in STANDING_I_SITES:
            gram2_site = leftover_076_070_site_for_3gram(site)
            self.assertIn(gram2_site, STANDING_LEFTOVER_SITES)
            self.assertIn(gram2_site, CYCLE211_MATCHING_SITES)
            self.assertNotIn(gram2_site, STANDING_PREFIXED_I_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
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
        self.assertEqual(self.previous_4grams, STANDING_I_PREVIOUS_4GRAMS)
        self.assertEqual(self.previous_4grams, CYCLE211_MATCHING_PREVIOUS_4GRAMS)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia7", 62),
                (SIDE_IA, "Ia8", 171),
                (SIDE_IA, "Ia9", 119),
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
                tuple(row["leftover_076_070_site"]),
                leftover_076_070_site_for_3gram(site),
            )
            self.assertTrue(row["in_cycle211_leftover_3"])
            self.assertTrue(row["in_cycle210_leftover_11"])
            self.assertFalse(row["prefixed_090_076_070"])
            self.assertFalse(row["inside_leftover_n4_maximal"])
        near_stems = line_stems_for_site(
            self.i_sides,
            STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
        )
        near_index = STANDING_NEAR_MISS_LEFTOVER_090_099_SITE[2]
        self.assertEqual(
            tuple(near_stems[near_index - 1 : near_index + 2]),
            ("099", "076", "070"),
        )
        self.assertNotEqual(
            tuple(near_stems[near_index - 1 : near_index + 2]),
            GRAM3,
        )
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_I_SITES)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        if self.i_hits != 3:
            self.fail("measured N_I drifted from 3")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_vs_extra_on_i(self):
        """All three I sites sit on leftover 076 070; extra is empty."""
        self.assertEqual(self.leftover, STANDING_LEFTOVER_3GRAM_SITES)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.leftover), STANDING_N_LEFTOVER)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER, 3)
        self.assertEqual(STANDING_N_EXTRA, 0)
        leftover_set = set(STANDING_LEFTOVER_3GRAM_SITES)
        for site in STANDING_LEFTOVER_3GRAM_SITES:
            self.assertIn(site, STANDING_I_SITES)
            gram2_site = leftover_076_070_site_for_3gram(site)
            self.assertIn(gram2_site, STANDING_LEFTOVER_SITES)
            self.assertIn(gram2_site, CYCLE211_MATCHING_SITES)
        for site in STANDING_EXTRA_I_SITES:
            self.assertIn(site, STANDING_I_SITES)
            self.assertNotIn(site, leftover_set)
        for site in STANDING_PREFIXED_I_SITES:
            self.assertNotIn(site, leftover_set)
            self.assertNotIn(site, STANDING_I_SITES)
        self.assertEqual(len(STANDING_PREFIXED_I_SITES), 8)
        self.assertEqual(len(CYCLE207_I_SITES), 8)
        self.assertTrue(STANDING_PREFIXED_090_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_zero_off_i_and_i_only(self):
        """3-gram is 0 on A–H and J–V. Ia has exactly 3 leftover. Claim holds."""
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
                self.assertEqual(count, 3)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(named_off_i_sites(GRAM3), ())
        self.assertEqual(
            i_3gram_720_076_070_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_3GRAM_720_076_070_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_720_076_070_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_3GRAM_720_076_070_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_3gram_720_076_070_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE192_GRAM3)
        self.assertNotEqual(GRAM3, NEAR_MISS_720_076_071)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE192_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE211)
        for site in CYCLE206_OFF_I_SITES:
            self.assertNotIn(site, STANDING_I_SITES)
            self.assertNotIn(site, STANDING_OFF_I_SITES)
        self.assertEqual(len(CYCLE206_OFF_I_SITES), 5)
        if self.off_i_hits != 0:
            self.fail("measured N_off_I drifted from 0")
        if self.i_hits != STANDING_N_I:
            self.fail("measured N_I drifted from the locked count")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_211_210_207_206_171_scoreboards_still_compute(self):
        """Cycle 211 N_share=3/11, 210 N_distinct=9, 207 8/1, 206 19/5, 171 43/0 stay."""
        prior_211 = TestMamariILeftover076070Previous720Scoreboard()
        prior_211.setUp()
        prior_211.test_counts_3_of_11_and_hypothesis_n_3_holds()
        prior_211.test_survey_matches_computed_lock()
        self.assertEqual(prior_211.n_share, 3)
        self.assertEqual(prior_211.n_leftover, 11)
        self.assertEqual(CYCLE211_N_SHARE, 3)
        self.assertEqual(CYCLE211_N_LEFTOVER, 11)
        self.assertEqual(prior_211.with_sites, CYCLE211_MATCHING_SITES)
        prior_210 = TestMamariILeftover076070PreviousStemScoreboard()
        prior_210.setUp()
        prior_210.test_counts_9_distinct_previous_stems_and_claim_loses()
        prior_210.test_survey_matches_computed_lock()
        self.assertEqual(prior_210.n_distinct, 9)
        self.assertEqual(prior_210.n_leftover, 11)
        self.assertEqual(CYCLE210_N_DISTINCT, 9)
        self.assertEqual(CYCLE210_N_LEFTOVER, 11)
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(CYCLE207_N_OFF_I, 1)
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        self.assertEqual(prior_206.i_hits, 19)
        self.assertEqual(prior_206.off_i_hits, 5)
        self.assertEqual(CYCLE206_N_I, 19)
        self.assertEqual(CYCLE206_N_OFF_I, 5)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_192 = TestMamariI3gram700076071IOnlyScoreboard()
        prior_192.setUp()
        prior_192.test_3gram_is_zero_off_i_and_i_only()
        prior_192.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE192_I_ONLY)
        self.assertEqual(CYCLE192_N_I, 3)
        self.assertEqual(CYCLE192_N_OFF_I, 0)
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-212 3-gram I-only lock."""
        lock = self.survey["i_3gram_720_076_070_i_only"]
        self.assertEqual(lock["cycle"], 212)
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
            [list(gram) for gram in STANDING_I_PREVIOUS_4GRAMS],
            lock["i_previous_4grams"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_076_070_sites"]),
            STANDING_LEFTOVER_076_070_SITES,
        )
        self.assertEqual(lock["N_leftover_076_070"], STANDING_N_LEFTOVER_076_070)
        self.assertEqual(lock["N_leftover_076_070"], 11)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_3gram_sites"]),
            STANDING_LEFTOVER_3GRAM_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 3)
        self.assertEqual(
            [list(site) for site in STANDING_EXTRA_I_SITES],
            lock["extra_i_sites"],
        )
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 0)
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
        self.assertEqual(
            tuple(lock["near_miss_leftover_090_099_site"]),
            STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
        )
        self.assertEqual(
            tuple(lock["near_miss_leftover_090_099_previous_4gram"]),
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
        )
        self.assertEqual(tuple(lock["near_miss_720_076_071"]), NEAR_MISS_720_076_071)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_3gram_720_076_070_i_only"])
        self.assertEqual(
            lock["i_3gram_720_076_070_i_only"],
            STANDING_I_3GRAM_720_076_070_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle192_3gram"])
        self.assertFalse(lock["same_as_cycle207_3gram"])
        self.assertFalse(lock["same_as_cycle206_2gram"])
        self.assertFalse(lock["same_as_cycle171_2gram"])
        self.assertFalse(lock["same_as_cycle211"])
        self.assertTrue(lock["720_076_071_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["700_076_071_does_not_count"])
        self.assertTrue(lock["076_070_without_720_does_not_count"])
        self.assertTrue(lock["prefixed_090_does_not_count"])
        self.assertTrue(lock["near_miss_090_099_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_leftover_076_070_previous_720_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_070_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_700_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_076_070_previous_720"]["cycle"], 211)
        self.assertTrue(
            self.survey["i_leftover_076_070_previous_720"][
                "i_leftover_076_070_previous_720"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_070_previous_720"]["N_share"], 3)
        self.assertEqual(self.survey["i_leftover_076_070_previous_720"]["N_leftover"], 11)
        self.assertEqual(self.survey["i_leftover_076_070_previous_stem"]["cycle"], 210)
        self.assertEqual(
            self.survey["i_leftover_076_070_previous_stem"]["N_distinct_previous_stems"],
            9,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_previous_stem"]["N_leftover"],
            11,
        )
        self.assertFalse(
            self.survey["i_leftover_076_070_previous_stem"][
                "i_leftover_076_070_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
        self.assertEqual(self.survey["i_3gram_700_076_071_i_only"]["cycle"], 192)
        self.assertTrue(self.survey["i_3gram_700_076_071_i_only"]["i_3gram_700_076_071_i_only"])
        self.assertEqual(self.survey["i_3gram_700_076_071_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_700_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"][
                "i_leftover_n4_exactly_1_contain_076_070"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
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


class TestMamariI3gram720076070IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 212 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
