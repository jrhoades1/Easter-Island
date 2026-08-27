"""H∩P∩Q maximal-island hits on existing non-H/P/Q fixtures.

Cycle 72 text-search lock. Uses only the already-vendored
non-H/P/Q fixtures: Ca calendar, Ca remainder, Cb, Aa, Ab, Br,
Bv, Ia, Gr, Gv, Kr, Kv. Does not scrape a new tablet. The five
sequences are the cycle-71 disjoint maximal H∩P∩Q islands. Raw
stems. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents. Not a meaning
dictionary.

Five-by-twelve count table: consecutive hits of each island per
fixture. Also whether any island hits anywhere off H/P/Q. Stem
ids only — not meanings. Image stays parked Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_hpq_triple_n8_scoreboard import (
    HPQ_SIDES,
    STANDING_MAXIMAL_COUNT,
    STANDING_MAXIMALS,
    STANDING_NEW_TABLET,
    STANDING_TABLET_D_SCRAPED,
    TestMamariHpqTripleN8Scoreboard,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import (
    PASSAGE_AA,
    PASSAGE_ORDER,
    STANDING_ROW_COUNT,
    existing_gk_17gram_lines,
)

LOCKED_ISLANDS = tuple(tokens for tokens, _n, _fh, _fp, _fq, _h, _p, _q in STANDING_MAXIMALS)
STANDING_GRAM_COUNT = STANDING_MAXIMAL_COUNT
STANDING_ZERO_ROW = (0,) * STANDING_ROW_COUNT
STANDING_HITS = (STANDING_ZERO_ROW,) * STANDING_GRAM_COUNT
STANDING_TABLE = tuple(zip(LOCKED_ISLANDS, STANDING_HITS))
STANDING_ANY_OFF_HPQ = False
STANDING_STEM_076_IN_ISLANDS = False


@dataclass(frozen=True)
class IslandFixtureRow:
    """One island's hits across the twelve non-H/P/Q fixtures. Ids only."""

    tokens: tuple[str, ...]
    hits: tuple[int, ...]


def score_island_row(
    by_passage: dict[str, list[list[str]]],
    gram: tuple[str, ...],
) -> IslandFixtureRow:
    """Twelve-row hit counts for one island in locked passage order."""
    return IslandFixtureRow(
        tokens=gram,
        hits=tuple(ngram_hit_count(by_passage[passage], gram) for passage in PASSAGE_ORDER),
    )


def score_island_table(
    by_passage: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...] = LOCKED_ISLANDS,
) -> tuple[IslandFixtureRow, ...]:
    """5×12 lock: one twelve-count row per maximal island. Search only."""
    return tuple(score_island_row(by_passage, gram) for gram in grams)


def table_tuples(
    table: tuple[IslandFixtureRow, ...],
) -> tuple[tuple[tuple[str, ...], tuple[int, ...]], ...]:
    """Stable lock: (tokens, twelve hit counts)."""
    return tuple((row.tokens, row.hits) for row in table)


def any_island_hits_off_hpq(table: tuple[IslandFixtureRow, ...]) -> bool:
    """True iff any island has a nonzero count on a non-H/P/Q fixture."""
    return any(any(row.hits) for row in table)


class TestHpqIslandOffHpqHelpers(unittest.TestCase):
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
        self.assertEqual("076" in gram, STANDING_STEM_076_IN_ISLANDS)
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
        self.assertTrue(any_island_hits_off_hpq(table))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariHpqIslandOffHpqScoreboard(unittest.TestCase):
    """Cited-fixture 5×12 off-H/P/Q island hit lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_passage = existing_gk_17gram_lines()
        self.table = score_island_table(self.by_passage)
        self.locked = table_tuples(self.table)

    def test_five_by_twelve_hit_table(self):
        """Hits per non-H/P/Q fixture for each cycle-71 maximal island."""
        self.assertEqual(self.locked, STANDING_TABLE)
        self.assertEqual(len(self.table), STANDING_GRAM_COUNT)
        self.assertEqual(len(self.table), STANDING_MAXIMAL_COUNT)
        self.assertEqual(tuple(row.tokens for row in self.table), LOCKED_ISLANDS)
        self.assertEqual(tuple(row.hits for row in self.table), STANDING_HITS)
        self.assertEqual(len(PASSAGE_ORDER), STANDING_ROW_COUNT)
        for side in HPQ_SIDES:
            self.assertNotIn(side, PASSAGE_ORDER)
            self.assertNotIn(side, self.by_passage)
        for row, (gram, hits) in zip(self.table, STANDING_TABLE):
            self.assertEqual(row.tokens, gram)
            self.assertEqual(row.hits, hits)
            self.assertEqual(row.hits, STANDING_ZERO_ROW)
            self.assertEqual(len(row.hits), STANDING_ROW_COUNT)
            self.assertFalse("076" in row.tokens)
            for passage, count in zip(PASSAGE_ORDER, row.hits):
                self.assertEqual(
                    count,
                    ngram_hit_count(self.by_passage[passage], gram),
                )
        self.assertEqual(any_island_hits_off_hpq(self.table), STANDING_ANY_OFF_HPQ)
        self.assertFalse(STANDING_ANY_OFF_HPQ)
        self.assertFalse(STANDING_STEM_076_IN_ISLANDS)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_TABLET_D_SCRAPED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_hpq_triple_n8_scoreboard_still_computes(self):
        """Cycle 71 H∩P∩Q n≥8 inventory lock stays."""
        prior = TestMamariHpqTripleN8Scoreboard()
        prior.setUp()
        prior.test_inventory_tokens_n_freq_and_hits()
        prior.test_per_side_inventory_and_cross_empty()
        prior.test_coverage_and_tradition_claim()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-72 5×12 off-H/P/Q table."""
        lock = self.survey["tablet_h_p_q_island_off_hpq_hits"]
        self.assertEqual(lock["cycle"], 72)
        self.assertEqual(lock["result"], "hpq_island_off_hpq_hits")
        self.assertEqual(tuple(tuple(tokens) for tokens in lock["islands"]), LOCKED_ISLANDS)
        self.assertEqual(lock["gram_count"], STANDING_GRAM_COUNT)
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        self.assertEqual(tuple(tuple(hits) for hits in lock["hits"]), STANDING_HITS)
        locked = tuple(
            (tuple(tokens), tuple(hits)) for tokens, hits in lock["table"]
        )
        self.assertEqual(locked, STANDING_TABLE)
        self.assertEqual(lock["any_off_hpq"], STANDING_ANY_OFF_HPQ)
        self.assertFalse(lock["any_off_hpq"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["tablet_d_scraped"])
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
        self.assertTrue(lock["standing_hp_shared_n8_unchanged"])
        self.assertTrue(lock["standing_q_shared_n8_unchanged"])
        self.assertTrue(lock["standing_hpq_triple_n8_unchanged"])
        self.assertTrue(lock["standing_gk_shared_n8_unchanged"])
        self.assertTrue(lock["standing_gk_island_off_gk_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_h_p_q_triple_n8_inventory"]["cycle"], 71)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariHpqIslandOffHpqImageSnapshot(unittest.TestCase):
    """Cycle 72 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
