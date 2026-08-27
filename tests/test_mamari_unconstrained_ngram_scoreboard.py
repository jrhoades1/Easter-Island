"""Unconstrained n-gram search: full Ca7+Ca8, not published Guy windows.

Cycle 16 scored 8-grams only as delimiter-window slot identity (0/8).
Cycle 17 searches the standing G00n reading-order sequence itself:
the concatenated Ca7+Ca8 line, and each line separately.

No clustering change. No detector retune. No G00n→Barthel map.
MockProvider only. Search lock, not a merge.
input/tablets/sample_tablet.png is a synthetic CV dummy, not Mamari.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_calendar_scoreboard import DELIMITER_MOTIF
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
from tests.test_mamari_position_alignment_scoreboard import (
    LINE_NAMES,
    delimiter_spans,
    find_ngram_hits,
    hit_on_delimiter_span,
    published_ca7_ca8_stems,
)
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_MIXED_REPEATING,
    STANDING_UNIQUE_CLUSTERS,
    mixed_repeating_ngrams,
    published_ca7_ca8_stem_counts,
    score_type_identity,
)

UNCONSTRAINED_N = 8
# Both mixed 2-grams are longest. G007 G006 sits on the slot-0 390
# (partial overlap). G011 G013 sits inside two Ca8 delimiter spans.
STANDING_UNCONSTRAINED_8GRAMS = ()
STANDING_LONGEST_MIXED_N = 2
STANDING_LONGEST_MIXED = (
    (("G007", "G006"), 2),
    (("G011", "G013"), 2),
)
STANDING_LONGEST_MIXED_HITS = (
    ("Ca7", 32, 34, ("G007", "G006"), True),
    ("Ca8", 14, 16, ("G007", "G006"), True),
    ("Ca8", 4, 6, ("G011", "G013"), True),
    ("Ca8", 29, 31, ("G011", "G013"), True),
)


@dataclass(frozen=True)
class UnconstrainedNgramScore:
    """Full-sequence 8-gram / longest-mixed snapshot. No type map."""

    eightgrams_concat: tuple[tuple[tuple[str, ...], int], ...]
    eightgrams_ca7: tuple[tuple[tuple[str, ...], int], ...]
    eightgrams_ca8: tuple[tuple[tuple[str, ...], int], ...]
    eightgrams_lines: tuple[tuple[tuple[str, ...], int], ...]
    longest_mixed_n: int
    longest_mixed: tuple[tuple[tuple[str, ...], int], ...]
    longest_mixed_hits: tuple[tuple, ...]
    longest_mixed_overlaps_delimiter: bool
    instance_count: int
    unique_cluster_count: int
    window_matches: int


def concatenated_ca7_ca8(lines: list[list[str]]) -> list[list[str]]:
    """One reading-order sequence: Ca7 then Ca8."""
    if len(lines) < 2:
        return [list(lines[0])] if lines else [[]]
    return [list(lines[0]) + list(lines[1])]


def search_scopes(lines: list[list[str]]) -> dict[str, list[list[str]]]:
    """Concatenated Ca7+Ca8, each line, and the two-line pair."""
    ca7 = [list(lines[0])] if lines else [[]]
    ca8 = [list(lines[1])] if len(lines) > 1 else [[]]
    return {
        "concat": concatenated_ca7_ca8(lines),
        "ca7": ca7,
        "ca8": ca8,
        "lines": lines,
    }


def extract_repeating_8grams(
    sequences: list[list[str]], analyzer: NgramAnalyzer
) -> tuple[tuple[tuple[str, ...], int], ...]:
    """8-grams with freq ≥2. Empty if none."""
    return tuple(analyzer.extract_ngrams(sequences, n=UNCONSTRAINED_N, min_frequency=2))


def unconstrained_max_n(sequences: list[list[str]]) -> int:
    """Largest n the analyzer can slide on these sequences."""
    return max((len(seq) for seq in sequences), default=0)


def longest_mixed_repeating(
    sequences: list[list[str]], analyzer: NgramAnalyzer
) -> tuple[int, tuple[tuple[tuple[str, ...], int], ...]]:
    """Longest mixed n-grams with freq ≥2. n=0 and empty if none."""
    max_n = unconstrained_max_n(sequences)
    found = mixed_repeating_ngrams(sequences, analyzer, max_n=max_n)
    if not found:
        return 0, ()
    longest = max(len(gram) for gram, _freq in found)
    return longest, tuple((gram, freq) for gram, freq in found if len(gram) == longest)


def longest_mixed_anywhere(
    lines: list[list[str]], analyzer: NgramAnalyzer
) -> tuple[int, tuple[tuple[tuple[str, ...], int], ...]]:
    """Longest mixed n with freq ≥2 on concat or either line."""
    best_n = 0
    grams: dict[tuple[str, ...], int] = {}
    for sequences in search_scopes(lines).values():
        n, found = longest_mixed_repeating(sequences, analyzer)
        if n > best_n:
            best_n = n
            grams = {gram: freq for gram, freq in found}
        elif n == best_n:
            for gram, freq in found:
                grams[gram] = max(grams.get(gram, 0), freq)
    return best_n, tuple(sorted(grams.items(), key=lambda item: item[0]))


def hit_overlaps_delimiter_span(
    line_index: int,
    start: int,
    end: int,
    spans: list[tuple[int, int, int]],
) -> bool:
    """True if [start, end) shares any index with a delimiter span on that line."""
    return any(
        span_line == line_index and start < span_end and end > span_start
        for span_line, span_start, span_end in spans
    )


def longest_mixed_hit_rows(
    lines: list[list[str]],
    grams: tuple[tuple[tuple[str, ...], int], ...],
    spans: list[tuple[int, int, int]],
) -> tuple[tuple, ...]:
    """(line, start, end, gram, overlaps) for each longest-mixed occurrence."""
    rows: list[tuple] = []
    for gram, _freq in grams:
        n = len(gram)
        for line_index, start in find_ngram_hits(lines, gram):
            end = start + n
            rows.append(
                (
                    LINE_NAMES[line_index],
                    start,
                    end,
                    gram,
                    hit_overlaps_delimiter_span(line_index, start, end, spans),
                )
            )
    return tuple(rows)


def score_unconstrained_ngrams(
    instances,
    image_lines: list[list[str]],
    published_lines: list[list[str]],
    analyzer: NgramAnalyzer,
) -> UnconstrainedNgramScore:
    """Search lock: unconstrained 8-grams + longest mixed n anywhere."""
    scopes = search_scopes(image_lines)
    longest_n, longest = longest_mixed_anywhere(image_lines, analyzer)
    spans = delimiter_spans(published_lines, DELIMITER_MOTIF)
    hits = longest_mixed_hit_rows(image_lines, longest, spans)
    cluster_ids = [inst.cluster_id for inst in instances if inst.cluster_id]
    window = score_delimiter_windows(instances, image_lines, published_lines)
    return UnconstrainedNgramScore(
        eightgrams_concat=extract_repeating_8grams(scopes["concat"], analyzer),
        eightgrams_ca7=extract_repeating_8grams(scopes["ca7"], analyzer),
        eightgrams_ca8=extract_repeating_8grams(scopes["ca8"], analyzer),
        eightgrams_lines=extract_repeating_8grams(scopes["lines"], analyzer),
        longest_mixed_n=longest_n,
        longest_mixed=longest,
        longest_mixed_hits=hits,
        longest_mixed_overlaps_delimiter=any(row[-1] for row in hits),
        instance_count=len(cluster_ids),
        unique_cluster_count=len(set(cluster_ids)),
        window_matches=window.slot_matches,
    )


class TestUnconstrainedNgramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_concat_is_ca7_then_ca8(self):
        lines = [["A", "B"], ["C", "D", "E"]]
        self.assertEqual(concatenated_ca7_ca8(lines), [["A", "B", "C", "D", "E"]])
        scopes = search_scopes(lines)
        self.assertEqual(scopes["ca7"], [["A", "B"]])
        self.assertEqual(scopes["ca8"], [["C", "D", "E"]])
        self.assertEqual(scopes["lines"], lines)

    def test_line_local_8gram_misses_cross_line_repeat(self):
        """Same 8-gram once per line: concat/lines count 2; each line is none."""
        gram = tuple(f"T{i}" for i in range(8))
        lines = [list(gram) + ["X"], ["Y"] + list(gram)]
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        scopes = search_scopes(lines)
        self.assertEqual(
            extract_repeating_8grams(scopes["concat"], analyzer),
            ((gram, 2),),
        )
        self.assertEqual(extract_repeating_8grams(scopes["ca7"], analyzer), ())
        self.assertEqual(extract_repeating_8grams(scopes["ca8"], analyzer), ())
        self.assertEqual(
            extract_repeating_8grams(scopes["lines"], analyzer),
            ((gram, 2),),
        )
        self.assertEqual(provider.get_call_history(), [])

    def test_join_spanning_8gram_is_concat_only(self):
        """An 8-gram that crosses Ca7|Ca8 is invisible to per-line search."""
        join = ("A", "B", "C", "D", "E", "F", "G", "H")
        ca7 = ["X"] * 4 + list(join[:5])
        ca8 = list(join[5:]) + list(join) + ["Y"]
        lines = [ca7, ca8]
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        scopes = search_scopes(lines)
        self.assertEqual(
            extract_repeating_8grams(scopes["concat"], analyzer),
            ((join, 2),),
        )
        self.assertEqual(extract_repeating_8grams(scopes["ca7"], analyzer), ())
        self.assertEqual(extract_repeating_8grams(scopes["ca8"], analyzer), ())
        self.assertEqual(extract_repeating_8grams(scopes["lines"], analyzer), ())
        self.assertEqual(provider.get_call_history(), [])

    def test_overlap_is_not_fully_inside(self):
        spans = [(0, 6, 14), (1, 15, 23)]
        self.assertTrue(hit_overlaps_delimiter_span(0, 32, 34, [(0, 33, 41)]))
        self.assertFalse(hit_on_delimiter_span(0, 32, 34, [(0, 33, 41)]))
        self.assertTrue(hit_overlaps_delimiter_span(1, 14, 16, spans))
        self.assertFalse(hit_on_delimiter_span(1, 14, 16, spans))
        self.assertTrue(hit_overlaps_delimiter_span(1, 4, 6, [(1, 3, 11)]))
        self.assertTrue(hit_on_delimiter_span(1, 4, 6, [(1, 3, 11)]))
        self.assertFalse(hit_overlaps_delimiter_span(0, 0, 2, spans))

    def test_longest_mixed_anywhere_is_uncapped(self):
        """n>8 mixed repeats are visible when the search is not window-capped."""
        gram = ("P", "Q", "R", "S", "T", "U", "V", "W", "X")
        lines = [list(gram) + ["Z"], list(gram) + ["Y"]]
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        n, found = longest_mixed_anywhere(lines, analyzer)
        self.assertEqual(n, 9)
        self.assertEqual(found, ((gram, 2),))
        capped = mixed_repeating_ngrams(lines, analyzer, max_n=8)
        self.assertTrue(capped)
        self.assertEqual(max(len(g) for g, _freq in capped), 8)
        self.assertNotIn((gram, 2), capped)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariUnconstrainedNgramScoreboard(unittest.TestCase):
    """Stock CV → unconstrained 8-gram / longest-mixed lock. MockProvider only."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.image_lines = ca7_ca8_sequences(self.instances)
        self.published_lines = published_ca7_ca8_stems()
        self.score = score_unconstrained_ngrams(
            self.instances,
            self.image_lines,
            self.published_lines,
            self.ngram_analyzer,
        )

    def test_no_unconstrained_8gram(self):
        """No 8-gram of freq ≥2 on concat, Ca7, Ca8, or the two-line pair."""
        s = self.score
        self.assertEqual(s.eightgrams_concat, STANDING_UNCONSTRAINED_8GRAMS)
        self.assertEqual(s.eightgrams_ca7, STANDING_UNCONSTRAINED_8GRAMS)
        self.assertEqual(s.eightgrams_ca8, STANDING_UNCONSTRAINED_8GRAMS)
        self.assertEqual(s.eightgrams_lines, STANDING_UNCONSTRAINED_8GRAMS)
        self.assertEqual(s.eightgrams_concat, ())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_longest_mixed_n_anywhere(self):
        """Longest mixed n with freq ≥2 is 2: G007 G006 and G011 G013.

        Uncapped search on concat and on each line does not raise n.
        Both grams overlap a published delimiter span: G007 G006 on the
        slot-0 390 (not fully inside); G011 G013 fully inside two Ca8
        windows. Not a type map.
        """
        s = self.score
        self.assertEqual(s.longest_mixed_n, STANDING_LONGEST_MIXED_N)
        self.assertEqual(s.longest_mixed, STANDING_LONGEST_MIXED)
        self.assertEqual(s.longest_mixed_hits, STANDING_LONGEST_MIXED_HITS)
        self.assertTrue(s.longest_mixed_overlaps_delimiter)
        self.assertEqual(s.longest_mixed, STANDING_MIXED_REPEATING)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_standing_83_62_and_window_0_of_8(self):
        """Search lock does not change clustering. 83/62 / 0/8 stays."""
        s = self.score
        published_ca7, published_ca8 = published_ca7_ca8_stem_counts()
        identity = score_type_identity(
            self.instances,
            self.ngram_analyzer,
            published_ca7,
            published_ca8,
        )
        window = score_delimiter_windows(
            self.instances, self.image_lines, self.published_lines
        )
        self.assertEqual(s.instance_count, 83)
        self.assertEqual(s.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(s.window_matches, STANDING_SLOT_MATCHES)
        self.assertEqual(identity.instance_count, sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(identity.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(identity.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(identity.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(window.slot_matches, 0)
        unique_counts = tuple(len(set(ids)) for ids in window.slot_ids)
        self.assertEqual(unique_counts, STANDING_SLOT_UNIQUE_COUNTS)
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
