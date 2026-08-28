"""H∩P∩Q recto gap-1 pairwise grams on existing H/P/Q fixtures.

Cycle 75 text-search lock. Uses already-vendored Hr/Pr/Qr, the
cycle-74 gap-1 intervening stems, and the existing parsers.
Existing line/index sites only. Does not scrape a new tablet.
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary. Verso island stays out.

Lock the exact H–Q gap-1 shared 31-gram (sequence + Hr/Qr sites),
the H–P gap-1 shared 22-gram (sequence + Hr/Pr sites), whether
each gram is a prefix / suffix / interior of that gap on each
side, coverage (n / gap length), and whether P has an exact hit
of the H–Q 31-gram on Pr gap 1.

Claim that can lose: H and Q share filler in gap 1 and P does
not (P is waypoint-only there).

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_hpq_island_recto_gap_scoreboard import (
    STANDING_GAPS,
    TestMamariHpqIslandRectoGapScoreboard,
    intervening_stems,
    longest_shared_ngram,
)
from tests.test_mamari_hpq_island_recto_order_scoreboard import (
    STANDING_HR_ORDER,
    STANDING_PR_ORDER,
    STANDING_QR_ORDER,
    island_from_triple_row,
    order_on,
    split_recto_verso,
)
from tests.test_mamari_hpq_triple_n8_scoreboard import (
    load_q_h_p_sides,
    maximal_triple_rows,
    score_hpq_triple_n8,
)
from tests.test_mamari_large_santiago_st_petersburg_shared_n8_scoreboard import (
    STANDING_MAXIMALS as STANDING_HP_MAXIMALS,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    H_SIDES,
    P_SIDES,
    SIDE_HR,
    SIDE_PR,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    LINE_NAMES,
    STANDING_QH_MAXIMALS,
)
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    Q_SIDES,
    SIDE_QR,
)

REL_PREFIX = "prefix"
REL_SUFFIX = "suffix"
REL_INTERIOR = "interior"
REL_ABSENT = "absent"
PLACEMENTS = (REL_PREFIX, REL_SUFFIX, REL_INTERIOR, REL_ABSENT)

STANDING_HQ_N = 31
STANDING_HQ_TOKENS = STANDING_QH_MAXIMALS[0][0]
STANDING_HQ_H_SITE = (SIDE_HR, "Hr3", 39)
STANDING_HQ_Q_SITE = (SIDE_QR, "Qr3", 19)
STANDING_HQ_H_OFFSET = 1
STANDING_HQ_Q_OFFSET = 1
STANDING_HQ_H_PLACE = REL_INTERIOR
STANDING_HQ_Q_PLACE = REL_INTERIOR
STANDING_HQ_H_COVERAGE = (31, 164)
STANDING_HQ_Q_COVERAGE = (31, 123)

STANDING_HP_N = 22
STANDING_HP_TOKENS = STANDING_HP_MAXIMALS[0][0]
STANDING_HP_H_SITE = (SIDE_HR, "Hr5", 6)
STANDING_HP_P_SITE = (SIDE_PR, "Pr4", 71)
STANDING_HP_H_OFFSET = 134
STANDING_HP_P_OFFSET = 151
STANDING_HP_H_PLACE = REL_INTERIOR
STANDING_HP_P_PLACE = REL_INTERIOR
STANDING_HP_H_COVERAGE = (22, 164)
STANDING_HP_P_COVERAGE = (22, 184)

STANDING_P_IN_HQ = False
STANDING_HQ_SHARE_FILLER = True
STANDING_P_WAYPOINT_ONLY = True
STANDING_NEW_TABLET = False
STANDING_TABLET_D_SCRAPED = False
STANDING_RESULT = "hpq_island_recto_gap1_pairwise"


@dataclass(frozen=True)
class Gap1Pairwise:
    """Gap-1 H–Q 31-gram, H–P 22-gram, and P-absent. Ids only."""

    hq_tokens: tuple[str, ...]
    hq_h_site: tuple[str, str, int]
    hq_q_site: tuple[str, str, int]
    hq_h_offset: int
    hq_q_offset: int
    hq_h_place: str
    hq_q_place: str
    hq_h_coverage: tuple[int, int]
    hq_q_coverage: tuple[int, int]
    hp_tokens: tuple[str, ...]
    hp_h_site: tuple[str, str, int]
    hp_p_site: tuple[str, str, int]
    hp_h_offset: int
    hp_p_offset: int
    hp_h_place: str
    hp_p_place: str
    hp_h_coverage: tuple[int, int]
    hp_p_coverage: tuple[int, int]
    p_in_hq: bool


def gap_hits(stems: list[str], gram: tuple[str, ...]) -> tuple[int, ...]:
    """Offsets of exact gram hits inside one gap string."""
    n = len(gram)
    if n == 0 or len(stems) < n:
        return ()
    return tuple(
        index
        for index in range(len(stems) - n + 1)
        if tuple(stems[index : index + n]) == gram
    )


def gap_placement(stems: list[str], gram: tuple[str, ...]) -> str:
    """prefix / suffix / interior of the gap, or absent."""
    hits = gap_hits(stems, gram)
    if not hits:
        return REL_ABSENT
    index = hits[0]
    n = len(gram)
    if index == 0:
        return REL_PREFIX
    if index + n == len(stems):
        return REL_SUFFIX
    return REL_INTERIOR


def gap_sites(
    by_side: dict[str, list[list[str]]],
    left: tuple[tuple[str, ...], int, tuple[str, str, int]],
    right: tuple[tuple[str, ...], int, tuple[str, str, int]],
) -> list[tuple[str, str, int]]:
    """Tablet (side, line, index) for each intervening stem."""
    _tokens, n, (side, start_line, start_index) = left
    _rt, _rn, (_rs, end_line, end_index) = right
    lines = by_side[side]
    names = LINE_NAMES[side]
    start_li = names.index(start_line)
    end_li = names.index(end_line)
    first = start_index + n
    if start_li == end_li:
        return [(side, names[start_li], index) for index in range(first, end_index)]
    sites = [
        (side, names[start_li], index)
        for index in range(first, len(lines[start_li]))
    ]
    for line_index in range(start_li + 1, end_li):
        sites.extend(
            (side, names[line_index], index)
            for index in range(len(lines[line_index]))
        )
    sites.extend((side, names[end_li], index) for index in range(end_index))
    return sites


def score_gap1_pairwise(
    by_side: dict[str, list[list[str]]],
    hr_order: tuple = STANDING_HR_ORDER,
    pr_order: tuple = STANDING_PR_ORDER,
    qr_order: tuple = STANDING_QR_ORDER,
) -> Gap1Pairwise:
    """H–Q 31-gram and H–P 22-gram inside gap 1, plus P-absent."""
    stems_h = intervening_stems(by_side, hr_order[0], hr_order[1])
    stems_p = intervening_stems(by_side, pr_order[0], pr_order[1])
    stems_q = intervening_stems(by_side, qr_order[0], qr_order[1])
    sites_h = gap_sites(by_side, hr_order[0], hr_order[1])
    sites_p = gap_sites(by_side, pr_order[0], pr_order[1])
    sites_q = gap_sites(by_side, qr_order[0], qr_order[1])
    hq_n, hq_tokens = longest_shared_ngram(stems_h, stems_q)
    hp_n, hp_tokens = longest_shared_ngram(stems_h, stems_p)
    hq_h_hits = gap_hits(stems_h, hq_tokens)
    hq_q_hits = gap_hits(stems_q, hq_tokens)
    hp_h_hits = gap_hits(stems_h, hp_tokens)
    hp_p_hits = gap_hits(stems_p, hp_tokens)
    hq_h_offset = hq_h_hits[0]
    hq_q_offset = hq_q_hits[0]
    hp_h_offset = hp_h_hits[0]
    hp_p_offset = hp_p_hits[0]
    return Gap1Pairwise(
        hq_tokens=hq_tokens,
        hq_h_site=sites_h[hq_h_offset],
        hq_q_site=sites_q[hq_q_offset],
        hq_h_offset=hq_h_offset,
        hq_q_offset=hq_q_offset,
        hq_h_place=gap_placement(stems_h, hq_tokens),
        hq_q_place=gap_placement(stems_q, hq_tokens),
        hq_h_coverage=(hq_n, len(stems_h)),
        hq_q_coverage=(hq_n, len(stems_q)),
        hp_tokens=hp_tokens,
        hp_h_site=sites_h[hp_h_offset],
        hp_p_site=sites_p[hp_p_offset],
        hp_h_offset=hp_h_offset,
        hp_p_offset=hp_p_offset,
        hp_h_place=gap_placement(stems_h, hp_tokens),
        hp_p_place=gap_placement(stems_p, hp_tokens),
        hp_h_coverage=(hp_n, len(stems_h)),
        hp_p_coverage=(hp_n, len(stems_p)),
        p_in_hq=bool(gap_hits(stems_p, hq_tokens)),
    )


class TestHpqIslandRectoGap1PairwiseHelpers(unittest.TestCase):
    """Helpers on synthetic gap strings. No CV, no LLM."""

    def test_placement_prefix_suffix_interior_absent(self):
        """Prefix and suffix beat interior; a miss is absent."""
        provider = MockProvider()
        stems = ["A", "B", "C", "D", "E"]
        self.assertEqual(gap_placement(stems, ("A", "B")), REL_PREFIX)
        self.assertEqual(gap_placement(stems, ("D", "E")), REL_SUFFIX)
        self.assertEqual(gap_placement(stems, ("B", "C")), REL_INTERIOR)
        self.assertEqual(gap_placement(stems, ("Z", "Z")), REL_ABSENT)
        self.assertEqual(gap_hits(stems, ("B", "C")), (1,))
        self.assertEqual(gap_hits(stems, ("Z",)), ())
        self.assertEqual(provider.get_call_history(), [])

    def test_p_absent_is_false_only_on_exact_hit(self):
        """P-in-HQ is true only when Pr gap 1 contains the H–Q gram."""
        provider = MockProvider()
        hq = ("1", "2", "3")
        self.assertFalse(bool(gap_hits(["A", "B", "C", "D"], hq)))
        self.assertTrue(bool(gap_hits(["A", "1", "2", "3", "B"], hq)))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHpqIslandRectoGap1PairwiseScoreboard(unittest.TestCase):
    """Cited-fixture H/P/Q recto gap-1 pairwise lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_q_h_p_sides()
        self.combined = score_hpq_triple_n8(self.by_side, H_SIDES, P_SIDES, Q_SIDES)
        self.maximals = tuple(
            island_from_triple_row(row)
            for row in maximal_triple_rows(self.combined)
        )
        self.recto, self.verso = split_recto_verso(self.maximals)
        self.hr_order = order_on(self.recto, "h")
        self.pr_order = order_on(self.recto, "p")
        self.qr_order = order_on(self.recto, "q")
        self.lock = score_gap1_pairwise(
            self.by_side, self.hr_order, self.pr_order, self.qr_order
        )

    def test_gap1_hq_31_hp_22_and_p_absent(self):
        """H–Q 31 and H–P 22 are interior; P misses the 31-gram."""
        self.assertEqual(self.hr_order, STANDING_HR_ORDER)
        self.assertEqual(self.pr_order, STANDING_PR_ORDER)
        self.assertEqual(self.qr_order, STANDING_QR_ORDER)
        self.assertEqual(STANDING_GAPS[0][:3], (164, 184, 123))
        self.assertEqual(self.lock.hq_tokens, STANDING_HQ_TOKENS)
        self.assertEqual(len(self.lock.hq_tokens), STANDING_HQ_N)
        self.assertEqual(self.lock.hq_h_site, STANDING_HQ_H_SITE)
        self.assertEqual(self.lock.hq_q_site, STANDING_HQ_Q_SITE)
        self.assertEqual(self.lock.hq_h_offset, STANDING_HQ_H_OFFSET)
        self.assertEqual(self.lock.hq_q_offset, STANDING_HQ_Q_OFFSET)
        self.assertEqual(self.lock.hq_h_place, STANDING_HQ_H_PLACE)
        self.assertEqual(self.lock.hq_q_place, STANDING_HQ_Q_PLACE)
        self.assertEqual(self.lock.hq_h_coverage, STANDING_HQ_H_COVERAGE)
        self.assertEqual(self.lock.hq_q_coverage, STANDING_HQ_Q_COVERAGE)
        self.assertEqual(self.lock.hq_tokens, STANDING_QH_MAXIMALS[0][0])
        self.assertEqual(self.lock.hq_h_site, STANDING_QH_MAXIMALS[0][5])
        self.assertEqual(self.lock.hq_q_site, STANDING_QH_MAXIMALS[0][4])
        self.assertEqual(self.lock.hp_tokens, STANDING_HP_TOKENS)
        self.assertEqual(len(self.lock.hp_tokens), STANDING_HP_N)
        self.assertEqual(self.lock.hp_h_site, STANDING_HP_H_SITE)
        self.assertEqual(self.lock.hp_p_site, STANDING_HP_P_SITE)
        self.assertEqual(self.lock.hp_h_offset, STANDING_HP_H_OFFSET)
        self.assertEqual(self.lock.hp_p_offset, STANDING_HP_P_OFFSET)
        self.assertEqual(self.lock.hp_h_place, STANDING_HP_H_PLACE)
        self.assertEqual(self.lock.hp_p_place, STANDING_HP_P_PLACE)
        self.assertEqual(self.lock.hp_h_coverage, STANDING_HP_H_COVERAGE)
        self.assertEqual(self.lock.hp_p_coverage, STANDING_HP_P_COVERAGE)
        self.assertEqual(self.lock.hp_tokens, STANDING_HP_MAXIMALS[0][0])
        self.assertEqual(self.lock.hp_h_site, STANDING_HP_MAXIMALS[0][4])
        self.assertEqual(self.lock.hp_p_site, STANDING_HP_MAXIMALS[0][5])
        self.assertEqual(self.lock.p_in_hq, STANDING_P_IN_HQ)
        self.assertFalse(STANDING_P_IN_HQ)
        self.assertTrue(STANDING_HQ_SHARE_FILLER)
        self.assertTrue(STANDING_P_WAYPOINT_ONLY)
        self.assertEqual(self.lock.p_in_hq, not STANDING_P_WAYPOINT_ONLY)
        self.assertNotEqual(self.lock.hq_h_place, REL_ABSENT)
        self.assertNotEqual(self.lock.hq_q_place, REL_ABSENT)
        self.assertEqual(len(self.verso), 1)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_hpq_island_recto_gap_scoreboard_still_computes(self):
        """Cycle 74 3-gap lock stays."""
        prior = TestMamariHpqIslandRectoGapScoreboard()
        prior.setUp()
        prior.test_three_gap_table_lengths_and_longest_shared_n()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-75 gap-1 pairwise lock."""
        lock = self.survey["tablet_h_p_q_island_recto_gap1_pairwise"]
        self.assertEqual(lock["cycle"], 75)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["hq_tokens"]), STANDING_HQ_TOKENS)
        self.assertEqual(lock["hq_n"], STANDING_HQ_N)
        self.assertEqual(tuple(lock["hq_sites"][0]), STANDING_HQ_H_SITE)
        self.assertEqual(tuple(lock["hq_sites"][1]), STANDING_HQ_Q_SITE)
        self.assertEqual(tuple(lock["hq_offsets"]), (STANDING_HQ_H_OFFSET, STANDING_HQ_Q_OFFSET))
        self.assertEqual(tuple(lock["hq_placements"]), (STANDING_HQ_H_PLACE, STANDING_HQ_Q_PLACE))
        self.assertEqual(tuple(lock["hq_coverage"][0]), STANDING_HQ_H_COVERAGE)
        self.assertEqual(tuple(lock["hq_coverage"][1]), STANDING_HQ_Q_COVERAGE)
        self.assertEqual(tuple(lock["hp_tokens"]), STANDING_HP_TOKENS)
        self.assertEqual(lock["hp_n"], STANDING_HP_N)
        self.assertEqual(tuple(lock["hp_sites"][0]), STANDING_HP_H_SITE)
        self.assertEqual(tuple(lock["hp_sites"][1]), STANDING_HP_P_SITE)
        self.assertEqual(tuple(lock["hp_offsets"]), (STANDING_HP_H_OFFSET, STANDING_HP_P_OFFSET))
        self.assertEqual(tuple(lock["hp_placements"]), (STANDING_HP_H_PLACE, STANDING_HP_P_PLACE))
        self.assertEqual(tuple(lock["hp_coverage"][0]), STANDING_HP_H_COVERAGE)
        self.assertEqual(tuple(lock["hp_coverage"][1]), STANDING_HP_P_COVERAGE)
        self.assertEqual(lock["p_in_hq_31"], STANDING_P_IN_HQ)
        self.assertFalse(lock["p_in_hq_31"])
        self.assertEqual(lock["hq_share_filler"], STANDING_HQ_SHARE_FILLER)
        self.assertTrue(lock["hq_share_filler"])
        self.assertEqual(lock["p_waypoint_only"], STANDING_P_WAYPOINT_ONLY)
        self.assertTrue(lock["p_waypoint_only"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertTrue(lock["standing_hpq_island_recto_gaps_unchanged"])
        self.assertTrue(lock["standing_hpq_island_recto_order_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hp_shared_n8_unchanged"])
        self.assertTrue(lock["standing_q_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_h_p_q_island_recto_gaps"]["cycle"], 74)
        self.assertEqual(self.survey["tablet_h_p_q_island_recto_order"]["cycle"], 73)
        self.assertEqual(self.survey["tablet_h_p_q_island_off_hpq_hits"]["cycle"], 72)
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHpqIslandRectoGap1PairwiseImageSnapshot(unittest.TestCase):
    """Cycle 75 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
