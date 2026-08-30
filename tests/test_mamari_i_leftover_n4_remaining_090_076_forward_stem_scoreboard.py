"""I's leftover n=4 remaining I 090 076 forward-stem lock.

Cycle 288 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–259 forward; 260–287 previous),
or the already-closed leftover remaining family. Does not
vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Unpublished Ib is 0. Does not redo
H∩P∩Q n≥8 or G–K inventories. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Leftover extra both sides are done. Cycle 260 deferred
leftover-of-leftover extra I; leftover extra is now exhausted,
so this is that leftover n=4 remaining population. Measuring
next stems of I 090 076 sites that are inside leftover n=4
remaining is not a leftover n=4 retune. Do not lock I-only of
leftover n=4 remaining 4-grams this cycle. Off-I T sites are
not this cycle.

For each leftover n=4 remaining I site, record the next token
immediately after 090 076 when it exists (the X in 090 076 X).
Sites with no next token (end of line) are N_no_next, not a
shared stem. Nested-assert N_I=69 / N_inside=13 /
N_leftover_extra=56 from cycles 223/224; do not retune those
cycles. Nested-check leftover extra remaining-after-009 extra
I=2 and remaining-after-000 extra I sites sit inside leftover
n=4 remaining (do not retune 258/259/286/287). Already-known
leftover n=4 remaining next tokens from extra I (057, 607,
020) are nested inventory, not this claim; measure the full
13. 076 071 and 076 070 do not count as this 2-gram. Leftover
extra sites do not count as leftover n=4 remaining.

Claim that can lose:
i_leftover_n4_remaining_090_076_share_one_forward_stem. True
only if N_with_next>=2 and N_distinct==1. Measured:
N_inside=13, N_with_next=13, N_no_next=0, N_distinct=6, most
frequent next stem G=020 K=4 (report; the claim is share-one,
not exactly-K), unique-max true (K>=2 and no tie at max K).
The claim is false. Same claim-shape as cycle 225 (leftover
extra share-one-forward-stem lost, 30 distinct G=070 K=8).
Unique-max G/K is inventory for a later peel. Nested cycle
224 13/56, cycle 225 30 distinct G=070 K=8, cycle 259 extra-I
fwd4 2/0, cycle 287 extra-I prev4 2/0, cycle 223 69/3, and
cycle 222 K=5 / G=090 076 stay. Do not assume the result;
measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_020010_COVERED,
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
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE225_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_K as CYCLE225_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE225_N_LEFTOVER,
    STANDING_N_NO_NEXT as CYCLE225_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE225_N_WITH_NEXT,
    TestMamariILeftoverExtra090076ForwardStemScoreboard,
    group_sites_by_next_stem,
    leftover_extra_forward_3grams,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
    leftover_sites_with_next,
    leftover_sites_without_next,
    next_stem_frequency_rows,
    next_stem_frequency_table,
    site_next_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_scoreboard import (
    STANDING_EXTRA_I_SITES as CYCLE259_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_EXTRA_I_FWD4_ALL_I_ONLY as CYCLE259_CLAIM,
    STANDING_N_I_ONLY as CYCLE259_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE259_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only_scoreboard import (
    STANDING_EXTRA_I_090_076_SITES as CYCLE287_EXTRA_I_090_076_SITES,
    STANDING_EXTRA_I_SITES as CYCLE287_EXTRA_I_SITES,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_009_EXTRA_I_PREV4_ALL_I_ONLY as CYCLE287_CLAIM,
    STANDING_N_EXTRA_I as CYCLE287_N_EXTRA_I,
    STANDING_N_I_ONLY as CYCLE287_N_I_ONLY,
    STANDING_N_NOT_I_ONLY as CYCLE287_N_NOT_I_ONLY,
    TestMamariILeftoverExtra090076RemainingAfter009ExtraIPrev4IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
    STANDING_N_REMAINING as CYCLE222_N_REMAINING,
    TestMamariILeftoverN4RemainingNext2gramScoreboard,
    i_leftover_n4_remaining_exactly_5_contain_090_076,
    leftover_n4_family_counts_hold,
    leftover_n4_rows,
    leftover_remaining_n4,
    leftover_remaining_with_g,
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
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_NEXT = 13
STANDING_N_NO_NEXT = 0
STANDING_NO_NEXT_SITES = ()
STANDING_N_DISTINCT_NEXT_STEMS = 6
STANDING_N_HAPAX_NEXT_STEMS = 2
STANDING_G = "020"
STANDING_K = 4
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_INSIDE_SITES_LOCK = STANDING_INSIDE_SITES
STANDING_PER_SITE_NEXT_STEMS = (
    "011",
    "020",
    "020",
    "087",
    "087",
    "020",
    "087",
    "607",
    "057",
    "057",
    "020",
    "021",
    "011",
)
STANDING_PER_SITE_FORWARD_3GRAMS = tuple(
    (("090", "076", stem) if stem is not None else None)
    for stem in STANDING_PER_SITE_NEXT_STEMS
)
STANDING_PER_SITE_NEXT_4GRAMS = (
    ("090", "076", "011", "027"),
    ("090", "076", "020", "010"),
    ("090", "076", "020", "010"),
    ("090", "076", "087", "291"),
    ("090", "076", "087", "224"),
    ("090", "076", "020", "010"),
    ("090", "076", "087", "755"),
    ("090", "076", "607", "755"),
    ("090", "076", "057", "600"),
    ("090", "076", "057", "600"),
    ("090", "076", "020", "010"),
    ("090", "076", "021", "020"),
    ("090", "076", "011", "400"),
)
STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN = (
    "011",
    "020",
    "087",
    "607",
    "057",
    "021",
)
STANDING_KNOWN_EXTRA_I_NEXT_STEMS = ("057", "607", "020")
STANDING_G_SITES = STANDING_LEFTOVER_020010_COVERED
STANDING_NEXT_STEM_FREQUENCY = (
    (
        "020",
        4,
        STANDING_G_SITES,
        (("090", "076", "020"),) * 4,
    ),
    (
        "087",
        3,
        (
            (SIDE_IA, "Ia4", 117),
            (SIDE_IA, "Ia5", 28),
            (SIDE_IA, "Ia6", 78),
        ),
        (("090", "076", "087"),) * 3,
    ),
    (
        "011",
        2,
        ((SIDE_IA, "Ia2", 107), (SIDE_IA, "Ia14", 54)),
        (("090", "076", "011"),) * 2,
    ),
    (
        "057",
        2,
        ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28)),
        (("090", "076", "057"),) * 2,
    ),
    ("607", 1, ((SIDE_IA, "Ia8", 106),), (("090", "076", "607"),)),
    ("021", 1, ((SIDE_IA, "Ia13", 17),), (("090", "076", "021"),)),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_remaining_090_076_share_one_forward_stem"
STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM = False
STANDING_RESULT = "i_leftover_n4_remaining_090_076_forward_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE225 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE225 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_N4_REMAINING_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_KNOWN_EXTRA_I_NEXT_STEMS_ARE_NOT_THE_WHOLE_TABLE = True


def leftover_n4_remaining_next_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_INSIDE_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str | None, ...]:
    """Per-site next stem or None for leftover n=4 remaining I 090 076."""
    return leftover_extra_next_stems(i_sides, sites, gram2)


def leftover_n4_remaining_forward_3grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_INSIDE_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site forward 3-gram or None for leftover n=4 remaining I 090 076."""
    return leftover_extra_forward_3grams(i_sides, sites, gram2)


