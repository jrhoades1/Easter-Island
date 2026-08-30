"""I's cycle-206 leftover 2-gram previous-stem lock.

Cycle 210 text-search lock. Uses already-vendored A–V and the
cycle-206 leftover I sites of 2-gram 076 070 (the I sites that
are not 090-prefixed 090 076 070). Does not retune that 2-gram,
those leftover sites, the cycle-207 8 I 090 076 070 sites, or
the leftover n=4 set. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished Ib
is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each leftover I site, record the previous token immediately
before 076 070 when it exists (backward 3-gram X 076 070, and
previous 4-gram V X 076 070 when it exists). Start-of-line is
no-backward. Cycle 209 extra 090 076 070 4-grams I-only hapax
1/0 x3, cycle 208 leftover 4-gram 999 090 076 070 I-only 5/0,
cycle 207 090 076 070 8/1 loss, cycle 206 076 070 19/5 loss,
and cycle 171 076 071 I-only 43/0 stay. The 8 I 090 076 070
sites do not count as leftover. Off-I 076 070 sites do not
count as leftover I. 076 071 is a different 2-gram.

Claim that can lose:
i_leftover_076_070_share_one_previous_stem. True only if
N_distinct_previous_stems=1 and N_leftover>=2. Measured:
N_leftover=11, N_090_prefixed=8, N_I=19, N_with_backward=11,
N_no_backward=0, N_distinct_previous_stems=9 (720×3, then
8 hapax previous stems 571/295/048/205/099/029/604/606).
The claim is false. Same claim-shape as cycle 190 (leftover
076 071 share-one-previous-stem lost, N_distinct=28). Do
not assume the result; measure. Do not retune.

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
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
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
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    STANDING_I_LEFTOVER_076_071_SHARE_ONE_PREVIOUS_STEM as CYCLE190_SHARE_ONE,
    STANDING_N_DISTINCT_PREVIOUS_STEMS as CYCLE190_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE190_N_LEFTOVER,
    group_sites_by_previous_stem,
    leftover_backward_3grams,
    leftover_previous_4grams,
    leftover_previous_stems,
    leftover_sites_with_backward,
    leftover_sites_without_backward,
    previous_stem_frequency_rows,
    previous_stem_frequency_table,
    site_backward_3gram,
    site_previous_4gram,
    site_previous_stem,
    TestMamariILeftover076071PreviousStemScoreboard,
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
GRAM2 = CYCLE206_GRAM2
PREFIXED_STEM = "090"
PREFIXED_3GRAM = CYCLE207_GRAM3
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_I = CYCLE206_N_I
STANDING_N_090_PREFIXED = CYCLE207_N_I
STANDING_N_LEFTOVER = 11
STANDING_N_WITH_BACKWARD = 11
STANDING_N_NO_BACKWARD = 0
STANDING_N_DISTINCT_PREVIOUS_STEMS = 9
STANDING_N_HAPAX_PREVIOUS_STEMS = 8
STANDING_NO_BACKWARD_SITES = ()
STANDING_PREFIXED_I_SITES = (
    (SIDE_IA, "Ia2", 11),
    (SIDE_IA, "Ia3", 5),
    (SIDE_IA, "Ia4", 113),
    (SIDE_IA, "Ia7", 69),
    (SIDE_IA, "Ia7", 130),
    (SIDE_IA, "Ia8", 121),
    (SIDE_IA, "Ia14", 98),
    (SIDE_IA, "Ia14", 141),
)
STANDING_LEFTOVER_SITES = (
    (SIDE_IA, "Ia1", 79),
    (SIDE_IA, "Ia1", 141),
    (SIDE_IA, "Ia2", 125),
    (SIDE_IA, "Ia3", 123),
    (SIDE_IA, "Ia5", 61),
    (SIDE_IA, "Ia6", 144),
    (SIDE_IA, "Ia7", 63),
    (SIDE_IA, "Ia8", 172),
    (SIDE_IA, "Ia9", 120),
    (SIDE_IA, "Ia13", 120),
    (SIDE_IA, "Ia13", 140),
)
STANDING_PER_SITE_PREVIOUS_STEMS = (
    "571",
    "295",
    "048",
    "205",
    "099",
    "029",
    "720",
    "720",
    "720",
    "604",
    "606",
)
STANDING_PER_SITE_BACKWARD_3GRAMS = tuple(
    (stem, "076", "070") for stem in STANDING_PER_SITE_PREVIOUS_STEMS
)
STANDING_PER_SITE_PREVIOUS_4GRAMS = (
    ("099", "571", "076", "070"),
    ("076", "295", "076", "070"),
    ("050", "048", "076", "070"),
    ("093", "205", "076", "070"),
    ("090", "099", "076", "070"),
    ("053", "029", "076", "070"),
    ("069", "720", "076", "070"),
    ("053", "720", "076", "070"),
    ("999", "720", "076", "070"),
    ("600", "604", "076", "070"),
    ("067", "606", "076", "070"),
)
STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN = (
    "571",
    "295",
    "048",
    "205",
    "099",
    "029",
    "720",
    "604",
    "606",
)
STANDING_PREVIOUS_STEM_FREQUENCY = (
    (
        "720",
        3,
        (
            (SIDE_IA, "Ia7", 63),
            (SIDE_IA, "Ia8", 172),
            (SIDE_IA, "Ia9", 120),
        ),
        (
            ("069", "720", "076", "070"),
            ("053", "720", "076", "070"),
            ("999", "720", "076", "070"),
        ),
    ),
    (
        "571",
        1,
        ((SIDE_IA, "Ia1", 79),),
        (("099", "571", "076", "070"),),
    ),
    (
        "295",
        1,
        ((SIDE_IA, "Ia1", 141),),
        (("076", "295", "076", "070"),),
    ),
    (
        "048",
        1,
        ((SIDE_IA, "Ia2", 125),),
        (("050", "048", "076", "070"),),
    ),
    (
        "205",
        1,
        ((SIDE_IA, "Ia3", 123),),
        (("093", "205", "076", "070"),),
    ),
    (
        "099",
        1,
        ((SIDE_IA, "Ia5", 61),),
        (("090", "099", "076", "070"),),
    ),
    (
        "029",
        1,
        ((SIDE_IA, "Ia6", 144),),
        (("053", "029", "076", "070"),),
    ),
    (
        "604",
        1,
        ((SIDE_IA, "Ia13", 120),),
        (("600", "604", "076", "070"),),
    ),
    (
        "606",
        1,
        ((SIDE_IA, "Ia13", 140),),
        (("067", "606", "076", "070"),),
    ),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_076_070_share_one_previous_stem"
STANDING_I_LEFTOVER_076_070_SHARE_ONE_PREVIOUS_STEM = False
STANDING_RESULT = "i_leftover_076_070_previous_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE190 = False
STANDING_SAME_AS_CYCLE209 = False
STANDING_090_PREFIXED_DOES_NOT_COUNT = True
STANDING_OFF_I_DOES_NOT_COUNT = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True


def split_i_076_070_sites(
    i_sides: dict[str, list[list[str]]],
    i_sites: tuple[tuple[str, str, int], ...],
    gram2: tuple[str, ...] = GRAM2,
    prefixed_stem: str = PREFIXED_STEM,
) -> tuple[tuple[tuple[str, str, int], ...], tuple[tuple[str, str, int], ...]]:
    """Split I 076 070 sites into leftover (not 090) and 090-prefixed."""
    leftover: list[tuple[str, str, int]] = []
    prefixed: list[tuple[str, str, int]] = []
    for site in i_sites:
        stems = line_stems_for_site(i_sides, site)
        prev = site_previous_stem(stems, site[2], gram2)
        if prev == prefixed_stem:
            prefixed.append(site)
        else:
            leftover.append(site)
    return tuple(leftover), tuple(prefixed)


def leftover_2gram_sites_from_prefixed_3grams(
    prefixed_3gram_sites: tuple[tuple[str, str, int], ...],
) -> tuple[tuple[str, str, int], ...]:
    """076 070 start is one token after each 090 076 070 start."""
    return tuple(
        (side, line, index + 1) for side, line, index in prefixed_3gram_sites
    )


def i_leftover_076_070_share_one_previous_stem(
    n_distinct_previous_stems: int,
    n_leftover: int,
) -> bool:
    """True iff N_distinct_previous_stems=1 and N_leftover>=2."""
    return n_distinct_previous_stems == 1 and n_leftover >= 2


class TestILeftover076070PreviousStemHelpers(unittest.TestCase):
    """Helpers on leftover I 076 070 previous stems. No CV, no LLM."""

    def test_previous_requires_stem_before_2gram(self):
        """A previous stem is a 3-gram; start-of-line is no-backward."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "070"))
        self.assertEqual(GRAM2, CYCLE206_GRAM2)
        self.assertEqual(PREFIXED_3GRAM, ("090", "076", "070"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N3, STANDING_N2 + 1)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_720 = ["069", "720", "076", "070", "720", "076"]
        self.assertEqual(site_previous_stem(has_720, 2, GRAM2), "720")
        self.assertEqual(site_backward_3gram(has_720, 2, GRAM2), ("720", "076", "070"))
        self.assertEqual(
            site_previous_4gram(has_720, 2, GRAM2),
            ("069", "720", "076", "070"),
        )
        has_090 = ["999", "090", "076", "070", "004", "004"]
        self.assertEqual(site_previous_stem(has_090, 2, GRAM2), "090")
        self.assertEqual(site_backward_3gram(has_090, 2, GRAM2), ("090", "076", "070"))
        start_of_line = ["076", "070", "090", "606"]
        self.assertIsNone(site_previous_stem(start_of_line, 0, GRAM2))
        self.assertIsNone(site_backward_3gram(start_of_line, 0, GRAM2))
        self.assertIsNone(site_previous_4gram(start_of_line, 0, GRAM2))
        only_one_prev = ["571", "076", "070"]
        self.assertEqual(site_previous_stem(only_one_prev, 1, GRAM2), "571")
        self.assertEqual(
            site_backward_3gram(only_one_prev, 1, GRAM2),
            ("571", "076", "070"),
        )
        self.assertIsNone(site_previous_4gram(only_one_prev, 1, GRAM2))
        mismatch_071 = ["720", "076", "071"]
        self.assertIsNone(site_previous_stem(mismatch_071, 1, GRAM2))
        self.assertIsNone(site_backward_3gram(mismatch_071, 1, GRAM2))
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
            ["099", "571", "076", "070"],
            ["999", "090", "076", "070"],
            ["069", "720", "076", "070"],
            ["036", "090", "076", "070"],
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
        self.assertTrue(i_leftover_076_070_share_one_previous_stem(1, 2))
        self.assertTrue(i_leftover_076_070_share_one_previous_stem(1, 11))
        self.assertFalse(i_leftover_076_070_share_one_previous_stem(9, 11))
        self.assertFalse(i_leftover_076_070_share_one_previous_stem(2, 11))
        self.assertFalse(i_leftover_076_070_share_one_previous_stem(1, 1))
        self.assertFalse(i_leftover_076_070_share_one_previous_stem(1, 0))
        self.assertFalse(i_leftover_076_070_share_one_previous_stem(0, 0))
        self.assertFalse(i_leftover_076_070_share_one_previous_stem(28, 34))
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_070_share_one_previous_stem")
        self.assertFalse(STANDING_I_LEFTOVER_076_070_SHARE_ONE_PREVIOUS_STEM)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_076_070_SHARE_ONE_PREVIOUS_STEM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(STANDING_N_DISTINCT_PREVIOUS_STEMS, 9)
        self.assertEqual(STANDING_N_LEFTOVER, 11)
        self.assertEqual(provider.get_call_history(), [])

    def test_frequency_table_sorts_highest_count_first_and_skips_none(self):
        """Frequency table is count-desc; no-backward sites are omitted."""
        provider = MockProvider()
        sites = STANDING_LEFTOVER_SITES[:6]
        previous = ("571", "720", "048", "720", None, "571")
        grams = (
            ("099", "571", "076", "070"),
            ("069", "720", "076", "070"),
            ("050", "048", "076", "070"),
            ("053", "720", "076", "070"),
            None,
            ("111", "571", "076", "070"),
        )
        table = previous_stem_frequency_table(sites, previous, grams)
        self.assertEqual(table[0][0], "571")
        self.assertEqual(table[0][1], 2)
        self.assertEqual(table[1][0], "720")
        self.assertEqual(table[1][1], 2)
        self.assertEqual(table[2][0], "048")
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
        shared = ("720",) * 6
        shared_grams = (("069", "720", "076", "070"),) * 6
        shared_table = previous_stem_frequency_table(sites, shared, shared_grams)
        self.assertEqual(len(shared_table), 1)
        self.assertEqual(shared_table[0][0], "720")
        self.assertEqual(shared_table[0][1], 6)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftover076070PreviousStemScoreboard(unittest.TestCase):
    """Cited-fixture leftover 076 070 previous-stem lock. Mock only."""

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
        self.n_i = len(self.i_sites)
        self.n_prefixed = len(self.measured_prefixed)
        self.n_leftover = len(self.measured_leftover)
        self.n_with_backward = len(self.with_backward)
        self.n_no_backward = len(self.no_backward)
        self.n_distinct = len(self.first_seen)
        self.claim_holds = i_leftover_076_070_share_one_previous_stem(
            self.n_distinct,
            self.n_leftover,
        )

    def test_tokens_and_sites_are_cycle_206_leftover_not_retuned(self):
        """2-gram and leftover 11 stay the cycle-206/207/208/209 locks."""
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
        prior_208 = self.survey["i_4gram_999_090_076_070_i_only"]
        self.assertEqual(prior_208["cycle"], 208)
        self.assertTrue(prior_208["i_4gram_999_090_076_070_i_only"])
        self.assertTrue(CYCLE208_I_ONLY)
        self.assertEqual(prior_208["N_I"], CYCLE208_N_I)
        self.assertEqual(prior_208["N_I"], 5)
        self.assertEqual(prior_208["N_off_I"], CYCLE208_N_OFF_I)
        self.assertEqual(prior_208["N_off_I"], 0)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        self.assertEqual(prior_207["N_I"], CYCLE207_N_I)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], CYCLE207_N_OFF_I)
        self.assertEqual(prior_207["N_off_I"], 1)
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
        prior_190 = self.survey["i_leftover_076_071_previous_stem"]
        self.assertEqual(prior_190["cycle"], 190)
        self.assertEqual(prior_190["N_leftover"], CYCLE190_N_LEFTOVER)
        self.assertEqual(prior_190["N_leftover"], 34)
        self.assertEqual(prior_190["N_distinct_previous_stems"], CYCLE190_N_DISTINCT)
        self.assertEqual(prior_190["N_distinct_previous_stems"], 28)
        self.assertFalse(prior_190["i_leftover_076_071_share_one_previous_stem"])
        self.assertFalse(CYCLE190_SHARE_ONE)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_9_distinct_previous_stems_and_claim_loses(self):
        """N_leftover=11, N_distinct=9. Claim loses. Nested 19 and 8 stay."""
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
        self.assertEqual(self.n_with_backward, STANDING_N_WITH_BACKWARD)
        self.assertEqual(STANDING_N_WITH_BACKWARD, 11)
        self.assertEqual(self.n_no_backward, STANDING_N_NO_BACKWARD)
        self.assertEqual(STANDING_N_NO_BACKWARD, 0)
        self.assertEqual(self.no_backward, STANDING_NO_BACKWARD_SITES)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_PREVIOUS_STEMS)
        self.assertEqual(STANDING_N_DISTINCT_PREVIOUS_STEMS, 9)
        if self.n_distinct != 1:
            self.assertFalse(
                i_leftover_076_070_share_one_previous_stem(
                    self.n_distinct,
                    self.n_leftover,
                )
            )
        self.assertNotEqual(self.n_distinct, 1)
        self.assertFalse(
            i_leftover_076_070_share_one_previous_stem(
                self.n_distinct,
                self.n_leftover,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_076_070_SHARE_ONE_PREVIOUS_STEM,
        )
        self.assertFalse(STANDING_I_LEFTOVER_076_070_SHARE_ONE_PREVIOUS_STEM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(STANDING_CLAIM, "i_leftover_076_070_share_one_previous_stem")
        self.assertEqual(self.previous, STANDING_PER_SITE_PREVIOUS_STEMS)
        self.assertEqual(self.backwards, STANDING_PER_SITE_BACKWARD_3GRAMS)
        self.assertEqual(self.previous_4grams, STANDING_PER_SITE_PREVIOUS_4GRAMS)
        self.assertEqual(
            tuple(stem for stem, _sites in self.first_seen),
            STANDING_DISTINCT_PREVIOUS_STEMS_FIRST_SEEN,
        )
        self.assertEqual(len(set(STANDING_PER_SITE_PREVIOUS_STEMS)), 9)
        self.assertEqual(len(STANDING_PREVIOUS_STEM_FREQUENCY), 9)
        self.assertEqual(STANDING_N_HAPAX_PREVIOUS_STEMS, 8)
        hapax = tuple(row for row in self.frequency if row[1] == 1)
        self.assertEqual(len(hapax), STANDING_N_HAPAX_PREVIOUS_STEMS)
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
        self.assertFalse(STANDING_SAME_AS_CYCLE190)
        self.assertFalse(STANDING_SAME_AS_CYCLE209)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_090_PREFIXED_DOES_NOT_COUNT)
        self.assertTrue(STANDING_OFF_I_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_frequency_table_and_per_site_previous_stems_match_fixtures(self):
        """Highest-count previous stems first; each leftover site has X 076 070."""
        self.assertEqual(self.frequency, STANDING_PREVIOUS_STEM_FREQUENCY)
        self.assertEqual(self.frequency[0][0], "720")
        self.assertEqual(self.frequency[0][1], 3)
        counts = [row[1] for row in self.frequency]
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertEqual(counts[0], 3)
        self.assertTrue(all(count == 1 for count in counts[1:]))
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
            self.assertNotEqual(prev, PREFIXED_STEM)
            self.assertEqual(site_previous_stem(stems, index, GRAM2), prev)
            self.assertEqual(site_backward_3gram(stems, index, GRAM2), back3)
            self.assertEqual(back3, (prev, "076", "070"))
            self.assertNotEqual(back3, PREFIXED_3GRAM)
            self.assertEqual(site_previous_4gram(stems, index, GRAM2), prev4)
            self.assertEqual(prev4[1:], back3)
            self.assertEqual(prev4[2:], GRAM2)
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
        self.assertEqual(IA_LINE_NAMES[6], "Ia7")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_209_208_207_206_and_171_scoreboards_still_compute(self):
        """Cycle 209 1/0 x3, 208 5/0, 207 8/1, 206 19/5, 171 43/0 stay."""
        prior_209 = TestMamariIExtra0900760704gramsIOnlyScoreboard()
        prior_209.setUp()
        prior_209.test_each_4gram_is_one_on_i_zero_off_i_and_claim_holds()
        prior_209.test_survey_matches_computed_lock()
        prior_208 = TestMamariI4gram999090076070IOnlyScoreboard()
        prior_208.setUp()
        prior_208.test_4gram_is_zero_off_i_and_i_only()
        prior_208.test_survey_matches_computed_lock()
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        prior_206 = TestMamariI2gram076070IOnlyScoreboard()
        prior_206.setUp()
        prior_206.test_2gram_is_five_off_i_and_not_i_only()
        prior_206.test_survey_matches_computed_lock()
        prior_205 = TestMamariILeftoverN4076070Scoreboard()
        prior_205.setUp()
        prior_205.test_counts_1_of_27_and_hypothesis_n_1_holds()
        prior_205.test_survey_matches_computed_lock()
        prior_190 = TestMamariILeftover076071PreviousStemScoreboard()
        prior_190.setUp()
        prior_190.test_counts_28_distinct_previous_stems_and_claim_loses()
        prior_190.test_survey_matches_computed_lock()
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-210 leftover previous-stem lock."""
        lock = self.survey["i_leftover_076_070_previous_stem"]
        self.assertEqual(lock["cycle"], 210)
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
        self.assertEqual(lock["N_with_backward"], STANDING_N_WITH_BACKWARD)
        self.assertEqual(lock["N_with_backward"], 11)
        self.assertEqual(lock["N_no_backward"], STANDING_N_NO_BACKWARD)
        self.assertEqual(lock["N_no_backward"], 0)
        self.assertEqual(lock["no_backward_sites"], [])
        self.assertEqual(
            lock["N_distinct_previous_stems"],
            STANDING_N_DISTINCT_PREVIOUS_STEMS,
        )
        self.assertEqual(lock["N_distinct_previous_stems"], 9)
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
            previous_stem_frequency_rows(STANDING_PREVIOUS_STEM_FREQUENCY),
        )
        self.assertEqual(len(lock["previous_stem_frequency"]), 9)
        self.assertEqual(lock["previous_stem_frequency"][0]["previous_stem"], "720")
        self.assertEqual(lock["previous_stem_frequency"][0]["count"], 3)
        self.assertEqual(lock["N_hapax_previous_stems"], STANDING_N_HAPAX_PREVIOUS_STEMS)
        self.assertEqual(lock["N_hapax_previous_stems"], 8)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_076_070_share_one_previous_stem"])
        self.assertEqual(
            lock["i_leftover_076_070_share_one_previous_stem"],
            STANDING_I_LEFTOVER_076_070_SHARE_ONE_PREVIOUS_STEM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle190"])
        self.assertFalse(lock["same_as_cycle209"])
        self.assertTrue(lock["090_prefixed_does_not_count"])
        self.assertTrue(lock["off_i_does_not_count"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_extra_090_076_070_4grams_i_only_unchanged"])
        self.assertTrue(lock["standing_i_4gram_999_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["cycle"], 209)
        self.assertTrue(
            self.survey["i_extra_090_076_070_4grams_i_only"][
                "i_extra_090_076_070_4grams_i_only"
            ]
        )
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_I_036"], 1)
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_off_I_036"], 0)
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_I_161"], 1)
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_off_I_161"], 0)
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_I_400"], 1)
        self.assertEqual(self.survey["i_extra_090_076_070_4grams_i_only"]["N_off_I_400"], 0)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["cycle"], 208)
        self.assertTrue(
            self.survey["i_4gram_999_090_076_070_i_only"]["i_4gram_999_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_4gram_999_090_076_070_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(
            self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["cycle"], 206)
        self.assertFalse(self.survey["i_2gram_076_070_i_only"]["i_2gram_076_070_i_only"])
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_I"], 19)
        self.assertEqual(self.survey["i_2gram_076_070_i_only"]["N_off_I"], 5)
        self.assertEqual(self.survey["i_leftover_n4_076_070"]["cycle"], 205)
        self.assertTrue(
            self.survey["i_leftover_n4_076_070"][
                "i_leftover_n4_exactly_1_contain_076_070"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_071_previous_stem"]["cycle"], 190)
        self.assertEqual(
            self.survey["i_leftover_076_071_previous_stem"]["N_distinct_previous_stems"],
            28,
        )
        self.assertFalse(
            self.survey["i_leftover_076_071_previous_stem"][
                "i_leftover_076_071_share_one_previous_stem"
            ]
        )
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
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


class TestMamariILeftover076070PreviousStemImageSnapshot(unittest.TestCase):
    """Cycle 210 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
