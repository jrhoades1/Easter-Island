"""B vs the G–K n=12 island's doubled 8-gram suffix.

Cycle 106 text-search lock. Uses already-vendored A–V and the
cycle-105 / cycle-67 n=12 island suffix. Does not vendor a new
tablet. Does not scrape X. W has no Barthel (cycle 100); skip W.
Does not redo G–K n≥8 inventories. Raw stems. No invented Barthel.
No G00n→Barthel map. No type merge. No detector retune. No CV.
No new agents. Not a meaning dictionary.

Locks exact hit counts and sites of 260 001 004 711 260 001 004 711
on every vendored tablet A–V (same contiguous Barthel parser as
the leak table / island scoreboards). Claim that can lose:
b_has_gk_doubled_8gram. Also restates that the full n=12 island
is 0 on B (suffix-only if B hits). Do not retune the sequence.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_aruku_br_scoreboard import BR_LINE_NAMES
from tests.test_mamari_aruku_bv_scoreboard import BV_LINE_NAMES
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    GRAM4,
    STANDING_B_SITES as CYCLE_105_B_SITES,
    STANDING_ISLAND_G_SITE,
    STANDING_ISLAND_K_SITE,
    STANDING_ISLAND_N,
    STANDING_ISLAND_OFFSETS,
    TestMamariKMaxNGkIslandSubstringScoreboard,
    load_b_sides,
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
from tests.test_mamari_small_santiago_london_island_off_gk_scoreboard import (
    TestMamariSmallSantiagoLondonIslandOffGkScoreboard,
)
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
    TestMamariSmallSantiagoLondonSharedN8Scoreboard,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

SIDE_BR = "Br"
SIDE_BV = "Bv"
GRAM8 = GRAM_12[4:]
STANDING_B_HITS = 1
STANDING_G_HITS = 1
STANDING_K_HITS = 1
STANDING_BR_HITS = 0
STANDING_BV_HITS = 1
STANDING_GR_HITS = 1
STANDING_GV_HITS = 0
STANDING_KR_HITS = 1
STANDING_KV_HITS = 0
STANDING_B_SITES = ((SIDE_BV, "Bv8", 21),)
STANDING_G_SITES = ((SIDE_GR, "Gr1", 8),)
STANDING_K_SITES = ((SIDE_KR, "Kr1", 6),)
STANDING_BR_SITES = ()
STANDING_GV_SITES = ()
STANDING_KV_SITES = ()
STANDING_HITS_BY_TABLET = (
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
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
STANDING_ISLAND12_B_HITS = 0
STANDING_ISLAND12_G_HITS = 1
STANDING_ISLAND12_K_HITS = 1
STANDING_ISLAND12_B_SITES = ()
STANDING_ISLAND12_G_SITES = (STANDING_ISLAND_G_SITE,)
STANDING_ISLAND12_K_SITES = (STANDING_ISLAND_K_SITE,)
STANDING_ISLAND12_HITS_BY_TABLET = (
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
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
STANDING_B_HAS_GK_DOUBLED_8GRAM = True
STANDING_CLAIM = "b_has_gk_doubled_8gram"
STANDING_RESULT = "b_has_gk_doubled_8gram"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_SUFFIX_ONLY_ON_B = True
CYCLE_105_CANDIDATE_B_SITE = (SIDE_BV, "Bv8", 21)


def b_has_gk_doubled_8gram(b_hits: int) -> bool:
    """True iff tablet B has at least one exact contiguous 8-gram hit."""
    return b_hits > 0


class TestBGkDoubled8GramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent doubled 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("260", "001", "004", "711"))
        self.assertEqual(GRAM8, GRAM4 + GRAM4)
        self.assertEqual(GRAM8, GRAM_12[4:])
        self.assertEqual(len(GRAM8), 8)
        adjacent = [list(GRAM8)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM8), 1)
        gapped = [list(GRAM4) + ["999"] + list(GRAM4)]
        self.assertEqual(ngram_hit_count(gapped, GRAM8), 0)
        four_only = [list(GRAM4)]
        self.assertEqual(ngram_hit_count(four_only, GRAM8), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM8), 0)
        self.assertTrue(b_has_gk_doubled_8gram(1))
        self.assertFalse(b_has_gk_doubled_8gram(0))
        self.assertEqual(STANDING_CLAIM, "b_has_gk_doubled_8gram")
        self.assertTrue(STANDING_B_HAS_GK_DOUBLED_8GRAM)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariBGkDoubled8GramScoreboard(unittest.TestCase):
    """Cited-fixture doubled 8-gram vs A–V. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.b_sides = load_b_sides()
        self.gk_sides = load_g_k_sides()
        self.k_sites = named_side_hits(
            self.gk_sides[SIDE_KR], KR_LINE_NAMES, SIDE_KR, GRAM8
        ) + named_side_hits(self.gk_sides[SIDE_KV], KV_LINE_NAMES, SIDE_KV, GRAM8)
        self.b_sites = named_side_hits(
            self.b_sides[SIDE_BR], BR_LINE_NAMES, SIDE_BR, GRAM8
        ) + named_side_hits(self.b_sides[SIDE_BV], BV_LINE_NAMES, SIDE_BV, GRAM8)
        self.g_sites = named_side_hits(
            self.gk_sides[SIDE_GR], GR_LINE_NAMES, SIDE_GR, GRAM8
        ) + named_side_hits(self.gk_sides[SIDE_GV], GV_LINE_NAMES, SIDE_GV, GRAM8)
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM8, VENDORED_TABLETS)
        self.island12_hits_by_tablet = tablet_hit_counts(
            self.by_tablet, GRAM_12, VENDORED_TABLETS
        )
        self.island12_b_sites = named_side_hits(
            self.b_sides[SIDE_BR], BR_LINE_NAMES, SIDE_BR, GRAM_12
        ) + named_side_hits(self.b_sides[SIDE_BV], BV_LINE_NAMES, SIDE_BV, GRAM_12)
        self.island12_g_sites = named_side_hits(
            self.gk_sides[SIDE_GR], GR_LINE_NAMES, SIDE_GR, GRAM_12
        ) + named_side_hits(self.gk_sides[SIDE_GV], GV_LINE_NAMES, SIDE_GV, GRAM_12)
        self.island12_k_sites = named_side_hits(
            self.gk_sides[SIDE_KR], KR_LINE_NAMES, SIDE_KR, GRAM_12
        ) + named_side_hits(self.gk_sides[SIDE_KV], KV_LINE_NAMES, SIDE_KV, GRAM_12)
        self.claim_holds = b_has_gk_doubled_8gram(
            self.hits_by_tablet[VENDORED_TABLETS.index("B")]
        )

    def test_tokens_are_locked_island_suffix(self):
        """8-gram is the cycle-67/105 n=12 island suffix. None invented."""
        self.assertEqual(GRAM8, ("260", "001", "004", "711", "260", "001", "004", "711"))
        self.assertEqual(GRAM8, GRAM4 + GRAM4)
        self.assertEqual(GRAM8, GRAM_12[4:])
        self.assertEqual(len(GRAM8), 8)
        self.assertEqual(GRAM4, ("260", "001", "004", "711"))
        self.assertEqual(STANDING_ISLAND_N, 12)
        self.assertEqual(len(GRAM_12), 12)
        self.assertEqual(STANDING_ISLAND_OFFSETS, (4, 8))
        self.assertEqual(
            tuple(
                self.survey["k_max_n_gk_island_substring"]["matching_islands"][0][
                    "tokens"
                ]
            ),
            GRAM_12,
        )
        self.assertEqual(
            tuple(self.survey["k_max_n_gk_island_substring"]["tokens4"]),
            GRAM4,
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_8gram_hits_on_every_vendored_tablet(self):
        """B=1, G=1, K=1; else 0 on A–V. Claim holds from the B count."""
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("B")], STANDING_B_HITS)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("G")], STANDING_G_HITS)
        self.assertEqual(self.hits_by_tablet[VENDORED_TABLETS.index("K")], STANDING_K_HITS)
        for letter, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], GRAM8))
            if letter not in ("B", "G", "K"):
                self.assertEqual(count, 0)
        self.assertEqual(self.claim_holds, STANDING_B_HAS_GK_DOUBLED_8GRAM)
        self.assertTrue(STANDING_B_HAS_GK_DOUBLED_8GRAM)
        self.assertTrue(b_has_gk_doubled_8gram(STANDING_B_HITS))
        self.assertEqual(STANDING_CLAIM, "b_has_gk_doubled_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_b_g_and_k_sites_are_locked_addresses(self):
        """B hit is the cycle-105 Bv8[21] candidate; G/K are island-suffix starts."""
        self.assertEqual(tuple(site_tuple(hit) for hit in self.b_sites), STANDING_B_SITES)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.g_sites), STANDING_G_SITES)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.k_sites), STANDING_K_SITES)
        self.assertEqual(len(self.b_sites), STANDING_B_HITS)
        self.assertEqual(len(self.g_sites), STANDING_G_HITS)
        self.assertEqual(len(self.k_sites), STANDING_K_HITS)
        self.assertEqual(STANDING_B_SITES[0], CYCLE_105_CANDIDATE_B_SITE)
        self.assertEqual(STANDING_B_SITES[0], CYCLE_105_B_SITES[0])
        self.assertEqual(STANDING_BR_SITES, ())
        self.assertEqual(STANDING_GV_SITES, ())
        self.assertEqual(STANDING_KV_SITES, ())
        self.assertEqual(ngram_hit_count(self.b_sides[SIDE_BR], GRAM8), STANDING_BR_HITS)
        self.assertEqual(ngram_hit_count(self.b_sides[SIDE_BV], GRAM8), STANDING_BV_HITS)
        self.assertEqual(ngram_hit_count(self.gk_sides[SIDE_GR], GRAM8), STANDING_GR_HITS)
        self.assertEqual(ngram_hit_count(self.gk_sides[SIDE_GV], GRAM8), STANDING_GV_HITS)
        self.assertEqual(ngram_hit_count(self.gk_sides[SIDE_KR], GRAM8), STANDING_KR_HITS)
        self.assertEqual(ngram_hit_count(self.gk_sides[SIDE_KV], GRAM8), STANDING_KV_HITS)
        for side, line, index in STANDING_B_SITES:
            names = BR_LINE_NAMES if side == SIDE_BR else BV_LINE_NAMES
            stems = self.b_sides[side][names.index(line)][index : index + 8]
            self.assertEqual(tuple(stems), GRAM8)
        for side, line, index in STANDING_G_SITES:
            names = GR_LINE_NAMES if side == SIDE_GR else GV_LINE_NAMES
            stems = self.gk_sides[side][names.index(line)][index : index + 8]
            self.assertEqual(tuple(stems), GRAM8)
        for side, line, index in STANDING_K_SITES:
            names = KR_LINE_NAMES if side == SIDE_KR else KV_LINE_NAMES
            stems = self.gk_sides[side][names.index(line)][index : index + 8]
            self.assertEqual(tuple(stems), GRAM8)
        g_start = STANDING_ISLAND_G_SITE[2] + STANDING_ISLAND_OFFSETS[0]
        k_start = STANDING_ISLAND_K_SITE[2] + STANDING_ISLAND_OFFSETS[0]
        self.assertEqual(STANDING_G_SITES, ((SIDE_GR, "Gr1", g_start),))
        self.assertEqual(STANDING_K_SITES, ((SIDE_KR, "Kr1", k_start),))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n12_island_remains_zero_on_b(self):
        """Full island stays 0 on B; 8-gram leak is suffix-only."""
        self.assertEqual(self.island12_hits_by_tablet, STANDING_ISLAND12_HITS_BY_TABLET)
        self.assertEqual(
            self.island12_hits_by_tablet[VENDORED_TABLETS.index("B")],
            STANDING_ISLAND12_B_HITS,
        )
        self.assertEqual(STANDING_ISLAND12_B_HITS, 0)
        self.assertEqual(
            ngram_hit_count(self.by_tablet["B"], GRAM_12),
            STANDING_ISLAND12_B_HITS,
        )
        self.assertEqual(
            tuple(site_tuple(hit) for hit in self.island12_b_sites),
            STANDING_ISLAND12_B_SITES,
        )
        self.assertEqual(
            tuple(site_tuple(hit) for hit in self.island12_g_sites),
            STANDING_ISLAND12_G_SITES,
        )
        self.assertEqual(
            tuple(site_tuple(hit) for hit in self.island12_k_sites),
            STANDING_ISLAND12_K_SITES,
        )
        self.assertEqual(
            self.island12_hits_by_tablet[VENDORED_TABLETS.index("G")],
            STANDING_ISLAND12_G_HITS,
        )
        self.assertEqual(
            self.island12_hits_by_tablet[VENDORED_TABLETS.index("K")],
            STANDING_ISLAND12_K_HITS,
        )
        self.assertTrue(STANDING_SUFFIX_ONLY_ON_B)
        self.assertGreater(STANDING_B_HITS, 0)
        self.assertEqual(STANDING_ISLAND12_B_HITS, 0)
        self.assertEqual(STANDING_MAXIMAL_COUNT, 6)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.survey["tablet_g_k_island_off_gk_hits"]["cycle"], 68)
        self.assertFalse(self.survey["tablet_g_k_island_off_gk_hits"]["any_off_gk"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_substring_island_and_w_scoreboards_still_compute(self):
        """Cycle 105 substring, cycle 68 off-G/K, cycle 67 n≥8, and W stay."""
        prior_105 = TestMamariKMaxNGkIslandSubstringScoreboard()
        prior_105.setUp()
        prior_105.test_4gram_is_substring_of_locked_n12_island_only()
        prior_105.test_survey_matches_computed_lock()
        prior_off = TestMamariSmallSantiagoLondonIslandOffGkScoreboard()
        prior_off.setUp()
        prior_off.test_six_by_eight_hit_table()
        prior_off.test_survey_matches_computed_lock()
        prior_n8 = TestMamariSmallSantiagoLondonSharedN8Scoreboard()
        prior_n8.setUp()
        prior_n8.test_inventory_tokens_n_freq_and_hits()
        prior_n8.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-106 doubled 8-gram lock."""
        lock = self.survey["b_gk_doubled_8gram"]
        self.assertEqual(lock["cycle"], 106)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens8"]), GRAM8)
        self.assertEqual(lock["n8"], 8)
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(tuple(lock["island12_tokens"]), GRAM_12)
        self.assertEqual(lock["from_cycle"], 105)
        self.assertEqual(lock["b_hits"], STANDING_B_HITS)
        self.assertEqual(lock["g_hits"], STANDING_G_HITS)
        self.assertEqual(lock["k_hits"], STANDING_K_HITS)
        self.assertEqual(tuple(tuple(row) for row in lock["b_sites"]), STANDING_B_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["g_sites"]), STANDING_G_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["k_sites"]), STANDING_K_SITES)
        self.assertEqual(lock["br_hits"], STANDING_BR_HITS)
        self.assertEqual(lock["bv_hits"], STANDING_BV_HITS)
        self.assertEqual(lock["gr_hits"], STANDING_GR_HITS)
        self.assertEqual(lock["gv_hits"], STANDING_GV_HITS)
        self.assertEqual(lock["kr_hits"], STANDING_KR_HITS)
        self.assertEqual(lock["kv_hits"], STANDING_KV_HITS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["b_has_gk_doubled_8gram"])
        self.assertEqual(
            lock["b_has_gk_doubled_8gram"],
            STANDING_B_HAS_GK_DOUBLED_8GRAM,
        )
        self.assertEqual(lock["island12_b_hits"], STANDING_ISLAND12_B_HITS)
        self.assertEqual(lock["island12_g_hits"], STANDING_ISLAND12_G_HITS)
        self.assertEqual(lock["island12_k_hits"], STANDING_ISLAND12_K_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["island12_b_sites"]),
            STANDING_ISLAND12_B_SITES,
        )
        self.assertEqual(
            tuple(lock["island12_hits_by_tablet"]),
            STANDING_ISLAND12_HITS_BY_TABLET,
        )
        self.assertTrue(lock["suffix_only_on_b"])
        self.assertEqual(lock["suffix_only_on_b"], STANDING_SUFFIX_ONLY_ON_B)
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_k_max_n_gk_island_substring_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["k_max_n_gk_island_substring"]["cycle"], 105)
        self.assertTrue(
            self.survey["k_max_n_gk_island_substring"]["k_max_n_is_gk_island_substring"]
        )
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["cycle"], 67)
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["maximal_count"], 6)
        self.assertEqual(self.survey["tablet_g_k_island_off_gk_hits"]["cycle"], 68)
        self.assertFalse(self.survey["tablet_g_k_island_off_gk_hits"]["any_off_gk"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariBGkDoubled8GramImageSnapshot(unittest.TestCase):
    """Cycle 106 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
