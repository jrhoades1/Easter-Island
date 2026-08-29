"""I's cycle-171 leftover 2-gram vs the locked leftover n=4 family.

Cycle 172 text-search lock. Uses already-vendored A–V and the
cycle-171 leftover 2-gram 076 071 (I-only, N_I=43, all Ia).
Does not retune that 2-gram or the four leftover n=4 maximals
from cycle 170. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each of the locked 43 I sites, whether the 2-gram sits as
a contiguous substring of leftover n=4 maximals 999 090 076 071,
999 205 076 071, 076 071 009 090, or 076 071 090 999. A site
is inside a container iff container start ≤ 2-gram start ≤
container start + n_container - 2. Other leftover n=4 (e.g.
071 065 071 999) do not count as this family. 071 999 and
076 076 do not count as this 2-gram. Hypothesis: every I
occurrence sits inside that leftover n=4 family. Measured:
N_inside=9, N_leftover=34. Claim that can lose:
i_2gram_076_071_all_inside_leftover_n4_family. The claim is
false. Same claim-shape as cycle 168 (999 090 076
all-inside leftover n=4 family lost, N_leftover=1 at Ia1[1])
and cycle 161 (076 020 010 all-inside-known-family lost,
N_leftover=4). Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_ON_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_inside_family_scoreboard import (
    STANDING_N_LEFTOVER as CYCLE168_N_LEFTOVER,
    TestMamariI3gram999090076InsideFamilyScoreboard,
    inside_sites_from_membership,
    leftover_sites_from_membership,
    membership_for_sites,
    sites_with_container,
)
from tests.test_mamari_i_leftover_n4_076_071_scoreboard import (
    NEAR_MISS_071_065_071_999,
    NEAR_MISS_700_076_076_053,
    STANDING_MATCHING_LEFTOVERS,
    STANDING_WITH_ROWS,
    TestMamariILeftoverN4076071Scoreboard,
)
from tests.test_mamari_i_leftover_n4_independent_n5_n3_overlap_scoreboard import (
    TestMamariILeftoverN4IndependentN5N3OverlapScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    STANDING_LEFTOVER,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_020_010_inside_family_scoreboard import (
    STANDING_N_LEFTOVER as CYCLE161_N_LEFTOVER,
    TestMamariIOverlap3gram076020010InsideFamilyScoreboard,
    site_inside_container,
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

HYPOTHESIS_ALL_INSIDE = True
CID_LEFTOVER_090071 = "leftover_999_090_076_071"
CID_LEFTOVER_205071 = "leftover_999_205_076_071"
CID_LEFTOVER_009 = "leftover_076_071_009_090"
CID_LEFTOVER_090999 = "leftover_076_071_090_999"
LEFTOVER_N4_090071 = ("999", "090", "076", "071")
LEFTOVER_N4_205071 = ("999", "205", "076", "071")
LEFTOVER_N4_009 = ("076", "071", "009", "090")
LEFTOVER_N4_090999 = ("076", "071", "090", "999")
STANDING_N2 = 2
STANDING_N4 = 4
STANDING_IA_HITS = 43
STANDING_IB_HITS = 0
STANDING_LEFTOVER_090071_SITES = (
    (SIDE_IA, "Ia4", 153),
    (SIDE_IA, "Ia5", 1),
    (SIDE_IA, "Ia5", 22),
)
STANDING_LEFTOVER_205071_SITES = (
    (SIDE_IA, "Ia3", 51),
    (SIDE_IA, "Ia3", 79),
)
STANDING_LEFTOVER_009_SITES = (
    (SIDE_IA, "Ia5", 161),
    (SIDE_IA, "Ia12", 71),
)
STANDING_LEFTOVER_090999_SITES = (
    (SIDE_IA, "Ia7", 166),
    (SIDE_IA, "Ia14", 136),
)
STANDING_CONTAINERS = (
    (CID_LEFTOVER_090071, LEFTOVER_N4_090071, STANDING_LEFTOVER_090071_SITES),
    (CID_LEFTOVER_205071, LEFTOVER_N4_205071, STANDING_LEFTOVER_205071_SITES),
    (CID_LEFTOVER_009, LEFTOVER_N4_009, STANDING_LEFTOVER_009_SITES),
    (CID_LEFTOVER_090999, LEFTOVER_N4_090999, STANDING_LEFTOVER_090999_SITES),
)
STANDING_N_IN_LEFTOVER_090071 = 3
STANDING_N_IN_LEFTOVER_205071 = 2
STANDING_N_IN_LEFTOVER_009 = 2
STANDING_N_IN_LEFTOVER_090999 = 2
STANDING_N_INSIDE = 9
STANDING_N_LEFTOVER = 34
STANDING_LEFTOVER_090071_COVERED = (
    (SIDE_IA, "Ia4", 155),
    (SIDE_IA, "Ia5", 3),
    (SIDE_IA, "Ia5", 24),
)
STANDING_LEFTOVER_205071_COVERED = (
    (SIDE_IA, "Ia3", 53),
    (SIDE_IA, "Ia3", 81),
)
STANDING_LEFTOVER_009_COVERED = (
    (SIDE_IA, "Ia5", 161),
    (SIDE_IA, "Ia12", 71),
)
STANDING_LEFTOVER_090999_COVERED = (
    (SIDE_IA, "Ia7", 166),
    (SIDE_IA, "Ia14", 136),
)
STANDING_INSIDE_SITES = (
    (SIDE_IA, "Ia3", 53),
    (SIDE_IA, "Ia3", 81),
    (SIDE_IA, "Ia4", 155),
    (SIDE_IA, "Ia5", 3),
    (SIDE_IA, "Ia5", 24),
    (SIDE_IA, "Ia5", 161),
    (SIDE_IA, "Ia7", 166),
    (SIDE_IA, "Ia12", 71),
    (SIDE_IA, "Ia14", 136),
)
STANDING_LEFTOVER_SITES = (
    (SIDE_IA, "Ia1", 86),
    (SIDE_IA, "Ia1", 163),
    (SIDE_IA, "Ia2", 43),
    (SIDE_IA, "Ia2", 51),
    (SIDE_IA, "Ia2", 104),
    (SIDE_IA, "Ia2", 169),
    (SIDE_IA, "Ia3", 13),
    (SIDE_IA, "Ia3", 85),
    (SIDE_IA, "Ia3", 110),
    (SIDE_IA, "Ia3", 133),
    (SIDE_IA, "Ia3", 147),
    (SIDE_IA, "Ia5", 67),
    (SIDE_IA, "Ia5", 79),
    (SIDE_IA, "Ia5", 134),
    (SIDE_IA, "Ia6", 117),
    (SIDE_IA, "Ia7", 32),
    (SIDE_IA, "Ia7", 48),
    (SIDE_IA, "Ia8", 27),
    (SIDE_IA, "Ia9", 10),
    (SIDE_IA, "Ia12", 6),
    (SIDE_IA, "Ia12", 19),
    (SIDE_IA, "Ia12", 59),
    (SIDE_IA, "Ia12", 63),
    (SIDE_IA, "Ia13", 44),
    (SIDE_IA, "Ia13", 54),
    (SIDE_IA, "Ia13", 92),
    (SIDE_IA, "Ia13", 101),
    (SIDE_IA, "Ia13", 114),
    (SIDE_IA, "Ia13", 128),
    (SIDE_IA, "Ia13", 149),
    (SIDE_IA, "Ia13", 153),
    (SIDE_IA, "Ia14", 81),
    (SIDE_IA, "Ia14", 106),
    (SIDE_IA, "Ia14", 166),
)
STANDING_LEFTOVER_PREVIOUS_4GRAMS = (
    ("027", "200", "076", "071"),
    ("090", "700", "076", "071"),
    ("430", "071", "076", "071"),
    ("999", "700", "076", "071"),
    ("005", "633", "076", "071"),
    ("147", "076", "076", "071"),
    ("205", "225", "076", "071"),
    ("076", "385", "076", "071"),
    ("530", "298", "076", "071"),
    ("070", "205", "076", "071"),
    ("600", "604", "076", "071"),
    ("000", "090", "076", "071"),
    ("999", "406", "076", "071"),
    ("071", "072", "076", "071"),
    ("430", "099", "076", "071"),
    ("076", "999", "076", "071"),
    ("400", "222", "076", "071"),
    ("002", "514", "076", "071"),
    ("700", "604", "076", "071"),
    ("019", "099", "076", "071"),
    ("490", "440", "076", "071"),
    ("050", "606", "076", "071"),
    ("061", "290", "076", "071"),
    ("002", "009", "076", "071"),
    ("999", "007", "076", "071"),
    ("073", "006", "076", "071"),
    ("042", "730", "076", "071"),
    ("084", "600", "076", "071"),
    ("040", "700", "076", "071"),
    ("006", "048", "076", "071"),
    ("076", "090", "076", "071"),
    ("076", "011", "076", "071"),
    ("090", "090", "076", "071"),
    ("006", "000", "076", "071"),
)
STANDING_LEFTOVER_NEXT_4GRAMS = (
    ("076", "071", "090", "606"),
    ("076", "071", "700", "076"),
    ("076", "071", "076", "021"),
    ("076", "071", "010", "660"),
    ("076", "071", "600", "090"),
    ("076", "071", "600", "009"),
    ("076", "071", "274", "604"),
    ("076", "071", "090", "076"),
    ("076", "071", "018", "049"),
    ("076", "071", "202", "604"),
    ("076", "071", "061", "011"),
    ("076", "071", "004", "004"),
    ("076", "071", "078", "999"),
    ("076", "071", "496", "999"),
    ("076", "071", "632", "670"),
    ("076", "071", "183", "430"),
    ("076", "071", "071", "076"),
    ("076", "071", "070", "076"),
    ("076", "071", "600", "999"),
    ("076", "071", "513", "001"),
    ("076", "071", "090", "047"),
    ("076", "071", "061", "290"),
    ("076", "071", "607", "208"),
    ("076", "071", "002", "536"),
    ("076", "071", "700", "430"),
    ("076", "071", "700", "128"),
    ("076", "071", "729", "073"),
    ("076", "071", "021", "090"),
    ("076", "071", "670", "009"),
    ("076", "071", "076", "090"),
    ("076", "071", "076", "430"),
    ("076", "071", "076", "010"),
    ("076", "071", "600", "053"),
    ("076", "071", "076", "011"),
)
STANDING_MEMBERSHIP = (
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (CID_LEFTOVER_205071,),
    (CID_LEFTOVER_205071,),
    (),
    (),
    (),
    (),
    (CID_LEFTOVER_090071,),
    (CID_LEFTOVER_090071,),
    (CID_LEFTOVER_090071,),
    (),
    (),
    (),
    (CID_LEFTOVER_009,),
    (),
    (),
    (),
    (CID_LEFTOVER_090999,),
    (),
    (),
    (),
    (),
    (),
    (),
    (CID_LEFTOVER_009,),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (CID_LEFTOVER_090999,),
    (),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_2gram_076_071_all_inside_leftover_n4_family"
STANDING_I_2GRAM_076_071_ALL_INSIDE_LEFTOVER_N4_FAMILY = False
STANDING_RESULT = "i_2gram_076_071_inside_family"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE161 = False
STANDING_SAME_AS_CYCLE168 = False
STANDING_071_999_DOES_NOT_COUNT = True
STANDING_076_076_DOES_NOT_COUNT = True
STANDING_OTHER_LEFTOVER_N4_DOES_NOT_COUNT = True


def leftover_local_4grams(
    i_sides: dict[str, list[list[str]]],
    leftover_sites: tuple[tuple[str, str, int], ...],
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[tuple[str, str, int], tuple[str, ...] | None, tuple[str, ...] | None], ...]:
    """Previous and next 4-grams (two stems Y / X) at leftover 2-gram sites."""
    rows = []
    n2 = len(gram2)
    extra = 4 - n2
    for site in leftover_sites:
        stems = line_stems_for_site(i_sides, site)
        _side, _line, start = site
        previous = (
            tuple(stems[start - extra : start + n2]) if start >= extra else None
        )
        nxt = (
            tuple(stems[start : start + n2 + extra])
            if start + n2 + extra - 1 < len(stems)
            else None
        )
        rows.append((site, previous, nxt))
    return tuple(rows)


def leftover_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    previous: tuple[tuple[str, ...], ...] = STANDING_LEFTOVER_PREVIOUS_4GRAMS,
    nxt: tuple[tuple[str, ...], ...] = STANDING_LEFTOVER_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped leftover local 4-gram rows, tablet/side/line/index order."""
    rows = []
    for (side, line, index), prev_gram, next_gram in zip(
        leftover_sites,
        previous,
        nxt,
        strict=True,
    ):
        rows.append(
            {
                "tablet": "I",
                "side": side,
                "line": line,
                "index": index,
                "previous_4gram": list(prev_gram),
                "next_4gram": list(next_gram),
            }
        )
    return rows