def leftover_n4_remaining_next_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_INSIDE_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site next 4-gram or None for leftover n=4 remaining I 090 076."""
    return leftover_extra_next_4grams(i_sides, sites, gram2)


def leftover_n4_remaining_sites_with_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites that have a next stem after 090 076."""
    return leftover_sites_with_next(sites, next_stems)


def leftover_n4_remaining_sites_without_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites that are end-of-line (no next token)."""
    return leftover_sites_without_next(sites, next_stems)


def i_leftover_n4_remaining_090_076_share_one_forward_stem(
    n_distinct_next_stems: int,
    n_with_next: int,
) -> bool:
    """True iff N_distinct==1 and N_with_next>=2."""
    return n_distinct_next_stems == 1 and n_with_next >= 2


def g_uniquely_most_frequent(
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


def extra_i_090_076_sites_sit_inside_leftover_n4_remaining(
    extra_090_076_sites: tuple[tuple[str, str, int], ...],
    inside_sites: tuple[tuple[str, str, int], ...] = STANDING_INSIDE_SITES,
) -> bool:
    """True iff every extra I 090 076 site is one of the leftover n=4 remaining 13."""
    inside = set(inside_sites)
    return bool(extra_090_076_sites) and all(site in inside for site in extra_090_076_sites)


class TestILeftoverN4Remaining090076ForwardStemHelpers(unittest.TestCase):
    """Helpers on leftover n=4 remaining I 090 076 next stems. No CV, no LLM."""

    def test_next_requires_stem_after_2gram(self):
        """A next stem is a 3-gram; end-of-line is no-next. One extra token is a stem."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N3, STANDING_N2 + 1)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_020 = ["090", "076", "020", "010"]
        self.assertEqual(site_next_stem(has_020, 0, GRAM2), "020")
        self.assertEqual(
            site_forward_3gram(has_020, 0, GRAM2),
            ("090", "076", "020"),
        )
        self.assertEqual(
            site_next_4gram(has_020, 0, GRAM2),
            ("090", "076", "020", "010"),
        )
        has_011 = ["600", "090", "076", "011"]
        self.assertEqual(site_next_stem(has_011, 1, GRAM2), "011")
        family_end_then_next = ["999", "021", "090", "076", "607", "755"]
        self.assertEqual(site_next_stem(family_end_then_next, 2, GRAM2), "607")
        end_of_line = ["999", "021", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        self.assertIsNone(site_forward_3gram(end_of_line, 2, GRAM2))
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_one_distinct_and_at_least_two_with_next(self):
        """Boolean is True only when N_distinct=1 and N_with_next>=2."""
        provider = MockProvider()
        self.assertTrue(i_leftover_n4_remaining_090_076_share_one_forward_stem(1, 2))
        self.assertTrue(i_leftover_n4_remaining_090_076_share_one_forward_stem(1, 13))
        self.assertFalse(i_leftover_n4_remaining_090_076_share_one_forward_stem(6, 13))
        self.assertFalse(i_leftover_n4_remaining_090_076_share_one_forward_stem(30, 55))
        self.assertFalse(i_leftover_n4_remaining_090_076_share_one_forward_stem(2, 13))
        self.assertFalse(i_leftover_n4_remaining_090_076_share_one_forward_stem(1, 1))
        self.assertFalse(i_leftover_n4_remaining_090_076_share_one_forward_stem(1, 0))
        self.assertFalse(i_leftover_n4_remaining_090_076_share_one_forward_stem(0, 0))
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_share_one_forward_stem",
        )
        self.assertFalse(STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(STANDING_N_DISTINCT_NEXT_STEMS, 6)
        self.assertEqual(STANDING_N_WITH_NEXT, 13)
        self.assertEqual(STANDING_G, "020")
        self.assertEqual(STANDING_K, 4)
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_requires_k_at_least_two_and_no_tie(self):
        """Unique-max is inventory: K>=2 and no tie at max K. Not the claim."""
        provider = MockProvider()
        sites = STANDING_INSIDE_SITES[:6]
        tied = ("020", "087", "020", "087", "011", "057")
        tied_grams = tuple(("090", "076", stem) for stem in tied)
        tied_table = next_stem_frequency_table(sites, tied, tied_grams)
        self.assertEqual(tied_table[0][1], 2)
        self.assertEqual(tied_table[1][1], 2)
        self.assertFalse(g_uniquely_most_frequent(tied_table))
        unique = ("020", "020", "087", "011", "057", "607")
        unique_grams = tuple(("090", "076", stem) for stem in unique)
        unique_table = next_stem_frequency_table(sites, unique, unique_grams)
        self.assertEqual(unique_table[0][0], "020")
        self.assertEqual(unique_table[0][1], 2)
        self.assertTrue(g_uniquely_most_frequent(unique_table))
        hapax = ("020", "087", "011", "057", "607", "021")
        hapax_grams = tuple(("090", "076", stem) for stem in hapax)
        hapax_table = next_stem_frequency_table(sites, hapax, hapax_grams)
        self.assertEqual(hapax_table[0][1], 1)
        self.assertFalse(g_uniquely_most_frequent(hapax_table))
        self.assertFalse(g_uniquely_most_frequent(()))
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(provider.get_call_history(), [])

    def test_frequency_table_sorts_highest_count_first_and_skips_none(self):
        """Frequency table is count-desc; no-next sites are omitted."""
        provider = MockProvider()
        sites = STANDING_INSIDE_SITES[:6]
        nxt = ("020", "087", "020", None, "011", "020")
        grams = (
            ("090", "076", "020"),
            ("090", "076", "087"),
            ("090", "076", "020"),
            None,
            ("090", "076", "011"),
            ("090", "076", "020"),
        )
        table = next_stem_frequency_table(sites, nxt, grams)
        self.assertEqual(table[0][0], "020")
        self.assertEqual(table[0][1], 3)
        self.assertEqual(table[1][0], "087")
        self.assertEqual(table[1][1], 1)
        self.assertEqual(len(table), 3)
        self.assertEqual(leftover_n4_remaining_sites_without_next(sites, nxt), (sites[3],))
        self.assertEqual(
            leftover_n4_remaining_sites_with_next(sites, nxt),
            (sites[0], sites[1], sites[2], sites[4], sites[5]),
        )
        shared = ("020",) * 6
        shared_grams = (("090", "076", "020"),) * 6
        shared_table = next_stem_frequency_table(sites, shared, shared_grams)
        self.assertEqual(len(shared_table), 1)
        self.assertEqual(shared_table[0][0], "020")
        self.assertEqual(shared_table[0][1], 6)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076ForwardStemScoreboard(unittest.TestCase):
    """Cited-fixture leftover n=4 remaining 090 076 next-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.inside_sites = STANDING_INSIDE_SITES
        self.next_stems = leftover_n4_remaining_next_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.forwards = leftover_n4_remaining_forward_3grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.next_4grams = leftover_n4_remaining_next_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.with_next = leftover_n4_remaining_sites_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next = leftover_n4_remaining_sites_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.first_seen = group_sites_by_next_stem(self.inside_sites, self.next_stems)
        self.frequency = next_stem_frequency_table(
            self.inside_sites,
            self.next_stems,
            self.forwards,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover_extra = len(STANDING_LEFTOVER_SITES)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.n_distinct = len(self.first_seen)
        self.g = self.frequency[0][0] if self.frequency else None
        self.k = self.frequency[0][1] if self.frequency else 0
        self.unique_max = g_uniquely_most_frequent(self.frequency)
        self.claim_holds = i_leftover_n4_remaining_090_076_share_one_forward_stem(
            self.n_distinct,
            self.n_with_next,
        )

    def test_tokens_and_sites_are_cycle_224_inside_not_retuned(self):
        """2-gram and leftover n=4 remaining 13 stay the cycle-224/223/222 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
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
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertEqual(prior_222["K"], CYCLE222_K)
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(tuple(prior_222["G"]), CYCLE222_G)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertTrue(CYCLE222_CLAIM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_6_distinct_next_stems_and_claim_loses(self):
        """N_inside=13, N_with_next=13, N_distinct=6, G=020 K=4. Claim loses."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 13)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 0)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ())
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_inside)
        self.assertEqual(13 + 0, 13)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_NEXT_STEMS)
        self.assertEqual(STANDING_N_DISTINCT_NEXT_STEMS, 6)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "020")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 4)
        self.assertTrue(self.unique_max)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(
            self.unique_max,
            g_uniquely_most_frequent(self.frequency),
        )
        self.assertGreater(STANDING_K, STANDING_NEXT_STEM_FREQUENCY[1][1])
        if self.n_distinct != 1:
            self.assertFalse(
                i_leftover_n4_remaining_090_076_share_one_forward_stem(
                    self.n_distinct,
                    self.n_with_next,
                )
            )
        self.assertNotEqual(self.n_distinct, 1)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_share_one_forward_stem(
                self.n_distinct,
                self.n_with_next,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM,
        )
        self.assertFalse(STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_share_one_forward_stem",
        )
        self.assertEqual(self.next_stems, STANDING_PER_SITE_NEXT_STEMS)
        self.assertEqual(self.forwards, STANDING_PER_SITE_FORWARD_3GRAMS)
        self.assertEqual(self.next_4grams, STANDING_PER_SITE_NEXT_4GRAMS)
        self.assertEqual(
            tuple(stem for stem, _sites in self.first_seen),
            STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN,
        )
        self.assertEqual(len(STANDING_NEXT_STEM_FREQUENCY), 6)
        self.assertEqual(STANDING_N_HAPAX_NEXT_STEMS, 2)
        hapax = tuple(row for row in self.frequency if row[1] == 1)
        self.assertEqual(len(hapax), STANDING_N_HAPAX_NEXT_STEMS)
        self.assertEqual(
            sum(count for _stem, count, _sites, _grams in self.frequency),
            13,
        )
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE225)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE225)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_REMAINING_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_frequency_table_and_known_extra_i_next_stems_are_not_the_whole_table(self):
        """G=020 K=4 unique-max; extra I 057/607/020 are nested inventory, not the 6."""
        self.assertEqual(self.frequency, STANDING_NEXT_STEM_FREQUENCY)
        counts = [row[1] for row in self.frequency]
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertEqual(counts[0], 4)
        self.assertEqual(self.frequency[0][0], "020")
        self.assertEqual(self.frequency[0][2], STANDING_G_SITES)
        self.assertEqual(STANDING_G_SITES, STANDING_LEFTOVER_020010_COVERED)
        self.assertEqual(len(STANDING_G_SITES), 4)
        measured_stems = tuple(row[0] for row in self.frequency)
        self.assertEqual(set(STANDING_KNOWN_EXTRA_I_NEXT_STEMS), {"057", "607", "020"})
        for stem in STANDING_KNOWN_EXTRA_I_NEXT_STEMS:
            self.assertIn(stem, measured_stems)
        self.assertGreater(len(measured_stems), len(STANDING_KNOWN_EXTRA_I_NEXT_STEMS))
        self.assertIn("011", measured_stems)
        self.assertIn("087", measured_stems)
        self.assertIn("021", measured_stems)
        self.assertTrue(STANDING_KNOWN_EXTRA_I_NEXT_STEMS_ARE_NOT_THE_WHOLE_TABLE)
        for site, nxt, fwd3, nxt4 in zip(
            STANDING_INSIDE_SITES,
            STANDING_PER_SITE_NEXT_STEMS,
            STANDING_PER_SITE_FORWARD_3GRAMS,
            STANDING_PER_SITE_NEXT_4GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(site_next_stem(stems, index, GRAM2), nxt)
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), fwd3)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), nxt4)
            self.assertIsNotNone(nxt)
            self.assertLess(index + STANDING_N2, len(stems))
            self.assertEqual(stems[index + STANDING_N2], nxt)
            self.assertEqual(fwd3, ("090", "076", nxt))
            self.assertIsNotNone(nxt4)
            self.assertEqual(nxt4[:3], fwd3)
            self.assertEqual(nxt4[:2], GRAM2)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        for stem, count, sites, grams in STANDING_NEXT_STEM_FREQUENCY:
            self.assertEqual(len(sites), count)
            self.assertEqual(len(grams), count)
            for site, gram3 in zip(sites, grams, strict=True):
                self.assertEqual(gram3[2], stem)
                self.assertEqual(gram3[:2], GRAM2)
                self.assertIn(site, STANDING_INSIDE_SITES)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_extra_i_sites_sit_inside_leftover_n4_remaining(self):
        """Remaining-after-009 extra I=2 and remaining-after-000 extra I sit inside."""
        self.assertEqual(CYCLE287_N_EXTRA_I, 2)
        self.assertEqual(CYCLE287_EXTRA_I_SITES, ((SIDE_IA, "Ia8", 113), (SIDE_IA, "Ia12", 82)))
        self.assertEqual(
            CYCLE287_EXTRA_I_090_076_SITES,
            ((SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia12", 83)),
        )
        self.assertTrue(
            extra_i_090_076_sites_sit_inside_leftover_n4_remaining(
                CYCLE287_EXTRA_I_090_076_SITES,
                STANDING_INSIDE_SITES,
            )
        )
        self.assertEqual(
            CYCLE259_EXTRA_I_SITES,
            ((SIDE_IA, "Ia8", 106), (SIDE_IA, "Ia8", 114), (SIDE_IA, "Ia9", 28)),
        )
        self.assertTrue(
            extra_i_090_076_sites_sit_inside_leftover_n4_remaining(
                CYCLE259_EXTRA_I_SITES,
                STANDING_INSIDE_SITES,
            )
        )
        prior_287 = self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]
        self.assertEqual(prior_287["cycle"], 287)
        self.assertEqual(prior_287["N_extra_i"], 2)
        self.assertEqual(prior_287["N_i_only"], 2)
        self.assertEqual(prior_287["N_not_i_only"], 0)
        self.assertTrue(prior_287["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_all_i_only"])
        prior_259 = self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]
        self.assertEqual(prior_259["cycle"], 259)
        self.assertEqual(prior_259["N_i_only"], 2)
        self.assertEqual(prior_259["N_not_i_only"], 0)
        self.assertTrue(prior_259["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_all_i_only"])
        extra_009_090 = tuple(tuple(row) for row in prior_287["extra_i_090_076_sites"])
        extra_000 = tuple(tuple(row) for row in prior_259["extra_i_sites"])
        self.assertEqual(extra_009_090, CYCLE287_EXTRA_I_090_076_SITES)
        self.assertEqual(extra_000, CYCLE259_EXTRA_I_SITES)
        for site in extra_009_090 + extra_000:
            self.assertIn(site, STANDING_INSIDE_SITES)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_224_225_259_287_223_222_still_compute(self):
        """Cycle 224 13/56, 225 30 distinct G=070 K=8, 259 2/0, 287 2/0, 223 69/3, 222 K=5 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
        if prior_224.n_inside != 13 or prior_224.n_leftover != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_225 = TestMamariILeftoverExtra090076ForwardStemScoreboard()
        prior_225.setUp()
        prior_225.test_counts_30_distinct_next_stems_and_claim_loses()
        prior_225.test_survey_matches_computed_lock()
        self.assertEqual(prior_225.n_leftover, CYCLE225_N_LEFTOVER)
        self.assertEqual(prior_225.n_leftover, 56)
        self.assertEqual(prior_225.n_with_next, CYCLE225_N_WITH_NEXT)
        self.assertEqual(prior_225.n_no_next, CYCLE225_N_NO_NEXT)
        self.assertEqual(prior_225.n_distinct, CYCLE225_N_DISTINCT)
        self.assertEqual(prior_225.n_distinct, 30)
        self.assertEqual(prior_225.g, CYCLE225_G)
        self.assertEqual(prior_225.g, "070")
        self.assertEqual(prior_225.k, CYCLE225_K)
        self.assertEqual(prior_225.k, 8)
        self.assertFalse(prior_225.claim_holds)
        self.assertFalse(CYCLE225_SHARE_ONE)
        if (
            prior_225.n_distinct != 30
            or prior_225.g != "070"
            or prior_225.k != 8
        ):
            self.fail("nested cycle 225 30 distinct G=070 K=8 drifted")
        prior_259 = TestMamariILeftoverExtra090076RemainingAfter000ExtraIFwd4IOnlyScoreboard()
        prior_259.setUp()
        prior_259.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE259_N_I_ONLY, 2)
        self.assertEqual(CYCLE259_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE259_CLAIM)
        if CYCLE259_N_I_ONLY != 2 or CYCLE259_N_NOT_I_ONLY != 0:
            self.fail("nested cycle 259 extra-I forward 4-grams 2/0 drifted")
        prior_287 = TestMamariILeftoverExtra090076RemainingAfter009ExtraIPrev4IOnlyScoreboard()
        prior_287.setUp()
        prior_287.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE287_N_I_ONLY, 2)
        self.assertEqual(CYCLE287_N_NOT_I_ONLY, 0)
        self.assertTrue(CYCLE287_CLAIM)
        if CYCLE287_N_I_ONLY != 2 or CYCLE287_N_NOT_I_ONLY != 0:
            self.fail("nested cycle 287 extra-I previous 4-grams 2/0 drifted")
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
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-288 leftover n=4 remaining next-stem lock."""
        lock = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(lock["cycle"], 288)
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
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 13)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(
            lock["N_distinct_next_stems"],
            STANDING_N_DISTINCT_NEXT_STEMS,
        )
        self.assertEqual(lock["N_distinct_next_stems"], 6)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "020")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 4)
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertEqual(
            lock["g_uniquely_most_frequent"],
            STANDING_G_UNIQUELY_MOST_FREQUENT,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["G_sites"]),
            STANDING_G_SITES,
        )
        self.assertEqual(
            tuple(lock["distinct_next_stems"]),
            STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN,
        )
        self.assertEqual(
            [stem if stem is not None else None for stem in STANDING_PER_SITE_NEXT_STEMS],
            lock["per_site_next_stems"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_PER_SITE_FORWARD_3GRAMS],
            lock["per_site_forward_3grams"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_PER_SITE_NEXT_4GRAMS],
            lock["per_site_next_4grams"],
        )
        self.assertEqual(
            lock["next_stem_frequency"],
            next_stem_frequency_rows(STANDING_NEXT_STEM_FREQUENCY),
        )
        self.assertEqual(len(lock["next_stem_frequency"]), 6)
        self.assertEqual(lock["next_stem_frequency"][0]["next_stem"], "020")
        self.assertEqual(lock["next_stem_frequency"][0]["count"], 4)
        self.assertEqual(lock["N_hapax_next_stems"], STANDING_N_HAPAX_NEXT_STEMS)
        self.assertEqual(lock["N_hapax_next_stems"], 2)
        self.assertEqual(
            tuple(lock["known_extra_i_next_stems"]),
            STANDING_KNOWN_EXTRA_I_NEXT_STEMS,
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        self.assertEqual(
            lock["i_leftover_n4_remaining_090_076_share_one_forward_stem"],
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle225"])
        self.assertTrue(lock["same_claim_shape_as_cycle225"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["leftover_n4_remaining_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["known_extra_i_next_stems_are_not_the_whole_table"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_I"], 69)
        self.assertEqual(
            self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"],
            13,
        )
        self.assertEqual(
            self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"],
            56,
        )
        self.assertFalse(
            self.survey["i_090_076_inside_leftover_n4_remaining_family"][
                "i_090_076_all_inside_leftover_n4_remaining_family"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["cycle"], 225)
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_forward_stem"][
                "i_leftover_extra_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_forward_stem"]["N_distinct_next_stems"],
            30,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["G"], "070")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["K"], 8)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]["cycle"],
            259,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]["N_i_only"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_000_extra_i_fwd4_i_only"]["N_not_i_only"],
            0,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]["cycle"],
            287,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]["N_i_only"],
            2,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]["N_not_i_only"],
            0,
        )
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_remaining_after_009_extra_i_prev4_i_only"]["N_extra_i"],
            2,
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_leftover_n4_remaining_next_2gram"]["cycle"], 222)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_next_2gram"][
                "i_leftover_n4_remaining_exactly_5_contain_090_076"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_next_2gram"]["K"], 5)
        self.assertEqual(tuple(self.survey["i_leftover_n4_remaining_next_2gram"]["G"]), GRAM2)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_n"], 5)
        self.assertEqual(self.survey["n_repeating_nge5"]["cycle"], 134)
        self.assertTrue(self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"])
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"], 5)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076ForwardStemImageSnapshot(unittest.TestCase):
    """Cycle 288 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
