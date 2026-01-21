"""LLM-guided ligature detection for composite glyphs."""

from dataclasses import dataclass
from typing import Optional

from ..base import LLMMessage, LLMProvider, LLMResponse


@dataclass
class LigatureAnalysis:
    """Analysis of a potential ligature (composite glyph)."""

    glyph_id: str
    is_ligature: bool
    confidence: float
    component_count: int  # Number of component glyphs if ligature
    component_descriptions: list[str]
    reasoning: str
    separation_feasible: bool


@dataclass
class LigatureCandidate:
    """A glyph candidate for ligature analysis."""

    glyph_id: str
    bounding_box: dict  # {"x": int, "y": int, "width": int, "height": int}
    aspect_ratio: float
    complexity_score: float  # Based on contour analysis
    stroke_count_estimate: int


class LigatureDetector:
    """
    Detects ligatures (composite glyphs) using LLM vision analysis.

    Ligatures in Rongorongo occur when two or more glyphs share strokes
    or are written as a combined unit.
    """

    SYSTEM_PROMPT = """You are an expert in Rongorongo script analysis, specializing in
identifying ligatures (composite glyphs) in the script.

A ligature in Rongorongo is a single written form that combines two or more distinct glyphs:
- May share strokes or connecting elements
- Often has unusual proportions (very wide or complex)
- Components may be vertically stacked or horizontally joined
- Some ligatures are rare while others are common combinations

Known ligature patterns include:
- Bird + object combinations (common)
- Human figure + tool combinations
- Repeated geometric elements

When analyzing a potential ligature:
1. Look for distinct visual components that could be separate glyphs
2. Check if the overall shape is more complex than typical single glyphs
3. Identify any shared strokes or connecting elements
4. Consider if separation would create meaningful component glyphs

Respond with JSON analysis."""

    def __init__(self, llm_provider: LLMProvider):
        """
        Initialize the ligature detector.

        Args:
            llm_provider: LLM provider for vision analysis
        """
        self.llm = llm_provider

    def analyze_candidate(
        self,
        candidate: LigatureCandidate,
        glyph_image: bytes,
        reference_glyphs: Optional[list[bytes]] = None,
    ) -> LigatureAnalysis:
        """
        Analyze a glyph to determine if it's a ligature.

        Args:
            candidate: The candidate glyph to analyze
            glyph_image: Image of the glyph
            reference_glyphs: Optional reference images of known single glyphs

        Returns:
            LigatureAnalysis with results
        """
        user_prompt = f"""Analyze this Rongorongo glyph to determine if it is a ligature (composite glyph):

Glyph ID: {candidate.glyph_id}
Dimensions: {candidate.bounding_box['width']}x{candidate.bounding_box['height']} pixels
Aspect ratio: {candidate.aspect_ratio:.2f}
Complexity score: {candidate.complexity_score:.2f}
Estimated stroke count: {candidate.stroke_count_estimate}

A high aspect ratio or complexity score may indicate a ligature.

Analyze the image and provide your assessment in this JSON format:
{{
    "is_ligature": true|false,
    "confidence": 0.0-1.0,
    "component_count": number of distinct glyph components (1 if not a ligature),
    "component_descriptions": ["description of each component if ligature"],
    "reasoning": "explanation of visual features",
    "separation_feasible": true|false (whether components could be separated cleanly)
}}"""

        images = [glyph_image]
        if reference_glyphs:
            images.extend(reference_glyphs[:3])  # Limit to 3 references

        messages = [
            LLMMessage(role="system", content=self.SYSTEM_PROMPT),
            LLMMessage(role="user", content=user_prompt, images=images),
        ]

        response = self.llm.complete(messages, max_tokens=600, temperature=0.0)

        return self._parse_response(candidate.glyph_id, response)

    def _parse_response(self, glyph_id: str, response: LLMResponse) -> LigatureAnalysis:
        """Parse LLM response into LigatureAnalysis."""
        import json

        try:
            content = response.content.strip()
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1])

            data = json.loads(content)

            return LigatureAnalysis(
                glyph_id=glyph_id,
                is_ligature=data.get("is_ligature", False),
                confidence=float(data.get("confidence", 0.5)),
                component_count=int(data.get("component_count", 1)),
                component_descriptions=data.get("component_descriptions", []),
                reasoning=data.get("reasoning", "No reasoning provided"),
                separation_feasible=data.get("separation_feasible", False),
            )
        except (json.JSONDecodeError, KeyError, ValueError):
            return LigatureAnalysis(
                glyph_id=glyph_id,
                is_ligature=False,
                confidence=0.3,
                component_count=1,
                component_descriptions=[],
                reasoning=f"Failed to parse response: {response.content[:100]}",
                separation_feasible=False,
            )

    def find_ligature_candidates(
        self,
        glyphs: list[LigatureCandidate],
        aspect_ratio_threshold: float = 1.8,
        complexity_threshold: float = 0.7,
    ) -> list[LigatureCandidate]:
        """
        Filter glyphs to find likely ligature candidates based on metrics.

        Args:
            glyphs: All detected glyphs
            aspect_ratio_threshold: Min aspect ratio to consider
            complexity_threshold: Min complexity score to consider

        Returns:
            Filtered list of candidates worth LLM analysis
        """
        candidates = []
        for glyph in glyphs:
            # Wide glyphs or complex glyphs are potential ligatures
            if (
                glyph.aspect_ratio >= aspect_ratio_threshold
                or glyph.complexity_score >= complexity_threshold
            ):
                candidates.append(glyph)
        return candidates

    def batch_analyze(
        self,
        candidates: list[LigatureCandidate],
        glyph_images: dict[str, bytes],
    ) -> list[LigatureAnalysis]:
        """
        Analyze multiple ligature candidates.

        Args:
            candidates: Candidates to analyze
            glyph_images: Map of glyph_id to image bytes

        Returns:
            List of LigatureAnalysis results
        """
        results = []
        for candidate in candidates:
            image = glyph_images.get(candidate.glyph_id)
            if image:
                analysis = self.analyze_candidate(candidate, image)
                results.append(analysis)
        return results
