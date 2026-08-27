"""090 076, 076 071, and 090 076 071 hits per existing fixture.

Cycle 52 text-search lock. Uses only the already-vendored fixtures:
Ca calendar, Ca remainder, Cb, Aa, Ab, Br, Bv, Ia. No new tablet.
Raw stems; 999 is kept. No invented Barthel. No G00n→Barthel map.
No type merge. No detector retune. No CV. No new agents.

Three eight-row count tables (a 3×8 lock): consecutive 090 076,
076 071, and 090 076 071 hits per fixture. These are stem-id
n-grams — not meanings, list markers, or punctuation. The cycle-49
090 |076| 071 cell pattern is a different claim.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_santiago_ia_076_inventory_scoreboard import (
    STANDING_076_LEFT_TOP,
    STANDING_076_RIGHT_TOP,
)
from tests.test_mamari_santiago_ia_076_rate_scoreboard import (
    IA_HTML_DIR,
    PASSAGE_AA,
    PASSAGE_IA,
    PASSAGE_ORDER,
    STANDING_ROW_COUNT,
    existing_076_rate_lines,
)
from tests.test_mamari_santiago_ia_090_071_rate_scoreboard import (
    TestMamariSantiagoIa090071RateScoreboard,
)
from tests.test_mamari_second_passage_scoreboard import (
    find_ngram_hits,
    load_corpus_survey,
)

GRAM_090_076 = ("090", "076")
GRAM_076_071 = ("076", "071")
GRAM_090_076_071 = ("090", "076", "071")
LOCKED_GRAMS = (GRAM_090_076, GRAM_076_071, GRAM_090_076_071)
STANDING_GRAM_COUNT = 3

STANDING_090_076_HITS = (0, 0, 0, 0, 0, 0, 0, 69)
STANDING_076_071_HITS = (0, 0, 0, 0, 0, 0, 0, 43)
STANDING_090_076_071_HITS = (0, 0, 0, 0, 0, 0, 0, 6)
STANDING_TABLE = (
    (GRAM_090_076, STANDING_090_076_HITS),
    (GRAM_076_071, STANDING_076_071_HITS),
    (GRAM_090_076_071, STANDING_090_076_071_HITS),
)
STANDING_HITS = {
    GRAM_090_076: STANDING_090_076_HITS,
    GRAM_076_071: STANDING_076_071_HITS,
    GRAM_090_076_071: STANDING_090_076_071_HITS,
}
STANDING_ONLY_IA_HAS_HITS = True


@dataclass(frozen=True)
class NgramFixtureRow:
    """One n-gram's hits across the eight fixtures. Ids only."""

    tokens: tuple[str, ...]
    hits: tuple[int, ...]


def ngram_hit_count(lines: list[list[str]], gram: tuple[str, ...]) -> int:
    """Exact consecutive hits of gram. Search only."""
    return len(find_ngram_hits(lines, gram))


def score_ngram_row(
    by_passage: dict[str, list[list[str]]],
    gram: tuple[str, ...],
) -> NgramFixtureRow:
    """Eight-row hit counts for one n-gram in locked passage order."""
    return NgramFixtureRow(
        tokens=gram,
        hits=tuple(ngram_hit_count(by_passage[passage], gram) for passage in PASSAGE_ORDER),
    )


def score_ngram_table(
    by_passage: dict[str, list[list[str]]],
    grams: tuple[tuple[str, ...], ...] = LOCKED_GRAMS,
) -> tuple[NgramFixtureRow, ...]:
    """3×8 lock: one eight-count row per locked n-gram. Search only."""
    return tuple(score_ngram_row(by_passage, gram) for gram in grams)


def table_tuples(
    table: tuple[NgramFixtureRow, ...],
) -> tuple[tuple[tuple[str, ...], tuple[int, ...]], ...]:
    """Stable lock: (tokens, eight hit counts)."""
    return tuple((row.tokens, row.hits) for row in table)


def only_ia_has_hits(row: NgramFixtureRow) -> bool:
    """True iff Ia is the only fixture with a nonzero count."""
    return row.hits[:-1] == (0,) * (STANDING_ROW_COUNT - 1) and row.hits[-1] > 0


