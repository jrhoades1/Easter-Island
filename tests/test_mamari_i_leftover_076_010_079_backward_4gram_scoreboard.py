"""I's cycle-142 leftover overlap 3-gram backward 4-gram lock.

Cycle 144 text-search lock. Uses already-vendored A–V and the
cycle-142 leftover sites of overlap 3-gram 076 010 079
(Ia5[139], Ia12[34], Ia14[83]). Does not retune that 3-gram
or those sites. Does not vendor a new tablet. Does not scrape
X. W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each leftover site, the backward 4-gram Y 076 010 079 if
the line has a previous stem before the 3-gram; start-of-line
is no-backward. Hypothesis: all three leftover sites share
one backward 4-gram (one stem Y). Measured: N_leftover=3,
N_with_backward=3, N_distinct_backward_4grams=2
(072 076 010 079 at Ia5[139], 071 076 010 079 at Ia12[34]
and Ia14[83]). Claim that can lose:
i_leftover_076_010_079_share_one_backward_4gram. True only
if N_with_backward=3 and N_distinct_backward_4grams=1. The
claim is false. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_independent_n5_cycle103_n3_overlap_scoreboard import (
    STANDING_SHARED_N3,
    TestMamariIIndependentN5Cycle103N3OverlapScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
)
from tests.test_mamari_i_leftover_076_010_079_forward_4gram_scoreboard import (
    TestMamariILeftover076010079Forward4gramScoreboard,
)
from tests.test_mamari_i_overlap_3gram_076_010_079_i_only_scoreboard import (
    GRAM3,
    TestMamariIOverlap3gram076010079IOnlyScoreboard,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    STANDING_LEFTOVER_SITES,
    STANDING_N_LEFTOVER,
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
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_WITH_BACKWARD = 3
STANDING_N_DISTINCT_BACKWARD_4GRAMS = 2
STANDING_N_NO_BACKWARD = 0
STANDING_BACKWARD_4GRAM_072 = ("072", "076", "010", "079")
STANDING_BACKWARD_4GRAM_071 = ("071", "076", "010", "079")
STANDING_DISTINCT_BACKWARD_4GRAMS = (
    STANDING_BACKWARD_4GRAM_072,
    STANDING_BACKWARD_4GRAM_071,
)
STANDING_PER_SITE_BACKWARD = (
    STANDING_BACKWARD_4GRAM_072,
    STANDING_BACKWARD_4GRAM_071,
    STANDING_BACKWARD_4GRAM_071,
)
STANDING_SITES_PER_BACKWARD_4GRAM = (
    (STANDING_BACKWARD_4GRAM_072, ((SIDE_IA, "Ia5", 139),)),
    (
        STANDING_BACKWARD_4GRAM_071,
        ((SIDE_IA, "Ia12", 34), (SIDE_IA, "Ia14", 83)),
    ),
)
STANDING_NO_BACKWARD_SITES = ()
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_010_079_share_one_backward_4gram"
STANDING_I_LEFTOVER_076_010_079_SHARE_ONE_BACKWARD_4GRAM = False
STANDING_RESULT = "i_leftover_076_010_079_backward_4gram"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_INDEPENDENT_PREFIX4 = False


def site_backward_4gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """Y 076 010 079 if a previous stem exists; None at start-of-line."""
    n3 = len(gram3)
    if tuple(stems[index : index + n3]) != gram3:
        return None
    if index == 0:
        return None
    return tuple(stems[index - 1 : index + n3])


def leftover_backward_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site backward 4-gram or None for the locked leftover sites."""
    return tuple(
        site_backward_4gram(line_stems_for_site(i_sides, site), site[2], gram3)
        for site in sites
    )


