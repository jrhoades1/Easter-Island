"""I's cycle-264 shared previous-000 cluster lock.

Cycle 265 text-search lock. Uses already-vendored A–V and the
cycle-262 I sites of 3-gram 999 090 076 (N_I=16, N_off_I=0,
extra I=1 at Ia9[27]). Cycle 263 lost all-hapax: N_i_only=14
/ N_not_i_only=0 / N_not_hapax=2. The two shared previous
4-grams (K=2 each) are 000 999 090 076 and 090 999 090 076.
Cycle 264 already locked previous 090 (largest-id of the K=2
tie) at Ia12[46]/Ia14[139]. This cycle locks the remaining
tied previous-000 cluster as an exact-K claim. Does not
retune that 3-gram, those previous 4-grams, leftover extra
previous-999 (cycle 261 K_999=15 / N_remaining_after_999=41),
leftover extra share-one-previous-stem (cycle 260 lost),
leftover extra sites, leftover n=4 remaining 999 090 076 057,
the leftover n=4 set, or the already-closed leftover remaining
family. Does not peel leftover extra remaining-after-999 this
cycle. Does not retune leftover n=4. Does not retune the
forward peel of leftover extra I 090 076 (cycles 225–259).
Does not overwrite cycle 167's 3-gram I-only 16/0 lock. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Same claim-shape as cycle 264 (exactly 2 I 999 090 076 sites
share one previous token of the cycle-263 K=2 tie) and cycle
235 (exactly K share G after a unique-max / hapax lose with
a K=2 tie), previous 000 of I 999 090 076 instead of previous
090. Cycle 253 leftover extra remaining-after-005 exactly 2
share forward 000 is a different previous-000 (forward peel
of leftover extra I 090 076 at Ia2[174]/Ia10[141]); do not
confuse with this previous-000 of I 999 090 076. Cycle 223
lost: 090 076 is not I-only (69/3 on T). Cycle 207 lost:
090 076 070 is not I-only (8/1 on T). Cycle 220 5-gram
999 090 076 070 000 is a different n=5 (1/0). 090 076 without
999, 720 076 070, and 999 090 076 071 do not count as this
3-gram. Off-I T sites are not this cycle. Do not assume K;
count each from fixtures.

Nested-check cycle 262: N_I==16, N_off_I==0, extra I==1 at
Ia9[27] (do not retune). Nested-check cycle 263: all-hapax
false, N_not_hapax==2, N_not_i_only==0, shared 4-grams
000 999 090 076 and 090 999 090 076 each N_I==2 (do not
retune). Nested-check cycle 264: K_090==2 at Ia12[46]/
Ia14[139] (do not retune). Count I 999 090 076 sites whose
previous token is 000. Lock those sites (3-gram start and
4-gram start). Lock K_000. Nested-check each previous-000 I
999 090 076 site ⊆ I 3-gram sites and has previous token 000.
Nested-check 4-gram 000 999 090 076 N_I==2 N_off_I==0 (do not
retune 263; still compute).

Hypothesis K=2: exactly 2 I 999 090 076 sites share previous
token 000 (4-gram 000 999 090 076). Measured: K_000=2 at
Ia3[36]/Ia5[1] (4-gram starts Ia3[35]/Ia5[0]). Claim that
can lose: i_999_090_076_exactly_2_share_previous_000. True
iff K_000==2 among I 999 090 076 sites. This can lose if
nested-check K differs from 2. The claim is true. Nested
cycle 264 K_090=2, cycle 263 14/0 N_not_hapax=2, cycle 262
16/0 extra I=1, cycle 261 K_999=15 N_remaining=41, cycle 260
34 distinct G=999 K=15, cycle 223 69/3, cycle 207 8/1 on T,
and cycle 167 16/0 stay. Do not assume the result; measure.
Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from collections import Counter

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_N_I as CYCLE223_N_I,
    STANDING_N_OFF_I as CYCLE223_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_720_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE212_GRAM3,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_I_SITES as CYCLE167_I_SITES,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_leftover_extra_previous_i_only_scoreboard import (
    GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE262_EXTRA_I_SITES,
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE262_CLAIM,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE262_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE262_I_SITES,
    STANDING_LEFTOVER_3GRAM_SITES as CYCLE262_LEFTOVER_3GRAM_SITES,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE262_LEFTOVER_MATCHING_SITES,
    STANDING_N_EXTRA as CYCLE262_N_EXTRA,
    STANDING_N_I as CYCLE262_N_I,
    STANDING_N_OFF_I as CYCLE262_N_OFF_I,
    leftover_extra_090_076_site_for_3gram,
    leftover_extra_previous_999_subset,
    leftover_3gram_sites,
    extra_i_sites,
    site_previous_4gram_for_3gram,
    TestMamariI3gram999090076LeftoverExtraPreviousIOnlyScoreboard,
)
from tests.test_mamari_i_5gram_999_090_076_070_000_i_only_scoreboard import (
    GRAM5 as CYCLE220_GRAM5,
    STANDING_I_5GRAM_999_090_076_070_000_I_ONLY as CYCLE220_CLAIM,
    STANDING_I_SITES as CYCLE220_I_SITES,
    STANDING_N_I as CYCLE220_N_I,
    STANDING_N_OFF_I as CYCLE220_N_OFF_I,
    TestMamariI5gram999090076070000IOnlyScoreboard,
)
from tests.test_mamari_i_999_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY as CYCLE263_ALL_I_ONLY,
    STANDING_I_999_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE263_ALL_HAPAX,
    STANDING_N_I_ONLY as CYCLE263_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE263_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE263_N_NOT_I_ONLY,
    STANDING_NOT_HAPAX_I_SITES as CYCLE263_NOT_HAPAX_I_SITES,
    STANDING_NOT_HAPAX_SEQUENCES as CYCLE263_NOT_HAPAX_SEQUENCES,
    previous_4gram_start_site,
    TestMamariI999090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_999_090_076_previous_090_scoreboard import (
    STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_090 as CYCLE264_CLAIM,
    STANDING_K_000 as CYCLE264_K_000,
    STANDING_K_090 as CYCLE264_K_090,
    STANDING_MATCHING_4GRAM_SITES as CYCLE264_MATCHING_4GRAM_SITES,
    STANDING_MATCHING_SITES as CYCLE264_MATCHING_SITES,
    STANDING_OTHER_TIED_4GRAM_SITES as CYCLE264_OTHER_TIED_4GRAM_SITES,
    STANDING_OTHER_TIED_SITES as CYCLE264_OTHER_TIED_SITES,
    i_999_090_076_previous_stems,
    site_previous_stem_for_3gram,
    TestMamariI999090076Previous090Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    STANDING_G as CYCLE261_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999 as CYCLE261_CLAIM,
    STANDING_K_999 as CYCLE261_K_999,
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
    STANDING_N_LEFTOVER_EXTRA as CYCLE261_N_LEFTOVER_EXTRA,
    STANDING_N_REMAINING_AFTER_999 as CYCLE261_N_REMAINING_AFTER_999,
    TestMamariILeftoverExtra090076Previous999Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE260_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM as CYCLE260_SHARE_ONE,
    STANDING_K as CYCLE260_K,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE260_N_DISTINCT,
    rank_previous_stems,
    select_previous_g,
    TestMamariILeftoverExtra090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_005_fwd000_scoreboard import (
    STANDING_G as CYCLE253_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_005_EXACTLY_2_SHARE_000 as CYCLE253_CLAIM,
    STANDING_K as CYCLE253_K,
    STANDING_MATCHING_SITES as CYCLE253_MATCHING_SITES,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    NEAR_MISS_999_090_076_071,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    barthel_id,
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

HYPOTHESIS_K = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N5 = 5
NEAR_MISS_720_076_070 = CYCLE212_GRAM3
NEAR_MISS_090_076_070 = CYCLE207_GRAM3
NEAR_MISS_090_076 = GRAM2
NEAR_MISS_5GRAM = CYCLE220_GRAM5
NEAR_MISS_LEFTOVER_N4_057 = ("999", "090", "076", "057")
GRAM4_PREVIOUS_000 = ("000", "999", "090", "076")
GRAM4_PREVIOUS_090 = ("090", "999", "090", "076")
STANDING_CYCLE262_SITES = CYCLE262_I_SITES
STANDING_N_I_3GRAM = 16
STANDING_N_OFF_I_3GRAM = 0
STANDING_N_EXTRA = 1
STANDING_N_WITH_PREVIOUS = 16
STANDING_N_LINE_INITIAL = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_G = "000"
STANDING_K = 2
STANDING_K_000 = 2
STANDING_K_090 = 2
STANDING_N_WITHOUT_000 = 14
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_TIED_STEMS = ("090", "000")
STANDING_N_TIED_AT_K = 2
STANDING_OTHER_TIED_STEM = "090"
STANDING_LARGEST_ID_G = "090"
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia3", 36),
    (SIDE_IA, "Ia5", 1),
)
STANDING_MATCHING_4GRAM_SITES = (
    (SIDE_IA, "Ia3", 35),
    (SIDE_IA, "Ia5", 0),
)
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    GRAM4_PREVIOUS_000,
    GRAM4_PREVIOUS_000,
)
STANDING_MATCHING_LEFTOVER_EXTRA_090_076_SITES = (
    (SIDE_IA, "Ia3", 37),
    (SIDE_IA, "Ia5", 2),
)
STANDING_OTHER_TIED_SITES = (
    (SIDE_IA, "Ia12", 46),
    (SIDE_IA, "Ia14", 139),
)
STANDING_OTHER_TIED_4GRAM_SITES = (
    (SIDE_IA, "Ia12", 45),
    (SIDE_IA, "Ia14", 138),
)
STANDING_N_I_4GRAM = 2
STANDING_N_OFF_I_4GRAM = 0
STANDING_IB_HITS = 0
STANDING_OFF_I_SITES = ()
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_N_I_4GRAM if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_MATCHING_EQUALS_CYCLE263_000_SITES = True
STANDING_MATCHING_EQUALS_CYCLE264_OTHER_TIED_SITES = True
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_999_090_076_exactly_2_share_previous_000"
STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_000 = True
STANDING_RESULT = "i_999_090_076_previous_000"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167_3GRAM = False
STANDING_SAME_AS_CYCLE235 = False
STANDING_SAME_AS_CYCLE253 = False
STANDING_SAME_AS_CYCLE261 = False
STANDING_SAME_AS_CYCLE262 = False
STANDING_SAME_AS_CYCLE263 = False
STANDING_SAME_AS_CYCLE264 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE264 = True
STANDING_090_076_WITHOUT_999_DOES_NOT_COUNT = True
STANDING_720_076_070_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_999_090_076_071_DOES_NOT_COUNT = True
STANDING_5GRAM_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_057_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_CYCLE167_NOT_OVERWRITTEN = True
STANDING_CYCLE253_FORWARD_000_IS_NOT_THIS_CYCLE = True
STANDING_CYCLE264_PREVIOUS_090_ALREADY_LOCKED = True
STANDING_OTHER_TIED_STEM_090_ALREADY_LOCKED = True
STANDING_OFF_I_T_SITES_OF_090_076_ARE_NOT_THIS_CYCLE = True


def i_999_090_076_sites_with_previous_000(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """I 999 090 076 sites whose previous token is 000."""
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev == stem
    )


def i_999_090_076_sites_without_previous_000(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """I 999 090 076 sites whose previous token is not 000, or none."""
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev != stem
    )


def matching_equals_cycle263_000_sites(
    matching_4gram_sites: tuple[tuple[str, str, int], ...],
    cycle263_000_sites: tuple[tuple[str, str, int], ...] = CYCLE263_NOT_HAPAX_I_SITES[0],
) -> bool:
    """True iff previous-000 4-gram starts equal cycle 263's 000 999 090 076 pair."""
    return matching_4gram_sites == cycle263_000_sites


