"""I's cycle-168 leftover 3-gram site 4-grams off-I lock.

Cycle 169 text-search lock. Uses already-vendored A–V and the
cycle-168 leftover site of 3-gram 999 090 076 (N_leftover=1
at tablet I / side Ia / line Ia1 / index 1). Local 4-grams:
previous 602 999 090 076, next 999 090 076 012. Does not
retune those 4-grams, the leftover 3-gram, or the leftover
n=4 set. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

Same leftover-shape as cycles 164/165 (leftover backward /
forward 4-grams of leftover 076 020 010 sites all I-only
hapax 1/0). Neither of these two 4-grams is in the cycle-166
family of seven leftover n=4 maximals. n=2 090 076 without
999 does not count. Do not retune.

Locks exact consecutive hits of each leftover-site 4-gram
on tablet I and on every other vendored tablet A–H and J–V.
Hypothesis: both are I-only (N_I>=1 and N_off_I=0).
Measured: 602 999 090 076 N_I=1 at Ia1[0];
999 090 076 012 N_I=1 at Ia1[1]; both N_off_I=0.
Claim that can lose: i_leftover_999_090_076_site_4grams_i_only.
True only if both have N_off_I=0 (and N_I>=1). The claim
is true. Do not assume hapax; measure. Do not retune.

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
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3,
    STANDING_I_SITES,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_inside_family_scoreboard import (
    STANDING_LEFTOVER_NEXT_4GRAMS,
    STANDING_LEFTOVER_PREVIOUS_4GRAMS,
    STANDING_LEFTOVER_SITES,
    STANDING_MATCHING_LEFTOVERS,
    STANDING_N_LEFTOVER,
    TestMamariI3gram999090076InsideFamilyScoreboard,
    leftover_local_4grams,
)
from tests.test_mamari_i_leftover_076_020_010_backward_4grams_i_only_scoreboard import (
    TestMamariILeftover076020010Backward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_020_010_forward_4grams_i_only_scoreboard import (
    TestMamariILeftover076020010Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_999_090_076_scoreboard import (
    NEAR_MISS_N2_090_076,
    NEAR_MISS_999_021_090_076,
    TestMamariILeftoverN4999090076Scoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    STANDING_LEFTOVER,
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
STANDING_N3 = 3
STANDING_N4 = 4
GRAM4_PREV = ("602", "999", "090", "076")
GRAM4_NEXT = ("999", "090", "076", "012")
STANDING_SEQUENCES = (GRAM4_PREV, GRAM4_NEXT)
STANDING_N_I_PREV = 1
STANDING_N_I_NEXT = 1
STANDING_N_ON_I_PREV = 1
STANDING_N_ON_I_NEXT = 1
STANDING_I_SITES_PREV = ((SIDE_IA, "Ia1", 0),)
STANDING_I_SITES_NEXT = ((SIDE_IA, "Ia1", 1),)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_PREV = 0
STANDING_N_OFF_I_NEXT = 0
STANDING_OFF_I_SITES_PREV = ()
STANDING_OFF_I_SITES_NEXT = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_999_090_076_site_4grams_i_only"
STANDING_I_LEFTOVER_999_090_076_SITE_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_999_090_076_site_4grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE164_LEFTOVER_4GRAMS = False
STANDING_SAME_AS_CYCLE165_LEFTOVER_4GRAMS = False
STANDING_SAME_LEFTOVER_SHAPE_AS_164_165 = True
STANDING_N2_DOES_NOT_COUNT = True
STANDING_NOT_IN_CYCLE166_FAMILY = True
PREV_OFFSET = 1


def leftover_previous_4gram_start_site(
    leftover_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Previous 4-gram starts one stem before leftover 999 090 076."""
    side, line, index = leftover_site
    return (side, line, index - PREV_OFFSET)