class TestSantiagoIa090076071NgramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 090 076 071 counts; a gap is not a hit."""
        provider = MockProvider()
        adjacent = [["090", "076", "071", "090", "076"]]
        self.assertEqual(ngram_hit_count(adjacent, GRAM_090_076), 2)
        self.assertEqual(ngram_hit_count(adjacent, GRAM_076_071), 1)
        self.assertEqual(ngram_hit_count(adjacent, GRAM_090_076_071), 1)
        gapped = [["090", "001", "076", "071"]]
        self.assertEqual(ngram_hit_count(gapped, GRAM_090_076), 0)
        self.assertEqual(ngram_hit_count(gapped, GRAM_076_071), 1)
        self.assertEqual(ngram_hit_count(gapped, GRAM_090_076_071), 0)
        empty = [[]]
        self.assertEqual(ngram_hit_count(empty, GRAM_090_076_071), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_table_follows_locked_grams_and_passage_order(self):
        """Scorer walks LOCKED_GRAMS × PASSAGE_ORDER; missing key is an error."""
        provider = MockProvider()
        by_passage = {passage: [[]] for passage in PASSAGE_ORDER}
        by_passage[PASSAGE_AA] = [["090", "076", "071"], ["090", "076"]]
        table = score_ngram_table(by_passage)
        self.assertEqual(tuple(row.tokens for row in table), LOCKED_GRAMS)
        self.assertEqual(len(table), STANDING_GRAM_COUNT)
        self.assertEqual(len(table[0].hits), STANDING_ROW_COUNT)
        self.assertEqual(table[0].hits[3], 2)
        self.assertEqual(table[1].hits[3], 1)
        self.assertEqual(table[2].hits[3], 1)
        self.assertFalse(only_ia_has_hits(table[0]))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSantiagoIa090076071NgramScoreboard(unittest.TestCase):
    """Cited-fixture 090 076 / 076 071 / 090 076 071 lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_passage = existing_076_rate_lines()
        self.table = score_ngram_table(self.by_passage)
        self.locked = table_tuples(self.table)

    def test_three_by_eight_hit_table(self):
        """Hits per fixture for 090 076, 076 071, and 090 076 071."""
        self.assertEqual(self.locked, STANDING_TABLE)
        self.assertEqual(len(self.table), STANDING_GRAM_COUNT)
        self.assertEqual(tuple(row.tokens for row in self.table), LOCKED_GRAMS)
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
            self.assertEqual(only_ia_has_hits(row), STANDING_ONLY_IA_HAS_HITS)
            self.assertTrue(STANDING_ONLY_IA_HAS_HITS)
        ia_hits = {row.tokens: row.hits[-1] for row in self.table}
        self.assertEqual(ia_hits[GRAM_090_076], STANDING_076_LEFT_TOP[1])
        self.assertEqual(ia_hits[GRAM_076_071], STANDING_076_RIGHT_TOP[1])
        self.assertEqual(STANDING_076_LEFT_TOP, ("090", 69))
        self.assertEqual(STANDING_076_RIGHT_TOP, ("071", 43))
        self.assertLessEqual(ia_hits[GRAM_090_076_071], ia_hits[GRAM_090_076])
        self.assertLessEqual(ia_hits[GRAM_090_076_071], ia_hits[GRAM_076_071])
        self.assertEqual(PASSAGE_ORDER[-1], PASSAGE_IA)
        self.assertFalse((IA_HTML_DIR / "Ib.html").exists())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_090_071_rate_and_scoreboards_still_compute(self):
        """Cycle 51 090/071 rate tables and A/B/C/Ia scoreboards stay."""
        prior = TestMamariSantiagoIa090071RateScoreboard()
        prior.setUp()
        prior.test_two_eight_row_rate_tables()
        prior.test_existing_076_rate_and_scoreboards_still_compute()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-52 3×8 n-gram table."""
        lock = self.survey["stem_090_076_071_ngram_per_fixture"]
        self.assertEqual(lock["cycle"], 52)
        self.assertEqual(tuple(tuple(tokens) for tokens in lock["grams"]), LOCKED_GRAMS)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["gram_count"], STANDING_GRAM_COUNT)
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        self.assertEqual(lock["only_ia_has_hits"], STANDING_ONLY_IA_HAS_HITS)
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
        self.assertTrue(lock["standing_ia_999_locks_unchanged"])
        self.assertTrue(lock["standing_ia_076_locks_unchanged"])
        self.assertTrue(lock["standing_ia_076_cells_unchanged"])
        self.assertTrue(lock["standing_ia_076_rate_unchanged"])
        self.assertTrue(lock["standing_ia_090_071_rate_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["stem_090_071_rate_per_fixture"]["cycle"], 51)
        self.assertEqual(self.survey["stem_076_rate_per_fixture"]["cycle"], 50)
        self.assertEqual(self.survey["santiago_ia_076_cells"]["cycle"], 49)
        self.assertEqual(self.survey["santiago_ia_076_inventory"]["cycle"], 48)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSantiagoIa090076071NgramImageSnapshot(unittest.TestCase):
    """Cycle 52 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
