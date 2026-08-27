"""G–K 17-gram hits per existing fixture.

Cycle 62 / focused-batch 1 of 5. Uses only the already-vendored
fixtures: Ca calendar, Ca remainder, Cb, Aa, Ab, Br, Bv, Ia, Gr,
Gv, Kr, Kv. No new tablet. Exact 17-gram from cycle 61. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents.

Twelve-row count table: consecutive hits of
380 001 003 005 006 010 380 001 003 315 380 001 003 090 001 380 001
per fixture. Stem ids only — not meanings. 076 is not in the gram.
Image stays parked Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_santiago_ia_076_rate_scoreboard import (
    PASSAGE_AA,
    PASSAGE_IA,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_london_kr_scoreboard import (
    extract_kr_published_tokens,
    kr_line_stems,
    load_vendored_kr_html,
)
from tests.test_mamari_small_london_kv_scoreboard import (
    extract_kv_published_tokens,
    kv_line_stems,
    load_vendored_kv_html,
)
from tests.test_mamari_small_santiago_gv_430_076_200_ngram_scoreboard import (
    PASSAGE_GR,
    PASSAGE_GV,
    PASSAGE_ORDER as TEN_PASSAGE_ORDER,
    existing_430_076_200_lines,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    STANDING_COMBINED_FREQ_G,
    STANDING_COMBINED_FREQ_K,
    STANDING_COMBINED_N,
    STANDING_COMBINED_TOKENS,
    STANDING_STEM_076_IN_LONGEST,
    TestMamariSmallSantiagoLondonParallelNgramScoreboard,
)

PASSAGE_KR = "tablet_k_small_london_recto"
PASSAGE_KV = "tablet_k_small_london_verso"
PASSAGE_ORDER = TEN_PASSAGE_ORDER + (PASSAGE_KR, PASSAGE_KV)
GRAM_17 = STANDING_COMBINED_TOKENS
STANDING_ROW_COUNT = 12
STANDING_HITS = (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0)
STANDING_TABLE = tuple(zip(PASSAGE_ORDER, STANDING_HITS))
STANDING_ONLY_GR_AND_KR_HAVE_HITS = True
STANDING_NEW_TABLET = False


@dataclass(frozen=True)
class FixtureHitRow:
    """One fixture's exact 17-gram hit count. Ids only."""

    passage: str
    hits: int


def existing_gk_17gram_lines() -> dict[str, list[list[str]]]:
    """Load the twelve already-vendored fixtures. No new scrape."""
    lines = existing_430_076_200_lines()
    lines[PASSAGE_KR] = kr_line_stems(extract_kr_published_tokens(load_vendored_kr_html()))
    lines[PASSAGE_KV] = kv_line_stems(extract_kv_published_tokens(load_vendored_kv_html()))
    return lines


def score_gk_17gram_hits(
    by_passage: dict[str, list[list[str]]],
    gram: tuple[str, ...] = GRAM_17,
) -> tuple[FixtureHitRow, ...]:
    """Twelve-row hit counts for the locked 17-gram. Search only."""
    return tuple(
        FixtureHitRow(passage, ngram_hit_count(by_passage[passage], gram))
        for passage in PASSAGE_ORDER
    )


def table_tuples(
    table: tuple[FixtureHitRow, ...],
) -> tuple[tuple[str, int], ...]:
    """Stable lock: (passage, hit count)."""
    return tuple((row.passage, row.hits) for row in table)


def only_gr_and_kr_have_hits(row_hits: tuple[int, ...]) -> bool:
    """True iff Gr and Kr are the only fixtures with a nonzero count."""
    gr_i = PASSAGE_ORDER.index(PASSAGE_GR)
    kr_i = PASSAGE_ORDER.index(PASSAGE_KR)
    return (
        row_hits[gr_i] > 0
        and row_hits[kr_i] > 0
        and all(count == 0 for i, count in enumerate(row_hits) if i not in (gr_i, kr_i))
    )


