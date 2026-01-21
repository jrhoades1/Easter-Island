"""LLM-guided boundary analysis for glyph segmentation."""

from dataclasses import dataclass
from typing import Optional

from ..base import LLMMessage, LLMProvider, LLMResponse


@dataclass
class BoundaryDecision:
    """Decision about a glyph boundary."""

    region_id: str
    decision: str  # "keep" | "merge_left" | "merge_right" | "split"
    confidence: float
    reasoning: str
    suggested_split_point: Optional[int] = None  # x-coordinate if splitting


@dataclass
class AmbiguousBoundary:
    """A boundary region requiring LLM analysis."""

    region_id: str
    x_start: int
    x_end: int
    y_start: int
    y_end: int
    left_glyph_id: Optional[str]
    right_glyph_id: Optional[str]
    overlap_percentage: float
    cv_confidence: float


class BoundaryAnalyzer:
    """
    Analyzes ambiguous glyph boundaries using LLM vision.

    Uses visual analysis to determine whether overlapping or touching
    regions should be merged or kept separate.
    """

    SYSTEM_PROMPT = """You are an expert in Rongorongo script analysis. Your task is to analyze
glyph boundaries in tablet images to determine where one glyph ends and another begins.

Rongorongo is an undeciphered script from Easter Island with approximately 120 distinct signs.
Glyphs are typically:
- Drawn in continuous lines without lifting the stylus
- Between 1-3cm in height
- Sometimes connected by ligatures or shared strokes
- Occasionally damaged or worn

When analyzing a boundary region, consider:
1. Visual continuity - does the stroke pattern suggest one glyph or two?
2. Spacing patterns - is there natural whitespace suggesting separation?
3. Glyph complexity - is this region too complex for a single glyph?
4. Damage patterns - could wear have merged or split glyphs?

Respond in JSON format with your analysis."""

    def __init__(self, llm_provider: LLMProvider):
        """
        Initialize the boundary analyzer.

        Args:
            llm_provider: LLM provider for vision analysis
        """
        self.llm = llm_provider

    def analyze_boundary(
        self,
        boundary: AmbiguousBoundary,
        region_image: bytes,
        context_image: Optional[bytes] = None,
    ) -> BoundaryDecision:
        """
        Analyze an ambiguous boundary region.

        Args:
            boundary: The boundary to analyze
            region_image: Cropped image of the boundary region
            context_image: Optional wider context image

        Returns:
            BoundaryDecision with analysis results
        """
        user_prompt = f"""Analyze this glyph boundary region:

Region ID: {boundary.region_id}
Position: ({boundary.x_start}, {boundary.y_start}) to ({boundary.x_end}, {boundary.y_end})
Overlap with neighbors: {boundary.overlap_percentage:.1%}
CV segmentation confidence: {boundary.cv_confidence:.1%}

The computer vision system is uncertain whether this region contains:
- A single glyph (keep as-is)
- Two glyphs that should be separated (split)
- Part of the left glyph (merge_left)
- Part of the right glyph (merge_right)

Analyze the image and provide your decision in this JSON format:
{{
    "decision": "keep|merge_left|merge_right|split",
    "confidence": 0.0-1.0,
    "reasoning": "explanation of visual features that led to this decision",
    "split_point_x": null or x-coordinate if splitting
}}"""

        messages = [
            LLMMessage(role="system", content=self.SYSTEM_PROMPT),
            LLMMessage(role="user", content=user_prompt, images=[region_image]),
        ]

        if context_image:
            messages[1].images.append(context_image)

        response = self.llm.complete(messages, max_tokens=500, temperature=0.0)

        return self._parse_response(boundary.region_id, response)

    def _parse_response(self, region_id: str, response: LLMResponse) -> BoundaryDecision:
        """Parse LLM response into BoundaryDecision."""
        import json

        try:
            # Extract JSON from response
            content = response.content.strip()
            if content.startswith("```"):
                # Remove markdown code blocks
                lines = content.split("\n")
                content = "\n".join(lines[1:-1])

            data = json.loads(content)

            return BoundaryDecision(
                region_id=region_id,
                decision=data.get("decision", "keep"),
                confidence=float(data.get("confidence", 0.5)),
                reasoning=data.get("reasoning", "No reasoning provided"),
                suggested_split_point=data.get("split_point_x"),
            )
        except (json.JSONDecodeError, KeyError, ValueError):
            # Return conservative default on parse failure
            return BoundaryDecision(
                region_id=region_id,
                decision="keep",
                confidence=0.3,
                reasoning=f"Failed to parse LLM response: {response.content[:100]}",
            )

    def batch_analyze(
        self,
        boundaries: list[AmbiguousBoundary],
        region_images: dict[str, bytes],
    ) -> list[BoundaryDecision]:
        """
        Analyze multiple boundaries.

        Args:
            boundaries: List of boundaries to analyze
            region_images: Map of region_id to image bytes

        Returns:
            List of BoundaryDecisions
        """
        decisions = []
        for boundary in boundaries:
            image = region_images.get(boundary.region_id)
            if image:
                decision = self.analyze_boundary(boundary, image)
                decisions.append(decision)
            else:
                # No image available, keep the boundary
                decisions.append(
                    BoundaryDecision(
                        region_id=boundary.region_id,
                        decision="keep",
                        confidence=0.0,
                        reasoning="No image available for analysis",
                    )
                )
        return decisions
