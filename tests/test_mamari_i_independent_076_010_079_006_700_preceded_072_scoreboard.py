"""I's cycle-139 independent 5-gram previous-stem lock.

Cycle 151 text-search lock. Uses already-vendored A–V and the
cycle-139 independent 5-gram 076 010 079 006 700 at Ia6[19]
and Ia13[72]. Does not retune that 5-gram or those sites.
Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not
redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

For each independent 5-gram site, the previous stem if the
line has one before the 5-gram; start-of-line is
no-previous. Hypothesis: both I sites are immediately
preceded by stem 072 (i.e. 072 076 010 079 006 700 at both).
Measured: N_sites=2, N_preceded_by_072=1 at Ia13[72]
(previous 072), N_not_preceded_by_072=1 at Ia6[19]
(previous 630). Claim that can lose:
i_independent_076_010_079_006_700_both_preceded_by_072.
True only if N_preceded_by_072=2. The claim is false. Do
not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_072_forward_5grams_i_only_scoreboard import (
    STANDING_FORWARD_5GRAM_006,
    STANDING_I_SITES_006,
    TestMamariI072Forward5gramsIOnlyScoreboard,
)
from tests.test_mamari_i_4gram_072_076_010_079_i_only_scoreboard import (
    GRAM4,
    STANDING_I_SITES as STANDING_CYCLE148_SITES,
    TestMamariI4gram072076010079IOnlyScoreboard,
)
from tests.test_mamari_i_independent_n5_076_scoreboard import (
    TestMamariIIndependentN5076Scoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    STANDING_INDEPENDENT_SITES,
    line_stems_for_site,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HYPOTHESIS_BOTH_PRECEDED_BY_072 = True
GRAM5_INDEPENDENT = MAXIMAL_N5_010
STEM_072 = "072"
STEM_630 = "630"
STANDING_N5 = 5
STANDING_N_SITES = 2
STANDING_I_SITES = STANDING_INDEPENDENT_SITES
STANDING_N_PRECEDED_BY_072 = 1
STANDING_N_NOT_PRECEDED_BY_072 = 1
STANDING_PRECEDED_BY_072_SITES = ((SIDE_IA, "Ia13", 72),)
STANDING_NOT_PRECEDED_BY_072_SITES = ((SIDE_IA, "Ia6", 19),)
STANDING_PER_SITE_PREVIOUS = (STEM_630, STEM_072)
STANDING_NO_PREVIOUS_SITES = ()
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_independent_076_010_079_006_700_both_preceded_by_072"
STANDING_I_INDEPENDENT_076_010_079_006_700_BOTH_PRECEDED_BY_072 = False
STANDING_RESULT = "i_independent_076_010_079_006_700_preceded_072"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE148_4GRAM = False


def site_previous_stem(
    stems: list[str],
    index: int,
    gram5: tuple[str, ...] = GRAM5_INDEPENDENT,
) -> str | None:
    """Previous stem before the 5-gram; None at start-of-line or mismatch."""
    if tuple(stems[index : index + len(gram5)]) != gram5:
        return None
    if index == 0:
        return None
    return stems[index - 1]


def i_site_previous_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    gram5: tuple[str, ...] = GRAM5_INDEPENDENT,
) -> tuple[str | None, ...]:
    """Per-site previous stem or None for the locked independent 5-gram sites."""
    return tuple(
        site_previous_stem(line_stems_for_site(i_sides, site), site[2], gram5)
        for site in sites
    )


def sites_preceded_by_072(
    sites: tuple[tuple[str, str, int], ...],
    previous: tuple[str | None, ...],
    stem: str = STEM_072,
) -> tuple[tuple[str, str, int], ...]:
    """Independent 5-gram sites whose previous stem is 072."""
    return tuple(
        site
        for site, prev in zip(sites, previous, strict=True)
        if prev == stem
    )


def sites_not_preceded_by_072(
    sites: tuple[tuple[str, str, int], ...],
    previous: tuple[str | None, ...],
    stem: str = STEM_072,
) -> tuple[tuple[str, str, int], ...]:
    """Independent 5-gram sites whose previous stem is not 072."""
    return tuple(
        site
        for site, prev in zip(sites, previous, strict=True)
        if prev != stem
    )


def i_independent_076_010_079_006_700_both_preceded_by_072(
    n_preceded_by_072: int,
) -> bool:
    """True iff N_preceded_by_072=2."""
    return n_preceded_by_072 == 2


class TestIIndependent076010079006700Preceded072Helpers(unittest.TestCase):
    """Helpers on cycle-139 independent 5-gram sites. No CV, no LLM."""

    def test_previous_requires_stem_before_5gram(self):
        """A previous stem is recorded; start-of-line is no-previous."""
        provider = MockProvider()
        self.assertEqual(GRAM5_INDEPENDENT, ("076", "010", "079", "006", "700"))
        has_072 = ["072", "076", "010", "079", "006", "700"]
        self.assertEqual(site_previous_stem(has_072, 1), STEM_072)
        has_630 = ["630", "076", "010", "079", "006", "700"]
        self.assertEqual(site_previous_stem(has_630, 1), STEM_630)
        start_of_line = ["076", "010", "079", "006", "700"]
        self.assertIsNone(site_previous_stem(start_of_line, 0))
        mismatch = ["072", "076", "010", "079", "090"]
        self.assertIsNone(site_previous_stem(mismatch, 1))
        self.assertEqual(provider.get_call_history(), [])

    def test_both_preceded_requires_n_preceded_eq_2(self):
        """Boolean is True only when N_preceded_by_072=2."""
        provider = MockProvider()
        self.assertTrue(i_independent_076_010_079_006_700_both_preceded_by_072(2))
        self.assertFalse(i_independent_076_010_079_006_700_both_preceded_by_072(1))
        self.assertFalse(i_independent_076_010_079_006_700_both_preceded_by_072(0))
        self.assertFalse(i_independent_076_010_079_006_700_both_preceded_by_072(3))
        self.assertEqual(
            STANDING_CLAIM,
            "i_independent_076_010_079_006_700_both_preceded_by_072",
        )
        self.assertFalse(STANDING_I_INDEPENDENT_076_010_079_006_700_BOTH_PRECEDED_BY_072)
        self.assertNotEqual(
            STANDING_I_INDEPENDENT_076_010_079_006_700_BOTH_PRECEDED_BY_072,
            HYPOTHESIS_BOTH_PRECEDED_BY_072,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_sites_split_by_previous_072(self):
        """Sites group into preceded-by-072 vs not."""
        provider = MockProvider()
        sites = STANDING_I_SITES
        mixed = (STEM_630, STEM_072)
        self.assertEqual(
            sites_preceded_by_072(sites, mixed),
            STANDING_PRECEDED_BY_072_SITES,
        )
        self.assertEqual(
            sites_not_preceded_by_072(sites, mixed),
            STANDING_NOT_PRECEDED_BY_072_SITES,
        )
        both_072 = (STEM_072, STEM_072)
        self.assertEqual(sites_preceded_by_072(sites, both_072), sites)
        self.assertEqual(sites_not_preceded_by_072(sites, both_072), ())
        none_prev = (None, None)
        self.assertEqual(sites_preceded_by_072(sites, none_prev), ())
        self.assertEqual(sites_not_preceded_by_072(sites, none_prev), sites)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariIIndependent076010079006700Preceded072Scoreboard(
    unittest.TestCase
):
    """Cited-fixture independent 5-gram previous-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = STANDING_I_SITES
        self.previous = i_site_previous_stems(self.i_sides, self.i_sites)
        self.preceded = sites_preceded_by_072(self.i_sites, self.previous)
        self.not_preceded = sites_not_preceded_by_072(self.i_sites, self.previous)
        self.n_sites = len(self.i_sites)
        self.n_preceded_by_072 = len(self.preceded)
        self.n_not_preceded_by_072 = len(self.not_preceded)
        self.claim_holds = i_independent_076_010_079_006_700_both_preceded_by_072(
            self.n_preceded_by_072
        )

    def test_tokens_and_sites_are_cycle_139_lock_not_retuned(self):
        """5-gram and I sites stay the cycle-139 independent n=5 lock."""
        self.assertEqual(GRAM5_INDEPENDENT, MAXIMAL_N5_010)
        self.assertEqual(GRAM5_INDEPENDENT, ("076", "010", "079", "006", "700"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(GRAM4, ("072", "076", "010", "079"))
        self.assertNotEqual(GRAM5_INDEPENDENT, GRAM5)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia6", 19),
                (SIDE_IA, "Ia13", 72),
            ),
        )
        self.assertEqual(STANDING_I_SITES, STANDING_INDEPENDENT_SITES)
        self.assertEqual(STANDING_N_SITES, 2)
        self.assertEqual(nge4_sites(GRAM5_INDEPENDENT, self.i_sides), STANDING_I_SITES)
        prior_139 = self.survey["i_independent_n5_maximals_076"]
        self.assertEqual(prior_139["cycle"], 139)
        self.assertTrue(prior_139["i_independent_n5_maximals_all_contain_076"])
        measured = [
            row
            for row in prior_139["n5_maximals"]
            if tuple(row["tokens"]) == GRAM5_INDEPENDENT
        ]
        self.assertEqual(len(measured), 1)
        self.assertEqual(
            tuple(tuple(site) for site in measured[0]["sites"]),
            STANDING_I_SITES,
        )
        prior_142 = self.survey["i_overlap_3gram_inside_two_5grams"]
        self.assertEqual(prior_142["N_in_independent_076_010_079_006_700"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in prior_142["independent_sites"]),
            STANDING_I_SITES,
        )
        prior_150 = self.survey["i_072_forward_5grams_i_only"]
        self.assertEqual(prior_150["cycle"], 150)
        self.assertTrue(prior_150["i_072_forward_5grams_both_i_only"])
        self.assertEqual(
            tuple(prior_150["independent_n5_site_after_ia13"]),
            (SIDE_IA, "Ia13", 72),
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_one_of_two_preceded_by_072_and_claim_loses(self):
        """N_sites=2, N_preceded_by_072=1, N_not=1. Claim loses."""
        self.assertEqual(self.n_sites, STANDING_N_SITES)
        self.assertEqual(STANDING_N_SITES, 2)
        self.assertEqual(self.n_preceded_by_072, STANDING_N_PRECEDED_BY_072)
        self.assertEqual(STANDING_N_PRECEDED_BY_072, 1)
        self.assertEqual(self.n_not_preceded_by_072, STANDING_N_NOT_PRECEDED_BY_072)
        self.assertEqual(STANDING_N_NOT_PRECEDED_BY_072, 1)
        self.assertEqual(
            STANDING_N_PRECEDED_BY_072 + STANDING_N_NOT_PRECEDED_BY_072,
            STANDING_N_SITES,
        )
        self.assertEqual(self.previous, STANDING_PER_SITE_PREVIOUS)
        self.assertEqual(self.preceded, STANDING_PRECEDED_BY_072_SITES)
        self.assertEqual(self.not_preceded, STANDING_NOT_PRECEDED_BY_072_SITES)
        self.assertEqual(STANDING_NO_PREVIOUS_SITES, ())
        expected = (
            ((SIDE_IA, "Ia6", 19), STEM_630, False),
            ((SIDE_IA, "Ia13", 72), STEM_072, True),
        )
        for (site, prev), (want_site, want_prev, want_072) in zip(
            zip(self.i_sites, self.previous, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N5]), GRAM5_INDEPENDENT)
            self.assertGreater(index, 0)
            self.assertEqual(stems[index - 1], want_prev)
            self.assertEqual(prev, want_prev)
            self.assertEqual(site_previous_stem(stems, index), want_prev)
            self.assertEqual(prev == STEM_072, want_072)
            self.assertEqual(site, want_site)
            self.assertEqual(side, SIDE_IA)
            self.assertEqual(line, want_site[1])
        ia13_stems = line_stems_for_site(self.i_sides, STANDING_I_SITES[1])
        ia13_index = STANDING_I_SITES[1][2]
        self.assertEqual(STANDING_CYCLE148_SITES[1][2] + 1, ia13_index)
        self.assertEqual(ia13_stems[ia13_index - 1], STEM_072)
        self.assertEqual(
            tuple(ia13_stems[ia13_index - 1 : ia13_index + 3]),
            GRAM4,
        )
        self.assertEqual(
            tuple(ia13_stems[ia13_index - 1 : ia13_index + 4]),
            STANDING_FORWARD_5GRAM_006,
        )
        self.assertEqual(STANDING_I_SITES_006[0][2] + 1, ia13_index)
        ia6_stems = line_stems_for_site(self.i_sides, STANDING_I_SITES[0])
        ia6_index = STANDING_I_SITES[0][2]
        self.assertEqual(ia6_stems[ia6_index - 1], STEM_630)
        self.assertNotEqual(ia6_stems[ia6_index - 1], STEM_072)
        self.assertEqual(
            i_independent_076_010_079_006_700_both_preceded_by_072(
                self.n_preceded_by_072
            ),
            STANDING_I_INDEPENDENT_076_010_079_006_700_BOTH_PRECEDED_BY_072,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_INDEPENDENT_076_010_079_006_700_BOTH_PRECEDED_BY_072,
        )
        self.assertFalse(STANDING_I_INDEPENDENT_076_010_079_006_700_BOTH_PRECEDED_BY_072)
        self.assertTrue(HYPOTHESIS_BOTH_PRECEDED_BY_072)
        self.assertEqual(STANDING_CLAIM, "i_independent_076_010_079_006_700_both_preceded_by_072")
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE148_4GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_150_148_139_103_and_w_scoreboards_still_compute(self):
        """Cycle 150 I-only, 148 I-only, 139 076, 103 I-only, W stay."""
        prior_150 = TestMamariI072Forward5gramsIOnlyScoreboard()
        prior_150.setUp()
        prior_150.test_each_5gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_150.test_survey_matches_computed_lock()
        prior_148 = TestMamariI4gram072076010079IOnlyScoreboard()
        prior_148.setUp()
        prior_148.test_i_hits_are_two_on_ia_including_leftover_start()
        prior_148.test_4gram_is_zero_off_i_and_i_only()
        prior_148.test_survey_matches_computed_lock()
        prior_139 = TestMamariIIndependentN5076Scoreboard()
        prior_139.setUp()
        prior_139.test_counts_4_of_4_and_hypothesis_all_contain_holds()
        prior_139.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-151 previous-stem lock."""
        lock = self.survey["i_independent_076_010_079_006_700_preceded_072"]
        self.assertEqual(lock["cycle"], 151)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_both_preceded_by_072"])
        self.assertEqual(
            lock["hypothesis_both_preceded_by_072"],
            HYPOTHESIS_BOTH_PRECEDED_BY_072,
        )
        self.assertEqual(tuple(lock["tokens5"]), GRAM5_INDEPENDENT)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["stem_072"], STEM_072)
        self.assertEqual(lock["N_sites"], STANDING_N_SITES)
        self.assertEqual(lock["N_sites"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_preceded_by_072"], STANDING_N_PRECEDED_BY_072)
        self.assertEqual(lock["N_preceded_by_072"], 1)
        self.assertEqual(
            lock["N_not_preceded_by_072"],
            STANDING_N_NOT_PRECEDED_BY_072,
        )
        self.assertEqual(lock["N_not_preceded_by_072"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["preceded_by_072_sites"]),
            STANDING_PRECEDED_BY_072_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["not_preceded_by_072_sites"]),
            STANDING_NOT_PRECEDED_BY_072_SITES,
        )
        self.assertEqual(
            tuple(lock["per_site_previous_stems"]),
            STANDING_PER_SITE_PREVIOUS,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_previous_sites"]),
            STANDING_NO_PREVIOUS_SITES,
        )
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_independent_076_010_079_006_700_both_preceded_by_072"])
        self.assertEqual(
            lock["i_independent_076_010_079_006_700_both_preceded_by_072"],
            STANDING_I_INDEPENDENT_076_010_079_006_700_BOTH_PRECEDED_BY_072,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle148_4gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_072_forward_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_072_076_010_079_forward_5gram_unchanged"])
        self.assertTrue(lock["standing_i_4gram_072_076_010_079_i_only_unchanged"])
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
        self.assertEqual(self.survey["i_072_forward_5grams_i_only"]["cycle"], 150)
        self.assertTrue(
            self.survey["i_072_forward_5grams_i_only"]["i_072_forward_5grams_both_i_only"]
        )
        self.assertEqual(self.survey["i_4gram_072_076_010_079_forward_5gram"]["cycle"], 149)
        self.assertFalse(
            self.survey["i_4gram_072_076_010_079_forward_5gram"][
                "i_4gram_072_076_010_079_share_one_forward_5gram"
            ]
        )
        self.assertEqual(self.survey["i_4gram_072_076_010_079_i_only"]["cycle"], 148)
        self.assertTrue(
            self.survey["i_4gram_072_076_010_079_i_only"][
                "i_4gram_072_076_010_079_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_4gram_072_076_010_079_i_only"]["N_on_I"], 2)
        self.assertEqual(self.survey["i_overlap_3gram_inside_two_5grams"]["cycle"], 142)
        self.assertEqual(
            self.survey["i_overlap_3gram_inside_two_5grams"][
                "N_in_independent_076_010_079_006_700"
            ],
            2,
        )
        self.assertEqual(self.survey["i_independent_n5_cycle103_n3_overlap"]["cycle"], 140)
        self.assertFalse(
            self.survey["i_independent_n5_cycle103_n3_overlap"][
                "i_independent_n5_share_no_n3plus_with_cycle103_5gram"
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


class TestMamariIIndependent076010079006700Preceded072ImageSnapshot(
    unittest.TestCase
):
    """Cycle 151 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
