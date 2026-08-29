"""I's cycle-139 independent 5-gram previous-stem lock.

Cycle 153 text-search lock. Uses already-vendored A–V and the
cycle-139 independent 5-gram 430 076 006 000 076 at Ia1[129]
and Ia14[162]. Does not retune that 5-gram or those sites.
Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not
redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

For each independent 5-gram site, the previous stem if the
line has one before the 5-gram; start-of-line is
no-previous. Hypothesis: both I sites share one previous
stem Y (i.e. Y 430 076 006 000 076 at both). Measured:
N_sites=2, N_with_previous=2, N_distinct_previous_stems=2
(090 at Ia1[129], 700 at Ia14[162]). Claim that can lose:
i_independent_430_076_006_000_076_share_one_previous_stem.
True only if N_with_previous=2 and
N_distinct_previous_stems=1. The claim is false. Do not
retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_4gram_630_076_010_079_i_only_scoreboard import (
    TestMamariI4gram630076010079IOnlyScoreboard,
)
from tests.test_mamari_i_independent_076_010_079_006_700_preceded_072_scoreboard import (
    TestMamariIIndependent076010079006700Preceded072Scoreboard,
    i_site_previous_stems,
    site_previous_stem,
)
from tests.test_mamari_i_independent_n5_076_scoreboard import (
    TestMamariIIndependentN5076Scoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
    MAXIMAL_N5_430,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
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

HYPOTHESIS_SHARE_ONE = True
GRAM5_INDEPENDENT = MAXIMAL_N5_430
STEM_090 = "090"
STEM_700 = "700"
STANDING_N5 = 5
STANDING_N_SITES = 2
STANDING_I_SITES = (
    (SIDE_IA, "Ia1", 129),
    (SIDE_IA, "Ia14", 162),
)
STANDING_N_WITH_PREVIOUS = 2
STANDING_N_NO_PREVIOUS = 0
STANDING_N_DISTINCT_PREVIOUS_STEMS = 2
STANDING_PER_SITE_PREVIOUS = (STEM_090, STEM_700)
STANDING_DISTINCT_PREVIOUS_STEMS = (STEM_090, STEM_700)
STANDING_SITES_PER_PREVIOUS_STEM = (
    (STEM_090, ((SIDE_IA, "Ia1", 129),)),
    (STEM_700, ((SIDE_IA, "Ia14", 162),)),
)
STANDING_NO_PREVIOUS_SITES = ()
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_independent_430_076_006_000_076_share_one_previous_stem"
STANDING_I_INDEPENDENT_430_076_006_000_076_SHARE_ONE_PREVIOUS_STEM = False
STANDING_RESULT = "i_independent_430_076_006_000_076_previous_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE151_INDEPENDENT_N5 = False


def sites_with_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Independent 5-gram sites that have a previous stem."""
    return tuple(
        site
        for site, prev in zip(sites, previous, strict=True)
        if prev is not None
    )


