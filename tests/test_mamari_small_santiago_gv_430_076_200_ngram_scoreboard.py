"""430 076, 076 200, and 430 076 200 hits per existing fixture.

Cycle 58 text-search lock. Uses only the already-vendored fixtures:
Ca calendar, Ca remainder, Cb, Aa, Ab, Br, Bv, Ia, Gr, Gv. No new
tablet. Raw stems; 999 is kept. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents.

Three ten-row count tables (a 3×10 lock): consecutive 430 076,
076 200, and 430 076 200 hits per fixture. These are stem-id
n-grams — not meanings. Not the Cycle 52 Ia pair 090 076 / 076 071.
Gv bigrams match the Cycle 57 neighbor tops (430 left of 076 ×5;
200 right of 076 ×5). The 3-gram is 0 on Gv.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_santiago_ia_076_rate_scoreboard import (
    IA_HTML_DIR,
    PASSAGE_AA,
    PASSAGE_IA,
    PASSAGE_ORDER as RATE_PASSAGE_ORDER,
    existing_076_rate_lines,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    GRAM_076_071,
    GRAM_090_076,
    GRAM_090_076_071,
    NgramFixtureRow,
    TestMamariSantiagoIa090076071NgramScoreboard,
    ngram_hit_count,
    table_tuples,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_santiago_gr_scoreboard import (
    extract_gr_published_tokens,
    gr_line_stems,
    load_vendored_gr_html,
)
from tests.test_mamari_small_santiago_gv_076_inventory_scoreboard import (
    STANDING_076_LEFT_TOP as STANDING_GV_076_LEFT_TOP,
    STANDING_076_RIGHT_TOP as STANDING_GV_076_RIGHT_TOP,
    TestMamariSmallSantiagoGv076InventoryScoreboard,
)
from tests.test_mamari_small_santiago_gv_scoreboard import (
    extract_gv_published_tokens,
    gv_line_stems,
    load_vendored_gv_html,
)

PASSAGE_GR = "tablet_g_small_santiago_recto"
PASSAGE_GV = "tablet_g_small_santiago_verso"
PASSAGE_ORDER = RATE_PASSAGE_ORDER + (PASSAGE_GR, PASSAGE_GV)

GRAM_430_076 = ("430", "076")
GRAM_076_200 = ("076", "200")
GRAM_430_076_200 = ("430", "076", "200")
LOCKED_GRAMS = (GRAM_430_076, GRAM_076_200, GRAM_430_076_200)
STANDING_GRAM_COUNT = 3
STANDING_ROW_COUNT = 10

STANDING_430_076_HITS = (0, 0, 0, 0, 0, 3, 1, 30, 0, 5)
STANDING_076_200_HITS = (0, 0, 0, 0, 0, 0, 0, 5, 0, 5)
STANDING_430_076_200_HITS = (0, 0, 0, 0, 0, 0, 0, 1, 0, 0)
STANDING_TABLE = (
    (GRAM_430_076, STANDING_430_076_HITS),
    (GRAM_076_200, STANDING_076_200_HITS),
    (GRAM_430_076_200, STANDING_430_076_200_HITS),
)
STANDING_HITS = {
    GRAM_430_076: STANDING_430_076_HITS,
    GRAM_076_200: STANDING_076_200_HITS,
    GRAM_430_076_200: STANDING_430_076_200_HITS,
}
STANDING_ONLY_GV_HAS_HITS = False
STANDING_ONLY_IA_HAS_HITS = False
STANDING_GV_TRIGRAM_HITS = 0
STANDING_IA_PAIR_GRAMS = (GRAM_090_076, GRAM_076_071, GRAM_090_076_071)


def existing_430_076_200_lines() -> dict[str, list[list[str]]]:
    """Load the ten already-vendored fixtures. No new scrape."""
    lines = existing_076_rate_lines()
    lines[PASSAGE_GR] = gr_line_stems(extract_gr_published_tokens(load_vendored_gr_html()))
    lines[PASSAGE_GV] = gv_line_stems(extract_gv_published_tokens(load_vendored_gv_html()))
    return lines


def score_ngram_row(
    by_passage: dict[str, list[list[str]]],
    gram: tuple[str, ...],
) -> NgramFixtureRow:
    """Ten-row hit counts for one n-gram in locked passage order."""
    return NgramFixtureRow(
        tokens=gram,
        hits=tuple(ngram_hit_count(by_passage[passage], gram) for passage in PASSAGE_ORDER),
    )


def score_ngram_table(
    by_passage: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...] = LOCKED_GRAMS,
) -> tuple[NgramFixtureRow, ...]:
    """3×10 lock: one ten-count row per locked n-gram. Search only."""
    return tuple(score_ngram_row(by_passage, gram) for gram in grams)


def only_gv_has_hits(row: NgramFixtureRow) -> bool:
    """True iff Gv is the only fixture with a nonzero count."""
    return row.hits[:-1] == (0,) * (STANDING_ROW_COUNT - 1) and row.hits[-1] > 0


class TestSmallSantiagoGv430076200NgramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 430 076 200 counts; a gap is not a hit."""
        provider = MockProvider()
        adjacent = [["430", "076", "200", "430", "076"]]
        self.assertEqual(ngram_hit_count(adjacent, GRAM_430_076), 2)
        self.assertEqual(ngram_hit_count(adjacent, GRAM_076_200), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM_430_076_200), 1)
        gapped = [["430", "001", "076", "200"]]
        self.assertEqual(ngram_hit_count(gapped, GRAM_430_076), 0)
        self.assertEqual(ngram_hit_count(gapped, GRAM_076_200), 1)
        self.assertEqual(ngram_hit_count(gapped, GRAM_430_076_200), 0)
        empty = [[]]
        self.assertEqual(ngram_hit_count(empty, GRAM_430_076_200), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_table_follows_locked_grams_and_passage_order(self):
        """Scorer walks LOCKED_GRAMS × PASSAGE_ORDER; missing key is an error."""
        provider = MockProvider()
        by_passage = {passage: [[]] for passage in PASSAGE_ORDER}
        by_passage[PASSAGE_AA] = [["430", "076", "200"], ["430", "076"]]
        table = score_ngram_table(by_passage)
        self.assertEqual(tuple(row.tokens for row in table), LOCKED_GRAMS)
        self.assertEqual(len(table), STANDING_GRAM_COUNT)
        self.assertEqual(len(table[0].hits), STANDING_ROW_COUNT)
        self.assertEqual(table[0].hits[3], 2)
        self.assertEqual(table[1].hits[3], 1)
        self.assertEqual(table[2].hits[3], 1)
        self.assertFalse(only_gv_has_hits(table[0]))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoGv430076200NgramScoreboard(unittest.TestCase):
    """Cited-fixture 430 076 / 076 200 / 430 076 200 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_passage = existing_430_076_200_lines()
        self.table = score_ngram_table(self.by_passage)
        self.locked = table_tuples(self.table)

    def test_three_by_ten_hit_table(self):
        """Hits per fixture for 430 076, 076 200, and 430 076 200."""
        self.assertEqual(self.locked, STANDING_TABLE)
        self.assertEqual(len(self.table), STANDING_GRAM_COUNT)
        self.assertEqual(tuple(row.tokens for row in self.table), LOCKED_GRAMS)
        self.assertNotEqual(LOCKED_GRAMS, STANDING_IA_PAIR_GRAMS)
        for row, (gram, hits) in zip(self.table, STANDING_TABLE):
            self.assertEqual(row.tokens, gram)
            self.assertEqual(row.hits, hits)
            self.assertEqual(row.hits, STANDING_HITS[gram])
            self.assertEqual(len(row.hits), STANDING_ROW_COUNT)
            self.assertEqual(len(row.hits), len(PASSAGE_ORDER))
            for passage, count in zip(PASSAGE_ORDER, row.hits):
                self.assertEqual(
                    count,
                    ngram_hit_count(self.by_passage[passage], gram),
                )
            self.assertEqual(only_gv_has_hits(row), STANDING_ONLY_GV_HAS_HITS)
            self.assertFalse(STANDING_ONLY_GV_HAS_HITS)
            self.assertFalse(STANDING_ONLY_IA_HAS_HITS)
        by_gram = {row.tokens: row.hits for row in self.table}
        gv_hits = {gram: hits[-1] for gram, hits in by_gram.items()}
        ia_hits = {gram: hits[-3] for gram, hits in by_gram.items()}
        self.assertEqual(PASSAGE_ORDER[-1], PASSAGE_GV)
        self.assertEqual(PASSAGE_ORDER[-2], PASSAGE_GR)
        self.assertEqual(PASSAGE_ORDER[-3], PASSAGE_IA)
        self.assertEqual(gv_hits[GRAM_430_076], STANDING_GV_076_LEFT_TOP[1])
        self.assertEqual(gv_hits[GRAM_076_200], STANDING_GV_076_RIGHT_TOP[1])
        self.assertEqual(STANDING_GV_076_LEFT_TOP, ("430", 5))
        self.assertEqual(STANDING_GV_076_RIGHT_TOP, ("200", 5))
        self.assertEqual(gv_hits[GRAM_430_076_200], STANDING_GV_TRIGRAM_HITS)
        self.assertEqual(STANDING_GV_TRIGRAM_HITS, 0)
        self.assertLessEqual(ia_hits[GRAM_430_076_200], ia_hits[GRAM_430_076])
        self.assertLessEqual(ia_hits[GRAM_430_076_200], ia_hits[GRAM_076_200])
        self.assertFalse((IA_HTML_DIR / "Ib.html").exists())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gv_076_and_ia_ngram_scoreboards_still_compute(self):
        """Cycle 57 Gv 076 inventory and Cycle 52 Ia n-gram table stay."""
        gv = TestMamariSmallSantiagoGv076InventoryScoreboard()
        gv.setUp()
        gv.test_076_count_line_density_and_neighbor_tops()
        gv.test_076_n5_wraps()
        gv.test_existing_gv_scoreboard_still_computes()
        gv.test_survey_matches_computed_lock()
        ia_pair = TestMamariSantiagoIa090076071NgramScoreboard()
        ia_pair.setUp()
        ia_pair.test_three_by_eight_hit_table()
        ia_pair.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-58 3×10 n-gram table."""
        lock = self.survey["stem_430_076_200_ngram_per_fixture"]
        self.assertEqual(lock["cycle"], 58)
        self.assertEqual(tuple(tuple(tokens) for tokens in lock["grams"]), LOCKED_GRAMS)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["gram_count"], STANDING_GRAM_COUNT)
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        self.assertEqual(lock["only_gv_has_hits"], STANDING_ONLY_GV_HAS_HITS)
        self.assertEqual(lock["only_ia_has_hits"], STANDING_ONLY_IA_HAS_HITS)
        self.assertEqual(lock["gv_trigram_hits"], STANDING_GV_TRIGRAM_HITS)
        locked = tuple(
            (tuple(tokens), tuple(hits)) for tokens, hits in lock["table"]
        )
        self.assertEqual(locked, STANDING_TABLE)
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_ia_090_076_071_ngram_unchanged"])
        self.assertTrue(lock["standing_gr_locks_unchanged"])
        self.assertTrue(lock["standing_gv_locks_unchanged"])
        self.assertTrue(lock["standing_gv_076_inventory_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["small_santiago_gv_076_inventory"]["cycle"], 57)
        self.assertEqual(self.survey["stem_090_076_071_ngram_per_fixture"]["cycle"], 52)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoGv430076200ImageSnapshot(unittest.TestCase):
    """Cycle 58 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
