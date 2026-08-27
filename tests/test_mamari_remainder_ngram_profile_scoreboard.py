"""Remainder repeating n-gram profile: second passage only, n≥4, freq≥2.

Cycle 29 text-search lock. Uses the already-vendored Kohaumotu Ca.html
remainder (cycle 28). Does not re-mine the 101-stem Ca6–Ca9 calendar
fixture. No invented Barthel. No Cb.html scrape. No G00n→Barthel map.
No type merge. No detector retune. No CV.

Per-line extract_ngrams, same analyzer as the calendar scoreboard.
For each distinct n-gram: tokens, n, freq, line spans. Guy's 8-stem
delimiter is still absent. 600's five remainder hits sit outside every
repeating n≥4 span.

Longest n with freq ≥2 is 9 (Ca10 / Ca11). Top 8-gram is the 9-gram
prefix, freq 2 — not Guy's delimiter. Cycle 30 locks that 9-gram as
a motif on this remainder and on the calendar fixture. Cycle 31
locks the six 002…002 n=9 wraps as a family (interior overlap with
the motif). Cycle 33 locks the same n≥4 freq≥2 profile on the
already-vendored Cb.html verso. Cycle 34 locks those three
Cb 5-grams on this remainder and the calendar fixture.
Image snapshot stays 83/62 / Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_second_passage_scoreboard import (
    REMAINDER_LINE_NAMES,
    STANDING_600_HITS,
    STANDING_REMAINDER_STEM_COUNTS,
    STANDING_REMAINDER_STEM_TOTAL,
    STEM_600,
    extract_ca_published_tokens,
    find_ngram_hits,
    load_corpus_survey,
    load_vendored_ca_html,
    remainder_line_stems,
    stem_hits,
)

PROFILE_MIN_N = 4
PROFILE_MIN_FREQ = 2
STANDING_REPEATING_NGRAM_COUNT = 31
STANDING_COUNTS_BY_N = {4: 11, 5: 8, 6: 6, 7: 3, 8: 2, 9: 1}
STANDING_LONGEST_N = 9
STANDING_LONGEST_NGRAM = (
    "002",
    "010",
    "070",
    "760",
    "040",
    "006",
    "430",
    "047",
    "002",
)
STANDING_LONGEST_FREQ = 2
STANDING_LONGEST_SPANS = (("Ca10", 26, 35), ("Ca11", 14, 23))
STANDING_TOP_8GRAM = (
    "002",
    "010",
    "070",
    "760",
    "040",
    "006",
    "430",
    "047",
)
STANDING_TOP_8GRAM_FREQ = 2
STANDING_EIGHTGRAM_COUNT = 2
STANDING_600_INSIDE_REPEATING = False

# (tokens, n, freq, spans)
STANDING_REPEATING_NGRAMS = (
    (("070", "760", "040", "006"), 4, 5, (
            ("Ca10", 9, 13),
            ("Ca10", 20, 24),
            ("Ca10", 28, 32),
            ("Ca11", 4, 8),
            ("Ca11", 16, 20),
        )),
    (("010", "070", "760", "040"), 4, 4, (
            ("Ca10", 19, 23),
            ("Ca10", 27, 31),
            ("Ca11", 3, 7),
            ("Ca11", 15, 19),
        )),
    (("380", "001", "022", "254"), 4, 3, (
            ("Ca3", 0, 4),
            ("Ca3", 13, 17),
            ("Ca3", 25, 29),
        )),
    (("760", "040", "006", "400"), 4, 3, (
            ("Ca10", 10, 14),
            ("Ca10", 21, 25),
            ("Ca11", 5, 9),
        )),
    (("002", "010", "070", "760"), 4, 3, (
            ("Ca10", 18, 22),
            ("Ca10", 26, 30),
            ("Ca11", 14, 18),
        )),
    (("760", "040", "006", "430"), 4, 3, (
            ("Ca10", 29, 33),
            ("Ca11", 17, 21),
            ("Ca12", 0, 4),
        )),
    (("040", "006", "430", "047"), 4, 3, (
            ("Ca10", 30, 34),
            ("Ca11", 18, 22),
            ("Ca12", 1, 5),
        )),
    (("040", "006", "400", "047"), 4, 2, (
            ("Ca10", 11, 15),
            ("Ca11", 6, 10),
        )),
    (("006", "430", "047", "002"), 4, 2, (
            ("Ca10", 31, 35),
            ("Ca11", 19, 23),
        )),
    (("002", "004", "760", "002"), 4, 2, (
            ("Ca11", 22, 26),
            ("Ca11", 26, 30),
        )),
    (("004", "760", "002", "002"), 4, 2, (
            ("Ca11", 23, 27),
            ("Ca11", 27, 31),
        )),
    (("010", "070", "760", "040", "006"), 5, 4, (
            ("Ca10", 19, 24),
            ("Ca10", 27, 32),
            ("Ca11", 3, 8),
            ("Ca11", 15, 20),
        )),
    (("070", "760", "040", "006", "400"), 5, 3, (
            ("Ca10", 9, 14),
            ("Ca10", 20, 25),
            ("Ca11", 4, 9),
        )),
    (("002", "010", "070", "760", "040"), 5, 3, (
            ("Ca10", 18, 23),
            ("Ca10", 26, 31),
            ("Ca11", 14, 19),
        )),
    (("760", "040", "006", "430", "047"), 5, 3, (
            ("Ca10", 29, 34),
            ("Ca11", 17, 22),
            ("Ca12", 0, 5),
        )),
    (("760", "040", "006", "400", "047"), 5, 2, (
            ("Ca10", 10, 15),
            ("Ca11", 5, 10),
        )),
    (("070", "760", "040", "006", "430"), 5, 2, (
            ("Ca10", 28, 33),
            ("Ca11", 16, 21),
        )),
    (("040", "006", "430", "047", "002"), 5, 2, (
            ("Ca10", 30, 35),
            ("Ca11", 18, 23),
        )),
    (("002", "004", "760", "002", "002"), 5, 2, (
            ("Ca11", 22, 27),
            ("Ca11", 26, 31),
        )),
    (("002", "010", "070", "760", "040", "006"), 6, 3, (
            ("Ca10", 18, 24),
            ("Ca10", 26, 32),
            ("Ca11", 14, 20),
        )),
    (("070", "760", "040", "006", "400", "047"), 6, 2, (
            ("Ca10", 9, 15),
            ("Ca11", 4, 10),
        )),
    (("010", "070", "760", "040", "006", "400"), 6, 2, (
            ("Ca10", 19, 25),
            ("Ca11", 3, 9),
        )),
    (("010", "070", "760", "040", "006", "430"), 6, 2, (
            ("Ca10", 27, 33),
            ("Ca11", 15, 21),
        )),
    (("070", "760", "040", "006", "430", "047"), 6, 2, (
            ("Ca10", 28, 34),
            ("Ca11", 16, 22),
        )),
    (("760", "040", "006", "430", "047", "002"), 6, 2, (
            ("Ca10", 29, 35),
            ("Ca11", 17, 23),
        )),
    (("002", "010", "070", "760", "040", "006", "430"), 7, 2, (
            ("Ca10", 26, 33),
            ("Ca11", 14, 21),
        )),
    (("010", "070", "760", "040", "006", "430", "047"), 7, 2, (
            ("Ca10", 27, 34),
            ("Ca11", 15, 22),
        )),
    (("070", "760", "040", "006", "430", "047", "002"), 7, 2, (
            ("Ca10", 28, 35),
            ("Ca11", 16, 23),
        )),
    (("002", "010", "070", "760", "040", "006", "430", "047"), 8, 2, (
            ("Ca10", 26, 34),
            ("Ca11", 14, 22),
        )),
    (("010", "070", "760", "040", "006", "430", "047", "002"), 8, 2, (
            ("Ca10", 27, 35),
            ("Ca11", 15, 23),
        )),
    (("002", "010", "070", "760", "040", "006", "430", "047", "002"), 9, 2, (
            ("Ca10", 26, 35),
            ("Ca11", 14, 23),
        )),
)


@dataclass(frozen=True)
class RemainderNgramRow:
    """One remainder n-gram with freq ≥2. Stems only; no meanings."""

    tokens: tuple[str, ...]
    n: int
    freq: int
    spans: tuple[tuple[str, int, int], ...]


@dataclass(frozen=True)
class RemainderNgramProfile:
    """n≥4 freq≥2 snapshot on the published Ca.html remainder."""

    rows: tuple[RemainderNgramRow, ...]
    longest_n: int
    longest: tuple[RemainderNgramRow, ...]
    eightgrams: tuple[RemainderNgramRow, ...]
    top_8gram: RemainderNgramRow | None


def profile_tuple(row: RemainderNgramRow) -> tuple:
    """Stable lock row: tokens, n, freq, spans."""
    return (row.tokens, row.n, row.freq, row.spans)


def ngram_spans(
    lines: list[list[str]],
    gram: tuple[str, ...],
    line_names: tuple[str, ...] = REMAINDER_LINE_NAMES,
) -> tuple[tuple[str, int, int], ...]:
    """(line, start, end) for every occurrence of gram."""
    n = len(gram)
    return tuple(
        (line_names[line_index], start, start + n)
        for line_index, start in find_ngram_hits(lines, gram)
    )


def score_remainder_repeating_ngrams(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
    min_n: int = PROFILE_MIN_N,
    min_freq: int = PROFILE_MIN_FREQ,
    line_names: tuple[str, ...] = REMAINDER_LINE_NAMES,
) -> RemainderNgramProfile:
    """Build the n≥4 freq≥2 remainder profile. Search only; no type map."""
    max_n = max((len(seq) for seq in lines), default=0)
    rows: list[RemainderNgramRow] = []
    for n in range(min_n, max_n + 1):
        for gram, freq in analyzer.extract_ngrams(lines, n=n, min_frequency=min_freq):
            rows.append(
                RemainderNgramRow(
                    tokens=gram,
                    n=n,
                    freq=freq,
                    spans=ngram_spans(lines, gram, line_names),
                )
            )
    longest_n = max((row.n for row in rows), default=0)
    eightgrams = tuple(row for row in rows if row.n == 8)
    return RemainderNgramProfile(
        rows=tuple(rows),
        longest_n=longest_n,
        longest=tuple(row for row in rows if row.n == longest_n),
        eightgrams=eightgrams,
        top_8gram=eightgrams[0] if eightgrams else None,
    )


def stem_inside_repeating(
    line: str,
    index: int,
    rows: tuple[RemainderNgramRow, ...] | list[RemainderNgramRow],
) -> bool:
    """True if (line, index) sits inside any repeating n-gram span."""
    return any(
        span_line == line and start <= index < end
        for row in rows
        for span_line, start, end in row.spans
    )


class TestRemainderNgramProfileHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_min_n_and_min_freq_filter(self):
        """n=3 repeats and hapax 4-grams are outside the lock."""
        gram4 = ("A", "B", "C", "D")
        lines = [list(gram4) + ["X"], ["Y"] + list(gram4)]
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        profile = score_remainder_repeating_ngrams(
            lines, analyzer, line_names=("L0", "L1")
        )
        self.assertEqual(profile.longest_n, 4)
        self.assertEqual(len(profile.rows), 1)
        self.assertEqual(profile.rows[0].tokens, gram4)
        self.assertEqual(profile.rows[0].freq, 2)
        self.assertEqual(profile.rows[0].spans, (("L0", 0, 4), ("L1", 1, 5)))
        self.assertIsNone(profile.top_8gram)
        self.assertEqual(provider.get_call_history(), [])

    def test_top_8gram_none_when_absent(self):
        """Lock none when no repeating 8-gram exists."""
        lines = [["W", "X", "Y", "Z", "Q"], ["W", "X", "Y", "Z", "R"]]
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        profile = score_remainder_repeating_ngrams(
            lines, analyzer, line_names=("L0", "L1")
        )
        self.assertEqual(profile.eightgrams, ())
        self.assertIsNone(profile.top_8gram)
        self.assertEqual(provider.get_call_history(), [])

    def test_stem_inside_repeating_needs_covering_span(self):
        """600-style hits are inside only when a repeating span covers them."""
        gram4 = ("A", "B", "600", "C")
        lines = [list(gram4) + ["600"], ["X"] + list(gram4)]
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        profile = score_remainder_repeating_ngrams(
            lines, analyzer, line_names=("L0", "L1")
        )
        self.assertTrue(stem_inside_repeating("L0", 2, profile.rows))
        self.assertFalse(stem_inside_repeating("L0", 4, profile.rows))
        self.assertTrue(stem_inside_repeating("L1", 3, profile.rows))
        self.assertEqual(provider.get_call_history(), [])


class TestMamariRemainderNgramProfileScoreboard(unittest.TestCase):
    """Cited Ca.html remainder n≥4 freq≥2 lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.published = extract_ca_published_tokens(load_vendored_ca_html())
        self.lines = remainder_line_stems(self.published)
        self.profile = score_remainder_repeating_ngrams(self.lines, self.analyzer)

    def test_fixture_is_the_remainder_not_the_calendar(self):
        """Second-passage stems only. Calendar Ca6–Ca9 is not re-mined."""
        self.assertEqual(tuple(REMAINDER_LINE_NAMES), (
            "Ca1", "Ca2", "Ca3", "Ca4", "Ca5", "Ca6",
            "Ca9", "Ca10", "Ca11", "Ca12", "Ca13", "Ca14",
        ))
        self.assertEqual(
            [len(line) for line in self.lines],
            list(STANDING_REMAINDER_STEM_COUNTS),
        )
        self.assertEqual(sum(len(line) for line in self.lines), STANDING_REMAINDER_STEM_TOTAL)
        self.assertNotIn("Ca7", REMAINDER_LINE_NAMES)
        self.assertNotIn("Ca8", REMAINDER_LINE_NAMES)
        calendar = fixture_line_stems(load_mamari_fixture())
        self.assertEqual([len(line) for line in calendar], [16, 43, 40, 2])
        self.assertNotEqual(self.lines, calendar)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_profile_table_is_standing_truth(self):
        """Lock every remainder n≥4 freq≥2 n-gram: tokens, n, freq, spans."""
        p = self.profile
        locked = tuple(profile_tuple(row) for row in p.rows)
        self.assertEqual(len(locked), STANDING_REPEATING_NGRAM_COUNT)
        self.assertEqual(locked, STANDING_REPEATING_NGRAMS)
        counts: dict[int, int] = {}
        for row in p.rows:
            self.assertGreaterEqual(row.n, PROFILE_MIN_N)
            self.assertGreaterEqual(row.freq, PROFILE_MIN_FREQ)
            self.assertEqual(row.n, len(row.tokens))
            self.assertEqual(row.freq, len(row.spans))
            counts[row.n] = counts.get(row.n, 0) + 1
        self.assertEqual(counts, STANDING_COUNTS_BY_N)
        self.assertNotIn(DELIMITER_MOTIF, [row.tokens for row in p.rows])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_n_is_9(self):
        """Longest repeating n is 002 010 070 760 040 006 430 047 002, freq 2."""
        p = self.profile
        self.assertEqual(p.longest_n, STANDING_LONGEST_N)
        self.assertEqual(len(p.longest), 1)
        longest = p.longest[0]
        self.assertEqual(longest.tokens, STANDING_LONGEST_NGRAM)
        self.assertEqual(longest.freq, STANDING_LONGEST_FREQ)
        self.assertEqual(longest.spans, STANDING_LONGEST_SPANS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_top_8gram_is_not_guys_delimiter(self):
        """Highest-frequency 8-gram exists and is not 390 041 378 041 670 008 078 711."""
        p = self.profile
        self.assertIsNotNone(p.top_8gram)
        top = p.top_8gram
        self.assertEqual(len(p.eightgrams), STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(top.tokens, STANDING_TOP_8GRAM)
        self.assertNotEqual(top.tokens, DELIMITER_MOTIF)
        self.assertEqual(top.freq, STANDING_TOP_8GRAM_FREQ)
        self.assertEqual(
            [row.tokens for row in p.eightgrams],
            [row[0] for row in STANDING_REPEATING_NGRAMS if row[1] == 8],
        )
        self.assertEqual(find_ngram_hits(self.lines, DELIMITER_MOTIF), [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_600_sits_outside_repeating_nge4(self):
        """Five remainder 600 hits; none sit inside a repeating n≥4 span."""
        hits = stem_hits(self.lines, STEM_600)
        self.assertEqual(hits, STANDING_600_HITS)
        inside = tuple(
            stem_inside_repeating(line, index, self.profile.rows)
            for line, index in hits
        )
        self.assertEqual(inside, (False,) * len(hits))
        self.assertEqual(any(inside), STANDING_600_INSIDE_REPEATING)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-29 remainder n-gram lock."""
        profile = self.survey["repeating_ngram_profile"]
        self.assertEqual(profile["cycle"], 29)
        self.assertEqual(profile["distinct_count"], STANDING_REPEATING_NGRAM_COUNT)
        self.assertEqual(profile["longest_n"], STANDING_LONGEST_N)
        self.assertEqual(profile["longest_tokens"], list(STANDING_LONGEST_NGRAM))
        self.assertEqual(profile["longest_freq"], STANDING_LONGEST_FREQ)
        self.assertEqual(
            [tuple(span) for span in profile["longest_spans"]],
            list(STANDING_LONGEST_SPANS),
        )
        self.assertEqual(profile["eightgram_count"], STANDING_EIGHTGRAM_COUNT)
        self.assertEqual(profile["top_8gram"], list(STANDING_TOP_8GRAM))
        self.assertEqual(profile["top_8gram_freq"], STANDING_TOP_8GRAM_FREQ)
        self.assertFalse(profile["top_8gram_is_guy_delimiter"])
        self.assertEqual(
            [tuple(hit) for hit in profile["stem_600_hits"]],
            list(STANDING_600_HITS),
        )
        self.assertEqual(
            profile["stem_600_inside_repeating_nge4"],
            STANDING_600_INSIDE_REPEATING,
        )
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariRemainderNgramImageSnapshot(unittest.TestCase):
    """Cycle 29 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