def matching_equals_cycle264_other_tied_sites(
    matching_3gram_sites: tuple[tuple[str, str, int], ...],
    cycle264_000_sites: tuple[tuple[str, str, int], ...] = CYCLE264_OTHER_TIED_SITES,
) -> bool:
    """True iff previous-000 3-gram starts equal cycle 264's unlocked 000 pair."""
    return matching_3gram_sites == cycle264_000_sites


def i_999_090_076_exactly_2_share_previous_000(
    k: int,
    expected: int = HYPOTHESIS_K,
) -> bool:
    """True iff K_000 equals the hypothesized 2."""
    return k == expected


def matching_site_row_as_survey(
    site: tuple[str, str, int],
    previous_4gram: tuple[str, ...] = GRAM4_PREVIOUS_000,
) -> dict:
    """JSON-ready previous-000 I 999 090 076 site row."""
    start = previous_4gram_start_site(site)
    leftover = leftover_extra_090_076_site_for_3gram(site)
    return {
        "tablet": "I",
        "side": site[0],
        "line": site[1],
        "index": site[2],
        "previous_4gram_start": list(start) if start is not None else None,
        "previous_4gram": list(previous_4gram),
        "previous_stem": previous_4gram[0],
        "leftover_extra_090_076_site": list(leftover),
        "in_cycle261_leftover_extra_15": leftover in CYCLE261_MATCHING_SITES,
        "N_I": STANDING_N_I_4GRAM,
        "N_off_I": STANDING_N_OFF_I_4GRAM,
    }


