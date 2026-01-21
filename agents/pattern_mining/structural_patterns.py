"""Structural pattern analysis for glyph sequences."""

from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Optional

from ..base import LLMMessage, LLMProvider, LLMResponse


@dataclass
class StructuralPattern:
    """A structural pattern in glyph positioning."""

    pattern_id: str
    pattern_type: str  # "line_marker", "section_break", "repetition", "alternation"
    glyph_ids: list[str]
    frequency: int
    position_preference: dict[str, float]  # Position -> probability
    context: str  # Description of where/how it appears
    llm_interpretation: Optional[str] = None


@dataclass
class LineStructure:
    """Analysis of line-level structure."""

    avg_length: float
    length_variance: float
    common_starters: list[tuple[str, int]]  # (glyph_id, count)
    common_enders: list[tuple[str, int]]
    line_break_indicators: list[str]  # Glyphs that often precede breaks


class StructuralPatternAnalyzer:
    """
    Analyzes structural patterns in glyph arrangements.

    Identifies:
    - Line-initial and line-final markers
    - Section breaks and delimiters
    - Repetition patterns (AAB, ABAB, etc.)
    - Structural indicators
    """

    SYSTEM_PROMPT = """You are an expert in structural analysis of ancient scripts,
specializing in identifying organizational patterns in texts.

In Rongorongo and similar scripts, structural patterns may indicate:
- Section or paragraph markers
- Line delimiters or continuations
- Emphasis through repetition
- Grammatical structures (like case markers)
- Numerical or counting sequences

When analyzing structural patterns:
1. Look for positional tendencies (always at start/end)
2. Consider repetition types (exact, with variation, alternating)
3. Note spacing or visual separation cues
4. Compare with known text organization in oral traditions

Provide interpretations while acknowledging uncertainty."""

    def __init__(self, llm_provider: Optional[LLMProvider] = None):
        """
        Initialize the structural pattern analyzer.

        Args:
            llm_provider: Optional LLM for pattern interpretation
        """
        self.llm = llm_provider

    def analyze_line_positions(
        self,
        lines: list[list[str]],
    ) -> dict[str, dict[str, float]]:
        """
        Analyze position preferences for each glyph.

        Args:
            lines: List of glyph sequences (one per line)

        Returns:
            Map of glyph_id -> position distribution
        """
        position_counts: dict[str, Counter[str]] = defaultdict(Counter)

        for line in lines:
            if not line:
                continue

            n = len(line)
            for i, glyph in enumerate(line):
                if i == 0:
                    position_counts[glyph]["initial"] += 1
                elif i == n - 1:
                    position_counts[glyph]["final"] += 1
                else:
                    position_counts[glyph]["medial"] += 1

        # Normalize to probabilities
        result = {}
        for glyph, counts in position_counts.items():
            total = sum(counts.values())
            result[glyph] = {pos: count / total for pos, count in counts.items()}

        return result

    def find_line_markers(
        self,
        lines: list[list[str]],
        threshold: float = 0.6,
    ) -> tuple[list[str], list[str]]:
        """
        Find glyphs that frequently mark line boundaries.

        Args:
            lines: Glyph sequences
            threshold: Minimum ratio to consider a marker

        Returns:
            (initial_markers, final_markers)
        """
        positions = self.analyze_line_positions(lines)

        initial_markers = [
            glyph
            for glyph, dist in positions.items()
            if dist.get("initial", 0) >= threshold
        ]

        final_markers = [
            glyph
            for glyph, dist in positions.items()
            if dist.get("final", 0) >= threshold
        ]

        return initial_markers, final_markers

    def find_repetition_patterns(
        self,
        lines: list[list[str]],
        min_frequency: int = 2,
    ) -> list[StructuralPattern]:
        """
        Find repetition patterns (AA, AAA, ABAB, etc.).

        Args:
            lines: Glyph sequences
            min_frequency: Minimum occurrences to report

        Returns:
            List of repetition patterns
        """
        patterns = []
        pattern_counts: Counter[tuple] = Counter()

        for line in lines:
            # Find consecutive repetitions (AA, AAA)
            i = 0
            while i < len(line):
                glyph = line[i]
                count = 1
                while i + count < len(line) and line[i + count] == glyph:
                    count += 1
                if count >= 2:
                    pattern_counts[("consecutive", glyph, count)] += 1
                i += count

            # Find alternating patterns (ABAB)
            for i in range(len(line) - 3):
                if (
                    line[i] == line[i + 2]
                    and line[i + 1] == line[i + 3]
                    and line[i] != line[i + 1]
                ):
                    pattern_counts[("alternating", line[i], line[i + 1])] += 1

        # Convert to StructuralPattern objects
        pattern_id = 0
        for pattern_key, count in pattern_counts.items():
            if count >= min_frequency:
                pattern_id += 1
                ptype = pattern_key[0]

                if ptype == "consecutive":
                    glyph, rep_count = pattern_key[1], pattern_key[2]
                    patterns.append(
                        StructuralPattern(
                            pattern_id=f"struct_{pattern_id:03d}",
                            pattern_type="repetition",
                            glyph_ids=[glyph],
                            frequency=count,
                            position_preference={},
                            context=f"{glyph} repeated {rep_count} times consecutively",
                        )
                    )
                elif ptype == "alternating":
                    g1, g2 = pattern_key[1], pattern_key[2]
                    patterns.append(
                        StructuralPattern(
                            pattern_id=f"struct_{pattern_id:03d}",
                            pattern_type="alternation",
                            glyph_ids=[g1, g2],
                            frequency=count,
                            position_preference={},
                            context=f"Alternating pattern: {g1} {g2} {g1} {g2}",
                        )
                    )

        return patterns

    def analyze_line_structure(
        self,
        lines: list[list[str]],
    ) -> LineStructure:
        """
        Analyze overall line structure.

        Args:
            lines: Glyph sequences

        Returns:
            LineStructure with statistics
        """
        lengths = [len(line) for line in lines if line]

        if not lengths:
            return LineStructure(
                avg_length=0,
                length_variance=0,
                common_starters=[],
                common_enders=[],
                line_break_indicators=[],
            )

        avg = sum(lengths) / len(lengths)
        variance = sum((l - avg) ** 2 for l in lengths) / len(lengths)

        # Find common starters/enders
        starters: Counter[str] = Counter()
        enders: Counter[str] = Counter()

        for line in lines:
            if line:
                starters[line[0]] += 1
                enders[line[-1]] += 1

        return LineStructure(
            avg_length=avg,
            length_variance=variance,
            common_starters=starters.most_common(5),
            common_enders=enders.most_common(5),
            line_break_indicators=[g for g, _ in enders.most_common(3)],
        )

    def find_all_patterns(
        self,
        lines: list[list[str]],
        min_frequency: int = 2,
    ) -> list[StructuralPattern]:
        """
        Find all structural patterns.

        Args:
            lines: Glyph sequences
            min_frequency: Minimum occurrences

        Returns:
            All discovered patterns
        """
        patterns = []
        pattern_id_counter = 0

        # Line markers
        positions = self.analyze_line_positions(lines)
        initial_markers, final_markers = self.find_line_markers(lines)

        for glyph in initial_markers:
            pattern_id_counter += 1
            patterns.append(
                StructuralPattern(
                    pattern_id=f"struct_{pattern_id_counter:03d}",
                    pattern_type="line_marker",
                    glyph_ids=[glyph],
                    frequency=int(positions[glyph].get("initial", 0) * len(lines)),
                    position_preference=positions[glyph],
                    context="Frequently appears at line start",
                )
            )

        for glyph in final_markers:
            pattern_id_counter += 1
            patterns.append(
                StructuralPattern(
                    pattern_id=f"struct_{pattern_id_counter:03d}",
                    pattern_type="line_marker",
                    glyph_ids=[glyph],
                    frequency=int(positions[glyph].get("final", 0) * len(lines)),
                    position_preference=positions[glyph],
                    context="Frequently appears at line end",
                )
            )

        # Repetition patterns
        rep_patterns = self.find_repetition_patterns(lines, min_frequency)
        for p in rep_patterns:
            pattern_id_counter += 1
            p.pattern_id = f"struct_{pattern_id_counter:03d}"
            patterns.append(p)

        return patterns

    def interpret_patterns(
        self,
        patterns: list[StructuralPattern],
    ) -> list[StructuralPattern]:
        """
        Use LLM to interpret structural patterns.

        Args:
            patterns: Patterns to interpret

        Returns:
            Patterns with interpretations added
        """
        if not self.llm or not patterns:
            return patterns

        pattern_desc = "\n".join(
            f"- {p.pattern_id}: Type={p.pattern_type}, Glyphs={p.glyph_ids}, "
            f"Freq={p.frequency}, Context={p.context}"
            for p in patterns[:15]  # Limit for context
        )

        user_prompt = f"""Analyze these structural patterns from Rongorongo:

{pattern_desc}

For each pattern, provide an interpretation of what structural role it might play.

Respond with JSON:
{{
    "interpretations": [
        {{
            "pattern_id": "struct_001",
            "interpretation": "your interpretation",
            "function": "delimiter|emphasis|grammatical|counting|other"
        }}
    ]
}}"""

        messages = [
            LLMMessage(role="system", content=self.SYSTEM_PROMPT),
            LLMMessage(role="user", content=user_prompt),
        ]

        response = self.llm.complete(messages, max_tokens=1000, temperature=0.2)

        self._apply_interpretations(patterns, response)
        return patterns

    def _apply_interpretations(
        self, patterns: list[StructuralPattern], response: LLMResponse
    ) -> None:
        """Apply LLM interpretations to patterns."""
        import json

        try:
            content = response.content.strip()
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1])

            data = json.loads(content)

            interp_map = {
                i["pattern_id"]: i["interpretation"]
                for i in data.get("interpretations", [])
            }

            for pattern in patterns:
                if pattern.pattern_id in interp_map:
                    pattern.llm_interpretation = interp_map[pattern.pattern_id]

        except (json.JSONDecodeError, KeyError):
            pass
