"""K's cycle-99/104 representative 4-gram vs locked G–K n≥8 islands.

Cycle 105 text-search lock. Uses already-vendored A–V and the
cycle-99/104 K representative plus the cycle-67 six maximal G–K
islands. Does not vendor a new tablet. Does not scrape X. W has
no Barthel (cycle 100); skip W. Does not redo G–K n≥8 inventories.
Raw stems. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents. Not a meaning dictionary.

Locks exact hit sites of 260 001 004 711 on K, B, and G (same
contiguous Barthel parser as the leak table) and whether that
4-gram is an exact contiguous substring of a locked G–K n≥8
island. Claim that can lose: k_max_n_is_gk_island_substring.
A leak-count clash locks the real counts and fails the cycle-104
restatement (no retune).

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_aruku_br_scoreboard import (
    BR_LINE_NAMES,
    br_line_stems,
    extract_br_published_tokens,
    load_vendored_br_html,
)
from tests.test_mamari_aruku_bv_scoreboard import (
    BV_LINE_NAMES,
    bv_line_stems,
    extract_bv_published_tokens,
    load_vendored_bv_html,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_N as INVENTORY_LONGEST_N,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_TOKENS as INVENTORY_LONGEST_TOKENS,
)
from tests.test_mamari_corpus_max_n_leak_table_scoreboard import (
    HYPOTHESIS_LEAK_PAIRS,
    TestMamariCorpusMaxNLeakTableScoreboard,
    leak_table_holds,
    leaks_from_hits,
    representative_hits,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_london_kr_scoreboard import KR_LINE_NAMES
from tests.test_mamari_small_london_kv_scoreboard import KV_LINE_NAMES
from tests.test_mamari_small_santiago_gr_scoreboard import GR_LINE_NAMES
from tests.test_mamari_small_santiago_gv_scoreboard import GV_LINE_NAMES
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_GV,
    SIDE_KR,
    SIDE_KV,
    load_g_k_sides,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    GRAM_12,
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    TestMamariSmallSantiagoLondonSharedN8Scoreboard,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

SIDE_BR = "Br"
SIDE_BV = "Bv"
GRAM4 = INVENTORY_LONGEST_TOKENS["K"]
LOCKED_ISLANDS = tuple(tokens for tokens, _n, _fg, _fk, _gs, _ks in STANDING_MAXIMALS)
STANDING_K_HITS = 2
STANDING_B_HITS = 3
STANDING_G_HITS = 2
STANDING_BR_HITS = 0
STANDING_BV_HITS = 3
STANDING_GR_HITS = 2
STANDING_GV_HITS = 0
STANDING_KR_HITS = 2
STANDING_KV_HITS = 0
STANDING_K_SITES = (
    (SIDE_KR, "Kr1", 6),
    (SIDE_KR, "Kr1", 10),
)
STANDING_B_SITES = (
    (SIDE_BV, "Bv8", 21),
    (SIDE_BV, "Bv8", 25),
    (SIDE_BV, "Bv9", 34),
)
STANDING_G_SITES = (
    (SIDE_GR, "Gr1", 8),
    (SIDE_GR, "Gr1", 12),
)
STANDING_BR_SITES = ()
STANDING_GV_SITES = ()
STANDING_KV_SITES = ()
STANDING_HITS_BY_TABLET = (
    0,
    3,
    0,
    0,
    0,
    0,
    2,
    0,
    0,
    0,
    2,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
)
STANDING_LEAK_COUNTS = {"B": 3, "G": 2}
STANDING_LEAK_TABLE_HOLDS = True
STANDING_ISLAND_N = 12
STANDING_ISLAND_TOKENS = GRAM_12
STANDING_ISLAND_G_SITE = (SIDE_GR, "Gr1", 4)
STANDING_ISLAND_K_SITE = (SIDE_KR, "Kr1", 2)
STANDING_ISLAND_OFFSETS = (4, 8)
STANDING_MATCHING_ISLANDS = (
    (
        STANDING_ISLAND_TOKENS,
        STANDING_ISLAND_N,
        STANDING_ISLAND_G_SITE,
        STANDING_ISLAND_K_SITE,
        STANDING_ISLAND_OFFSETS,
    ),
)
STANDING_MATCHING_ISLAND_COUNT = 1
STANDING_K_MAX_N_IS_GK_ISLAND_SUBSTRING = True
STANDING_CLAIM = "k_max_n_is_gk_island_substring"
STANDING_RESULT = "k_max_n_gk_island_substring"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False


def load_b_sides() -> dict[str, list[list[str]]]:
    """Already-vendored Br / Bv. No new scrape."""
    return {
        SIDE_BR: br_line_stems(extract_br_published_tokens(load_vendored_br_html())),
        SIDE_BV: bv_line_stems(extract_bv_published_tokens(load_vendored_bv_html())),
    }


def is_contiguous_substring(
    needle: tuple[str, ...],
    haystack: tuple[str, ...],
) -> bool:
    """True iff needle is an exact contiguous run inside haystack."""
    return bool(substring_offsets(needle, haystack))


def substring_offsets(
    needle: tuple[str, ...],
    haystack: tuple[str, ...],
) -> tuple[int, ...]:
    """Start indexes of exact contiguous needle hits. Search only."""
    n = len(needle)
    if n == 0 or n > len(haystack):
        return ()
    return tuple(
        index
        for index in range(len(haystack) - n + 1)
        if haystack[index : index + n] == needle
    )


def matching_islands(
    gram: tuple[str, ...] = GRAM4,
    maximals: tuple = STANDING_MAXIMALS,
) -> tuple[tuple, ...]:
    """Locked islands whose tokens contain gram as a contiguous run."""
    rows = []
    for tokens, n, _freq_g, _freq_k, g_site, k_site in maximals:
        offsets = substring_offsets(gram, tokens)
        if offsets:
            rows.append((tokens, n, g_site, k_site, offsets))
    return tuple(rows)


def k_max_n_is_gk_island_substring(
    gram: tuple[str, ...] = GRAM4,
    maximals: tuple = STANDING_MAXIMALS,
) -> bool:
    """True iff the K representative sits inside at least one locked island."""
    return bool(matching_islands(gram, maximals))


class TestKMaxNGkIslandSubstringHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_substring_requires_contiguous_tokens(self):
        """A gap is not a substring; the planted island is."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("260", "001", "004", "711"))
        self.assertTrue(is_contiguous_substring(GRAM4, GRAM_12))
        self.assertEqual(substring_offsets(GRAM4, GRAM_12), (4, 8))
        gapped = GRAM_12[:4] + ("999",) + GRAM_12[4:]
        self.assertFalse(is_contiguous_substring(GRAM4, gapped[:8]))
        self.assertEqual(substring_offsets(GRAM4, ("260", "001", "999", "004", "711")), ())
        self.assertEqual(substring_offsets((), GRAM_12), ())
        self.assertEqual(substring_offsets(GRAM4, GRAM4[:3]), ())
        self.assertTrue(is_contiguous_substring(GRAM4, GRAM4))
        self.assertEqual(provider.get_call_history(), [])

    def test_matching_islands_are_exact_locked_rows(self):
        """Only islands that contain the 4-gram count; a miss stays empty."""
        provider = MockProvider()
        planted = (
            (GRAM_12, 12, 1, 1, STANDING_ISLAND_G_SITE, STANDING_ISLAND_K_SITE),
            (("380", "001", "003", "005", "006", "010", "380", "001"), 8, 1, 1, ("Gr", "Gx", 0), ("Kr", "Kx", 0)),
        )
        self.assertEqual(matching_islands(GRAM4, planted), STANDING_MATCHING_ISLANDS)
        self.assertTrue(k_max_n_is_gk_island_substring(GRAM4, planted))
        self.assertFalse(k_max_n_is_gk_island_substring(("999", "999", "999", "999"), planted))
        self.assertEqual(STANDING_CLAIM, "k_max_n_is_gk_island_substring")
        self.assertTrue(STANDING_K_MAX_N_IS_GK_ISLAND_SUBSTRING)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariKMaxNGkIslandSubstringScoreboard(unittest.TestCase):
    """Cited-fixture K 4-gram vs G–K islands. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.b_sides = load_b_sides()
        self.gk_sides = load_g_k_sides()
        self.k_sites = named_side_hits(
            self.gk_sides[SIDE_KR], KR_LINE_NAMES, SIDE_KR, GRAM4
        ) + named_side_hits(self.gk_sides[SIDE_KV], KV_LINE_NAMES, SIDE_KV, GRAM4)
        self.b_sites = named_side_hits(
            self.b_sides[SIDE_BR], BR_LINE_NAMES, SIDE_BR, GRAM4
        ) + named_side_hits(self.b_sides[SIDE_BV], BV_LINE_NAMES, SIDE_BV, GRAM4)
        self.g_sites = named_side_hits(
            self.gk_sides[SIDE_GR], GR_LINE_NAMES, SIDE_GR, GRAM4
        ) + named_side_hits(self.gk_sides[SIDE_GV], GV_LINE_NAMES, SIDE_GV, GRAM4)
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM4, VENDORED_TABLETS)
        self.leaks = leaks_from_hits("K", self.hits_by_tablet)
        self.matches = matching_islands(GRAM4)
        self.claim_holds = k_max_n_is_gk_island_substring(GRAM4)

    def test_tokens_are_cycle_99_k_representative(self):
        """4-gram is the cycle-99/104 K representative. None invented."""
        self.assertEqual(GRAM4, INVENTORY_LONGEST_TOKENS["K"])
        self.assertEqual(GRAM4, ("260", "001", "004", "711"))
        self.assertEqual(INVENTORY_LONGEST_N["K"], 4)
        self.assertEqual(len(GRAM4), 4)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["K"]["longest_tokens"]),
            GRAM4,
        )
        self.assertEqual(
            tuple(self.survey["corpus_max_n_leak_table"]["rows"]["K"]["longest_tokens"]),
            GRAM4,
        )
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["K"]["longest_n"], 4)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_leak_counts_hold_at_cycle_104_sites(self):
        """B=3, G=2, K=2; else 0 on A–V. Leak-table restatement holds."""
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("B")], STANDING_B_HITS)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("G")], STANDING_G_HITS)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("K")], STANDING_K_HITS)
        self.assertEqual(self.leaks, STANDING_LEAK_COUNTS)
        for letter, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], GRAM4))
            if letter not in ("B", "G", "K"):
                self.assertEqual(count, 0)
        representative = representative_hits(GRAM4, self.by_tablet)
        self.assertEqual(representative, STANDING_HITS_BY_TABLET)
        self.assertEqual(leaks_from_hits("K", representative), {"B": 3, "G": 2})
        self.assertTrue(
            leak_table_holds(
                {
                    "H": {"Q": 2},
                    "K": self.leaks,
                    "P": {"H": 2, "Q": 2},
                    "Q": {"H": 2},
                }
            )
        )
        self.assertTrue(STANDING_LEAK_TABLE_HOLDS)
        self.assertIn(("K", "B", 3), HYPOTHESIS_LEAK_PAIRS)
        self.assertIn(("K", "G", 2), HYPOTHESIS_LEAK_PAIRS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_b_g_and_k_sites_are_locked_addresses(self):
        """K→B leak has a site list, not just a count. G and K too."""
        self.assertEqual(tuple(site_tuple(hit) for hit in self.k_sites), STANDING_K_SITES)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.b_sites), STANDING_B_SITES)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.g_sites), STANDING_G_SITES)
        self.assertEqual(len(self.k_sites), STANDING_K_HITS)
        self.assertEqual(len(self.b_sites), STANDING_B_HITS)
        self.assertEqual(len(self.g_sites), STANDING_G_HITS)
        self.assertEqual(STANDING_BR_SITES, ())
        self.assertEqual(STANDING_GV_SITES, ())
        self.assertEqual(STANDING_KV_SITES, ())
        self.assertEqual(ngram_hit_count(self.b_sides[SIDE_BR], GRAM4), STANDING_BR_HITS)
        self.assertEqual(ngram_hit_count(self.b_sides[SIDE_BV], GRAM4), STANDING_BV_HITS)
        self.assertEqual(ngram_hit_count(self.gk_sides[SIDE_GR], GRAM4), STANDING_GR_HITS)
        self.assertEqual(ngram_hit_count(self.gk_sides[SIDE_GV], GRAM4), STANDING_GV_HITS)
        self.assertEqual(ngram_hit_count(self.gk_sides[SIDE_KR], GRAM4), STANDING_KR_HITS)
        self.assertEqual(ngram_hit_count(self.gk_sides[SIDE_KV], GRAM4), STANDING_KV_HITS)
        for side, line, index in STANDING_B_SITES:
            names = BR_LINE_NAMES if side == SIDE_BR else BV_LINE_NAMES
            stems = self.b_sides[side][names.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), GRAM4)
        for side, line, index in STANDING_G_SITES:
            names = GR_LINE_NAMES if side == SIDE_GR else GV_LINE_NAMES
            stems = self.gk_sides[side][names.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), GRAM4)
        for side, line, index in STANDING_K_SITES:
            names = KR_LINE_NAMES if side == SIDE_KR else KV_LINE_NAMES
            stems = self.gk_sides[side][names.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), GRAM4)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_4gram_is_substring_of_locked_n12_island_only(self):
        """Boolean is true; only the Gr1[4]/Kr1[2] n=12 island contains it."""
        self.assertEqual(len(LOCKED_ISLANDS), STANDING_MAXIMAL_COUNT)
        self.assertEqual(STANDING_MAXIMAL_COUNT, 6)
        self.assertEqual(self.matches, STANDING_MATCHING_ISLANDS)
        self.assertEqual(len(self.matches), STANDING_MATCHING_ISLAND_COUNT)
        self.assertEqual(STANDING_MATCHING_ISLAND_COUNT, 1)
        tokens, n, g_site, k_site, offsets = self.matches[0]
        self.assertEqual(tokens, STANDING_ISLAND_TOKENS)
        self.assertEqual(tokens, GRAM_12)
        self.assertEqual(n, STANDING_ISLAND_N)
        self.assertEqual(g_site, STANDING_ISLAND_G_SITE)
        self.assertEqual(k_site, STANDING_ISLAND_K_SITE)
        self.assertEqual(offsets, STANDING_ISLAND_OFFSETS)
        self.assertTrue(is_contiguous_substring(GRAM4, GRAM_12))
        for island in LOCKED_ISLANDS:
            if island == GRAM_12:
                self.assertTrue(is_contiguous_substring(GRAM4, island))
            else:
                self.assertFalse(is_contiguous_substring(GRAM4, island))
        g_start = STANDING_ISLAND_G_SITE[2]
        k_start = STANDING_ISLAND_K_SITE[2]
        self.assertEqual(
            tuple((SIDE_GR, "Gr1", g_start + offset) for offset in offsets),
            STANDING_G_SITES,
        )
        self.assertEqual(
            tuple((SIDE_KR, "Kr1", k_start + offset) for offset in offsets),
            STANDING_K_SITES,
        )
        self.assertEqual(self.claim_holds, STANDING_K_MAX_N_IS_GK_ISLAND_SUBSTRING)
        self.assertTrue(STANDING_K_MAX_N_IS_GK_ISLAND_SUBSTRING)
        self.assertEqual(STANDING_CLAIM, "k_max_n_is_gk_island_substring")
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertLess(len(GRAM4), 8)
        self.assertEqual(ngram_hit_count(self.by_tablet["B"], GRAM_12), 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_leak_inventory_and_gk_scoreboards_still_compute(self):
        """Cycle 104 leak table, cycle 99 inventory, and cycle 67 G–K stay."""
        prior_leak = TestMamariCorpusMaxNLeakTableScoreboard()
        prior_leak.setUp()
        prior_leak.test_leak_table_holds_at_cycle_99_counts()
        prior_leak.test_survey_matches_computed_lock()
        prior_n8 = TestMamariSmallSantiagoLondonSharedN8Scoreboard()
        prior_n8.setUp()
        prior_n8.test_inventory_tokens_n_freq_and_hits()
        prior_n8.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-105 K 4-gram island lock."""
        lock = self.survey["k_max_n_gk_island_substring"]
        self.assertEqual(lock["cycle"], 105)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], 4)
        self.assertEqual(lock["from_cycle"], 99)
        self.assertEqual(lock["k_hits"], STANDING_K_HITS)
        self.assertEqual(lock["b_hits"], STANDING_B_HITS)
        self.assertEqual(lock["g_hits"], STANDING_G_HITS)
        self.assertEqual(tuple(tuple(row) for row in lock["k_sites"]), STANDING_K_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["b_sites"]), STANDING_B_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["g_sites"]), STANDING_G_SITES)
        self.assertEqual(lock["br_hits"], STANDING_BR_HITS)
        self.assertEqual(lock["bv_hits"], STANDING_BV_HITS)
        self.assertEqual(lock["gr_hits"], STANDING_GR_HITS)
        self.assertEqual(lock["gv_hits"], STANDING_GV_HITS)
        self.assertEqual(lock["kr_hits"], STANDING_KR_HITS)
        self.assertEqual(lock["kv_hits"], STANDING_KV_HITS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["leak_counts"], STANDING_LEAK_COUNTS)
        self.assertTrue(lock["leak_table_holds"])
        self.assertEqual(lock["leak_table_holds"], STANDING_LEAK_TABLE_HOLDS)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["k_max_n_is_gk_island_substring"])
        self.assertEqual(
            lock["k_max_n_is_gk_island_substring"],
            STANDING_K_MAX_N_IS_GK_ISLAND_SUBSTRING,
        )
        self.assertEqual(lock["matching_island_count"], STANDING_MATCHING_ISLAND_COUNT)
        self.assertEqual(lock["island_count"], STANDING_MAXIMAL_COUNT)
        match = lock["matching_islands"][0]
        self.assertEqual(tuple(match["tokens"]), STANDING_ISLAND_TOKENS)
        self.assertEqual(match["n"], STANDING_ISLAND_N)
        self.assertEqual(tuple(match["g_site"]), STANDING_ISLAND_G_SITE)
        self.assertEqual(tuple(match["k_site"]), STANDING_ISLAND_K_SITE)
        self.assertEqual(tuple(match["offsets"]), STANDING_ISLAND_OFFSETS)
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(
            self.survey["corpus_max_n_leak_table"]["rows"]["K"]["leak_counts"],
            {"B": 3, "G": 2},
        )
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["cycle"], 67)
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["maximal_count"], 6)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariKMaxNGkIslandSubstringImageSnapshot(unittest.TestCase):
    """Cycle 105 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
