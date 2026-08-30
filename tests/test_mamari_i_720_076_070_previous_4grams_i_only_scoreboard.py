"""I's cycle-212 3-gram site previous 4-grams off-I lock.

Cycle 213 text-search lock. Uses already-vendored A–V and the
cycle-212 I sites of 3-gram 720 076 070 (N_I=3, N_off_I=0, all
Ia leftover-3 / leftover-11: Ia7[62] 069 720 076 070,
Ia8[171] 053 720 076 070, Ia9[119] 999 720 076 070). Those
three ARE the cycle-211 leftover matching previous 4-grams.
Does not retune those 4-grams, the leftover 3-gram, or the
leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished
Ib is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Same leftover-shape as cycle 193 (700 076 071 previous
4-grams all I-only hapax 1/0). This cycle is the previous
4-grams of 720 076 070 only. Cycle 212 I-only 3/0, cycle
211 leftover N_share=3 / N_leftover=11, cycle 210 leftover
N_distinct=9, cycle 206 076 070 19/5 loss, and cycle 171
076 071 I-only 43/0 stay. 720 076 071 is a different
3-gram. 090 076 070 prefixes are a different 3-gram
(already lost 8/1). Do not retune the leftover n=4 set.
Do not assume the I-only result; measure each 4-gram
across all vendored tablets.

Locks exact consecutive hits of each previous 4-gram on
tablet I and on every other vendored tablet A–H and J–V.
The three 4-grams: 069 720 076 070, 053 720 076 070, and
999 720 076 070. Do not assume hapax; count each from
fixtures. Claim that can lose:
i_720_076_070_previous_4grams_i_only. True only if ALL
three have N_off_I=0 and N_I>=1. Measured: each N_I=1 at
the cycle-212 previous-4 start Ia7[61] / Ia8[170] /
Ia9[118]; all N_off_I=0. The claim is true. Do not
assume hapax; measure. Do not retune.

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
from tests.test_mamari_i_2gram_076_070_i_only_scoreboard import (
    GRAM2 as CYCLE206_GRAM2,
    STANDING_N_I as CYCLE206_N_I,
    STANDING_N_OFF_I as CYCLE206_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE206_OFF_I_SITES,
    TestMamariI2gram076070IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_I_SITES as CYCLE171_I_SITES,
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
from tests.test_mamari_i_3gram_720_076_070_i_only_scoreboard import (
    GRAM3,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE212_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE212_I_SITES,
    STANDING_N_I as CYCLE212_N_I,
    STANDING_N_OFF_I as CYCLE212_N_OFF_I,
    TestMamariI3gram720076070IOnlyScoreboard,
)
from tests.test_mamari_i_700_076_071_previous_4grams_i_only_scoreboard import (
    TestMamariI700076071Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_previous_720_scoreboard import (
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
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    site_previous_4gram,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
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

HYPOTHESIS_ALL_I_ONLY = True
STANDING_N3 = 3
STANDING_N4 = 4
GRAM4_069 = ("069", "720", "076", "070")
GRAM4_053 = ("053", "720", "076", "070")
GRAM4_999 = ("999", "720", "076", "070")
STANDING_SEQUENCES = (
    GRAM4_069,
    GRAM4_053,
    GRAM4_999,
)
STANDING_PREVIOUS_STEMS = ("069", "053", "999")
STANDING_ROLES = (
    "leftover",
    "leftover",
    "leftover",
)
NEAR_MISS_720_076_071 = ("720", "076", "071")
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
STANDING_N_I_069 = 1
STANDING_N_I_053 = 1
STANDING_N_I_999 = 1
STANDING_N_ON_I_069 = 1
STANDING_N_ON_I_053 = 1
STANDING_N_ON_I_999 = 1
STANDING_I_SITES_069 = ((SIDE_IA, "Ia7", 61),)
STANDING_I_SITES_053 = ((SIDE_IA, "Ia8", 170),)
STANDING_I_SITES_999 = ((SIDE_IA, "Ia9", 118),)
STANDING_I_SITES = (
    STANDING_I_SITES_069,
    STANDING_I_SITES_053,
    STANDING_I_SITES_999,
)
STANDING_CYCLE212_SITES = CYCLE212_I_SITES
STANDING_LEFTOVER_076_070_SITES = CYCLE211_MATCHING_SITES
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_069 = 0
STANDING_N_OFF_I_053 = 0
STANDING_N_OFF_I_999 = 0
STANDING_OFF_I_SITES_069 = ()
STANDING_OFF_I_SITES_053 = ()
STANDING_OFF_I_SITES_999 = ()
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_SITE_ROWS = (
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia7",
        "index": 61,
        "tokens4": GRAM4_069,
        "cycle212_site": (SIDE_IA, "Ia7", 62),
        "leftover_076_070_site": (SIDE_IA, "Ia7", 63),
        "previous_stem": "069",
        "role": "leftover",
        "in_cycle211_leftover_3": True,
        "in_cycle210_leftover_11": True,
        "prefixed_090_076_070": False,
        "inside_leftover_n4_maximal": False,
        "N_I": 1,
        "N_off_I": 0,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia8",
        "index": 170,
        "tokens4": GRAM4_053,
        "cycle212_site": (SIDE_IA, "Ia8", 171),
        "leftover_076_070_site": (SIDE_IA, "Ia8", 172),
        "previous_stem": "053",
        "role": "leftover",
        "in_cycle211_leftover_3": True,
        "in_cycle210_leftover_11": True,
        "prefixed_090_076_070": False,
        "inside_leftover_n4_maximal": False,
        "N_I": 1,
        "N_off_I": 0,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia9",
        "index": 118,
        "tokens4": GRAM4_999,
        "cycle212_site": (SIDE_IA, "Ia9", 119),
        "leftover_076_070_site": (SIDE_IA, "Ia9", 120),
        "previous_stem": "999",
        "role": "leftover",
        "in_cycle211_leftover_3": True,
        "in_cycle210_leftover_11": True,
        "prefixed_090_076_070": False,
        "inside_leftover_n4_maximal": False,
        "N_I": 1,
        "N_off_I": 0,
    },
)
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_069 = True
STANDING_HAPAX_053 = True
STANDING_HAPAX_999 = True
STANDING_CLAIM = "i_720_076_070_previous_4grams_i_only"
STANDING_I_720_076_070_PREVIOUS_4GRAMS_ALL_I_ONLY = True
STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_720_076_070_previous_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE193_PREVIOUS_4GRAMS = False
STANDING_SAME_AS_CYCLE207_3GRAM = False
STANDING_SAME_AS_CYCLE206_2GRAM = False
STANDING_SAME_AS_CYCLE171_2GRAM = False
STANDING_SAME_AS_CYCLE212 = False
STANDING_SAME_LEFTOVER_SHAPE_AS_193 = True
STANDING_720_076_071_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_700_076_071_DOES_NOT_COUNT = True
STANDING_076_070_WITHOUT_720_DOES_NOT_COUNT = True
STANDING_PREFIXED_090_DOES_NOT_COUNT = True
STANDING_NEAR_MISS_090_099_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_SITE_INCLUDED = False
STANDING_INSIDE_FAMILY_COUNT = 0
STANDING_INSIDE_FAMILY_SITES = ()
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def previous_4gram_start_site(
    cycle212_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Previous 4-gram starts one token before 720 076 070."""
    side, line, index = cycle212_site
    return (side, line, index - 1)


