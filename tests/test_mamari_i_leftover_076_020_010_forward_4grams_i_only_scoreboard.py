"""I's cycle-162 leftover forward 4-grams off-I lock.

Cycle 165 text-search lock. Uses already-vendored A–V and the
cycle-162 leftover forward 4-grams of overlap 3-gram
076 020 010 (076 020 010 150 at Ia4[158],
076 020 010 090 at Ia5[56], 076 020 010 146 at Ia6[102],
076 020 010 076 at Ia13[48]). Does not retune those
4-grams, the leftover 3-gram, or those I sites. Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same leftover-shape as cycle 164 (leftover backward 4-grams
all I-only hapax 1/0), now the four forward 4-grams. Glyph
090 already appears as leftover n=4 maximal 090 076 020 010
(cycle 159). Sandwich 076 020 010 076 is the last of the
four. Context only; do not retune.

Locks exact consecutive hits of each leftover forward
4-gram on tablet I and on every other vendored tablet A–H
and J–V. Hypothesis: all four are I-only (N_on_I>=1 and
N_off_I=0). Measured: each N_on_I=1 at the leftover site
above; all N_off_I=0. Claim that can lose:
i_leftover_076_020_010_forward_4grams_all_i_only. True
only if ALL four have N_on_I>=1 and N_off_I=0. The claim
is true. Do not retune.

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
from tests.test_mamari_i_leftover_023_077_400_070_076_i_only_scoreboard import (
    GRAM4_023 as CYCLE158_GRAM4_023,
    GRAM4_077 as CYCLE158_GRAM4_077,
    TestMamariILeftover023077400070076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_020_010_backward_4grams_i_only_scoreboard import (
    TestMamariILeftover076020010Backward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_020_010_forward_4gram_scoreboard import (
    STANDING_FORWARD_4GRAM_076,
    STANDING_FORWARD_4GRAM_090,
    STANDING_FORWARD_4GRAM_146,
    STANDING_FORWARD_4GRAM_150,
    STANDING_N_DISTINCT_FORWARD_4GRAMS,
    STANDING_N_WITH_FORWARD,
    TestMamariILeftover076020010Forward4gramScoreboard,
)
from tests.test_mamari_i_leftover_633_006_076_011_090_i_only_scoreboard import (
    GRAM4_006 as CYCLE156_GRAM4_006,
    GRAM4_633 as CYCLE156_GRAM4_633,
    TestMamariILeftover633006076011090IOnlyScoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_020_010_i_only_scoreboard import (
    GRAM3,
    TestMamariIOverlap3gram076020010IOnlyScoreboard,
)
from tests.test_mamari_i_overlap_3gram_076_020_010_inside_family_scoreboard import (
    LEFTOVER_N4_090,
    STANDING_LEFTOVER_090_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_LEFTOVER,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    line_stems_for_site,
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
GRAM4_150 = STANDING_FORWARD_4GRAM_150
GRAM4_090 = STANDING_FORWARD_4GRAM_090
GRAM4_146 = STANDING_FORWARD_4GRAM_146
GRAM4_076 = STANDING_FORWARD_4GRAM_076
STANDING_SEQUENCES = (GRAM4_150, GRAM4_090, GRAM4_146, GRAM4_076)
STANDING_NEXT_STEMS = ("150", "090", "146", "076")
STANDING_N_ON_I_150 = 1
STANDING_N_ON_I_090 = 1
STANDING_N_ON_I_146 = 1
STANDING_N_ON_I_076 = 1
STANDING_I_SITES_150 = ((SIDE_IA, "Ia4", 158),)
STANDING_I_SITES_090 = ((SIDE_IA, "Ia5", 56),)
STANDING_I_SITES_146 = ((SIDE_IA, "Ia6", 102),)
STANDING_I_SITES_076 = ((SIDE_IA, "Ia13", 48),)
STANDING_I_SITES = (
    STANDING_I_SITES_150,
    STANDING_I_SITES_090,
    STANDING_I_SITES_146,
    STANDING_I_SITES_076,
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_150 = 0
STANDING_N_OFF_I_090 = 0
STANDING_N_OFF_I_146 = 0
STANDING_N_OFF_I_076 = 0
STANDING_OFF_I_SITES_150 = ()
STANDING_OFF_I_SITES_090 = ()
STANDING_OFF_I_SITES_146 = ()
STANDING_OFF_I_SITES_076 = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_020_010_forward_4grams_all_i_only"
STANDING_I_LEFTOVER_076_020_010_FORWARD_4GRAMS_ALL_I_ONLY = True
STANDING_RESULT = "i_leftover_076_020_010_forward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE154_LEFTOVER_4GRAMS = False
STANDING_SAME_AS_CYCLE156_LEFTOVER_4GRAMS = False
STANDING_SAME_AS_CYCLE158_LEFTOVER_4GRAMS = False
STANDING_SAME_AS_CYCLE164_LEFTOVER_4GRAMS = False
STANDING_SAME_LEFTOVER_SHAPE_AS_164 = True
STANDING_GLYPH_090_CONTEXT_ONLY = True
STANDING_SANDWICH_076_CONTEXT_ONLY = True
STANDING_CYCLE159_LEFTOVER_N4_090 = LEFTOVER_N4_090


def leftover_forward_4gram_start_site(
    leftover_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Forward 4-gram starts at the leftover 076 020 010 site."""
    return leftover_site


