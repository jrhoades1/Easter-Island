"""I's cycle-192 3-gram site previous 4-grams off-I lock.

Cycle 193 text-search lock. Uses already-vendored A–V and the
cycle-192 I sites of 3-gram 700 076 071 (N_I=3, N_off_I=0, all
Ia leftover-3 / leftover-34: Ia1[162] 090 700 076 071,
Ia2[50] 999 700 076 071, Ia13[127] 040 700 076 071). Those
three ARE the cycle-191 leftover matching previous 4-grams.
Does not retune those 4-grams, the leftover 3-gram, or the
leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished
Ib is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Same leftover-shape as cycle 187 (076 071 061 forward
4-grams all I-only hapax 1/0), cycle 184 (076 071 700
forward 4-grams all I-only hapax 1/0), cycle 181
(076 071 090 forward 4-grams all I-only), cycle 178
(076 071 600 forward 4-grams all I-only hapax 1/0), and
cycle 175 (076 071 076 forward 4-grams all I-only hapax
1/0). This cycle is the previous 4-grams of 700 076 071
only. Cycle 192 I-only 3/0, cycle 191 leftover N=3, cycle
172 leftover N=34, and leftover n=4 set stay. 071 999 and
076 076 do not count. Near-miss Ia9[10] 700 604 076 071
does not. Do not retune.

Locks exact consecutive hits of each previous 4-gram on
tablet I and on every other vendored tablet A–H and J–V.
The three 4-grams: 090 700 076 071, 999 700 076 071, and
040 700 076 071. Do not assume hapax; count each from
fixtures. Claim that can lose:
i_700_076_071_previous_4grams_all_i_only. True only if ALL
three have N_off_I=0 and N_I>=1. Measured: each N_I=1 at
the cycle-192 previous-4 start Ia1[161] / Ia2[49] /
Ia13[126]; all N_off_I=0. The claim is true. Do not
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
from tests.test_mamari_i_3gram_700_076_071_i_only_scoreboard import (
    GRAM3,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE192_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE192_I_SITES,
    STANDING_N_I as CYCLE192_N_I,
    STANDING_N_OFF_I as CYCLE192_N_OFF_I,
    TestMamariI3gram700076071IOnlyScoreboard,
)
from tests.test_mamari_i_076_071_061_forward_4grams_i_only_scoreboard import (
    TestMamariI076071061Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_700_scoreboard import (
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE191_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE191_MATCHING_SITES,
    STANDING_N_WITH_PREVIOUS_700_076_071 as CYCLE191_N_WITH,
    STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
    STANDING_NEAR_MISS_LEFTOVER_700_604_SITE,
    TestMamariILeftover076071Previous700Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE190_N_DISTINCT,
    site_previous_4gram,
    TestMamariILeftover076071PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
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

HYPOTHESIS_ALL_I_ONLY = True
STANDING_N3 = 3
STANDING_N4 = 4
GRAM4_090 = ("090", "700", "076", "071")
GRAM4_999 = ("999", "700", "076", "071")
GRAM4_040 = ("040", "700", "076", "071")
STANDING_SEQUENCES = (
    GRAM4_090,
    GRAM4_999,
    GRAM4_040,
)
STANDING_PREVIOUS_STEMS = ("090", "999", "040")
STANDING_ROLES = (
    "leftover",
    "leftover",
    "leftover",
)
STANDING_N_I_090 = 1
STANDING_N_I_999 = 1
STANDING_N_I_040 = 1
STANDING_N_ON_I_090 = 1
STANDING_N_ON_I_999 = 1
STANDING_N_ON_I_040 = 1
STANDING_I_SITES_090 = ((SIDE_IA, "Ia1", 161),)
STANDING_I_SITES_999 = ((SIDE_IA, "Ia2", 49),)
STANDING_I_SITES_040 = ((SIDE_IA, "Ia13", 126),)
STANDING_I_SITES = (
    STANDING_I_SITES_090,
    STANDING_I_SITES_999,
    STANDING_I_SITES_040,
)
STANDING_CYCLE192_SITES = CYCLE192_I_SITES
STANDING_LEFTOVER_076_071_SITES = CYCLE191_MATCHING_SITES
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_090 = 0
STANDING_N_OFF_I_999 = 0
STANDING_N_OFF_I_040 = 0
STANDING_OFF_I_SITES_090 = ()
STANDING_OFF_I_SITES_999 = ()
STANDING_OFF_I_SITES_040 = ()
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_SITE_ROWS = (
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia1",
        "index": 161,
        "tokens4": GRAM4_090,
        "cycle192_site": (SIDE_IA, "Ia1", 162),
        "leftover_076_071_site": (SIDE_IA, "Ia1", 163),
        "previous_stem": "090",
        "role": "leftover",
        "in_cycle191_leftover_3": True,
        "in_cycle172_leftover_34": True,
        "inside_family": False,
        "N_I": 1,
        "N_off_I": 0,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia2",
        "index": 49,
        "tokens4": GRAM4_999,
        "cycle192_site": (SIDE_IA, "Ia2", 50),
        "leftover_076_071_site": (SIDE_IA, "Ia2", 51),
        "previous_stem": "999",
        "role": "leftover",
        "in_cycle191_leftover_3": True,
        "in_cycle172_leftover_34": True,
        "inside_family": False,
        "N_I": 1,
        "N_off_I": 0,
    },
    {
        "tablet": "I",
        "side": SIDE_IA,
        "line": "Ia13",
        "index": 126,
        "tokens4": GRAM4_040,
        "cycle192_site": (SIDE_IA, "Ia13", 127),
        "leftover_076_071_site": (SIDE_IA, "Ia13", 128),
        "previous_stem": "040",
        "role": "leftover",
        "in_cycle191_leftover_3": True,
        "in_cycle172_leftover_34": True,
        "inside_family": False,
        "N_I": 1,
        "N_off_I": 0,
    },
)
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_090 = True
STANDING_HAPAX_999 = True
STANDING_HAPAX_040 = True
STANDING_CLAIM = "i_700_076_071_previous_4grams_all_i_only"
STANDING_I_700_076_071_PREVIOUS_4GRAMS_ALL_I_ONLY = True
STANDING_I_700_076_071_PREVIOUS_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_700_076_071_previous_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE178_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE181_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE184_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE187_FORWARD_4GRAMS = False
STANDING_SAME_AS_CYCLE192 = False
STANDING_SAME_LEFTOVER_SHAPE_AS_175_178_181_184_187 = True
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_NEAR_MISS_700_604_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_SITE_INCLUDED = False
STANDING_INSIDE_FAMILY_COUNT = 0
STANDING_INSIDE_FAMILY_SITES = ()
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def previous_4gram_start_site(
    cycle192_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Previous 4-gram starts one token before 700 076 071."""
    side, line, index = cycle192_site
    return (side, line, index - 1)


