"""H∩P∩Q recto-island reading order on existing H/P/Q fixtures.

Cycle 73 text-search lock. Uses already-vendored Hr/Hv, Pr/Pv,
Qr/Qv and the cycle-71 maximal islands. Existing line/index sites
only. Does not scrape a new tablet. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. Not a meaning dictionary.

Sort the four recto islands (Hr/Pr/Qr) by line then index on each
tablet. Lock those three sequences and whether they match. Keep
the verso island as a separate Hv/Pv/Qv row so it is not mixed
into the recto order.

Claim that can lose: the four recto islands are in the same order
on H, P, and Q (one text copied three times) vs a bag of formulas
(orders differ).

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import re
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_hpq_island_off_hpq_scoreboard import (
    TestMamariHpqIslandOffHpqScoreboard,
)
from tests.test_mamari_hpq_triple_n8_scoreboard import (
    STANDING_HR_PR_QR_MAXIMALS,
    STANDING_HV_PV_QV_MAXIMALS,
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    TripleN8Row,
    load_q_h_p_sides,
    maximal_triple_rows,
    score_hpq_triple_n8,
)
from tests.test_mamari_large_santiago_st_petersburg_vendor_scoreboard import (
    H_SIDES,
    P_SIDES,
    SIDE_HR,
    SIDE_HV,
    SIDE_PR,
    SIDE_PV,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_st_petersburg_vendor_scoreboard import (
    Q_SIDES,
    SIDE_QR,
    SIDE_QV,
)

RECTO_SIDES = (SIDE_HR, SIDE_PR, SIDE_QR)
VERSO_SIDES = (SIDE_HV, SIDE_PV, SIDE_QV)
SITE_H = 5
SITE_P = 6
SITE_Q = 7

STANDING_RECTO_COUNT = 4
STANDING_VERSO_COUNT = 1
STANDING_HR_ORDER = (
    (("062", "006", "001", "062", "006", "001", "062", "006", "001", "020", "064"), 11, (SIDE_HR, "Hr3", 27)),
    (("005", "002", "041", "220", "009", "220", "009", "440", "440", "440"), 10, (SIDE_HR, "Hr5", 36)),
    (("005", "099", "011", "007", "004", "600", "522", "606"), 8, (SIDE_HR, "Hr7", 47)),
    (("002", "144", "002", "662", "680", "005", "010", "005", "052", "022", "243", "001"), 12, (SIDE_HR, "Hr8", 0)),
)
STANDING_PR_ORDER = (
    (("062", "006", "001", "062", "006", "001", "062", "006", "001", "020", "064"), 11, (SIDE_PR, "Pr3", 14)),
    (("005", "002", "041", "220", "009", "220", "009", "440", "440", "440"), 10, (SIDE_PR, "Pr5", 9)),
    (("005", "099", "011", "007", "004", "600", "522", "606"), 8, (SIDE_PR, "Pr7", 10)),
    (("002", "144", "002", "662", "680", "005", "010", "005", "052", "022", "243", "001"), 12, (SIDE_PR, "Pr7", 29)),
)
STANDING_QR_ORDER = (
    (("062", "006", "001", "062", "006", "001", "062", "006", "001", "020", "064"), 11, (SIDE_QR, "Qr3", 7)),
    (("005", "002", "041", "220", "009", "220", "009", "440", "440", "440"), 10, (SIDE_QR, "Qr5", 15)),
    (("005", "099", "011", "007", "004", "600", "522", "606"), 8, (SIDE_QR, "Qr7", 28)),
    (("002", "144", "002", "662", "680", "005", "010", "005", "052", "022", "243", "001"), 12, (SIDE_QR, "Qr7", 47)),
)
STANDING_TOKEN_ORDER = tuple(row[0] for row in STANDING_HR_ORDER)
STANDING_VERSO = (
    ("301", "004", "064", "004", "064", "209", "081", "050"),
    8,
    (SIDE_HV, "Hv2", 32),
    (SIDE_PV, "Pv4", 50),
    (SIDE_QV, "Qv5", 11),
)
STANDING_SAME_ORDER = True
STANDING_BAG_OF_FORMULAS = False
STANDING_COPIED_RECTO_ORDER = True
STANDING_VERSO_MIXED_INTO_RECTO = False
STANDING_NEW_TABLET = False
STANDING_TABLET_D_SCRAPED = False
STANDING_RESULT = "hpq_island_recto_order"


@dataclass(frozen=True)
class IslandSites:
    """One maximal island's tokens and one site per tablet. Ids only."""

    tokens: tuple[str, ...]
    n: int
    h: tuple[str, str, int]
    p: tuple[str, str, int]
    q: tuple[str, str, int]