def sequence_is_i_only(n_on_i: int, n_off_i: int) -> bool:
    """True iff N_on_I>=1 and N_off_I=0."""
    return n_on_i >= 1 and n_off_i == 0


def i_leftover_076_020_010_forward_4grams_all_i_only(
    n_on_i_150: int,
    n_off_i_150: int,
    n_on_i_090: int,
    n_off_i_090: int,
    n_on_i_146: int,
    n_off_i_146: int,
    n_on_i_076: int,
    n_off_i_076: int,
) -> bool:
    """True iff all four leftover forward 4-grams are I-only."""
    return (
        sequence_is_i_only(n_on_i_150, n_off_i_150)
        and sequence_is_i_only(n_on_i_090, n_off_i_090)
        and sequence_is_i_only(n_on_i_146, n_off_i_146)
        and sequence_is_i_only(n_on_i_076, n_off_i_076)
    )


class TestILeftover076020010Forward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-162 leftover forward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4_150, ("076", "020", "010", "150"))
        self.assertEqual(GRAM4_090, ("076", "020", "010", "090"))
        self.assertEqual(GRAM4_146, ("076", "020", "010", "146"))
        self.assertEqual(GRAM4_076, ("076", "020", "010", "076"))
        self.assertEqual(GRAM4_150[:3], GRAM3)
        self.assertEqual(GRAM4_090[:3], GRAM3)
        self.assertEqual(GRAM4_146[:3], GRAM3)
        self.assertEqual(GRAM4_076[:3], GRAM3)
        adjacent = [list(GRAM4_150), list(GRAM4_090)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_150), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_090), 1)
        overlap = [["076", "020", "010", "150", "076", "020", "010", "150"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_150), 2)
        gapped = [list(GRAM4_150[:2]) + ["000"] + list(GRAM4_150[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_150), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_150), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_076), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all four leftover 4-grams are I-only."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_076_020_010_forward_4grams_all_i_only(1, 0, 1, 0, 1, 0, 1, 0)
        )
        self.assertTrue(
            i_leftover_076_020_010_forward_4grams_all_i_only(2, 0, 1, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_forward_4grams_all_i_only(1, 1, 1, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_forward_4grams_all_i_only(1, 0, 1, 1, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_forward_4grams_all_i_only(1, 0, 1, 0, 1, 1, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_forward_4grams_all_i_only(1, 0, 1, 0, 1, 0, 1, 1)
        )
        self.assertFalse(
            i_leftover_076_020_010_forward_4grams_all_i_only(0, 0, 1, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_forward_4grams_all_i_only(1, 0, 0, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_forward_4grams_all_i_only(0, 0, 0, 0, 0, 0, 0, 0)
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_020_010_forward_4grams_all_i_only")
        self.assertTrue(STANDING_I_LEFTOVER_076_020_010_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_020_010_FORWARD_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_162_leftovers_not_retuned(self):
        """4-grams stay the cycle-162 leftover set; none is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "020", "010"))
        self.assertEqual(STANDING_SEQUENCES, (GRAM4_150, GRAM4_090, GRAM4_146, GRAM4_076))
        self.assertEqual(STANDING_NEXT_STEMS, ("150", "090", "146", "076"))
        self.assertNotEqual(GRAM4_150, GRAM5)
        self.assertNotEqual(GRAM4_090, CYCLE156_GRAM4_633)
        self.assertNotEqual(GRAM4_146, CYCLE156_GRAM4_006)
        self.assertNotEqual(GRAM4_150, CYCLE158_GRAM4_023)
        self.assertNotEqual(GRAM4_076, CYCLE158_GRAM4_077)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(LEFTOVER_N4_090, ("090", "076", "020", "010"))
        self.assertEqual(STANDING_CYCLE159_LEFTOVER_N4_090, LEFTOVER_N4_090)
        self.assertNotEqual(GRAM4_090, LEFTOVER_N4_090)
        self.assertEqual(GRAM4_090[-1], LEFTOVER_N4_090[0])
        self.assertEqual(GRAM4_076[0], GRAM4_076[-1])
        self.assertEqual(GRAM4_076[-1], "076")
        for leftover, start in zip(
            STANDING_LEFTOVER_SITES,
            (
                STANDING_I_SITES_150[0],
                STANDING_I_SITES_090[0],
                STANDING_I_SITES_146[0],
                STANDING_I_SITES_076[0],
            ),
            strict=True,
        ):
            self.assertEqual(leftover_forward_4gram_start_site(leftover), start)
            self.assertEqual(leftover, start)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE154_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE156_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE158_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE164_LEFTOVER_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_164)
        self.assertTrue(STANDING_GLYPH_090_CONTEXT_ONLY)
        self.assertTrue(STANDING_SANDWICH_076_CONTEXT_ONLY)
        self.assertEqual(len(GRAM4_150), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076020010Forward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover forward-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.grams = STANDING_SEQUENCES
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in self.grams)
        self.n_on_i = tuple(
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
        self.claim_holds = i_leftover_076_020_010_forward_4grams_all_i_only(
            *sum(zip(self.n_on_i, self.n_off_i, strict=True), ())
        )

    def test_tokens_and_sites_are_cycle_162_lock_not_retuned(self):
        """4-grams and leftover sites stay the cycle-162 forward lock."""
        self.assertEqual(GRAM3, ("076", "020", "010"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(
            STANDING_LEFTOVER_SITES,
            (
                (SIDE_IA, "Ia4", 158),
                (SIDE_IA, "Ia5", 56),
                (SIDE_IA, "Ia6", 102),
                (SIDE_IA, "Ia13", 48),
            ),
        )
        prior_162 = self.survey["i_leftover_076_020_010_forward_4gram"]
        self.assertEqual(prior_162["cycle"], 162)
        self.assertEqual(tuple(prior_162["tokens3"]), GRAM3)
        self.assertEqual(prior_162["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_162["N_with_forward"], STANDING_N_WITH_FORWARD)
        self.assertEqual(
            prior_162["N_distinct_forward_4grams"],
            STANDING_N_DISTINCT_FORWARD_4GRAMS,
        )
        self.assertEqual(prior_162["N_distinct_forward_4grams"], 4)
        self.assertFalse(prior_162["i_leftover_076_020_010_share_one_forward_4gram"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_162["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_162["distinct_forward_4grams"]),
            STANDING_SEQUENCES,
        )
        prior_164 = self.survey["i_leftover_076_020_010_backward_4grams_i_only"]
        self.assertEqual(prior_164["cycle"], 164)
        self.assertTrue(prior_164["i_leftover_076_020_010_backward_4grams_all_i_only"])
        prior_163 = self.survey["i_leftover_076_020_010_backward_4gram"]
        self.assertEqual(prior_163["cycle"], 163)
        self.assertFalse(prior_163["i_leftover_076_020_010_share_one_backward_4gram"])
        prior_160 = self.survey["i_overlap_3gram_076_020_010_i_only"]
        self.assertEqual(prior_160["cycle"], 160)
        self.assertTrue(prior_160["i_overlap_3gram_076_020_010_is_i_only"])
        prior_159 = self.survey["i_leftover_n4_independent_n5_n3_overlap"]
        self.assertEqual(prior_159["cycle"], 159)
        self.assertTrue(
            prior_159["i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"]
        )
        prior_158 = self.survey["i_leftover_023_077_400_070_076_i_only"]
        self.assertEqual(prior_158["cycle"], 158)
        self.assertTrue(prior_158["i_leftover_023_077_400_070_076_both_i_only"])
        prior_156 = self.survey["i_leftover_633_006_076_011_090_i_only"]
        self.assertEqual(prior_156["cycle"], 156)
        self.assertTrue(prior_156["i_leftover_633_006_076_011_090_both_i_only"])
        self.assertEqual(LEFTOVER_N4_090, ("090", "076", "020", "010"))
        self.assertEqual(STANDING_LEFTOVER_090_SITES[0], (SIDE_IA, "Ia2", 119))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_on_I=1/1/1/1, N_off_I=0/0/0/0. All I-only. Claim holds."""
        standing_on = (
            STANDING_N_ON_I_150,
            STANDING_N_ON_I_090,
            STANDING_N_ON_I_146,
            STANDING_N_ON_I_076,
        )
        standing_off = (
            STANDING_N_OFF_I_150,
            STANDING_N_OFF_I_090,
            STANDING_N_OFF_I_146,
            STANDING_N_OFF_I_076,
        )
        standing_sites = STANDING_I_SITES
        self.assertEqual(self.i_sites, standing_sites)
        self.assertEqual(self.n_on_i, standing_on)
        self.assertEqual(standing_on, (1, 1, 1, 1))
        self.assertEqual(self.n_off_i, standing_off)
        self.assertEqual(standing_off, (0, 0, 0, 0))
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        for leftover, start, gram, nxt in zip(
            STANDING_LEFTOVER_SITES,
            (
                STANDING_I_SITES_150[0],
                STANDING_I_SITES_090[0],
                STANDING_I_SITES_146[0],
                STANDING_I_SITES_076[0],
            ),
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            strict=True,
        ):
            self.assertEqual(leftover_forward_4gram_start_site(leftover), start)
            self.assertEqual(leftover, start)
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2] + STANDING_N3], nxt)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N3]), GRAM3)
            leftover_stems = line_stems_for_site(self.i_sides, leftover)
            self.assertEqual(
                tuple(leftover_stems[leftover[2] : leftover[2] + STANDING_N3]),
                GRAM3,
            )
            self.assertEqual(leftover_stems[leftover[2] + STANDING_N3], nxt)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram, LEFTOVER_N4_090)
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
            i_leftover_076_020_010_forward_4grams_all_i_only(
                *sum(zip(self.n_on_i, self.n_off_i, strict=True), ())
            ),
            STANDING_I_LEFTOVER_076_020_010_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_020_010_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_020_010_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(
            STANDING_CLAIM, "i_leftover_076_020_010_forward_4grams_all_i_only"
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE154_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE156_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE158_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE164_LEFTOVER_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_164)
        self.assertTrue(STANDING_GLYPH_090_CONTEXT_ONLY)
        self.assertTrue(STANDING_SANDWICH_076_CONTEXT_ONLY)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_164_162_160_158_156_103_and_w_scoreboards_still_compute(self):
        """Cycle 164 backward I-only, 162 forward, 160 I-only, 158/156, 103, W stay."""
        prior_164 = TestMamariILeftover076020010Backward4gramsIOnlyScoreboard()
        prior_164.setUp()
        prior_164.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_164.test_survey_matches_computed_lock()
        prior_162 = TestMamariILeftover076020010Forward4gramScoreboard()
        prior_162.setUp()
        prior_162.test_four_leftovers_have_four_distinct_forwards_and_claim_loses()
        prior_162.test_survey_matches_computed_lock()
        prior_160 = TestMamariIOverlap3gram076020010IOnlyScoreboard()
        prior_160.setUp()
        prior_160.test_i_hits_are_twelve_on_ia()
        prior_160.test_3gram_is_zero_off_i_and_i_only()
        prior_160.test_survey_matches_computed_lock()
        prior_158 = TestMamariILeftover023077400070076IOnlyScoreboard()
        prior_158.setUp()
        prior_158.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_158.test_survey_matches_computed_lock()
        prior_156 = TestMamariILeftover633006076011090IOnlyScoreboard()
        prior_156.setUp()
        prior_156.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_156.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-165 leftover forward-4 I-only lock."""
        lock = self.survey["i_leftover_076_020_010_forward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 165)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle162_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_forward"], STANDING_N_WITH_FORWARD)
        self.assertEqual(lock["N_distinct_forward_4grams"], 4)
        self.assertEqual(tuple(lock["per_site_next_stems"]), STANDING_NEXT_STEMS)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 4)
        standing_sites = (
            STANDING_I_SITES_150,
            STANDING_I_SITES_090,
            STANDING_I_SITES_146,
            STANDING_I_SITES_076,
        )
        standing_on = (
            STANDING_N_ON_I_150,
            STANDING_N_ON_I_090,
            STANDING_N_ON_I_146,
            STANDING_N_ON_I_076,
        )
        standing_off = (
            STANDING_N_OFF_I_150,
            STANDING_N_OFF_I_090,
            STANDING_N_OFF_I_146,
            STANDING_N_OFF_I_076,
        )
        for row, gram, leftover, nxt, sites, n_on, n_off in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_LEFTOVER_SITES,
            STANDING_NEXT_STEMS,
            standing_sites,
            standing_on,
            standing_off,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle162_site"]), leftover)
            self.assertEqual(row["next_stem"], nxt)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_on_I"], 1)
            self.assertEqual(row["ia_hits"], 1)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site) for site in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site) for site in row["ib_sites"]),
                STANDING_IB_SITES,
            )
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(
                tuple(row["hits_by_tablet"]),
                STANDING_HITS_BY_TABLET_ONE_ON_I,
            )
            self.assertTrue(row["i_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_076_020_010_forward_4grams_all_i_only"])
        self.assertEqual(
            lock["i_leftover_076_020_010_forward_4grams_all_i_only"],
            STANDING_I_LEFTOVER_076_020_010_FORWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle154_leftover_4grams"])
        self.assertFalse(lock["same_as_cycle156_leftover_4grams"])
        self.assertFalse(lock["same_as_cycle158_leftover_4grams"])
        self.assertFalse(lock["same_as_cycle164_leftover_4grams"])
        self.assertTrue(lock["same_leftover_shape_as_cycle_164"])
        self.assertTrue(lock["glyph_090_also_leftover_n4_maximal_090_076_020_010"])
        self.assertEqual(tuple(lock["leftover_n4_090_tokens"]), LEFTOVER_N4_090)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_090_sites"]),
            STANDING_LEFTOVER_090_SITES,
        )
        self.assertTrue(lock["sandwich_076_020_010_076_is_last_of_four"])
        self.assertEqual(tuple(lock["sandwich_tokens4"]), GRAM4_076)
        self.assertTrue(lock["glyph_090_and_sandwich_076_context_only"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_backward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_backward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_forward_4gram_unchanged"])
        self.assertTrue(
            lock["standing_i_overlap_3gram_076_020_010_inside_family_unchanged"]
        )
        self.assertTrue(lock["standing_i_overlap_3gram_076_020_010_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_023_077_400_070_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_633_006_076_011_090_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_independent_n5_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_leftover_090_700_430_076_006_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_backward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_forward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_inside_two_5grams_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_independent_n5_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_independent_nge4_maximals_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_076_020_010_backward_4grams_i_only"]["cycle"], 164
        )
        self.assertTrue(
            self.survey["i_leftover_076_020_010_backward_4grams_i_only"][
                "i_leftover_076_020_010_backward_4grams_all_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_020_010_backward_4gram"]["cycle"], 163
        )
        self.assertFalse(
            self.survey["i_leftover_076_020_010_backward_4gram"][
                "i_leftover_076_020_010_share_one_backward_4gram"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_020_010_forward_4gram"]["cycle"], 162
        )
        self.assertFalse(
            self.survey["i_leftover_076_020_010_forward_4gram"][
                "i_leftover_076_020_010_share_one_forward_4gram"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_020_010_forward_4gram"][
                "N_distinct_forward_4grams"
            ],
            4,
        )
        self.assertEqual(
            self.survey["i_overlap_3gram_076_020_010_inside_family"]["cycle"], 161
        )
        self.assertFalse(
            self.survey["i_overlap_3gram_076_020_010_inside_family"][
                "i_overlap_3gram_076_020_010_all_inside_known_family"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_i_only"]["cycle"], 160)
        self.assertTrue(
            self.survey["i_overlap_3gram_076_020_010_i_only"][
                "i_overlap_3gram_076_020_010_is_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"]["cycle"], 159
        )
        self.assertTrue(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"][
                "i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_023_077_400_070_076_i_only"]["cycle"], 158
        )
        self.assertTrue(
            self.survey["i_leftover_023_077_400_070_076_i_only"][
                "i_leftover_023_077_400_070_076_both_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_633_006_076_011_090_i_only"]["cycle"], 156
        )
        self.assertTrue(
            self.survey["i_leftover_633_006_076_011_090_i_only"][
                "i_leftover_633_006_076_011_090_both_i_only"
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


class TestMamariILeftover076020010Forward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 165 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
