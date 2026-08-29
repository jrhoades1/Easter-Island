"""I's cycle-144 majority leftover backward 4-gram vs cycle-103.

Cycle 145 text-search lock. Uses already-vendored A–V and the
cycle-144 majority leftover backward 4-gram 071 076 010 079
(the suffix-4 of cycle-103 999 071 076 010 079). Does not
retune leftover 3-gram sites. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Locks exact consecutive hits of 071 076 010 079 on tablet I
and on every other vendored tablet A–H and J–V. For each I
site, whether the 4-gram sits as the exact consecutive suffix
of cycle-103 999 071 076 010 079. Hypothesis: every I
occurrence sits inside that 5-gram. Measured: N_on_I=5;
N_in_cycle103=3 at Ia4[7]/Ia4[26]/Ia5[109]; N_leftover=2 at
Ia12[33]/Ia14[82]; N_off_I=0. Claim that can lose:
i_4gram_071_076_010_079_all_inside_cycle103_5gram. The claim
is false. Do not retune.

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
from tests.test_mamari_i_independent_n5_cycle103_n3_overlap_scoreboard import (
    TestMamariIIndependentN5Cycle103N3OverlapScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
)
from tests.test_mamari_i_leftover_076_010_079_backward_4gram_scoreboard import (
    STANDING_BACKWARD_4GRAM_071,
    TestMamariILeftover076010079Backward4gramScoreboard,
)
from tests.test_mamari_i_nge4_scoreboard import (
    STANDING_N4_SUFFIX,
    STANDING_N4_SUFFIX_SITES,
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_010_079_i_only_scoreboard import (
    TestMamariIOverlap3gram076010079IOnlyScoreboard,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    STANDING_CYCLE103_SITES as OVERLAP_CYCLE103_SITES,
    STANDING_LEFTOVER_SITES as OVERLAP_LEFTOVER_SITES,
    TestMamariIOverlap3gramInsideTwo5gramsScoreboard,
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

HYPOTHESIS_ALL_INSIDE = True
CLASS_CYCLE103 = "cycle103"
CLASS_LEFTOVER = "leftover"
CYCLE103_SUFFIX_OFFSET = 1
GRAM4 = ("071", "076", "010", "079")
STANDING_N4 = 4
STANDING_N5 = 5
STANDING_I_HITS = 5
STANDING_IA_HITS = 5
STANDING_IB_HITS = 0
STANDING_N_ON_I = 5
STANDING_I_SITES = (
    (SIDE_IA, "Ia4", 7),
    (SIDE_IA, "Ia4", 26),
    (SIDE_IA, "Ia5", 109),
    (SIDE_IA, "Ia12", 33),
    (SIDE_IA, "Ia14", 82),
)
STANDING_IB_SITES = ()
STANDING_N_IN_CYCLE103 = 3
STANDING_N_LEFTOVER = 2
STANDING_CYCLE103_SITES = (
    (SIDE_IA, "Ia4", 7),
    (SIDE_IA, "Ia4", 26),
    (SIDE_IA, "Ia5", 109),
)
STANDING_LEFTOVER_SITES = (
    (SIDE_IA, "Ia12", 33),
    (SIDE_IA, "Ia14", 82),
)
STANDING_CLASSES = (
    CLASS_CYCLE103,
    CLASS_CYCLE103,
    CLASS_CYCLE103,
    CLASS_LEFTOVER,
    CLASS_LEFTOVER,
)
STANDING_OFF_I_HITS = 0
STANDING_N_OFF_I = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_4gram_071_076_010_079_all_inside_cycle103_5gram"
STANDING_I_4GRAM_071_076_010_079_ALL_INSIDE_CYCLE103_5GRAM = False
STANDING_RESULT = "i_4gram_071_076_010_079_inside_cycle103"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False


def site_inside_cycle103(
    stems: list[str],
    index: int,
    gram4: tuple[str, ...] = GRAM4,
    cycle103: tuple[str, ...] = GRAM5,
) -> bool:
    """True iff gram4 at index is the exact suffix of cycle-103."""
    if tuple(stems[index : index + len(gram4)]) != gram4:
        return False
    start = index - CYCLE103_SUFFIX_OFFSET
    if start < 0:
        return False
    return tuple(stems[start : start + len(cycle103)]) == cycle103


def classify_4gram_site(
    stems: list[str],
    index: int,
    gram4: tuple[str, ...] = GRAM4,
    cycle103: tuple[str, ...] = GRAM5,
) -> str:
    """cycle103 or leftover. Suffix only."""
    if site_inside_cycle103(stems, index, gram4, cycle103):
        return CLASS_CYCLE103
    return CLASS_LEFTOVER


def classify_i_sites(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    gram4: tuple[str, ...] = GRAM4,
    cycle103: tuple[str, ...] = GRAM5,
) -> tuple[str, ...]:
    """Per-site class for the I 4-gram hits."""
    return tuple(
        classify_4gram_site(
            line_stems_for_site(i_sides, site),
            site[2],
            gram4,
            cycle103,
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


def i_4gram_071_076_010_079_all_inside_cycle103_5gram(
    leftover_sites: tuple[tuple[str, str, int], ...],
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff every I 4-gram site sits inside the cycle-103 5-gram.

    An empty I-site set is false here (the five I sites must
    be present and none may be leftover).
    """
    return bool(i_sites) and leftover_sites == ()


