"""Data models for a transliterated Rongorongo corpus.

Unlike ``models/glyphs.py`` (which models glyphs detected from images by the
computer-vision pipeline), this module models *transliterated* text: corpus
artifacts that scholars have already encoded as sequences of glyph codes
(e.g. the Barthel numbering system). It is the input to statistical analysis.

A glyph "token" is whatever appears between spaces in a transliteration. A
token may be a single glyph code (``"6"``) or a ligature/fusion of several
codes joined by ``-`` (``"6-700"``). Tokens are kept opaque strings; the
statistics layer decides when to decompose ligatures into component glyphs.
"""

from dataclasses import dataclass, field

LIGATURE_SEP = "-"


@dataclass
class CorpusLine:
    """A single line of transliterated text from a tablet side."""

    line_id: str  # e.g. "Ca1" (tablet C, side a, line 1)
    tokens: list[str]  # glyph tokens as written, in reading order

    @property
    def length(self) -> int:
        """Number of tokens (as-written) in the line."""
        return len(self.tokens)

    def glyphs(self) -> list[str]:
        """Tokens decomposed into component glyph codes.

        Ligature tokens (``"6-700"``) are split into their parts so that a
        fused glyph contributes to the frequency of each component.
        """
        out: list[str] = []
        for token in self.tokens:
            out.extend(token.split(LIGATURE_SEP))
        return out

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {"line_id": self.line_id, "tokens": list(self.tokens)}

    @classmethod
    def from_dict(cls, data: dict) -> "CorpusLine":
        """Create from dictionary."""
        return cls(line_id=data["line_id"], tokens=list(data["tokens"]))


@dataclass
class Tablet:
    """A single corpus artifact (tablet, staff, or other inscribed object)."""

    tablet_id: str  # short code, e.g. "C"
    name: str = ""  # common name, e.g. "Mamari"
    side: str = ""  # optional side label, e.g. "recto"
    lines: list[CorpusLine] = field(default_factory=list)
    is_synthetic: bool = False  # True for test/demo data, not real attestations

    @property
    def total_tokens(self) -> int:
        """Total as-written tokens across all lines."""
        return sum(line.length for line in self.lines)

    def all_tokens(self) -> list[str]:
        """Every as-written token in the tablet, in reading order."""
        return [token for line in self.lines for token in line.tokens]

    def all_glyphs(self) -> list[str]:
        """Every component glyph code (ligatures decomposed)."""
        return [glyph for line in self.lines for glyph in line.glyphs()]

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "tablet_id": self.tablet_id,
            "name": self.name,
            "side": self.side,
            "is_synthetic": self.is_synthetic,
            "lines": [line.to_dict() for line in self.lines],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Tablet":
        """Create from dictionary."""
        return cls(
            tablet_id=data["tablet_id"],
            name=data.get("name", ""),
            side=data.get("side", ""),
            is_synthetic=data.get("is_synthetic", False),
            lines=[CorpusLine.from_dict(line) for line in data.get("lines", [])],
        )


@dataclass
class RongorongoCorpus:
    """A collection of transliterated tablets to be analyzed together."""

    tablets: list[Tablet] = field(default_factory=list)

    @property
    def has_synthetic(self) -> bool:
        """Whether any tablet is flagged as synthetic (non-attested) data."""
        return any(tablet.is_synthetic for tablet in self.tablets)

    def lines(self) -> list[CorpusLine]:
        """Every line across every tablet."""
        return [line for tablet in self.tablets for line in tablet.lines]

    def token_sequences(self) -> list[list[str]]:
        """One as-written token sequence per line (for n-gram analysis)."""
        return [list(line.tokens) for line in self.lines()]

    def glyph_sequences(self) -> list[list[str]]:
        """One decomposed-glyph sequence per line (ligatures split)."""
        return [line.glyphs() for line in self.lines()]

    def all_glyphs(self) -> list[str]:
        """Every component glyph code across the whole corpus."""
        return [glyph for tablet in self.tablets for glyph in tablet.all_glyphs()]

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {"tablets": [tablet.to_dict() for tablet in self.tablets]}

    @classmethod
    def from_dict(cls, data: dict) -> "RongorongoCorpus":
        """Create from dictionary."""
        return cls(tablets=[Tablet.from_dict(t) for t in data.get("tablets", [])])
