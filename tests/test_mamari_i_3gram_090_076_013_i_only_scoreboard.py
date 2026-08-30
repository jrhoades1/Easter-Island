"""I's cycle-228 leftover extra remaining-after-071 3-gram 090 076 013 off-I lock.

Cycle 229 text-search lock. Uses already-vendored A–V and the
cycle-228 leftover extra remaining-after-071 next stem G=013
(K=5 of N_remaining2=41). Does not retune that leftover extra
remaining-after-071 lock, leftover extra remaining 071, leftover
extra forward 070, leftover extra sites, the leftover n=4 set,
or the already-closed leftover remaining family. Does not vendor
a new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same claim-shape as cycle 195 (090 076 071 was I-only 6/0),
cycle 174 (076 071 076 was I-only 6/0), and cycle 171
(076 071 was I-only 43/0). Cycle 207 lost: 090 076 070 is
not I-only (8/1 on T). Cycle 223 lost: 090 076 is not I-only
(69/3 on T). This cycle is the new leftover extra
remaining-after-071 3-gram 090 076 013 only. 090 076 070,
090 076 071, and 090 076 without 013 do not count as this
3-gram. Do not retune leftover n=4, 076-cells, or any
detector. Do not lock leftover extra remaining after 013
this cycle. Off-I T sites of 090 076 are not this cycle
except as off-I of 090 076 013 if they match. Do not assume
the I-only result.

Locks exact consecutive hits of 090 076 013 on tablet I and
on every other vendored tablet A–H and J–V. Claim that can
lose: i_3gram_090_076_013_i_only (I hits ≥ 1 and off-I hits
== 0). True only if N_off_I == 0. Measured: Ia is exactly 5
at Ia3[37]/Ia5[6]/Ia5[164]/Ia6[92]/Ia13[67]; Ib unpublished
0; every other vendored tablet is exact-0. Those 5 equal the
cycle-228 leftover extra remaining-after-071 013 cluster
(next 4-grams 090 076 013 073 / 291 / 076 / 070 / 755). Extra
I sites not in leftover extra remaining-after-071 = 0
(leftover of leftover would be a later cycle if any
appeared). The claim is true. Not an n≥8 island. Not the
cycle-103 I 5-gram. Nested leftover extra remaining-after-071
K=5 / G=013, cycle 227 6/071, cycle 226 8/070, cycle 223
69/3, cycle 195 6/0, and cycle 171 43/0 stay.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_g_nge8_scoreboard import (
    nge8_sites,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    TA_LINE_NAMES,
    load_t_sides,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES as CYCLE223_I_SITES,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_FOLLOWING_3GRAMS as CYCLE223_OFF_I_FOLLOWING_3GRAMS,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_076_071_076_i_only_scoreboard import (
    GRAM3 as CYCLE174_GRAM3,
    STANDING_I_3GRAM_076_071_076_I_ONLY as CYCLE174_CLAIM,
    STANDING_N_I as CYCLE174_N_I,
    STANDING_N_OFF_I as CYCLE174_N_OFF_I,
    TestMamariI3gram076071076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
    STANDING_I_3GRAM_090_076_071_I_ONLY as CYCLE195_CLAIM,
    STANDING_I_SITES as CYCLE195_I_SITES,
    STANDING_N_I as CYCLE195_N_I,
    STANDING_N_OFF_I as CYCLE195_N_OFF_I,
    TestMamariI3gram090076071IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_070_scoreboard import (
    STANDING_G as CYCLE226_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070 as CYCLE226_CLAIM,
    STANDING_K as CYCLE226_K,
    STANDING_MATCHING_SITES as CYCLE226_MATCHING_SITES,
    TestMamariILeftoverExtra090076Forward070Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_071_next_stem_scoreboard import (
    GRAM3_FORWARD,
    STANDING_G as CYCLE228_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G as CYCLE228_CLAIM,
    STANDING_K as CYCLE228_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE228_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE228_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING2 as CYCLE228_N_DISTINCT_REMAINING2,
    STANDING_N_REMAINING2 as CYCLE228_N_REMAINING2,
    leftover_extra_remaining_after_071,
    leftover_extra_remaining_after_071_with_g,
    TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    STANDING_G as CYCLE227_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071 as CYCLE227_CLAIM,
    STANDING_K as CYCLE227_K,
    STANDING_MATCHING_SITES as CYCLE227_MATCHING_SITES,
    TestMamariILeftoverExtra090076RemainingNextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    leftover_extra_next_stems,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
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
from tests.test_mamari_keiti_n9_scoreboard import (
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_s_nge6_scoreboard import (
    nge6_sites,
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
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
    load_g_k_sides,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    SIDE_SA,
    SIDE_SB,
    load_s_sides,
)

HYPOTHESIS_I_ONLY = True
GRAM3 = GRAM3_FORWARD
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_090_076_071 = CYCLE195_GRAM3
NEAR_MISS_076_071_076 = CYCLE174_GRAM3
NEAR_MISS_090_076 = GRAM2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_I_HITS = 5
STANDING_IA_HITS = 5
STANDING_IB_HITS = 0
STANDING_N_ON_I = 5
STANDING_N_I = 5
STANDING_I_SITES = (
    (SIDE_IA, "Ia3", 37),
    (SIDE_IA, "Ia5", 6),
    (SIDE_IA, "Ia5", 164),
    (SIDE_IA, "Ia6", 92),
    (SIDE_IA, "Ia13", 67),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_MATCHING_SITES = CYCLE228_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_COUNT = 5
STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS = CYCLE228_MATCHING_NEXT_4GRAMS
STANDING_EXTRA_I_SITES = ()
STANDING_N_EXTRA = 0
STANDING_I_PREVIOUS_4GRAMS = (
    ("999", "090", "076", "013"),
    ("295", "090", "076", "013"),
    ("009", "090", "076", "013"),
    ("999", "090", "076", "013"),
    ("386", "090", "076", "013"),
)
STANDING_I_NEXT_4GRAMS = (
    ("090", "076", "013", "073"),
    ("090", "076", "013", "291"),
    ("090", "076", "013", "076"),
    ("090", "076", "013", "070"),
    ("090", "076", "013", "755"),
)
STANDING_OFF_I_HITS = 0
STANDING_N_OFF_I = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_OFF_I_BY_TABLET_NONZERO = {}
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_3gram_090_076_013_i_only"
STANDING_I_3GRAM_090_076_013_I_ONLY = True
STANDING_RESULT = "i_3gram_090_076_013_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE174_3GRAM = False
STANDING_SAME_AS_CYCLE195_3GRAM = False
STANDING_SAME_AS_CYCLE207_3GRAM = False
STANDING_SAME_AS_CYCLE223_2GRAM = False
STANDING_SAME_AS_CYCLE228 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE174 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE195 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207 = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_090_076_WITHOUT_013_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_013_IS_NOT_THIS_CYCLE = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_CYCLE228_K = 5
STANDING_CYCLE228_G = "013"


def i_3gram_090_076_013_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


def leftover_extra_remaining_after_071_013_subset(
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff leftover extra remaining-after-071 013 sites ⊆ I 090 076 013."""
    return set(leftover_matching).issubset(set(i_sites))


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 090 076 013 sites that are not leftover extra remaining-after-071 013."""
    leftover_set = set(leftover_matching)
    return tuple(site for site in i_sites if site not in leftover_set)


def named_off_i_sites(
    gram: tuple[str, ...] = GRAM3,
) -> tuple[tuple[str, str, int], ...]:
    """Named (side, line, index) hits on G, S, and T. Search only."""
    gk = load_g_k_sides()
    g_sites = nge8_sites(gram, gk)
    s_sites = nge6_sites(gram, load_s_sides())
    t = load_t_sides()
    t_sites = tuple(
        site_tuple(hit)
        for hit in named_side_hits(t[SIDE_TA], TA_LINE_NAMES, SIDE_TA, gram)
    )
    return g_sites + s_sites + t_sites


class TestI3gram090076013IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-228 leftover extra remaining-after-071 3-gram. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. 090 076 070 / 071 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "013"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["090", "076", "013", "090", "076", "013"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 2)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_071)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_076_071_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "070"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "071"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "013"]], GRAM3), 0)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_013_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Measured 5/0 holds."""
        provider = MockProvider()
        self.assertTrue(i_3gram_090_076_013_i_only(1, 0))
        self.assertTrue(i_3gram_090_076_013_i_only(5, 0))
        self.assertFalse(i_3gram_090_076_013_i_only(5, 1))
        self.assertFalse(i_3gram_090_076_013_i_only(1, 1))
        self.assertFalse(i_3gram_090_076_013_i_only(0, 0))
        self.assertFalse(i_3gram_090_076_013_i_only(0, 1))
        self.assertEqual(STANDING_CLAIM, "i_3gram_090_076_013_i_only")
        self.assertTrue(STANDING_I_3GRAM_090_076_013_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(
            STANDING_I_3GRAM_090_076_013_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_fail(self):
        """Leftover extra remaining-after-071 013 ⊆ I sites; extra can be nonempty."""
        provider = MockProvider()
        self.assertTrue(
            leftover_extra_remaining_after_071_013_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(STANDING_LEFTOVER_MATCHING_SITES, STANDING_I_SITES)
        self.assertEqual(extra_i_sites(), STANDING_EXTRA_I_SITES)
        self.assertEqual(len(extra_i_sites()), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        planted_extra = STANDING_I_SITES + ((SIDE_IA, "Ia1", 0),)
        self.assertFalse(
            leftover_extra_remaining_after_071_013_subset(
                STANDING_LEFTOVER_MATCHING_SITES + ((SIDE_IA, "Ia1", 0),),
                STANDING_I_SITES,
            )
        )
        self.assertEqual(len(extra_i_sites(planted_extra)), 1)
        dropped = STANDING_I_SITES[1:]
        self.assertFalse(
            leftover_extra_remaining_after_071_013_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                dropped,
            )
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_cycle228_leftover_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-228 leftover extra remaining-after-071 G, not priors."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "013"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM3[:2], GRAM2)
        self.assertEqual(GRAM3[2], CYCLE228_G)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE174_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, GRAM2)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE174_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE223_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE228)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE174)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE195)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        self.assertLess(len(GRAM3), 8)
        for nxt4 in STANDING_I_NEXT_4GRAMS:
            self.assertTrue(is_contiguous_substring(GRAM3, nxt4))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_070))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_071))
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM3))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram090076013IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover extra remaining-after-071 3-gram 090 076 013 off-I lock."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM3, self.i_sides)
        self.ia_hits = ngram_hit_count(self.i_sides[SIDE_IA], GRAM3)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM3, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM3, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)
        self.off_i_sites = named_off_i_sites(GRAM3)
        self.next_stems = leftover_extra_next_stems(
            self.i_sides,
            STANDING_LEFTOVER_SITES,
            GRAM2,
        )
        self.remaining2 = leftover_extra_remaining_after_071(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.leftover_matching = leftover_extra_remaining_after_071_with_g(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
            CYCLE228_G,
        )
        self.extra = extra_i_sites(self.i_sites, self.leftover_matching)
        self.claim_holds = i_3gram_090_076_013_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_228_leftover_not_retuned(self):
        """3-gram is the cycle-228 leftover extra remaining-after-071 G, not a new inventory."""
        self.assertEqual(GRAM3, ("090", "076", "013"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM3[:2], GRAM2)
        self.assertEqual(GRAM3[2], "013")
        prior_228 = self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]
        self.assertEqual(prior_228["cycle"], 228)
        self.assertEqual(tuple(prior_228["forward_3gram"]), GRAM3)
        self.assertEqual(prior_228["G"], "013")
        self.assertEqual(prior_228["K"], 5)
        self.assertEqual(prior_228["N_remaining2"], 41)
        self.assertEqual(prior_228["N_distinct_remaining2"], 28)
        self.assertEqual(CYCLE228_G, "013")
        self.assertEqual(CYCLE228_K, 5)
        self.assertEqual(CYCLE228_N_REMAINING2, 41)
        self.assertEqual(CYCLE228_N_DISTINCT_REMAINING2, 28)
        self.assertTrue(CYCLE228_CLAIM)
        self.assertTrue(prior_228["i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G"])
        measured_matching = [list(site) for site in CYCLE228_MATCHING_SITES]
        self.assertEqual(
            [list(site) for site in prior_228["matching_leftover_extra_remaining_after_071_sites"]],
            measured_matching,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE228_MATCHING_NEXT_4GRAMS],
            prior_228["matching_next_4grams"],
        )
        self.assertEqual(self.leftover_matching, CYCLE228_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE228_K)
        self.assertEqual(STANDING_CYCLE228_K, 5)
        self.assertEqual(STANDING_CYCLE228_G, "013")
        self.assertEqual(len(self.remaining2), 41)
        if len(self.leftover_matching) != 5 or CYCLE228_G != "013":
            self.fail("nested cycle 228 leftover extra remaining-after-071 G=013 K=5 drifted")
        prior_227 = self.survey["i_leftover_extra_090_076_remaining_next_stem"]
        self.assertEqual(prior_227["cycle"], 227)
        self.assertEqual(prior_227["G"], "071")
        self.assertEqual(prior_227["K"], 6)
        self.assertTrue(prior_227["i_leftover_extra_090_076_remaining_exactly_6_share_071"])
        prior_226 = self.survey["i_leftover_extra_090_076_forward_070"]
        self.assertEqual(prior_226["cycle"], 226)
        self.assertEqual(prior_226["G"], "070")
        self.assertEqual(prior_226["K"], 8)
        self.assertTrue(prior_226["i_leftover_extra_090_076_exactly_8_share_forward_070"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_195 = self.survey["i_3gram_090_076_071_i_only"]
        self.assertEqual(prior_195["cycle"], 195)
        self.assertEqual(prior_195["N_I"], 6)
        self.assertEqual(prior_195["N_off_I"], 0)
        self.assertTrue(prior_195["i_3gram_090_076_071_i_only"])
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE195_GRAM3)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_013_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_five_on_ia_and_equal_leftover_extra_013(self):
        """3-gram is 5 on Ia; Ib 0. Those 5 equal leftover extra remaining-after-071 013."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 5)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 5)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 5)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM3, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM3), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE228_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, STANDING_I_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 5)
        self.assertTrue(
            leftover_extra_remaining_after_071_013_subset(
                self.leftover_matching,
                self.i_sites,
            )
        )
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        if self.i_hits != 5:
            self.fail("measured N_I drifted from 5")
        if self.leftover_matching != self.i_sites:
            self.fail("leftover extra remaining-after-071 013 set drifted from I 090 076 013")
        if self.extra:
            self.fail("extra I 090 076 013 sites appeared; leftover of leftover is not this cycle")
        for (side, line, index), prev4, nxt4 in zip(
            STANDING_I_SITES,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            strict=True,
        ):
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N3]), prev4)
            self.assertEqual(tuple(stems[index : index + STANDING_N4]), nxt4)
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), nxt4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn((side, line, index), STANDING_LEFTOVER_SITES)
            self.assertIn((side, line, index), CYCLE228_MATCHING_SITES)
            self.assertNotIn((side, line, index), CYCLE224_INSIDE_SITES)
            self.assertNotIn((side, line, index), CYCLE226_MATCHING_SITES)
            self.assertNotIn((side, line, index), CYCLE227_MATCHING_SITES)
            self.assertNotIn((side, line, index), CYCLE195_I_SITES)
            self.assertNotIn((side, line, index), CYCLE207_I_SITES)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia3", 37),
                (SIDE_IA, "Ia5", 6),
                (SIDE_IA, "Ia5", 164),
                (SIDE_IA, "Ia6", 92),
                (SIDE_IA, "Ia13", 67),
            ),
        )
        self.assertEqual(STANDING_I_NEXT_4GRAMS, CYCLE228_MATCHING_NEXT_4GRAMS)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_I_SITES)
        for site in CYCLE223_I_SITES:
            if site not in STANDING_I_SITES:
                stems = line_stems_for_site(self.i_sides, site)
                index = site[2]
                self.assertEqual(tuple(stems[index : index + 2]), GRAM2)
                if index + 3 <= len(stems):
                    self.assertNotEqual(tuple(stems[index : index + 3]), GRAM3)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_013_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_zero_off_i_and_i_only(self):
        """3-gram is 0 on A–H and J–V. Ia has exactly 5. T 090 076 is not this 3-gram."""
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
        self.assertEqual(self.off_i_sites, STANDING_OFF_I_SITES)
        self.assertEqual(STANDING_OFF_I_SITES, ())
        self.assertEqual(STANDING_OFF_I_TABLETS_WITH_HITS, ())
        self.assertEqual(STANDING_OFF_I_BY_TABLET_NONZERO, {})
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM3))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 5)
            else:
                self.assertEqual(count, 0)
        gk = load_g_k_sides()
        self.assertEqual(ngram_hit_count(gk[SIDE_GR], GRAM3), 0)
        self.assertEqual(ngram_hit_count(gk[SIDE_GV], GRAM3), 0)
        s_sides = load_s_sides()
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SA], GRAM3), 0)
        self.assertEqual(ngram_hit_count(s_sides[SIDE_SB], GRAM3), 0)
        t_sides = load_t_sides()
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], GRAM3), 0)
        self.assertEqual(named_off_i_sites(GRAM3), ())
        self.assertEqual(CYCLE223_OFF_I_SITES, (
            (SIDE_TA, "Ta5", 9),
            (SIDE_TA, "Ta7", 5),
            (SIDE_TA, "Ta9", 2),
        ))
        self.assertEqual(
            CYCLE223_OFF_I_FOLLOWING_3GRAMS,
            (("090", "076", "010"), ("090", "076", "126"), ("090", "076", "070")),
        )
        for site, following in zip(
            CYCLE223_OFF_I_SITES,
            CYCLE223_OFF_I_FOLLOWING_3GRAMS,
            strict=True,
        ):
            side, line, index = site
            stems = t_sides[side][TA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + 2]), GRAM2)
            self.assertEqual(tuple(stems[index : index + 3]), following)
            self.assertNotEqual(following, GRAM3)
            self.assertNotIn(site, STANDING_I_SITES)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        ta9 = t_sides[SIDE_TA][TA_LINE_NAMES.index("Ta9")]
        self.assertEqual(tuple(ta9[2:5]), CYCLE207_GRAM3)
        self.assertNotEqual(tuple(ta9[2:5]), GRAM3)
        self.assertEqual(
            i_3gram_090_076_013_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_3GRAM_090_076_013_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_090_076_013_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_3GRAM_090_076_013_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_3gram_090_076_013_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE174_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE223_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE228)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE174)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE195)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        if self.off_i_hits != 0:
            self.fail("measured N_off_I drifted from 0")
        if self.i_hits != STANDING_N_I:
            self.fail("measured N_I drifted from the locked count")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_228_227_226_223_195_and_171_still_compute(self):
        """Cycle 228 K=5/G=013, 227 6/071, 226 8/070, 223 69/3, 195 6/0, 171 43/0 stay."""
        prior_228 = TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard()
        prior_228.setUp()
        prior_228.test_counts_41_remaining2_g_013_k_5_and_hypothesis_holds()
        prior_228.test_survey_matches_computed_lock()
        self.assertEqual(prior_228.k, 5)
        self.assertEqual(prior_228.g, "013")
        self.assertEqual(prior_228.n_remaining2, 41)
        self.assertEqual(prior_228.matching, CYCLE228_MATCHING_SITES)
        self.assertTrue(prior_228.claim_holds)
        self.assertTrue(CYCLE228_CLAIM)
        if prior_228.k != 5 or prior_228.g != "013" or prior_228.n_remaining2 != 41:
            self.fail("nested cycle 228 leftover extra remaining-after-071 G=013 K=5 drifted")
        prior_227 = TestMamariILeftoverExtra090076RemainingNextStemScoreboard()
        prior_227.setUp()
        prior_227.test_counts_47_remaining_g_071_k_6_and_hypothesis_holds()
        prior_227.test_survey_matches_computed_lock()
        self.assertEqual(prior_227.k, 6)
        self.assertEqual(CYCLE227_G, "071")
        self.assertEqual(CYCLE227_K, 6)
        self.assertEqual(prior_227.matching, CYCLE227_MATCHING_SITES)
        self.assertTrue(prior_227.claim_holds)
        self.assertTrue(CYCLE227_CLAIM)
        if prior_227.k != 6 or CYCLE227_G != "071":
            self.fail("nested cycle 227 leftover extra remaining 6/071 drifted")
        prior_226 = TestMamariILeftoverExtra090076Forward070Scoreboard()
        prior_226.setUp()
        prior_226.test_counts_8_of_56_and_hypothesis_k_8_holds()
        prior_226.test_survey_matches_computed_lock()
        self.assertEqual(prior_226.k, 8)
        self.assertEqual(CYCLE226_G, "070")
        self.assertEqual(CYCLE226_K, 8)
        self.assertEqual(prior_226.matching, CYCLE226_MATCHING_SITES)
        self.assertTrue(prior_226.claim_holds)
        self.assertTrue(CYCLE226_CLAIM)
        if prior_226.k != 8 or CYCLE226_G != "070":
            self.fail("nested cycle 226 leftover extra 8/070 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, CYCLE223_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, CYCLE223_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, CYCLE223_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertFalse(prior_207.claim_holds)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_195 = TestMamariI3gram090076071IOnlyScoreboard()
        prior_195.setUp()
        prior_195.test_i_hits_are_six_on_ia()
        prior_195.test_3gram_is_zero_off_i_and_i_only()
        prior_195.test_survey_matches_computed_lock()
        self.assertEqual(prior_195.i_hits, CYCLE195_N_I)
        self.assertEqual(prior_195.i_hits, 6)
        self.assertEqual(prior_195.off_i_hits, CYCLE195_N_OFF_I)
        self.assertEqual(prior_195.off_i_hits, 0)
        self.assertEqual(prior_195.i_sites, CYCLE195_I_SITES)
        self.assertTrue(prior_195.claim_holds)
        self.assertTrue(CYCLE195_CLAIM)
        if prior_195.i_hits != 6 or prior_195.off_i_hits != 0:
            self.fail("nested cycle 195 090 076 071 I-only 6/0 drifted")
        prior_174 = TestMamariI3gram076071076IOnlyScoreboard()
        prior_174.setUp()
        prior_174.test_3gram_is_zero_off_i_and_i_only()
        self.assertEqual(CYCLE174_N_I, 6)
        self.assertEqual(CYCLE174_N_OFF_I, 0)
        self.assertTrue(CYCLE174_CLAIM)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-229 3-gram I-only lock."""
        lock = self.survey["i_3gram_090_076_013_i_only"]
        self.assertEqual(lock["cycle"], 229)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 5)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_extra_remaining_after_071_013_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(
            lock["leftover_extra_remaining_after_071_013_count"],
            STANDING_LEFTOVER_MATCHING_COUNT,
        )
        self.assertEqual(lock["leftover_extra_remaining_after_071_013_count"], 5)
        self.assertTrue(lock["leftover_extra_remaining_after_071_013_subset_of_i_sites"])
        self.assertEqual(lock["extra_i_sites"], [])
        self.assertEqual(lock["N_extra"], 0)
        self.assertEqual(
            [list(gram) for gram in STANDING_I_PREVIOUS_4GRAMS],
            lock["i_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_I_NEXT_4GRAMS],
            lock["i_next_4grams"],
        )
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(lock["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(lock["N_off_I"], 0)
        self.assertEqual(
            [list(site) for site in STANDING_OFF_I_SITES],
            lock["off_i_sites"],
        )
        self.assertEqual(tuple(lock["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(lock["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(lock["off_i_tablets_with_hits"]), STANDING_OFF_I_TABLETS_WITH_HITS)
        self.assertEqual(lock["off_i_by_tablet_nonzero"], STANDING_OFF_I_BY_TABLET_NONZERO)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["nested_cycle228_G"], STANDING_CYCLE228_G)
        self.assertEqual(lock["nested_cycle228_G"], "013")
        self.assertEqual(lock["nested_cycle228_K"], STANDING_CYCLE228_K)
        self.assertEqual(lock["nested_cycle228_K"], 5)
        self.assertEqual(lock["nested_cycle228_N_remaining2"], 41)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_3gram_090_076_013_i_only"])
        self.assertEqual(
            lock["i_3gram_090_076_013_i_only"],
            STANDING_I_3GRAM_090_076_013_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle174_3gram"])
        self.assertFalse(lock["same_as_cycle195_3gram"])
        self.assertFalse(lock["same_as_cycle207_3gram"])
        self.assertFalse(lock["same_as_cycle223_2gram"])
        self.assertFalse(lock["same_as_cycle228"])
        self.assertTrue(lock["same_claim_shape_as_cycle174"])
        self.assertTrue(lock["same_claim_shape_as_cycle195"])
        self.assertTrue(lock["same_claim_shape_as_cycle207"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["090_076_without_013_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_013_is_not_this_cycle"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_071_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_070_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_076_071_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["cycle"],
            228,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"][
                "i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["G"],
            "013",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["K"],
            5,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]["N_remaining2"],
            41,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["cycle"], 227)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_next_stem"][
                "i_leftover_extra_090_076_remaining_exactly_6_share_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["G"], "071")
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["K"], 6)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["cycle"], 226)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_forward_070"][
                "i_leftover_extra_090_076_exactly_8_share_forward_070"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["G"], "070")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["K"], 8)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["cycle"], 195)
        self.assertTrue(self.survey["i_3gram_090_076_071_i_only"]["i_3gram_090_076_071_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["cycle"], 174)
        self.assertTrue(self.survey["i_3gram_076_071_076_i_only"]["i_3gram_076_071_076_i_only"])
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_076_071_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
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


class TestMamariI3gram090076013IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 229 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