def leftover_076_071_site_for_4gram(
    site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """076 071 start two tokens after the previous-4 start."""
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
        "cycle192_site": list(row["cycle192_site"]),
        "leftover_076_071_site": list(row["leftover_076_071_site"]),
        "previous_stem": row["previous_stem"],
        "role": row["role"],
        "in_cycle191_leftover_3": row["in_cycle191_leftover_3"],
        "in_cycle172_leftover_34": row["in_cycle172_leftover_34"],
        "inside_family": row["inside_family"],
        "N_I": row["N_I"],
        "N_off_I": row["N_off_I"],
    }


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_700_076_071_previous_4grams_all_i_only(
    n_i_090: int,
    n_off_i_090: int,
    n_i_999: int,
    n_off_i_999: int,
    n_i_040: int,
    n_off_i_040: int,
) -> bool:
    """True iff all three previous 4-grams are I-only.

    Claim holds only if every one has N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only. Hapax is not
    assumed; N_I may be greater than 1.
    """
    return (
        sequence_is_i_only(n_i_090, n_off_i_090)
        and sequence_is_i_only(n_i_999, n_off_i_999)
        and sequence_is_i_only(n_i_040, n_off_i_040)
    )


class TestI700076071Previous4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-192 previous 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 071 999 / 076 076 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM4_090, ("090", "700", "076", "071"))
        self.assertEqual(GRAM4_999, ("999", "700", "076", "071"))
        self.assertEqual(GRAM4_040, ("040", "700", "076", "071"))
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[1:], GRAM3)
        adjacent = [list(GRAM4_090), list(GRAM4_999), list(GRAM4_040)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_090), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_999), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_040), 1)
        overlap = [["090", "700", "076", "071", "090", "700", "076", "071"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_090), 2)
        gapped = [list(GRAM4_090[:2]) + ["000"] + list(GRAM4_090[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_999), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_040), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_071_065_071_999)], GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_700_076_076_053)], GRAM4_999), 0)
        self.assertEqual(
            ngram_hit_count(
                [list(STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM)],
                GRAM4_040,
            ),
            0,
        )
        self.assertEqual(ngram_hit_count([["071", "999"]], GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([["076", "076"]], GRAM4_999), 0)
        self.assertEqual(ngram_hit_count([["700", "076", "071"]], GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([["700", "604", "076", "071"]], GRAM4_090), 0)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_NEAR_MISS_700_604_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all three previous 4-grams are I-only."""
        provider = MockProvider()
        hold = (1, 0, 1, 0, 1, 0)
        self.assertTrue(i_700_076_071_previous_4grams_all_i_only(*hold))
        self.assertTrue(i_700_076_071_previous_4grams_all_i_only(2, 0, 1, 0, 1, 0))
        lose_off = (
            (1, 1, 1, 0, 1, 0),
            (1, 0, 1, 1, 1, 0),
            (1, 0, 1, 0, 1, 1),
        )
        for counts in lose_off:
            self.assertFalse(i_700_076_071_previous_4grams_all_i_only(*counts))
        lose_missing_i = (
            (0, 0, 1, 0, 1, 0),
            (1, 0, 0, 0, 1, 0),
            (1, 0, 1, 0, 0, 0),
        )
        for counts in lose_missing_i:
            self.assertFalse(i_700_076_071_previous_4grams_all_i_only(*counts))
        self.assertFalse(i_700_076_071_previous_4grams_all_i_only(0, 0, 0, 0, 0, 0))
        self.assertEqual(STANDING_CLAIM, "i_700_076_071_previous_4grams_all_i_only")
        self.assertTrue(STANDING_I_700_076_071_PREVIOUS_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_700_076_071_PREVIOUS_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_700_076_071_PREVIOUS_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_192_previous_not_retuned(self):
        """4-grams stay the cycle-192 I-site previous runs; none is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("700", "076", "071"))
        self.assertEqual(STANDING_SEQUENCES, CYCLE192_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_SEQUENCES, CYCLE191_MATCHING_PREVIOUS_4GRAMS)
        self.assertEqual(STANDING_PREVIOUS_STEMS, ("090", "999", "040"))
        self.assertEqual(STANDING_CYCLE192_SITES, CYCLE192_I_SITES)
        self.assertNotEqual(GRAM4_090, GRAM5)
        self.assertNotEqual(GRAM4_999, GRAM5)
        self.assertNotEqual(GRAM4_040, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM4_090, GRAM5))
        self.assertEqual(STANDING_INSIDE_FAMILY_SITES, ())
        self.assertEqual(STANDING_INSIDE_FAMILY_COUNT, 0)
        for gram in STANDING_SEQUENCES:
            self.assertTrue(is_contiguous_substring(GRAM3, gram))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_071_065_071_999))
            self.assertFalse(is_contiguous_substring(gram, NEAR_MISS_700_076_076_053))
            self.assertFalse(
                is_contiguous_substring(
                    gram,
                    STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
                )
            )
        for site, start in zip(
            STANDING_CYCLE192_SITES,
            (
                STANDING_I_SITES_090[0],
                STANDING_I_SITES_999[0],
                STANDING_I_SITES_040[0],
            ),
            strict=True,
        ):
            self.assertEqual(previous_4gram_start_site(site), start)
            self.assertEqual(start[2], site[2] - 1)
        self.assertEqual(
            leftover_076_071_site_for_4gram(STANDING_I_SITES_090[0]),
            (SIDE_IA, "Ia1", 163),
        )
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE178_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE181_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE184_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE187_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE192)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_175_178_181_184_187)
        self.assertFalse(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(len(GRAM4_090), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI700076071Previous4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture cycle-192 previous-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle192_sites = STANDING_CYCLE192_SITES
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
        self.claim_holds = i_700_076_071_previous_4grams_all_i_only(
            *sum(zip(self.n_i, self.n_off_i, strict=True), ())
        )

    def test_tokens_and_sites_are_cycle_192_lock_not_retuned(self):
        """4-grams and I sites stay the cycle-192 previous lock."""
        self.assertEqual(GRAM3, ("700", "076", "071"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle192_sites, STANDING_CYCLE192_SITES)
        self.assertEqual(
            STANDING_CYCLE192_SITES,
            (
                (SIDE_IA, "Ia1", 162),
                (SIDE_IA, "Ia2", 50),
                (SIDE_IA, "Ia13", 127),
            ),
        )
        prior_192 = self.survey["i_3gram_700_076_071_i_only"]
        self.assertEqual(prior_192["cycle"], 192)
        self.assertEqual(tuple(prior_192["tokens3"]), GRAM3)
        self.assertEqual(prior_192["N_I"], CYCLE192_N_I)
        self.assertEqual(prior_192["N_I"], 3)
        self.assertEqual(prior_192["N_off_I"], CYCLE192_N_OFF_I)
        self.assertEqual(prior_192["N_off_I"], 0)
        self.assertTrue(prior_192["i_3gram_700_076_071_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_192["i_sites"]),
            STANDING_CYCLE192_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_192["i_previous_4grams"],
        )
        prior_191 = self.survey["i_leftover_076_071_previous_700"]
        self.assertEqual(prior_191["cycle"], 191)
        self.assertEqual(tuple(prior_191["backward_3gram"]), GRAM3)
        self.assertEqual(prior_191["N_with_previous_700_076_071"], CYCLE191_N_WITH)
        self.assertEqual(prior_191["N_with_previous_700_076_071"], 3)
        self.assertTrue(prior_191["i_leftover_076_071_exactly_3_previous_700_076_071"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_191["matching_leftover_sites"]),
            CYCLE191_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            prior_191["matching_previous_4grams"],
        )
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertEqual(GRAM3[1:], CYCLE171_GRAM2)
        prior_172 = self.survey["i_2gram_076_071_inside_family"]
        self.assertEqual(prior_172["cycle"], 172)
        self.assertEqual(prior_172["N_leftover"], 34)
        self.assertFalse(prior_172["i_2gram_076_071_all_inside_leftover_n4_family"])
        prior_190 = self.survey["i_leftover_076_071_previous_stem"]
        self.assertEqual(prior_190["cycle"], 190)
        self.assertEqual(prior_190["N_distinct_previous_stems"], 28)
        self.assertFalse(prior_190["i_leftover_076_071_share_one_previous_stem"])
        prior_187 = self.survey["i_076_071_061_forward_4grams_i_only"]
        self.assertEqual(prior_187["cycle"], 187)
        self.assertTrue(prior_187["i_076_071_061_forward_4grams_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(CYCLE191_N_WITH, 3)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_I=1/1/1, N_off_I=0/0/0. All I-only. Claim holds."""
        standing_on = (
            STANDING_N_I_090,
            STANDING_N_I_999,
            STANDING_N_I_040,
        )
        standing_off = (
            STANDING_N_OFF_I_090,
            STANDING_N_OFF_I_999,
            STANDING_N_OFF_I_040,
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
            STANDING_CYCLE192_SITES,
            (
                STANDING_I_SITES_090[0],
                STANDING_I_SITES_999[0],
                STANDING_I_SITES_040[0],
            ),
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_LEFTOVER_076_071_SITES,
            strict=True,
        ):
            self.assertEqual(previous_4gram_start_site(site), start)
            self.assertEqual(leftover_076_071_site_for_4gram(start), leftover)
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2]], prev)
            self.assertEqual(tuple(stems[start[2] + 1 : start[2] + STANDING_N4]), GRAM3)
            self.assertEqual(
                site_previous_4gram(stems, leftover[2], CYCLE171_GRAM2),
                gram,
            )
            self.assertNotEqual(gram, GRAM5)
            self.assertEqual(role, "leftover")
            self.assertIn(leftover, CYCLE191_MATCHING_SITES)
            self.assertIn(leftover, STANDING_LEFTOVER_SITES)
            self.assertNotIn(leftover, STANDING_INSIDE_SITES)
            self.assertIn(gram, CYCLE191_MATCHING_PREVIOUS_4GRAMS)
        self.assertFalse(STANDING_INSIDE_FAMILY_SITE_INCLUDED)
        self.assertEqual(STANDING_INSIDE_FAMILY_COUNT, 0)
        self.assertEqual(STANDING_INSIDE_FAMILY_SITES, ())
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_090)
        self.assertTrue(STANDING_HAPAX_999)
        self.assertTrue(STANDING_HAPAX_040)
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
            i_700_076_071_previous_4grams_all_i_only(
                *sum(zip(self.n_i, self.n_off_i, strict=True), ())
            ),
            STANDING_I_700_076_071_PREVIOUS_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_700_076_071_PREVIOUS_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_I_700_076_071_PREVIOUS_4GRAMS_ALL_I_ONLY)
        self.assertTrue(STANDING_I_700_076_071_PREVIOUS_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_700_076_071_previous_4grams_all_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE175_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE178_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE181_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE184_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE187_FORWARD_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE192)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_175_178_181_184_187)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_NEAR_MISS_700_604_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        for row, site, gram in zip(
            STANDING_SITE_ROWS,
            (
                STANDING_I_SITES_090[0],
                STANDING_I_SITES_999[0],
                STANDING_I_SITES_040[0],
            ),
            STANDING_SEQUENCES,
            strict=True,
        ):
            self.assertEqual((row["side"], row["line"], row["index"]), site)
            self.assertEqual(row["tokens4"], gram)
            self.assertEqual(row["tablet"], "I")
            self.assertTrue(row["in_cycle191_leftover_3"])
            self.assertTrue(row["in_cycle172_leftover_34"])
            self.assertFalse(row["inside_family"])
            self.assertEqual(row["N_I"], 1)
            self.assertEqual(row["N_off_I"], 0)
        near_stems = line_stems_for_site(
            self.i_sides,
            STANDING_NEAR_MISS_LEFTOVER_700_604_SITE,
        )
        near_index = STANDING_NEAR_MISS_LEFTOVER_700_604_SITE[2]
        self.assertEqual(
            site_previous_4gram(near_stems, near_index, CYCLE171_GRAM2),
            STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
        )
        self.assertNotIn(
            STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
            STANDING_SEQUENCES,
        )
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, STANDING_I_SITES_090)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, STANDING_I_SITES_999)
        self.assertNotIn(STANDING_NEAR_MISS_LEFTOVER_700_604_SITE, STANDING_I_SITES_040)
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        for n_on, locked in zip(self.n_i, standing_on, strict=True):
            if n_on != locked:
                self.fail("measured N_I drifted from the locked count")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_192_191_171_scoreboards_still_compute(self):
        """Cycle 192 I-only 3/0, 191 leftover-3, and 171 I-only 43/0 stay."""
        prior_192 = TestMamariI3gram700076071IOnlyScoreboard()
        prior_192.setUp()
        prior_192.test_i_hits_are_three_on_ia()
        prior_192.test_3gram_is_zero_off_i_and_i_only()
        prior_192.test_survey_matches_computed_lock()
        self.assertEqual(prior_192.i_hits, 3)
        self.assertEqual(prior_192.off_i_hits, 0)
        self.assertEqual(prior_192.i_sites, CYCLE192_I_SITES)
        self.assertEqual(CYCLE192_N_I, 3)
        self.assertEqual(CYCLE192_N_OFF_I, 0)
        prior_191 = TestMamariILeftover076071Previous700Scoreboard()
        prior_191.setUp()
        prior_191.test_counts_3_of_34_and_hypothesis_n_3_holds()
        prior_191.test_survey_matches_computed_lock()
        self.assertEqual(prior_191.n_with, 3)
        self.assertEqual(prior_191.n_leftover, 34)
        self.assertEqual(CYCLE191_N_WITH, 3)
        self.assertEqual(prior_191.with_sites, CYCLE191_MATCHING_SITES)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(len(prior_171.i_sites), 43)
        self.assertEqual(prior_171.i_sites, CYCLE171_I_SITES)
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_172 = TestMamariI2gram076071InsideFamilyScoreboard()
        prior_172.setUp()
        prior_172.test_forty_three_sites_split_9_inside_34_leftover_and_claim_loses()
        prior_172.test_survey_matches_computed_lock()
        self.assertEqual(prior_172.n_leftover, CYCLE172_N_LEFTOVER)
        self.assertEqual(CYCLE172_N_LEFTOVER, 34)
        prior_190 = TestMamariILeftover076071PreviousStemScoreboard()
        prior_190.setUp()
        prior_190.test_counts_28_distinct_previous_stems_and_claim_loses()
        prior_190.test_survey_matches_computed_lock()
        self.assertEqual(prior_190.n_distinct, CYCLE190_N_DISTINCT)
        self.assertEqual(CYCLE190_N_DISTINCT, 28)
        prior_187 = TestMamariI076071061Forward4gramsIOnlyScoreboard()
        prior_187.setUp()
        prior_187.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_187.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-193 previous-4 I-only lock."""
        lock = self.survey["i_700_076_071_previous_4grams_i_only"]
        self.assertEqual(lock["cycle"], 193)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I_3gram"], CYCLE192_N_I)
        self.assertEqual(lock["N_I_3gram"], 3)
        self.assertEqual(lock["N_off_I_3gram"], CYCLE192_N_OFF_I)
        self.assertEqual(lock["N_off_I_3gram"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle192_sites"]),
            STANDING_CYCLE192_SITES,
        )
        self.assertEqual(lock["leftover_matching_count"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_matching_sites"]),
            STANDING_LEFTOVER_076_071_SITES,
        )
        self.assertEqual(lock["inside_family_sites"], [])
        self.assertEqual(lock["inside_family_count"], 0)
        self.assertFalse(lock["inside_family_site_included"])
        self.assertEqual(tuple(lock["per_site_previous_stems"]), STANDING_PREVIOUS_STEMS)
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), 3)
        standing_on = (
            STANDING_N_I_090,
            STANDING_N_I_999,
            STANDING_N_I_040,
        )
        standing_off = (
            STANDING_N_OFF_I_090,
            STANDING_N_OFF_I_999,
            STANDING_N_OFF_I_040,
        )
        standing_hapax = (
            STANDING_HAPAX_090,
            STANDING_HAPAX_999,
            STANDING_HAPAX_040,
        )
        standing_off_sites = (
            STANDING_OFF_I_SITES_090,
            STANDING_OFF_I_SITES_999,
            STANDING_OFF_I_SITES_040,
        )
        for row, gram, site, prev, role, sites, n_on, n_off, hapax, off_sites in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CYCLE192_SITES,
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
            self.assertEqual(tuple(row["cycle192_site"]), site)
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
        self.assertEqual(lock["N_I_090"], STANDING_N_I_090)
        self.assertEqual(lock["N_off_I_090"], STANDING_N_OFF_I_090)
        self.assertEqual(lock["N_I_999"], STANDING_N_I_999)
        self.assertEqual(lock["N_off_I_999"], STANDING_N_OFF_I_999)
        self.assertEqual(lock["N_I_040"], STANDING_N_I_040)
        self.assertEqual(lock["N_off_I_040"], STANDING_N_OFF_I_040)
        self.assertEqual(
            tuple(lock["near_miss_leftover_700_604_site"]),
            STANDING_NEAR_MISS_LEFTOVER_700_604_SITE,
        )
        self.assertEqual(
            tuple(lock["near_miss_leftover_700_604_previous_4gram"]),
            STANDING_NEAR_MISS_LEFTOVER_700_604_PREVIOUS_4GRAM,
        )
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_700_076_071_previous_4grams_all_i_only"])
        self.assertTrue(lock["i_700_076_071_previous_4grams_i_only"])
        self.assertEqual(
            lock["i_700_076_071_previous_4grams_all_i_only"],
            STANDING_I_700_076_071_PREVIOUS_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle175_forward_4grams"])
        self.assertFalse(lock["same_as_cycle178_forward_4grams"])
        self.assertFalse(lock["same_as_cycle181_forward_4grams"])
        self.assertFalse(lock["same_as_cycle184_forward_4grams"])
        self.assertFalse(lock["same_as_cycle187_forward_4grams"])
        self.assertFalse(lock["same_as_cycle192"])
        self.assertTrue(lock["same_leftover_shape_as_cycle_175_178_181_184_187"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["near_miss_700_604_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_700_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_700_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_076_071_061_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_700_076_071_i_only"]["cycle"], 192)
        self.assertTrue(
            self.survey["i_3gram_700_076_071_i_only"]["i_3gram_700_076_071_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_700_076_071_i_only"]["N_I"], 3)
        self.assertEqual(self.survey["i_3gram_700_076_071_i_only"]["N_off_I"], 0)
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
        self.assertEqual(self.survey["i_leftover_076_071_previous_stem"]["cycle"], 190)
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_stem"]["N_distinct_previous_stems"],
            28,
        )
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["cycle"], 172)
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_076_071_061_forward_4grams_i_only"]["cycle"], 187)
        self.assertTrue(
            self.survey["i_076_071_061_forward_4grams_i_only"][
                "i_076_071_061_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"][
                "i_leftover_n4_exactly_4_contain_076_071"
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


class TestMamariI700076071Previous4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 193 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
