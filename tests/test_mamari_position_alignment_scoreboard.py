"""Position-alignment scoreboard: mixed G00n n-grams vs published Barthel stems.

No G00n→Barthel type map. Image Ca7/Ca8 lengths already match published
stem counts (43+40). Each mixed repeating n-gram hit is scored by the
published stems at the same reading-order indexes.

A published slice is a delimiter hit if it is a contiguous subsequence of
Guy's 8-stem delimiter. It is a ligature hit if it is a contiguous
subsequence of a published ligature encoding (390.041 or 008.078.711).
Glyph meanings are not assigned.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from models.glyphs import GlyphInstance
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    barthel_stems,
    load_mamari_fixture,
)
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_MIXED_REPEATING,
    STANDING_UNIQUE_CLUSTERS,
    mixed_repeating_ngrams,
)

LINE_NAMES = ("Ca7", "Ca8")
# Guy 390.41 / 8.78.711 as written in the Kohaumotu fixture.
KNOWN_LIGATURE_TOKENS = ("390.041", "008.078.711")

# (line, start, end, image_gram, published_stems, on_delimiter, in_delimiter, in_ligature)
STANDING_MIXED_HITS = (
    ("Ca7", 39, 41, ("G004", "G003"), ("078", "711"), True, True, True),
    ("Ca8", 8, 10, ("G004", "G003"), ("008", "078"), True, True, True),
    ("Ca8", 19, 21, ("G004", "G003"), ("670", "008"), True, True, False),
    ("Ca8", 7, 9, ("G009", "G004"), ("670", "008"), True, True, False),
    ("Ca8", 18, 20, ("G009", "G004"), ("041", "670"), True, True, False),
    ("Ca8", 7, 10, ("G009", "G004", "G003"), ("670", "008", "078"), True, True, False),
    ("Ca8", 18, 21, ("G009", "G004", "G003"), ("041", "670", "008"), True, True, False),
)
STANDING_DELIMITER_HITS = 7
STANDING_LIGATURE_HITS = 2
STANDING_HIT_TOTAL = 7


@dataclass(frozen=True)
class MixedNgramHit:
    """One mixed n-gram occurrence aligned to published stems by index."""

    line: str
    start: int
    end: int
    image_gram: tuple[str, ...]
    published_stems: tuple[str, ...]
    on_delimiter_span: bool
    in_delimiter: bool
    in_known_ligature: bool


@dataclass(frozen=True)
class PositionAlignmentScore:
    """Hit-rates for mixed n-grams vs delimiter / known ligature encodings."""

    hits: tuple[MixedNgramHit, ...]
    delimiter_hits: int
    ligature_hits: int
    hit_total: int
    instance_count: int
    unique_cluster_count: int
    ca7_length: int
    ca8_length: int


def published_ca7_ca8_stems() -> list[list[str]]:
    """Ca7/Ca8 Barthel stems from the published fixture. No remapping."""
    lines = load_mamari_fixture()["lines"]
    return [barthel_stems(lines["Ca7"]), barthel_stems(lines["Ca8"])]


def known_ligature_encodings() -> tuple[tuple[str, ...], ...]:
    """Mechanical stems of the published 390.041 and 008.078.711 ligatures."""
    return tuple(tuple(barthel_stems([token])) for token in KNOWN_LIGATURE_TOKENS)


def is_contiguous_subsequence(needle: tuple[str, ...], haystack: tuple[str, ...]) -> bool:
    """True if needle appears as consecutive tokens in haystack."""
    n = len(needle)
    if n == 0 or n > len(haystack):
        return False
    return any(haystack[i : i + n] == needle for i in range(len(haystack) - n + 1))


def find_ngram_hits(sequences: list[list[str]], gram: tuple[str, ...]) -> list[tuple[int, int]]:
    """(line_index, start) for every occurrence of gram, reading order."""
    n = len(gram)
    hits: list[tuple[int, int]] = []
    for line_index, sequence in enumerate(sequences):
        for start in range(len(sequence) - n + 1):
            if tuple(sequence[start : start + n]) == gram:
                hits.append((line_index, start))
    return hits


def delimiter_spans(
    published_lines: list[list[str]], motif: tuple[str, ...] = DELIMITER_MOTIF
) -> list[tuple[int, int, int]]:
    """(line_index, start, end) of each Guy delimiter occurrence."""
    n = len(motif)
    return [
        (line_index, start, start + n)
        for line_index, start in find_ngram_hits(published_lines, motif)
    ]


def hit_on_delimiter_span(
    line_index: int,
    start: int,
    end: int,
    spans: list[tuple[int, int, int]],
) -> bool:
    """True if [start, end) is fully inside a delimiter span on that line."""
    return any(
        span_line == line_index and span_start <= start and end <= span_end
        for span_line, span_start, span_end in spans
    )


def score_mixed_ngram_alignment(
    image_lines: list[list[str]],
    published_lines: list[list[str]],
    grams: list[tuple[str, ...]],
    motif: tuple[str, ...] = DELIMITER_MOTIF,
    ligatures: tuple[tuple[str, ...], ...] | None = None,
) -> list[MixedNgramHit]:
    """Align mixed n-gram indexes to published stems. No type map."""
    if len(image_lines) != len(published_lines):
        raise ValueError("image and published line counts differ")
    for image, published in zip(image_lines, published_lines):
        if len(image) != len(published):
            raise ValueError("image and published stem lengths differ")

    ligatures = ligatures if ligatures is not None else known_ligature_encodings()
    spans = delimiter_spans(published_lines, motif)
    hits: list[MixedNgramHit] = []
    for gram in grams:
        n = len(gram)
        for line_index, start in find_ngram_hits(image_lines, gram):
            end = start + n
            published = tuple(published_lines[line_index][start:end])
            hits.append(
                MixedNgramHit(
                    line=LINE_NAMES[line_index],
                    start=start,
                    end=end,
                    image_gram=gram,
                    published_stems=published,
                    on_delimiter_span=hit_on_delimiter_span(
                        line_index, start, end, spans
                    ),
                    in_delimiter=is_contiguous_subsequence(published, motif),
                    in_known_ligature=any(
                        is_contiguous_subsequence(published, ligature)
                        for ligature in ligatures
                    ),
                )
            )
    return hits


def score_position_alignment(
    instances: list[GlyphInstance],
    image_lines: list[list[str]],
    published_lines: list[list[str]],
) -> PositionAlignmentScore:
    """Record mixed-n-gram alignment plus the standing 83/62 / 43+40 lock."""
    grams = [gram for gram, _freq in STANDING_MIXED_REPEATING]
    hits = score_mixed_ngram_alignment(image_lines, published_lines, grams)
    cluster_ids = [inst.cluster_id for inst in instances if inst.cluster_id]
    return PositionAlignmentScore(
        hits=tuple(hits),
        delimiter_hits=sum(1 for hit in hits if hit.in_delimiter),
        ligature_hits=sum(1 for hit in hits if hit.in_known_ligature),
        hit_total=len(hits),
        instance_count=len(cluster_ids),
        unique_cluster_count=len(set(cluster_ids)),
        ca7_length=len(image_lines[0]) if image_lines else 0,
        ca8_length=len(image_lines[1]) if len(image_lines) > 1 else 0,
    )


def hit_tuple(hit: MixedNgramHit) -> tuple:
    """Stable lock row for one mixed n-gram occurrence."""
    return (
        hit.line,
        hit.start,
        hit.end,
        hit.image_gram,
        hit.published_stems,
        hit.on_delimiter_span,
        hit.in_delimiter,
        hit.in_known_ligature,
    )


class TestPositionAlignmentHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_contiguous_subsequence_accepts_internal_slice(self):
        motif = DELIMITER_MOTIF
        self.assertTrue(is_contiguous_subsequence(("078", "711"), motif))
        self.assertTrue(is_contiguous_subsequence(("670", "008", "078"), motif))
        self.assertTrue(is_contiguous_subsequence(("390", "041"), motif))
        self.assertFalse(is_contiguous_subsequence(("041", "041"), motif))
        self.assertFalse(is_contiguous_subsequence(("670", "078"), motif))
        self.assertFalse(is_contiguous_subsequence(("008", "078", "711", "040"), motif))

    def test_known_ligatures_are_fixture_encodings(self):
        self.assertEqual(
            known_ligature_encodings(),
            (("390", "041"), ("008", "078", "711")),
        )
        self.assertTrue(is_contiguous_subsequence(("008", "078"), ("008", "078", "711")))
        self.assertFalse(is_contiguous_subsequence(("670", "008"), ("008", "078", "711")))
        self.assertFalse(is_contiguous_subsequence(("670", "008"), ("390", "041")))

    def test_find_ngram_hits_and_delimiter_spans(self):
        published = [
            ["390", "041", "378", "041", "670", "008", "078", "711", "040"],
            ["040", "390", "041", "378", "041", "670", "008", "078", "711"],
        ]
        self.assertEqual(
            find_ngram_hits(published, ("008", "078")),
            [(0, 5), (1, 6)],
        )
        self.assertEqual(
            delimiter_spans(published),
            [(0, 0, 8), (1, 1, 9)],
        )
        self.assertTrue(hit_on_delimiter_span(0, 5, 7, delimiter_spans(published)))
        self.assertFalse(hit_on_delimiter_span(0, 7, 9, delimiter_spans(published)))

    def test_score_aligns_indexes_without_type_map(self):
        image = [["G009", "G004", "G003", "X"], ["A", "G004", "G003"]]
        published = [["670", "008", "078", "040"], ["040", "078", "711"]]
        hits = score_mixed_ngram_alignment(
            image,
            published,
            [("G004", "G003"), ("G009", "G004", "G003")],
        )
        self.assertEqual(
            [hit_tuple(hit) for hit in hits],
            [
                ("Ca7", 1, 3, ("G004", "G003"), ("008", "078"), False, True, True),
                ("Ca8", 1, 3, ("G004", "G003"), ("078", "711"), False, True, True),
                ("Ca7", 0, 3, ("G009", "G004", "G003"), ("670", "008", "078"), False, True, False),
            ],
        )


class TestMamariPositionAlignmentScoreboard(unittest.TestCase):
    """Stock CV indexes → published Ca7/Ca8 stems. MockProvider only."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.image_lines = ca7_ca8_sequences(self.instances)
        self.published_lines = published_ca7_ca8_stems()
        self.score = score_position_alignment(
            self.instances, self.image_lines, self.published_lines
        )

    def test_standing_counts_unchanged(self):
        """Cycle 6 does not retune detection; 83/62 / 43+40 stays locked."""
        s = self.score
        self.assertEqual(s.instance_count, sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(s.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(s.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(s.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(len(self.published_lines[0]), STANDING_CA7_LEN)
        self.assertEqual(len(self.published_lines[1]), STANDING_CA8_LEN)
        self.assertEqual(s.ca7_length, len(self.published_lines[0]))
        self.assertEqual(s.ca8_length, len(self.published_lines[1]))
        self.assertEqual(
            mixed_repeating_ngrams(self.image_lines, self.ngram_analyzer),
            list(STANDING_MIXED_REPEATING),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_mixed_ngrams_align_to_published_stems(self):
        """Lock published stems under each mixed n-gram and the two hit-rates.

        Honest result: every hit sits on a delimiter span and its published
        slice is a delimiter subsequence (7/7). Only two G004 G003 hits are
        a known ligature encoding (078 711 and 008 078 ⊂ 8.78.711). The
        repeating 3-gram is 670 008 078 and 041 670 008 — delimiter-internal
        splitter offsets, not 390.041 / 008.078.711.
        """
        s = self.score
        self.assertEqual([hit_tuple(hit) for hit in s.hits], list(STANDING_MIXED_HITS))
        self.assertEqual(s.delimiter_hits, STANDING_DELIMITER_HITS)
        self.assertEqual(s.ligature_hits, STANDING_LIGATURE_HITS)
        self.assertEqual(s.hit_total, STANDING_HIT_TOTAL)
        self.assertEqual(s.delimiter_hits / s.hit_total, 1.0)
        self.assertEqual(s.ligature_hits / s.hit_total, 2 / 7)
        self.assertTrue(all(hit.on_delimiter_span for hit in s.hits))
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