def leftover_076_070_site_for_4gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """076 070 start two tokens after the previous-4 start."""
    side, line, index = site
    return (side, line, index + 2)


def site_row_as_survey(row: dict) -> dict:
    """JSON-ready site row (lists, not tuples)."""
    return {
        "tablet": row["tablet"],
        "side": row["side"],
        "line": row["line"],
        "index": row["index"],
        "tokens4": list(row["tokens4"]),
        "cycle212_site": list(row["cycle212_site"]),
        "leftover_076_070_site": list(row["leftover_076_070_site"]),
        "previous_stem": row["previous_stem"],
        "role": row["role"],
        "in_cycle211_leftover_3": row["in_cycle211_leftover_3"],
        "in_cycle210_leftover_11": row["in_cycle210_leftover_11"],
        "prefixed_090_076_070": row["prefixed_090_076_070"],
        "inside_leftover_n4_maximal": row["inside_leftover_n4_maximal"],
        "N_I": row["N_I"],
        "N_off_I": row["N_off_I"],
    }


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_720_076_070_previous_4grams_i_only(
    n_i_069: int,
    n_off_i_069: int,
    n_i_053: int,
    n_off_i_053: int,
    n_i_999: int,
    n_off_i_999: int,
) -> bool:
    """True iff all three previous 4-grams are I-only.

    Claim holds only if every one has N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only. Hapax is not
    assumed; N_I may be greater than 1.
    """
    return (
        sequence_is_i_only(n_i_069, n_off_i_069)
        and sequence_is_i_only(n_i_053, n_off_i_053)
        and sequence_is_i_only(n_i_999, n_off_i_999)
    )


