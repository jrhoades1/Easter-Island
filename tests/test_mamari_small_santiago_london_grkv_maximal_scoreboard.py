"""Gr–Kv island 6 n=15: suffix of the n=25 vs a separate maximal.

Cycle 78 text-search lock. Uses already-vendored Gr.html and Kv.html,
the cycle-67/74 island-5 and island-6 sites, the cycle-75 gap
10-gram, and the cycle-76 n=25 (gap 10-gram + island 6). Does not
scrape a new tablet. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents. Not a meaning dictionary.

On Gr and on Kv the n=15 sits inside the n=25 at the same sites:
the n=25 starts 10 stems earlier at the gap 10-gram (measured).
Flattened Gr–Kv maximals n≥8 through that window are n=10
(island 5) and n=25 (gap+6), not n=10 and n=15.

Claim that can lose: the old island 6 n=15 is not a Gr–Kv
maximal (it is a suffix of the n=25) vs it is still a separate
maximal. Operationalized as island6_is_suffix vs
island6_is_maximal.

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_gk_islands_off_hpq_scoreboard import (
    TestMamariGkIslandsOffHpqScoreboard,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_gr_kv_15gram_scoreboard import GRAM_15
from tests.test_mamari_small_santiago_london_grkv_block_scoreboard import (
    ISLAND_5_GR,
    ISLAND_6_GR,
    ISLAND_5_KV,
    ISLAND_6_KV,
    STANDING_COMBINED_SHARED_TOKENS,
    STANDING_FLATTENED_MAXIMAL_NS,
    STANDING_GAP_10GRAM,
    flattened_maximals,
    span_stems,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_KV,
    load_g_k_sides,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    GRAM_10_KV,
    LINE_NAMES,
    STANDING_GR_KV_MAXIMALS as STANDING_PER_LINE_GR_KV_MAXIMALS,
    STANDING_NEW_TABLET,
    SharedN8Row,
)

MIN_SHARED_N8 = 8
STANDING_N15 = GRAM_15
STANDING_N25 = STANDING_COMBINED_SHARED_TOKENS
STANDING_N25_GR = (SIDE_GR, "Gr6", 44)
STANDING_N25_KV = (SIDE_KV, "Kv3", 26)
STANDING_N25_END_GR = (SIDE_GR, "Gr7", 14)
STANDING_N25_END_KV = (SIDE_KV, "Kv4", 21)
STANDING_N15_GR = (SIDE_GR, "Gr7", 0)
STANDING_N15_KV = (SIDE_KV, "Kv4", 7)
STANDING_N15_END_GR = STANDING_N25_END_GR
STANDING_N15_END_KV = STANDING_N25_END_KV
STANDING_SUFFIX_OFFSET = 10
STANDING_N25_HIT_COUNT = 1
STANDING_N15_HIT_COUNT = 1
STANDING_ISLAND6_IS_SUFFIX = True
STANDING_ISLAND6_IS_MAXIMAL = False
STANDING_GR_KV_MAXIMALS = (10, 25)
STANDING_TABLET_D_SCRAPED = False
STANDING_RESULT = "gk_grkv_maximals"


@dataclass(frozen=True)
class GrKvMaximals:
    """Island-6 vs n=25 suffix / maximal poles. Ids only."""

    n25_tokens: tuple[str, ...]
    n15_tokens: tuple[str, ...]
    n25_starts: tuple[tuple[str, str, int], ...]
    n15_starts: tuple[tuple[str, str, int], ...]
    n25_ends: tuple[tuple[str, str, int], ...]
    n15_ends: tuple[tuple[str, str, int], ...]
    suffix_offset: int
    island6_is_suffix: bool
    island6_is_maximal: bool
    gr_kv_maximals: tuple[int, ...]


def flatten_side(
    by_side: dict[str, list[list[str]]],
    side: str,
) -> tuple[list[str], list[tuple[str, str, int]]]:
    """Concatenated stems with (side, line, index) sites. Crosses lines."""
    stems: list[str] = []
    sites: list[tuple[str, str, int]] = []
    names = LINE_NAMES[side]
    for line_index, line in enumerate(by_side[side]):
        for index, stem in enumerate(line):
            stems.append(stem)
            sites.append((side, names[line_index], index))
    return stems, sites


def find_gram_hits(
    stems: list[str],
    sites: list[tuple[str, str, int]],
    gram: tuple[str, ...],
) -> tuple[tuple[int, tuple[str, str, int], tuple[str, str, int]], ...]:
    """(flat_index, start_site, end_site) for every exact hit."""
    n = len(gram)
    hits: list[tuple[int, tuple[str, str, int], tuple[str, str, int]]] = []
    if n == 0 or n > len(stems):
        return ()
    for start in range(len(stems) - n + 1):
        if tuple(stems[start : start + n]) == gram:
            hits.append((start, sites[start], sites[start + n - 1]))
    return tuple(hits)


def tokens_are_suffix(inner: tuple[str, ...], outer: tuple[str, ...]) -> bool:
    """True iff inner is a proper suffix of outer."""
    return bool(inner) and len(inner) < len(outer) and outer[-len(inner) :] == inner


def sites_are_suffix(
    inner_hits: tuple[tuple[int, tuple[str, str, int], tuple[str, str, int]], ...],
    outer_hits: tuple[tuple[int, tuple[str, str, int], tuple[str, str, int]], ...],
    inner_n: int,
    outer_n: int,
) -> bool:
    """True iff each inner hit is the last inner_n stems of an outer hit."""
    offset = outer_n - inner_n
    if offset <= 0 or not inner_hits or not outer_hits:
        return False
    outer_by_end = {end: flat for flat, _start, end in outer_hits}
    for flat, _start, end in inner_hits:
        if end not in outer_by_end:
            return False
        if flat != outer_by_end[end] + offset:
            return False
    return True


def island6_is_suffix(
    n15: tuple[str, ...],
    n25: tuple[str, ...],
    n15_hits: tuple[tuple[int, tuple[str, str, int], tuple[str, str, int]], ...],
    n25_hits: tuple[tuple[int, tuple[str, str, int], tuple[str, str, int]], ...],
) -> bool:
    """True iff the n=15 is a suffix of the n=25 at the same sites."""
    return tokens_are_suffix(n15, n25) and sites_are_suffix(
        n15_hits, n25_hits, len(n15), len(n25)
    )


def island6_is_maximal(
    maximals: tuple[SharedN8Row, ...],
    n15: tuple[str, ...] = STANDING_N15,
) -> bool:
    """True iff the n=15 is itself a flattened maximal (not a subspan)."""
    return any(row.tokens == n15 for row in maximals)


def reading_order_maximal_ns(
    window: list[str] | tuple[str, ...],
    maximals: tuple[SharedN8Row, ...],
) -> tuple[int, ...]:
    """Maximal n values in first-start order on one flattened window."""
    window_tokens = tuple(window)
    starts: list[tuple[int, int]] = []
    for row in maximals:
        start = len(window_tokens)
        for index in range(len(window_tokens) - row.n + 1):
            if window_tokens[index : index + row.n] == row.tokens:
                start = index
                break
        starts.append((start, row.n))
    starts.sort()
    return tuple(n for _start, n in starts)


def suffix_offset(
    inner_hits: tuple[tuple[int, tuple[str, str, int], tuple[str, str, int]], ...],
    outer_hits: tuple[tuple[int, tuple[str, str, int], tuple[str, str, int]], ...],
) -> int:
    """Flat-index delta from n=25 start to n=15 start. -1 if a hit is missing."""
    if not inner_hits or not outer_hits:
        return -1
    return inner_hits[0][0] - outer_hits[0][0]


def score_grkv_maximals(
    by_side: dict[str, list[list[str]]],
    n15: tuple[str, ...] = STANDING_N15,
    n25: tuple[str, ...] = STANDING_N25,
) -> GrKvMaximals:
    """Sites, suffix / maximal poles, and reading-order flattened ns."""
    window_gr = span_stems(by_side, ISLAND_5_GR, ISLAND_6_GR)
    window_kv = span_stems(by_side, ISLAND_5_KV, ISLAND_6_KV)
    maximals = flattened_maximals(window_gr, window_kv)
    gr_stems, gr_sites = flatten_side(by_side, SIDE_GR)
    kv_stems, kv_sites = flatten_side(by_side, SIDE_KV)
    n25_gr = find_gram_hits(gr_stems, gr_sites, n25)
    n25_kv = find_gram_hits(kv_stems, kv_sites, n25)
    n15_gr = find_gram_hits(gr_stems, gr_sites, n15)
    n15_kv = find_gram_hits(kv_stems, kv_sites, n15)
    suffix = island6_is_suffix(n15, n25, n15_gr, n25_gr) and island6_is_suffix(
        n15, n25, n15_kv, n25_kv
    )
    offset_gr = suffix_offset(n15_gr, n25_gr)
    offset_kv = suffix_offset(n15_kv, n25_kv)
    offset = offset_gr if offset_gr == offset_kv else -1
    return GrKvMaximals(
        n25_tokens=n25,
        n15_tokens=n15,
        n25_starts=(n25_gr[0][1], n25_kv[0][1]) if n25_gr and n25_kv else (),
        n15_starts=(n15_gr[0][1], n15_kv[0][1]) if n15_gr and n15_kv else (),
        n25_ends=(n25_gr[0][2], n25_kv[0][2]) if n25_gr and n25_kv else (),
        n15_ends=(n15_gr[0][2], n15_kv[0][2]) if n15_gr and n15_kv else (),
        suffix_offset=offset,
        island6_is_suffix=suffix,
        island6_is_maximal=island6_is_maximal(maximals, n15),
        gr_kv_maximals=reading_order_maximal_ns(window_gr, maximals),
    )


class TestSmallSantiagoLondonGrkvMaximalHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_suffix_tokens_and_sites(self):
        """Suffix needs a proper token tail and matching ends / offset."""
        provider = MockProvider()
        n25 = STANDING_N25
        n15 = STANDING_N15
        self.assertTrue(tokens_are_suffix(n15, n25))
        self.assertEqual(n25[:10], STANDING_GAP_10GRAM)
        self.assertEqual(n25[10:], n15)
        self.assertFalse(tokens_are_suffix(n25, n15))
        self.assertFalse(tokens_are_suffix(n15, n15))
        self.assertFalse(tokens_are_suffix((), n25))
        broken = n25[:-1] + ("999",)
        self.assertFalse(tokens_are_suffix(n15, broken))
        outer = ((0, ("Gr", "Gr6", 44), ("Gr", "Gr7", 14)),)
        inner = ((10, ("Gr", "Gr7", 0), ("Gr", "Gr7", 14)),)
        self.assertTrue(sites_are_suffix(inner, outer, 15, 25))
        self.assertTrue(island6_is_suffix(n15, n25, inner, outer))
        shifted = ((11, ("Gr", "Gr7", 1), ("Gr", "Gr7", 15)),)
        self.assertFalse(sites_are_suffix(shifted, outer, 15, 25))
        self.assertFalse(island6_is_suffix(n15, n25, shifted, outer))
        self.assertFalse(island6_is_suffix(n15, n25, (), outer))
        self.assertEqual(suffix_offset(inner, outer), 10)
        self.assertEqual(suffix_offset((), outer), -1)
        self.assertEqual(provider.get_call_history(), [])

    def test_maximal_vs_suffix_poles(self):
        """Contained n=15 is not a maximal; a planted n=15 is."""
        provider = MockProvider()
        window = list(GRAM_10_KV) + ["066"] + list(STANDING_N25)
        peer = list(GRAM_10_KV) + ["009"] + list(STANDING_N25)
        maximals = flattened_maximals(window, peer)
        self.assertEqual(tuple(row.n for row in maximals), STANDING_FLATTENED_MAXIMAL_NS)
        self.assertEqual(reading_order_maximal_ns(window, maximals), (10, 25))
        self.assertFalse(island6_is_maximal(maximals, STANDING_N15))
        planted = (
            SharedN8Row(STANDING_N15, 15, 1, 1, (), ()),
            SharedN8Row(GRAM_10_KV, 10, 1, 1, (), ()),
        )
        self.assertTrue(island6_is_maximal(planted, STANDING_N15))
        self.assertEqual(reading_order_maximal_ns(list(GRAM_10_KV) + list(STANDING_N15), planted), (10, 15))
        self.assertNotEqual((10, 15), STANDING_GR_KV_MAXIMALS)
        self.assertEqual(
            tuple(row[1] for row in STANDING_PER_LINE_GR_KV_MAXIMALS),
            (15, 10),
        )
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonGrkvMaximalScoreboard(unittest.TestCase):
    """Cited-fixture Gr–Kv n=15 suffix vs maximal lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_g_k_sides()
        self.scored = score_grkv_maximals(self.by_side)

    def test_n15_is_suffix_of_n25_not_a_maximal(self):
        """n=25 at Gr6[44]/Kv3[26]; n=15 is its suffix; maximals [10, 25]."""
        self.assertEqual(self.scored.n25_tokens, STANDING_N25)
        self.assertEqual(self.scored.n15_tokens, STANDING_N15)
        self.assertEqual(len(STANDING_N25), 25)
        self.assertEqual(len(STANDING_N15), 15)
        self.assertEqual(STANDING_N25[:10], STANDING_GAP_10GRAM)
        self.assertEqual(STANDING_N25[10:], STANDING_N15)
        self.assertTrue(tokens_are_suffix(STANDING_N15, STANDING_N25))
        self.assertEqual(self.scored.n25_starts, (STANDING_N25_GR, STANDING_N25_KV))
        self.assertEqual(self.scored.n15_starts, (STANDING_N15_GR, STANDING_N15_KV))
        self.assertEqual(self.scored.n25_ends, (STANDING_N25_END_GR, STANDING_N25_END_KV))
        self.assertEqual(self.scored.n15_ends, (STANDING_N15_END_GR, STANDING_N15_END_KV))
        self.assertEqual(self.scored.n25_ends, self.scored.n15_ends)
        self.assertEqual(self.scored.suffix_offset, STANDING_SUFFIX_OFFSET)
        self.assertEqual(self.scored.suffix_offset, 10)
        self.assertEqual(len(STANDING_N25) - len(STANDING_N15), STANDING_SUFFIX_OFFSET)
        self.assertEqual(ISLAND_6_GR[2], STANDING_N15_GR)
        self.assertEqual(ISLAND_6_KV[2], STANDING_N15_KV)
        self.assertEqual(ISLAND_5_GR[0], GRAM_10_KV)
        self.assertEqual(ISLAND_6_GR[0], GRAM_15)
        gr_stems, gr_sites = flatten_side(self.by_side, SIDE_GR)
        kv_stems, kv_sites = flatten_side(self.by_side, SIDE_KV)
        n25_gr = find_gram_hits(gr_stems, gr_sites, STANDING_N25)
        n25_kv = find_gram_hits(kv_stems, kv_sites, STANDING_N25)
        n15_gr = find_gram_hits(gr_stems, gr_sites, STANDING_N15)
        n15_kv = find_gram_hits(kv_stems, kv_sites, STANDING_N15)
        self.assertEqual(len(n25_gr), STANDING_N25_HIT_COUNT)
        self.assertEqual(len(n25_kv), STANDING_N25_HIT_COUNT)
        self.assertEqual(len(n15_gr), STANDING_N15_HIT_COUNT)
        self.assertEqual(len(n15_kv), STANDING_N15_HIT_COUNT)
        self.assertEqual(n25_gr[0][1], STANDING_N25_GR)
        self.assertEqual(n25_kv[0][1], STANDING_N25_KV)
        self.assertEqual(n15_gr[0][1], STANDING_N15_GR)
        self.assertEqual(n15_kv[0][1], STANDING_N15_KV)
        self.assertTrue(island6_is_suffix(STANDING_N15, STANDING_N25, n15_gr, n25_gr))
        self.assertTrue(island6_is_suffix(STANDING_N15, STANDING_N25, n15_kv, n25_kv))
        self.assertEqual(self.scored.island6_is_suffix, STANDING_ISLAND6_IS_SUFFIX)
        self.assertEqual(self.scored.island6_is_maximal, STANDING_ISLAND6_IS_MAXIMAL)
        self.assertTrue(STANDING_ISLAND6_IS_SUFFIX)
        self.assertFalse(STANDING_ISLAND6_IS_MAXIMAL)
        self.assertNotEqual(STANDING_ISLAND6_IS_SUFFIX, STANDING_ISLAND6_IS_MAXIMAL)
        window_gr = span_stems(self.by_side, ISLAND_5_GR, ISLAND_6_GR)
        window_kv = span_stems(self.by_side, ISLAND_5_KV, ISLAND_6_KV)
        maximals = flattened_maximals(window_gr, window_kv)
        self.assertEqual(tuple(row.n for row in maximals), STANDING_FLATTENED_MAXIMAL_NS)
        self.assertEqual(self.scored.gr_kv_maximals, STANDING_GR_KV_MAXIMALS)
        self.assertEqual(self.scored.gr_kv_maximals, (10, 25))
        self.assertNotEqual(self.scored.gr_kv_maximals, (10, 15))
        self.assertFalse(island6_is_maximal(maximals, STANDING_N15))
        self.assertGreaterEqual(len(STANDING_N25), MIN_SHARED_N8)
        self.assertEqual(
            tuple(row[1] for row in STANDING_PER_LINE_GR_KV_MAXIMALS),
            (15, 10),
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_island_off_hpq_scoreboard_still_computes(self):
        """Cycle 77 G–K island-absent-on-H/P/Q lock stays."""
        prior = TestMamariGkIslandsOffHpqScoreboard()
        prior.setUp()
        prior.test_seven_by_six_hit_table()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-78 Gr–Kv maximal lock."""
        lock = self.survey["tablet_g_k_grkv_maximals"]
        self.assertEqual(lock["cycle"], 78)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["n25_tokens"]), STANDING_N25)
        self.assertEqual(tuple(lock["n15_tokens"]), STANDING_N15)
        self.assertEqual(tuple(lock["gap_10gram"]), STANDING_GAP_10GRAM)
        self.assertEqual(
            tuple(tuple(site) for site in lock["n25_starts"]),
            (STANDING_N25_GR, STANDING_N25_KV),
        )
        self.assertEqual(
            tuple(tuple(site) for site in lock["n15_starts"]),
            (STANDING_N15_GR, STANDING_N15_KV),
        )
        self.assertEqual(
            tuple(tuple(site) for site in lock["n25_ends"]),
            (STANDING_N25_END_GR, STANDING_N25_END_KV),
        )
        self.assertEqual(
            tuple(tuple(site) for site in lock["n15_ends"]),
            (STANDING_N15_END_GR, STANDING_N15_END_KV),
        )
        self.assertEqual(lock["suffix_offset"], STANDING_SUFFIX_OFFSET)
        self.assertEqual(lock["suffix_offset"], 10)
        self.assertEqual(lock["island6_is_suffix"], STANDING_ISLAND6_IS_SUFFIX)
        self.assertEqual(lock["island6_is_maximal"], STANDING_ISLAND6_IS_MAXIMAL)
        self.assertTrue(lock["island6_is_suffix"])
        self.assertFalse(lock["island6_is_maximal"])
        self.assertEqual(tuple(lock["gr_kv_maximals"]), STANDING_GR_KV_MAXIMALS)
        self.assertEqual(tuple(lock["gr_kv_maximals"]), (10, 25))
        self.assertNotEqual(tuple(lock["gr_kv_maximals"]), (10, 15))
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertTrue(lock["standing_gk_island_reading_order_unchanged"])
        self.assertTrue(lock["standing_gk_island_gaps_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_block_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_hpq_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_island_off_hpq_hits"]["cycle"], 77)
        self.assertEqual(self.survey["tablet_g_k_grkv_block"]["cycle"], 76)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonGrkvMaximalImageSnapshot(unittest.TestCase):
    """Cycle 78 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
