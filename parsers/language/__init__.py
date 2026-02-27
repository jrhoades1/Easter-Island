"""Language-specific parsers for Rapa Nui and other Polynesian languages."""

from .asjp import ASJPParser
from .base import BaseLanguageParser
from .glosbe import GlosbeParser
from .hawaiian_parser import HawaiianDictionaryParser
from .ids import IDSParser
from .maori_parser import MaoriDictionaryParser
from .omniglot import OmniglotParser
from .tahitian_parser import TahitianDictionaryParser
from .wikipedia import WikipediaLanguageParser

# Parser registry - maps URL patterns to parser instances
_PARSERS = [
    ASJPParser(),
    IDSParser(),
    GlosbeParser(),
    OmniglotParser(),
    WikipediaLanguageParser(),
    MaoriDictionaryParser(),
    HawaiianDictionaryParser(),
    TahitianDictionaryParser(),
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
    "MaoriDictionaryParser",
    "HawaiianDictionaryParser",
    "TahitianDictionaryParser",
    "get_language_parser",
]
