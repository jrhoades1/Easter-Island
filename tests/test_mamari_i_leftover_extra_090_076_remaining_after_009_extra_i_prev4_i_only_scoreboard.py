"""I's cycle-286 leftover extra remaining-after-009 extra-I previous-4 lock.

Cycle 287 text-search lock. Uses already-vendored A–V and the
cycle-286 leftover extra remaining-after-009 extra I sites of
3-grams 000 090 076 and 008 090 076 (the 2 I sites of those
3-grams that are not leftover extra remaining-after-009).
Does not retune leftover extra remaining-after-009 unique-max
(cycle 284 lost: 27 hapax, G=724 K=1), leftover extra
remaining-after-009 previous 4-grams (cycle 285 held: 27/27
hapax 1/0 of the 27 remaining-after-009 SITES only), leftover
extra remaining-after-009 3-grams (cycle 286 held: 27/27
I-only, extra I=2), leftover extra remaining-after-045
previous-009, leftover extra sites, leftover n=4, or the
already-closed leftover remaining family. Does not retune the
forward peel (225–259). Does not overwrite cycle 167's
3-gram I-only 16/0 lock. Does not overwrite cycles 268–286.
Does not vendor a new tablet. Does not scrape X. W has no
Barthel (cycle 100); skip W. Unpublished Ib is 0. Does not
redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Cycle 285 locked previous 4-grams of the 27 leftover extra
remaining-after-009 SITES only. Extra I sites of 000 090 076
and 008 090 076 are leftover-of-leftover; their previous
4-grams X W 090 076 were not locked. Extra I of 000 is one
site of leftover n=4 remaining 090 076 057 600 (090-start
Ia8[114]). Extra I of 008 is one site of leftover n=4
remaining 090 076 020 010 (090-start Ia12[83]). Do not
confuse with already-locked remaining-after-009 site 4-grams
490 000 090 076 and 727 008 090 076. Do not peel leftover
extra I 090 076 further previous stems this cycle. Do not
retune leftover n=4. Do not retune the forward peel
(225–259).

Same claim-shape as cycle 259 leftover extra remaining-after-
000 extra-I forward 4-grams 2/0, previous side instead of
forward, and cycle 219 (090 076 070 000 leaking on T). Cycle
286 remaining-after-009 3-grams all I-only 27/27 extra I=2,
cycle 285 remaining-after-009 site 4-grams 27/27 hapax 1/0,
cycle 284 unique-max lost N_remaining_after_009=27 K=1
G=724, cycle 259 extra-I fwd4 2/0, cycle 223 69/3, and cycle
167 16/0 stay. Nested-check leftover extra remaining-after-
009 unique-max false, N_remaining_after_009==27, K==1, cycle
285 27/0 previous 4-grams 1/0, cycle 286 27/0 3-grams I-only
with extra I=2 on 000/008 (do not retune 284/285/286).
Nested-check extra I sites: 000 090 076 extra I = Ia8[113];
008 090 076 extra I = Ia12[82]. Measure; do not assume the
remaining-after-009 stem list if nested-check differs.

Locks exact consecutive hits of each leftover extra
remaining-after-009 extra-I previous 4-gram X W 090 076 on
tablet I and on every other vendored tablet A–H and J–V.
The extra-I 4-grams: 607 000 090 076 at Ia8[113] (N_I=1
hapax), 700 008 090 076 at Ia12[82] (N_I=1 hapax). All 2
extra I sites have a 4th token X (no line-initial).
Hypothesis: all leftover extra remaining-after-009 extra-I
previous 4-grams are I-only. Hapax is not required. Claim
that can lose:
i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only.
True iff every extra-I 4-gram has N_I ≥ 1 and N_off_I = 0
(and every extra I site that has a 4th token X is covered).
Shared previous token / N_I>1 does not make the claim lose.
This can lose if any extra-I 4-gram leaks off I (same shape
as cycle 219 090 076 070 000 leaking on T). Measured:
N_i_only=2 / N_not_i_only=0; no off-I tablets. Nested extra
I site ⊆ I sites of its 4-gram. The claim is true. Do not
assume; measure. Do not retune.

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
    LEFTOVER_N4_020010,
    LEFTOVER_N4_057600,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_020010_COVERED,
    STANDING_LEFTOVER_057600_COVERED,
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
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE167_GRAM3,
    STANDING_I_3GRAM_999_090_076_I_ONLY as CYCLE167_CLAIM,
    STANDING_I_SITES as CYCLE167_I_SITES,
    STANDING_N_I as CYCLE167_N_I,
    STANDING_N_OFF_I as CYCLE167_N_OFF_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    leftover_extra_backward_3grams,
    leftover_extra_previous_4grams,
    leftover_extra_previous_stems,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_N_I_ONLY as CYCLE259_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE259_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_3grams_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE286_EXTRA_I_SITES_EACH,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_3GRAMS_ALL_I_ONLY as CYCLE286_CLAIM,
    STANDING_N_EXTRA_EACH as CYCLE286_N_EXTRA_EACH,
    STANDING_N_EXTRA_TOTAL as CYCLE286_N_EXTRA_TOTAL,
    STANDING_N_I_ONLY as CYCLE286_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE286_N_NOT_I_ONLY,
    STANDING_WS_WITH_EXTRA as CYCLE286_WS_WITH_EXTRA,
    extra_i_sites,
    leftover_extra_090_076_site_for_3gram,
    remaining_after_009_3grams,
    TestMamariILeftoverExtra090076RemainingAfter0093gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_prev4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_ALL_I_ONLY as CYCLE285_CLAIM,
    STANDING_N_I_ONLY as CYCLE285_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE285_N_NOT_I_ONLY,
    STANDING_REMAINING_PREVIOUS_4GRAMS as CYCLE285_PREVIOUS_4GRAMS,
    leftover_extra_remaining_after_009_continuing_sites,
    leftover_extra_remaining_after_009_line_initial_sites,
    leftover_extra_remaining_after_009_previous_4grams,
    TestMamariILeftoverExtra090076RemainingAfter009Prev4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_prev_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_009,
    STANDING_G as CYCLE284_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE284_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_UNIQUE_PREVIOUS_STEM as CYCLE284_CLAIM,
    STANDING_K as CYCLE284_K,
    STANDING_N_REMAINING_AFTER_009 as CYCLE284_N_REMAINING,
    STANDING_REMAINING_PREVIOUS_STEMS as CYCLE284_REMAINING_PREVIOUS_STEMS,
    STANDING_REMAINING_SITES as CYCLE284_REMAINING_SITES,
    i_leftover_extra_090_076_remaining_after_009_unique_previous_stem,
    leftover_extra_remaining_after_009,
    leftover_extra_remaining_after_009_nested_counts_hold,
    leftover_extra_remaining_after_009_previous_stems,
    leftover_extra_remaining_after_009_with_g,
    select_remaining_after_009_g,
    TestMamariILeftoverExtra090076RemainingAfter009PrevStemScoreboard,
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
STANDING_N_LEFTOVER = 56
STANDING_N_REMAINING_AFTER_009 = 27
STANDING_N_DISTINCT_REMAINING = 27
STANDING_REMAINING_SITES = CYCLE284_REMAINING_SITES
STANDING_REMAINING_PREVIOUS_STEMS = CYCLE284_REMAINING_PREVIOUS_STEMS
STANDING_N_EXTRA_I = 2
STANDING_EXTRA_I_SITES = (
    (SIDE_IA, "Ia8", 113),
    (SIDE_IA, "Ia12", 82),
)
STANDING_EXTRA_I_BY_W = {
    "000": ((SIDE_IA, "Ia8", 113),),
    "008": ((SIDE_IA, "Ia12", 82),),
}
STANDING_WS_WITH_EXTRA = ("000", "008")
STANDING_EXTRA_I_090_076_SITES = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia12", 83),
)
STANDING_PER_SITE_PREVIOUS_4GRAMS = (
    ("607", "000", "090", "076"),
    ("700", "008", "090", "076"),
)
STANDING_PER_SITE_W = ("000", "008")
STANDING_N_WITH_FOURTH = 2
STANDING_N_LINE_INITIAL = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_N_DISTINCT_4GRAMS = 2
STANDING_SEQUENCES = (
    ("607", "000", "090", "076"),
    ("700", "008", "090", "076"),
)
STANDING_PREVIOUS_STEMS = ("000", "008")
STANDING_ROLES = (
    "leftover_extra_remaining_after_009_extra_i",
    "leftover_extra_remaining_after_009_extra_i",
)
STANDING_N_I_EACH = (1, 1)
STANDING_N_ON_I_EACH = STANDING_N_I_EACH
STANDING_I_SITES = (
    ((SIDE_IA, "Ia8", 112),),
    ((SIDE_IA, "Ia12", 81),),
)
STANDING_EXTRA_I_SITES_EACH = (
    ((SIDE_IA, "Ia8", 113),),
    ((SIDE_IA, "Ia12", 82),),
)
STANDING_HAPAX_EACH = (True, True)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0, 0)
STANDING_OFF_I_SITES = ((), ())
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (
    STANDING_HITS_BY_TABLET_ONE_ON_I,
    STANDING_HITS_BY_TABLET_ONE_ON_I,
)
STANDING_N_I_ONLY = 2
STANDING_N_NOT_I_ONLY = 0
STANDING_LEAKING_4GRAMS = ()
STANDING_OFF_I_TABLETS_WITH_HITS = ()
STANDING_CYCLE285_SITE_4GRAMS_NOT_THIS_CYCLE = (
    ("490", "000", "090", "076"),
    ("727", "008", "090", "076"),
)
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_SHARED_PREVIOUS_DOES_NOT_MAKE_CLAIM_LOSE = True
STANDING_CLAIM = (
    "i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only"
)
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_EXTRA_I_PREV4_ALL_I_ONLY = True
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_EXTRA_I_PREV4_I_ONLY = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167 = False
STANDING_SAME_AS_CYCLE207 = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE259 = False
STANDING_SAME_AS_CYCLE284 = False
STANDING_SAME_AS_CYCLE285 = False
STANDING_SAME_AS_CYCLE286 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE259 = True
STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS = True
STANDING_PREVIOUS_STEMS_OF_090_076_ARE_NOT_THIS_CYCLE = True
STANDING_REMAINING_AFTER_009_SITE_4GRAMS_ARE_NOT_THIS_CYCLE = True
STANDING_999_090_076_DOES_NOT_COUNT = True
STANDING_600_090_076_DOES_NOT_COUNT = True
STANDING_090_090_076_DOES_NOT_COUNT = True
STANDING_076_090_076_DOES_NOT_COUNT = True
STANDING_071_090_076_DOES_NOT_COUNT = True
STANDING_045_090_076_DOES_NOT_COUNT = True
STANDING_009_090_076_DOES_NOT_COUNT = True
STANDING_490_000_090_076_DOES_NOT_COUNT = True
STANDING_727_008_090_076_DOES_NOT_COUNT = True
STANDING_090_076_070_000_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_ARE_THIS_CYCLE_ONLY_IF_MATCHING_4GRAM = True
STANDING_CYCLE286_N_I_ONLY = 27
STANDING_CYCLE286_N_NOT_I_ONLY = 0
STANDING_CYCLE286_N_EXTRA = 2
STANDING_CYCLE285_N_I_ONLY = 27
STANDING_CYCLE285_N_NOT_I_ONLY = 0
STANDING_CYCLE284_N_REMAINING = 27
STANDING_CYCLE284_K = 1
STANDING_CYCLE284_G = "724"
STANDING_CYCLE284_UNIQUE = False
STANDING_CYCLE259_N_I_ONLY = 2
STANDING_CYCLE259_N_NOT_I_ONLY = 0
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE223_N_OFF_I = 3
STANDING_CYCLE219_N_I_ONLY = 7
STANDING_CYCLE219_N_NOT_I_ONLY = 1
STANDING_CYCLE207_N_I = 8
STANDING_CYCLE207_N_OFF_I = 1
STANDING_CYCLE167_N_I = 16
STANDING_CYCLE167_N_OFF_I = 0


def flatten_extra_i_sites(
    extra_each: tuple[tuple[tuple[str, str, int], ...], ...] = CYCLE286_EXTRA_I_SITES_EACH,
) -> tuple[tuple[str, str, int], ...]:
    """Flatten per-W extra I rows into leftover-of-leftover extra I sites."""
    return tuple(site for row in extra_each for site in row)


def leftover_extra_remaining_after_009_extra_i_sites(
    leftover_sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    i_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """Extra I of leftover extra remaining-after-009 3-grams W 090 076."""
    remaining_stems = leftover_extra_remaining_after_009_previous_stems(
        leftover_sites,
        previous_stems,
    )
    grams = remaining_after_009_3grams(remaining_stems)
    i_sites_each = tuple(nge4_sites(gram, i_sides) for gram in grams)
    leftover_matching = tuple(
        leftover_extra_remaining_after_009_with_g(
            leftover_sites,
            previous_stems,
            stem,
        )
        for stem in remaining_stems
    )
    extra_each = tuple(
        extra_i_sites(sites, matching)
        for sites, matching in zip(i_sites_each, leftover_matching, strict=True)
    )
    return flatten_extra_i_sites(extra_each)


def leftover_extra_remaining_after_009_extra_i_090_076_sites(
    extra_sites: tuple[tuple[str, str, int], ...],
) -> tuple[tuple[str, str, int], ...]:
    """090-starts one token after extra I W-starts."""
    return tuple(leftover_extra_090_076_site_for_3gram(site) for site in extra_sites)


def leftover_extra_remaining_after_009_extra_i_previous_4grams(
    extra_sites: tuple[tuple[str, str, int], ...],
    i_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, ...] | None, ...]:
    """Per extra I site previous 4-gram X W 090 076, or None if line-initial."""
    extra_090 = leftover_extra_remaining_after_009_extra_i_090_076_sites(extra_sites)
    return leftover_extra_previous_4grams(i_sides, extra_090, GRAM2)


def extra_i_previous_4gram_start_site(
    extra_w_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Previous 4-gram starts one token before the extra I W-start."""
    side, line, index = extra_w_site
    return (side, line, index - 1)


