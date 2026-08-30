"""I's leftover n=4 remaining I 090 076 previous-stem lock.

Cycle 302 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–259 forward; 260–287 previous),
leftover n=4 remaining forward peel (288–301), leftover extra
previous-stem (cycle 260), leftover extra remaining-after-000
extra-I 4-grams (cycle 259), leftover n=4 remaining
share-one-forward-stem (cycle 288), or remaining-after-011
extra-I 4-grams (cycle 301). Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); skip W.
Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new
agents. Not a meaning dictionary.

Leftover n=4 remaining forward is exhausted: cycle 288 LOSE
share-one-forward-stem (6 distinct, G=020 K=4); cycles 289–
297 peeled 020 / 087 / 057 / 011; cycle 298 LOSE remaining-
after-011 unique next stem (hapax pile G=607 K=1); cycles
299–301 HOLD remaining-after-011 4-grams / 3-grams / extra-I
4-grams. Analog after leftover extra remaining-after-000
extra-I 4-grams HOLD (cycle 259): cycle 260 leftover extra
I 090 076 share-one-previous-stem LOST (34 distinct, G=999
K=15). Leftover n=4 remaining previous-stem has not been
locked. Do not re-lock leftover extra previous-stem
(cycles 260–287). This is leftover n=4 remaining previous-
stem, a different direction on a different population from
leftover extra.

For each leftover n=4 remaining I site, record the previous
token immediately before 090 076 when it exists (the Y in
Y 090 076; backward 3-gram Y 090 076, and previous 4-gram
X Y 090 076 when it exists). Sites with no previous token
(line-initial) are N_line_initial, a nested fact; do not
drop the site from N. Nested-assert N_I=69 / N_inside=13 /
N_leftover_extra=56 from cycles 223/224; do not retune those
cycles. Nested leftover n=4 remaining 13 / 4 / 9 / 3 / 6 /
2 / 4 / 2 / 2 still computes (do not retune 288–297).
076 071 and 076 070 do not count as this 2-gram. Leftover
extra sites do not count as leftover n=4 remaining.

Claim that can lose:
i_leftover_n4_remaining_090_076_unique_previous_stem. True
iff N_inside==13 and leftover n=4 remaining I 090 076 has a
unique most frequent previous stem G with K ≥ 2 (no tie at
max K; not a hapax pile). This can lose the same way cycle
260 lost share-one-previous-stem (34 distinct G=999 K=15)
and cycle 288 lost share-one-forward-stem (6 distinct G=020
K=4), or hold the same way cycle 266 held (G=600 K=4).
Unique-max is the claim (not share-one). G = the unique-max
previous stem if unique_max else the first max by larger
Barthel id. K = that count. Measured: N_inside=13,
N_with_previous=13, N_line_initial=0, N_distinct=8,
unique-max G=021 K=5 at Ia4[117]/Ia5[28]/Ia6[78]/Ia8[106]/
Ia13[17], N_remaining_after_G=8. The claim is true. Nested
overlap of G sites with leftover extra previous-999 (cycle
261) is empty; overlap with leftover extra remaining-after-
000 extra I (cycles 258/259) is Ia8[106] only; record, do
not fail unique-max on it. Nested cycle 224 13/56, cycle
223 69/3, cycle 288 share-one-forward lost G=020 K=4, and
cycle 301 extra-I 4-gram 090 076 607 073 1/0 stay. Do not
assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_021087_COVERED,
    STANDING_LEFTOVER_600011_COVERED,
    STANDING_LEFTOVER_999021_COVERED,
    STANDING_LEFTOVER_SITES,
    STANDING_N_I as CYCLE224_N_I,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_OFF_I,
    STANDING_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    group_sites_by_previous_stem,
    leftover_sites_with_backward,
    leftover_sites_without_backward,
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_999_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_15_SHARE_PREVIOUS_999 as CYCLE261_CLAIM,
    STANDING_K_999 as CYCLE261_K_999,
    STANDING_MATCHING_SITES as CYCLE261_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_999 as CYCLE261_N_REMAINING_AFTER_999,
    TestMamariILeftoverExtra090076Previous999Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_previous_stem_scoreboard import (
    STANDING_G as CYCLE260_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE260_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_PREVIOUS_STEM as CYCLE260_SHARE_ONE,
    STANDING_K as CYCLE260_K,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE260_N_DISTINCT,
    leftover_extra_backward_3grams,
    leftover_extra_previous_4grams,
    leftover_extra_previous_stems,
    leftover_sites_with_previous,
    leftover_sites_without_previous,
    rank_previous_stems,
    select_previous_g,
    TestMamariILeftoverExtra090076PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_3GRAMS_ALL_I_ONLY as CYCLE258_CLAIM,
    STANDING_N_EXTRA_TOTAL as CYCLE258_N_EXTRA,
    STANDING_N_I_ONLY as CYCLE258_N_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_BY_X as CYCLE259_EXTRA_I_BY_X,
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_N_I_ONLY as CYCLE259_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE259_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_999_previous_stem_scoreboard import (
    STANDING_G as CYCLE266_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE266_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_999_UNIQUE_PREVIOUS_STEM as CYCLE266_CLAIM,
    STANDING_K as CYCLE266_K,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE288_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE288_N_INSIDE,
    STANDING_N_NO_NEXT as CYCLE288_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE288_N_WITH_NEXT,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_011_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE301_CLAIM,
    STANDING_N_I_ONLY as CYCLE301_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE301_N_NOT_I_ONLY,
    STANDING_SEQUENCES as CYCLE301_SEQUENCES,
    TestMamariILeftoverN4Remaining090076RemainingAfter011ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_011_next_stem_scoreboard import (
    STANDING_K_011,
    STANDING_K_020,
    STANDING_K_057,
    STANDING_K_087,
    STANDING_N_REMAINING_AFTER_011,
    STANDING_N_REMAINING_AFTER_020,
    STANDING_N_REMAINING_AFTER_057,
    STANDING_N_REMAINING_AFTER_087,
    leftover_n4_remaining_remaining_after_011_nested_counts_hold,
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
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HYPOTHESIS_UNIQUE_MAX = True
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_PREVIOUS = 13
STANDING_N_LINE_INITIAL = 0
STANDING_N_NO_PREVIOUS = 0
STANDING_LINE_INITIAL_SITES = ()
STANDING_NO_PREVIOUS_SITES = ()
STANDING_N_DISTINCT_PREVIOUS_STEMS = 8
STANDING_N_HAPAX_PREVIOUS_STEMS = 6
STANDING_G = "021"
STANDING_K = 5
STANDING_N_REMAINING_AFTER_G = 8
STANDING_N_WITHOUT_G = 8
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_INSIDE_SITES_LOCK = STANDING_INSIDE_SITES
STANDING_PER_SITE_PREVIOUS_STEMS = (
    "600",
    "591",
    "076",
    "021",
    "021",
    "090",
    "021",
    "021",
    "000",
    "999",
    "008",
    "021",
    "600",
)
STANDING_PER_SITE_BACKWARD_3GRAMS = tuple(
    ((stem, "090", "076") if stem is not None else None)
    for stem in STANDING_PER_SITE_PREVIOUS_STEMS
)
STANDING_PER_SITE_PREVIOUS_4GRAMS = (
    ("071", "600", "090", "076"),
    ("570", "591", "090", "076"),
    ("090", "076", "090", "076"),
    ("600", "021", "090", "076"),
    ("007", "021", "090", "076"),
    ("079", "090", "090", "076"),
    ("150", "021", "090", "076"),
    ("999", "021", "090", "076"),
    ("607", "000", "090", "076"),
    ("244", "999", "090", "076"),
    ("700", "008", "090", "076"),
    ("999", "021", "090", "076"),
    ("175", "600", "090", "076"),
)
STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN = (
    "600",
    "591",
    "076",
    "021",
    "090",
    "000",
    "999",
    "008",
)
STANDING_G_SITES = (
    (SIDE_IA, "Ia4", 117),
    (SIDE_IA, "Ia5", 28),
    (SIDE_IA, "Ia6", 78),
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia13", 17),
)
STANDING_MATCHING_SITES = STANDING_G_SITES
STANDING_MATCHING_PREVIOUS_4GRAMS = (
    ("600", "021", "090", "076"),
    ("007", "021", "090", "076"),
    ("150", "021", "090", "076"),
    ("999", "021", "090", "076"),
    ("999", "021", "090", "076"),
)
STANDING_REMAINING_AFTER_G_SITES = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia2", 119),
    (SIDE_IA, "Ia4", 86),
    (SIDE_IA, "Ia5", 143),
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
    (SIDE_IA, "Ia12", 83),
    (SIDE_IA, "Ia14", 54),
)
STANDING_PREVIOUS_STEM_FREQUENCY = (
    (
        "021",
        5,
        STANDING_G_SITES,
        (("021", "090", "076"),) * 5,
    ),
    (
        "600",
        2,
        STANDING_LEFTOVER_600011_COVERED,
        (("600", "090", "076"),) * 2,
    ),
    ("999", 1, ((SIDE_IA, "Ia9", 28),), (("999", "090", "076"),)),
    ("591", 1, ((SIDE_IA, "Ia2", 119),), (("591", "090", "076"),)),
    ("090", 1, ((SIDE_IA, "Ia5", 143),), (("090", "090", "076"),)),
    ("076", 1, ((SIDE_IA, "Ia4", 86),), (("076", "090", "076"),)),
    ("008", 1, ((SIDE_IA, "Ia12", 83),), (("008", "090", "076"),)),
    ("000", 1, ((SIDE_IA, "Ia8", 114),), (("000", "090", "076"),)),
)
STANDING_OVERLAP_CYCLE261_PREVIOUS_999 = ()
STANDING_OVERLAP_CYCLE258_EXTRA_I = ((SIDE_IA, "Ia8", 106),)
STANDING_OVERLAP_CYCLE259_EXTRA_I = ((SIDE_IA, "Ia8", 106),)
STANDING_OVERLAP_DOES_NOT_LOSE = True
STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_999_IS_NOT_CYCLE261 = True
STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_999_SITE = ((SIDE_IA, "Ia9", 28),)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_remaining_090_076_unique_previous_stem"
STANDING_I_LEFTOVER_N4_REMAINING_090_076_UNIQUE_PREVIOUS_STEM = True
STANDING_RESULT = "i_leftover_n4_remaining_090_076_previous_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE260 = False
STANDING_SAME_AS_CYCLE261 = False
STANDING_SAME_AS_CYCLE266 = False
STANDING_SAME_AS_CYCLE288 = False
STANDING_SAME_AS_CYCLE301 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE260 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE266 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE288 = False
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_PREVIOUS_STEM_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_FORWARD_STEM_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_AFTER_011_EXTRA_I_FWD4_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_NESTED_LEFTOVER_N4_REMAINING = (13, 4, 9, 3, 6, 2, 4, 2, 2)


def leftover_n4_remaining_previous_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_INSIDE_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str | None, ...]:
    """Per-site previous stem or None for leftover n=4 remaining I 090 076."""
    return leftover_extra_previous_stems(i_sides, sites, gram2)


def leftover_n4_remaining_backward_3grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_INSIDE_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site backward 3-gram or None for leftover n=4 remaining I 090 076."""
    return leftover_extra_backward_3grams(i_sides, sites, gram2)


