"""I's cycle-137 leftover n=4 exception off-I lock.

Cycle 138 text-search lock. Uses already-vendored A–V and the
cycle-137 leftover n=4 exception 071 065 071 999 (the only leftover
maximal that does not contain 076). Does not retune the leftover
set. Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents. Not a meaning dictionary.

Locks exact consecutive hits of 071 065 071 999 on tablet I and
on every other vendored tablet A–H and J–V. Claim that can lose:
i_exception_n4_071_065_071_999_is_i_only (I hits ≥ 2 and off-I
hits == 0). Ia is exactly 2 at Ia9[1]/Ia9[56]; Ib unpublished 0;
every other vendored tablet is exact-0. Not an n≥8 island. Not
the cycle-103 I 5-gram.

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
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    STANDING_LEFTOVER_N4_COUNT,
    STANDING_N,
    leftover_n4_rows,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
    EXCEPTION_SITES,
    STANDING_LEFTOVER,
    STANDING_LEFTOVER_N,
    STANDING_WITHOUT_076,
    TestMamariILeftoverN4Maximals076Scoreboard,
    leftover_without_076,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
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
    is_i_only,
    load_i_sides,
    load_vendored_by_tablet,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)

HYPOTHESIS_I_ONLY = True
GRAM4 = EXCEPTION_GRAM
STANDING_N4 = 4
STANDING_I_HITS = 2
STANDING_IA_HITS = 2
STANDING_IB_HITS = 0
STANDING_I_SITES = EXCEPTION_SITES
STANDING_IB_SITES = ()
STANDING_OFF_I_HITS = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_exception_n4_071_065_071_999_is_i_only"
STANDING_I_EXCEPTION_N4_071_065_071_999_IS_I_ONLY = True
STANDING_RESULT = "i_exception_n4_071_065_071_999_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False


def i_exception_n4_071_065_071_999_is_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 2 and off-I hits == 0."""
    return is_i_only(i_hits, off_i_hits)