def leftover_next_4gram_start_site(
    leftover_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Next 4-gram starts at the leftover 999 090 076 site."""
    return leftover_site


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_999_090_076_site_4grams_i_only(
    n_i_prev: int,
    n_off_i_prev: int,
    n_i_next: int,
    n_off_i_next: int,
) -> bool:
    """True iff both leftover-site 4-grams are I-only.

    Claim holds only if both have N_off_I=0. N_I>=1 is
    required so a missing I hit is not I-only.
    """
    return sequence_is_i_only(n_i_prev, n_off_i_prev) and sequence_is_i_only(
        n_i_next, n_off_i_next
    )


class TestILeftover999090076Site4gramsIOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-168 leftover-site 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. n=2 090 076 is not."""
        provider = MockProvider()
        self.assertEqual(GRAM4_PREV, ("602", "999", "090", "076"))
        self.assertEqual(GRAM4_NEXT, ("999", "090", "076", "012"))
        self.assertEqual(GRAM4_PREV[1:], GRAM3)
        self.assertEqual(GRAM4_NEXT[:3], GRAM3)
        adjacent = [list(GRAM4_PREV), list(GRAM4_NEXT)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_PREV), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM4_NEXT), 1)
        overlap = [["602", "999", "090", "076", "602", "999", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4_PREV), 2)
        gapped = [list(GRAM4_PREV[:2]) + ["000"] + list(GRAM4_PREV[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4_PREV), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_PREV), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4_NEXT), 0)
        n2_only = [list(NEAR_MISS_N2_090_076)]
        self.assertEqual(ngram_hit_count(n2_only, GRAM4_PREV), 0)
        self.assertEqual(ngram_hit_count(n2_only, GRAM4_NEXT), 0)
        self.assertTrue(STANDING_N2_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_both_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when both leftover-site 4-grams are I-only."""
        provider = MockProvider()
        self.assertTrue(i_leftover_999_090_076_site_4grams_i_only(1, 0, 1, 0))
        self.assertTrue(i_leftover_999_090_076_site_4grams_i_only(2, 0, 1, 0))
        self.assertFalse(i_leftover_999_090_076_site_4grams_i_only(1, 1, 1, 0))
        self.assertFalse(i_leftover_999_090_076_site_4grams_i_only(1, 0, 1, 1))
        self.assertFalse(i_leftover_999_090_076_site_4grams_i_only(0, 0, 1, 0))
        self.assertFalse(i_leftover_999_090_076_site_4grams_i_only(1, 0, 0, 0))
        self.assertFalse(i_leftover_999_090_076_site_4grams_i_only(0, 0, 0, 0))
        self.assertFalse(i_leftover_999_090_076_site_4grams_i_only(1, 1, 1, 1))
        self.assertEqual(STANDING_CLAIM, "i_leftover_999_090_076_site_4grams_i_only")
        self.assertTrue(STANDING_I_LEFTOVER_999_090_076_SITE_4GRAMS_I_ONLY)
        self.assertEqual(
            STANDING_I_LEFTOVER_999_090_076_SITE_4GRAMS_I_ONLY,
            HYPOTHESIS_BOTH_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_168_leftover_locals_not_retuned(self):
        """4-grams stay the cycle-168 leftover locals; not the n=4 family."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES, (GRAM4_PREV, GRAM4_NEXT))
        self.assertEqual(STANDING_LEFTOVER_PREVIOUS_4GRAMS, (GRAM4_PREV,))
        self.assertEqual(STANDING_LEFTOVER_NEXT_4GRAMS, (GRAM4_NEXT,))
        self.assertNotEqual(GRAM4_PREV, GRAM5)
        self.assertNotEqual(GRAM4_NEXT, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        family = set(STANDING_MATCHING_LEFTOVERS)
        self.assertNotIn(GRAM4_PREV, family)
        self.assertNotIn(GRAM4_NEXT, family)
        self.assertTrue(STANDING_NOT_IN_CYCLE166_FAMILY)
        self.assertNotEqual(GRAM4_PREV, NEAR_MISS_999_021_090_076)
        self.assertNotEqual(GRAM4_NEXT, NEAR_MISS_N2_090_076)
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_N2_090_076))
        leftover = STANDING_LEFTOVER_SITES[0]
        self.assertEqual(leftover_previous_4gram_start_site(leftover), STANDING_I_SITES_PREV[0])
        self.assertEqual(leftover_next_4gram_start_site(leftover), STANDING_I_SITES_NEXT[0])
        self.assertEqual(leftover_next_4gram_start_site(leftover), leftover)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE164_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE165_LEFTOVER_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_164_165)
        self.assertEqual(len(GRAM4_PREV), STANDING_N4)
        self.assertEqual(len(GRAM4_NEXT), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover999090076Site4gramsIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover-site 4-gram off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
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
        self.local_4grams = leftover_local_4grams(self.i_sides, self.leftover_sites)
        self.claim_holds = i_leftover_999_090_076_site_4grams_i_only(
            self.n_i[0],
            self.n_off_i[0],
            self.n_i[1],
            self.n_off_i[1],
        )

    def test_tokens_and_sites_are_cycle_168_lock_not_retuned(self):
        """4-grams and leftover site stay the cycle-168 leftover locals."""
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(STANDING_LEFTOVER_SITES, ((SIDE_IA, "Ia1", 1),))
        self.assertEqual(STANDING_N_LEFTOVER, 1)
        prior_168 = self.survey["i_3gram_999_090_076_inside_family"]
        self.assertEqual(prior_168["cycle"], 168)
        self.assertEqual(tuple(prior_168["tokens3"]), GRAM3)
        self.assertEqual(prior_168["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_168["N_leftover"], 1)
        self.assertFalse(prior_168["i_3gram_999_090_076_all_inside_leftover_n4_family"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_168["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_LEFTOVER_PREVIOUS_4GRAMS],
            prior_168["leftover_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_LEFTOVER_NEXT_4GRAMS],
            prior_168["leftover_next_4grams"],
        )
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertTrue(prior_167["i_3gram_999_090_076_i_only"])
        self.assertEqual(prior_167["N_I"], CYCLE167_N_I)
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], CYCLE167_N_OFF_I)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in prior_167["i_sites"]),
            STANDING_I_SITES,
        )
        prior_166 = self.survey["i_leftover_n4_999_090_076"]
        self.assertEqual(prior_166["cycle"], 166)
        self.assertTrue(prior_166["i_leftover_n4_exactly_7_contain_999_090_076"])
        self.assertEqual(prior_166["N_with_999_090_076"], 7)
        leftover_grams = {row[0] for row in STANDING_LEFTOVER}
        family = set(STANDING_MATCHING_LEFTOVERS)
        self.assertNotIn(GRAM4_PREV, leftover_grams)
        self.assertNotIn(GRAM4_NEXT, leftover_grams)
        self.assertNotIn(GRAM4_PREV, family)
        self.assertNotIn(GRAM4_NEXT, family)
        self.assertIn(NEAR_MISS_999_021_090_076, leftover_grams)
        self.assertNotIn(NEAR_MISS_999_021_090_076, family)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds(self):
        """N_I=1/1, N_off_I=0/0. Both I-only hapax. Claim holds."""
        standing_on = (STANDING_N_I_PREV, STANDING_N_I_NEXT)
        standing_off = (STANDING_N_OFF_I_PREV, STANDING_N_OFF_I_NEXT)
        standing_sites = (STANDING_I_SITES_PREV, STANDING_I_SITES_NEXT)
        self.assertEqual(self.i_sites, standing_sites)
        self.assertEqual(self.n_i, standing_on)
        self.assertEqual(standing_on, (1, 1))
        self.assertEqual(self.n_off_i, standing_off)
        self.assertEqual(standing_off, (0, 0))
        self.assertEqual(STANDING_N_ON_I_PREV, STANDING_N_I_PREV)
        self.assertEqual(STANDING_N_ON_I_NEXT, STANDING_N_I_NEXT)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        leftover = STANDING_LEFTOVER_SITES[0]
        prev_start = leftover_previous_4gram_start_site(leftover)
        next_start = leftover_next_4gram_start_site(leftover)
        self.assertEqual(prev_start, STANDING_I_SITES_PREV[0])
        self.assertEqual(next_start, STANDING_I_SITES_NEXT[0])
        stems = line_stems_for_site(self.i_sides, leftover)
        self.assertEqual(tuple(stems[0:4]), GRAM4_PREV)
        self.assertEqual(tuple(stems[1:4]), GRAM3)
        self.assertEqual(tuple(stems[1:5]), GRAM4_NEXT)
        self.assertEqual(self.local_4grams, (
            (
                (SIDE_IA, "Ia1", 1),
                GRAM4_PREV,
                GRAM4_NEXT,
            ),
        ))
        family = set(STANDING_MATCHING_LEFTOVERS)
        self.assertNotIn(GRAM4_PREV, family)
        self.assertNotIn(GRAM4_NEXT, family)
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
            i_leftover_999_090_076_site_4grams_i_only(
                self.n_i[0],
                self.n_off_i[0],
                self.n_i[1],
                self.n_off_i[1],
            ),
            STANDING_I_LEFTOVER_999_090_076_SITE_4GRAMS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_999_090_076_SITE_4GRAMS_I_ONLY,
        )
        self.assertTrue(STANDING_I_LEFTOVER_999_090_076_SITE_4GRAMS_I_ONLY)
        self.assertTrue(HYPOTHESIS_BOTH_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_leftover_999_090_076_site_4grams_i_only")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE164_LEFTOVER_4GRAMS)
        self.assertFalse(STANDING_SAME_AS_CYCLE165_LEFTOVER_4GRAMS)
        self.assertTrue(STANDING_SAME_LEFTOVER_SHAPE_AS_164_165)
        self.assertTrue(STANDING_N2_DOES_NOT_COUNT)
        self.assertTrue(STANDING_NOT_IN_CYCLE166_FAMILY)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_168_167_166_165_164_103_and_w_scoreboards_still_compute(self):
        """Cycle 168 leftover site, 167 I-only, 166 family 7, 165/164, 103, W stay."""
        prior_168 = TestMamariI3gram999090076InsideFamilyScoreboard()
        prior_168.setUp()
        prior_168.test_sixteen_sites_split_15_inside_1_leftover_and_claim_loses()
        prior_168.test_leftover_site_local_4grams_are_602_and_012()
        prior_168.test_survey_matches_computed_lock()
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_i_hits_are_sixteen_on_ia()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        prior_166 = TestMamariILeftoverN4999090076Scoreboard()
        prior_166.setUp()
        prior_166.test_counts_7_of_27_and_hypothesis_n_7_holds()
        prior_166.test_survey_matches_computed_lock()
        prior_165 = TestMamariILeftover076020010Forward4gramsIOnlyScoreboard()
        prior_165.setUp()
        prior_165.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_165.test_survey_matches_computed_lock()
        prior_164 = TestMamariILeftover076020010Backward4gramsIOnlyScoreboard()
        prior_164.setUp()
        prior_164.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_164.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-169 leftover-site 4-gram I-only lock."""
        lock = self.survey["i_leftover_999_090_076_site_4grams_i_only"]
        self.assertEqual(lock["cycle"], 169)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_both_i_only"])
        self.assertEqual(lock["hypothesis_both_i_only"], HYPOTHESIS_BOTH_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle168_leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            tuple(lock["cycle168_leftover_site"]),
            STANDING_LEFTOVER_SITES[0],
        )
        self.assertEqual(lock["cycle168_leftover_tablet"], "I")
        self.assertEqual(lock["cycle168_leftover_side"], "Ia")
        self.assertEqual(lock["cycle168_leftover_line"], "Ia1")
        self.assertEqual(lock["cycle168_leftover_index"], 1)
        rows = lock["sequences"]
        self.assertEqual(len(rows), 2)
        row_prev, row_next = rows
        self.assertEqual(tuple(row_prev["tokens4"]), GRAM4_PREV)
        self.assertEqual(tuple(row_next["tokens4"]), GRAM4_NEXT)
        self.assertEqual(row_prev["role"], "previous")
        self.assertEqual(row_next["role"], "next")
        self.assertEqual(tuple(row_prev["cycle168_leftover_site"]), STANDING_LEFTOVER_SITES[0])
        self.assertEqual(tuple(row_next["cycle168_leftover_site"]), STANDING_LEFTOVER_SITES[0])
        self.assertEqual(row_prev["N_I"], STANDING_N_I_PREV)
        self.assertEqual(row_next["N_I"], STANDING_N_I_NEXT)
        self.assertEqual(row_prev["N_on_I"], STANDING_N_ON_I_PREV)
        self.assertEqual(row_next["N_on_I"], STANDING_N_ON_I_NEXT)
        self.assertEqual(row_prev["N_I"], 1)
        self.assertEqual(row_next["N_I"], 1)
        self.assertEqual(row_prev["ia_hits"], 1)
        self.assertEqual(row_next["ia_hits"], 1)
        self.assertEqual(row_prev["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(row_next["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(site) for site in row_prev["i_sites"]),
            STANDING_I_SITES_PREV,
        )
        self.assertEqual(
            tuple(tuple(site) for site in row_next["i_sites"]),
            STANDING_I_SITES_NEXT,
        )
        self.assertEqual(tuple(tuple(site) for site in row_prev["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(tuple(tuple(site) for site in row_next["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(row_prev["N_off_I"], STANDING_N_OFF_I_PREV)
        self.assertEqual(row_next["N_off_I"], STANDING_N_OFF_I_NEXT)
        self.assertEqual(row_prev["N_off_I"], 0)
        self.assertEqual(row_next["N_off_I"], 0)
        self.assertEqual(row_prev["off_i_sites"], [])
        self.assertEqual(row_next["off_i_sites"], [])
        self.assertEqual(tuple(row_prev["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(row_next["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(row_prev["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(row_next["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(row_prev["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(row_next["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(row_prev["hits_by_tablet"]), STANDING_HITS_BY_TABLET_ONE_ON_I)
        self.assertEqual(tuple(row_next["hits_by_tablet"]), STANDING_HITS_BY_TABLET_ONE_ON_I)
        self.assertTrue(row_prev["i_only"])
        self.assertTrue(row_next["i_only"])
        self.assertEqual(lock["N_I_previous"], STANDING_N_I_PREV)
        self.assertEqual(lock["N_off_I_previous"], STANDING_N_OFF_I_PREV)
        self.assertEqual(lock["N_I_next"], STANDING_N_I_NEXT)
        self.assertEqual(lock["N_off_I_next"], STANDING_N_OFF_I_NEXT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_999_090_076_site_4grams_i_only"])
        self.assertEqual(
            lock["i_leftover_999_090_076_site_4grams_i_only"],
            STANDING_I_LEFTOVER_999_090_076_SITE_4GRAMS_I_ONLY,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle164_leftover_4grams"])
        self.assertFalse(lock["same_as_cycle165_leftover_4grams"])
        self.assertTrue(lock["same_leftover_shape_as_cycles_164_165"])
        self.assertTrue(lock["n2_090_076_without_999_does_not_count"])
        self.assertTrue(lock["not_in_cycle166_leftover_n4_family"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_999_090_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_backward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_3gram_999_090_076_inside_family"]["cycle"], 168)
        self.assertFalse(
            self.survey["i_3gram_999_090_076_inside_family"][
                "i_3gram_999_090_076_all_inside_leftover_n4_family"
            ]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_inside_family"]["N_leftover"], 1)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_999_090_076"]["cycle"], 166)
        self.assertTrue(
            self.survey["i_leftover_n4_999_090_076"][
                "i_leftover_n4_exactly_7_contain_999_090_076"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_999_090_076"]["N_with_999_090_076"],
            7,
        )
        self.assertEqual(
            self.survey["i_leftover_076_020_010_forward_4grams_i_only"]["cycle"], 165
        )
        self.assertTrue(
            self.survey["i_leftover_076_020_010_forward_4grams_i_only"][
                "i_leftover_076_020_010_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_020_010_backward_4grams_i_only"]["cycle"], 164
        )
        self.assertTrue(
            self.survey["i_leftover_076_020_010_backward_4grams_i_only"][
                "i_leftover_076_020_010_backward_4grams_all_i_only"
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


class TestMamariILeftover999090076Site4gramsIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 169 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
