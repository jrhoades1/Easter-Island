"""Old Rapanui running text and lexicon for Round 3 Track C.

Running text and lexicon lists stay separate. Track 2's Thomson-only loader
is unchanged. Normalization of a word is ``decipherment.rapanui.phonemes``
and ``syllabify_word``. The rules are listed in ``NORMALIZATION_RULES`` so
the report can print every one of them.

Primary running text, fixed before the scores were read:

- Thomson 1891 chants, love song excluded, section order of the vendored file
- Metoro's recitations for Jaussen, one line per vendored tablet line, filename order
- Routledge 1919's printed timo formula

Orthography for that primary sample is ``mapped``. Jaussen writes ``g`` for
the velar nasal, and Thomson uses letters that are not Rapanui phonemes.
``strict`` is reported beside it. A consonant that has no following vowel is
dropped by ``syllabify_word``, which is the Track 2 behavior. Lexicon and
crib matching use ``cv_syllables_mapped``, which rejects that word instead.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from html import unescape
from pathlib import Path

from decipherment.rapanui import (
    CHANTS_PATH,
    CONSONANTS,
    GLOTTAL_CHARS,
    LETTER_MAP,
    MACRON_MAP,
    RAPANUI_DIR,
    VOWELS,
    build_sample,
    phonemes,
    tokenize_words,
)
from decipherment.round2_trackb import LEXICON_EXAMPLES

REPO_ROOT = Path(__file__).resolve().parents[1]
METORO_DIR = REPO_ROOT / "data" / "readings" / "metoro_jaussen" / "lines"
CHURCHILL_HEADWORDS = RAPANUI_DIR / "churchill_1912_headwords.txt"
ROUTLEDGE_CHANTS = RAPANUI_DIR / "routledge_1919_chants.txt"
ROUTLEDGE_NAMES = RAPANUI_DIR / "routledge_1919_names.txt"

# Tablets C and E are the lines Jaussen says he reduced to the essential word.
ELLIPTICAL_TABLETS = frozenset({"C", "E"})

_PUNCT = ".,;:!?\"“”()[]¿¡*«»"
_POLY_CHARS = frozenset("abcdefghijklmnopqrstuvwxyz'-")
_CONSONANT_LETTERS = frozenset("bcdfghjklmnpqrstvwxyz")
_ENGLISH_FIRST = frozenset(
    {
        "the", "of", "and", "in", "for", "from", "with", "by", "or", "as", "at",
        "be", "is", "are", "was", "were", "not", "but", "his", "her", "its",
        "which", "when", "that", "this", "an", "it", "if", "my", "we", "do",
        "so", "up", "us", "see", "into", "than", "then", "also", "such", "may",
        "can", "one", "two", "same", "there", "their", "them", "these", "those",
        "have", "has", "had", "been", "being", "would", "could", "should",
        "other", "only", "very", "more", "some", "any", "all", "each", "both",
        "over", "under", "after", "before", "about", "between", "through",
        "during", "without", "within", "upon", "off", "out", "our", "you",
        "your", "they", "she", "him", "who", "what", "where", "how", "why",
        "because", "while", "thus", "hence", "thence", "make", "false",
        "statement", "accusation", "advise", "declare", "continued", "id",
        "cf", "page", "sense", "word", "form", "compare", "samoan",
        # Gloss and essay words that are not Rapanui headwords. OCR prose
        # inside the vocabulary starts with these.
        "again", "against", "adulate", "aim", "arose", "aside", "away", "axes",
        "axis", "becomes", "canoe", "case", "causative", "come", "comes",
        "coming", "courageous", "cover", "cup", "day", "decayed", "dedicate",
        "division", "does", "edifice", "equal", "evacuation", "examine", "face",
        "fixed", "honorific", "house", "images", "jaw", "joy", "juice",
        "languages", "leaves", "leisure", "liquid", "locative", "lose", "loyal",
        "macerated", "melanesia", "menace", "militates", "money", "names",
        "noise", "notice", "obey", "ocean", "pacific", "paradise", "peculiar",
        "piece", "pieces", "poisoned", "position", "quiet", "quite", "race",
        "received", "said", "sail", "samoa", "save", "seal", "season", "seat",
        "seawater", "set", "several", "singular", "situation", "soil", "son",
        "song", "soon", "soot", "unusual", "usage", "use", "used", "vexation",
        "violet", "virile", "voice", "vowel", "vowels", "voyages", "wages",
        "water", "wave", "waver", "way", "woman", "yes", "yet",
        "bed", "reading", "rise", "side", "solid", "red", "bad", "end",
        "old", "new", "big", "hot", "good", "long", "hand", "head", "foot",
        "back", "time", "year", "life", "man", "men", "god", "sun", "moon",
        "day", "name", "part", "place", "kind", "line", "left", "right",
    }
)
_PROSE_FUNCTION = frozenset(
    {
        "the", "of", "and", "in", "that", "which", "with", "from", "for", "by",
        "this", "these", "those", "their", "they", "we", "was", "were", "is",
        "are", "be", "been", "being", "have", "has", "had", "not", "but", "or",
        "as", "at", "on", "into", "than", "then", "also", "such", "may", "would",
        "could", "his", "her", "its", "who", "what", "when", "where", "how",
        "our", "you", "your", "she", "him", "if", "because", "while", "there",
        "over", "after", "before", "about", "between", "through", "during",
        "without", "upon", "other", "only", "very", "more", "some", "any",
        "all", "each", "both", "an",
    }
)
# Second-word particles that mark an example phrase rather than a gloss.
_PARTICLES = frozenset(
    {
        "a", "e", "i", "o", "u", "te", "ki", "ka", "ko", "ku", "ma", "mo", "me",
        "no", "na", "ni", "ra", "re", "ri", "ro", "ru", "he", "hai", "atu",
        "mai", "ana", "ai",
    }
)
_ITALIC = re.compile(r"<i>.*?</i>", re.IGNORECASE | re.DOTALL)
_PARA = re.compile(r"<p>(.*?)</p>", re.IGNORECASE | re.DOTALL)
_TAG = re.compile(r"<[^>]+>")
_LOCATOR = re.compile(r"=\d+=")
_PAGE = re.compile(r"\[p\.\d+\]", re.IGNORECASE)
_HEAD_TOKEN = re.compile(r"^[a-z][a-z'-]*$")
_SENSE = re.compile(r"^\d+$")
_PAREN = re.compile(r"\(([a-z][a-z'-]*)\)")
_LANG_BLEED = ("Mgv", "Mq.", "Mq:", "Ta.", "Ta:", "Sa.", "Sa:", "Pau.", "Pau:", "Niue", "Moriori")

NORMALIZATION_RULES: tuple[dict[str, str], ...] = (
    {
        "id": "lowercase",
        "rule": "Case is folded to lowercase before any letter test.",
    },
    {
        "id": "edge_punctuation",
        "rule": "Whitespace tokens lose edge punctuation . , ; : ! ? quotes and brackets. An em dash or en dash becomes a space. A token with no letter is dropped.",
    },
    {
        "id": "digits",
        "rule": "A token that contains a digit is dropped. Sense numbers in Churchill stay off the headword.",
    },
    {
        "id": "macron",
        "rule": "ā ē ī ō ū become a e i o u before other marks are stripped.",
    },
    {
        "id": "combining",
        "rule": "NFKD decomposition, then combining marks are deleted, so â ê î ô û and other accents become plain vowels.",
    },
    {
        "id": "glottal",
        "rule": "ʻ ʼ ꞌ ' ’ ʿ and ʔ become one glottal onset, written as an apostrophe plus the vowel.",
    },
    {
        "id": "eng",
        "rule": "The letter ŋ and the digraph ng are one consonant. The digraph is read before single-letter substitution, so ng is not g.",
    },
    {
        "id": "hyphen",
        "rule": "A hyphen is a reduplication boundary. It is kept in the stored word and removed before syllabification.",
    },
    {
        "id": "mapped_letters",
        "rule": "Orthography mapped, applied only after ng is read: b→p, d→t, f→h, l→r, w→v, c→k, j→h, q→k, y→i, g→ŋ, and s and x are deleted. This is the 19th-century spelling map from Track 2, not a phonetic claim.",
    },
    {
        "id": "reject",
        "rule": "A word is rejected when any remaining segment is not a vowel (a e i o u) or a consonant (p t k m n ŋ h r v ʔ).",
    },
    {
        "id": "syllables",
        "rule": "Syllables are (C)V. A consonant with no following vowel is dropped in running-text syllabification, matching Track 2. Lexicon and crib matching reject that word instead.",
    },
    {
        "id": "streams",
        "rule": "Lexicon headwords are not concatenated into running-text lines. Bigrams do not cross a chant section, a Metoro tablet line, or a Routledge formula.",
    },
)


@dataclass(frozen=True)
class RunningLine:
    """One running-text line after tokenization, before syllabification."""

    source: str
    line_id: str
    elliptical: bool
    words: tuple[str, ...]


@dataclass(frozen=True)
class Headword:
    """One lexicon entry. Not a running-text token sequence."""

    word: str
    source: str
    thomson: bool = False
    geiseler: bool = False


def cv_syllables_mapped(word: str) -> tuple[str, ...] | None:
    """Mapped (C)V syllables, or None if any consonant lacks a vowel.

    ``syllabify_word`` would drop the stranded consonant. The lexicon does not.
    """
    phones = phonemes(word, "mapped")
    if not phones:
        return None
    syllables: list[str] = []
    index = 0
    while index < len(phones):
        phoneme = phones[index]
        if phoneme not in VOWELS:
            if phoneme not in CONSONANTS:
                return None
            if index + 1 >= len(phones) or phones[index + 1] not in VOWELS:
                return None
            vowel = phones[index + 1]
            if phoneme == "ŋ":
                syllables.append("ng" + vowel)
            elif phoneme == "ʔ":
                syllables.append("'" + vowel)
            else:
                syllables.append(phoneme + vowel)
            index += 2
            continue
        syllables.append(phoneme)
        index += 1
    return tuple(syllables) if syllables else None


def _has_cluster(word: str) -> bool:
    """True when two consonants meet after ``ng`` is treated as one unit."""
    text = word.lower().replace("ng", "N")
    previous = False
    for character in text:
        if character in _CONSONANT_LETTERS or character == "N":
            if previous:
                return True
            previous = True
            continue
        if character in VOWELS or character in {"'", "-"}:
            previous = False
            continue
        return True
    return False


def _clean_token(token: str) -> str:
    return token.strip(_PUNCT).lower()


def _poly(token: str) -> bool:
    core = _clean_token(token)
    if not core or not _HEAD_TOKEN.match(core):
        return False
    if any(character.isdigit() for character in token):
        return False
    return any(character in VOWELS for character in core)


def _language_bleed(line: str) -> bool:
    if any(mark in line for mark in _LANG_BLEED):
        return True
    stripped = line.strip()
    if stripped.startswith(("P ", "PS", "PS.", "T ", "Fu.", "Ha.", "Ma.", "Vi.")):
        return True
    return False


def _rap_token(token: str) -> str | None:
    """A Rapanui-shaped token, or None when the token is a gloss or a number."""
    if token.startswith("("):
        return None
    core = _clean_token(token)
    if not core or _SENSE.match(core):
        return None
    if not _poly(token) or _has_cluster(core) or core in _ENGLISH_FIRST:
        return None
    return core


def _is_example_phrase(tokens: list[str]) -> bool:
    """True for a cited phrase, not for ``headword gloss``.

    ``poki aana, legitimate`` and ``aaki ki te mea`` are phrases. ``ure penis``
    is a headword plus a gloss that happens to alternate consonant and vowel.
    """
    phrase: list[str] = []
    saw_comma = False
    for token in tokens:
        if "," in token:
            saw_comma = True
            core = _rap_token(token)
            if core:
                phrase.append(core)
            break
        core = _rap_token(token)
        if core is None:
            break
        phrase.append(core)
    if len(phrase) < 2:
        return False
    if saw_comma:
        return True
    return any(part in _PARTICLES for part in phrase[1:])


def _is_prose(tokens: list[str]) -> bool:
    """Essay sentences inside the vocabulary use English function words."""
    hits = sum(1 for token in tokens if _clean_token(token) in _PROSE_FUNCTION)
    return hits >= 2


def parse_churchill_vocabulary(text: str) -> tuple[Headword, ...]:
    """Rapanui headwords from the Rapanui–English vocabulary, not the finding list.

    Headword lines are lowercase Polynesian words. A line of two or more such
    words is an example phrase and is not a headword. A line after a hyphenated
    break continues the previous gloss. ``T`` and ``Q`` suffixes, on a gloss
    line that is not a comparative note, mark Thomson and Geiseler.
    """
    lines = text.splitlines()
    try:
        start = next(index for index, line in enumerate(lines) if line.startswith("RAPANUI-ENGLISH"))
        end = next(index for index, line in enumerate(lines) if "ENGLISH-RAPANUI" in line and "FINDING" in line)
    except StopIteration as exc:
        raise ValueError("Churchill vocabulary bounds were not found") from exc

    raw_lines = lines[start:end]
    skipped_hyphen = False
    entries: list[tuple[str, list[str]]] = []
    current_word = ""
    current_lines: list[str] = []

    def close() -> None:
        nonlocal current_word, current_lines
        if current_word:
            entries.append((current_word, current_lines))
        current_word = ""
        current_lines = []

    for raw in raw_lines:
        stripped = raw.strip()
        if not stripped:
            skipped_hyphen = False
            continue
        if stripped.startswith("RAPANUI-ENGLISH"):
            skipped_hyphen = False
            continue
        if skipped_hyphen:
            skipped_hyphen = stripped.endswith("-")
            if current_word:
                current_lines.append(stripped)
            continue
        skipped_hyphen = stripped.endswith("-")
        if _language_bleed(stripped):
            if current_word:
                current_lines.append(stripped)
            continue
        tokens = stripped.split()
        first = _clean_token(tokens[0])
        to_without_sense = first == "to" and (
            len(tokens) < 2 or not _SENSE.match(_clean_token(tokens[1]))
        )
        if (
            _rap_token(tokens[0])
            and not to_without_sense
            and not _is_example_phrase(tokens)
            and not _is_prose(tokens)
        ):
            close()
            current_word = first
            current_lines = [stripped]
            continue
        if current_word:
            current_lines.append(stripped)
    close()

    found: dict[str, Headword] = {}
    for word, gloss_lines in entries:
        if _has_cluster(word) or not any(character in VOWELS for character in word):
            continue
        if any(character in "cjqsy" for character in word) or "'" in word:
            continue
        thomson = False
        geiseler = False
        extras: list[str] = []
        for gloss in gloss_lines:
            if _language_bleed(gloss):
                continue
            parts = gloss.replace(".", " ").split()
            if parts and parts[-1] == "T":
                thomson = True
            if parts and parts[-1] == "Q":
                geiseler = True
            if gloss == gloss_lines[0]:
                extras.extend(_PAREN.findall(gloss))
        words = [word, *extras]
        for item in words:
            if _has_cluster(item) or item in _ENGLISH_FIRST:
                continue
            if any(character in "cjqsy" for character in item) or "'" in item:
                continue
            previous = found.get(item)
            if previous is None:
                found[item] = Headword(item, "churchill_1912", thomson, geiseler)
                continue
            found[item] = Headword(
                item,
                "churchill_1912",
                previous.thomson or thomson,
                previous.geiseler or geiseler,
            )
    ordered = sorted(found.values(), key=lambda item: item.word)
    return tuple(ordered)


def load_churchill_headwords(path: Path = CHURCHILL_HEADWORDS) -> tuple[Headword, ...]:
    """Committed headword list. One word, then optional T and Q marks."""
    rows: list[Headword] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        word = parts[0].strip().lower()
        marks = set(parts[1:])
        if not word or _has_cluster(word):
            raise ValueError(f"bad Churchill headword {raw!r}")
        rows.append(Headword(word, "churchill_1912", "T" in marks, "Q" in marks))
    return tuple(rows)


def extract_metoro_lines(directory: Path = METORO_DIR) -> tuple[RunningLine, ...]:
    """Word sequences from the vendored Metoro HTML. Comments in italics are dropped."""
    rows: list[RunningLine] = []
    for path in sorted(directory.glob("*.html")):
        html = path.read_text(encoding="utf-8", errors="replace")
        words: list[str] = []
        for paragraph in _PARA.findall(html):
            if "__" not in paragraph and not re.search(r"=\d+=", paragraph):
                continue
            # The line header (tablet id, "Show hieroglyphs") sits before =01=.
            marker = re.search(r"=\d+\s*=", paragraph)
            if marker:
                paragraph = paragraph[marker.end() :]
            text = _ITALIC.sub(" ", paragraph)
            text = text.replace("<SUP>__</SUP>", " ").replace("<sup>__</sup>", " ")
            text = _LOCATOR.sub(" ", text)
            text = _PAGE.sub(" ", text)
            text = _TAG.sub(" ", text)
            text = unescape(text)
            text = unicodedata.normalize("NFKC", text)
            words.extend(tokenize_words(text))
        if not words:
            continue
        line_id = path.stem
        tablet = line_id[0].upper()
        rows.append(
            RunningLine(
                source="metoro_jaussen",
                line_id=line_id,
                elliptical=tablet in ELLIPTICAL_TABLETS,
                words=tuple(words),
            )
        )
    return tuple(rows)


def _routledge_lines(path: Path, source: str) -> tuple[RunningLine, ...]:
    if not path.exists():
        return ()
    rows: list[RunningLine] = []
    section = source
    buffer: list[str] = []

    def flush() -> None:
        if buffer:
            rows.append(RunningLine(source, section, False, tuple(buffer)))

    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("# section:"):
            flush()
            buffer = []
            section = raw.split(":", 1)[1].strip()
            continue
        if not raw.strip() or raw.startswith("#"):
            continue
        buffer.extend(tokenize_words(raw))
    flush()
    return tuple(rows)


def load_routledge_chants() -> tuple[RunningLine, ...]:
    return _routledge_lines(ROUTLEDGE_CHANTS, "routledge_1919")


def load_routledge_names() -> tuple[Headword, ...]:
    if not ROUTLEDGE_NAMES.exists():
        return ()
    rows: list[Headword] = []
    for raw in ROUTLEDGE_NAMES.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        rows.append(Headword(line.split("\t", 1)[0].lower(), "routledge_1919"))
    return tuple(rows)


def load_thomson_running(*, include_love_song: bool = False) -> tuple[RunningLine, ...]:
    """One line per chant section, the same sections Track 2 uses."""
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
        if name and raw.strip() and not raw.startswith("#"):
            buffer.extend(tokenize_words(raw))
    if name:
        sections.append((name, buffer))
    rows: list[RunningLine] = []
    for section, words in sections:
        if not include_love_song and section == "love_song":
            continue
        if words:
            rows.append(RunningLine("thomson_1891", section, False, tuple(words)))
    return tuple(rows)


def load_thomson_example_headwords() -> tuple[Headword, ...]:
    rows: list[Headword] = []
    seen: set[str] = set()
    for raw in Path(LEXICON_EXAMPLES).read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.startswith("#"):
            continue
        for word in tokenize_words(raw):
            key = word.lower()
            if key in seen:
                continue
            seen.add(key)
            rows.append(Headword(key, "thomson_1891_examples"))
    return tuple(rows)


def primary_running_lines(*, include_elliptical: bool = True) -> tuple[RunningLine, ...]:
    """Thomson, then Metoro, then Routledge. Love song stays out."""
    lines = list(load_thomson_running(include_love_song=False))
    for row in extract_metoro_lines():
        if not include_elliptical and row.elliptical:
            continue
        lines.append(row)
    lines.extend(load_routledge_chants())
    return tuple(lines)


def word_lines_of(rows: tuple[RunningLine, ...] | list[RunningLine]) -> list[list[str]]:
    return [list(row.words) for row in rows if row.words]


def lexicon_headwords() -> tuple[Headword, ...]:
    """Dictionary and name lists. Not running text."""
    merged: dict[str, Headword] = {}
    for item in (
        *load_churchill_headwords(),
        *load_thomson_example_headwords(),
        *load_routledge_names(),
    ):
        previous = merged.get(item.word)
        if previous is None:
            merged[item.word] = item
            continue
        merged[item.word] = Headword(
            item.word,
            previous.source,
            previous.thomson or item.thomson,
            previous.geiseler or item.geiseler,
        )
    return tuple(sorted(merged.values(), key=lambda item: item.word))


def sample_from_lines(name: str, rows: tuple[RunningLine, ...], orthography: str):
    """``RapanuiSample`` for a running-text selection."""
    return build_sample(name, word_lines_of(rows), orthography)


def letter_map_text() -> str:
    """The mapped substitutions, in the order they are applied after ``ng``."""
    parts = [f"{source}→{target or '∅'}" for source, target in LETTER_MAP.items()]
    return ", ".join(parts)


def glottal_text() -> str:
    return " ".join(GLOTTAL_CHARS)


def macron_text() -> str:
    shown = []
    for source, target in MACRON_MAP.items():
        shown.append(f"{chr(source)}→{chr(target)}")
    return ", ".join(shown)
