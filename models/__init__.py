"""Data models for Easter Island scraper."""

from .language import LanguageEntry, Translation, Example
from .cross_reference import (
    ShapeCategory,
    EvidenceType,
    ShapeTag,
    EvidenceItem,
    CrossReference,
    GlyphSemanticProfile,
    CrossReferenceStatistics,
    CrossReferenceLexicon,
)

__all__ = [
    "LanguageEntry",
    "Translation",
    "Example",
    "ShapeCategory",
    "EvidenceType",
    "ShapeTag",
    "EvidenceItem",
    "CrossReference",
    "GlyphSemanticProfile",
    "CrossReferenceStatistics",
    "CrossReferenceLexicon",
]