def sites_without_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Independent 5-gram sites that are start-of-line (no-previous)."""
    return tuple(
        site
        for site, prev in zip(sites, previous, strict=True)
        if prev is None
    )


def group_sites_by_previous_stem(
    sites: tuple[tuple[str, str, int], ...],
    previous: tuple[str | None, ...],
) -> tuple[tuple[str, tuple[tuple[str, str, int], ...]], ...]:
    """Distinct previous stems in first-seen order, with their sites."""
    groups: list[tuple[str, list[tuple[str, str, int]]]] = []
    index_by_stem: dict[str, int] = {}
    for site, prev in zip(sites, previous, strict=True):
        if prev is None:
            continue
        if prev not in index_by_stem:
            index_by_stem[prev] = len(groups)
            groups.append((prev, [site]))
        else:
            groups[index_by_stem[prev]][1].append(site)
    return tuple((stem, tuple(stem_sites)) for stem, stem_sites in groups)


def i_independent_430_076_006_000_076_share_one_previous_stem(
    n_with_previous: int,
    n_distinct_previous_stems: int,
) -> bool:
    """True iff N_with_previous=2 and N_distinct_previous_stems=1."""
    return n_with_previous == 2 and n_distinct_previous_stems == 1


class TestIIndependent430076006000076PreviousStemHelpers(unittest.TestCase):
    """Helpers on cycle-139 independent 5-gram sites. No CV, no LLM."""

    def test_previous_requires_stem_before_5gram(self):
        """A previous stem is recorded; start-of-line is no-previous."""
        provider = MockProvider()
        self.assertEqual(GRAM5_INDEPENDENT, ("430", "076", "006", "000", "076"))
        has_090 = ["090", "430", "076", "006", "000", "076"]
        self.assertEqual(site_previous_stem(has_090, 1, GRAM5_INDEPENDENT), STEM_090)
        has_700 = ["700", "430", "076", "006", "000", "076"]
        self.assertEqual(site_previous_stem(has_700, 1, GRAM5_INDEPENDENT), STEM_700)
        start_of_line = ["430", "076", "006", "000", "076"]
        self.assertIsNone(site_previous_stem(start_of_line, 0, GRAM5_INDEPENDENT))
        mismatch = ["090", "430", "076", "006", "000", "011"]
        self.assertIsNone(site_previous_stem(mismatch, 1, GRAM5_INDEPENDENT))
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_two_previous_and_one_distinct(self):
        """Boolean is True only when N_with_previous=2 and N_distinct=1."""
        provider = MockProvider()
        self.assertTrue(
            i_independent_430_076_006_000_076_share_one_previous_stem(2, 1)
        )
        self.assertFalse(
            i_independent_430_076_006_000_076_share_one_previous_stem(2, 2)
        )
        self.assertFalse(
            i_independent_430_076_006_000_076_share_one_previous_stem(1, 1)
        )
        self.assertFalse(
            i_independent_430_076_006_000_076_share_one_previous_stem(0, 0)
        )
        self.assertFalse(
            i_independent_430_076_006_000_076_share_one_previous_stem(3, 1)
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_independent_430_076_006_000_076_share_one_previous_stem",
        )
        self.assertFalse(
            STANDING_I_INDEPENDENT_430_076_006_000_076_SHARE_ONE_PREVIOUS_STEM
        )
        self.assertNotEqual(
            STANDING_I_INDEPENDENT_430_076_006_000_076_SHARE_ONE_PREVIOUS_STEM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_sites_group_by_previous_stem(self):
        """Sites group into previous-present vs start-of-line, then by stem."""
        provider = MockProvider()
        sites = STANDING_I_SITES
        mixed = (STEM_090, STEM_700)
        self.assertEqual(sites_with_previous(sites, mixed), sites)
        self.assertEqual(sites_without_previous(sites, mixed), ())
        self.assertEqual(
            group_sites_by_previous_stem(sites, mixed),
            STANDING_SITES_PER_PREVIOUS_STEM,
        )
        both_090 = (STEM_090, STEM_090)
        self.assertEqual(sites_with_previous(sites, both_090), sites)
        self.assertEqual(
            group_sites_by_previous_stem(sites, both_090),
            ((STEM_090, sites),),
        )
        none_prev = (None, None)
        self.assertEqual(sites_with_previous(sites, none_prev), ())
        self.assertEqual(sites_without_previous(sites, none_prev), sites)
        self.assertEqual(group_sites_by_previous_stem(sites, none_prev), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariIIndependent430076006000076PreviousStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture independent 5-gram previous-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = STANDING_I_SITES
        self.previous = i_site_previous_stems(
            self.i_sides, self.i_sites, GRAM5_INDEPENDENT
        )
        self.with_previous = sites_with_previous(self.i_sites, self.previous)
        self.no_previous = sites_without_previous(self.i_sites, self.previous)
        self.grouped = group_sites_by_previous_stem(self.i_sites, self.previous)
        self.n_sites = len(self.i_sites)
        self.n_with_previous = len(self.with_previous)
        self.n_no_previous = len(self.no_previous)
        self.n_distinct_previous_stems = len(self.grouped)
        self.claim_holds = i_independent_430_076_006_000_076_share_one_previous_stem(
            self.n_with_previous,
            self.n_distinct_previous_stems,
        )

    def test_tokens_and_sites_are_cycle_139_lock_not_retuned(self):
        """5-gram and I sites stay the cycle-139 independent n=5 lock."""
        self.assertEqual(GRAM5_INDEPENDENT, MAXIMAL_N5_430)
        self.assertEqual(GRAM5_INDEPENDENT, ("430", "076", "006", "000", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertNotEqual(GRAM5_INDEPENDENT, GRAM5)
        self.assertNotEqual(GRAM5_INDEPENDENT, MAXIMAL_N5_010)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia1", 129),
                (SIDE_IA, "Ia14", 162),
            ),
        )
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
        prior_152 = self.survey["i_4gram_630_076_010_079_i_only"]
        self.assertEqual(prior_152["cycle"], 152)
        self.assertTrue(prior_152["i_4gram_630_076_010_079_is_i_only"])
        prior_151 = self.survey["i_independent_076_010_079_006_700_preceded_072"]
        self.assertEqual(prior_151["cycle"], 151)
        self.assertFalse(prior_151["i_independent_076_010_079_006_700_both_preceded_by_072"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_two_distinct_previous_stems_and_claim_loses(self):
        """N_sites=2, N_with_previous=2, N_distinct=2. Claim loses."""
        self.assertEqual(self.n_sites, STANDING_N_SITES)
        self.assertEqual(STANDING_N_SITES, 2)
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 2)
        self.assertEqual(self.n_no_previous, STANDING_N_NO_PREVIOUS)
        self.assertEqual(STANDING_N_NO_PREVIOUS, 0)
        self.assertEqual(
            self.n_distinct_previous_stems,
            STANDING_N_DISTINCT_PREVIOUS_STEMS,
        )
        self.assertEqual(STANDING_N_DISTINCT_PREVIOUS_STEMS, 2)
        self.assertEqual(
            STANDING_N_WITH_PREVIOUS + STANDING_N_NO_PREVIOUS,
            STANDING_N_SITES,
        )
        self.assertEqual(self.previous, STANDING_PER_SITE_PREVIOUS)
        self.assertEqual(self.with_previous, STANDING_I_SITES)
        self.assertEqual(self.no_previous, STANDING_NO_PREVIOUS_SITES)
        self.assertEqual(self.grouped, STANDING_SITES_PER_PREVIOUS_STEM)
        self.assertEqual(
            tuple(stem for stem, _sites in self.grouped),
            STANDING_DISTINCT_PREVIOUS_STEMS,
        )
        expected = (
            ((SIDE_IA, "Ia1", 129), STEM_090),
            ((SIDE_IA, "Ia14", 162), STEM_700),
        )
        for (site, prev), (want_site, want_prev) in zip(
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
            self.assertEqual(
                site_previous_stem(stems, index, GRAM5_INDEPENDENT),
                want_prev,
            )
            self.assertEqual(site, want_site)
            self.assertEqual(side, SIDE_IA)
            self.assertEqual(line, want_site[1])
        self.assertEqual(
            i_independent_430_076_006_000_076_share_one_previous_stem(
                self.n_with_previous,
                self.n_distinct_previous_stems,
            ),
            STANDING_I_INDEPENDENT_430_076_006_000_076_SHARE_ONE_PREVIOUS_STEM,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_INDEPENDENT_430_076_006_000_076_SHARE_ONE_PREVIOUS_STEM,
        )
        self.assertFalse(
            STANDING_I_INDEPENDENT_430_076_006_000_076_SHARE_ONE_PREVIOUS_STEM
        )
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(
            STANDING_CLAIM,
            "i_independent_430_076_006_000_076_share_one_previous_stem",
        )
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE151_INDEPENDENT_N5)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_152_151_139_103_and_w_scoreboards_still_compute(self):
        """Cycle 152 I-only, 151 previous-stem, 139 076, 103 I-only, W stay."""
        prior_152 = TestMamariI4gram630076010079IOnlyScoreboard()
        prior_152.setUp()
        prior_152.test_i_hits_are_one_on_ia_at_leftover_start()
        prior_152.test_4gram_is_zero_off_i_and_i_only()
        prior_152.test_survey_matches_computed_lock()
        prior_151 = TestMamariIIndependent076010079006700Preceded072Scoreboard()
        prior_151.setUp()
        prior_151.test_one_of_two_preceded_by_072_and_claim_loses()
        prior_151.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-153 previous-stem lock."""
        lock = self.survey["i_independent_430_076_006_000_076_previous_stem"]
        self.assertEqual(lock["cycle"], 153)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_one_previous_stem"])
        self.assertEqual(
            lock["hypothesis_share_one_previous_stem"],
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(tuple(lock["tokens5"]), GRAM5_INDEPENDENT)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_sites"], STANDING_N_SITES)
        self.assertEqual(lock["N_sites"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 2)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_previous_sites"]),
            STANDING_NO_PREVIOUS_SITES,
        )
        self.assertEqual(
            lock["N_distinct_previous_stems"],
            STANDING_N_DISTINCT_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_distinct_previous_stems"], 2)
        self.assertEqual(
            tuple(lock["distinct_previous_stems"]),
            STANDING_DISTINCT_PREVIOUS_STEMS,
        )
        self.assertEqual(
            tuple(lock["per_site_previous_stems"]),
            STANDING_PER_SITE_PREVIOUS,
        )
        self.assertEqual(
            tuple(
                (row["previous_stem"], tuple(tuple(site) for site in row["sites"]))
                for row in lock["sites_per_previous_stem"]
            ),
            STANDING_SITES_PER_PREVIOUS_STEM,
        )
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(
            lock["i_independent_430_076_006_000_076_share_one_previous_stem"]
        )
        self.assertEqual(
            lock["i_independent_430_076_006_000_076_share_one_previous_stem"],
            STANDING_I_INDEPENDENT_430_076_006_000_076_SHARE_ONE_PREVIOUS_STEM,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle151_independent_n5"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_4gram_630_076_010_079_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_independent_076_010_079_006_700_preceded_072_unchanged"]
        )
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
        self.assertEqual(self.survey["i_4gram_630_076_010_079_i_only"]["cycle"], 152)
        self.assertTrue(
            self.survey["i_4gram_630_076_010_079_i_only"][
                "i_4gram_630_076_010_079_is_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_independent_076_010_079_006_700_preceded_072"]["cycle"],
            151,
        )
        self.assertFalse(
            self.survey["i_independent_076_010_079_006_700_preceded_072"][
                "i_independent_076_010_079_006_700_both_preceded_by_072"
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


class TestMamariIIndependent430076006000076PreviousStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 153 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
