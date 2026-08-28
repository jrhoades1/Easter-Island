"""G–K maximal-island hits on existing H/P/Q fixtures.

Cycle 77 text-search lock. Uses only the already-vendored
H/P/Q fixtures: Hr, Hv, Pr, Pv, Qr, Qv. Does not scrape a new
tablet. The six sequences are the cycle-67/74 Gr-order G–K
islands. Also the cycle-76 n=25 (gap 10-gram + island 6). Raw
stems. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents. Not a meaning
dictionary.

Seven-by-six count table: consecutive hits of each sequence per
H/P/Q side. Also any_hit / all_zero. Stem ids only — not
meanings. Image stays parked Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_hpq_triple_n8_scoreboard import HPQ_SIDES
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_grkv_block_scoreboard import (
    STANDING_COMBINED_SHARED_TOKENS,
    TestMamariSmallSantiagoLondonGrkvBlockScoreboard,
)
from tests.test_mamari_small_santiago_london_island_order_scoreboard import (
    STANDING_GR_TOKEN_ORDER,
    STANDING_TABLET_D_SCRAPED,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    G_SIDES,
    K_SIDES,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    STANDING_MAXIMAL_COUNT,
    STANDING_NEW_TABLET,
)
from tests.test_mamari_small_st_petersburg_shared_n8_scoreboard import (
    load_q_h_p_sides,
)

LOCKED_ISLANDS = STANDING_GR_TOKEN_ORDER
LOCKED_COMBINED_N25 = STANDING_COMBINED_SHARED_TOKENS
LOCKED_GRAMS = LOCKED_ISLANDS + (LOCKED_COMBINED_N25,)
SIDE_ORDER = HPQ_SIDES
STANDING_ISLAND_COUNT = STANDING_MAXIMAL_COUNT
STANDING_GRAM_COUNT = 7
STANDING_ROW_COUNT = 6
STANDING_ZERO_ROW = (0,) * STANDING_ROW_COUNT
STANDING_HITS = (STANDING_ZERO_ROW,) * STANDING_GRAM_COUNT
STANDING_TABLE = tuple(zip(LOCKED_GRAMS, STANDING_HITS))
STANDING_ANY_HIT = False
STANDING_ALL_ZERO = True
STANDING_STEM_076_IN_GRAMS = False
STANDING_RESULT = "gk_island_off_hpq_hits"


@dataclass(frozen=True)
class IslandFixtureRow:
    """One sequence's hits across the six H/P/Q sides. Ids only."""

    tokens: tuple[str, ...]
    hits: tuple[int, ...]


def score_island_row(
    by_side: dict[str, list[list[str]]],
    gram: tuple[str, ...],
) -> IslandFixtureRow:
    """Six-row hit counts for one sequence in locked side order."""
    return IslandFixtureRow(
        tokens=gram,
        hits=tuple(ngram_hit_count(by_side[side], gram) for side in SIDE_ORDER),
    )


def score_island_table(
    by_side: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...] = LOCKED_GRAMS,
) -> tuple[IslandFixtureRow, ...]:
    """7×6 lock: one six-count row per island and the n=25. Search only."""
    return tuple(score_island_row(by_side, gram) for gram in grams)


def table_tuples(
    table: tuple[IslandFixtureRow, ...],
) -> tuple[tuple[tuple[str, ...], tuple[int, ...]], ...]:
    """Stable lock: (tokens, six hit counts)."""
    return tuple((row.tokens, row.hits) for row in table)


def any_hit(table: tuple[IslandFixtureRow, ...]) -> bool:
    """True iff any locked sequence has a nonzero count on H/P/Q."""
    return any(any(row.hits) for row in table)


def all_zero(table: tuple[IslandFixtureRow, ...]) -> bool:
    """True iff every locked sequence is 0 on every H/P/Q side."""
    return not any_hit(table)


class TestGkIslandsOffHpqHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent island counts; a gap is not a hit."""
        provider = MockProvider()
        gram = LOCKED_ISLANDS[0]
        adjacent = [list(gram) + list(gram[:3])]
        self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        empty = [[]]
        self.assertEqual(ngram_hit_count(empty, gram), 0)
        self.assertEqual(len(LOCKED_ISLANDS), STANDING_ISLAND_COUNT)
        self.assertEqual(len(LOCKED_GRAMS), STANDING_GRAM_COUNT)
        self.assertEqual(len(LOCKED_COMBINED_N25), 25)
        self.assertEqual(LOCKED_COMBINED_N25, LOCKED_GRAMS[-1])
        self.assertFalse("076" in gram)
        self.assertEqual(provider.get_call_history(), [])

    def test_table_follows_grams_and_side_order(self):
        """Scorer walks LOCKED_GRAMS × SIDE_ORDER; missing key is an error."""
        provider = MockProvider()
        by_side = {side: [[]] for side in SIDE_ORDER}
        planted = LOCKED_ISLANDS[2]
        by_side["Hr"] = [list(planted), list(planted)]
        table = score_island_table(by_side)
        self.assertEqual(tuple(row.tokens for row in table), LOCKED_GRAMS)
        self.assertEqual(len(table), STANDING_GRAM_COUNT)
        self.assertEqual(len(table[0].hits), STANDING_ROW_COUNT)
        self.assertEqual(table[2].hits[0], 2)
        self.assertEqual(table[0].hits[0], 0)
        self.assertTrue(any_hit(table))
        self.assertFalse(all_zero(table))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariGkIslandsOffHpqScoreboard(unittest.TestCase):
    """Cited-fixture 7×6 G–K island hits on H/P/Q. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_q_h_p_sides()
        self.table = score_island_table(self.by_side)
        self.locked = table_tuples(self.table)

    def test_seven_by_six_hit_table(self):
        """Hits per H/P/Q side for each Gr-order island and the n=25."""
        self.assertEqual(self.locked, STANDING_TABLE)
        self.assertEqual(len(self.table), STANDING_GRAM_COUNT)
        self.assertEqual(len(LOCKED_ISLANDS), STANDING_ISLAND_COUNT)
        self.assertEqual(tuple(row.tokens for row in self.table), LOCKED_GRAMS)
        self.assertEqual(tuple(row.tokens for row in self.table[:6]), LOCKED_ISLANDS)
        self.assertEqual(self.table[-1].tokens, LOCKED_COMBINED_N25)
        self.assertEqual(tuple(row.hits for row in self.table), STANDING_HITS)
        self.assertEqual(len(SIDE_ORDER), STANDING_ROW_COUNT)
        self.assertEqual(SIDE_ORDER, ("Hr", "Hv", "Pr", "Pv", "Qr", "Qv"))
        for side in G_SIDES + K_SIDES:
            self.assertNotIn(side, SIDE_ORDER)
        self.assertEqual(tuple(self.by_side), SIDE_ORDER)
        for row, (gram, hits) in zip(self.table, STANDING_TABLE):
            self.assertEqual(row.tokens, gram)
            self.assertEqual(row.hits, hits)
            self.assertEqual(row.hits, STANDING_ZERO_ROW)
            self.assertEqual(len(row.hits), STANDING_ROW_COUNT)
            self.assertFalse("076" in row.tokens)
            for side, count in zip(SIDE_ORDER, row.hits):
                self.assertEqual(
                    count,
                    ngram_hit_count(self.by_side[side], gram),
                )
        self.assertEqual(any_hit(self.table), STANDING_ANY_HIT)
        self.assertEqual(all_zero(self.table), STANDING_ALL_ZERO)
        self.assertFalse(STANDING_ANY_HIT)
        self.assertTrue(STANDING_ALL_ZERO)
        self.assertNotEqual(STANDING_ANY_HIT, STANDING_ALL_ZERO)
        self.assertFalse(STANDING_STEM_076_IN_GRAMS)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_grkv_block_scoreboard_still_computes(self):
        """Cycle 76 Gr–Kv 5–6 block lock stays."""
        prior = TestMamariSmallSantiagoLondonGrkvBlockScoreboard()
        prior.setUp()
        prior.test_windows_adjacency_hamming_and_block_claim()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-77 7×6 off-H/P/Q table."""
        lock = self.survey["tablet_g_k_island_off_hpq_hits"]
        self.assertEqual(lock["cycle"], 77)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(
            tuple(tuple(tokens) for tokens in lock["islands"]),
            LOCKED_ISLANDS,
        )
        self.assertEqual(tuple(lock["combined_n25"]), LOCKED_COMBINED_N25)
        self.assertEqual(
            tuple(tuple(tokens) for tokens in lock["grams"]),
            LOCKED_GRAMS,
        )
        self.assertEqual(lock["island_count"], STANDING_ISLAND_COUNT)
        self.assertEqual(lock["gram_count"], STANDING_GRAM_COUNT)
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(tuple(lock["passages"]), SIDE_ORDER)
        self.assertEqual(tuple(tuple(hits) for hits in lock["hits"]), STANDING_HITS)
        locked = tuple(
            (tuple(tokens), tuple(hits)) for tokens, hits in lock["table"]
        )
        self.assertEqual(locked, STANDING_TABLE)
        self.assertEqual(lock["any_hit"], STANDING_ANY_HIT)
        self.assertEqual(lock["all_zero"], STANDING_ALL_ZERO)
        self.assertFalse(lock["any_hit"])
        self.assertTrue(lock["all_zero"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
        self.assertFalse(lock["stem_076_in_grams"])
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_gr_locks_unchanged"])
        self.assertTrue(lock["standing_gv_locks_unchanged"])
        self.assertTrue(lock["standing_kr_locks_unchanged"])
        self.assertTrue(lock["standing_kv_locks_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertTrue(lock["standing_gk_island_reading_order_unchanged"])
        self.assertTrue(lock["standing_gk_island_gaps_unchanged"])
        self.assertTrue(lock["standing_gk_grkv_block_unchanged"])
        self.assertTrue(lock["standing_hp_vendor_unchanged"])
        self.assertTrue(lock["standing_q_vendor_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_island_off_hpq_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_grkv_block"]["cycle"], 76)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariGkIslandsOffHpqImageSnapshot(unittest.TestCase):
    """Cycle 77 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