class TestSmallSantiagoLondon17gramHitHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 17-gram counts; a gap is not a hit."""
        provider = MockProvider()
        gram = GRAM_17
        adjacent = [list(gram) + list(gram[:3])]
        self.assertEqual(ngram_hit_count(adjacent, gram), 1)
        gapped = [list(gram[:8]) + ["999"] + list(gram[8:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        empty = [[]]
        self.assertEqual(ngram_hit_count(empty, gram), 0)
        self.assertEqual(len(gram), STANDING_COMBINED_N)
        self.assertEqual("076" in gram, STANDING_STEM_076_IN_LONGEST)
        self.assertEqual(provider.get_call_history(), [])

    def test_table_follows_passage_order(self):
        """Scorer walks PASSAGE_ORDER; missing key is an error."""
        provider = MockProvider()
        by_passage = {passage: [[]] for passage in PASSAGE_ORDER}
        by_passage[PASSAGE_AA] = [list(GRAM_17), list(GRAM_17)]
        table = score_gk_17gram_hits(by_passage)
        self.assertEqual(tuple(row.passage for row in table), PASSAGE_ORDER)
        self.assertEqual(len(table), STANDING_ROW_COUNT)
        self.assertEqual(table[3].hits, 2)
        self.assertEqual(table[8].hits, 0)
        self.assertFalse(only_gr_and_kr_have_hits(tuple(row.hits for row in table)))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondon17gramHitScoreboard(unittest.TestCase):
    """Cited-fixture G–K 17-gram 12-row hit lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_passage = existing_gk_17gram_lines()
        self.table = score_gk_17gram_hits(self.by_passage)
        self.locked = table_tuples(self.table)

    def test_twelve_row_hit_table(self):
        """Hits per fixture for the cycle-61 G vs K 17-gram."""
        self.assertEqual(self.locked, STANDING_TABLE)
        self.assertEqual(len(self.table), STANDING_ROW_COUNT)
        self.assertEqual(len(self.table), len(PASSAGE_ORDER))
        self.assertEqual(tuple(row.passage for row in self.table), PASSAGE_ORDER)
        self.assertEqual(tuple(row.hits for row in self.table), STANDING_HITS)
        self.assertEqual(len(GRAM_17), STANDING_COMBINED_N)
        self.assertEqual("076" in GRAM_17, STANDING_STEM_076_IN_LONGEST)
        self.assertFalse(STANDING_STEM_076_IN_LONGEST)
        for row, (passage, hits) in zip(self.table, STANDING_TABLE):
            self.assertEqual(row.passage, passage)
            self.assertEqual(row.hits, hits)
            self.assertEqual(
                row.hits,
                ngram_hit_count(self.by_passage[passage], GRAM_17),
            )
        by_passage = {row.passage: row.hits for row in self.table}
        self.assertEqual(PASSAGE_ORDER[-4], PASSAGE_GR)
        self.assertEqual(PASSAGE_ORDER[-3], PASSAGE_GV)
        self.assertEqual(PASSAGE_ORDER[-2], PASSAGE_KR)
        self.assertEqual(PASSAGE_ORDER[-1], PASSAGE_KV)
        self.assertEqual(by_passage[PASSAGE_GR], STANDING_COMBINED_FREQ_G)
        self.assertEqual(by_passage[PASSAGE_KR], STANDING_COMBINED_FREQ_K)
        self.assertEqual(by_passage[PASSAGE_GV], 0)
        self.assertEqual(by_passage[PASSAGE_KV], 0)
        self.assertEqual(by_passage[PASSAGE_IA], 0)
        self.assertEqual(
            only_gr_and_kr_have_hits(STANDING_HITS),
            STANDING_ONLY_GR_AND_KR_HAVE_HITS,
        )
        self.assertTrue(STANDING_ONLY_GR_AND_KR_HAVE_HITS)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_parallel_scoreboard_still_computes(self):
        """Cycle 61 G vs K longest-shared n-gram lock stays."""
        prior = TestMamariSmallSantiagoLondonParallelNgramScoreboard()
        prior.setUp()
        prior.test_combined_longest_shared_ngram_and_claim()
        prior.test_per_side_longest_shared_ngrams()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-62 12-row 17-gram table."""
        lock = self.survey["tablet_g_k_17gram_hits_per_fixture"]
        self.assertEqual(lock["cycle"], 62)
        self.assertEqual(lock["focused_batch"], 1)
        self.assertEqual(lock["focused_batch_of"], 5)
        self.assertEqual(tuple(lock["tokens"]), GRAM_17)
        self.assertEqual(lock["n"], STANDING_COMBINED_N)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        self.assertEqual(tuple(lock["hits"]), STANDING_HITS)
        locked = tuple((passage, hits) for passage, hits in lock["table"])
        self.assertEqual(locked, STANDING_TABLE)
        self.assertEqual(
            lock["only_gr_and_kr_have_hits"],
            STANDING_ONLY_GR_AND_KR_HAVE_HITS,
        )
        self.assertFalse(lock["stem_076_in_gram"])
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
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_parallel_shared_ngram"]["cycle"], 61)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondon17gramHitImageSnapshot(unittest.TestCase):
    """Cycle 62 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
