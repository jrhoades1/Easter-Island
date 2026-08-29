"""I's cycle-145 leftover 4-gram backward 5-gram lock.

Cycle 146 text-search lock. Uses already-vendored A–V and the
cycle-145 leftover sites of 4-gram 071 076 010 079
(Ia12[33], Ia14[82]). Does not retune that 4-gram or those
sites. Does not vendor a new tablet. Does not scrape X. W has
no Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not
redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

For each leftover site, the backward 5-gram Y 071 076 010 079
if the line has a previous stem before the 4-gram;
start-of-line is no-backward. Hypothesis: both leftover sites
share one backward 5-gram (one stem Y, not 999). Measured:
N_leftover=2, N_with_backward=2, N_distinct_backward_5grams=2
(200 071 076 010 079 at Ia12[33], 076 071 076 010 079 at
Ia14[82]). Claim that can lose:
i_leftover_071_076_010_079_share_one_backward_5gram. True
only if N_with_backward=2 and N_distinct_backward_5grams=1.
The claim is false. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_4gram_071_076_010_079_inside_cycle103_scoreboard import (
    GRAM4,
    STANDING_LEFTOVER_SITES,
    STANDING_N_LEFTOVER,
    TestMamariI4gram071076010079InsideCycle103Scoreboard,
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
from tests.test_mamari_i_overlap_3gram_076_010_079_i_only_scoreboard import (
    TestMamariIOverlap3gram076010079IOnlyScoreboard,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    TestMamariIOverlap3gramInsideTwo5gramsScoreboard,
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
STANDING_N4 = 4
STANDING_N5 = 5
STANDING_N_WITH_BACKWARD = 2
STANDING_N_DISTINCT_BACKWARD_5GRAMS = 2
STANDING_N_NO_BACKWARD = 0
STANDING_BACKWARD_5GRAM_200 = ("200", "071", "076", "010", "079")
STANDING_BACKWARD_5GRAM_076 = ("076", "071", "076", "010", "079")
STANDING_DISTINCT_BACKWARD_5GRAMS = (
    STANDING_BACKWARD_5GRAM_200,
    STANDING_BACKWARD_5GRAM_076,
)
STANDING_PER_SITE_BACKWARD = (
    STANDING_BACKWARD_5GRAM_200,
    STANDING_BACKWARD_5GRAM_076,
)
STANDING_SITES_PER_BACKWARD_5GRAM = (
    (STANDING_BACKWARD_5GRAM_200, ((SIDE_IA, "Ia12", 33),)),
    (STANDING_BACKWARD_5GRAM_076, ((SIDE_IA, "Ia14", 82),)),
)
STANDING_NO_BACKWARD_SITES = ()
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_071_076_010_079_share_one_backward_5gram"
STANDING_I_LEFTOVER_071_076_010_079_SHARE_ONE_BACKWARD_5GRAM = False
STANDING_RESULT = "i_leftover_071_076_010_079_backward_5gram"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
CYCLE103_PREFIX = "999"


def site_backward_5gram(
    stems: list[str],
    index: int,
    gram4: tuple[str, ...] = GRAM4,
) -> tuple[str, ...] | None:
    """Y 071 076 010 079 if a previous stem exists; None at start-of-line."""
    n4 = len(gram4)
    if tuple(stems[index : index + n4]) != gram4:
        return None
    if index == 0:
        return None
    return tuple(stems[index - 1 : index + n4])


def leftover_backward_5grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram4: tuple[str, ...] = GRAM4,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site backward 5-gram or None for the locked leftover sites."""
    return tuple(
        site_backward_5gram(line_stems_for_site(i_sides, site), site[2], gram4)
        for site in sites
    )