def island_from_maximal(row: tuple) -> IslandSites:
    """Unpack a cycle-71 maximal tuple."""
    tokens, n, _fh, _fp, _fq, h_site, p_site, q_site = row
    return IslandSites(tokens=tokens, n=n, h=h_site, p=p_site, q=q_site)


def island_from_triple_row(row: TripleN8Row) -> IslandSites:
    """One site per tablet from a scored triple row."""
    return IslandSites(
        tokens=row.tokens,
        n=row.n,
        h=row.hits_h[0],
        p=row.hits_p[0],
        q=row.hits_q[0],
    )


def line_then_index(site: tuple[str, str, int]) -> tuple[int, int]:
    """(line number, index) from a (side, line_name, index) site."""
    _side, line_name, index = site
    match = re.search(r"(\d+)$", line_name)
    if match is None:
        raise ValueError(f"no line number in {line_name!r}")
    return (int(match.group(1)), index)


def split_recto_verso(
    islands: tuple[IslandSites, ...],
) -> tuple[tuple[IslandSites, ...], tuple[IslandSites, ...]]:
    """Recto = Hr/Pr/Qr only. Verso = Hv/Pv/Qv only. No mixing."""
    recto = tuple(
        island
        for island in islands
        if island.h[0] == SIDE_HR
        and island.p[0] == SIDE_PR
        and island.q[0] == SIDE_QR
    )
    verso = tuple(
        island
        for island in islands
        if island.h[0] == SIDE_HV
        and island.p[0] == SIDE_PV
        and island.q[0] == SIDE_QV
    )
    return recto, verso


def order_on(
    islands: tuple[IslandSites, ...],
    site_attr: str,
) -> tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...]:
    """Sort islands by line then index of that tablet's site."""
    sorted_islands = sorted(
        islands,
        key=lambda island: line_then_index(getattr(island, site_attr)),
    )
    return tuple(
        (island.tokens, island.n, getattr(island, site_attr))
        for island in sorted_islands
    )


def token_order(
    ordered: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
) -> tuple[tuple[str, ...], ...]:
    """Island token sequences in the given reading order."""
    return tuple(tokens for tokens, _n, _site in ordered)


def same_recto_order(
    hr_order: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
    pr_order: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
    qr_order: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
) -> bool:
    """True iff H, P, and Q share the same island-token sequence."""
    return token_order(hr_order) == token_order(pr_order) == token_order(qr_order)


def verso_row(verso: tuple[IslandSites, ...]) -> tuple:
    """Single verso island as (tokens, n, Hv, Pv, Qv)."""
    if len(verso) != 1:
        raise ValueError(f"expected one verso island, got {len(verso)}")
    island = verso[0]
    return (island.tokens, island.n, island.h, island.p, island.q)


def verso_mixed_into_recto(
    recto_orders: tuple[tuple, ...],
    verso: tuple,
) -> bool:
    """True iff the verso token sequence appears in a recto order."""
    verso_tokens = verso[0]
    return any(tokens == verso_tokens for ordered in recto_orders for tokens, _n, _site in ordered)


