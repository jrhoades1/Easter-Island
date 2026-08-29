"""I's cycle-141 overlap 3-gram vs the two locked 5-grams.

Cycle 142 text-search lock. Uses already-vendored A–V and the
cycle-141 leftover overlap 3-gram 076 010 079 (I-only, N_on_I=8).
Does not retune that 3-gram or the two 5-grams. Does not vendor
a new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

For each of the locked 8 I sites, whether the 3-gram sits as
the exact consecutive suffix of cycle-103 999 071 076 010 079
or as the exact consecutive prefix of independent
076 010 079 006 700. Hypothesis: every I occurrence sits
inside one of those two 5-grams. Measured: 3 cycle-103
(Ia4[8]/Ia4[27]/Ia5[110]), 2 independent (Ia6[19]/Ia13[72]),
3 leftover (Ia5[139]/Ia12[34]/Ia14[83]). Claim that can lose:
i_overlap_3gram_076_010_079_all_inside_two_5grams. The claim
is false. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_independent_n5_076_scoreboard import (
    TestMamariIIndependentN5076Scoreboard,
)
from tests.test_mamari_i_independent_n5_cycle103_n3_overlap_scoreboard import (
    STANDING_SHARED_N3,
    TestMamariIIndependentN5Cycle103N3OverlapScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_010_079_i_only_scoreboard import (
    GRAM3,
    STANDING_I_SITES,
    STANDING_N_ON_I,
    TestMamariIOverlap3gram076010079IOnlyScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HYPOTHESIS_ALL_INSIDE = True
CLASS_CYCLE103 = "cycle103"
CLASS_INDEPENDENT = "independent"
CLASS_LEFTOVER = "leftover"
CYCLE103_SUFFIX_OFFSET = 2
INDEPENDENT_PREFIX_OFFSET = 0
STANDING_N3 = 3
STANDING_N5 = 5
STANDING_IA_HITS = 8
STANDING_IB_HITS = 0
STANDING_N_IN_CYCLE103 = 3
STANDING_N_IN_INDEPENDENT = 2
STANDING_N_LEFTOVER = 3
STANDING_CYCLE103_SITES = (
    (SIDE_IA, "Ia4", 8),
    (SIDE_IA, "Ia4", 27),
    (SIDE_IA, "Ia5", 110),
)
STANDING_INDEPENDENT_SITES = (
    (SIDE_IA, "Ia6", 19),
    (SIDE_IA, "Ia13", 72),
)
STANDING_LEFTOVER_SITES = (
    (SIDE_IA, "Ia5", 139),
    (SIDE_IA, "Ia12", 34),
    (SIDE_IA, "Ia14", 83),
)
STANDING_CLASSES = (
    CLASS_CYCLE103,
    CLASS_CYCLE103,
    CLASS_CYCLE103,
    CLASS_LEFTOVER,
    CLASS_INDEPENDENT,
    CLASS_LEFTOVER,
    CLASS_INDEPENDENT,
    CLASS_LEFTOVER,
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_overlap_3gram_076_010_079_all_inside_two_5grams"
STANDING_I_OVERLAP_3GRAM_076_010_079_ALL_INSIDE_TWO_5GRAMS = False
STANDING_RESULT = "i_overlap_3gram_inside_two_5grams"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False


def line_stems_for_site(
    i_sides: dict[str, list[list[str]]],
    site: tuple[str, str, int],
) -> list[str]:
    """Ia line stems for a locked (side, line, index) site."""
    side, line, _index = site
    return i_sides[side][IA_LINE_NAMES.index(line)]


def site_inside_cycle103(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
    cycle103: tuple[str, ...] = GRAM5,
) -> bool:
    """True iff gram3 at index is the exact suffix of cycle-103."""
    if tuple(stems[index : index + len(gram3)]) != gram3:
        return False
    start = index - CYCLE103_SUFFIX_OFFSET
    if start < 0:
        return False
    return tuple(stems[start : start + len(cycle103)]) == cycle103


def site_inside_independent(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
    independent: tuple[str, ...] = MAXIMAL_N5_010,
) -> bool:
    """True iff gram3 at index is the exact prefix of the independent 5-gram."""
    if tuple(stems[index : index + len(gram3)]) != gram3:
        return False
    window = stems[index : index + len(independent)]
    return tuple(window) == independent


def classify_3gram_site(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
    cycle103: tuple[str, ...] = GRAM5,
    independent: tuple[str, ...] = MAXIMAL_N5_010,
) -> str:
    """cycle103, independent, or leftover. Suffix/prefix only."""
    in_cycle103 = site_inside_cycle103(stems, index, gram3, cycle103)
    in_independent = site_inside_independent(stems, index, gram3, independent)
    if in_cycle103:
        return CLASS_CYCLE103
    if in_independent:
        return CLASS_INDEPENDENT
    return CLASS_LEFTOVER


def classify_i_sites(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    gram3: tuple[str, ...] = GRAM3,
    cycle103: tuple[str, ...] = GRAM5,
    independent: tuple[str, ...] = MAXIMAL_N5_010,
) -> tuple[str, ...]:
    """Per-site class for the locked I 3-gram hits."""
    return tuple(
        classify_3gram_site(
            line_stems_for_site(i_sides, site),
            site[2],
            gram3,
            cycle103,
            independent,
        )
        for site in sites
    )


def sites_with_class(
    sites: tuple[tuple[str, str, int], ...],
    classes: tuple[str, ...],
    label: str,
) -> tuple[tuple[str, str, int], ...]:
    """Sites whose locked class equals label."""
    return tuple(
        site
        for site, cls in zip(sites, classes, strict=True)
        if cls == label
    )


def i_overlap_3gram_076_010_079_all_inside_two_5grams(
    leftover_sites: tuple[tuple[str, str, int], ...],
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff every I 3-gram site sits inside one of the two 5-grams.

    An empty I-site set is false here (the cycle-141 8 sites must
    be present and none may be leftover).
    """
    return bool(i_sites) and leftover_sites == ()