def i_2gram_076_071_all_inside_leftover_n4_family(
    leftover_sites: tuple[tuple[str, str, int], ...],
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff every I 2-gram site sits inside the leftover n=4 family.

    An empty I-site set is false here (the cycle-171 43 sites must
    be present and none may be leftover).
    """
    return bool(i_sites) and leftover_sites == ()


class TestI2gram076071InsideFamilyHelpers(unittest.TestCase):
    """Helpers on cycle-171 leftover tokens. No CV, no LLM."""

    def test_inside_requires_contiguous_substring_and_window(self):
        """Family leftover n=4 count; a near-miss or out-of-window site does not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(LEFTOVER_N4_090071, ("999", "090", "076", "071"))
        self.assertEqual(LEFTOVER_N4_205071, ("999", "205", "076", "071"))
        self.assertEqual(LEFTOVER_N4_009, ("076", "071", "009", "090"))
        self.assertEqual(LEFTOVER_N4_090999, ("076", "071", "090", "999"))
        self.assertEqual(LEFTOVER_N4_009[:STANDING_N2], GRAM2)
        self.assertEqual(LEFTOVER_N4_090999[:STANDING_N2], GRAM2)
        self.assertEqual(LEFTOVER_N4_090071[-STANDING_N2:], GRAM2)
        self.assertEqual(LEFTOVER_N4_205071[-STANDING_N2:], GRAM2)
        prefix_line = ["076", "071", "009", "090"]
        self.assertTrue(site_inside_container(prefix_line, 0, LEFTOVER_N4_009, 0, GRAM2))
        suffix_line = ["999", "090", "076", "071"]
        self.assertTrue(
            site_inside_container(suffix_line, 2, LEFTOVER_N4_090071, 0, GRAM2)
        )
        leftover_site = ["027", "200", "076", "071", "090", "606"]
        self.assertFalse(
            site_inside_container(leftover_site, 2, LEFTOVER_N4_090071, 0, GRAM2)
        )
        self.assertFalse(
            site_inside_container(leftover_site, 2, LEFTOVER_N4_009, 2, GRAM2)
        )
        almost_071_999 = ["071", "065", "071", "999"]
        self.assertFalse(
            site_inside_container(almost_071_999, 0, LEFTOVER_N4_009, 0, GRAM2)
        )
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_071_065_071_999))
        n2_076_076 = ["700", "076", "076", "053"]
        self.assertFalse(
            site_inside_container(n2_076_076, 1, LEFTOVER_N4_090071, 0, GRAM2)
        )
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        out_of_window = ["999", "090", "076", "071", "076", "071"]
        self.assertTrue(
            site_inside_container(out_of_window, 2, LEFTOVER_N4_090071, 0, GRAM2)
        )
        self.assertFalse(
            site_inside_container(out_of_window, 4, LEFTOVER_N4_090071, 0, GRAM2)
        )
        self.assertFalse(
            site_inside_container(["076", "071"], 0, LEFTOVER_N4_009, 0, GRAM2)
        )
        self.assertTrue(STANDING_071_999_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_076_DOES_NOT_COUNT)
        self.assertTrue(STANDING_OTHER_LEFTOVER_N4_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_inside_requires_empty_leftover_and_present_sites(self):
        """Boolean is True only when I sites exist and leftover is empty."""
        provider = MockProvider()
        self.assertTrue(
            i_2gram_076_071_all_inside_leftover_n4_family((), STANDING_I_SITES)
        )
        self.assertFalse(
            i_2gram_076_071_all_inside_leftover_n4_family(
                STANDING_LEFTOVER_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertFalse(i_2gram_076_071_all_inside_leftover_n4_family((), ()))
        self.assertEqual(
            STANDING_CLAIM,
            "i_2gram_076_071_all_inside_leftover_n4_family",
        )
        self.assertFalse(STANDING_I_2GRAM_076_071_ALL_INSIDE_LEFTOVER_N4_FAMILY)
        self.assertNotEqual(
            STANDING_I_2GRAM_076_071_ALL_INSIDE_LEFTOVER_N4_FAMILY,
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(CYCLE168_N_LEFTOVER, 1)
        self.assertEqual(CYCLE161_N_LEFTOVER, 4)
        self.assertFalse(STANDING_SAME_AS_CYCLE168)
        self.assertFalse(STANDING_SAME_AS_CYCLE161)
        self.assertEqual(provider.get_call_history(), [])

    def test_2gram_is_substring_of_each_locked_leftover_n4(self):
        """2-gram is the locked shared run, not a retuned inventory."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertNotEqual(GRAM2, GRAM5)
        self.assertFalse(is_contiguous_substring(GRAM2, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N2, 2)
        leftover_grams = {row[0] for row in STANDING_LEFTOVER}
        for tokens in STANDING_MATCHING_LEFTOVERS:
            self.assertTrue(is_contiguous_substring(GRAM2, tokens))
            self.assertEqual(len(tokens), STANDING_N4)
            self.assertIn(tokens, leftover_grams)
        self.assertEqual(STANDING_MATCHING_LEFTOVERS, (
            LEFTOVER_N4_090071,
            LEFTOVER_N4_205071,
            LEFTOVER_N4_009,
            LEFTOVER_N4_090999,
        ))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_071_065_071_999))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_700_076_076_053))
        self.assertIn(NEAR_MISS_071_065_071_999, leftover_grams)
        self.assertIn(NEAR_MISS_700_076_076_053, leftover_grams)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI2gram076071InsideFamilyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 2-gram leftover-n=4-family lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.membership = membership_for_sites(
            self.i_sides,
            self.i_sites,
            STANDING_CONTAINERS,
            GRAM2,
        )
        self.leftover_090071_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_090071,
        )
        self.leftover_205071_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_205071,
        )
        self.leftover_009_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_009,
        )
        self.leftover_090999_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_090999,
        )
        self.inside_sites = inside_sites_from_membership(self.i_sites, self.membership)
        self.leftover_sites = leftover_sites_from_membership(
            self.i_sites,
            self.membership,
        )
        self.local_4grams = leftover_local_4grams(self.i_sides, self.leftover_sites)
        self.n_on_i = len(self.i_sites)
        self.n_in_leftover_090071 = len(self.leftover_090071_sites)
        self.n_in_leftover_205071 = len(self.leftover_205071_sites)
        self.n_in_leftover_009 = len(self.leftover_009_sites)
        self.n_in_leftover_090999 = len(self.leftover_090999_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover = len(self.leftover_sites)
        self.claim_holds = i_2gram_076_071_all_inside_leftover_n4_family(
            self.leftover_sites,
            self.i_sites,
        )

    def test_tokens_and_containers_are_cycle_170_family_not_retuned(self):
        """2-gram and four leftover n=4 stay the cycle-171/170/136 locks."""
        self.assertEqual(GRAM2, ("076", "071"))
        self.assertEqual(
            STANDING_MATCHING_LEFTOVERS,
            (
                LEFTOVER_N4_090071,
                LEFTOVER_N4_205071,
                LEFTOVER_N4_009,
                LEFTOVER_N4_090999,
            ),
        )
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertEqual(tuple(prior_171["tokens2"]), GRAM2)
        self.assertEqual(prior_171["N_I"], STANDING_N_I)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(
            tuple(tuple(row) for row in prior_171["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        prior_170 = self.survey["i_leftover_n4_076_071"]
        self.assertEqual(prior_170["cycle"], 170)
        self.assertEqual(prior_170["N_with_076_071"], 4)
        leftover_by_gram = {row[0]: row[3] for row in STANDING_WITH_ROWS}
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_090071], STANDING_LEFTOVER_090071_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_205071], STANDING_LEFTOVER_205071_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_009], STANDING_LEFTOVER_009_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_090999], STANDING_LEFTOVER_090999_SITES)
        leftover_grams = {row[0] for row in STANDING_LEFTOVER}
        self.assertIn(NEAR_MISS_071_065_071_999, leftover_grams)
        self.assertNotIn(NEAR_MISS_071_065_071_999, STANDING_MATCHING_LEFTOVERS)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_forty_three_sites_split_9_inside_34_leftover_and_claim_loses(self):
        """N_I=43: N_inside=9, N_leftover=34. Claim loses."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_on_i, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 43)
        self.assertEqual(self.n_on_i, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(self.membership, STANDING_MEMBERSHIP)
        self.assertEqual(self.leftover_090071_sites, STANDING_LEFTOVER_090071_COVERED)
        self.assertEqual(self.leftover_205071_sites, STANDING_LEFTOVER_205071_COVERED)
        self.assertEqual(self.leftover_009_sites, STANDING_LEFTOVER_009_COVERED)
        self.assertEqual(self.leftover_090999_sites, STANDING_LEFTOVER_090999_COVERED)
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.n_in_leftover_090071, STANDING_N_IN_LEFTOVER_090071)
        self.assertEqual(STANDING_N_IN_LEFTOVER_090071, 3)
        self.assertEqual(self.n_in_leftover_205071, STANDING_N_IN_LEFTOVER_205071)
        self.assertEqual(STANDING_N_IN_LEFTOVER_205071, 2)
        self.assertEqual(self.n_in_leftover_009, STANDING_N_IN_LEFTOVER_009)
        self.assertEqual(STANDING_N_IN_LEFTOVER_009, 2)
        self.assertEqual(self.n_in_leftover_090999, STANDING_N_IN_LEFTOVER_090999)
        self.assertEqual(STANDING_N_IN_LEFTOVER_090999, 2)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 9)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 34)
        self.assertEqual(self.n_inside + self.n_leftover, self.n_on_i)
        self.assertEqual(
            self.n_in_leftover_090071
            + self.n_in_leftover_205071
            + self.n_in_leftover_009
            + self.n_in_leftover_090999,
            9,
        )
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(side, SIDE_IA)
        for side, line, index in STANDING_LEFTOVER_090071_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_090071, index - 2, GRAM2)
            )
        for side, line, index in STANDING_LEFTOVER_205071_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_205071, index - 2, GRAM2)
            )
        for side, line, index in STANDING_LEFTOVER_009_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_009, index, GRAM2)
            )
        for side, line, index in STANDING_LEFTOVER_090999_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_090999, index, GRAM2)
            )
        for side, line, index in STANDING_LEFTOVER_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            for _cid, tokens, c_sites in STANDING_CONTAINERS:
                for c_side, c_line, c_start in c_sites:
                    if (c_side, c_line) != (side, line):
                        continue
                    self.assertFalse(
                        site_inside_container(stems, index, tokens, c_start, GRAM2)
                    )
        self.assertEqual(
            i_2gram_076_071_all_inside_leftover_n4_family(
                self.leftover_sites,
                self.i_sites,
            ),
            STANDING_I_2GRAM_076_071_ALL_INSIDE_LEFTOVER_N4_FAMILY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_2GRAM_076_071_ALL_INSIDE_LEFTOVER_N4_FAMILY,
        )
        self.assertFalse(STANDING_I_2GRAM_076_071_ALL_INSIDE_LEFTOVER_N4_FAMILY)
        self.assertTrue(HYPOTHESIS_ALL_INSIDE)
        self.assertEqual(
            STANDING_CLAIM,
            "i_2gram_076_071_all_inside_leftover_n4_family",
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_site_local_4grams_are_locked_and_not_the_family(self):
        """N_leftover=34; previous/next 4-grams are not the leftover family."""
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), 34)
        self.assertEqual(STANDING_LEFTOVER_SITES[0], (SIDE_IA, "Ia1", 86))
        self.assertEqual(STANDING_LEFTOVER_SITES[-1], (SIDE_IA, "Ia14", 166))
        self.assertEqual(self.local_4grams, tuple(
            (site, prev, nxt)
            for site, prev, nxt in zip(
                STANDING_LEFTOVER_SITES,
                STANDING_LEFTOVER_PREVIOUS_4GRAMS,
                STANDING_LEFTOVER_NEXT_4GRAMS,
                strict=True,
            )
        ))
        self.assertEqual(
            tuple(prev for _site, prev, _nxt in self.local_4grams),
            STANDING_LEFTOVER_PREVIOUS_4GRAMS,
        )
        self.assertEqual(
            tuple(nxt for _site, _prev, nxt in self.local_4grams),
            STANDING_LEFTOVER_NEXT_4GRAMS,
        )
        stems = line_stems_for_site(self.i_sides, STANDING_LEFTOVER_SITES[0])
        self.assertEqual(tuple(stems[84:88]), ("027", "200", "076", "071"))
        self.assertEqual(tuple(stems[86:88]), GRAM2)
        self.assertEqual(tuple(stems[86:90]), ("076", "071", "090", "606"))
        family = set(STANDING_MATCHING_LEFTOVERS)
        for prev, nxt in zip(
            STANDING_LEFTOVER_PREVIOUS_4GRAMS,
            STANDING_LEFTOVER_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertNotIn(prev, family)
            self.assertNotIn(nxt, family)
            self.assertEqual(prev[2:], GRAM2)
            self.assertEqual(nxt[:2], GRAM2)
        self.assertNotEqual(("027", "200", "076", "071"), NEAR_MISS_071_065_071_999)
        self.assertNotEqual(("076", "071", "090", "606"), NEAR_MISS_700_076_076_053)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_171_170_168_161_159_103_and_w_scoreboards_still_compute(self):
        """Cycle 171 I-only, 170 leftover 4, 168 family, 161 family, 159, 103, W stay."""
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_i_hits_are_forty_three_on_ia()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        prior_170 = TestMamariILeftoverN4076071Scoreboard()
        prior_170.setUp()
        prior_170.test_counts_4_of_27_and_hypothesis_n_4_holds()
        prior_170.test_survey_matches_computed_lock()
        prior_168 = TestMamariI3gram999090076InsideFamilyScoreboard()
        prior_168.setUp()
        prior_168.test_sixteen_sites_split_15_inside_1_leftover_and_claim_loses()
        prior_168.test_survey_matches_computed_lock()
        prior_161 = TestMamariIOverlap3gram076020010InsideFamilyScoreboard()
        prior_161.setUp()
        prior_161.test_twelve_sites_split_8_inside_4_leftover_and_claim_loses()
        prior_161.test_survey_matches_computed_lock()
        prior_159 = TestMamariILeftoverN4IndependentN5N3OverlapScoreboard()
        prior_159.setUp()
        prior_159.test_counts_5_of_27_and_hypothesis_n_5_holds()
        prior_159.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-172 inside-leftover-n=4 lock."""
        lock = self.survey["i_2gram_076_071_inside_family"]
        self.assertEqual(lock["cycle"], 172)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_inside_leftover_n4_family"])
        self.assertEqual(
            lock["hypothesis_all_inside_leftover_n4_family"],
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["leftover_n4_090071_tokens"]), LEFTOVER_N4_090071)
        self.assertEqual(tuple(lock["leftover_n4_205071_tokens"]), LEFTOVER_N4_205071)
        self.assertEqual(tuple(lock["leftover_n4_009_tokens"]), LEFTOVER_N4_009)
        self.assertEqual(tuple(lock["leftover_n4_090999_tokens"]), LEFTOVER_N4_090999)
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_LEFTOVERS],
            lock["family_leftover_n4"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_090071_container_sites"]),
            STANDING_LEFTOVER_090071_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_205071_container_sites"]),
            STANDING_LEFTOVER_205071_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_009_container_sites"]),
            STANDING_LEFTOVER_009_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_090999_container_sites"]),
            STANDING_LEFTOVER_090999_SITES,
        )
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 43)
        self.assertEqual(lock["i_hits"], STANDING_N_I)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_in_leftover_999_090_076_071"], STANDING_N_IN_LEFTOVER_090071)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_090071_covered_sites"]),
            STANDING_LEFTOVER_090071_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_999_205_076_071"], STANDING_N_IN_LEFTOVER_205071)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_205071_covered_sites"]),
            STANDING_LEFTOVER_205071_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_076_071_009_090"], STANDING_N_IN_LEFTOVER_009)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_009_covered_sites"]),
            STANDING_LEFTOVER_009_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_076_071_090_999"], STANDING_N_IN_LEFTOVER_090999)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_090999_covered_sites"]),
            STANDING_LEFTOVER_090999_COVERED,
        )
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 9)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 34)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(site) for site in STANDING_LEFTOVER_SITES],
            lock["leftover_sites"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_LEFTOVER_PREVIOUS_4GRAMS],
            lock["leftover_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_LEFTOVER_NEXT_4GRAMS],
            lock["leftover_next_4grams"],
        )
        self.assertEqual(lock["leftover_local_4grams"], leftover_local_4gram_rows())
        self.assertEqual(
            [list(members) for members in STANDING_MEMBERSHIP],
            lock["membership"],
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_2gram_076_071_all_inside_leftover_n4_family"])
        self.assertEqual(
            lock["i_2gram_076_071_all_inside_leftover_n4_family"],
            STANDING_I_2GRAM_076_071_ALL_INSIDE_LEFTOVER_N4_FAMILY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle161"])
        self.assertFalse(lock["same_as_cycle168"])
        self.assertTrue(lock["071_999_does_not_count"])
        self.assertTrue(lock["076_076_does_not_count"])
        self.assertTrue(lock["other_leftover_n4_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_076_071_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_020_010_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_independent_n5_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["cycle"], 170)
        self.assertTrue(
            self.survey["i_leftover_n4_076_071"][
                "i_leftover_n4_exactly_4_contain_076_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_076_071"]["N_with_076_071"], 4)
        self.assertEqual(self.survey["i_3gram_999_090_076_inside_family"]["cycle"], 168)
        self.assertFalse(
            self.survey["i_3gram_999_090_076_inside_family"][
                "i_3gram_999_090_076_all_inside_leftover_n4_family"
            ]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_inside_family"]["N_leftover"], 1)
        self.assertEqual(
            self.survey["i_overlap_3gram_076_020_010_inside_family"]["cycle"],
            161,
        )
        self.assertFalse(
            self.survey["i_overlap_3gram_076_020_010_inside_family"][
                "i_overlap_3gram_076_020_010_all_inside_known_family"
            ]
        )
        self.assertEqual(
            self.survey["i_overlap_3gram_076_020_010_inside_family"]["N_leftover"],
            4,
        )
        self.assertEqual(self.survey["i_leftover_n4_independent_n5_n3_overlap"]["cycle"], 159)
        self.assertTrue(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"][
                "i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"]["N_with_n3plus_overlap"],
            5,
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


class TestMamariI2gram076071InsideFamilyImageSnapshot(unittest.TestCase):
    """Cycle 172 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
