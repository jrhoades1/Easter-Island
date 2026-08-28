"""G–K maximal-island reading order on existing G/K fixtures.

Cycle 74 text-search lock. Uses already-vendored Gr/Gv, Kr/Kv
and the cycle-67 maximal islands. Existing line/index sites
only. Does not scrape a new tablet. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. Not a meaning dictionary.

Sort all six islands by Gr line then index. Sort the four
Gr–Kr islands by Kr line then index. Sort the two Gr–Kv
islands by Kv line then index. Lock those three sequences
and whether Gr–Kr (resp. Gr–Kv) share relative order.

Claim that can lose: the four Gr–Kr islands are colinear
(same order on Gr and Kr) vs scrambled (orders differ).

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import re
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_island_off_gk_scoreboard import (
    TestMamariSmallSantiagoLondonIslandOffGkScoreboard,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    G_SIDES,
    K_SIDES,
    SIDE_GR,
    SIDE_GV,
    SIDE_KR,
    SIDE_KV,
    load_g_k_sides,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    GRAM_10_KR,
    GRAM_10_KV,
    GRAM_12,
    GRAM_13,
    STANDING_GR_KR_MAXIMALS,
    STANDING_GR_KV_MAXIMALS,
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    STANDING_NEW_TABLET,
    SharedN8Row,
    maximal_rows,
    score_shared_n8,
)
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import GRAM_17
from tests.test_mamari_small_santiago_london_gr_kv_15gram_scoreboard import GRAM_15

STANDING_GR_COUNT = 6
STANDING_KR_COUNT = 4
STANDING_KV_COUNT = 2
STANDING_GV_COUNT = 0
STANDING_GR_ORDER = (
    (GRAM_12, 12, (SIDE_GR, "Gr1", 4)),
    (GRAM_13, 13, (SIDE_GR, "Gr2", 4)),
    (GRAM_10_KR, 10, (SIDE_GR, "Gr3", 28)),
    (GRAM_17, 17, (SIDE_GR, "Gr4", 3)),
    (GRAM_10_KV, 10, (SIDE_GR, "Gr6", 33)),
    (GRAM_15, 15, (SIDE_GR, "Gr7", 0)),
)
STANDING_KR_ORDER = (
    (GRAM_12, 12, (SIDE_KR, "Kr1", 2)),
    (GRAM_13, 13, (SIDE_KR, "Kr2", 16)),
    (GRAM_10_KR, 10, (SIDE_KR, "Kr4", 12)),
    (GRAM_17, 17, (SIDE_KR, "Kr5", 0)),
)
STANDING_KV_ORDER = (
    (GRAM_10_KV, 10, (SIDE_KV, "Kv3", 15)),
    (GRAM_15, 15, (SIDE_KV, "Kv4", 7)),
)
STANDING_GR_TOKEN_ORDER = tuple(row[0] for row in STANDING_GR_ORDER)
STANDING_GR_KR_TOKEN_ORDER = tuple(row[0] for row in STANDING_KR_ORDER)
STANDING_GR_KV_TOKEN_ORDER = tuple(row[0] for row in STANDING_KV_ORDER)
STANDING_GR_KR_SAME_ORDER = True
STANDING_GR_KV_SAME_ORDER = True
STANDING_KR_COLINEAR = True
STANDING_KR_SCRAMBLED = False
STANDING_TABLET_D_SCRAPED = False
STANDING_RESULT = "gk_island_reading_order"


@dataclass(frozen=True)
class IslandSites:
    """One maximal island's tokens and Gr / K sites. Ids only."""

    tokens: tuple[str, ...]
    n: int
    g: tuple[str, str, int]
    k: tuple[str, str, int]


def island_from_maximal(row: tuple) -> IslandSites:
    """Unpack a cycle-67 maximal tuple."""
    tokens, n, _freq_g, _freq_k, g_site, k_site = row
    return IslandSites(tokens=tokens, n=n, g=g_site, k=k_site)


def island_from_shared_row(row: SharedN8Row) -> IslandSites:
    """One Gr site and one K site from a scored maximal row."""
    return IslandSites(
        tokens=row.tokens,
        n=row.n,
        g=row.hits_g[0],
        k=row.hits_k[0],
    )


def line_then_index(site: tuple[str, str, int]) -> tuple[int, int]:
    """(line number, index) from a (side, line_name, index) site."""
    _side, line_name, index = site
    match = re.search(r"(\d+)$", line_name)
    if match is None:
        raise ValueError(f"no line number in {line_name!r}")
    return (int(match.group(1)), index)


def split_kr_kv(
    islands: tuple[IslandSites, ...],
) -> tuple[tuple[IslandSites, ...], tuple[IslandSites, ...]]:
    """Kr-sided and Kv-sided partitions. No mixing."""
    kr = tuple(island for island in islands if island.k[0] == SIDE_KR)
    kv = tuple(island for island in islands if island.k[0] == SIDE_KV)
    return kr, kv


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


