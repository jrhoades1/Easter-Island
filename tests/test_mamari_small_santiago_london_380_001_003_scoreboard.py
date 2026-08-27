"""380 001 003 hits per existing fixture.

Cycle 65 / focused-batch 4 of 5. Uses only the already-vendored
fixtures: Ca calendar, Ca remainder, Cb, Aa, Ab, Br, Bv, Ia, Gr,
Gv, Kr, Kv. No new tablet. The 3-gram is the internal repeat of
the cycle-61/62/63/64 G–K 17-gram (slots 0, 6, 10). Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents.

Twelve-row count table: consecutive hits of 380 001 003 per
fixture. Also locks whether Gr and Kr are the only fixtures with
hits ≥ 3 (the 17-gram's internal repeat count). Stem ids only —
not meanings. Image stays parked Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_santiago_ia_076_rate_scoreboard import (
    PASSAGE_AA,
    PASSAGE_CB,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_gv_430_076_200_ngram_scoreboard import (
    PASSAGE_GR,
    PASSAGE_GV,
)
from tests.test_mamari_small_santiago_london_17gram_hamming_scoreboard import (
    TestMamariSmallSantiagoLondon17gramHammingScoreboard,
)
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import (
    GRAM_17,
    PASSAGE_KR,
    PASSAGE_KV,
    PASSAGE_ORDER,
    STANDING_COMBINED_N,
    STANDING_NEW_TABLET,
    STANDING_ROW_COUNT,
    STANDING_STEM_076_IN_LONGEST,
    existing_gk_17gram_lines,
)

GRAM_3 = ("380", "001", "003")
STANDING_INTERNAL_REPEAT = 3
STANDING_INTERNAL_SLOTS = (0, 6, 10)
STANDING_HITS = (0, 0, 1, 0, 0, 0, 0, 0, 30, 0, 6, 11)
STANDING_TABLE = tuple(zip(PASSAGE_ORDER, STANDING_HITS))
STANDING_GE_REPEAT = tuple(hits >= STANDING_INTERNAL_REPEAT for hits in STANDING_HITS)
STANDING_GE_REPEAT_PASSAGES = (PASSAGE_GR, PASSAGE_KR, PASSAGE_KV)
STANDING_ONLY_GR_AND_KR_GE_REPEAT = False


@dataclass(frozen=True)
class FixtureHitRow:
    """One fixture's exact 3-gram hit count. Ids only."""

    passage: str
    hits: int


def gram_slots(haystack: tuple[str, ...], needle: tuple[str, ...]) -> tuple[int, ...]:
    """Start indexes of needle inside haystack. Search only."""
    n = len(needle)
    return tuple(
        index
        for index in range(len(haystack) - n + 1)
        if haystack[index : index + n] == needle
    )


def score_380_001_003_hits(
    by_passage: dict[str, list[list[str]]],
    gram: tuple[str, ...] = GRAM_3,
) -> tuple[FixtureHitRow, ...]:
    """Twelve-row hit counts for 380 001 003. Search only."""
    return tuple(
        FixtureHitRow(passage, ngram_hit_count(by_passage[passage], gram))
        for passage in PASSAGE_ORDER
    )


def table_tuples(
    table: tuple[FixtureHitRow, ...],
) -> tuple[tuple[str, int], ...]:
    """Stable lock: (passage, hit count)."""
    return tuple((row.passage, row.hits) for row in table)


def only_gr_and_kr_ge_repeat(
    row_hits: tuple[int, ...],
    threshold: int = STANDING_INTERNAL_REPEAT,
) -> bool:
    """True iff Gr and Kr are the only fixtures with hits ≥ threshold."""
    gr_i = PASSAGE_ORDER.index(PASSAGE_GR)
    kr_i = PASSAGE_ORDER.index(PASSAGE_KR)
    return (
        row_hits[gr_i] >= threshold
        and row_hits[kr_i] >= threshold
        and all(
            count < threshold
            for index, count in enumerate(row_hits)
            if index not in (gr_i, kr_i)
        )
    )


