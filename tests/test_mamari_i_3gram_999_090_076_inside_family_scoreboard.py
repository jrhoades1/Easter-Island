"""I's cycle-167 leftover 3-gram vs the locked leftover n=4 family.

Cycle 168 text-search lock. Uses already-vendored A–V and the
cycle-167 leftover 3-gram 999 090 076 (I-only, N_I=16, all Ia).
Does not retune that 3-gram or the seven leftover n=4 maximals
from cycle 166. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each of the locked 16 I sites, whether the 3-gram sits as
a contiguous substring of leftover n=4 maximals 999 090 076 070,
999 090 076 071, 000 999 090 076, 999 090 076 013,
999 090 076 005, 999 090 076 057, or 090 999 090 076. A site
is inside a container iff container start ≤ 3-gram start ≤
container start + n_container - 3. Other leftover n=4 (e.g.
999 021 090 076) do not count as this family. Independent I
5-grams do not contain this 3-gram. n=2 090 076 without 999
does not count. Hypothesis: every I occurrence sits inside
that leftover n=4 family. Measured: N_inside=15, N_leftover=1
at Ia1[1] (local 4-grams 602 999 090 076 / 999 090 076 012).
Claim that can lose:
i_3gram_999_090_076_all_inside_leftover_n4_family. The claim
is false. Same claim-shape as cycle 161 (076 020 010
all-inside-known-family lost, N_leftover=4). Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_i_only_scoreboard import (
    GRAM3,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_ON_I,
    TestMamariI3gram999090076IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_n4_999_090_076_scoreboard import (
    NEAR_MISS_999_021_090_076,
    NEAR_MISS_N2_090_076,
    STANDING_MATCHING_LEFTOVERS,
    STANDING_WITH_ROWS,
    TestMamariILeftoverN4999090076Scoreboard,
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
CID_LEFTOVER_070 = "leftover_999_090_076_070"
CID_LEFTOVER_071 = "leftover_999_090_076_071"
CID_LEFTOVER_000 = "leftover_000_999_090_076"
CID_LEFTOVER_013 = "leftover_999_090_076_013"
CID_LEFTOVER_005 = "leftover_999_090_076_005"
CID_LEFTOVER_057 = "leftover_999_090_076_057"
CID_LEFTOVER_090 = "leftover_090_999_090_076"
LEFTOVER_N4_070 = ("999", "090", "076", "070")
LEFTOVER_N4_071 = ("999", "090", "076", "071")
LEFTOVER_N4_000 = ("000", "999", "090", "076")
LEFTOVER_N4_013 = ("999", "090", "076", "013")
LEFTOVER_N4_005 = ("999", "090", "076", "005")
LEFTOVER_N4_057 = ("999", "090", "076", "057")
LEFTOVER_N4_090 = ("090", "999", "090", "076")
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_IA_HITS = 16
STANDING_IB_HITS = 0
STANDING_LEFTOVER_070_SITES = (
    (SIDE_IA, "Ia2", 9),
    (SIDE_IA, "Ia4", 111),
    (SIDE_IA, "Ia7", 67),
    (SIDE_IA, "Ia7", 128),
    (SIDE_IA, "Ia14", 139),
)
STANDING_LEFTOVER_071_SITES = (
    (SIDE_IA, "Ia4", 153),
    (SIDE_IA, "Ia5", 1),
    (SIDE_IA, "Ia5", 22),
)
STANDING_LEFTOVER_000_SITES = (
    (SIDE_IA, "Ia3", 35),
    (SIDE_IA, "Ia5", 0),
)
STANDING_LEFTOVER_013_SITES = (
    (SIDE_IA, "Ia3", 36),
    (SIDE_IA, "Ia6", 91),
)
STANDING_LEFTOVER_005_SITES = (
    (SIDE_IA, "Ia3", 70),
    (SIDE_IA, "Ia13", 108),
)
STANDING_LEFTOVER_057_SITES = (
    (SIDE_IA, "Ia9", 27),
    (SIDE_IA, "Ia9", 128),
)
STANDING_LEFTOVER_090_SITES = (
    (SIDE_IA, "Ia12", 45),
    (SIDE_IA, "Ia14", 138),
)
STANDING_CONTAINERS = (
    (CID_LEFTOVER_070, LEFTOVER_N4_070, STANDING_LEFTOVER_070_SITES),
    (CID_LEFTOVER_071, LEFTOVER_N4_071, STANDING_LEFTOVER_071_SITES),
    (CID_LEFTOVER_000, LEFTOVER_N4_000, STANDING_LEFTOVER_000_SITES),
    (CID_LEFTOVER_013, LEFTOVER_N4_013, STANDING_LEFTOVER_013_SITES),
    (CID_LEFTOVER_005, LEFTOVER_N4_005, STANDING_LEFTOVER_005_SITES),
    (CID_LEFTOVER_057, LEFTOVER_N4_057, STANDING_LEFTOVER_057_SITES),
    (CID_LEFTOVER_090, LEFTOVER_N4_090, STANDING_LEFTOVER_090_SITES),
)
STANDING_N_IN_LEFTOVER_070 = 5
STANDING_N_IN_LEFTOVER_071 = 3
STANDING_N_IN_LEFTOVER_000 = 2
STANDING_N_IN_LEFTOVER_013 = 2
STANDING_N_IN_LEFTOVER_005 = 2
STANDING_N_IN_LEFTOVER_057 = 2
STANDING_N_IN_LEFTOVER_090 = 2
STANDING_N_INSIDE = 15
STANDING_N_LEFTOVER = 1
STANDING_LEFTOVER_070_COVERED = (
    (SIDE_IA, "Ia2", 9),
    (SIDE_IA, "Ia4", 111),
    (SIDE_IA, "Ia7", 67),
    (SIDE_IA, "Ia7", 128),
    (SIDE_IA, "Ia14", 139),
)
STANDING_LEFTOVER_071_COVERED = (
    (SIDE_IA, "Ia4", 153),
    (SIDE_IA, "Ia5", 1),
    (SIDE_IA, "Ia5", 22),
)
STANDING_LEFTOVER_000_COVERED = (
    (SIDE_IA, "Ia3", 36),
    (SIDE_IA, "Ia5", 1),
)
STANDING_LEFTOVER_013_COVERED = (
    (SIDE_IA, "Ia3", 36),
    (SIDE_IA, "Ia6", 91),
)
STANDING_LEFTOVER_005_COVERED = (
    (SIDE_IA, "Ia3", 70),
    (SIDE_IA, "Ia13", 108),
)
STANDING_LEFTOVER_057_COVERED = (
    (SIDE_IA, "Ia9", 27),
    (SIDE_IA, "Ia9", 128),
)
STANDING_LEFTOVER_090_COVERED = (
    (SIDE_IA, "Ia12", 46),
    (SIDE_IA, "Ia14", 139),
)
STANDING_INSIDE_SITES = (
    (SIDE_IA, "Ia2", 9),
    (SIDE_IA, "Ia3", 36),
    (SIDE_IA, "Ia3", 70),
    (SIDE_IA, "Ia4", 111),
    (SIDE_IA, "Ia4", 153),
    (SIDE_IA, "Ia5", 1),
    (SIDE_IA, "Ia5", 22),
    (SIDE_IA, "Ia6", 91),
    (SIDE_IA, "Ia7", 67),
    (SIDE_IA, "Ia7", 128),
    (SIDE_IA, "Ia9", 27),
    (SIDE_IA, "Ia9", 128),
    (SIDE_IA, "Ia12", 46),
    (SIDE_IA, "Ia13", 108),
    (SIDE_IA, "Ia14", 139),
)
STANDING_LEFTOVER_SITES = (
    (SIDE_IA, "Ia1", 1),
)
STANDING_LEFTOVER_PREVIOUS_4GRAMS = (
    ("602", "999", "090", "076"),
)
STANDING_LEFTOVER_NEXT_4GRAMS = (
    ("999", "090", "076", "012"),
)
STANDING_MEMBERSHIP = (
    (),
    (CID_LEFTOVER_070,),
    (CID_LEFTOVER_000, CID_LEFTOVER_013),
    (CID_LEFTOVER_005,),
    (CID_LEFTOVER_070,),
    (CID_LEFTOVER_071,),
    (CID_LEFTOVER_071, CID_LEFTOVER_000),
    (CID_LEFTOVER_071,),
    (CID_LEFTOVER_013,),
    (CID_LEFTOVER_070,),
    (CID_LEFTOVER_070,),
    (CID_LEFTOVER_057,),
    (CID_LEFTOVER_057,),
    (CID_LEFTOVER_090,),
    (CID_LEFTOVER_005,),
    (CID_LEFTOVER_070, CID_LEFTOVER_090),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_3gram_999_090_076_all_inside_leftover_n4_family"
STANDING_I_3GRAM_999_090_076_ALL_INSIDE_LEFTOVER_N4_FAMILY = False
STANDING_RESULT = "i_3gram_999_090_076_inside_family"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE161 = False
STANDING_N2_DOES_NOT_COUNT = True
STANDING_OTHER_LEFTOVER_N4_DOES_NOT_COUNT = True


def containers_for_site(
    i_sides: dict[str, list[list[str]]],
    site: tuple[str, str, int],
    containers: tuple[
        tuple[str, tuple[str, ...], tuple[tuple[str, str, int], ...]],
        ...,
    ] = STANDING_CONTAINERS,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...]:
    """Locked leftover n=4 ids that contain this 3-gram site, in family order."""
    stems = line_stems_for_site(i_sides, site)
    side, line, gram3_start = site
    members = []
    for cid, tokens, c_sites in containers:
        for c_side, c_line, c_start in c_sites:
            if (c_side, c_line) != (side, line):
                continue
            if site_inside_container(stems, gram3_start, tokens, c_start, gram3):
                members.append(cid)
                break
    return tuple(members)


def membership_for_sites(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
    containers: tuple[
        tuple[str, tuple[str, ...], tuple[tuple[str, str, int], ...]],
        ...,
    ] = STANDING_CONTAINERS,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[tuple[str, ...], ...]:
    """Per-site leftover n=4 membership for the locked I 3-gram hits."""
    return tuple(
        containers_for_site(i_sides, site, containers, gram3) for site in sites
    )


def sites_with_container(
    sites: tuple[tuple[str, str, int], ...],
    membership: tuple[tuple[str, ...], ...],
    cid: str,
) -> tuple[tuple[str, str, int], ...]:
    """Sites whose membership includes cid."""
    return tuple(
        site
        for site, members in zip(sites, membership, strict=True)
        if cid in members
    )


def leftover_sites_from_membership(
    sites: tuple[tuple[str, str, int], ...],
    membership: tuple[tuple[str, ...], ...],
) -> tuple[tuple[str, str, int], ...]:
    """Sites inside no locked leftover n=4 container."""
    return tuple(
        site
        for site, members in zip(sites, membership, strict=True)
        if members == ()
    )


def inside_sites_from_membership(
    sites: tuple[tuple[str, str, int], ...],
    membership: tuple[tuple[str, ...], ...],
) -> tuple[tuple[str, str, int], ...]:
    """Sites inside at least one locked leftover n=4 container."""
    return tuple(
        site
        for site, members in zip(sites, membership, strict=True)
        if members
    )


def leftover_local_4grams(
    i_sides: dict[str, list[list[str]]],
    leftover_sites: tuple[tuple[str, str, int], ...],
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[tuple[tuple[str, str, int], tuple[str, ...] | None, tuple[str, ...] | None], ...]:
    """Previous and next 4-grams (one stem Y / X) at leftover 3-gram sites."""
    rows = []
    n3 = len(gram3)
    for site in leftover_sites:
        stems = line_stems_for_site(i_sides, site)
        _side, _line, start = site
        previous = tuple(stems[start - 1 : start + n3]) if start >= 1 else None
        nxt = tuple(stems[start : start + n3 + 1]) if start + n3 < len(stems) else None
        rows.append((site, previous, nxt))
    return tuple(rows)


def i_3gram_999_090_076_all_inside_leftover_n4_family(
    leftover_sites: tuple[tuple[str, str, int], ...],
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff every I 3-gram site sits inside the leftover n=4 family.

    An empty I-site set is false here (the cycle-167 16 sites must
    be present and none may be leftover).
    """
    return bool(i_sites) and leftover_sites == ()


