"""I's cycle-207 leftover 3-gram forward-stem lock.

Cycle 218 text-search lock. Uses already-vendored A–V and the
cycle-207 I sites of 3-gram 090 076 070 (the leftover for this
cycle: all I 090 076 070 sites). Does not retune that 3-gram,
those 8 I sites, the leftover n=4 set, or the already-closed
leftover 076 070 that is not 090 076 070. Does not vendor a
new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

For each I 090 076 070 site, record the next token immediately
after 090 076 070 when it exists (forward 4-gram 090 076 070 X,
and next 5-gram 090 076 070 X Y when it exists). End-of-line
is no-forward. Nested-assert N_I(090 076 070)=8 from cycle 207;
do not assume 8. Cycle 217 leftover 076 070 forward 4-grams
I-only hapax 1/0 x11, cycle 209 extra 090 076 070 4-grams
I-only hapax 1/0 x3, cycle 208 leftover 4-gram 999 090 076 070
I-only 5/0, cycle 207 090 076 070 8/1 loss, and cycle 171
076 071 I-only 43/0 stay. Off-I 090 076 070 (Ta9[2]
059 090 076 070) does not count. Leftover 076 070 that is not
090 076 070 is a different leftover (already closed, cycles
210–217). 090 076 071 is a different 3-gram.

Claim that can lose:
i_090_076_070_share_one_forward_stem. True only if
N_distinct_next_stems=1 and N_I>=2. Measured: N_I=8,
N_with_forward=8, N_no_forward=0, N_distinct_next_stems=8
(all hapax next stems 499/200/600/027/532/071/073/000). The
claim is false. Same claim-shape as cycle 216 (leftover
076 070 share-one-forward-stem lost, N_distinct=11). Do not
assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_honolulu_vendor_scoreboard import (
    SIDE_TA,
    TA_LINE_NAMES,
    load_t_sides,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3,
    STANDING_EXTRA_I_SITES,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_LEFTOVER_3GRAM_SITES,
    STANDING_N_EXTRA,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_INSIDE_LEFTOVER,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    STANDING_OFF_I_PREVIOUS_4GRAM,
    STANDING_OFF_I_SITES as CYCLE207_OFF_I_SITES,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
)
from tests.test_mamari_i_4gram_999_090_076_070_i_only_scoreboard import (
    GRAM4 as CYCLE208_GRAM4,
    STANDING_I_4GRAM_999_090_076_070_I_ONLY as CYCLE208_I_ONLY,
    STANDING_N_I as CYCLE208_N_I,
    STANDING_N_OFF_I as CYCLE208_N_OFF_I,
    TestMamariI4gram999090076070IOnlyScoreboard,
)
from tests.test_mamari_i_extra_090_076_070_4grams_i_only_scoreboard import (
    STANDING_I_EXTRA_090_076_070_4GRAMS_I_ONLY as CYCLE209_I_ONLY,
    STANDING_N_I_036 as CYCLE209_N_I_036,
    STANDING_N_I_161 as CYCLE209_N_I_161,
    STANDING_N_I_400 as CYCLE209_N_I_400,
    STANDING_N_OFF_I_036 as CYCLE209_N_OFF_I_036,
    STANDING_N_OFF_I_161 as CYCLE209_N_OFF_I_161,
    STANDING_N_OFF_I_400 as CYCLE209_N_OFF_I_400,
    TestMamariIExtra0900760704gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_forward_4grams_i_only_scoreboard import (
    STANDING_I_LEFTOVER_076_070_FORWARD_4GRAMS_I_ONLY as CYCLE217_I_ONLY,
    STANDING_N_I_EACH as CYCLE217_N_I_EACH,
    STANDING_N_LEFTOVER as CYCLE217_N_LEFTOVER,
    STANDING_N_OFF_I_EACH as CYCLE217_N_OFF_I_EACH,
    TestMamariILeftover076070Forward4gramsIOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_forward_stem_scoreboard import (
    STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM as CYCLE216_SHARE_ONE,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE216_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE216_N_LEFTOVER,
    leftover_next_stems as leftover_2gram_next_stems,
    site_next_stem as site_2gram_next_stem,
    TestMamariILeftover076070ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    group_sites_by_previous_stem,
    leftover_sites_with_backward,
    leftover_sites_without_backward,
    previous_stem_frequency_table,
)
from tests.test_mamari_i_leftover_n4_076_070_scoreboard import (
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
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N5 = 5
STANDING_N_I = 8
STANDING_I_SITES = CYCLE207_I_SITES
STANDING_N_WITH_FORWARD = 8
STANDING_N_NO_FORWARD = 0
STANDING_NO_FORWARD_SITES = ()
STANDING_N_DISTINCT_NEXT_STEMS = 8
STANDING_N_HAPAX_NEXT_STEMS = 8
STANDING_PER_SITE_NEXT_STEMS = (
    "499",
    "200",
    "600",
    "027",
    "532",
    "071",
    "073",
    "000",
)
STANDING_PER_SITE_FORWARD_4GRAMS = tuple(
    ("090", "076", "070", stem) for stem in STANDING_PER_SITE_NEXT_STEMS
)
STANDING_PER_SITE_NEXT_5GRAMS = (
    ("090", "076", "070", "499", "090"),
    ("090", "076", "070", "200", "069"),
    ("090", "076", "070", "600", "021"),
    ("090", "076", "070", "027", "141"),
    ("090", "076", "070", "532", "084"),
    ("090", "076", "070", "071", "600"),
    ("090", "076", "070", "073", "006"),
    ("090", "076", "070", "000", "205"),
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
        STANDING_I_SITES,
        STANDING_PER_SITE_FORWARD_4GRAMS,
        strict=True,
    )
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_090_076_070_share_one_forward_stem"
STANDING_I_090_076_070_SHARE_ONE_FORWARD_STEM = False
STANDING_RESULT = "i_090_076_070_forward_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE216 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE216 = True
STANDING_OFF_I_DOES_NOT_COUNT = True
STANDING_LEFTOVER_076_070_NOT_090_DOES_NOT_COUNT = True
STANDING_090_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_076_070_SIDES_CLOSED = True


def site_next_stem(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> str | None:
    """Next stem X after 090 076 070; None at end-of-line or mismatch."""
    n3 = len(gram3)
    if tuple(stems[index : index + n3]) != gram3:
        return None
    next_index = index + n3
    if next_index >= len(stems):
        return None
    return stems[next_index]


def site_forward_4gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """090 076 070 X if a next stem exists; None at end-of-line."""
    n3 = len(gram3)
    if tuple(stems[index : index + n3]) != gram3:
        return None
    next_index = index + n3
    if next_index >= len(stems):
        return None
    return tuple(stems[index : index + n3 + 1])


def site_next_5gram(
    stems: list[str],
    index: int,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...] | None:
    """090 076 070 X Y if two next stems exist; None otherwise."""
    n3 = len(gram3)
    if tuple(stems[index : index + n3]) != gram3:
        return None
    if index + n3 + 1 >= len(stems):
        return None
    return tuple(stems[index : index + n3 + 2])


def i_090_076_070_next_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str | None, ...]:
    """Per-site next stem or None for the locked I 090 076 070 sites."""
    return tuple(
        site_next_stem(line_stems_for_site(i_sides, site), site[2], gram3)
        for site in sites
    )


def i_090_076_070_forward_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site forward 4-gram or None for the locked I sites."""
    return tuple(
        site_forward_4gram(line_stems_for_site(i_sides, site), site[2], gram3)
        for site in sites
    )


