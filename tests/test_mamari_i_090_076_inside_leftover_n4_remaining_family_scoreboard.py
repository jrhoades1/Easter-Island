"""I's cycle-223 leftover remaining 2-gram vs leftover n=4 remaining family.

Cycle 224 text-search lock. Uses already-vendored A–V and the
cycle-223 leftover remaining 2-gram 090 076 (I-only lost, N_I=69
all Ia, N_off_I=3 on T). Does not retune that 2-gram or the five
leftover n=4 remaining maximals from cycle 222. Does not vendor
a new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

For each of the locked 69 I sites, whether the 2-gram sits as
a contiguous substring of leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600. A site at
tablet/side/line/index i is inside the family iff there exists
a family leftover 4-gram L such that 090 076 at i is a
contiguous substring of L aligned at that location (the 2-gram
occupies positions 0-1, 1-2, or 2-3 of L starting at i, i-1,
or i-2 respectively, and those four tokens match L). Other
leftover n=4 (e.g. 999 090 076 070, 000 999 090 076) do not
count as this remaining family. 076 071 and 076 070 do not
count as this 2-gram. Off-I T sites are not this cycle.
I-only of leftover extra 4-grams is leftover-of-leftover for
a later cycle. Hypothesis: every I occurrence sits inside
that leftover n=4 remaining family. Measured: N_inside=13,
N_leftover=56. Claim that can lose:
i_090_076_all_inside_leftover_n4_remaining_family. The claim
is false. Same claim-shape as cycle 172 (076 071 all-inside
leftover n=4 family lost, N_leftover=34) and cycle 168
(999 090 076 all-inside leftover n=4 family lost,
N_leftover=1 at Ia1[1]). Do not retune leftover n=4,
076-cells, or any detector.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_inside_family_scoreboard import (
    STANDING_N_LEFTOVER as CYCLE172_N_LEFTOVER,
    leftover_local_4grams,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_OFF_I,
    STANDING_N_ON_I,
    STANDING_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_999_090_076_inside_family_scoreboard import (
    STANDING_N_LEFTOVER as CYCLE168_N_LEFTOVER,
    TestMamariI3gram999090076InsideFamilyScoreboard,
    inside_sites_from_membership,
    leftover_sites_from_membership,
    membership_for_sites,
    sites_with_container,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
    STANDING_LEFTOVER,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
    STANDING_MATCHING_LEFTOVERS,
    STANDING_N_REMAINING as CYCLE222_N_REMAINING,
    STANDING_WITH_ROWS,
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
from tests.test_mamari_i_overlap_3gram_076_020_010_inside_family_scoreboard import (
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
CID_LEFTOVER_020010 = "leftover_090_076_020_010"
CID_LEFTOVER_021087 = "leftover_021_090_076_087"
CID_LEFTOVER_600011 = "leftover_600_090_076_011"
CID_LEFTOVER_999021 = "leftover_999_021_090_076"
CID_LEFTOVER_057600 = "leftover_090_076_057_600"
LEFTOVER_N4_020010 = ("090", "076", "020", "010")
LEFTOVER_N4_021087 = ("021", "090", "076", "087")
LEFTOVER_N4_600011 = ("600", "090", "076", "011")
LEFTOVER_N4_999021 = ("999", "021", "090", "076")
LEFTOVER_N4_057600 = ("090", "076", "057", "600")
NEAR_MISS_999_090_076_070 = ("999", "090", "076", "070")
NEAR_MISS_999_090_076_071 = ("999", "090", "076", "071")
NEAR_MISS_000_999_090_076 = ("000", "999", "090", "076")
NEAR_MISS_090_999_090_076 = ("090", "999", "090", "076")
NEAR_MISS_028_076_011_076 = ("028", "076", "011", "076")
NEAR_MISS_071_065_071_999 = EXCEPTION_GRAM
STANDING_N2 = 2
STANDING_N4 = 4
STANDING_IA_HITS = 69
STANDING_IB_HITS = 0
STANDING_LEFTOVER_020010_SITES = (
    (SIDE_IA, "Ia2", 119),
    (SIDE_IA, "Ia4", 86),
    (SIDE_IA, "Ia5", 143),
    (SIDE_IA, "Ia12", 83),
)
STANDING_LEFTOVER_021087_SITES = (
    (SIDE_IA, "Ia4", 116),
    (SIDE_IA, "Ia5", 27),
    (SIDE_IA, "Ia6", 77),
)
STANDING_LEFTOVER_600011_SITES = (
    (SIDE_IA, "Ia2", 106),
    (SIDE_IA, "Ia14", 53),
)
STANDING_LEFTOVER_999021_SITES = (
    (SIDE_IA, "Ia8", 104),
    (SIDE_IA, "Ia13", 15),
)
STANDING_LEFTOVER_057600_SITES = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
)
STANDING_CONTAINERS = (
    (CID_LEFTOVER_020010, LEFTOVER_N4_020010, STANDING_LEFTOVER_020010_SITES),
    (CID_LEFTOVER_021087, LEFTOVER_N4_021087, STANDING_LEFTOVER_021087_SITES),
    (CID_LEFTOVER_600011, LEFTOVER_N4_600011, STANDING_LEFTOVER_600011_SITES),
    (CID_LEFTOVER_999021, LEFTOVER_N4_999021, STANDING_LEFTOVER_999021_SITES),
    (CID_LEFTOVER_057600, LEFTOVER_N4_057600, STANDING_LEFTOVER_057600_SITES),
)
STANDING_N_IN_LEFTOVER_020010 = 4
STANDING_N_IN_LEFTOVER_021087 = 3
STANDING_N_IN_LEFTOVER_600011 = 2
STANDING_N_IN_LEFTOVER_999021 = 2
STANDING_N_IN_LEFTOVER_057600 = 2
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_LEFTOVER_020010_COVERED = (
    (SIDE_IA, "Ia2", 119),
    (SIDE_IA, "Ia4", 86),
    (SIDE_IA, "Ia5", 143),
    (SIDE_IA, "Ia12", 83),
)
STANDING_LEFTOVER_021087_COVERED = (
    (SIDE_IA, "Ia4", 117),
    (SIDE_IA, "Ia5", 28),
    (SIDE_IA, "Ia6", 78),
)
STANDING_LEFTOVER_600011_COVERED = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia14", 54),
)
STANDING_LEFTOVER_999021_COVERED = (
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia13", 17),
)
STANDING_LEFTOVER_057600_COVERED = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
)
STANDING_INSIDE_SITES = (
    (SIDE_IA, "Ia2", 107),
    (SIDE_IA, "Ia2", 119),
    (SIDE_IA, "Ia4", 86),
    (SIDE_IA, "Ia4", 117),
    (SIDE_IA, "Ia5", 28),
    (SIDE_IA, "Ia5", 143),
    (SIDE_IA, "Ia6", 78),
    (SIDE_IA, "Ia8", 106),
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
    (SIDE_IA, "Ia12", 83),
    (SIDE_IA, "Ia13", 17),
    (SIDE_IA, "Ia14", 54),
)
STANDING_LEFTOVER_SITES = (
    (SIDE_IA, "Ia1", 2),
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 10),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 37),
    (SIDE_IA, "Ia2", 114),
    (SIDE_IA, "Ia2", 128),
    (SIDE_IA, "Ia2", 154),
    (SIDE_IA, "Ia2", 159),
    (SIDE_IA, "Ia2", 165),
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia3", 4),
    (SIDE_IA, "Ia3", 37),
    (SIDE_IA, "Ia3", 71),
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 112),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia4", 134),
    (SIDE_IA, "Ia4", 154),
    (SIDE_IA, "Ia4", 162),
    (SIDE_IA, "Ia4", 166),
    (SIDE_IA, "Ia5", 2),
    (SIDE_IA, "Ia5", 6),
    (SIDE_IA, "Ia5", 23),
    (SIDE_IA, "Ia5", 66),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia5", 164),
    (SIDE_IA, "Ia6", 92),
    (SIDE_IA, "Ia6", 134),
    (SIDE_IA, "Ia7", 2),
    (SIDE_IA, "Ia7", 68),
    (SIDE_IA, "Ia7", 88),
    (SIDE_IA, "Ia7", 113),
    (SIDE_IA, "Ia7", 129),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia8", 120),
    (SIDE_IA, "Ia9", 129),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia10", 141),
    (SIDE_IA, "Ia12", 42),
    (SIDE_IA, "Ia12", 47),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 67),
    (SIDE_IA, "Ia13", 109),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia13", 143),
    (SIDE_IA, "Ia13", 152),
    (SIDE_IA, "Ia14", 9),
    (SIDE_IA, "Ia14", 97),
    (SIDE_IA, "Ia14", 105),
    (SIDE_IA, "Ia14", 140),
    (SIDE_IA, "Ia14", 177),
)
STANDING_LEFTOVER_PREVIOUS_4GRAMS = (
    ("602", "999", "090", "076"),
    ("093", "045", "090", "076"),
    ("027", "048", "090", "076"),
    ("380", "380", "090", "076"),
    ("076", "011", "090", "076"),
    ("070", "999", "090", "076"),
    ("070", "499", "090", "076"),
    ("061", "045", "090", "076"),
    ("076", "600", "090", "076"),
    ("070", "600", "090", "076"),
    ("455", "600", "090", "076"),
    ("050", "497", "090", "076"),
    ("076", "076", "090", "076"),
    ("009", "009", "090", "076"),
    ("061", "036", "090", "076"),
    ("000", "999", "090", "076"),
    ("499", "999", "090", "076"),
    ("076", "071", "090", "076"),
    ("090", "092", "090", "076"),
    ("060", "999", "090", "076"),
    ("087", "291", "090", "076"),
    ("460", "522", "090", "076"),
    ("254", "999", "090", "076"),
    ("010", "150", "090", "076"),
    ("087", "078", "090", "076"),
    ("000", "999", "090", "076"),
    ("071", "295", "090", "076"),
    ("381", "999", "090", "076"),
    ("490", "000", "090", "076"),
    ("090", "109", "090", "076"),
    ("071", "009", "090", "076"),
    ("023", "999", "090", "076"),
    ("055", "052", "090", "076"),
    ("000", "099", "090", "076"),
    ("064", "999", "090", "076"),
    ("092", "071", "090", "076"),
    ("168", "600", "090", "076"),
    ("518", "999", "090", "076"),
    ("670", "700", "090", "076"),
    ("076", "161", "090", "076"),
    ("075", "999", "090", "076"),
    ("208", "010", "090", "076"),
    ("072", "205", "090", "076"),
    ("011", "090", "090", "076"),
    ("090", "999", "090", "076"),
    ("071", "382", "090", "076"),
    ("011", "386", "090", "076"),
    ("700", "999", "090", "076"),
    ("727", "008", "090", "076"),
    ("070", "027", "090", "076"),
    ("071", "076", "090", "076"),
    ("724", "724", "090", "076"),
    ("007", "400", "090", "076"),
    ("011", "090", "090", "076"),
    ("090", "999", "090", "076"),
    ("600", "326", "090", "076"),
)
STANDING_LEFTOVER_NEXT_4GRAMS = (
    ("090", "076", "012", "076"),
    ("090", "076", "175", "002"),
    ("090", "076", "755", "509"),
    ("090", "076", "470", "700"),
    ("090", "076", "430", "076"),
    ("090", "076", "070", "499"),
    ("090", "076", "600", "002"),
    ("090", "076", "011", "678"),
    ("090", "076", "384", "570"),
    ("090", "076", "535", "076"),
    ("090", "076", "050", "050"),
    ("090", "076", "700", "011"),
    ("090", "076", "147", "076"),
    None,
    ("090", "076", "070", "200"),
    ("090", "076", "013", "073"),
    ("090", "076", "005", "406"),
    ("090", "076", "087", "499"),
    ("090", "076", "090", "076"),
    ("090", "076", "070", "600"),
    ("090", "076", "386", "202"),
    ("090", "076", "001", "048"),
    ("090", "076", "071", "633"),
    ("090", "076", "087", "078"),
    None,
    ("090", "076", "071", "295"),
    ("090", "076", "013", "291"),
    ("090", "076", "071", "007"),
    ("090", "076", "071", "004"),
    ("090", "076", "505", "633"),
    ("090", "076", "013", "076"),
    ("090", "076", "013", "070"),
    ("090", "076", "001", "224"),
    ("090", "076", "280", "139"),
    ("090", "076", "070", "027"),
    ("090", "076", "001", "071"),
    ("090", "076", "280", "067"),
    ("090", "076", "070", "532"),
    ("090", "076", "607", "073"),
    ("090", "076", "070", "071"),
    ("090", "076", "057", "240"),
    ("090", "076", "072", "205"),
    ("090", "076", "000", "076"),
    ("090", "076", "530", "090"),
    ("090", "076", "011", "130"),
    ("090", "076", "300", "000"),
    ("090", "076", "013", "755"),
    ("090", "076", "005", "084"),
    ("090", "076", "255", "067"),
    ("090", "076", "700", "076"),
    ("090", "076", "071", "076"),
    ("090", "076", "530", "499"),
    ("090", "076", "070", "073"),
    ("090", "076", "071", "600"),
    ("090", "076", "070", "000"),
    ("090", "076", "670", "700"),
)
STANDING_MEMBERSHIP = (
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (CID_LEFTOVER_600011,),
    (),
    (CID_LEFTOVER_020010,),
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
    (CID_LEFTOVER_020010,),
    (),
    (CID_LEFTOVER_021087,),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (CID_LEFTOVER_021087,),
    (),
    (),
    (CID_LEFTOVER_020010,),
    (),
    (CID_LEFTOVER_021087,),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (),
    (CID_LEFTOVER_999021,),
    (CID_LEFTOVER_057600,),
    (),
    (CID_LEFTOVER_057600,),
    (),
    (),
    (),
    (),
    (),
    (CID_LEFTOVER_020010,),
    (),
    (CID_LEFTOVER_999021,),
    (),
    (),
    (),
    (),
    (),
    (),
    (CID_LEFTOVER_600011,),
    (),
    (),
    (),
    (),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_090_076_all_inside_leftover_n4_remaining_family"
STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY = False
STANDING_RESULT = "i_090_076_inside_leftover_n4_remaining_family"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE168 = False
STANDING_SAME_AS_CYCLE172 = False
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_OTHER_LEFTOVER_N4_DOES_NOT_COUNT = True


def leftover_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    previous: tuple[tuple[str, ...] | None, ...] = STANDING_LEFTOVER_PREVIOUS_4GRAMS,
    nxt: tuple[tuple[str, ...] | None, ...] = STANDING_LEFTOVER_NEXT_4GRAMS,
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
                "previous_4gram": list(prev_gram) if prev_gram is not None else None,
                "next_4gram": list(next_gram) if next_gram is not None else None,
            }
        )
    return rows


def i_090_076_all_inside_leftover_n4_remaining_family(
    leftover_sites: tuple[tuple[str, str, int], ...],
    i_sites: tuple[tuple[str, str, int], ...] = STANDING_I_SITES,
) -> bool:
    """True iff every I 2-gram site sits inside the leftover n=4 remaining family.

    An empty I-site set is false here (the cycle-223 69 sites must
    be present and none may be leftover).
    """
    return bool(i_sites) and leftover_sites == ()


class TestI090076InsideLeftoverN4RemainingFamilyHelpers(unittest.TestCase):
    """Helpers on cycle-223 leftover remaining tokens. No CV, no LLM."""

    def test_inside_requires_contiguous_substring_and_window(self):
        """Family leftover n=4 count; a near-miss or out-of-window site does not."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(LEFTOVER_N4_020010, ("090", "076", "020", "010"))
        self.assertEqual(LEFTOVER_N4_021087, ("021", "090", "076", "087"))
        self.assertEqual(LEFTOVER_N4_600011, ("600", "090", "076", "011"))
        self.assertEqual(LEFTOVER_N4_999021, ("999", "021", "090", "076"))
        self.assertEqual(LEFTOVER_N4_057600, ("090", "076", "057", "600"))
        self.assertEqual(LEFTOVER_N4_020010[:STANDING_N2], GRAM2)
        self.assertEqual(LEFTOVER_N4_057600[:STANDING_N2], GRAM2)
        self.assertEqual(LEFTOVER_N4_999021[-STANDING_N2:], GRAM2)
        self.assertEqual(LEFTOVER_N4_021087[1:3], GRAM2)
        self.assertEqual(LEFTOVER_N4_600011[1:3], GRAM2)
        prefix_line = ["090", "076", "020", "010"]
        self.assertTrue(site_inside_container(prefix_line, 0, LEFTOVER_N4_020010, 0, GRAM2))
        mid_line = ["021", "090", "076", "087"]
        self.assertTrue(site_inside_container(mid_line, 1, LEFTOVER_N4_021087, 0, GRAM2))
        suffix_line = ["999", "021", "090", "076"]
        self.assertTrue(site_inside_container(suffix_line, 2, LEFTOVER_N4_999021, 0, GRAM2))
        leftover_site = ["602", "999", "090", "076", "012", "076"]
        self.assertFalse(
            site_inside_container(leftover_site, 2, LEFTOVER_N4_999021, 0, GRAM2)
        )
        self.assertFalse(
            site_inside_container(leftover_site, 2, LEFTOVER_N4_020010, 2, GRAM2)
        )
        almost_999_family = ["999", "090", "076", "070"]
        self.assertFalse(
            site_inside_container(almost_999_family, 1, LEFTOVER_N4_020010, 0, GRAM2)
        )
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_999_090_076_070))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_028_076_011_076))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_071_065_071_999))
        n2_076_071 = ["076", "071", "009", "090"]
        self.assertFalse(
            site_inside_container(n2_076_071, 0, LEFTOVER_N4_020010, 0, GRAM2)
        )
        out_of_window = ["090", "076", "020", "010", "090", "076"]
        self.assertTrue(
            site_inside_container(out_of_window, 0, LEFTOVER_N4_020010, 0, GRAM2)
        )
        self.assertFalse(
            site_inside_container(out_of_window, 4, LEFTOVER_N4_020010, 0, GRAM2)
        )
        self.assertFalse(
            site_inside_container(["090", "076"], 0, LEFTOVER_N4_020010, 0, GRAM2)
        )
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_OTHER_LEFTOVER_N4_DOES_NOT_COUNT)
        self.assertEqual(provider.get_call_history(), [])

    def test_all_inside_requires_empty_leftover_and_present_sites(self):
        """Boolean is True only when I sites exist and leftover is empty."""
        provider = MockProvider()
        self.assertTrue(
            i_090_076_all_inside_leftover_n4_remaining_family((), STANDING_I_SITES)
        )
        self.assertFalse(
            i_090_076_all_inside_leftover_n4_remaining_family(
                STANDING_LEFTOVER_SITES,
                STANDING_I_SITES,
            )
        )
        self.assertFalse(i_090_076_all_inside_leftover_n4_remaining_family((), ()))
        self.assertEqual(
            STANDING_CLAIM,
            "i_090_076_all_inside_leftover_n4_remaining_family",
        )
        self.assertFalse(STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY)
        self.assertNotEqual(
            STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY,
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(CYCLE172_N_LEFTOVER, 34)
        self.assertEqual(CYCLE168_N_LEFTOVER, 1)
        self.assertFalse(STANDING_SAME_AS_CYCLE172)
        self.assertFalse(STANDING_SAME_AS_CYCLE168)
        self.assertEqual(provider.get_call_history(), [])

    def test_2gram_is_substring_of_each_locked_leftover_n4(self):
        """2-gram is the locked remaining G, not a retuned inventory."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
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
            LEFTOVER_N4_020010,
            LEFTOVER_N4_021087,
            LEFTOVER_N4_600011,
            LEFTOVER_N4_999021,
            LEFTOVER_N4_057600,
        ))
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_999_090_076_070))
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_000_999_090_076))
        self.assertTrue(is_contiguous_substring(GRAM2, NEAR_MISS_090_999_090_076))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_028_076_011_076))
        self.assertFalse(is_contiguous_substring(GRAM2, NEAR_MISS_071_065_071_999))
        self.assertIn(NEAR_MISS_999_090_076_070, leftover_grams)
        self.assertIn(NEAR_MISS_028_076_011_076, leftover_grams)
        self.assertNotIn(NEAR_MISS_999_090_076_070, STANDING_MATCHING_LEFTOVERS)
        self.assertNotIn(NEAR_MISS_028_076_011_076, STANDING_MATCHING_LEFTOVERS)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard(unittest.TestCase):
    """Cited-fixture leftover remaining 2-gram leftover-n=4-family lock. Mock only."""

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
        self.leftover_020010_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_020010,
        )
        self.leftover_021087_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_021087,
        )
        self.leftover_600011_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_600011,
        )
        self.leftover_999021_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_999021,
        )
        self.leftover_057600_sites = sites_with_container(
            self.i_sites,
            self.membership,
            CID_LEFTOVER_057600,
        )
        self.inside_sites = inside_sites_from_membership(self.i_sites, self.membership)
        self.leftover_sites = leftover_sites_from_membership(
            self.i_sites,
            self.membership,
        )
        self.local_4grams = leftover_local_4grams(self.i_sides, self.leftover_sites, GRAM2)
        self.n_on_i = len(self.i_sites)
        self.n_in_leftover_020010 = len(self.leftover_020010_sites)
        self.n_in_leftover_021087 = len(self.leftover_021087_sites)
        self.n_in_leftover_600011 = len(self.leftover_600011_sites)
        self.n_in_leftover_999021 = len(self.leftover_999021_sites)
        self.n_in_leftover_057600 = len(self.leftover_057600_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover = len(self.leftover_sites)
        self.claim_holds = i_090_076_all_inside_leftover_n4_remaining_family(
            self.leftover_sites,
            self.i_sites,
        )

    def test_tokens_and_containers_are_cycle_222_family_not_retuned(self):
        """2-gram and five leftover n=4 remaining stay the cycle-223/222/136 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(
            STANDING_MATCHING_LEFTOVERS,
            (
                LEFTOVER_N4_020010,
                LEFTOVER_N4_021087,
                LEFTOVER_N4_600011,
                LEFTOVER_N4_999021,
                LEFTOVER_N4_057600,
            ),
        )
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(tuple(prior_223["tokens2"]), GRAM2)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in prior_223["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertEqual(prior_222["K"], CYCLE222_K)
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(tuple(prior_222["G"]), CYCLE222_G)
        leftover_by_gram = {row[0]: row[3] for row in STANDING_WITH_ROWS}
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_020010], STANDING_LEFTOVER_020010_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_021087], STANDING_LEFTOVER_021087_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_600011], STANDING_LEFTOVER_600011_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_999021], STANDING_LEFTOVER_999021_SITES)
        self.assertEqual(leftover_by_gram[LEFTOVER_N4_057600], STANDING_LEFTOVER_057600_SITES)
        leftover_grams = {row[0] for row in STANDING_LEFTOVER}
        self.assertIn(NEAR_MISS_999_090_076_070, leftover_grams)
        self.assertNotIn(NEAR_MISS_999_090_076_070, STANDING_MATCHING_LEFTOVERS)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses(self):
        """N_I=69: N_inside=13, N_leftover=56. Claim loses."""
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.n_on_i, STANDING_N_ON_I)
        self.assertEqual(STANDING_N_ON_I, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_on_i, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(self.membership, STANDING_MEMBERSHIP)
        self.assertEqual(self.leftover_020010_sites, STANDING_LEFTOVER_020010_COVERED)
        self.assertEqual(self.leftover_021087_sites, STANDING_LEFTOVER_021087_COVERED)
        self.assertEqual(self.leftover_600011_sites, STANDING_LEFTOVER_600011_COVERED)
        self.assertEqual(self.leftover_999021_sites, STANDING_LEFTOVER_999021_COVERED)
        self.assertEqual(self.leftover_057600_sites, STANDING_LEFTOVER_057600_COVERED)
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.n_in_leftover_020010, STANDING_N_IN_LEFTOVER_020010)
        self.assertEqual(STANDING_N_IN_LEFTOVER_020010, 4)
        self.assertEqual(self.n_in_leftover_021087, STANDING_N_IN_LEFTOVER_021087)
        self.assertEqual(STANDING_N_IN_LEFTOVER_021087, 3)
        self.assertEqual(self.n_in_leftover_600011, STANDING_N_IN_LEFTOVER_600011)
        self.assertEqual(STANDING_N_IN_LEFTOVER_600011, 2)
        self.assertEqual(self.n_in_leftover_999021, STANDING_N_IN_LEFTOVER_999021)
        self.assertEqual(STANDING_N_IN_LEFTOVER_999021, 2)
        self.assertEqual(self.n_in_leftover_057600, STANDING_N_IN_LEFTOVER_057600)
        self.assertEqual(STANDING_N_IN_LEFTOVER_057600, 2)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(self.n_inside + self.n_leftover, self.n_on_i)
        self.assertEqual(
            self.n_in_leftover_020010
            + self.n_in_leftover_021087
            + self.n_in_leftover_600011
            + self.n_in_leftover_999021
            + self.n_in_leftover_057600,
            13,
        )
        for side, line, index in STANDING_I_SITES:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(side, SIDE_IA)
        for side, line, index in STANDING_LEFTOVER_020010_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_020010, index, GRAM2)
            )
        for side, line, index in STANDING_LEFTOVER_021087_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_021087, index - 1, GRAM2)
            )
        for side, line, index in STANDING_LEFTOVER_600011_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_600011, index - 1, GRAM2)
            )
        for side, line, index in STANDING_LEFTOVER_999021_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_999021, index - 2, GRAM2)
            )
        for side, line, index in STANDING_LEFTOVER_057600_COVERED:
            stems = self.i_sides[side][IA_LINE_NAMES.index(line)]
            self.assertTrue(
                site_inside_container(stems, index, LEFTOVER_N4_057600, index, GRAM2)
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
            i_090_076_all_inside_leftover_n4_remaining_family(
                self.leftover_sites,
                self.i_sites,
            ),
            STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY,
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY,
        )
        self.assertFalse(STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY)
        self.assertTrue(HYPOTHESIS_ALL_INSIDE)
        self.assertEqual(
            STANDING_CLAIM,
            "i_090_076_all_inside_leftover_n4_remaining_family",
        )
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leftover_site_local_4grams_are_locked_and_not_the_family(self):
        """N_leftover=56; previous/next 4-grams are not the leftover remaining family."""
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), 56)
        self.assertEqual(STANDING_LEFTOVER_SITES[0], (SIDE_IA, "Ia1", 2))
        self.assertEqual(STANDING_LEFTOVER_SITES[-1], (SIDE_IA, "Ia14", 177))
        self.assertEqual(STANDING_LEFTOVER_SITES[13], (SIDE_IA, "Ia2", 174))
        self.assertEqual(STANDING_LEFTOVER_SITES[24], (SIDE_IA, "Ia4", 166))
        self.assertIsNone(STANDING_LEFTOVER_NEXT_4GRAMS[13])
        self.assertIsNone(STANDING_LEFTOVER_NEXT_4GRAMS[24])
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
        self.assertEqual(tuple(stems[0:4]), ("602", "999", "090", "076"))
        self.assertEqual(tuple(stems[2:4]), GRAM2)
        self.assertEqual(tuple(stems[2:6]), ("090", "076", "012", "076"))
        family = set(STANDING_MATCHING_LEFTOVERS)
        for prev, nxt in zip(
            STANDING_LEFTOVER_PREVIOUS_4GRAMS,
            STANDING_LEFTOVER_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertIsNotNone(prev)
            self.assertNotIn(prev, family)
            self.assertEqual(prev[2:], GRAM2)
            if nxt is None:
                continue
            self.assertNotIn(nxt, family)
            self.assertEqual(nxt[:2], GRAM2)
        self.assertNotEqual(("602", "999", "090", "076"), NEAR_MISS_999_090_076_070)
        self.assertNotEqual(("090", "076", "012", "076"), NEAR_MISS_000_999_090_076)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_223_222_207_171_168_and_w_scoreboards_still_compute(self):
        """Cycle 223 69/3, 222 K=5, 207 8/1, 171 43/0, 168 family, W stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        self.assertTrue(CYCLE222_CLAIM)
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
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertFalse(prior_207.claim_holds)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_168 = TestMamariI3gram999090076InsideFamilyScoreboard()
        prior_168.setUp()
        prior_168.test_sixteen_sites_split_15_inside_1_leftover_and_claim_loses()
        prior_168.test_survey_matches_computed_lock()
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-224 inside-leftover-n=4-remaining lock."""
        lock = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(lock["cycle"], 224)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_all_inside_leftover_n4_remaining_family"])
        self.assertEqual(
            lock["hypothesis_all_inside_leftover_n4_remaining_family"],
            HYPOTHESIS_ALL_INSIDE,
        )
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["leftover_n4_020010_tokens"]), LEFTOVER_N4_020010)
        self.assertEqual(tuple(lock["leftover_n4_021087_tokens"]), LEFTOVER_N4_021087)
        self.assertEqual(tuple(lock["leftover_n4_600011_tokens"]), LEFTOVER_N4_600011)
        self.assertEqual(tuple(lock["leftover_n4_999021_tokens"]), LEFTOVER_N4_999021)
        self.assertEqual(tuple(lock["leftover_n4_057600_tokens"]), LEFTOVER_N4_057600)
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_LEFTOVERS],
            lock["family_leftover_n4"],
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_020010_container_sites"]),
            STANDING_LEFTOVER_020010_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_021087_container_sites"]),
            STANDING_LEFTOVER_021087_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_600011_container_sites"]),
            STANDING_LEFTOVER_600011_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_999021_container_sites"]),
            STANDING_LEFTOVER_999021_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_n4_057600_container_sites"]),
            STANDING_LEFTOVER_057600_SITES,
        )
        self.assertEqual(lock["N_on_I"], STANDING_N_ON_I)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["i_hits"], STANDING_N_I)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["i_sites"]),
            STANDING_I_SITES,
        )
        self.assertEqual(lock["N_in_leftover_090_076_020_010"], STANDING_N_IN_LEFTOVER_020010)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_020010_covered_sites"]),
            STANDING_LEFTOVER_020010_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_021_090_076_087"], STANDING_N_IN_LEFTOVER_021087)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_021087_covered_sites"]),
            STANDING_LEFTOVER_021087_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_600_090_076_011"], STANDING_N_IN_LEFTOVER_600011)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_600011_covered_sites"]),
            STANDING_LEFTOVER_600011_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_999_021_090_076"], STANDING_N_IN_LEFTOVER_999021)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_999021_covered_sites"]),
            STANDING_LEFTOVER_999021_COVERED,
        )
        self.assertEqual(lock["N_in_leftover_090_076_057_600"], STANDING_N_IN_LEFTOVER_057600)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_057600_covered_sites"]),
            STANDING_LEFTOVER_057600_COVERED,
        )
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            [list(site) for site in STANDING_LEFTOVER_SITES],
            lock["leftover_sites"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_LEFTOVER_PREVIOUS_4GRAMS],
            lock["leftover_previous_4grams"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_LEFTOVER_NEXT_4GRAMS],
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
        self.assertFalse(lock["i_090_076_all_inside_leftover_n4_remaining_family"])
        self.assertEqual(
            lock["i_090_076_all_inside_leftover_n4_remaining_family"],
            STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle168"])
        self.assertFalse(lock["same_as_cycle172"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["other_leftover_n4_does_not_count"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_999_090_076_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
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
        self.assertEqual(self.survey["i_leftover_n4_remaining_next_2gram"]["N_remaining"], 16)
        self.assertEqual(tuple(self.survey["i_leftover_n4_remaining_next_2gram"]["G"]), GRAM2)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_999_090_076_inside_family"]["cycle"], 168)
        self.assertFalse(
            self.survey["i_3gram_999_090_076_inside_family"][
                "i_3gram_999_090_076_all_inside_leftover_n4_family"
            ]
        )
        self.assertEqual(self.survey["i_3gram_999_090_076_inside_family"]["N_leftover"], 1)
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


class TestMamariI090076InsideLeftoverN4RemainingFamilyImageSnapshot(unittest.TestCase):
    """Cycle 224 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
