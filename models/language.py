"""Data models for language entries."""

from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import datetime
import unicodedata


@dataclass
class Translation:
    """A translation of a word into another language."""
    language: str  # ISO code (e.g., "en", "es")
    text: str
    gloss: Optional[str] = None  # Short linguistic gloss


@dataclass
class Example:
    """An example usage of a word or phrase."""
    rapa_nui: str
    translation: str
    source: Optional[str] = None


@dataclass
class Metadata:
    """Source and tracking metadata for an entry."""
    source_url: str
    source_name: str
    scraped_at: str = field(default_factory=lambda: datetime.now().isoformat())
    confidence: str = "medium"  # "high", "medium", "low"


@dataclass
class Etymology:
    """Etymology information for a word."""
    origin: Optional[str] = None  # e.g., "Proto-Polynesian"
    cognates: list = field(default_factory=list)
    loan: bool = False


@dataclass
class LanguageEntry:
    """A single language entry (word or phrase)."""
    word: str
    normalized: str = ""
    ipa: Optional[str] = None
    translations: list[Translation] = field(default_factory=list)
    part_of_speech: Optional[str] = None
    semantic_category: Optional[str] = None
    examples: list[Example] = field(default_factory=list)
    etymology: Optional[Etymology] = None
    metadata: Optional[Metadata] = None

    def __post_init__(self):
        """Normalize the word after initialization."""
        if not self.normalized:
            self.normalized = self.normalize_word(self.word)

    @staticmethod
    def normalize_word(word: str) -> str:
        """Normalize word for deduplication (lowercase, remove diacritics)."""
        normalized = unicodedata.normalize("NFD", word.lower())
        return "".join(c for c in normalized if unicodedata.category(c) != "Mn")

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        result = {
            "word": self.word,
            "normalized": self.normalized,
        }
        if self.ipa:
            result["ipa"] = self.ipa
        if self.translations:
            result["translations"] = [
                {"language": t.language, "text": t.text, "gloss": t.gloss}
                for t in self.translations
            ]
        if self.part_of_speech:
            result["part_of_speech"] = self.part_of_speech
        if self.semantic_category:
            result["semantic_category"] = self.semantic_category
        if self.examples:
            result["examples"] = [
                {"rapa_nui": e.rapa_nui, "translation": e.translation, "source": e.source}
                for e in self.examples
            ]
        if self.etymology:
            result["etymology"] = {
                "origin": self.etymology.origin,
                "cognates": self.etymology.cognates,
                "loan": self.etymology.loan,
            }
        if self.metadata:
            result["metadata"] = {
                "source_url": self.metadata.source_url,
                "source_name": self.metadata.source_name,
                "scraped_at": self.metadata.scraped_at,
                "confidence": self.metadata.confidence,
            }
        return result

    def merge_with(self, other: "LanguageEntry") -> "LanguageEntry":
        """Merge another entry into this one, combining translations and examples."""
        # Merge translations (avoid duplicates by text)
        existing_texts = {t.text for t in self.translations}
        for t in other.translations:
            if t.text not in existing_texts:
                self.translations.append(t)
                existing_texts.add(t.text)

        # Merge examples (avoid duplicates by rapa_nui text)
        existing_examples = {e.rapa_nui for e in self.examples}
        for e in other.examples:
            if e.rapa_nui not in existing_examples:
                self.examples.append(e)
                existing_examples.add(e.rapa_nui)

        # Take IPA if we don't have it
        if not self.ipa and other.ipa:
            self.ipa = other.ipa

        # Take part of speech if we don't have it
        if not self.part_of_speech and other.part_of_speech:
            self.part_of_speech = other.part_of_speech

        # Take semantic category if we don't have it
        if not self.semantic_category and other.semantic_category:
            self.semantic_category = other.semantic_category

        # Merge etymology
        if other.etymology:
            if not self.etymology:
                self.etymology = other.etymology
            else:
                if not self.etymology.origin and other.etymology.origin:
                    self.etymology.origin = other.etymology.origin
                for cognate in other.etymology.cognates:
                    if cognate not in self.etymology.cognates:
                        self.etymology.cognates.append(cognate)

        return self
