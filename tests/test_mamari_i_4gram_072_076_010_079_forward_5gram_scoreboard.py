"""I's cycle-148 minority I-only 4-gram forward 5-gram lock.

Cycle 149 text-search lock. Uses already-vendored A–V and the
cycle-148 I-only 4-gram 072 076 010 079 at Ia5[138] and
Ia13[71]. Does not retune that 4-gram or those sites. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

For each I site, the forward 5-gram 072 076 010 079 X if the
line has a next stem after the 4-gram; end-of-line is
no-forward. Hypothesis: both I sites share one forward
5-gram (one stem X). Measured: N_on_I=2, N_with_forward=2,
N_distinct_forward_5grams=2 (072 076 010 079 090 at
Ia5[138], 072 076 010 079 006 at Ia13[71]). Claim that can
lose: i_4gram_072_076_010_079_share_one_forward_5gram. True
only if N_with_forward=2 and N_distinct_forward_5grams=1.
The claim is false. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_4gram_072_076_010_079_i_only_scoreboard import (
    GRAM4,
    STANDING_I_SITES,
    STANDING_N_ON_I,
    TestMamariI4gram072076010079IOnlyScoreboard,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_010,
)
from tests.test_mamari_i_leftover_076_010_079_backward_4gram_scoreboard import (
    STANDING_BACKWARD_4GRAM_072,
    TestMamariILeftover076010079Backward4gramScoreboard,
)
from tests.test_mamari_i_leftover_076_010_079_forward_4gram_scoreboard import (
    STANDING_FORWARD_4GRAM_090,
    TestMamariILeftover076010079Forward4gramScoreboard,
)
from tests.test_mamari_i_overlap_3gram_076_010_079_i_only_scoreboard import (
    GRAM3,
    TestMamariIOverlap3gram076010079IOnlyScoreboard,
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
STANDING_N4 = 4
STANDING_N5 = 5
STANDING_N_WITH_FORWARD = 2
STANDING_N_DISTINCT_FORWARD_5GRAMS = 2
STANDING_N_NO_FORWARD = 0
STANDING_FORWARD_5GRAM_090 = ("072", "076", "010", "079", "090")
STANDING_FORWARD_5GRAM_006 = ("072", "076", "010", "079", "006")
STANDING_DISTINCT_FORWARD_5GRAMS = (
    STANDING_FORWARD_5GRAM_090,
    STANDING_FORWARD_5GRAM_006,
)
STANDING_PER_SITE_FORWARD = (
    STANDING_FORWARD_5GRAM_090,
    STANDING_FORWARD_5GRAM_006,
)
STANDING_SITES_PER_FORWARD_5GRAM = (
    (STANDING_FORWARD_5GRAM_090, ((SIDE_IA, "Ia5", 138),)),
    (STANDING_FORWARD_5GRAM_006, ((SIDE_IA, "Ia13", 71),)),
)
STANDING_NO_FORWARD_SITES = ()
STANDING_INDEPENDENT_N5_SITE = (SIDE_IA, "Ia13", 72)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_4gram_072_076_010_079_share_one_forward_5gram"
STANDING_I_4GRAM_072_076_010_079_SHARE_ONE_FORWARD_5GRAM = False
STANDING_RESULT = "i_4gram_072_076_010_079_forward_5gram"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_INDEPENDENT_N5 = False


def site_forward_5gram(
    stems: list[str],
    index: int,
    gram4: tuple[str, ...] = GRAM4,
) -> tuple[str, ...] | None:
    """072 076 010 079 X if a next stem exists; None at end-of-line."""
    n4 = len(gram4)
    if tuple(stems[index : index + n4]) != gram4:
        return None
    next_index = index + n4
    if next_index >= len(stems):
        return None
    return tuple(stems[index : index + n4 + 1])


def i_site_forward_5grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    gram4: tuple[str, ...] = GRAM4,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site forward 5-gram or None for the locked I 4-gram sites."""
    return tuple(
        site_forward_5gram(line_stems_for_site(i_sides, site), site[2], gram4)
        for site in sites
    )