def extra_i_line_initial_sites(
    extra_sites: tuple[tuple[str, str, int], ...],
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Extra I sites with no 4th token X. Do not invent a 4-gram."""
    return tuple(
        site
        for site, gram in zip(extra_sites, per_site_4grams, strict=True)
        if gram is None
    )


def extra_i_continuing_sites(
    extra_sites: tuple[tuple[str, str, int], ...],
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Extra I sites that continue to a 4th token X."""
    return tuple(
        site
        for site, gram in zip(extra_sites, per_site_4grams, strict=True)
        if gram is not None
    )


def distinct_extra_i_previous_4grams(
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, ...], ...]:
    """First-seen distinct extra-I previous 4-grams. Shared X is one 4-gram."""
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
    """Extra I sites whose contiguous previous 4-gram is gram."""
    return tuple(
        site
        for site, prev in zip(extra_sites, per_site_4grams, strict=True)
        if prev == gram
    )


def extra_i_site_subset_of_4gram(
    extra_site: tuple[str, str, int],
    i_sites: tuple[tuple[str, str, int], ...],
) -> bool:
    """True iff extra I 4-gram start ⊆ I sites of its 4-gram."""
    return extra_i_previous_4gram_start_site(extra_site) in i_sites


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
    """True iff N_I==1 and N_off_I=0. Shared previous token is not hapax."""
    return n_i == 1 and n_off_i == 0


