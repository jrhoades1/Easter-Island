"""Round 2 Track B: test Round 1 anchors as a phonetic crib and as logograms.

The anchors are the Mamari night crescent, the full-moon pair, the calendar
separator, the Gv6 ``200 X Y.076`` handoff, and the Staff bar that is
followed by 076. Sound values are the first (C)V syllable of a cited
Rapanui word. A reading is adopted only when the crib words those values
spell, outside the anchor passages, beat both a permutation of the same
syllables and a draw of random attested syllables. ``MockProvider`` is
accepted and never called.
"""

from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass
from html import unescape
from itertools import permutations
from pathlib import Path
from typing import Iterable

from agents.base.providers import MockProvider
from decipherment.barthel_corpus import (
    _LINE_ANCHOR,
    _SIDE_FILENAME,
    _SIDE_LINE,
    _TD,
    FIXTURES,
)
from decipherment.rapanui import (
    VOWELS,
    load_thomson_word_lines,
    load_wikipedia_word_lines,
    phonemes,
    tokenize_words,
)
from decipherment.track3_genealogy import (
    chain_links,
    extract_quad_phrases,
    extract_strict_phrases,
    group_stems,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
HEADWORD_PATH = REPO_ROOT / "data" / "rapanui" / "crib_headwords.txt"
LEXICON_EXAMPLES = REPO_ROOT / "data" / "rapanui" / "thomson_1891_lexicon_examples.txt"

TABLETS = tuple("ABCDEFGHIJKLMNOPQRSTUV")
SIGNS = ("040", "143", "152", "200", "076")
WINDOW_LENGTHS = (2, 3, 4)
# Same gate as Track 2. A tie with the null is not a reading.
ADOPT_FRACTION = 0.05

# Guy 1990 delimiter, with the two Ca6 third-sign variants kept distinct
# (Track 1). Slices of these tuples are the sub-clusters.
SEPARATORS = (
    ("390", "041", "378", "041", "670", "008", "078", "711"),
    ("390", "041", "315", "041", "670", "008", "078", "711"),
    ("390", "041", "375", "041"),
)
# Lunar and delimiter signs cited in Track 1, plus 008. 008 is inside the
# delimiter; Fischer 1995 also glosses one 008 as the sun. Both citations
# are hypotheses about meaning. The set is fixed before the counts.
SKY_SIGNS = frozenset({"040", "041", "143", "152", "008"})
SKY_OTHER = frozenset({"041", "143", "152", "008"})

CALENDAR_CA6_START = 24
CALENDAR_CA9_END = 2

RANDOM_TRIALS = 500
RANDOM_SEED = 0
REGION_TRIALS = 500
REGION_SEED = 1
SEPARATOR_TRIALS = 500
SEPARATOR_SEED = 2
PHRASE_TRIALS = 500
PHRASE_SEED = 3
SLOT_TRIALS = 500
SLOT_SEED = 5

_CIRCUMFLEX = str.maketrans({"â": "a", "ê": "e", "î": "i", "ô": "o", "û": "u"})


@dataclass(frozen=True)
class LineText:
    """One Barthel line. Groups keep ligatures; flat is the stem sequence."""

    side: str
    number: int
    groups: tuple[str, ...]
    stems: tuple[tuple[str, ...], ...]

    @property
    def line_id(self) -> str:
        return f"{self.side}{self.number}"

    @property
    def tablet(self) -> str:
        return self.side[0]

    @property
    def flat(self) -> tuple[str, ...]:
        return tuple(stem for group in self.stems for stem in group)

    def group_index_of_stem(self) -> tuple[int, ...]:
        indexes: list[int] = []
        for group_index, group in enumerate(self.stems):
            indexes.extend([group_index] * len(group))
        return tuple(indexes)


@dataclass(frozen=True)
class Gloss:
    """One cited word a sign would stand for if the crib were phonetic."""

    sign: str
    word: str
    citation: str


@dataclass(frozen=True)
class Hypothesis:
    """A fixed map from the five anchor signs to cited words.

    The syllable value is the first (C)V of ``word``, computed, not typed.
    """

    name: str
    glosses: tuple[Gloss, ...]

    def words(self) -> dict[str, str]:
        return {gloss.sign: gloss.word for gloss in self.glosses}

    def syllables(self) -> dict[str, str]:
        return {gloss.sign: first_syllable(gloss.word) for gloss in self.glosses}


@dataclass(frozen=True)
class NullCount:
    """How often a null reaches the observed score.

    ``positive`` is the number of trials whose score was greater than zero.
    It is recorded for the separator-length test, where the observed score
    is zero and ``ge`` is then the whole trial count.
    """

    observed: int
    ge: int
    trials: int
    positive: int = -1

    @property
    def survives(self) -> bool:
        """True only when the score is positive and beats the adopt gate."""
        if self.observed <= 0 or self.trials <= 0:
            return False
        return (self.ge / self.trials) <= ADOPT_FRACTION


@dataclass(frozen=True)
class HypothesisScore:
    name: str
    syllables: tuple[tuple[str, str], ...]
    open_hits: tuple[tuple[tuple[str, ...], int], ...]
    crib_hits: tuple[tuple[tuple[str, ...], int], ...]
    open_permutation: NullCount
    crib_permutation: NullCount
    open_random: NullCount
    crib_random: NullCount
    phrase_hits: int
    phrase_permutation: NullCount

    @property
    def reading_adopted(self) -> bool:
        """A reading requires the crib score, not the open-lexicon score."""
        return self.crib_permutation.survives and self.crib_random.survives


def cv_syllables(word: str) -> tuple[str, ...] | None:
    """(C)V syllables, or None when a consonant has no following vowel.

    ``syllabify_word`` drops a stranded consonant and can turn Thomson's
    ``tantan`` into ta-ta. The crib lexicon does not use those forms.
    """
    phones = phonemes(word.translate(_CIRCUMFLEX), "strict")
    if not phones:
        return None
    syllables: list[str] = []
    index = 0
    while index < len(phones):
        phoneme = phones[index]
        if phoneme not in VOWELS:
            if index + 1 < len(phones) and phones[index + 1] in VOWELS:
                vowel = phones[index + 1]
                if phoneme == "ŋ":
                    syllables.append("ng" + vowel)
                elif phoneme == "ʔ":
                    syllables.append("'" + vowel)
                else:
                    syllables.append(phoneme + vowel)
                index += 2
                continue
            return None
        syllables.append(phoneme)
        index += 1
    return tuple(syllables)


def first_syllable(word: str) -> str:
    syllables = cv_syllables(word)
    if not syllables:
        raise ValueError(f"{word!r} is not a strict (C)V crib word")
    return syllables[0]


def load_headwords(path: Path = HEADWORD_PATH) -> tuple[tuple[str, str], ...]:
    """(word, citation) rows. Comments and blank lines are skipped."""
    rows: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        word, _sep, citation = line.partition("\t")
        word = word.strip()
        if not word or not citation.strip():
            raise ValueError(f"crib headword row needs a word and a citation: {raw!r}")
        if cv_syllables(word) is None:
            raise ValueError(f"crib headword {word!r} is not strict (C)V")
        rows.append((word, citation.strip()))
    return tuple(rows)


def _add_words(words: Iterable[str], lexicon: set[tuple[str, ...]], forms: dict) -> None:
    for word in words:
        syllables = cv_syllables(word)
        if not syllables:
            continue
        lexicon.add(syllables)
        forms.setdefault(syllables, set()).add(word.lower())


def build_lexicon(
    headwords: tuple[tuple[str, str], ...] | None = None,
) -> tuple[frozenset[tuple[str, ...]], dict[tuple[str, ...], frozenset[str]], frozenset[tuple[str, ...]]]:
    """Open lexicon, surface forms, and the multi-syllable crib targets.

    The open lexicon is Thomson's chants (love song excluded), his lexicon
    examples, the Wikipedia ``lang=rap`` spans, and the crib headwords.
    Targets are the headwords of two or more syllables: the words the crib
    is supposed to produce.
    """
    if headwords is None:
        headwords = load_headwords()
    lexicon: set[tuple[str, ...]] = set()
    forms: dict[tuple[str, ...], set[str]] = {}
    for line in load_thomson_word_lines(include_love_song=False):
        _add_words(line, lexicon, forms)
    example_words: list[str] = []
    for raw in LEXICON_EXAMPLES.read_text(encoding="utf-8").splitlines():
        if raw.strip() and not raw.startswith("#"):
            example_words.extend(tokenize_words(raw))
    _add_words(example_words, lexicon, forms)
    for line in load_wikipedia_word_lines():
        _add_words(line, lexicon, forms)
    _add_words((word for word, _citation in headwords), lexicon, forms)
    targets = {
        syllables
        for word, _citation in headwords
        if (syllables := cv_syllables(word)) is not None and len(syllables) >= 2
    }
    frozen_forms = {key: frozenset(value) for key, value in forms.items()}
    return frozenset(lexicon), frozen_forms, frozenset(targets)


def load_lines(fixtures: Path = FIXTURES) -> tuple[LineText, ...]:
    """Vendored A–V sides. Line numbers come from the Kohaumotu anchors.

    Ia.html publishes Horley's order, which is not numeric. The anchor
    number is the line id, and the cells stay in published order.
    """
    lines: list[LineText] = []
    for path in sorted(fixtures.rglob("*.html")):
        if not _SIDE_FILENAME.match(path.name):
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        anchors = [(int(match.group(1)), match.end()) for match in _LINE_ANCHOR.finditer(html)]
        if not anchors:
            anchors = [(int(match.group(1)), match.end()) for match in _SIDE_LINE.finditer(html)]
        for index, (number, start) in enumerate(anchors):
            end = len(html)
            if index + 1 < len(anchors):
                next_header = html.rfind("<h3", 0, anchors[index + 1][1])
                end = next_header if next_header != -1 else anchors[index + 1][1]
            tokens: list[str] = []
            for cell in _TD.findall(html[start:end]):
                text = unescape(cell).strip()
                if not text or not any(character.isdigit() for character in text):
                    continue
                for part in text.split("-"):
                    part = part.strip()
                    if part:
                        tokens.append(part)
            groups = tuple(tokens)
            lines.append(
                LineText(
                    side=path.stem,
                    number=number,
                    groups=groups,
                    stems=tuple(group_stems(token) for token in groups),
                )
            )
    return tuple(lines)


def is_calendar_stem(line: LineText, index: int) -> bool:
    """True inside Ca6 from stem 24, all of Ca7–Ca8, and Ca9's first two stems."""
    if line.side != "Ca":
        return False
    if line.number == 6:
        return index >= CALENDAR_CA6_START
    if line.number in (7, 8):
        return True
    if line.number == 9:
        return index < CALENDAR_CA9_END
    return False


def region_spans(line: LineText) -> tuple[tuple[int, int], ...]:
    """Spans shuffled separately so the calendar block does not leak."""
    length = len(line.flat)
    if length == 0:
        return ()
    if line.side == "Ca" and line.number == 6:
        cut = min(CALENDAR_CA6_START, length)
        spans = ((0, cut), (cut, length))
    elif line.side == "Ca" and line.number == 9:
        cut = min(CALENDAR_CA9_END, length)
        spans = ((0, cut), (cut, length))
    else:
        spans = ((0, length),)
    return tuple(span for span in spans if span[1] > span[0])


def _shuffle_spans(flat: list[str], spans: tuple[tuple[int, int], ...], rng: random.Random) -> None:
    for start, end in spans:
        chunk = flat[start:end]
        rng.shuffle(chunk)
        flat[start:end] = chunk


@dataclass(frozen=True)
class Anchors:
    """Positions that Round 1 already accounted for."""

    chain_groups: frozenset[int]
    bracket_groups: frozenset[tuple[int, int]]
    calendar_types: frozenset[str]

    def stem_is_anchor(self, line: LineText, index: int, sign: str) -> bool:
        if sign in {"040", "143", "152"} and is_calendar_stem(line, index):
            return True
        group_index = line.group_index_of_stem()[index]
        if (
            sign in {"200", "076"}
            and line.side == "Gv"
            and line.number == 6
            and group_index in self.chain_groups
        ):
            return True
        if sign == "076" and line.side == "Ia" and (line.number, group_index) in self.bracket_groups:
            return True
        return False


def build_anchors(lines: tuple[LineText, ...]) -> Anchors:
    gv6 = next(line for line in lines if line.side == "Gv" and line.number == 6)
    phrases = extract_strict_phrases(gv6.groups, gv6.line_id)
    chain: set[int] = set()
    for phrase in phrases:
        chain.update(range(phrase.index, phrase.index + 3))
    bracket: set[tuple[int, int]] = set()
    for line in lines:
        if line.side != "Ia":
            continue
        for group_index, token in enumerate(line.groups):
            if group_stems(token) != ("999",):
                continue
            if group_index + 1 >= len(line.groups):
                continue
            if "076" in group_stems(line.groups[group_index + 1]):
                bracket.add((line.number, group_index + 1))
    calendar: set[str] = set()
    for line in lines:
        for index, sign in enumerate(line.flat):
            if is_calendar_stem(line, index):
                calendar.add(sign)
    return Anchors(frozenset(chain), frozenset(bracket), frozenset(calendar))


def _guard_calendar(lines: tuple[LineText, ...]) -> None:
    ca6 = next(line for line in lines if line.side == "Ca" and line.number == 6)
    opening = ("390", "041", "315", "041", "670", "008", "078", "711")
    if tuple(ca6.flat[CALENDAR_CA6_START : CALENDAR_CA6_START + 8]) != opening:
        raise ValueError("Ca6 stem 24 is not the published 315 delimiter")


def separator_slices() -> tuple[tuple[str, ...], ...]:
    """Every contiguous slice of length at least 2, from the published separators."""
    found: list[tuple[str, ...]] = []
    seen: set[tuple[str, ...]] = set()
    for separator in SEPARATORS:
        length = len(separator)
        for start in range(length):
            for end in range(start + 2, length + 1):
                piece = separator[start:end]
                if piece not in seen:
                    seen.add(piece)
                    found.append(piece)
    return tuple(found)


def _count_slice(lines: Iterable[LineText], gram: tuple[str, ...], *, outside: bool) -> int:
    width = len(gram)
    hits = 0
    for line in lines:
        flat = line.flat
        for start in range(len(flat) - width + 1):
            if tuple(flat[start : start + width]) != gram:
                continue
            inside = all(is_calendar_stem(line, index) for index in range(start, start + width))
            if outside and inside:
                continue
            if not outside and not inside:
                continue
            hits += 1
    return hits


def hypotheses() -> tuple[Hypothesis, ...]:
    """Four maps fixed from the cited glosses. Syllables are derived."""
    lunar = (
        Gloss("143", "rakau", "Night before omotohi in the Track 1 alignment; Guy 1990 places 143 there"),
        Gloss("152", "omotohi", "Full-moon night in Thomson and Englert; Guy 1990 and Horley 2011 place it at 152"),
    )
    return (
        Hypothesis(
            "H1",
            (
                Gloss("040", "po", "Night; Wikipedia pō and Thomson raa-po-tahi"),
                *lunar,
                Gloss("200", "tangata", "Man; Thomson Apai tangata; Davletshin 2012 man/title, a hypothesis"),
                Gloss("076", "ure", "Patronym; Davletshin cites ure, a hypothesis; Thomson Apai ure"),
            ),
        ),
        Hypothesis(
            "H2",
            (
                Gloss("040", "marama", "Moon; Metoro vocabulary marama, not a Barthel gloss"),
                *lunar,
                Gloss("200", "ko", "Personal article; Wikipedia ko"),
                Gloss("076", "poki", "Child; Thomson poki and Wikipedia poki"),
            ),
        ),
        Hypothesis(
            "H3",
            (
                Gloss("040", "po", "Night; Wikipedia pō and Thomson raa-po-tahi"),
                *lunar,
                Gloss("200", "ko", "Personal article; Wikipedia ko"),
                Gloss("076", "ure", "Patronym hypothesis ure"),
            ),
        ),
        Hypothesis(
            "H4",
            (
                Gloss("040", "po", "Night; Wikipedia pō and Thomson raa-po-tahi"),
                *lunar,
                Gloss("200", "ko", "Personal article; Wikipedia ko"),
                Gloss("076", "tama", "Child; Metoro tama, tamaiti; Thomson tamahine and tamaroa"),
            ),
        ),
    )


def _windows(
    lines: tuple[LineText, ...],
    anchors: Anchors,
    *,
    outside: bool,
) -> tuple[tuple[str, ...], ...]:
    """Contiguous stems whose every sign is one of the five anchors."""
    assigned = set(SIGNS)
    found: list[tuple[str, ...]] = []
    for line in lines:
        flat = line.flat
        length = len(flat)
        for start in range(length):
            for width in WINDOW_LENGTHS:
                if start + width > length:
                    continue
                gram = tuple(flat[start : start + width])
                if any(sign not in assigned for sign in gram):
                    continue
                anchored = [
                    anchors.stem_is_anchor(line, start + offset, gram[offset])
                    for offset in range(width)
                ]
                if outside and any(anchored):
                    continue
                if not outside and not all(anchored):
                    continue
                found.append(gram)
    return tuple(found)


def _score_windows(
    windows: tuple[tuple[str, ...], ...],
    assignment: dict[str, str],
    vocabulary: frozenset[tuple[str, ...]],
) -> Counter[tuple[str, ...]]:
    hits: Counter[tuple[str, ...]] = Counter()
    for gram in windows:
        syllables = tuple(assignment[sign] for sign in gram)
        if syllables in vocabulary:
            hits[syllables] += 1
    return hits


def _word_sequences() -> tuple[tuple[tuple[str, ...], ...], ...]:
    """Attested word sequences. A rejected word breaks the sequence."""
    sequences: list[tuple[tuple[str, ...], ...]] = []

    def consume(words: list[str]) -> None:
        buffer: list[tuple[str, ...]] = []
        for word in words:
            syllables = cv_syllables(word)
            if syllables is None:
                if len(buffer) >= 2:
                    sequences.append(tuple(buffer))
                buffer = []
                continue
            buffer.append(syllables)
        if len(buffer) >= 2:
            sequences.append(tuple(buffer))

    for line in load_thomson_word_lines(include_love_song=False):
        consume(line)
    for line in load_wikipedia_word_lines():
        consume(line)
    return tuple(sequences)


def _phrase_vocabulary(
    sequences: tuple[tuple[tuple[str, ...], ...], ...],
) -> frozenset[tuple[tuple[str, ...], ...]]:
    phrases: set[tuple[tuple[str, ...], ...]] = set()
    for sequence in sequences:
        length = len(sequence)
        for width in WINDOW_LENGTHS:
            for start in range(length - width + 1):
                phrases.add(tuple(sequence[start : start + width]))
    return frozenset(phrases)


def _score_phrases(
    windows: tuple[tuple[str, ...], ...],
    words: dict[str, str],
    phrases: frozenset[tuple[tuple[str, ...], ...]],
) -> int:
    syllables = {sign: cv_syllables(word) for sign, word in words.items()}
    hits = 0
    for gram in windows:
        phrase = tuple(syllables[sign] for sign in gram)
        if phrase in phrases:
            hits += 1
    return hits


def _permutation_null(
    windows: tuple[tuple[str, ...], ...],
    syllables: tuple[str, ...],
    observed: int,
    vocabulary: frozenset[tuple[str, ...]],
) -> NullCount:
    ge = 0
    for perm in permutations(syllables):
        assignment = dict(zip(SIGNS, perm))
        score = sum(_score_windows(windows, assignment, vocabulary).values())
        if score >= observed:
            ge += 1
    return NullCount(observed, ge, len(tuple(permutations(syllables))))


def _phrase_permutation_null(
    windows: tuple[tuple[str, ...], ...],
    word_list: tuple[str, ...],
    observed: int,
    phrases: frozenset[tuple[tuple[str, ...], ...]],
) -> NullCount:
    ge = 0
    total = 0
    for perm in permutations(word_list):
        total += 1
        score = _score_phrases(windows, dict(zip(SIGNS, perm)), phrases)
        if score >= observed:
            ge += 1
    return NullCount(observed, ge, total)


def _random_scores(
    windows: tuple[tuple[str, ...], ...],
    syllable_types: tuple[str, ...],
    open_lexicon: frozenset[tuple[str, ...]],
    targets: frozenset[tuple[str, ...]],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    rng = random.Random(RANDOM_SEED)
    open_scores: list[int] = []
    crib_scores: list[int] = []
    for _ in range(RANDOM_TRIALS):
        drawn = rng.sample(list(syllable_types), len(SIGNS))
        assignment = dict(zip(SIGNS, drawn))
        open_scores.append(sum(_score_windows(windows, assignment, open_lexicon).values()))
        crib_scores.append(sum(_score_windows(windows, assignment, targets).values()))
    return tuple(open_scores), tuple(crib_scores)


def _null_from_scores(observed: int, scores: tuple[int, ...]) -> NullCount:
    ge = sum(1 for score in scores if score >= observed)
    positive = sum(1 for score in scores if score > 0)
    return NullCount(observed, ge, len(scores), positive)


def _outside_sign_counts(
    lines: tuple[LineText, ...], anchors: Anchors
) -> dict[str, tuple[int, ...]]:
    counts = {sign: Counter() for sign in SIGNS}
    for line in lines:
        for index, sign in enumerate(line.flat):
            if sign not in counts:
                continue
            if anchors.stem_is_anchor(line, index, sign):
                continue
            counts[sign][line.tablet] += 1
    return {sign: tuple(counts[sign][tablet] for tablet in TABLETS) for sign in SIGNS}


def _neighbor_frames(
    lines: tuple[LineText, ...],
    anchors: Anchors,
    sign: str,
) -> tuple[Counter[tuple[str, str]], dict[tuple[str, str], tuple[str, ...]]]:
    """Interior (left, right) pairs around an outside occurrence of ``sign``."""
    frames: Counter[tuple[str, str]] = Counter()
    sites: dict[tuple[str, str], list[str]] = {}
    for line in lines:
        flat = line.flat
        for index, token in enumerate(flat):
            if token != sign or anchors.stem_is_anchor(line, index, sign):
                continue
            if index == 0 or index + 1 == len(flat):
                continue
            key = (flat[index - 1], flat[index + 1])
            frames[key] += 1
            sites.setdefault(key, []).append(f"{line.line_id}:{index}")
    frozen = {key: tuple(value) for key, value in sites.items()}
    return frames, frozen


def _run_lengths(lines: tuple[LineText, ...], sign: str, *, outside: bool) -> Counter[int]:
    lengths: Counter[int] = Counter()
    for line in lines:
        flat = line.flat
        index = 0
        while index < len(flat):
            if flat[index] != sign:
                index += 1
                continue
            end = index
            while end < len(flat) and flat[end] == sign:
                end += 1
            in_calendar = [is_calendar_stem(line, cursor) for cursor in range(index, end)]
            if outside and not any(in_calendar):
                lengths[end - index] += 1
            if not outside and all(in_calendar):
                lengths[end - index] += 1
            index = end
    return lengths


def _run_sites(lines: tuple[LineText, ...], sign: str, minimum: int) -> tuple[tuple[str, int, int], ...]:
    """(line, start, length) for outside runs of ``sign`` at least ``minimum`` long."""
    found: list[tuple[str, int, int]] = []
    for line in lines:
        flat = line.flat
        index = 0
        while index < len(flat):
            if flat[index] != sign:
                index += 1
                continue
            end = index
            while end < len(flat) and flat[end] == sign:
                end += 1
            if end - index >= minimum and not any(
                is_calendar_stem(line, cursor) for cursor in range(index, end)
            ):
                found.append((line.line_id, index, end - index))
            index = end
    return tuple(found)


def _sky_and_pairs(lines: tuple[LineText, ...], flats: dict[str, list[str]] | None = None) -> tuple[int, int, int, int]:
    """Sky-neighbor tokens, neighbor slots, 040-040 pairs, calendar-type neighbors.

    ``flats`` overrides the stem sequence and keeps the calendar mask on
    the original indexes. Counts use 040 stems sitting outside the calendar.
    """
    sky = 0
    slots = 0
    pairs = 0
    calendar_neighbors = 0
    anchors = build_anchors(lines)
    for line in lines:
        flat = flats[line.line_id] if flats is not None else list(line.flat)
        for index, sign in enumerate(flat):
            if sign != "040" or is_calendar_stem(line, index):
                continue
            for neighbor in (index - 1, index + 1):
                if not 0 <= neighbor < len(flat):
                    continue
                slots += 1
                if flat[neighbor] in SKY_OTHER:
                    sky += 1
                if flat[neighbor] in anchors.calendar_types and flat[neighbor] != "040":
                    calendar_neighbors += 1
        for index in range(len(flat) - 1):
            if flat[index] == flat[index + 1] == "040":
                if is_calendar_stem(line, index) or is_calendar_stem(line, index + 1):
                    continue
                pairs += 1
    return sky, slots, pairs, calendar_neighbors


def _region_null(lines: tuple[LineText, ...], observed: tuple[int, int, int]) -> tuple[NullCount, NullCount, NullCount]:
    rng = random.Random(REGION_SEED)
    ge_sky = ge_pairs = ge_calendar = 0
    for _ in range(REGION_TRIALS):
        flats: dict[str, list[str]] = {}
        for line in lines:
            flat = list(line.flat)
            _shuffle_spans(flat, region_spans(line), rng)
            flats[line.line_id] = flat
        sky, _slots, pairs, calendar_neighbors = _sky_and_pairs(lines, flats)
        if sky >= observed[0]:
            ge_sky += 1
        if pairs >= observed[1]:
            ge_pairs += 1
        if calendar_neighbors >= observed[2]:
            ge_calendar += 1
    return (
        NullCount(observed[0], ge_sky, REGION_TRIALS),
        NullCount(observed[1], ge_pairs, REGION_TRIALS),
        NullCount(observed[2], ge_calendar, REGION_TRIALS),
    )


def _outside_gram_counts(
    lines: tuple[LineText, ...],
    wanted: frozenset[tuple[str, ...]],
) -> Counter[tuple[str, ...]]:
    """Hits whose span is not entirely inside the calendar."""
    counts: Counter[tuple[str, ...]] = Counter()
    for line in lines:
        flat = line.flat
        flags = [is_calendar_stem(line, index) for index in range(len(flat))]
        for start in range(len(flat)):
            for width in range(2, 9):
                end = start + width
                if end > len(flat):
                    break
                if all(flags[start:end]):
                    continue
                gram = tuple(flat[start:end])
                if gram in wanted:
                    counts[gram] += 1
    return counts


def _separator_null(
    lines: tuple[LineText, ...],
    slices: tuple[tuple[str, ...], ...],
) -> dict[str, NullCount]:
    """Whole-line shuffle. Asks whether the outside hits are above chance."""
    long = frozenset(gram for gram in slices if len(gram) >= 3)
    named = frozenset({("670", "008"), ("375", "041")})
    wanted = long | named
    observed = _outside_gram_counts(lines, wanted)
    observed_ge3 = sum(observed[gram] for gram in long)
    rng = random.Random(SEPARATOR_SEED)
    ge_long = 0
    positive_long = 0
    ge_named = {gram: 0 for gram in named}
    for _ in range(SEPARATOR_TRIALS):
        shuffled: list[LineText] = []
        for line in lines:
            flat = list(line.flat)
            rng.shuffle(flat)
            shuffled.append(
                LineText(
                    side=line.side,
                    number=line.number,
                    groups=tuple(flat),
                    stems=tuple((stem,) for stem in flat),
                )
            )
        counts = _outside_gram_counts(tuple(shuffled), wanted)
        long_hits = sum(counts[gram] for gram in long)
        if long_hits >= observed_ge3:
            ge_long += 1
        if long_hits > 0:
            positive_long += 1
        for gram in named:
            if counts[gram] >= observed[gram]:
                ge_named[gram] += 1
    result = {
        "length_at_least_3": NullCount(observed_ge3, ge_long, SEPARATOR_TRIALS, positive_long)
    }
    for gram in (("670", "008"), ("375", "041")):
        result[" ".join(gram)] = NullCount(observed[gram], ge_named[gram], SEPARATOR_TRIALS)
    return result


def _phrase_sites(lines: tuple[LineText, ...], *, skip_gv6: bool) -> tuple[tuple, int, int]:
    sites: list[tuple] = []
    phrases_n = 0
    handoffs = 0
    for line in lines:
        if skip_gv6 and line.side == "Gv" and line.number == 6:
            continue
        phrases = extract_strict_phrases(line.groups, line.line_id)
        phrases_n += len(phrases)
        handoffs += chain_links(phrases)
        for phrase in phrases:
            sites.append((line.side, line.number, phrase.index, phrase.groups))
    sites.sort()
    return tuple(sites), phrases_n, handoffs


def _phrase_structure_null(lines: tuple[LineText, ...], observed_phrases: int, observed_links: int) -> tuple[NullCount, int]:
    """Shuffle groups inside each non-Gv6 line. ``links_ge`` counts trials with at least one handoff."""
    rng = random.Random(PHRASE_SEED)
    ge_phrases = 0
    trials_with_links = 0
    for _ in range(PHRASE_TRIALS):
        phrases_n = 0
        links = 0
        for line in lines:
            if line.side == "Gv" and line.number == 6:
                continue
            groups = list(line.groups)
            rng.shuffle(groups)
            phrases = extract_strict_phrases(groups, line.line_id)
            phrases_n += len(phrases)
            links += chain_links(phrases)
        if phrases_n >= observed_phrases:
            ge_phrases += 1
        if links >= 1:
            trials_with_links += 1
    return NullCount(observed_phrases, ge_phrases, PHRASE_TRIALS), trials_with_links


def _slot_null(groups: tuple[tuple[str, ...], ...]) -> tuple[int, int, NullCount]:
    """Groups with exactly one 076 and a host. Null puts that 076 in a random slot."""
    eligible = [group for group in groups if group.count("076") == 1 and len(group) >= 2]
    finals = sum(1 for group in eligible if group[-1] == "076")
    rng = random.Random(SLOT_SEED)
    ge = 0
    for _ in range(SLOT_TRIALS):
        got = sum(1 for group in eligible if rng.randrange(len(group)) == len(group) - 1)
        if got >= finals:
            ge += 1
    return len(eligible), finals, NullCount(finals, ge, SLOT_TRIALS)


def _outside_076_groups(
    lines: tuple[LineText, ...], anchors: Anchors, *, tablet: str | None
) -> tuple[tuple[str, ...], ...]:
    found: list[tuple[str, ...]] = []
    for line in lines:
        if tablet is not None and line.tablet != tablet:
            continue
        if tablet is None and line.tablet == "I":
            continue
        for group_index, stems in enumerate(line.stems):
            if "076" not in stems:
                continue
            if line.side == "Ia" and (line.number, group_index) in anchors.bracket_groups:
                continue
            if line.side == "Gv" and line.number == 6 and group_index in anchors.chain_groups:
                continue
            found.append(stems)
    return tuple(found)


def _role(stems: tuple[str, ...], sign: str) -> str:
    if sign not in stems:
        raise ValueError(sign)
    if len(stems) == 1:
        return "bare"
    if stems[-1] == sign:
        return "suffix"
    if stems[0] == sign:
        return "prefix"
    return "medial"


def _roles(lines: tuple[LineText, ...], anchors: Anchors, sign: str) -> Counter[str]:
    roles: Counter[str] = Counter()
    seen: set[tuple[str, int]] = set()
    for line in lines:
        group_indexes = line.group_index_of_stem()
        for index, token in enumerate(line.flat):
            if token != sign or anchors.stem_is_anchor(line, index, sign):
                continue
            group_index = group_indexes[index]
            key = (line.line_id, group_index)
            if key in seen:
                continue
            seen.add(key)
            roles[_role(line.stems[group_index], sign)] += 1
    return roles


@dataclass(frozen=True)
class TrackBReport:
    """Measurements. No field here is an adopted reading."""

    corpus_stems: int
    sign_totals: tuple[tuple[str, int], ...]
    anchor_stem_counts: tuple[tuple[str, str, int], ...]
    outside_by_tablet: tuple[tuple[str, tuple[int, ...]], ...]
    outside_positions: tuple[tuple[str, tuple[tuple[str, int], ...]], ...]
    outside_runs_040: tuple[tuple[int, int], ...]
    outside_run_sites_040: tuple[tuple[str, int, int], ...]
    frames_040: tuple[tuple[tuple[str, str], int], ...]
    frames_200: tuple[tuple[tuple[str, str], int], ...]
    frame_sites_040: tuple[tuple[tuple[str, str], tuple[str, ...]], ...]
    host_076: tuple[tuple[str, int], ...]
    sky_breakdown: tuple[tuple[str, int], ...]
    sky_slots: int
    sky_null: NullCount
    pair_null: NullCount
    calendar_neighbor_null: NullCount
    separator_outside: tuple[tuple[tuple[str, ...], int], ...]
    separator_inside_full: tuple[tuple[tuple[str, ...], int], ...]
    separator_null: tuple[tuple[str, NullCount], ...]
    phrase_sites: tuple[tuple, ...]
    phrase_handoffs: int
    phrase_null: NullCount
    phrase_trials_with_handoff: int
    gv6_chain: int
    gv6_handoffs: int
    gv6_quad: tuple[str, ...] | None
    slot_staff: tuple[int, int, NullCount]
    slot_other: tuple[int, int, NullCount]
    roles_076: tuple[tuple[str, int], ...]
    roles_200: tuple[tuple[str, int], ...]
    hypotheses: tuple[HypothesisScore, ...]
    inside_crib_hits: tuple[tuple[str, int], ...]
    lexicon_sizes: tuple[int, int, int]
    adopted_readings: tuple[str, ...]


def _score_hypothesis(
    hypothesis: Hypothesis,
    windows: tuple[tuple[str, ...], ...],
    open_lexicon: frozenset[tuple[str, ...]],
    targets: frozenset[tuple[str, ...]],
    open_random: tuple[int, ...],
    crib_random: tuple[int, ...],
    phrases: frozenset[tuple[tuple[str, ...], ...]],
) -> HypothesisScore:
    syllables = hypothesis.syllables()
    syllable_tuple = tuple(syllables[sign] for sign in SIGNS)
    open_counter = _score_windows(windows, syllables, open_lexicon)
    crib_counter = _score_windows(windows, syllables, targets)
    open_observed = sum(open_counter.values())
    crib_observed = sum(crib_counter.values())
    word_list = tuple(hypothesis.words()[sign] for sign in SIGNS)
    phrase_hits = _score_phrases(windows, hypothesis.words(), phrases)
    return HypothesisScore(
        name=hypothesis.name,
        syllables=tuple((sign, syllables[sign]) for sign in SIGNS),
        open_hits=tuple(sorted(open_counter.items(), key=lambda item: (-item[1], item[0]))),
        crib_hits=tuple(sorted(crib_counter.items(), key=lambda item: (-item[1], item[0]))),
        open_permutation=_permutation_null(windows, syllable_tuple, open_observed, open_lexicon),
        crib_permutation=_permutation_null(windows, syllable_tuple, crib_observed, targets),
        open_random=_null_from_scores(open_observed, open_random),
        crib_random=_null_from_scores(crib_observed, crib_random),
        phrase_hits=phrase_hits,
        phrase_permutation=_phrase_permutation_null(windows, word_list, phrase_hits, phrases),
    )


def run_round2_trackb(provider: MockProvider | None = None) -> TrackBReport:
    """Run the crib. The provider is not asked for a completion."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Round 2 Track B accepts MockProvider only")

    lines = load_lines()
    _guard_calendar(lines)
    anchors = build_anchors(lines)
    headwords = load_headwords()
    open_lexicon, _forms, targets = build_lexicon(headwords)
    windows = _windows(lines, anchors, outside=True)
    inside = _windows(lines, anchors, outside=False)
    phrases = _phrase_vocabulary(_word_sequences())
    syllable_types = tuple(sorted({piece for word in open_lexicon for piece in word}))
    open_random, crib_random = _random_scores(windows, syllable_types, open_lexicon, targets)

    sign_totals = tuple(
        (sign, sum(line.flat.count(sign) for line in lines)) for sign in SIGNS
    )
    anchor_counter: Counter[tuple[str, str]] = Counter()
    for line in lines:
        for index, sign in enumerate(line.flat):
            if sign not in SIGNS or not anchors.stem_is_anchor(line, index, sign):
                continue
            if sign in {"040", "143", "152"}:
                anchor_counter[(sign, "calendar")] += 1
            elif line.side == "Gv":
                anchor_counter[(sign, "gv6-chain")] += 1
            else:
                anchor_counter[(sign, "staff-bracket")] += 1

    outside = _outside_sign_counts(lines, anchors)
    positions: dict[str, Counter[str]] = {sign: Counter() for sign in SIGNS}
    for line in lines:
        flat = line.flat
        length = len(flat)
        for index, sign in enumerate(flat):
            if sign not in positions or anchors.stem_is_anchor(line, index, sign):
                continue
            if index == 0:
                positions[sign]["start"] += 1
            elif index + 1 == length:
                positions[sign]["end"] += 1
            else:
                positions[sign]["mid"] += 1
    position_rows = tuple(
        (sign, tuple(sorted(positions[sign].items()))) for sign in SIGNS
    )
    frames_040, sites_040 = _neighbor_frames(lines, anchors, "040")
    frames_200, _sites_200 = _neighbor_frames(lines, anchors, "200")
    repeated_040 = tuple(
        (pair, sites_040[pair]) for pair, count in frames_040.most_common() if count >= 4
    )
    runs = _run_lengths(lines, "040", outside=True)
    run_sites = _run_sites(lines, "040", 2)

    sky_sites: Counter[str] = Counter()
    for line in lines:
        flat = line.flat
        for index, sign in enumerate(flat):
            if sign != "040" or is_calendar_stem(line, index):
                continue
            for neighbor in (index - 1, index + 1):
                if 0 <= neighbor < len(flat) and flat[neighbor] in SKY_OTHER:
                    sky_sites[flat[neighbor]] += 1
    sky, slots, pairs, calendar_neighbors = _sky_and_pairs(lines)
    sky_null, pair_null, calendar_null = _region_null(lines, (sky, pairs, calendar_neighbors))

    slices = separator_slices()
    outside_counts = _outside_gram_counts(lines, frozenset(slices))
    outside_slices = tuple(
        (gram, outside_counts[gram]) for gram in slices if outside_counts[gram]
    )
    inside_full = tuple(
        (gram, _count_slice(lines, gram, outside=False)) for gram in SEPARATORS
    )
    separator_null = _separator_null(lines, slices)

    gv6 = next(line for line in lines if line.side == "Gv" and line.number == 6)
    gv6_phrases = extract_strict_phrases(gv6.groups, gv6.line_id)
    quads = extract_quad_phrases(gv6.groups, gv6.line_id)
    sites, phrase_n, handoffs = _phrase_sites(lines, skip_gv6=True)
    phrase_null, trials_with_links = _phrase_structure_null(lines, phrase_n, handoffs)

    staff_groups = _outside_076_groups(lines, anchors, tablet="I")
    other_groups = _outside_076_groups(lines, anchors, tablet=None)
    slot_staff = _slot_null(staff_groups)
    slot_other = _slot_null(other_groups)

    hosts: Counter[str] = Counter()
    # Ligature host on the Staff only. Off-staff 076 is in the slot test.
    for line in lines:
        if line.side != "Ia":
            continue
        group_indexes = line.group_index_of_stem()
        for index, sign in enumerate(line.flat):
            if sign != "076" or anchors.stem_is_anchor(line, index, sign):
                continue
            if index == 0:
                continue
            if group_indexes[index] == group_indexes[index - 1]:
                hosts[line.flat[index - 1]] += 1

    scored = tuple(
        _score_hypothesis(
            hypothesis,
            windows,
            open_lexicon,
            targets,
            open_random,
            crib_random,
            phrases,
        )
        for hypothesis in hypotheses()
    )
    inside_crib: Counter[str] = Counter()
    for hypothesis in hypotheses():
        inside_crib[hypothesis.name] = sum(
            _score_windows(inside, hypothesis.syllables(), targets).values()
        )

    adopted = tuple(item.name for item in scored if item.reading_adopted or item.phrase_permutation.survives)
    return TrackBReport(
        corpus_stems=sum(len(line.flat) for line in lines),
        sign_totals=sign_totals,
        anchor_stem_counts=tuple(sorted(anchor_counter.items())),
        outside_by_tablet=tuple((sign, outside[sign]) for sign in SIGNS),
        outside_positions=position_rows,
        outside_runs_040=tuple(sorted(runs.items())),
        outside_run_sites_040=run_sites,
        frames_040=tuple(frames_040.most_common()),
        frames_200=tuple(frames_200.most_common()),
        frame_sites_040=repeated_040,
        host_076=tuple(hosts.most_common(8)),
        sky_breakdown=tuple(sorted(sky_sites.items())),
        sky_slots=slots,
        sky_null=sky_null,
        pair_null=pair_null,
        calendar_neighbor_null=calendar_null,
        separator_outside=outside_slices,
        separator_inside_full=inside_full,
        separator_null=tuple(separator_null.items()),
        phrase_sites=sites,
        phrase_handoffs=handoffs,
        phrase_null=phrase_null,
        phrase_trials_with_handoff=trials_with_links,
        gv6_chain=len(gv6_phrases),
        gv6_handoffs=chain_links(gv6_phrases),
        gv6_quad=quads[0].groups if quads else None,
        slot_staff=slot_staff,
        slot_other=slot_other,
        roles_076=tuple(sorted(_roles(lines, anchors, "076").items())),
        roles_200=tuple(sorted(_roles(lines, anchors, "200").items())),
        hypotheses=scored,
        inside_crib_hits=tuple(sorted(inside_crib.items())),
        lexicon_sizes=(len(open_lexicon), len(targets), len(syllable_types)),
        adopted_readings=adopted,
    )