def sites_with_backward(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that have a previous stem before the 3-gram."""
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


def group_sites_by_backward_4gram(
    sites: tuple[tuple[str, str, int], ...],
    backwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[tuple[str, ...], tuple[tuple[str, str, int], ...]], ...]:
    """Distinct backward 4-grams in first-seen order, with their sites."""
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


def i_leftover_076_010_079_share_one_backward_4gram(
    n_with_backward: int,
    n_distinct_backward_4grams: int,
) -> bool:
    """True iff N_with_backward=3 and N_distinct_backward_4grams=1."""
    return n_with_backward == 3 and n_distinct_backward_4grams == 1


class TestILeftover076010079Backward4gramHelpers(unittest.TestCase):
    """Helpers on cycle-142 leftover sites. No CV, no LLM."""

    def test_backward_requires_previous_stem_before_3gram(self):
        """A previous stem is a 4-gram; start-of-line is no-backward."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "010", "079"))
        self.assertEqual(GRAM3, STANDING_SHARED_N3)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        has_prev = ["200", "072", "076", "010", "079", "090"]
        self.assertEqual(site_backward_4gram(has_prev, 2), ("072", "076", "010", "079"))
        start_of_line = ["076", "010", "079", "090"]
        self.assertIsNone(site_backward_4gram(start_of_line, 0))
        self.assertIsNone(site_backward_4gram(["076", "010", "079"], 0))
        mismatch = ["072", "076", "010", "006"]
        self.assertIsNone(site_backward_4gram(mismatch, 1))
        gapped = ["072", "076", "011", "079"]
        self.assertIsNone(site_backward_4gram(gapped, 1))
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_three_backwards_and_one_distinct(self):
        """Boolean is True only when N_with_backward=3 and N_distinct=1."""
        provider = MockProvider()
        self.assertTrue(i_leftover_076_010_079_share_one_backward_4gram(3, 1))
        self.assertFalse(i_leftover_076_010_079_share_one_backward_4gram(3, 2))
        self.assertFalse(i_leftover_076_010_079_share_one_backward_4gram(3, 3))
        self.assertFalse(i_leftover_076_010_079_share_one_backward_4gram(2, 1))
        self.assertFalse(i_leftover_076_010_079_share_one_backward_4gram(0, 0))
        self.assertFalse(i_leftover_076_010_079_share_one_backward_4gram(1, 1))
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_010_079_share_one_backward_4gram")
        self.assertFalse(STANDING_I_LEFTOVER_076_010_079_SHARE_ONE_BACKWARD_4GRAM)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_076_010_079_SHARE_ONE_BACKWARD_4GRAM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_grouping_keeps_first_seen_order_and_skips_none(self):
        """Sites group by backward 4-gram; no-backward sites are omitted."""
        provider = MockProvider()
        sites = (
            (SIDE_IA, "Ia5", 139),
            (SIDE_IA, "Ia12", 34),
            (SIDE_IA, "Ia14", 83),
        )
        two_distinct = (
            STANDING_BACKWARD_4GRAM_072,
            STANDING_BACKWARD_4GRAM_071,
            STANDING_BACKWARD_4GRAM_071,
        )
        self.assertEqual(
            group_sites_by_backward_4gram(sites, two_distinct),
            STANDING_SITES_PER_BACKWARD_4GRAM,
        )
        shared = (
            STANDING_BACKWARD_4GRAM_071,
            STANDING_BACKWARD_4GRAM_071,
            STANDING_BACKWARD_4GRAM_071,
        )
        self.assertEqual(
            group_sites_by_backward_4gram(sites, shared),
            ((STANDING_BACKWARD_4GRAM_071, sites),),
        )
        one_none = (STANDING_BACKWARD_4GRAM_072, None, STANDING_BACKWARD_4GRAM_072)
        self.assertEqual(
            group_sites_by_backward_4gram(sites, one_none),
            (
                (
                    STANDING_BACKWARD_4GRAM_072,
                    ((SIDE_IA, "Ia5", 139), (SIDE_IA, "Ia14", 83)),
                ),
            ),
        )
        self.assertEqual(sites_with_backward(sites, one_none), (sites[0], sites[2]))
        self.assertEqual(sites_without_backward(sites, one_none), (sites[1],))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076010079Backward4gramScoreboard(unittest.TestCase):
    """Cited-fixture leftover overlap 3-gram backward-4 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.backwards = leftover_backward_4grams(self.i_sides, self.leftover_sites)
        self.with_backward = sites_with_backward(self.leftover_sites, self.backwards)
        self.no_backward = sites_without_backward(self.leftover_sites, self.backwards)
        self.groups = group_sites_by_backward_4gram(self.leftover_sites, self.backwards)
        self.n_leftover = len(self.leftover_sites)
        self.n_with_backward = len(self.with_backward)
        self.n_no_backward = len(self.no_backward)
        self.n_distinct = len(self.groups)
        self.claim_holds = i_leftover_076_010_079_share_one_backward_4gram(
            self.n_with_backward,
            self.n_distinct,
        )

    def test_tokens_and_sites_are_cycle_142_lock_not_retuned(self):
        """3-gram and leftover sites stay the cycle-142 lock."""
        self.assertEqual(GRAM3, STANDING_SHARED_N3)
        self.assertEqual(GRAM3, ("076", "010", "079"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(
            STANDING_LEFTOVER_SITES,
            (
                (SIDE_IA, "Ia5", 139),
                (SIDE_IA, "Ia12", 34),
                (SIDE_IA, "Ia14", 83),
            ),
        )
        prior_143 = self.survey["i_leftover_076_010_079_forward_4gram"]
        self.assertEqual(prior_143["cycle"], 143)
        self.assertEqual(tuple(prior_143["tokens3"]), GRAM3)
        self.assertEqual(prior_143["N_leftover"], STANDING_N_LEFTOVER)
        self.assertFalse(prior_143["i_leftover_076_010_079_share_one_forward_4gram"])
        prior_142 = self.survey["i_overlap_3gram_inside_two_5grams"]
        self.assertEqual(prior_142["cycle"], 142)
        self.assertEqual(tuple(prior_142["tokens3"]), GRAM3)
        self.assertEqual(prior_142["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_142["N_leftover"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in prior_142["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertFalse(prior_142["i_overlap_3gram_076_010_079_all_inside_two_5grams"])
        prior_141 = self.survey["i_overlap_3gram_076_010_079_i_only"]
        self.assertEqual(prior_141["cycle"], 141)
        self.assertEqual(prior_141["N_on_I"], 8)
        self.assertTrue(prior_141["i_overlap_3gram_076_010_079_is_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_three_leftovers_have_two_distinct_backwards_and_claim_loses(self):
        """N_leftover=3, N_with_backward=3, N_distinct=2. Claim loses."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 3)
        self.assertEqual(self.n_with_backward, STANDING_N_WITH_BACKWARD)
        self.assertEqual(STANDING_N_WITH_BACKWARD, 3)
        self.assertEqual(self.n_no_backward, STANDING_N_NO_BACKWARD)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_BACKWARD_4GRAMS)
        self.assertEqual(STANDING_N_DISTINCT_BACKWARD_4GRAMS, 2)
        self.assertEqual(self.backwards, STANDING_PER_SITE_BACKWARD)
        self.assertEqual(self.with_backward, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.no_backward, STANDING_NO_BACKWARD_SITES)
        self.assertEqual(self.groups, STANDING_SITES_PER_BACKWARD_4GRAM)
        self.assertEqual(
            tuple(gram for gram, _sites in self.groups),
            STANDING_DISTINCT_BACKWARD_4GRAMS,
        )
        expected = (
            (("072", "076", "010", "079"), (SIDE_IA, "Ia5", 139)),
            (("071", "076", "010", "079"), (SIDE_IA, "Ia12", 34)),
            (("071", "076", "010", "079"), (SIDE_IA, "Ia14", 83)),
        )
        for (back, site), (want_back, want_site) in zip(
            zip(self.backwards, self.leftover_sites, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertGreater(index, 0)
            self.assertEqual(back, want_back)
            self.assertEqual(site, want_site)
            self.assertEqual(site_backward_4gram(stems, index), want_back)
            self.assertEqual(len(back), STANDING_N4)
            self.assertEqual(back[1:], GRAM3)
            self.assertEqual(side, SIDE_IA)
            self.assertEqual(line, want_site[1])
        self.assertEqual(
            i_leftover_076_010_079_share_one_backward_4gram(
                self.n_with_backward,
                self.n_distinct,
            ),
            STANDING_I_LEFTOVER_076_010_079_SHARE_ONE_BACKWARD_4GRAM,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_010_079_SHARE_ONE_BACKWARD_4GRAM,
        )
        self.assertFalse(STANDING_I_LEFTOVER_076_010_079_SHARE_ONE_BACKWARD_4GRAM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_010_079_share_one_backward_4gram")
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_PREFIX4)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_143_142_141_140_103_and_w_scoreboards_still_compute(self):
        """Cycle 143 forward, 142 inside, 141 I-only, 140 overlap, 103, W stay."""
        prior_143 = TestMamariILeftover076010079Forward4gramScoreboard()
        prior_143.setUp()
        prior_143.test_three_leftovers_have_three_distinct_forwards_and_claim_loses()
        prior_143.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-144 leftover backward-4 lock."""
        lock = self.survey["i_leftover_076_010_079_backward_4gram"]
        self.assertEqual(lock["cycle"], 144)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_one_backward_4gram"])
        self.assertEqual(
            lock["hypothesis_share_one_backward_4gram"],
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_backward"], STANDING_N_WITH_BACKWARD)
        self.assertEqual(lock["N_with_backward"], 3)
        self.assertEqual(lock["N_no_backward"], STANDING_N_NO_BACKWARD)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_backward_sites"]),
            STANDING_NO_BACKWARD_SITES,
        )
        self.assertEqual(
            lock["N_distinct_backward_4grams"],
            STANDING_N_DISTINCT_BACKWARD_4GRAMS,
        )
        self.assertEqual(lock["N_distinct_backward_4grams"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["distinct_backward_4grams"]),
            STANDING_DISTINCT_BACKWARD_4GRAMS,
        )
        self.assertEqual(
            tuple(
                tuple(row) if row is not None else None
                for row in lock["per_site_backward_4grams"]
            ),
            STANDING_PER_SITE_BACKWARD,
        )
        grouped = tuple(
            (tuple(row["tokens4"]), tuple(tuple(site) for site in row["sites"]))
            for row in lock["sites_per_backward_4gram"]
        )
        self.assertEqual(grouped, STANDING_SITES_PER_BACKWARD_4GRAM)
        self.assertEqual(
            [list(site) for site in STANDING_LEFTOVER_SITES],
            lock["leftover_sites"],
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_076_010_079_share_one_backward_4gram"])
        self.assertEqual(
            lock["i_leftover_076_010_079_share_one_backward_4gram"],
            STANDING_I_LEFTOVER_076_010_079_SHARE_ONE_BACKWARD_4GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_independent_prefix4"])
        self.assertTrue(lock["raw_stems_999_kept"])
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
        self.assertEqual(self.survey["i_leftover_076_010_079_forward_4gram"]["cycle"], 143)
        self.assertFalse(
            self.survey["i_leftover_076_010_079_forward_4gram"][
                "i_leftover_076_010_079_share_one_forward_4gram"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_010_079_forward_4gram"][
                "N_distinct_forward_4grams"
            ],
            3,
        )
        self.assertEqual(self.survey["i_overlap_3gram_inside_two_5grams"]["cycle"], 142)
        self.assertFalse(
            self.survey["i_overlap_3gram_inside_two_5grams"][
                "i_overlap_3gram_076_010_079_all_inside_two_5grams"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_inside_two_5grams"]["N_leftover"], 3)
        self.assertEqual(
            tuple(
                tuple(row)
                for row in self.survey["i_overlap_3gram_inside_two_5grams"]["leftover_sites"]
            ),
            STANDING_LEFTOVER_SITES,
        )
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
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftover076010079Backward4gramImageSnapshot(unittest.TestCase):
    """Cycle 144 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