class TestI3gram999090076InsideFamilyHelpers(unittest.TestCase):
    """Helpers on cycle-167 leftover tokens. No CV, no LLM."""

    def test_inside_requires_contiguous_substring_and_window(self):
        """Family leftover n=4 count; a near-miss or out-of-window site does not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(LEFTOVER_N4_070, ("999", "090", "076", "070"))
        self.assertEqual(LEFTOVER_N4_071, ("999", "090", "076", "071"))
        self.assertEqual(LEFTOVER_N4_000, ("000", "999", "090", "076"))
        self.assertEqual(LEFTOVER_N4_013, ("999", "090", "076", "013"))
        self.assertEqual(LEFTOVER_N4_005, ("999", "090", "076", "005"))
        self.assertEqual(LEFTOVER_N4_057, ("999", "090", "076", "057"))
        self.assertEqual(LEFTOVER_N4_090, ("090", "999", "090", "076"))
        self.assertEqual(LEFTOVER_N4_070[:STANDING_N3], GRAM3)
        self.assertEqual(LEFTOVER_N4_000[-STANDING_N3:], GRAM3)
        self.assertEqual(LEFTOVER_N4_090[-STANDING_N3:], GRAM3)
        prefix_line = ["070", "999", "090", "076", "070"]
        self.assertTrue(site_inside_container(prefix_line, 1, LEFTOVER_N4_070, 1, GRAM3))
        suffix_line = ["000", "999", "090", "076", "013"]
        self.assertTrue(site_inside_container(suffix_line, 1, LEFTOVER_N4_000, 0, GRAM3))
        self.assertTrue(site_inside_container(suffix_line, 1, LEFTOVER_N4_013, 1, GRAM3))
        leftover_site = ["602", "999", "090", "076", "012"]
        self.assertFalse(site_inside_container(leftover_site, 1, LEFTOVER_N4_000, 0, GRAM3))
        self.assertFalse(site_inside_container(leftover_site, 1, LEFTOVER_N4_070, 1, GRAM3))
        almost_021 = ["999", "021", "090", "076"]
        self.assertFalse(site_inside_container(almost_021, 1, LEFTOVER_N4_000, 0, GRAM3))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_999_021_090_076))
        n2_only = ["600", "090", "076", "011"]
        self.assertFalse(site_inside_container(n2_only, 1, LEFTOVER_N4_070, 0, GRAM3))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_N2_090_076))
        out_of_window = ["999", "090", "076", "070", "999", "090", "076"]
        self.assertTrue(site_inside_container(out_of_window, 0, LEFTOVER_N4_070, 0, GRAM3))
        self.assertFalse(site_inside_container(out_of_window, 4, LEFTOVER_N4_070, 0, GRAM3))
        self.assertFalse(site_inside_container(["999", "090", "076"], 0, LEFTOVER_N4_070, 0, GRAM3))
        self.assertTrue(STANDING_N2_DOES_NOT_COUNT)
        self.assertTrue(STANDING_OTHER_LEFTOVER_N4_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_inside_requires_empty_leftover_and_present_sites(self):
        """Boolean is True only when I sites exist and leftover is empty."""
        provider = MockProvider()
        self.assertTrue(
            i_3gram_999_090_076_all_inside_leftover_n4_family((), STANDING_I_SITES)
        )
        self.assertFalse(
            i_3gram_999_090_076_all_inside_leftover_n4_family(
                STANDING_LEFTOVER_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertFalse(i_3gram_999_090_076_all_inside_leftover_n4_family((), ()))
        self.assertEqual(
            STANDING_CLAIM,
            "i_3gram_999_090_076_all_inside_leftover_n4_family",
        )
        self.assertFalse(STANDING_I_3GRAM_999_090_076_ALL_INSIDE_LEFTOVER_N4_FAMILY)
        self.assertNotEqual(
            STANDING_I_3GRAM_999_090_076_ALL_INSIDE_LEFTOVER_N4_FAMILY,
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(CYCLE161_N_LEFTOVER, 4)
        self.assertFalse(STANDING_SAME_AS_CYCLE161)
        self.assertEqual(provider.get_call_history(), [])

    def test_3gram_is_substring_of_each_locked_leftover_n4(self):
        """3-gram is the locked shared run, not a retuned inventory."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        leftover_grams = {row[0] for row in STANDING_LEFTOVER}
        for tokens in STANDING_MATCHING_LEFTOVERS:
            self.assertTrue(is_contiguous_substring(GRAM3, tokens))
            self.assertEqual(len(tokens), STANDING_N4)
            self.assertIn(tokens, leftover_grams)
        self.assertEqual(STANDING_MATCHING_LEFTOVERS, (
            LEFTOVER_N4_070,
            LEFTOVER_N4_071,
            LEFTOVER_N4_000,
            LEFTOVER_N4_013,
            LEFTOVER_N4_005,
            LEFTOVER_N4_057,
            LEFTOVER_N4_090,
        ))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_N2_090_076))
        self.assertFalse(is_contiguous_substring(GRAM3, NEAR_MISS_999_021_090_076))
        self.assertIn(NEAR_MISS_N2_090_076, leftover_grams)
        self.assertIn(NEAR_MISS_999_021_090_076, leftover_grams)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI3gram999090076InsideFamilyScoreboard(unittest.TestCase):
    """Cited-fixture leftover 3-gram leftover-n=4-family lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM3, self.i_sides)
        self.membership = membership_for_sites(self.i_sides, self.i_sites)
        self.leftover_070_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_070,
        )
        self.leftover_071_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_071,
        )
        self.leftover_000_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_000,
        )
        self.leftover_013_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_013,
        )
        self.leftover_005_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_005,
        )
        self.leftover_057_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_057,
        )
        self.leftover_090_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_090,
        )
        self.inside_sites = inside_sites_from_membership(self.i_sites, self.membership)
        self.leftover_sites = leftover_sites_from_membership(
            self.i_sites,
            self.membership,
        )
        self.local_4grams = leftover_local_4grams(self.i_sides, self.leftover_sites)
        self.n_on_i = len(self.i_sites)
        self.n_in_leftover_070 = len(self.leftover_070_sites)
        self.n_in_leftover_071 = len(self.leftover_071_sites)
        self.n_in_leftover_000 = len(self.leftover_000_sites)
        self.n_in_leftover_013 = len(self.leftover_013_sites)
        self.n_in_leftover_005 = len(self.leftover_005_sites)
        self.n_in_leftover_057 = len(self.leftover_057_sites)
        self.n_in_leftover_090 = len(self.leftover_090_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover = len(self.leftover_sites)
        self.claim_holds = i_3gram_999_090_076_all_inside_leftover_n4_family(
            self.leftover_sites,
            self.i_sites,
        )

    def test_tokens_and_containers_are_cycle_166_family_not_retuned(self):
        """3-gram and seven leftover n=4 stay the cycle-167/166/136 locks."""
        self.assertEqual(GRAM3, ("999", "090", "076"))
        self.assertEqual(
            STANDING_MATCHING_LEFTOVERS,
            (
                LEFTOVER_N4_070,
                LEFTOVER_N4_071,
                LEFTOVER_N4_000,
                LEFTOVER_N4_013,
                LEFTOVER_N4_005,
                LEFTOVER_N4_057,
                LEFTOVER_N4_090,
            ),
        )
        prior_167 = self.survey["i_3gram_999_090_076_i_only"]
        self.assertEqual(prior_167["cycle"], 167)
        self.assertEqual(tuple(prior_167["tokens3"]), GRAM3)
        self.assertEqual(prior_167["N_I"], STANDING_N_I)
        self.assertEqual(prior_167["N_I"], 16)
        self.assertEqual(
            tuple(tuple(row) for row in prior_167["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertTrue(prior_167["i_3gram_999_090_076_i_only"])
        prior_166 = self.survey["i_leftover_n4_999_090_076"]
        self.assertEqual(prior_166["cycle"], 166)
        self.assertEqual(prior_166["N_with_999_090_076"], 7)
        leftover_by_gram = {row[0]: row[3] for row in STANDING_WITH_ROWS}
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_070], STANDING_LEFTOVER_070_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_071], STANDING_LEFTOVER_071_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_000], STANDING_LEFTOVER_000_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_013], STANDING_LEFTOVER_013_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_005], STANDING_LEFTOVER_005_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_057], STANDING_LEFTOVER_057_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_090], STANDING_LEFTOVER_090_SITES)
        leftover_grams = {row[0] for row in STANDING_LEFTOVER}
        self.assertIn(NEAR_MISS_999_021_090_076, leftover_grams)
        self.assertNotIn(NEAR_MISS_999_021_090_076, STANDING_MATCHING_LEFTOVERS)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_sixteen_sites_split_15_inside_1_leftover_and_claim_loses(self):
        """N_I=16: N_inside=15, N_leftover=1 at Ia1[1]. Claim loses."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_on_i, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 16)
        self.assertEqual(self.n_on_i, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(self.membership, STANDING_MEMBERSHIP)
        self.assertEqual(self.leftover_070_sites, STANDING_LEFTOVER_070_COVERED)
        self.assertEqual(self.leftover_071_sites, STANDING_LEFTOVER_071_COVERED)
        self.assertEqual(self.leftover_000_sites, STANDING_LEFTOVER_000_COVERED)
        self.assertEqual(self.leftover_013_sites, STANDING_LEFTOVER_013_COVERED)
        self.assertEqual(self.leftover_005_sites, STANDING_LEFTOVER_005_COVERED)
        self.assertEqual(self.leftover_057_sites, STANDING_LEFTOVER_057_COVERED)
        self.assertEqual(self.leftover_090_sites, STANDING_LEFTOVER_090_COVERED)
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.n_in_leftover_070, STANDING_N_IN_LEFTOVER_070)
        self.assertEqual(STANDING_N_IN_LEFTOVER_070, 5)
        self.assertEqual(self.n_in_leftover_071, STANDING_N_IN_LEFTOVER_071)
        self.assertEqual(STANDING_N_IN_LEFTOVER_071, 3)
        self.assertEqual(self.n_in_leftover_000, STANDING_N_IN_LEFTOVER_000)
        self.assertEqual(STANDING_N_IN_LEFTOVER_000, 2)
        self.assertEqual(self.n_in_leftover_013, STANDING_N_IN_LEFTOVER_013)
        self.assertEqual(STANDING_N_IN_LEFTOVER_013, 2)
        self.assertEqual(self.n_in_leftover_005, STANDING_N_IN_LEFTOVER_005)
        self.assertEqual(STANDING_N_IN_LEFTOVER_005, 2)
        self.assertEqual(self.n_in_leftover_057, STANDING_N_IN_LEFTOVER_057)
        self.assertEqual(STANDING_N_IN_LEFTOVER_057, 2)
        self.assertEqual(self.n_in_leftover_090, STANDING_N_IN_LEFTOVER_090)
        self.assertEqual(STANDING_N_IN_LEFTOVER_090, 2)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 15)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 1)
        self.assertEqual(self.n_inside + self.n_leftover, self.n_on_i)
        self.assertEqual(
            self.n_in_leftover_070
            + self.n_in_leftover_071
            + self.n_in_leftover_000
            + self.n_in_leftover_013
            + self.n_in_leftover_005
            + self.n_in_leftover_057
            + self.n_in_leftover_090,
            18,
        )
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertEqual(side, SIDE_IA)
        for side, line, index in STANDING_LEFTOVER_070_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_070, index, GRAM3)
            )
        for side, line, index in STANDING_LEFTOVER_071_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_071, index, GRAM3)
            )
        for side, line, index in STANDING_LEFTOVER_000_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_000, index - 1, GRAM3)
            )
        for side, line, index in STANDING_LEFTOVER_013_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_013, index, GRAM3)
            )
        for side, line, index in STANDING_LEFTOVER_005_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_005, index, GRAM3)
            )
        for side, line, index in STANDING_LEFTOVER_057_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_057, index, GRAM3)
            )
        for side, line, index in STANDING_LEFTOVER_090_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_090, index - 1, GRAM3)
            )
        for side, line, index in STANDING_LEFTOVER_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            for _cid, tokens, c_sites in STANDING_CONTAINERS:
                for c_side, c_line, c_start in c_sites:
                    if (c_side, c_line) != (side, line):
                        continue
                    self.assertFalse(
                        site_inside_container(stems, index, tokens, c_start, GRAM3)
                    )
        self.assertEqual(
            i_3gram_999_090_076_all_inside_leftover_n4_family(
                self.leftover_sites,
                self.i_sites,
            ),
            STANDING_I_3GRAM_999_090_076_ALL_INSIDE_LEFTOVER_N4_FAMILY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_3GRAM_999_090_076_ALL_INSIDE_LEFTOVER_N4_FAMILY,
        )
        self.assertFalse(STANDING_I_3GRAM_999_090_076_ALL_INSIDE_LEFTOVER_N4_FAMILY)
        self.assertTrue(HYPOTHESIS_ALL_INSIDE)
        self.assertEqual(
            STANDING_CLAIM,
            "i_3gram_999_090_076_all_inside_leftover_n4_family",
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_site_local_4grams_are_602_and_012(self):
        """N_leftover=1 at I / Ia / Ia1 / 1; local 4-grams are not the family."""
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(STANDING_LEFTOVER_SITES, ((SIDE_IA, "Ia1", 1),))
        self.assertEqual(self.local_4grams, (
            (
                (SIDE_IA, "Ia1", 1),
                ("602", "999", "090", "076"),
                ("999", "090", "076", "012"),
            ),
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
        self.assertEqual(tuple(stems[0:4]), ("602", "999", "090", "076"))
        self.assertEqual(tuple(stems[1:4]), GRAM3)
        self.assertEqual(tuple(stems[1:5]), ("999", "090", "076", "012"))
        family = set(STANDING_MATCHING_LEFTOVERS)
        self.assertNotIn(("602", "999", "090", "076"), family)
        self.assertNotIn(("999", "090", "076", "012"), family)
        self.assertNotEqual(("602", "999", "090", "076"), NEAR_MISS_999_021_090_076)
        self.assertNotEqual(("999", "090", "076", "012"), NEAR_MISS_N2_090_076)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_167_166_161_159_103_and_w_scoreboards_still_compute(self):
        """Cycle 167 I-only, 166 leftover 7, 161 family, 159 n≥3, 103, W stay."""
        prior_167 = TestMamariI3gram999090076IOnlyScoreboard()
        prior_167.setUp()
        prior_167.test_i_hits_are_sixteen_on_ia()
        prior_167.test_3gram_is_zero_off_i_and_i_only()
        prior_167.test_survey_matches_computed_lock()
        prior_166 = TestMamariILeftoverN4999090076Scoreboard()
        prior_166.setUp()
        prior_166.test_counts_7_of_27_and_hypothesis_n_7_holds()
        prior_166.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-168 inside-leftover-n=4 lock."""
        lock = self.survey["i_3gram_999_090_076_inside_family"]
        self.assertEqual(lock["cycle"], 168)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_inside_leftover_n4_family"])
        self.assertEqual(
            lock["hypothesis_all_inside_leftover_n4_family"],
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(tuple(lock["leftover_n4_070_tokens"]), LEFTOVER_N4_070)
        self.assertEqual(tuple(lock["leftover_n4_071_tokens"]), LEFTOVER_N4_071)
        self.assertEqual(tuple(lock["leftover_n4_000_tokens"]), LEFTOVER_N4_000)
        self.assertEqual(tuple(lock["leftover_n4_013_tokens"]), LEFTOVER_N4_013)
        self.assertEqual(tuple(lock["leftover_n4_005_tokens"]), LEFTOVER_N4_005)
        self.assertEqual(tuple(lock["leftover_n4_057_tokens"]), LEFTOVER_N4_057)
        self.assertEqual(tuple(lock["leftover_n4_090_tokens"]), LEFTOVER_N4_090)
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_LEFTOVERS],
            lock["family_leftover_n4"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_070_container_sites"]),
            STANDING_LEFTOVER_070_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_071_container_sites"]),
            STANDING_LEFTOVER_071_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_000_container_sites"]),
            STANDING_LEFTOVER_000_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_013_container_sites"]),
            STANDING_LEFTOVER_013_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_005_container_sites"]),
            STANDING_LEFTOVER_005_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_057_container_sites"]),
            STANDING_LEFTOVER_057_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_090_container_sites"]),
            STANDING_LEFTOVER_090_SITES,
        )
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 16)
        self.assertEqual(lock["i_hits"], STANDING_N_I)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_in_leftover_999_090_076_070"], STANDING_N_IN_LEFTOVER_070)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_070_covered_sites"]),
            STANDING_LEFTOVER_070_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_999_090_076_071"], STANDING_N_IN_LEFTOVER_071)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_071_covered_sites"]),
            STANDING_LEFTOVER_071_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_000_999_090_076"], STANDING_N_IN_LEFTOVER_000)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_000_covered_sites"]),
            STANDING_LEFTOVER_000_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_999_090_076_013"], STANDING_N_IN_LEFTOVER_013)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_013_covered_sites"]),
            STANDING_LEFTOVER_013_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_999_090_076_005"], STANDING_N_IN_LEFTOVER_005)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_005_covered_sites"]),
            STANDING_LEFTOVER_005_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_999_090_076_057"], STANDING_N_IN_LEFTOVER_057)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_057_covered_sites"]),
            STANDING_LEFTOVER_057_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_090_999_090_076"], STANDING_N_IN_LEFTOVER_090)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_090_covered_sites"]),
            STANDING_LEFTOVER_090_COVERED,
        )
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 15)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 1)
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
        self.assertEqual(
            lock["leftover_local_4grams"],
            [
                {
                    "tablet": "I",
                    "side": "Ia",
                    "line": "Ia1",
                    "index": 1,
                    "previous_4gram": ["602", "999", "090", "076"],
                    "next_4gram": ["999", "090", "076", "012"],
                }
            ],
        )
        self.assertEqual(
            [list(members) for members in STANDING_MEMBERSHIP],
            lock["membership"],
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_3gram_999_090_076_all_inside_leftover_n4_family"])
        self.assertEqual(
            lock["i_3gram_999_090_076_all_inside_leftover_n4_family"],
            STANDING_I_3GRAM_999_090_076_ALL_INSIDE_LEFTOVER_N4_FAMILY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle161"])
        self.assertTrue(lock["n2_090_076_without_999_does_not_count"])
        self.assertTrue(lock["other_leftover_n4_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_999_090_076_unchanged"])
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
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["cycle"], 167)
        self.assertTrue(
            self.survey["i_3gram_999_090_076_i_only"]["i_3gram_999_090_076_i_only"]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_I"], 16)
        self.assertEqual(self.survey["i_3gram_999_090_076_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_leftover_n4_999_090_076"]["cycle"], 166)
        self.assertTrue(
            self.survey["i_leftover_n4_999_090_076"][
                "i_leftover_n4_exactly_7_contain_999_090_076"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_999_090_076"]["N_with_999_090_076"],
            7,
        )
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


class TestMamariI3gram999090076InsideFamilyImageSnapshot(unittest.TestCase):
    """Cycle 168 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