class TestHpqIslandRectoOrderHelpers(unittest.TestCase):
    """Helpers on synthetic sites. No CV, no LLM."""

    def test_line_then_index_sorts_line_before_index(self):
        """Later line sorts after; same line sorts by index."""
        provider = MockProvider()
        self.assertEqual(line_then_index((SIDE_HR, "Hr3", 27)), (3, 27))
        self.assertEqual(line_then_index((SIDE_PR, "Pr7", 10)), (7, 10))
        self.assertEqual(line_then_index((SIDE_QR, "Qr12", 0)), (12, 0))
        earlier = IslandSites(("A",), 1, (SIDE_HR, "Hr7", 47), (SIDE_PR, "Pr7", 10), (SIDE_QR, "Qr7", 28))
        later = IslandSites(("B",), 1, (SIDE_HR, "Hr8", 0), (SIDE_PR, "Pr7", 29), (SIDE_QR, "Qr7", 47))
        self.assertLess(line_then_index(earlier.h), line_then_index(later.h))
        self.assertLess(line_then_index(earlier.p), line_then_index(later.p))
        self.assertLess(line_then_index(earlier.q), line_then_index(later.q))
        self.assertEqual(provider.get_call_history(), [])

    def test_split_and_order_keep_verso_out(self):
        """Recto sort ignores verso; swapped P sites make orders differ."""
        provider = MockProvider()
        islands = tuple(island_from_maximal(row) for row in STANDING_MAXIMALS)
        recto, verso = split_recto_verso(islands)
        self.assertEqual(len(recto), STANDING_RECTO_COUNT)
        self.assertEqual(len(verso), STANDING_VERSO_COUNT)
        self.assertEqual(verso_row(verso), STANDING_VERSO)
        hr_order = order_on(recto, "h")
        pr_order = order_on(recto, "p")
        qr_order = order_on(recto, "q")
        self.assertEqual(token_order(hr_order), STANDING_TOKEN_ORDER)
        self.assertTrue(same_recto_order(hr_order, pr_order, qr_order))
        self.assertFalse(verso_mixed_into_recto((hr_order, pr_order, qr_order), STANDING_VERSO))
        swapped = (
            IslandSites(recto[0].tokens, recto[0].n, recto[0].h, recto[1].p, recto[0].q),
            IslandSites(recto[1].tokens, recto[1].n, recto[1].h, recto[0].p, recto[1].q),
            *recto[2:],
        )
        swapped_pr = order_on(swapped, "p")
        self.assertFalse(same_recto_order(hr_order, swapped_pr, qr_order))
        self.assertEqual(len(islands), STANDING_MAXIMAL_COUNT)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHpqIslandRectoOrderScoreboard(unittest.TestCase):
    """Cited-fixture H/P/Q recto-island reading-order lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_q_h_p_sides()
        self.combined = score_hpq_triple_n8(self.by_side, H_SIDES, P_SIDES, Q_SIDES)
        self.maximals = tuple(
            island_from_triple_row(row)
            for row in maximal_triple_rows(self.combined)
        )
        self.standing = tuple(island_from_maximal(row) for row in STANDING_MAXIMALS)
        self.recto, self.verso = split_recto_verso(self.maximals)
        self.hr_order = order_on(self.recto, "h")
        self.pr_order = order_on(self.recto, "p")
        self.qr_order = order_on(self.recto, "q")

    def test_recto_orders_match_and_verso_is_separate(self):
        """Hr/Pr/Qr share one four-island order. Verso stays off that row."""
        self.assertEqual(self.maximals, self.standing)
        self.assertEqual(len(self.recto), STANDING_RECTO_COUNT)
        self.assertEqual(len(self.verso), STANDING_VERSO_COUNT)
        self.assertEqual(len(self.recto) + len(self.verso), STANDING_MAXIMAL_COUNT)
        self.assertEqual(self.hr_order, STANDING_HR_ORDER)
        self.assertEqual(self.pr_order, STANDING_PR_ORDER)
        self.assertEqual(self.qr_order, STANDING_QR_ORDER)
        self.assertEqual(token_order(self.hr_order), STANDING_TOKEN_ORDER)
        self.assertEqual(token_order(self.pr_order), STANDING_TOKEN_ORDER)
        self.assertEqual(token_order(self.qr_order), STANDING_TOKEN_ORDER)
        self.assertEqual(
            same_recto_order(self.hr_order, self.pr_order, self.qr_order),
            STANDING_SAME_ORDER,
        )
        self.assertTrue(STANDING_SAME_ORDER)
        self.assertFalse(STANDING_BAG_OF_FORMULAS)
        self.assertTrue(STANDING_COPIED_RECTO_ORDER)
        self.assertEqual(verso_row(self.verso), STANDING_VERSO)
        self.assertEqual(
            verso_mixed_into_recto(
                (self.hr_order, self.pr_order, self.qr_order),
                STANDING_VERSO,
            ),
            STANDING_VERSO_MIXED_INTO_RECTO,
        )
        self.assertFalse(STANDING_VERSO_MIXED_INTO_RECTO)
        for island in self.recto:
            self.assertEqual(island.h[0], SIDE_HR)
            self.assertEqual(island.p[0], SIDE_PR)
            self.assertEqual(island.q[0], SIDE_QR)
            self.assertNotIn(island.h[0], VERSO_SIDES)
        for island in self.verso:
            self.assertEqual(island.h[0], SIDE_HV)
            self.assertEqual(island.p[0], SIDE_PV)
            self.assertEqual(island.q[0], SIDE_QV)
            self.assertNotIn(island.h[0], RECTO_SIDES)
        standing_recto, standing_verso = split_recto_verso(self.standing)
        self.assertEqual(
            tuple(row[5][0] for row in STANDING_HR_PR_QR_MAXIMALS),
            (SIDE_HR,) * STANDING_RECTO_COUNT,
        )
        self.assertEqual(
            tuple(row[5][0] for row in STANDING_HV_PV_QV_MAXIMALS),
            (SIDE_HV,) * STANDING_VERSO_COUNT,
        )
        self.assertEqual(len(standing_recto), STANDING_RECTO_COUNT)
        self.assertEqual(len(standing_verso), STANDING_VERSO_COUNT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_hpq_island_off_hpq_scoreboard_still_computes(self):
        """Cycle 72 off-H/P/Q island-absent lock stays."""
        prior = TestMamariHpqIslandOffHpqScoreboard()
        prior.setUp()
        prior.test_five_by_twelve_hit_table()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-73 recto reading-order lock."""
        lock = self.survey["tablet_h_p_q_island_recto_order"]
        self.assertEqual(lock["cycle"], 73)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["recto_count"], STANDING_RECTO_COUNT)
        self.assertEqual(lock["verso_count"], STANDING_VERSO_COUNT)

        def locked_order(rows):
            return tuple(
                (tuple(tokens), n, tuple(site))
                for tokens, n, site in rows
            )

        self.assertEqual(locked_order(lock["hr_order"]), STANDING_HR_ORDER)
        self.assertEqual(locked_order(lock["pr_order"]), STANDING_PR_ORDER)
        self.assertEqual(locked_order(lock["qr_order"]), STANDING_QR_ORDER)
        self.assertEqual(
            tuple(tuple(tokens) for tokens in lock["token_order"]),
            STANDING_TOKEN_ORDER,
        )
        self.assertEqual(lock["same_order"], STANDING_SAME_ORDER)
        self.assertTrue(lock["same_order"])
        self.assertEqual(lock["bag_of_formulas"], STANDING_BAG_OF_FORMULAS)
        self.assertFalse(lock["bag_of_formulas"])
        self.assertEqual(lock["copied_recto_order"], STANDING_COPIED_RECTO_ORDER)
        self.assertTrue(lock["copied_recto_order"])
        locked_verso = (
            tuple(lock["verso"][0]),
            lock["verso"][1],
            tuple(lock["verso"][2]),
            tuple(lock["verso"][3]),
            tuple(lock["verso"][4]),
        )
        self.assertEqual(locked_verso, STANDING_VERSO)
        self.assertEqual(lock["verso_mixed_into_recto"], STANDING_VERSO_MIXED_INTO_RECTO)
        self.assertFalse(lock["verso_mixed_into_recto"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hp_shared_n8_unchanged"])
        self.assertTrue(lock["standing_q_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_h_p_q_island_off_hpq_hits"]["cycle"], 72)
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHpqIslandRectoOrderImageSnapshot(unittest.TestCase):
    """Cycle 73 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
