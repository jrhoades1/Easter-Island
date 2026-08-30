"""I's cycle-215 leftover 2-gram forward-stem lock.

Cycle 216 text-search lock. Uses already-vendored A–V and the
cycle-206 leftover I sites of 2-gram 076 070 (the I sites that
are not 090-prefixed 090 076 070). Does not retune that 2-gram,
those leftover sites, the cycle-207 8 I 090 076 070 sites, or
the leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished Ib
is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each leftover I site, record the next token immediately
after 076 070 when it exists (forward 3-gram 076 070 X, and
next 4-gram 076 070 X Y when it exists). End-of-line is
no-forward. Previous side of leftover 076 070 is closed
(cycles 210–215). Cycle 215 remaining previous 4-grams I-only
hapax 1/0 x8, cycle 214 remaining N_remaining=8 / N_distinct=8,
cycle 210 leftover share-one-previous-stem lost N_leftover=11
N_distinct=9, cycle 206 076 070 19/5 loss, and cycle 171
076 071 I-only 43/0 stay. The 8 I 090 076 070 sites do not
count as leftover. Off-I 076 070 sites do not count as leftover
I. 076 071 is a different 2-gram.

Claim that can lose:
i_leftover_076_070_share_one_forward_stem. True only if
N_distinct_next_stems=1 and N_leftover>=2. Measured:
N_leftover=11, N_090_prefixed=8, N_I=19, N_with_forward=11,
N_no_forward=0, N_distinct_next_stems=11 (all hapax next stems
449/560/600/430/146/305/073/701/091/076/027). The claim is
false. Same claim-shape as cycle 210 (leftover 076 070
share-one-previous-stem lost, N_distinct=9) and cycle 173's
forward-cluster start on leftover 076 071. Do not assume the
result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_2gram_076_070_i_only_scoreboard import (
    GRAM2 as CYCLE206_GRAM2,
    STANDING_I_SITES as CYCLE206_I_SITES,
    STANDING_N_I as CYCLE206_N_I,
    STANDING_N_OFF_I as CYCLE206_N_OFF_I,
    STANDING_OFF_I_SITES as CYCLE206_OFF_I_SITES,
    TestMamariI2gram076070IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_previous_stem_scoreboard import (
    GRAM2,
    PREFIXED_STEM,
    STANDING_I_LEFTOVER_076_070_SHARE_ONE_PREVIOUS_STEM as CYCLE210_SHARE_ONE,
    STANDING_LEFTOVER_SITES,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE210_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE210_N_LEFTOVER,
    STANDING_N_090_PREFIXED as CYCLE210_N_090_PREFIXED,
    STANDING_PREFIXED_I_SITES,
    leftover_2gram_sites_from_prefixed_3grams,
    split_i_076_070_sites,
    TestMamariILeftover076070PreviousStemScoreboard,
)
from tests.test_mamari_i_leftover_076_070_remaining_previous_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_4GRAMS_I_ONLY as CYCLE215_I_ONLY,
    STANDING_N_I_EACH as CYCLE215_N_I_EACH,
    STANDING_N_OFF_I_EACH as CYCLE215_N_OFF_I_EACH,
    STANDING_N_REMAINING as CYCLE215_N_REMAINING,
    TestMamariILeftover076070RemainingPrevious4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_remaining_previous_stems_distinct_scoreboard import (
    STANDING_I_LEFTOVER_076_070_REMAINING_PREVIOUS_STEMS_DISTINCT as CYCLE214_CLAIM,
    STANDING_N_DISTINCT_REMAINING as CYCLE214_N_DISTINCT,
    STANDING_N_REMAINING as CYCLE214_N_REMAINING,
    TestMamariILeftover076070RemainingPreviousStemsDistinctScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    STANDING_I_LEFTOVER_076_071_EXACTLY_5_FORWARD_076_071_076 as CYCLE173_CLAIM,
    STANDING_N_LEFTOVER as CYCLE173_N_LEFTOVER,
    STANDING_N_WITH_FORWARD_076_071_076 as CYCLE173_N_WITH,
    site_forward_3gram,
    site_next_4gram,
    TestMamariILeftover076071Forward076Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    group_sites_by_previous_stem,
    leftover_sites_with_backward,
    leftover_sites_without_backward,
    previous_stem_frequency_table,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
    GRAM2 as CYCLE205_GRAM2,
    NEAR_MISS_700_076_076_053,
    NEAR_MISS_999_090_076_071,
    TestMamariILeftoverN4076070Scoreboard,
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
PREFIXED_3GRAM = CYCLE207_GRAM3
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_I = CYCLE206_N_I
STANDING_N_090_PREFIXED = CYCLE210_N_090_PREFIXED
STANDING_N_LEFTOVER = 11
STANDING_N_WITH_FORWARD = 11
STANDING_N_NO_FORWARD = 0
STANDING_N_DISTINCT_NEXT_STEMS = 11
STANDING_N_HAPAX_NEXT_STEMS = 11
STANDING_NO_FORWARD_SITES = ()
STANDING_PER_SITE_NEXT_STEMS = (
    "449",
    "560",
    "600",
    "430",
    "146",
    "305",
    "073",
    "701",
    "091",
    "076",
    "027",
)
STANDING_PER_SITE_FORWARD_3GRAMS = tuple(
    ("076", "070", stem) for stem in STANDING_PER_SITE_NEXT_STEMS
)
STANDING_PER_SITE_NEXT_4GRAMS = (
    ("076", "070", "449", "449"),
    ("076", "070", "560", "072"),
    ("076", "070", "600", "090"),
    ("076", "070", "430", "061"),
    ("076", "070", "146", "490"),
    ("076", "070", "305", "999"),
    ("076", "070", "073", "064"),
    ("076", "070", "701", "214"),
    ("076", "070", "091", "430"),
    ("076", "070", "076", "670"),
    ("076", "070", "027", "090"),
)
STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN = STANDING_PER_SITE_NEXT_STEMS
STANDING_NEXT_STEM_FREQUENCY = tuple(
    (
        stem,
        1,
        (site,),
        (gram4,),
    )
    for stem, site, gram4 in zip(
        STANDING_PER_SITE_NEXT_STEMS,
        STANDING_LEFTOVER_SITES,
        STANDING_PER_SITE_NEXT_4GRAMS,
        strict=True,
    )
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_070_share_one_forward_stem"
STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM = False
STANDING_RESULT = "i_leftover_076_070_forward_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE173 = False
STANDING_SAME_AS_CYCLE210 = False
STANDING_SAME_AS_CYCLE215 = False
STANDING_090_PREFIXED_DOES_NOT_COUNT = True
STANDING_OFF_I_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_PREVIOUS_SIDE_CLOSED = True


def site_next_stem(
    stems: list[str],
    index: int,
    gram2: tuple[str, ...] = GRAM2,
) -> str | None:
    """Next stem X after 076 070; None at end-of-line or mismatch."""
    n2 = len(gram2)
    if tuple(stems[index : index + n2]) != gram2:
        return None
    next_index = index + n2
    if next_index >= len(stems):
        return None
    return stems[next_index]


def leftover_next_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str | None, ...]:
    """Per-site next stem or None for the locked leftover sites."""
    return tuple(
        site_next_stem(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_forward_3grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site forward 3-gram or None for the locked leftover sites."""
    return tuple(
        site_forward_3gram(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_next_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site next 4-gram or None for the locked leftover sites."""
    return tuple(
        site_next_4gram(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_sites_with_forward(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that have a next stem after 076 070."""
    return leftover_sites_with_backward(sites, next_stems)


def leftover_sites_without_forward(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover sites that are end-of-line (no-forward)."""
    return leftover_sites_without_backward(sites, next_stems)


def group_sites_by_next_stem(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, tuple[tuple[str, str, int], ...]], ...]:
    """Distinct next stems in first-seen order, with their sites."""
    return group_sites_by_previous_stem(sites, next_stems)


def next_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    next_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Next-stem frequency: highest count first, then first-seen."""
    return previous_stem_frequency_table(sites, next_stems, next_4grams)


def next_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_NEXT_STEM_FREQUENCY,
) -> list[dict]:
    """Survey-shaped next-stem frequency table, highest count first."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "next_stem": stem,
                "count": count,
                "leftover_sites": [list(site) for site in sites],
                "next_4grams": [list(gram) for gram in grams],
            }
        )
    return rows


def i_leftover_076_070_share_one_forward_stem(
    n_distinct_next_stems: int,
    n_leftover: int,
) -> bool:
    """True iff N_distinct_next_stems=1 and N_leftover>=2."""
    return n_distinct_next_stems == 1 and n_leftover >= 2


class TestILeftover076070ForwardStemHelpers(unittest.TestCase):
    """Helpers on leftover I 076 070 next stems. No CV, no LLM."""

    def test_next_requires_stem_after_2gram(self):
        """A next stem is a 3-gram; end-of-line is no-forward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM2, CYCLE206_GRAM2)
        self.assertEqual(PREFIXED_3GRAM, ("090", "076", "070"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N3, STANDING_N2 + 1)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_449 = ["099", "571", "076", "070", "449", "449"]
        self.assertEqual(site_next_stem(has_449, 2, GRAM2), "449")
        self.assertEqual(site_forward_3gram(has_449, 2, GRAM2), ("076", "070", "449"))
        self.assertEqual(
            site_next_4gram(has_449, 2, GRAM2),
            ("076", "070", "449", "449"),
        )
        has_076 = ["600", "604", "076", "070", "076", "670"]
        self.assertEqual(site_next_stem(has_076, 2, GRAM2), "076")
        self.assertEqual(site_forward_3gram(has_076, 2, GRAM2), ("076", "070", "076"))
        end_of_line = ["067", "606", "076", "070"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        self.assertIsNone(site_forward_3gram(end_of_line, 2, GRAM2))
        self.assertIsNone(site_next_4gram(end_of_line, 2, GRAM2))
        only_one_next = ["076", "070", "027"]
        self.assertEqual(site_next_stem(only_one_next, 0, GRAM2), "027")
        self.assertEqual(
            site_forward_3gram(only_one_next, 0, GRAM2),
            ("076", "070", "027"),
        )
        self.assertIsNone(site_next_4gram(only_one_next, 0, GRAM2))
        mismatch_071 = ["720", "076", "071", "076"]
        self.assertIsNone(site_next_stem(mismatch_071, 1, GRAM2))
        self.assertIsNone(site_forward_3gram(mismatch_071, 1, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_split_excludes_090_prefixed_and_keeps_leftover(self):
        """090-prefixed I sites are not leftover; leftover cannot silently drift."""
        provider = MockProvider()
        self.assertEqual(STANDING_N_I, 19)
        self.assertEqual(STANDING_N_090_PREFIXED, 8)
        self.assertEqual(STANDING_N_LEFTOVER, STANDING_N_I - STANDING_N_090_PREFIXED)
        self.assertEqual(STANDING_N_LEFTOVER, 11)
        planted_i = [
            ["099", "571", "076", "070", "449"],
            ["999", "090", "076", "070", "499"],
            ["069", "720", "076", "070", "073"],
            ["036", "090", "076", "070", "200"],
        ]
        planted_sides = {SIDE_IA: planted_i}
        planted_sites = (
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia2", 2),
            (SIDE_IA, "Ia3", 2),
            (SIDE_IA, "Ia4", 2),
        )
        leftover, prefixed = split_i_076_070_sites(
            planted_sides,
            planted_sites,
            GRAM2,
            PREFIXED_STEM,
        )
        self.assertEqual(leftover, (planted_sites[0], planted_sites[2]))
        self.assertEqual(prefixed, (planted_sites[1], planted_sites[3]))
        self.assertEqual(len(leftover) + len(prefixed), 4)
        self.assertEqual(
            leftover_2gram_sites_from_prefixed_3grams(
                ((SIDE_IA, "Ia2", 10), (SIDE_IA, "Ia3", 4))
            ),
            ((SIDE_IA, "Ia2", 11), (SIDE_IA, "Ia3", 5)),
        )
        off_i = CYCLE206_OFF_I_SITES
        self.assertEqual(len(off_i), CYCLE206_N_OFF_I)
        self.assertEqual(CYCLE206_N_OFF_I, 5)
        for site in off_i:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, STANDING_PREFIXED_I_SITES)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_one_distinct_and_at_least_two_leftover(self):
        """Boolean is True only when N_distinct=1 and N_leftover>=2."""
        provider = MockProvider()
        self.assertTrue(i_leftover_076_070_share_one_forward_stem(1, 2))
        self.assertTrue(i_leftover_076_070_share_one_forward_stem(1, 11))
        self.assertFalse(i_leftover_076_070_share_one_forward_stem(11, 11))
        self.assertFalse(i_leftover_076_070_share_one_forward_stem(9, 11))
        self.assertFalse(i_leftover_076_070_share_one_forward_stem(2, 11))
        self.assertFalse(i_leftover_076_070_share_one_forward_stem(1, 1))
        self.assertFalse(i_leftover_076_070_share_one_forward_stem(1, 0))
        self.assertFalse(i_leftover_076_070_share_one_forward_stem(0, 0))
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_070_share_one_forward_stem")
        self.assertFalse(STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(STANDING_N_DISTINCT_NEXT_STEMS, 11)
        self.assertEqual(STANDING_N_LEFTOVER, 11)
        self.assertEqual(provider.get_call_history(), [])

    def test_frequency_table_sorts_highest_count_first_and_skips_none(self):
        """Frequency table is count-desc; no-forward sites are omitted."""
        provider = MockProvider()
        sites = STANDING_LEFTOVER_SITES[:6]
        nxt = ("449", "076", "600", "076", None, "449")
        grams = (
            ("076", "070", "449", "449"),
            ("076", "070", "076", "670"),
            ("076", "070", "600", "090"),
            ("076", "070", "076", "011"),
            None,
            ("076", "070", "449", "072"),
        )
        table = next_stem_frequency_table(sites, nxt, grams)
        self.assertEqual(table[0][0], "449")
        self.assertEqual(table[0][1], 2)
        self.assertEqual(table[1][0], "076")
        self.assertEqual(table[1][1], 2)
        self.assertEqual(table[2][0], "600")
        self.assertEqual(table[2][1], 1)
        self.assertEqual(len(table), 3)
        self.assertEqual(
            leftover_sites_without_forward(sites, nxt),
            (sites[4],),
        )
        self.assertEqual(
            leftover_sites_with_forward(sites, nxt),
            (sites[0], sites[1], sites[2], sites[3], sites[5]),
        )
        shared = ("449",) * 6
        shared_grams = (("076", "070", "449", "449"),) * 6
        shared_table = next_stem_frequency_table(sites, shared, shared_grams)
        self.assertEqual(len(shared_table), 1)
        self.assertEqual(shared_table[0][0], "449")
        self.assertEqual(shared_table[0][1], 6)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076070ForwardStemScoreboard(unittest.TestCase):
    """Cited-fixture leftover 076 070 next-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.measured_leftover, self.measured_prefixed = split_i_076_070_sites(
            self.i_sides,
            self.i_sites,
            GRAM2,
            PREFIXED_STEM,
        )
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.next_stems = leftover_next_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.forwards = leftover_forward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.next_4grams = leftover_next_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.with_forward = leftover_sites_with_forward(
            self.leftover_sites,
            self.next_stems,
        )
        self.no_forward = leftover_sites_without_forward(
            self.leftover_sites,
            self.next_stems,
        )
        self.first_seen = group_sites_by_next_stem(
            self.leftover_sites,
            self.next_stems,
        )
        self.frequency = next_stem_frequency_table(
            self.leftover_sites,
            self.next_stems,
            self.next_4grams,
        )
        self.n_i = len(self.i_sites)
        self.n_prefixed = len(self.measured_prefixed)
        self.n_leftover = len(self.measured_leftover)
        self.n_with_forward = len(self.with_forward)
        self.n_no_forward = len(self.no_forward)
        self.n_distinct = len(self.first_seen)
        self.claim_holds = i_leftover_076_070_share_one_forward_stem(
            self.n_distinct,
            self.n_leftover,
        )

    def test_tokens_and_sites_are_cycle_206_leftover_not_retuned(self):
        """2-gram and leftover 11 stay the cycle-206/207/210/214/215 locks."""
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM2, CYCLE205_GRAM2)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.i_sites, CYCLE206_I_SITES)
        self.assertEqual(len(self.i_sites), CYCLE206_N_I)
        self.assertEqual(CYCLE206_N_I, 19)
        self.assertEqual(self.n_i, 19)
        self.assertEqual(self.measured_prefixed, STANDING_PREFIXED_I_SITES)
        self.assertEqual(self.n_prefixed, STANDING_N_090_PREFIXED)
        self.assertEqual(STANDING_N_090_PREFIXED, 8)
        self.assertEqual(self.n_prefixed, CYCLE207_N_I)
        self.assertEqual(
            leftover_2gram_sites_from_prefixed_3grams(CYCLE207_I_SITES),
            STANDING_PREFIXED_I_SITES,
        )
        self.assertEqual(self.measured_leftover, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 11)
        self.assertEqual(self.n_leftover, 11)
        self.assertEqual(self.n_i - self.n_prefixed, self.n_leftover)
        self.assertEqual(19 - 8, 11)
        prior_215 = self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"]
        self.assertEqual(prior_215["cycle"], 215)
        self.assertTrue(prior_215["i_leftover_076_070_remaining_previous_4grams_i_only"])
        self.assertTrue(CYCLE215_I_ONLY)
        self.assertEqual(prior_215["N_remaining"], CYCLE215_N_REMAINING)
        self.assertEqual(prior_215["N_remaining"], 8)
        self.assertEqual(tuple(prior_215["N_I_each"]), CYCLE215_N_I_EACH)
        self.assertEqual(tuple(prior_215["N_off_I_each"]), CYCLE215_N_OFF_I_EACH)
        self.assertEqual(prior_215["N_i_only"], 8)
        self.assertEqual(prior_215["N_not_i_only"], 0)
        prior_214 = self.survey["i_leftover_076_070_remaining_previous_stems_distinct"]
        self.assertEqual(prior_214["cycle"], 214)
        self.assertTrue(prior_214["i_leftover_076_070_remaining_previous_stems_distinct"])
        self.assertTrue(CYCLE214_CLAIM)
        self.assertEqual(prior_214["N_remaining"], CYCLE214_N_REMAINING)
        self.assertEqual(prior_214["N_remaining"], 8)
        self.assertEqual(
            prior_214["N_distinct_remaining_previous_stems"],
            CYCLE214_N_DISTINCT,
        )
        self.assertEqual(prior_214["N_distinct_remaining_previous_stems"], 8)
        prior_210 = self.survey["i_leftover_076_070_previous_stem"]
        self.assertEqual(prior_210["cycle"], 210)
        self.assertEqual(prior_210["N_leftover"], CYCLE210_N_LEFTOVER)
        self.assertEqual(prior_210["N_leftover"], 11)
        self.assertEqual(prior_210["N_distinct_previous_stems"], CYCLE210_N_DISTINCT)
        self.assertEqual(prior_210["N_distinct_previous_stems"], 9)
        self.assertFalse(prior_210["i_leftover_076_070_share_one_previous_stem"])
        self.assertFalse(CYCLE210_SHARE_ONE)
        prior_206 = self.survey["i_2gram_076_070_i_only"]
        self.assertEqual(prior_206["cycle"], 206)
        self.assertFalse(prior_206["i_2gram_076_070_i_only"])
        self.assertEqual(prior_206["N_I"], CYCLE206_N_I)
        self.assertEqual(prior_206["N_I"], 19)
        self.assertEqual(prior_206["N_off_I"], CYCLE206_N_OFF_I)
        self.assertEqual(prior_206["N_off_I"], 5)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], CYCLE171_N_I)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], CYCLE171_N_OFF_I)
        self.assertEqual(prior_171["N_off_I"], 0)
        prior_173 = self.survey["i_leftover_076_071_forward_076"]
        self.assertEqual(prior_173["cycle"], 173)
        self.assertEqual(prior_173["N_leftover"], CYCLE173_N_LEFTOVER)
        self.assertEqual(prior_173["N_leftover"], 34)
        self.assertEqual(prior_173["N_with_forward_076_071_076"], CYCLE173_N_WITH)
        self.assertEqual(prior_173["N_with_forward_076_071_076"], 5)
        self.assertTrue(prior_173["i_leftover_076_071_exactly_5_forward_076_071_076"])
        self.assertTrue(CYCLE173_CLAIM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_PREVIOUS_SIDE_CLOSED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_11_distinct_next_stems_and_claim_loses(self):
        """N_leftover=11, N_distinct=11. Claim loses. Nested 19 and 8 stay."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 19)
        self.assertEqual(self.n_prefixed, STANDING_N_090_PREFIXED)
        self.assertEqual(STANDING_N_090_PREFIXED, 8)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 11)
        if self.n_leftover != 11:
            self.fail("measured N_leftover drifted from 11")
        if self.n_i != 19 or self.n_prefixed != 8:
            self.fail("nested cycle 206/207 counts drifted; leftover cannot be trusted")
        self.assertEqual(self.n_i - self.n_prefixed, self.n_leftover)
        self.assertEqual(self.n_with_forward, STANDING_N_WITH_FORWARD)
        self.assertEqual(STANDING_N_WITH_FORWARD, 11)
        self.assertEqual(self.n_no_forward, STANDING_N_NO_FORWARD)
        self.assertEqual(STANDING_N_NO_FORWARD, 0)
        self.assertEqual(self.no_forward, STANDING_NO_FORWARD_SITES)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_NEXT_STEMS)
        self.assertEqual(STANDING_N_DISTINCT_NEXT_STEMS, 11)
        if self.n_distinct != 1:
            self.assertFalse(
                i_leftover_076_070_share_one_forward_stem(
                    self.n_distinct,
                    self.n_leftover,
                )
            )
        self.assertNotEqual(self.n_distinct, 1)
        self.assertFalse(
            i_leftover_076_070_share_one_forward_stem(
                self.n_distinct,
                self.n_leftover,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM,
        )
        self.assertFalse(STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_070_share_one_forward_stem")
        self.assertEqual(self.next_stems, STANDING_PER_SITE_NEXT_STEMS)
        self.assertEqual(self.forwards, STANDING_PER_SITE_FORWARD_3GRAMS)
        self.assertEqual(self.next_4grams, STANDING_PER_SITE_NEXT_4GRAMS)
        self.assertEqual(
            tuple(stem for stem, _sites in self.first_seen),
            STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN,
        )
        self.assertEqual(len(set(STANDING_PER_SITE_NEXT_STEMS)), 11)
        self.assertEqual(len(STANDING_NEXT_STEM_FREQUENCY), 11)
        self.assertEqual(STANDING_N_HAPAX_NEXT_STEMS, 11)
        hapax = tuple(row for row in self.frequency if row[1] == 1)
        self.assertEqual(len(hapax), STANDING_N_HAPAX_NEXT_STEMS)
        self.assertEqual(
            sum(count for _stem, count, _sites, _grams in self.frequency),
            11,
        )
        for site in STANDING_PREFIXED_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        for site in CYCLE206_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_999_090_076_071))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE173)
        self.assertFalse(STANDING_SAME_AS_CYCLE210)
        self.assertFalse(STANDING_SAME_AS_CYCLE215)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_frequency_table_and_per_site_next_stems_match_fixtures(self):
        """Each leftover site has a distinct next stem; 076 070 X is hapax."""
        self.assertEqual(self.frequency, STANDING_NEXT_STEM_FREQUENCY)
        counts = [row[1] for row in self.frequency]
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertTrue(all(count == 1 for count in counts))
        self.assertEqual(len(counts), 11)
        for site, nxt, fwd3, nxt4 in zip(
            STANDING_LEFTOVER_SITES,
            STANDING_PER_SITE_NEXT_STEMS,
            STANDING_PER_SITE_FORWARD_3GRAMS,
            STANDING_PER_SITE_NEXT_4GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertLess(index + STANDING_N2, len(stems))
            self.assertEqual(stems[index + STANDING_N2], nxt)
            self.assertEqual(site_next_stem(stems, index, GRAM2), nxt)
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), fwd3)
            self.assertEqual(fwd3, ("076", "070", nxt))
            self.assertNotEqual(fwd3[:3], PREFIXED_3GRAM)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), nxt4)
            self.assertEqual(nxt4[:3], fwd3)
            self.assertEqual(nxt4[:2], GRAM2)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, STANDING_PREFIXED_I_SITES)
        for site in STANDING_PREFIXED_I_SITES:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(stems[index - 1], PREFIXED_STEM)
            self.assertEqual(
                tuple(stems[index - 1 : index + STANDING_N2]),
                PREFIXED_3GRAM,
            )
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        for stem, count, sites, grams in STANDING_NEXT_STEM_FREQUENCY:
            self.assertEqual(len(sites), count)
            self.assertEqual(len(grams), count)
            for site, gram4 in zip(sites, grams, strict=True):
                self.assertEqual(gram4[2], stem)
                self.assertEqual(gram4[:2], GRAM2)
                self.assertIn(site, STANDING_LEFTOVER_SITES)
        self.assertEqual(IA_LINE_NAMES[0], "Ia1")
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_215_214_210_206_and_171_scoreboards_still_compute(self):
        """Cycle 215 8/8, 214 8/8, 210 11/9, 206 19/5, 171 43/0 stay."""
        prior_215 = TestMamariILeftover076070RemainingPrevious4gramsIOnlyScoreboard()
        prior_215.setUp()
        prior_215.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_215.test_survey_matches_computed_lock()
        self.assertEqual(prior_215.n_i, CYCLE215_N_I_EACH)
        self.assertEqual(prior_215.n_off_i, CYCLE215_N_OFF_I_EACH)
        self.assertTrue(prior_215.claim_holds)
        self.assertTrue(CYCLE215_I_ONLY)
        self.assertEqual(CYCLE215_N_REMAINING, 8)
        self.assertEqual(sum(CYCLE215_N_I_EACH), 8)
        self.assertEqual(sum(CYCLE215_N_OFF_I_EACH), 0)
        prior_214 = TestMamariILeftover076070RemainingPreviousStemsDistinctScoreboard()
        prior_214.setUp()
        prior_214.test_counts_8_remaining_all_distinct_and_claim_holds()
        prior_214.test_survey_matches_computed_lock()
        self.assertEqual(prior_214.n_remaining, 8)
        self.assertEqual(prior_214.n_distinct, 8)
        self.assertEqual(prior_214.n_leftover, 11)
        self.assertTrue(prior_214.claim_holds)
        self.assertEqual(CYCLE214_N_REMAINING, 8)
        self.assertEqual(CYCLE214_N_DISTINCT, 8)
        prior_210 = TestMamariILeftover076070PreviousStemScoreboard()
        prior_210.setUp()
        prior_210.test_counts_9_distinct_previous_stems_and_claim_loses()
        prior_210.test_survey_matches_computed_lock()
        self.assertEqual(prior_210.n_leftover, CYCLE210_N_LEFTOVER)
        self.assertEqual(prior_210.n_leftover, 11)
        self.assertEqual(prior_210.n_distinct, CYCLE210_N_DISTINCT)
        self.assertEqual(prior_210.n_distinct, 9)
        self.assertFalse(prior_210.claim_holds)
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        self.assertEqual(prior_206.i_hits, 19)
        self.assertEqual(prior_206.off_i_hits, 5)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        prior_173 = TestMamariILeftover076071Forward076Scoreboard()
        prior_173.setUp()
        prior_173.test_counts_5_of_34_and_hypothesis_n_5_holds()
        prior_173.test_survey_matches_computed_lock()
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-216 leftover next-stem lock."""
        lock = self.survey["i_leftover_076_070_forward_stem"]
        self.assertEqual(lock["cycle"], 216)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_one_forward_stem"])
        self.assertEqual(
            lock["hypothesis_share_one_forward_stem"],
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 19)
        self.assertEqual(lock["N_090_prefixed"], STANDING_N_090_PREFIXED)
        self.assertEqual(lock["N_090_prefixed"], 8)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 11)
        self.assertEqual(lock["N_leftover"], lock["N_I"] - lock["N_090_prefixed"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["prefixed_i_sites"]),
            STANDING_PREFIXED_I_SITES,
        )
        self.assertEqual(lock["N_with_forward"], STANDING_N_WITH_FORWARD)
        self.assertEqual(lock["N_with_forward"], 11)
        self.assertEqual(lock["N_no_forward"], STANDING_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(lock["no_forward_sites"], [])
        self.assertEqual(
            lock["N_distinct_next_stems"],
            STANDING_N_DISTINCT_NEXT_STEMS,
        )
        self.assertEqual(lock["N_distinct_next_stems"], 11)
        self.assertEqual(
            tuple(lock["distinct_next_stems"]),
            STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN,
        )
        self.assertEqual(
            tuple(lock["per_site_next_stems"]),
            STANDING_PER_SITE_NEXT_STEMS,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_FORWARD_3GRAMS],
            lock["per_site_forward_3grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_NEXT_4GRAMS],
            lock["per_site_next_4grams"],
        )
        self.assertEqual(
            lock["next_stem_frequency"],
            next_stem_frequency_rows(STANDING_NEXT_STEM_FREQUENCY),
        )
        self.assertEqual(len(lock["next_stem_frequency"]), 11)
        self.assertEqual(lock["next_stem_frequency"][0]["next_stem"], "449")
        self.assertEqual(lock["next_stem_frequency"][0]["count"], 1)
        self.assertEqual(lock["N_hapax_next_stems"], STANDING_N_HAPAX_NEXT_STEMS)
        self.assertEqual(lock["N_hapax_next_stems"], 11)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_076_070_share_one_forward_stem"])
        self.assertEqual(
            lock["i_leftover_076_070_share_one_forward_stem"],
            STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle173"])
        self.assertFalse(lock["same_as_cycle210"])
        self.assertFalse(lock["same_as_cycle215"])
        self.assertTrue(lock["090_prefixed_does_not_count"])
        self.assertTrue(lock["off_i_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["previous_side_closed"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_076_070_remaining_previous_4grams_i_only_unchanged"]
        )
        self.assertTrue(
            lock["standing_i_leftover_076_070_remaining_previous_stems_distinct_unchanged"]
        )
        self.assertTrue(lock["standing_i_leftover_076_070_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"]["cycle"],
            215,
        )
        self.assertTrue(
            self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"][
                "i_leftover_076_070_remaining_previous_4grams_i_only"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"][
                "N_i_only"
            ],
            8,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_4grams_i_only"][
                "N_not_i_only"
            ],
            0,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_stems_distinct"]["cycle"],
            214,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_stems_distinct"][
                "N_remaining"
            ],
            8,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_remaining_previous_stems_distinct"][
                "N_distinct_remaining_previous_stems"
            ],
            8,
        )
        self.assertEqual(self.survey["i_leftover_076_070_previous_stem"]["cycle"], 210)
        self.assertEqual(self.survey["i_leftover_076_070_previous_stem"]["N_leftover"], 11)
        self.assertEqual(
            self.survey["i_leftover_076_070_previous_stem"]["N_distinct_previous_stems"],
            9,
        )
        self.assertFalse(
            self.survey["i_leftover_076_070_previous_stem"][
                "i_leftover_076_070_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_076_071_forward_076"]["cycle"], 173)
        self.assertEqual(
            self.survey["i_leftover_076_071_forward_076"]["N_with_forward_076_071_076"],
            5,
        )
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"][
                "i_leftover_n4_exactly_1_contain_076_070"
            ]
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


class TestMamariILeftover076070ForwardStemImageSnapshot(unittest.TestCase):
    """Cycle 216 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
