"""I's cycle-161 leftover overlap 3-gram backward 4-gram lock.

Cycle 163 text-search lock. Uses already-vendored A–V and the
cycle-161 leftover sites of overlap 3-gram 076 020 010
(Ia4[158], Ia5[56], Ia6[102], Ia13[48]). Does not retune that
3-gram or those sites. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished Ib
is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each leftover site, the backward 4-gram Y 076 020 010 if
the line has a previous stem before the 3-gram; start-of-line
is no-backward. Hypothesis: all four leftover sites share one
backward 4-gram (one stem Y). Measured: N_leftover=4,
N_with_backward=4, N_distinct_backward_4grams=4
(633 076 020 010 at Ia4[158], 208 076 020 010 at Ia5[56],
005 076 020 010 at Ia6[102], 536 076 020 010 at Ia13[48]).
Claim that can lose:
i_leftover_076_020_010_share_one_backward_4gram. True only
if N_with_backward=4 and N_distinct_backward_4grams=1. The
claim is false. Same claim-shape as cycle 144 (076 010 079
share-one-backward-4gram lost, N_distinct=2). Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_independent_400_070_076_020_010_previous_stem_scoreboard import (
    LEFTOVER_N4_053,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_400,
)
from tests.test_mamari_i_leftover_076_010_079_backward_4gram_scoreboard import (
    STANDING_N_DISTINCT_BACKWARD_4GRAMS as CYCLE144_N_DISTINCT,
    TestMamariILeftover076010079Backward4gramScoreboard,
    group_sites_by_backward_4gram,
    leftover_backward_4grams,
    site_backward_4gram,
    sites_with_backward,
    sites_without_backward,
)
from tests.test_mamari_i_leftover_076_020_010_forward_4gram_scoreboard import (
    TestMamariILeftover076020010Forward4gramScoreboard,
)
from tests.test_mamari_i_overlap_3gram_076_020_010_i_only_scoreboard import (
    GRAM3,
    TestMamariIOverlap3gram076020010IOnlyScoreboard,
)
from tests.test_mamari_i_overlap_3gram_076_020_010_inside_family_scoreboard import (
    LEFTOVER_N4_050,
    LEFTOVER_N4_090,
    STANDING_LEFTOVER_SITES,
    STANDING_N_LEFTOVER,
    TestMamariIOverlap3gram076020010InsideFamilyScoreboard,
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
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_WITH_BACKWARD = 4
STANDING_N_DISTINCT_BACKWARD_4GRAMS = 4
STANDING_N_NO_BACKWARD = 0
STANDING_BACKWARD_4GRAM_633 = ("633", "076", "020", "010")
STANDING_BACKWARD_4GRAM_208 = ("208", "076", "020", "010")
STANDING_BACKWARD_4GRAM_005 = ("005", "076", "020", "010")
STANDING_BACKWARD_4GRAM_536 = ("536", "076", "020", "010")
STANDING_DISTINCT_BACKWARD_4GRAMS = (
    STANDING_BACKWARD_4GRAM_633,
    STANDING_BACKWARD_4GRAM_208,
    STANDING_BACKWARD_4GRAM_005,
    STANDING_BACKWARD_4GRAM_536,
)
STANDING_PER_SITE_BACKWARD = (
    STANDING_BACKWARD_4GRAM_633,
    STANDING_BACKWARD_4GRAM_208,
    STANDING_BACKWARD_4GRAM_005,
    STANDING_BACKWARD_4GRAM_536,
)
STANDING_SITES_PER_BACKWARD_4GRAM = (
    (STANDING_BACKWARD_4GRAM_633, ((SIDE_IA, "Ia4", 158),)),
    (STANDING_BACKWARD_4GRAM_208, ((SIDE_IA, "Ia5", 56),)),
    (STANDING_BACKWARD_4GRAM_005, ((SIDE_IA, "Ia6", 102),)),
    (STANDING_BACKWARD_4GRAM_536, ((SIDE_IA, "Ia13", 48),)),
)
STANDING_NO_BACKWARD_SITES = ()
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_020_010_share_one_backward_4gram"
STANDING_I_LEFTOVER_076_020_010_SHARE_ONE_BACKWARD_4GRAM = False
STANDING_RESULT = "i_leftover_076_020_010_backward_4gram"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE144 = False
STANDING_SAME_AS_FAMILY_090 = False


def i_leftover_076_020_010_share_one_backward_4gram(
    n_with_backward: int,
    n_distinct_backward_4grams: int,
) -> bool:
    """True iff N_with_backward=4 and N_distinct_backward_4grams=1."""
    return n_with_backward == 4 and n_distinct_backward_4grams == 1


class TestILeftover076020010Backward4gramHelpers(unittest.TestCase):
    """Helpers on cycle-161 leftover sites. No CV, no LLM."""

    def test_backward_requires_previous_stem_before_3gram(self):
        """A previous stem is a 4-gram; start-of-line is no-backward."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "020", "010"))
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        has_prev = ["200", "633", "076", "020", "010", "150"]
        self.assertEqual(
            site_backward_4gram(has_prev, 2, GRAM3),
            ("633", "076", "020", "010"),
        )
        start_of_line = ["076", "020", "010", "150"]
        self.assertIsNone(site_backward_4gram(start_of_line, 0, GRAM3))
        self.assertIsNone(site_backward_4gram(["076", "020", "010"], 0, GRAM3))
        mismatch = ["633", "076", "020", "006"]
        self.assertIsNone(site_backward_4gram(mismatch, 1, GRAM3))
        gapped = ["633", "076", "021", "010"]
        self.assertIsNone(site_backward_4gram(gapped, 1, GRAM3))
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_four_backwards_and_one_distinct(self):
        """Boolean is True only when N_with_backward=4 and N_distinct=1."""
        provider = MockProvider()
        self.assertTrue(i_leftover_076_020_010_share_one_backward_4gram(4, 1))
        self.assertFalse(i_leftover_076_020_010_share_one_backward_4gram(4, 4))
        self.assertFalse(i_leftover_076_020_010_share_one_backward_4gram(4, 3))
        self.assertFalse(i_leftover_076_020_010_share_one_backward_4gram(4, 2))
        self.assertFalse(i_leftover_076_020_010_share_one_backward_4gram(3, 1))
        self.assertFalse(i_leftover_076_020_010_share_one_backward_4gram(0, 0))
        self.assertFalse(i_leftover_076_020_010_share_one_backward_4gram(1, 1))
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_020_010_share_one_backward_4gram")
        self.assertFalse(STANDING_I_LEFTOVER_076_020_010_SHARE_ONE_BACKWARD_4GRAM)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_076_020_010_SHARE_ONE_BACKWARD_4GRAM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(CYCLE144_N_DISTINCT, 2)
        self.assertFalse(STANDING_SAME_AS_CYCLE144)
        self.assertEqual(provider.get_call_history(), [])

    def test_grouping_keeps_first_seen_order_and_skips_none(self):
        """Sites group by backward 4-gram; no-backward sites are omitted."""
        provider = MockProvider()
        sites = STANDING_LEFTOVER_SITES
        four_distinct = STANDING_PER_SITE_BACKWARD
        self.assertEqual(
            group_sites_by_backward_4gram(sites, four_distinct),
            STANDING_SITES_PER_BACKWARD_4GRAM,
        )
        shared = (
            STANDING_BACKWARD_4GRAM_633,
            STANDING_BACKWARD_4GRAM_633,
            STANDING_BACKWARD_4GRAM_633,
            STANDING_BACKWARD_4GRAM_633,
        )
        self.assertEqual(
            group_sites_by_backward_4gram(sites, shared),
            ((STANDING_BACKWARD_4GRAM_633, sites),),
        )
        one_none = (
            STANDING_BACKWARD_4GRAM_633,
            None,
            STANDING_BACKWARD_4GRAM_633,
            STANDING_BACKWARD_4GRAM_208,
        )
        self.assertEqual(
            group_sites_by_backward_4gram(sites, one_none),
            (
                (
                    STANDING_BACKWARD_4GRAM_633,
                    ((SIDE_IA, "Ia4", 158), (SIDE_IA, "Ia6", 102)),
                ),
                (STANDING_BACKWARD_4GRAM_208, ((SIDE_IA, "Ia13", 48),)),
            ),
        )
        self.assertEqual(
            sites_with_backward(sites, one_none),
            (sites[0], sites[2], sites[3]),
        )
        self.assertEqual(sites_without_backward(sites, one_none), (sites[1],))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076020010Backward4gramScoreboard(unittest.TestCase):
    """Cited-fixture leftover overlap 3-gram backward-4 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.backwards = leftover_backward_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM3,
        )
        self.with_backward = sites_with_backward(self.leftover_sites, self.backwards)
        self.no_backward = sites_without_backward(self.leftover_sites, self.backwards)
        self.groups = group_sites_by_backward_4gram(self.leftover_sites, self.backwards)
        self.n_leftover = len(self.leftover_sites)
        self.n_with_backward = len(self.with_backward)
        self.n_no_backward = len(self.no_backward)
        self.n_distinct = len(self.groups)
        self.claim_holds = i_leftover_076_020_010_share_one_backward_4gram(
            self.n_with_backward,
            self.n_distinct,
        )

    def test_tokens_and_sites_are_cycle_161_lock_not_retuned(self):
        """3-gram and leftover sites stay the cycle-161 lock."""
        self.assertEqual(GRAM3, ("076", "020", "010"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(MAXIMAL_N5_400, ("400", "070", "076", "020", "010"))
        self.assertEqual(LEFTOVER_N4_050, ("076", "020", "010", "050"))
        self.assertEqual(LEFTOVER_N4_090, ("090", "076", "020", "010"))
        self.assertEqual(LEFTOVER_N4_053, ("053", "076", "020", "010"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(
            STANDING_LEFTOVER_SITES,
            (
                (SIDE_IA, "Ia4", 158),
                (SIDE_IA, "Ia5", 56),
                (SIDE_IA, "Ia6", 102),
                (SIDE_IA, "Ia13", 48),
            ),
        )
        prior_162 = self.survey["i_leftover_076_020_010_forward_4gram"]
        self.assertEqual(prior_162["cycle"], 162)
        self.assertEqual(tuple(prior_162["tokens3"]), GRAM3)
        self.assertEqual(prior_162["N_leftover"], STANDING_N_LEFTOVER)
        self.assertFalse(prior_162["i_leftover_076_020_010_share_one_forward_4gram"])
        self.assertEqual(prior_162["N_distinct_forward_4grams"], 4)
        prior_161 = self.survey["i_overlap_3gram_076_020_010_inside_family"]
        self.assertEqual(prior_161["cycle"], 161)
        self.assertEqual(tuple(prior_161["tokens3"]), GRAM3)
        self.assertEqual(prior_161["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(prior_161["N_leftover"], 4)
        self.assertEqual(prior_161["N_inside"], 8)
        self.assertEqual(
            tuple(tuple(row) for row in prior_161["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertFalse(prior_161["i_overlap_3gram_076_020_010_all_inside_known_family"])
        prior_160 = self.survey["i_overlap_3gram_076_020_010_i_only"]
        self.assertEqual(prior_160["cycle"], 160)
        self.assertEqual(prior_160["N_on_I"], 12)
        self.assertTrue(prior_160["i_overlap_3gram_076_020_010_is_i_only"])
        prior_144 = self.survey["i_leftover_076_010_079_backward_4gram"]
        self.assertEqual(prior_144["cycle"], 144)
        self.assertEqual(prior_144["N_distinct_backward_4grams"], 2)
        self.assertFalse(prior_144["i_leftover_076_010_079_share_one_backward_4gram"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_four_leftovers_have_four_distinct_backwards_and_claim_loses(self):
        """N_leftover=4, N_with_backward=4, N_distinct=4. Claim loses."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 4)
        self.assertEqual(self.n_with_backward, STANDING_N_WITH_BACKWARD)
        self.assertEqual(STANDING_N_WITH_BACKWARD, 4)
        self.assertEqual(self.n_no_backward, STANDING_N_NO_BACKWARD)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_BACKWARD_4GRAMS)
        self.assertEqual(STANDING_N_DISTINCT_BACKWARD_4GRAMS, 4)
        self.assertEqual(self.backwards, STANDING_PER_SITE_BACKWARD)
        self.assertEqual(self.with_backward, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.no_backward, STANDING_NO_BACKWARD_SITES)
        self.assertEqual(self.groups, STANDING_SITES_PER_BACKWARD_4GRAM)
        self.assertEqual(
            tuple(gram for gram, _sites in self.groups),
            STANDING_DISTINCT_BACKWARD_4GRAMS,
        )
        expected = (
            (("633", "076", "020", "010"), (SIDE_IA, "Ia4", 158)),
            (("208", "076", "020", "010"), (SIDE_IA, "Ia5", 56)),
            (("005", "076", "020", "010"), (SIDE_IA, "Ia6", 102)),
            (("536", "076", "020", "010"), (SIDE_IA, "Ia13", 48)),
        )
        family_prefixes = (
            LEFTOVER_N4_090,
            LEFTOVER_N4_053,
            MAXIMAL_N5_400[1:],
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
            self.assertEqual(site_backward_4gram(stems, index, GRAM3), want_back)
            self.assertEqual(len(back), STANDING_N4)
            self.assertEqual(back[1:], GRAM3)
            self.assertNotIn(back, family_prefixes)
            self.assertNotEqual(back, LEFTOVER_N4_050)
            self.assertEqual(side, SIDE_IA)
            self.assertEqual(line, want_site[1])
        self.assertEqual(
            i_leftover_076_020_010_share_one_backward_4gram(
                self.n_with_backward,
                self.n_distinct,
            ),
            STANDING_I_LEFTOVER_076_020_010_SHARE_ONE_BACKWARD_4GRAM,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_020_010_SHARE_ONE_BACKWARD_4GRAM,
        )
        self.assertFalse(STANDING_I_LEFTOVER_076_020_010_SHARE_ONE_BACKWARD_4GRAM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_020_010_share_one_backward_4gram")
        self.assertFalse(STANDING_SAME_AS_FAMILY_090)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE144)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_162_161_160_144_103_and_w_scoreboards_still_compute(self):
        """Cycle 162 forward, 161 inside, 160 I-only, 144 backward, 103, W stay."""
        prior_162 = TestMamariILeftover076020010Forward4gramScoreboard()
        prior_162.setUp()
        prior_162.test_four_leftovers_have_four_distinct_forwards_and_claim_loses()
        prior_162.test_survey_matches_computed_lock()
        prior_161 = TestMamariIOverlap3gram076020010InsideFamilyScoreboard()
        prior_161.setUp()
        prior_161.test_twelve_sites_split_8_inside_4_leftover_and_claim_loses()
        prior_161.test_survey_matches_computed_lock()
        prior_160 = TestMamariIOverlap3gram076020010IOnlyScoreboard()
        prior_160.setUp()
        prior_160.test_i_hits_are_twelve_on_ia()
        prior_160.test_3gram_is_zero_off_i_and_i_only()
        prior_160.test_survey_matches_computed_lock()
        prior_144 = TestMamariILeftover076010079Backward4gramScoreboard()
        prior_144.setUp()
        prior_144.test_three_leftovers_have_two_distinct_backwards_and_claim_loses()
        prior_144.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-163 leftover backward-4 lock."""
        lock = self.survey["i_leftover_076_020_010_backward_4gram"]
        self.assertEqual(lock["cycle"], 163)
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
        self.assertEqual(lock["N_leftover"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_backward"], STANDING_N_WITH_BACKWARD)
        self.assertEqual(lock["N_with_backward"], 4)
        self.assertEqual(lock["N_no_backward"], STANDING_N_NO_BACKWARD)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_backward_sites"]),
            STANDING_NO_BACKWARD_SITES,
        )
        self.assertEqual(
            lock["N_distinct_backward_4grams"],
            STANDING_N_DISTINCT_BACKWARD_4GRAMS,
        )
        self.assertEqual(lock["N_distinct_backward_4grams"], 4)
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
        self.assertFalse(lock["i_leftover_076_020_010_share_one_backward_4gram"])
        self.assertEqual(
            lock["i_leftover_076_020_010_share_one_backward_4gram"],
            STANDING_I_LEFTOVER_076_020_010_SHARE_ONE_BACKWARD_4GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle144"])
        self.assertFalse(lock["same_as_family_090"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_076_020_010_forward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_020_010_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_020_010_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_backward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_010_079_forward_4gram_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_inside_two_5grams_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_independent_n5_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_independent_n5_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_independent_nge4_maximals_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_076_020_010_forward_4gram"]["cycle"], 162)
        self.assertFalse(
            self.survey["i_leftover_076_020_010_forward_4gram"][
                "i_leftover_076_020_010_share_one_forward_4gram"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_020_010_forward_4gram"][
                "N_distinct_forward_4grams"
            ],
            4,
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_inside_family"]["cycle"], 161)
        self.assertFalse(
            self.survey["i_overlap_3gram_076_020_010_inside_family"][
                "i_overlap_3gram_076_020_010_all_inside_known_family"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_inside_family"]["N_leftover"], 4)
        self.assertEqual(
            tuple(
                tuple(row)
                for row in self.survey["i_overlap_3gram_076_020_010_inside_family"]["leftover_sites"]
            ),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_i_only"]["cycle"], 160)
        self.assertTrue(
            self.survey["i_overlap_3gram_076_020_010_i_only"][
                "i_overlap_3gram_076_020_010_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_i_only"]["N_on_I"], 12)
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
        self.assertEqual(
            self.survey["i_leftover_076_010_079_forward_4gram"]["N_distinct_forward_4grams"],
            3,
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
        self.assertEqual(self.survey["i_leftover_n4_independent_n5_n3_overlap"]["cycle"], 159)
        self.assertTrue(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"][
                "i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"
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
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftover076020010Backward4gramImageSnapshot(unittest.TestCase):
    """Cycle 163 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