def sites_with_backward(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that have a previous stem before the 4-gram."""
    return tuple(
        site
        for site, back in zip(sites, backwards, strict=True)
        if back is not None
    )


def sites_without_backward(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that are start-of-line (no-backward)."""
    return tuple(
        site
        for site, back in zip(sites, backwards, strict=True)
        if back is None
    )


def group_sites_by_backward_5gram(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[tuple[str, ...], tuple[tuple[str, str, int], ...]], ...]:
    """Distinct backward 5-grams in first-seen order, with their sites."""
    groups: list[tuple[tuple[str, ...], list[tuple[str, str, int]]]] = []
    index_by_gram: dict[tuple[str, ...], int] = {}
    for site, back in zip(sites, backwards, strict=True):
        if back is None:
            continue
        if back not in index_by_gram:
            index_by_gram[back] = len(groups)
            groups.append((back, [site]))
        else:
            groups[index_by_gram[back]][1].append(site)
    return tuple((gram, tuple(gram_sites)) for gram, gram_sites in groups)


def i_leftover_071_076_010_079_share_one_backward_5gram(
    n_with_backward: int,
    n_distinct_backward_5grams: int,
) -> bool:
    """True iff N_with_backward=2 and N_distinct_backward_5grams=1."""
    return n_with_backward == 2 and n_distinct_backward_5grams == 1


class TestILeftover071076010079Backward5gramHelpers(unittest.TestCase):
    """Helpers on cycle-145 leftover sites. No CV, no LLM."""

    def test_backward_requires_previous_stem_before_4gram(self):
        """A previous stem is a 5-gram; start-of-line is no-backward."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("071", "076", "010", "079"))
        self.assertEqual(GRAM4, STANDING_BACKWARD_4GRAM_071)
        self.assertEqual(len(GRAM4), STANDING_N4)
        self.assertEqual(STANDING_N5, STANDING_N4 + 1)
        has_prev = ["011", "200", "071", "076", "010", "079", "029"]
        self.assertEqual(
            site_backward_5gram(has_prev, 2),
            ("200", "071", "076", "010", "079"),
        )
        start_of_line = ["071", "076", "010", "079", "029"]
        self.assertIsNone(site_backward_5gram(start_of_line, 0))
        self.assertIsNone(site_backward_5gram(["071", "076", "010", "079"], 0))
        mismatch = ["200", "071", "076", "010", "006"]
        self.assertIsNone(site_backward_5gram(mismatch, 1))
        gapped = ["200", "071", "076", "011", "079"]
        self.assertIsNone(site_backward_5gram(gapped, 1))
        cycle103 = ["999", "071", "076", "010", "079"]
        self.assertEqual(site_backward_5gram(cycle103, 1), GRAM5)
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_two_backwards_and_one_distinct(self):
        """Boolean is True only when N_with_backward=2 and N_distinct=1."""
        provider = MockProvider()
        self.assertTrue(i_leftover_071_076_010_079_share_one_backward_5gram(2, 1))
        self.assertFalse(i_leftover_071_076_010_079_share_one_backward_5gram(2, 2))
        self.assertFalse(i_leftover_071_076_010_079_share_one_backward_5gram(1, 1))
        self.assertFalse(i_leftover_071_076_010_079_share_one_backward_5gram(0, 0))
        self.assertFalse(i_leftover_071_076_010_079_share_one_backward_5gram(2, 0))
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_071_076_010_079_share_one_backward_5gram",
        )
        self.assertFalse(STANDING_I_LEFTOVER_071_076_010_079_SHARE_ONE_BACKWARD_5GRAM)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_071_076_010_079_SHARE_ONE_BACKWARD_5GRAM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_grouping_keeps_first_seen_order_and_skips_none(self):
        """Sites group by backward 5-gram; no-backward sites are omitted."""
        provider = MockProvider()
        sites = (
            (SIDE_IA, "Ia12", 33),
            (SIDE_IA, "Ia14", 82),
        )
        two_distinct = (
            STANDING_BACKWARD_5GRAM_200,
            STANDING_BACKWARD_5GRAM_076,
        )
        self.assertEqual(
            group_sites_by_backward_5gram(sites, two_distinct),
            STANDING_SITES_PER_BACKWARD_5GRAM,
        )
        shared = (
            STANDING_BACKWARD_5GRAM_200,
            STANDING_BACKWARD_5GRAM_200,
        )
        self.assertEqual(
            group_sites_by_backward_5gram(sites, shared),
            ((STANDING_BACKWARD_5GRAM_200, sites),),
        )
        one_none = (STANDING_BACKWARD_5GRAM_200, None)
        self.assertEqual(
            group_sites_by_backward_5gram(sites, one_none),
            ((STANDING_BACKWARD_5GRAM_200, (sites[0],)),),
        )
        self.assertEqual(sites_with_backward(sites, one_none), (sites[0],))
        self.assertEqual(sites_without_backward(sites, one_none), (sites[1],))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover071076010079Backward5gramScoreboard(unittest.TestCase):
    """Cited-fixture leftover 4-gram backward-5 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.backwards = leftover_backward_5grams(self.i_sides, self.leftover_sites)
        self.with_backward = sites_with_backward(self.leftover_sites, self.backwards)
        self.no_backward = sites_without_backward(self.leftover_sites, self.backwards)
        self.groups = group_sites_by_backward_5gram(self.leftover_sites, self.backwards)
        self.n_leftover = len(self.leftover_sites)
        self.n_with_backward = len(self.with_backward)
        self.n_no_backward = len(self.no_backward)
        self.n_distinct = len(self.groups)
        self.claim_holds = i_leftover_071_076_010_079_share_one_backward_5gram(
            self.n_with_backward,
            self.n_distinct,
        )

    def test_tokens_and_sites_are_cycle_145_lock_not_retuned(self):
        """4-gram and leftover sites stay the cycle-145 lock."""
        self.assertEqual(GRAM4, STANDING_BACKWARD_4GRAM_071)
        self.assertEqual(GRAM4, ("071", "076", "010", "079"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(
            STANDING_LEFTOVER_SITES,
            (
                (SIDE_IA, "Ia12", 33),
                (SIDE_IA, "Ia14", 82),
            ),
        )
        self.assertEqual(STANDING_N_LEFTOVER, 2)
        prior_145 = self.survey["i_4gram_071_076_010_079_inside_cycle103"]
        self.assertEqual(prior_145["cycle"], 145)
        self.assertEqual(tuple(prior_145["tokens4"]), GRAM4)
        self.assertEqual(prior_145["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(
            tuple(tuple(row) for row in prior_145["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertFalse(prior_145["i_4gram_071_076_010_079_all_inside_cycle103_5gram"])
        prior_144 = self.survey["i_leftover_076_010_079_backward_4gram"]
        self.assertEqual(prior_144["cycle"], 144)
        self.assertEqual(prior_144["N_distinct_backward_4grams"], 2)
        self.assertFalse(prior_144["i_leftover_076_010_079_share_one_backward_4gram"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_two_leftovers_have_two_distinct_backwards_and_claim_loses(self):
        """N_leftover=2, N_with_backward=2, N_distinct=2. Claim loses."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 2)
        self.assertEqual(self.n_with_backward, STANDING_N_WITH_BACKWARD)
        self.assertEqual(STANDING_N_WITH_BACKWARD, 2)
        self.assertEqual(self.n_no_backward, STANDING_N_NO_BACKWARD)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_BACKWARD_5GRAMS)
        self.assertEqual(STANDING_N_DISTINCT_BACKWARD_5GRAMS, 2)
        self.assertEqual(self.backwards, STANDING_PER_SITE_BACKWARD)
        self.assertEqual(self.with_backward, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.no_backward, STANDING_NO_BACKWARD_SITES)
        self.assertEqual(self.groups, STANDING_SITES_PER_BACKWARD_5GRAM)
        self.assertEqual(
            tuple(gram for gram, _sites in self.groups),
            STANDING_DISTINCT_BACKWARD_5GRAMS,
        )
        expected = (
            (("200", "071", "076", "010", "079"), (SIDE_IA, "Ia12", 33)),
            (("076", "071", "076", "010", "079"), (SIDE_IA, "Ia14", 82)),
        )
        for (back, site), (want_back, want_site) in zip(
            zip(self.backwards, self.leftover_sites, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N4]), GRAM4)
            self.assertGreater(index, 0)
            self.assertEqual(back, want_back)
            self.assertEqual(site, want_site)
            self.assertEqual(site_backward_5gram(stems, index), want_back)
            self.assertEqual(len(back), STANDING_N5)
            self.assertEqual(back[1:], GRAM4)
            self.assertNotEqual(back[0], CYCLE103_PREFIX)
            self.assertNotEqual(back, GRAM5)
            self.assertEqual(side, SIDE_IA)
            self.assertEqual(line, want_site[1])
        self.assertEqual(
            i_leftover_071_076_010_079_share_one_backward_5gram(
                self.n_with_backward,
                self.n_distinct,
            ),
            STANDING_I_LEFTOVER_071_076_010_079_SHARE_ONE_BACKWARD_5GRAM,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_071_076_010_079_SHARE_ONE_BACKWARD_5GRAM,
        )
        self.assertFalse(STANDING_I_LEFTOVER_071_076_010_079_SHARE_ONE_BACKWARD_5GRAM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_071_076_010_079_share_one_backward_5gram",
        )
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_145_144_142_141_140_103_and_w_scoreboards_still_compute(self):
        """Cycle 145 inside, 144 backward-4, 142, 141, 140, 103, W stay."""
        prior_145 = TestMamariI4gram071076010079InsideCycle103Scoreboard()
        prior_145.setUp()
        prior_145.test_five_sites_split_3_2_and_claim_loses()
        prior_145.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-146 leftover backward-5 lock."""
        lock = self.survey["i_leftover_071_076_010_079_backward_5gram"]
        self.assertEqual(lock["cycle"], 146)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_one_backward_5gram"])
        self.assertEqual(
            lock["hypothesis_share_one_backward_5gram"],
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_backward"], STANDING_N_WITH_BACKWARD)
        self.assertEqual(lock["N_with_backward"], 2)
        self.assertEqual(lock["N_no_backward"], STANDING_N_NO_BACKWARD)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_backward_sites"]),
            STANDING_NO_BACKWARD_SITES,
        )
        self.assertEqual(
            lock["N_distinct_backward_5grams"],
            STANDING_N_DISTINCT_BACKWARD_5GRAMS,
        )
        self.assertEqual(lock["N_distinct_backward_5grams"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["distinct_backward_5grams"]),
            STANDING_DISTINCT_BACKWARD_5GRAMS,
        )
        self.assertEqual(
            tuple(
                tuple(row) if row is not None else None
                for row in lock["per_site_backward_5grams"]
            ),
            STANDING_PER_SITE_BACKWARD,
        )
        grouped = tuple(
            (tuple(row["tokens5"]), tuple(tuple(site) for site in row["sites"]))
            for row in lock["sites_per_backward_5gram"]
        )
        self.assertEqual(grouped, STANDING_SITES_PER_BACKWARD_5GRAM)
        self.assertEqual(
            [list(site) for site in STANDING_LEFTOVER_SITES],
            lock["leftover_sites"],
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_071_076_010_079_share_one_backward_5gram"])
        self.assertEqual(
            lock["i_leftover_071_076_010_079_share_one_backward_5gram"],
            STANDING_I_LEFTOVER_071_076_010_079_SHARE_ONE_BACKWARD_5GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_4gram_071_076_010_079_inside_cycle103_unchanged"])
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
        self.assertEqual(
            self.survey["i_4gram_071_076_010_079_inside_cycle103"]["cycle"],
            145,
        )
        self.assertFalse(
            self.survey["i_4gram_071_076_010_079_inside_cycle103"][
                "i_4gram_071_076_010_079_all_inside_cycle103_5gram"
            ]
        )
        self.assertEqual(
            self.survey["i_4gram_071_076_010_079_inside_cycle103"]["N_leftover"],
            2,
        )
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
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftover071076010079Backward5gramImageSnapshot(unittest.TestCase):
    """Cycle 146 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