def i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    extra_sites: tuple[tuple[str, str, int], ...],
    per_site_4grams: tuple[tuple[str, ...] | None, ...],
    i_sites_each: tuple[tuple[tuple[str, str, int], ...], ...],
    grams: tuple[tuple[str, ...], ...],
    expected_n: int = STANDING_N_DISTINCT_4GRAMS,
) -> bool:
    """True iff every extra-I previous 4-gram is I-only and covered.

    Hapax is not required. Shared previous token / N_I>1 does
    not make the claim lose. Line-initial extra I sites (no
    4th token X) are skipped, not invented. Length must stay
    the distinct extra-I 4-gram count.
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


class TestILeftoverExtra090076RemainingAfter009ExtraIPrev4IOnlyHelpers(
    unittest.TestCase
):
    """Helpers on leftover extra remaining-after-009 extra-I 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. Site 4-grams / 070 000 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("607", "000", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[1], ("700", "008", "090", "076"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_DISTINCT_4GRAMS)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_DISTINCT_4GRAMS)
        self.assertEqual(
            distinct_extra_i_previous_4grams(STANDING_PER_SITE_PREVIOUS_4GRAMS),
            STANDING_SEQUENCES,
        )
        for gram, prev in zip(STANDING_SEQUENCES, STANDING_PREVIOUS_STEMS, strict=True):
            self.assertEqual(gram[2:], GRAM2)
            self.assertEqual(gram[1], prev)
            self.assertEqual(len(gram), STANDING_N4)
            self.assertIn(prev, STANDING_WS_WITH_EXTRA)
            self.assertNotIn(prev, LOCKED_PREVIOUS_STEMS_AFTER_009)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotIn(gram, STANDING_CYCLE285_SITE_4GRAMS_NOT_THIS_CYCLE)
            self.assertNotIn(gram, CYCLE285_PREVIOUS_4GRAMS)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["607", "000", "090", "076", "607", "000", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [list(STANDING_SEQUENCES[0][:2]) + ["006"] + list(STANDING_SEQUENCES[0][2:])]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(
            ngram_hit_count([list(STANDING_CYCLE285_SITE_4GRAMS_NOT_THIS_CYCLE[0])], STANDING_SEQUENCES[0]),
            0,
        )
        planted = ["607", "000", "090", "076"]
        self.assertEqual(site_previous_4gram(planted, 2, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_backward_3gram(planted, 2, GRAM2), ("000", "090", "076"))
        self.assertEqual(site_previous_stem(planted, 2, GRAM2), "000")
        line_initial_after_w = ["000", "090", "076"]
        self.assertEqual(site_backward_3gram(line_initial_after_w, 1, GRAM2), ("000", "090", "076"))
        self.assertEqual(site_previous_stem(line_initial_after_w, 1, GRAM2), "000")
        self.assertIsNone(site_previous_4gram(line_initial_after_w, 1, GRAM2))
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_REMAINING_AFTER_009_SITE_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_490_000_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_727_008_090_076_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_zero_off_i_and_coverage(self):
        """Boolean is True only when all extra-I 4-grams are I-only and covered."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                hold_ones,
                hold_zeros,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                (2, 2),
                hold_zeros,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        lose_off = (1, 0)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                hold_ones,
                lose_off,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        lose_off_shared = (0, 1)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                hold_ones,
                lose_off_shared,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        lose_missing_i = (0, 0)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                lose_missing_i,
                hold_zeros,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                STANDING_I_SITES,
                STANDING_SEQUENCES,
            )
        )
        uncovered = (
            ((SIDE_IA, "Ia5", 64),),
            STANDING_I_SITES[1],
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                hold_ones,
                hold_zeros,
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                uncovered,
                STANDING_SEQUENCES,
            )
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                (),
                (),
                (),
                (),
                (),
                (),
            )
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                hold_ones[:1],
                hold_zeros[:1],
                STANDING_EXTRA_I_SITES,
                STANDING_PER_SITE_PREVIOUS_4GRAMS,
                STANDING_I_SITES[:1],
                STANDING_SEQUENCES[:1],
            )
        )
        self.assertTrue(STANDING_SHARED_PREVIOUS_DOES_NOT_MAKE_CLAIM_LOSE)
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertEqual(STANDING_HAPAX_EACH, (True, True))
        self.assertFalse(sequence_is_hapax(2, 0))
        self.assertTrue(sequence_is_hapax(1, 0))
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_EXTRA_I_PREV4_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_EXTRA_I_PREV4_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(CYCLE207_N_OFF_I, 1)
        self.assertEqual(provider.get_call_history(), [])

    def test_extra_i_sites_are_leftover_of_leftover_not_remaining_sites(self):
        """Extra I sites stay cycle-286 leftover-of-leftover; site 4-grams stay 285."""
        provider = MockProvider()
        self.assertEqual(flatten_extra_i_sites(), STANDING_EXTRA_I_SITES)
        self.assertEqual(len(STANDING_EXTRA_I_SITES), STANDING_N_EXTRA_I)
        self.assertEqual(STANDING_N_EXTRA_I, CYCLE286_N_EXTRA_TOTAL)
        self.assertEqual(STANDING_N_EXTRA_I, 2)
        self.assertEqual(CYCLE286_N_EXTRA_EACH[12], 1)
        self.assertEqual(CYCLE286_N_EXTRA_EACH[22], 1)
        self.assertEqual(CYCLE286_WS_WITH_EXTRA, STANDING_WS_WITH_EXTRA)
        self.assertEqual(STANDING_EXTRA_I_BY_W["000"], ((SIDE_IA, "Ia8", 113),))
        self.assertEqual(STANDING_EXTRA_I_BY_W["008"], ((SIDE_IA, "Ia12", 82),))
        self.assertNotEqual(STANDING_SEQUENCES[0], STANDING_SEQUENCES[1])
        self.assertEqual(
            leftover_extra_remaining_after_009_extra_i_090_076_sites(
                STANDING_EXTRA_I_SITES
            ),
            STANDING_EXTRA_I_090_076_SITES,
        )
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[0], CYCLE224_INSIDE_SITES)
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[0], STANDING_LEFTOVER_057600_COVERED)
        self.assertEqual(LEFTOVER_N4_057600, ("090", "076", "057", "600"))
        self.assertIn(LEFTOVER_N4_057600, CYCLE222_MATCHING)
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[1], CYCLE224_INSIDE_SITES)
        self.assertIn(STANDING_EXTRA_I_090_076_SITES[1], STANDING_LEFTOVER_020010_COVERED)
        self.assertEqual(LEFTOVER_N4_020010, ("090", "076", "020", "010"))
        self.assertIn(LEFTOVER_N4_020010, CYCLE222_MATCHING)
        for site, gram090 in zip(
            STANDING_EXTRA_I_SITES,
            STANDING_EXTRA_I_090_076_SITES,
            strict=True,
        ):
            self.assertNotIn(site, STANDING_REMAINING_SITES)
            self.assertNotIn(gram090, STANDING_REMAINING_SITES)
            self.assertNotIn(gram090, STANDING_LEFTOVER_SITES)
            self.assertEqual(
                leftover_extra_090_076_site_for_3gram(site),
                gram090,
            )
            self.assertEqual(
                extra_i_previous_4gram_start_site(site)[2],
                site[2] - 1,
            )
        for gram in STANDING_CYCLE285_SITE_4GRAMS_NOT_THIS_CYCLE:
            self.assertIn(gram, CYCLE285_PREVIOUS_4GRAMS)
            self.assertNotIn(gram, STANDING_SEQUENCES)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter009ExtraIPrev4IOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-009 extra-I previous-4 off-I lock."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.by_tablet = load_vendored_by_tablet()
        self.previous_stems = leftover_extra_previous_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.leftover_previous_4grams = leftover_extra_previous_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.backwards = leftover_extra_backward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.remaining = leftover_extra_remaining_after_009(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_stems = leftover_extra_remaining_after_009_previous_stems(
            self.leftover_sites,
            self.previous_stems,
        )
        self.grams3 = remaining_after_009_3grams(self.remaining_stems)
        self.i_sites3 = tuple(nge4_sites(gram, self.i_sides) for gram in self.grams3)
        self.leftover_matching = tuple(
            leftover_extra_remaining_after_009_with_g(
                self.leftover_sites,
                self.previous_stems,
                stem,
            )
            for stem in self.remaining_stems
        )
        self.extra_each = tuple(
            extra_i_sites(sites, matching)
            for sites, matching in zip(
                self.i_sites3,
                self.leftover_matching,
                strict=True,
            )
        )
        self.extra_sites = leftover_extra_remaining_after_009_extra_i_sites(
            self.leftover_sites,
            self.previous_stems,
            self.i_sides,
        )
        self.extra_090 = leftover_extra_remaining_after_009_extra_i_090_076_sites(
            self.extra_sites,
        )
        self.per_site_previous_4grams = (
            leftover_extra_remaining_after_009_extra_i_previous_4grams(
                self.extra_sites,
                self.i_sides,
            )
        )
        self.line_initial = extra_i_line_initial_sites(
            self.extra_sites,
            self.per_site_previous_4grams,
        )
        self.continuing = extra_i_continuing_sites(
            self.extra_sites,
            self.per_site_previous_4grams,
        )
        self.grams = distinct_extra_i_previous_4grams(self.per_site_previous_4grams)
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
        self.g, self.k, self.unique = select_remaining_after_009_g(
            self.remaining_stems
        )
        self.unique_max = i_leftover_extra_090_076_remaining_after_009_unique_previous_stem(
            self.leftover_sites,
            self.previous_stems,
        )
        self.site_previous_4grams = leftover_extra_remaining_after_009_previous_4grams(
            self.leftover_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.site_line_initial = leftover_extra_remaining_after_009_line_initial_sites(
            self.leftover_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.site_continuing = leftover_extra_remaining_after_009_continuing_sites(
            self.leftover_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.claim_holds = (
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                self.n_i,
                self.n_off_i,
                self.extra_sites,
                self.per_site_previous_4grams,
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

    def test_tokens_and_sites_are_cycle_286_extra_i_not_retuned(self):
        """4-grams stay the cycle-286 extra I previouss. Nested 27/K=1/G=724 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(self.leftover_sites), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE284_REMAINING_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_PREVIOUS_STEMS)
        self.assertEqual(len(self.remaining), STANDING_N_REMAINING_AFTER_009)
        self.assertEqual(STANDING_N_REMAINING_AFTER_009, 27)
        self.assertEqual(self.g, CYCLE284_G)
        self.assertEqual(self.g, "724")
        self.assertEqual(self.k, CYCLE284_K)
        self.assertEqual(self.k, 1)
        self.assertFalse(self.unique)
        self.assertFalse(CYCLE284_UNIQUE)
        self.assertFalse(self.unique_max)
        self.assertFalse(CYCLE284_CLAIM)
        if (
            len(self.remaining) != 27
            or self.k != 1
            or self.g != "724"
            or self.unique
            or self.unique_max
        ):
            self.fail("nested cycle 284 unique-max false N_remaining_after_009=27 K=1 G=724 drifted")
        self.assertEqual(self.remaining_stems, CYCLE284_REMAINING_PREVIOUS_STEMS)
        self.assertEqual(self.site_previous_4grams, CYCLE285_PREVIOUS_4GRAMS)
        self.assertEqual(self.site_line_initial, ())
        self.assertEqual(len(self.site_continuing), 27)
        self.assertEqual(self.extra_each, CYCLE286_EXTRA_I_SITES_EACH)
        self.assertEqual(sum(len(row) for row in self.extra_each), CYCLE286_N_EXTRA_TOTAL)
        self.assertEqual(sum(len(row) for row in self.extra_each), 2)
        self.assertEqual(self.extra_sites, STANDING_EXTRA_I_SITES)
        self.assertEqual(self.extra_sites, flatten_extra_i_sites(self.extra_each))
        self.assertEqual(self.extra_each[12], STANDING_EXTRA_I_BY_W["000"])
        self.assertEqual(self.extra_each[22], STANDING_EXTRA_I_BY_W["008"])
        if self.extra_sites != STANDING_EXTRA_I_SITES:
            self.fail("nested cycle 286 extra I sites drifted from Ia8[113]/Ia12[82]")
        self.assertEqual(self.extra_090, STANDING_EXTRA_I_090_076_SITES)
        self.assertTrue(
            leftover_extra_remaining_after_009_nested_counts_hold(
                69,
                56,
                15,
                41,
                4,
                37,
                2,
                27,
            )
        )
        prior_286 = self.survey["i_leftover_extra_090_076_remaining_after_009_3grams_i_only"]
        self.assertEqual(prior_286["cycle"], 286)
        self.assertEqual(prior_286["N_i_only"], 27)
        self.assertEqual(prior_286["N_not_i_only"], 0)
        self.assertEqual(prior_286["N_extra_total"], 2)
        self.assertTrue(prior_286["i_leftover_extra_090_076_remaining_after_009_3grams_all_i_only"])
        self.assertTrue(CYCLE286_CLAIM)
        self.assertEqual(CYCLE286_N_I_ONLY, 27)
        self.assertEqual(CYCLE286_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE286_N_EXTRA_TOTAL, 2)
        prior_285 = self.survey["i_leftover_extra_090_076_remaining_after_009_prev4_i_only"]
        self.assertEqual(prior_285["cycle"], 285)
        self.assertEqual(prior_285["N_i_only"], 27)
        self.assertEqual(prior_285["N_not_i_only"], 0)
        self.assertTrue(prior_285["i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only"])
        self.assertTrue(CYCLE285_CLAIM)
        prior_284 = self.survey["i_leftover_extra_090_076_remaining_after_009_previous_stem"]
        self.assertEqual(prior_284["cycle"], 284)
        self.assertEqual(prior_284["N_remaining_after_009"], 27)
        self.assertEqual(prior_284["K"], 1)
        self.assertEqual(prior_284["G"], "724")
        self.assertFalse(prior_284["G_uniquely_most_frequent"])
        prior_259 = self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]
        self.assertEqual(prior_259["cycle"], 259)
        self.assertEqual(prior_259["N_i_only"], 2)
        self.assertEqual(prior_259["N_not_i_only"], 0)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        prior_219 = self.survey["i_090_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_219["cycle"], 219)
        self.assertEqual(prior_219["N_i_only"], 7)
        self.assertEqual(prior_219["N_not_i_only"], 1)
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_extra_i_4gram_lock_and_claim_holds(self):
        """Extra-I previous 4-grams are I-only. Shared X / N_I>1 would not lose."""
        self.assertEqual(self.per_site_previous_4grams, STANDING_PER_SITE_PREVIOUS_4GRAMS)
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(self.line_initial, ())
        self.assertEqual(self.continuing, STANDING_EXTRA_I_SITES)
        self.assertEqual(len(self.grams), STANDING_N_DISTINCT_4GRAMS)
        self.assertEqual(STANDING_N_DISTINCT_4GRAMS, 2)
        self.assertEqual(len(self.continuing), STANDING_N_WITH_FOURTH)
        self.assertEqual(STANDING_N_WITH_FOURTH, 2)
        self.assertEqual(len(self.line_initial), STANDING_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
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
        if self.line_initial:
            self.fail("measured line-initial extra I set drifted from empty")
        if self.leaking:
            self.fail("measured extra-I previous 4-grams leaked off I")
        self.assertTrue(
            extra_i_sites_covered_by_4grams(
                self.extra_sites,
                self.per_site_previous_4grams,
                self.i_sites,
                self.grams,
            )
        )
        for site, gram4, prev, gram090 in zip(
            STANDING_EXTRA_I_SITES,
            STANDING_PER_SITE_PREVIOUS_4GRAMS,
            STANDING_PER_SITE_W,
            STANDING_EXTRA_I_090_076_SITES,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, gram090)
            self.assertEqual(tuple(stems[gram090[2] - 2 : gram090[2] + STANDING_N2]), gram4)
            self.assertEqual(stems[gram090[2] - 1], prev)
            self.assertEqual(tuple(stems[gram090[2] : gram090[2] + STANDING_N2]), GRAM2)
            self.assertEqual(site_previous_4gram(stems, gram090[2], GRAM2), gram4)
            self.assertEqual(site_backward_3gram(stems, gram090[2], GRAM2), (prev, "090", "076"))
            self.assertGreater(gram090[2], 1)
            self.assertNotIn(prev, LOCKED_PREVIOUS_STEMS_AFTER_009)
            self.assertIn(gram090, CYCLE224_INSIDE_SITES)
            self.assertNotIn(gram090, STANDING_REMAINING_SITES)
            self.assertEqual(leftover_extra_090_076_site_for_3gram(site), gram090)
            self.assertEqual(
                extra_i_previous_4gram_start_site(site),
                (site[0], site[1], site[2] - 1),
            )
        for gram, prev, role, sites, extra, n_on, n_off, hapax in zip(
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
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
                    STANDING_PER_SITE_PREVIOUS_4GRAMS,
                    gram,
                ),
                extra,
            )
            for site in extra:
                self.assertTrue(extra_i_site_subset_of_4gram(site, sites))
                self.assertEqual(extra_i_previous_4gram_start_site(site), sites[0])
            self.assertEqual(gram[1], prev)
            self.assertEqual(role, "leftover_extra_remaining_after_009_extra_i")
            self.assertGreaterEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
            self.assertEqual(sequence_is_hapax(n_on, n_off), hapax)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotIn(gram, CYCLE285_PREVIOUS_4GRAMS)
        self.assertTrue(STANDING_HAPAX_EACH[0])
        self.assertTrue(STANDING_HAPAX_EACH[1])
        self.assertEqual(STANDING_SEQUENCES[0][0], "607")
        self.assertEqual(STANDING_SEQUENCES[1][0], "700")
        self.assertIn((SIDE_IA, "Ia8", 114), STANDING_LEFTOVER_057600_COVERED)
        self.assertIn((SIDE_IA, "Ia12", 83), STANDING_LEFTOVER_020010_COVERED)
        self.assertIn(("090", "076", "057", "600"), CYCLE222_MATCHING)
        self.assertIn(("090", "076", "020", "010"), CYCLE222_MATCHING)
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        if not self.claim_holds:
            self.fail("measured extra-I previous 4-grams are not all I-only")
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_SHARED_PREVIOUS_DOES_NOT_MAKE_CLAIM_LOSE)
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
            if index >= 2:
                t_prev4 = tuple(stems[index - 2 : index + 2])
                self.assertNotIn(t_prev4, STANDING_SEQUENCES)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertEqual(
            i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only(
                self.n_i,
                self.n_off_i,
                self.extra_sites,
                self.per_site_previous_4grams,
                self.i_sites,
                self.grams,
            ),
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_EXTRA_I_PREV4_ALL_I_ONLY,
        )
        self.assertTrue(self.claim_holds)
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_DO_NOT_PEEL_LEFTOVER_EXTRA_I_PREVIOUS_STEMS)
        self.assertTrue(STANDING_REMAINING_AFTER_009_SITE_4GRAMS_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_FORWARD_PEEL_NOT_RETUNED)
        self.assertFalse(STANDING_SAME_AS_CYCLE207)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE259)
        self.assertFalse(STANDING_SAME_AS_CYCLE285)
        self.assertFalse(STANDING_SAME_AS_CYCLE286)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE207)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE259)
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_286_285_284_259_223_219_and_167_still_compute(self):
        """Cycle 286 27/0 extra I=2, 285 27/0 hapax, 284 unique-max lose 27/K=1/G=724, 259 2/0, 223 69/3, 219 T leak, 167 16/0 stay."""
        prior_286 = TestMamariILeftoverExtra090076RemainingAfter0093gramsIOnlyScoreboard()
        prior_286.setUp()
        prior_286.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_286.test_survey_matches_computed_lock()
        self.assertEqual(prior_286.n_i_only, 27)
        self.assertEqual(prior_286.n_not_i_only, 0)
        self.assertEqual(sum(prior_286.n_extra), 2)
        self.assertEqual(prior_286.extra, CYCLE286_EXTRA_I_SITES_EACH)
        self.assertTrue(prior_286.claim_holds)
        self.assertTrue(CYCLE286_CLAIM)
        if (
            prior_286.n_i_only != 27
            or prior_286.n_not_i_only != 0
            or sum(prior_286.n_extra) != 2
        ):
            self.fail("nested cycle 286 remaining-after-009 3-grams 27/0 extra I=2 drifted")
        prior_285 = TestMamariILeftoverExtra090076RemainingAfter009Prev4IOnlyScoreboard()
        prior_285.setUp()
        prior_285.test_each_4gram_is_one_on_i_zero_off_i_no_line_initial_and_claim_holds()
        prior_285.test_survey_matches_computed_lock()
        self.assertEqual(prior_285.n_i_only, 27)
        self.assertEqual(prior_285.n_not_i_only, 0)
        self.assertTrue(prior_285.claim_holds)
        self.assertTrue(CYCLE285_CLAIM)
        if prior_285.n_i_only != 27 or prior_285.n_not_i_only != 0:
            self.fail("nested cycle 285 remaining-after-009 previous 4-grams 27/0 hapax drifted")
        prior_284 = TestMamariILeftoverExtra090076RemainingAfter009PrevStemScoreboard()
        prior_284.setUp()
        prior_284.test_counts_27_remaining_all_hapax_g_724_k_1_and_hypothesis_loses()
        prior_284.test_survey_matches_computed_lock()
        self.assertEqual(prior_284.n_remaining, 27)
        self.assertEqual(prior_284.k, 1)
        self.assertEqual(prior_284.g, "724")
        self.assertFalse(prior_284.unique)
        self.assertFalse(prior_284.claim_holds)
        self.assertFalse(CYCLE284_CLAIM)
        if (
            prior_284.n_remaining != 27
            or prior_284.k != 1
            or prior_284.g != "724"
            or prior_284.unique
        ):
            self.fail("nested cycle 284 unique-max false N_remaining_after_009=27 K=1 G=724 drifted")
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_259.test_survey_matches_computed_lock()
        self.assertEqual(prior_259.n_i_only, 2)
        self.assertEqual(prior_259.n_not_i_only, 0)
        self.assertTrue(prior_259.claim_holds)
        self.assertTrue(CYCLE259_CLAIM)
        if prior_259.n_i_only != 2 or prior_259.n_not_i_only != 0:
            self.fail("nested cycle 259 extra-I forward 4-grams 2/0 drifted")
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
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(prior_167.i_hits, CYCLE167_N_I)
        self.assertEqual(prior_167.off_i_hits, CYCLE167_N_OFF_I)
        self.assertTrue(prior_167.claim_holds)
        self.assertTrue(CYCLE167_CLAIM)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
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
        """CORPUS_SURVEY.json records the cycle-287 extra-I previous-4 I-only lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]
        self.assertEqual(lock["cycle"], 287)
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
        self.assertEqual(lock["N_remaining_after_009"], STANDING_N_REMAINING_AFTER_009)
        self.assertEqual(lock["N_remaining_after_009"], 27)
        self.assertEqual(lock["N_distinct_remaining"], STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(lock["K"], 1)
        self.assertEqual(lock["G"], "724")
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertFalse(lock["i_leftover_extra_090_076_remaining_after_009_unique_previous_stem"])
        self.assertEqual(
            tuple(lock["locked_previous_stems_after_009"]),
            LOCKED_PREVIOUS_STEMS_AFTER_009,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_009_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_009_previous_stems"]),
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_extra_i"], STANDING_N_EXTRA_I)
        self.assertEqual(lock["N_extra_i"], 2)
        self.assertEqual(
            tuple(tuple(row) for row in lock["extra_i_sites"]),
            STANDING_EXTRA_I_SITES,
        )
        self.assertEqual(
            [list(site) for site in STANDING_EXTRA_I_BY_W["000"]],
            lock["extra_i_sites_000"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_EXTRA_I_BY_W["008"]],
            lock["extra_i_sites_008"],
        )
        self.assertEqual(tuple(lock["ws_with_extra"]), STANDING_WS_WITH_EXTRA)
        self.assertEqual(
            [list(site) for site in STANDING_EXTRA_I_090_076_SITES],
            lock["extra_i_090_076_sites"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS],
            lock["extra_i_per_site_previous_4grams"],
        )
        self.assertEqual(lock["N_with_fourth"], 2)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["line_initial_extra_i_sites"], [])
        self.assertTrue(lock["all_extra_i_have_fourth_token"])
        self.assertEqual(lock["N_distinct_4grams"], 2)
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["extra_i_previous_4grams"],
        )
        self.assertTrue(lock["not_assumed_hapax"])
        self.assertTrue(lock["shared_previous_does_not_make_claim_lose"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_DISTINCT_4GRAMS)
        for row, gram, prev, role, sites, extra, n_on, n_off, hapax in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_EXTRA_I_SITES_EACH,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            STANDING_HAPAX_EACH,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(row["previous_stem"], prev)
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
            lock["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only"]
        )
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]
        )
        self.assertEqual(lock["N_i_only"], 2)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(lock["off_i_tablets_with_hits"], [])
        self.assertTrue(lock["shared_previous_does_not_make_claim_lose"])
        self.assertEqual(lock["nested_cycle286_N_i_only"], 27)
        self.assertEqual(lock["nested_cycle286_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle286_N_extra"], 2)
        self.assertEqual(lock["nested_cycle285_N_i_only"], 27)
        self.assertEqual(lock["nested_cycle285_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle284_N_remaining_after_009"], 27)
        self.assertEqual(lock["nested_cycle284_K"], 1)
        self.assertEqual(lock["nested_cycle284_G"], "724")
        self.assertFalse(lock["nested_cycle284_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle259_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle259_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle219_N_i_only"], 7)
        self.assertEqual(lock["nested_cycle219_N_not_i_only"], 1)
        self.assertEqual(tuple(lock["nested_cycle219_leak_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(lock["nested_cycle207_N_I"], 8)
        self.assertEqual(lock["nested_cycle207_N_off_I"], 1)
        self.assertEqual(tuple(lock["nested_cycle207_off_i_sites"][0]), CYCLE207_OFF_I_SITES[0])
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167"])
        self.assertFalse(lock["same_as_cycle207"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle259"])
        self.assertFalse(lock["same_as_cycle284"])
        self.assertFalse(lock["same_as_cycle285"])
        self.assertFalse(lock["same_as_cycle286"])
        self.assertTrue(lock["same_claim_shape_as_cycle207"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["same_claim_shape_as_cycle259"])
        self.assertTrue(lock["do_not_peel_leftover_extra_i_previous_stems"])
        self.assertTrue(lock["previous_stems_of_090_076_are_not_this_cycle"])
        self.assertTrue(lock["remaining_after_009_site_4grams_are_not_this_cycle"])
        self.assertTrue(lock["999_090_076_does_not_count"])
        self.assertTrue(lock["600_090_076_does_not_count"])
        self.assertTrue(lock["090_090_076_does_not_count"])
        self.assertTrue(lock["076_090_076_does_not_count"])
        self.assertTrue(lock["071_090_076_does_not_count"])
        self.assertTrue(lock["045_090_076_does_not_count"])
        self.assertTrue(lock["009_090_076_does_not_count"])
        self.assertTrue(lock["490_000_090_076_does_not_count"])
        self.assertTrue(lock["727_008_090_076_does_not_count"])
        self.assertTrue(lock["090_076_070_000_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_are_this_cycle_only_if_matching_4gram"])
        self.assertTrue(lock["raw_stems_090_kept"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_009_3grams_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_009_prev4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_009_previous_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_3grams_i_only"]["cycle"],
            286,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_prev4_i_only"]["cycle"],
            285,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_previous_stem"]["cycle"],
            284,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]["cycle"],
            259,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter009ExtraIPrev4IOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 287 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