i_720_076_070_previous_4grams_all_i_only = i_720_076_070_previous_4grams_i_only


class TestI720076070Previous4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-212 previous 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 720 076 071 / 090 076 070 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM4_069, ("069", "720", "076", "070"))
        self.assertEqual(GRAM4_053, ("053", "720", "076", "070"))
        self.assertEqual(GRAM4_999, ("999", "720", "076", "070"))
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[1:], GRAM3)
        adjacent = [list(GRAM4_069), list(GRAM4_053), list(GRAM4_999)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_069), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_053), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_999), 1)
        overlap = [["069", "720", "076", "070", "069", "720", "076", "070"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_069), 2)
        gapped = [list(GRAM4_069[:2]) + ["000"] + list(GRAM4_069[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_069), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_069), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_053), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_999), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_720_076_071)], GRAM4_069), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM4_053), 0)
        self.assertEqual(
            ngram_hit_count(
                [list(STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM)],
                GRAM4_999,
            ),
            0,
        )
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_071)], GRAM4_069), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM4_053), 0)
        self.assertEqual(ngram_hit_count([["076", "070"]], GRAM4_069), 0)
        self.assertEqual(ngram_hit_count([["720", "076", "071"]], GRAM4_053), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "070"]], GRAM4_999), 0)
        self.assertEqual(ngram_hit_count([["720", "076", "070"]], GRAM4_069), 0)
        self.assertTrue(STANDING_720_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_700_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_WITHOUT_720_DOES_NOT_COUNT)
        self.assertTrue(STANDING_NEAR_MISS_090_099_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all three previous 4-grams are I-only."""
        provider = MockProvider()
        hold = (1, 0, 1, 0, 1, 0)
        self.assertTrue(i_720_076_070_previous_4grams_i_only(*hold))
        self.assertTrue(i_720_076_070_previous_4grams_i_only(2, 0, 1, 0, 1, 0))
        lose_off = (
            (1, 1, 1, 0, 1, 0),
            (1, 0, 1, 1, 1, 0),
            (1, 0, 1, 0, 1, 1),
        )
        for counts in lose_off:
            self.assertFalse(i_720_076_070_previous_4grams_i_only(*counts))
        lose_missing_i = (
            (0, 0, 1, 0, 1, 0),
            (1, 0, 0, 0, 1, 0),
            (1, 0, 1, 0, 0, 0),
        )
        for counts in lose_missing_i:
            self.assertFalse(i_720_076_070_previous_4grams_i_only(*counts))
        self.assertFalse(i_720_076_070_previous_4grams_i_only(0, 0, 0, 0, 0, 0))
        self.assertEqual(STANDING_CLAIM, "i_720_076_070_previous_4grams_i_only")
        self.assertTrue(STANDING_I_720_076_070_PREVIOUS_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_212_previous_not_retuned(self):
        """4-grams stay the cycle-212 I-site previous runs; none is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("720", "076", "070"))
        self.assertEqual(STANDING_SEQUENCES, CYCLE212_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_SEQUENCES, CYCLE211_MATCHING_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_PREVIOUS_STEMS, ("069", "053", "999"))
        self.assertEqual(STANDING_CYCLE212_SITES, CYCLE212_I_SITES)
        self.assertNotEqual(GRAM4_069, GRAM5)
        self.assertNotEqual(GRAM4_053, GRAM5)
        self.assertNotEqual(GRAM4_999, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM4_069, GRAM5))
        self.assertEqual(STANDING_INSIDE_FAMILY_SITES, ())
        self.assertEqual(STANDING_INSIDE_FAMILY_COUNT, 0)
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_720_076_071))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_090_076_070))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_999_090_076_071))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_700_076_076_053))
            self.assertFalse(
                is_contiguous_substring(
                    gram,
                    STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
                )
            )
            self.assertFalse(is_contiguous_substring(gram, CYCLE205_MATCHING_LEFTOVERS[0]))
        for site, start in zip(
            STANDING_CYCLE212_SITES,
            (
                STANDING_I_SITES_069[0],
                STANDING_I_SITES_053[0],
                STANDING_I_SITES_999[0],
            ),
            strict=True,
        ):
            self.assertEqual(previous_4gram_start_site(site), start)
            self.assertEqual(start[2], site[2] - 1)
        self.assertEqual(
            leftover_076_070_site_for_4gram(STANDING_I_SITES_069[0]),
            (SIDE_IA, "Ia7", 63),
        )
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE193_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE212)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_193)
        self.assertFalse(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(GRAM4_069), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI720076070Previous4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture cycle-212 previous-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle212_sites = STANDING_CYCLE212_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.grams = STANDING_SEQUENCES
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in self.grams)
        self.n_i = tuple(
            ngram_hit_count(self.i_sides[SIDE_IA], gram) + STANDING_IB_HITS
            for gram in self.grams
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in self.grams
        )
        self.off_i = tuple(
            tablet_hit_counts(self.by_tablet, gram, OFF_I_TABLETS)
            for gram in self.grams
        )
        self.n_off_i = tuple(sum(row) for row in self.off_i)
        self.claim_holds = i_720_076_070_previous_4grams_i_only(
            *sum(zip(self.n_i, self.n_off_i, strict=True), ())
        )

    def test_tokens_and_sites_are_cycle_212_lock_not_retuned(self):
        """4-grams and I sites stay the cycle-212 previous lock."""
        self.assertEqual(GRAM3, ("720", "076", "070"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle212_sites, STANDING_CYCLE212_SITES)
        self.assertEqual(
            STANDING_CYCLE212_SITES,
            (
                (SIDE_IA, "Ia7", 62),
                (SIDE_IA, "Ia8", 171),
                (SIDE_IA, "Ia9", 119),
            ),
        )
        prior_212 = self.survey["i_3gram_720_076_070_i_only"]
        self.assertEqual(prior_212["cycle"], 212)
        self.assertEqual(tuple(prior_212["tokens3"]), GRAM3)
        self.assertEqual(prior_212["N_I"], CYCLE212_N_I)
        self.assertEqual(prior_212["N_I"], 3)
        self.assertEqual(prior_212["N_off_I"], CYCLE212_N_OFF_I)
        self.assertEqual(prior_212["N_off_I"], 0)
        self.assertTrue(prior_212["i_3gram_720_076_070_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_212["i_sites"]),
            STANDING_CYCLE212_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_212["i_previous_4grams"],
        )
        prior_211 = self.survey["i_leftover_076_070_previous_720"]
        self.assertEqual(prior_211["cycle"], 211)
        self.assertEqual(tuple(prior_211["backward_3gram"]), GRAM3)
        self.assertEqual(prior_211["N_share"], CYCLE211_N_SHARE)
        self.assertEqual(prior_211["N_share"], 3)
        self.assertEqual(prior_211["N_leftover"], CYCLE211_N_LEFTOVER)
        self.assertEqual(prior_211["N_leftover"], 11)
        self.assertEqual(prior_211["N_with_previous_720_076_070"], 3)
        self.assertTrue(prior_211["i_leftover_076_070_previous_720"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_211["matching_leftover_sites"]),
            CYCLE211_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_211["matching_previous_4grams"],
        )
        prior_210 = self.survey["i_leftover_076_070_previous_stem"]
        self.assertEqual(prior_210["cycle"], 210)
        self.assertEqual(prior_210["N_leftover"], 11)
        self.assertEqual(prior_210["N_distinct_previous_stems"], 9)
        self.assertEqual(prior_210["N_distinct_previous_stems"], CYCLE210_N_DISTINCT)
        self.assertFalse(prior_210["i_leftover_076_070_share_one_previous_stem"])
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
        self.assertEqual(GRAM3[1:], CYCLE206_GRAM2)
        self.assertNotEqual(GRAM3[1:], CYCLE171_GRAM2)
        prior_193 = self.survey["i_700_076_071_previous_4grams_i_only"]
        self.assertEqual(prior_193["cycle"], 193)
        self.assertTrue(prior_193["i_700_076_071_previous_4grams_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(CYCLE211_N_SHARE, 3)
        self.assertEqual(CYCLE211_N_LEFTOVER, 11)
        self.assertEqual(CYCLE210_N_DISTINCT, 9)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_I=1/1/1, N_off_I=0/0/0. All I-only. Claim holds."""
        standing_on = (
            STANDING_N_I_069,
            STANDING_N_I_053,
            STANDING_N_I_999,
        )
        standing_off = (
            STANDING_N_OFF_I_069,
            STANDING_N_OFF_I_053,
            STANDING_N_OFF_I_999,
        )
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, standing_on)
        self.assertEqual(standing_on, (1, 1, 1))
        self.assertEqual(self.n_off_i, standing_off)
        self.assertEqual(standing_off, (0, 0, 0))
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(STANDING_OFF_I_SITES, ())
        for site, start, gram, prev, role, leftover in zip(
            STANDING_CYCLE212_SITES,
            (
                STANDING_I_SITES_069[0],
                STANDING_I_SITES_053[0],
                STANDING_I_SITES_999[0],
            ),
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_LEFTOVER_076_070_SITES,
            strict=True,
        ):
            self.assertEqual(previous_4gram_start_site(site), start)
            self.assertEqual(leftover_076_070_site_for_4gram(start), leftover)
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2]], prev)
            self.assertEqual(tuple(stems[start[2] + 1 : start[2] + STANDING_N4]), GRAM3)
            self.assertEqual(
                site_previous_4gram(stems, leftover[2], CYCLE206_GRAM2),
                gram,
            )
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram[1:], NEAR_MISS_720_076_071)
            self.assertNotEqual(gram[1:], NEAR_MISS_090_076_070)
            self.assertEqual(role, "leftover")
            self.assertIn(leftover, CYCLE211_MATCHING_SITES)
            self.assertIn(leftover, STANDING_LEFTOVER_SITES)
            self.assertNotIn(leftover, STANDING_PREFIXED_I_SITES)
            self.assertIn(gram, CYCLE211_MATCHING_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
        self.assertEqual(STANDING_INSIDE_FAMILY_COUNT, 0)
        self.assertEqual(STANDING_INSIDE_FAMILY_SITES, ())
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_069)
        self.assertTrue(STANDING_HAPAX_053)
        self.assertTrue(STANDING_HAPAX_999)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off in zip(self.hits_by_tablet, self.off_i, strict=True):
            self.assertEqual(hits, STANDING_HITS_BY_TABLET_ONE_ON_I)
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
        for tablet, *counts in zip(
            VENDORED_TABLETS,
            *self.hits_by_tablet,
            strict=True,
        ):
            for count, gram in zip(counts, self.grams, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                self.assertEqual(count, 1 if tablet == "I" else 0)
        self.assertEqual(
            i_720_076_070_previous_4grams_i_only(
                *sum(zip(self.n_i, self.n_off_i, strict=True), ())
            ),
            STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY,
        )
        self.assertTrue(STANDING_I_720_076_070_PREVIOUS_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_720_076_070_previous_4grams_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE193_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE206_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE171_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE212)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_193)
        self.assertTrue(STANDING_720_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_700_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_WITHOUT_720_DOES_NOT_COUNT)
        self.assertTrue(STANDING_PREFIXED_090_DOES_NOT_COUNT)
        self.assertTrue(STANDING_NEAR_MISS_090_099_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        for row, site, gram in zip(
            STANDING_SITE_ROWS,
            (
                STANDING_I_SITES_069[0],
                STANDING_I_SITES_053[0],
                STANDING_I_SITES_999[0],
            ),
            STANDING_SEQUENCES,
            strict=True,
        ):
            self.assertEqual((row["side"], row["line"], row["index"]), site)
            self.assertEqual(row["tokens4"], gram)
            self.assertEqual(row["tablet"], "I")
            self.assertTrue(row["in_cycle211_leftover_3"])
            self.assertTrue(row["in_cycle210_leftover_11"])
            self.assertFalse(row["prefixed_090_076_070"])
            self.assertFalse(row["inside_leftover_n4_maximal"])
            self.assertEqual(row["N_I"], 1)
            self.assertEqual(row["N_off_I"], 0)
        near_stems = line_stems_for_site(
            self.i_sides,
            STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
        )
        near_index = STANDING_NEAR_MISS_LEFTOVER_090_099_SITE[2]
        self.assertEqual(
            site_previous_4gram(near_stems, near_index, CYCLE206_GRAM2),
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
        )
        self.assertNotIn(
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
            STANDING_SEQUENCES,
        )
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_I_SITES_069)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_I_SITES_053)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_090_099_SITE, STANDING_I_SITES_999)
        for site in STANDING_PREFIXED_I_SITES:
            self.assertNotIn(site, STANDING_I_SITES_069)
            self.assertNotIn(site, STANDING_I_SITES_053)
            self.assertNotIn(site, STANDING_I_SITES_999)
        for site in CYCLE207_I_SITES:
            self.assertNotIn(site, STANDING_I_SITES_069)
            self.assertNotIn(site, STANDING_I_SITES_053)
            self.assertNotIn(site, STANDING_I_SITES_999)
        for site in CYCLE206_OFF_I_SITES:
            self.assertNotIn(site, STANDING_OFF_I_SITES)
        self.assertEqual(len(CYCLE206_OFF_I_SITES), 5)
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        for n_on, locked in zip(self.n_i, standing_on, strict=True):
            if n_on != locked:
                self.fail("measured N_I drifted from the locked count")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_212_211_210_206_171_scoreboards_still_compute(self):
        """Cycle 212 I-only 3/0, 211 N_share=3/11, 210 N_distinct=9, 206 19/5, 171 43/0 stay."""
        prior_212 = TestMamariI3gram720076070IOnlyScoreboard()
        prior_212.setUp()
        prior_212.test_i_hits_are_three_on_ia_all_leftover()
        prior_212.test_3gram_is_zero_off_i_and_i_only()
        prior_212.test_survey_matches_computed_lock()
        self.assertEqual(prior_212.i_hits, 3)
        self.assertEqual(prior_212.off_i_hits, 0)
        self.assertEqual(prior_212.i_sites, CYCLE212_I_SITES)
        self.assertEqual(CYCLE212_N_I, 3)
        self.assertEqual(CYCLE212_N_OFF_I, 0)
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
        self.assertEqual(prior_210.n_distinct, CYCLE210_N_DISTINCT)
        self.assertEqual(prior_210.n_leftover, CYCLE210_N_LEFTOVER)
        self.assertEqual(CYCLE210_N_DISTINCT, 9)
        self.assertEqual(CYCLE210_N_LEFTOVER, 11)
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
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(len(prior_171.i_sites), 43)
        self.assertEqual(prior_171.i_sites, CYCLE171_I_SITES)
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(CYCLE207_N_OFF_I, 1)
        prior_193 = TestMamariI700076071Previous4gramsIOnlyScoreboard()
        prior_193.setUp()
        prior_193.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_193.test_survey_matches_computed_lock()
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-213 previous-4 I-only lock."""
        lock = self.survey["i_720_076_070_previous_4grams_i_only"]
        self.assertEqual(lock["cycle"], 213)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I_3gram"], CYCLE212_N_I)
        self.assertEqual(lock["N_I_3gram"], 3)
        self.assertEqual(lock["N_off_I_3gram"], CYCLE212_N_OFF_I)
        self.assertEqual(lock["N_off_I_3gram"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle212_sites"]),
            STANDING_CYCLE212_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_076_070_SITES,
        )
        self.assertEqual(lock["inside_family_sites"], [])
        self.assertEqual(lock["inside_family_count"], 0)
        self.assertFalse(lock["inside_family_site_included"])
        self.assertEqual(tuple(lock["per_site_previous_stems"]), STANDING_PREVIOUS_STEMS)
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), 3)
        standing_on = (
            STANDING_N_I_069,
            STANDING_N_I_053,
            STANDING_N_I_999,
        )
        standing_off = (
            STANDING_N_OFF_I_069,
            STANDING_N_OFF_I_053,
            STANDING_N_OFF_I_999,
        )
        standing_hapax = (
            STANDING_HAPAX_069,
            STANDING_HAPAX_053,
            STANDING_HAPAX_999,
        )
        standing_off_sites = (
            STANDING_OFF_I_SITES_069,
            STANDING_OFF_I_SITES_053,
            STANDING_OFF_I_SITES_999,
        )
        for row, gram, site, prev, role, sites, n_on, n_off, hapax, off_sites in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CYCLE212_SITES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            standing_on,
            standing_off,
            standing_hapax,
            standing_off_sites,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle212_site"]), site)
            self.assertEqual(row["previous_stem"], prev)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_I"], 1)
            self.assertEqual(row["ia_hits"], 1)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["ib_sites"]),
                STANDING_IB_SITES,
            )
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(
                [list(site_row) for site_row in off_sites],
                row["off_i_sites"],
            )
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(
                tuple(row["hits_by_tablet"]),
                STANDING_HITS_BY_TABLET_ONE_ON_I,
            )
            self.assertTrue(row["i_only"])
            self.assertEqual(row["hapax"], hapax)
        self.assertEqual(
            [site_row_as_survey(row) for row in STANDING_SITE_ROWS],
            lock["site_rows"],
        )
        self.assertEqual(lock["N_I_069"], STANDING_N_I_069)
        self.assertEqual(lock["N_off_I_069"], STANDING_N_OFF_I_069)
        self.assertEqual(lock["N_I_053"], STANDING_N_I_053)
        self.assertEqual(lock["N_off_I_053"], STANDING_N_OFF_I_053)
        self.assertEqual(lock["N_I_999"], STANDING_N_I_999)
        self.assertEqual(lock["N_off_I_999"], STANDING_N_OFF_I_999)
        self.assertEqual(
            tuple(lock["near_miss_leftover_090_099_site"]),
            STANDING_NEAR_MISS_LEFTOVER_090_099_SITE,
        )
        self.assertEqual(
            tuple(lock["near_miss_leftover_090_099_previous_4gram"]),
            STANDING_NEAR_MISS_LEFTOVER_090_099_PREVIOUS_4GRAM,
        )
        self.assertEqual(tuple(lock["near_miss_720_076_071"]), NEAR_MISS_720_076_071)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_720_076_070_previous_4grams_all_i_only"])
        self.assertTrue(lock["i_720_076_070_previous_4grams_i_only"])
        self.assertEqual(
            lock["i_720_076_070_previous_4grams_i_only"],
            STANDING_I_720_076_070_PREVIOUS_4GRAMS_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle193_previous_4grams"])
        self.assertFalse(lock["same_as_cycle207_3gram"])
        self.assertFalse(lock["same_as_cycle206_2gram"])
        self.assertFalse(lock["same_as_cycle171_2gram"])
        self.assertFalse(lock["same_as_cycle212"])
        self.assertTrue(lock["same_leftover_shape_as_cycle_193"])
        self.assertTrue(lock["720_076_071_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["700_076_071_does_not_count"])
        self.assertTrue(lock["076_070_without_720_does_not_count"])
        self.assertTrue(lock["prefixed_090_does_not_count"])
        self.assertTrue(lock["near_miss_090_099_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_720_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_070_previous_720_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_070_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_700_076_071_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["cycle"], 212)
        self.assertTrue(
            self.survey["i_3gram_720_076_070_i_only"]["i_3gram_720_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_720_076_070_i_only"]["N_off_I"], 0)
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
        self.assertEqual(self.survey["i_leftover_076_070_previous_stem"]["N_leftover"], 11)
        self.assertFalse(
            self.survey["i_leftover_076_070_previous_stem"][
                "i_leftover_076_070_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(
            self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_700_076_071_previous_4grams_i_only"]["cycle"], 193)
        self.assertTrue(
            self.survey["i_700_076_071_previous_4grams_i_only"][
                "i_700_076_071_previous_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"][
                "i_leftover_n4_exactly_1_contain_076_070"
            ]
        )
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_n"], 5)
        self.assertEqual(self.survey["n_repeating_nge5"]["cycle"], 134)
        self.assertTrue(
            self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"]
        )
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(
            self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"]
        )
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(
            self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"],
            5,
        )
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI720076070Previous4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 213 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