def sites_with_forward(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """I sites that have a next stem after the 4-gram."""
    return tuple(
        site
        for site, fwd in zip(sites, forwards, strict=True)
        if fwd is not None
    )


def sites_without_forward(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """I sites that are end-of-line (no-forward)."""
    return tuple(
        site
        for site, fwd in zip(sites, forwards, strict=True)
        if fwd is None
    )


def group_sites_by_forward_5gram(
    sites: tuple[tuple[str, str, int], ...],
    forwards: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[tuple[str, ...], tuple[tuple[str, str, int], ...]], ...]:
    """Distinct forward 5-grams in first-seen order, with their sites."""
    groups: list[tuple[tuple[str, ...], list[tuple[str, str, int]]]] = []
    index_by_gram: dict[tuple[str, ...], int] = {}
    for site, fwd in zip(sites, forwards, strict=True):
        if fwd is None:
            continue
        if fwd not in index_by_gram:
            index_by_gram[fwd] = len(groups)
            groups.append((fwd, [site]))
        else:
            groups[index_by_gram[fwd]][1].append(site)
    return tuple((gram, tuple(gram_sites)) for gram, gram_sites in groups)


def i_4gram_072_076_010_079_share_one_forward_5gram(
    n_with_forward: int,
    n_distinct_forward_5grams: int,
) -> bool:
    """True iff N_with_forward=2 and N_distinct_forward_5grams=1."""
    return n_with_forward == 2 and n_distinct_forward_5grams == 1


class TestI4gram072076010079Forward5gramHelpers(unittest.TestCase):
    """Helpers on cycle-148 I 4-gram sites. No CV, no LLM."""

    def test_forward_requires_next_stem_after_4gram(self):
        """A next stem is a 5-gram; end-of-line is no-forward."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("072", "076", "010", "079"))
        self.assertEqual(GRAM4, STANDING_BACKWARD_4GRAM_072)
        self.assertEqual(len(GRAM4), STANDING_N4)
        self.assertEqual(STANDING_N5, STANDING_N4 + 1)
        has_next = ["999", "072", "076", "010", "079", "090", "076"]
        self.assertEqual(
            site_forward_5gram(has_next, 1),
            ("072", "076", "010", "079", "090"),
        )
        end_of_line = ["999", "072", "076", "010", "079"]
        self.assertIsNone(site_forward_5gram(end_of_line, 1))
        self.assertIsNone(site_forward_5gram(["072", "076", "010", "079"], 0))
        mismatch = ["072", "076", "010", "006", "090"]
        self.assertIsNone(site_forward_5gram(mismatch, 0))
        gapped = ["072", "076", "011", "079", "090"]
        self.assertIsNone(site_forward_5gram(gapped, 0))
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_two_forwards_and_one_distinct(self):
        """Boolean is True only when N_with_forward=2 and N_distinct=1."""
        provider = MockProvider()
        self.assertTrue(i_4gram_072_076_010_079_share_one_forward_5gram(2, 1))
        self.assertFalse(i_4gram_072_076_010_079_share_one_forward_5gram(2, 2))
        self.assertFalse(i_4gram_072_076_010_079_share_one_forward_5gram(1, 1))
        self.assertFalse(i_4gram_072_076_010_079_share_one_forward_5gram(0, 0))
        self.assertFalse(i_4gram_072_076_010_079_share_one_forward_5gram(2, 0))
        self.assertEqual(STANDING_CLAIM, "i_4gram_072_076_010_079_share_one_forward_5gram")
        self.assertFalse(STANDING_I_4GRAM_072_076_010_079_SHARE_ONE_FORWARD_5GRAM)
        self.assertNotEqual(
            STANDING_I_4GRAM_072_076_010_079_SHARE_ONE_FORWARD_5GRAM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_grouping_keeps_first_seen_order_and_skips_none(self):
        """Sites group by forward 5-gram; no-forward sites are omitted."""
        provider = MockProvider()
        sites = (
            (SIDE_IA, "Ia5", 138),
            (SIDE_IA, "Ia13", 71),
        )
        two_distinct = (
            STANDING_FORWARD_5GRAM_090,
            STANDING_FORWARD_5GRAM_006,
        )
        self.assertEqual(
            group_sites_by_forward_5gram(sites, two_distinct),
            STANDING_SITES_PER_FORWARD_5GRAM,
        )
        shared = (
            STANDING_FORWARD_5GRAM_090,
            STANDING_FORWARD_5GRAM_090,
        )
        self.assertEqual(
            group_sites_by_forward_5gram(sites, shared),
            ((STANDING_FORWARD_5GRAM_090, sites),),
        )
        one_none = (STANDING_FORWARD_5GRAM_090, None)
        self.assertEqual(
            group_sites_by_forward_5gram(sites, one_none),
            ((STANDING_FORWARD_5GRAM_090, (sites[0],)),),
        )
        self.assertEqual(sites_with_forward(sites, one_none), (sites[0],))
        self.assertEqual(sites_without_forward(sites, one_none), (sites[1],))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI4gram072076010079Forward5gramScoreboard(unittest.TestCase):
    """Cited-fixture minority 4-gram forward-5 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = STANDING_I_SITES
        self.forwards = i_site_forward_5grams(self.i_sides, self.i_sites)
        self.with_forward = sites_with_forward(self.i_sites, self.forwards)
        self.no_forward = sites_without_forward(self.i_sites, self.forwards)
        self.groups = group_sites_by_forward_5gram(self.i_sites, self.forwards)
        self.n_on_i = len(self.i_sites)
        self.n_with_forward = len(self.with_forward)
        self.n_no_forward = len(self.no_forward)
        self.n_distinct = len(self.groups)
        self.claim_holds = i_4gram_072_076_010_079_share_one_forward_5gram(
            self.n_with_forward,
            self.n_distinct,
        )

    def test_tokens_and_sites_are_cycle_148_lock_not_retuned(self):
        """4-gram and I sites stay the cycle-148 I-only lock."""
        self.assertEqual(GRAM4, STANDING_BACKWARD_4GRAM_072)
        self.assertEqual(GRAM4, ("072", "076", "010", "079"))
        self.assertEqual(GRAM3, ("076", "010", "079"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_010, ("076", "010", "079", "006", "700"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia5", 138),
                (SIDE_IA, "Ia13", 71),
            ),
        )
        self.assertEqual(STANDING_N_ON_I, 2)
        prior_148 = self.survey["i_4gram_072_076_010_079_i_only"]
        self.assertEqual(prior_148["cycle"], 148)
        self.assertEqual(tuple(prior_148["tokens4"]), GRAM4)
        self.assertEqual(prior_148["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(
            tuple(tuple(row) for row in prior_148["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertTrue(prior_148["i_4gram_072_076_010_079_is_i_only"])
        prior_143 = self.survey["i_leftover_076_010_079_forward_4gram"]
        self.assertEqual(prior_143["cycle"], 143)
        self.assertEqual(tuple(prior_143["distinct_forward_4grams"][0]), STANDING_FORWARD_4GRAM_090)
        prior_139 = self.survey["i_independent_n5_maximals_076"]
        self.assertEqual(prior_139["cycle"], 139)
        self.assertTrue(prior_139["i_independent_n5_maximals_all_contain_076"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_two_i_sites_have_two_distinct_forwards_and_claim_loses(self):
        """N_on_I=2, N_with_forward=2, N_distinct=2. Claim loses."""
        self.assertEqual(self.n_on_i, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, 2)
        self.assertEqual(self.n_with_forward, STANDING_N_WITH_FORWARD)
        self.assertEqual(STANDING_N_WITH_FORWARD, 2)
        self.assertEqual(self.n_no_forward, STANDING_N_NO_FORWARD)
        self.assertEqual(STANDING_N_NO_FORWARD, 0)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_FORWARD_5GRAMS)
        self.assertEqual(STANDING_N_DISTINCT_FORWARD_5GRAMS, 2)
        self.assertEqual(self.forwards, STANDING_PER_SITE_FORWARD)
        self.assertEqual(self.with_forward, STANDING_I_SITES)
        self.assertEqual(self.no_forward, STANDING_NO_FORWARD_SITES)
        self.assertEqual(self.groups, STANDING_SITES_PER_FORWARD_5GRAM)
        self.assertEqual(
            tuple(gram for gram, _sites in self.groups),
            STANDING_DISTINCT_FORWARD_5GRAMS,
        )
        expected = (
            (("072", "076", "010", "079", "090"), (SIDE_IA, "Ia5", 138)),
            (("072", "076", "010", "079", "006"), (SIDE_IA, "Ia13", 71)),
        )
        for (fwd, site), (want_fwd, want_site) in zip(
            zip(self.forwards, self.i_sites, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N4]), GRAM4)
            self.assertLess(index + STANDING_N4, len(stems))
            self.assertEqual(fwd, want_fwd)
            self.assertEqual(site, want_site)
            self.assertEqual(site_forward_5gram(stems, index), want_fwd)
            self.assertEqual(len(fwd), STANDING_N5)
            self.assertEqual(fwd[:STANDING_N4], GRAM4)
            self.assertEqual(fwd[1:4], GRAM3)
            self.assertNotEqual(fwd, GRAM5)
            self.assertNotEqual(fwd, MAXIMAL_N5_010)
            self.assertEqual(side, SIDE_IA)
            self.assertEqual(line, want_site[1])
        ia13_stems = line_stems_for_site(self.i_sides, STANDING_I_SITES[1])
        ia13_index = STANDING_I_SITES[1][2]
        self.assertEqual(STANDING_I_SITES[1][2] + 1, STANDING_INDEPENDENT_N5_SITE[2])
        self.assertEqual(
            tuple(ia13_stems[ia13_index + 1 : ia13_index + 6]),
            MAXIMAL_N5_010,
        )
        ia5_stems = line_stems_for_site(self.i_sides, STANDING_I_SITES[0])
        ia5_index = STANDING_I_SITES[0][2]
        self.assertEqual(
            tuple(ia5_stems[ia5_index + 1 : ia5_index + 5]),
            STANDING_FORWARD_4GRAM_090,
        )
        self.assertEqual(
            i_4gram_072_076_010_079_share_one_forward_5gram(
                self.n_with_forward,
                self.n_distinct,
            ),
            STANDING_I_4GRAM_072_076_010_079_SHARE_ONE_FORWARD_5GRAM,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_4GRAM_072_076_010_079_SHARE_ONE_FORWARD_5GRAM,
        )
        self.assertFalse(STANDING_I_4GRAM_072_076_010_079_SHARE_ONE_FORWARD_5GRAM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(STANDING_CLAIM, "i_4gram_072_076_010_079_share_one_forward_5gram")
        self.assertFalse(STANDING_SAME_AS_INDEPENDENT_N5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_148_144_143_141_103_and_w_scoreboards_still_compute(self):
        """Cycle 148 I-only, 144 backward-4, 143 forward-4, 141, 103, W stay."""
        prior_148 = TestMamariI4gram072076010079IOnlyScoreboard()
        prior_148.setUp()
        prior_148.test_i_hits_are_two_on_ia_including_leftover_start()
        prior_148.test_4gram_is_zero_off_i_and_i_only()
        prior_148.test_survey_matches_computed_lock()
        prior_144 = TestMamariILeftover076010079Backward4gramScoreboard()
        prior_144.setUp()
        prior_144.test_three_leftovers_have_two_distinct_backwards_and_claim_loses()
        prior_144.test_survey_matches_computed_lock()
        prior_143 = TestMamariILeftover076010079Forward4gramScoreboard()
        prior_143.setUp()
        prior_143.test_three_leftovers_have_three_distinct_forwards_and_claim_loses()
        prior_143.test_survey_matches_computed_lock()
        prior_141 = TestMamariIOverlap3gram076010079IOnlyScoreboard()
        prior_141.setUp()
        prior_141.test_i_hits_are_eight_on_ia()
        prior_141.test_3gram_is_zero_off_i_and_i_only()
        prior_141.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-149 minority 4-gram forward-5 lock."""
        lock = self.survey["i_4gram_072_076_010_079_forward_5gram"]
        self.assertEqual(lock["cycle"], 149)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_one_forward_5gram"])
        self.assertEqual(
            lock["hypothesis_share_one_forward_5gram"],
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_on_I"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_with_forward"], STANDING_N_WITH_FORWARD)
        self.assertEqual(lock["N_with_forward"], 2)
        self.assertEqual(lock["N_no_forward"], STANDING_N_NO_FORWARD)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_forward_sites"]),
            STANDING_NO_FORWARD_SITES,
        )
        self.assertEqual(
            lock["N_distinct_forward_5grams"],
            STANDING_N_DISTINCT_FORWARD_5GRAMS,
        )
        self.assertEqual(lock["N_distinct_forward_5grams"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["distinct_forward_5grams"]),
            STANDING_DISTINCT_FORWARD_5GRAMS,
        )
        self.assertEqual(
            tuple(
                tuple(row) if row is not None else None
                for row in lock["per_site_forward_5grams"]
            ),
            STANDING_PER_SITE_FORWARD,
        )
        grouped = tuple(
            (tuple(row["tokens5"]), tuple(tuple(site) for site in row["sites"]))
            for row in lock["sites_per_forward_5gram"]
        )
        self.assertEqual(grouped, STANDING_SITES_PER_FORWARD_5GRAM)
        self.assertEqual(
            [list(site) for site in STANDING_I_SITES],
            lock["i_sites"],
        )
        self.assertEqual(
            tuple(lock["independent_n5_site_after_ia13"]),
            STANDING_INDEPENDENT_N5_SITE,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_4gram_072_076_010_079_share_one_forward_5gram"])
        self.assertEqual(
            lock["i_4gram_072_076_010_079_share_one_forward_5gram"],
            STANDING_I_4GRAM_072_076_010_079_SHARE_ONE_FORWARD_5GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_independent_n5"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_4gram_072_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_backward_5grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_071_076_010_079_backward_5gram_unchanged"])
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
        self.assertEqual(self.survey["i_4gram_072_076_010_079_i_only"]["cycle"], 148)
        self.assertTrue(
            self.survey["i_4gram_072_076_010_079_i_only"][
                "i_4gram_072_076_010_079_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_4gram_072_076_010_079_i_only"]["N_on_I"], 2)
        self.assertEqual(
            tuple(
                tuple(row)
                for row in self.survey["i_4gram_072_076_010_079_i_only"]["i_sites"]
            ),
            STANDING_I_SITES,
        )
        self.assertEqual(self.survey["i_leftover_backward_5grams_i_only"]["cycle"], 147)
        self.assertTrue(
            self.survey["i_leftover_backward_5grams_i_only"][
                "i_leftover_backward_5grams_both_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_071_076_010_079_backward_5gram"]["cycle"],
            146,
        )
        self.assertEqual(
            self.survey["i_4gram_071_076_010_079_inside_cycle103"]["cycle"],
            145,
        )
        self.assertFalse(
            self.survey["i_4gram_071_076_010_079_inside_cycle103"][
                "i_4gram_071_076_010_079_all_inside_cycle103_5gram"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_010_079_backward_4gram"]["cycle"], 144)
        self.assertFalse(
            self.survey["i_leftover_076_010_079_backward_4gram"][
                "i_leftover_076_010_079_share_one_backward_4gram"
            ]
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
        self.assertFalse(
            self.survey["i_independent_nge4_maximals"]["i_independent_nge4_has_exactly_4_maximals"]
        )
        self.assertEqual(self.survey["i_repeating_nge4"]["cycle"], 135)
        self.assertFalse(
            self.survey["i_repeating_nge4"]["i_repeating_nge4_all_substrings_of_i_5gram"]
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
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI4gram072076010079Forward5gramImageSnapshot(unittest.TestCase):
    """Cycle 149 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
