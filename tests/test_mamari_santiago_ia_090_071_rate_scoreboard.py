"""090 and 071 rates per existing fixture: hits, stems, rate, threshold.

Cycle 51 text-search lock. Uses only the already-vendored fixtures:
Ca calendar, Ca remainder, Cb, Aa, Ab, Br, Bv, Ia. No new tablet.
Raw stems; 999 is kept. No invented Barthel. No G00n→Barthel map.
No type merge. No detector retune. No CV. No new agents.

Two eight-row tables: per fixture, 090 and 071 hit counts, stem
count, rate (hits/stems), and whether rate ≥ 0.10. Also locks
whether Ia is the only fixture that clears 0.10 for each. 090 and
071 are stem ids only — not meanings, list markers, or punctuation.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_santiago_ia_076_rate_scoreboard import (
    AA_STEM_TOTAL,
    AB_STEM_TOTAL,
    BR_STEM_TOTAL,
    BV_STEM_TOTAL,
    CB_STEM_TOTAL,
    IA_HTML_DIR,
    IA_STEM_TOTAL,
    PASSAGE_AA,
    PASSAGE_IA,
    PASSAGE_ORDER,
    RATE_THRESHOLD,
    STANDING_CALENDAR_STEM_TOTAL,
    STANDING_REMAINDER_STEM_TOTAL,
    STANDING_ROW_COUNT,
    STANDING_TABLE as STANDING_076_TABLE,
    TestMamariSantiagoIa076RateScoreboard,
    existing_076_rate_lines,
    rate_row_tuple,
    score_076_rate,
    score_076_rate_table,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

STEM_090 = "090"
STEM_071 = "071"
STANDING_STEMS = (STEM_090, STEM_071)

STANDING_CB_090_HITS = 1
STANDING_AA_090_HITS = 4
STANDING_AB_090_HITS = 2
STANDING_IA_090_HITS = 114
STANDING_090_ONLY_IA_GE_THRESHOLD = False

STANDING_CB_071_HITS = 2
STANDING_AA_071_HITS = 3
STANDING_AB_071_HITS = 2
STANDING_BR_071_HITS = 3
STANDING_BV_071_HITS = 2
STANDING_IA_071_HITS = 93
STANDING_071_ONLY_IA_GE_THRESHOLD = False

STANDING_FIXTURE_STEMS = (
    STANDING_CALENDAR_STEM_TOTAL,
    STANDING_REMAINDER_STEM_TOTAL,
    CB_STEM_TOTAL,
    AA_STEM_TOTAL,
    AB_STEM_TOTAL,
    BR_STEM_TOTAL,
    BV_STEM_TOTAL,
    IA_STEM_TOTAL,
)


def standing_rate_table(hits: tuple[int, ...]) -> tuple[tuple[str, int, int, float, bool], ...]:
    """Eight-row lock: passage, hits, stems, rate, ge_0.10."""
    return tuple(
        (
            passage,
            hit_count,
            stem_count,
            hit_count / stem_count,
            (hit_count / stem_count) >= RATE_THRESHOLD,
        )
        for passage, hit_count, stem_count in zip(
            PASSAGE_ORDER, hits, STANDING_FIXTURE_STEMS, strict=True
        )
    )


STANDING_090_TABLE = standing_rate_table(
    (0, 0, STANDING_CB_090_HITS, STANDING_AA_090_HITS, STANDING_AB_090_HITS, 0, 0, STANDING_IA_090_HITS)
)
STANDING_071_TABLE = standing_rate_table(
    (
        0,
        0,
        STANDING_CB_071_HITS,
        STANDING_AA_071_HITS,
        STANDING_AB_071_HITS,
        STANDING_BR_071_HITS,
        STANDING_BV_071_HITS,
        STANDING_IA_071_HITS,
    )
)
STANDING_ONLY_IA_GE = {
    STEM_090: STANDING_090_ONLY_IA_GE_THRESHOLD,
    STEM_071: STANDING_071_ONLY_IA_GE_THRESHOLD,
}


def score_stem_rate_table(by_passage: dict[str, list[list[str]]], stem: str):
    """Eight-row rate table for one stem id. Search only."""
    return tuple(
        score_076_rate(by_passage[passage], passage, stem=stem) for passage in PASSAGE_ORDER
    )


def ge_passages(table) -> tuple[str, ...]:
    """Fixtures whose rate is ≥ 0.10."""
    return tuple(row.passage for row in table if row.ge_threshold)


def only_ia_ge_threshold(table) -> bool:
    """True iff Ia is the only fixture at or above 0.10."""
    return ge_passages(table) == (PASSAGE_IA,)


class TestSantiagoIa090071RateHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_rate_uses_requested_stem_and_threshold(self):
        """090 1/10 meets 0.10; 071 1/11 does not; empty stems are rate 0."""
        provider = MockProvider()
        at = score_076_rate([[STEM_090] + ["001"] * 9], "syn", stem=STEM_090)
        self.assertEqual(rate_row_tuple(at), ("syn", 1, 10, 0.10, True))
        below = score_076_rate([[STEM_071] + ["001"] * 10], "syn", stem=STEM_071)
        self.assertEqual(rate_row_tuple(below), ("syn", 1, 11, 1 / 11, False))
        empty = score_076_rate([[]], "empty", stem=STEM_090)
        self.assertEqual(rate_row_tuple(empty), ("empty", 0, 0, 0.0, False))
        self.assertFalse(only_ia_ge_threshold((at, below)))
        self.assertEqual(provider.get_call_history(), [])

    def test_tables_follow_passage_order_per_stem(self):
        """Each stem walks PASSAGE_ORDER; missing key is an error."""
        provider = MockProvider()
        by_passage = {passage: [[]] for passage in PASSAGE_ORDER}
        by_passage[PASSAGE_AA] = [[STEM_090, STEM_071, STEM_071]]
        table_090 = score_stem_rate_table(by_passage, STEM_090)
        table_071 = score_stem_rate_table(by_passage, STEM_071)
        self.assertEqual(tuple(row.passage for row in table_090), PASSAGE_ORDER)
        self.assertEqual(tuple(row.passage for row in table_071), PASSAGE_ORDER)
        self.assertEqual(len(table_090), STANDING_ROW_COUNT)
        self.assertEqual(rate_row_tuple(table_090[3])[1:3], (1, 3))
        self.assertEqual(rate_row_tuple(table_071[3])[1:3], (2, 3))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSantiagoIa090071RateScoreboard(unittest.TestCase):
    """Cited-fixture 090 / 071 rate lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_passage = existing_076_rate_lines()
        self.tables = {
            stem: score_stem_rate_table(self.by_passage, stem) for stem in STANDING_STEMS
        }
        self.locked = {
            stem: tuple(rate_row_tuple(row) for row in table)
            for stem, table in self.tables.items()
        }

    def test_two_eight_row_rate_tables(self):
        """Hits / stems / rate / ≥0.10 for 090 and 071 on the same fixtures."""
        standing = {STEM_090: STANDING_090_TABLE, STEM_071: STANDING_071_TABLE}
        ia_hits = {STEM_090: STANDING_IA_090_HITS, STEM_071: STANDING_IA_071_HITS}
        for stem in STANDING_STEMS:
            table = self.tables[stem]
            self.assertEqual(self.locked[stem], standing[stem])
            self.assertEqual(len(table), STANDING_ROW_COUNT)
            self.assertEqual(tuple(row.passage for row in table), PASSAGE_ORDER)
            for row, expected in zip(table, standing[stem]):
                passage, hits, stems, rate, ge_threshold = expected
                self.assertEqual(row.passage, passage)
                self.assertEqual(row.hits, hits)
                self.assertEqual(row.stems, stems)
                self.assertEqual(row.rate, rate)
                self.assertEqual(row.rate, hits / stems)
                self.assertEqual(row.ge_threshold, ge_threshold)
                self.assertEqual(row.ge_threshold, row.rate >= RATE_THRESHOLD)
                self.assertEqual(
                    row.stems, sum(len(line) for line in self.by_passage[passage])
                )
                self.assertEqual(
                    row.hits,
                    sum(line.count(stem) for line in self.by_passage[passage]),
                )
            self.assertEqual(ge_passages(table), ())
            self.assertEqual(only_ia_ge_threshold(table), STANDING_ONLY_IA_GE[stem])
            self.assertFalse(STANDING_ONLY_IA_GE[stem])
            self.assertEqual(table[-1].hits, ia_hits[stem])
        self.assertFalse((IA_HTML_DIR / "Ib.html").exists())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_076_rate_and_scoreboards_still_compute(self):
        """Cycle 50 076 table and A/B/C/Ia scoreboards stay."""
        self.assertEqual(
            tuple(rate_row_tuple(row) for row in score_076_rate_table(self.by_passage)),
            STANDING_076_TABLE,
        )
        prior = TestMamariSantiagoIa076RateScoreboard()
        prior.setUp()
        prior.test_eight_row_076_rate_table()
        prior.test_existing_a_b_c_and_ia_scoreboards_still_compute()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-51 090 and 071 rate tables."""
        lock = self.survey["stem_090_071_rate_per_fixture"]
        self.assertEqual(lock["cycle"], 51)
        self.assertEqual(tuple(lock["stems"]), STANDING_STEMS)
        self.assertEqual(lock["threshold"], RATE_THRESHOLD)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(tuple(lock["passages"]), PASSAGE_ORDER)
        standing = {STEM_090: STANDING_090_TABLE, STEM_071: STANDING_071_TABLE}
        for stem in STANDING_STEMS:
            self.assertEqual(lock["only_ia_ge_threshold"][stem], STANDING_ONLY_IA_GE[stem])
            locked = tuple(
                (
                    passage,
                    hits,
                    stems,
                    (hits / stems) if stems else 0.0,
                    ge_threshold,
                )
                for passage, hits, stems, ge_threshold in lock["tables"][stem]
            )
            self.assertEqual(locked, standing[stem])
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
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["stem_076_rate_per_fixture"]["cycle"], 50)
        self.assertEqual(self.survey["santiago_ia_076_cells"]["cycle"], 49)
        self.assertEqual(self.survey["santiago_ia_076_inventory"]["cycle"], 48)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSantiagoIa090071RateImageSnapshot(unittest.TestCase):
    """Cycle 51 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
