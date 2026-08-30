"""I's cycle-253 leftover extra remaining-after-005 3-gram 090 076 000 off-I lock.

Cycle 254 text-search lock. Uses already-vendored A–V and the
cycle-253 leftover extra remaining-after-005 next stem G=000
(K=2 of N_remaining10=21). Does not retune that leftover extra
remaining-after-005 000 lock, leftover extra remaining-after-011
005, leftover extra remaining-after-087 011, leftover extra
remaining-after-280 087, leftover extra remaining-after-530 280,
leftover extra remaining-after-700 530, leftover extra
remaining-after-001 700, leftover extra remaining-after-001
unique-max (cycle 234 lost), leftover extra remaining-after-013
001, leftover extra remaining-after-071 013, leftover extra
remaining 071, leftover extra forward 070, leftover extra sites,
the leftover n=4 set, or the already-closed leftover remaining
family. Does not vendor a new tablet. Does not scrape X. W has
no Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not
redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 251 (090 076 005 was I-only 2/0 extra
I=0), cycle 248 (090 076 011 was I-only 4/0 extra I=2), cycle
245 (090 076 087 was I-only 5/0 extra I=3), cycle 242
(090 076 280 was I-only 2/0), cycle 239 (090 076 530 was
I-only 2/0), cycle 236 (090 076 700 was I-only 2/0), cycle 232
(090 076 001 was I-only 3/0), cycle 229 (090 076 013 was
I-only 5/0), cycle 195 (090 076 071 was I-only 6/0), and cycle
171 (076 071 was I-only 43/0). Cycle 207 lost: 090 076 070 is
not I-only (8/1 on T). Cycle 223 lost: 090 076 is not I-only
(69/3 on T). Cycle 219 lost: I 090 076 070 forward 4-grams
7/8; 090 076 070 000 leaks 1/1 on T. This cycle is the new
leftover extra remaining-after-005 3-gram 090 076 000 only.
090 076 005, 090 076 011, 090 076 087, 090 076 280,
090 076 530, 090 076 700, 090 076 001, 090 076 013,
090 076 070, 090 076 071, and 090 076 without 000 do not
count as this 3-gram. Cycle 219's T leak 090 076 070 000 is a
4-gram, not this 3-gram. Cycle 220 999 090 076 070 000 is a
5-gram, not this 3-gram. Ia14[140] 090 076 070 000 is leftover
extra forward 070, not contiguous 090 076 000. Do not retune
leftover n=4, 076-cells, or any detector. Do not lock leftover
extra remaining after 000 this cycle. Off-I T sites of 090 076
are this cycle only as off-I of 090 076 000 if they match.
Do not assume the I-only result.

Locks exact consecutive hits of 090 076 000 on tablet I and
on every other vendored tablet A–H and J–V. Include line-final
090 076 000 (no next token) as a 3-gram site. Claim that can
lose: i_3gram_090_076_000_i_only (I hits ≥ 1 and off-I hits
== 0). True only if N_off_I == 0. Measured: Ia is exactly 2
at Ia2[174]/Ia10[141]; Ib unpublished 0; every other vendored
tablet is exact-0. Those 2 equal the cycle-253 leftover extra
remaining-after-005 000 cluster (next 4-grams None /
090 076 000 076). Extra I sites not in leftover extra
remaining-after-005 = 0 (leftover of leftover would be a later
cycle if any appeared). Ia2[174] has next token 000 and no
following token on that line. Nested leftover extra
remaining-after-005 K=2 / G=000 N_remaining10=21, cycle 252
2/2 hapax, cycle 251 2/0 extra I=0, cycle 250 K=2 / G=005,
cycle 219 7/8 lose on T 000, and cycle 223 69/3 stay.
The claim is true. Not an n≥8 island. Not the cycle-103 I
5-gram.

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
from tests.test_mamari_i_090_076_005_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_005_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE252_CLAIM,
    STANDING_N_I_ONLY as CYCLE252_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE252_N_NOT_I_ONLY,
    TestMamariI090076005Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_CLAIM,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
    TestMamariI090076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
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
from tests.test_mamari_i_3gram_090_076_001_i_only_scoreboard import (
    GRAM3 as CYCLE232_GRAM3,
    STANDING_I_3GRAM_090_076_001_I_ONLY as CYCLE232_CLAIM,
    STANDING_I_SITES as CYCLE232_I_SITES,
    STANDING_N_I as CYCLE232_N_I,
    STANDING_N_OFF_I as CYCLE232_N_OFF_I,
)
from tests.test_mamari_i_3gram_090_076_005_i_only_scoreboard import (
    GRAM3 as CYCLE251_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE251_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_005_I_ONLY as CYCLE251_CLAIM,
    STANDING_I_SITES as CYCLE251_I_SITES,
    STANDING_N_EXTRA as CYCLE251_N_EXTRA,
    STANDING_N_I as CYCLE251_N_I,
    STANDING_N_OFF_I as CYCLE251_N_OFF_I,
    TestMamariI3gram090076005IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_011_i_only_scoreboard import (
    GRAM3 as CYCLE248_GRAM3,
    STANDING_I_3GRAM_090_076_011_I_ONLY as CYCLE248_CLAIM,
    STANDING_I_SITES as CYCLE248_I_SITES,
    STANDING_N_EXTRA as CYCLE248_N_EXTRA,
    STANDING_N_I as CYCLE248_N_I,
    STANDING_N_OFF_I as CYCLE248_N_OFF_I,
)
from tests.test_mamari_i_3gram_090_076_013_i_only_scoreboard import (
    GRAM3 as CYCLE229_GRAM3,
    STANDING_I_SITES as CYCLE229_I_SITES,
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
    STANDING_I_SITES as CYCLE195_I_SITES,
    STANDING_N_I as CYCLE195_N_I,
    STANDING_N_OFF_I as CYCLE195_N_OFF_I,
)
from tests.test_mamari_i_3gram_090_076_087_i_only_scoreboard import (
    GRAM3 as CYCLE245_GRAM3,
    STANDING_I_SITES as CYCLE245_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_280_i_only_scoreboard import (
    GRAM3 as CYCLE242_GRAM3,
    STANDING_I_SITES as CYCLE242_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_530_i_only_scoreboard import (
    GRAM3 as CYCLE239_GRAM3,
    STANDING_I_SITES as CYCLE239_I_SITES,
)
from tests.test_mamari_i_3gram_090_076_700_i_only_scoreboard import (
    GRAM3 as CYCLE236_GRAM3,
    STANDING_I_SITES as CYCLE236_I_SITES,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    GRAM5 as CYCLE220_GRAM5,
    STANDING_I_5GRAM_999_090_076_070_000_I_ONLY as CYCLE220_CLAIM,
    STANDING_N_I as CYCLE220_N_I,
    STANDING_N_OFF_I as CYCLE220_N_OFF_I,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_070_scoreboard import (
    STANDING_MATCHING_SITES as CYCLE226_MATCHING_SITES,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_IA2_174,
    STANDING_IA2_174_NEXT_STEM,
    leftover_extra_next_stems,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_next_stem_scoreboard import (
    STANDING_G as CYCLE234_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE234_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G as CYCLE234_CLAIM,
    STANDING_K as CYCLE234_K,
    STANDING_N_REMAINING4 as CYCLE234_N_REMAINING4,
    STANDING_N_TIED_AT_K as CYCLE234_N_TIED_AT_K,
    STANDING_TIED_STEMS as CYCLE234_TIED_STEMS,
    leftover_extra_remaining_after_001,
    TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_005_fwd000_scoreboard import (
    GRAM3_FORWARD,
    STANDING_G as CYCLE253_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000 as CYCLE253_CLAIM,
    STANDING_IA14_140,
    STANDING_IA14_140_NEXT_4GRAM,
    STANDING_K as CYCLE253_K,
    STANDING_MATCHING_NEXT_4GRAMS as CYCLE253_MATCHING_NEXT_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE253_MATCHING_SITES,
    STANDING_N_REMAINING10 as CYCLE253_N_REMAINING10,
    leftover_extra_remaining_after_005,
    leftover_extra_remaining_after_005_with_000,
    TestMamariILeftoverExtra090076RemainingAfter005Fwd000Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_011_fwd005_scoreboard import (
    STANDING_G as CYCLE250_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_011_EXACTLY_2_SHARE_005 as CYCLE250_CLAIM,
    STANDING_K as CYCLE250_K,
    STANDING_MATCHING_SITES as CYCLE250_MATCHING_SITES,
    STANDING_N_REMAINING9 as CYCLE250_N_REMAINING9,
    leftover_extra_remaining_after_011,
    leftover_extra_remaining_after_011_with_005,
    leftover_extra_remaining_after_011_without_005,
    TestMamariILeftoverExtra090076RemainingAfter011Fwd005Scoreboard,
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
NEAR_MISS_090_076_005 = CYCLE251_GRAM3
NEAR_MISS_090_076_011 = CYCLE248_GRAM3
NEAR_MISS_090_076_087 = CYCLE245_GRAM3
NEAR_MISS_090_076_280 = CYCLE242_GRAM3
NEAR_MISS_090_076_530 = CYCLE239_GRAM3
NEAR_MISS_090_076_700 = CYCLE236_GRAM3
NEAR_MISS_090_076_001 = CYCLE232_GRAM3
NEAR_MISS_090_076_013 = CYCLE229_GRAM3
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_090_076_071 = CYCLE195_GRAM3
NEAR_MISS_090_076 = GRAM2
NEAR_MISS_090_076_070_000 = CYCLE219_LEAK_4GRAM
NEAR_MISS_999_090_076_070_000 = CYCLE220_GRAM5
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_I_HITS = 2
STANDING_IA_HITS = 2
STANDING_IB_HITS = 0
STANDING_N_ON_I = 2
STANDING_N_I = 2
STANDING_I_SITES = (
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia10", 141),
)
STANDING_IB_SITES = ()
STANDING_LEFTOVER_MATCHING_SITES = CYCLE253_MATCHING_SITES
STANDING_LEFTOVER_MATCHING_COUNT = 2
STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS = CYCLE253_MATCHING_NEXT_4GRAMS
STANDING_EXTRA_I_SITES = ()
STANDING_N_EXTRA = 0
STANDING_I_PREVIOUS_4GRAMS = (
    ("009", "090", "076", "000"),
    ("205", "090", "076", "000"),
)
STANDING_I_NEXT_4GRAMS = (
    None,
    ("090", "076", "000", "076"),
)
STANDING_IA2_174_LINE_FINAL = True
STANDING_IA2_174_NEXT_TOKEN = "000"
STANDING_IA2_174_HAS_FOLLOWING_TOKEN = False
STANDING_IA2_174_HAS_NO_NEXT_4GRAM = True
STANDING_IA14_140_IS_NOT_090_076_000 = True
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
STANDING_CLAIM = "i_3gram_090_076_000_i_only"
STANDING_I_3GRAM_090_076_000_I_ONLY = True
STANDING_RESULT = "i_3gram_090_076_000_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE195_3GRAM = False
STANDING_SAME_AS_CYCLE207_3GRAM = False
STANDING_SAME_AS_CYCLE219_4GRAM = False
STANDING_SAME_AS_CYCLE220_5GRAM = False
STANDING_SAME_AS_CYCLE223_2GRAM = False
STANDING_SAME_AS_CYCLE229_3GRAM = False
STANDING_SAME_AS_CYCLE232_3GRAM = False
STANDING_SAME_AS_CYCLE236_3GRAM = False
STANDING_SAME_AS_CYCLE239_3GRAM = False
STANDING_SAME_AS_CYCLE242_3GRAM = False
STANDING_SAME_AS_CYCLE245_3GRAM = False
STANDING_SAME_AS_CYCLE248_3GRAM = False
STANDING_SAME_AS_CYCLE251_3GRAM = False
STANDING_SAME_AS_CYCLE253 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE195 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE229 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE232 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE236 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE239 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE242 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE248 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE251 = True
STANDING_090_076_005_DOES_NOT_COUNT = True
STANDING_090_076_011_DOES_NOT_COUNT = True
STANDING_090_076_087_DOES_NOT_COUNT = True
STANDING_090_076_280_DOES_NOT_COUNT = True
STANDING_090_076_530_DOES_NOT_COUNT = True
STANDING_090_076_700_DOES_NOT_COUNT = True
STANDING_090_076_001_DOES_NOT_COUNT = True
STANDING_090_076_013_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_090_076_WITHOUT_000_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_090_076_070_000_DOES_NOT_COUNT = True
STANDING_999_090_076_070_000_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_THIS_CYCLE_ONLY_IF_000 = True
STANDING_CYCLE253_K = 2
STANDING_CYCLE253_G = "000"
STANDING_CYCLE253_N_REMAINING10 = 21


def i_3gram_090_076_000_i_only(
    i_hits: int,
    off_i_hits: int,
) -> bool:
    """True iff I hits ≥ 1 and off-I hits == 0."""
    return i_hits >= 1 and off_i_hits == 0


def leftover_extra_remaining_after_005_000_subset(
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff leftover extra remaining-after-005 000 sites ⊆ I 090 076 000."""
    return set(leftover_matching).issubset(set(i_sites))


