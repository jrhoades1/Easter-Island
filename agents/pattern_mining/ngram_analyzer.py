"""N-gram analysis for glyph sequences."""

from collections import Counter
from dataclasses import dataclass
from typing import Optional

from ..base import LLMMessage, LLMProvider, LLMResponse


@dataclass
class NgramPattern:
    """A discovered n-gram pattern."""

    pattern_id: str
    sequence: list[str]  # List of glyph IDs
    n: int  # Length of the n-gram
    frequency: int
    probability: float  # P(sequence)
    positions: list[str]  # "line_initial", "line_medial", "line_final"
    tablets: list[str]  # Tablets where this pattern appears
    llm_hypothesis: Optional[str] = None


@dataclass
class NgramStatistics:
    """Statistics about n-gram patterns."""

    total_ngrams: dict[int, int]  # n -> count of unique n-grams
    hapax_legomena: dict[int, int]  # n -> count appearing only once
    most_frequent: dict[int, list[tuple[tuple[str, ...], int]]]


class NgramAnalyzer:
    """
    Analyzes n-gram patterns in glyph sequences.

    Identifies recurring sequences that may represent:
    - Formulaic phrases
    - Grammatical patterns
    - Semantic units
    """

    SYSTEM_PROMPT = """You are an expert in computational linguistics and script analysis,
specializing in pattern discovery in undeciphered writing systems.

For Rongorongo, recurring n-gram patterns may indicate:
- Formulaic openings or closings (like "In the name of...")
- Grammatical structures (subject-verb-object patterns)
- Numbering or counting sequences
- Names or titles
- Repeated liturgical or ritual phrases

When analyzing n-gram patterns, consider:
1. Position in text - line-initial patterns may be section markers
2. Frequency - high frequency suggests common words or particles
3. Co-occurrence - what patterns appear near each other
4. Length - longer patterns are more likely meaningful units

Provide hypotheses about what these patterns might represent,
while acknowledging the script is undeciphered."""

    def __init__(self, llm_provider: Optional[LLMProvider] = None):
        """
        Initialize the n-gram analyzer.

        Args:
            llm_provider: Optional LLM for pattern interpretation
        """
        self.llm = llm_provider

    def extract_ngrams(
        self,
        sequences: list[list[str]],
        n: int,
        min_frequency: int = 2,
    ) -> list[tuple[tuple[str, ...], int]]:
        """
        Extract n-grams from glyph sequences.

        Args:
            sequences: List of glyph ID sequences (one per line/tablet)
            n: N-gram size
            min_frequency: Minimum occurrences to include

        Returns:
            List of (n-gram tuple, frequency) pairs, sorted by frequency
        """
        ngram_counts: Counter[tuple[str, ...]] = Counter()

        for sequence in sequences:
            if len(sequence) >= n:
                for i in range(len(sequence) - n + 1):
                    ngram = tuple(sequence[i : i + n])
                    ngram_counts[ngram] += 1

        # Filter by minimum frequency
        filtered = [
            (ngram, count)
            for ngram, count in ngram_counts.items()
            if count >= min_frequency
        ]

        # Sort by frequency descending
        return sorted(filtered, key=lambda x: x[1], reverse=True)

    def analyze_positions(
        self,
        ngram: tuple[str, ...],
        sequences: list[list[str]],
    ) -> dict[str, float]:
        """
        Analyze where an n-gram tends to appear in sequences.

        Returns distribution across positions.
        """
        positions = {"line_initial": 0, "line_medial": 0, "line_final": 0}
        total = 0

        for sequence in sequences:
            n = len(ngram)
            for i in range(len(sequence) - n + 1):
                if tuple(sequence[i : i + n]) == ngram:
                    total += 1
                    if i == 0:
                        positions["line_initial"] += 1
                    elif i == len(sequence) - n:
                        positions["line_final"] += 1
                    else:
                        positions["line_medial"] += 1

        # Normalize
        if total > 0:
            positions = {k: v / total for k, v in positions.items()}

        return positions

    def find_patterns(
        self,
        glyph_sequences: list[dict],
        max_n: int = 5,
        min_frequency: int = 2,
    ) -> list[NgramPattern]:
        """
        Find significant n-gram patterns across all sizes.

        Args:
            glyph_sequences: List of {"sequence": [...], "source": "tablet_id"}
            max_n: Maximum n-gram size to consider
            min_frequency: Minimum frequency to include

        Returns:
            List of NgramPattern objects
        """
        patterns = []
        pattern_id = 0

        # Extract sequences
        sequences = [s["sequence"] for s in glyph_sequences]
        sources = [s.get("source", "unknown") for s in glyph_sequences]

        total_glyphs = sum(len(s) for s in sequences)

        for n in range(2, max_n + 1):
            ngrams = self.extract_ngrams(sequences, n, min_frequency)

            for ngram, frequency in ngrams:
                # Analyze position distribution
                position_dist = self.analyze_positions(ngram, sequences)
                dominant_positions = [
                    pos for pos, ratio in position_dist.items() if ratio > 0.3
                ]

                # Find which tablets contain this pattern
                tablets_with_pattern = set()
                for i, seq in enumerate(sequences):
                    for j in range(len(seq) - n + 1):
                        if tuple(seq[j : j + n]) == ngram:
                            tablets_with_pattern.add(sources[i])

                # Calculate probability
                probability = frequency / (total_glyphs - n + 1) if total_glyphs > n else 0

                pattern_id += 1
                patterns.append(
                    NgramPattern(
                        pattern_id=f"ngram_{pattern_id:03d}",
                        sequence=list(ngram),
                        n=n,
                        frequency=frequency,
                        probability=probability,
                        positions=dominant_positions or ["line_medial"],
                        tablets=sorted(tablets_with_pattern),
                    )
                )

        return patterns

    def interpret_patterns(
        self,
        patterns: list[NgramPattern],
        top_k: int = 10,
    ) -> list[NgramPattern]:
        """
        Use LLM to hypothesize meanings for top patterns.

        Args:
            patterns: Patterns to interpret
            top_k: Number of top patterns to analyze

        Returns:
            Patterns with llm_hypothesis filled in
        """
        if not self.llm:
            return patterns

        # Sort by significance (frequency * length)
        sorted_patterns = sorted(
            patterns,
            key=lambda p: p.frequency * p.n,
            reverse=True,
        )[:top_k]

        # Build prompt with pattern data
        pattern_desc = "\n".join(
            f"- {p.pattern_id}: {' → '.join(p.sequence)} "
            f"(freq: {p.frequency}, positions: {p.positions})"
            for p in sorted_patterns
        )

        user_prompt = f"""Analyze these recurring n-gram patterns from Rongorongo tablets:

{pattern_desc}

For each pattern, provide a hypothesis about what it might represent.
Consider the frequency, length, and positional tendencies.

Respond with JSON:
{{
    "interpretations": [
        {{
            "pattern_id": "ngram_001",
            "hypothesis": "your interpretation",
            "confidence": 0.0-1.0,
            "reasoning": "why you think this"
        }}
    ]
}}"""

        messages = [
            LLMMessage(role="system", content=self.SYSTEM_PROMPT),
            LLMMessage(role="user", content=user_prompt),
        ]

        response = self.llm.complete(messages, max_tokens=1500, temperature=0.2)

        # Parse and apply interpretations
        self._apply_interpretations(sorted_patterns, response)

        return patterns

    def _apply_interpretations(
        self, patterns: list[NgramPattern], response: LLMResponse
    ) -> None:
        """Apply LLM interpretations to patterns."""
        import json

        try:
            content = response.content.strip()
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1])

            data = json.loads(content)

            interpretation_map = {
                i["pattern_id"]: i["hypothesis"]
                for i in data.get("interpretations", [])
            }

            for pattern in patterns:
                if pattern.pattern_id in interpretation_map:
                    pattern.llm_hypothesis = interpretation_map[pattern.pattern_id]

        except (json.JSONDecodeError, KeyError):
            pass  # Leave hypotheses as None

    def get_statistics(
        self,
        sequences: list[list[str]],
        max_n: int = 5,
    ) -> NgramStatistics:
        """
        Calculate n-gram statistics.

        Args:
            sequences: Glyph sequences
            max_n: Maximum n to analyze

        Returns:
            NgramStatistics object
        """
        total_ngrams = {}
        hapax = {}
        most_frequent = {}

        for n in range(2, max_n + 1):
            ngrams = self.extract_ngrams(sequences, n, min_frequency=1)
            total_ngrams[n] = len(ngrams)
            hapax[n] = sum(1 for _, count in ngrams if count == 1)
            most_frequent[n] = ngrams[:5]  # Top 5

        return NgramStatistics(
            total_ngrams=total_ngrams,
            hapax_legomena=hapax,
            most_frequent=most_frequent,
        )
