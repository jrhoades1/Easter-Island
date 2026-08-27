"""Cb longest 5-grams on existing Ca calendar and Ca remainder only.

Cycle 34 text-search lock. Uses the cycle-33 Cb n=5 motifs and the
already-vendored Ca calendar fixture plus Ca.html remainder. Does not
scrape a new tablet. Does not re-mine Cb. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV.

Three-row table: motif, Ca-calendar hits, Ca-remainder hits. Hits are
(line, start, end) spans; empty means absent (freq 0). All three Cb
5-grams are absent from both Ca fixtures.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_calendar_scoreboard import (
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_LONGEST_NGRAMS,
)
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    REMAINDER_LINE_NAMES,
    extract_ca_published_tokens,
    find_ngram_hits,
    load_corpus_survey,
    load_vendored_ca_html,
    remainder_line_stems,
)

CB_5GRAMS = tuple(tokens for tokens, _n, _freq, _spans in STANDING_LONGEST_NGRAMS)

# (tokens, calendar_hits, remainder_hits) — empty hits = absent.
STANDING_CA_CROSS_TABLE = (
    (("660", "005", "064", "660", "005"), (), ()),
    (("381", "004", "066", "760", "004"), (), ()),
    (("099", "004", "002", "004", "002"), (), ()),
)
STANDING_ROW_COUNT = 3
STANDING_CALENDAR_ALL_ABSENT = True
STANDING_REMAINDER_ALL_ABSENT = True


@dataclass(frozen=True)
class CrossHitRow:
    """One Cb 5-gram on the two Ca fixtures. Stems only; no meanings."""

    tokens: tuple[str, ...]
    calendar_hits: tuple[tuple[str, int, int], ...]
    remainder_hits: tuple[tuple[str, int, int], ...]


def hit_spans(
    lines: list[list[str]],
    gram: tuple[str, ...],
    line_names: tuple[str, ...],
) -> tuple[tuple[str, int, int], ...]:
    """Exact (line, start, end) hits of gram. Search only."""
    n = len(gram)
    return tuple(
        (line_names[line_index], start, start + n)
        for line_index, start in find_ngram_hits(lines, gram)
    )


def score_cb_5gram_ca_cross(
    motifs: tuple[tuple[str, ...], ...],
    calendar_lines: list[list[str]],
    calendar_names: tuple[str, ...],
    remainder_lines: list[list[str]],
    remainder_names: tuple[str, ...],
) -> tuple[CrossHitRow, ...]:
    """3-row motif / calendar-hits / remainder-hits table. Search only."""
    return tuple(
        CrossHitRow(
            tokens=gram,
            calendar_hits=hit_spans(calendar_lines, gram, calendar_names),
            remainder_hits=hit_spans(remainder_lines, gram, remainder_names),
        )
        for gram in motifs
    )


def row_tuple(row: CrossHitRow) -> tuple:
    """Stable lock row: motif, calendar hits, remainder hits."""
    return (row.tokens, row.calendar_hits, row.remainder_hits)


class TestCb5gramCaCrossHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_records_hits_or_absent(self):
        """Present grams keep spans; missing grams stay empty (freq 0)."""
        gram = ("660", "005", "064", "660", "005")
        other = ("381", "004", "066", "760", "004")
        calendar = [["040", "010"], ["390", "041"]]
        remainder = [list(gram) + ["X"], ["Y"] + list(gram)]
        provider = MockProvider()
        table = score_cb_5gram_ca_cross(
            (gram, other),
            calendar,
            ("Ca6", "Ca7"),
            remainder,
            ("Ca1", "Ca2"),
        )
        self.assertEqual(
            tuple(row_tuple(row) for row in table),
            (
                (gram, (), (("Ca1", 0, 5), ("Ca2", 1, 6))),
                (other, (), ()),
            ),
        )
        self.assertEqual(len(table[0].remainder_hits), 2)
        self.assertEqual(len(table[1].calendar_hits), 0)
        self.assertEqual(len(table[1].remainder_hits), 0)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariCb5gramCaCrossScoreboard(unittest.TestCase):
    """Cited Ca calendar + remainder lock of the three Cb 5-grams. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.calendar = fixture_line_stems(load_mamari_fixture())
        self.remainder = remainder_line_stems(
            extract_ca_published_tokens(load_vendored_ca_html())
        )
        self.table = score_cb_5gram_ca_cross(
            CB_5GRAMS,
            self.calendar,
            CALENDAR_LINE_NAMES,
            self.remainder,
            REMAINDER_LINE_NAMES,
        )

    def test_uses_existing_ca_fixtures_and_cb_motifs(self):
        """Cycle-33 5-grams only. Calendar 101 stems, remainder 416. No Cb remine."""
        self.assertEqual(CB_5GRAMS, tuple(row[0] for row in STANDING_CA_CROSS_TABLE))
        self.assertEqual(CB_5GRAMS, tuple(tokens for tokens, *_rest in STANDING_LONGEST_NGRAMS))
        self.assertEqual(len(CB_5GRAMS), STANDING_ROW_COUNT)
        self.assertTrue(all(len(gram) == 5 for gram in CB_5GRAMS))
        self.assertEqual(sum(len(line) for line in self.calendar), 101)
        self.assertEqual(sum(len(line) for line in self.remainder), 416)
        self.assertEqual(tuple(CALENDAR_LINE_NAMES), ("Ca6", "Ca7", "Ca8", "Ca9"))
        self.assertNotEqual(self.calendar, self.remainder)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_three_row_table_is_standing_truth(self):
        """Lock motif / Ca-calendar hits / Ca-remainder hits. All absent."""
        locked = tuple(row_tuple(row) for row in self.table)
        self.assertEqual(len(locked), STANDING_ROW_COUNT)
        self.assertEqual(locked, STANDING_CA_CROSS_TABLE)
        calendar_absent = all(not row.calendar_hits for row in self.table)
        remainder_absent = all(not row.remainder_hits for row in self.table)
        self.assertEqual(calendar_absent, STANDING_CALENDAR_ALL_ABSENT)
        self.assertEqual(remainder_absent, STANDING_REMAINDER_ALL_ABSENT)
        for row in self.table:
            self.assertEqual(len(row.calendar_hits), 0)
            self.assertEqual(len(row.remainder_hits), 0)
            self.assertEqual(
                find_ngram_hits(self.calendar, row.tokens),
                [],
            )
            self.assertEqual(
                find_ngram_hits(self.remainder, row.tokens),
                [],
            )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-34 Ca cross lock."""
        lock = self.survey["cb_5gram_ca_cross"]
        self.assertEqual(lock["cycle"], 34)
        self.assertEqual(lock["calendar_passage"], "ca6_ca9_calendar")
        self.assertEqual(lock["remainder_passage"], "ca_side_a_remainder")
        self.assertEqual(lock["source_motifs"], "cb_repeating_ngram_profile.longest")
        locked = tuple(
            (tuple(tokens), tuple(tuple(hit) for hit in cal), tuple(tuple(hit) for hit in rem))
            for tokens, cal, rem in lock["table"]
        )
        self.assertEqual(locked, STANDING_CA_CROSS_TABLE)
        self.assertEqual(lock["row_count"], STANDING_ROW_COUNT)
        self.assertEqual(lock["calendar_all_absent"], STANDING_CALENDAR_ALL_ABSENT)
        self.assertEqual(lock["remainder_all_absent"], STANDING_REMAINDER_ALL_ABSENT)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariCb5gramCaCrossImageSnapshot(unittest.TestCase):
    """Cycle 34 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
