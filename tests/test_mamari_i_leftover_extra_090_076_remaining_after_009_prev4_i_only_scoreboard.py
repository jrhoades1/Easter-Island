"""I's cycle-284 leftover extra remaining-after-009 previous-4 off-I lock.

Cycle 285 text-search lock. Uses already-vendored A–V and the
cycle-284 leftover extra remaining-after-009 I sites of 2-gram
090 076 (the 27 leftover extra with-previous sites whose
previous token is none of 999, 600, 090, 076, 071, 045, or
009). Does not retune those 4-grams, leftover extra
remaining-after-009 unique-max (cycle 284 lost: 27 hapax,
G=724 K=1), leftover extra remaining-after-045 previous-009
(cycle 281 K=2 N_remaining=27), leftover extra remaining-
after-600 unique-max (cycle 270 lost 5-way K=2), leftover
extra sites, leftover n=4, or the already-closed leftover
remaining family. Does not retune the forward peel (225–259).
Does not overwrite cycle 167's 3-gram I-only 16/0 lock. Does
not overwrite cycles 268–284. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Same claim-shape as cycle 257 leftover extra remaining-after-
000 forward 4-grams all I-only hapax 1/0 x19, previous side
instead of forward. Cycle 284 leftover extra remaining-after-
009 unique-max lost N_remaining_after_009=27 K=1 27-way tie
G=724, cycle 283 I 009 090 076 previous-4 all I-only hapax
2/0, cycle 282 009 090 076 I-only 2/0 extra I=0, cycle 281
K_009=2 N_remaining=27, cycle 270 5-way tie at 2, cycle 257
19/19 hapax, cycle 223 69/3, and cycle 167 16/0 stay.
Nested-check leftover extra remaining-after-009 unique-max
false, N_remaining_after_009==27, K==1, 27 distinct previous
stems, G=724 (do not retune cycle 284). Nested-check each
remaining-after-009 site has a previous token W. If a site is
line-initial after W (3-gram W 090 076 with no 4th token X),
lock that as no previous 4-gram rather than inventing one;
that site then does not count as a 4-gram hapax. Measure; do
not assume all 27 have a 4th token. Do not peel a specific
remaining-after-009 stem this cycle. Do not lock 3-grams of
remaining-after-009 previous stems (later cycle if this
holds, analog of cycle 258). Off-I T sites are this cycle
only as off-I of a remaining-after-009 previous 4-gram if
they match. 999 090 076, 600 090 076, 090 090 076,
076 090 076, 071 090 076, 045 090 076, 009 090 076,
009 009 090 076, and 071 009 090 076 do not count. Do not
retune leftover n=4, 076-cells, or any detector.

Locks exact consecutive hits of each continuing leftover
extra remaining-after-009 previous 4-gram on tablet I and on
every other vendored tablet A–H and J–V. The twenty-seven
4-grams: 027 048 090 076, 380 380 090 076, 076 011 090 076,
070 499 090 076, 050 497 090 076, 061 036 090 076,
090 092 090 076, 087 291 090 076, 460 522 090 076,
010 150 090 076, 087 078 090 076, 071 295 090 076,
490 000 090 076, 090 109 090 076, 055 052 090 076,
000 099 090 076, 670 700 090 076, 076 161 090 076,
208 010 090 076, 072 205 090 076, 071 382 090 076,
011 386 090 076, 727 008 090 076, 070 027 090 076,
724 724 090 076, 007 400 090 076, 600 326 090 076.
Do not assume hapax; count each from fixtures. Hypothesis:
all continuing remaining-after-009 previous 4-grams are
I-only. Measured: each N_I=1 at the previous-4 start two
tokens before the cycle-284 remaining-after-009 site; all
N_off_I=0; no remaining-after-009 site is line-initial after
W (all 27 have a 4th token X). Cycle 281 previous-009 sites
Ia2[174]/Ia5[164] are excluded. Claim that can lose:
i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only.
True iff every continuing remaining-after-009 previous
4-gram has N_I ≥ 1 and N_off_I = 0 (hapax 1/0 expected
given K=1). This can lose if any leaks off I (same shape
as cycle 219 090 076 070 000 1/1 on T). The claim is true.
Do not assume hapax; measure. Do not retune.

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
from tests.test_mamari_i_009_090_076_previous_4grams_i_only_scoreboard import (
    STANDING_I_009_090_076_PREVIOUS_4GRAMS_ALL_I_ONLY_HAPAX as CYCLE283_ALL_HAPAX,
    STANDING_N_I_ONLY as CYCLE283_N_I_ONLY,
    STANDING_N_NOT_HAPAX as CYCLE283_N_NOT_HAPAX,
    STANDING_N_NOT_I_ONLY as CYCLE283_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE283_SEQUENCES,
    TestMamariI009090076Previous4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_090_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE219_CLAIM,
    STANDING_N_I_ONLY as CYCLE219_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE219_N_NOT_I_ONLY,
    STANDING_OFF_I_FORWARD_4GRAM as CYCLE219_LEAK_4GRAM,
    TestMamariI090076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
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
    STANDING_OFF_I_SITES as CYCLE223_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_009_090_076_i_only_scoreboard import (
    GRAM3 as CYCLE282_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE282_EXTRA_I_SITES,
    STANDING_I_3GRAM_009_090_076_I_ONLY as CYCLE282_CLAIM,
    STANDING_I_PREVIOUS_4GRAMS as CYCLE282_PREVIOUS_4GRAMS,
    STANDING_I_SITES as CYCLE282_I_SITES,
    STANDING_N_EXTRA as CYCLE282_N_EXTRA,
    STANDING_N_I as CYCLE282_N_I,
    STANDING_N_OFF_I as CYCLE282_N_OFF_I,
    TestMamariI3gram009090076IOnlyScoreboard,
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
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_FORWARD_4GRAMS_ALL_I_ONLY as CYCLE257_CLAIM,
    STANDING_N_I_ONLY as CYCLE257_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE257_N_NOT_I_ONLY,
    STANDING_REMAINING11_NEXT_4GRAMS as CYCLE257_NEXT_4GRAMS,
    TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_045_prev009_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_REMAINING_AFTER_090_REMAINING_AFTER_076_REMAINING_AFTER_071_REMAINING_AFTER_045_EXACTLY_2_SHARE_PREVIOUS_009 as CYCLE281_CLAIM,
    STANDING_K_009 as CYCLE281_K_009,
    STANDING_MATCHING_SITES as CYCLE281_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_090_AND_076_AND_071_AND_045_AND_009 as CYCLE281_N_REMAINING_AFTER_045_AND_009,
    leftover_extra_remaining_after_090_and_076_and_071_and_045_without_previous_009,
    TestMamariILeftoverExtra090076RemainingAfter045Prev009Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_prev_stem_scoreboard import (
    LOCKED_PREVIOUS_STEMS_AFTER_009,
    STANDING_CYCLE281_009_SITES as CYCLE281_009_SITES,
    STANDING_G as CYCLE284_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE284_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_UNIQUE_PREVIOUS_STEM as CYCLE284_CLAIM,
    STANDING_K as CYCLE284_K,
    STANDING_MATCHING_PREVIOUS_4GRAMS as CYCLE284_MATCHING_PREVIOUS_4GRAMS,
    STANDING_MATCHING_SITES as CYCLE284_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING as CYCLE284_N_DISTINCT,
    STANDING_N_NO_PREVIOUS as CYCLE284_N_NO_PREVIOUS,
    STANDING_N_REMAINING_AFTER_009 as CYCLE284_N_REMAINING,
    STANDING_N_WITH_PREVIOUS as CYCLE284_N_WITH_PREVIOUS,
    STANDING_REMAINING_PREVIOUS_STEMS as CYCLE284_REMAINING_PREVIOUS_STEMS,
    STANDING_REMAINING_SITES as CYCLE284_REMAINING_SITES,
    i_leftover_extra_090_076_remaining_after_009_unique_previous_stem,
    leftover_extra_remaining_after_009,
    leftover_extra_remaining_after_009_nested_counts_hold,
    leftover_extra_remaining_after_009_previous_stems,
    leftover_extra_remaining_after_009_with_previous,
    leftover_extra_remaining_after_009_without_previous,
    select_remaining_after_009_g,
    TestMamariILeftoverExtra090076RemainingAfter009PrevStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_stem_scoreboard import (
    STANDING_G as CYCLE270_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE270_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE270_CLAIM,
    STANDING_K as CYCLE270_K,
    STANDING_N_REMAINING_AFTER_600 as CYCLE270_N_REMAINING,
    STANDING_N_TIED_AT_K as CYCLE270_N_TIED_AT_K,
    STANDING_TIED_STEMS as CYCLE270_TIED_STEMS,
    TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard,
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
STANDING_N_REMAINING_AFTER_009 = 27
STANDING_N_DISTINCT_REMAINING = 27
STANDING_N_CONTINUING = 27
STANDING_N_NO_PREVIOUS = 0
STANDING_N_LINE_INITIAL = 0
STANDING_REMAINING_SITES = CYCLE284_REMAINING_SITES
STANDING_REMAINING_PREVIOUS_STEMS = CYCLE284_REMAINING_PREVIOUS_STEMS
STANDING_REMAINING_PREVIOUS_4GRAMS = (
    ("027", "048", "090", "076"),
    ("380", "380", "090", "076"),
    ("076", "011", "090", "076"),
    ("070", "499", "090", "076"),
    ("050", "497", "090", "076"),
    ("061", "036", "090", "076"),
    ("090", "092", "090", "076"),
    ("087", "291", "090", "076"),
    ("460", "522", "090", "076"),
    ("010", "150", "090", "076"),
    ("087", "078", "090", "076"),
    ("071", "295", "090", "076"),
    ("490", "000", "090", "076"),
    ("090", "109", "090", "076"),
    ("055", "052", "090", "076"),
    ("000", "099", "090", "076"),
    ("670", "700", "090", "076"),
    ("076", "161", "090", "076"),
    ("208", "010", "090", "076"),
    ("072", "205", "090", "076"),
    ("071", "382", "090", "076"),
    ("011", "386", "090", "076"),
    ("727", "008", "090", "076"),
    ("070", "027", "090", "076"),
    ("724", "724", "090", "076"),
    ("007", "400", "090", "076"),
    ("600", "326", "090", "076"),
)
STANDING_SEQUENCES = STANDING_REMAINING_PREVIOUS_4GRAMS
STANDING_CONTINUING_SITES = STANDING_REMAINING_SITES
STANDING_LINE_INITIAL_SITES = ()
STANDING_NO_PREVIOUS_SITES = ()
STANDING_PREVIOUS_STEMS = STANDING_REMAINING_PREVIOUS_STEMS
STANDING_ROLES = ("leftover_extra_remaining_after_009",) * STANDING_N_CONTINUING
STANDING_N_I_EACH = (1,) * STANDING_N_CONTINUING
STANDING_N_ON_I_EACH = (1,) * STANDING_N_CONTINUING
STANDING_I_SITES = tuple(
    ((side, line, index - 2),) for side, line, index in STANDING_CONTINUING_SITES
)
STANDING_IB_HITS = 0
STANDING_IB_SITES = ()
STANDING_N_OFF_I_EACH = (0,) * STANDING_N_CONTINUING
STANDING_OFF_I_SITES = ((),) * STANDING_N_CONTINUING
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET_ONE_ON_I = tuple(
    1 if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_HITS_BY_TABLET = (STANDING_HITS_BY_TABLET_ONE_ON_I,) * STANDING_N_CONTINUING
STANDING_N_I_ONLY = 27
STANDING_N_NOT_I_ONLY = 0
STANDING_LEAKING_4GRAMS = ()
STANDING_CYCLE281_009_EXCLUDED = True
STANDING_ALL_REMAINING_HAVE_PREVIOUS_TOKEN = True
STANDING_ALL_REMAINING_HAVE_FOURTH_TOKEN = True
STANDING_KNOWN_DISTINCT = True
STANDING_NOT_ASSUMED_HAPAX = True
STANDING_HAPAX_EACH = True
STANDING_CLAIM = (
    "i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only"
)
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_ALL_I_ONLY = True
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_I_ONLY = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_009_prev4_i_only"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE167 = False
STANDING_SAME_AS_CYCLE219 = False
STANDING_SAME_AS_CYCLE223 = False
STANDING_SAME_AS_CYCLE257 = False
STANDING_SAME_AS_CYCLE270 = False
STANDING_SAME_AS_CYCLE281 = False
STANDING_SAME_AS_CYCLE282 = False
STANDING_SAME_AS_CYCLE283 = False
STANDING_SAME_AS_CYCLE284 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE257 = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_DO_NOT_LOCK_REMAINING_AFTER_009_3GRAMS = True
STANDING_009_090_076_DOES_NOT_COUNT = True
STANDING_009_009_090_076_DOES_NOT_COUNT = True
STANDING_071_009_090_076_DOES_NOT_COUNT = True
STANDING_999_090_076_DOES_NOT_COUNT = True
STANDING_600_090_076_DOES_NOT_COUNT = True
STANDING_090_090_076_DOES_NOT_COUNT = True
STANDING_076_090_076_DOES_NOT_COUNT = True
STANDING_071_090_076_DOES_NOT_COUNT = True
STANDING_045_090_076_DOES_NOT_COUNT = True
STANDING_090_076_070_000_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_FORWARD_PEEL_NOT_RETUNED = True
STANDING_OFF_I_T_SITES_ARE_THIS_CYCLE_ONLY_IF_MATCHING_4GRAM = True
STANDING_CYCLE284_N_REMAINING = 27
STANDING_CYCLE284_K = 1
STANDING_CYCLE284_G = "724"
STANDING_CYCLE284_UNIQUE = False
STANDING_CYCLE283_N_I_ONLY = 2
STANDING_CYCLE283_N_NOT_I_ONLY = 0
STANDING_CYCLE282_N_I = 2
STANDING_CYCLE282_N_OFF_I = 0
STANDING_CYCLE282_N_EXTRA = 0
STANDING_CYCLE281_K = 2
STANDING_CYCLE281_G = "009"
STANDING_CYCLE281_N_REMAINING = 27
STANDING_CYCLE270_N_TIED_AT_K = 5
STANDING_CYCLE257_N_I_ONLY = 19
STANDING_CYCLE257_N_NOT_I_ONLY = 0
STANDING_CYCLE223_N_I = 69
STANDING_CYCLE223_N_OFF_I = 3
STANDING_CYCLE167_N_I = 16
STANDING_CYCLE167_N_OFF_I = 0


def leftover_previous_4gram_start_site(
    remaining_site: tuple[str, str, int],
) -> tuple[str, str, int]:
    """Previous 4-gram starts two tokens before the remaining-after-009 site."""
    side, line, index = remaining_site
    return (side, line, index - 2)


def leftover_extra_remaining_after_009_previous_4grams(
    leftover_sites: tuple[tuple[str, str, int], ...],
    leftover_previous_4grams: tuple[tuple[str, ...] | None, ...],
    leftover_previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_009,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per remaining-after-009 site previous 4-gram or None if line-initial after W."""
    locked_set = set(locked)
    return tuple(
        gram
        for prev, gram in zip(
            leftover_previous_stems,
            leftover_previous_4grams,
            strict=True,
        )
        if prev is not None and prev not in locked_set
    )