class TestIExceptionN4IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-137 exception tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("071", "065", "071", "999"))
        self.assertEqual(GRAM4, EXCEPTION_GRAM)
        adjacent = [list(GRAM4), list(GRAM4)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4), 2)
        overlap = [["071", "065", "071", "999", "071", "065", "071", "999"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4), 2)
        gapped = [list(GRAM4[:2]) + ["076"] + list(GRAM4[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_2_and_zero_off_i(self):
        """Boolean is True only when I ≥ 2 and off-I is 0."""
        provider = MockProvider()
        self.assertTrue(i_exception_n4_071_065_071_999_is_i_only(2, 0))
        self.assertTrue(i_exception_n4_071_065_071_999_is_i_only(3, 0))
        self.assertFalse(i_exception_n4_071_065_071_999_is_i_only(2, 1))
        self.assertFalse(i_exception_n4_071_065_071_999_is_i_only(1, 0))
        self.assertFalse(i_exception_n4_071_065_071_999_is_i_only(0, 0))
        self.assertFalse(i_exception_n4_071_065_071_999_is_i_only(0, 2))
        self.assertEqual(STANDING_CLAIM, "i_exception_n4_071_065_071_999_is_i_only")
        self.assertTrue(STANDING_I_EXCEPTION_N4_071_065_071_999_IS_I_ONLY)
        self.assertEqual(
            STANDING_I_EXCEPTION_N4_071_065_071_999_IS_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_exception_is_not_the_cycle_103_5gram(self):
        """Exception 4-gram is a different string from the I 5-gram."""
        provider = MockProvider()
        self.assertNotEqual(GRAM4, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(len(GRAM4), STANDING_N4)
        self.assertEqual(STANDING_N4, 4)
        self.assertLess(len(GRAM4), 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariIExceptionN4071065071999IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 exception off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM4, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM4)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM4, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM4, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.claim_holds = i_exception_n4_071_065_071_999_is_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_137_exception_not_retuned(self):
        """Exception is the cycle-137 leftover lock, not a new inventory."""
        self.assertEqual(GRAM4, EXCEPTION_GRAM)
        self.assertEqual(GRAM4, ("071", "065", "071", "999"))
        self.assertEqual(STANDING_I_SITES, EXCEPTION_SITES)
        self.assertEqual(STANDING_I_SITES, (("Ia", "Ia9", 1), ("Ia", "Ia9", 56)))
        leftover = leftover_n4_rows()
        self.assertEqual(leftover, STANDING_LEFTOVER)
        self.assertEqual(len(leftover), STANDING_LEFTOVER_N)
        self.assertEqual(STANDING_LEFTOVER_N, STANDING_LEFTOVER_N4_COUNT)
        self.assertEqual(STANDING_LEFTOVER_N, 27)
        without_076 = leftover_without_076(leftover)
        self.assertEqual(len(without_076), STANDING_WITHOUT_076)
        self.assertEqual(STANDING_WITHOUT_076, 1)
        self.assertEqual(without_076[0][0], GRAM4)
        self.assertEqual(without_076[0][3], STANDING_I_SITES)
        self.assertIn(GRAM4, {gram for gram, _n, _f, _s in leftover})
        self.assertNotIn(GRAM5, {gram for gram, _n, _f, _s in leftover})
        prior_137 = self.survey["i_leftover_n4_maximals_076"]
        self.assertEqual(prior_137["cycle"], 137)
        self.assertEqual(tuple(prior_137["exception_tokens"]), GRAM4)
        self.assertEqual(
            [list(site) for site in STANDING_I_SITES],
            prior_137["exception_sites"],
        )
        self.assertEqual(prior_137["without_076_count"], 1)
        self.assertFalse(prior_137["i_leftover_n4_maximals_all_contain_076"])
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["maximal_count"], STANDING_N)
        self.assertEqual(STANDING_N, 31)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_two_at_ia9(self):
        """Exception is 2 on Ia at Ia9[1]/Ia9[56]; Ib unpublished 0."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 2)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, 2)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM4, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM4), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)][index : index + STANDING_N4]
            self.assertEqual(tuple(stems), GRAM4)
            self.assertEqual(side, SIDE_IA)
            self.assertEqual(line, "Ia9")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_4gram_is_zero_off_i_and_i_only(self):
        """4-gram is 0 on A–H and J–V. Ia has exactly 2. W is not a tablet."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, 0)
        self.assertEqual(STANDING_OFF_I_SITES, ())
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM4))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 2)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(
            i_exception_n4_071_065_071_999_is_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_EXCEPTION_N4_071_065_071_999_IS_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_EXCEPTION_N4_071_065_071_999_IS_I_ONLY,
        )
        self.assertTrue(STANDING_I_EXCEPTION_N4_071_065_071_999_IS_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_exception_n4_071_065_071_999_is_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM4, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_137_136_103_and_w_scoreboards_still_compute(self):
        """Cycle 137 leftover 076, 136 maximals, 103 I-only, and W stay."""
        prior_137 = TestMamariILeftoverN4Maximals076Scoreboard()
        prior_137.setUp()
        prior_137.test_counts_26_of_27_and_hypothesis_all_contain_loses()
        prior_137.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-138 exception I-only lock."""
        lock = self.survey["i_exception_n4_071_065_071_999_i_only"]
        self.assertEqual(lock["cycle"], 138)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(
            [list(site) for site in STANDING_OFF_I_SITES],
            lock["off_i_sites"],
        )
        self.assertEqual(tuple(lock["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(lock["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_exception_n4_071_065_071_999_is_i_only"])
        self.assertEqual(
            lock["i_exception_n4_071_065_071_999_is_i_only"],
            STANDING_I_EXCEPTION_N4_071_065_071_999_IS_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
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
        self.assertEqual(self.survey["i_leftover_n4_maximals_076"]["cycle"], 137)
        self.assertEqual(
            tuple(self.survey["i_leftover_n4_maximals_076"]["exception_tokens"]),
            GRAM4,
        )
        self.assertFalse(
            self.survey["i_leftover_n4_maximals_076"]["i_leftover_n4_maximals_all_contain_076"]
        )
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["cycle"], 136)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["maximal_count"], 31)
        self.assertEqual(self.survey["i_independent_nge4_maximals"]["leftover_n4_count"], 27)
        self.assertFalse(
            self.survey["i_independent_nge4_maximals"]["i_independent_nge4_has_exactly_4_maximals"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertFalse(
            self.survey["i_repeating_nge4"]["i_repeating_nge4_all_substrings_of_i_5gram"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["independent_count"], 39)
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


class TestMamariIExceptionN4071065071999IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 138 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