STANDING_SITE_ROWS = tuple(
    matching_site_row_as_survey(site, gram)
    for site, gram in zip(
        STANDING_MATCHING_SITES,
        STANDING_MATCHING_PREVIOUS_4GRAMS,
        strict=True,
    )
)


class TestI999090076Previous000Helpers(unittest.TestCase):
    """Helpers on I 999 090 076 previous 000. No CV, no LLM."""

    def test_previous_000_requires_stem_before_3gram(self):
        """Previous stem 000 is 000 999 090 076; line-initial is no-previous."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(GRAM4_PREVIOUS_000, ("000", "999", "090", "076"))
        self.assertEqual(GRAM4_PREVIOUS_090, ("090", "999", "090", "076"))
        self.assertEqual(GRAM4_PREVIOUS_000[1:], GRAM3)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(len(GRAM4_PREVIOUS_000), STANDING_N4)
        has_000 = ["000", "999", "090", "076", "013"]
        self.assertEqual(site_previous_stem_for_3gram(has_000, 1, GRAM3), "000")
        self.assertEqual(
            site_previous_4gram_for_3gram(has_000, 1, GRAM3),
            GRAM4_PREVIOUS_000,
        )
        has_090 = ["090", "999", "090", "076", "011"]
        self.assertEqual(site_previous_stem_for_3gram(has_090, 1, GRAM3), "090")
        self.assertNotEqual(site_previous_stem_for_3gram(has_090, 1, GRAM3), "000")
        has_244 = ["244", "999", "090", "076", "057"]
        self.assertEqual(site_previous_stem_for_3gram(has_244, 1, GRAM3), "244")
        self.assertNotEqual(site_previous_stem_for_3gram(has_244, 1, GRAM3), "000")
        line_initial = ["999", "090", "076"]
        self.assertIsNone(site_previous_stem_for_3gram(line_initial, 0, GRAM3))
        self.assertIsNone(site_previous_4gram_for_3gram(line_initial, 0, GRAM3))
        mismatch_071 = ["000", "999", "090", "071"]
        self.assertIsNone(site_previous_stem_for_3gram(mismatch_071, 1, GRAM3))
        self.assertEqual(ngram_hit_count([list(GRAM4_PREVIOUS_000)], GRAM4_PREVIOUS_000), 1)
        self.assertEqual(ngram_hit_count([list(GRAM4_PREVIOUS_090)], GRAM4_PREVIOUS_000), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_720_076_070)], GRAM4_PREVIOUS_000), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076_070)], GRAM4_PREVIOUS_000), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_090_076)], GRAM4_PREVIOUS_000), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_999_090_076_071)], GRAM4_PREVIOUS_000), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_5GRAM)], GRAM4_PREVIOUS_000), 0)
        self.assertEqual(ngram_hit_count([list(NEAR_MISS_LEFTOVER_N4_057)], GRAM4_PREVIOUS_000), 0)
        self.assertEqual(ngram_hit_count([["999", "090", "076"]], GRAM4_PREVIOUS_000), 0)
        self.assertTrue(STANDING_090_076_WITHOUT_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_720_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_999_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_5GRAM_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_057_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_2_can_fail(self):
        """Boolean is True only when K_000=2."""
        provider = MockProvider()
        self.assertTrue(i_999_090_076_exactly_2_share_previous_000(2))
        self.assertFalse(i_999_090_076_exactly_2_share_previous_000(0))
        self.assertFalse(i_999_090_076_exactly_2_share_previous_000(1))
        self.assertFalse(i_999_090_076_exactly_2_share_previous_000(3))
        self.assertFalse(i_999_090_076_exactly_2_share_previous_000(14))
        self.assertFalse(i_999_090_076_exactly_2_share_previous_000(16))
        planted = STANDING_MATCHING_SITES + ((SIDE_IA, "Ia1", 1),)
        planted_stems = ("000",) * 3
        self.assertEqual(
            i_999_090_076_sites_with_previous_000(planted, planted_stems),
            planted,
        )
        self.assertFalse(i_999_090_076_exactly_2_share_previous_000(len(planted)))
        self.assertEqual(STANDING_CLAIM, "i_999_090_076_exactly_2_share_previous_000")
        self.assertTrue(STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_000)
        self.assertEqual(
            STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_000,
            HYPOTHESIS_K == STANDING_K_000,
        )
        self.assertEqual(STANDING_K_000 + STANDING_N_WITHOUT_000, STANDING_N_I_3GRAM)
        self.assertEqual(2 + 14, 16)
        self.assertEqual(provider.get_call_history(), [])

    def test_cycle263_site_agreement_and_090_already_locked_can_fail(self):
        """Matching 4-gram starts must equal cycle 263's 000 pair; 090 stays cycle 264."""
        provider = MockProvider()
        self.assertTrue(matching_equals_cycle263_000_sites(STANDING_MATCHING_4GRAM_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE263_000_SITES)
        self.assertEqual(STANDING_MATCHING_4GRAM_SITES, CYCLE263_NOT_HAPAX_I_SITES[0])
        self.assertEqual(CYCLE263_NOT_HAPAX_SEQUENCES[0], GRAM4_PREVIOUS_000)
        self.assertEqual(CYCLE263_NOT_HAPAX_SEQUENCES[1], GRAM4_PREVIOUS_090)
        planted = STANDING_MATCHING_4GRAM_SITES[:-1]
        self.assertFalse(matching_equals_cycle263_000_sites(planted))
        self.assertFalse(i_999_090_076_exactly_2_share_previous_000(len(planted)))
        swapped = STANDING_OTHER_TIED_4GRAM_SITES
        self.assertFalse(matching_equals_cycle263_000_sites(swapped))
        self.assertTrue(i_999_090_076_exactly_2_share_previous_000(len(swapped)))
        self.assertEqual(STANDING_OTHER_TIED_4GRAM_SITES, CYCLE263_NOT_HAPAX_I_SITES[1])
        self.assertEqual(STANDING_OTHER_TIED_4GRAM_SITES, CYCLE264_MATCHING_4GRAM_SITES)
        self.assertTrue(matching_equals_cycle264_other_tied_sites(STANDING_MATCHING_SITES))
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE264_OTHER_TIED_SITES)
        self.assertEqual(STANDING_MATCHING_SITES, CYCLE264_OTHER_TIED_SITES)
        self.assertEqual(STANDING_MATCHING_4GRAM_SITES, CYCLE264_OTHER_TIED_4GRAM_SITES)
        self.assertTrue(STANDING_CYCLE264_PREVIOUS_090_ALREADY_LOCKED)
        self.assertTrue(STANDING_OTHER_TIED_STEM_090_ALREADY_LOCKED)
        self.assertEqual(STANDING_OTHER_TIED_STEM, "090")
        self.assertEqual(STANDING_TIED_STEMS, ("090", "000"))
        self.assertGreater(barthel_id("090"), barthel_id("000"))
        ranked = rank_previous_stems(Counter({"090": 2, "000": 2, "244": 1}))
        self.assertEqual(ranked[0], ("090", 2))
        self.assertEqual(ranked[1], ("000", 2))
        g, k, unique = select_previous_g(("090", "000", "090", "000", "244"))
        self.assertEqual(g, "090")
        self.assertEqual(STANDING_LARGEST_ID_G, "090")
        self.assertEqual(k, 2)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertFalse(CYCLE263_ALL_HAPAX)
        self.assertTrue(CYCLE263_ALL_I_ONLY)
        self.assertEqual(CYCLE263_N_NOT_HAPAX, 2)
        self.assertEqual(CYCLE263_N_NOT_I_ONLY, 0)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE264)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE253)
        self.assertFalse(STANDING_SAME_AS_CYCLE263)
        self.assertFalse(STANDING_SAME_AS_CYCLE264)
        self.assertNotEqual(STANDING_MATCHING_SITES, CYCLE253_MATCHING_SITES)
        self.assertNotEqual(STANDING_MATCHING_LEFTOVER_EXTRA_090_076_SITES, CYCLE253_MATCHING_SITES)
        self.assertTrue(STANDING_CYCLE253_FORWARD_000_IS_NOT_THIS_CYCLE)
        self.assertEqual(CYCLE253_G, "000")
        self.assertEqual(CYCLE253_K, 2)
        self.assertTrue(CYCLE253_CLAIM)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI999090076Previous000Scoreboard(unittest.TestCase):
    """Cited-fixture I 999 090 076 previous-000 exact-K lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.by_tablet = load_vendored_by_tablet()
        self.cycle262_sites = STANDING_CYCLE262_SITES
        self.previous_stems = i_999_090_076_previous_stems(
            self.i_sides,
            self.cycle262_sites,
        )
        self.previous_4grams = tuple(
            site_previous_4gram_for_3gram(
                line_stems_for_site(self.i_sides, site),
                site[2],
                GRAM3,
            )
            for site in self.cycle262_sites
        )
        self.line_initial = tuple(
            site
            for site, prev in zip(self.cycle262_sites, self.previous_stems, strict=True)
            if prev is None
        )
        self.matching = i_999_090_076_sites_with_previous_000(
            self.cycle262_sites,
            self.previous_stems,
        )
        self.without = i_999_090_076_sites_without_previous_000(
            self.cycle262_sites,
            self.previous_stems,
        )
        self.k_000 = len(self.matching)
        self.matching_4gram_sites = tuple(
            previous_4gram_start_site(site) for site in self.matching
        )
        self.matching_previous_4grams = tuple(
            self.previous_4grams[self.cycle262_sites.index(site)]
            for site in self.matching
        )
        self.largest_id_g, self.tiebreak_k, self.unique = select_previous_g(
            self.previous_stems
        )
        ranked = rank_previous_stems(
            Counter(stem for stem in self.previous_stems if stem is not None)
        )
        self.tied = tuple(stem for stem, count in ranked if count == self.tiebreak_k)
        self.k_090 = sum(1 for stem in self.previous_stems if stem == "090")
        self.gram4_i_sites = nge4_sites(GRAM4_PREVIOUS_000, self.i_sides)
        self.n_i_4gram = ngram_hit_count(self.i_sides[SIDE_IA], GRAM4_PREVIOUS_000)
        self.hits_by_tablet = tablet_hit_counts(
            self.by_tablet,
            GRAM4_PREVIOUS_000,
            VENDORED_TABLETS,
        )
        self.off_i = tablet_hit_counts(
            self.by_tablet,
            GRAM4_PREVIOUS_000,
            OFF_I_TABLETS,
        )
        self.n_off_i_4gram = sum(self.off_i)
        self.equals_cycle263 = matching_equals_cycle263_000_sites(
            self.matching_4gram_sites
        )
        self.equals_cycle264_other = matching_equals_cycle264_other_tied_sites(
            self.matching
        )
        self.claim_holds = i_999_090_076_exactly_2_share_previous_000(self.k_000)

    def test_tokens_and_sites_are_cycle_262_263_264_locks_not_retuned(self):
        """3-gram sites stay cycle 262; shared 4-grams stay 263; 090 stays 264. Cycle 167 stays 16/0."""
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.cycle262_sites, STANDING_CYCLE262_SITES)
        self.assertEqual(self.cycle262_sites, CYCLE167_I_SITES)
        self.assertEqual(self.cycle262_sites, CYCLE262_I_SITES)
        self.assertEqual(len(self.cycle262_sites), 16)
        self.assertEqual(self.previous_4grams, CYCLE262_PREVIOUS_4GRAMS)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(len(self.line_initial), STANDING_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_EXTRA, 1)
        self.assertEqual(CYCLE262_EXTRA_I_SITES, ((SIDE_IA, "Ia9", 27),))
        self.assertNotIn(CYCLE262_EXTRA_I_SITES[0], self.matching)
        extra_prev = self.previous_stems[self.cycle262_sites.index(CYCLE262_EXTRA_I_SITES[0])]
        self.assertEqual(extra_prev, "244")
        prior_264 = self.survey["i_999_090_076_previous_090"]
        self.assertEqual(prior_264["cycle"], 264)
        self.assertTrue(prior_264["i_999_090_076_exactly_2_share_previous_090"])
        self.assertEqual(prior_264["K_090"], 2)
        self.assertEqual(prior_264["K_000"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in prior_264["matching_3gram_sites"]),
            CYCLE264_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_264["matching_3gram_sites"]),
            (
                (SIDE_IA, "Ia12", 46),
                (SIDE_IA, "Ia14", 139),
            ),
        )
        self.assertTrue(CYCLE264_CLAIM)
        self.assertEqual(CYCLE264_K_090, 2)
        self.assertEqual(CYCLE264_K_000, 2)
        prior_263 = self.survey["i_999_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_263["cycle"], 263)
        self.assertFalse(prior_263["i_999_090_076_previous_4grams_all_i_only_hapax"])
        self.assertTrue(prior_263["i_999_090_076_previous_4grams_all_i_only"])
        self.assertEqual(prior_263["N_i_only"], 14)
        self.assertEqual(prior_263["N_not_i_only"], 0)
        self.assertEqual(prior_263["N_not_hapax"], 2)
        self.assertEqual(
            [list(gram) for gram in CYCLE263_NOT_HAPAX_SEQUENCES],
            prior_263["not_hapax_4grams"],
        )
        prior_262 = self.survey["i_3gram_999_090_076_leftover_extra_previous_i_only"]
        self.assertEqual(prior_262["cycle"], 262)
        self.assertEqual(tuple(prior_262["tokens3"]), GRAM3)
        self.assertEqual(prior_262["N_I"], 16)
        self.assertEqual(prior_262["N_off_I"], 0)
        self.assertEqual(prior_262["N_extra"], 1)
        self.assertTrue(prior_262["i_3gram_999_090_076_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_262["extra_i_sites"]),
            CYCLE262_EXTRA_I_SITES,
        )
        self.assertTrue(leftover_extra_previous_999_subset())
        self.assertEqual(extra_i_sites(), CYCLE262_EXTRA_I_SITES)
        self.assertEqual(leftover_3gram_sites(), CYCLE262_LEFTOVER_3GRAM_SITES)
        prior_261 = self.survey["i_leftover_extra_090_076_previous_999"]
        self.assertEqual(prior_261["cycle"], 261)
        self.assertEqual(prior_261["K_999"], 15)
        self.assertEqual(prior_261["N_remaining_after_999"], 41)
        self.assertTrue(prior_261["i_leftover_extra_090_076_exactly_15_share_previous_999"])
        prior_260 = self.survey["i_leftover_extra_090_076_previous_stem"]
        self.assertEqual(prior_260["cycle"], 260)
        self.assertEqual(prior_260["N_distinct_previous_stems"], 34)
        self.assertEqual(prior_260["G"], "999")
        self.assertEqual(prior_260["K"], 15)
        self.assertFalse(prior_260["i_leftover_extra_090_076_share_one_previous_stem"])
        prior_253 = self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]
        self.assertEqual(prior_253["cycle"], 253)
        self.assertEqual(prior_253["G"], "000")
        self.assertEqual(prior_253["K"], 2)
        self.assertTrue(prior_253["i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_253["matching_leftover_extra_remaining_after_005_sites"]),
            CYCLE253_MATCHING_SITES,
        )
        self.assertNotEqual(CYCLE253_MATCHING_SITES, STANDING_MATCHING_SITES)
        self.assertNotEqual(
            CYCLE253_MATCHING_SITES,
            STANDING_MATCHING_LEFTOVER_EXTRA_090_076_SITES,
        )
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertTrue(prior_167["i_3gram_999_090_076_i_only"])
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in prior_167["i_sites"]),
            CYCLE167_I_SITES,
        )
        self.assertNotEqual(STANDING_CLAIM, "i_3gram_999_090_076_i_only")
        self.assertNotEqual(STANDING_CLAIM, "i_999_090_076_exactly_2_share_previous_090")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertTrue(STANDING_CYCLE264_PREVIOUS_090_ALREADY_LOCKED)
        self.assertTrue(STANDING_CYCLE253_FORWARD_000_IS_NOT_THIS_CYCLE)
        self.assertEqual(CYCLE261_K_999, 15)
        self.assertEqual(CYCLE261_N_REMAINING_AFTER_999, 41)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_exactly_2_share_previous_000_and_hypothesis_holds(self):
        """K_000=2 at Ia3[36]/Ia5[1]. Other tied stem 090 already locked. Claim holds."""
        self.assertEqual(len(self.cycle262_sites), STANDING_N_I_3GRAM)
        self.assertEqual(len(self.previous_stems), STANDING_N_I_3GRAM)
        self.assertEqual(len(self.line_initial), STANDING_N_LINE_INITIAL)
        self.assertEqual(self.k_000, STANDING_K_000)
        self.assertEqual(STANDING_K_000, HYPOTHESIS_K)
        self.assertEqual(STANDING_K_000, 2)
        self.assertEqual(self.k_000, STANDING_K)
        self.assertEqual(len(self.without), STANDING_N_WITHOUT_000)
        self.assertEqual(STANDING_N_WITHOUT_000, 14)
        self.assertEqual(self.k_000 + len(self.without), STANDING_N_I_3GRAM)
        self.assertEqual(2 + 14, 16)
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(
            self.matching,
            (
                (SIDE_IA, "Ia3", 36),
                (SIDE_IA, "Ia5", 1),
            ),
        )
        self.assertEqual(self.matching_4gram_sites, STANDING_MATCHING_4GRAM_SITES)
        self.assertEqual(
            self.matching_4gram_sites,
            (
                (SIDE_IA, "Ia3", 35),
                (SIDE_IA, "Ia5", 0),
            ),
        )
        self.assertEqual(self.matching_previous_4grams, STANDING_MATCHING_PREVIOUS_4GRAMS)
        self.assertTrue(self.equals_cycle263)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE263_000_SITES)
        self.assertTrue(matching_equals_cycle263_000_sites(self.matching_4gram_sites))
        self.assertTrue(self.equals_cycle264_other)
        self.assertTrue(STANDING_MATCHING_EQUALS_CYCLE264_OTHER_TIED_SITES)
        self.assertEqual(STANDING_G, "000")
        self.assertEqual(self.largest_id_g, STANDING_LARGEST_ID_G)
        self.assertEqual(STANDING_LARGEST_ID_G, "090")
        self.assertEqual(self.tiebreak_k, 2)
        self.assertEqual(self.k_090, STANDING_K_090)
        self.assertEqual(STANDING_K_090, 2)
        self.assertEqual(self.k_090, CYCLE264_K_090)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.tied, STANDING_TIED_STEMS)
        self.assertEqual(self.tied, ("090", "000"))
        self.assertEqual(len(self.tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 2)
        self.assertGreater(barthel_id(self.largest_id_g), barthel_id(STANDING_G))
        if self.k_000 != 2:
            self.fail("measured K_000 drifted from 2")
        if self.largest_id_g != "090" or self.unique or self.tied != ("090", "000"):
            self.fail("largest-id max-K previous G=090 tied with 000 at K=2 drifted")
        self.assertTrue(i_999_090_076_exactly_2_share_previous_000(self.k_000))
        self.assertEqual(
            self.claim_holds,
            STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_000,
        )
        self.assertTrue(STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_000)
        self.assertEqual(STANDING_CLAIM, "i_999_090_076_exactly_2_share_previous_000")
        self.assertEqual(self.n_i_4gram, STANDING_N_I_4GRAM)
        self.assertEqual(self.n_off_i_4gram, STANDING_N_OFF_I_4GRAM)
        self.assertEqual(self.n_i_4gram, 2)
        self.assertEqual(self.n_off_i_4gram, 0)
        self.assertEqual(self.gram4_i_sites, STANDING_MATCHING_4GRAM_SITES)
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i, STANDING_OFF_I_BY_TABLET)
        if self.n_i_4gram != 2 or self.n_off_i_4gram != 0:
            self.fail("4-gram 000 999 090 076 N_I/N_off_I drifted from 2/0")
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE167_3GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE235)
        self.assertFalse(STANDING_SAME_AS_CYCLE253)
        self.assertFalse(STANDING_SAME_AS_CYCLE261)
        self.assertFalse(STANDING_SAME_AS_CYCLE262)
        self.assertFalse(STANDING_SAME_AS_CYCLE263)
        self.assertFalse(STANDING_SAME_AS_CYCLE264)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE235)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE264)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_CYCLE264_PREVIOUS_090_ALREADY_LOCKED)
        self.assertTrue(STANDING_OTHER_TIED_STEM_090_ALREADY_LOCKED)
        self.assertTrue(STANDING_CYCLE253_FORWARD_000_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_previous_000_sites_subset_i_3gram_and_have_previous_000(self):
        """Each previous-000 site ⊆ I 3-gram sites and previous token is 000."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        expected = (
            ((SIDE_IA, "Ia3", 36), (SIDE_IA, "Ia3", 35), (SIDE_IA, "Ia3", 37)),
            ((SIDE_IA, "Ia5", 1), (SIDE_IA, "Ia5", 0), (SIDE_IA, "Ia5", 2)),
        )
        for site, start, leftover, (want_3, want_4, want_2) in zip(
            self.matching,
            self.matching_4gram_sites,
            STANDING_MATCHING_LEFTOVER_EXTRA_090_076_SITES,
            expected,
            strict=True,
        ):
            self.assertIn(site, STANDING_CYCLE262_SITES)
            self.assertIn(site, CYCLE262_I_SITES)
            self.assertIn(site, CYCLE167_I_SITES)
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N3]), GRAM3)
            self.assertEqual(site_previous_stem_for_3gram(stems, site[2], GRAM3), "000")
            self.assertEqual(
                site_previous_4gram_for_3gram(stems, site[2], GRAM3),
                GRAM4_PREVIOUS_000,
            )
            self.assertEqual(previous_4gram_start_site(site), start)
            self.assertEqual(start, want_4)
            self.assertEqual(site, want_3)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), GRAM4_PREVIOUS_000)
            self.assertIn(start, self.gram4_i_sites)
            self.assertEqual(leftover_extra_090_076_site_for_3gram(site), leftover)
            self.assertEqual(leftover, want_2)
            self.assertIn(leftover, CYCLE261_MATCHING_SITES)
            self.assertIn(leftover, CYCLE262_LEFTOVER_MATCHING_SITES)
            self.assertNotIn(site, CYCLE262_EXTRA_I_SITES)
            self.assertNotIn(site, STANDING_OTHER_TIED_SITES)
            self.assertNotIn(leftover, CYCLE253_MATCHING_SITES)
            self.assertTrue(is_contiguous_substring(GRAM3, GRAM4_PREVIOUS_000))
        for site in STANDING_OTHER_TIED_SITES:
            self.assertIn(site, STANDING_CYCLE262_SITES)
            self.assertNotIn(site, self.matching)
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(site_previous_stem_for_3gram(stems, site[2], GRAM3), "090")
            self.assertEqual(
                site_previous_4gram_for_3gram(stems, site[2], GRAM3),
                GRAM4_PREVIOUS_090,
            )
        extra = CYCLE262_EXTRA_I_SITES[0]
        extra_stems = line_stems_for_site(self.i_sides, extra)
        self.assertEqual(site_previous_stem_for_3gram(extra_stems, extra[2], GRAM3), "244")
        self.assertNotIn(extra, self.matching)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, self.matching)
        for site in CYCLE253_MATCHING_SITES:
            self.assertNotIn(site, self.matching)
            self.assertNotIn(site, STANDING_MATCHING_LEFTOVER_EXTRA_090_076_SITES)
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertTrue(STANDING_CYCLE264_PREVIOUS_090_ALREADY_LOCKED)
        self.assertTrue(STANDING_CYCLE253_FORWARD_000_IS_NOT_THIS_CYCLE)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM4_PREVIOUS_000))
            self.assertEqual(count, 2 if tablet == "I" else 0)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_OFF_I_SITES, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_264_263_262_261_260_223_207_167_scoreboards_still_compute(self):
        """Cycle 264 K_090=2, 263 14/0 N_not_hapax=2, 262 16/0 extra I=1, 261 K=15/41, 260 34/999/15, 223 69/3, 207 8/1, 167 16/0 stay."""
        prior_264 = TestMamariI999090076Previous090Scoreboard()
        prior_264.setUp()
        prior_264.test_counts_exactly_2_share_previous_090_and_hypothesis_holds()
        prior_264.test_survey_matches_computed_lock()
        self.assertEqual(prior_264.k_090, 2)
        self.assertEqual(prior_264.k_000, 2)
        self.assertEqual(prior_264.matching, CYCLE264_MATCHING_SITES)
        self.assertEqual(
            prior_264.matching,
            (
                (SIDE_IA, "Ia12", 46),
                (SIDE_IA, "Ia14", 139),
            ),
        )
        self.assertTrue(prior_264.claim_holds)
        self.assertTrue(CYCLE264_CLAIM)
        self.assertEqual(CYCLE264_K_090, 2)
        if prior_264.k_090 != 2 or not prior_264.claim_holds:
            self.fail("nested cycle 264 K_090=2 drifted")
        prior_263 = TestMamariI999090076Previous4gramsIOnlyScoreboard()
        prior_263.setUp()
        prior_263.test_shared_4grams_are_i_only_not_hapax_and_claim_loses()
        prior_263.test_survey_matches_computed_lock()
        self.assertEqual(prior_263.n_i_only, 14)
        self.assertEqual(prior_263.n_not_i_only, 0)
        self.assertEqual(prior_263.n_not_hapax, 2)
        self.assertFalse(prior_263.claim_holds)
        self.assertFalse(CYCLE263_ALL_HAPAX)
        self.assertTrue(CYCLE263_ALL_I_ONLY)
        self.assertEqual(CYCLE263_N_I_ONLY, 14)
        self.assertEqual(CYCLE263_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE263_N_NOT_HAPAX, 2)
        self.assertEqual(CYCLE263_NOT_HAPAX_SEQUENCES[0], GRAM4_PREVIOUS_000)
        self.assertEqual(CYCLE263_NOT_HAPAX_SEQUENCES[1], GRAM4_PREVIOUS_090)
        self.assertEqual(CYCLE263_NOT_HAPAX_I_SITES[0], STANDING_MATCHING_4GRAM_SITES)
        self.assertEqual(CYCLE263_NOT_HAPAX_I_SITES[1], STANDING_OTHER_TIED_4GRAM_SITES)
        if (
            prior_263.n_i_only != 14
            or prior_263.n_not_i_only != 0
            or prior_263.n_not_hapax != 2
            or prior_263.claim_holds
        ):
            self.fail("nested cycle 263 14/0 N_not_hapax=2 drifted")
        prior_262 = TestMamariI3gram999090076LeftoverExtraPreviousIOnlyScoreboard()
        prior_262.setUp()
        prior_262.test_i_hits_are_sixteen_on_ia_and_leftover_extra_999_is_subset()
        prior_262.test_3gram_is_zero_off_i_and_i_only()
        prior_262.test_survey_matches_computed_lock()
        self.assertEqual(prior_262.i_hits, 16)
        self.assertEqual(prior_262.off_i_hits, 0)
        self.assertEqual(prior_262.i_sites, CYCLE262_I_SITES)
        self.assertEqual(len(prior_262.extra), 1)
        self.assertEqual(prior_262.extra, CYCLE262_EXTRA_I_SITES)
        self.assertEqual(CYCLE262_N_I, 16)
        self.assertEqual(CYCLE262_N_OFF_I, 0)
        self.assertEqual(CYCLE262_N_EXTRA, 1)
        self.assertTrue(CYCLE262_CLAIM)
        if prior_262.i_hits != 16 or prior_262.off_i_hits != 0 or len(prior_262.extra) != 1:
            self.fail("nested cycle 262 999 090 076 leftover extra previous I-only 16/0 extra I=1 drifted")
        prior_261 = TestMamariILeftoverExtra090076Previous999Scoreboard()
        prior_261.setUp()
        prior_261.test_counts_15_of_56_and_hypothesis_k_15_holds()
        prior_261.test_survey_matches_computed_lock()
        self.assertEqual(prior_261.k_999, 15)
        self.assertEqual(CYCLE261_G, "999")
        self.assertEqual(prior_261.n_remaining_after_999, 41)
        self.assertEqual(prior_261.n_leftover_extra, 56)
        self.assertTrue(CYCLE261_CLAIM)
        if (
            prior_261.k_999 != 15
            or CYCLE261_G != "999"
            or prior_261.n_remaining_after_999 != 41
        ):
            self.fail("nested cycle 261 leftover extra previous-999 K_999=15 N_remaining=41 drifted")
        prior_260 = TestMamariILeftoverExtra090076PreviousStemScoreboard()
        prior_260.setUp()
        prior_260.test_counts_34_distinct_previous_stems_and_claim_loses()
        prior_260.test_survey_matches_computed_lock()
        self.assertEqual(prior_260.n_distinct, 34)
        self.assertEqual(CYCLE260_G, "999")
        self.assertEqual(CYCLE260_K, 15)
        self.assertFalse(CYCLE260_SHARE_ONE)
        if prior_260.n_distinct != 34 or CYCLE260_G != "999" or CYCLE260_K != 15:
            self.fail("nested cycle 260 34 distinct G=999 K=15 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, CYCLE223_OFF_I_SITES)
        self.assertEqual(CYCLE223_N_I, 69)
        self.assertEqual(CYCLE223_N_OFF_I, 3)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertEqual(prior_207.off_i_sites, CYCLE207_OFF_I_SITES)
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(CYCLE207_N_OFF_I, 1)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(prior_167.i_hits, 16)
        self.assertEqual(prior_167.off_i_hits, 0)
        self.assertEqual(prior_167.i_sites, CYCLE167_I_SITES)
        self.assertTrue(CYCLE167_CLAIM)
        self.assertEqual(CYCLE167_N_I, 16)
        self.assertEqual(CYCLE167_N_OFF_I, 0)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
        prior_220 = TestMamariI5gram999090076070000IOnlyScoreboard()
        prior_220.setUp()
        prior_220.test_5gram_is_zero_off_i_and_i_only()
        prior_220.test_survey_matches_computed_lock()
        self.assertEqual(prior_220.i_hits, 1)
        self.assertEqual(prior_220.off_i_hits, 0)
        self.assertEqual(prior_220.i_sites, CYCLE220_I_SITES)
        self.assertTrue(CYCLE220_CLAIM)
        self.assertEqual(CYCLE220_N_I, 1)
        self.assertEqual(CYCLE220_N_OFF_I, 0)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_999_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_NOT_OVERWRITTEN)
        self.assertEqual(CYCLE261_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-265 previous-000 exact-K lock."""
        lock = self.survey["i_999_090_076_previous_000"]
        self.assertEqual(lock["cycle"], 265)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 2)
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(tuple(lock["previous_4gram"]), GRAM4_PREVIOUS_000)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_I_3gram"], CYCLE262_N_I)
        self.assertEqual(lock["N_I_3gram"], 16)
        self.assertEqual(lock["N_off_I_3gram"], CYCLE262_N_OFF_I)
        self.assertEqual(lock["N_off_I_3gram"], 0)
        self.assertEqual(lock["N_extra"], STANDING_N_EXTRA)
        self.assertEqual(lock["N_extra"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["cycle262_sites"]),
            STANDING_CYCLE262_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            CYCLE262_EXTRA_I_SITES,
        )
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 16)
        self.assertEqual(lock["line_initial_sites"], [])
        self.assertEqual(tuple(lock["per_site_previous_stems"]), self.previous_stems)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "000")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertEqual(lock["K_000"], STANDING_K_000)
        self.assertEqual(lock["K_000"], 2)
        self.assertEqual(lock["K_090"], STANDING_K_090)
        self.assertEqual(lock["K_090"], 2)
        self.assertEqual(lock["largest_id_G"], STANDING_LARGEST_ID_G)
        self.assertEqual(lock["largest_id_G"], "090")
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 2)
        self.assertEqual(lock["other_tied_stem"], STANDING_OTHER_TIED_STEM)
        self.assertEqual(lock["N_without_000"], STANDING_N_WITHOUT_000)
        self.assertEqual(lock["N_without_000"], 14)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_3gram_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_4gram_sites"]),
            STANDING_MATCHING_4GRAM_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_090_076_sites"]),
            STANDING_MATCHING_LEFTOVER_EXTRA_090_076_SITES,
        )
        self.assertTrue(lock["matching_equals_cycle263_000_sites"])
        self.assertTrue(lock["matching_equals_cycle264_other_tied_sites"])
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_PREVIOUS_4GRAMS],
            lock["matching_previous_4grams"],
        )
        self.assertEqual(
            [matching_site_row_as_survey(site) for site in STANDING_MATCHING_SITES],
            lock["site_rows"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["other_tied_3gram_sites"]),
            STANDING_OTHER_TIED_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["other_tied_4gram_sites"]),
            STANDING_OTHER_TIED_4GRAM_SITES,
        )
        self.assertEqual(lock["N_I_4gram"], STANDING_N_I_4GRAM)
        self.assertEqual(lock["N_I_4gram"], 2)
        self.assertEqual(lock["N_off_I_4gram"], STANDING_N_OFF_I_4GRAM)
        self.assertEqual(lock["N_off_I_4gram"], 0)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(lock["off_i_sites"], [])
        self.assertEqual(tuple(lock["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(lock["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_999_090_076_exactly_2_share_previous_000"])
        self.assertEqual(
            lock["i_999_090_076_exactly_2_share_previous_000"],
            STANDING_I_999_090_076_EXACTLY_2_SHARE_PREVIOUS_000,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167_3gram"])
        self.assertFalse(lock["same_as_cycle235"])
        self.assertFalse(lock["same_as_cycle253"])
        self.assertFalse(lock["same_as_cycle261"])
        self.assertFalse(lock["same_as_cycle262"])
        self.assertFalse(lock["same_as_cycle263"])
        self.assertFalse(lock["same_as_cycle264"])
        self.assertTrue(lock["same_claim_shape_as_cycle235"])
        self.assertTrue(lock["same_claim_shape_as_cycle264"])
        self.assertTrue(lock["090_076_without_999_does_not_count"])
        self.assertTrue(lock["720_076_070_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["999_090_076_071_does_not_count"])
        self.assertTrue(lock["5gram_does_not_count"])
        self.assertTrue(lock["leftover_n4_057_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_remaining_after_999_is_not_this_cycle"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["cycle167_not_overwritten"])
        self.assertTrue(lock["cycle253_forward_000_is_not_this_cycle"])
        self.assertTrue(lock["cycle264_previous_090_already_locked"])
        self.assertTrue(lock["other_tied_stem_090_already_locked"])
        self.assertTrue(lock["off_i_t_sites_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertEqual(lock["nested_cycle264_K_090"], 2)
        self.assertEqual(lock["nested_cycle264_K_000"], 2)
        self.assertTrue(lock["nested_cycle264_exactly_2_share_previous_090"])
        self.assertEqual(lock["nested_cycle263_N_i_only"], 14)
        self.assertEqual(lock["nested_cycle263_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle263_N_not_hapax"], 2)
        self.assertFalse(lock["nested_cycle263_all_i_only_hapax"])
        self.assertTrue(lock["nested_cycle263_all_i_only"])
        self.assertEqual(lock["nested_cycle262_N_I"], 16)
        self.assertEqual(lock["nested_cycle262_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle262_N_extra"], 1)
        self.assertEqual(lock["nested_cycle261_K_999"], 15)
        self.assertEqual(lock["nested_cycle261_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle260_N_distinct_previous_stems"], 34)
        self.assertEqual(lock["nested_cycle260_G"], "999")
        self.assertEqual(lock["nested_cycle260_K"], 15)
        self.assertFalse(lock["nested_cycle260_share_one_previous_stem"])
        self.assertEqual(lock["nested_cycle253_K"], 2)
        self.assertEqual(lock["nested_cycle253_G"], "000")
        self.assertTrue(lock["nested_cycle253_exactly_2_share_000"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(lock["standing_i_999_090_076_previous_090_unchanged"])
        self.assertTrue(lock["standing_i_999_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_leftover_extra_previous_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_005_fwd000_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_999_090_076_previous_090"]["cycle"], 264)
        self.assertTrue(
            self.survey["i_999_090_076_previous_090"][
                "i_999_090_076_exactly_2_share_previous_090"
            ]
        )
        self.assertEqual(self.survey["i_999_090_076_previous_4grams_i_only"]["cycle"], 263)
        self.assertFalse(
            self.survey["i_999_090_076_previous_4grams_i_only"][
                "i_999_090_076_previous_4grams_all_i_only_hapax"
            ]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_leftover_extra_previous_i_only"]["cycle"], 262)
        self.assertTrue(
            self.survey["i_3gram_999_090_076_leftover_extra_previous_i_only"][
                "i_3gram_999_090_076_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["cycle"], 261)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["K_999"], 15)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_previous_999"]["N_remaining_after_999"],
            41,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_stem"]["cycle"], 260)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_previous_stem"]["N_distinct_previous_stems"],
            34,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"]["cycle"],
            253,
        )
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_after_005_fwd000"][
                "i_leftover_extra_090_076_remaining_after_005_exactly_2_share_000"
            ]
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariI999090076Previous000ImageSnapshot(unittest.TestCase):
    """Cycle 265 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
