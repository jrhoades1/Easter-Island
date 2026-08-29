"""I's cycle-153 leftover prefix 4-grams off-I lock.

Cycle 154 text-search lock. Uses already-vendored A–V and the
cycle-153 leftover prefix 4-grams of independent 5-gram
430 076 006 000 076 (090 430 076 006 at Ia1[128],
700 430 076 006 at Ia14[161]). Does not retune those
4-grams, the independent 5-gram, or those I sites. Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Glyph 700 is already the last stem of independent 5-gram
076 010 079 006 700 (cycles 140–152). Glyph 090 is already
the last stem of leftover 5-gram 072 076 010 079 090
(cycle 150). Context only; do not retune those sequences.

Locks exact consecutive hits of each leftover prefix 4-gram
on tablet I and on every other vendored tablet A–H and J–V.
Hypothesis: both are I-only (N_on_I>=1 and N_off_I=0).
Measured: 090 430 076 006 N_on_I=1 at Ia1[128];
700 430 076 006 N_on_I=1 at Ia14[161]; both N_off_I=0.
Claim that can lose: i_leftover_090_700_430_076_006_both_i_only.
True only if both have N_on_I>=1 and N_off_I=0. The claim
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
from tests.test_mamari_i_072_forward_5grams_i_only_scoreboard import (
    GRAM5_090 as CYCLE150_LEFTOVER_5GRAM_090,
    TestMamariI072Forward5gramsIOnlyScoreboard,
)
from tests.test_mamari_i_4gram_630_076_010_079_i_only_scoreboard import (
    TestMamariI4gram630076010079IOnlyScoreboard,
)
from tests.test_mamari_i_independent_430_076_006_000_076_previous_stem_scoreboard import (
    STANDING_I_SITES as STANDING_CYCLE153_SITES,
    STANDING_PER_SITE_PREVIOUS,
    STEM_090,
    STEM_700,
    TestMamariIIndependent430076006000076PreviousStemScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
    MAXIMAL_N5_430,
)
from tests.test_mamari_i_leftover_backward_5grams_i_only_scoreboard import (
    TestMamariILeftoverBackward5gramsIOnlyScoreboard,
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

HYPOTHESIS_BOTH_I_ONLY = True
STANDING_N4 = 4
GRAM5_INDEPENDENT = MAXIMAL_N5_430
GRAM4_090 = (STEM_090, "430", "076", "006")
GRAM4_700 = (STEM_700, "430", "076", "006")
STANDING_SEQUENCES = (GRAM4_090, GRAM4_700)
STANDING_N_ON_I_090 = 1
STANDING_N_ON_I_700 = 1
STANDING_I_SITES_090 = ((SIDE_IA, "Ia1", 128),)
STANDING_I_SITES_700 = ((SIDE_IA, "Ia14", 161),)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_090 = 0
STANDING_N_OFF_I_700 = 0
STANDING_OFF_I_SITES_090 = ()
STANDING_OFF_I_SITES_700 = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_090 = tuple(
    STANDING_N_ON_I_090 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET_700 = tuple(
    STANDING_N_ON_I_700 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_090_700_430_076_006_both_i_only"
STANDING_I_LEFTOVER_090_700_430_076_006_BOTH_I_ONLY = True
STANDING_RESULT = "i_leftover_090_700_430_076_006_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE150_LEFTOVER_5GRAM_090 = False
STANDING_SAME_AS_INDEPENDENT_N5_700 = False
INDEPENDENT_TO_4GRAM_OFFSET = 1


def leftover_prefix_4gram_start_site(
    independent_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """4-gram starts one stem before independent 430 076 006 000 076."""
    side, line, index = independent_site
    return (side, line, index - INDEPENDENT_TO_4GRAM_OFFSET)


def sequence_is_i_only(n_on_i: int, n_off_i: int) -> bool:
    """True iff N_on_I>=1 and N_off_I=0."""
    return n_on_i >= 1 and n_off_i == 0


def i_leftover_090_700_430_076_006_both_i_only(
    n_on_i_090: int,
    n_off_i_090: int,
    n_on_i_700: int,
    n_off_i_700: int,
) -> bool:
    """True iff both leftover prefix 4-grams are I-only."""
    return sequence_is_i_only(n_on_i_090, n_off_i_090) and sequence_is_i_only(
        n_on_i_700, n_off_i_700
    )


class TestILeftover090700430076006IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-153 leftover prefix 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4_090, ("090", "430", "076", "006"))
        self.assertEqual(GRAM4_700, ("700", "430", "076", "006"))
        self.assertEqual(GRAM4_090[1:], GRAM5_INDEPENDENT[:3])
        self.assertEqual(GRAM4_700[1:], GRAM5_INDEPENDENT[:3])
        adjacent = [list(GRAM4_090), list(GRAM4_700)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_090), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_700), 1)
        overlap = [["090", "430", "076", "006", "090", "430", "076", "006"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_090), 2)
        gapped = [list(GRAM4_090[:2]) + ["000"] + list(GRAM4_090[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_090), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_700), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_both_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when both leftover 4-grams are I-only."""
        provider = MockProvider()
        self.assertTrue(i_leftover_090_700_430_076_006_both_i_only(1, 0, 1, 0))
        self.assertTrue(i_leftover_090_700_430_076_006_both_i_only(2, 0, 1, 0))
        self.assertFalse(i_leftover_090_700_430_076_006_both_i_only(1, 1, 1, 0))
        self.assertFalse(i_leftover_090_700_430_076_006_both_i_only(1, 0, 1, 1))
        self.assertFalse(i_leftover_090_700_430_076_006_both_i_only(0, 0, 1, 0))
        self.assertFalse(i_leftover_090_700_430_076_006_both_i_only(1, 0, 0, 0))
        self.assertFalse(i_leftover_090_700_430_076_006_both_i_only(0, 0, 0, 0))
        self.assertFalse(i_leftover_090_700_430_076_006_both_i_only(1, 1, 1, 1))
        self.assertEqual(STANDING_CLAIM, "i_leftover_090_700_430_076_006_both_i_only")
        self.assertTrue(STANDING_I_LEFTOVER_090_700_430_076_006_BOTH_I_ONLY)
        self.assertEqual(
            STANDING_I_LEFTOVER_090_700_430_076_006_BOTH_I_ONLY,
            HYPOTHESIS_BOTH_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_153_leftovers_not_retuned(self):
        """4-grams stay the cycle-153 pair; neither is a retuned 5-gram."""
        provider = MockProvider()
        self.assertEqual(GRAM4_090, (STEM_090, "430", "076", "006"))
        self.assertEqual(GRAM4_700, (STEM_700, "430", "076", "006"))
        self.assertEqual(STANDING_SEQUENCES, (GRAM4_090, GRAM4_700))
        self.assertNotEqual(GRAM4_090, GRAM5)
        self.assertNotEqual(GRAM4_700, GRAM5)
        self.assertNotEqual(GRAM4_090, GRAM5_INDEPENDENT)
        self.assertNotEqual(GRAM4_700, GRAM5_INDEPENDENT)
        self.assertNotEqual(GRAM4_090, CYCLE150_LEFTOVER_5GRAM_090)
        self.assertNotEqual(GRAM4_700, MAXIMAL_N5_010)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(GRAM5_INDEPENDENT, ("430", "076", "006", "000", "076"))
        self.assertEqual(CYCLE150_LEFTOVER_5GRAM_090, ("072", "076", "010", "079", "090"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertEqual(CYCLE150_LEFTOVER_5GRAM_090[-1], STEM_090)
        self.assertEqual(MAXIMAL_N5_010[-1], STEM_700)
        self.assertTrue(is_contiguous_substring(GRAM4_090[1:], GRAM5_INDEPENDENT))
        self.assertTrue(is_contiguous_substring(GRAM4_700[1:], GRAM5_INDEPENDENT))
        self.assertFalse(is_contiguous_substring(GRAM4_090, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM4_700, GRAM5))
        self.assertEqual(
            leftover_prefix_4gram_start_site((SIDE_IA, "Ia1", 129)),
            (SIDE_IA, "Ia1", 128),
        )
        self.assertEqual(
            leftover_prefix_4gram_start_site((SIDE_IA, "Ia14", 162)),
            (SIDE_IA, "Ia14", 161),
        )
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE150_LEFTOVER_5GRAM_090)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5_700)
        self.assertEqual(len(GRAM4_090), STANDING_N4)
        self.assertEqual(len(GRAM4_700), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover090700430076006IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover prefix-4 off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.cycle153_sites = STANDING_CYCLE153_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.i_sites_090 = nge4_sites(GRAM4_090, self.i_sides)
        self.i_sites_700 = nge4_sites(GRAM4_700, self.i_sides)
        self.n_on_i_090 = ngram_hit_count(self.i_sides[SIDE_IA], GRAM4_090) + STANDING_IB_HITS
        self.n_on_i_700 = ngram_hit_count(self.i_sides[SIDE_IA], GRAM4_700) + STANDING_IB_HITS
        self.hits_by_tablet_090 = tablet_hit_counts(
            self.by_tablet, GRAM4_090, VENDORED_TABLETS
        )
        self.hits_by_tablet_700 = tablet_hit_counts(
            self.by_tablet, GRAM4_700, VENDORED_TABLETS
        )
        self.off_i_090 = tablet_hit_counts(self.by_tablet, GRAM4_090, OFF_I_TABLETS)
        self.off_i_700 = tablet_hit_counts(self.by_tablet, GRAM4_700, OFF_I_TABLETS)
        self.n_off_i_090 = sum(self.off_i_090)
        self.n_off_i_700 = sum(self.off_i_700)
        self.claim_holds = i_leftover_090_700_430_076_006_both_i_only(
            self.n_on_i_090,
            self.n_off_i_090,
            self.n_on_i_700,
            self.n_off_i_700,
        )

    def test_tokens_and_sites_are_cycle_153_lock_not_retuned(self):
        """4-grams and I sites stay the cycle-153 leftover previous stems."""
        self.assertEqual(GRAM5_INDEPENDENT, MAXIMAL_N5_430)
        self.assertEqual(GRAM5_INDEPENDENT, ("430", "076", "006", "000", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(GRAM4_090, ("090", "430", "076", "006"))
        self.assertEqual(GRAM4_700, ("700", "430", "076", "006"))
        self.assertEqual(self.cycle153_sites, STANDING_CYCLE153_SITES)
        self.assertEqual(
            STANDING_CYCLE153_SITES,
            (
                (SIDE_IA, "Ia1", 129),
                (SIDE_IA, "Ia14", 162),
            ),
        )
        self.assertEqual(STANDING_PER_SITE_PREVIOUS, (STEM_090, STEM_700))
        prior_153 = self.survey["i_independent_430_076_006_000_076_previous_stem"]
        self.assertEqual(prior_153["cycle"], 153)
        self.assertEqual(tuple(prior_153["tokens5"]), GRAM5_INDEPENDENT)
        self.assertEqual(prior_153["N_sites"], 2)
        self.assertEqual(prior_153["N_with_previous"], 2)
        self.assertEqual(prior_153["N_distinct_previous_stems"], 2)
        self.assertEqual(tuple(prior_153["per_site_previous_stems"]), (STEM_090, STEM_700))
        self.assertEqual(
            tuple(tuple(row) for row in prior_153["i_sites"]),
            STANDING_CYCLE153_SITES,
        )
        self.assertFalse(
            prior_153["i_independent_430_076_006_000_076_share_one_previous_stem"]
        )
        prior_150 = self.survey["i_072_forward_5grams_i_only"]
        self.assertEqual(prior_150["cycle"], 150)
        self.assertTrue(prior_150["i_072_forward_5grams_both_i_only"])
        self.assertEqual(tuple(prior_150["sequences"][0]["tokens5"]), CYCLE150_LEFTOVER_5GRAM_090)
        prior_147 = self.survey["i_leftover_backward_5grams_i_only"]
        self.assertEqual(prior_147["cycle"], 147)
        self.assertTrue(prior_147["i_leftover_backward_5grams_both_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_on_I=1/1, N_off_I=0/0. Both I-only. Claim holds."""
        self.assertEqual(self.i_sites_090, STANDING_I_SITES_090)
        self.assertEqual(self.i_sites_700, STANDING_I_SITES_700)
        self.assertEqual(self.n_on_i_090, STANDING_N_ON_I_090)
        self.assertEqual(STANDING_N_ON_I_090, 1)
        self.assertEqual(self.n_on_i_700, STANDING_N_ON_I_700)
        self.assertEqual(STANDING_N_ON_I_700, 1)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(
            leftover_prefix_4gram_start_site(STANDING_CYCLE153_SITES[0]),
            STANDING_I_SITES_090[0],
        )
        self.assertEqual(
            leftover_prefix_4gram_start_site(STANDING_CYCLE153_SITES[1]),
            STANDING_I_SITES_700[0],
        )
        for site, want_gram, prev in (
            (STANDING_I_SITES_090[0], GRAM4_090, STEM_090),
            (STANDING_I_SITES_700[0], GRAM4_700, STEM_700),
        ):
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N4]), want_gram)
            self.assertEqual(stems[site[2]], prev)
            self.assertEqual(
                tuple(stems[site[2] + 1 : site[2] + 6]),
                GRAM5_INDEPENDENT,
            )
            self.assertNotEqual(want_gram, GRAM5)
            self.assertNotEqual(want_gram, GRAM5_INDEPENDENT)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet_090, STANDING_HITS_BY_TABLET_090)
        self.assertEqual(self.hits_by_tablet_700, STANDING_HITS_BY_TABLET_700)
        self.assertEqual(self.off_i_090, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_700, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.n_off_i_090, STANDING_N_OFF_I_090)
        self.assertEqual(self.n_off_i_700, STANDING_N_OFF_I_700)
        self.assertEqual(STANDING_N_OFF_I_090, 0)
        self.assertEqual(STANDING_N_OFF_I_700, 0)
        self.assertEqual(STANDING_OFF_I_SITES_090, ())
        self.assertEqual(STANDING_OFF_I_SITES_700, ())
        for tablet, count_090, count_700 in zip(
            VENDORED_TABLETS,
            self.hits_by_tablet_090,
            self.hits_by_tablet_700,
            strict=True,
        ):
            self.assertEqual(count_090, ngram_hit_count(self.by_tablet[tablet], GRAM4_090))
            self.assertEqual(count_700, ngram_hit_count(self.by_tablet[tablet], GRAM4_700))
            if tablet == "I":
                self.assertEqual(count_090, 1)
                self.assertEqual(count_700, 1)
            else:
                self.assertEqual(count_090, 0)
                self.assertEqual(count_700, 0)
        self.assertEqual(
            i_leftover_090_700_430_076_006_both_i_only(
                self.n_on_i_090,
                self.n_off_i_090,
                self.n_on_i_700,
                self.n_off_i_700,
            ),
            STANDING_I_LEFTOVER_090_700_430_076_006_BOTH_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_090_700_430_076_006_BOTH_I_ONLY,
        )
        self.assertTrue(STANDING_I_LEFTOVER_090_700_430_076_006_BOTH_I_ONLY)
        self.assertTrue(HYPOTHESIS_BOTH_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_leftover_090_700_430_076_006_both_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE150_LEFTOVER_5GRAM_090)
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5_700)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_153_152_150_147_103_and_w_scoreboards_still_compute(self):
        """Cycle 153 previous-stem, 152 I-only, 150 I-only, 147 I-only, 103, W stay."""
        prior_153 = TestMamariIIndependent430076006000076PreviousStemScoreboard()
        prior_153.setUp()
        prior_153.test_two_distinct_previous_stems_and_claim_loses()
        prior_153.test_survey_matches_computed_lock()
        prior_152 = TestMamariI4gram630076010079IOnlyScoreboard()
        prior_152.setUp()
        prior_152.test_i_hits_are_one_on_ia_at_leftover_start()
        prior_152.test_4gram_is_zero_off_i_and_i_only()
        prior_152.test_survey_matches_computed_lock()
        prior_150 = TestMamariI072Forward5gramsIOnlyScoreboard()
        prior_150.setUp()
        prior_150.test_each_5gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_150.test_survey_matches_computed_lock()
        prior_147 = TestMamariILeftoverBackward5gramsIOnlyScoreboard()
        prior_147.setUp()
        prior_147.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-154 leftover 4-gram I-only lock."""
        lock = self.survey["i_leftover_090_700_430_076_006_i_only"]
        self.assertEqual(lock["cycle"], 154)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_both_i_only"])
        self.assertEqual(lock["hypothesis_both_i_only"], HYPOTHESIS_BOTH_I_ONLY)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["tokens5"]), GRAM5_INDEPENDENT)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle153_sites"]),
            STANDING_CYCLE153_SITES,
        )
        self.assertEqual(tuple(lock["per_site_previous_stems"]), STANDING_PER_SITE_PREVIOUS)
        self.assertEqual(lock["N_distinct_previous_stems"], 2)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 2)
        row_090, row_700 = rows
        self.assertEqual(tuple(row_090["tokens4"]), GRAM4_090)
        self.assertEqual(tuple(row_700["tokens4"]), GRAM4_700)
        self.assertEqual(tuple(row_090["cycle153_site"]), STANDING_CYCLE153_SITES[0])
        self.assertEqual(tuple(row_700["cycle153_site"]), STANDING_CYCLE153_SITES[1])
        self.assertEqual(row_090["previous_stem"], STEM_090)
        self.assertEqual(row_700["previous_stem"], STEM_700)
        self.assertEqual(row_090["N_on_I"], STANDING_N_ON_I_090)
        self.assertEqual(row_700["N_on_I"], STANDING_N_ON_I_700)
        self.assertEqual(row_090["N_on_I"], 1)
        self.assertEqual(row_700["N_on_I"], 1)
        self.assertEqual(row_090["ia_hits"], 1)
        self.assertEqual(row_700["ia_hits"], 1)
        self.assertEqual(row_090["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(row_700["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(site) for site in row_090["i_sites"]),
            STANDING_I_SITES_090,
        )
        self.assertEqual(
            tuple(tuple(site) for site in row_700["i_sites"]),
            STANDING_I_SITES_700,
        )
        self.assertEqual(tuple(tuple(site) for site in row_090["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(tuple(tuple(site) for site in row_700["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(row_090["N_off_I"], STANDING_N_OFF_I_090)
        self.assertEqual(row_700["N_off_I"], STANDING_N_OFF_I_700)
        self.assertEqual(row_090["N_off_I"], 0)
        self.assertEqual(row_700["N_off_I"], 0)
        self.assertEqual(row_090["off_i_sites"], [])
        self.assertEqual(row_700["off_i_sites"], [])
        self.assertEqual(tuple(row_090["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(row_700["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(row_090["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(row_700["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(row_090["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(row_700["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(row_090["hits_by_tablet"]), STANDING_HITS_BY_TABLET_090)
        self.assertEqual(tuple(row_700["hits_by_tablet"]), STANDING_HITS_BY_TABLET_700)
        self.assertTrue(row_090["i_only"])
        self.assertTrue(row_700["i_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_090_700_430_076_006_both_i_only"])
        self.assertEqual(
            lock["i_leftover_090_700_430_076_006_both_i_only"],
            STANDING_I_LEFTOVER_090_700_430_076_006_BOTH_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle150_leftover_5gram_090"])
        self.assertFalse(lock["same_as_independent_n5_700"])
        self.assertTrue(lock["glyph_090_also_last_stem_of_cycle150_leftover_5gram"])
        self.assertTrue(lock["glyph_700_also_last_stem_of_independent_n5"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_independent_430_076_006_000_076_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_4gram_630_076_010_079_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_independent_076_010_079_006_700_preceded_072_unchanged"]
        )
        self.assertTrue(lock["standing_i_072_forward_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_072_076_010_079_forward_5gram_unchanged"])
        self.assertTrue(lock["standing_i_4gram_072_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_backward_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_inside_two_5grams_unchanged"])
        self.assertTrue(lock["standing_i_independent_n5_cycle103_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_independent_n5_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_exception_n4_071_065_071_999_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_independent_nge4_maximals_unchanged"])
        self.assertTrue(lock["standing_i_repeating_nge4_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_independent_430_076_006_000_076_previous_stem"]["cycle"],
            153,
        )
        self.assertFalse(
            self.survey["i_independent_430_076_006_000_076_previous_stem"][
                "i_independent_430_076_006_000_076_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_4gram_630_076_010_079_i_only"]["cycle"], 152)
        self.assertTrue(
            self.survey["i_4gram_630_076_010_079_i_only"][
                "i_4gram_630_076_010_079_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_072_forward_5grams_i_only"]["cycle"], 150)
        self.assertTrue(
            self.survey["i_072_forward_5grams_i_only"]["i_072_forward_5grams_both_i_only"]
        )
        self.assertEqual(self.survey["i_leftover_backward_5grams_i_only"]["cycle"], 147)
        self.assertTrue(
            self.survey["i_leftover_backward_5grams_i_only"][
                "i_leftover_backward_5grams_both_i_only"
            ]
        )
        self.assertEqual(self.survey["i_independent_n5_maximals_076"]["cycle"], 139)
        self.assertTrue(
            self.survey["i_independent_n5_maximals_076"][
                "i_independent_n5_maximals_all_contain_076"
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


class TestMamariILeftover090700430076006IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 154 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
