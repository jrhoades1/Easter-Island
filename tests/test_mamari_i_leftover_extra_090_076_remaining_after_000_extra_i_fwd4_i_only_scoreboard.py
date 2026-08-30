"""I's cycle-258 leftover extra remaining-after-000 extra-I forward-4 lock.

Cycle 259 text-search lock. Uses already-vendored A–V and the
cycle-258 leftover extra remaining-after-000 extra I sites of
3-grams 090 076 057 and 090 076 607 (the 3 I sites of those
3-grams that are not leftover extra remaining-after-000).
Does not retune leftover extra remaining-after-000 unique-max
(cycle 256 lost: 19 hapax, G=755 K=1), leftover extra
remaining-after-000 forward 4-grams (cycle 257 held: 19/19
hapax 1/0 of the 19 remaining-after-000 SITES only), leftover
extra remaining-after-000 3-grams (cycle 258 held: 19/19
I-only, extra I=3), leftover extra remaining-after-005 G=000
K=2, leftover extra remaining-after-001 unique-max (cycle 234
lost), leftover extra remaining 071, leftover extra forward
070, leftover extra sites, leftover n=4, or the already-closed
leftover remaining family. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new
agents. Not a meaning dictionary.

Cycle 257 locked 4-grams of the 19 leftover extra
remaining-after-000 SITES only. Extra I sites of 090 076 057
and 090 076 607 are leftover-of-leftover; their forward
4-grams were not locked. Extra I of 057 is two sites of
leftover n=4 remaining 090 076 057 600 (shared 4th token
600, so NOT hapax). Extra I of 607 is one site after leftover
n=4 remaining 999 021 090 076 (4-gram 090 076 607 Y). Do not
confuse with already-locked remaining-after-000 site 4-grams
090 076 607 073 and 090 076 057 240. Do not peel leftover
extra I 090 076 previous stems this cycle. Do not retune
leftover n=4.

Same claim-shape as cycle 207 (090 076 070 lost 8/1 on T)
and cycle 219 (090 076 070 000 leaking on T). Cycle 258
remaining-after-000 3-grams all I-only 19/19 extra I=3,
cycle 257 remaining-after-000 site 4-grams 19/19 hapax 1/0,
cycle 256 unique-max lost N_remaining11=19 K=1 G=755, cycle
223 69/3, and cycle 207 8/1 stay. Nested-check leftover extra
remaining-after-000 unique-max false, N_remaining11==19,
K==1, cycle 257 19/19 4-grams 1/0, cycle 258 19/19 3-grams
I-only with extra I=3 on 057/607 (do not retune 256/257/258).
Nested-check extra I sites: 090 076 607 extra I = Ia8[106];
090 076 057 extra I = Ia8[114], Ia9[28]. Measure; do not
assume the remaining-after-000 stem list if nested-check
differs.

Locks exact consecutive hits of each leftover extra
remaining-after-000 extra-I forward 4-gram 090 076 X Y on
tablet I and on every other vendored tablet A–H and J–V.
The extra-I 4-grams: 090 076 607 755 at Ia8[106] (N_I=1
hapax), 090 076 057 600 at Ia8[114]/Ia9[28] (N_I=2, shared
4th token 600, not hapax). All 3 extra I sites have a 4th
token (no line-final). Hypothesis: all leftover extra
remaining-after-000 extra-I forward 4-grams are I-only.
Hapax is not required. Claim that can lose:
i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only.
True iff every extra-I 4-gram has N_I ≥ 1 and N_off_I = 0
(and every extra I site that has a 4th token is covered).
Shared 4th token / N_I>1 does not make the claim lose. This
can lose if any extra-I 4-gram leaks off I (same shape as
cycle 207 090 076 070 8/1 on T, and as cycle 219 090 076 070
000 leaking on T). Measured: N_i_only=2 / N_not_i_only=0;
no off-I tablets. Nested extra I site ⊆ I sites of its
4-gram. The claim is true. Do not assume; measure. Do not
retune.

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
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_CLAIM,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
    TestMamariI090076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    LEFTOVER_N4_057600,
    LEFTOVER_N4_999021,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_057600_COVERED,
    STANDING_LEFTOVER_999021_COVERED,
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
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    leftover_extra_forward_3grams,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE258_EXTRA_I_SITES_EACH,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    STANDING_N_EXTRA_EACH as CYCLE258_N_EXTRA_EACH,
    STANDING_N_EXTRA_TOTAL as CYCLE258_N_EXTRA_TOTAL,
    STANDING_N_I_ONLY as CYCLE258_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE258_N_NOT_I_ONLY,
    STANDING_XS_WITH_EXTRA as CYCLE258_XS_WITH_EXTRA,
    extra_i_sites,
    remaining_after_000_3grams,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE257_CLAIM,
    STANDING_N_I_ONLY as CYCLE257_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE257_N_NOT_I_ONLY,
    STANDING_REMAINING11_NEXT_4GRAMS as CYCLE257_NEXT_4GRAMS,
    leftover_extra_remaining_after_000_continuing_sites,
    leftover_extra_remaining_after_000_line_final_sites,
    leftover_extra_remaining_after_000_next_4grams,
    TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    LOCKED_FORWARD_STEMS_AFTER_000,
    STANDING_G as CYCLE256_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE256_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
    STANDING_REMAINING11_NEXT_STEMS as CYCLE256_REMAINING11_NEXT_STEMS,
    STANDING_REMAINING11_SITES as CYCLE256_REMAINING11_SITES,
    i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem,
    leftover_extra_remaining_after_000,
    leftover_extra_remaining_after_000_nested_counts_hold,
    leftover_extra_remaining_after_000_next_stems,
    leftover_extra_remaining_after_000_with_g,
    select_remaining_after_000_g,
    TestMamariILeftoverExtra090076RemainingAfter000NextStemScoreboard,
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

HYPOTHESIS_ALL_I_ONLY = True
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_I = 69
STANDING_N_LEFTOVER = 56
STANDING_N_REMAINING11 = 19
STANDING_N_DISTINCT_REMAINING11 = 19
STANDING_REMAINING11_SITES = CYCLE256_REMAINING11_SITES
STANDING_REMAINING11_NEXT_STEMS = CYCLE256_REMAINING11_NEXT_STEMS
STANDING_N_EXTRA_I = 3
STANDING_EXTRA_I_SITES = (
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
)
STANDING_EXTRA_I_BY_X = {
    "607": ((SIDE_IA, "Ia8", 106),),
    "057": ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28)),
}
STANDING_XS_WITH_EXTRA = ("607", "057")
STANDING_PER_SITE_NEXT_4GRAMS = (
    ("090", "076", "607", "755"),
    ("090", "076", "057", "600"),
    ("090", "076", "057", "600"),
)
STANDING_PER_SITE_X = ("607", "057", "057")
STANDING_N_WITH_FOURTH = 3
STANDING_N_LINE_FINAL = 0
STANDING_LINE_FINAL_SITES = ()
STANDING_N_DISTINCT_4GRAMS = 2
STANDING_SEQUENCES = (
    ("090", "076", "607", "755"),
    ("090", "076", "057", "600"),
)
STANDING_NEXT_STEMS = ("607", "057")
STANDING_ROLES = (
    "leftover_extra_remaining_after_000_extra_i",
    "leftover_extra_remaining_after_000_extra_i",
)
STANDING_N_I_EACH = (1, 2)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_I_SITES = (
    ((SIDE_IA, "Ia8", 106),),
    ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28)),
)
STANDING_EXTRA_I_SITES_EACH = STANDING_I_SITES
STANDING_HAPAX_EACH = (True, False)
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
    STANDING_HITS_BY_TABLET_ONE_ON_I,
    STANDING_HITS_BY_TABLET_TWO_ON_I,
)
STANDING_N_I_ONLY = 2
STANDING_N_NOT_I_ONLY = 0
STANDING_LEAKING_4GRAMS = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_CYCLE257_SITE_4GRAMS_NOT_THIS_CYCLE = (
    ("090", "076", "607", "073"),
    ("090", "076", "057", "240"),
)
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_SHARED_FOURTH_DOES_NOT_MAKE_CLAIM_LOSE = True
STANDING_CLAIM = (
    "i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only"
)
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY = True
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_I_ONLY = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE207 = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE256 = False
STANDING_SAME_AS_CYCLE257 = False
STANDING_SAME_AS_CYCLE258 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS = True
STANDING_PREVIOUS_STEMS_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_REMAINING_AFTER_000_SITE_4GRAMS_ARE_NOT_THIS_CYCLE = True
STANDING_090_076_000_DOES_NOT_COUNT = True
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
STANDING_090_076_070_000_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_ARE_THIS_CYCLE_ONLY_IF_MATCHING_4GRAM = True
STANDING_CYCLE258_N_I_ONLY = 19
STANDING_CYCLE258_N_NOT_I_ONLY = 0
STANDING_CYCLE258_N_EXTRA = 3
STANDING_CYCLE257_N_I_ONLY = 19
STANDING_CYCLE257_N_NOT_I_ONLY = 0
STANDING_CYCLE256_N_REMAINING11 = 19
STANDING_CYCLE256_K = 1
STANDING_CYCLE256_G = "755"
STANDING_CYCLE256_UNIQUE = False
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE223_N_OFF_I = 3
STANDING_CYCLE207_N_I = 8
STANDING_CYCLE207_N_OFF_I = 1
STANDING_CYCLE219_N_I_ONLY = 7
STANDING_CYCLE219_N_NOT_I_ONLY = 1


def flatten_extra_i_sites(
    extra_each: tuple[tuple[tuple[str, str, int], ...], ...] = CYCLE258_EXTRA_I_SITES_EACH,
) -> tuple[tuple[str, str, int], ...]:
    """Flatten per-X extra I rows into leftover-of-leftover extra I sites."""
    return tuple(site for row in extra_each for site in row)


def leftover_extra_remaining_after_000_extra_i_sites(
    leftover_sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    i_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """Extra I of leftover extra remaining-after-000 3-grams 090 076 X."""
    remaining11_stems = leftover_extra_remaining_after_000_next_stems(
        leftover_sites,
        next_stems,
    )
    grams = remaining_after_000_3grams(remaining11_stems)
    i_sites_each = tuple(nge4_sites(gram, i_sides) for gram in grams)
    leftover_matching = tuple(
        leftover_extra_remaining_after_000_with_g(
            leftover_sites,
            next_stems,
            stem,
        )
        for stem in remaining11_stems
    )
    extra_each = tuple(
        extra_i_sites(sites, matching)
        for sites, matching in zip(i_sites_each, leftover_matching, strict=True)
    )
    return flatten_extra_i_sites(extra_each)


def extra_i_line_final_sites(
    extra_sites: tuple[tuple[str, str, int], ...],
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Extra I sites with no 4th token. Do not invent a 4-gram."""
    return tuple(
        site
        for site, gram in zip(extra_sites, per_site_4grams, strict=True)
        if gram is None
    )


