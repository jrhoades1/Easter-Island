"""G–K maximal-island hits on existing non-G/K fixtures.

Cycle 68 text-search lock. Uses only the already-vendored non-G/K
fixtures: Ca calendar, Ca remainder, Cb, Aa, Ab, Br, Bv, Ia. Does
not scrape a new tablet. The six sequences are the cycle-67
disjoint maximal G–K shared islands. Raw stems. No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.
No CV. No new agents. Not a meaning dictionary.

Six-by-eight count table: consecutive hits of each island per
fixture. Also whether any island hits anywhere off G/K. Stem ids
only — not meanings. Image stays parked Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_santiago_ia_076_rate_scoreboard import (
    PASSAGE_AA,
    PASSAGE_ORDER,
    STANDING_ROW_COUNT,
    existing_076_rate_lines,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_gv_430_076_200_ngram_scoreboard import (
    PASSAGE_GR,
    PASSAGE_GV,
)
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import (
    PASSAGE_KR,
    PASSAGE_KV,
)
from tests.test_mamari_small_santiago_london_shared_n8_scoreboard import (
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    STANDING_NEW_TABLET,
    STANDING_STEM_076_IN_LONGEST,
    TestMamariSmallSantiagoLondonSharedN8Scoreboard,
)

LOCKED_ISLANDS = tuple(tokens for tokens, _n, _fg, _fk, _gs, _ks in STANDING_MAXIMALS)
STANDING_GRAM_COUNT = STANDING_MAXIMAL_COUNT
STANDING_ZERO_ROW = (0,) * STANDING_ROW_COUNT
STANDING_HITS = (STANDING_ZERO_ROW,) * STANDING_GRAM_COUNT
STANDING_TABLE = tuple(zip(LOCKED_ISLANDS, STANDING_HITS))
STANDING_ANY_OFF_GK = False
GK_PASSAGES = (PASSAGE_GR, PASSAGE_GV, PASSAGE_KR, PASSAGE_KV)


@dataclass(frozen=True)
class IslandFixtureRow:
    """One island's hits across the eight non-G/K fixtures. Ids only."""

    tokens: tuple[str, ...]
    hits: tuple[int, ...]


def score_island_row(
    by_passage: dict[str, list[list[str]]],
    gram: tuple[str, ...],
) -> IslandFixtureRow:
    """Eight-row hit counts for one island in locked passage order."""
    return IslandFixtureRow(
        tokens=gram,
        hits=tuple(ngram_hit_count(by_passage[passage], gram) for passage in PASSAGE_ORDER),
    )


def score_island_table(
    by_passage: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...] = LOCKED_ISLANDS,
) -> tuple[IslandFixtureRow, ...]:
    """6×8 lock: one eight-count row per maximal island. Search only."""
    return tuple(score_island_row(by_passage, gram) for gram in grams)


def table_tuples(
    table: tuple[IslandFixtureRow, ...],
) -> tuple[tuple[tuple[str, ...], tuple[int, ...]], ...]:
    """Stable lock: (tokens, eight hit counts)."""
    return tuple((row.tokens, row.hits) for row in table)


def any_island_hits_off_gk(table: tuple[IslandFixtureRow, ...]) -> bool:
    """True iff any island has a nonzero count on a non-G/K fixture."""
    return any(any(row.hits) for row in table)


