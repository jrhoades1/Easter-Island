"""I's cycle-289 leftover n=4 remaining 3-gram 090 076 020 off-I lock.

Cycle 290 text-search lock. Uses already-vendored A–V and the
cycle-289 leftover n=4 remaining I 090 076 exactly 4 share
next 020 cluster (the 4 leftover n=4 remaining sites inside
090 076 020 010). Does not retune that leftover n=4 remaining
020 lock, leftover n=4 remaining share-one-forward-stem
(cycle 288 lost), leftover n=4 remaining sites, the leftover
n=4 set, leftover extra peels (225–287), leftover extra
remaining-after-000 next stems (cycle 256), or the
already-closed leftover remaining family. Does not vendor a
new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same claim-shape as cycle 236 (090 076 700 was I-only 2/0),
`020` instead of `700`. Cycle 245 leftover extra 090 076 087
I-only 5/0 extra I=3 and cycle 248 leftover extra 090 076 011
I-only 4/0 extra I=2 are leftover extra remaining-after-280/087
3-grams, different from leftover n=4 remaining 090 076 020.
Cycle 207 lost: 090 076 070 is not I-only (8/1 on T). Cycle
223 lost: 090 076 is not I-only (69/3 on T). This cycle is
the new leftover n=4 remaining 3-gram 090 076 020 only.
090 076 700, 090 076 087, 090 076 011, 090 076 070,
090 076 071, and 090 076 without 020 do not count as this
3-gram. Leftover extra remaining-after-000 next stems exclude
020, so leftover extra has zero 090 076 020 sites. Extra I of
leftover extra remaining-after-009 008 090 076 at Ia12[82]
sits inside leftover n=4 remaining 090 076 020 010 at
Ia12[83] (nested inventory, not this claim). Do not retune
leftover extra peels (225–287). Do not overwrite cycle
167/268–289. Do not retune leftover n=4, 076-cells, or any
detector. Do not lock leftover n=4 remaining remaining-after-
020 next stems this cycle. Do not lock I 090 076 020 forward
4-grams this cycle (later cycle if this holds; cycle 289
already notes all 4 continue 010, so a later hapax claim can
lose). Off-I T sites of 090 076 are not this cycle except as
off-I of 090 076 020 if they match. Do not assume the I-only
result.

Locks exact consecutive hits of 090 076 020 on tablet I and
on every other vendored tablet A–H and J–V. Claim that can
lose: i_3gram_090_076_020_i_only (I hits ≥ 1 and off-I hits
== 0). True only if N_off_I == 0. Measured: Ia is exactly 4
at Ia2[119]/Ia4[86]/Ia5[143]/Ia12[83]; Ib unpublished 0;
every other vendored tablet is exact-0. Those 4 equal the
cycle-289 leftover n=4 remaining 020 cluster (every next
4-gram 090 076 020 010). Extra I sites not in leftover n=4
remaining = 0 (leftover extra has no 020 and N_I=69 = 56+13).
Extra I ≠ 0 does not make the claim lose (still I-only);
still lock extra I. Nested leftover n=4 remaining 4 share
020 ⊆ I 090 076 020 sites. Nested Ia12[83] ∈ that set. The
claim is true. Not an n≥8 island. Not the cycle-103 I 5-gram.
Nested cycle 289 K=4 / G=020, cycle 288 N_distinct=6
unique-max G=020 K=4, cycle 256 leftover extra remaining-
after-000 next stems exclude 020, cycle 236 2/0, cycle 224
13/56, cycle 223 69/3, and cycle 207 8/1 on T stay.

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
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_020010_COVERED,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
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
from tests.test_mamari_i_3gram_090_076_011_i_only_scoreboard import (
    GRAM3 as CYCLE248_GRAM3,
    STANDING_I_3GRAM_090_076_011_I_ONLY as CYCLE248_CLAIM,
    STANDING_I_SITES as CYCLE248_I_SITES,
    STANDING_N_EXTRA as CYCLE248_N_EXTRA,
    STANDING_N_I as CYCLE248_N_I,
    STANDING_N_OFF_I as CYCLE248_N_OFF_I,
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
)
from tests.test_mamari_i_3gram_090_076_087_i_only_scoreboard import (
    GRAM3 as CYCLE245_GRAM3,
    STANDING_I_3GRAM_090_076_087_I_ONLY as CYCLE245_CLAIM,
    STANDING_I_SITES as CYCLE245_I_SITES,
    STANDING_N_EXTRA as CYCLE245_N_EXTRA,
    STANDING_N_I as CYCLE245_N_I,
    STANDING_N_OFF_I as CYCLE245_N_OFF_I,
)
from tests.test_mamari_i_3gram_090_076_700_i_only_scoreboard import (
    GRAM3 as CYCLE236_GRAM3,
    STANDING_I_3GRAM_090_076_700_I_ONLY as CYCLE236_CLAIM,
    STANDING_I_SITES as CYCLE236_I_SITES,
    STANDING_N_I as CYCLE236_N_I,
    STANDING_N_OFF_I as CYCLE236_N_OFF_I,
    TestMamariI3gram090076700IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    STANDING_REMAINING11_NEXT_STEMS as CYCLE256_REMAINING11_NEXT_STEMS,
    TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only_scoreboard import (
    STANDING_EXTRA_I_090_076_SITES as CYCLE287_EXTRA_I_090_076_SITES,
    STANDING_EXTRA_I_SITES as CYCLE287_EXTRA_I_SITES,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_020_scoreboard import (
    GRAM3_FORWARD,
    STANDING_G as CYCLE289_G,
    STANDING_IA12_82,
    STANDING_IA12_83,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020 as CYCLE289_CLAIM,
    STANDING_K as CYCLE289_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE289_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE289_MATCHING_SITES,
    STANDING_N_INSIDE as CYCLE289_N_INSIDE,
    STANDING_N_REMAINING_AFTER_020 as CYCLE289_N_REMAINING_AFTER_020,
    TestMamariILeftoverN4Remaining090076Forward020Scoreboard,
    leftover_n4_remaining_with_forward_020,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_SITES as CYCLE288_G_SITES,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE288_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE288_N_INSIDE,
    STANDING_N_WITH_NEXT as CYCLE288_N_WITH_NEXT,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
    leftover_n4_remaining_next_stems,
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
NEAR_MISS_090_076_700 = CYCLE236_GRAM3
NEAR_MISS_090_076_087 = CYCLE245_GRAM3
NEAR_MISS_090_076_011 = CYCLE248_GRAM3
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_090_076_071 = CYCLE195_GRAM3
NEAR_MISS_090_076 = GRAM2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_I_HITS = 4
STANDING_IA_HITS = 4
STANDING_IB_HITS = 0
STANDING_N_ON_I = 4
STANDING_N_I = 4
STANDING_I_SITES = (
    (SIDE_IA, "Ia2", 119),
    (SIDE_IA, "Ia4", 86),
    (SIDE_IA, "Ia5", 143),
    (SIDE_IA, "Ia12", 83),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_MATCHING_SITES = CYCLE289_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_COUNT = 4
STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS = CYCLE289_MATCHING_NEXT_4GRAMS
STANDING_EXTRA_I_SITES = ()
STANDING_N_EXTRA = 0
STANDING_I_PREVIOUS_4GRAMS = (
    ("591", "090", "076", "020"),
    ("076", "090", "076", "020"),
    ("090", "090", "076", "020"),
    ("008", "090", "076", "020"),
)
STANDING_I_NEXT_4GRAMS = (
    ("090", "076", "020", "010"),
    ("090", "076", "020", "010"),
    ("090", "076", "020", "010"),
    ("090", "076", "020", "010"),
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
STANDING_CLAIM = "i_3gram_090_076_020_i_only"
STANDING_I_3GRAM_090_076_020_I_ONLY = True
STANDING_RESULT = "i_3gram_090_076_020_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE195_3GRAM = False
STANDING_SAME_AS_CYCLE207_3GRAM = False
STANDING_SAME_AS_CYCLE223_2GRAM = False
STANDING_SAME_AS_CYCLE236_3GRAM = False
STANDING_SAME_AS_CYCLE245_3GRAM = False
STANDING_SAME_AS_CYCLE248_3GRAM = False
STANDING_SAME_AS_CYCLE289 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE236 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE248 = True
STANDING_090_076_700_DOES_NOT_COUNT = True
STANDING_090_076_087_DOES_NOT_COUNT = True
STANDING_090_076_011_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_090_076_WITHOUT_020_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED = True
STANDING_I_090_076_020_FORWARD_4GRAMS_NOT_LOCKED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_EXCLUDES_020 = True
STANDING_CYCLE289_K = 4
STANDING_CYCLE289_G = "020"
STANDING_CYCLE288_N_DISTINCT = 6
STANDING_IA12_83_IN_I_SITES = True


def i_3gram_090_076_020_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


def leftover_n4_remaining_020_subset(
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff leftover n=4 remaining 020 sites ⊆ I 090 076 020."""
    return set(leftover_matching).issubset(set(i_sites))


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 090 076 020 sites that are not leftover n=4 remaining 020."""
    leftover_set = set(leftover_matching)
    return tuple(site for site in i_sites if site not in leftover_set)


def leftover_extra_remaining_after_000_excludes_020(
    remaining_stems: tuple[str, ...] = CYCLE256_REMAINING11_NEXT_STEMS,
    stem: str = STANDING_CYCLE289_G,
) -> bool:
    """True iff leftover extra remaining-after-000 next stems exclude 020."""
    return stem not in remaining_stems


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


class TestI3gram090076020IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-289 leftover n=4 remaining 3-gram. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. 090 076 700 / 070 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "020"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["090", "076", "020", "090", "076", "020"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 2)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_700)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_087)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_011)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_071)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "700"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "070"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "020"]], GRAM3), 0)
        self.assertTrue(STANDING_090_076_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_087_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_011_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_020_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Measured 4/0 holds."""
        provider = MockProvider()
        self.assertTrue(i_3gram_090_076_020_i_only(1, 0))
        self.assertTrue(i_3gram_090_076_020_i_only(4, 0))
        self.assertFalse(i_3gram_090_076_020_i_only(4, 1))
        self.assertFalse(i_3gram_090_076_020_i_only(1, 1))
        self.assertFalse(i_3gram_090_076_020_i_only(0, 0))
        self.assertFalse(i_3gram_090_076_020_i_only(0, 1))
        self.assertEqual(STANDING_CLAIM, "i_3gram_090_076_020_i_only")
        self.assertTrue(STANDING_I_3GRAM_090_076_020_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(
            STANDING_I_3GRAM_090_076_020_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_fail(self):
        """Leftover n=4 remaining 020 ⊆ I sites; extra can be nonempty."""
        provider = MockProvider()
        self.assertTrue(
            leftover_n4_remaining_020_subset(
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
            leftover_n4_remaining_020_subset(
                STANDING_LEFTOVER_MATCHING_SITES + ((SIDE_IA, "Ia1", 0),),
                STANDING_I_SITES,
            )
        )
        self.assertEqual(len(extra_i_sites(planted_extra)), 1)
        dropped = STANDING_I_SITES[1:]
        self.assertFalse(
            leftover_n4_remaining_020_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                dropped,
            )
        )
        self.assertTrue(leftover_extra_remaining_after_000_excludes_020())
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_EXCLUDES_020)
        self.assertNotIn("020", CYCLE256_REMAINING11_NEXT_STEMS)
        planted_stems = CYCLE256_REMAINING11_NEXT_STEMS + ("020",)
        self.assertFalse(leftover_extra_remaining_after_000_excludes_020(planted_stems))
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_cycle289_leftover_n4_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-289 leftover n=4 remaining G, not priors."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "020"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM3[:2], GRAM2)
        self.assertEqual(GRAM3[2], CYCLE289_G)
        self.assertNotEqual(GRAM3, CYCLE236_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE245_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE248_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, GRAM2)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE223_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE236_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE245_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE248_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE236)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE248)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        self.assertLess(len(GRAM3), 8)
        for nxt4 in STANDING_I_NEXT_4GRAMS:
            self.assertTrue(is_contiguous_substring(GRAM3, nxt4))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_700))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_087))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_011))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_070))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_071))
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM3))
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_I_090_076_020_FORWARD_4GRAMS_NOT_LOCKED)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram090076020IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 remaining 3-gram 090 076 020 off-I lock."""

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
        self.next_stems = leftover_n4_remaining_next_stems(
            self.i_sides,
            CYCLE224_INSIDE_SITES,
            GRAM2,
        )
        self.leftover_matching = leftover_n4_remaining_with_forward_020(
            CYCLE224_INSIDE_SITES,
            self.next_stems,
        )
        self.extra = extra_i_sites(self.i_sites, self.leftover_matching)
        self.claim_holds = i_3gram_090_076_020_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_289_leftover_n4_not_retuned(self):
        """3-gram is the cycle-289 leftover n=4 remaining G, not a new inventory."""
        self.assertEqual(GRAM3, ("090", "076", "020"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM3[:2], GRAM2)
        self.assertEqual(GRAM3[2], "020")
        prior_289 = self.survey["i_leftover_n4_remaining_090_076_forward_020"]
        self.assertEqual(prior_289["cycle"], 289)
        self.assertEqual(tuple(prior_289["forward_3gram"]), GRAM3)
        self.assertEqual(prior_289["G"], "020")
        self.assertEqual(prior_289["K"], 4)
        self.assertEqual(prior_289["N_inside"], 13)
        self.assertEqual(prior_289["N_remaining_after_020"], 9)
        self.assertEqual(CYCLE289_G, "020")
        self.assertEqual(CYCLE289_K, 4)
        self.assertEqual(CYCLE289_N_INSIDE, 13)
        self.assertEqual(CYCLE289_N_REMAINING_AFTER_020, 9)
        self.assertTrue(CYCLE289_CLAIM)
        self.assertTrue(prior_289["i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"])
        measured_matching = [list(site) for site in CYCLE289_MATCHING_SITES]
        self.assertEqual(
            [list(site) for site in prior_289["matching_leftover_n4_remaining_sites"]],
            measured_matching,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE289_MATCHING_NEXT_4GRAMS],
            prior_289["matching_next_4grams"],
        )
        self.assertEqual(self.leftover_matching, CYCLE289_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE288_G_SITES)
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_020010_COVERED)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE289_K)
        self.assertEqual(STANDING_CYCLE289_K, 4)
        self.assertEqual(STANDING_CYCLE289_G, "020")
        if len(self.leftover_matching) != 4 or CYCLE289_G != "020":
            self.fail("nested cycle 289 leftover n=4 remaining G=020 K=4 drifted")
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["N_inside"], 13)
        self.assertEqual(prior_288["N_with_next"], 13)
        self.assertEqual(prior_288["N_distinct_next_stems"], 6)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertTrue(prior_288["g_uniquely_most_frequent"])
        self.assertFalse(prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        prior_256 = self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]
        self.assertEqual(prior_256["cycle"], 256)
        remaining_stems = tuple(prior_256["remaining_after_000_next_stems"])
        self.assertEqual(remaining_stems, CYCLE256_REMAINING11_NEXT_STEMS)
        self.assertNotIn("020", remaining_stems)
        self.assertTrue(leftover_extra_remaining_after_000_excludes_020(remaining_stems))
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_EXCLUDES_020)
        prior_236 = self.survey["i_3gram_090_076_700_i_only"]
        self.assertEqual(prior_236["cycle"], 236)
        self.assertEqual(prior_236["N_I"], 2)
        self.assertEqual(prior_236["N_off_I"], 0)
        self.assertTrue(prior_236["i_3gram_090_076_700_i_only"])
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_I"], 69)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(prior_224["i_090_076_all_inside_leftover_n4_remaining_family"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, CYCLE236_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_I_090_076_020_FORWARD_4GRAMS_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_four_on_ia_and_equal_leftover_n4_remaining_020(self):
        """3-gram is 4 on Ia; Ib 0. Those 4 equal leftover n=4 remaining 020."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 4)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 4)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 4)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM3, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM3), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE289_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE288_G_SITES)
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_020010_COVERED)
        self.assertEqual(self.leftover_matching, STANDING_I_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 4)
        self.assertTrue(
            leftover_n4_remaining_020_subset(
                self.leftover_matching,
                self.i_sites,
            )
        )
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        if self.i_hits != 4:
            self.fail("measured N_I drifted from 4")
        if self.leftover_matching != self.i_sites:
            self.fail("leftover n=4 remaining 020 set drifted from I 090 076 020")
        if self.extra:
            self.fail("extra I 090 076 020 sites appeared; leftover extra has no 020")
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
            self.assertIn((side, line, index), CYCLE224_INSIDE_SITES)
            self.assertIn((side, line, index), CYCLE289_MATCHING_SITES)
            self.assertIn((side, line, index), CYCLE288_G_SITES)
            self.assertIn((side, line, index), STANDING_LEFTOVER_020010_COVERED)
            self.assertNotIn((side, line, index), STANDING_LEFTOVER_SITES)
            self.assertNotIn((side, line, index), CYCLE236_I_SITES)
            self.assertNotIn((side, line, index), CYCLE245_I_SITES)
            self.assertNotIn((side, line, index), CYCLE248_I_SITES)
            self.assertNotIn((side, line, index), CYCLE207_I_SITES)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia2", 119),
                (SIDE_IA, "Ia4", 86),
                (SIDE_IA, "Ia5", 143),
                (SIDE_IA, "Ia12", 83),
            ),
        )
        self.assertEqual(STANDING_I_NEXT_4GRAMS, CYCLE289_MATCHING_NEXT_4GRAMS)
        self.assertEqual(
            STANDING_I_NEXT_4GRAMS,
            (
                ("090", "076", "020", "010"),
                ("090", "076", "020", "010"),
                ("090", "076", "020", "010"),
                ("090", "076", "020", "010"),
            ),
        )
        self.assertIn(STANDING_IA12_83, STANDING_I_SITES)
        self.assertTrue(STANDING_IA12_83_IN_I_SITES)
        self.assertEqual(STANDING_IA12_83, (SIDE_IA, "Ia12", 83))
        self.assertEqual(STANDING_IA12_82, (SIDE_IA, "Ia12", 82))
        self.assertEqual(CYCLE287_EXTRA_I_SITES[1], STANDING_IA12_82)
        self.assertEqual(CYCLE287_EXTRA_I_090_076_SITES[1], STANDING_IA12_83)
        stems_008 = line_stems_for_site(self.i_sides, STANDING_IA12_82)
        self.assertEqual(tuple(stems_008[82:85]), ("008", "090", "076"))
        stems_090 = line_stems_for_site(self.i_sides, STANDING_IA12_83)
        self.assertEqual(tuple(stems_090[83:86]), GRAM3)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        self.assertEqual(CYCLE223_N_I, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        for site in CYCLE224_INSIDE_SITES:
            if site not in STANDING_I_SITES:
                stems = line_stems_for_site(self.i_sides, site)
                index = site[2]
                self.assertEqual(tuple(stems[index : index + 2]), GRAM2)
                if index + 3 <= len(stems):
                    self.assertNotEqual(tuple(stems[index : index + 3]), GRAM3)
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_I_SITES)
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + 2]), GRAM2)
            if index + 3 <= len(stems):
                self.assertNotEqual(tuple(stems[index : index + 3]), GRAM3)
        for site in CYCLE223_I_SITES:
            if site not in STANDING_I_SITES:
                stems = line_stems_for_site(self.i_sides, site)
                index = site[2]
                self.assertEqual(tuple(stems[index : index + 2]), GRAM2)
                if index + 3 <= len(stems):
                    self.assertNotEqual(tuple(stems[index : index + 3]), GRAM3)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_I_090_076_020_FORWARD_4GRAMS_NOT_LOCKED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_zero_off_i_and_i_only(self):
        """3-gram is 0 on A–H and J–V. Ia has exactly 4. T 090 076 is not this 3-gram."""
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
                self.assertEqual(count, 4)
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
            i_3gram_090_076_020_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_3GRAM_090_076_020_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_090_076_020_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_3GRAM_090_076_020_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_3gram_090_076_020_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE223_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE236_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE245_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE248_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE236)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE248)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE)
        if self.off_i_hits != 0:
            self.fail("measured N_off_I drifted from 0")
        if self.i_hits != STANDING_N_I:
            self.fail("measured N_I drifted from the locked count")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_289_288_256_236_224_223_and_207_still_compute(self):
        """Cycle 289 K=4/G=020, 288 N_distinct=6 unique-max, 256 excludes 020, 236 2/0, 224 13/56, 223 69/3, 207 8/1 stay."""
        prior_289 = TestMamariILeftoverN4Remaining090076Forward020Scoreboard()
        prior_289.setUp()
        prior_289.test_counts_4_of_13_and_hypothesis_k_4_holds()
        prior_289.test_survey_matches_computed_lock()
        self.assertEqual(prior_289.k, 4)
        self.assertEqual(CYCLE289_G, "020")
        self.assertEqual(prior_289.n_inside, 13)
        self.assertEqual(prior_289.matching, CYCLE289_MATCHING_SITES)
        self.assertEqual(prior_289.matching_next_4grams, CYCLE289_MATCHING_NEXT_4GRAMS)
        for nxt4 in prior_289.matching_next_4grams:
            self.assertEqual(nxt4, ("090", "076", "020", "010"))
        self.assertTrue(prior_289.claim_holds)
        self.assertTrue(CYCLE289_CLAIM)
        if prior_289.k != 4 or CYCLE289_G != "020" or prior_289.n_inside != 13:
            self.fail("nested cycle 289 leftover n=4 remaining G=020 K=4 drifted")
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.n_inside, 13)
        self.assertEqual(prior_288.n_with_next, 13)
        self.assertEqual(prior_288.n_distinct, 6)
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_INSIDE, 13)
        self.assertEqual(CYCLE288_N_WITH_NEXT, 13)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        if (
            prior_288.n_inside != 13
            or prior_288.n_with_next != 13
            or prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or not prior_288.unique_max
        ):
            self.fail("nested cycle 288 leftover n=4 remaining 13/13 N_distinct=6 G=020 K=4 unique-max drifted")
        prior_256 = TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard()
        prior_256.setUp()
        prior_256.test_counts_19_remaining11_all_hapax_g_755_k_1_and_hypothesis_loses()
        prior_256.test_survey_matches_computed_lock()
        self.assertEqual(prior_256.remaining11_stems, CYCLE256_REMAINING11_NEXT_STEMS)
        self.assertNotIn("020", prior_256.remaining11_stems)
        self.assertTrue(
            leftover_extra_remaining_after_000_excludes_020(prior_256.remaining11_stems)
        )
        if "020" in prior_256.remaining11_stems:
            self.fail("nested cycle 256 leftover extra remaining-after-000 next stems include 020")
        prior_236 = TestMamariI3gram090076700IOnlyScoreboard()
        prior_236.setUp()
        prior_236.test_i_hits_are_two_on_ia_and_equal_leftover_extra_700()
        prior_236.test_3gram_is_zero_off_i_and_i_only()
        prior_236.test_survey_matches_computed_lock()
        self.assertEqual(prior_236.i_hits, CYCLE236_N_I)
        self.assertEqual(prior_236.i_hits, 2)
        self.assertEqual(prior_236.off_i_hits, CYCLE236_N_OFF_I)
        self.assertEqual(prior_236.off_i_hits, 0)
        self.assertEqual(prior_236.i_sites, CYCLE236_I_SITES)
        self.assertTrue(prior_236.claim_holds)
        self.assertTrue(CYCLE236_CLAIM)
        if prior_236.i_hits != 2 or prior_236.off_i_hits != 0:
            self.fail("nested cycle 236 090 076 700 I-only 2/0 drifted")
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
        if prior_224.n_inside != 13 or prior_224.n_leftover != 56:
            self.fail("nested cycle 224 13/56 drifted")
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
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE245_N_I, 5)
        self.assertEqual(CYCLE245_N_OFF_I, 0)
        self.assertEqual(CYCLE245_N_EXTRA, 3)
        self.assertTrue(CYCLE245_CLAIM)
        self.assertEqual(CYCLE248_N_I, 4)
        self.assertEqual(CYCLE248_N_OFF_I, 0)
        self.assertEqual(CYCLE248_N_EXTRA, 2)
        self.assertTrue(CYCLE248_CLAIM)
        self.assertEqual(STANDING_CYCLE288_N_DISTINCT, 6)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_REMAINING_AFTER_020_NEXT_STEMS_NOT_LOCKED)
        self.assertTrue(STANDING_I_090_076_020_FORWARD_4GRAMS_NOT_LOCKED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-290 3-gram I-only lock."""
        lock = self.survey["i_3gram_090_076_020_i_only"]
        self.assertEqual(lock["cycle"], 290)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 4)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_remaining_020_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(
            lock["leftover_n4_remaining_020_count"],
            STANDING_LEFTOVER_MATCHING_COUNT,
        )
        self.assertEqual(lock["leftover_n4_remaining_020_count"], 4)
        self.assertTrue(lock["leftover_n4_remaining_020_subset_of_i_sites"])
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
        self.assertEqual(lock["nested_cycle289_G"], STANDING_CYCLE289_G)
        self.assertEqual(lock["nested_cycle289_G"], "020")
        self.assertEqual(lock["nested_cycle289_K"], STANDING_CYCLE289_K)
        self.assertEqual(lock["nested_cycle289_K"], 4)
        self.assertEqual(lock["nested_cycle289_N_inside"], 13)
        self.assertEqual(lock["nested_cycle289_N_remaining_after_020"], 9)
        self.assertEqual(lock["nested_cycle288_N_inside"], 13)
        self.assertEqual(lock["nested_cycle288_N_with_next"], 13)
        self.assertEqual(lock["nested_cycle288_N_distinct_next_stems"], STANDING_CYCLE288_N_DISTINCT)
        self.assertEqual(lock["nested_cycle288_N_distinct_next_stems"], 6)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertTrue(lock["leftover_extra_remaining_after_000_excludes_020"])
        self.assertEqual(
            lock["leftover_extra_remaining_after_000_excludes_020"],
            STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_EXCLUDES_020,
        )
        self.assertEqual(tuple(lock["nested_cycle256_remaining_after_000_next_stems"]), CYCLE256_REMAINING11_NEXT_STEMS)
        self.assertNotIn("020", lock["nested_cycle256_remaining_after_000_next_stems"])
        self.assertEqual(lock["nested_cycle236_N_I"], 2)
        self.assertEqual(lock["nested_cycle236_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertTrue(lock["ia12_83_in_i_sites"])
        self.assertEqual(lock["ia12_83_in_i_sites"], STANDING_IA12_83_IN_I_SITES)
        self.assertEqual(tuple(lock["ia12_83"]), STANDING_IA12_83)
        self.assertEqual(tuple(lock["ia12_82"]), STANDING_IA12_82)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_3gram_090_076_020_i_only"])
        self.assertEqual(
            lock["i_3gram_090_076_020_i_only"],
            STANDING_I_3GRAM_090_076_020_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle195_3gram"])
        self.assertFalse(lock["same_as_cycle207_3gram"])
        self.assertFalse(lock["same_as_cycle223_2gram"])
        self.assertFalse(lock["same_as_cycle236_3gram"])
        self.assertFalse(lock["same_as_cycle245_3gram"])
        self.assertFalse(lock["same_as_cycle248_3gram"])
        self.assertFalse(lock["same_as_cycle289"])
        self.assertTrue(lock["same_claim_shape_as_cycle207"])
        self.assertTrue(lock["same_claim_shape_as_cycle236"])
        self.assertTrue(lock["same_claim_shape_as_cycle245"])
        self.assertTrue(lock["same_claim_shape_as_cycle248"])
        self.assertTrue(lock["090_076_700_does_not_count"])
        self.assertTrue(lock["090_076_087_does_not_count"])
        self.assertTrue(lock["090_076_011_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["090_076_without_020_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_n4_remaining_remaining_after_020_next_stems_not_locked"])
        self.assertTrue(lock["i_090_076_020_forward_4grams_not_locked"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_020_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_700_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_087_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_011_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"]["cycle"],
            289,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"][
                "i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"]["G"],
            "020",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"]["K"],
            4,
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"], 288)
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"][
                "i_leftover_n4_remaining_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["N_distinct_next_stems"], 6)
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["G"], "020")
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["K"], 4)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["g_uniquely_most_frequent"]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]["cycle"],
            256,
        )
        self.assertNotIn(
            "020",
            self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"][
                "remaining_after_000_next_stems"
            ],
        )
        self.assertEqual(self.survey["i_3gram_090_076_700_i_only"]["cycle"], 236)
        self.assertTrue(self.survey["i_3gram_090_076_700_i_only"]["i_3gram_090_076_700_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_700_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_090_076_700_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["cycle"], 245)
        self.assertTrue(self.survey["i_3gram_090_076_087_i_only"]["i_3gram_090_076_087_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["N_extra"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["cycle"], 248)
        self.assertTrue(self.survey["i_3gram_090_076_011_i_only"]["i_3gram_090_076_011_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_I"], 4)
        self.assertEqual(self.survey["i_3gram_090_076_011_i_only"]["N_extra"], 2)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"], 13)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
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


class TestMamariI3gram090076020IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 290 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
