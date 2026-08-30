"""I's leftover n=4 remaining remaining-after-011 3-grams I-only lock.

Cycle 300 text-search lock. Uses already-vendored A–V and the
cycle-298 leftover n=4 remaining remaining-after-011 I sites
of 2-gram 090 076 (the 2 leftover n=4 remaining sites whose
next token is none of 020, 087, 057, or 011). Does not retune
those leftover n=4 remaining remaining-after-011 unique-max
(cycle 298 lost: 2 hapax, G=607 K=1, N_distinct=2), leftover
n=4 remaining remaining-after-011 forward 4-grams (cycle 299
held: 2/2 hapax 1/0), leftover n=4 remaining remaining-after-
057 exactly 2 share next 011 (cycle 297), 3-gram 090 076 011
I-only (cycle 248), leftover extra remaining-after-011 (cycle
250), leftover extra remaining-after-000 3-grams (cycle 258,
including 607 extra I=1 at Ia8[106]), leftover extra
remaining-after-000 extra-I 4-grams (cycle 259, including
607), leftover extra remaining-after-000 unique next stem
(cycle 256), or leftover extra remaining-after-000 forward
4-grams (cycle 257). Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished
Ib is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Same claim-shape as cycle 258 (leftover extra remaining-
after-000 3-grams all I-only HOLD 19/19 extra I=3) after
cycle 257 leftover extra remaining-after-000 forward 4-grams
all I-only HOLD 19/19. Cycle 299 leftover n=4 remaining
remaining-after-011 forward 4-grams all I-only HOLD hapax
1/0; a 4-gram being I-only hapax does NOT imply its 3-gram
prefix is I-only (the 3-gram can appear elsewhere with a
different fourth token). That is the claim that can lose.
Nested-check leftover n=4 remaining remaining-after-011
unique-max false, N_remaining_after_011==2, K==1,
N_distinct==2, G=607 (do not retune cycle 298). Nested-check
cycle 299 remaining-after-011 forward 4-grams 2/0 hapax (do
not retune). Measure; do not assume the 3-gram prefixes are
hapax. Do not re-lock leftover extra remaining-after-000
3-grams (cycle 258), leftover extra remaining-after-000
extra-I 4-grams (cycle 259, including 607), leftover extra
remaining-after-011 (cycle 250), 3-gram 090 076 011 I-only
(cycle 248), or cycle 299 4-grams. This is leftover n=4
remaining remaining-after-011 3-grams, a different
population. Off-I T sites are this cycle only as off-I of a
remaining-after-011 3-gram if they match.

Locks exact consecutive hits of each leftover n=4 remaining
remaining-after-011 3-gram 090 076 X on tablet I and on
every other vendored tablet A–H and J–V. The two 3-grams:
090 076 607 (prefix of Ia8[106] 090 076 607 755) and
090 076 021 (prefix of Ia13[17] 090 076 021 020). Do not
assume hapax; count each from fixtures. Also count extra I:
I occurrences of that 3-gram that are not one of the
remaining-after-011 leftover n=4 remaining sites. Hypothesis:
all remaining-after-011 3-grams 090 076 X are I-only.
Measured: 090 076 607 is N_I=2 / N_off_I=0 extra I=1 at
Ia7[137] (leftover extra remaining-after-000); 090 076 021
is N_I=1 / N_off_I=0 extra I=0. N_remaining_after_011=2,
N_3grams=2, N_i_only=2, N_leak_off_i=0, extra_I_total=1.
Claim that can lose:
i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only.
True iff N_remaining_after_011==2, the two sites still
compute as remaining-after-011 leftover n=4 remaining I
090 076, and every remaining-after-011 3-gram has N_I ≥ 1
and N_off_I = 0. Extra I ≠ 0 does not make the claim lose
(still I-only); still lock extra I (cycle 258 held with
extra I=3). This can lose if any 090 076 X leaks off I
(same shape as cycle 207 090 076 070 8/1 on T), if
N_remaining_after_011 != 2, or if the two sites no longer
compute as remaining-after-011. The claim is true. Nested
overlap: Ia8[106] overlaps cycle 258 extra I=3 and cycle 259
extra-I of leftover extra remaining-after-000 607; Ia13[17]
does not. Record, do not fail the I-only claim on it.
Nested leftover n=4 remaining 13 / 4 / 9 / 3 / 6 / 2 / 4 /
2 / 2, cycle 298 unique-max false G=607 K=1 N_distinct=2,
cycle 299 4-grams 2/0 hapax, cycle 224 13/56, and cycle 223
69/3 stay. Do not assume; measure. Do not retune.

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
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    TA_LINE_NAMES,
    load_t_sides,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_999021_COVERED,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
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
from tests.test_mamari_i_3gram_090_076_011_i_only_scoreboard import (
    GRAM3 as CYCLE248_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE248_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_011_I_ONLY as CYCLE248_CLAIM,
    STANDING_I_SITES as CYCLE248_I_SITES,
    STANDING_N_EXTRA as CYCLE248_N_EXTRA,
    STANDING_N_I as CYCLE248_N_I,
    STANDING_N_OFF_I as CYCLE248_N_OFF_I,
    TestMamariI3gram090076011IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_087_i_only_scoreboard import (
    STANDING_I_3GRAM_090_076_087_I_ONLY as CYCLE245_CLAIM,
    STANDING_N_EXTRA as CYCLE245_N_EXTRA,
    STANDING_N_I as CYCLE245_N_I,
    STANDING_N_OFF_I as CYCLE245_N_OFF_I,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE258_EXTRA_I_SITES_EACH,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    STANDING_I_SITES as CYCLE258_I_SITES,
    STANDING_LEFTOVER_MATCHING_SITES as CYCLE258_LEFTOVER_MATCHING,
    STANDING_N_EXTRA_TOTAL as CYCLE258_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE258_N_I_ONLY,
    STANDING_SEQUENCES as CYCLE258_SEQUENCES,
    extra_i_sites,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_BY_X as CYCLE259_EXTRA_I_BY_X,
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_SEQUENCES as CYCLE259_SEQUENCES,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE257_CLAIM,
    STANDING_N_I_ONLY as CYCLE257_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE257_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    STANDING_G as CYCLE256_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE256_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
    TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_011_fwd005_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_011_EXACTLY_2_SHARE_005 as CYCLE250_CLAIM,
    STANDING_K as CYCLE250_K,
    TestMamariILeftoverExtra090076RemainingAfter011Fwd005Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    leftover_n4_remaining_forward_3grams,
    leftover_n4_remaining_next_4grams,
    leftover_n4_remaining_next_stems,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE299_CLAIM,
    STANDING_N_HAPAX_I_ONLY as CYCLE299_N_HAPAX_I_ONLY,
    STANDING_N_I_ONLY as CYCLE299_N_I_ONLY,
    STANDING_N_LEAK_OFF_I as CYCLE299_N_LEAK_OFF_I,
    STANDING_N_NOT_I_ONLY as CYCLE299_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE299_SEQUENCES,
    TestMamariILeftoverN4Remaining090076RemainingAfter011Fwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_next_stem_scoreboard import (
    LOCKED_FORWARD_STEMS,
    STANDING_G as CYCLE298_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE298_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_UNIQUE_NEXT_STEM as CYCLE298_CLAIM,
    STANDING_K as CYCLE298_K,
    STANDING_K_011,
    STANDING_K_020,
    STANDING_K_057,
    STANDING_K_087,
    STANDING_N_DISTINCT as CYCLE298_N_DISTINCT,
    STANDING_N_INSIDE,
    STANDING_N_REMAINING_AFTER_011,
    STANDING_N_REMAINING_AFTER_011 as CYCLE298_N_REMAINING_AFTER_011,
    STANDING_N_REMAINING_AFTER_020,
    STANDING_N_REMAINING_AFTER_057,
    STANDING_N_REMAINING_AFTER_087,
    STANDING_OVERLAP_CYCLE258_EXTRA_I,
    STANDING_OVERLAP_CYCLE259_EXTRA_I,
    STANDING_OVERLAP_DOES_NOT_LOSE,
    STANDING_REMAINING_NEXT_STEMS as CYCLE298_REMAINING_NEXT_STEMS,
    STANDING_REMAINING_SITES as CYCLE298_REMAINING_SITES,
    STANDING_TIED_STEMS as CYCLE298_TIED_STEMS,
    leftover_n4_remaining_remaining_after_011,
    leftover_n4_remaining_remaining_after_011_nested_counts_hold,
    leftover_n4_remaining_remaining_after_011_next_stems,
    leftover_n4_remaining_remaining_after_011_with_g,
    leftover_n4_remaining_remaining_after_011_without_next,
    leftover_n4_remaining_remaining_after_011_with_next,
    remaining_after_011_overlap_sites,
    select_remaining_after_011_g,
    TestMamariILeftoverN4Remaining090076RemainingAfter011NextStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_057_forward_011_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_057_EXACTLY_2_SHARE_FORWARD_011 as CYCLE297_CLAIM,
    STANDING_K_011 as CYCLE297_K_011,
    STANDING_MATCHING_SITES as CYCLE297_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_011 as CYCLE297_N_REMAINING_AFTER_011,
    TestMamariILeftoverN4Remaining090076RemainingAfter057Forward011Scoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    STANDING_MATCHING_LEFTOVERS as CYCLE222_MATCHING,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    line_stems_for_site,
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

HYPOTHESIS_ALL_I_ONLY = True
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_I = 69
STANDING_N_INSIDE_LOCK = STANDING_N_INSIDE
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_REMAINING_AFTER_011_LOCK = STANDING_N_REMAINING_AFTER_011
STANDING_REMAINING_SITES = CYCLE298_REMAINING_SITES
STANDING_REMAINING_NEXT_STEMS = CYCLE298_REMAINING_NEXT_STEMS
STANDING_SEQUENCES = tuple(
    ("090", "076", stem) for stem in STANDING_REMAINING_NEXT_STEMS
)
STANDING_N_3GRAMS = 2
STANDING_N_DISTINCT_3GRAMS = 2
STANDING_NEXT_STEMS = STANDING_REMAINING_NEXT_STEMS
STANDING_ROLES = ("leftover_n4_remaining_remaining_after_011",) * STANDING_N_3GRAMS
STANDING_N_I_EACH = (2, 1)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_I_SITES = (
    ((SIDE_IA, "Ia7", 137), (SIDE_IA, "Ia8", 106)),
    ((SIDE_IA, "Ia13", 17),),
)
STANDING_LEFTOVER_MATCHING_SITES = tuple(
    (site,) for site in STANDING_REMAINING_SITES
)
STANDING_EXTRA_I_SITES = (
    ((SIDE_IA, "Ia7", 137),),
    (),
)
STANDING_N_EXTRA_EACH = (1, 0)
STANDING_N_EXTRA_TOTAL = 1
STANDING_XS_WITH_EXTRA = ("607",)
STANDING_I_PREVIOUS_4GRAMS = (
    (("700", "090", "076", "607"), ("021", "090", "076", "607")),
    (("021", "090", "076", "021"),),
)
STANDING_I_NEXT_4GRAMS = (
    (("090", "076", "607", "073"), ("090", "076", "607", "755")),
    (("090", "076", "021", "020"),),
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0, 0)
STANDING_OFF_I_SITES = ((), ())
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET_TWO_ON_I = tuple(
    2 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (
    STANDING_HITS_BY_TABLET_TWO_ON_I,
    STANDING_HITS_BY_TABLET_ONE_ON_I,
)
STANDING_N_I_ONLY = 2
STANDING_N_NOT_I_ONLY = 0
STANDING_N_LEAK_OFF_I = 0
STANDING_LEAKING_3GRAMS = ()
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_OVERLAP_CYCLE258_EXTRA_I_607 = True
STANDING_OVERLAP_CYCLE259_EXTRA_I_607 = True
STANDING_IA13_OVERLAPS_CYCLE258_OR_259 = False
STANDING_EXTRA_I_607_IS_LEFTOVER_EXTRA_REMAINING_AFTER_000 = True
STANDING_CLAIM = (
    "i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only"
)
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_3GRAMS_ALL_I_ONLY = True
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_3GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_remaining_after_011_3grams_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE207 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE245 = False
STANDING_SAME_AS_CYCLE248 = False
STANDING_SAME_AS_CYCLE250 = False
STANDING_SAME_AS_CYCLE256 = False
STANDING_SAME_AS_CYCLE257 = False
STANDING_SAME_AS_CYCLE258 = False
STANDING_SAME_AS_CYCLE259 = False
STANDING_SAME_AS_CYCLE297 = False
STANDING_SAME_AS_CYCLE298 = False
STANDING_SAME_AS_CYCLE299 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE245 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE258 = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_I_ONLY_OF_090_076_011_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_011_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_3GRAMS_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_EXTRA_I_FWD4_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_AFTER_011_FWD4_IS_NOT_THIS_CYCLE = True
STANDING_090_076_011_DOES_NOT_COUNT = True
STANDING_090_076_070_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_ARE_THIS_CYCLE_ONLY_IF_MATCHING_3GRAM = True
STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE = True
STANDING_CYCLE299_N_I_ONLY = 2
STANDING_CYCLE299_N_HAPAX_I_ONLY = 2
STANDING_CYCLE299_N_NOT_I_ONLY = 0
STANDING_CYCLE299_N_LEAK_OFF_I = 0
STANDING_CYCLE298_N_REMAINING_AFTER_011 = 2
STANDING_CYCLE298_K = 1
STANDING_CYCLE298_G = "607"
STANDING_CYCLE298_UNIQUE = False
STANDING_CYCLE298_N_DISTINCT = 2
STANDING_CYCLE258_N_I_ONLY = 19
STANDING_CYCLE258_N_EXTRA = 3
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE223_N_OFF_I = 3
STANDING_CYCLE207_N_I = 8
STANDING_CYCLE207_N_OFF_I = 1


def remaining_after_011_3grams(
    remaining_stems: tuple[str, ...] = STANDING_REMAINING_NEXT_STEMS,
) -> tuple[tuple[str, ...], ...]:
    """3-grams 090 076 X for leftover n=4 remaining remaining-after-011 next stems."""
    return tuple(("090", "076", stem) for stem in remaining_stems)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    n_remaining: int,
    remaining_sites: tuple[tuple[str, str, int], ...],
    expected_n: int = STANDING_N_REMAINING_AFTER_011_LOCK,
    expected_sites: tuple[tuple[str, str, int], ...] = STANDING_REMAINING_SITES,
) -> bool:
    """True iff remaining-after-011 N=2 and every 3-gram is I-only.

    Extra I does not make the claim lose. Loses if any 3-gram
    appears off I, if N_remaining_after_011 != 2, or if the two
    sites no longer compute as remaining-after-011 leftover n=4
    remaining I 090 076.
    """
    return (
        n_remaining == expected_n
        and remaining_sites == expected_sites
        and len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


def leftover_n4_remaining_remaining_after_011_3gram_subset(
    leftover_site: tuple[str, str, int],
    i_sites: tuple[tuple[str, str, int], ...],
) -> bool:
    """True iff leftover n=4 remaining remaining-after-011 site ⊆ I 090 076 X."""
    return leftover_site in i_sites


def leftover_n4_remaining_remaining_after_011_3grams_subset_all(
    leftover_sites: tuple[tuple[str, str, int], ...],
    i_sites_each: tuple[tuple[tuple[str, str, int], ...], ...],
) -> bool:
    """True iff every remaining-after-011 site sits in its I 3-gram sites."""
    if len(leftover_sites) != len(i_sites_each):
        return False
    return all(
        leftover_n4_remaining_remaining_after_011_3gram_subset(site, sites)
        for site, sites in zip(leftover_sites, i_sites_each, strict=True)
    )


class TestILeftoverN4Remaining090076RemainingAfter0113gramsIOnlyHelpers(
    unittest.TestCase
):
    """Helpers on leftover n=4 remaining remaining-after-011 3-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 3-gram counts; a gap is not a hit. Locked 011 / 070 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "607"))
        self.assertEqual(STANDING_SEQUENCES[1], ("090", "076", "021"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_3GRAMS)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_DISTINCT_3GRAMS)
        self.assertEqual(remaining_after_011_3grams(), STANDING_SEQUENCES)
        for gram, nxt in zip(STANDING_SEQUENCES, STANDING_NEXT_STEMS, strict=True):
            self.assertEqual(gram[:2], GRAM2)
            self.assertEqual(gram[2], nxt)
            self.assertEqual(len(gram), STANDING_N3)
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS)
            self.assertNotEqual(gram, CYCLE248_GRAM3)
            self.assertNotEqual(gram, CYCLE207_GRAM3)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["090", "076", "607", "090", "076", "607"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [
            list(STANDING_SEQUENCES[0][:2])
            + ["006"]
            + list(STANDING_SEQUENCES[0][2:])
        ]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(
            ngram_hit_count([list(CYCLE248_GRAM3)], STANDING_SEQUENCES[0]), 0
        )
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(
            ngram_hit_count([list(CYCLE207_GRAM3)], STANDING_SEQUENCES[0]), 0
        )
        self.assertEqual(
            ngram_hit_count([["090", "076", "011"]], STANDING_SEQUENCES[0]), 0
        )
        planted = ["999", "021", "090", "076", "607", "755"]
        self.assertEqual(
            site_forward_3gram(planted, 2, GRAM2), STANDING_SEQUENCES[0]
        )
        self.assertEqual(site_next_4gram(planted, 2, GRAM2), CYCLE299_SEQUENCES[0])
        no_next = ["087", "078", "090", "076"]
        self.assertIsNone(site_forward_3gram(no_next, 2, GRAM2))
        self.assertTrue(STANDING_090_076_011_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_zero_off_i_and_n2(self):
        """Boolean is True only when N=2 and both 3-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
                hold_ones,
                hold_zeros,
                STANDING_N_REMAINING_AFTER_011_LOCK,
                STANDING_REMAINING_SITES,
            )
        )
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
                (3, 1),
                hold_zeros,
                STANDING_N_REMAINING_AFTER_011_LOCK,
                STANDING_REMAINING_SITES,
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
                hold_ones,
                (1, 0),
                STANDING_N_REMAINING_AFTER_011_LOCK,
                STANDING_REMAINING_SITES,
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
                (0, 1),
                hold_zeros,
                STANDING_N_REMAINING_AFTER_011_LOCK,
                STANDING_REMAINING_SITES,
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
                hold_ones,
                hold_zeros,
                1,
                STANDING_REMAINING_SITES,
            )
        )
        drifted = ((SIDE_IA, "Ia2", 107), (SIDE_IA, "Ia14", 54))
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
                hold_ones,
                hold_zeros,
                STANDING_N_REMAINING_AFTER_011_LOCK,
                drifted,
            )
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
                (),
                (),
                0,
                (),
            )
        )
        self.assertTrue(STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertEqual(STANDING_N_EXTRA_TOTAL, 1)
        self.assertTrue(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_3GRAMS_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_3GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertFalse(CYCLE207_GRAM3[2] in STANDING_NEXT_STEMS)
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(CYCLE207_N_OFF_I, 1)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        self.assertTrue(CYCLE245_CLAIM)
        self.assertEqual(CYCLE245_N_EXTRA, 3)
        self.assertEqual(provider.get_call_history(), [])

    def test_leftover_matching_subset_and_extra_can_be_nonempty(self):
        """Remaining-after-011 site ⊆ I sites; extra I of 607 is nonempty."""
        provider = MockProvider()
        self.assertTrue(
            leftover_n4_remaining_remaining_after_011_3grams_subset_all(
                STANDING_REMAINING_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertEqual(STANDING_N_EXTRA_EACH[0], 1)
        self.assertEqual(STANDING_N_EXTRA_EACH[1], 0)
        self.assertEqual(sum(STANDING_N_EXTRA_EACH), STANDING_N_EXTRA_TOTAL)
        self.assertEqual(
            extra_i_sites(STANDING_I_SITES[0], STANDING_LEFTOVER_MATCHING_SITES[0]),
            STANDING_EXTRA_I_SITES[0],
        )
        self.assertEqual(
            extra_i_sites(STANDING_I_SITES[1], STANDING_LEFTOVER_MATCHING_SITES[1]),
            STANDING_EXTRA_I_SITES[1],
        )
        self.assertEqual(STANDING_EXTRA_I_SITES[0], ((SIDE_IA, "Ia7", 137),))
        self.assertEqual(STANDING_EXTRA_I_SITES[1], ())
        self.assertIn(STANDING_EXTRA_I_SITES[0][0], STANDING_LEFTOVER_SITES)
        self.assertNotIn(STANDING_EXTRA_I_SITES[0][0], STANDING_INSIDE_SITES)
        self.assertEqual(CYCLE258_SEQUENCES[13], ("090", "076", "607"))
        self.assertEqual(CYCLE258_LEFTOVER_MATCHING[13], STANDING_EXTRA_I_SITES[0])
        self.assertEqual(
            CYCLE258_EXTRA_I_SITES_EACH[13],
            ((SIDE_IA, "Ia8", 106),),
        )
        planted_extra = STANDING_REMAINING_SITES + ((SIDE_IA, "Ia1", 0),)
        self.assertFalse(
            leftover_n4_remaining_remaining_after_011_3grams_subset_all(
                planted_extra,
                STANDING_I_SITES,
            )
        )
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter0113gramsIOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining remaining-after-011 3-gram off-I lock."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.inside_sites = STANDING_INSIDE_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.next_stems = leftover_n4_remaining_next_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.leftover_next_4grams = leftover_n4_remaining_next_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.forwards = leftover_n4_remaining_forward_3grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.remaining = leftover_n4_remaining_remaining_after_011(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_stems = leftover_n4_remaining_remaining_after_011_next_stems(
            self.inside_sites,
            self.next_stems,
        )
        self.with_next = leftover_n4_remaining_remaining_after_011_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next = leftover_n4_remaining_remaining_after_011_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.grams = remaining_after_011_3grams(self.remaining_stems)
        self.i_sites = tuple(nge4_sites(gram, self.i_sides) for gram in self.grams)
        self.n_i = tuple(
            ngram_hit_count(self.i_sides[SIDE_IA], gram) + STANDING_IB_HITS
            for gram in self.grams
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in self.grams
        )
        self.off_i = tuple(
            tablet_hit_counts(self.by_tablet, gram, OFF_I_TABLETS)
            for gram in self.grams
        )
        self.n_off_i = tuple(sum(row) for row in self.off_i)
        self.leftover_matching = tuple(
            leftover_n4_remaining_remaining_after_011_with_g(
                self.inside_sites,
                self.next_stems,
                stem,
            )
            for stem in self.remaining_stems
        )
        self.extra = tuple(
            extra_i_sites(sites, matching)
            for sites, matching in zip(
                self.i_sites,
                self.leftover_matching,
                strict=True,
            )
        )
        self.n_extra = tuple(len(row) for row in self.extra)
        self.g, self.k, self.unique = select_remaining_after_011_g(
            self.remaining_stems
        )
        self.n_remaining = len(self.remaining)
        self.overlap_258 = remaining_after_011_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_259 = remaining_after_011_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_258_607 = remaining_after_011_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_BY_X["607"],
        )
        self.overlap_259_607 = remaining_after_011_overlap_sites(
            self.remaining,
            CYCLE259_EXTRA_I_BY_X["607"],
        )
        self.claim_holds = (
            i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
                self.n_i,
                self.n_off_i,
                self.n_remaining,
                self.remaining,
            )
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = len(self.grams) - self.n_i_only
        self.n_leak_off_i = sum(1 for off in self.n_off_i if off > 0)
        self.leaking = tuple(
            gram
            for gram, on, off in zip(self.grams, self.n_i, self.n_off_i, strict=True)
            if not sequence_is_i_only(on, off)
        )

    def test_tokens_and_sites_are_cycle_298_remaining_after_011_not_retuned(self):
        """3-grams stay the cycle-298 remaining-after-011 X. Nested 2/K=1/G=607 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(len(self.inside_sites), STANDING_N_INSIDE_LOCK)
        self.assertEqual(STANDING_N_INSIDE_LOCK, CYCLE224_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE_LOCK, 13)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE298_REMAINING_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_NEXT_STEMS)
        self.assertEqual(len(self.remaining), STANDING_N_REMAINING_AFTER_011_LOCK)
        self.assertEqual(STANDING_N_REMAINING_AFTER_011_LOCK, 2)
        self.assertEqual(len(set(self.remaining_stems)), CYCLE298_N_DISTINCT)
        self.assertEqual(self.g, CYCLE298_G)
        self.assertEqual(self.g, "607")
        self.assertEqual(self.k, CYCLE298_K)
        self.assertEqual(self.k, 1)
        self.assertFalse(self.unique)
        self.assertFalse(CYCLE298_UNIQUE)
        self.assertFalse(CYCLE298_CLAIM)
        if (
            len(self.remaining) != 2
            or self.k != 1
            or self.g != "607"
            or self.unique
            or CYCLE298_CLAIM
        ):
            self.fail(
                "nested cycle 298 unique-max false N_remaining_after_011=2 K=1 G=607 drifted"
            )
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(len(self.grams), STANDING_N_3GRAMS)
        self.assertEqual(STANDING_N_3GRAMS, 2)
        self.assertEqual(len(set(self.grams)), STANDING_N_DISTINCT_3GRAMS)
        self.assertTrue(all(stem is not None for stem in self.remaining_stems))
        self.assertEqual(self.with_next, self.remaining)
        self.assertEqual(self.no_next, ())
        self.assertTrue(
            leftover_n4_remaining_remaining_after_011_nested_counts_hold(
                13,
                4,
                9,
                3,
                6,
                2,
                4,
                2,
                2,
            )
        )
        self.assertEqual(STANDING_K_020, 4)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(STANDING_K_087, 3)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(STANDING_K_057, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, 4)
        self.assertEqual(STANDING_K_011, 2)
        for nxt in self.remaining_stems:
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS)
        prior_299 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_011_fwd4_i_only"
        ]
        self.assertEqual(prior_299["cycle"], 299)
        self.assertEqual(prior_299["N_i_only"], 2)
        self.assertEqual(prior_299["N_hapax_i_only"], 2)
        self.assertEqual(prior_299["N_leak_off_i"], 0)
        self.assertTrue(
            prior_299[
                "i_leftover_n4_remaining_090_076_remaining_after_011_forward_4grams_all_i_only"
            ]
        )
        self.assertTrue(CYCLE299_CLAIM)
        self.assertEqual(CYCLE299_SEQUENCES[0][:3], STANDING_SEQUENCES[0])
        self.assertEqual(CYCLE299_SEQUENCES[1][:3], STANDING_SEQUENCES[1])
        prior_298 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_011_next_stem"
        ]
        self.assertEqual(prior_298["cycle"], 298)
        self.assertEqual(prior_298["N_remaining_after_011"], 2)
        self.assertEqual(prior_298["K"], 1)
        self.assertEqual(prior_298["G"], "607")
        self.assertEqual(prior_298["N_distinct"], 2)
        self.assertFalse(prior_298["G_uniquely_most_frequent"])
        self.assertFalse(
            prior_298[
                "i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem"
            ]
        )
        prior_258 = self.survey[
            "i_leftover_extra_090_076_remaining_after_000_3grams_i_only"
        ]
        self.assertEqual(prior_258["cycle"], 258)
        self.assertEqual(prior_258["N_i_only"], 19)
        self.assertEqual(prior_258["N_extra_total"], 3)
        self.assertTrue(
            prior_258["i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only"]
        )
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_3gram_lock_extra_i_and_claim_holds(self):
        """Each remaining-after-011 3-gram is I-only. Extra I=1 does not lose."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (2, 1))
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0, 0))
        self.assertEqual(self.n_extra, STANDING_N_EXTRA_EACH)
        self.assertEqual(self.extra, STANDING_EXTRA_I_SITES)
        self.assertEqual(sum(self.n_extra), STANDING_N_EXTRA_TOTAL)
        self.assertEqual(STANDING_N_EXTRA_TOTAL, 1)
        self.assertEqual(self.leaking, STANDING_LEAKING_3GRAMS)
        self.assertEqual(self.leaking, ())
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_i_only, 2)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_not_i_only, 0)
        self.assertEqual(self.n_leak_off_i, STANDING_N_LEAK_OFF_I)
        self.assertEqual(self.n_leak_off_i, 0)
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from 0")
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked remaining-after-011 3-grams")
        if self.leaking:
            self.fail("measured remaining-after-011 3-grams leaked off I")
        if self.extra != STANDING_EXTRA_I_SITES:
            self.fail("extra I leftover-of-leftover sites drifted")
        if self.n_remaining != 2:
            self.fail("measured N_remaining_after_011 drifted from 2")
        self.assertTrue(
            leftover_n4_remaining_remaining_after_011_3grams_subset_all(
                self.remaining,
                self.i_sites,
            )
        )
        for site, gram, nxt, role, sites, matching, extra, n_on, n_off, n_ex, prevs, nexts in zip(
            STANDING_REMAINING_SITES,
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_LEFTOVER_MATCHING_SITES,
            STANDING_EXTRA_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_N_EXTRA_EACH,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(matching, (site,))
            self.assertIn(site, sites)
            self.assertEqual(extra_i_sites(sites, matching), extra)
            self.assertEqual(len(extra), n_ex)
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N3]), gram)
            self.assertEqual(stems[site[2] + STANDING_N2], nxt)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N2]), GRAM2)
            self.assertEqual(site_forward_3gram(stems, site[2], GRAM2), gram)
            self.assertEqual(
                site_next_4gram(stems, site[2], GRAM2), nexts[sites.index(site)]
            )
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS)
            self.assertEqual(role, "leftover_n4_remaining_remaining_after_011")
            self.assertGreaterEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertNotEqual(gram, CYCLE248_GRAM3)
            self.assertNotEqual(gram, CYCLE207_GRAM3)
            for i_site, prev4, nxt4 in zip(sites, prevs, nexts, strict=True):
                line = line_stems_for_site(self.i_sides, i_site)
                idx = i_site[2]
                self.assertEqual(tuple(line[idx : idx + STANDING_N3]), gram)
                self.assertEqual(tuple(line[idx - 1 : idx + STANDING_N3]), prev4)
                self.assertEqual(site_next_4gram(line, idx, GRAM2), nxt4)
                if i_site != site:
                    self.assertIn(i_site, STANDING_LEFTOVER_SITES)
                    self.assertNotIn(i_site, STANDING_INSIDE_SITES)
        self.assertEqual(STANDING_XS_WITH_EXTRA, ("607",))
        self.assertIn((SIDE_IA, "Ia8", 106), STANDING_LEFTOVER_999021_COVERED)
        self.assertIn((SIDE_IA, "Ia13", 17), STANDING_LEFTOVER_999021_COVERED)
        self.assertIn(("999", "021", "090", "076"), CYCLE222_MATCHING)
        self.assertTrue(STANDING_EXTRA_I_607_IS_LEFTOVER_EXTRA_REMAINING_AFTER_000)
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        if not self.claim_holds:
            self.fail("measured remaining-after-011 3-grams are not all I-only")
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_EXTRA_I_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off, n_on, expected in zip(
            self.hits_by_tablet,
            self.off_i,
            self.n_i,
            STANDING_HITS_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
            self.assertEqual(hits, expected)
            self.assertEqual(hits[VENDORED_TABLETS.index("I")], n_on)
            self.assertEqual(sum(hits) - n_on, 0)
        t_sides = load_t_sides()
        self.assertEqual(
            CYCLE223_OFF_I_SITES,
            (
                (SIDE_TA, "Ta5", 9),
                (SIDE_TA, "Ta7", 5),
                (SIDE_TA, "Ta9", 2),
            ),
        )
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
            self.assertNotIn(following, STANDING_SEQUENCES)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertEqual(
            i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only(
                self.n_i,
                self.n_off_i,
                self.n_remaining,
                self.remaining,
            ),
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_3GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE258)
        self.assertFalse(STANDING_SAME_AS_CYCLE299)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE258)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_090_076_011_DOES_NOT_COUNT)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_011_IS_NOT_THIS_CYCLE)
        self.assertTrue(
            STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_3GRAMS_IS_NOT_THIS_CYCLE
        )
        self.assertTrue(
            STANDING_LEFTOVER_EXTRA_REMAINING_AFTER_000_EXTRA_I_FWD4_IS_NOT_THIS_CYCLE
        )
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_AFTER_011_FWD4_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        for site in CYCLE297_MATCHING_SITES:
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        for site in CYCLE223_OFF_I_SITES:
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        self.assertIn(STANDING_SEQUENCES[0], CYCLE258_SEQUENCES)
        self.assertNotIn(STANDING_SEQUENCES[1], CYCLE258_SEQUENCES)
        self.assertEqual(CYCLE299_SEQUENCES[0][:3], STANDING_SEQUENCES[0])
        self.assertEqual(CYCLE259_SEQUENCES[0][:3], STANDING_SEQUENCES[0])
        self.assertNotEqual(CYCLE299_SEQUENCES[0], STANDING_SEQUENCES[0])
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_overlap_cycle258_259_extra_i_recorded_does_not_lose(self):
        """Ia8[106] overlaps cycle 258/259 extra I 607; Ia13[17] does not. Record, do not fail."""
        self.assertEqual(self.overlap_258, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_258_607, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259_607, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_258, ((SIDE_IA, "Ia8", 106),))
        self.assertTrue(STANDING_OVERLAP_CYCLE258_EXTRA_I_607)
        self.assertTrue(STANDING_OVERLAP_CYCLE259_EXTRA_I_607)
        self.assertFalse(STANDING_IA13_OVERLAPS_CYCLE258_OR_259)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE259_EXTRA_I_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE259_EXTRA_I_BY_X["607"])
        self.assertNotIn((SIDE_IA, "Ia13", 17), CYCLE259_EXTRA_I_SITES)
        self.assertNotIn((SIDE_IA, "Ia13", 17), CYCLE259_EXTRA_I_BY_X["607"])
        self.assertNotIn((SIDE_IA, "Ia13", 17), CYCLE259_EXTRA_I_BY_X["057"])
        self.assertEqual(CYCLE258_EXTRA_I_SITES_EACH[13], ((SIDE_IA, "Ia8", 106),))
        self.assertEqual(CYCLE258_I_SITES[13], STANDING_I_SITES[0])
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(self.claim_holds)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        self.assertEqual(len(CYCLE259_EXTRA_I_SITES), 3)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertTrue(CYCLE259_CLAIM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_299_298_297_258_259_250_248_224_223_still_compute(self):
        """Cycle 299 2/0 hapax, 298 unique-max lose, 297 K_011=2, 258 19/0 extra I=3, 259 extra-I, 250 leftover extra 005, 248 4/0, 224 13/56, 223 69/3 stay."""
        prior_299 = TestMamariILeftoverN4Remaining090076RemainingAfter011Fwd4IOnlyScoreboard()
        prior_299.setUp()
        prior_299.test_each_4gram_is_one_on_i_zero_off_i_no_line_final_and_claim_holds()
        prior_299.test_survey_matches_computed_lock()
        self.assertEqual(prior_299.n_i_only, 2)
        self.assertEqual(prior_299.n_hapax_i_only, 2)
        self.assertEqual(prior_299.n_not_i_only, 0)
        self.assertEqual(prior_299.n_leak_off_i, 0)
        self.assertTrue(prior_299.claim_holds)
        self.assertTrue(CYCLE299_CLAIM)
        self.assertEqual(CYCLE299_N_I_ONLY, 2)
        self.assertEqual(CYCLE299_N_HAPAX_I_ONLY, 2)
        self.assertEqual(CYCLE299_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE299_N_LEAK_OFF_I, 0)
        if (
            prior_299.n_i_only != 2
            or prior_299.n_hapax_i_only != 2
            or prior_299.n_not_i_only != 0
        ):
            self.fail(
                "nested cycle 299 leftover n=4 remaining remaining-after-011 forward 4-grams 2/0 hapax drifted"
            )
        prior_298 = TestMamariILeftoverN4Remaining090076RemainingAfter011NextStemScoreboard()
        prior_298.setUp()
        prior_298.test_counts_2_remaining_g_607_k_1_hapax_and_hypothesis_loses()
        prior_298.test_survey_matches_computed_lock()
        self.assertEqual(prior_298.n_remaining, 2)
        self.assertEqual(prior_298.k, 1)
        self.assertEqual(prior_298.g, "607")
        self.assertEqual(prior_298.n_distinct, 2)
        self.assertFalse(prior_298.unique)
        self.assertFalse(prior_298.claim_holds)
        self.assertFalse(CYCLE298_CLAIM)
        self.assertEqual(CYCLE298_N_REMAINING_AFTER_011, 2)
        self.assertEqual(CYCLE298_K, 1)
        self.assertEqual(CYCLE298_G, "607")
        self.assertEqual(CYCLE298_N_DISTINCT, 2)
        if (
            prior_298.n_remaining != 2
            or prior_298.k != 1
            or prior_298.g != "607"
            or prior_298.unique
            or prior_298.n_distinct != 2
        ):
            self.fail(
                "nested cycle 298 unique-max false N_remaining_after_011=2 K=1 G=607 drifted"
            )
        prior_297 = TestMamariILeftoverN4Remaining090076RemainingAfter057Forward011Scoreboard()
        prior_297.setUp()
        prior_297.test_counts_2_of_4_and_hypothesis_k_2_holds()
        prior_297.test_survey_matches_computed_lock()
        self.assertEqual(prior_297.k_011, 2)
        self.assertEqual(prior_297.n_remaining_after_011, 2)
        self.assertEqual(prior_297.matching, CYCLE297_MATCHING_SITES)
        self.assertTrue(prior_297.claim_holds)
        self.assertTrue(CYCLE297_CLAIM)
        self.assertEqual(CYCLE297_K_011, 2)
        self.assertEqual(CYCLE297_N_REMAINING_AFTER_011, 2)
        if prior_297.k_011 != 2 or prior_297.n_remaining_after_011 != 2:
            self.fail(
                "nested cycle 297 leftover n=4 remaining remaining-after-057 exactly 2 share 011 drifted"
            )
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_258.test_survey_matches_computed_lock()
        self.assertTrue(prior_258.claim_holds)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertEqual(CYCLE258_N_I_ONLY, 19)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        if prior_258.n_i_only != 19 or sum(prior_258.n_extra) != 3:
            self.fail(
                "nested cycle 258 leftover extra remaining-after-000 3-grams 19/0 extra I=3 drifted"
            )
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_259.test_survey_matches_computed_lock()
        self.assertTrue(prior_259.claim_holds)
        self.assertTrue(CYCLE259_CLAIM)
        prior_257 = TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard()
        prior_257.setUp()
        prior_257.test_each_4gram_is_one_on_i_zero_off_i_no_line_final_and_claim_holds()
        prior_257.test_survey_matches_computed_lock()
        self.assertEqual(prior_257.n_i_only, 19)
        self.assertEqual(prior_257.n_not_i_only, 0)
        self.assertTrue(prior_257.claim_holds)
        self.assertTrue(CYCLE257_CLAIM)
        self.assertEqual(CYCLE257_N_I_ONLY, 19)
        self.assertEqual(CYCLE257_N_NOT_I_ONLY, 0)
        prior_256 = TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard()
        prior_256.setUp()
        prior_256.test_counts_19_remaining11_all_hapax_g_755_k_1_and_hypothesis_loses()
        prior_256.test_survey_matches_computed_lock()
        self.assertEqual(prior_256.n_remaining11, 19)
        self.assertEqual(prior_256.k, 1)
        self.assertEqual(prior_256.g, "755")
        self.assertFalse(prior_256.unique)
        self.assertFalse(prior_256.claim_holds)
        self.assertFalse(CYCLE256_CLAIM)
        self.assertEqual(CYCLE256_N_REMAINING11, 19)
        self.assertEqual(CYCLE256_K, 1)
        self.assertEqual(CYCLE256_G, "755")
        self.assertFalse(CYCLE256_UNIQUE)
        prior_250 = TestMamariILeftoverExtra090076RemainingAfter011Fwd005Scoreboard()
        prior_250.setUp()
        prior_250.test_survey_matches_computed_lock()
        self.assertTrue(CYCLE250_CLAIM)
        self.assertEqual(CYCLE250_K, 2)
        prior_248 = TestMamariI3gram090076011IOnlyScoreboard()
        prior_248.setUp()
        prior_248.test_3gram_is_zero_off_i_and_i_only()
        prior_248.test_survey_matches_computed_lock()
        self.assertEqual(prior_248.i_hits, CYCLE248_N_I)
        self.assertEqual(prior_248.i_hits, 4)
        self.assertEqual(prior_248.off_i_hits, CYCLE248_N_OFF_I)
        self.assertEqual(prior_248.off_i_hits, 0)
        self.assertEqual(len(prior_248.extra), CYCLE248_N_EXTRA)
        self.assertEqual(len(prior_248.extra), 2)
        self.assertEqual(prior_248.extra, CYCLE248_EXTRA_I_SITES)
        self.assertEqual(prior_248.i_sites, CYCLE248_I_SITES)
        self.assertTrue(prior_248.claim_holds)
        self.assertTrue(CYCLE248_CLAIM)
        if prior_248.i_hits != 4 or prior_248.off_i_hits != 0:
            self.fail("nested cycle 248 090 076 011 I-only 4/0 extra I=2 drifted")
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(CYCLE224_N_LEFTOVER, 56)
        if CYCLE224_N_INSIDE != 13 or CYCLE224_N_LEFTOVER != 56:
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
        self.assertEqual(len(CYCLE223_I_SITES), 69)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_sites, CYCLE207_OFF_I_SITES)
        self.assertFalse(prior_207.claim_holds)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-300 remaining-after-011 3-gram I-only lock."""
        lock = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_011_3grams_i_only"
        ]
        self.assertEqual(lock["cycle"], 300)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE_LOCK)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(lock["N_remaining_after_011"], STANDING_N_REMAINING_AFTER_011_LOCK)
        self.assertEqual(lock["N_remaining_after_011"], 2)
        self.assertEqual(lock["N_3grams"], STANDING_N_3GRAMS)
        self.assertEqual(lock["N_3grams"], 2)
        self.assertEqual(lock["N_distinct_3grams"], STANDING_N_DISTINCT_3GRAMS)
        self.assertEqual(lock["K"], 1)
        self.assertEqual(lock["G"], "607")
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertFalse(
            lock["i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem"]
        )
        self.assertEqual(lock["N_distinct"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_011_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_011_next_stems"]),
            STANDING_REMAINING_NEXT_STEMS,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["remaining_after_011_3grams"],
        )
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_3GRAMS)
        for row, gram, site, nxt, role, sites, matching, extra, n_on, n_off, n_ex, prevs, nexts, hits in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_REMAINING_SITES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_LEFTOVER_MATCHING_SITES,
            STANDING_EXTRA_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_N_EXTRA_EACH,
            STANDING_I_PREVIOUS_4GRAMS,
            STANDING_I_NEXT_4GRAMS,
            STANDING_HITS_BY_TABLET,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens3"]), gram)
            self.assertEqual(tuple(row["cycle298_site"]), site)
            self.assertEqual(row["next_stem"], nxt)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["ia_hits"], n_on)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["leftover_n4_remaining_remaining_after_011_sites"]),
                matching,
            )
            self.assertTrue(row["leftover_n4_remaining_remaining_after_011_subset_of_i_sites"])
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["extra_i_sites"]),
                extra,
            )
            self.assertEqual(row["N_extra"], n_ex)
            self.assertEqual(
                [list(gram4) for gram4 in prevs],
                row["i_previous_4grams"],
            )
            self.assertEqual(
                [list(gram4) for gram4 in nexts],
                row["i_next_4grams"],
            )
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(row["off_i_tablets_with_hits"], [])
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(tuple(row["hits_by_tablet"]), hits)
            self.assertTrue(row["i_only"])
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(tuple(lock["N_extra_each"]), STANDING_N_EXTRA_EACH)
        self.assertEqual(lock["N_extra_total"], 1)
        self.assertEqual(tuple(lock["xs_with_extra"]), STANDING_XS_WITH_EXTRA)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_n4_remaining_090_076_remaining_after_011_3grams_all_i_only"]
        )
        self.assertTrue(
            lock["i_leftover_n4_remaining_090_076_remaining_after_011_3grams_i_only"]
        )
        self.assertEqual(lock["N_i_only"], 2)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["N_leak_off_i"], 0)
        self.assertEqual(lock["leaking_3grams"], [])
        self.assertTrue(lock["extra_i_does_not_make_claim_lose"])
        self.assertTrue(lock["extra_i_607_is_leftover_extra_remaining_after_000"])
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE258_EXTRA_I],
            lock["overlap_cycle258_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE259_EXTRA_I],
            lock["overlap_cycle259_extra_i_sites"],
        )
        self.assertTrue(lock["overlap_cycle258_extra_i_607"])
        self.assertTrue(lock["overlap_cycle259_extra_i_607"])
        self.assertFalse(lock["ia13_overlaps_cycle258_or_259"])
        self.assertTrue(lock["overlap_does_not_lose"])
        self.assertEqual(lock["nested_leftover_n4_remaining"], [13, 4, 9, 3, 6, 2, 4, 2, 2])
        self.assertEqual(lock["nested_cycle299_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle299_N_hapax_i_only"], 2)
        self.assertEqual(lock["nested_cycle299_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle299_N_leak_off_i"], 0)
        self.assertEqual(lock["nested_cycle298_N_remaining_after_011"], 2)
        self.assertEqual(lock["nested_cycle298_K"], 1)
        self.assertEqual(lock["nested_cycle298_G"], "607")
        self.assertEqual(lock["nested_cycle298_N_distinct"], 2)
        self.assertFalse(lock["nested_cycle298_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle297_K_011"], 2)
        self.assertEqual(lock["nested_cycle297_N_remaining_after_011"], 2)
        self.assertEqual(lock["nested_cycle258_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle258_N_extra"], 3)
        self.assertEqual(lock["nested_cycle259_N_extra_i"], 3)
        self.assertEqual(lock["nested_cycle257_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle257_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle256_N_remaining11"], 19)
        self.assertEqual(lock["nested_cycle256_K"], 1)
        self.assertEqual(lock["nested_cycle256_G"], "755")
        self.assertFalse(lock["nested_cycle256_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle250_K"], 2)
        self.assertEqual(lock["nested_cycle248_N_I"], 4)
        self.assertEqual(lock["nested_cycle248_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle248_N_extra"], 2)
        self.assertEqual(lock["nested_cycle245_N_I"], 5)
        self.assertEqual(lock["nested_cycle245_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle245_N_extra"], 3)
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(tuple(lock["nested_cycle207_off_i_sites"][0]), CYCLE207_OFF_I_SITES[0])
        self.assertEqual(lock["nested_cycle171_N_I"], 43)
        self.assertEqual(lock["nested_cycle171_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle207"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle245"])
        self.assertFalse(lock["same_as_cycle248"])
        self.assertFalse(lock["same_as_cycle250"])
        self.assertFalse(lock["same_as_cycle256"])
        self.assertFalse(lock["same_as_cycle257"])
        self.assertFalse(lock["same_as_cycle258"])
        self.assertFalse(lock["same_as_cycle259"])
        self.assertFalse(lock["same_as_cycle297"])
        self.assertFalse(lock["same_as_cycle298"])
        self.assertFalse(lock["same_as_cycle299"])
        self.assertTrue(lock["same_claim_shape_as_cycle207"])
        self.assertTrue(lock["same_claim_shape_as_cycle245"])
        self.assertTrue(lock["same_claim_shape_as_cycle258"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["i_only_of_090_076_011_is_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_remaining_after_011_is_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_remaining_after_000_3grams_is_not_this_cycle"])
        self.assertTrue(
            lock["leftover_extra_remaining_after_000_extra_i_fwd4_is_not_this_cycle"]
        )
        self.assertTrue(lock["leftover_n4_remaining_after_011_fwd4_is_not_this_cycle"])
        self.assertTrue(lock["090_076_011_does_not_count"])
        self.assertTrue(lock["090_076_070_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_are_this_cycle_only_if_matching_3gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_090_076_remaining_after_011_fwd4_i_only_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_090_076_remaining_after_011_next_stem_unchanged"
            ]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_n4_remaining_090_076_remaining_after_057_forward_011_unchanged"
            ]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_unchanged"]
        )
        self.assertTrue(
            lock[
                "standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"
            ]
        )
        self.assertTrue(lock["standing_i_3gram_090_076_011_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"]
        )
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey[
                "i_leftover_n4_remaining_090_076_remaining_after_011_fwd4_i_only"
            ]["cycle"],
            299,
        )
        self.assertTrue(
            self.survey[
                "i_leftover_n4_remaining_090_076_remaining_after_011_fwd4_i_only"
            ][
                "i_leftover_n4_remaining_090_076_remaining_after_011_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(
            self.survey[
                "i_leftover_n4_remaining_090_076_remaining_after_011_next_stem"
            ]["cycle"],
            298,
        )
        self.assertFalse(
            self.survey[
                "i_leftover_n4_remaining_090_076_remaining_after_011_next_stem"
            ]["i_leftover_n4_remaining_090_076_remaining_after_011_unique_next_stem"]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"][
                "cycle"
            ],
            258,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter0113gramsIOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 300 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
