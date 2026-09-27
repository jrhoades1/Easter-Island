"""Rapanui word and (C)V syllable samples.

Primary sequences are Thomson 1891 chants. Wikipedia ``lang=rap`` spans are a
modern-orthography check and are not pooled into the chant bigrams.
"""

from __future__ import annotations

import unicodedata
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RAPANUI_DIR = REPO_ROOT / "data" / "rapanui"
CHANTS_PATH = RAPANUI_DIR / "thomson_1891_chants.txt"
WIKI_PATH = RAPANUI_DIR / "wikipedia_rap_spans.txt"

# Vendored Wikipedia phonology: ten consonants, five vowels.
# Assumption, stated in data/rapanui/SOURCES.md: every consonant combines
# with every vowel, and each vowel also occurs with no onset.
CONSONANT_COUNT = 10
VOWEL_COUNT = 5
PHONOLOGICAL_CV_CEILING = CONSONANT_COUNT * VOWEL_COUNT + VOWEL_COUNT

VOWELS = frozenset("aeiou")
CONSONANTS = frozenset({"p", "t", "k", "m", "n", "ŋ", "h", "r", "v", "ʔ"})
GLOTTAL_CHARS = ("ʻ", "ʼ", "ꞌ", "'", "’", "ʔ", "ʿ")
MACRON_MAP = str.maketrans({"ā": "a", "ē": "e", "ī": "i", "ō": "o", "ū": "u"})
# Analysis map for 19th-century spelling. Not a phonetic claim.
LETTER_MAP = {
    "b": "p",
    "d": "t",
    "f": "h",
    "l": "r",
    "w": "v",
    "c": "k",
    "j": "h",
    "q": "k",
    "y": "i",
    "g": "ŋ",
    "s": "",
    "x": "",
}
PRIMARY_MIN_SYLLABLES = 1500
LOVE_SONG_SECTION = "love_song"

_PUNCT_EDGES = '.,;:!?"“”()[]¿¡*«»'


@dataclass(frozen=True)
class RapanuiSample:
    """Word sequences and the syllable sequences derived from them."""

    name: str
    orthography: str
    word_lines: tuple[tuple[str, ...], ...]
    syllable_lines: tuple[tuple[str, ...], ...]
    words_rejected: int

    @property
    def word_count(self) -> int:
        return sum(len(line) for line in self.word_lines)

    @property
    def syllable_count(self) -> int:
        return sum(len(line) for line in self.syllable_lines)


def tokenize_words(text: str) -> list[str]:
    """Whitespace words. Em-dashes break tokens. Edge punctuation is stripped."""
    text = text.replace("—", " ").replace("–", " ")
    words: list[str] = []
    for raw in text.split():
        word = raw.strip(_PUNCT_EDGES)
        if word and any(character.isalpha() for character in word):
            words.append(word)
    return words


def _format_syllable(onset: str | None, vowel: str) -> str:
    if onset is None:
        return vowel
    if onset == "ŋ":
        return "ng" + vowel
    if onset == "ʔ":
        return "'" + vowel
    return onset + vowel


def phonemes(word: str, orthography: str) -> list[str] | None:
    """Map one orthographic word to phoneme tokens, or reject it.

    Macrons collapse to one vowel. ``ng`` is one consonant. A leading glottal
    mark is an onset. Hyphens are removed after they have marked a
    reduplication boundary in the original word.
    """
    if orthography not in {"strict", "mapped"}:
        raise ValueError(orthography)
    text = word.lower().translate(MACRON_MAP)
    text = text.replace("ŋ", "ng")
    for mark in GLOTTAL_CHARS:
        text = text.replace(mark, "ʔ")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(character for character in text if not unicodedata.combining(character))
    text = text.replace("-", "")
    if not text:
        return []

    raw: list[str] = []
    index = 0
    while index < len(text):
        if text.startswith("ng", index):
            raw.append("ŋ")
            index += 2
            continue
        character = text[index]
        if orthography == "mapped" and character in LETTER_MAP:
            replacement = LETTER_MAP[character]
            if replacement:
                raw.append(replacement)
            index += 1
            continue
        raw.append(character)
        index += 1

    for phoneme in raw:
        if phoneme not in CONSONANTS and phoneme not in VOWELS:
            return None
    return raw


def syllabify_word(word: str, orthography: str) -> list[str] | None:
    """(C)V syllables. ``None`` means the word was rejected."""
    phones = phonemes(word, orthography)
    if phones is None:
        return None
    syllables: list[str] = []
    index = 0
    while index < len(phones):
        phoneme = phones[index]
        if phoneme in CONSONANTS:
            if index + 1 < len(phones) and phones[index + 1] in VOWELS:
                syllables.append(_format_syllable(phoneme, phones[index + 1]))
                index += 2
            else:
                index += 1
        else:
            syllables.append(_format_syllable(None, phoneme))
            index += 1
    return syllables


def is_full_reduplication(syllables: list[str] | tuple[str, ...]) -> bool:
    """True when the syllable string is two identical halves."""
    count = len(syllables)
    if count < 2 or count % 2:
        return False
    half = count // 2
    return list(syllables[:half]) == list(syllables[half:])


def load_thomson_word_lines(*, include_love_song: bool = False) -> list[list[str]]:
    """One word sequence per chant section."""
    sections: list[tuple[str, list[str]]] = []
    name = ""
    buffer: list[str] = []
    for raw in CHANTS_PATH.read_text(encoding="utf-8").splitlines():
        if raw.startswith("# section:"):
            if name:
                sections.append((name, buffer))
            name = raw.split(":", 1)[1].strip()
            buffer = []
            continue
        if name and raw.strip():
            buffer.extend(tokenize_words(raw))
    if name:
        sections.append((name, buffer))
    lines: list[list[str]] = []
    for section, words in sections:
        if not include_love_song and section == LOVE_SONG_SECTION:
            continue
        if words:
            lines.append(words)
    return lines


def load_wikipedia_word_lines() -> list[list[str]]:
    """Each kept span is its own short line."""
    lines: list[list[str]] = []
    for raw in WIKI_PATH.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.startswith("#"):
            continue
        words = tokenize_words(raw)
        if words:
            lines.append(words)
    return lines


def syllabify_lines(
    word_lines: list[list[str]],
    orthography: str,
) -> tuple[list[list[str]], int]:
    """Drop rejected words. A line that loses every word is dropped."""
    syllable_lines: list[list[str]] = []
    rejected = 0
    for words in word_lines:
        syllables: list[str] = []
        for word in words:
            parsed = syllabify_word(word, orthography)
            if parsed is None:
                rejected += 1
                continue
            syllables.extend(parsed)
        if syllables:
            syllable_lines.append(syllables)
    return syllable_lines, rejected


def build_sample(
    name: str,
    word_lines: list[list[str]],
    orthography: str,
) -> RapanuiSample:
    syllable_lines, rejected = syllabify_lines(word_lines, orthography)
    return RapanuiSample(
        name=name,
        orthography=orthography,
        word_lines=tuple(tuple(line) for line in word_lines),
        syllable_lines=tuple(tuple(line) for line in syllable_lines),
        words_rejected=rejected,
    )


def primary_thomson_sample() -> RapanuiSample:
    """Strict orthography when the clean sample is long enough, else mapped."""
    words = load_thomson_word_lines(include_love_song=False)
    strict = build_sample("thomson_strict", words, "strict")
    if strict.syllable_count >= PRIMARY_MIN_SYLLABLES:
        return strict
    return build_sample("thomson_mapped", words, "mapped")
