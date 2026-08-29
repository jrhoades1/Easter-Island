"""I's cycle-163 leftover backward 4-grams off-I lock.

Cycle 164 text-search lock. Uses already-vendored A–V and the
cycle-163 leftover backward 4-grams of overlap 3-gram
076 020 010 (633 076 020 010 at Ia4[157],
208 076 020 010 at Ia5[55], 005 076 020 010 at Ia6[101],
536 076 020 010 at Ia13[47]). Does not retune those
4-grams, the leftover 3-gram, or those I sites. Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same leftover-shape as cycles 154/156/158 (leftover prefix
4-grams both I-only hapax 1/0), now four sequences instead
of two. Glyph 633 already appears as previous stem of
independent 5-gram 076 011 090 090 076 at Ia12[39]
(cycle 155). Context only; do not retune.

Locks exact consecutive hits of each leftover backward
4-gram on tablet I and on every other vendored tablet A–H
and J–V. Hypothesis: all four are I-only (N_on_I>=1 and
N_off_I=0). Measured: each N_on_I=1 at the start site
above; all N_off_I=0. Claim that can lose:
i_leftover_076_020_010_backward_4grams_all_i_only. True
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
from tests.test_mamari_i_independent_076_011_090_090_076_previous_stem_scoreboard import (
    STANDING_I_SITES as STANDING_CYCLE155_SITES,
    STEM_633,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_011,
)
from tests.test_mamari_i_leftover_023_077_400_070_076_i_only_scoreboard import (
    GRAM4_023 as CYCLE158_GRAM4_023,
    GRAM4_077 as CYCLE158_GRAM4_077,
    TestMamariILeftover023077400070076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_020_010_backward_4gram_scoreboard import (
    STANDING_BACKWARD_4GRAM_005,
    STANDING_BACKWARD_4GRAM_208,
    STANDING_BACKWARD_4GRAM_536,
    STANDING_BACKWARD_4GRAM_633,
    STANDING_N_DISTINCT_BACKWARD_4GRAMS,
    STANDING_N_WITH_BACKWARD,
    TestMamariILeftover076020010Backward4gramScoreboard,
)
from tests.test_mamari_i_leftover_090_700_430_076_006_i_only_scoreboard import (
    leftover_prefix_4gram_start_site,
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
GRAM4_633 = STANDING_BACKWARD_4GRAM_633
GRAM4_208 = STANDING_BACKWARD_4GRAM_208
GRAM4_005 = STANDING_BACKWARD_4GRAM_005
GRAM4_536 = STANDING_BACKWARD_4GRAM_536
STANDING_SEQUENCES = (GRAM4_633, GRAM4_208, GRAM4_005, GRAM4_536)
STANDING_PREVIOUS_STEMS = ("633", "208", "005", "536")
STANDING_N_ON_I_633 = 1
STANDING_N_ON_I_208 = 1
STANDING_N_ON_I_005 = 1
STANDING_N_ON_I_536 = 1
STANDING_I_SITES_633 = ((SIDE_IA, "Ia4", 157),)
STANDING_I_SITES_208 = ((SIDE_IA, "Ia5", 55),)
STANDING_I_SITES_005 = ((SIDE_IA, "Ia6", 101),)
STANDING_I_SITES_536 = ((SIDE_IA, "Ia13", 47),)
STANDING_I_SITES = (
    STANDING_I_SITES_633,
    STANDING_I_SITES_208,
    STANDING_I_SITES_005,
    STANDING_I_SITES_536,
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_633 = 0
STANDING_N_OFF_I_208 = 0
STANDING_N_OFF_I_005 = 0
STANDING_N_OFF_I_536 = 0
STANDING_OFF_I_SITES_633 = ()
STANDING_OFF_I_SITES_208 = ()
STANDING_OFF_I_SITES_005 = ()
STANDING_OFF_I_SITES_536 = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_020_010_backward_4grams_all_i_only"
STANDING_I_LEFTOVER_076_020_010_BACKWARD_4GRAMS_ALL_I_ONLY = True
STANDING_RESULT = "i_leftover_076_020_010_backward_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE154_LEFTOVER_4GRAMS = False
STANDING_SAME_AS_CYCLE156_LEFTOVER_4GRAMS = False
STANDING_SAME_AS_CYCLE158_LEFTOVER_4GRAMS = False
STANDING_SAME_LEFTOVER_SHAPE_AS_154_156_158 = True
STANDING_GLYPH_633_CONTEXT_ONLY = True
STANDING_CYCLE155_633_SITE = (SIDE_IA, "Ia12", 39)


def sequence_is_i_only(n_on_i: int, n_off_i: int) -> bool:
    """True iff N_on_I>=1 and N_off_I=0."""
    return n_on_i >= 1 and n_off_i == 0


def i_leftover_076_020_010_backward_4grams_all_i_only(
    n_on_i_633: int,
    n_off_i_633: int,
    n_on_i_208: int,
    n_off_i_208: int,
    n_on_i_005: int,
    n_off_i_005: int,
    n_on_i_536: int,
    n_off_i_536: int,
) -> bool:
    """True iff all four leftover backward 4-grams are I-only."""
    return (
        sequence_is_i_only(n_on_i_633, n_off_i_633)
        and sequence_is_i_only(n_on_i_208, n_off_i_208)
        and sequence_is_i_only(n_on_i_005, n_off_i_005)
        and sequence_is_i_only(n_on_i_536, n_off_i_536)
    )


class TestILeftover076020010Backward4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-163 leftover backward 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4_633, ("633", "076", "020", "010"))
        self.assertEqual(GRAM4_208, ("208", "076", "020", "010"))
        self.assertEqual(GRAM4_005, ("005", "076", "020", "010"))
        self.assertEqual(GRAM4_536, ("536", "076", "020", "010"))
        self.assertEqual(GRAM4_633[1:], GRAM3)
        self.assertEqual(GRAM4_208[1:], GRAM3)
        self.assertEqual(GRAM4_005[1:], GRAM3)
        self.assertEqual(GRAM4_536[1:], GRAM3)
        adjacent = [list(GRAM4_633), list(GRAM4_208)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_633), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_208), 1)
        overlap = [["633", "076", "020", "010", "633", "076", "020", "010"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_633), 2)
        gapped = [list(GRAM4_633[:2]) + ["000"] + list(GRAM4_633[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_633), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_633), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_536), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all four leftover 4-grams are I-only."""
        provider = MockProvider()
        self.assertTrue(
            i_leftover_076_020_010_backward_4grams_all_i_only(1, 0, 1, 0, 1, 0, 1, 0)
        )
        self.assertTrue(
            i_leftover_076_020_010_backward_4grams_all_i_only(2, 0, 1, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_backward_4grams_all_i_only(1, 1, 1, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_backward_4grams_all_i_only(1, 0, 1, 1, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_backward_4grams_all_i_only(1, 0, 1, 0, 1, 1, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_backward_4grams_all_i_only(1, 0, 1, 0, 1, 0, 1, 1)
        )
        self.assertFalse(
            i_leftover_076_020_010_backward_4grams_all_i_only(0, 0, 1, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_backward_4grams_all_i_only(1, 0, 0, 0, 1, 0, 1, 0)
        )
        self.assertFalse(
            i_leftover_076_020_010_backward_4grams_all_i_only(0, 0, 0, 0, 0, 0, 0, 0)
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_020_010_backward_4grams_all_i_only")
        self.assertTrue(STANDING_I_LEFTOVER_076_020_010_BACKWARD_4GRAMS_ALL_I_ONLY)
        self.assertEqual(
            STANDING_I_LEFTOVER_076_020_010_BACKWARD_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_163_leftovers_not_retuned(self):
        """4-grams stay the cycle-163 leftover set; none is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "020", "010"))
        self.assertEqual(STANDING_SEQUENCES, (GRAM4_633, GRAM4_208, GRAM4_005, GRAM4_536))
        self.assertEqual(STANDING_PREVIOUS_STEMS, ("633", "208", "005", "536"))
        self.assertNotEqual(GRAM4_633, GRAM5)
        self.assertNotEqual(GRAM4_633, CYCLE156_GRAM4_633)
        self.assertNotEqual(GRAM4_208, CYCLE156_GRAM4_006)
        self.assertNotEqual(GRAM4_633, CYCLE158_GRAM4_023)
        self.assertNotEqual(GRAM4_536, CYCLE158_GRAM4_077)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(CYCLE156_GRAM4_633, ("633", "076", "011", "090"))
        self.assertEqual(MAXIMAL_N5_011, ("076", "011", "090", "090", "076"))
        self.assertEqual(STANDING_CYCLE155_SITES[0], STANDING_CYCLE155_633_SITE)
        self.assertEqual(STEM_633, "633")
        self.assertEqual(GRAM4_633[0], STEM_633)
        self.assertNotEqual(GRAM4_633[1:], MAXIMAL_N5_011[:3])
        for leftover, start in zip(
            STANDING_LEFTOVER_SITES,
            (
                STANDING_I_SITES_633[0],
                STANDING_I_SITES_208[0],
                STANDING_I_SITES_005[0],
                STANDING_I_SITES_536[0],
            ),
            strict=True,
        ):
            self.assertEqual(leftover_prefix_4gram_start_site(leftover), start)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE154_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE156_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE158_LEFTOVER_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_154_156_158)
        self.assertTrue(STANDING_GLYPH_633_CONTEXT_ONLY)
        self.assertEqual(len(GRAM4_633), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076020010Backward4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover backward-4 off-I lock. Mock only."""

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
        self.claim_holds = i_leftover_076_020_010_backward_4grams_all_i_only(
            *sum(zip(self.n_on_i, self.n_off_i, strict=True), ())
        )

    def test_tokens_and_sites_are_cycle_163_lock_not_retuned(self):
        """4-grams and leftover sites stay the cycle-163 backward lock."""
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
        prior_163 = self.survey["i_leftover_076_020_010_backward_4gram"]
        self.assertEqual(prior_163["cycle"], 163)
        self.assertEqual(tuple(prior_163["tokens3"]), GRAM3)
        self.assertEqual(prior_163["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_163["N_with_backward"], STANDING_N_WITH_BACKWARD)
        self.assertEqual(
            prior_163["N_distinct_backward_4grams"],
            STANDING_N_DISTINCT_BACKWARD_4GRAMS,
        )
        self.assertEqual(prior_163["N_distinct_backward_4grams"], 4)
        self.assertFalse(prior_163["i_leftover_076_020_010_share_one_backward_4gram"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_163["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_163["distinct_backward_4grams"]),
            STANDING_SEQUENCES,
        )
        prior_162 = self.survey["i_leftover_076_020_010_forward_4gram"]
        self.assertEqual(prior_162["cycle"], 162)
        self.assertFalse(prior_162["i_leftover_076_020_010_share_one_forward_4gram"])
        prior_160 = self.survey["i_overlap_3gram_076_020_010_i_only"]
        self.assertEqual(prior_160["cycle"], 160)
        self.assertTrue(prior_160["i_overlap_3gram_076_020_010_is_i_only"])
        prior_158 = self.survey["i_leftover_023_077_400_070_076_i_only"]
        self.assertEqual(prior_158["cycle"], 158)
        self.assertTrue(prior_158["i_leftover_023_077_400_070_076_both_i_only"])
        prior_156 = self.survey["i_leftover_633_006_076_011_090_i_only"]
        self.assertEqual(prior_156["cycle"], 156)
        self.assertTrue(prior_156["i_leftover_633_006_076_011_090_both_i_only"])
        prior_155 = self.survey["i_independent_076_011_090_090_076_previous_stem"]
        self.assertEqual(prior_155["cycle"], 155)
        self.assertEqual(tuple(prior_155["i_sites"][0]), STANDING_CYCLE155_633_SITE)
        self.assertEqual(prior_155["per_site_previous_stems"][0], STEM_633)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_on_I=1/1/1/1, N_off_I=0/0/0/0. All I-only. Claim holds."""
        standing_on = (
            STANDING_N_ON_I_633,
            STANDING_N_ON_I_208,
            STANDING_N_ON_I_005,
            STANDING_N_ON_I_536,
        )
        standing_off = (
            STANDING_N_OFF_I_633,
            STANDING_N_OFF_I_208,
            STANDING_N_OFF_I_005,
            STANDING_N_OFF_I_536,
        )
        standing_sites = STANDING_I_SITES
        self.assertEqual(self.i_sites, standing_sites)
        self.assertEqual(self.n_on_i, standing_on)
        self.assertEqual(standing_on, (1, 1, 1, 1))
        self.assertEqual(self.n_off_i, standing_off)
        self.assertEqual(standing_off, (0, 0, 0, 0))
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        for leftover, start, gram, prev in zip(
            STANDING_LEFTOVER_SITES,
            (
                STANDING_I_SITES_633[0],
                STANDING_I_SITES_208[0],
                STANDING_I_SITES_005[0],
                STANDING_I_SITES_536[0],
            ),
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
            strict=True,
        ):
            self.assertEqual(leftover_prefix_4gram_start_site(leftover), start)
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2]], prev)
            self.assertEqual(tuple(stems[start[2] + 1 : start[2] + 4]), GRAM3)
            leftover_stems = line_stems_for_site(self.i_sides, leftover)
            self.assertEqual(
                tuple(leftover_stems[leftover[2] : leftover[2] + STANDING_N3]),
                GRAM3,
            )
            self.assertEqual(leftover_stems[leftover[2] - 1], prev)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram, CYCLE156_GRAM4_633)
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
            i_leftover_076_020_010_backward_4grams_all_i_only(
                *sum(zip(self.n_on_i, self.n_off_i, strict=True), ())
            ),
            STANDING_I_LEFTOVER_076_020_010_BACKWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_020_010_BACKWARD_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_I_LEFTOVER_076_020_010_BACKWARD_4GRAMS_ALL_I_ONLY)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(
            STANDING_CLAIM, "i_leftover_076_020_010_backward_4grams_all_i_only"
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE154_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE156_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE158_LEFTOVER_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_154_156_158)
        self.assertTrue(STANDING_GLYPH_633_CONTEXT_ONLY)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_163_162_160_158_156_103_and_w_scoreboards_still_compute(self):
        """Cycle 163 backward, 162 forward, 160 I-only, 158/156, 103, W stay."""
        prior_163 = TestMamariILeftover076020010Backward4gramScoreboard()
        prior_163.setUp()
        prior_163.test_four_leftovers_have_four_distinct_backwards_and_claim_loses()
        prior_163.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-164 leftover backward-4 I-only lock."""
        lock = self.survey["i_leftover_076_020_010_backward_4grams_i_only"]
        self.assertEqual(lock["cycle"], 164)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle163_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_backward"], STANDING_N_WITH_BACKWARD)
        self.assertEqual(lock["N_distinct_backward_4grams"], 4)
        self.assertEqual(tuple(lock["per_site_previous_stems"]), STANDING_PREVIOUS_STEMS)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 4)
        standing_sites = (
            STANDING_I_SITES_633,
            STANDING_I_SITES_208,
            STANDING_I_SITES_005,
            STANDING_I_SITES_536,
        )
        standing_on = (
            STANDING_N_ON_I_633,
            STANDING_N_ON_I_208,
            STANDING_N_ON_I_005,
            STANDING_N_ON_I_536,
        )
        standing_off = (
            STANDING_N_OFF_I_633,
            STANDING_N_OFF_I_208,
            STANDING_N_OFF_I_005,
            STANDING_N_OFF_I_536,
        )
        for row, gram, leftover, prev, sites, n_on, n_off in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_LEFTOVER_SITES,
            STANDING_PREVIOUS_STEMS,
            standing_sites,
            standing_on,
            standing_off,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle163_site"]), leftover)
            self.assertEqual(row["previous_stem"], prev)
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
        self.assertTrue(lock["i_leftover_076_020_010_backward_4grams_all_i_only"])
        self.assertEqual(
            lock["i_leftover_076_020_010_backward_4grams_all_i_only"],
            STANDING_I_LEFTOVER_076_020_010_BACKWARD_4GRAMS_ALL_I_ONLY,
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
        self.assertTrue(lock["same_leftover_shape_as_cycles_154_156_158"])
        self.assertTrue(lock["glyph_633_also_previous_stem_of_independent_n5_011"])
        self.assertEqual(tuple(lock["cycle155_633_site"]), STANDING_CYCLE155_633_SITE)
        self.assertTrue(lock["glyph_633_context_only"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_backward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_forward_4gram_unchanged"])
        self.assertTrue(
            lock["standing_i_overlap_3gram_076_020_010_inside_family_unchanged"]
        )
        self.assertTrue(lock["standing_i_overlap_3gram_076_020_010_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_023_077_400_070_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_633_006_076_011_090_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_independent_076_011_090_090_076_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_090_700_430_076_006_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_backward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_forward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_inside_two_5grams_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_010_079_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_n4_independent_n5_n3_overlap_unchanged"]
        )
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
            self.survey["i_leftover_076_020_010_backward_4gram"]["cycle"], 163
        )
        self.assertFalse(
            self.survey["i_leftover_076_020_010_backward_4gram"][
                "i_leftover_076_020_010_share_one_backward_4gram"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_020_010_backward_4gram"][
                "N_distinct_backward_4grams"
            ],
            4,
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
        self.assertEqual(
            self.survey["i_independent_076_011_090_090_076_previous_stem"]["cycle"],
            155,
        )
        self.assertEqual(
            tuple(
                self.survey["i_independent_076_011_090_090_076_previous_stem"][
                    "i_sites"
                ][0]
            ),
            STANDING_CYCLE155_633_SITE,
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


class TestMamariILeftover076020010Backward4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 164 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