class TestSmallSantiagoLondon380001003Helpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 380 001 003 counts; a gap is not a hit."""
        provider = MockProvider()
        gram = GRAM_3
        adjacent = [list(gram) + list(gram)]
        self.assertEqual(ngram_hit_count(adjacent, gram), 2)
        gapped = [list(gram[:2]) + ["999"] + list(gram[2:])]
        self.assertEqual(ngram_hit_count(gapped, gram), 0)
        empty = [[]]
        self.assertEqual(ngram_hit_count(empty, gram), 0)
        self.assertEqual(gram_slots(GRAM_17, gram), STANDING_INTERNAL_SLOTS)
        self.assertEqual(len(gram_slots(GRAM_17, gram)), STANDING_INTERNAL_REPEAT)
        self.assertEqual("076" in gram, STANDING_STEM_076_IN_LONGEST)
        self.assertEqual(provider.get_call_history(), [])

    def test_table_follows_passage_order(self):
        """Scorer walks PASSAGE_ORDER; missing key is an error."""
        provider = MockProvider()
        by_passage = {passage: [[]] for passage in PASSAGE_ORDER}
        by_passage[PASSAGE_AA] = [list(GRAM_3), list(GRAM_3), list(GRAM_3)]
        table = score_380_001_003_hits(by_passage)
        self.assertEqual(tuple(row.passage for row in table), PASSAGE_ORDER)
        self.assertEqual(len(table), STANDING_ROW_COUNT)
        self.assertEqual(table[3].hits, 3)
        self.assertEqual(table[8].hits, 0)
        self.assertFalse(only_gr_and_kr_ge_repeat(tuple(row.hits for row in table)))
        only_gk = [0] * STANDING_ROW_COUNT
        only_gk[PASSAGE_ORDER.index(PASSAGE_GR)] = 3
        only_gk[PASSAGE_ORDER.index(PASSAGE_KR)] = 3
        self.assertTrue(only_gr_and_kr_ge_repeat(tuple(only_gk)))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondon380001003Scoreboard(unittest.TestCase):
    """Cited-fixture 380 001 003 12-row hit lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_passage = existing_gk_17gram_lines()
        self.table = score_380_001_003_hits(self.by_passage)
        self.locked = table_tuples(self.table)

    def test_twelve_row_hit_table(self):
        """Hits per fixture for the 17-gram's internal 380 001 003."""
        self.assertEqual(self.locked, STANDING_TABLE)
        self.assertEqual(len(self.table), STANDING_ROW_COUNT)
        self.assertEqual(len(self.table), len(PASSAGE_ORDER))
        self.assertEqual(tuple(row.passage for row in self.table), PASSAGE_ORDER)
        self.assertEqual(tuple(row.hits for row in self.table), STANDING_HITS)
        self.assertEqual(GRAM_3, GRAM_17[:3])
        self.assertEqual(gram_slots(GRAM_17, GRAM_3), STANDING_INTERNAL_SLOTS)
        self.assertEqual(len(STANDING_INTERNAL_SLOTS), STANDING_INTERNAL_REPEAT)
        self.assertEqual(len(GRAM_17), STANDING_COMBINED_N)
        self.assertEqual("076" in GRAM_3, STANDING_STEM_076_IN_LONGEST)
        self.assertFalse(STANDING_STEM_076_IN_LONGEST)
        for row, (passage, hits) in zip(self.table, STANDING_TABLE):
            self.assertEqual(row.passage, passage)
            self.assertEqual(row.hits, hits)
            self.assertEqual(
                row.hits,
                ngram_hit_count(self.by_passage[passage], GRAM_3),
            )
        by_passage = {row.passage: row.hits for row in self.table}
        self.assertEqual(PASSAGE_ORDER[-4], PASSAGE_GR)
        self.assertEqual(PASSAGE_ORDER[-3], PASSAGE_GV)
        self.assertEqual(PASSAGE_ORDER[-2], PASSAGE_KR)
        self.assertEqual(PASSAGE_ORDER[-1], PASSAGE_KV)
        self.assertEqual(by_passage[PASSAGE_GR], 30)
        self.assertEqual(by_passage[PASSAGE_KR], 6)
        self.assertEqual(by_passage[PASSAGE_KV], 11)
        self.assertEqual(by_passage[PASSAGE_GV], 0)
        self.assertEqual(by_passage[PASSAGE_CB], 1)
        self.assertEqual(by_passage[PASSAGE_AA], 0)
        ge_repeat = tuple(row.hits >= STANDING_INTERNAL_REPEAT for row in self.table)
        self.assertEqual(ge_repeat, STANDING_GE_REPEAT)
        ge_passages = tuple(
            row.passage for row in self.table if row.hits >= STANDING_INTERNAL_REPEAT
        )
        self.assertEqual(ge_passages, STANDING_GE_REPEAT_PASSAGES)
        self.assertEqual(
            only_gr_and_kr_ge_repeat(STANDING_HITS),
            STANDING_ONLY_GR_AND_KR_GE_REPEAT,
        )
        self.assertFalse(STANDING_ONLY_GR_AND_KR_GE_REPEAT)
        self.assertGreaterEqual(by_passage[PASSAGE_KV], STANDING_INTERNAL_REPEAT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_17gram_hamming_scoreboard_still_computes(self):
        """Cycle 64 nearest-Hamming lock stays."""
        prior = TestMamariSmallSantiagoLondon17gramHammingScoreboard()
        prior.setUp()
        prior.test_nearest_window_and_le4_flag()
        prior.test_best_hamming_per_fixture()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-65 12-row 3-gram table."""
        lock = self.survey["tablet_g_k_380_001_003_hits_per_fixture"]
        self.assertEqual(lock["cycle"], 65)
        self.assertEqual(lock["focused_batch"], 4)
        self.assertEqual(lock["focused_batch_of"], 5)
        self.assertEqual(tuple(lock["tokens"]), GRAM_3)
        self.assertEqual(lock["n"], 3)
        self.assertEqual(tuple(lock["internal_slots"]), STANDING_INTERNAL_SLOTS)
        self.assertEqual(lock["internal_repeat"], STANDING_INTERNAL_REPEAT)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        self.assertEqual(tuple(lock["hits"]), STANDING_HITS)
        locked = tuple((passage, hits) for passage, hits in lock["table"])
        self.assertEqual(locked, STANDING_TABLE)
        self.assertEqual(tuple(lock["ge_internal_repeat"]), STANDING_GE_REPEAT)
        self.assertEqual(
            tuple(lock["ge_internal_repeat_passages"]),
            STANDING_GE_REPEAT_PASSAGES,
        )
        self.assertEqual(
            lock["only_gr_and_kr_ge_internal_repeat"],
            STANDING_ONLY_GR_AND_KR_GE_REPEAT,
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
        self.assertTrue(lock["standing_gk_17gram_hits_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_sites_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_hamming_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_17gram_nearest_hamming"]["cycle"], 64)
        self.assertEqual(self.survey["tablet_g_k_17gram_hit_sites"]["cycle"], 63)
        self.assertEqual(self.survey["tablet_g_k_17gram_hits_per_fixture"]["cycle"], 62)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondon380001003ImageSnapshot(unittest.TestCase):
    """Cycle 65 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
