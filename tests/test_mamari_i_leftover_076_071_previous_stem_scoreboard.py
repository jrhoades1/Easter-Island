"""I's cycle-172 leftover 2-gram previous-stem lock.

Cycle 190 text-search lock. Uses already-vendored A–V and the
cycle-172 leftover 34 sites of 2-gram 076 071 (the I sites
that do not sit inside leftover n=4 maximals 999 090 076 071,
999 205 076 071, 076 071 009 090, or 076 071 090 999). Does
not retune that 2-gram, those leftover sites, or the leftover
n=4 set. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each leftover site, record the previous token immediately
before 076 071 when it exists (backward 3-gram W 076 071, and
previous 4-gram V W 076 071 when it exists). Start-of-line is
no-backward. Cycle 189 remaining leftover forward 4-grams
I-only, cycle 188 remaining-17-distinct, cycle 172 leftover
N=34, and cycle 171 I-only 43/0 stay. The 9 inside-family
sites do not count as leftover. 071 999 and 076 076 do not
count as this 2-gram.

Claim that can lose:
i_leftover_076_071_share_one_previous_stem. True only if
N_distinct_previous_stems=1 and N_no_backward=0. Measured:
N_leftover=34, N_with_backward=34, N_no_backward=0,
N_distinct_previous_stems=28 (700×3, 090×3, 604×2, 099×2,
then 24 leftover hapax previous stems). The claim is false.
Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES as CYCLE171_I_SITES,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_inside_family_scoreboard import (
    STANDING_CONTAINERS,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_PREVIOUS_4GRAMS as CYCLE172_PREVIOUS_4GRAMS,
    STANDING_LEFTOVER_SITES,
    STANDING_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE172_N_LEFTOVER,
    leftover_local_4grams,
    TestMamariI2gram076071InsideFamilyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_inside_family_scoreboard import (
    leftover_sites_from_membership,
    membership_for_sites,
)
from tests.test_mamari_i_leftover_076_071_remaining_forward_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_ALL_I_ONLY,
    TestMamariILeftover076071RemainingForward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_remaining_next_stems_distinct_scoreboard import (
    STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT,
    STANDING_N_DISTINCT_REMAINING_NEXT_STEMS as CYCLE188_N_DISTINCT,
    STANDING_N_REMAINING as CYCLE188_N_REMAINING,
    TestMamariILeftover076071RemainingNextStemsDistinctScoreboard,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    NEAR_MISS_071_065_071_999,
    NEAR_MISS_700_076_076_053,
    TestMamariILeftoverN4076071Scoreboard,
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

HYPOTHESIS_SHARE_ONE = True
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_LEFTOVER = 34
STANDING_N_WITH_BACKWARD = 34
STANDING_N_NO_BACKWARD = 0
STANDING_N_DISTINCT_PREVIOUS_STEMS = 28
STANDING_N_HAPAX_PREVIOUS_STEMS = 24
STANDING_NO_BACKWARD_SITES = ()
STANDING_PER_SITE_PREVIOUS_STEMS = (
    "200",
    "700",
    "071",
    "700",
    "633",
    "076",
    "225",
    "385",
    "298",
    "205",
    "604",
    "090",
    "406",
    "072",
    "099",
    "999",
    "222",
    "514",
    "604",
    "099",
    "440",
    "606",
    "290",
    "009",
    "007",
    "006",
    "730",
    "600",
    "700",
    "048",
    "090",
    "011",
    "090",
    "000",
)
STANDING_PER_SITE_BACKWARD_3GRAMS = tuple(
    (stem, "076", "071") for stem in STANDING_PER_SITE_PREVIOUS_STEMS
)
STANDING_PER_SITE_PREVIOUS_4GRAMS = CYCLE172_PREVIOUS_4GRAMS
STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN = (
    "200",
    "700",
    "071",
    "633",
    "076",
    "225",
    "385",
    "298",
    "205",
    "604",
    "090",
    "406",
    "072",
    "099",
    "999",
    "222",
    "514",
    "440",
    "606",
    "290",
    "009",
    "007",
    "006",
    "730",
    "600",
    "048",
    "011",
    "000",
)
STANDING_PREVIOUS_STEM_FREQUENCY = (
    (
        "700",
        3,
        (
            (SIDE_IA, "Ia1", 163),
            (SIDE_IA, "Ia2", 51),
            (SIDE_IA, "Ia13", 128),
        ),
        (
            ("090", "700", "076", "071"),
            ("999", "700", "076", "071"),
            ("040", "700", "076", "071"),
        ),
    ),
    (
        "090",
        3,
        (
            (SIDE_IA, "Ia5", 67),
            (SIDE_IA, "Ia13", 153),
            (SIDE_IA, "Ia14", 106),
        ),
        (
            ("000", "090", "076", "071"),
            ("076", "090", "076", "071"),
            ("090", "090", "076", "071"),
        ),
    ),
    (
        "604",
        2,
        (
            (SIDE_IA, "Ia3", 147),
            (SIDE_IA, "Ia9", 10),
        ),
        (
            ("600", "604", "076", "071"),
            ("700", "604", "076", "071"),
        ),
    ),
    (
        "099",
        2,
        (
            (SIDE_IA, "Ia6", 117),
            (SIDE_IA, "Ia12", 6),
        ),
        (
            ("430", "099", "076", "071"),
            ("019", "099", "076", "071"),
        ),
    ),
    (
        "200",
        1,
        ((SIDE_IA, "Ia1", 86),),
        (("027", "200", "076", "071"),),
    ),
    (
        "071",
        1,
        ((SIDE_IA, "Ia2", 43),),
        (("430", "071", "076", "071"),),
    ),
    (
        "633",
        1,
        ((SIDE_IA, "Ia2", 104),),
        (("005", "633", "076", "071"),),
    ),
    (
        "076",
        1,
        ((SIDE_IA, "Ia2", 169),),
        (("147", "076", "076", "071"),),
    ),
    (
        "225",
        1,
        ((SIDE_IA, "Ia3", 13),),
        (("205", "225", "076", "071"),),
    ),
    (
        "385",
        1,
        ((SIDE_IA, "Ia3", 85),),
        (("076", "385", "076", "071"),),
    ),
    (
        "298",
        1,
        ((SIDE_IA, "Ia3", 110),),
        (("530", "298", "076", "071"),),
    ),
    (
        "205",
        1,
        ((SIDE_IA, "Ia3", 133),),
        (("070", "205", "076", "071"),),
    ),
    (
        "406",
        1,
        ((SIDE_IA, "Ia5", 79),),
        (("999", "406", "076", "071"),),
    ),
    (
        "072",
        1,
        ((SIDE_IA, "Ia5", 134),),
        (("071", "072", "076", "071"),),
    ),
    (
        "999",
        1,
        ((SIDE_IA, "Ia7", 32),),
        (("076", "999", "076", "071"),),
    ),
    (
        "222",
        1,
        ((SIDE_IA, "Ia7", 48),),
        (("400", "222", "076", "071"),),
    ),
    (
        "514",
        1,
        ((SIDE_IA, "Ia8", 27),),
        (("002", "514", "076", "071"),),
    ),
    (
        "440",
        1,
        ((SIDE_IA, "Ia12", 19),),
        (("490", "440", "076", "071"),),
    ),
    (
        "606",
        1,
        ((SIDE_IA, "Ia12", 59),),
        (("050", "606", "076", "071"),),
    ),
    (
        "290",
        1,
        ((SIDE_IA, "Ia12", 63),),
        (("061", "290", "076", "071"),),
    ),
    (
        "009",
        1,
        ((SIDE_IA, "Ia13", 44),),
        (("002", "009", "076", "071"),),
    ),
    (
        "007",
        1,
        ((SIDE_IA, "Ia13", 54),),
        (("999", "007", "076", "071"),),
    ),
    (
        "006",
        1,
        ((SIDE_IA, "Ia13", 92),),
        (("073", "006", "076", "071"),),
    ),
    (
        "730",
        1,
        ((SIDE_IA, "Ia13", 101),),
        (("042", "730", "076", "071"),),
    ),
    (
        "600",
        1,
        ((SIDE_IA, "Ia13", 114),),
        (("084", "600", "076", "071"),),
    ),
    (
        "048",
        1,
        ((SIDE_IA, "Ia13", 149),),
        (("006", "048", "076", "071"),),
    ),
    (
        "011",
        1,
        ((SIDE_IA, "Ia14", 81),),
        (("076", "011", "076", "071"),),
    ),
    (
        "000",
        1,
        ((SIDE_IA, "Ia14", 166),),
        (("006", "000", "076", "071"),),
    ),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_071_share_one_previous_stem"
STANDING_I_LEFTOVER_076_071_SHARE_ONE_PREVIOUS_STEM = False
STANDING_RESULT = "i_leftover_076_071_previous_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE189 = False
STANDING_SAME_AS_CYCLE188 = False
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def site_previous_stem(
    stems: list[str],
    index: int,
    gram2: tuple[str, ...] = GRAM2,
) -> str | None:
    """Previous stem W before 076 071; None at start-of-line or mismatch."""
    if tuple(stems[index : index + len(gram2)]) != gram2:
        return None
    if index == 0:
        return None
    return stems[index - 1]


def site_backward_3gram(
    stems: list[str],
    index: int,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str, ...] | None:
    """W 076 071 if a previous stem exists; None at start-of-line."""
    prev = site_previous_stem(stems, index, gram2)
    if prev is None:
        return None
    return (prev,) + gram2


def site_previous_4gram(
    stems: list[str],
    index: int,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str, ...] | None:
    """V W 076 071 if two previous stems exist; None otherwise."""
    n2 = len(gram2)
    if tuple(stems[index : index + n2]) != gram2:
        return None
    if index < 2:
        return None
    return tuple(stems[index - 2 : index + n2])


def leftover_previous_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str | None, ...]:
    """Per-site previous stem or None for the locked leftover sites."""
    return tuple(
        site_previous_stem(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_backward_3grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site backward 3-gram or None for the locked leftover sites."""
    return tuple(
        site_backward_3gram(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_previous_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site previous 4-gram or None for the locked leftover sites."""
    return tuple(
        site_previous_4gram(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_sites_with_backward(
    sites: tuple[tuple[str, str, int], ...],
    previous: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that have a previous stem before 076 071."""
    return tuple(
        site
        for site, prev in zip(sites, previous, strict=True)
        if prev is not None
    )


def leftover_sites_without_backward(
    sites: tuple[tuple[str, str, int], ...],
    previous: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that are start-of-line (no-backward)."""
    return tuple(
        site
        for site, prev in zip(sites, previous, strict=True)
        if prev is None
    )


def group_sites_by_previous_stem(
    sites: tuple[tuple[str, str, int], ...],
    previous: tuple[str | None, ...],
) -> tuple[tuple[str, tuple[tuple[str, str, int], ...]], ...]:
    """Distinct previous stems in first-seen order, with their sites."""
    groups: list[tuple[str, list[tuple[str, str, int]]]] = []
    index_by_stem: dict[str, int] = {}
    for site, prev in zip(sites, previous, strict=True):
        if prev is None:
            continue
        if prev not in index_by_stem:
            index_by_stem[prev] = len(groups)
            groups.append((prev, [site]))
        else:
            groups[index_by_stem[prev]][1].append(site)
    return tuple((stem, tuple(stem_sites)) for stem, stem_sites in groups)


def previous_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    previous: tuple[str | None, ...],
    previous_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Previous-stem frequency: highest count first, then first-seen."""
    first_seen = group_sites_by_previous_stem(sites, previous)
    grams_by_stem: dict[str, list[tuple[str, ...]]] = {stem: [] for stem, _ in first_seen}
    for prev, gram4 in zip(previous, previous_4grams, strict=True):
        if prev is None or gram4 is None:
            continue
        grams_by_stem[prev].append(gram4)
    rows = tuple(
        (stem, len(stem_sites), stem_sites, tuple(grams_by_stem[stem]))
        for stem, stem_sites in first_seen
    )
    return tuple(sorted(rows, key=lambda row: (-row[1],)))


def previous_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_PREVIOUS_STEM_FREQUENCY,
) -> list[dict]:
    """Survey-shaped previous-stem frequency table, highest count first."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "previous_stem": stem,
                "count": count,
                "leftover_sites": [list(site) for site in sites],
                "previous_4grams": [list(gram) for gram in grams],
            }
        )
    return rows


def i_leftover_076_071_share_one_previous_stem(
    n_distinct_previous_stems: int,
    n_no_backward: int,
) -> bool:
    """True iff N_distinct_previous_stems=1 and N_no_backward=0."""
    return n_distinct_previous_stems == 1 and n_no_backward == 0


class TestILeftover076071PreviousStemHelpers(unittest.TestCase):
    """Helpers on cycle-172 leftover 076 071 previous stems. No CV, no LLM."""

    def test_previous_requires_stem_before_2gram(self):
        """A previous stem is a 3-gram; start-of-line is no-backward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N3, STANDING_N2 + 1)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_700 = ["090", "700", "076", "071", "700", "076"]
        self.assertEqual(site_previous_stem(has_700, 2, GRAM2), "700")
        self.assertEqual(site_backward_3gram(has_700, 2, GRAM2), ("700", "076", "071"))
        self.assertEqual(
            site_previous_4gram(has_700, 2, GRAM2),
            ("090", "700", "076", "071"),
        )
        has_090 = ["000", "090", "076", "071", "004", "004"]
        self.assertEqual(site_previous_stem(has_090, 2, GRAM2), "090")
        self.assertEqual(site_backward_3gram(has_090, 2, GRAM2), ("090", "076", "071"))
        start_of_line = ["076", "071", "090", "606"]
        self.assertIsNone(site_previous_stem(start_of_line, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(start_of_line, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(start_of_line, 0, GRAM2))
        only_one_prev = ["200", "076", "071"]
        self.assertEqual(site_previous_stem(only_one_prev, 1, GRAM2), "200")
        self.assertEqual(site_backward_3gram(only_one_prev, 1, GRAM2), ("200", "076", "071"))
        self.assertIsNone(site_previous_4gram(only_one_prev, 1, GRAM2))
        mismatch = ["700", "076", "070"]
        self.assertIsNone(site_previous_stem(mismatch, 1, GRAM2))
        self.assertIsNone(site_backward_3gram(mismatch, 1, GRAM2))
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_one_distinct_and_zero_no_backward(self):
        """Boolean is True only when N_distinct=1 and N_no_backward=0."""
        provider = MockProvider()
        self.assertTrue(i_leftover_076_071_share_one_previous_stem(1, 0))
        self.assertFalse(i_leftover_076_071_share_one_previous_stem(28, 0))
        self.assertFalse(i_leftover_076_071_share_one_previous_stem(2, 0))
        self.assertFalse(i_leftover_076_071_share_one_previous_stem(1, 1))
        self.assertFalse(i_leftover_076_071_share_one_previous_stem(0, 0))
        self.assertFalse(i_leftover_076_071_share_one_previous_stem(34, 0))
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_share_one_previous_stem")
        self.assertFalse(STANDING_I_LEFTOVER_076_071_SHARE_ONE_PREVIOUS_STEM)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_076_071_SHARE_ONE_PREVIOUS_STEM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(STANDING_N_DISTINCT_PREVIOUS_STEMS, 28)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_frequency_table_sorts_highest_count_first_and_skips_none(self):
        """Frequency table is count-desc; no-backward sites are omitted."""
        provider = MockProvider()
        sites = STANDING_LEFTOVER_SITES[:6]
        previous = ("200", "700", "071", "700", None, "200")
        grams = (
            ("027", "200", "076", "071"),
            ("090", "700", "076", "071"),
            ("430", "071", "076", "071"),
            ("999", "700", "076", "071"),
            None,
            ("111", "200", "076", "071"),
        )
        table = previous_stem_frequency_table(sites, previous, grams)
        self.assertEqual(table[0][0], "200")
        self.assertEqual(table[0][1], 2)
        self.assertEqual(table[1][0], "700")
        self.assertEqual(table[1][1], 2)
        self.assertEqual(table[2][0], "071")
        self.assertEqual(table[2][1], 1)
        self.assertEqual(len(table), 3)
        self.assertEqual(
            leftover_sites_without_backward(sites, previous),
            (sites[4],),
        )
        self.assertEqual(
            leftover_sites_with_backward(sites, previous),
            (sites[0], sites[1], sites[2], sites[3], sites[5]),
        )
        shared = ("700",) * 6
        shared_grams = (("090", "700", "076", "071"),) * 6
        shared_table = previous_stem_frequency_table(sites, shared, shared_grams)
        self.assertEqual(len(shared_table), 1)
        self.assertEqual(shared_table[0][0], "700")
        self.assertEqual(shared_table[0][1], 6)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076071PreviousStemScoreboard(unittest.TestCase):
    """Cited-fixture leftover 076 071 previous-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.membership = membership_for_sites(
            self.i_sides,
            self.i_sites,
            STANDING_CONTAINERS,
            GRAM2,
        )
        self.measured_leftover = leftover_sites_from_membership(
            self.i_sites,
            self.membership,
        )
        self.previous = leftover_previous_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.backwards = leftover_backward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.previous_4grams = leftover_previous_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.with_backward = leftover_sites_with_backward(
            self.leftover_sites,
            self.previous,
        )
        self.no_backward = leftover_sites_without_backward(
            self.leftover_sites,
            self.previous,
        )
        self.first_seen = group_sites_by_previous_stem(
            self.leftover_sites,
            self.previous,
        )
        self.frequency = previous_stem_frequency_table(
            self.leftover_sites,
            self.previous,
            self.previous_4grams,
        )
        self.n_leftover = len(self.leftover_sites)
        self.n_with_backward = len(self.with_backward)
        self.n_no_backward = len(self.no_backward)
        self.n_distinct = len(self.first_seen)
        self.claim_holds = i_leftover_076_071_share_one_previous_stem(
            self.n_distinct,
            self.n_no_backward,
        )

    def test_tokens_and_sites_are_cycle_172_leftover_not_retuned(self):
        """2-gram and leftover 34 stay the cycle-172/171/189/188 locks."""
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.measured_leftover, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.measured_leftover, self.leftover_sites)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE172_N_LEFTOVER)
        self.assertEqual(CYCLE172_N_LEFTOVER, 34)
        self.assertEqual(self.i_sites, CYCLE171_I_SITES)
        self.assertEqual(len(self.i_sites), CYCLE171_N_I)
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(len(STANDING_INSIDE_SITES), STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 9)
        self.assertEqual(STANDING_N_INSIDE + STANDING_N_LEFTOVER, CYCLE171_N_I)
        prior_189 = self.survey["i_leftover_076_071_remaining_forward_4grams_i_only"]
        self.assertEqual(prior_189["cycle"], 189)
        self.assertTrue(prior_189["i_leftover_076_071_remaining_forward_4grams_all_i_only"])
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_FORWARD_4GRAMS_ALL_I_ONLY)
        self.assertEqual(prior_189["N_leftover"], 34)
        self.assertEqual(prior_189["N_remaining"], 17)
        prior_188 = self.survey["i_leftover_076_071_remaining_next_stems_distinct"]
        self.assertEqual(prior_188["cycle"], 188)
        self.assertTrue(prior_188["i_leftover_076_071_remaining_next_stems_all_distinct"])
        self.assertTrue(STANDING_I_LEFTOVER_076_071_REMAINING_NEXT_STEMS_ALL_DISTINCT)
        self.assertEqual(prior_188["N_leftover"], 34)
        self.assertEqual(prior_188["N_remaining"], CYCLE188_N_REMAINING)
        self.assertEqual(prior_188["N_remaining"], 17)
        self.assertEqual(
            prior_188["N_distinct_remaining_next_stems"],
            CYCLE188_N_DISTINCT,
        )
        self.assertEqual(prior_188["N_distinct_remaining_next_stems"], 17)
        prior_172 = self.survey["i_2gram_076_071_inside_family"]
        self.assertEqual(prior_172["cycle"], 172)
        self.assertEqual(prior_172["N_leftover"], 34)
        self.assertFalse(prior_172["i_2gram_076_071_all_inside_leftover_n4_family"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_172["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in CYCLE172_PREVIOUS_4GRAMS],
            prior_172["leftover_previous_4grams"],
        )
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], CYCLE171_N_I)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], CYCLE171_N_OFF_I)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_28_distinct_previous_stems_and_claim_loses(self):
        """N_leftover=34, N_with_backward=34, N_distinct=28. Claim loses."""
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 34)
        self.assertEqual(self.n_with_backward, STANDING_N_WITH_BACKWARD)
        self.assertEqual(STANDING_N_WITH_BACKWARD, 34)
        self.assertEqual(self.n_no_backward, STANDING_N_NO_BACKWARD)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(self.no_backward, STANDING_NO_BACKWARD_SITES)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_PREVIOUS_STEMS)
        self.assertEqual(STANDING_N_DISTINCT_PREVIOUS_STEMS, 28)
        self.assertEqual(
            self.n_with_backward + self.n_no_backward,
            self.n_leftover,
        )
        self.assertNotEqual(self.n_distinct, 1)
        self.assertFalse(
            i_leftover_076_071_share_one_previous_stem(
                self.n_distinct,
                self.n_no_backward,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_071_SHARE_ONE_PREVIOUS_STEM,
        )
        self.assertFalse(STANDING_I_LEFTOVER_076_071_SHARE_ONE_PREVIOUS_STEM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_071_share_one_previous_stem")
        self.assertEqual(self.previous, STANDING_PER_SITE_PREVIOUS_STEMS)
        self.assertEqual(self.backwards, STANDING_PER_SITE_BACKWARD_3GRAMS)
        self.assertEqual(self.previous_4grams, STANDING_PER_SITE_PREVIOUS_4GRAMS)
        self.assertEqual(self.previous_4grams, CYCLE172_PREVIOUS_4GRAMS)
        measured_local = leftover_local_4grams(self.i_sides, self.leftover_sites)
        self.assertEqual(
            measured_local,
            leftover_local_4grams(self.i_sides, STANDING_LEFTOVER_SITES),
        )
        for (_site, prev4, _nxt), prev in zip(
            measured_local,
            self.previous,
            strict=True,
        ):
            self.assertIsNotNone(prev4)
            self.assertEqual(prev4[1], prev)
            self.assertEqual(prev4[2:], GRAM2)
        self.assertEqual(
            tuple(stem for stem, _sites in self.first_seen),
            STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN,
        )
        self.assertEqual(len(set(STANDING_PER_SITE_PREVIOUS_STEMS)), 28)
        self.assertEqual(len(STANDING_PREVIOUS_STEM_FREQUENCY), 28)
        self.assertEqual(STANDING_N_HAPAX_PREVIOUS_STEMS, 24)
        hapax = tuple(row for row in self.frequency if row[1] == 1)
        self.assertEqual(len(hapax), STANDING_N_HAPAX_PREVIOUS_STEMS)
        self.assertEqual(
            sum(count for _stem, count, _sites, _grams in self.frequency),
            34,
        )
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE189)
        self.assertFalse(STANDING_SAME_AS_CYCLE188)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_frequency_table_and_per_site_previous_stems_match_fixtures(self):
        """Highest-count previous stems first; each leftover site has W 076 071."""
        self.assertEqual(self.frequency, STANDING_PREVIOUS_STEM_FREQUENCY)
        self.assertEqual(self.frequency[0][0], "700")
        self.assertEqual(self.frequency[0][1], 3)
        self.assertEqual(self.frequency[1][0], "090")
        self.assertEqual(self.frequency[1][1], 3)
        self.assertEqual(self.frequency[2][0], "604")
        self.assertEqual(self.frequency[2][1], 2)
        self.assertEqual(self.frequency[3][0], "099")
        self.assertEqual(self.frequency[3][1], 2)
        counts = [row[1] for row in self.frequency]
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertEqual(counts[:4], [3, 3, 2, 2])
        self.assertTrue(all(count == 1 for count in counts[4:]))
        for site, prev, back3, prev4 in zip(
            STANDING_LEFTOVER_SITES,
            STANDING_PER_SITE_PREVIOUS_STEMS,
            STANDING_PER_SITE_BACKWARD_3GRAMS,
            STANDING_PER_SITE_PREVIOUS_4GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertGreaterEqual(index, 1)
            self.assertEqual(stems[index - 1], prev)
            self.assertEqual(site_previous_stem(stems, index, GRAM2), prev)
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), back3)
            self.assertEqual(back3, (prev, "076", "071"))
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), prev4)
            self.assertEqual(prev4[1:], back3)
            self.assertEqual(prev4[2:], GRAM2)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, STANDING_INSIDE_SITES)
        for site in STANDING_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_071_065_071_999))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        for stem, count, sites, grams in STANDING_PREVIOUS_STEM_FREQUENCY:
            self.assertEqual(len(sites), count)
            self.assertEqual(len(grams), count)
            for site, gram4 in zip(sites, grams, strict=True):
                self.assertEqual(gram4[1], stem)
                self.assertEqual(gram4[2:], GRAM2)
                self.assertIn(site, STANDING_LEFTOVER_SITES)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[11], "Ia12")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_189_188_172_171_scoreboards_still_compute(self):
        """Cycle 189 remaining-4 I-only, 188 remaining-17, 172 leftover-34, 171 I-only stay."""
        prior_189 = TestMamariILeftover076071RemainingForward4gramsIOnlyScoreboard()
        prior_189.setUp()
        prior_189.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_189.test_survey_matches_computed_lock()
        prior_188 = TestMamariILeftover076071RemainingNextStemsDistinctScoreboard()
        prior_188.setUp()
        prior_188.test_counts_17_of_34_remaining_all_distinct_and_claim_holds()
        prior_188.test_survey_matches_computed_lock()
        prior_172 = TestMamariI2gram076071InsideFamilyScoreboard()
        prior_172.setUp()
        prior_172.test_forty_three_sites_split_9_inside_34_leftover_and_claim_loses()
        prior_172.test_survey_matches_computed_lock()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-190 leftover previous-stem lock."""
        lock = self.survey["i_leftover_076_071_previous_stem"]
        self.assertEqual(lock["cycle"], 190)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_one_previous_stem"])
        self.assertEqual(
            lock["hypothesis_share_one_previous_stem"],
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 34)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_backward"], STANDING_N_WITH_BACKWARD)
        self.assertEqual(lock["N_with_backward"], 34)
        self.assertEqual(lock["N_no_backward"], STANDING_N_NO_BACKWARD)
        self.assertEqual(lock["N_no_backward"], 0)
        self.assertEqual(lock["no_backward_sites"], [])
        self.assertEqual(
            lock["N_distinct_previous_stems"],
            STANDING_N_DISTINCT_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_distinct_previous_stems"], 28)
        self.assertEqual(
            tuple(lock["distinct_previous_stems"]),
            STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN,
        )
        self.assertEqual(
            tuple(lock["per_site_previous_stems"]),
            STANDING_PER_SITE_PREVIOUS_STEMS,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_BACKWARD_3GRAMS],
            lock["per_site_backward_3grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_PREVIOUS_4GRAMS],
            lock["per_site_previous_4grams"],
        )
        self.assertEqual(
            lock["previous_stem_frequency"],
            previous_stem_frequency_rows(),
        )
        self.assertEqual(len(lock["previous_stem_frequency"]), 28)
        self.assertEqual(lock["previous_stem_frequency"][0]["previous_stem"], "700")
        self.assertEqual(lock["previous_stem_frequency"][0]["count"], 3)
        self.assertEqual(lock["previous_stem_frequency"][1]["previous_stem"], "090")
        self.assertEqual(lock["previous_stem_frequency"][1]["count"], 3)
        self.assertEqual(lock["previous_stem_frequency"][2]["previous_stem"], "604")
        self.assertEqual(lock["previous_stem_frequency"][2]["count"], 2)
        self.assertEqual(lock["previous_stem_frequency"][3]["previous_stem"], "099")
        self.assertEqual(lock["previous_stem_frequency"][3]["count"], 2)
        self.assertEqual(lock["N_hapax_previous_stems"], STANDING_N_HAPAX_PREVIOUS_STEMS)
        self.assertEqual(lock["N_hapax_previous_stems"], 24)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_076_071_share_one_previous_stem"])
        self.assertEqual(
            lock["i_leftover_076_071_share_one_previous_stem"],
            STANDING_I_LEFTOVER_076_071_SHARE_ONE_PREVIOUS_STEM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle189"])
        self.assertFalse(lock["same_as_cycle188"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_076_071_remaining_forward_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_remaining_next_stems_distinct_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_forward_4grams_i_only"]["cycle"],
            189,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_remaining_forward_4grams_i_only"][
                "i_leftover_076_071_remaining_forward_4grams_all_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_next_stems_distinct"]["cycle"],
            188,
        )
        self.assertTrue(
            self.survey["i_leftover_076_071_remaining_next_stems_distinct"][
                "i_leftover_076_071_remaining_next_stems_all_distinct"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_071_remaining_next_stems_distinct"]["N_remaining"],
            17,
        )
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["cycle"], 172)
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["N_leftover"], 34)
        self.assertFalse(
            self.survey["i_2gram_076_071_inside_family"][
                "i_2gram_076_071_all_inside_leftover_n4_family"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"]["i_leftover_n4_exactly_4_contain_076_071"]
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
        self.assertTrue(
            self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"]
        )
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(
            self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"]
        )
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(
            self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"],
            5,
        )
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftover076071PreviousStemImageSnapshot(unittest.TestCase):
    """Cycle 190 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
