"""LLM-guided damage assessment for glyph regions."""

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from ..base import LLMMessage, LLMProvider, LLMResponse


class DamageType(Enum):
    """Types of damage that can affect glyph visibility."""

    NONE = "none"
    WEAR = "wear"  # Surface wear from handling
    CRACK = "crack"  # Physical crack through the wood
    EROSION = "erosion"  # Environmental erosion
    STAIN = "stain"  # Discoloration obscuring details
    MISSING = "missing"  # Section completely missing
    OVERLAY = "overlay"  # Later markings overlaid


@dataclass
class DamageAssessment:
    """Assessment of damage in a glyph region."""

    region_id: str
    damage_type: DamageType
    severity: float  # 0.0 (none) to 1.0 (complete)
    affected_percentage: float  # Percentage of region affected
    recoverable: bool  # Whether original form can be inferred
    reconstruction_confidence: float
    original_form_hypothesis: Optional[str]
    reasoning: str


@dataclass
class DamagedRegion:
    """A region identified as potentially damaged."""

    region_id: str
    bounding_box: dict
    contrast_score: float  # Low contrast may indicate wear
    edge_continuity: float  # Broken edges may indicate damage
    texture_anomaly: float  # Unusual texture patterns


class DamageAssessor:
    """
    Assesses damage to glyph regions and attempts reconstruction.

    Uses LLM vision to identify damage types and hypothesize original forms.
    """

    SYSTEM_PROMPT = """You are an expert in Rongorongo tablet conservation and paleography.
Your task is to assess damage to glyph regions and attempt to reconstruct original forms.

Rongorongo tablets are wooden artifacts, typically showing:
- Surface wear from handling (smoothed incisions)
- Cracks from wood drying and aging
- Environmental erosion from burial or exposure
- Staining from soil, water, or organic materials
- Missing sections from breakage

When assessing damage:
1. Identify the type and extent of damage
2. Determine if enough of the glyph remains for identification
3. Look for partial strokes that suggest the original form
4. Consider common glyph patterns that match visible portions
5. Be conservative - indicate low confidence if uncertain

Known Rongorongo signs include:
- Bird forms (various orientations)
- Human figures (standing, seated, holding objects)
- Geometric shapes (circles, lines, crescents)
- Plant/object forms (fish, tools, celestial symbols)

Respond with JSON analysis."""

    def __init__(self, llm_provider: LLMProvider):
        """
        Initialize the damage assessor.

        Args:
            llm_provider: LLM provider for vision analysis
        """
        self.llm = llm_provider

    def assess_region(
        self,
        region: DamagedRegion,
        region_image: bytes,
        undamaged_reference: Optional[bytes] = None,
    ) -> DamageAssessment:
        """
        Assess damage in a glyph region.

        Args:
            region: The damaged region to assess
            region_image: Image of the damaged region
            undamaged_reference: Optional image of similar undamaged region

        Returns:
            DamageAssessment with analysis
        """
        user_prompt = f"""Assess the damage in this Rongorongo glyph region:

Region ID: {region.region_id}
Dimensions: {region.bounding_box['width']}x{region.bounding_box['height']} pixels
Contrast score: {region.contrast_score:.2f} (lower = more faded)
Edge continuity: {region.edge_continuity:.2f} (lower = more broken edges)
Texture anomaly: {region.texture_anomaly:.2f} (higher = more unusual)

Analyze the image and provide your assessment in this JSON format:
{{
    "damage_type": "none|wear|crack|erosion|stain|missing|overlay",
    "severity": 0.0-1.0,
    "affected_percentage": 0-100,
    "recoverable": true|false,
    "reconstruction_confidence": 0.0-1.0,
    "original_form_hypothesis": "description of likely original glyph or null",
    "reasoning": "explanation of damage assessment"
}}"""

        images = [region_image]
        if undamaged_reference:
            images.append(undamaged_reference)

        messages = [
            LLMMessage(role="system", content=self.SYSTEM_PROMPT),
            LLMMessage(role="user", content=user_prompt, images=images),
        ]

        response = self.llm.complete(messages, max_tokens=600, temperature=0.0)

        return self._parse_response(region.region_id, response)

    def _parse_response(
        self, region_id: str, response: LLMResponse
    ) -> DamageAssessment:
        """Parse LLM response into DamageAssessment."""
        import json

        try:
            content = response.content.strip()
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1])

            data = json.loads(content)

            damage_type_str = data.get("damage_type", "none")
            try:
                damage_type = DamageType(damage_type_str)
            except ValueError:
                damage_type = DamageType.NONE

            return DamageAssessment(
                region_id=region_id,
                damage_type=damage_type,
                severity=float(data.get("severity", 0.0)),
                affected_percentage=float(data.get("affected_percentage", 0.0)),
                recoverable=data.get("recoverable", True),
                reconstruction_confidence=float(
                    data.get("reconstruction_confidence", 0.0)
                ),
                original_form_hypothesis=data.get("original_form_hypothesis"),
                reasoning=data.get("reasoning", "No reasoning provided"),
            )
        except (json.JSONDecodeError, KeyError, ValueError):
            return DamageAssessment(
                region_id=region_id,
                damage_type=DamageType.NONE,
                severity=0.0,
                affected_percentage=0.0,
                recoverable=True,
                reconstruction_confidence=0.0,
                original_form_hypothesis=None,
                reasoning=f"Failed to parse response: {response.content[:100]}",
            )

    def identify_damaged_regions(
        self,
        regions: list[DamagedRegion],
        contrast_threshold: float = 0.4,
        edge_threshold: float = 0.5,
        anomaly_threshold: float = 0.6,
    ) -> list[DamagedRegion]:
        """
        Filter regions to find likely damaged ones based on metrics.

        Args:
            regions: All detected regions
            contrast_threshold: Below this indicates possible wear
            edge_threshold: Below this indicates possible damage
            anomaly_threshold: Above this indicates unusual texture

        Returns:
            Filtered list of likely damaged regions
        """
        damaged = []
        for region in regions:
            if (
                region.contrast_score < contrast_threshold
                or region.edge_continuity < edge_threshold
                or region.texture_anomaly > anomaly_threshold
            ):
                damaged.append(region)
        return damaged

    def batch_assess(
        self,
        regions: list[DamagedRegion],
        region_images: dict[str, bytes],
    ) -> list[DamageAssessment]:
        """
        Assess multiple damaged regions.

        Args:
            regions: Regions to assess
            region_images: Map of region_id to image bytes

        Returns:
            List of DamageAssessment results
        """
        results = []
        for region in regions:
            image = region_images.get(region.region_id)
            if image:
                assessment = self.assess_region(region, image)
                results.append(assessment)
        return results
