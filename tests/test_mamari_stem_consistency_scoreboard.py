"""Stem-consistency scoreboard: G00n IDs vs published stems on mixed hits.

Cycle 6 locked seven delimiter-aligned mixed n-grams. The same G00n
3-gram sits on two different published stem triples:

    Ca8 [7:10]  G009 G004 G003 = 670 008 078
    Ca8 [18:21] G009 G004 G003 = 041 670 008

So G009 is 670 in one hit and 041 in the other. This cycle records that
inconsistency as standing truth. It is a positional alignment table, not
a G00n→Barthel dictionary and not a meaning assignment. No detector
retune. Glyph meanings are not assigned.
"""

import unittest
from collections import defaultdict
from dataclasses import dataclass

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_image_scoreboard import (
    TRACING_DIR,
    TRACING_NAMES,
    ca7_ca8_sequences,
    process_tracings,
)
from tests.test_mamari_neighbor_allograph_scoreboard import longest_mixed_repeating_n
from tests.test_mamari_position_alignment_scoreboard import (
    MixedNgramHit,
    STANDING_MIXED_HITS,
    hit_tuple,
    published_ca7_ca8_stems,
    score_position_alignment,
)
from tests.test_mamari_type_identity_scoreboard import (
    STANDING_CA7_LEN,
    STANDING_CA8_LEN,
    STANDING_INSTANCES_PER_STRIP,
    STANDING_MIXED_REPEATING,
    STANDING_UNIQUE_CLUSTERS,
    mixed_repeating_ngrams,
)

# Observed G00n → distinct published stems on the cycle-6 mixed hits.
# Sorted unique values. Not a type map.
STANDING_GLYPH_STEM_MULTIMAP = {
    "G003": ("008", "078", "711"),
    "G004": ("008", "078", "670"),
    "G009": ("041", "670"),
}
STANDING_INCONSISTENT_GLYPHS = ("G003", "G004", "G009")
STANDING_3GRAM_TRIPLES = (
    ("Ca8", 7, 10, ("G009", "G004", "G003"), ("670", "008", "078")),
    ("Ca8", 18, 21, ("G009", "G004", "G003"), ("041", "670", "008")),
)


@dataclass(frozen=True)
class StemAlignment:
    """One G00n token paired with the published stem at the same index."""

    glyph_id: str
    published_stem: str
    line: str
    index: int


@dataclass(frozen=True)
class StemConsistencyScore:
    """Multimap of G00n IDs to published stems on the mixed hits."""

    alignments: tuple[StemAlignment, ...]
    multimap: dict[str, tuple[str, ...]]
    inconsistent_glyphs: tuple[str, ...]
    triples: tuple[tuple, ...]
    instance_count: int
    unique_cluster_count: int
    ca7_length: int
    ca8_length: int


def alignments_from_hits(hits: tuple[MixedNgramHit, ...] | list[MixedNgramHit]) -> list[StemAlignment]:
    """Pair each G00n in a mixed hit with the published stem at that index."""
    seen: set[tuple[str, str, str, int]] = set()
    alignments: list[StemAlignment] = []
    for hit in hits:
        if len(hit.image_gram) != len(hit.published_stems):
            raise ValueError("image gram and published stems differ in length")
        for offset, (glyph_id, stem) in enumerate(zip(hit.image_gram, hit.published_stems)):
            index = hit.start + offset
            key = (glyph_id, stem, hit.line, index)
            if key in seen:
                continue
            seen.add(key)
            alignments.append(
                StemAlignment(
                    glyph_id=glyph_id,
                    published_stem=stem,
                    line=hit.line,
                    index=index,
                )
            )
    return alignments


def glyph_stem_multimap(alignments: list[StemAlignment]) -> dict[str, tuple[str, ...]]:
    """G00n ID → sorted unique published stems. Observation, not a dictionary."""
    stems: dict[str, set[str]] = defaultdict(set)
    for alignment in alignments:
        stems[alignment.glyph_id].add(alignment.published_stem)
    return {glyph_id: tuple(sorted(values)) for glyph_id, values in sorted(stems.items())}


def inconsistent_glyphs(multimap: dict[str, tuple[str, ...]]) -> tuple[str, ...]:
    """G00n IDs that align to more than one distinct published stem."""
    return tuple(
        glyph_id for glyph_id, stems in sorted(multimap.items()) if len(stems) > 1
    )


def hit_triples(hits: tuple[MixedNgramHit, ...] | list[MixedNgramHit]) -> tuple[tuple, ...]:
    """(line, start, end, image_gram, published_stems) for length-3 mixed hits."""
    return tuple(
        (hit.line, hit.start, hit.end, hit.image_gram, hit.published_stems)
        for hit in hits
        if len(hit.image_gram) == 3
    )


def score_stem_consistency(
    instances,
    image_lines: list[list[str]],
    published_lines: list[list[str]],
) -> StemConsistencyScore:
    """Build the cycle-6 mixed-hit multimap. No type map, no detector retune."""
    position = score_position_alignment(instances, image_lines, published_lines)
    alignments = alignments_from_hits(position.hits)
    multimap = glyph_stem_multimap(alignments)
    return StemConsistencyScore(
        alignments=tuple(alignments),
        multimap=multimap,
        inconsistent_glyphs=inconsistent_glyphs(multimap),
        triples=hit_triples(position.hits),
        instance_count=position.instance_count,
        unique_cluster_count=position.unique_cluster_count,
        ca7_length=position.ca7_length,
        ca8_length=position.ca8_length,
    )