def i_090_076_070_next_5grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site next 5-gram or None for the locked I sites."""
    return tuple(
        site_next_5gram(line_stems_for_site(i_sides, site), site[2], gram3)
        for site in sites
    )


def i_sites_with_forward(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """I 090 076 070 sites that have a next stem."""
    return leftover_sites_with_backward(sites, next_stems)


def i_sites_without_forward(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """I 090 076 070 sites that are end-of-line (no-forward)."""
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
    forward_4grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Next-stem frequency: highest count first, then first-seen."""
    return previous_stem_frequency_table(sites, next_stems, forward_4grams)


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
                "i_sites": [list(site) for site in sites],
                "forward_4grams": [list(gram) for gram in grams],
            }
        )
    return rows


def i_090_076_070_share_one_forward_stem(
    n_distinct_next_stems: int,
    n_i: int,
) -> bool:
    """True iff N_distinct_next_stems=1 and N_I>=2."""
    return n_distinct_next_stems == 1 and n_i >= 2


class TestI090076070ForwardStemHelpers(unittest.TestCase):
    """Helpers on I 090 076 070 next stems. No CV, no LLM."""

    def test_next_requires_stem_after_3gram(self):
        """A next stem is a 4-gram; end-of-line is no-forward."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("090", "076", "070"))
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N3 + 1)
        self.assertEqual(STANDING_N5, STANDING_N3 + 2)
        has_499 = ["999", "090", "076", "070", "499", "090"]
        self.assertEqual(site_next_stem(has_499, 1, GRAM3), "499")
        self.assertEqual(
            site_forward_4gram(has_499, 1, GRAM3),
            ("090", "076", "070", "499"),
        )
        self.assertEqual(
            site_next_5gram(has_499, 1, GRAM3),
            ("090", "076", "070", "499", "090"),
        )
        has_000 = ["999", "090", "076", "070", "000", "205"]
        self.assertEqual(site_next_stem(has_000, 1, GRAM3), "000")
        self.assertEqual(
            site_forward_4gram(has_000, 1, GRAM3),
            ("090", "076", "070", "000"),
        )
        end_of_line = ["999", "090", "076", "070"]
        self.assertIsNone(site_next_stem(end_of_line, 1, GRAM3))
        self.assertIsNone(site_forward_4gram(end_of_line, 1, GRAM3))
        self.assertIsNone(site_next_5gram(end_of_line, 1, GRAM3))
        only_one_next = ["090", "076", "070", "200"]
        self.assertEqual(site_next_stem(only_one_next, 0, GRAM3), "200")
        self.assertEqual(
            site_forward_4gram(only_one_next, 0, GRAM3),
            ("090", "076", "070", "200"),
        )
        self.assertIsNone(site_next_5gram(only_one_next, 0, GRAM3))
        mismatch_071 = ["090", "076", "071", "076"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM3))
        self.assertIsNone(site_forward_4gram(mismatch_071, 0, GRAM3))
        leftover_not_090 = ["099", "571", "076", "070", "449"]
        self.assertIsNone(site_next_stem(leftover_not_090, 2, GRAM3))
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_076_070_NOT_090_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_one_distinct_and_at_least_two_i(self):
        """Boolean is True only when N_distinct=1 and N_I>=2."""
        provider = MockProvider()
        self.assertTrue(i_090_076_070_share_one_forward_stem(1, 2))
        self.assertTrue(i_090_076_070_share_one_forward_stem(1, 8))
        self.assertFalse(i_090_076_070_share_one_forward_stem(8, 8))
        self.assertFalse(i_090_076_070_share_one_forward_stem(11, 11))
        self.assertFalse(i_090_076_070_share_one_forward_stem(2, 8))
        self.assertFalse(i_090_076_070_share_one_forward_stem(1, 1))
        self.assertFalse(i_090_076_070_share_one_forward_stem(1, 0))
        self.assertFalse(i_090_076_070_share_one_forward_stem(0, 0))
        self.assertEqual(STANDING_CLAIM, "i_090_076_070_share_one_forward_stem")
        self.assertFalse(STANDING_I_090_076_070_SHARE_ONE_FORWARD_STEM)
        self.assertNotEqual(
            STANDING_I_090_076_070_SHARE_ONE_FORWARD_STEM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(STANDING_N_DISTINCT_NEXT_STEMS, 8)
        self.assertEqual(STANDING_N_I, 8)
        self.assertEqual(provider.get_call_history(), [])

    def test_frequency_table_sorts_highest_count_first_and_skips_none(self):
        """Frequency table is count-desc; no-forward sites are omitted."""
        provider = MockProvider()
        sites = STANDING_I_SITES[:6]
        nxt = ("499", "071", "600", "071", None, "499")
        grams = (
            ("090", "076", "070", "499"),
            ("090", "076", "070", "071"),
            ("090", "076", "070", "600"),
            ("090", "076", "070", "071"),
            None,
            ("090", "076", "070", "499"),
        )
        table = next_stem_frequency_table(sites, nxt, grams)
        self.assertEqual(table[0][0], "499")
        self.assertEqual(table[0][1], 2)
        self.assertEqual(table[1][0], "071")
        self.assertEqual(table[1][1], 2)
        self.assertEqual(table[2][0], "600")
        self.assertEqual(table[2][1], 1)
        self.assertEqual(len(table), 3)
        self.assertEqual(i_sites_without_forward(sites, nxt), (sites[4],))
        self.assertEqual(
            i_sites_with_forward(sites, nxt),
            (sites[0], sites[1], sites[2], sites[3], sites[5]),
        )
        shared = ("499",) * 6
        shared_grams = (("090", "076", "070", "499"),) * 6
        shared_table = next_stem_frequency_table(sites, shared, shared_grams)
        self.assertEqual(len(shared_table), 1)
        self.assertEqual(shared_table[0][0], "499")
        self.assertEqual(shared_table[0][1], 6)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI090076070ForwardStemScoreboard(unittest.TestCase):
    """Cited-fixture I 090 076 070 next-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM3, self.i_sides)
        self.next_stems = i_090_076_070_next_stems(
            self.i_sides,
            self.i_sites,
            GRAM3,
        )
        self.forwards = i_090_076_070_forward_4grams(
            self.i_sides,
            self.i_sites,
            GRAM3,
        )
        self.next_5grams = i_090_076_070_next_5grams(
            self.i_sides,
            self.i_sites,
            GRAM3,
        )
        self.with_forward = i_sites_with_forward(self.i_sites, self.next_stems)
        self.no_forward = i_sites_without_forward(self.i_sites, self.next_stems)
        self.first_seen = group_sites_by_next_stem(self.i_sites, self.next_stems)
        self.frequency = next_stem_frequency_table(
            self.i_sites,
            self.next_stems,
            self.forwards,
        )
        self.n_i = len(self.i_sites)
        self.n_with_forward = len(self.with_forward)
        self.n_no_forward = len(self.no_forward)
        self.n_distinct = len(self.first_seen)
        self.claim_holds = i_090_076_070_share_one_forward_stem(
            self.n_distinct,
            self.n_i,
        )

    def test_tokens_and_sites_are_cycle_207_i_sites_not_retuned(self):
        """3-gram and 8 I sites stay the cycle-207 lock. Nested 8 must hold."""
        self.assertEqual(GRAM3, ("090", "076", "070"))
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(self.i_sites, CYCLE207_I_SITES)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(len(self.i_sites), CYCLE207_N_I)
        self.assertEqual(CYCLE207_N_I, 8)
        self.assertEqual(self.n_i, 8)
        if self.n_i != 8:
            self.fail("nested cycle 207 N_I drifted from 8")
        self.assertEqual(len(STANDING_LEFTOVER_3GRAM_SITES), STANDING_N_INSIDE_LEFTOVER)
        self.assertEqual(STANDING_N_INSIDE_LEFTOVER, 5)
        self.assertEqual(len(STANDING_EXTRA_I_SITES), STANDING_N_EXTRA)
        self.assertEqual(STANDING_N_EXTRA, 3)
        self.assertEqual(STANDING_N_INSIDE_LEFTOVER + STANDING_N_EXTRA, 8)
        prior_217 = self.survey["i_leftover_076_070_forward_4grams_i_only"]
        self.assertEqual(prior_217["cycle"], 217)
        self.assertTrue(prior_217["i_leftover_076_070_forward_4grams_i_only"])
        self.assertTrue(CYCLE217_I_ONLY)
        self.assertEqual(prior_217["N_leftover"], CYCLE217_N_LEFTOVER)
        self.assertEqual(prior_217["N_leftover"], 11)
        self.assertEqual(tuple(prior_217["N_I_each"]), CYCLE217_N_I_EACH)
        self.assertEqual(tuple(prior_217["N_off_I_each"]), CYCLE217_N_OFF_I_EACH)
        self.assertEqual(prior_217["N_i_only"], 11)
        self.assertEqual(prior_217["N_not_i_only"], 0)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], CYCLE207_N_I)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], CYCLE207_N_OFF_I)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertEqual(
            tuple(tuple(row) for row in prior_207["i_sites"]),
            STANDING_I_SITES,
        )
        prior_208 = self.survey["i_4gram_999_090_076_070_i_only"]
        self.assertEqual(prior_208["cycle"], 208)
        self.assertTrue(prior_208["i_4gram_999_090_076_070_i_only"])
        self.assertTrue(CYCLE208_I_ONLY)
        self.assertEqual(prior_208["N_I"], CYCLE208_N_I)
        self.assertEqual(prior_208["N_I"], 5)
        self.assertEqual(prior_208["N_off_I"], CYCLE208_N_OFF_I)
        self.assertEqual(prior_208["N_off_I"], 0)
        prior_209 = self.survey["i_extra_090_076_070_4grams_i_only"]
        self.assertEqual(prior_209["cycle"], 209)
        self.assertTrue(prior_209["i_extra_090_076_070_4grams_i_only"])
        self.assertTrue(CYCLE209_I_ONLY)
        self.assertEqual(prior_209["N_I_036"], CYCLE209_N_I_036)
        self.assertEqual(prior_209["N_off_I_036"], CYCLE209_N_OFF_I_036)
        self.assertEqual(prior_209["N_I_161"], CYCLE209_N_I_161)
        self.assertEqual(prior_209["N_off_I_161"], CYCLE209_N_OFF_I_161)
        self.assertEqual(prior_209["N_I_400"], CYCLE209_N_I_400)
        self.assertEqual(prior_209["N_off_I_400"], CYCLE209_N_OFF_I_400)
        self.assertEqual(prior_209["N_I_036"], 1)
        self.assertEqual(prior_209["N_off_I_036"], 0)
        self.assertEqual(prior_209["N_I_161"], 1)
        self.assertEqual(prior_209["N_off_I_161"], 0)
        self.assertEqual(prior_209["N_I_400"], 1)
        self.assertEqual(prior_209["N_off_I_400"], 0)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertEqual(prior_171["N_I"], CYCLE171_N_I)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], CYCLE171_N_OFF_I)
        self.assertEqual(prior_171["N_off_I"], 0)
        prior_216 = self.survey["i_leftover_076_070_forward_stem"]
        self.assertEqual(prior_216["cycle"], 216)
        self.assertEqual(prior_216["N_leftover"], CYCLE216_N_LEFTOVER)
        self.assertEqual(prior_216["N_leftover"], 11)
        self.assertEqual(prior_216["N_distinct_next_stems"], CYCLE216_N_DISTINCT)
        self.assertEqual(prior_216["N_distinct_next_stems"], 11)
        self.assertFalse(prior_216["i_leftover_076_070_share_one_forward_stem"])
        self.assertFalse(CYCLE216_SHARE_ONE)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_076_070_SIDES_CLOSED)
        unused = leftover_2gram_next_stems
        self.assertTrue(callable(unused))
        self.assertTrue(callable(site_2gram_next_stem))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_8_distinct_next_stems_and_claim_loses(self):
        """N_I=8, N_distinct=8. Claim loses. Nested 8 must not drift."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 8)
        if self.n_i != 8:
            self.fail("measured N_I drifted from 8")
        self.assertEqual(self.n_with_forward, STANDING_N_WITH_FORWARD)
        self.assertEqual(STANDING_N_WITH_FORWARD, 8)
        self.assertEqual(self.n_no_forward, STANDING_N_NO_FORWARD)
        self.assertEqual(STANDING_N_NO_FORWARD, 0)
        self.assertEqual(self.no_forward, STANDING_NO_FORWARD_SITES)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_NEXT_STEMS)
        self.assertEqual(STANDING_N_DISTINCT_NEXT_STEMS, 8)
        if self.n_distinct != 1:
            self.assertFalse(
                i_090_076_070_share_one_forward_stem(
                    self.n_distinct,
                    self.n_i,
                )
            )
        self.assertNotEqual(self.n_distinct, 1)
        self.assertFalse(
            i_090_076_070_share_one_forward_stem(
                self.n_distinct,
                self.n_i,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_090_076_070_SHARE_ONE_FORWARD_STEM,
        )
        self.assertFalse(STANDING_I_090_076_070_SHARE_ONE_FORWARD_STEM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(STANDING_CLAIM, "i_090_076_070_share_one_forward_stem")
        self.assertEqual(self.next_stems, STANDING_PER_SITE_NEXT_STEMS)
        self.assertEqual(self.forwards, STANDING_PER_SITE_FORWARD_4GRAMS)
        self.assertEqual(self.next_5grams, STANDING_PER_SITE_NEXT_5GRAMS)
        self.assertEqual(
            tuple(stem for stem, _sites in self.first_seen),
            STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN,
        )
        self.assertEqual(len(set(STANDING_PER_SITE_NEXT_STEMS)), 8)
        self.assertEqual(len(STANDING_NEXT_STEM_FREQUENCY), 8)
        self.assertEqual(STANDING_N_HAPAX_NEXT_STEMS, 8)
        hapax = tuple(row for row in self.frequency if row[1] == 1)
        self.assertEqual(len(hapax), STANDING_N_HAPAX_NEXT_STEMS)
        self.assertEqual(
            sum(count for _stem, count, _sites, _grams in self.frequency),
            8,
        )
        for site in CYCLE207_OFF_I_SITES:
            self.assertNotIn(site, STANDING_I_SITES)
        self.assertEqual(CYCLE207_OFF_I_SITES, ((SIDE_TA, "Ta9", 2),))
        self.assertNotEqual(GRAM3, CYCLE171_GRAM2)
        self.assertNotEqual(GRAM3, CYCLE195_GRAM3)
        self.assertEqual(CYCLE195_GRAM3, ("090", "076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_999_090_076_071))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_700_076_076_053))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE216)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE216)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_076_070_NOT_090_DOES_NOT_COUNT)
        self.assertTrue(STANDING_090_076_071_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_frequency_table_and_per_site_next_stems_match_fixtures(self):
        """Each I site has a distinct next stem; 090 076 070 X is hapax."""
        self.assertEqual(self.frequency, STANDING_NEXT_STEM_FREQUENCY)
        counts = [row[1] for row in self.frequency]
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertTrue(all(count == 1 for count in counts))
        self.assertEqual(len(counts), 8)
        for site, nxt, fwd4, nxt5 in zip(
            STANDING_I_SITES,
            STANDING_PER_SITE_NEXT_STEMS,
            STANDING_PER_SITE_FORWARD_4GRAMS,
            STANDING_PER_SITE_NEXT_5GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertLess(index + STANDING_N3, len(stems))
            self.assertEqual(stems[index + STANDING_N3], nxt)
            self.assertEqual(site_next_stem(stems, index, GRAM3), nxt)
            self.assertEqual(site_forward_4gram(stems, index, GRAM3), fwd4)
            self.assertEqual(fwd4, ("090", "076", "070", nxt))
            self.assertEqual(site_next_5gram(stems, index, GRAM3), nxt5)
            self.assertEqual(nxt5[:4], fwd4)
            self.assertEqual(nxt5[:3], GRAM3)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, CYCLE207_OFF_I_SITES)
        t_sides = load_t_sides()
        off_side, off_line, off_index = CYCLE207_OFF_I_SITES[0]
        off_stems = t_sides[off_side][TA_LINE_NAMES.index(off_line)]
        self.assertEqual(
            tuple(off_stems[off_index : off_index + STANDING_N3]),
            GRAM3,
        )
        self.assertEqual(
            tuple(off_stems[off_index - 1 : off_index + STANDING_N3]),
            STANDING_OFF_I_PREVIOUS_4GRAM,
        )
        self.assertEqual(STANDING_OFF_I_PREVIOUS_4GRAM, ("059", "090", "076", "070"))
        self.assertNotIn(CYCLE207_OFF_I_SITES[0], STANDING_I_SITES)
        for stem, count, sites, grams in STANDING_NEXT_STEM_FREQUENCY:
            self.assertEqual(len(sites), count)
            self.assertEqual(len(grams), count)
            for site, gram4 in zip(sites, grams, strict=True):
                self.assertEqual(gram4[3], stem)
                self.assertEqual(gram4[:3], GRAM3)
                self.assertIn(site, STANDING_I_SITES)
        for leftover_site in STANDING_LEFTOVER_3GRAM_SITES:
            self.assertIn(leftover_site, STANDING_I_SITES)
        for extra_site in STANDING_EXTRA_I_SITES:
            self.assertIn(extra_site, STANDING_I_SITES)
        self.assertEqual(CYCLE208_GRAM4, ("999", "090", "076", "070"))
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_217_207_208_209_and_171_scoreboards_still_compute(self):
        """Cycle 217 11/11, 207 8/1, 208 5/0, 209 1/0 x3, 171 43/0 stay."""
        prior_217 = TestMamariILeftover076070Forward4gramsIOnlyScoreboard()
        prior_217.setUp()
        prior_217.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_217.test_survey_matches_computed_lock()
        self.assertEqual(prior_217.n_i, CYCLE217_N_I_EACH)
        self.assertEqual(prior_217.n_off_i, CYCLE217_N_OFF_I_EACH)
        self.assertTrue(prior_217.claim_holds)
        self.assertTrue(CYCLE217_I_ONLY)
        self.assertEqual(CYCLE217_N_LEFTOVER, 11)
        self.assertEqual(sum(CYCLE217_N_I_EACH), 11)
        self.assertEqual(sum(CYCLE217_N_OFF_I_EACH), 0)
        if sum(CYCLE217_N_I_EACH) != 11 or sum(CYCLE217_N_OFF_I_EACH) != 0:
            self.fail("nested cycle 217 leftover forward 4-grams 11/11 drifted")
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 8/1 drifted")
        prior_208 = TestMamariI4gram999090076070IOnlyScoreboard()
        prior_208.setUp()
        prior_208.test_4gram_is_zero_off_i_and_i_only()
        prior_208.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE208_N_I, 5)
        self.assertEqual(CYCLE208_N_OFF_I, 0)
        self.assertTrue(CYCLE208_I_ONLY)
        if CYCLE208_N_I != 5 or CYCLE208_N_OFF_I != 0:
            self.fail("nested cycle 208 5/0 drifted")
        prior_209 = TestMamariIExtra0900760704gramsIOnlyScoreboard()
        prior_209.setUp()
        prior_209.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_209.test_survey_matches_computed_lock()
        self.assertTrue(prior_209.claim_holds)
        self.assertTrue(CYCLE209_I_ONLY)
        self.assertEqual(CYCLE209_N_I_036, 1)
        self.assertEqual(CYCLE209_N_OFF_I_036, 0)
        self.assertEqual(CYCLE209_N_I_161, 1)
        self.assertEqual(CYCLE209_N_OFF_I_161, 0)
        self.assertEqual(CYCLE209_N_I_400, 1)
        self.assertEqual(CYCLE209_N_OFF_I_400, 0)
        if (
            CYCLE209_N_I_036 != 1
            or CYCLE209_N_OFF_I_036 != 0
            or CYCLE209_N_I_161 != 1
            or CYCLE209_N_OFF_I_161 != 0
            or CYCLE209_N_I_400 != 1
            or CYCLE209_N_OFF_I_400 != 0
        ):
            self.fail("nested cycle 209 extra 1/0 x3 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_216 = TestMamariILeftover076070ForwardStemScoreboard()
        prior_216.setUp()
        prior_216.test_counts_11_distinct_next_stems_and_claim_loses()
        prior_216.test_survey_matches_computed_lock()
        self.assertEqual(prior_216.n_leftover, CYCLE216_N_LEFTOVER)
        self.assertEqual(prior_216.n_distinct, CYCLE216_N_DISTINCT)
        self.assertFalse(prior_216.claim_holds)
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-218 I next-stem lock."""
        lock = self.survey["i_090_076_070_forward_stem"]
        self.assertEqual(lock["cycle"], 218)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_one_forward_stem"])
        self.assertEqual(
            lock["hypothesis_share_one_forward_stem"],
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["n5"], STANDING_N5)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 8)
        self.assertEqual(lock["N_I"], CYCLE207_N_I)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_with_forward"], STANDING_N_WITH_FORWARD)
        self.assertEqual(lock["N_with_forward"], 8)
        self.assertEqual(lock["N_no_forward"], STANDING_N_NO_FORWARD)
        self.assertEqual(lock["N_no_forward"], 0)
        self.assertEqual(lock["no_forward_sites"], [])
        self.assertEqual(
            lock["N_distinct_next_stems"],
            STANDING_N_DISTINCT_NEXT_STEMS,
        )
        self.assertEqual(lock["N_distinct_next_stems"], 8)
        self.assertEqual(
            tuple(lock["distinct_next_stems"]),
            STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN,
        )
        self.assertEqual(
            tuple(lock["per_site_next_stems"]),
            STANDING_PER_SITE_NEXT_STEMS,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_FORWARD_4GRAMS],
            lock["per_site_forward_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_PER_SITE_NEXT_5GRAMS],
            lock["per_site_next_5grams"],
        )
        self.assertEqual(
            lock["next_stem_frequency"],
            next_stem_frequency_rows(STANDING_NEXT_STEM_FREQUENCY),
        )
        self.assertEqual(len(lock["next_stem_frequency"]), 8)
        self.assertEqual(lock["next_stem_frequency"][0]["next_stem"], "499")
        self.assertEqual(lock["next_stem_frequency"][0]["count"], 1)
        self.assertEqual(lock["N_hapax_next_stems"], STANDING_N_HAPAX_NEXT_STEMS)
        self.assertEqual(lock["N_hapax_next_stems"], 8)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_090_076_070_share_one_forward_stem"])
        self.assertEqual(
            lock["i_090_076_070_share_one_forward_stem"],
            STANDING_I_090_076_070_SHARE_ONE_FORWARD_STEM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle216"])
        self.assertTrue(lock["same_claim_shape_as_cycle216"])
        self.assertTrue(lock["off_i_does_not_count"])
        self.assertTrue(lock["leftover_076_070_not_090_does_not_count"])
        self.assertTrue(lock["090_076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_076_070_sides_closed"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(
            lock["standing_i_leftover_076_070_forward_4grams_i_only_unchanged"]
        )
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_extra_090_076_070_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_070_forward_stem_unchanged"])
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
            self.survey["i_leftover_076_070_forward_4grams_i_only"]["cycle"],
            217,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_4grams_i_only"]["N_i_only"],
            11,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_4grams_i_only"]["N_not_i_only"],
            0,
        )
        self.assertTrue(
            self.survey["i_leftover_076_070_forward_4grams_i_only"][
                "i_leftover_076_070_forward_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertFalse(
            self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_off_I"], 0)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"][
                "i_4gram_999_090_076_070_i_only"
            ]
        )
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["cycle"], 209)
        self.assertTrue(
            self.survey["i_extra_090_076_070_4grams_i_only"][
                "i_extra_090_076_070_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_I_036"], 1)
        self.assertEqual(
            self.survey["i_extra_090_076_070_4grams_i_only"]["N_off_I_036"],
            0,
        )
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_I_161"], 1)
        self.assertEqual(
            self.survey["i_extra_090_076_070_4grams_i_only"]["N_off_I_161"],
            0,
        )
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_I_400"], 1)
        self.assertEqual(
            self.survey["i_extra_090_076_070_4grams_i_only"]["N_off_I_400"],
            0,
        )
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_076_070_forward_stem"]["cycle"], 216)
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_stem"]["N_leftover"],
            11,
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_stem"]["N_distinct_next_stems"],
            11,
        )
        self.assertFalse(
            self.survey["i_leftover_076_070_forward_stem"][
                "i_leftover_076_070_share_one_forward_stem"
            ]
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


class TestMamariI090076070ForwardStemImageSnapshot(unittest.TestCase):
    """Cycle 218 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
