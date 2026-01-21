"""Data models for symbolic cross-referencing between Rongorongo glyphs and linguistic roots."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class ShapeCategory(Enum):
    """Visual shape categories for glyph classification."""

    AVIAN = "avian"  # Bird-like forms (manu-related)
    ANTHROPOMORPHIC = "anthropomorphic"  # Human figures (tangata, body parts)
    PHYTOMORPHIC = "phytomorphic"  # Plant forms (rakau, vegetation)
    ICHTHYOMORPHIC = "ichthyomorphic"  # Fish/marine (ika, moana)
    GEOMETRIC = "geometric"  # Abstract shapes (quantity, spatial)
    COMPOSITE = "composite"  # Combined elements
    UNDETERMINED = "undetermined"  # Cannot classify


class EvidenceType(Enum):
    """Types of evidence supporting a cross-reference."""

    SHAPE_SEMANTIC = "shape_semantic"  # Visual similarity to semantic domain
    FREQUENCY_CORRELATION = "frequency"  # Statistical frequency match
    POSITIONAL_PATTERN = "positional"  # Word order / position evidence
    NEIGHBOR_CONTEXT = "neighbor"  # Co-occurrence patterns
    PUBLISHED_HYPOTHESIS = "published"  # From Rongorongo scholarship
    MANUAL_ANNOTATION = "manual"  # Expert tagging


@dataclass
class ShapeTag:
    """A shape classification tag for a glyph cluster."""

    category: ShapeCategory
    confidence: float  # 0.0 to 1.0
    subcategory: Optional[str] = None  # e.g., "frigate_bird", "standing_figure"
    visual_features: list[str] = field(default_factory=list)  # ["wings", "beak"]
    tagged_by: str = "manual"  # "manual", "rule_based"
    tagged_at: Optional[str] = None

    def __post_init__(self):
        if self.tagged_at is None:
            self.tagged_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "category": self.category.value,
            "confidence": round(self.confidence, 3),
            "subcategory": self.subcategory,
            "visual_features": self.visual_features,
            "tagged_by": self.tagged_by,
            "tagged_at": self.tagged_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "ShapeTag":
        """Create from dictionary."""
        return cls(
            category=ShapeCategory(data["category"]),
            confidence=data["confidence"],
            subcategory=data.get("subcategory"),
            visual_features=data.get("visual_features", []),
            tagged_by=data.get("tagged_by", "manual"),
            tagged_at=data.get("tagged_at"),
        )


@dataclass
class EvidenceItem:
    """A single piece of evidence supporting a cross-reference."""

    evidence_type: EvidenceType
    description: str
    strength: float  # 0.0 to 1.0
    source: Optional[str] = None  # Citation or method name
    data: dict = field(default_factory=dict)  # Supporting data

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {
            "type": self.evidence_type.value,
            "description": self.description,
            "strength": round(self.strength, 3),
        }
        if self.source:
            result["source"] = self.source
        if self.data:
            result["data"] = self.data
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceItem":
        """Create from dictionary."""
        return cls(
            evidence_type=EvidenceType(data["type"]),
            description=data["description"],
            strength=data["strength"],
            source=data.get("source"),
            data=data.get("data", {}),
        )


@dataclass
class CrossReference:
    """A proposed link between a glyph cluster and language entry."""

    reference_id: str
    glyph_cluster_id: str  # References GlyphCluster.cluster_id
    language_entry_word: str  # References LanguageEntry.word
    language_entry_normalized: str  # For lookup

    # Confidence and reasoning
    overall_confidence: float  # 0.0 to 1.0
    confidence_level: str  # "speculative", "tentative", "plausible", "strong"

    # Semantic connection
    semantic_domain: str  # e.g., "animals", "kinship", "nature"

    # Fields with defaults must come after fields without defaults
    evidence: list[EvidenceItem] = field(default_factory=list)
    proto_polynesian_root: Optional[str] = None  # e.g., "*manu"

    # Metadata
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    created_by: str = "system"
    notes: Optional[str] = None

    # Status flags
    is_published_hypothesis: bool = False  # From scholarly sources
    requires_review: bool = True

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {
            "reference_id": self.reference_id,
            "glyph_cluster_id": self.glyph_cluster_id,
            "language_entry_word": self.language_entry_word,
            "language_entry_normalized": self.language_entry_normalized,
            "overall_confidence": round(self.overall_confidence, 3),
            "confidence_level": self.confidence_level,
            "evidence": [e.to_dict() for e in self.evidence],
            "semantic_domain": self.semantic_domain,
            "created_at": self.created_at,
            "created_by": self.created_by,
            "is_published_hypothesis": self.is_published_hypothesis,
            "requires_review": self.requires_review,
        }
        if self.proto_polynesian_root:
            result["proto_polynesian_root"] = self.proto_polynesian_root
        if self.notes:
            result["notes"] = self.notes
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "CrossReference":
        """Create from dictionary."""
        return cls(
            reference_id=data["reference_id"],
            glyph_cluster_id=data["glyph_cluster_id"],
            language_entry_word=data["language_entry_word"],
            language_entry_normalized=data["language_entry_normalized"],
            overall_confidence=data["overall_confidence"],
            confidence_level=data["confidence_level"],
            evidence=[EvidenceItem.from_dict(e) for e in data.get("evidence", [])],
            semantic_domain=data["semantic_domain"],
            proto_polynesian_root=data.get("proto_polynesian_root"),
            created_at=data.get("created_at", datetime.now().isoformat()),
            created_by=data.get("created_by", "system"),
            notes=data.get("notes"),
            is_published_hypothesis=data.get("is_published_hypothesis", False),
            requires_review=data.get("requires_review", True),
        )

    @staticmethod
    def generate_id(index: int) -> str:
        """Generate a cross-reference ID in format XR001, XR002, etc."""
        return f"XR{index:03d}"


@dataclass
class GlyphSemanticProfile:
    """Extended semantic profile for a glyph cluster."""

    cluster_id: str
    shape_tags: list[ShapeTag] = field(default_factory=list)
    primary_category: Optional[ShapeCategory] = None

    # Cross-references
    cross_reference_ids: list[str] = field(default_factory=list)

    # Statistical features useful for matching
    frequency_rank: int = 0  # 1 = most frequent
    frequency_count: int = 0
    positional_tendency: str = "neutral"  # "initial", "medial", "final", "neutral"

    # Barthel sign number if known
    barthel_number: Optional[str] = None  # e.g., "001", "076"

    def add_shape_tag(self, tag: ShapeTag) -> None:
        """Add a shape tag to this profile."""
        self.shape_tags.append(tag)
        # Update primary category to highest confidence tag
        if self.shape_tags:
            best = max(self.shape_tags, key=lambda t: t.confidence)
            self.primary_category = best.category

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {
            "cluster_id": self.cluster_id,
            "shape_tags": [t.to_dict() for t in self.shape_tags],
            "cross_reference_ids": self.cross_reference_ids,
            "frequency_rank": self.frequency_rank,
            "frequency_count": self.frequency_count,
            "positional_tendency": self.positional_tendency,
        }
        if self.primary_category:
            result["primary_category"] = self.primary_category.value
        if self.barthel_number:
            result["barthel_number"] = self.barthel_number
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "GlyphSemanticProfile":
        """Create from dictionary."""
        profile = cls(
            cluster_id=data["cluster_id"],
            shape_tags=[ShapeTag.from_dict(t) for t in data.get("shape_tags", [])],
            cross_reference_ids=data.get("cross_reference_ids", []),
            frequency_rank=data.get("frequency_rank", 0),
            frequency_count=data.get("frequency_count", 0),
            positional_tendency=data.get("positional_tendency", "neutral"),
            barthel_number=data.get("barthel_number"),
        )
        if data.get("primary_category"):
            profile.primary_category = ShapeCategory(data["primary_category"])
        return profile


@dataclass
class CrossReferenceStatistics:
    """Statistics about the cross-reference lexicon."""

    total_glyphs_profiled: int = 0
    total_cross_references: int = 0
    by_confidence_level: dict[str, int] = field(default_factory=dict)
    by_shape_category: dict[str, int] = field(default_factory=dict)
    by_semantic_domain: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "total_glyphs_profiled": self.total_glyphs_profiled,
            "total_cross_references": self.total_cross_references,
            "by_confidence_level": self.by_confidence_level,
            "by_shape_category": self.by_shape_category,
            "by_semantic_domain": self.by_semantic_domain,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "CrossReferenceStatistics":
        """Create from dictionary."""
        return cls(
            total_glyphs_profiled=data.get("total_glyphs_profiled", 0),
            total_cross_references=data.get("total_cross_references", 0),
            by_confidence_level=data.get("by_confidence_level", {}),
            by_shape_category=data.get("by_shape_category", {}),
            by_semantic_domain=data.get("by_semantic_domain", {}),
        )


@dataclass
class CrossReferenceLexicon:
    """Complete cross-reference dataset linking glyphs to linguistic roots."""

    version: str = "1.0.0"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    # Methodology warning
    methodology: dict = field(
        default_factory=lambda: {
            "description": "Hypothetical associations based on shape-semantic analysis",
            "warning": "Rongorongo is undeciphered. All associations are speculative.",
            "evidence_types": ["shape_semantic", "frequency", "positional", "neighbor"],
        }
    )

    # Source data references
    glyph_lexicon_file: str = ""
    language_lexicon_file: str = ""

    # Core data
    glyph_profiles: list[GlyphSemanticProfile] = field(default_factory=list)
    cross_references: list[CrossReference] = field(default_factory=list)

    # Statistics
    statistics: CrossReferenceStatistics = field(default_factory=CrossReferenceStatistics)

    def add_profile(self, profile: GlyphSemanticProfile) -> None:
        """Add a glyph profile to the lexicon."""
        self.glyph_profiles.append(profile)

    def add_cross_reference(self, xref: CrossReference) -> None:
        """Add a cross-reference to the lexicon."""
        self.cross_references.append(xref)

    def get_profile(self, cluster_id: str) -> Optional[GlyphSemanticProfile]:
        """Get a glyph profile by cluster ID."""
        for profile in self.glyph_profiles:
            if profile.cluster_id == cluster_id:
                return profile
        return None

    def get_references_for_glyph(self, cluster_id: str) -> list[CrossReference]:
        """Get all cross-references for a glyph cluster."""
        return [xr for xr in self.cross_references if xr.glyph_cluster_id == cluster_id]

    def get_references_for_word(self, word: str) -> list[CrossReference]:
        """Get all cross-references for a language entry word."""
        word_lower = word.lower()
        return [
            xr
            for xr in self.cross_references
            if xr.language_entry_word.lower() == word_lower
            or xr.language_entry_normalized == word_lower
        ]

    def compute_statistics(self) -> None:
        """Compute statistics from the current data."""
        self.statistics.total_glyphs_profiled = len(self.glyph_profiles)
        self.statistics.total_cross_references = len(self.cross_references)

        # Count by confidence level
        level_counts: dict[str, int] = {}
        for xr in self.cross_references:
            level_counts[xr.confidence_level] = level_counts.get(xr.confidence_level, 0) + 1
        self.statistics.by_confidence_level = level_counts

        # Count by shape category
        category_counts: dict[str, int] = {}
        for profile in self.glyph_profiles:
            if profile.primary_category:
                cat = profile.primary_category.value
                category_counts[cat] = category_counts.get(cat, 0) + 1
        self.statistics.by_shape_category = category_counts

        # Count by semantic domain
        domain_counts: dict[str, int] = {}
        for xr in self.cross_references:
            domain_counts[xr.semantic_domain] = domain_counts.get(xr.semantic_domain, 0) + 1
        self.statistics.by_semantic_domain = domain_counts

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "version": self.version,
            "created_at": self.created_at,
            "methodology": self.methodology,
            "source_data": {
                "glyph_lexicon": self.glyph_lexicon_file,
                "language_lexicon": self.language_lexicon_file,
            },
            "statistics": self.statistics.to_dict(),
            "glyph_profiles": [p.to_dict() for p in self.glyph_profiles],
            "cross_references": [xr.to_dict() for xr in self.cross_references],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "CrossReferenceLexicon":
        """Create from dictionary."""
        source = data.get("source_data", {})
        return cls(
            version=data.get("version", "1.0.0"),
            created_at=data.get("created_at", datetime.now().isoformat()),
            methodology=data.get("methodology", {}),
            glyph_lexicon_file=source.get("glyph_lexicon", ""),
            language_lexicon_file=source.get("language_lexicon", ""),
            glyph_profiles=[
                GlyphSemanticProfile.from_dict(p) for p in data.get("glyph_profiles", [])
            ],
            cross_references=[
                CrossReference.from_dict(xr) for xr in data.get("cross_references", [])
            ],
            statistics=CrossReferenceStatistics.from_dict(data.get("statistics", {})),
        )