def extra_i_continuing_sites(
    extra_sites: tuple[tuple[str, str, int], ...],
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Extra I sites that continue to a 4th token."""
    return tuple(
        site
        for site, gram in zip(extra_sites, per_site_4grams, strict=True)
        if gram is not None
    )


def distinct_extra_i_forward_4grams(
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, ...], ...]:
    """First-seen distinct extra-I forward 4-grams. Shared Y is one 4-gram."""
    seen: list[tuple[str, ...]] = []
    for gram in per_site_4grams:
        if gram is not None and gram not in seen:
            seen.append(gram)
    return tuple(seen)


def extra_i_sites_of_4gram(
    extra_sites: tuple[tuple[str, str, int], ...],
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
    gram: tuple[str, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Extra I sites whose contiguous forward 4-gram is gram."""
    return tuple(
        site
        for site, nxt in zip(extra_sites, per_site_4grams, strict=True)
        if nxt == gram
    )


def extra_i_site_subset_of_4gram(
    extra_site: tuple[str, str, int],
    i_sites: tuple[tuple[str, str, int], ...],
) -> bool:
    """True iff extra I site ⊆ I sites of its 4-gram."""
    return extra_site in i_sites


def extra_i_sites_covered_by_4grams(
    extra_sites: tuple[tuple[str, str, int], ...],
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
    i_sites_each: tuple[tuple[tuple[str, str, int], ...], ...],
    grams: tuple[tuple[str, ...], ...],
) -> bool:
    """True iff every extra I site with a 4th token sits in its 4-gram I sites."""
    gram_to_sites = dict(zip(grams, i_sites_each, strict=True))
    for site, gram in zip(extra_sites, per_site_4grams, strict=True):
        if gram is None:
            continue
        if gram not in gram_to_sites:
            return False
        if not extra_i_site_subset_of_4gram(site, gram_to_sites[gram]):
            return False
    return True


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def sequence_is_hapax(n_i: int, n_off_i: int) -> bool:
    """True iff N_I==1 and N_off_I=0. Shared 4th token is not hapax."""
    return n_i == 1 and n_off_i == 0


def i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    extra_sites: tuple[tuple[str, str, int], ...],
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
    i_sites_each: tuple[tuple[tuple[str, str, int], ...], ...],
    grams: tuple[tuple[str, ...], ...],
    expected_n: int = STANDING_N_DISTINCT_4GRAMS,
) -> bool:
    """True iff every extra-I 4-gram is I-only and covered.

    Hapax is not required. Shared 4th token / N_I>1 does not
    make the claim lose. Line-final extra I sites (no 4th
    token) are skipped, not invented. Length must stay the
    distinct extra-I 4-gram count.
    """
    if len(n_i) != expected_n or len(n_off_i) != expected_n:
        return False
    if len(grams) != expected_n:
        return False
    if not all(
        sequence_is_i_only(on, off)
        for on, off in zip(n_i, n_off_i, strict=True)
    ):
        return False
    return extra_i_sites_covered_by_4grams(
        extra_sites,
        per_site_4grams,
        i_sites_each,
        grams,
    )


class TestILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyHelpers(
    unittest.TestCase
):
    """Helpers on leftover extra remaining-after-000 extra-I 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. Site 4-grams / 070 000 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("090", "076", "607", "755"))
        self.assertEqual(STANDING_SEQUENCES[1], ("090", "076", "057", "600"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_DISTINCT_4GRAMS)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_DISTINCT_4GRAMS)
        self.assertEqual(
            distinct_extra_i_forward_4grams(STANDING_PER_SITE_NEXT_4GRAMS),
            STANDING_SEQUENCES,
        )
        for gram, nxt in zip(STANDING_SEQUENCES, STANDING_NEXT_STEMS, strict=True):
            self.assertEqual(gram[:2], GRAM2)
            self.assertEqual(gram[2], nxt)
            self.assertEqual(len(gram), STANDING_N4)
            self.assertIn(nxt, STANDING_XS_WITH_EXTRA)
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS_AFTER_000)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotIn(gram, STANDING_CYCLE257_SITE_4GRAMS_NOT_THIS_CYCLE)
            self.assertNotIn(gram, CYCLE257_NEXT_4GRAMS)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["090", "076", "057", "600", "090", "076", "057", "600"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[1]), 2)
        gapped = [list(STANDING_SEQUENCES[0][:2]) + ["006"] + list(STANDING_SEQUENCES[0][2:])]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(
            ngram_hit_count([list(STANDING_CYCLE257_SITE_4GRAMS_NOT_THIS_CYCLE[0])], STANDING_SEQUENCES[0]),
            0,
        )
        planted = ["999", "021", "090", "076", "607", "755"]
        self.assertEqual(site_next_4gram(planted, 2, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_forward_3gram(planted, 2, GRAM2), ("090", "076", "607"))
        line_final_after_x = ["999", "021", "090", "076", "607"]
        self.assertEqual(site_forward_3gram(line_final_after_x, 2, GRAM2), ("090", "076", "607"))
        self.assertIsNone(site_next_4gram(line_final_after_x, 2, GRAM2))
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_REMAINING_AFTER_000_SITE_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_zero_off_i_and_coverage(self):
        """Boolean is True only when all extra-I 4-grams are I-only and covered."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                hold_ones,
                hold_zeros,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_NEXT_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                (2, 2),
                hold_zeros,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_NEXT_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        lose_off = (1, 0)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                hold_ones,
                lose_off,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_NEXT_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        lose_off_shared = (0, 1)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                hold_ones,
                lose_off_shared,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_NEXT_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        lose_missing_i = (0, 2)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                lose_missing_i,
                hold_zeros,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_NEXT_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        uncovered = (
            ((SIDE_IA, "Ia7", 137),),
            STANDING_I_SITES[1],
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                hold_ones,
                hold_zeros,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_NEXT_4GRAMS,
                uncovered,
                STANDING_SEQUENCES,
            )
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                (),
                (),
                (),
                (),
                (),
                (),
            )
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                hold_ones[:1],
                hold_zeros[:1],
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_NEXT_4GRAMS,
                STANDING_I_SITES[:1],
                STANDING_SEQUENCES[:1],
            )
        )
        self.assertTrue(STANDING_SHARED_FOURTH_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(STANDING_HAPAX_EACH, (True, False))
        self.assertFalse(sequence_is_hapax(2, 0))
        self.assertTrue(sequence_is_hapax(1, 0))
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(CYCLE207_N_OFF_I, 1)
        self.assertEqual(provider.get_call_history(), [])

    def test_extra_i_sites_and_shared_fourth_are_leftover_of_leftover(self):
        """Extra I sites stay cycle-258 leftover-of-leftover; 057 shares 600."""
        provider = MockProvider()
        self.assertEqual(flatten_extra_i_sites(), STANDING_EXTRA_I_SITES)
        self.assertEqual(len(STANDING_EXTRA_I_SITES), STANDING_N_EXTRA_I)
        self.assertEqual(STANDING_N_EXTRA_I, CYCLE258_N_EXTRA_TOTAL)
        self.assertEqual(STANDING_N_EXTRA_I, 3)
        self.assertEqual(CYCLE258_N_EXTRA_EACH[13], 1)
        self.assertEqual(CYCLE258_N_EXTRA_EACH[14], 2)
        self.assertEqual(CYCLE258_XS_WITH_EXTRA, STANDING_XS_WITH_EXTRA)
        self.assertEqual(STANDING_EXTRA_I_BY_X["607"], ((SIDE_IA, "Ia8", 106),))
        self.assertEqual(
            STANDING_EXTRA_I_BY_X["057"],
            ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28)),
        )
        self.assertEqual(STANDING_PER_SITE_NEXT_4GRAMS[1], STANDING_PER_SITE_NEXT_4GRAMS[2])
        self.assertEqual(STANDING_PER_SITE_NEXT_4GRAMS[1][3], "600")
        self.assertNotEqual(STANDING_SEQUENCES[0], STANDING_SEQUENCES[1])
        self.assertIn(STANDING_EXTRA_I_SITES[0], CYCLE224_INSIDE_SITES)
        self.assertIn(STANDING_EXTRA_I_SITES[0], STANDING_LEFTOVER_999021_COVERED)
        self.assertEqual(LEFTOVER_N4_999021, ("999", "021", "090", "076"))
        self.assertIn(LEFTOVER_N4_999021, CYCLE222_MATCHING)
        for site in STANDING_EXTRA_I_BY_X["057"]:
            self.assertIn(site, CYCLE224_INSIDE_SITES)
            self.assertIn(site, STANDING_LEFTOVER_057600_COVERED)
        self.assertEqual(LEFTOVER_N4_057600, ("090", "076", "057", "600"))
        self.assertEqual(LEFTOVER_N4_057600, STANDING_SEQUENCES[1])
        self.assertIn(LEFTOVER_N4_057600, CYCLE222_MATCHING)
        for site in STANDING_EXTRA_I_SITES:
            self.assertNotIn(site, STANDING_REMAINING11_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        for gram in STANDING_CYCLE257_SITE_4GRAMS_NOT_THIS_CYCLE:
            self.assertIn(gram, CYCLE257_NEXT_4GRAMS)
            self.assertNotIn(gram, STANDING_SEQUENCES)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-000 extra-I 4-gram off-I lock."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.next_stems = leftover_extra_next_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.leftover_next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.forwards = leftover_extra_forward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.remaining11 = leftover_extra_remaining_after_000(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining11_stems = leftover_extra_remaining_after_000_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.grams3 = remaining_after_000_3grams(self.remaining11_stems)
        self.i_sites3 = tuple(nge4_sites(gram, self.i_sides) for gram in self.grams3)
        self.leftover_matching = tuple(
            leftover_extra_remaining_after_000_with_g(
                self.leftover_sites,
                self.next_stems,
                stem,
            )
            for stem in self.remaining11_stems
        )
        self.extra_each = tuple(
            extra_i_sites(sites, matching)
            for sites, matching in zip(
                self.i_sites3,
                self.leftover_matching,
                strict=True,
            )
        )
        self.extra_sites = leftover_extra_remaining_after_000_extra_i_sites(
            self.leftover_sites,
            self.next_stems,
            self.i_sides,
        )
        self.per_site_next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.extra_sites,
            GRAM2,
        )
        self.line_final = extra_i_line_final_sites(
            self.extra_sites,
            self.per_site_next_4grams,
        )
        self.continuing = extra_i_continuing_sites(
            self.extra_sites,
            self.per_site_next_4grams,
        )
        self.grams = distinct_extra_i_forward_4grams(self.per_site_next_4grams)
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
        self.hapax_each = tuple(
            sequence_is_hapax(on, off)
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
        )
        self.g, self.k, self.unique = select_remaining_after_000_g(
            self.remaining11_stems
        )
        self.unique_max = i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem(
            self.leftover_sites,
            self.next_stems,
        )
        self.site_next_4grams = leftover_extra_remaining_after_000_next_4grams(
            self.leftover_sites,
            self.leftover_next_4grams,
            self.next_stems,
        )
        self.site_line_final = leftover_extra_remaining_after_000_line_final_sites(
            self.leftover_sites,
            self.leftover_next_4grams,
            self.next_stems,
        )
        self.site_continuing = leftover_extra_remaining_after_000_continuing_sites(
            self.leftover_sites,
            self.leftover_next_4grams,
            self.next_stems,
        )
        self.claim_holds = (
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                self.n_i,
                self.n_off_i,
                self.extra_sites,
                self.per_site_next_4grams,
                self.i_sites,
                self.grams,
            )
        )
        self.n_i_only = sum(
            1
            for on, off in zip(self.n_i, self.n_off_i, strict=True)
            if sequence_is_i_only(on, off)
        )
        self.n_not_i_only = len(self.grams) - self.n_i_only
        self.leaking = tuple(
            gram
            for gram, on, off in zip(self.grams, self.n_i, self.n_off_i, strict=True)
            if not sequence_is_i_only(on, off)
        )

    def test_tokens_and_sites_are_cycle_258_extra_i_not_retuned(self):
        """4-grams stay the cycle-258 extra I forwards. Nested 19/K=1/G=755 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(self.leftover_sites), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.remaining11, STANDING_REMAINING11_SITES)
        self.assertEqual(self.remaining11, CYCLE256_REMAINING11_SITES)
        self.assertEqual(self.remaining11_stems, STANDING_REMAINING11_NEXT_STEMS)
        self.assertEqual(len(self.remaining11), STANDING_N_REMAINING11)
        self.assertEqual(STANDING_N_REMAINING11, 19)
        self.assertEqual(self.g, CYCLE256_G)
        self.assertEqual(self.g, "755")
        self.assertEqual(self.k, CYCLE256_K)
        self.assertEqual(self.k, 1)
        self.assertFalse(self.unique)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertFalse(self.unique_max)
        self.assertFalse(CYCLE256_CLAIM)
        if (
            len(self.remaining11) != 19
            or self.k != 1
            or self.g != "755"
            or self.unique
            or self.unique_max
        ):
            self.fail("nested cycle 256 unique-max false N_remaining11=19 K=1 G=755 drifted")
        self.assertEqual(self.remaining11_stems, CYCLE256_REMAINING11_NEXT_STEMS)
        self.assertEqual(self.site_next_4grams, CYCLE257_NEXT_4GRAMS)
        self.assertEqual(self.site_line_final, ())
        self.assertEqual(len(self.site_continuing), 19)
        self.assertEqual(self.extra_each, CYCLE258_EXTRA_I_SITES_EACH)
        self.assertEqual(sum(len(row) for row in self.extra_each), CYCLE258_N_EXTRA_TOTAL)
        self.assertEqual(sum(len(row) for row in self.extra_each), 3)
        self.assertEqual(self.extra_sites, STANDING_EXTRA_I_SITES)
        self.assertEqual(self.extra_sites, flatten_extra_i_sites(self.extra_each))
        self.assertEqual(self.extra_each[13], STANDING_EXTRA_I_BY_X["607"])
        self.assertEqual(self.extra_each[14], STANDING_EXTRA_I_BY_X["057"])
        if self.extra_sites != STANDING_EXTRA_I_SITES:
            self.fail("nested cycle 258 extra I sites drifted from Ia8[106]/Ia8[114]/Ia9[28]")
        self.assertTrue(
            leftover_extra_remaining_after_000_nested_counts_hold(
                56, 55, 1, 8, 47, 6, 41, 5, 36, 3, 33, 2, 31, 2, 29, 2, 27, 2, 25, 2, 23, 2, 21, 2, 19,
            )
        )
        prior_258 = self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]
        self.assertEqual(prior_258["cycle"], 258)
        self.assertEqual(prior_258["N_i_only"], 19)
        self.assertEqual(prior_258["N_not_i_only"], 0)
        self.assertEqual(prior_258["N_extra_total"], 3)
        self.assertTrue(prior_258["i_leftover_extra_090_076_remaining_after_000_3grams_all_i_only"])
        self.assertTrue(CYCLE258_CLAIM)
        self.assertEqual(CYCLE258_N_I_ONLY, 19)
        self.assertEqual(CYCLE258_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE258_N_EXTRA_TOTAL, 3)
        prior_257 = self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"]
        self.assertEqual(prior_257["cycle"], 257)
        self.assertEqual(prior_257["N_i_only"], 19)
        self.assertEqual(prior_257["N_not_i_only"], 0)
        self.assertTrue(prior_257["i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only"])
        self.assertTrue(CYCLE257_CLAIM)
        prior_256 = self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]
        self.assertEqual(prior_256["cycle"], 256)
        self.assertEqual(prior_256["N_remaining11"], 19)
        self.assertEqual(prior_256["K"], 1)
        self.assertEqual(prior_256["G"], "755")
        self.assertFalse(prior_256["G_uniquely_most_frequent"])
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_extra_i_4gram_lock_and_claim_holds(self):
        """Extra-I 4-grams are I-only. Shared 600 / N_I=2 does not lose."""
        self.assertEqual(self.per_site_next_4grams, STANDING_PER_SITE_NEXT_4GRAMS)
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(self.line_final, STANDING_LINE_FINAL_SITES)
        self.assertEqual(self.line_final, ())
        self.assertEqual(self.continuing, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.grams), STANDING_N_DISTINCT_4GRAMS)
        self.assertEqual(STANDING_N_DISTINCT_4GRAMS, 2)
        self.assertEqual(len(self.continuing), STANDING_N_WITH_FOURTH)
        self.assertEqual(STANDING_N_WITH_FOURTH, 3)
        self.assertEqual(len(self.line_final), STANDING_N_LINE_FINAL)
        self.assertEqual(STANDING_N_LINE_FINAL, 0)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(self.hapax_each, STANDING_HAPAX_EACH)
        self.assertEqual(self.leaking, STANDING_LEAKING_4GRAMS)
        self.assertEqual(self.leaking, ())
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_i_only, 2)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_not_i_only, 0)
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from 0")
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked extra-I 4-grams")
        if self.line_final:
            self.fail("measured line-final extra I set drifted from empty")
        if self.leaking:
            self.fail("measured extra-I forward 4-grams leaked off I")
        self.assertTrue(
            extra_i_sites_covered_by_4grams(
                self.extra_sites,
                self.per_site_next_4grams,
                self.i_sites,
                self.grams,
            )
        )
        for site, gram4, nxt in zip(
            STANDING_EXTRA_I_SITES,
            STANDING_PER_SITE_NEXT_4GRAMS,
            STANDING_PER_SITE_X,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N4]), gram4)
            self.assertEqual(stems[site[2] + STANDING_N2], nxt)
            self.assertEqual(tuple(stems[site[2] : site[2] + STANDING_N2]), GRAM2)
            self.assertEqual(site_next_4gram(stems, site[2], GRAM2), gram4)
            self.assertEqual(site_forward_3gram(stems, site[2], GRAM2), ("090", "076", nxt))
            self.assertGreater(len(stems), site[2] + 3)
            self.assertNotIn(nxt, LOCKED_FORWARD_STEMS_AFTER_000)
            self.assertIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, STANDING_REMAINING11_SITES)
        for gram, nxt, role, sites, extra, n_on, n_off, hapax in zip(
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_EXTRA_I_SITES_EACH,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_HAPAX_EACH,
            strict=True,
        ):
            self.assertEqual(
                extra_i_sites_of_4gram(
                    STANDING_EXTRA_I_SITES,
                    STANDING_PER_SITE_NEXT_4GRAMS,
                    gram,
                ),
                extra,
            )
            self.assertEqual(extra, sites)
            for site in extra:
                self.assertTrue(extra_i_site_subset_of_4gram(site, sites))
            self.assertEqual(gram[2], nxt)
            self.assertEqual(role, "leftover_extra_remaining_after_000_extra_i")
            self.assertGreaterEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertEqual(sequence_is_hapax(n_on, n_off), hapax)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotIn(gram, CYCLE257_NEXT_4GRAMS)
        self.assertTrue(STANDING_HAPAX_EACH[0])
        self.assertFalse(STANDING_HAPAX_EACH[1])
        self.assertEqual(STANDING_SEQUENCES[0][3], "755")
        self.assertEqual(STANDING_SEQUENCES[1][3], "600")
        self.assertEqual(STANDING_SEQUENCES[1], LEFTOVER_N4_057600)
        self.assertIn((SIDE_IA, "Ia8", 106), STANDING_LEFTOVER_999021_COVERED)
        self.assertIn(("999", "021", "090", "076"), CYCLE222_MATCHING)
        self.assertIn(("090", "076", "057", "600"), CYCLE222_MATCHING)
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        if not self.claim_holds:
            self.fail("measured extra-I forward 4-grams are not all I-only")
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_SHARED_FOURTH_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off, n_on in zip(self.hits_by_tablet, self.off_i, self.n_i, strict=True):
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
            self.assertEqual(hits[VENDORED_TABLETS.index("I")], n_on)
            self.assertEqual(sum(hits) - n_on, 0)
        t_sides = load_t_sides()
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
            self.assertNotIn(following, (("090", "076", "607"), ("090", "076", "057")))
            for gram in STANDING_SEQUENCES:
                self.assertNotEqual(tuple(stems[index : index + 4]), gram)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertEqual(
            i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only(
                self.n_i,
                self.n_off_i,
                self.extra_sites,
                self.per_site_next_4grams,
                self.i_sites,
                self.grams,
            ),
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_REMAINING_AFTER_000_SITE_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_SAME_AS_CYCLE207)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE257)
        self.assertFalse(STANDING_SAME_AS_CYCLE258)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_258_257_256_223_and_207_still_compute(self):
        """Cycle 258 19/19 extra I=3, 257 19/19 hapax, 256 unique-max lose 19/K=1/G=755, 223 69/3, 207 8/1 stay."""
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_258.test_survey_matches_computed_lock()
        self.assertEqual(prior_258.n_i_only, 19)
        self.assertEqual(prior_258.n_not_i_only, 0)
        self.assertEqual(sum(prior_258.n_extra), 3)
        self.assertEqual(prior_258.extra, CYCLE258_EXTRA_I_SITES_EACH)
        self.assertTrue(prior_258.claim_holds)
        self.assertTrue(CYCLE258_CLAIM)
        if (
            prior_258.n_i_only != 19
            or prior_258.n_not_i_only != 0
            or sum(prior_258.n_extra) != 3
        ):
            self.fail("nested cycle 258 remaining-after-000 3-grams 19/19 extra I=3 drifted")
        prior_257 = TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard()
        prior_257.setUp()
        prior_257.test_each_4gram_is_one_on_i_zero_off_i_no_line_final_and_claim_holds()
        prior_257.test_survey_matches_computed_lock()
        self.assertEqual(prior_257.n_i_only, 19)
        self.assertEqual(prior_257.n_not_i_only, 0)
        self.assertTrue(prior_257.claim_holds)
        self.assertTrue(CYCLE257_CLAIM)
        if prior_257.n_i_only != 19 or prior_257.n_not_i_only != 0:
            self.fail("nested cycle 257 remaining-after-000 forward 4-grams 19/19 hapax drifted")
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
        if (
            prior_256.n_remaining11 != 19
            or prior_256.k != 1
            or prior_256.g != "755"
            or prior_256.unique
        ):
            self.fail("nested cycle 256 unique-max false N_remaining11=19 K=1 G=755 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, CYCLE223_N_I)
        self.assertEqual(prior_223.off_i_hits, CYCLE223_N_OFF_I)
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
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        prior_219.test_survey_matches_computed_lock()
        self.assertEqual(prior_219.n_i_only, 7)
        self.assertEqual(prior_219.n_not_i_only, 1)
        self.assertFalse(prior_219.claim_holds)
        self.assertFalse(CYCLE219_CLAIM)
        if prior_219.n_i_only != 7 or prior_219.n_not_i_only != 1:
            self.fail("nested cycle 219 090 076 070 forward 4-grams 7/8 lose on T 000 drifted")
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
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-259 extra-I forward-4 I-only lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]
        self.assertEqual(lock["cycle"], 259)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_i_only"])
        self.assertEqual(lock["hypothesis_all_i_only"], HYPOTHESIS_ALL_I_ONLY)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(lock["N_remaining11"], STANDING_N_REMAINING11)
        self.assertEqual(lock["N_remaining11"], 19)
        self.assertEqual(lock["N_distinct_remaining11"], STANDING_N_DISTINCT_REMAINING11)
        self.assertEqual(lock["K"], 1)
        self.assertEqual(lock["G"], "755")
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertFalse(lock["i_leftover_extra_090_076_remaining_after_000_unique_max_next_stem"])
        self.assertEqual(
            tuple(lock["locked_forward_stems_after_000"]),
            LOCKED_FORWARD_STEMS_AFTER_000,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_000_sites"]),
            STANDING_REMAINING11_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_000_next_stems"]),
            STANDING_REMAINING11_NEXT_STEMS,
        )
        self.assertEqual(lock["N_extra_i"], STANDING_N_EXTRA_I)
        self.assertEqual(lock["N_extra_i"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertEqual(
            [list(site) for site in STANDING_EXTRA_I_BY_X["607"]],
            lock["extra_i_sites_607"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_EXTRA_I_BY_X["057"]],
            lock["extra_i_sites_057"],
        )
        self.assertEqual(tuple(lock["xs_with_extra"]), STANDING_XS_WITH_EXTRA)
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_NEXT_4GRAMS],
            lock["extra_i_per_site_next_4grams"],
        )
        self.assertEqual(lock["N_with_fourth"], 3)
        self.assertEqual(lock["N_line_final"], 0)
        self.assertEqual(lock["line_final_extra_i_sites"], [])
        self.assertTrue(lock["all_extra_i_have_fourth_token"])
        self.assertEqual(lock["N_distinct_4grams"], 2)
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["extra_i_forward_4grams"],
        )
        self.assertTrue(lock["not_assumed_hapax"])
        self.assertTrue(lock["shared_fourth_does_not_make_claim_lose"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_DISTINCT_4GRAMS)
        for row, gram, nxt, role, sites, extra, n_on, n_off, hapax in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_NEXT_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_EXTRA_I_SITES_EACH,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_HAPAX_EACH,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(row["next_stem"], nxt)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["ia_hits"], n_on)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["extra_i_sites"]),
                extra,
            )
            self.assertTrue(row["extra_i_subset_of_i_sites"])
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(row["off_i_tablets_with_hits"], [])
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertTrue(row["i_only"])
            self.assertEqual(row["hapax"], hapax)
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(tuple(lock["hapax_each"]), STANDING_HAPAX_EACH)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only"]
        )
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]
        )
        self.assertEqual(lock["N_i_only"], 2)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(lock["off_i_tablets_with_hits"], [])
        self.assertTrue(lock["shared_fourth_does_not_make_claim_lose"])
        self.assertEqual(lock["nested_cycle258_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle258_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle258_N_extra"], 3)
        self.assertEqual(lock["nested_cycle257_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle257_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle256_N_remaining11"], 19)
        self.assertEqual(lock["nested_cycle256_K"], 1)
        self.assertEqual(lock["nested_cycle256_G"], "755")
        self.assertFalse(lock["nested_cycle256_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle219_N_i_only"], 7)
        self.assertEqual(lock["nested_cycle219_N_not_i_only"], 1)
        self.assertEqual(tuple(lock["nested_cycle219_leak_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(tuple(lock["nested_cycle207_off_i_sites"][0]), CYCLE207_OFF_I_SITES[0])
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle207"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle256"])
        self.assertFalse(lock["same_as_cycle257"])
        self.assertFalse(lock["same_as_cycle258"])
        self.assertTrue(lock["same_claim_shape_as_cycle207"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["do_not_peel_leftover_extra_i_previous_stems"])
        self.assertTrue(lock["previous_stems_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["remaining_after_000_site_4grams_are_not_this_cycle"])
        self.assertTrue(lock["090_076_000_does_not_count"])
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
        self.assertTrue(lock["090_076_070_000_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_are_this_cycle_only_if_matching_4gram"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_3grams_i_only"]["cycle"],
            258,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"]["cycle"],
            257,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_next_stem"]["cycle"],
            256,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 259 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