def leftover_extra_remaining_after_009_line_initial_sites(
    leftover_sites: tuple[tuple[str, str, int], ...],
    leftover_previous_4grams: tuple[tuple[str, ...] | None, ...],
    leftover_previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_009,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-009 sites with a previous stem and no 4th token X."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev, gram in zip(
            leftover_sites,
            leftover_previous_stems,
            leftover_previous_4grams,
            strict=True,
        )
        if prev is not None and prev not in locked_set and gram is None
    )


def leftover_extra_remaining_after_009_continuing_sites(
    leftover_sites: tuple[tuple[str, str, int], ...],
    leftover_previous_4grams: tuple[tuple[str, ...] | None, ...],
    leftover_previous_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_PREVIOUS_STEMS_AFTER_009,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-009 sites that continue to a 4th token X."""
    locked_set = set(locked)
    return tuple(
        site
        for site, prev, gram in zip(
            leftover_sites,
            leftover_previous_stems,
            leftover_previous_4grams,
            strict=True,
        )
        if prev is not None and prev not in locked_set and gram is not None
    )


def continuing_previous_4grams(
    per_site_previous_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[tuple[str, ...], ...]:
    """Distinct-preserving continuing remaining-after-009 previous 4-grams."""
    return tuple(gram for gram in per_site_previous_4grams if gram is not None)


def sequence_is_i_only(n_i: int, n_off_i: int) -> bool:
    """True iff N_I>=1 and N_off_I=0."""
    return n_i >= 1 and n_off_i == 0


def i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
    n_i: tuple[int, ...],
    n_off_i: tuple[int, ...],
    expected_n: int = STANDING_N_CONTINUING,
) -> bool:
    """True iff every continuing remaining-after-009 previous 4-gram is I-only.

    Claim holds only if every continuing gram has N_off_I=0 and
    N_I>=1. Hapax is not assumed; N_I may be greater than 1.
    Line-initial remaining-after-009 sites (no 4th token X) do
    not count as 4-gram hapax and are not invented. Length must
    stay the continuing count.
    """
    return (
        len(n_i) == expected_n
        and len(n_off_i) == expected_n
        and all(
            sequence_is_i_only(on, off)
            for on, off in zip(n_i, n_off_i, strict=True)
        )
    )


class TestILeftoverExtra090076RemainingAfter009Prev4IOnlyHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-009 previous 4-grams. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit. 009 / 009 009 are not."""
        provider = MockProvider()
        self.assertEqual(STANDING_SEQUENCES[0], ("027", "048", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[24], ("724", "724", "090", "076"))
        self.assertEqual(STANDING_SEQUENCES[-1], ("600", "326", "090", "076"))
        self.assertEqual(len(STANDING_SEQUENCES), STANDING_N_CONTINUING)
        self.assertEqual(len(set(STANDING_SEQUENCES)), STANDING_N_CONTINUING)
        for gram in STANDING_SEQUENCES:
            self.assertEqual(gram[2:], GRAM2)
            self.assertEqual(len(gram), STANDING_N4)
            self.assertNotEqual(gram[1:], CYCLE282_GRAM3)
            self.assertNotIn(gram, CYCLE283_SEQUENCES)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
        adjacent = [list(gram) for gram in STANDING_SEQUENCES]
        for gram in STANDING_SEQUENCES:
            self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        overlap = [["027", "048", "090", "076", "027", "048", "090", "076"]]
        self.assertEqual(ngram_hit_count(overlap, STANDING_SEQUENCES[0]), 2)
        gapped = [
            list(STANDING_SEQUENCES[0][:2])
            + ["006"]
            + list(STANDING_SEQUENCES[0][2:])
        ]
        self.assertEqual(ngram_hit_count(gapped, STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([[]], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE282_GRAM3)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(GRAM2)], STANDING_SEQUENCES[0]), 0)
        self.assertEqual(ngram_hit_count([list(CYCLE219_LEAK_4GRAM)], STANDING_SEQUENCES[0]), 0)
        planted = ["027", "048", "090", "076"]
        self.assertEqual(site_previous_4gram(planted, 2, GRAM2), STANDING_SEQUENCES[0])
        self.assertEqual(site_backward_3gram(planted, 2, GRAM2), ("048", "090", "076"))
        line_initial_after_w = ["048", "090", "076"]
        self.assertEqual(site_previous_stem(line_initial_after_w, 1, GRAM2), "048")
        self.assertEqual(
            site_backward_3gram(line_initial_after_w, 1, GRAM2),
            ("048", "090", "076"),
        )
        self.assertIsNone(site_previous_4gram(line_initial_after_w, 1, GRAM2))
        no_prev = ["090", "076", "012"]
        self.assertIsNone(site_previous_stem(no_prev, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(no_prev, 0, GRAM2))
        self.assertTrue(STANDING_009_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_009_009_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_i_only_requires_on_i_and_zero_off_i_for_each_4gram(self):
        """Boolean is True only when all continuing remaining-after-009 4-grams are I-only."""
        provider = MockProvider()
        hold_ones = STANDING_N_I_EACH
        hold_zeros = STANDING_N_OFF_I_EACH
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
                hold_ones,
                hold_zeros,
            )
        )
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
                (2,) + hold_ones[1:],
                hold_zeros,
            )
        )
        lose_off = list(hold_zeros)
        lose_off[0] = 1
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
                hold_ones,
                tuple(lose_off),
            )
        )
        lose_off_mid = list(hold_zeros)
        lose_off_mid[24] = 1
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
                hold_ones,
                tuple(lose_off_mid),
            )
        )
        lose_missing_i = list(hold_ones)
        lose_missing_i[0] = 0
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
                tuple(lose_missing_i),
                hold_zeros,
            )
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
                (),
                (),
            )
        )
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
                hold_ones[:-1],
                hold_zeros[:-1],
            )
        )
        self.assertEqual(STANDING_CLAIM, STANDING_CLAIM)
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_ALL_I_ONLY
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_ALL_I_ONLY,
            HYPOTHESIS_ALL_I_ONLY,
        )
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertFalse(CYCLE219_CLAIM)
        self.assertEqual(CYCLE219_N_I_ONLY, 7)
        self.assertEqual(CYCLE219_N_NOT_I_ONLY, 1)
        self.assertEqual(CYCLE219_LEAK_4GRAM, ("090", "076", "070", "000"))
        self.assertTrue(CYCLE257_CLAIM)
        self.assertEqual(CYCLE257_N_I_ONLY, 19)
        self.assertEqual(CYCLE257_N_NOT_I_ONLY, 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_4grams_are_cycle_284_remaining_after_009_previous_not_retuned(self):
        """4-grams stay the cycle-284 remaining-after-009 previouss; 009 / 009 009 are not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(STANDING_REMAINING_SITES, CYCLE284_REMAINING_SITES)
        self.assertEqual(STANDING_REMAINING_PREVIOUS_STEMS, CYCLE284_REMAINING_PREVIOUS_STEMS)
        self.assertEqual(len(STANDING_SEQUENCES), CYCLE284_N_REMAINING)
        self.assertEqual(CYCLE284_N_REMAINING, 27)
        self.assertEqual(CYCLE284_N_DISTINCT, 27)
        self.assertEqual(CYCLE284_G, "724")
        self.assertEqual(CYCLE284_K, 1)
        self.assertFalse(CYCLE284_UNIQUE)
        self.assertFalse(CYCLE284_CLAIM)
        self.assertEqual(len(set(STANDING_PREVIOUS_STEMS)), 27)
        self.assertEqual(len(set(STANDING_SEQUENCES)), 27)
        self.assertNotEqual(STANDING_SEQUENCES[0], GRAM5)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        for gram, prev in zip(STANDING_SEQUENCES, STANDING_PREVIOUS_STEMS, strict=True):
            self.assertTrue(is_contiguous_substring(GRAM2, gram))
            self.assertFalse(is_contiguous_substring(gram, GRAM5))
            self.assertEqual(gram[1], prev)
            self.assertNotIn(prev, LOCKED_PREVIOUS_STEMS_AFTER_009)
            self.assertNotEqual(gram[1:], CYCLE282_GRAM3)
            self.assertNotIn(gram, CYCLE283_SEQUENCES)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotEqual(gram[2:], CYCLE171_GRAM2)
        for site, start in zip(
            STANDING_CONTINUING_SITES,
            (sites[0] for sites in STANDING_I_SITES),
            strict=True,
        ):
            self.assertEqual(leftover_previous_4gram_start_site(site), start)
            self.assertEqual(start[2], site[2] - 2)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertEqual(STANDING_N_NO_PREVIOUS, 0)
        self.assertEqual(STANDING_SEQUENCES[24], CYCLE284_MATCHING_PREVIOUS_4GRAMS[0])
        self.assertEqual(STANDING_CONTINUING_SITES[24], CYCLE284_MATCHING_SITES[0])
        for site in CYCLE281_009_SITES:
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        self.assertTrue(STANDING_CYCLE281_009_EXCLUDED)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE257)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_LOCK_REMAINING_AFTER_009_3GRAMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertFalse(STANDING_SAME_AS_CYCLE284)
        self.assertFalse(STANDING_SAME_AS_CYCLE283)
        self.assertFalse(STANDING_SAME_AS_CYCLE257)
        self.assertEqual(len(STANDING_SEQUENCES[0]), STANDING_N4)
        self.assertLess(STANDING_N4, 8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter009Prev4IOnlyScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-009 previous-4 off-I lock. Mock only."""

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
        self.with_previous = leftover_extra_remaining_after_009_with_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.no_previous = leftover_extra_remaining_after_009_without_previous(
            self.leftover_sites,
            self.previous_stems,
        )
        self.per_site_previous_4grams = leftover_extra_remaining_after_009_previous_4grams(
            self.leftover_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.line_initial = leftover_extra_remaining_after_009_line_initial_sites(
            self.leftover_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.continuing = leftover_extra_remaining_after_009_continuing_sites(
            self.leftover_sites,
            self.leftover_previous_4grams,
            self.previous_stems,
        )
        self.grams = continuing_previous_4grams(self.per_site_previous_4grams)
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
        self.g, self.k, self.unique = select_remaining_after_009_g(self.remaining_stems)
        self.unique_max = i_leftover_extra_090_076_remaining_after_009_unique_previous_stem(
            self.leftover_sites,
            self.previous_stems,
        )
        self.remaining_after_045_and_009 = (
            leftover_extra_remaining_after_090_and_076_and_071_and_045_without_previous_009(
                self.leftover_sites,
                self.previous_stems,
            )
        )
        self.claim_holds = (
            i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
                self.n_i,
                self.n_off_i,
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

    def test_tokens_and_sites_are_cycle_284_remaining_after_009_not_retuned(self):
        """4-grams stay the cycle-284 remaining-after-009 lock. Nested 27/K=1/G=724 stay."""
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
        self.assertEqual(len(set(self.remaining_stems)), STANDING_N_DISTINCT_REMAINING)
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
        self.assertEqual(self.per_site_previous_4grams, STANDING_REMAINING_PREVIOUS_4GRAMS)
        self.assertEqual(self.grams, STANDING_SEQUENCES)
        self.assertEqual(self.continuing, STANDING_CONTINUING_SITES)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(self.line_initial, ())
        self.assertEqual(self.no_previous, STANDING_NO_PREVIOUS_SITES)
        self.assertEqual(len(self.grams), STANDING_N_CONTINUING)
        self.assertEqual(STANDING_N_CONTINUING, 27)
        self.assertEqual(len(self.line_initial), STANDING_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertTrue(all(stem is not None for stem in self.remaining_stems))
        self.assertTrue(all(gram is not None for gram in self.per_site_previous_4grams))
        self.assertEqual(self.remaining, self.remaining_after_045_and_009)
        self.assertEqual(len(self.remaining_after_045_and_009), 27)
        for site in CYCLE281_009_SITES:
            self.assertNotIn(site, self.remaining)
            self.assertIn(site, CYCLE281_MATCHING_SITES)
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
        prior_284 = self.survey["i_leftover_extra_090_076_remaining_after_009_previous_stem"]
        self.assertEqual(prior_284["cycle"], 284)
        self.assertEqual(prior_284["N_remaining_after_009"], 27)
        self.assertEqual(prior_284["K"], 1)
        self.assertEqual(prior_284["G"], "724")
        self.assertFalse(prior_284["G_uniquely_most_frequent"])
        self.assertFalse(prior_284["i_leftover_extra_090_076_remaining_after_009_unique_previous_stem"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_284["remaining_after_009_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(prior_284["remaining_after_009_previous_stems"]),
            STANDING_REMAINING_PREVIOUS_STEMS,
        )
        prior_283 = self.survey["i_009_090_076_previous_4grams_i_only"]
        self.assertEqual(prior_283["cycle"], 283)
        self.assertEqual(prior_283["N_i_only"], 2)
        self.assertEqual(prior_283["N_not_i_only"], 0)
        self.assertEqual(prior_283["N_not_hapax"], 0)
        self.assertTrue(prior_283["i_009_090_076_previous_4grams_all_i_only_hapax"])
        self.assertTrue(CYCLE283_ALL_HAPAX)
        prior_282 = self.survey["i_3gram_009_090_076_i_only"]
        self.assertEqual(prior_282["cycle"], 282)
        self.assertEqual(prior_282["N_I"], 2)
        self.assertEqual(prior_282["N_off_I"], 0)
        self.assertEqual(prior_282["N_extra"], 0)
        self.assertTrue(prior_282["i_3gram_009_090_076_i_only"])
        self.assertTrue(CYCLE282_CLAIM)
        prior_281 = self.survey[
            "i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_remaining_after_071_remaining_after_045_previous_009"
        ]
        self.assertEqual(prior_281["cycle"], 281)
        self.assertEqual(prior_281["G"], "009")
        self.assertEqual(prior_281["K"], 2)
        self.assertEqual(prior_281["N_remaining_after_090_and_076_and_071_and_045_and_009"], 27)
        self.assertTrue(CYCLE281_CLAIM)
        prior_270 = self.survey["i_leftover_extra_090_076_remaining_after_600_previous_stem"]
        self.assertEqual(prior_270["cycle"], 270)
        self.assertEqual(prior_270["G"], "090")
        self.assertEqual(prior_270["K"], 2)
        self.assertEqual(prior_270["N_tied_at_K"], 5)
        self.assertFalse(prior_270["G_uniquely_most_frequent"])
        self.assertFalse(CYCLE270_CLAIM)
        prior_257 = self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"]
        self.assertEqual(prior_257["cycle"], 257)
        self.assertTrue(prior_257["i_leftover_extra_090_076_remaining_after_000_forward_4grams_all_i_only"])
        self.assertEqual(prior_257["N_i_only"], 19)
        self.assertEqual(prior_257["N_not_i_only"], 0)
        self.assertTrue(CYCLE257_CLAIM)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(prior_167["N_off_I"], 0)
        self.assertTrue(prior_167["i_3gram_999_090_076_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_LOCK_REMAINING_AFTER_009_3GRAMS)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_each_4gram_is_one_on_i_zero_off_i_no_line_initial_and_claim_holds(self):
        """Each remaining-after-009 previous 4-gram is N_I=1, N_off_I=0. Claim holds."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_i, STANDING_N_I_EACH)
        self.assertEqual(STANDING_N_I_EACH, (1,) * STANDING_N_CONTINUING)
        self.assertEqual(self.n_off_i, STANDING_N_OFF_I_EACH)
        self.assertEqual(STANDING_N_OFF_I_EACH, (0,) * STANDING_N_CONTINUING)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.line_initial, ())
        self.assertEqual(self.leaking, STANDING_LEAKING_4GRAMS)
        self.assertEqual(self.leaking, ())
        self.assertEqual(self.n_i_only, STANDING_N_I_ONLY)
        self.assertEqual(self.n_i_only, 27)
        self.assertEqual(self.n_not_i_only, STANDING_N_NOT_I_ONLY)
        self.assertEqual(self.n_not_i_only, 0)
        if self.n_off_i != STANDING_N_OFF_I_EACH:
            self.fail("measured N_off_I drifted from 0")
        if self.n_i != STANDING_N_I_EACH:
            self.fail("measured N_I drifted from the locked remaining-after-009 hapax")
        if self.line_initial:
            self.fail("measured line-initial remaining-after-009 set drifted from empty")
        if self.leaking:
            self.fail("measured remaining-after-009 previous 4-grams leaked off I")
        for site, start, gram, prev, role, sites, n_on, n_off in zip(
            STANDING_CONTINUING_SITES,
            (row[0] for row in STANDING_I_SITES),
            STANDING_SEQUENCES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            strict=True,
        ):
            self.assertEqual(leftover_previous_4gram_start_site(site), start)
            self.assertEqual(sites, (start,))
            stems = line_stems_for_site(self.i_sides, start)
            self.assertEqual(tuple(stems[start[2] : start[2] + STANDING_N4]), gram)
            self.assertEqual(stems[start[2] + 1], prev)
            self.assertEqual(tuple(stems[start[2] + 2 : start[2] + 4]), GRAM2)
            self.assertEqual(site_previous_4gram(stems, site[2], GRAM2), gram)
            self.assertGreaterEqual(site[2], 2)
            self.assertNotEqual(gram, GRAM5)
            self.assertNotEqual(gram[1:], CYCLE282_GRAM3)
            self.assertNotIn(gram, CYCLE283_SEQUENCES)
            self.assertNotEqual(gram, CYCLE219_LEAK_4GRAM)
            self.assertNotIn(prev, LOCKED_PREVIOUS_STEMS_AFTER_009)
            self.assertEqual(role, "leftover_extra_remaining_after_009")
            self.assertEqual(n_on, 1)
            self.assertEqual(n_off, 0)
            self.assertTrue(sequence_is_i_only(n_on, n_off))
        for n_off in self.n_off_i:
            if n_off != 0:
                self.fail("measured N_off_I drifted from 0")
        for n_on, locked in zip(self.n_i, STANDING_N_I_EACH, strict=True):
            if n_on != locked:
                self.fail("measured N_I drifted from the locked count")
        if not self.claim_holds:
            self.fail("measured remaining-after-009 previous 4-grams are not all I-only")
        self.assertTrue(STANDING_NOT_ASSUMED_HAPAX)
        self.assertTrue(STANDING_HAPAX_EACH)
        self.assertTrue(STANDING_ALL_REMAINING_HAVE_PREVIOUS_TOKEN)
        self.assertTrue(STANDING_ALL_REMAINING_HAVE_FOURTH_TOKEN)
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        for hits, off in zip(self.hits_by_tablet, self.off_i, strict=True):
            self.assertEqual(hits, STANDING_HITS_BY_TABLET_ONE_ON_I)
            self.assertEqual(off, STANDING_OFF_I_BY_TABLET)
        for tablet, *counts in zip(
            VENDORED_TABLETS,
            *self.hits_by_tablet,
            strict=True,
        ):
            for count, gram in zip(counts, self.grams, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], gram))
                self.assertEqual(count, 1 if tablet == "I" else 0)
        self.assertEqual(
            i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only(
                self.n_i,
                self.n_off_i,
            ),
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_ALL_I_ONLY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_ALL_I_ONLY,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_PREVIOUS_4GRAMS_ALL_I_ONLY
        )
        self.assertTrue(HYPOTHESIS_ALL_I_ONLY)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE257)
        self.assertFalse(STANDING_SAME_AS_CYCLE219)
        self.assertFalse(STANDING_SAME_AS_CYCLE284)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE257)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE219)
        self.assertTrue(STANDING_009_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_009_009_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_071_009_090_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_070_000_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_DO_NOT_LOCK_REMAINING_AFTER_009_3GRAMS)
        self.assertTrue(STANDING_CYCLE281_009_EXCLUDED)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        for site in CYCLE281_009_SITES:
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        for site in CYCLE223_OFF_I_SITES:
            self.assertNotIn(site, STANDING_REMAINING_SITES)
        for gram in CYCLE283_SEQUENCES:
            self.assertNotIn(gram, STANDING_SEQUENCES)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_284_283_282_281_270_257_223_and_167_still_compute(self):
        """Cycle 284 unique-max lose 27/K=1/G=724, 283 2/0 hapax, 282 2/0, 281 K=2/27, 270 5-way, 257 19/19, 223 69/3, 167 16/0 stay."""
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
        prior_283 = TestMamariI009090076Previous4gramsIOnlyScoreboard()
        prior_283.setUp()
        prior_283.test_all_4grams_are_i_only_hapax_and_claim_holds()
        prior_283.test_survey_matches_computed_lock()
        self.assertEqual(prior_283.n_i_only, 2)
        self.assertEqual(prior_283.n_not_i_only, 0)
        self.assertEqual(prior_283.n_not_hapax, 0)
        self.assertTrue(prior_283.claim_holds)
        self.assertTrue(CYCLE283_ALL_HAPAX)
        if prior_283.n_i_only != 2 or prior_283.n_not_i_only != 0 or prior_283.n_not_hapax != 0:
            self.fail("nested cycle 283 2/0 hapax drifted")
        prior_282 = TestMamariI3gram009090076IOnlyScoreboard()
        prior_282.setUp()
        prior_282.test_i_hits_are_two_on_ia_and_leftover_extra_009_is_subset()
        prior_282.test_3gram_is_zero_off_i_and_i_only()
        prior_282.test_survey_matches_computed_lock()
        self.assertEqual(prior_282.i_hits, CYCLE282_N_I)
        self.assertEqual(prior_282.i_hits, 2)
        self.assertEqual(prior_282.off_i_hits, CYCLE282_N_OFF_I)
        self.assertEqual(prior_282.off_i_hits, 0)
        self.assertEqual(len(prior_282.extra), CYCLE282_N_EXTRA)
        self.assertEqual(len(prior_282.extra), 0)
        self.assertTrue(prior_282.claim_holds)
        self.assertTrue(CYCLE282_CLAIM)
        if prior_282.i_hits != 2 or prior_282.off_i_hits != 0 or prior_282.extra:
            self.fail("nested cycle 282 009 090 076 I-only 2/0 extra I=0 drifted")
        prior_281 = TestMamariILeftoverExtra090076RemainingAfter045Prev009Scoreboard()
        prior_281.setUp()
        prior_281.test_counts_2_of_31_and_hypothesis_k_2_holds()
        prior_281.test_survey_matches_computed_lock()
        self.assertEqual(prior_281.k_009, 2)
        self.assertEqual(prior_281.n_without, 27)
        self.assertEqual(prior_281.matching, CYCLE281_MATCHING_SITES)
        self.assertTrue(prior_281.claim_holds)
        self.assertTrue(CYCLE281_CLAIM)
        if prior_281.k_009 != 2 or prior_281.n_without != 27:
            self.fail("nested cycle 281 leftover extra remaining-after-045 G=009 K=2 drifted")
        prior_270 = TestMamariILeftoverExtra090076RemainingAfter600PreviousStemScoreboard()
        prior_270.setUp()
        prior_270.test_counts_37_remaining_g_090_k_2_five_way_tie_and_hypothesis_loses()
        prior_270.test_survey_matches_computed_lock()
        self.assertEqual(prior_270.g, "090")
        self.assertEqual(prior_270.k, 2)
        self.assertEqual(prior_270.n_remaining, 37)
        self.assertFalse(prior_270.unique)
        self.assertFalse(prior_270.claim_holds)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertEqual(CYCLE270_N_TIED_AT_K, 5)
        self.assertEqual(CYCLE270_TIED_STEMS[0], "090")
        if prior_270.n_remaining != 37 or prior_270.k != 2 or prior_270.unique:
            self.fail("nested cycle 270 leftover extra remaining-after-600 5-way tie at 2 drifted")
        prior_257 = TestMamariILeftoverExtra090076RemainingAfter000Fwd4IOnlyScoreboard()
        prior_257.setUp()
        prior_257.test_each_4gram_is_one_on_i_zero_off_i_no_line_final_and_claim_holds()
        prior_257.test_survey_matches_computed_lock()
        self.assertEqual(prior_257.n_i_only, 19)
        self.assertEqual(prior_257.n_not_i_only, 0)
        self.assertTrue(prior_257.claim_holds)
        self.assertTrue(CYCLE257_CLAIM)
        self.assertEqual(CYCLE257_N_I_ONLY, 19)
        self.assertEqual(len(CYCLE257_NEXT_4GRAMS), 19)
        if prior_257.n_i_only != 19 or prior_257.n_not_i_only != 0:
            self.fail("nested cycle 257 leftover extra remaining-after-000 forward 4-grams 19/19 hapax drifted")
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
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        self.assertEqual(prior_167.i_hits, CYCLE167_N_I)
        self.assertEqual(prior_167.i_hits, 16)
        self.assertEqual(prior_167.off_i_hits, CYCLE167_N_OFF_I)
        self.assertEqual(prior_167.off_i_hits, 0)
        self.assertEqual(prior_167.i_sites, CYCLE167_I_SITES)
        self.assertTrue(prior_167.claim_holds)
        self.assertTrue(CYCLE167_CLAIM)
        if prior_167.i_hits != 16 or prior_167.off_i_hits != 0:
            self.fail("nested cycle 167 999 090 076 I-only 16/0 drifted")
        prior_219 = TestMamariI090076070Forward4gramsIOnlyScoreboard()
        prior_219.setUp()
        prior_219.test_each_4gram_lock_and_claim_loses_on_000()
        prior_219.test_survey_matches_computed_lock()
        self.assertEqual(prior_219.n_i_only, 7)
        self.assertEqual(prior_219.n_not_i_only, 1)
        self.assertFalse(prior_219.claim_holds)
        self.assertFalse(CYCLE219_CLAIM)
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
        self.assertTrue(STANDING_DO_NOT_LOCK_REMAINING_AFTER_009_3GRAMS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-285 remaining-after-009 previous-4 I-only lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_009_prev4_i_only"]
        self.assertEqual(lock["cycle"], 285)
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
        self.assertEqual(lock["N_distinct_remaining"], 27)
        self.assertEqual(lock["N_continuing"], STANDING_N_CONTINUING)
        self.assertEqual(lock["N_continuing"], 27)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
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
        self.assertEqual(
            [list(gram) for gram in STANDING_SEQUENCES],
            lock["remaining_after_009_previous_4grams"],
        )
        self.assertEqual(lock["line_initial_remaining_after_009_sites"], [])
        self.assertEqual(
            tuple(tuple(row) for row in lock["continuing_sites"]),
            STANDING_CONTINUING_SITES,
        )
        self.assertTrue(lock["all_remaining_have_previous_token"])
        self.assertTrue(lock["all_remaining_have_fourth_token"])
        self.assertTrue(lock["cycle281_009_excluded"])
        self.assertTrue(lock["not_assumed_hapax"])
        rows = lock["sequences"]
        self.assertEqual(len(rows), STANDING_N_CONTINUING)
        for row, gram, site, prev, role, sites, n_on, n_off in zip(
            rows,
            STANDING_SEQUENCES,
            STANDING_CONTINUING_SITES,
            STANDING_PREVIOUS_STEMS,
            STANDING_ROLES,
            STANDING_I_SITES,
            STANDING_N_I_EACH,
            STANDING_N_OFF_I_EACH,
            strict=True,
        ):
            self.assertEqual(tuple(row["tokens4"]), gram)
            self.assertEqual(tuple(row["cycle284_site"]), site)
            self.assertEqual(row["previous_stem"], prev)
            self.assertEqual(row["role"], role)
            self.assertEqual(row["N_I"], n_on)
            self.assertEqual(row["N_on_I"], n_on)
            self.assertEqual(row["N_I"], 1)
            self.assertEqual(row["ia_hits"], 1)
            self.assertEqual(row["ib_hits"], STANDING_IB_HITS)
            self.assertEqual(tuple(tuple(site_row) for site_row in row["i_sites"]), sites)
            self.assertEqual(
                tuple(tuple(site_row) for site_row in row["ib_sites"]),
                STANDING_IB_SITES,
            )
            self.assertEqual(row["N_off_I"], n_off)
            self.assertEqual(row["N_off_I"], 0)
            self.assertEqual(row["off_i_sites"], [])
            self.assertEqual(tuple(row["off_i_tablets"]), OFF_I_TABLETS)
            self.assertEqual(tuple(row["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
            self.assertEqual(row["off_i_tablets_with_hits"], [])
            self.assertEqual(row["off_i_by_tablet_nonzero"], {})
            self.assertEqual(tuple(row["vendored_tablets"]), VENDORED_TABLETS)
            self.assertEqual(
                tuple(row["hits_by_tablet"]),
                STANDING_HITS_BY_TABLET_ONE_ON_I,
            )
            self.assertTrue(row["i_only"])
            self.assertTrue(row["hapax"])
        self.assertEqual(tuple(lock["N_I_each"]), STANDING_N_I_EACH)
        self.assertEqual(tuple(lock["N_off_I_each"]), STANDING_N_OFF_I_EACH)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_009_previous_4grams_all_i_only"]
        )
        self.assertTrue(
            lock["i_leftover_extra_090_076_remaining_after_009_previous_4grams_i_only"]
        )
        self.assertEqual(lock["N_i_only"], 27)
        self.assertEqual(lock["N_not_i_only"], 0)
        self.assertEqual(lock["leaking_4grams"], [])
        self.assertEqual(lock["nested_cycle284_N_remaining_after_009"], 27)
        self.assertEqual(lock["nested_cycle284_K"], 1)
        self.assertEqual(lock["nested_cycle284_G"], "724")
        self.assertFalse(lock["nested_cycle284_G_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle283_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle283_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle283_N_not_hapax"], 0)
        self.assertEqual(lock["nested_cycle282_N_I"], 2)
        self.assertEqual(lock["nested_cycle282_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle282_N_extra"], 0)
        self.assertEqual(lock["nested_cycle281_G"], "009")
        self.assertEqual(lock["nested_cycle281_K"], 2)
        self.assertEqual(lock["nested_cycle281_N_remaining"], 27)
        self.assertEqual(lock["nested_cycle270_G"], "090")
        self.assertEqual(lock["nested_cycle270_K"], 2)
        self.assertEqual(lock["nested_cycle270_N_tied_at_K"], 5)
        self.assertFalse(lock["nested_cycle270_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle257_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle257_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertEqual(lock["nested_cycle219_N_i_only"], 7)
        self.assertEqual(lock["nested_cycle219_N_not_i_only"], 1)
        self.assertEqual(tuple(lock["nested_cycle219_leak_4gram"]), CYCLE219_LEAK_4GRAM)
        self.assertEqual(lock["nested_cycle167_N_I"], 16)
        self.assertEqual(lock["nested_cycle167_N_off_I"], 0)
        self.assertEqual(lock["nested_cycle171_N_I"], 43)
        self.assertEqual(lock["nested_cycle171_N_off_I"], 0)
        self.assertTrue(lock["known_distinct"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle167"])
        self.assertFalse(lock["same_as_cycle219"])
        self.assertFalse(lock["same_as_cycle223"])
        self.assertFalse(lock["same_as_cycle257"])
        self.assertFalse(lock["same_as_cycle270"])
        self.assertFalse(lock["same_as_cycle281"])
        self.assertFalse(lock["same_as_cycle282"])
        self.assertFalse(lock["same_as_cycle283"])
        self.assertFalse(lock["same_as_cycle284"])
        self.assertTrue(lock["same_claim_shape_as_cycle219"])
        self.assertTrue(lock["same_claim_shape_as_cycle257"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["do_not_lock_remaining_after_009_3grams"])
        self.assertTrue(lock["009_090_076_does_not_count"])
        self.assertTrue(lock["009_009_090_076_does_not_count"])
        self.assertTrue(lock["071_009_090_076_does_not_count"])
        self.assertTrue(lock["999_090_076_does_not_count"])
        self.assertTrue(lock["600_090_076_does_not_count"])
        self.assertTrue(lock["090_090_076_does_not_count"])
        self.assertTrue(lock["076_090_076_does_not_count"])
        self.assertTrue(lock["071_090_076_does_not_count"])
        self.assertTrue(lock["045_090_076_does_not_count"])
        self.assertTrue(lock["090_076_070_000_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["forward_peel_not_retuned"])
        self.assertTrue(lock["off_i_t_sites_are_this_cycle_only_if_matching_4gram"])
        self.assertTrue(lock["raw_stems_090_kept"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_009_previous_stem_unchanged"]
        )
        self.assertTrue(lock["standing_i_009_090_076_previous_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_009_090_076_i_only_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_remaining_after_090_remaining_after_076_remaining_after_071_remaining_after_045_previous_009_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_stem_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_fwd4_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_previous_stem"]["cycle"],
            284,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_previous_stem"][
                "N_remaining_after_009"
            ],
            27,
        )
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_remaining_after_009_previous_stem"][
                "i_leftover_extra_090_076_remaining_after_009_unique_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_009_090_076_previous_4grams_i_only"]["cycle"], 283)
        self.assertTrue(
            self.survey["i_009_090_076_previous_4grams_i_only"][
                "i_009_090_076_previous_4grams_all_i_only_hapax"
            ]
        )
        self.assertEqual(self.survey["i_3gram_009_090_076_i_only"]["cycle"], 282)
        self.assertTrue(self.survey["i_3gram_009_090_076_i_only"]["i_3gram_009_090_076_i_only"])
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_fwd4_i_only"]["cycle"],
            257,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter009Prev4IOnlyImageSnapshot(
    unittest.TestCase
):
    """Cycle 285 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
