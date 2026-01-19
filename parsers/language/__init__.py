"""Language-specific parsers for Rapa Nui and other languages."""

from .base import BaseLanguageParser
from .asjp import ASJPParser
from .ids import IDSParser
from .glosbe import GlosbeParser
from .omniglot import OmniglotParser
from .wikipedia import WikipediaLanguageParser

# Parser registry - maps URL patterns to parser instances
_PARSERS = [
    ASJPParser(),
    IDSParser(),
    GlosbeParser(),
    OmniglotParser(),
    WikipediaLanguageParser(),
]


def get_language_parser(url: str) -> BaseLanguageParser | None:
    """Get the appropriate parser for a URL."""
    for parser in _PARSERS:
        if parser.can_parse(url):
            return parser
    return None


__all__ = [
    "BaseLanguageParser",
    "ASJPParser",
    "IDSParser",
    "GlosbeParser",
    "OmniglotParser",
    "WikipediaLanguageParser",
    "get_language_parser",
]