def leftover_n4_remaining_previous_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_INSIDE_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site previous 4-gram or None for leftover n=4 remaining I 090 076."""
    return leftover_extra_previous_4grams(i_sides, sites, gram2)


def leftover_n4_remaining_sites_with_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites that have a previous stem before 090 076."""
    return leftover_sites_with_previous(sites, previous_stems)


def leftover_n4_remaining_sites_without_previous(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites that are line-initial (no previous token)."""
    return leftover_sites_without_previous(sites, previous_stems)


def leftover_n4_remaining_with_previous_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites whose previous token is G."""
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev == stem
    )


def leftover_n4_remaining_without_previous_g(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites whose previous token is not G (includes line-initial)."""
    return tuple(
        site
        for site, prev in zip(sites, previous_stems, strict=True)
        if prev != stem
    )


def leftover_n4_remaining_previous_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    previous_stems: tuple[str | None, ...],
    backward_3grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Previous-stem frequency: highest count first, then larger Barthel id."""
    first_seen = group_sites_by_previous_stem(sites, previous_stems)
    grams_by_stem: dict[str, list[tuple[str, ...]]] = {
        stem: [] for stem, _ in first_seen
    }
    for prev, gram in zip(previous_stems, backward_3grams, strict=True):
        if prev is not None and gram is not None:
            grams_by_stem[prev].append(gram)
    rows = tuple(
        (stem, len(stem_sites), stem_sites, tuple(grams_by_stem[stem]))
        for stem, stem_sites in first_seen
    )
    return tuple(sorted(rows, key=lambda row: (-row[1], -barthel_id(row[0]))))


def leftover_n4_remaining_previous_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_PREVIOUS_STEM_FREQUENCY,
) -> list[dict]:
    """Survey-shaped leftover n=4 remaining previous-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "previous_stem": stem,
                "count": count,
                "leftover_n4_remaining_sites": [list(site) for site in sites],
                "backward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def leftover_n4_remaining_g_overlap_sites(
    g_sites: tuple[tuple[str, str, int], ...],
    other: tuple[tuple[str, str, int], ...],
) -> tuple[tuple[str, str, int], ...]:
    """Site-level overlap of leftover n=4 remaining previous-stem G sites with another set."""
    other_set = set(other)
    return tuple(site for site in g_sites if site in other_set)


def g_uniquely_most_frequent_previous(
    frequency: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ],
    min_k: int = 2,
) -> bool:
    """True iff unique-max G with K >= 2 and no tie at max K."""
    if not frequency:
        return False
    k = frequency[0][1]
    if k < min_k:
        return False
    if len(frequency) > 1 and frequency[1][1] == k:
        return False
    return True


def i_leftover_n4_remaining_090_076_unique_previous_stem(
    n_inside: int,
    previous_stems: tuple[str | None, ...],
    expected_n: int = STANDING_N_INSIDE,
) -> bool:
    """True iff N_inside==13 and a unique most frequent previous stem has K ≥ 2."""
    if n_inside != expected_n:
        return False
    gram, count, unique = select_previous_g(previous_stems)
    return bool(unique and gram is not None and count >= 2)


class TestILeftoverN4Remaining090076PreviousStemHelpers(unittest.TestCase):
    """Helpers on leftover n=4 remaining I 090 076 previous stems. No CV, no LLM."""

    def test_previous_requires_stem_before_2gram(self):
        """A previous stem is a 3-gram; line-initial is no-previous. Keep the site in N."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N3, STANDING_N2 + 1)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_021 = ["600", "021", "090", "076", "087"]
        self.assertEqual(site_previous_stem(has_021, 2, GRAM2), "021")
        self.assertEqual(
            site_backward_3gram(has_021, 2, GRAM2),
            ("021", "090", "076"),
        )
        self.assertEqual(
            site_previous_4gram(has_021, 2, GRAM2),
            ("600", "021", "090", "076"),
        )
        line_initial = ["090", "076", "011"]
        self.assertIsNone(site_previous_stem(line_initial, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(line_initial, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(line_initial, 0, GRAM2))
        one_token_before = ["021", "090", "076"]
        self.assertEqual(site_previous_stem(one_token_before, 1, GRAM2), "021")
        self.assertEqual(
            site_backward_3gram(one_token_before, 1, GRAM2),
            ("021", "090", "076"),
        )
        self.assertIsNone(site_previous_4gram(one_token_before, 1, GRAM2))
        family_999_021 = ["999", "021", "090", "076", "607", "755"]
        self.assertEqual(site_previous_stem(family_999_021, 2, GRAM2), "021")
        mismatch_071 = ["999", "076", "071", "090"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(callable(leftover_sites_without_backward))
        self.assertTrue(callable(leftover_sites_with_backward))
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_requires_k_at_least_two_and_no_tie_and_n_13(self):
        """Boolean is True only when N=13 and some G has unique K≥2."""
        provider = MockProvider()
        stems = leftover_n4_remaining_previous_stems(load_i_sides(), STANDING_INSIDE_SITES, GRAM2)
        self.assertTrue(
            i_leftover_n4_remaining_090_076_unique_previous_stem(13, stems)
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_unique_previous_stem(12, stems)
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_unique_previous_stem(14, stems)
        )
        g, k, unique = select_previous_g(stems)
        self.assertEqual(g, "021")
        self.assertEqual(k, 5)
        self.assertTrue(unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        hapax = ("021", "600", "591", "076", "090", "000", "999", "008")
        hap_g, hap_k, hap_unique = select_previous_g(hapax)
        self.assertEqual(hap_k, 1)
        self.assertFalse(hap_unique)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_unique_previous_stem(13, hapax + (None,) * 5)
        )
        tied = ("021", "021", "600", "600") + (None,) * 9
        tied_g, tied_k, tied_unique = select_previous_g(tied)
        self.assertEqual(tied_g, "600")
        self.assertEqual(tied_k, 2)
        self.assertFalse(tied_unique)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_unique_previous_stem(13, tied)
        )
        self.assertTrue(
            i_leftover_n4_remaining_090_076_unique_previous_stem(
                13,
                ("021", "021") + ("600",) + (None,) * 10,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_unique_previous_stem",
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_090_076_UNIQUE_PREVIOUS_STEM)
        self.assertEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_UNIQUE_PREVIOUS_STEM,
            HYPOTHESIS_UNIQUE_MAX,
        )
        self.assertEqual(STANDING_N_DISTINCT_PREVIOUS_STEMS, 8)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 13)
        self.assertEqual(STANDING_G, "021")
        self.assertEqual(STANDING_K, 5)
        self.assertEqual(STANDING_N_REMAINING_AFTER_G, 8)
        self.assertEqual(STANDING_K + STANDING_N_REMAINING_AFTER_G, STANDING_N_INSIDE)
        self.assertEqual(5 + 8, 13)
        self.assertEqual(provider.get_call_history(), [])

    def test_frequency_table_sorts_highest_count_first_and_skips_none(self):
        """Frequency table is count-desc then larger id; line-initial omitted from stems."""
        provider = MockProvider()
        sites = STANDING_INSIDE_SITES[:6]
        prev = ("021", "600", "021", None, "591", "021")
        grams = (
            ("021", "090", "076"),
            ("600", "090", "076"),
            ("021", "090", "076"),
            None,
            ("591", "090", "076"),
            ("021", "090", "076"),
        )
        table = leftover_n4_remaining_previous_stem_frequency_table(sites, prev, grams)
        self.assertEqual(table[0][0], "021")
        self.assertEqual(table[0][1], 3)
        self.assertEqual(table[1][0], "600")
        self.assertEqual(table[1][1], 1)
        self.assertEqual(len(table), 3)
        self.assertTrue(g_uniquely_most_frequent_previous(table))
        self.assertEqual(
            leftover_n4_remaining_sites_without_previous(sites, prev),
            (sites[3],),
        )
        self.assertEqual(
            leftover_n4_remaining_sites_with_previous(sites, prev),
            (sites[0], sites[1], sites[2], sites[4], sites[5]),
        )
        self.assertEqual(
            leftover_n4_remaining_with_previous_g(sites, prev),
            (sites[0], sites[2], sites[5]),
        )
        self.assertEqual(
            leftover_n4_remaining_without_previous_g(sites, prev),
            (sites[1], sites[3], sites[4]),
        )
        tied = leftover_n4_remaining_previous_stem_frequency_table(
            sites[:4],
            ("021", "600", "021", "600"),
            (
                ("021", "090", "076"),
                ("600", "090", "076"),
                ("021", "090", "076"),
                ("600", "090", "076"),
            ),
        )
        self.assertEqual(tied[0][0], "600")
        self.assertEqual(tied[0][1], 2)
        self.assertEqual(tied[1][0], "021")
        self.assertEqual(tied[1][1], 2)
        self.assertFalse(g_uniquely_most_frequent_previous(tied))
        hapax_table = leftover_n4_remaining_previous_stem_frequency_table(
            sites[:4],
            ("021", "600", "591", "076"),
            (
                ("021", "090", "076"),
                ("600", "090", "076"),
                ("591", "090", "076"),
                ("076", "090", "076"),
            ),
        )
        self.assertEqual(hapax_table[0][1], 1)
        self.assertFalse(g_uniquely_most_frequent_previous(hapax_table))
        self.assertFalse(g_uniquely_most_frequent_previous(()))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076PreviousStemScoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 remaining 090 076 previous-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.inside_sites = STANDING_INSIDE_SITES
        self.previous_stems = leftover_n4_remaining_previous_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.backwards = leftover_n4_remaining_backward_3grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.previous_4grams = leftover_n4_remaining_previous_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.with_previous = leftover_n4_remaining_sites_with_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.line_initial = leftover_n4_remaining_sites_without_previous(
            self.inside_sites,
            self.previous_stems,
        )
        self.first_seen = group_sites_by_previous_stem(
            self.inside_sites,
            self.previous_stems,
        )
        self.frequency = leftover_n4_remaining_previous_stem_frequency_table(
            self.inside_sites,
            self.previous_stems,
            self.backwards,
        )
        self.matching = leftover_n4_remaining_with_previous_g(
            self.inside_sites,
            self.previous_stems,
        )
        self.remaining = leftover_n4_remaining_without_previous_g(
            self.inside_sites,
            self.previous_stems,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover_extra = len(STANDING_LEFTOVER_SITES)
        self.n_with_previous = len(self.with_previous)
        self.n_line_initial = len(self.line_initial)
        self.n_distinct = len(self.first_seen)
        self.g, self.k, self.unique = select_previous_g(self.previous_stems)
        self.unique_max = g_uniquely_most_frequent_previous(self.frequency)
        self.n_remaining = len(self.remaining)
        self.overlap_261 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE261_MATCHING_SITES,
        )
        self.overlap_258 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_259 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE259_EXTRA_I_SITES,
        )
        self.overlap_259_607 = leftover_n4_remaining_g_overlap_sites(
            self.matching,
            CYCLE259_EXTRA_I_BY_X["607"],
        )
        self.claim_holds = i_leftover_n4_remaining_090_076_unique_previous_stem(
            self.n_inside,
            self.previous_stems,
        )

    def test_tokens_and_sites_are_cycle_224_inside_not_retuned(self):
        """2-gram and leftover n=4 remaining 13 stay the cycle-224/223/288 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_i, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(len(STANDING_INSIDE_SITES), STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE224_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE288_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_I"], 69)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(prior_224["i_090_076_all_inside_leftover_n4_remaining_family"])
        self.assertFalse(CYCLE224_ALL_INSIDE)
        self.assertEqual(
            tuple(tuple(row) for row in prior_224["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_224["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertFalse(prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(prior_288["N_distinct_next_stems"], 6)
        self.assertEqual(prior_288["N_distinct_next_stems"], CYCLE288_N_DISTINCT)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["G"], CYCLE288_G)
        self.assertEqual(prior_288["K"], 4)
        self.assertEqual(prior_288["K"], CYCLE288_K)
        self.assertTrue(prior_288["g_uniquely_most_frequent"])
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        if (
            prior_288["N_distinct_next_stems"] != 6
            or prior_288["G"] != "020"
            or prior_288["K"] != 4
            or prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"]
        ):
            self.fail("nested cycle 288 share-one-forward lost 6 distinct G=020 K=4 drifted")
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_301 = self.survey[
            "i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"
        ]
        self.assertEqual(prior_301["cycle"], 301)
        self.assertEqual(prior_301["N_i_only"], 1)
        self.assertEqual(prior_301["N_not_i_only"], 0)
        self.assertEqual(tuple(prior_301["extra_i_forward_4grams"][0]), CYCLE301_SEQUENCES[0])
        self.assertEqual(CYCLE301_SEQUENCES[0], ("090", "076", "607", "073"))
        self.assertTrue(
            leftover_n4_remaining_remaining_after_011_nested_counts_hold(
                13, 4, 9, 3, 6, 2, 4, 2, 2
            )
        )
        self.assertEqual(STANDING_NESTED_LEFTOVER_N4_REMAINING, (13, 4, 9, 3, 6, 2, 4, 2, 2))
        self.assertEqual(STANDING_K_020, 4)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(STANDING_K_087, 3)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(STANDING_K_057, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_057, 4)
        self.assertEqual(STANDING_K_011, 2)
        self.assertEqual(STANDING_N_REMAINING_AFTER_011, 2)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PREVIOUS_STEM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_FORWARD_STEM_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_8_distinct_previous_stems_g_021_k_5_and_claim_holds(self):
        """N_inside=13, N_line_initial=0, N_distinct=8, unique-max G=021 K=5. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        if self.n_inside != 13:
            self.fail("leftover n=4 remaining I 090 076 N drifted from 13")
        self.assertEqual(self.n_with_previous, STANDING_N_WITH_PREVIOUS)
        self.assertEqual(STANDING_N_WITH_PREVIOUS, 13)
        self.assertEqual(self.n_line_initial, STANDING_N_LINE_INITIAL)
        self.assertEqual(STANDING_N_LINE_INITIAL, 0)
        self.assertEqual(self.n_line_initial, STANDING_N_NO_PREVIOUS)
        self.assertEqual(self.line_initial, STANDING_LINE_INITIAL_SITES)
        self.assertEqual(STANDING_LINE_INITIAL_SITES, ())
        self.assertEqual(self.n_with_previous + self.n_line_initial, self.n_inside)
        self.assertEqual(13 + 0, 13)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_PREVIOUS_STEMS)
        self.assertEqual(STANDING_N_DISTINCT_PREVIOUS_STEMS, 8)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "021")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 5)
        self.assertTrue(self.unique)
        self.assertTrue(self.unique_max)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.unique_max, g_uniquely_most_frequent_previous(self.frequency))
        self.assertGreater(STANDING_K, STANDING_PREVIOUS_STEM_FREQUENCY[1][1])
        leftover_ranked = rank_previous_stems(
            Counter(stem for stem in self.previous_stems if stem is not None)
        )
        self.assertEqual(leftover_ranked[0], ("021", 5))
        self.assertEqual(leftover_ranked[1], ("600", 2))
        self.assertTrue(
            i_leftover_n4_remaining_090_076_unique_previous_stem(
                self.n_inside,
                self.previous_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_UNIQUE_PREVIOUS_STEM,
        )
        self.assertTrue(STANDING_I_LEFTOVER_N4_REMAINING_090_076_UNIQUE_PREVIOUS_STEM)
        self.assertTrue(HYPOTHESIS_UNIQUE_MAX)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_unique_previous_stem",
        )
        self.assertEqual(self.previous_stems, STANDING_PER_SITE_PREVIOUS_STEMS)
        self.assertEqual(self.backwards, STANDING_PER_SITE_BACKWARD_3GRAMS)
        self.assertEqual(self.previous_4grams, STANDING_PER_SITE_PREVIOUS_4GRAMS)
        self.assertEqual(
            tuple(stem for stem, _sites in self.first_seen),
            STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN,
        )
        self.assertEqual(self.matching, STANDING_G_SITES)
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(len(STANDING_G_SITES), 5)
        self.assertEqual(self.remaining, STANDING_REMAINING_AFTER_G_SITES)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_G)
        self.assertEqual(STANDING_N_REMAINING_AFTER_G, 8)
        self.assertEqual(self.k + self.n_remaining, self.n_inside)
        self.assertEqual(5 + 8, 13)
        self.assertEqual(len(STANDING_PREVIOUS_STEM_FREQUENCY), 8)
        self.assertEqual(STANDING_N_HAPAX_PREVIOUS_STEMS, 6)
        hapax = tuple(row for row in self.frequency if row[1] == 1)
        self.assertEqual(len(hapax), STANDING_N_HAPAX_PREVIOUS_STEMS)
        self.assertEqual(
            sum(count for _stem, count, _sites, _grams in self.frequency),
            13,
        )
        self.assertEqual(
            STANDING_G_SITES,
            STANDING_LEFTOVER_021087_COVERED + STANDING_LEFTOVER_999021_COVERED,
        )
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE260)
        self.assertFalse(STANDING_SAME_AS_CYCLE288)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE266)
        self.assertFalse(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE260)
        self.assertFalse(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE288)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PREVIOUS_STEM_IS_NOT_THIS_CYCLE)
        self.assertFalse(CYCLE260_SHARE_ONE)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertTrue(CYCLE266_CLAIM)
        self.assertEqual(CYCLE260_N_DISTINCT, 34)
        self.assertEqual(CYCLE260_G, "999")
        self.assertEqual(CYCLE260_K, 15)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertEqual(CYCLE266_G, "600")
        self.assertEqual(CYCLE266_K, 4)
        self.assertTrue(CYCLE266_UNIQUE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_frequency_table_and_matching_g_021_k_5(self):
        """G=021 K=5 unique-max; all leftover n=4 remaining sites have a previous token."""
        self.assertEqual(self.frequency, STANDING_PREVIOUS_STEM_FREQUENCY)
        counts = [row[1] for row in self.frequency]
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertEqual(counts[0], 5)
        self.assertEqual(self.frequency[0][0], "021")
        self.assertEqual(self.frequency[0][2], STANDING_G_SITES)
        self.assertEqual(len(STANDING_G_SITES), 5)
        self.assertEqual(self.g, "021")
        self.assertEqual(self.k, 5)
        self.assertTrue(self.unique)
        for site, prev, bwd3, prev4 in zip(
            STANDING_INSIDE_SITES,
            STANDING_PER_SITE_PREVIOUS_STEMS,
            STANDING_PER_SITE_BACKWARD_3GRAMS,
            STANDING_PER_SITE_PREVIOUS_4GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(site_previous_stem(stems, index, GRAM2), prev)
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), bwd3)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), prev4)
            self.assertIsNotNone(prev)
            self.assertGreater(index, 0)
            self.assertEqual(stems[index - 1], prev)
            self.assertEqual(bwd3, (prev, "090", "076"))
            self.assertIsNotNone(prev4)
            self.assertEqual(prev4[1:], bwd3)
            self.assertEqual(prev4[2:], GRAM2)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        for stem, count, sites, grams in STANDING_PREVIOUS_STEM_FREQUENCY:
            self.assertEqual(len(sites), count)
            self.assertEqual(len(grams), count)
            for site, gram3 in zip(sites, grams, strict=True):
                self.assertEqual(gram3[0], stem)
                self.assertEqual(gram3[1:], GRAM2)
                self.assertIn(site, STANDING_INSIDE_SITES)
        for site, prev4 in zip(
            STANDING_MATCHING_SITES,
            STANDING_MATCHING_PREVIOUS_4GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(stems[index - 1], "021")
            self.assertEqual(site_previous_stem(stems, index, GRAM2), "021")
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), prev4)
            self.assertIn(site, STANDING_INSIDE_SITES)
        for site in self.remaining:
            stems = line_stems_for_site(self.i_sides, site)
            prev = site_previous_stem(stems, site[2], GRAM2)
            self.assertIsNotNone(prev)
            self.assertNotEqual(prev, "021")
            self.assertIn(site, STANDING_REMAINING_AFTER_G_SITES)
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_nested_overlap_cycle261_259_recorded_does_not_lose(self):
        """G sites do not overlap leftover extra previous-999; overlap 258/259 extra I at Ia8[106]."""
        self.assertEqual(self.overlap_261, STANDING_OVERLAP_CYCLE261_PREVIOUS_999)
        self.assertEqual(self.overlap_261, ())
        self.assertEqual(self.overlap_258, STANDING_OVERLAP_CYCLE258_EXTRA_I)
        self.assertEqual(self.overlap_259, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_259_607, STANDING_OVERLAP_CYCLE259_EXTRA_I)
        self.assertEqual(self.overlap_258, ((SIDE_IA, "Ia8", 106),))
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE259_EXTRA_I_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), CYCLE259_EXTRA_I_BY_X["607"])
        self.assertIn((SIDE_IA, "Ia8", 106), STANDING_G_SITES)
        self.assertIn((SIDE_IA, "Ia8", 106), STANDING_LEFTOVER_999021_COVERED)
        for site in CYCLE261_MATCHING_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, STANDING_G_SITES)
        self.assertEqual(
            STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_999_SITE,
            ((SIDE_IA, "Ia9", 28),),
        )
        self.assertIn((SIDE_IA, "Ia9", 28), STANDING_INSIDE_SITES)
        self.assertNotIn((SIDE_IA, "Ia9", 28), STANDING_G_SITES)
        self.assertNotIn((SIDE_IA, "Ia9", 28), CYCLE261_MATCHING_SITES)
        self.assertIn((SIDE_IA, "Ia9", 28), CYCLE259_EXTRA_I_SITES)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_999_IS_NOT_CYCLE261)
        self.assertTrue(STANDING_OVERLAP_DOES_NOT_LOSE)
        self.assertTrue(self.claim_holds)
        self.assertEqual(CYCLE261_K_999, 15)
        self.assertEqual(CYCLE261_N_REMAINING_AFTER_999, 41)
        self.assertTrue(CYCLE261_CLAIM)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        self.assertEqual(len(CYCLE259_EXTRA_I_SITES), 3)
        self.assertEqual(CYCLE259_N_I_ONLY, 2)
        self.assertEqual(CYCLE259_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertTrue(CYCLE259_CLAIM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_301_288_266_261_260_259_224_223_still_compute(self):
        """Cycle 301 1/0, 288 share-one lost G=020 K=4, 266 unique-max G=600 K=4, 261 15/41, 260 34/999/15, 259 2/0, 224 13/56, 223 69/3 stay."""
        prior_301 = TestMamariILeftoverN4Remaining090076RemainingAfter011ExtraIFwd4IOnlyScoreboard()
        prior_301.setUp()
        prior_301.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_301.test_survey_matches_computed_lock()
        self.assertEqual(prior_301.n_i_only, 1)
        self.assertEqual(prior_301.n_not_i_only, 0)
        self.assertTrue(prior_301.claim_holds)
        self.assertTrue(CYCLE301_CLAIM)
        self.assertEqual(CYCLE301_N_I_ONLY, 1)
        self.assertEqual(CYCLE301_N_NOT_I_ONLY, 0)
        self.assertEqual(CYCLE301_SEQUENCES[0], ("090", "076", "607", "073"))
        if prior_301.n_i_only != 1 or prior_301.n_not_i_only != 0:
            self.fail("nested cycle 301 extra-I 4-gram 090 076 607 073 1/0 drifted")
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.n_inside, CYCLE288_N_INSIDE)
        self.assertEqual(prior_288.n_inside, 13)
        self.assertEqual(prior_288.n_with_next, CYCLE288_N_WITH_NEXT)
        self.assertEqual(prior_288.n_no_next, CYCLE288_N_NO_NEXT)
        self.assertEqual(prior_288.n_distinct, CYCLE288_N_DISTINCT)
        self.assertEqual(prior_288.n_distinct, 6)
        self.assertEqual(prior_288.g, CYCLE288_G)
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, CYCLE288_K)
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        if (
            prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or prior_288.claim_holds
        ):
            self.fail("nested cycle 288 share-one-forward lost 6 distinct G=020 K=4 drifted")
        prior_261 = TestMamariILeftoverExtra090076Previous999Scoreboard()
        prior_261.setUp()
        prior_261.test_counts_15_of_56_and_hypothesis_k_15_holds()
        prior_261.test_survey_matches_computed_lock()
        self.assertEqual(prior_261.k_999, 15)
        self.assertEqual(prior_261.n_remaining_after_999, 41)
        self.assertTrue(CYCLE261_CLAIM)
        if prior_261.k_999 != 15 or prior_261.n_remaining_after_999 != 41:
            self.fail("nested cycle 261 leftover extra previous-999 K_999=15 N_remaining=41 drifted")
        prior_260 = TestMamariILeftoverExtra090076PreviousStemScoreboard()
        prior_260.setUp()
        prior_260.test_counts_34_distinct_previous_stems_and_claim_loses()
        prior_260.test_survey_matches_computed_lock()
        self.assertEqual(prior_260.n_distinct, 34)
        self.assertEqual(CYCLE260_G, "999")
        self.assertEqual(CYCLE260_K, 15)
        self.assertTrue(CYCLE260_UNIQUE)
        self.assertFalse(CYCLE260_SHARE_ONE)
        if prior_260.n_distinct != 34 or CYCLE260_G != "999" or CYCLE260_K != 15:
            self.fail("nested cycle 260 34 distinct G=999 K=15 drifted")
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_each_extra_i_4gram_lock_and_claim_holds()
        prior_259.test_survey_matches_computed_lock()
        self.assertEqual(prior_259.n_i_only, 2)
        self.assertEqual(prior_259.n_not_i_only, 0)
        self.assertTrue(prior_259.claim_holds)
        self.assertTrue(CYCLE259_CLAIM)
        if prior_259.n_i_only != 2 or prior_259.n_not_i_only != 0:
            self.fail("nested cycle 259 leftover extra remaining-after-000 extra-I 4-grams 2/0 drifted")
        prior_258 = TestMamariILeftoverExtra090076RemainingAfter0003gramsIOnlyScoreboard()
        prior_258.setUp()
        prior_258.test_each_3gram_lock_extra_i_and_claim_holds()
        prior_258.test_survey_matches_computed_lock()
        self.assertTrue(prior_258.claim_holds)
        self.assertTrue(CYCLE258_CLAIM)
        self.assertEqual(CYCLE258_N_I_ONLY, 19)
        self.assertEqual(CYCLE258_N_EXTRA, 3)
        if prior_258.n_i_only != 19 or sum(prior_258.n_extra) != 3:
            self.fail("nested cycle 258 leftover extra remaining-after-000 3-grams 19/0 extra I=3 drifted")
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
        self.assertEqual(prior_223.i_hits, STANDING_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, STANDING_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, STANDING_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-302 leftover n=4 remaining previous-stem lock."""
        lock = self.survey["i_leftover_n4_remaining_090_076_previous_stem"]
        self.assertEqual(lock["cycle"], 302)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_unique_previous_stem"])
        self.assertEqual(
            lock["hypothesis_unique_previous_stem"],
            HYPOTHESIS_UNIQUE_MAX,
        )
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_with_previous"], STANDING_N_WITH_PREVIOUS)
        self.assertEqual(lock["N_with_previous"], 13)
        self.assertEqual(lock["N_line_initial"], STANDING_N_LINE_INITIAL)
        self.assertEqual(lock["N_line_initial"], 0)
        self.assertEqual(lock["N_no_previous"], STANDING_N_NO_PREVIOUS)
        self.assertEqual(lock["N_no_previous"], 0)
        self.assertEqual(lock["line_initial_sites"], [])
        self.assertEqual(lock["no_previous_sites"], [])
        self.assertEqual(
            lock["N_distinct_previous_stems"],
            STANDING_N_DISTINCT_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_distinct_previous_stems"], 8)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "021")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 5)
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertTrue(lock["G_uniquely_most_frequent"])
        self.assertEqual(
            lock["g_uniquely_most_frequent"],
            STANDING_G_UNIQUELY_MOST_FREQUENT,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["G_sites"]),
            STANDING_G_SITES,
        )
        self.assertEqual(lock["N_remaining_after_G"], STANDING_N_REMAINING_AFTER_G)
        self.assertEqual(lock["N_remaining_after_G"], 8)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_G_sites"]),
            STANDING_REMAINING_AFTER_G_SITES,
        )
        self.assertEqual(
            tuple(lock["distinct_previous_stems"]),
            STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN,
        )
        self.assertEqual(
            list(STANDING_PER_SITE_PREVIOUS_STEMS),
            lock["per_site_previous_stems"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_PER_SITE_BACKWARD_3GRAMS],
            lock["per_site_backward_3grams"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS],
            lock["per_site_previous_4grams"],
        )
        self.assertEqual(
            lock["previous_stem_frequency"],
            leftover_n4_remaining_previous_stem_frequency_rows(
                STANDING_PREVIOUS_STEM_FREQUENCY
            ),
        )
        self.assertEqual(len(lock["previous_stem_frequency"]), 8)
        self.assertEqual(lock["previous_stem_frequency"][0]["previous_stem"], "021")
        self.assertEqual(lock["previous_stem_frequency"][0]["count"], 5)
        self.assertEqual(lock["N_hapax_previous_stems"], STANDING_N_HAPAX_PREVIOUS_STEMS)
        self.assertEqual(lock["N_hapax_previous_stems"], 6)
        self.assertEqual(lock["overlap_cycle261_previous_999_sites"], [])
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE258_EXTRA_I],
            lock["overlap_cycle258_extra_i_sites"],
        )
        self.assertEqual(
            [list(site) for site in STANDING_OVERLAP_CYCLE259_EXTRA_I],
            lock["overlap_cycle259_extra_i_sites"],
        )
        self.assertTrue(lock["overlap_does_not_lose"])
        self.assertTrue(lock["leftover_n4_remaining_previous_999_is_not_cycle261"])
        self.assertEqual(
            [list(site) for site in STANDING_LEFTOVER_N4_REMAINING_PREVIOUS_999_SITE],
            lock["leftover_n4_remaining_previous_999_sites"],
        )
        self.assertEqual(
            list(STANDING_NESTED_LEFTOVER_N4_REMAINING),
            lock["nested_leftover_n4_remaining"],
        )
        self.assertEqual(lock["nested_cycle301_N_i_only"], 1)
        self.assertEqual(lock["nested_cycle301_N_not_i_only"], 0)
        self.assertEqual(
            tuple(lock["nested_cycle301_extra_i_4gram"]),
            ("090", "076", "607", "073"),
        )
        self.assertEqual(lock["nested_cycle288_N_distinct_next_stems"], 6)
        self.assertEqual(lock["nested_cycle288_G"], "020")
        self.assertEqual(lock["nested_cycle288_K"], 4)
        self.assertFalse(lock["nested_cycle288_share_one_forward_stem"])
        self.assertTrue(lock["nested_cycle288_g_uniquely_most_frequent"])
        self.assertEqual(lock["nested_cycle266_G"], "600")
        self.assertEqual(lock["nested_cycle266_K"], 4)
        self.assertTrue(lock["nested_cycle266_unique_previous_stem"])
        self.assertEqual(lock["nested_cycle261_K_999"], 15)
        self.assertEqual(lock["nested_cycle261_N_remaining_after_999"], 41)
        self.assertEqual(lock["nested_cycle260_N_distinct_previous_stems"], 34)
        self.assertEqual(lock["nested_cycle260_G"], "999")
        self.assertEqual(lock["nested_cycle260_K"], 15)
        self.assertFalse(lock["nested_cycle260_share_one_previous_stem"])
        self.assertEqual(lock["nested_cycle259_N_i_only"], 2)
        self.assertEqual(lock["nested_cycle259_N_not_i_only"], 0)
        self.assertEqual(lock["nested_cycle258_N_i_only"], 19)
        self.assertEqual(lock["nested_cycle258_N_extra"], 3)
        self.assertEqual(lock["nested_cycle224_N_inside"], 13)
        self.assertEqual(lock["nested_cycle224_N_leftover"], 56)
        self.assertEqual(lock["nested_cycle223_N_I"], 69)
        self.assertEqual(lock["nested_cycle223_N_off_I"], 3)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_n4_remaining_090_076_unique_previous_stem"])
        self.assertEqual(
            lock["i_leftover_n4_remaining_090_076_unique_previous_stem"],
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_UNIQUE_PREVIOUS_STEM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle260"])
        self.assertFalse(lock["same_as_cycle261"])
        self.assertFalse(lock["same_as_cycle266"])
        self.assertFalse(lock["same_as_cycle288"])
        self.assertFalse(lock["same_as_cycle301"])
        self.assertFalse(lock["same_claim_shape_as_cycle260"])
        self.assertTrue(lock["same_claim_shape_as_cycle266"])
        self.assertFalse(lock["same_claim_shape_as_cycle288"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["leftover_n4_remaining_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_extra_previous_stem_is_not_this_cycle"])
        self.assertTrue(lock["leftover_n4_remaining_forward_stem_is_not_this_cycle"])
        self.assertTrue(
            lock["leftover_n4_remaining_after_011_extra_i_fwd4_is_not_this_cycle"]
        )
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_999_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_previous_stem_unchanged"])
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_extra_090_076_remaining_after_000_3grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"][
                "cycle"
            ],
            301,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_011_extra_i_fwd4_i_only"][
                "N_i_only"
            ],
            1,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"],
            288,
        )
        self.assertFalse(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"][
                "i_leftover_n4_remaining_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["G"],
            "020",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["K"],
            4,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_stem"]["cycle"], 260)
        self.assertEqual(self.survey["i_leftover_extra_090_076_previous_999"]["cycle"], 261)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"][
                "cycle"
            ],
            259,
        )
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"], 13)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076PreviousStemImageSnapshot(unittest.TestCase):
    """Cycle 302 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