def _synthetic_hit(line, start, end, image_gram, published_stems) -> MixedNgramHit:
    return MixedNgramHit(
        line=line,
        start=start,
        end=end,
        image_gram=image_gram,
        published_stems=published_stems,
        on_delimiter_span=True,
        in_delimiter=True,
        in_known_ligature=False,
    )


class TestStemConsistencyHelpers(unittest.TestCase):
    """Helpers on synthetic mixed hits. No CV, no LLM."""

    def test_multimap_records_inconsistent_g009(self):
        hits = (
            _synthetic_hit("Ca8", 7, 10, ("G009", "G004", "G003"), ("670", "008", "078")),
            _synthetic_hit("Ca8", 18, 21, ("G009", "G004", "G003"), ("041", "670", "008")),
        )
        alignments = alignments_from_hits(hits)
        multimap = glyph_stem_multimap(alignments)
        self.assertEqual(multimap["G009"], ("041", "670"))
        self.assertEqual(multimap["G004"], ("008", "670"))
        self.assertEqual(multimap["G003"], ("008", "078"))
        self.assertEqual(inconsistent_glyphs(multimap), ("G003", "G004", "G009"))
        self.assertEqual(hit_triples(hits), STANDING_3GRAM_TRIPLES)

    def test_consistent_glyph_is_not_flagged(self):
        hits = (
            _synthetic_hit("Ca7", 0, 2, ("G001", "G002"), ("390", "041")),
            _synthetic_hit("Ca8", 0, 2, ("G001", "G002"), ("390", "041")),
        )
        multimap = glyph_stem_multimap(alignments_from_hits(hits))
        self.assertEqual(multimap, {"G001": ("390",), "G002": ("041",)})
        self.assertEqual(inconsistent_glyphs(multimap), ())

    def test_duplicate_index_pairs_are_deduped(self):
        hits = (
            _synthetic_hit("Ca8", 7, 9, ("G009", "G004"), ("670", "008")),
            _synthetic_hit("Ca8", 7, 10, ("G009", "G004", "G003"), ("670", "008", "078")),
        )
        alignments = alignments_from_hits(hits)
        self.assertEqual(
            [(a.glyph_id, a.published_stem, a.index) for a in alignments],
            [("G009", "670", 7), ("G004", "008", 8), ("G003", "078", 9)],
        )


class TestMamariStemConsistencyScoreboard(unittest.TestCase):
    """Stock CV mixed hits → G00n/stem multimap. MockProvider only."""

    def setUp(self):
        self.paths = [TRACING_DIR / name for name in TRACING_NAMES]
        for path in self.paths:
            self.assertTrue(path.is_file(), f"missing vendored tracing {path.name}")
        self.provider = MockProvider()
        self.ngram_analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.instances = process_tracings(self.paths)
        self.image_lines = ca7_ca8_sequences(self.instances)
        self.published_lines = published_ca7_ca8_stems()
        self.score = score_stem_consistency(
            self.instances, self.image_lines, self.published_lines
        )

    def test_cycle8_snapshot_unchanged(self):
        """PR snapshot vs cycle 8: 83/62 / 43+40, mixed 3-gram, no 8-gram."""
        s = self.score
        self.assertEqual(s.instance_count, sum(STANDING_INSTANCES_PER_STRIP.values()))
        self.assertEqual(s.unique_cluster_count, STANDING_UNIQUE_CLUSTERS)
        self.assertEqual(s.ca7_length, STANDING_CA7_LEN)
        self.assertEqual(s.ca8_length, STANDING_CA8_LEN)
        self.assertEqual(
            mixed_repeating_ngrams(self.image_lines, self.ngram_analyzer),
            list(STANDING_MIXED_REPEATING),
        )
        self.assertEqual(
            longest_mixed_repeating_n(self.image_lines, self.ngram_analyzer), 3
        )
        eight = self.ngram_analyzer.extract_ngrams(
            self.image_lines, n=8, min_frequency=2
        )
        self.assertEqual(eight, [])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_standing_mixed_hits_and_triples_locked(self):
        """Cycle-6 lock rows and the two published 3-gram triples stay put."""
        position = score_position_alignment(
            self.instances, self.image_lines, self.published_lines
        )
        self.assertEqual([hit_tuple(hit) for hit in position.hits], list(STANDING_MIXED_HITS))
        self.assertEqual(self.score.triples, STANDING_3GRAM_TRIPLES)
        self.assertEqual(
            STANDING_3GRAM_TRIPLES[0][4],
            ("670", "008", "078"),
        )
        self.assertEqual(
            STANDING_3GRAM_TRIPLES[1][4],
            ("041", "670", "008"),
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def test_g00n_stem_inconsistency_is_standing_truth(self):
        """Fail if the mixed-hit G00n→stem inconsistency disappears.

        Today's observation: G009, G004, and G003 each align to more than
        one published Barthel stem. That is the lock. If a later pipeline
        change makes every G00n map to a single stem, update this table
        and document the change — do not silently drop the assertion.
        """
        s = self.score
        self.assertEqual(s.multimap, STANDING_GLYPH_STEM_MULTIMAP)
        self.assertEqual(s.inconsistent_glyphs, STANDING_INCONSISTENT_GLYPHS)
        self.assertGreater(len(s.inconsistent_glyphs), 0)
        self.assertGreater(max(len(stems) for stems in s.multimap.values()), 1)
        self.assertEqual(s.multimap["G009"], ("041", "670"))
        self.assertIn("670", s.multimap["G009"])
        self.assertIn("041", s.multimap["G009"])
        self.assertEqual(self.provider.get_call_history(), [])


if __name__ == "__main__":
    unittest.main()
