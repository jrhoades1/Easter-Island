"""B's cycle-99 representative 8-gram vs the G–K doubled 8-gram.

Cycle 114 text-search lock. Uses already-vendored A–V and the
cycle-99 / cycle-104 B representative plus the cycle-106
doubled 8-gram suffix. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Does not redo
G–K n≥8 inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents. Not a meaning dictionary.

Locks whether B's cycle-99 longest 8-gram is that doubled G–K
suffix, and the representative's exact hits on every vendored
tablet A–V. Claim that can lose: b_max_n_is_gk_doubled_8gram.
The sequences differ, so the claim is false. Cycle 104 said B
is exact-0 off home; this cycle locks the real B leak row
(B=2, else 0; leak_table_b_home_only holds). Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_aruku_br_scoreboard import BR_LINE_NAMES
from tests.test_mamari_aruku_bv_scoreboard import BV_LINE_NAMES
from tests.test_mamari_b_gk_doubled_8gram_scoreboard import (
    GRAM8,
    TestMamariBGkDoubled8GramScoreboard,
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
    TestMamariCorpusMaxNLeakTableScoreboard,
    leaks_from_hits,
    representative_hits,
)
from tests.test_mamari_gk_islands_zero_on_b_scoreboard import (
    TestMamariGkIslandsZeroOnBScoreboard,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import load_b_sides
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    GRAM_12,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

SIDE_BR = "Br"
SIDE_BV = "Bv"
GRAM8_B = INVENTORY_LONGEST_TOKENS["B"]
STANDING_B_HITS = 2
STANDING_G_HITS = 0
STANDING_K_HITS = 0
STANDING_BR_HITS = 0
STANDING_BV_HITS = 2
STANDING_B_SITES = (
    (SIDE_BV, "Bv5", 18),
    (SIDE_BV, "Bv6", 39),
)
STANDING_BR_SITES = ()
STANDING_G_SITES = ()
STANDING_K_SITES = ()
STANDING_HITS_BY_TABLET = (
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
STANDING_LEAK_COUNTS = {}
STANDING_LEAK_HITS = 0
STANDING_OWN_HITS = 2
STANDING_B_MAX_N_IS_GK_DOUBLED_8GRAM = False
STANDING_LEAK_TABLE_B_HOME_ONLY = True
STANDING_CLAIM = "b_max_n_is_gk_doubled_8gram"
STANDING_RESULT = "b_max_n_gk_doubled_8gram"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def b_max_n_is_gk_doubled_8gram(
    representative: tuple[str, ...] = GRAM8_B,
    doubled: tuple[str, ...] = GRAM8,
) -> bool:
    """True iff B's cycle-99 max-n 8-gram is the cycle-106 doubled suffix."""
    return representative == doubled and len(representative) == 8