class TestI4gram071076010079InsideCycle103Helpers(unittest.TestCase):
    """Helpers on cycle-144 majority leftover backward tokens. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("071", "076", "010", "079"))
        self.assertEqual(GRAM4, STANDING_N4_SUFFIX)
        self.assertEqual(GRAM4, STANDING_BACKWARD_4GRAM_071)
        adjacent = [list(GRAM4), list(GRAM4)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4), 2)
        overlap = [["071", "076", "010", "079", "071", "076", "010", "079"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4), 2)
        gapped = [list(GRAM4[:2]) + ["006"] + list(GRAM4[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_inside_requires_exact_cycle103_suffix(self):
        """Suffix of cycle-103 counts; a near-miss or start-of-line does not."""
        provider = MockProvider()
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(GRAM5[-STANDING_N4:], GRAM4)
        self.assertEqual(CYCLE103_SUFFIX_OFFSET, 1)
        cycle103_line = ["700", "999", "071", "076", "010", "079", "071"]
        self.assertTrue(site_inside_cycle103(cycle103_line, 2))
        self.assertEqual(classify_4gram_site(cycle103_line, 2), CLASS_CYCLE103)
        leftover_200 = ["200", "071", "076", "010", "079", "029"]
        self.assertFalse(site_inside_cycle103(leftover_200, 1))
        self.assertEqual(classify_4gram_site(leftover_200, 1), CLASS_LEFTOVER)
        leftover_076 = ["076", "071", "076", "010", "079", "053"]
        self.assertFalse(site_inside_cycle103(leftover_076, 1))
        self.assertEqual(classify_4gram_site(leftover_076, 1), CLASS_LEFTOVER)
        almost_072 = ["999", "072", "076", "010", "079"]
        self.assertFalse(site_inside_cycle103(almost_072, 1))
        self.assertEqual(classify_4gram_site(almost_072, 1), CLASS_LEFTOVER)
        gapped = ["999", "071", "076", "006", "079"]
        self.assertFalse(site_inside_cycle103(gapped, 1))
        self.assertFalse(site_inside_cycle103(["071", "076", "010", "079"], 0))
        mismatch = ["071", "076", "010", "006"]
        self.assertFalse(site_inside_cycle103(mismatch, 0))
        self.assertEqual(provider.get_call_history(), [])

    def test_all_inside_requires_empty_leftover_and_present_sites(self):
        """Boolean is True only when I sites exist and leftover is empty."""
        provider = MockProvider()
        self.assertTrue(
            i_4gram_071_076_010_079_all_inside_cycle103_5gram((), STANDING_I_SITES)
        )
        self.assertFalse(
            i_4gram_071_076_010_079_all_inside_cycle103_5gram(
                STANDING_LEFTOVER_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertFalse(i_4gram_071_076_010_079_all_inside_cycle103_5gram((), ()))
        self.assertEqual(STANDING_CLAIM, "i_4gram_071_076_010_079_all_inside_cycle103_5gram")
        self.assertFalse(STANDING_I_4GRAM_071_076_010_079_ALL_INSIDE_CYCLE103_5GRAM)
        self.assertNotEqual(
            STANDING_I_4GRAM_071_076_010_079_ALL_INSIDE_CYCLE103_5GRAM,
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_4gram_is_cycle103_suffix_not_the_5gram(self):
        """4-gram is the locked suffix-4, not a retuned inventory."""
        provider = MockProvider()
        self.assertEqual(GRAM4, STANDING_N4_SUFFIX)
        self.assertNotEqual(GRAM4, GRAM5)
        self.assertNotEqual(GRAM4, MAXIMAL_N5_010)
        self.assertTrue(is_contiguous_substring(GRAM4, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM4, MAXIMAL_N5_010))
        self.assertEqual(GRAM5[CYCLE103_SUFFIX_OFFSET:], GRAM4)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(len(GRAM4), STANDING_N4)
        self.assertEqual(STANDING_N4, 4)
        self.assertEqual(len(GRAM5), STANDING_N5)
        self.assertLess(len(GRAM4), 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI4gram071076010079InsideCycle103Scoreboard(unittest.TestCase):
    """Cited-fixture majority leftover backward-4 inside-cycle103 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM4, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM4)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.classes = classify_i_sites(self.i_sides, self.i_sites)
        self.cycle103_sites = sites_with_class(
            self.i_sites,
            self.classes,
            CLASS_CYCLE103,
        )
        self.leftover_sites = sites_with_class(
            self.i_sites,
            self.classes,
            CLASS_LEFTOVER,
        )
        self.n_on_i = len(self.i_sites)
        self.n_in_cycle103 = len(self.cycle103_sites)
        self.n_leftover = len(self.leftover_sites)
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM4, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM4, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.claim_holds = i_4gram_071_076_010_079_all_inside_cycle103_5gram(
            self.leftover_sites,
            self.i_sites,
        )

    def test_tokens_are_cycle_144_majority_backward_not_retuned(self):
        """4-gram is the cycle-144 majority leftover backward lock."""
        self.assertEqual(GRAM4, STANDING_BACKWARD_4GRAM_071)
        self.assertEqual(GRAM4, STANDING_N4_SUFFIX)
        self.assertEqual(GRAM4, ("071", "076", "010", "079"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertEqual(self.i_sites, STANDING_N4_SUFFIX_SITES)
        prior_144 = self.survey["i_leftover_076_010_079_backward_4gram"]
        self.assertEqual(prior_144["cycle"], 144)
        self.assertEqual(
            tuple(prior_144["distinct_backward_4grams"][1]),
            GRAM4,
        )
        self.assertEqual(prior_144["N_distinct_backward_4grams"], 2)
        self.assertFalse(prior_144["i_leftover_076_010_079_share_one_backward_4gram"])
        prior_142 = self.survey["i_overlap_3gram_inside_two_5grams"]
        self.assertEqual(prior_142["cycle"], 142)
        self.assertEqual(prior_142["N_leftover"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in prior_142["leftover_sites"]),
            OVERLAP_LEFTOVER_SITES,
        )
        self.assertFalse(prior_142["i_overlap_3gram_076_010_079_all_inside_two_5grams"])
        prior_141 = self.survey["i_overlap_3gram_076_010_079_i_only"]
        self.assertEqual(prior_141["cycle"], 141)
        self.assertEqual(prior_141["N_on_I"], 8)
        self.assertTrue(prior_141["i_overlap_3gram_076_010_079_is_i_only"])
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_five_sites_split_3_2_and_claim_loses(self):
        """N_on_I=5: 3 cycle-103, 2 leftover. Claim loses."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_on_i, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, 5)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(self.n_on_i, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(self.classes, STANDING_CLASSES)
        self.assertEqual(self.cycle103_sites, STANDING_CYCLE103_SITES)
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.n_in_cycle103, STANDING_N_IN_CYCLE103)
        self.assertEqual(STANDING_N_IN_CYCLE103, 3)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 2)
        self.assertEqual(self.n_in_cycle103 + self.n_leftover, self.n_on_i)
        self.assertEqual(nge4_sites(GRAM4, self.i_sides), STANDING_I_SITES)
        self.assertEqual(STANDING_IB_SITES, ())
        for site, overlap_3 in zip(
            STANDING_CYCLE103_SITES,
            OVERLAP_CYCLE103_SITES,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N4]), GRAM4)
            self.assertTrue(site_inside_cycle103(stems, index))
            self.assertEqual(classify_4gram_site(stems, index), CLASS_CYCLE103)
            self.assertEqual(side, SIDE_IA)
            self.assertEqual(index, overlap_3[2] - 1)
            self.assertEqual(line, overlap_3[1])
            self.assertEqual(
                tuple(stems[index - CYCLE103_SUFFIX_OFFSET : index + STANDING_N4]),
                GRAM5,
            )
        leftover_3gram = (
            (SIDE_IA, "Ia12", 34),
            (SIDE_IA, "Ia14", 83),
        )
        for site, overlap_3 in zip(
            STANDING_LEFTOVER_SITES,
            leftover_3gram,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N4]), GRAM4)
            self.assertFalse(site_inside_cycle103(stems, index))
            self.assertEqual(classify_4gram_site(stems, index), CLASS_LEFTOVER)
            self.assertEqual(side, SIDE_IA)
            self.assertEqual(index, overlap_3[2] - 1)
            self.assertEqual(line, overlap_3[1])
            self.assertNotEqual(stems[index - 1], "999")
        self.assertEqual(
            i_4gram_071_076_010_079_all_inside_cycle103_5gram(
                self.leftover_sites,
                self.i_sites,
            ),
            STANDING_I_4GRAM_071_076_010_079_ALL_INSIDE_CYCLE103_5GRAM,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_4GRAM_071_076_010_079_ALL_INSIDE_CYCLE103_5GRAM,
        )
        self.assertFalse(STANDING_I_4GRAM_071_076_010_079_ALL_INSIDE_CYCLE103_5GRAM)
        self.assertTrue(HYPOTHESIS_ALL_INSIDE)
        self.assertEqual(STANDING_CLAIM, "i_4gram_071_076_010_079_all_inside_cycle103_5gram")
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_4gram_is_zero_off_i(self):
        """4-gram is 0 on A–H and J–V. Ia has exactly 5. W is not a tablet."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, STANDING_N_OFF_I)
        self.assertEqual(STANDING_N_OFF_I, 0)
        self.assertEqual(STANDING_OFF_I_SITES, ())
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM4))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 5)
            else:
                self.assertEqual(count, 0)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_144_142_141_140_103_and_w_scoreboards_still_compute(self):
        """Cycle 144 backward, 142 inside, 141 I-only, 140, 103, W stay."""
        prior_144 = TestMamariILeftover076010079Backward4gramScoreboard()
        prior_144.setUp()
        prior_144.test_three_leftovers_have_two_distinct_backwards_and_claim_loses()
        prior_144.test_survey_matches_computed_lock()
        prior_142 = TestMamariIOverlap3gramInsideTwo5gramsScoreboard()
        prior_142.setUp()
        prior_142.test_eight_sites_split_3_2_3_and_claim_loses()
        prior_142.test_survey_matches_computed_lock()
        prior_141 = TestMamariIOverlap3gram076010079IOnlyScoreboard()
        prior_141.setUp()
        prior_141.test_i_hits_are_eight_on_ia()
        prior_141.test_3gram_is_zero_off_i_and_i_only()
        prior_141.test_survey_matches_computed_lock()
        prior_140 = TestMamariIIndependentN5Cycle103N3OverlapScoreboard()
        prior_140.setUp()
        prior_140.test_counts_1_of_4_and_hypothesis_none_share_loses()
        prior_140.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-145 inside-cycle103 lock."""
        lock = self.survey["i_4gram_071_076_010_079_inside_cycle103"]
        self.assertEqual(lock["cycle"], 145)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_inside_cycle103_5gram"])
        self.assertEqual(
            lock["hypothesis_all_inside_cycle103_5gram"],
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["cycle103_tokens5"]), GRAM5)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["i_hits"], STANDING_N_ON_I)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(lock["N_in_cycle103"], STANDING_N_IN_CYCLE103)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle103_sites"]),
            STANDING_CYCLE103_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(tuple(lock["classes"]), STANDING_CLASSES)
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(lock["N_off_I"], 0)
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
        self.assertFalse(lock["i_4gram_071_076_010_079_all_inside_cycle103_5gram"])
        self.assertEqual(
            lock["i_4gram_071_076_010_079_all_inside_cycle103_5gram"],
            STANDING_I_4GRAM_071_076_010_079_ALL_INSIDE_CYCLE103_5GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_backward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_forward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_inside_two_5grams_unchanged"])
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
        self.assertEqual(self.survey["i_leftover_076_010_079_backward_4gram"]["cycle"], 144)
        self.assertFalse(
            self.survey["i_leftover_076_010_079_backward_4gram"][
                "i_leftover_076_010_079_share_one_backward_4gram"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_010_079_backward_4gram"][
                "N_distinct_backward_4grams"
            ],
            2,
        )
        self.assertEqual(self.survey["i_leftover_076_010_079_forward_4gram"]["cycle"], 143)
        self.assertFalse(
            self.survey["i_leftover_076_010_079_forward_4gram"][
                "i_leftover_076_010_079_share_one_forward_4gram"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_inside_two_5grams"]["cycle"], 142)
        self.assertFalse(
            self.survey["i_overlap_3gram_inside_two_5grams"][
                "i_overlap_3gram_076_010_079_all_inside_two_5grams"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_inside_two_5grams"]["N_leftover"], 3)
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
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI4gram071076010079InsideCycle103ImageSnapshot(unittest.TestCase):
    """Cycle 145 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
