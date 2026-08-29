"""I's cycle-160 overlap 3-gram vs the locked known family.

Cycle 161 text-search lock. Uses already-vendored A–V and the
cycle-160 leftover overlap 3-gram 076 020 010 (I-only,
N_on_I=12). Does not retune that 3-gram or the four locked
containers. Does not vendor a new tablet. Does not scrape X.
W has no Barthel (cycle 100); skip W. Unpublished Ib is 0.
Does not redo H∩P∩Q n≥8 or G–K inventories. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents. Not a meaning
dictionary.

For each of the locked 12 I sites, whether the 3-gram sits as
a contiguous substring of independent 5-gram
400 070 076 020 010 or leftover n=4 maximals 090 076 020 010,
076 020 010 050, or 053 076 020 010. A site is inside a
container iff container start ≤ 3-gram start ≤ container
start + n_container - 3. Hypothesis: every I occurrence sits
inside that known family. Measured: N_inside=8, N_leftover=4
at Ia4[158]/Ia5[56]/Ia6[102]/Ia13[48]. Claim that can lose:
i_overlap_3gram_076_020_010_all_inside_known_family. The
claim is false. Same claim-shape as cycle 142 (076 010 079
all-inside-two-5grams lost, N_leftover=3). Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_independent_400_070_076_020_010_previous_stem_scoreboard import (
    LEFTOVER_N4_053,
    STANDING_I_SITES as STANDING_INDEPENDENT_5_SITES,
)
from tests.test_mamari_i_independent_nge4_maximals_scoreboard import (
    MAXIMAL_N5_400,
)
from tests.test_mamari_i_leftover_n4_independent_n5_n3_overlap_scoreboard import (
    STANDING_SHARED_076_020_010,
    TestMamariILeftoverN4IndependentN5N3OverlapScoreboard,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    STANDING_LEFTOVER,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_076_020_010_i_only_scoreboard import (
    GRAM3,
    STANDING_I_SITES,
    STANDING_N_ON_I,
    TestMamariIOverlap3gram076020010IOnlyScoreboard,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    STANDING_N_LEFTOVER as CYCLE142_N_LEFTOVER,
    TestMamariIOverlap3gramInsideTwo5gramsScoreboard,
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
CID_INDEPENDENT = "independent_400_070_076_020_010"
CID_LEFTOVER_090 = "leftover_090_076_020_010"
CID_LEFTOVER_050 = "leftover_076_020_010_050"
CID_LEFTOVER_053 = "leftover_053_076_020_010"
LEFTOVER_N4_090 = ("090", "076", "020", "010")
LEFTOVER_N4_050 = ("076", "020", "010", "050")
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N5 = 5
STANDING_IA_HITS = 12
STANDING_IB_HITS = 0
STANDING_INDEPENDENT_SITES = STANDING_INDEPENDENT_5_SITES
STANDING_LEFTOVER_090_SITES = (
    (SIDE_IA, "Ia2", 119),
    (SIDE_IA, "Ia4", 86),
    (SIDE_IA, "Ia5", 143),
    (SIDE_IA, "Ia12", 83),
)
STANDING_LEFTOVER_050_SITES = (
    (SIDE_IA, "Ia2", 120),
    (SIDE_IA, "Ia14", 110),
)
STANDING_LEFTOVER_053_SITES = (
    (SIDE_IA, "Ia12", 0),
    (SIDE_IA, "Ia14", 109),
)
STANDING_CONTAINERS = (
    (CID_INDEPENDENT, MAXIMAL_N5_400, STANDING_INDEPENDENT_SITES),
    (CID_LEFTOVER_090, LEFTOVER_N4_090, STANDING_LEFTOVER_090_SITES),
    (CID_LEFTOVER_050, LEFTOVER_N4_050, STANDING_LEFTOVER_050_SITES),
    (CID_LEFTOVER_053, LEFTOVER_N4_053, STANDING_LEFTOVER_053_SITES),
)
STANDING_N_IN_INDEPENDENT = 2
STANDING_N_IN_LEFTOVER_090 = 4
STANDING_N_IN_LEFTOVER_050 = 2
STANDING_N_IN_LEFTOVER_053 = 2
STANDING_N_INSIDE = 8
STANDING_N_LEFTOVER = 4
STANDING_INDEPENDENT_COVERED = (
    (SIDE_IA, "Ia13", 87),
    (SIDE_IA, "Ia14", 128),
)
STANDING_LEFTOVER_090_COVERED = (
    (SIDE_IA, "Ia2", 120),
    (SIDE_IA, "Ia4", 87),
    (SIDE_IA, "Ia5", 144),
    (SIDE_IA, "Ia12", 84),
)
STANDING_LEFTOVER_050_COVERED = (
    (SIDE_IA, "Ia2", 120),
    (SIDE_IA, "Ia14", 110),
)
STANDING_LEFTOVER_053_COVERED = (
    (SIDE_IA, "Ia12", 1),
    (SIDE_IA, "Ia14", 110),
)
STANDING_INSIDE_SITES = (
    (SIDE_IA, "Ia2", 120),
    (SIDE_IA, "Ia4", 87),
    (SIDE_IA, "Ia5", 144),
    (SIDE_IA, "Ia12", 1),
    (SIDE_IA, "Ia12", 84),
    (SIDE_IA, "Ia13", 87),
    (SIDE_IA, "Ia14", 110),
    (SIDE_IA, "Ia14", 128),
)
STANDING_LEFTOVER_SITES = (
    (SIDE_IA, "Ia4", 158),
    (SIDE_IA, "Ia5", 56),
    (SIDE_IA, "Ia6", 102),
    (SIDE_IA, "Ia13", 48),
)
STANDING_MEMBERSHIP = (
    (CID_LEFTOVER_090, CID_LEFTOVER_050),
    (CID_LEFTOVER_090,),
    (),
    (),
    (CID_LEFTOVER_090,),
    (),
    (CID_LEFTOVER_053,),
    (CID_LEFTOVER_090,),
    (),
    (CID_INDEPENDENT,),
    (CID_LEFTOVER_050, CID_LEFTOVER_053),
    (CID_INDEPENDENT,),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_overlap_3gram_076_020_010_all_inside_known_family"
STANDING_I_OVERLAP_3GRAM_076_020_010_ALL_INSIDE_KNOWN_FAMILY = False
STANDING_RESULT = "i_overlap_3gram_076_020_010_inside_family"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE142 = False


def site_inside_container(
    stems: list[str],
    gram3_start: int,
    container_tokens: tuple[str, ...],
    container_start: int,
    gram3: tuple[str, ...] = GRAM3,
) -> bool:
    """True iff gram3 at gram3_start is a contiguous run of the container."""
    n_container = len(container_tokens)
    n3 = len(gram3)
    if tuple(stems[gram3_start : gram3_start + n3]) != gram3:
        return False
    if tuple(stems[container_start : container_start + n_container]) != container_tokens:
        return False
    if not (container_start <= gram3_start <= container_start + n_container - n3):
        return False
    offset = gram3_start - container_start
    return container_tokens[offset : offset + n3] == gram3


def containers_for_site(
    i_sides: dict[str, list[list[str]]],
    site: tuple[str, str, int],
    containers: tuple[
        tuple[str, tuple[str, ...], tuple[tuple[str, str, int], ...]],
        ...,
    ] = STANDING_CONTAINERS,
    gram3: tuple[str, ...] = GRAM3,
) -> tuple[str, ...]:
    """Locked container ids that contain this 3-gram site, in family order."""
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
    """Per-site container membership for the locked I 3-gram hits."""
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
    """Sites inside no locked container."""
    return tuple(
        site
        for site, members in zip(sites, membership, strict=True)
        if members == ()
    )


def inside_sites_from_membership(
    sites: tuple[tuple[str, str, int], ...],
    membership: tuple[tuple[str, ...], ...],
) -> tuple[tuple[str, str, int], ...]:
    """Sites inside at least one locked container."""
    return tuple(
        site
        for site, members in zip(sites, membership, strict=True)
        if members
    )


def i_overlap_3gram_076_020_010_all_inside_known_family(
    leftover_sites: tuple[tuple[str, str, int], ...],
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff every I 3-gram site sits inside the known family.

    An empty I-site set is false here (the cycle-160 12 sites must
    be present and none may be leftover).
    """
    return bool(i_sites) and leftover_sites == ()


