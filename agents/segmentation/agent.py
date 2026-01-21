"""Glyph Segmentation Agent - LLM-guided glyph boundary detection."""

import json
from pathlib import Path
from typing import Optional

from ..base import BaseAgent, LLMCache, LLMProvider
from .boundary_analyzer import AmbiguousBoundary, BoundaryAnalyzer
from .damage_assessor import DamagedRegion, DamageAssessor
from .ligature_detector import LigatureCandidate, LigatureDetector


class GlyphSegmentationAgent(BaseAgent):
    """
    LLM-guided glyph segmentation agent.

    Enhances computer vision segmentation with LLM-based decisions for:
    - Ambiguous boundary regions
    - Ligature (composite glyph) detection
    - Damaged region assessment
    """

    AGENT_NAME = "glyph_segmentation"
    VERSION = "1.0.0"

    def __init__(
        self,
        llm_provider: LLMProvider,
        cache: Optional[LLMCache] = None,
    ):
        """
        Initialize the segmentation agent.

        Args:
            llm_provider: LLM provider for vision analysis
            cache: Optional response cache
        """
        super().__init__(llm_provider, cache)
        self.boundary_analyzer = BoundaryAnalyzer(llm_provider)
        self.ligature_detector = LigatureDetector(llm_provider)
        self.damage_assessor = DamageAssessor(llm_provider)

    def get_input_schema(self) -> dict:
        """Get input schema for segmentation agent."""
        return {
            "type": "object",
            "required": ["source_image", "cv_segmentation"],
            "properties": {
                "source_image": {
                    "type": "string",
                    "description": "Path to the tablet image file",
                },
                "cv_segmentation": {
                    "type": "object",
                    "description": "CV segmentation results",
                    "properties": {
                        "glyphs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "glyph_id": {"type": "string"},
                                    "bounding_box": {"type": "object"},
                                    "confidence": {"type": "number"},
                                },
                            },
                        },
                        "ambiguous_regions": {"type": "array"},
                    },
                },
                "glyph_images": {
                    "type": "object",
                    "description": "Map of glyph_id to base64 image data",
                },
                "analyze_ligatures": {
                    "type": "boolean",
                    "default": True,
                },
                "analyze_damage": {
                    "type": "boolean",
                    "default": True,
                },
            },
        }

    def get_output_schema(self) -> dict:
        """Get output schema for segmentation agent."""
        return {
            "type": "object",
            "properties": {
                "run_metadata": {"type": "object"},
                "source_image": {"type": "string"},
                "segmentation_results": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "glyph_id": {"type": "string"},
                            "bounding_box": {"type": "object"},
                            "confidence": {"type": "number"},
                            "method": {"type": "string"},
                            "notes": {"type": "string"},
                        },
                    },
                },
                "boundary_decisions": {"type": "array"},
                "ligature_analysis": {"type": "array"},
                "damage_assessments": {"type": "array"},
                "statistics": {"type": "object"},
            },
        }

    def run(self, input_data: dict) -> dict:
        """
        Execute segmentation analysis.

        Args:
            input_data: Contains source_image, cv_segmentation, glyph_images

        Returns:
            Refined segmentation with LLM-guided decisions
        """
        source_image = input_data["source_image"]
        cv_seg = input_data["cv_segmentation"]
        glyph_images = input_data.get("glyph_images", {})
        analyze_ligatures = input_data.get("analyze_ligatures", True)
        analyze_damage = input_data.get("analyze_damage", True)

        # Start with CV segmentation results
        segmentation_results = []
        for glyph in cv_seg.get("glyphs", []):
            segmentation_results.append({
                "glyph_id": glyph["glyph_id"],
                "bounding_box": glyph["bounding_box"],
                "confidence": glyph["confidence"],
                "method": "cv_only",
                "notes": None,
            })

        # Analyze ambiguous boundaries
        boundary_decisions = []
        ambiguous = cv_seg.get("ambiguous_regions", [])
        if ambiguous:
            boundaries = [
                AmbiguousBoundary(
                    region_id=r["region_id"],
                    x_start=r["x_start"],
                    x_end=r["x_end"],
                    y_start=r["y_start"],
                    y_end=r["y_end"],
                    left_glyph_id=r.get("left_glyph_id"),
                    right_glyph_id=r.get("right_glyph_id"),
                    overlap_percentage=r.get("overlap_percentage", 0.0),
                    cv_confidence=r.get("cv_confidence", 0.5),
                )
                for r in ambiguous
            ]

            # Get images for boundaries
            boundary_images = {}
            for b in boundaries:
                if b.region_id in glyph_images:
                    boundary_images[b.region_id] = self._decode_image(
                        glyph_images[b.region_id]
                    )

            decisions = self.boundary_analyzer.batch_analyze(boundaries, boundary_images)
            boundary_decisions = [
                {
                    "region_id": d.region_id,
                    "decision": d.decision,
                    "confidence": d.confidence,
                    "reasoning": d.reasoning,
                    "suggested_split_point": d.suggested_split_point,
                }
                for d in decisions
            ]

            # Update segmentation based on decisions
            self._apply_boundary_decisions(segmentation_results, boundary_decisions)

        # Analyze for ligatures
        ligature_analysis = []
        if analyze_ligatures:
            candidates = self._find_ligature_candidates(cv_seg.get("glyphs", []))
            if candidates:
                candidate_images = {
                    c.glyph_id: self._decode_image(glyph_images[c.glyph_id])
                    for c in candidates
                    if c.glyph_id in glyph_images
                }

                analyses = self.ligature_detector.batch_analyze(
                    candidates, candidate_images
                )
                ligature_analysis = [
                    {
                        "glyph_id": a.glyph_id,
                        "is_ligature": a.is_ligature,
                        "confidence": a.confidence,
                        "component_count": a.component_count,
                        "component_descriptions": a.component_descriptions,
                        "reasoning": a.reasoning,
                        "separation_feasible": a.separation_feasible,
                    }
                    for a in analyses
                ]

                # Update segmentation notes for ligatures
                self._annotate_ligatures(segmentation_results, ligature_analysis)

        # Assess damage
        damage_assessments = []
        if analyze_damage:
            damaged_regions = self._find_damaged_regions(cv_seg.get("glyphs", []))
            if damaged_regions:
                region_images = {
                    r.region_id: self._decode_image(glyph_images[r.region_id])
                    for r in damaged_regions
                    if r.region_id in glyph_images
                }

                assessments = self.damage_assessor.batch_assess(
                    damaged_regions, region_images
                )
                damage_assessments = [
                    {
                        "region_id": a.region_id,
                        "damage_type": a.damage_type.value,
                        "severity": a.severity,
                        "affected_percentage": a.affected_percentage,
                        "recoverable": a.recoverable,
                        "reconstruction_confidence": a.reconstruction_confidence,
                        "original_form_hypothesis": a.original_form_hypothesis,
                        "reasoning": a.reasoning,
                    }
                    for a in assessments
                ]

        # Compile statistics
        statistics = {
            "total_glyphs": len(segmentation_results),
            "cv_only": sum(
                1 for s in segmentation_results if s["method"] == "cv_only"
            ),
            "llm_assisted": sum(
                1 for s in segmentation_results if s["method"] == "llm_assisted"
            ),
            "boundaries_analyzed": len(boundary_decisions),
            "ligatures_found": sum(1 for l in ligature_analysis if l["is_ligature"]),
            "damaged_regions": len(damage_assessments),
        }

        return {
            "source_image": source_image,
            "segmentation_results": segmentation_results,
            "boundary_decisions": boundary_decisions,
            "ligature_analysis": ligature_analysis,
            "damage_assessments": damage_assessments,
            "statistics": statistics,
        }

    def _decode_image(self, image_data: str) -> bytes:
        """Decode base64 image data to bytes."""
        import base64

        if image_data.startswith("data:"):
            # Remove data URL prefix
            image_data = image_data.split(",", 1)[1]
        return base64.b64decode(image_data)

    def _find_ligature_candidates(
        self, glyphs: list[dict]
    ) -> list[LigatureCandidate]:
        """Find glyphs that might be ligatures."""
        candidates = []
        for glyph in glyphs:
            bbox = glyph.get("bounding_box", {})
            width = bbox.get("width", 1)
            height = bbox.get("height", 1)
            aspect_ratio = width / height if height > 0 else 1.0

            # Use heuristics to identify candidates
            complexity = glyph.get("complexity_score", 0.5)
            stroke_count = glyph.get("stroke_count", 3)

            if aspect_ratio > 1.5 or complexity > 0.7:
                candidates.append(
                    LigatureCandidate(
                        glyph_id=glyph["glyph_id"],
                        bounding_box=bbox,
                        aspect_ratio=aspect_ratio,
                        complexity_score=complexity,
                        stroke_count_estimate=stroke_count,
                    )
                )
        return candidates

    def _find_damaged_regions(self, glyphs: list[dict]) -> list[DamagedRegion]:
        """Find regions that might be damaged."""
        damaged = []
        for glyph in glyphs:
            contrast = glyph.get("contrast_score", 1.0)
            edge_cont = glyph.get("edge_continuity", 1.0)
            anomaly = glyph.get("texture_anomaly", 0.0)

            if contrast < 0.5 or edge_cont < 0.5 or anomaly > 0.5:
                damaged.append(
                    DamagedRegion(
                        region_id=glyph["glyph_id"],
                        bounding_box=glyph.get("bounding_box", {}),
                        contrast_score=contrast,
                        edge_continuity=edge_cont,
                        texture_anomaly=anomaly,
                    )
                )
        return damaged

    def _apply_boundary_decisions(
        self, results: list[dict], decisions: list[dict]
    ) -> None:
        """Apply boundary decisions to segmentation results."""
        for decision in decisions:
            if decision["decision"] in ("merge_left", "merge_right", "split"):
                # Find affected glyphs and update
                for result in results:
                    if result["glyph_id"] in (
                        decision.get("left_glyph_id"),
                        decision.get("right_glyph_id"),
                    ):
                        result["method"] = "llm_assisted"
                        result["notes"] = (
                            f"Boundary {decision['decision']}: {decision['reasoning']}"
                        )

    def _annotate_ligatures(
        self, results: list[dict], analyses: list[dict]
    ) -> None:
        """Annotate ligatures in segmentation results."""
        ligature_ids = {a["glyph_id"] for a in analyses if a["is_ligature"]}
        for result in results:
            if result["glyph_id"] in ligature_ids:
                analysis = next(
                    a for a in analyses if a["glyph_id"] == result["glyph_id"]
                )
                result["notes"] = (
                    f"Ligature ({analysis['component_count']} components): "
                    f"{', '.join(analysis['component_descriptions'])}"
                )


def save_results(results: dict, output_path: str) -> None:
    """Save segmentation results to JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