class TestIOverlap3gramInsideTwo5gramsHelpers(unittest.TestCase):
    """Helpers on cycle-141 overlap tokens. No CV, no LLM."""

    def test_inside_requires_exact_suffix_or_prefix(self):
        """Suffix of cycle-103 and prefix of independent count; a near-miss does not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "010", "079"))
        self.assertEqual(GRAM3, STANDING_SHARED_N3)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertEqual(GRAM5[-STANDING_N3:], GRAM3)
        self.assertEqual(MAXIMAL_N5_010[:STANDING_N3], GRAM3)
        self.assertEqual(CYCLE103_SUFFIX_OFFSET, 2)
        self.assertEqual(INDEPENDENT_PREFIX_OFFSET, 0)
        cycle103_line = ["700", "999", "071", "076", "010", "079", "071"]
        self.assertTrue(site_inside_cycle103(cycle103_line, 3))
        self.assertFalse(site_inside_independent(cycle103_line, 3))
        self.assertEqual(classify_3gram_site(cycle103_line, 3), CLASS_CYCLE103)
        independent_line = ["678", "630", "076", "010", "079", "006", "700"]
        self.assertTrue(site_inside_independent(independent_line, 2))
        self.assertFalse(site_inside_cycle103(independent_line, 2))
        self.assertEqual(classify_3gram_site(independent_line, 2), CLASS_INDEPENDENT)
        almost_071 = ["999", "072", "076", "010", "079"]
        self.assertFalse(site_inside_cycle103(almost_071, 2))
        self.assertFalse(site_inside_independent(almost_071, 2))
        self.assertEqual(classify_3gram_site(almost_071, 2), CLASS_LEFTOVER)
        suffix4_only = ["200", "071", "076", "010", "079"]
        self.assertFalse(site_inside_cycle103(suffix4_only, 2))
        self.assertEqual(classify_3gram_site(suffix4_only, 2), CLASS_LEFTOVER)
        gapped = ["999", "071", "076", "006", "079"]
        self.assertFalse(site_inside_cycle103(gapped, 2))
        self.assertEqual(classify_3gram_site(gapped, 2), CLASS_LEFTOVER)
        self.assertFalse(site_inside_cycle103(["076", "010", "079"], 0))
        self.assertEqual(provider.get_call_history(), [])

    def test_all_inside_requires_empty_leftover_and_present_sites(self):
        """Boolean is True only when I sites exist and leftover is empty."""
        provider = MockProvider()
        self.assertTrue(
            i_overlap_3gram_076_010_079_all_inside_two_5grams((), STANDING_I_SITES)
        )
        self.assertFalse(
            i_overlap_3gram_076_010_079_all_inside_two_5grams(
                STANDING_LEFTOVER_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertFalse(i_overlap_3gram_076_010_079_all_inside_two_5grams((), ()))
        self.assertEqual(STANDING_CLAIM, "i_overlap_3gram_076_010_079_all_inside_two_5grams")
        self.assertFalse(STANDING_I_OVERLAP_3GRAM_076_010_079_ALL_INSIDE_TWO_5GRAMS)
        self.assertNotEqual(
            STANDING_I_OVERLAP_3GRAM_076_010_079_ALL_INSIDE_TWO_5GRAMS,
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_overlap_3gram_is_suffix_of_cycle103_and_prefix_of_independent(self):
        """3-gram is the locked shared run, not a retuned inventory."""
        provider = MockProvider()
        self.assertEqual(GRAM3, STANDING_SHARED_N3)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, MAXIMAL_N5_010)
        self.assertTrue(is_contiguous_substring(GRAM3, GRAM5))
        self.assertTrue(is_contiguous_substring(GRAM3, MAXIMAL_N5_010))
        self.assertEqual(GRAM5[CYCLE103_SUFFIX_OFFSET:], GRAM3)
        self.assertEqual(MAXIMAL_N5_010[INDEPENDENT_PREFIX_OFFSET:STANDING_N3], GRAM3)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(len(GRAM5), STANDING_N5)
        self.assertEqual(len(MAXIMAL_N5_010), STANDING_N5)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariIOverlap3gramInsideTwo5gramsScoreboard(unittest.TestCase):
    """Cited-fixture leftover overlap 3-gram 5-gram-inside lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM3, self.i_sides)
        self.classes = classify_i_sites(self.i_sides, self.i_sites)
        self.cycle103_sites = sites_with_class(
            self.i_sites,
            self.classes,
            CLASS_CYCLE103,
        )
        self.independent_sites = sites_with_class(
            self.i_sites,
            self.classes,
            CLASS_INDEPENDENT,
        )
        self.leftover_sites = sites_with_class(
            self.i_sites,
            self.classes,
            CLASS_LEFTOVER,
        )
        self.n_on_i = len(self.i_sites)
        self.n_in_cycle103 = len(self.cycle103_sites)
        self.n_in_independent = len(self.independent_sites)
        self.n_leftover = len(self.leftover_sites)
        self.claim_holds = i_overlap_3gram_076_010_079_all_inside_two_5grams(
            self.leftover_sites,
            self.i_sites,
        )

    def test_tokens_are_cycle_141_lock_not_retuned(self):
        """3-gram and both 5-grams stay the cycle-141/140/103 locks."""
        self.assertEqual(GRAM3, STANDING_SHARED_N3)
        self.assertEqual(GRAM3, ("076", "010", "079"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        prior_141 = self.survey["i_overlap_3gram_076_010_079_i_only"]
        self.assertEqual(prior_141["cycle"], 141)
        self.assertEqual(tuple(prior_141["tokens3"]), GRAM3)
        self.assertEqual(prior_141["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(prior_141["N_on_I"], 8)
        self.assertEqual(
            tuple(tuple(row) for row in prior_141["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertTrue(prior_141["i_overlap_3gram_076_010_079_is_i_only"])
        prior_140 = self.survey["i_independent_n5_cycle103_n3_overlap"]
        self.assertEqual(prior_140["cycle"], 140)
        self.assertEqual(tuple(prior_140["overlaps"][0]["shared"]), GRAM3)
        self.assertEqual(tuple(prior_140["cycle103_tokens5"]), GRAM5)
        self.assertEqual(self.survey["i_independent_n5_maximals_076"]["cycle"], 139)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_eight_sites_split_3_2_3_and_claim_loses(self):
        """N_on_I=8: 3 cycle-103, 2 independent, 3 leftover. Claim loses."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_on_i, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, 8)
        self.assertEqual(self.n_on_i, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(self.classes, STANDING_CLASSES)
        self.assertEqual(self.cycle103_sites, STANDING_CYCLE103_SITES)
        self.assertEqual(self.independent_sites, STANDING_INDEPENDENT_SITES)
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.n_in_cycle103, STANDING_N_IN_CYCLE103)
        self.assertEqual(STANDING_N_IN_CYCLE103, 3)
        self.assertEqual(self.n_in_independent, STANDING_N_IN_INDEPENDENT)
        self.assertEqual(STANDING_N_IN_INDEPENDENT, 2)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 3)
        self.assertEqual(
            self.n_in_cycle103 + self.n_in_independent + self.n_leftover,
            self.n_on_i,
        )
        for side, line, index in STANDING_CYCLE103_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertTrue(site_inside_cycle103(stems, index))
            self.assertFalse(site_inside_independent(stems, index))
            self.assertEqual(classify_3gram_site(stems, index), CLASS_CYCLE103)
        for side, line, index in STANDING_INDEPENDENT_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertTrue(site_inside_independent(stems, index))
            self.assertFalse(site_inside_cycle103(stems, index))
            self.assertEqual(classify_3gram_site(stems, index), CLASS_INDEPENDENT)
        for side, line, index in STANDING_LEFTOVER_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertFalse(site_inside_cycle103(stems, index))
            self.assertFalse(site_inside_independent(stems, index))
            self.assertEqual(classify_3gram_site(stems, index), CLASS_LEFTOVER)
        self.assertEqual(
            i_overlap_3gram_076_010_079_all_inside_two_5grams(
                self.leftover_sites,
                self.i_sites,
            ),
            STANDING_I_OVERLAP_3GRAM_076_010_079_ALL_INSIDE_TWO_5GRAMS,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_OVERLAP_3GRAM_076_010_079_ALL_INSIDE_TWO_5GRAMS,
        )
        self.assertFalse(STANDING_I_OVERLAP_3GRAM_076_010_079_ALL_INSIDE_TWO_5GRAMS)
        self.assertTrue(HYPOTHESIS_ALL_INSIDE)
        self.assertEqual(STANDING_CLAIM, "i_overlap_3gram_076_010_079_all_inside_two_5grams")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_141_140_139_103_and_w_scoreboards_still_compute(self):
        """Cycle 141 I-only, 140 overlap, 139 076, 103 I-only, and W stay."""
        prior_141 = TestMamariIOverlap3gram076010079IOnlyScoreboard()
        prior_141.setUp()
        prior_141.test_i_hits_are_eight_on_ia()
        prior_141.test_3gram_is_zero_off_i_and_i_only()
        prior_141.test_survey_matches_computed_lock()
        prior_140 = TestMamariIIndependentN5Cycle103N3OverlapScoreboard()
        prior_140.setUp()
        prior_140.test_counts_1_of_4_and_hypothesis_none_share_loses()
        prior_140.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-142 inside-two-5grams lock."""
        lock = self.survey["i_overlap_3gram_inside_two_5grams"]
        self.assertEqual(lock["cycle"], 142)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_inside_two_5grams"])
        self.assertEqual(lock["hypothesis_all_inside_two_5grams"], HYPOTHESIS_ALL_INSIDE)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(tuple(lock["cycle103_tokens5"]), GRAM5)
        self.assertEqual(tuple(lock["independent_tokens5"]), MAXIMAL_N5_010)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["i_hits"], STANDING_N_ON_I)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_in_cycle103"], STANDING_N_IN_CYCLE103)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle103_sites"]),
            STANDING_CYCLE103_SITES,
        )
        self.assertEqual(
            lock["N_in_independent_076_010_079_006_700"],
            STANDING_N_IN_INDEPENDENT,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["independent_sites"]),
            STANDING_INDEPENDENT_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(tuple(lock["classes"]), STANDING_CLASSES)
        self.assertEqual(
            [list(site) for site in STANDING_LEFTOVER_SITES],
            lock["leftover_sites"],
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_overlap_3gram_076_010_079_all_inside_two_5grams"])
        self.assertEqual(
            lock["i_overlap_3gram_076_010_079_all_inside_two_5grams"],
            STANDING_I_OVERLAP_3GRAM_076_010_079_ALL_INSIDE_TWO_5GRAMS,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_010_079_i_only_unchanged"])
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
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["cycle"], 141)
        self.assertTrue(
            self.survey["i_overlap_3gram_076_010_079_i_only"][
                "i_overlap_3gram_076_010_079_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["N_on_I"], 8)
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
        self.assertEqual(self.survey["i_exception_n4_071_065_071_999_i_only"]["cycle"], 138)
        self.assertTrue(
            self.survey["i_exception_n4_071_065_071_999_i_only"][
                "i_exception_n4_071_065_071_999_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_maximals_076"]["cycle"], 137)
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


class TestMamariIOverlap3gramInsideTwo5gramsImageSnapshot(unittest.TestCase):
    """Cycle 142 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