class TestIOverlap3gram076020010InsideFamilyHelpers(unittest.TestCase):
    """Helpers on cycle-160 overlap tokens. No CV, no LLM."""

    def test_inside_requires_contiguous_substring_and_window(self):
        """Family containers count; a near-miss or out-of-window site does not."""
        provider = MockProvider()
        self.assertEqual(GRAM3, ("076", "020", "010"))
        self.assertEqual(GRAM3, STANDING_SHARED_076_020_010)
        self.assertEqual(MAXIMAL_N5_400, ("400", "070", "076", "020", "010"))
        self.assertEqual(LEFTOVER_N4_090, ("090", "076", "020", "010"))
        self.assertEqual(LEFTOVER_N4_050, ("076", "020", "010", "050"))
        self.assertEqual(LEFTOVER_N4_053, ("053", "076", "020", "010"))
        self.assertEqual(MAXIMAL_N5_400[-STANDING_N3:], GRAM3)
        self.assertEqual(LEFTOVER_N4_090[-STANDING_N3:], GRAM3)
        self.assertEqual(LEFTOVER_N4_050[:STANDING_N3], GRAM3)
        self.assertEqual(LEFTOVER_N4_053[-STANDING_N3:], GRAM3)
        independent_line = ["023", "400", "070", "076", "020", "010", "073"]
        self.assertTrue(site_inside_container(independent_line, 3, MAXIMAL_N5_400, 1))
        self.assertFalse(site_inside_container(independent_line, 3, LEFTOVER_N4_090, 2))
        leftover_090_line = ["591", "090", "076", "020", "010", "050"]
        self.assertTrue(site_inside_container(leftover_090_line, 2, LEFTOVER_N4_090, 1))
        self.assertTrue(site_inside_container(leftover_090_line, 2, LEFTOVER_N4_050, 2))
        almost_070 = ["400", "071", "076", "020", "010"]
        self.assertFalse(site_inside_container(almost_070, 2, MAXIMAL_N5_400, 0))
        gapped = ["400", "070", "076", "006", "010"]
        self.assertFalse(site_inside_container(gapped, 2, MAXIMAL_N5_400, 0))
        out_of_window = ["400", "070", "076", "020", "010", "076", "020", "010"]
        self.assertTrue(site_inside_container(out_of_window, 2, MAXIMAL_N5_400, 0))
        self.assertFalse(site_inside_container(out_of_window, 5, MAXIMAL_N5_400, 0))
        self.assertFalse(site_inside_container(["076", "020", "010"], 0, MAXIMAL_N5_400, 0))
        self.assertEqual(provider.get_call_history(), [])

    def test_all_inside_requires_empty_leftover_and_present_sites(self):
        """Boolean is True only when I sites exist and leftover is empty."""
        provider = MockProvider()
        self.assertTrue(
            i_overlap_3gram_076_020_010_all_inside_known_family((), STANDING_I_SITES)
        )
        self.assertFalse(
            i_overlap_3gram_076_020_010_all_inside_known_family(
                STANDING_LEFTOVER_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertFalse(i_overlap_3gram_076_020_010_all_inside_known_family((), ()))
        self.assertEqual(
            STANDING_CLAIM,
            "i_overlap_3gram_076_020_010_all_inside_known_family",
        )
        self.assertFalse(STANDING_I_OVERLAP_3GRAM_076_020_010_ALL_INSIDE_KNOWN_FAMILY)
        self.assertNotEqual(
            STANDING_I_OVERLAP_3GRAM_076_020_010_ALL_INSIDE_KNOWN_FAMILY,
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(CYCLE142_N_LEFTOVER, 3)
        self.assertFalse(STANDING_SAME_AS_CYCLE142)
        self.assertEqual(provider.get_call_history(), [])

    def test_overlap_3gram_is_substring_of_each_locked_container(self):
        """3-gram is the locked shared run, not a retuned inventory."""
        provider = MockProvider()
        self.assertEqual(GRAM3, STANDING_SHARED_076_020_010)
        self.assertNotEqual(GRAM3, GRAM5)
        self.assertNotEqual(GRAM3, MAXIMAL_N5_400)
        self.assertTrue(is_contiguous_substring(GRAM3, MAXIMAL_N5_400))
        self.assertTrue(is_contiguous_substring(GRAM3, LEFTOVER_N4_090))
        self.assertTrue(is_contiguous_substring(GRAM3, LEFTOVER_N4_050))
        self.assertTrue(is_contiguous_substring(GRAM3, LEFTOVER_N4_053))
        self.assertFalse(is_contiguous_substring(GRAM3, GRAM5))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(len(GRAM3), STANDING_N3)
        self.assertEqual(STANDING_N3, 3)
        self.assertEqual(len(MAXIMAL_N5_400), STANDING_N5)
        self.assertEqual(len(LEFTOVER_N4_090), STANDING_N4)
        self.assertEqual(len(LEFTOVER_N4_050), STANDING_N4)
        self.assertEqual(len(LEFTOVER_N4_053), STANDING_N4)
        leftover_grams = {row[0] for row in STANDING_LEFTOVER}
        self.assertIn(LEFTOVER_N4_090, leftover_grams)
        self.assertIn(LEFTOVER_N4_050, leftover_grams)
        self.assertIn(LEFTOVER_N4_053, leftover_grams)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariIOverlap3gram076020010InsideFamilyScoreboard(unittest.TestCase):
    """Cited-fixture leftover overlap 3-gram known-family lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM3, self.i_sides)
        self.membership = membership_for_sites(self.i_sides, self.i_sites)
        self.independent_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_INDEPENDENT,
        )
        self.leftover_090_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_090,
        )
        self.leftover_050_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_050,
        )
        self.leftover_053_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_053,
        )
        self.inside_sites = inside_sites_from_membership(self.i_sites, self.membership)
        self.leftover_sites = leftover_sites_from_membership(
            self.i_sites,
            self.membership,
        )
        self.n_on_i = len(self.i_sites)
        self.n_in_independent = len(self.independent_sites)
        self.n_in_leftover_090 = len(self.leftover_090_sites)
        self.n_in_leftover_050 = len(self.leftover_050_sites)
        self.n_in_leftover_053 = len(self.leftover_053_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover = len(self.leftover_sites)
        self.claim_holds = i_overlap_3gram_076_020_010_all_inside_known_family(
            self.leftover_sites,
            self.i_sites,
        )

    def test_tokens_and_containers_are_cycle_160_family_not_retuned(self):
        """3-gram and four containers stay the cycle-160/159/136 locks."""
        self.assertEqual(GRAM3, STANDING_SHARED_076_020_010)
        self.assertEqual(GRAM3, ("076", "020", "010"))
        self.assertEqual(MAXIMAL_N5_400, ("400", "070", "076", "020", "010"))
        self.assertEqual(LEFTOVER_N4_090, ("090", "076", "020", "010"))
        self.assertEqual(LEFTOVER_N4_050, ("076", "020", "010", "050"))
        self.assertEqual(LEFTOVER_N4_053, ("053", "076", "020", "010"))
        prior_160 = self.survey["i_overlap_3gram_076_020_010_i_only"]
        self.assertEqual(prior_160["cycle"], 160)
        self.assertEqual(tuple(prior_160["tokens3"]), GRAM3)
        self.assertEqual(prior_160["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(prior_160["N_on_I"], 12)
        self.assertEqual(
            tuple(tuple(row) for row in prior_160["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertTrue(prior_160["i_overlap_3gram_076_020_010_is_i_only"])
        prior_159 = self.survey["i_leftover_n4_independent_n5_n3_overlap"]
        self.assertEqual(prior_159["cycle"], 159)
        self.assertEqual(prior_159["with_n3plus_overlap_count"], 5)
        self.assertEqual(self.survey["i_independent_n5_maximals_076"]["cycle"], 139)
        self.assertEqual(
            STANDING_INDEPENDENT_SITES,
            ((SIDE_IA, "Ia13", 85), (SIDE_IA, "Ia14", 126)),
        )
        leftover_by_gram = {row[0]: row[3] for row in STANDING_LEFTOVER}
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_090], STANDING_LEFTOVER_090_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_050], STANDING_LEFTOVER_050_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_053], STANDING_LEFTOVER_053_SITES)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_twelve_sites_split_8_inside_4_leftover_and_claim_loses(self):
        """N_on_I=12: N_inside=8, N_leftover=4. Claim loses."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_on_i, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, 12)
        self.assertEqual(self.n_on_i, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(self.membership, STANDING_MEMBERSHIP)
        self.assertEqual(self.independent_sites, STANDING_INDEPENDENT_COVERED)
        self.assertEqual(self.leftover_090_sites, STANDING_LEFTOVER_090_COVERED)
        self.assertEqual(self.leftover_050_sites, STANDING_LEFTOVER_050_COVERED)
        self.assertEqual(self.leftover_053_sites, STANDING_LEFTOVER_053_COVERED)
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.n_in_independent, STANDING_N_IN_INDEPENDENT)
        self.assertEqual(STANDING_N_IN_INDEPENDENT, 2)
        self.assertEqual(self.n_in_leftover_090, STANDING_N_IN_LEFTOVER_090)
        self.assertEqual(STANDING_N_IN_LEFTOVER_090, 4)
        self.assertEqual(self.n_in_leftover_050, STANDING_N_IN_LEFTOVER_050)
        self.assertEqual(STANDING_N_IN_LEFTOVER_050, 2)
        self.assertEqual(self.n_in_leftover_053, STANDING_N_IN_LEFTOVER_053)
        self.assertEqual(STANDING_N_IN_LEFTOVER_053, 2)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 8)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 4)
        self.assertEqual(self.n_inside + self.n_leftover, self.n_on_i)
        self.assertEqual(
            self.n_in_independent
            + self.n_in_leftover_090
            + self.n_in_leftover_050
            + self.n_in_leftover_053,
            10,
        )
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            self.assertEqual(side, SIDE_IA)
        for side, line, index in STANDING_INDEPENDENT_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, MAXIMAL_N5_400, index - 2)
            )
        for side, line, index in STANDING_LEFTOVER_090_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_090, index - 1)
            )
        for side, line, index in STANDING_LEFTOVER_050_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_050, index)
            )
        for side, line, index in STANDING_LEFTOVER_053_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_053, index - 1)
            )
        for side, line, index in STANDING_LEFTOVER_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3)
            for _cid, tokens, c_sites in STANDING_CONTAINERS:
                for c_side, c_line, c_start in c_sites:
                    if (c_side, c_line) != (side, line):
                        continue
                    self.assertFalse(
                        site_inside_container(stems, index, tokens, c_start)
                    )
        self.assertEqual(
            i_overlap_3gram_076_020_010_all_inside_known_family(
                self.leftover_sites,
                self.i_sites,
            ),
            STANDING_I_OVERLAP_3GRAM_076_020_010_ALL_INSIDE_KNOWN_FAMILY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_OVERLAP_3GRAM_076_020_010_ALL_INSIDE_KNOWN_FAMILY,
        )
        self.assertFalse(STANDING_I_OVERLAP_3GRAM_076_020_010_ALL_INSIDE_KNOWN_FAMILY)
        self.assertTrue(HYPOTHESIS_ALL_INSIDE)
        self.assertEqual(
            STANDING_CLAIM,
            "i_overlap_3gram_076_020_010_all_inside_known_family",
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_160_159_142_103_and_w_scoreboards_still_compute(self):
        """Cycle 160 I-only, 159 overlap, 142 family, 103 I-only, and W stay."""
        prior_160 = TestMamariIOverlap3gram076020010IOnlyScoreboard()
        prior_160.setUp()
        prior_160.test_i_hits_are_twelve_on_ia()
        prior_160.test_3gram_is_zero_off_i_and_i_only()
        prior_160.test_survey_matches_computed_lock()
        prior_159 = TestMamariILeftoverN4IndependentN5N3OverlapScoreboard()
        prior_159.setUp()
        prior_159.test_counts_5_of_27_and_hypothesis_n_5_holds()
        prior_159.test_survey_matches_computed_lock()
        prior_142 = TestMamariIOverlap3gramInsideTwo5gramsScoreboard()
        prior_142.setUp()
        prior_142.test_eight_sites_split_3_2_3_and_claim_loses()
        prior_142.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_103.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-161 inside-known-family lock."""
        lock = self.survey["i_overlap_3gram_076_020_010_inside_family"]
        self.assertEqual(lock["cycle"], 161)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_inside_known_family"])
        self.assertEqual(
            lock["hypothesis_all_inside_known_family"],
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(tuple(lock["tokens3"]), GRAM3)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(tuple(lock["independent_tokens5"]), MAXIMAL_N5_400)
        self.assertEqual(tuple(lock["leftover_n4_090_tokens"]), LEFTOVER_N4_090)
        self.assertEqual(tuple(lock["leftover_n4_050_tokens"]), LEFTOVER_N4_050)
        self.assertEqual(tuple(lock["leftover_n4_053_tokens"]), LEFTOVER_N4_053)
        self.assertEqual(
            tuple(tuple(row) for row in lock["independent_container_sites"]),
            STANDING_INDEPENDENT_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_090_container_sites"]),
            STANDING_LEFTOVER_090_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_050_container_sites"]),
            STANDING_LEFTOVER_050_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_053_container_sites"]),
            STANDING_LEFTOVER_053_SITES,
        )
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["i_hits"], STANDING_N_ON_I)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_in_independent_400_070_076_020_010"], STANDING_N_IN_INDEPENDENT)
        self.assertEqual(
            tuple(tuple(row) for row in lock["independent_covered_sites"]),
            STANDING_INDEPENDENT_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_090_076_020_010"], STANDING_N_IN_LEFTOVER_090)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_090_covered_sites"]),
            STANDING_LEFTOVER_090_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_076_020_010_050"], STANDING_N_IN_LEFTOVER_050)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_050_covered_sites"]),
            STANDING_LEFTOVER_050_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_053_076_020_010"], STANDING_N_IN_LEFTOVER_053)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_053_covered_sites"]),
            STANDING_LEFTOVER_053_COVERED,
        )
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(site) for site in STANDING_LEFTOVER_SITES],
            lock["leftover_sites"],
        )
        self.assertEqual(
            [list(members) for members in STANDING_MEMBERSHIP],
            lock["membership"],
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_overlap_3gram_076_020_010_all_inside_known_family"])
        self.assertEqual(
            lock["i_overlap_3gram_076_020_010_all_inside_known_family"],
            STANDING_I_OVERLAP_3GRAM_076_020_010_ALL_INSIDE_KNOWN_FAMILY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle142"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_020_010_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_independent_n5_n3_overlap_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_inside_two_5grams_unchanged"])
        self.assertTrue(lock["standing_i_overlap_3gram_076_010_079_i_only_unchanged"])
        self.assertTrue(lock["standing_i_independent_n5_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_maximals_076_unchanged"])
        self.assertTrue(lock["standing_i_independent_nge4_maximals_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_i_only"]["cycle"], 160)
        self.assertTrue(
            self.survey["i_overlap_3gram_076_020_010_i_only"][
                "i_overlap_3gram_076_020_010_is_i_only"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_076_020_010_i_only"]["N_on_I"], 12)
        self.assertEqual(self.survey["i_leftover_n4_independent_n5_n3_overlap"]["cycle"], 159)
        self.assertTrue(
            self.survey["i_leftover_n4_independent_n5_n3_overlap"][
                "i_leftover_n4_exactly_5_share_n3plus_with_independent_n5"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_inside_two_5grams"]["cycle"], 142)
        self.assertFalse(
            self.survey["i_overlap_3gram_inside_two_5grams"][
                "i_overlap_3gram_076_010_079_all_inside_two_5grams"
            ]
        )
        self.assertEqual(self.survey["i_overlap_3gram_inside_two_5grams"]["N_leftover"], 3)
        self.assertEqual(self.survey["i_overlap_3gram_076_010_079_i_only"]["cycle"], 141)
        self.assertTrue(
            self.survey["i_overlap_3gram_076_010_079_i_only"][
                "i_overlap_3gram_076_010_079_is_i_only"
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


class TestMamariIOverlap3gram076020010InsideFamilyImageSnapshot(unittest.TestCase):
    """Cycle 161 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