def extra_i_sites(
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    leftover_matching: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_MATCHING_SITES,
) -> tuple[tuple[str, str, int], ...]:
    """I 090 076 000 sites that are not leftover extra remaining-after-005 000."""
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


class TestI3gram090076000IOnlyHelpers(unittest.TestCase):
    """Helpers on cycle-253 leftover extra remaining-after-005 3-gram. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. 090 076 070 000 is not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "000"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        adjacent = [list(GRAM3), list(GRAM3)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM3), 2)
        overlap = [["090", "076", "000", "090", "076", "000"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM3), 2)
        gapped = [list(GRAM3[:2]) + ["006"] + list(GRAM3[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM3), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_005)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_011)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_087)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_280)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_530)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_700)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_001)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_013)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_071)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070_000)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_070_000)], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "070"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "070", "000"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["076", "000"]], GRAM3), 0)
        self.assertEqual(ngram_hit_count([["090", "076", "000"]], GRAM3), 1)
        self.assertTrue(STANDING_090_076_005_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_011_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_087_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_280_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_530_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_700_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_001_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_013_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_WITHOUT_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_070_000_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_1_and_zero_off_i(self):
        """Boolean is True only when I ≥ 1 and off-I is 0. Measured 2/0 holds."""
        provider = MockProvider()
        self.assertTrue(i_3gram_090_076_000_i_only(1, 0))
        self.assertTrue(i_3gram_090_076_000_i_only(2, 0))
        self.assertFalse(i_3gram_090_076_000_i_only(2, 1))
        self.assertFalse(i_3gram_090_076_000_i_only(1, 1))
        self.assertFalse(i_3gram_090_076_000_i_only(0, 0))
        self.assertFalse(i_3gram_090_076_000_i_only(0, 1))
        self.assertEqual(STANDING_CLAIM, "i_3gram_090_076_000_i_only")
        self.assertTrue(STANDING_I_3GRAM_090_076_000_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(
            STANDING_I_3GRAM_090_076_000_I_ONLY,
            HYPOTHESIS_I_ONLY,
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_fail(self):
        """Leftover extra remaining-after-005 000 ⊆ I sites; extra can be nonempty."""
        provider = MockProvider()
        self.assertTrue(
            leftover_extra_remaining_after_005_000_subset(
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
            leftover_extra_remaining_after_005_000_subset(
                STANDING_LEFTOVER_MATCHING_SITES + ((SIDE_IA, "Ia1", 0),),
                STANDING_I_SITES,
            )
        )
        self.assertEqual(len(extra_i_sites(planted_extra)), 1)
        dropped = STANDING_I_SITES[1:]
        self.assertFalse(
            leftover_extra_remaining_after_005_000_subset(
                STANDING_LEFTOVER_MATCHING_SITES,
                dropped,
            )
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_cycle253_leftover_not_the_cycle_103_5gram(self):
        """3-gram is the cycle-253 leftover extra remaining-after-005 G, not priors."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "000"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM3[:2], GRAM2)
        self.assertEqual(GRAM3[2], CYCLE253_G)
        self.assertNotEqual(GRAM3, CYCLE251_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE248_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE245_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE242_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE239_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE236_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE232_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE229_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE207_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, GRAM2)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, NEAR_MISS_090_076_070_000)
        self.assertNotEqual(GRAM3, NEAR_MISS_999_090_076_070_000)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(CYCLE220_GRAM5, ("999", "090", "076", "070", "000"))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_070_000))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_999_090_076_070_000))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219_4GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE220_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE223_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE229_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE232_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE236_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE239_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE242_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE245_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE248_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE251_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE253)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE195)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE229)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE232)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE236)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE239)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE242)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE248)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE251)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        self.assertLess(len(GRAM3), 8)
        self.assertIsNone(STANDING_I_NEXT_4GRAMS[0])
        self.assertTrue(is_contiguous_substring(GRAM3, STANDING_I_NEXT_4GRAMS[1]))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_005))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_011))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_087))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_280))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_530))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_700))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_001))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_013))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_070))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_090_076_071))
        self.assertTrue(is_contiguous_substring(GRAM2, GRAM3))
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram090076000IOnlyScoreboard(unittest.TestCase):
    """Cited-fixture leftover extra remaining-after-005 3-gram 090 076 000 off-I lock."""

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
        self.remaining4 = leftover_extra_remaining_after_001(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.remaining9 = leftover_extra_remaining_after_011(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.share_005 = leftover_extra_remaining_after_011_with_005(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.remaining10 = leftover_extra_remaining_after_005(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.leftover_matching = leftover_extra_remaining_after_005_with_000(
            STANDING_LEFTOVER_SITES,
            self.next_stems,
        )
        self.extra = extra_i_sites(self.i_sites, self.leftover_matching)
        self.claim_holds = i_3gram_090_076_000_i_only(
            self.i_hits,
            self.off_i_hits,
        )

    def test_tokens_are_cycle_253_leftover_not_retuned(self):
        """3-gram is the cycle-253 leftover extra remaining-after-005 G, not a new inventory."""
        self.assertEqual(GRAM3, ("090", "076", "000"))
        self.assertEqual(GRAM3, GRAM3_FORWARD)
        self.assertEqual(GRAM3[:2], GRAM2)
        self.assertEqual(GRAM3[2], "000")
        prior_253 = self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]
        self.assertEqual(prior_253["cycle"], 253)
        self.assertEqual(tuple(prior_253["forward_3gram"]), GRAM3)
        self.assertEqual(prior_253["G"], "000")
        self.assertEqual(prior_253["K"], 2)
        self.assertEqual(prior_253["N_remaining10"], 21)
        self.assertEqual(CYCLE253_G, "000")
        self.assertEqual(CYCLE253_K, 2)
        self.assertEqual(CYCLE253_N_REMAINING10, 21)
        self.assertTrue(CYCLE253_CLAIM)
        self.assertTrue(prior_253["i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"])
        measured_matching = [list(site) for site in CYCLE253_MATCHING_SITES]
        self.assertEqual(
            [list(site) for site in prior_253["matching_leftover_extra_remaining_after_005_sites"]],
            measured_matching,
        )
        self.assertEqual(
            [
                None if gram is None else list(gram)
                for gram in CYCLE253_MATCHING_NEXT_4GRAMS
            ],
            prior_253["matching_next_4grams"],
        )
        self.assertEqual(self.leftover_matching, CYCLE253_MATCHING_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_CYCLE253_K)
        self.assertEqual(STANDING_CYCLE253_K, 2)
        self.assertEqual(STANDING_CYCLE253_G, "000")
        self.assertEqual(STANDING_CYCLE253_N_REMAINING10, 21)
        self.assertEqual(len(self.remaining10), 21)
        self.assertEqual(len(self.remaining9), 23)
        self.assertEqual(len(self.share_005), 2)
        self.assertEqual(len(self.remaining4), 33)
        self.assertEqual(
            self.remaining10,
            leftover_extra_remaining_after_011_without_005(
                STANDING_LEFTOVER_SITES,
                self.next_stems,
            ),
        )
        if (
            len(self.leftover_matching) != 2
            or CYCLE253_G != "000"
            or len(self.remaining10) != 21
        ):
            self.fail("nested cycle 253 leftover extra remaining-after-005 G=000 K=2 drifted")
        prior_252 = self.survey["i_090_076_005_forward_4grams_i_only"]
        self.assertEqual(prior_252["cycle"], 252)
        self.assertEqual(prior_252["N_i_only"], 2)
        self.assertEqual(prior_252["N_not_i_only"], 0)
        self.assertTrue(prior_252["i_090_076_005_forward_4grams_all_i_only"])
        prior_251 = self.survey["i_3gram_090_076_005_i_only"]
        self.assertEqual(prior_251["cycle"], 251)
        self.assertEqual(prior_251["N_I"], 2)
        self.assertEqual(prior_251["N_off_I"], 0)
        self.assertEqual(prior_251["N_extra"], 0)
        self.assertTrue(prior_251["i_3gram_090_076_005_i_only"])
        prior_250 = self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"]
        self.assertEqual(prior_250["cycle"], 250)
        self.assertEqual(prior_250["G"], "005")
        self.assertEqual(prior_250["K"], 2)
        self.assertEqual(prior_250["N_remaining9"], 23)
        self.assertTrue(prior_250["i_leftover_extra_090_076_remaining_after_011_exactly_2_share_005"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_219 = self.survey["i_090_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_219["cycle"], 219)
        self.assertEqual(prior_219["N_i_only"], 7)
        self.assertEqual(prior_219["N_not_i_only"], 1)
        self.assertFalse(prior_219["i_090_076_070_forward_4grams_i_only"])
        self.assertEqual(tuple(prior_219["off_i_forward_4gram"]), CYCLE219_LEAK_4GRAM)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, CYCLE251_GRAM3)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_THIS_CYCLE_ONLY_IF_000)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_i_hits_are_two_on_ia_and_equal_leftover_extra_000(self):
        """3-gram is 2 on Ia; Ib 0. Those 2 equal leftover extra remaining-after-005 000."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(STANDING_I_SITES), 2)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 2)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(STANDING_I_HITS, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 2)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(nge4_sites(GRAM3, self.i_sides), STANDING_I_SITES)
        self.assertEqual(ngram_hit_count(self.i_sides[SIDE_IA], GRAM3), STANDING_I_HITS)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.leftover_matching, STANDING_LEFTOVER_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, CYCLE253_MATCHING_SITES)
        self.assertEqual(self.leftover_matching, STANDING_I_SITES)
        self.assertEqual(len(self.leftover_matching), STANDING_LEFTOVER_MATCHING_COUNT)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_COUNT, 2)
        self.assertTrue(
            leftover_extra_remaining_after_005_000_subset(
                self.leftover_matching,
                self.i_sites,
            )
        )
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.extra), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 0)
        if self.i_hits != 2:
            self.fail("measured N_I drifted from 2")
        if self.leftover_matching != CYCLE253_MATCHING_SITES:
            self.fail("leftover extra remaining-after-005 000 set drifted")
        if self.leftover_matching != self.i_sites:
            self.fail("leftover extra remaining-after-005 000 set drifted from I 090 076 000")
        if not leftover_extra_remaining_after_005_000_subset(
            self.leftover_matching,
            self.i_sites,
        ):
            self.fail("leftover extra remaining-after-005 000 not subset of I 090 076 000")
        if self.extra:
            self.fail("extra I 090 076 000 leftover-of-leftover sites appeared")
        for (side, line, index), prev4, nxt4 in zip(
            STANDING_I_SITES,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            strict=True,
        ):
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertEqual(tuple(stems[index - 1 : index + STANDING_N3]), prev4)
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), nxt4)
            if nxt4 is None:
                self.assertEqual(len(stems), index + STANDING_N3)
                self.assertEqual(stems[index + 2], STANDING_IA2_174_NEXT_TOKEN)
            else:
                self.assertEqual(tuple(stems[index : index + STANDING_N4]), nxt4)
            self.assertEqual(side, SIDE_IA)
            site = (side, line, index)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, CYCLE253_MATCHING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE226_MATCHING_SITES)
            self.assertNotIn(site, CYCLE229_I_SITES)
            self.assertNotIn(site, CYCLE232_I_SITES)
            self.assertNotIn(site, CYCLE236_I_SITES)
            self.assertNotIn(site, CYCLE239_I_SITES)
            self.assertNotIn(site, CYCLE242_I_SITES)
            self.assertNotIn(site, CYCLE245_I_SITES)
            self.assertNotIn(site, CYCLE248_I_SITES)
            self.assertNotIn(site, CYCLE251_I_SITES)
            self.assertNotIn(site, CYCLE195_I_SITES)
            self.assertNotIn(site, CYCLE207_I_SITES)
            self.assertNotEqual(site, STANDING_IA14_140)
        self.assertEqual(
            STANDING_I_SITES,
            (
                (SIDE_IA, "Ia2", 174),
                (SIDE_IA, "Ia10", 141),
            ),
        )
        self.assertEqual(STANDING_I_SITES[0], STANDING_IA2_174)
        self.assertEqual(STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS, CYCLE253_MATCHING_NEXT_4GRAMS)
        self.assertEqual(
            STANDING_LEFTOVER_MATCHING_NEXT_4GRAMS,
            (
                None,
                ("090", "076", "000", "076"),
            ),
        )
        self.assertEqual(STANDING_I_NEXT_4GRAMS, CYCLE253_MATCHING_NEXT_4GRAMS)
        ia2 = self.i_sides[SIDE_IA][IA_LINE_NAMES.index("Ia2")]
        self.assertEqual(tuple(ia2[174:177]), GRAM3)
        self.assertEqual(len(ia2), 177)
        self.assertEqual(ia2[176], STANDING_IA2_174_NEXT_TOKEN)
        self.assertEqual(STANDING_IA2_174_NEXT_STEM, "000")
        self.assertTrue(STANDING_IA2_174_LINE_FINAL)
        self.assertFalse(STANDING_IA2_174_HAS_FOLLOWING_TOKEN)
        self.assertTrue(STANDING_IA2_174_HAS_NO_NEXT_4GRAM)
        self.assertIsNone(site_next_4gram(ia2, 174, GRAM2))
        self.assertEqual(site_forward_3gram(ia2, 174, GRAM2), GRAM3)
        ia14 = self.i_sides[SIDE_IA][IA_LINE_NAMES.index("Ia14")]
        self.assertEqual(tuple(ia14[140:144]), STANDING_IA14_140_NEXT_4GRAM)
        self.assertEqual(tuple(ia14[140:144]), NEAR_MISS_090_076_070_000)
        self.assertEqual(tuple(ia14[140:143]), CYCLE207_GRAM3)
        self.assertNotEqual(tuple(ia14[140:143]), GRAM3)
        self.assertEqual(STANDING_IA14_140, (SIDE_IA, "Ia14", 140))
        self.assertNotIn(STANDING_IA14_140, STANDING_I_SITES)
        self.assertTrue(STANDING_IA14_140_IS_NOT_090_076_000)
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
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_3gram_is_zero_off_i_and_i_only(self):
        """3-gram is 0 on A–H and J–V. Ia has exactly 2. T 090 076 070 000 is not this 3-gram."""
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
                self.assertEqual(count, 2)
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
        self.assertEqual(ngram_hit_count(t_sides[SIDE_TA], NEAR_MISS_090_076_070_000), 1)
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
        self.assertEqual(tuple(ta9[2:6]), CYCLE219_LEAK_4GRAM)
        self.assertNotEqual(tuple(ta9[2:5]), GRAM3)
        self.assertEqual(
            i_3gram_090_076_000_i_only(self.i_hits, self.off_i_hits),
            STANDING_I_3GRAM_090_076_000_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_090_076_000_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(STANDING_I_3GRAM_090_076_000_I_ONLY)
        self.assertTrue(HYPOTHESIS_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_3gram_090_076_000_i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE195_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE207_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE219_4GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE220_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE223_2GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE251_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE253)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE251)
        self.assertTrue(STANDING_OFF_I_T_SITES_OF_090_076_ARE_THIS_CYCLE_ONLY_IF_000)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        if self.off_i_hits != 0:
            self.fail("measured N_off_I drifted from 0")
        if self.i_hits != STANDING_N_I:
            self.fail("measured N_I drifted from the locked count")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_253_252_251_250_219_and_223_still_compute(self):
        """Cycle 253 K=2/G=000 N_remaining10=21, 252 2/2 hapax, 251 2/0 extra I=0, 250 K=2/G=005, 219 7/8 lose on T 000, 223 69/3 stay."""
        prior_253 = TestMamariILeftoverExtra090076RemainingAfter005Fwd000Scoreboard()
        prior_253.setUp()
        prior_253.test_counts_2_of_21_and_hypothesis_k_2_holds()
        prior_253.test_survey_matches_computed_lock()
        self.assertEqual(prior_253.k, 2)
        self.assertEqual(CYCLE253_G, "000")
        self.assertEqual(prior_253.n_remaining10, 21)
        self.assertEqual(prior_253.matching, CYCLE253_MATCHING_SITES)
        self.assertTrue(prior_253.claim_holds)
        self.assertTrue(CYCLE253_CLAIM)
        if prior_253.k != 2 or CYCLE253_G != "000" or prior_253.n_remaining10 != 21:
            self.fail("nested cycle 253 leftover extra remaining-after-005 G=000 K=2 drifted")
        prior_252 = TestMamariI090076005Forward4gramsIOnlyScoreboard()
        prior_252.setUp()
        prior_252.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_252.test_survey_matches_computed_lock()
        self.assertEqual(prior_252.n_i_only, 2)
        self.assertEqual(prior_252.n_not_i_only, 0)
        self.assertTrue(prior_252.claim_holds)
        self.assertTrue(CYCLE252_CLAIM)
        self.assertEqual(CYCLE252_N_I_ONLY, 2)
        self.assertEqual(CYCLE252_N_NOT_I_ONLY, 0)
        if prior_252.n_i_only != 2 or prior_252.n_not_i_only != 0:
            self.fail("nested cycle 252 090 076 005 forward 4-grams 2/2 hapax drifted")
        prior_251 = TestMamariI3gram090076005IOnlyScoreboard()
        prior_251.setUp()
        prior_251.test_i_hits_are_two_on_ia_and_equal_leftover_extra_005()
        prior_251.test_3gram_is_zero_off_i_and_i_only()
        prior_251.test_survey_matches_computed_lock()
        self.assertEqual(prior_251.i_hits, CYCLE251_N_I)
        self.assertEqual(prior_251.i_hits, 2)
        self.assertEqual(prior_251.off_i_hits, CYCLE251_N_OFF_I)
        self.assertEqual(prior_251.off_i_hits, 0)
        self.assertEqual(prior_251.i_sites, CYCLE251_I_SITES)
        self.assertEqual(prior_251.extra, CYCLE251_EXTRA_I_SITES)
        self.assertEqual(len(prior_251.extra), CYCLE251_N_EXTRA)
        self.assertEqual(CYCLE251_N_EXTRA, 0)
        self.assertTrue(prior_251.claim_holds)
        self.assertTrue(CYCLE251_CLAIM)
        if prior_251.i_hits != 2 or prior_251.off_i_hits != 0 or len(prior_251.extra) != 0:
            self.fail("nested cycle 251 090 076 005 I-only 2/0 extra I=0 drifted")
        prior_250 = TestMamariILeftoverExtra090076RemainingAfter011Fwd005Scoreboard()
        prior_250.setUp()
        prior_250.test_counts_2_of_23_and_hypothesis_k_2_holds()
        prior_250.test_survey_matches_computed_lock()
        self.assertEqual(prior_250.k, 2)
        self.assertEqual(CYCLE250_G, "005")
        self.assertEqual(prior_250.n_remaining9, 23)
        self.assertEqual(prior_250.matching, CYCLE250_MATCHING_SITES)
        self.assertTrue(prior_250.claim_holds)
        self.assertTrue(CYCLE250_CLAIM)
        if prior_250.k != 2 or CYCLE250_G != "005" or prior_250.n_remaining9 != 23:
            self.fail("nested cycle 250 leftover extra remaining-after-011 G=005 K=2 drifted")
        prior_234 = TestMamariILeftoverExtra090076RemainingAfter001NextStemScoreboard()
        prior_234.setUp()
        prior_234.test_counts_33_remaining4_g_700_k_2_and_hypothesis_loses()
        prior_234.test_survey_matches_computed_lock()
        self.assertEqual(prior_234.n_remaining4, 33)
        self.assertEqual(prior_234.k, 2)
        self.assertEqual(CYCLE234_G, "700")
        self.assertFalse(prior_234.unique)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(prior_234.claim_holds)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertEqual(CYCLE234_N_REMAINING4, 33)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertEqual(CYCLE234_TIED_STEMS[-1], "000")
        if (
            prior_234.n_remaining4 != 33
            or prior_234.k != 2
            or prior_234.unique
        ):
            self.fail("nested cycle 234 leftover extra remaining-after-001 7-way tie at 2 drifted")
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
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        prior_219.test_survey_matches_computed_lock()
        self.assertEqual(prior_219.n_i_only, 7)
        self.assertEqual(prior_219.n_not_i_only, 1)
        self.assertFalse(prior_219.claim_holds)
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        if prior_219.n_i_only != 7 or prior_219.n_not_i_only != 1:
            self.fail("nested cycle 219 090 076 070 forward 4-grams 7/8 lose on T 000 drifted")
        prior_220_n_i = CYCLE220_N_I
        prior_220_n_off = CYCLE220_N_OFF_I
        self.assertEqual(prior_220_n_i, 1)
        self.assertEqual(prior_220_n_off, 0)
        self.assertTrue(CYCLE220_CLAIM)
        self.assertEqual(CYCLE220_GRAM5, ("999", "090", "076", "070", "000"))
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
        self.assertEqual(CYCLE195_N_I, 6)
        self.assertEqual(CYCLE195_N_OFF_I, 0)
        self.assertEqual(CYCLE232_N_I, 3)
        self.assertEqual(CYCLE232_N_OFF_I, 0)
        self.assertTrue(CYCLE232_CLAIM)
        self.assertEqual(CYCLE248_N_I, 4)
        self.assertEqual(CYCLE248_N_OFF_I, 0)
        self.assertEqual(CYCLE248_N_EXTRA, 2)
        self.assertTrue(CYCLE248_CLAIM)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-254 3-gram I-only lock."""
        lock = self.survey["i_3gram_090_076_000_i_only"]
        self.assertEqual(lock["cycle"], 254)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_i_only"])
        self.assertEqual(lock["hypothesis_i_only"], HYPOTHESIS_I_ONLY)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 2)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_extra_remaining_after_005_000_sites"]),
            STANDING_LEFTOVER_MATCHING_SITES,
        )
        self.assertEqual(
            lock["leftover_extra_remaining_after_005_000_count"],
            STANDING_LEFTOVER_MATCHING_COUNT,
        )
        self.assertEqual(lock["leftover_extra_remaining_after_005_000_count"], 2)
        self.assertTrue(lock["leftover_extra_remaining_after_005_000_subset_of_i_sites"])
        self.assertEqual(lock["extra_i_sites"], [])
        self.assertEqual(lock["N_extra"], 0)
        self.assertEqual(
            [list(gram) for gram in STANDING_I_PREVIOUS_4GRAMS],
            lock["i_previous_4grams"],
        )
        self.assertEqual(
            [None if gram is None else list(gram) for gram in STANDING_I_NEXT_4GRAMS],
            lock["i_next_4grams"],
        )
        self.assertTrue(lock["ia2_174_line_final"])
        self.assertEqual(lock["ia2_174_next_token"], "000")
        self.assertFalse(lock["ia2_174_has_following_token"])
        self.assertTrue(lock["ia2_174_has_no_next_4gram"])
        self.assertTrue(lock["ia14_140_is_not_090_076_000"])
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
        self.assertEqual(lock["nested_cycle253_G"], STANDING_CYCLE253_G)
        self.assertEqual(lock["nested_cycle253_G"], "000")
        self.assertEqual(lock["nested_cycle253_K"], STANDING_CYCLE253_K)
        self.assertEqual(lock["nested_cycle253_K"], 2)
        self.assertEqual(lock["nested_cycle253_N_remaining10"], STANDING_CYCLE253_N_REMAINING10)
        self.assertEqual(lock["nested_cycle253_N_remaining10"], 21)
        self.assertEqual(lock["nested_cycle252_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle252_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle251_N_I"], 2)
        self.assertEqual(lock["nested_cycle251_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle251_N_extra"], 0)
        self.assertEqual(lock["nested_cycle250_G"], "005")
        self.assertEqual(lock["nested_cycle250_K"], 2)
        self.assertEqual(lock["nested_cycle250_N_remaining9"], 23)
        self.assertEqual(lock["nested_cycle234_N_remaining4"], 33)
        self.assertEqual(lock["nested_cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["nested_cycle234_G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["nested_cycle234_tied_stems_at_K"]), CYCLE234_TIED_STEMS)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle219_N_i_only"], 7)
        self.assertEqual(lock["nested_cycle219_N_not_i_only"], 1)
        self.assertEqual(tuple(lock["nested_cycle219_leak_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(lock["nested_cycle220_N_I"], 1)
        self.assertEqual(lock["nested_cycle220_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle171_N_I"], 43)
        self.assertEqual(lock["nested_cycle171_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_3gram_090_076_000_i_only"])
        self.assertEqual(
            lock["i_3gram_090_076_000_i_only"],
            STANDING_I_3GRAM_090_076_000_I_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle195_3gram"])
        self.assertFalse(lock["same_as_cycle207_3gram"])
        self.assertFalse(lock["same_as_cycle219_4gram"])
        self.assertFalse(lock["same_as_cycle220_5gram"])
        self.assertFalse(lock["same_as_cycle223_2gram"])
        self.assertFalse(lock["same_as_cycle229_3gram"])
        self.assertFalse(lock["same_as_cycle232_3gram"])
        self.assertFalse(lock["same_as_cycle236_3gram"])
        self.assertFalse(lock["same_as_cycle239_3gram"])
        self.assertFalse(lock["same_as_cycle242_3gram"])
        self.assertFalse(lock["same_as_cycle245_3gram"])
        self.assertFalse(lock["same_as_cycle248_3gram"])
        self.assertFalse(lock["same_as_cycle251_3gram"])
        self.assertFalse(lock["same_as_cycle253"])
        self.assertTrue(lock["same_claim_shape_as_cycle195"])
        self.assertTrue(lock["same_claim_shape_as_cycle207"])
        self.assertTrue(lock["same_claim_shape_as_cycle229"])
        self.assertTrue(lock["same_claim_shape_as_cycle232"])
        self.assertTrue(lock["same_claim_shape_as_cycle236"])
        self.assertTrue(lock["same_claim_shape_as_cycle239"])
        self.assertTrue(lock["same_claim_shape_as_cycle242"])
        self.assertTrue(lock["same_claim_shape_as_cycle245"])
        self.assertTrue(lock["same_claim_shape_as_cycle248"])
        self.assertTrue(lock["same_claim_shape_as_cycle251"])
        self.assertTrue(lock["090_076_005_does_not_count"])
        self.assertTrue(lock["090_076_011_does_not_count"])
        self.assertTrue(lock["090_076_087_does_not_count"])
        self.assertTrue(lock["090_076_280_does_not_count"])
        self.assertTrue(lock["090_076_530_does_not_count"])
        self.assertTrue(lock["090_076_700_does_not_count"])
        self.assertTrue(lock["090_076_001_does_not_count"])
        self.assertTrue(lock["090_076_013_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["090_076_without_000_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["090_076_070_000_does_not_count"])
        self.assertTrue(lock["999_090_076_070_000_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_000_is_not_this_cycle"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_this_cycle_only_if_000"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_005_fwd000_unchanged"])
        self.assertTrue(lock["standing_i_090_076_005_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_005_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_011_fwd005_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["cycle"],
            253,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"][
                "i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["G"],
            "000",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["K"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["N_remaining10"],
            21,
        )
        self.assertEqual(self.survey["i_090_076_005_forward_4grams_i_only"]["cycle"], 252)
        self.assertTrue(
            self.survey["i_090_076_005_forward_4grams_i_only"][
                "i_090_076_005_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(self.survey["i_090_076_005_forward_4grams_i_only"]["N_i_only"], 2)
        self.assertEqual(self.survey["i_090_076_005_forward_4grams_i_only"]["N_not_i_only"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_005_i_only"]["cycle"], 251)
        self.assertTrue(self.survey["i_3gram_090_076_005_i_only"]["i_3gram_090_076_005_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_005_i_only"]["N_I"], 2)
        self.assertEqual(self.survey["i_3gram_090_076_005_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_005_i_only"]["N_extra"], 0)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"]["cycle"],
            250,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"][
                "i_leftover_extra_090_076_remaining_after_011_exactly_2_share_005"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"]["G"],
            "005",
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"]["K"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_011_fwd005"]["N_remaining9"],
            23,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"]["cycle"],
            234,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_001_next_stem"][
                "G_uniquely_most_frequent"
            ]
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_090_076_070_forward_4grams_i_only"]["cycle"], 219)
        self.assertFalse(
            self.survey["i_090_076_070_forward_4grams_i_only"][
                "i_090_076_070_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI3gram090076000IOnlyImageSnapshot(unittest.TestCase):
    """Cycle 254 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
