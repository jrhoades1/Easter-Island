"""Statistical analysis of a transliterated Rongorongo corpus.

This module is deliberately *descriptive*, not interpretive. It reports the
statistical structure of the script — sign frequencies, n-grams, repeated
sequences, positional tendencies — without claiming what any glyph *means*.
That restraint is the point: structural statistics are the part of
computational Rongorongo work that can be done honestly while the script
remains undeciphered.

All analysis operates on decomposed glyph codes (ligatures split into their
component glyphs) unless otherwise noted.
"""

import math
from collections import Counter
from dataclasses import dataclass, field

from models.corpus import LIGATURE_SEP, RongorongoCorpus


@dataclass
class FrequencyEntry:
    """One row of the sign-frequency table."""

    rank: int
    glyph: str
    count: int
    relative: float  # count / total glyph occurrences

    def to_dict(self) -> dict:
        return {
            "rank": self.rank,
            "glyph": self.glyph,
            "count": self.count,
            "relative": round(self.relative, 6),
        }


@dataclass
class RepeatedSequence:
    """A glyph sequence that recurs within the corpus (possible parallelism)."""

    sequence: list[str]
    length: int
    frequency: int
    lines: list[str]  # ids of lines where it occurs

    def to_dict(self) -> dict:
        return {
            "sequence": list(self.sequence),
            "length": self.length,
            "frequency": self.frequency,
            "lines": list(self.lines),
        }


@dataclass
class PositionalEntry:
    """How a single glyph distributes across line positions."""

    glyph: str
    count: int
    initial: float  # fraction of occurrences that are line-initial
    medial: float
    final: float

    def to_dict(self) -> dict:
        return {
            "glyph": self.glyph,
            "count": self.count,
            "initial": round(self.initial, 4),
            "medial": round(self.medial, 4),
            "final": round(self.final, 4),
        }


@dataclass
class CorpusStatisticsReport:
    """Full statistical profile of a corpus."""

    is_synthetic: bool
    tablet_count: int
    line_count: int
    total_tokens: int  # as-written tokens (ligatures counted once)
    total_glyphs: int  # component glyph occurrences (ligatures decomposed)
    unique_glyphs: int
    hapax_count: int  # glyphs occurring exactly once
    type_token_ratio: float
    ligature_token_count: int  # as-written tokens that are ligatures
    zipf_correlation: float  # corr of log(rank) vs log(freq); ~ -1 is Zipfian
    line_length: dict = field(default_factory=dict)  # min/max/mean/stdev
    frequency_table: list[FrequencyEntry] = field(default_factory=list)
    hapax_glyphs: list[str] = field(default_factory=list)
    ngrams: dict = field(default_factory=dict)  # n -> top (sequence, freq) pairs
    repeated_sequences: list[RepeatedSequence] = field(default_factory=list)
    positional: list[PositionalEntry] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "is_synthetic": self.is_synthetic,
            "tablet_count": self.tablet_count,
            "line_count": self.line_count,
            "total_tokens": self.total_tokens,
            "total_glyphs": self.total_glyphs,
            "unique_glyphs": self.unique_glyphs,
            "hapax_count": self.hapax_count,
            "type_token_ratio": round(self.type_token_ratio, 6),
            "ligature_token_count": self.ligature_token_count,
            "zipf_correlation": round(self.zipf_correlation, 4),
            "line_length": self.line_length,
            "frequency_table": [e.to_dict() for e in self.frequency_table],
            "hapax_glyphs": list(self.hapax_glyphs),
            "ngrams": {
                str(n): [[list(seq), freq] for seq, freq in items]
                for n, items in self.ngrams.items()
            },
            "repeated_sequences": [r.to_dict() for r in self.repeated_sequences],
            "positional": [p.to_dict() for p in self.positional],
        }


def _ngram_counts(sequences: list[list[str]], n: int) -> Counter:
    """Count n-grams across a list of sequences."""
    counts: Counter = Counter()
    for seq in sequences:
        for i in range(len(seq) - n + 1):
            counts[tuple(seq[i : i + n])] += 1
    return counts


def _zipf_correlation(counts: list[int]) -> float:
    """Pearson correlation between log(rank) and log(frequency).

    A value near -1.0 indicates a Zipf-like distribution, which natural-
    language texts (and genuine writing systems) tend to exhibit.
    """
    counts = [c for c in counts if c > 0]
    if len(counts) < 3:
        return 0.0
    counts = sorted(counts, reverse=True)
    xs = [math.log(rank) for rank in range(1, len(counts) + 1)]
    ys = [math.log(c) for c in counts]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx == 0 or vy == 0:
        return 0.0
    return cov / math.sqrt(vx * vy)


def _line_length_stats(lengths: list[int]) -> dict:
    """Min/max/mean/stdev of line lengths."""
    if not lengths:
        return {"min": 0, "max": 0, "mean": 0.0, "stdev": 0.0}
    n = len(lengths)
    mean = sum(lengths) / n
    variance = sum((x - mean) ** 2 for x in lengths) / n
    return {
        "min": min(lengths),
        "max": max(lengths),
        "mean": round(mean, 3),
        "stdev": round(math.sqrt(variance), 3),
    }


