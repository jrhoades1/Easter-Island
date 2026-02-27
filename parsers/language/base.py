"""Base class for language content parsers."""

import os
import sys
from abc import ABC, abstractmethod
from datetime import datetime

from bs4 import BeautifulSoup

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from models.language import Example, LanguageEntry, Metadata, Translation


class BaseLanguageParser(ABC):
    """Abstract base class for language content parsers."""

    source_name: str = "Unknown"
    source_url_pattern: str = ""

    @abstractmethod
    def can_parse(self, url: str) -> bool:
        """Check if this parser can handle the given URL."""
        pass

    @abstractmethod
    def parse(self, html: str, url: str) -> list[LanguageEntry]:
        """Parse HTML and return language entries."""
        pass

    def get_soup(self, html: str) -> BeautifulSoup:
        """Create a BeautifulSoup object from HTML."""
        return BeautifulSoup(html, "lxml")

    def create_metadata(self, url: str, confidence: str = "medium") -> Metadata:
        """Generate metadata for entries from this source."""
        return Metadata(
            source_url=url,
            source_name=self.source_name,
            scraped_at=datetime.now().isoformat(),
            confidence=confidence,
        )

    def create_translation(self, text: str, language: str = "en", gloss: str = None) -> Translation:
        """Create a translation object."""
        return Translation(language=language, text=text, gloss=gloss)

    def create_example(self, rapa_nui: str, translation: str, source: str = None) -> Example:
        """Create an example object."""
        return Example(rapa_nui=rapa_nui, translation=translation, source=source or self.source_name)

    def clean_text(self, text: str) -> str:
        """Clean and normalize text."""
        if not text:
            return ""
        # Remove extra whitespace
        return " ".join(text.split())