class TestSmallSantiagoLondonIslandOffGkHelpers(unittest.TestCase):
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
        self.assertEqual(len(LOCKED_ISLANDS), STANDING_GRAM_COUNT)
        self.assertEqual("076" in gram, STANDING_STEM_076_IN_LONGEST)
        self.assertEqual(provider.get_call_history(), [])

    def test_table_follows_islands_and_passage_order(self):
        """Scorer walks LOCKED_ISLANDS × PASSAGE_ORDER; missing key is an error."""
        provider = MockProvider()
        by_passage = {passage: [[]] for passage in PASSAGE_ORDER}
        planted = LOCKED_ISLANDS[2]
        by_passage[PASSAGE_AA] = [list(planted), list(planted)]
        table = score_island_table(by_passage)
        self.assertEqual(tuple(row.tokens for row in table), LOCKED_ISLANDS)
        self.assertEqual(len(table), STANDING_GRAM_COUNT)
        self.assertEqual(len(table[0].hits), STANDING_ROW_COUNT)
        self.assertEqual(table[2].hits[3], 2)
        self.assertEqual(table[0].hits[3], 0)
        self.assertTrue(any_island_hits_off_gk(table))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonIslandOffGkScoreboard(unittest.TestCase):
    """Cited-fixture 6×8 off-G/K island hit lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_passage = existing_076_rate_lines()
        self.table = score_island_table(self.by_passage)
        self.locked = table_tuples(self.table)

    def test_six_by_eight_hit_table(self):
        """Hits per non-G/K fixture for each cycle-67 maximal island."""
        self.assertEqual(self.locked, STANDING_TABLE)
        self.assertEqual(len(self.table), STANDING_GRAM_COUNT)
        self.assertEqual(len(self.table), STANDING_MAXIMAL_COUNT)
        self.assertEqual(tuple(row.tokens for row in self.table), LOCKED_ISLANDS)
        self.assertEqual(tuple(row.hits for row in self.table), STANDING_HITS)
        self.assertEqual(len(PASSAGE_ORDER), STANDING_ROW_COUNT)
        for passage in GK_PASSAGES:
            self.assertNotIn(passage, PASSAGE_ORDER)
            self.assertNotIn(passage, self.by_passage)
        for row, (gram, hits) in zip(self.table, STANDING_TABLE):
            self.assertEqual(row.tokens, gram)
            self.assertEqual(row.hits, hits)
            self.assertEqual(row.hits, STANDING_ZERO_ROW)
            self.assertEqual(len(row.hits), STANDING_ROW_COUNT)
            self.assertEqual("076" in row.tokens, STANDING_STEM_076_IN_LONGEST)
            for passage, count in zip(PASSAGE_ORDER, row.hits):
                self.assertEqual(
                    count,
                    ngram_hit_count(self.by_passage[passage], gram),
                )
        self.assertEqual(any_island_hits_off_gk(self.table), STANDING_ANY_OFF_GK)
        self.assertFalse(STANDING_ANY_OFF_GK)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_STEM_076_IN_LONGEST)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_shared_n8_scoreboard_still_computes(self):
        """Cycle 67 G–K n≥8 inventory lock stays."""
        prior = TestMamariSmallSantiagoLondonSharedN8Scoreboard()
        prior.setUp()
        prior.test_inventory_tokens_n_freq_and_hits()
        prior.test_coverage_and_same_text_claim()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-68 6×8 off-G/K table."""
        lock = self.survey["tablet_g_k_island_off_gk_hits"]
        self.assertEqual(lock["cycle"], 68)
        self.assertEqual(lock["result"], "gk_island_off_gk_hits")
        self.assertEqual(tuple(tuple(tokens) for tokens in lock["islands"]), LOCKED_ISLANDS)
        self.assertEqual(lock["gram_count"], STANDING_GRAM_COUNT)
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        self.assertEqual(tuple(tuple(hits) for hits in lock["hits"]), STANDING_HITS)
        locked = tuple(
            (tuple(tokens), tuple(hits)) for tokens, hits in lock["table"]
        )
        self.assertEqual(locked, STANDING_TABLE)
        self.assertEqual(lock["any_off_gk"], STANDING_ANY_OFF_GK)
        self.assertFalse(lock["any_off_gk"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["stem_076_in_islands"])
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
        self.assertTrue(lock["standing_gk_parallel_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_hits_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_sites_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_hamming_unchanged"])
        self.assertTrue(lock["standing_gk_380_001_003_unchanged"])
        self.assertTrue(lock["standing_gk_gr_kv_15gram_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_shared_n8_inventory"]["cycle"], 67)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonIslandOffGkImageSnapshot(unittest.TestCase):
    """Cycle 68 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