class CorpusStatistics:
    """Computes descriptive statistics for a :class:`RongorongoCorpus`."""

    def __init__(
        self,
        max_ngram: int = 5,
        min_ngram_frequency: int = 2,
        top_k: int = 25,
    ):
        """
        Args:
            max_ngram: Largest n-gram size to extract.
            min_ngram_frequency: Minimum count for an n-gram to be reported.
            top_k: Number of rows to keep in "top" tables (frequency,
                positional, repeated sequences).
        """
        self.max_ngram = max_ngram
        self.min_ngram_frequency = min_ngram_frequency
        self.top_k = top_k

    def frequency_table(self, glyphs: list[str]) -> list[FrequencyEntry]:
        """Rank-ordered sign-frequency table for every glyph in the corpus."""
        total = len(glyphs)
        counts = Counter(glyphs)
        table: list[FrequencyEntry] = []
        for rank, (glyph, count) in enumerate(
            counts.most_common(), start=1
        ):
            table.append(
                FrequencyEntry(
                    rank=rank,
                    glyph=glyph,
                    count=count,
                    relative=count / total if total else 0.0,
                )
            )
        return table

    def repeated_sequences(
        self, corpus: RongorongoCorpus
    ) -> list[RepeatedSequence]:
        """Find maximal glyph sequences that recur within the corpus.

        A sequence is *maximal* if no longer repeated sequence contains it at
        the same frequency — this avoids reporting every sub-fragment of a
        long repeat. Recurring sequences are candidate formulae or parallel
        passages (a hallmark of the Mamari calendar and chant-like texts).
        """
        glyph_lines = [
            (line.line_id, line.glyphs()) for line in corpus.lines()
        ]
        sequences = [glyphs for _, glyphs in glyph_lines]

        # Collect repeated n-grams from longest to shortest.
        repeats: dict[int, Counter] = {}
        for n in range(self.max_ngram, 1, -1):
            counts = _ngram_counts(sequences, n)
            repeats[n] = Counter(
                {seq: c for seq, c in counts.items() if c >= 2}
            )

        # Drop a shorter sequence if it is a sub-span of a longer repeat
        # that occurs at least as often (i.e. it carries no extra evidence).
        longer_spans: set[tuple] = set()
        results: list[RepeatedSequence] = []
        for n in range(self.max_ngram, 1, -1):
            for seq, count in repeats[n].most_common():
                subsumed = False
                for span in longer_spans:
                    if len(span) > n and _contains(span, seq):
                        subsumed = True
                        break
                if subsumed:
                    continue
                longer_spans.add(seq)
                lines_with = [
                    line_id
                    for line_id, glyphs in glyph_lines
                    if _contains(tuple(glyphs), seq)
                ]
                results.append(
                    RepeatedSequence(
                        sequence=list(seq),
                        length=n,
                        frequency=count,
                        lines=lines_with,
                    )
                )

        results.sort(key=lambda r: (r.length * r.frequency), reverse=True)
        return results[: self.top_k]

    def positional_distribution(
        self, corpus: RongorongoCorpus
    ) -> list[PositionalEntry]:
        """Per-glyph distribution across line-initial/medial/final positions."""
        initial: Counter = Counter()
        final: Counter = Counter()
        medial: Counter = Counter()
        totals: Counter = Counter()

        for seq in corpus.glyph_sequences():
            last = len(seq) - 1
            for i, glyph in enumerate(seq):
                totals[glyph] += 1
                if i == 0:
                    initial[glyph] += 1
                elif i == last:
                    final[glyph] += 1
                else:
                    medial[glyph] += 1

        entries: list[PositionalEntry] = []
        for glyph, count in totals.most_common(self.top_k):
            entries.append(
                PositionalEntry(
                    glyph=glyph,
                    count=count,
                    initial=initial[glyph] / count,
                    medial=medial[glyph] / count,
                    final=final[glyph] / count,
                )
            )
        return entries

    def analyze(self, corpus: RongorongoCorpus) -> CorpusStatisticsReport:
        """Produce a full statistical profile of the corpus."""
        glyphs = corpus.all_glyphs()
        lines = corpus.lines()
        glyph_sequences = corpus.glyph_sequences()

        freq_table = self.frequency_table(glyphs)
        hapax = [e.glyph for e in freq_table if e.count == 1]

        ngrams: dict[int, list] = {}
        for n in range(2, self.max_ngram + 1):
            counts = _ngram_counts(glyph_sequences, n)
            top = [
                (seq, c)
                for seq, c in counts.most_common()
                if c >= self.min_ngram_frequency
            ][: self.top_k]
            if top:
                ngrams[n] = top

        ligature_tokens = sum(
            1
            for line in lines
            for token in line.tokens
            if LIGATURE_SEP in token
        )

        return CorpusStatisticsReport(
            is_synthetic=corpus.has_synthetic,
            tablet_count=len(corpus.tablets),
            line_count=len(lines),
            total_tokens=sum(line.length for line in lines),
            total_glyphs=len(glyphs),
            unique_glyphs=len(freq_table),
            hapax_count=len(hapax),
            type_token_ratio=(len(freq_table) / len(glyphs)) if glyphs else 0.0,
            ligature_token_count=ligature_tokens,
            zipf_correlation=_zipf_correlation([e.count for e in freq_table]),
            line_length=_line_length_stats([line.length for line in lines]),
            frequency_table=freq_table[: self.top_k],
            hapax_glyphs=hapax,
            ngrams=ngrams,
            repeated_sequences=self.repeated_sequences(corpus),
            positional=self.positional_distribution(corpus),
        )


def _contains(haystack: tuple, needle: tuple) -> bool:
    """Return True if ``needle`` appears as a contiguous span of ``haystack``."""
    n, m = len(haystack), len(needle)
    if m > n:
        return False
    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return True
    return False
