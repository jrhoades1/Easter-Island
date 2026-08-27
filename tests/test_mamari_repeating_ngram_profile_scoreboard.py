"""Published Barthel repeating n-gram profile: Ca6–Ca9, n≥4, freq≥2.

Cycle 24 text-search lock. Uses only the existing Kohaumotu / Guy
fixture (tests/fixtures/mamari_ca6_ca9_barthel.json). No invented
Barthel. No G00n→Barthel map. No type merge. No detector retune.

Per-line extract_ngrams, same as the calendar scoreboard. For each
distinct n-gram: tokens, n, freq, line spans, whether it is Guy's
8-stem delimiter, and whether any span overlaps a published delimiter
window. Ca6 first-delimiter variants (315 / 375) are not remapped, so
their shared tail does not count as a Guy window.

Longest n with freq ≥2 is 13 (five 040 + delimiter). Top 8-gram is
still the delimiter (freq 6). Image snapshot stays 83/62 / Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from processors.glyph_processor import min_pairwise_window_hamming
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_delimiter_window_scoreboard import (
    STANDING_SLOT_MATCHES,
    STANDING_SLOT_UNIQUE_COUNTS,
    score_delimiter_windows,
)
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)
from tests.test_mamari_nearest_8window_scoreboard import STANDING_PUBLISHED_MIN_HAMMING
from tests.test_mamari_position_alignment_scoreboard import (
    delimiter_spans,
    find_ngram_hits,
    published_ca7_ca8_stems,
)
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_UNIQUE_CLUSTERS,
    published_ca7_ca8_stem_counts,
    score_type_identity,
)
from tests.test_mamari_unconstrained_ngram_scoreboard import hit_overlaps_delimiter_span

LINE_NAMES = ("Ca6", "Ca7", "Ca8", "Ca9")
PROFILE_MIN_N = 4
PROFILE_MIN_FREQ = 2
STANDING_REPEATING_NGRAM_COUNT = 70
STANDING_LONGEST_N = 13
STANDING_LONGEST_NGRAM = (
    "040",
    "040",
    "040",
    "040",
    "040",
    "390",
    "041",
    "378",
    "041",
    "670",
    "008",
    "078",
    "711",
)
STANDING_LONGEST_FREQ = 2
STANDING_TOP_8GRAM = DELIMITER_MOTIF
STANDING_TOP_8GRAM_FREQ = 6
# Ca6 first-delimiter variant tail. Same numbers as Guy after 315/375,
# but those lines have no exact 378 window, so the Ca6 hits do not overlap.
STANDING_CA6_VARIANT_TAIL = ("041", "670", "008", "078", "711")

# (tokens, n, freq, is_delimiter, overlaps_window, spans)
# spans: (line, start, end, overlaps_that_span)
STANDING_REPEATING_NGRAMS = (
    (("041", "670", "008", "078"), 4, 7, False, True, (
            ("Ca6", 3, 7, False),
            ("Ca7", 9, 13, True),
            ("Ca7", 22, 26, True),
            ("Ca7", 36, 40, True),
            ("Ca8", 6, 10, True),
            ("Ca8", 18, 22, True),
            ("Ca8", 32, 36, True),
        )),
    (("670", "008", "078", "711"), 4, 7, False, True, (
            ("Ca6", 4, 8, False),
            ("Ca7", 10, 14, True),
            ("Ca7", 23, 27, True),
            ("Ca7", 37, 41, True),
            ("Ca8", 7, 11, True),
            ("Ca8", 19, 23, True),
            ("Ca8", 33, 37, True),
        )),
    (("390", "041", "378", "041"), 4, 6, False, True, (
            ("Ca7", 6, 10, True),
            ("Ca7", 19, 23, True),
            ("Ca7", 33, 37, True),
            ("Ca8", 3, 7, True),
            ("Ca8", 15, 19, True),
            ("Ca8", 29, 33, True),
        )),
    (("041", "378", "041", "670"), 4, 6, False, True, (
            ("Ca7", 7, 11, True),
            ("Ca7", 20, 24, True),
            ("Ca7", 34, 38, True),
            ("Ca8", 4, 8, True),
            ("Ca8", 16, 20, True),
            ("Ca8", 30, 34, True),
        )),
    (("378", "041", "670", "008"), 4, 6, False, True, (
            ("Ca7", 8, 12, True),
            ("Ca7", 21, 25, True),
            ("Ca7", 35, 39, True),
            ("Ca8", 5, 9, True),
            ("Ca8", 17, 21, True),
            ("Ca8", 31, 35, True),
        )),
    (("040", "040", "040", "040"), 4, 5, False, False, (
            ("Ca7", 0, 4, False),
            ("Ca7", 1, 5, False),
            ("Ca7", 2, 6, False),
            ("Ca8", 24, 28, False),
            ("Ca8", 25, 29, False),
        )),
    (("040", "390", "041", "378"), 4, 5, False, True, (
            ("Ca7", 5, 9, True),
            ("Ca7", 18, 22, True),
            ("Ca8", 2, 6, True),
            ("Ca8", 14, 18, True),
            ("Ca8", 28, 32, True),
        )),
    (("008", "078", "711", "040"), 4, 4, False, True, (
            ("Ca6", 5, 9, False),
            ("Ca7", 11, 15, True),
            ("Ca7", 38, 42, True),
            ("Ca8", 8, 12, True),
        )),
    (("040", "040", "040", "390"), 4, 3, False, True, (
            ("Ca7", 3, 7, True),
            ("Ca8", 0, 4, True),
            ("Ca8", 26, 30, True),
        )),
    (("040", "040", "390", "041"), 4, 3, False, True, (
            ("Ca7", 4, 8, True),
            ("Ca8", 1, 5, True),
            ("Ca8", 27, 31, True),
        )),
    (("078", "711", "040", "040"), 4, 2, False, True, (
            ("Ca7", 39, 43, True),
            ("Ca8", 9, 13, True),
        )),
    (("041", "670", "008", "078", "711"), 5, 7, False, True, (
            ("Ca6", 3, 8, False),
            ("Ca7", 9, 14, True),
            ("Ca7", 22, 27, True),
            ("Ca7", 36, 41, True),
            ("Ca8", 6, 11, True),
            ("Ca8", 18, 23, True),
            ("Ca8", 32, 37, True),
        )),
    (("390", "041", "378", "041", "670"), 5, 6, False, True, (
            ("Ca7", 6, 11, True),
            ("Ca7", 19, 24, True),
            ("Ca7", 33, 38, True),
            ("Ca8", 3, 8, True),
            ("Ca8", 15, 20, True),
            ("Ca8", 29, 34, True),
        )),
    (("041", "378", "041", "670", "008"), 5, 6, False, True, (
            ("Ca7", 7, 12, True),
            ("Ca7", 20, 25, True),
            ("Ca7", 34, 39, True),
            ("Ca8", 4, 9, True),
            ("Ca8", 16, 21, True),
            ("Ca8", 30, 35, True),
        )),
    (("378", "041", "670", "008", "078"), 5, 6, False, True, (
            ("Ca7", 8, 13, True),
            ("Ca7", 21, 26, True),
            ("Ca7", 35, 40, True),
            ("Ca8", 5, 10, True),
            ("Ca8", 17, 22, True),
            ("Ca8", 31, 36, True),
        )),
    (("040", "390", "041", "378", "041"), 5, 5, False, True, (
            ("Ca7", 5, 10, True),
            ("Ca7", 18, 23, True),
            ("Ca8", 2, 7, True),
            ("Ca8", 14, 19, True),
            ("Ca8", 28, 33, True),
        )),
    (("670", "008", "078", "711", "040"), 5, 4, False, True, (
            ("Ca6", 4, 9, False),
            ("Ca7", 10, 15, True),
            ("Ca7", 37, 42, True),
            ("Ca8", 7, 12, True),
        )),
    (("040", "040", "040", "040", "040"), 5, 3, False, False, (
            ("Ca7", 0, 5, False),
            ("Ca7", 1, 6, False),
            ("Ca8", 24, 29, False),
        )),
    (("040", "040", "040", "390", "041"), 5, 3, False, True, (
            ("Ca7", 3, 8, True),
            ("Ca8", 0, 5, True),
            ("Ca8", 26, 31, True),
        )),
    (("040", "040", "390", "041", "378"), 5, 3, False, True, (
            ("Ca7", 4, 9, True),
            ("Ca8", 1, 6, True),
            ("Ca8", 27, 32, True),
        )),
    (("040", "040", "040", "040", "390"), 5, 2, False, True, (
            ("Ca7", 2, 7, True),
            ("Ca8", 25, 30, True),
        )),
    (("008", "078", "711", "040", "040"), 5, 2, False, True, (
            ("Ca7", 38, 43, True),
            ("Ca8", 8, 13, True),
        )),
    (("390", "041", "378", "041", "670", "008"), 6, 6, False, True, (
            ("Ca7", 6, 12, True),
            ("Ca7", 19, 25, True),
            ("Ca7", 33, 39, True),
            ("Ca8", 3, 9, True),
            ("Ca8", 15, 21, True),
            ("Ca8", 29, 35, True),
        )),
    (("041", "378", "041", "670", "008", "078"), 6, 6, False, True, (
            ("Ca7", 7, 13, True),
            ("Ca7", 20, 26, True),
            ("Ca7", 34, 40, True),
            ("Ca8", 4, 10, True),
            ("Ca8", 16, 22, True),
            ("Ca8", 30, 36, True),
        )),
    (("378", "041", "670", "008", "078", "711"), 6, 6, False, True, (
            ("Ca7", 8, 14, True),
            ("Ca7", 21, 27, True),
            ("Ca7", 35, 41, True),
            ("Ca8", 5, 11, True),
            ("Ca8", 17, 23, True),
            ("Ca8", 31, 37, True),
        )),
    (("040", "390", "041", "378", "041", "670"), 6, 5, False, True, (
            ("Ca7", 5, 11, True),
            ("Ca7", 18, 24, True),
            ("Ca8", 2, 8, True),
            ("Ca8", 14, 20, True),
            ("Ca8", 28, 34, True),
        )),
    (("041", "670", "008", "078", "711", "040"), 6, 4, False, True, (
            ("Ca6", 3, 9, False),
            ("Ca7", 9, 15, True),
            ("Ca7", 36, 42, True),
            ("Ca8", 6, 12, True),
        )),
    (("040", "040", "040", "390", "041", "378"), 6, 3, False, True, (
            ("Ca7", 3, 9, True),
            ("Ca8", 0, 6, True),
            ("Ca8", 26, 32, True),
        )),
    (("040", "040", "390", "041", "378", "041"), 6, 3, False, True, (
            ("Ca7", 4, 10, True),
            ("Ca8", 1, 7, True),
            ("Ca8", 27, 33, True),
        )),
    (("040", "040", "040", "040", "040", "390"), 6, 2, False, True, (
            ("Ca7", 1, 7, True),
            ("Ca8", 24, 30, True),
        )),
    (("040", "040", "040", "040", "390", "041"), 6, 2, False, True, (
            ("Ca7", 2, 8, True),
            ("Ca8", 25, 31, True),
        )),
    (("670", "008", "078", "711", "040", "040"), 6, 2, False, True, (
            ("Ca7", 37, 43, True),
            ("Ca8", 7, 13, True),
        )),
    (("390", "041", "378", "041", "670", "008", "078"), 7, 6, False, True, (
            ("Ca7", 6, 13, True),
            ("Ca7", 19, 26, True),
            ("Ca7", 33, 40, True),
            ("Ca8", 3, 10, True),
            ("Ca8", 15, 22, True),
            ("Ca8", 29, 36, True),
        )),
    (("041", "378", "041", "670", "008", "078", "711"), 7, 6, False, True, (
            ("Ca7", 7, 14, True),
            ("Ca7", 20, 27, True),
            ("Ca7", 34, 41, True),
            ("Ca8", 4, 11, True),
            ("Ca8", 16, 23, True),
            ("Ca8", 30, 37, True),
        )),
    (("040", "390", "041", "378", "041", "670", "008"), 7, 5, False, True, (
            ("Ca7", 5, 12, True),
            ("Ca7", 18, 25, True),
            ("Ca8", 2, 9, True),
            ("Ca8", 14, 21, True),
            ("Ca8", 28, 35, True),
        )),
    (("040", "040", "040", "390", "041", "378", "041"), 7, 3, False, True, (
            ("Ca7", 3, 10, True),
            ("Ca8", 0, 7, True),
            ("Ca8", 26, 33, True),
        )),
    (("040", "040", "390", "041", "378", "041", "670"), 7, 3, False, True, (
            ("Ca7", 4, 11, True),
            ("Ca8", 1, 8, True),
            ("Ca8", 27, 34, True),
        )),
    (("378", "041", "670", "008", "078", "711", "040"), 7, 3, False, True, (
            ("Ca7", 8, 15, True),
            ("Ca7", 35, 42, True),
            ("Ca8", 5, 12, True),
        )),
    (("040", "040", "040", "040", "040", "390", "041"), 7, 2, False, True, (
            ("Ca7", 1, 8, True),
            ("Ca8", 24, 31, True),
        )),
    (("040", "040", "040", "040", "390", "041", "378"), 7, 2, False, True, (
            ("Ca7", 2, 9, True),
            ("Ca8", 25, 32, True),
        )),
    (("041", "670", "008", "078", "711", "040", "040"), 7, 2, False, True, (
            ("Ca7", 36, 43, True),
            ("Ca8", 6, 13, True),
        )),
    (("390", "041", "378", "041", "670", "008", "078", "711"), 8, 6, True, True, (
            ("Ca7", 6, 14, True),
            ("Ca7", 19, 27, True),
            ("Ca7", 33, 41, True),
            ("Ca8", 3, 11, True),
            ("Ca8", 15, 23, True),
            ("Ca8", 29, 37, True),
        )),
    (("040", "390", "041", "378", "041", "670", "008", "078"), 8, 5, False, True, (
            ("Ca7", 5, 13, True),
            ("Ca7", 18, 26, True),
            ("Ca8", 2, 10, True),
            ("Ca8", 14, 22, True),
            ("Ca8", 28, 36, True),
        )),
    (("040", "040", "040", "390", "041", "378", "041", "670"), 8, 3, False, True, (
            ("Ca7", 3, 11, True),
            ("Ca8", 0, 8, True),
            ("Ca8", 26, 34, True),
        )),
    (("040", "040", "390", "041", "378", "041", "670", "008"), 8, 3, False, True, (
            ("Ca7", 4, 12, True),
            ("Ca8", 1, 9, True),
            ("Ca8", 27, 35, True),
        )),
    (("041", "378", "041", "670", "008", "078", "711", "040"), 8, 3, False, True, (
            ("Ca7", 7, 15, True),
            ("Ca7", 34, 42, True),
            ("Ca8", 4, 12, True),
        )),
    (("040", "040", "040", "040", "040", "390", "041", "378"), 8, 2, False, True, (
            ("Ca7", 1, 9, True),
            ("Ca8", 24, 32, True),
        )),
    (("040", "040", "040", "040", "390", "041", "378", "041"), 8, 2, False, True, (
            ("Ca7", 2, 10, True),
            ("Ca8", 25, 33, True),
        )),
    (("378", "041", "670", "008", "078", "711", "040", "040"), 8, 2, False, True, (
            ("Ca7", 35, 43, True),
            ("Ca8", 5, 13, True),
        )),
    (("040", "390", "041", "378", "041", "670", "008", "078", "711"), 9, 5, False, True, (
            ("Ca7", 5, 14, True),
            ("Ca7", 18, 27, True),
            ("Ca8", 2, 11, True),
            ("Ca8", 14, 23, True),
            ("Ca8", 28, 37, True),
        )),
    (("040", "040", "040", "390", "041", "378", "041", "670", "008"), 9, 3, False, True, (
            ("Ca7", 3, 12, True),
            ("Ca8", 0, 9, True),
            ("Ca8", 26, 35, True),
        )),
    (("040", "040", "390", "041", "378", "041", "670", "008", "078"), 9, 3, False, True, (
            ("Ca7", 4, 13, True),
            ("Ca8", 1, 10, True),
            ("Ca8", 27, 36, True),
        )),
    (("390", "041", "378", "041", "670", "008", "078", "711", "040"), 9, 3, False, True, (
            ("Ca7", 6, 15, True),
            ("Ca7", 33, 42, True),
            ("Ca8", 3, 12, True),
        )),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041"), 9, 2, False, True, (
            ("Ca7", 1, 10, True),
            ("Ca8", 24, 33, True),
        )),
    (("040", "040", "040", "040", "390", "041", "378", "041", "670"), 9, 2, False, True, (
            ("Ca7", 2, 11, True),
            ("Ca8", 25, 34, True),
        )),
    (("041", "378", "041", "670", "008", "078", "711", "040", "040"), 9, 2, False, True, (
            ("Ca7", 34, 43, True),
            ("Ca8", 4, 13, True),
        )),
    (("040", "040", "040", "390", "041", "378", "041", "670", "008", "078"), 10, 3, False, True, (
            ("Ca7", 3, 13, True),
            ("Ca8", 0, 10, True),
            ("Ca8", 26, 36, True),
        )),
    (("040", "040", "390", "041", "378", "041", "670", "008", "078", "711"), 10, 3, False, True, (
            ("Ca7", 4, 14, True),
            ("Ca8", 1, 11, True),
            ("Ca8", 27, 37, True),
        )),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041", "670"), 10, 2, False, True, (
            ("Ca7", 1, 11, True),
            ("Ca8", 24, 34, True),
        )),
    (("040", "040", "040", "040", "390", "041", "378", "041", "670", "008"), 10, 2, False, True, (
            ("Ca7", 2, 12, True),
            ("Ca8", 25, 35, True),
        )),
    (("040", "390", "041", "378", "041", "670", "008", "078", "711", "040"), 10, 2, False, True, (
            ("Ca7", 5, 15, True),
            ("Ca8", 2, 12, True),
        )),
    (("390", "041", "378", "041", "670", "008", "078", "711", "040", "040"), 10, 2, False, True, (
            ("Ca7", 33, 43, True),
            ("Ca8", 3, 13, True),
        )),
    (("040", "040", "040", "390", "041", "378", "041", "670", "008", "078", "711"), 11, 3, False, True, (
            ("Ca7", 3, 14, True),
            ("Ca8", 0, 11, True),
            ("Ca8", 26, 37, True),
        )),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041", "670", "008"), 11, 2, False, True, (
            ("Ca7", 1, 12, True),
            ("Ca8", 24, 35, True),
        )),
    (("040", "040", "040", "040", "390", "041", "378", "041", "670", "008", "078"), 11, 2, False, True, (
            ("Ca7", 2, 13, True),
            ("Ca8", 25, 36, True),
        )),
    (("040", "040", "390", "041", "378", "041", "670", "008", "078", "711", "040"), 11, 2, False, True, (
            ("Ca7", 4, 15, True),
            ("Ca8", 1, 12, True),
        )),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041", "670", "008", "078"), 12, 2, False, True, (
            ("Ca7", 1, 13, True),
            ("Ca8", 24, 36, True),
        )),
    (("040", "040", "040", "040", "390", "041", "378", "041", "670", "008", "078", "711"), 12, 2, False, True, (
            ("Ca7", 2, 14, True),
            ("Ca8", 25, 37, True),
        )),
    (("040", "040", "040", "390", "041", "378", "041", "670", "008", "078", "711", "040"), 12, 2, False, True, (
            ("Ca7", 3, 15, True),
            ("Ca8", 0, 12, True),
        )),
    (("040", "040", "040", "040", "040", "390", "041", "378", "041", "670", "008", "078", "711"), 13, 2, False, True, (
            ("Ca7", 1, 14, True),
            ("Ca8", 24, 37, True),
        )),
)


@dataclass(frozen=True)
class RepeatingNgramRow:
    """One published n-gram with freq ≥2. Stems only; no meanings."""

    tokens: tuple[str, ...]
    n: int
    freq: int
    is_delimiter: bool
    overlaps_delimiter_window: bool
    spans: tuple[tuple[str, int, int, bool], ...]


@dataclass(frozen=True)
class RepeatingNgramProfile:
    """Full n≥4 freq≥2 snapshot on the published Ca6–Ca9 fixture."""

    rows: tuple[RepeatingNgramRow, ...]
    longest_n: int
    longest: tuple[RepeatingNgramRow, ...]
    eightgrams: tuple[RepeatingNgramRow, ...]
    top_8gram: RepeatingNgramRow | None


def profile_tuple(row: RepeatingNgramRow) -> tuple:
    """Stable lock row: tokens, n, freq, delimiter flag, overlap, spans."""
    return (
        row.tokens,
        row.n,
        row.freq,
        row.is_delimiter,
        row.overlaps_delimiter_window,
        row.spans,
    )


def ngram_spans(
    lines: list[list[str]],
    gram: tuple[str, ...],
    published_spans: list[tuple[int, int, int]],
    line_names: tuple[str, ...] = LINE_NAMES,
) -> tuple[tuple[str, int, int, bool], ...]:
    """(line, start, end, overlaps) for every occurrence of gram."""
    n = len(gram)
    rows: list[tuple[str, int, int, bool]] = []
    for line_index, start in find_ngram_hits(lines, gram):
        end = start + n
        rows.append(
            (
                line_names[line_index],
                start,
                end,
                hit_overlaps_delimiter_span(line_index, start, end, published_spans),
            )
        )
    return tuple(rows)


def repeating_ngram_rows(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
    min_n: int = PROFILE_MIN_N,
    min_freq: int = PROFILE_MIN_FREQ,
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    line_names: tuple[str, ...] = LINE_NAMES,
) -> tuple[RepeatingNgramRow, ...]:
    """All distinct n-grams with n≥min_n and freq≥min_freq. Per line."""
    published_spans = delimiter_spans(lines, motif)
    max_n = max((len(seq) for seq in lines), default=0)
    rows: list[RepeatingNgramRow] = []
    for n in range(min_n, max_n + 1):
        for gram, freq in analyzer.extract_ngrams(lines, n=n, min_frequency=min_freq):
            spans = ngram_spans(lines, gram, published_spans, line_names)
            rows.append(
                RepeatingNgramRow(
                    tokens=gram,
                    n=n,
                    freq=freq,
                    is_delimiter=gram == motif,
                    overlaps_delimiter_window=any(span[-1] for span in spans),
                    spans=spans,
                )
            )
    return tuple(rows)


def score_repeating_ngram_profile(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
    min_n: int = PROFILE_MIN_N,
    min_freq: int = PROFILE_MIN_FREQ,
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    line_names: tuple[str, ...] = LINE_NAMES,
) -> RepeatingNgramProfile:
    """Build the n≥4 freq≥2 profile. Search only; no type map."""
    rows = repeating_ngram_rows(
        lines, analyzer, min_n=min_n, min_freq=min_freq, motif=motif, line_names=line_names
    )
    longest_n = max((row.n for row in rows), default=0)
    eightgrams = tuple(row for row in rows if row.n == 8)
    return RepeatingNgramProfile(
        rows=rows,
        longest_n=longest_n,
        longest=tuple(row for row in rows if row.n == longest_n),
        eightgrams=eightgrams,
        top_8gram=eightgrams[0] if eightgrams else None,
    )


class TestRepeatingNgramProfileHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_min_n_and_min_freq_filter(self):
        """n=3 repeats and hapax 4-grams are outside the lock."""
        gram4 = ("A", "B", "C", "D")
        lines = [list(gram4) + ["X"], ["Y"] + list(gram4)]
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        profile = score_repeating_ngram_profile(
            lines, analyzer, motif=("Z",) * 8, line_names=("L0", "L1")
        )
        self.assertEqual(profile.longest_n, 4)
        self.assertEqual(len(profile.rows), 1)
        self.assertEqual(profile.rows[0].tokens, gram4)
        self.assertEqual(profile.rows[0].freq, 2)
        self.assertEqual(
            profile.rows[0].spans,
            (("L0", 0, 4, False), ("L1", 1, 5, False)),
        )
        self.assertFalse(profile.rows[0].is_delimiter)
        self.assertFalse(profile.rows[0].overlaps_delimiter_window)
        self.assertIsNone(profile.top_8gram)
        self.assertEqual(provider.get_call_history(), [])

    def test_delimiter_row_and_overlap_on_window_only(self):
        """Exact motif is the delimiter; a side 4-gram overlaps that window."""
        motif = DELIMITER_MOTIF
        extra = ("Q", "R", "S", "T")
        lines = [list(motif) + ["040"], ["X"] + list(motif), list(extra) + list(extra)]
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        profile = score_repeating_ngram_profile(
            lines, analyzer, line_names=("Ca6", "Ca7", "Ca8")
        )
        by_tokens = {row.tokens: row for row in profile.rows}
        delim = by_tokens[motif]
        self.assertTrue(delim.is_delimiter)
        self.assertTrue(delim.overlaps_delimiter_window)
        self.assertEqual(delim.freq, 2)
        self.assertEqual(delim.n, 8)
        self.assertEqual(profile.top_8gram, delim)
        tail = motif[4:]
        self.assertIn(tail, by_tokens)
        self.assertFalse(by_tokens[tail].is_delimiter)
        self.assertTrue(by_tokens[tail].overlaps_delimiter_window)
        self.assertFalse(by_tokens[extra].overlaps_delimiter_window)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariRepeatingNgramProfileScoreboard(unittest.TestCase):
    """Published Ca6–Ca9 n≥4 freq≥2 lock. MockProvider only. No CV."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.fixture = load_mamari_fixture()
        self.lines = fixture_line_stems(self.fixture)
        self.profile = score_repeating_ngram_profile(self.lines, self.analyzer)

    def test_fixture_is_the_existing_published_passage(self):
        """Same cited fixture as the calendar scoreboard. No new numbers."""
        source = self.fixture["source"]
        self.assertIn("kohaumotu.org", source["primary"]["url"])
        self.assertEqual(tuple(self.fixture["lines"]), LINE_NAMES)
        self.assertEqual([len(line) for line in self.lines], [16, 43, 40, 2])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_profile_table_is_standing_truth(self):
        """Lock every n≥4 freq≥2 n-gram: tokens, n, freq, spans, flags."""
        p = self.profile
        locked = tuple(profile_tuple(row) for row in p.rows)
        self.assertEqual(len(locked), STANDING_REPEATING_NGRAM_COUNT)
        self.assertEqual(locked, STANDING_REPEATING_NGRAMS)
        for row in p.rows:
            self.assertGreaterEqual(row.n, PROFILE_MIN_N)
            self.assertGreaterEqual(row.freq, PROFILE_MIN_FREQ)
            self.assertEqual(row.n, len(row.tokens))
            self.assertEqual(row.freq, len(row.spans))
            self.assertEqual(row.is_delimiter, row.tokens == DELIMITER_MOTIF)
            self.assertEqual(row.overlaps_delimiter_window, any(span[-1] for span in row.spans))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_n_is_13(self):
        """Longest repeating n is five 040 + Guy's delimiter, freq 2."""
        p = self.profile
        self.assertEqual(p.longest_n, STANDING_LONGEST_N)
        self.assertEqual(len(p.longest), 1)
        longest = p.longest[0]
        self.assertEqual(longest.tokens, STANDING_LONGEST_NGRAM)
        self.assertEqual(longest.freq, STANDING_LONGEST_FREQ)
        self.assertFalse(longest.is_delimiter)
        self.assertTrue(longest.overlaps_delimiter_window)
        self.assertEqual(
            longest.spans,
            (("Ca7", 1, 14, True), ("Ca8", 24, 37, True)),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_top_8gram_is_guys_delimiter(self):
        """Highest-frequency 8-gram is still 390 041 378 041 670 008 078 711."""
        p = self.profile
        self.assertIsNotNone(p.top_8gram)
        top = p.top_8gram
        self.assertEqual(top.tokens, STANDING_TOP_8GRAM)
        self.assertEqual(top.tokens, DELIMITER_MOTIF)
        self.assertEqual(top.freq, STANDING_TOP_8GRAM_FREQ)
        self.assertTrue(top.is_delimiter)
        self.assertTrue(top.overlaps_delimiter_window)
        self.assertEqual(
            [row.tokens for row in p.eightgrams],
            [row[0] for row in STANDING_REPEATING_NGRAMS if row[1] == 8],
        )
        self.assertGreater(top.freq, p.eightgrams[1].freq)
        self.assertEqual(
            top.spans,
            (
                ("Ca7", 6, 14, True),
                ("Ca7", 19, 27, True),
                ("Ca7", 33, 41, True),
                ("Ca8", 3, 11, True),
                ("Ca8", 15, 23, True),
                ("Ca8", 29, 37, True),
            ),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ca6_variant_tail_is_not_a_guy_window(self):
        """315/375 first-delimiter tails share stems but are not Guy windows."""
        p = self.profile
        tail = next(row for row in p.rows if row.tokens == STANDING_CA6_VARIANT_TAIL)
        self.assertFalse(tail.is_delimiter)
        self.assertTrue(tail.overlaps_delimiter_window)
        ca6 = [span for span in tail.spans if span[0] == "Ca6"]
        self.assertEqual(ca6, [("Ca6", 3, 8, False)])
        self.assertTrue(any(span[-1] for span in tail.spans if span[0] != "Ca6"))
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariRepeatingNgramImageSnapshot(unittest.TestCase):
    """Cycle 24 does not touch clustering. 83/62 / Hamming 6 stays."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.image_lines = ca7_ca8_sequences(self.instances)
        self.published_lines = published_ca7_ca8_stems()

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. 83/62 / published Hamming 6 / 0/8."""
        published = self.published_lines
        window = score_delimiter_windows(self.instances, self.image_lines, published)
        published_ca7, published_ca8 = published_ca7_ca8_stem_counts()
        identity = score_type_identity(
            self.instances, self.analyzer, published_ca7, published_ca8
        )
        grams = tuple(w.image_ids for w in window.windows)
        self.assertEqual(window.instance_count, 83)
        self.assertEqual(window.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(identity.instance_count, sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(identity.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(identity.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(identity.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(min_pairwise_window_hamming(grams), STANDING_PUBLISHED_MIN_HAMMING)
        self.assertEqual(min_pairwise_window_hamming(grams), 6)
        self.assertEqual(window.slot_matches, STANDING_SLOT_MATCHES)
        unique_counts = tuple(len(set(ids)) for ids in window.slot_ids)
        self.assertEqual(unique_counts, STANDING_SLOT_UNIQUE_COUNTS)
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