def same_relative_order(
    left: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
    right: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
) -> bool:
    """True iff both orders share the same island-token sequence."""
    return token_order(left) == token_order(right)


def kr_colinear(
    gr_kr_on_gr: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
    kr_order: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
) -> bool:
    """True iff the four Gr–Kr islands keep Gr order on Kr."""
    return same_relative_order(gr_kr_on_gr, kr_order)


def kr_scrambled(
    gr_kr_on_gr: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
    kr_order: tuple[tuple[tuple[str, ...], int, tuple[str, str, int]], ...],
) -> bool:
    """True iff the four Gr–Kr islands change order on Kr."""
    return not kr_colinear(gr_kr_on_gr, kr_order)


class TestSmallSantiagoLondonIslandOrderHelpers(unittest.TestCase):
    """Helpers on synthetic sites. No CV, no LLM."""

    def test_line_then_index_sorts_line_before_index(self):
        """Later line sorts after; same line sorts by index."""
        provider = MockProvider()
        self.assertEqual(line_then_index((SIDE_GR, "Gr1", 4)), (1, 4))
        self.assertEqual(line_then_index((SIDE_KR, "Kr4", 12)), (4, 12))
        self.assertEqual(line_then_index((SIDE_KV, "Kv12", 0)), (12, 0))
        earlier = IslandSites(
            ("A",), 1, (SIDE_GR, "Gr3", 28), (SIDE_KR, "Kr4", 12)
        )
        later = IslandSites(
            ("B",), 1, (SIDE_GR, "Gr4", 3), (SIDE_KR, "Kr5", 0)
        )
        self.assertLess(line_then_index(earlier.g), line_then_index(later.g))
        self.assertLess(line_then_index(earlier.k), line_then_index(later.k))
        self.assertEqual(provider.get_call_history(), [])

    def test_split_and_order_keep_sides_apart(self):
        """Kr sort ignores Kv; swapped Kr sites scramble colinearity."""
        provider = MockProvider()
        islands = tuple(island_from_maximal(row) for row in STANDING_MAXIMALS)
        kr, kv = split_kr_kv(islands)
        self.assertEqual(len(islands), STANDING_GR_COUNT)
        self.assertEqual(len(kr), STANDING_KR_COUNT)
        self.assertEqual(len(kv), STANDING_KV_COUNT)
        self.assertEqual(len(kr) + len(kv), STANDING_MAXIMAL_COUNT)
        gr_order = order_on(islands, "g")
        kr_order = order_on(kr, "k")
        kv_order = order_on(kv, "k")
        gr_kr_on_gr = order_on(kr, "g")
        gr_kv_on_gr = order_on(kv, "g")
        self.assertEqual(token_order(gr_order), STANDING_GR_TOKEN_ORDER)
        self.assertEqual(token_order(kr_order), STANDING_GR_KR_TOKEN_ORDER)
        self.assertEqual(token_order(kv_order), STANDING_GR_KV_TOKEN_ORDER)
        self.assertTrue(same_relative_order(gr_kr_on_gr, kr_order))
        self.assertTrue(same_relative_order(gr_kv_on_gr, kv_order))
        self.assertTrue(kr_colinear(gr_kr_on_gr, kr_order))
        self.assertFalse(kr_scrambled(gr_kr_on_gr, kr_order))
        swapped = (
            IslandSites(kr[0].tokens, kr[0].n, kr[0].g, kr[1].k),
            IslandSites(kr[1].tokens, kr[1].n, kr[1].g, kr[0].k),
            *kr[2:],
        )
        swapped_kr = order_on(swapped, "k")
        self.assertFalse(same_relative_order(gr_kr_on_gr, swapped_kr))
        self.assertFalse(kr_colinear(gr_kr_on_gr, swapped_kr))
        self.assertTrue(kr_scrambled(gr_kr_on_gr, swapped_kr))
        self.assertEqual(len(STANDING_GR_KR_MAXIMALS), STANDING_KR_COUNT)
        self.assertEqual(len(STANDING_GR_KV_MAXIMALS), STANDING_KV_COUNT)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonIslandOrderScoreboard(unittest.TestCase):
    """Cited-fixture G–K island reading-order lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_g_k_sides()
        self.combined = score_shared_n8(self.by_side, G_SIDES, K_SIDES)
        self.maximals = tuple(
            island_from_shared_row(row) for row in maximal_rows(self.combined)
        )
        self.standing = tuple(island_from_maximal(row) for row in STANDING_MAXIMALS)
        self.kr, self.kv = split_kr_kv(self.maximals)
        self.gr_order = order_on(self.maximals, "g")
        self.kr_order = order_on(self.kr, "k")
        self.kv_order = order_on(self.kv, "k")
        self.gr_kr_on_gr = order_on(self.kr, "g")
        self.gr_kv_on_gr = order_on(self.kv, "g")

    def test_orders_and_same_order_booleans(self):
        """Gr order of six; Kr of four; Kv of two. Kr colinear, not scrambled."""
        self.assertEqual(self.maximals, self.standing)
        self.assertEqual(len(self.maximals), STANDING_GR_COUNT)
        self.assertEqual(len(self.kr), STANDING_KR_COUNT)
        self.assertEqual(len(self.kv), STANDING_KV_COUNT)
        self.assertEqual(len(self.kr) + len(self.kv), STANDING_MAXIMAL_COUNT)
        self.assertEqual(self.gr_order, STANDING_GR_ORDER)
        self.assertEqual(self.kr_order, STANDING_KR_ORDER)
        self.assertEqual(self.kv_order, STANDING_KV_ORDER)
        self.assertEqual(token_order(self.gr_order), STANDING_GR_TOKEN_ORDER)
        self.assertEqual(token_order(self.kr_order), STANDING_GR_KR_TOKEN_ORDER)
        self.assertEqual(token_order(self.kv_order), STANDING_GR_KV_TOKEN_ORDER)
        self.assertEqual(
            same_relative_order(self.gr_kr_on_gr, self.kr_order),
            STANDING_GR_KR_SAME_ORDER,
        )
        self.assertEqual(
            same_relative_order(self.gr_kv_on_gr, self.kv_order),
            STANDING_GR_KV_SAME_ORDER,
        )
        self.assertEqual(
            kr_colinear(self.gr_kr_on_gr, self.kr_order),
            STANDING_KR_COLINEAR,
        )
        self.assertEqual(
            kr_scrambled(self.gr_kr_on_gr, self.kr_order),
            STANDING_KR_SCRAMBLED,
        )
        self.assertTrue(STANDING_GR_KR_SAME_ORDER)
        self.assertTrue(STANDING_GR_KV_SAME_ORDER)
        self.assertTrue(STANDING_KR_COLINEAR)
        self.assertFalse(STANDING_KR_SCRAMBLED)
        for island in self.maximals:
            self.assertEqual(island.g[0], SIDE_GR)
            self.assertNotEqual(island.g[0], SIDE_GV)
        for island in self.kr:
            self.assertEqual(island.k[0], SIDE_KR)
            self.assertNotEqual(island.k[0], SIDE_KV)
        for island in self.kv:
            self.assertEqual(island.k[0], SIDE_KV)
            self.assertNotEqual(island.k[0], SIDE_KR)
        self.assertEqual(STANDING_GV_COUNT, 0)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_island_off_gk_scoreboard_still_computes(self):
        """Cycle 68 off-G/K island-absent lock stays."""
        prior = TestMamariSmallSantiagoLondonIslandOffGkScoreboard()
        prior.setUp()
        prior.test_six_by_eight_hit_table()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-74 G–K reading-order lock."""
        lock = self.survey["tablet_g_k_island_reading_order"]
        self.assertEqual(lock["cycle"], 74)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["gr_count"], STANDING_GR_COUNT)
        self.assertEqual(lock["kr_count"], STANDING_KR_COUNT)
        self.assertEqual(lock["kv_count"], STANDING_KV_COUNT)
        self.assertEqual(lock["gv_count"], STANDING_GV_COUNT)

        def locked_order(rows):
            return tuple(
                (tuple(tokens), n, tuple(site))
                for tokens, n, site in rows
            )

        self.assertEqual(locked_order(lock["gr_order"]), STANDING_GR_ORDER)
        self.assertEqual(locked_order(lock["kr_order"]), STANDING_KR_ORDER)
        self.assertEqual(locked_order(lock["kv_order"]), STANDING_KV_ORDER)
        self.assertEqual(
            tuple(tuple(tokens) for tokens in lock["gr_token_order"]),
            STANDING_GR_TOKEN_ORDER,
        )
        self.assertEqual(lock["gr_kr_same_order"], STANDING_GR_KR_SAME_ORDER)
        self.assertTrue(lock["gr_kr_same_order"])
        self.assertEqual(lock["gr_kv_same_order"], STANDING_GR_KV_SAME_ORDER)
        self.assertTrue(lock["gr_kv_same_order"])
        self.assertEqual(lock["kr_colinear"], STANDING_KR_COLINEAR)
        self.assertTrue(lock["kr_colinear"])
        self.assertEqual(lock["kr_scrambled"], STANDING_KR_SCRAMBLED)
        self.assertFalse(lock["kr_scrambled"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_island_off_hpq_unchanged"])
        self.assertTrue(lock["standing_hpq_island_recto_order_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_island_off_gk_hits"]["cycle"], 68)
        self.assertEqual(self.survey["tablet_h_p_q_island_recto_order"]["cycle"], 73)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonIslandOrderImageSnapshot(unittest.TestCase):
    """Cycle 74 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