def leak_table_b_home_only(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> bool:
    """True iff B's representative is exact-0 off B. Cycle-104 restatement."""
    leaks = leaks_from_hits("B", hits, tablets)
    own = hits[tablets.index("B")]
    return own > 0 and not leaks


class TestBMaxNGkDoubled8GramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_identity_and_home_only_fail_when_sequences_or_leaks_clash(self):
        """A planted match or off-B leak fails the locked booleans."""
        provider = MockProvider()
        self.assertEqual(GRAM8_B, INVENTORY_LONGEST_TOKENS["B"])
        self.assertEqual(
            GRAM8_B,
            ("002", "065", "042", "300", "385", "003", "065", "200"),
        )
        self.assertEqual(
            GRAM8,
            ("260", "001", "004", "711", "260", "001", "004", "711"),
        )
        self.assertNotEqual(GRAM8_B, GRAM8)
        self.assertFalse(b_max_n_is_gk_doubled_8gram(GRAM8_B, GRAM8))
        self.assertTrue(b_max_n_is_gk_doubled_8gram(GRAM8, GRAM8))
        planted = [list(GRAM8_B)]
        self.assertEqual(ngram_hit_count(planted, GRAM8_B), 1)
        gapped = [list(GRAM8_B[:4]) + ["999"] + list(GRAM8_B[4:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM8_B), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM8_B), 0)
        home_only = (0, 2) + (0,) * 20
        leaked = (0, 2, 0, 0, 0, 0, 1) + (0,) * 15
        self.assertTrue(leak_table_b_home_only(home_only))
        self.assertFalse(leak_table_b_home_only(leaked))
        self.assertEqual(STANDING_CLAIM, "b_max_n_is_gk_doubled_8gram")
        self.assertFalse(STANDING_B_MAX_N_IS_GK_DOUBLED_8GRAM)
        self.assertTrue(STANDING_LEAK_TABLE_B_HOME_ONLY)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariBMaxNGkDoubled8GramScoreboard(unittest.TestCase):
    """Cited-fixture B max-n vs the doubled 8-gram. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.b_sides = load_b_sides()
        self.hits_by_tablet = representative_hits(GRAM8_B, self.by_tablet)
        self.b_sites = named_side_hits(
            self.b_sides[SIDE_BR], BR_LINE_NAMES, SIDE_BR, GRAM8_B
        ) + named_side_hits(self.b_sides[SIDE_BV], BV_LINE_NAMES, SIDE_BV, GRAM8_B)
        self.g_hits = self.hits_by_tablet[VENDORED_TABLETS.index("G")]
        self.k_hits = self.hits_by_tablet[VENDORED_TABLETS.index("K")]
        self.b_hits = self.hits_by_tablet[VENDORED_TABLETS.index("B")]
        self.leaks = leaks_from_hits("B", self.hits_by_tablet)
        self.claim_holds = b_max_n_is_gk_doubled_8gram(GRAM8_B, GRAM8)
        self.home_only = leak_table_b_home_only(self.hits_by_tablet)

    def test_tokens_are_cycle_99_b_representative_not_invented(self):
        """8-gram is the inventory / leak-table B row. None invented."""
        self.assertEqual(GRAM8_B, INVENTORY_LONGEST_TOKENS["B"])
        self.assertEqual(INVENTORY_LONGEST_N["B"], 8)
        self.assertEqual(len(GRAM8_B), 8)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["B"]["longest_tokens"]),
            GRAM8_B,
        )
        self.assertEqual(
            tuple(self.survey["corpus_max_n_leak_table"]["rows"]["B"]["longest_tokens"]),
            GRAM8_B,
        )
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertEqual(GRAM8, GRAM_12[4:])
        self.assertEqual(tuple(self.survey["b_gk_doubled_8gram"]["tokens8"]), GRAM8)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_b_max_n_is_not_the_gk_doubled_8gram(self):
        """Sequences differ. Claim that can lose is false."""
        self.assertNotEqual(GRAM8_B, GRAM8)
        self.assertFalse(b_max_n_is_gk_doubled_8gram(GRAM8_B, GRAM8))
        self.assertEqual(self.claim_holds, STANDING_B_MAX_N_IS_GK_DOUBLED_8GRAM)
        self.assertFalse(STANDING_B_MAX_N_IS_GK_DOUBLED_8GRAM)
        self.assertEqual(STANDING_CLAIM, "b_max_n_is_gk_doubled_8gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_representative_hits_on_every_vendored_tablet(self):
        """B=2 at Bv5[18]/Bv6[39]; else 0 on A–V. G=0 and K=0."""
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.b_hits, STANDING_B_HITS)
        self.assertEqual(self.g_hits, STANDING_G_HITS)
        self.assertEqual(self.k_hits, STANDING_K_HITS)
        self.assertEqual(STANDING_B_HITS, 2)
        self.assertEqual(STANDING_G_HITS, 0)
        self.assertEqual(STANDING_K_HITS, 0)
        for letter, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], GRAM8_B))
            if letter != "B":
                self.assertEqual(count, 0)
        self.assertEqual(
            tablet_hit_counts(self.by_tablet, GRAM8_B, VENDORED_TABLETS),
            STANDING_HITS_BY_TABLET,
        )
        self.assertEqual(self.leaks, STANDING_LEAK_COUNTS)
        self.assertEqual(sum(self.leaks.values()), STANDING_LEAK_HITS)
        self.assertEqual(STANDING_LEAK_HITS, 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_b_sites_and_leak_table_b_home_only_holds(self):
        """Cycle-45 Bv sites; cycle-104 B-home-only row is not lost."""
        self.assertEqual(
            tuple(site_tuple(hit) for hit in self.b_sites),
            STANDING_B_SITES,
        )
        self.assertEqual(len(self.b_sites), STANDING_B_HITS)
        self.assertEqual(STANDING_BR_SITES, ())
        self.assertEqual(STANDING_G_SITES, ())
        self.assertEqual(STANDING_K_SITES, ())
        self.assertEqual(ngram_hit_count(self.b_sides[SIDE_BR], GRAM8_B), STANDING_BR_HITS)
        self.assertEqual(ngram_hit_count(self.b_sides[SIDE_BV], GRAM8_B), STANDING_BV_HITS)
        for side, line, index in STANDING_B_SITES:
            names = BR_LINE_NAMES if side == SIDE_BR else BV_LINE_NAMES
            stems = self.b_sides[side][names.index(line)][index : index + 8]
            self.assertEqual(tuple(stems), GRAM8_B)
        self.assertTrue(self.home_only)
        self.assertEqual(self.home_only, STANDING_LEAK_TABLE_B_HOME_ONLY)
        self.assertTrue(STANDING_LEAK_TABLE_B_HOME_ONLY)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["rows"]["B"]["leak_hits"], 0)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["rows"]["B"]["leak_counts"], {})
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["rows"]["B"]["tablet_only"])
        self.assertIn("B", self.survey["corpus_max_n_leak_table"]["zero_off_home"])
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_inventory_leak_suffix_and_w_scoreboards_still_compute(self):
        """Cycles 99, 104, 106, 113, and W stay."""
        prior_inv = TestMamariCorpusMaxNLeakTableScoreboard()
        prior_inv.setUp()
        prior_inv.test_representatives_are_cycle_99_tokens()
        prior_inv.test_survey_matches_computed_lock()
        prior_106 = TestMamariBGkDoubled8GramScoreboard()
        prior_106.setUp()
        prior_106.test_8gram_hits_on_every_vendored_tablet()
        prior_106.test_survey_matches_computed_lock()
        prior_113 = TestMamariGkIslandsZeroOnBScoreboard()
        prior_113.setUp()
        prior_113.test_six_of_six_are_exact_zero_on_b()
        prior_113.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-114 identity and leak row."""
        lock = self.survey["b_max_n_gk_doubled_8gram"]
        self.assertEqual(lock["cycle"], 114)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens8"]), GRAM8_B)
        self.assertEqual(lock["n8"], 8)
        self.assertEqual(tuple(lock["doubled_tokens8"]), GRAM8)
        self.assertEqual(tuple(lock["island12_tokens"]), GRAM_12)
        self.assertEqual(lock["from_cycle"], 99)
        self.assertEqual(lock["b_hits"], STANDING_B_HITS)
        self.assertEqual(lock["g_hits"], STANDING_G_HITS)
        self.assertEqual(lock["k_hits"], STANDING_K_HITS)
        self.assertEqual(tuple(tuple(row) for row in lock["b_sites"]), STANDING_B_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["g_sites"]), STANDING_G_SITES)
        self.assertEqual(tuple(tuple(row) for row in lock["k_sites"]), STANDING_K_SITES)
        self.assertEqual(lock["br_hits"], STANDING_BR_HITS)
        self.assertEqual(lock["bv_hits"], STANDING_BV_HITS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["own_hits"], STANDING_OWN_HITS)
        self.assertEqual(lock["leak_hits"], STANDING_LEAK_HITS)
        self.assertEqual(lock["leak_counts"], STANDING_LEAK_COUNTS)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["b_max_n_is_gk_doubled_8gram"])
        self.assertEqual(
            lock["b_max_n_is_gk_doubled_8gram"],
            STANDING_B_MAX_N_IS_GK_DOUBLED_8GRAM,
        )
        self.assertTrue(lock["leak_table_b_home_only"])
        self.assertEqual(
            lock["leak_table_b_home_only"],
            STANDING_LEAK_TABLE_B_HOME_ONLY,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_b_gk_doubled_8gram_unchanged"])
        self.assertTrue(lock["standing_gk_islands_zero_on_b_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["B"]["longest_tokens"]),
            GRAM8_B,
        )
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["b_gk_doubled_8gram"]["cycle"], 106)
        self.assertTrue(self.survey["b_gk_doubled_8gram"]["b_has_gk_doubled_8gram"])
        self.assertEqual(tuple(self.survey["b_gk_doubled_8gram"]["tokens8"]), GRAM8)
        self.assertEqual(self.survey["gk_islands_zero_on_b"]["cycle"], 113)
        self.assertEqual(self.survey["gk_islands_zero_on_b"]["gk_islands_zero_on_b"], 6)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariBMaxNGkDoubled8GramImageSnapshot(unittest.TestCase):
    """Cycle 114 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
