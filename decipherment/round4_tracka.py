"""Round 4 Track A: pictographic meanings and a rebus test.

The sign list, the semantic classes, the two rebus maps, the hit
definition, the nulls, and the gates below were fixed before the
scores were read. ``MockProvider`` is accepted and never called.
No Barthel number is invented. A word is either a published proposal
or marked ``HYPOTHESIS``. A statistical gate is not a translation:
``reading`` stays None unless the pre-registered adoption rule passes.
"""

from __future__ import annotations

import json
import random
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable

from agents.base.providers import MockProvider
from decipherment.old_rapanui import (
    cv_syllables_mapped,
    lexicon_headwords,
    primary_running_lines,
    word_lines_of,
)
from decipherment.rapanui import load_wikipedia_word_lines
from decipherment.round2_trackb import is_calendar_stem, load_headwords, load_lines
from decipherment.track3_genealogy import extract_quad_phrases, extract_strict_phrases, group_stems
from decipherment.track_c_parallels import JSON_PATH, load_side_texts, smith_waterman

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs" / "decipherment"
OUT_JSON = REPO_ROOT / "data" / "decipherment" / "round4a_pictograph_rebus.json"
OUT_MD = DOCS_DIR / "round4a_pictograph_rebus.md"

# Pre-registered gates. Not retuned after the scores.
PAIR_TRIALS = 500
PAIR_SEED = 40
SLOT_TRIALS = 500
SLOT_SEED = 41
REBUS_TRIALS = 500
REBUS_SEED_R1 = 42
REBUS_SEED_R2 = 43
ADOPT_FRACTION = 0.05
CONTEXT_NAMES = ("calendar", "gv6", "parallels")
CONTEXT_BONFERRONI = ADOPT_FRACTION / len(CONTEXT_NAMES)
CLASS_BONFERRONI = ADOPT_FRACTION / 6
WINDOW_LENGTHS = (2, 3, 4)
FORMULA_MIN_STRICT = 4

# Testable co-occurrence classes (at least two different signs).
# plant and lizard are single signs; they are counted and not gated.
TESTABLE_CLASSES = ("moon", "hand", "bird", "sea", "human", "human_gaping")

# 064 is Pozdniakov's hand allograph of 006. It copies 006's word.
# It is not a separate item in the permutation.
HAND_ALIAS = {"064": "006"}


@dataclass(frozen=True)
class Pictograph:
    """One cited picture. ``word`` is empty when no value is assigned."""

    stem: str
    icon: str
    semantic_class: str
    icon_confidence: str
    word: str
    word_label: str
    rebus: str
    source: str


# Order is the report order. rebus "R1" is also included in R2.
# rebus "R2" is the sensitivity map only. rebus "" is not sounded.
PICTOGRAPHS: tuple[Pictograph, ...] = (
    Pictograph(
        "040",
        "Crescent. In the Mamari calendar, the repeated night sign.",
        "moon",
        "high",
        "marama",
        "HYPOTHESIS",
        "R1",
        "Guy 1990, JSO 91: 135–149: glyph 40A is the repeated night sign. "
        "Guy 2006, Rapa Nui Journal 20(1): glyph 40 is a crescent, and glyph 42 "
        "is that crescent rotated in one stacked pair (not applied to every 042). "
        "The word marama is the ordinary noun 'moon' (Metoro, vendored ca06–ca09; "
        "Churchill 1912 headword). Guy does not read the sign as that word. "
        "HYPOTHESIS: object-noun for the picture.",
    ),
    Pictograph(
        "041",
        "Mirror-image crescent. Guy's calendar delimiter uses it; he does not count it as a night.",
        "moon",
        "high",
        "",
        "",
        "",
        "Guy 2006, Rapa Nui Journal 20(1): the signs under 41 are the mirror image of those under 40. "
        "Guy 1990: delimiter crescents are not nights. No separate word is assigned.",
    ),
    Pictograph(
        "143",
        "Deep filled crescent, the night before the full-moon sign.",
        "moon",
        "medium",
        "rakau",
        "HYPOTHESIS",
        "R1",
        "Guy 1990: a deep filled crescent immediately before glyph 152. "
        "Horley 2011, JSO 132: 17–38, agrees 152 is full moon. "
        "The Track 1 alignment of the Thomson / Englert / Métraux lists puts rakau "
        "on the night before omotohi. HYPOTHESIS: that night-name, not a phonetic proof.",
    ),
    Pictograph(
        "152",
        "Figure seated in an oval: the full-moon sign, Guy's 'man in the moon'.",
        "moon",
        "medium-high",
        "omotohi",
        "HYPOTHESIS",
        "R1",
        "Guy 1990 and Horley 2011: sign 152 is full moon. "
        "Guy 2006: an anthropomorphic figure seated above a heap of stones inside an ovoid, "
        "the cook in the moon. The word omotohi is the recorded full-moon night name "
        "(Thomson 1891; Englert's list as already printed in Track 1). "
        "HYPOTHESIS: the night name at that slot.",
    ),
    Pictograph(
        "200",
        "Human figure with a lozenge head and side protrusions. Guy's 'Big Ears'.",
        "human",
        "high",
        "tangata",
        "published_hypothesis",
        "R1",
        "Barthel 1958: 40–41, via Guy 2006: series 200–299 are headed figures with ears or eyes. "
        "Wikipedia 'Rongorongo' groups glyph 200 with that head shape. "
        "Butinov and Knorozov 1957, JPS 66: 5–17, and Davletshin 2012, JSO 134: 95–110, "
        "treat 200 as a man or a title. The word tangata is that proposal. "
        "Guy 2006 also argues the head behaves as a taxogram, which is a different claim.",
    ),
    Pictograph(
        "300",
        "Anthropomorph with a round head and a gaping mouth, the head of Barthel's 300 series.",
        "human_gaping",
        "high",
        "",
        "",
        "",
        "Barthel 1958: 40–41, via Guy 2006 and the kohaumotu summary already cited in "
        "decipherment/allographs.py: series 300–399 have a round head and a gaping mouth. "
        "No agreed Rapanui word.",
    ),
    Pictograph(
        "400",
        "Bird-bodied figure. Guy: the first ten signs of series 400 are birds.",
        "bird",
        "medium-high",
        "",
        "",
        "",
        "Guy 2006: glyph 400 has the head of series 300 and the body of a bird; "
        "glyphs 400–409 are clear depictions of a bird. No separate word is assigned. "
        "Reading it as tangata manu would be an uncited extra.",
    ),
    Pictograph(
        "600",
        "Bird, the head of Barthel's ornithomorphic series.",
        "bird",
        "high",
        "manu",
        "HYPOTHESIS",
        "R1",
        "Barthel 1958: 40–41, via Guy 2006: series 600–699 are ornithomorphic. "
        "Wikipedia 'Rongorongo': the hundreds digit 6 is figures with beaks. "
        "The word manu is the ordinary noun 'bird' (Churchill 1912 headword). "
        "HYPOTHESIS: object-noun. Not a claim that every 600-series sign is this one species.",
    ),
    Pictograph(
        "680",
        "Double-headed frigatebird.",
        "bird",
        "medium-high",
        "makohe",
        "HYPOTHESIS",
        "R1",
        "Wikipedia 'Rongorongo', citing McLaughlin 2004, Rapa Nui Journal 18: 87–94, "
        "and Lee 1992: glyph 680 is a double-headed frigatebird, also on a moai topknot. "
        "Horley 2005 maps long-beak heads 661–684 to 660, so 680 may be an allograph of a "
        "long-beaked bird rather than its own logogram. The word makohe is the Churchill 1912 "
        "headword for the frigatebird. HYPOTHESIS: object-noun.",
    ),
    Pictograph(
        "700",
        "Fish.",
        "sea",
        "high",
        "ika",
        "HYPOTHESIS",
        "R1",
        "Guy 2006: 700 has been suggested as a fish. "
        "Wikipedia 'Rongorongo': hundreds digit 7 is fish, arthropods, and the like, "
        "and human skulls carry the single fish glyph 700, which may stand for ika "
        "'war casualty; fish'. The homophone is the ethnographic name kohau ika in that article. "
        "HYPOTHESIS: the word ika (Churchill 1912; Wikipedia lang=rap). The casualty sense is the same word.",
    ),
    Pictograph(
        "721",
        "Shark. Guy reports the suggestion and does not name its author.",
        "sea",
        "medium",
        "",
        "",
        "",
        "Guy 2006: 721 has been suggested as a shark. No Rapanui word is assigned. "
        "The English gloss is not turned into a headword that is absent from the vendored lexicon.",
    ),
    Pictograph(
        "760",
        "Lizard. Guy reports the suggestion and does not name its author.",
        "lizard",
        "medium",
        "moko",
        "HYPOTHESIS",
        "R2",
        "Guy 2006: 760 has been suggested as a lizard. Not in the widely agreed set, "
        "because he marks it as a suggestion. The word moko is the Churchill 1912 headword. "
        "HYPOTHESIS: object-noun. Sensitivity map R2 only.",
    ),
    Pictograph(
        "006",
        "Hand with three fingers and a thumb.",
        "hand",
        "high",
        "rima",
        "HYPOTHESIS",
        "R1",
        "Guy 2006: isolated glyph 6 is the same shape as hand 6 (lifted, three fingers and a thumb). "
        "Pozdniakov 1996, JSO 103: 296: hands 6 and 64 substitute in repeated phrases. "
        "The word rima is the Churchill 1912 headword and the Track 1 numeral rima. "
        "HYPOTHESIS: object-noun 'hand', which is homophonous with the numeral five. "
        "Neither Guy nor Pozdniakov prints that reading.",
    ),
    Pictograph(
        "064",
        "Forked hand. Allograph of 006 in repeated phrases.",
        "hand",
        "high",
        "rima",
        "HYPOTHESIS",
        "alias",
        "Pozdniakov 1996: 296 and Guy 2006: hand 4 alternates with hand 6. "
        "The rebus copies the word assigned to 006. 064 is not its own permutation item.",
    ),
    Pictograph(
        "061",
        "Lifted hand, turned inward, three fingers. Guy's hand shape 1.",
        "hand",
        "high",
        "",
        "",
        "",
        "Guy 2006, Figure 10d: glyphs 61–64 are the same shapes as hands 1–4. "
        "No separate word. Isolated digits 1–5 and 7 are different signs, and they are not put in this class.",
    ),
    Pictograph(
        "062",
        "Lifted hand clenched in a fist. Guy's hand shape 2.",
        "hand",
        "high",
        "",
        "",
        "",
        "Guy 2006, Figure 10d: glyph 62 is hand shape 2, a lifted fist. No separate Rapanui word is assigned.",
    ),
    Pictograph(
        "063",
        "Lifted hand pointing down. Guy's hand shape 3.",
        "hand",
        "high",
        "",
        "",
        "",
        "Guy 2006, Figure 10d. No separate word. Not read as an adze.",
    ),
    Pictograph(
        "067",
        "Palm. Barthel's identification, later tied to the Jaussen list's niu.",
        "plant",
        "medium",
        "niu",
        "contested",
        "R2",
        "Wikipedia 'Rongorongo', note 6, citing Barthel 1958: 66: glyph 67 is thought to "
        "represent the extinct Easter Island palm. The same note says the Jaussen list "
        "identified it as the niu coconut palm, a species introduced after contact. "
        "Contested. Sensitivity map R2 only. niu is not a Churchill headword in the vendored list.",
    ),
    Pictograph(
        "076",
        "Phallus, if Fischer is right. Guy treats the genealogy suffix as a patronym instead.",
        "contested",
        "low",
        "ure",
        "published_hypothesis",
        "R2",
        "Fischer 1995 and 1997: 076 is a phallic suffix. "
        "Davletshin 2012: patronymic ure. Guy 1998, Anthropos 93: 552–555, rejects Fischer's "
        "cosmogonic reading. The picture is not widely agreed. Sensitivity map R2 only. "
        "The word ure is in Thomson and in Churchill 1912.",
    ),
    Pictograph(
        "008",
        "Conflicting nicknames: Guy's flower, Fischer's sun in one Staff triad.",
        "",
        "low",
        "",
        "",
        "",
        "Guy 2006 uses glyph 8 as a nickname 'flower'. "
        "Fischer's Staff example, already locked in Track 3 as 606.076 700 008, glosses one 008 as the sun. "
        "The two claims disagree. No class and no word.",
    ),
)

# Signs deliberately absent. Stated so a later edit cannot smuggle a number in.
OMITTED = (
    {
        "picture": "canoe",
        "reason": (
            "No Barthel number for a canoe is stated by Barthel 1958 as cited here, "
            "Guy 1990, Guy 2006, Horley 2011, Davletshin 2012, or the Wikipedia glyph notes used above. "
            "The Churchill headword vaka is not attached to a sign."
        ),
    },
    {
        "picture": "sea turtle",
        "reason": (
            "Wikipedia mentions a sea-turtle glyph in a caption and does not give a Barthel number in the prose. "
            "Glyph 280 is described there with glyph 200 as a headed figure, and Horley 2005 decomposes 280 as 070.002. "
            "It is not entered as a turtle. The Churchill headword honu is not attached to a sign."
        ),
    },
    {
        "picture": "Guy 2006 calendar phonograms atua, hua, hiro/ro",
        "reason": (
            "Guy 2006 proposes a feather-cloak sign for atua, a fruit or scrotum sign for hua, "
            "and glyph 3 or 30 for ro or hiro. The prose does not lock those pictures to a "
            "Barthel number that this track can separate from the plate. They are not encoded."
        ),
    },
)


def class_of(stem: str) -> str | None:
    """Iconographic class. Specific signs override the hundreds digit.

    042 is not a moon sign: Guy's rotation claim is one stacked pair.
    760 is the suggested lizard, not a sea creature.
    Series 400–409 are birds (Guy 2006). Series 410–599 are not classed:
    Guy says the digit system breaks down there.
    """
    if stem in {"040", "041", "143", "152"}:
        return "moon"
    if stem in {"006", "061", "062", "063", "064"}:
        return "hand"
    if stem == "067":
        return "plant"
    if stem == "760":
        return "lizard"
    if not stem.isdigit():
        return None
    number = int(stem)
    if 400 <= number <= 409 or 600 <= number <= 699:
        return "bird"
    if 700 <= number <= 759 or 770 <= number <= 799:
        return "sea"
    if 200 <= number <= 299:
        return "human"
    if 300 <= number <= 399:
        return "human_gaping"
    return None


def _r1_words() -> dict[str, str]:
    return {row.stem: row.word for row in PICTOGRAPHS if row.rebus == "R1"}


def _r2_words() -> dict[str, str]:
    words = _r1_words()
    for row in PICTOGRAPHS:
        if row.rebus == "R2":
            words[row.stem] = row.word
    return words


def _resolve(stem: str) -> str:
    return HAND_ALIAS.get(stem, stem)


def _grams(run: list[str]) -> list[tuple[str, ...]]:
    grams: list[tuple[str, ...]] = []
    for width in WINDOW_LENGTHS:
        if len(run) < width:
            continue
        for start in range(len(run) - width + 1):
            grams.append(tuple(run[start : start + width]))
    return grams


def windows_in(stems: Iterable[str], vocabulary: set[str]) -> list[tuple[str, ...]]:
    """Contiguous runs whose every sign has a word. Unmapped signs break the run."""
    run: list[str] = []
    grams: list[tuple[str, ...]] = []
    for stem in stems:
        key = _resolve(stem)
        if key in vocabulary:
            run.append(key)
            continue
        grams.extend(_grams(run))
        run = []
    grams.extend(_grams(run))
    return grams


def _pair_counts(rows: list[list[str]], step: int) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        limit = len(row) - step
        for index in range(limit):
            left = row[index]
            right = row[index + step]
            if left == right:
                continue
            klass = class_of(left)
            if klass is None or klass not in TESTABLE_CLASSES:
                continue
            if class_of(right) == klass:
                counts[klass] += 1
    return counts


def _shuffle_rows(rows: list[list[str]], rng: random.Random) -> list[list[str]]:
    shuffled: list[list[str]] = []
    for row in rows:
        copy = list(row)
        rng.shuffle(copy)
        shuffled.append(copy)
    return shuffled


def _null_pair(
    rows: list[list[str]],
    observed: Counter[str],
    *,
    seed: int,
) -> dict[str, Any]:
    rng = random.Random(seed)
    sum_ge = 0
    class_ge = {name: 0 for name in TESTABLE_CLASSES}
    step2_ge = 0
    step2_class_ge = {name: 0 for name in TESTABLE_CLASSES}
    observed_sum = sum(observed.values())
    # The secondary distance is counted on the same draws. The first pass
    # records the unshuffled step-2 total before the loop consumes the seed.
    step2_observed = _pair_counts(rows, 2)
    observed_step2 = sum(step2_observed.values())
    for _trial in range(PAIR_TRIALS):
        shuffled = _shuffle_rows(rows, rng)
        counts = _pair_counts(shuffled, 1)
        if sum(counts.values()) >= observed_sum:
            sum_ge += 1
        for name in TESTABLE_CLASSES:
            if counts[name] >= observed[name]:
                class_ge[name] += 1
        counts2 = _pair_counts(shuffled, 2)
        if sum(counts2.values()) >= observed_step2:
            step2_ge += 1
        for name in TESTABLE_CLASSES:
            if counts2[name] >= step2_observed[name]:
                step2_class_ge[name] += 1
    return _pack_pairs(
        observed,
        observed_sum,
        sum_ge,
        class_ge,
        step2_observed,
        observed_step2,
        step2_ge,
        step2_class_ge,
        seed,
    )


def _pack_pairs(
    observed: Counter[str],
    observed_sum: int,
    sum_ge: int,
    class_ge: dict[str, int],
    step2_observed: Counter[str],
    observed_step2: int,
    step2_ge: int,
    step2_class_ge: dict[str, int],
    seed: int,
) -> dict[str, Any]:
    fraction = sum_ge / PAIR_TRIALS
    classes = []
    for name in TESTABLE_CLASSES:
        class_fraction = class_ge[name] / PAIR_TRIALS
        classes.append(
            {
                "class": name,
                "adjacent_different_signs": observed[name],
                "null_ge": class_ge[name],
                "null_fraction": class_fraction,
                "p_add_one": (class_ge[name] + 1) / (PAIR_TRIALS + 1),
                "holds_bonferroni": observed[name] > 0 and class_fraction <= CLASS_BONFERRONI,
            }
        )
    return {
        "statistic": "adjacent different signs of the same class, summed",
        "observed": observed_sum,
        "by_class": classes,
        "trials": PAIR_TRIALS,
        "seed": seed,
        "null_ge": sum_ge,
        "null_fraction": fraction,
        "p_add_one": (sum_ge + 1) / (PAIR_TRIALS + 1),
        "holds": observed_sum > 0 and fraction <= ADOPT_FRACTION,
        "step2": {
            "statistic": "same, two signs apart, secondary, same draws",
            "observed": observed_step2,
            "by_class": [
                {
                    "class": name,
                    "pairs": step2_observed[name],
                    "null_ge": step2_class_ge[name],
                    "null_fraction": step2_class_ge[name] / PAIR_TRIALS,
                }
                for name in TESTABLE_CLASSES
            ],
            "null_ge": step2_ge,
            "null_fraction": step2_ge / PAIR_TRIALS,
            "p_add_one": (step2_ge + 1) / (PAIR_TRIALS + 1),
            "gated": False,
            "holds_if_it_were_gated": observed_step2 > 0 and (step2_ge / PAIR_TRIALS) <= ADOPT_FRACTION,
        },
    }


def _language() -> tuple[set[tuple[str, ...]], dict[int, Counter[tuple[tuple[str, ...], ...]]], dict[str, int]]:
    """Attested word shapes, running-text formulae, and word counts.

    Formulae are counted inside a line of the primary running text only.
    Lexicon headwords and the crib list can make a word hit. They do not
    make a phrase hit.
    """
    shapes: set[tuple[str, ...]] = set()
    word_counts: Counter[str] = Counter()
    syllable_lines: list[list[tuple[str, ...]]] = []
    for line in word_lines_of(primary_running_lines()):
        syllables: list[tuple[str, ...]] = []
        for word in line:
            parsed = cv_syllables_mapped(word)
            if not parsed:
                continue
            shapes.add(parsed)
            syllables.append(parsed)
            word_counts["".join(parsed)] += 1
        if syllables:
            syllable_lines.append(syllables)
    for item in lexicon_headwords():
        parsed = cv_syllables_mapped(item.word)
        if parsed:
            shapes.add(parsed)
    for line in load_wikipedia_word_lines():
        for word in line:
            parsed = cv_syllables_mapped(word)
            if parsed:
                shapes.add(parsed)
    for word, _citation in load_headwords():
        parsed = cv_syllables_mapped(word)
        if parsed:
            shapes.add(parsed)
    formulae = {2: Counter(), 3: Counter(), 4: Counter()}
    for line in syllable_lines:
        for width in WINDOW_LENGTHS:
            if len(line) < width:
                continue
            bucket = formulae[width]
            for start in range(len(line) - width + 1):
                bucket[tuple(line[start : start + width])] += 1
    return shapes, formulae, dict(word_counts)


def _score_windows(
    windows: list[tuple[str, ...]],
    words: dict[str, str],
    syllables: dict[str, tuple[str, ...]],
    shapes: set[tuple[str, ...]],
    formulae: dict[int, Counter[tuple[tuple[str, ...], ...]]],
) -> dict[str, Any]:
    hits = 0
    diverse_hits = 0
    word_hits = 0
    phrase_hits = 0
    strict_hits = 0
    window_counts: Counter[str] = Counter()
    corpus_counts: dict[str, int] = {}
    for gram in windows:
        parts = tuple(syllables[sign] for sign in gram)
        flat = tuple(piece for part in parts for piece in part)
        phrase_count = formulae[len(gram)][parts] if len(gram) in formulae else 0
        is_word = flat in shapes
        is_phrase = phrase_count >= 1
        if is_word:
            word_hits += 1
        if is_phrase:
            phrase_hits += 1
        if phrase_count >= FORMULA_MIN_STRICT:
            strict_hits += 1
        if not (is_word or is_phrase):
            continue
        hits += 1
        if len(set(words[sign] for sign in gram)) >= 2:
            diverse_hits += 1
        text = " ".join(words[sign] for sign in gram)
        window_counts[text] += 1
        corpus_counts[text] = max(corpus_counts.get(text, 0), phrase_count)
    examples = [
        {"phrase": text, "windows": count, "running_text": corpus_counts[text]}
        for text, count in window_counts.most_common(8)
    ]
    return {
        "windows": len(windows),
        "hits": hits,
        "diverse_hits": diverse_hits,
        "word_hits": word_hits,
        "phrase_hits": phrase_hits,
        "strict_formula_hits": strict_hits,
        "hit_rate": (hits / len(windows)) if windows else 0.0,
        "examples": examples,
    }


def _rebus_null(
    windows_by_context: dict[str, list[tuple[str, ...]]],
    words: dict[str, str],
    shapes: set[tuple[str, ...]],
    formulae: dict[int, Counter[tuple[tuple[str, ...], ...]]],
    *,
    seed: int,
    can_adopt: bool,
) -> dict[str, Any]:
    signs = tuple(words)
    values = [words[sign] for sign in signs]
    syllables = {word: cv_syllables_mapped(word) for word in values}
    for word, parsed in syllables.items():
        if not parsed:
            raise ValueError(f"rebus word {word!r} is not mapped (C)V")
    base_syllables = {sign: syllables[words[sign]] for sign in signs}
    observed_parts = {
        name: _score_windows(windows_by_context[name], words, base_syllables, shapes, formulae)
        for name in CONTEXT_NAMES
    }
    observed_hits = sum(part["hits"] for part in observed_parts.values())
    observed_diverse = sum(part["diverse_hits"] for part in observed_parts.values())
    rng = random.Random(seed)
    ge_hits = 0
    ge_diverse = 0
    ge_context = {name: 0 for name in CONTEXT_NAMES}
    null_hits: list[int] = []
    for _trial in range(REBUS_TRIALS):
        shuffled = list(values)
        rng.shuffle(shuffled)
        assignment = dict(zip(signs, shuffled))
        trial_syllables = {sign: syllables[assignment[sign]] for sign in signs}
        trial_hits = 0
        trial_diverse = 0
        for name in CONTEXT_NAMES:
            scored = _score_windows(
                windows_by_context[name],
                assignment,
                trial_syllables,
                shapes,
                formulae,
            )
            trial_hits += scored["hits"]
            trial_diverse += scored["diverse_hits"]
            if scored["hits"] >= observed_parts[name]["hits"]:
                ge_context[name] += 1
        null_hits.append(trial_hits)
        if trial_hits >= observed_hits:
            ge_hits += 1
        if trial_diverse >= observed_diverse:
            ge_diverse += 1
    hit_fraction = ge_hits / REBUS_TRIALS
    diverse_fraction = ge_diverse / REBUS_TRIALS
    contexts = []
    for name in CONTEXT_NAMES:
        fraction = ge_context[name] / REBUS_TRIALS
        part = dict(observed_parts[name])
        part["context"] = name
        part["null_ge"] = ge_context[name]
        part["null_fraction"] = fraction
        part["p_add_one"] = (ge_context[name] + 1) / (REBUS_TRIALS + 1)
        part["holds_bonferroni"] = part["hits"] > 0 and fraction <= CONTEXT_BONFERRONI
        contexts.append(part)
    total_windows = sum(part["windows"] for part in observed_parts.values())
    return {
        "signs": list(signs),
        "words": dict(words),
        "windows": total_windows,
        "hits": observed_hits,
        "hit_rate": (observed_hits / total_windows) if total_windows else 0.0,
        "diverse_hits": observed_diverse,
        "null_ge": ge_hits,
        "null_fraction": hit_fraction,
        "p_add_one": (ge_hits + 1) / (REBUS_TRIALS + 1),
        "null_mean_hits": (sum(null_hits) / len(null_hits)) if null_hits else 0.0,
        "holds": observed_hits > 0 and hit_fraction <= ADOPT_FRACTION,
        "diverse_null_ge": ge_diverse,
        "diverse_null_fraction": diverse_fraction,
        "diverse_p_add_one": (ge_diverse + 1) / (REBUS_TRIALS + 1),
        "diverse_holds": observed_diverse > 0 and diverse_fraction <= ADOPT_FRACTION,
        "adopted": bool(can_adopt)
        and observed_hits > 0
        and hit_fraction <= ADOPT_FRACTION
        and observed_diverse > 0
        and diverse_fraction <= ADOPT_FRACTION,
        "contexts": contexts,
        "trials": REBUS_TRIALS,
        "seed": seed,
    }


def _attestation(words: dict[str, str], shapes: set[tuple[str, ...]], word_counts: dict[str, int]) -> list[dict[str, Any]]:
    rows = []
    for sign, word in words.items():
        parsed = cv_syllables_mapped(word)
        key = "".join(parsed) if parsed else ""
        rows.append(
            {
                "sign": sign,
                "word": word,
                "syllables": list(parsed) if parsed else [],
                "in_word_list": parsed in shapes if parsed else False,
                "running_text_count": word_counts.get(key, 0),
            }
        )
    return rows


def _slot_pairs(passages: list[dict[str, Any]], texts: dict[str, Any]) -> tuple[list[tuple[str, str]], dict[str, int]]:
    pairs: list[tuple[str, str]] = []
    published_mismatches = 0
    realigned_mismatches = 0
    realigned_columns = 0
    for passage in passages:
        published_mismatches += int(passage["mismatches"])
        left = texts[passage["left"]["side"]].signs
        right = texts[passage["right"]["side"]].signs
        seq_a = left[passage["left"]["start"] : passage["left"]["end"] + 1]
        seq_b = right[passage["right"]["start"] : passage["right"]["end"] + 1]
        _score, _a0, _a1, _b0, _b1, columns = smith_waterman(seq_a, seq_b)
        realigned_columns += len(columns)
        for sign_a, sign_b in columns:
            if sign_a is None or sign_b is None or sign_a == sign_b:
                continue
            realigned_mismatches += 1
            pairs.append((sign_a, sign_b))
    meta = {
        "passages": len(passages),
        "published_mismatches": published_mismatches,
        "realigned_mismatches": realigned_mismatches,
        "realigned_columns": realigned_columns,
    }
    return pairs, meta


def _classify_pairs(pairs: list[tuple[str, str]], lookup: Callable[[str], str | None]) -> dict[str, int]:
    classified = 0
    same = 0
    cross = 0
    cross_same = 0
    for left, right in pairs:
        left_class = lookup(left)
        right_class = lookup(right)
        if left_class is None or right_class is None:
            continue
        classified += 1
        shared = left_class == right_class
        if shared:
            same += 1
        if int(left) // 100 != int(right) // 100:
            cross += 1
            if shared:
                cross_same += 1
    return {
        "classified_mismatch_pairs": classified,
        "same_class": same,
        "cross_hundred_classified": cross,
        "cross_hundred_same_class": cross_same,
    }


def _slot_null(pairs: list[tuple[str, str]], observed: dict[str, int]) -> dict[str, Any]:
    typed = sorted(stem for stem in {sign for pair in pairs for sign in pair} if class_of(stem))
    # Permute every classified stem that occurs in a mismatch column.
    # Stems that the class function does not label stay unlabeled.
    labels = [class_of(stem) for stem in typed]
    rng = random.Random(SLOT_SEED)
    ge_same = 0
    ge_cross = 0
    for _trial in range(SLOT_TRIALS):
        shuffled = list(labels)
        rng.shuffle(shuffled)
        lookup = dict(zip(typed, shuffled))
        scored = _classify_pairs(pairs, lookup.get)
        if scored["same_class"] >= observed["same_class"]:
            ge_same += 1
        if scored["cross_hundred_same_class"] >= observed["cross_hundred_same_class"]:
            ge_cross += 1
    same_fraction = ge_same / SLOT_TRIALS
    cross_fraction = ge_cross / SLOT_TRIALS
    return {
        "trials": SLOT_TRIALS,
        "seed": SLOT_SEED,
        "same_class": {
            "observed": observed["same_class"],
            "classified_pairs": observed["classified_mismatch_pairs"],
            "rate": (
                observed["same_class"] / observed["classified_mismatch_pairs"]
                if observed["classified_mismatch_pairs"]
                else 0.0
            ),
            "null_ge": ge_same,
            "null_fraction": same_fraction,
            "p_add_one": (ge_same + 1) / (SLOT_TRIALS + 1),
            "note": "Includes substitutions inside one Barthel hundred. Not the semantic gate.",
            "holds": False,
        },
        "cross_hundred": {
            "observed": observed["cross_hundred_same_class"],
            "classified_pairs": observed["cross_hundred_classified"],
            "rate": (
                observed["cross_hundred_same_class"] / observed["cross_hundred_classified"]
                if observed["cross_hundred_classified"]
                else 0.0
            ),
            "null_ge": ge_cross,
            "null_fraction": cross_fraction,
            "p_add_one": (ge_cross + 1) / (SLOT_TRIALS + 1),
            "holds": observed["cross_hundred_same_class"] > 0 and cross_fraction <= ADOPT_FRACTION,
        },
    }


def _same_sign_adjacency(rows: list[list[str]], stem: str) -> int:
    total = 0
    for row in rows:
        for index in range(len(row) - 1):
            if row[index] == stem and row[index + 1] == stem:
                total += 1
    return total


def _gv6_gloss(lines, words: dict[str, str]) -> list[dict[str, Any]]:
    line = next(item for item in lines if item.side == "Gv" and item.number == 6)
    rows = []
    for phrase in extract_strict_phrases(line.groups, "Gv6"):
        stems = [stem for group in phrase.groups for stem in group_stems(group)]
        rows.append(
            {
                "kind": "strict",
                "groups": list(phrase.groups),
                "stems": stems,
                "mapped": [_resolve(stem) if _resolve(stem) in words else None for stem in stems],
            }
        )
    for phrase in extract_quad_phrases(line.groups, "Gv6"):
        stems = [stem for group in phrase.groups for stem in group_stems(group)]
        rows.append(
            {
                "kind": "quad",
                "groups": list(phrase.groups),
                "stems": stems,
                "mapped": [_resolve(stem) if _resolve(stem) in words else None for stem in stems],
            }
        )
    return rows


def _token_counts(lines) -> Counter[str]:
    counts: Counter[str] = Counter()
    for line in lines:
        counts.update(line.flat)
    return counts


def run_round4_tracka(provider: MockProvider | None = None) -> dict[str, Any]:
    """Run the pre-registered tests. The provider is not asked for a completion."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Round 4 Track A accepts MockProvider only")

    lines = load_lines()
    rows = [list(line.flat) for line in lines]
    observed = _pair_counts(rows, 1)
    semantic = _null_pair(rows, observed, seed=PAIR_SEED)
    shortened = []
    for line in lines:
        kept = [stem for index, stem in enumerate(line.flat) if not is_calendar_stem(line, index)]
        if kept:
            shortened.append(kept)
    semantic_outside = _null_pair(shortened, _pair_counts(shortened, 1), seed=PAIR_SEED)

    payload = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    passages = [item for item in payload["stem"]["passages"] if item.get("significant")]
    texts = {text.side: text for text in load_side_texts("stem")}
    pairs, slot_meta = _slot_pairs(passages, texts)
    slot_observed = _classify_pairs(pairs, class_of)
    slots = _slot_null(pairs, slot_observed)
    slots["alignment"] = slot_meta

    shapes, formulae, word_counts = _language()
    r1 = _r1_words()
    r2 = _r2_words()
    calendar = []
    for line in lines:
        if line.side != "Ca":
            continue
        for index, stem in enumerate(line.flat):
            if is_calendar_stem(line, index):
                calendar.append(stem)
    gv6 = next(line for line in lines if line.side == "Gv" and line.number == 6)
    # Each significant passage contributes its left slice. A line break inside
    # a passage stays inside that slice. Windows do not jump from one passage
    # to the next. Overlapping copies (H in both an H–P passage and an H–Q
    # passage) are both counted. The shuffle scores the same windows, so the
    # fraction is still a comparison of assignments.
    parallel_sequences = []
    parallel_signs = 0
    for passage in passages:
        sequence = tuple(
            texts[passage["left"]["side"]].signs[
                passage["left"]["start"] : passage["left"]["end"] + 1
            ]
        )
        parallel_sequences.append(sequence)
        parallel_signs += len(sequence)
    cross_by_class: Counter[str] = Counter()
    cross_pairs: Counter[tuple[str, str]] = Counter()
    for left, right in pairs:
        left_class = class_of(left)
        right_class = class_of(right)
        if left_class is None or left_class != right_class:
            continue
        if int(left) // 100 == int(right) // 100:
            continue
        cross_by_class[left_class] += 1
        ordered = tuple(sorted((left, right)))
        cross_pairs[ordered] += 1

    def context_windows(vocabulary: set[str]) -> dict[str, list[tuple[str, ...]]]:
        parallel: list[tuple[str, ...]] = []
        for sequence in parallel_sequences:
            parallel.extend(windows_in(sequence, vocabulary))
        return {
            "calendar": windows_in(calendar, vocabulary),
            "gv6": windows_in(gv6.flat, vocabulary),
            "parallels": parallel,
        }

    rebus_r1 = _rebus_null(
        context_windows(set(r1)), r1, shapes, formulae, seed=REBUS_SEED_R1, can_adopt=True
    )
    rebus_r2 = _rebus_null(
        context_windows(set(r2)), r2, shapes, formulae, seed=REBUS_SEED_R2, can_adopt=False
    )
    adopted = bool(rebus_r1["adopted"])
    counts = _token_counts(lines)
    table = []
    for row in PICTOGRAPHS:
        table.append(
            {
                "stem": row.stem,
                "icon": row.icon,
                "semantic_class": row.semantic_class,
                "icon_confidence": row.icon_confidence,
                "word": row.word,
                "word_label": row.word_label,
                "rebus": row.rebus,
                "source": row.source,
                "tokens": counts[row.stem],
            }
        )
    result = {
        "round": 4,
        "track": "A",
        "provider": "mock",
        "provider_calls": 0,
        "reading": "R1" if adopted else None,
        "adoption_rule": (
            "R1 total hits and R1 diverse hits (a hit window whose signs are not "
            "all the same word) both beat the assignment shuffle at 5%. "
            "R2 cannot be adopted. A pass is a statistical result, not a translation."
        ),
        "pictographs": table,
        "omitted": list(OMITTED),
        "class_tokens": {
            name: sum(count for stem, count in counts.items() if class_of(stem) == name)
            for name in ("moon", "hand", "bird", "sea", "human", "human_gaping", "plant", "lizard")
        },
        "single_sign_adjacency": {
            "067": _same_sign_adjacency(rows, "067"),
            "760": _same_sign_adjacency(rows, "760"),
        },
        "semantic_cooccurrence": semantic,
        "semantic_cooccurrence_calendar_removed": semantic_outside,
        "parallel_slots": slots,
        "cross_hundred_by_class": dict(cross_by_class),
        "cross_hundred_pairs": [
            {"signs": list(pair), "count": count}
            for pair, count in cross_pairs.most_common()
        ],
        "rebus_r1": rebus_r1,
        "rebus_r2": rebus_r2,
        "attestation_r1": _attestation(r1, shapes, word_counts),
        "attestation_r2_extra": _attestation(
            {sign: word for sign, word in r2.items() if sign not in r1},
            shapes,
            word_counts,
        ),
        "gv6_phrases_r1": _gv6_gloss(lines, r1),
        "corpus_stems": sum(counts.values()),
        "calendar_stems": len(calendar),
        "significant_passages": len(passages),
        "parallel_slice_signs": parallel_signs,
    }
    return result


def _fmt(value: float) -> str:
    return f"{value:.3f}"


def _yn(flag: bool) -> str:
    return "yes" if flag else "no"


def render_round4_tracka(result: dict[str, Any]) -> str:
    """Plain-English report. Every number is taken from the result."""
    semantic = result["semantic_cooccurrence"]
    outside = result["semantic_cooccurrence_calendar_removed"]
    slots = result["parallel_slots"]
    r1 = result["rebus_r1"]
    r2 = result["rebus_r2"]
    same = slots["same_class"]
    cross = slots["cross_hundred"]
    rows = []
    for item in result["pictographs"]:
        word = item["word"] or "—"
        label = item["word_label"] or "—"
        rebus = item["rebus"] or "—"
        rows.append(
            f"| `{item['stem']}` | {item['icon_confidence']} | {item['semantic_class'] or '—'} | "
            f"{item['tokens']} | {word} | {label} | {rebus} |"
        )
    class_rows = []
    for item in semantic["by_class"]:
        class_rows.append(
            f"| {item['class']} | {item['adjacent_different_signs']} | {item['null_ge']} of {semantic['trials']} | "
            f"{_fmt(item['null_fraction'])} | {_yn(item['holds_bonferroni'])} |"
        )
    outside_rows = []
    for item in outside["by_class"]:
        outside_rows.append(
            f"| {item['class']} | {item['adjacent_different_signs']} | {item['null_ge']} of {outside['trials']} | "
            f"{_fmt(item['null_fraction'])} | {_yn(item['holds_bonferroni'])} |"
        )
    context_rows = []
    for item in r1["contexts"]:
        context_rows.append(
            f"| {item['context']} | {item['windows']} | {item['hits']} | {_fmt(item['hit_rate'])} | "
            f"{item['diverse_hits']} | {item['phrase_hits']} | {item['word_hits']} | {item['strict_formula_hits']} | "
            f"{item['null_ge']} of {r1['trials']} | {_fmt(item['null_fraction'])} | {_yn(item['holds_bonferroni'])} |"
        )
    r2_rows = []
    for item in r2["contexts"]:
        r2_rows.append(
            f"| {item['context']} | {item['windows']} | {item['hits']} | {_fmt(item['hit_rate'])} | "
            f"{item['diverse_hits']} | {item['null_ge']} of {r2['trials']} | {_fmt(item['null_fraction'])} |"
        )
    attest = []
    for item in result["attestation_r1"]:
        attest.append(
            f"| `{item['sign']}` | {item['word']} | {'-'.join(item['syllables'])} | "
            f"{_yn(item['in_word_list'])} | {item['running_text_count']} |"
        )
    examples = []
    for item in r1["contexts"]:
        if not item["examples"]:
            examples.append(f"- {item['context']}: none")
            continue
        shown = ", ".join(
            f"{hit['phrase']} ×{hit['windows']} (running text {hit['running_text']})"
            for hit in item["examples"]
        )
        examples.append(f"- {item['context']}: {shown}")
    sources = []
    for item in result["pictographs"]:
        sources.append(f"- `{item['stem']}`: {item['source']}")
    omitted = []
    for item in result["omitted"]:
        omitted.append(f"- **{item['picture']}.** {item['reason']}")
    gv6_lines = []
    for phrase in result["gv6_phrases_r1"]:
        gloss = []
        for stem, mapped in zip(phrase["stems"], phrase["mapped"]):
            gloss.append(r1["words"][mapped] if mapped else stem)
        gv6_lines.append(
            f"- {phrase['kind']}: {' '.join(phrase['groups'])} → {' '.join(gloss)}"
        )
    if not gv6_lines:
        gv6_lines.append("- No strict phrase and no quad on Gv6.")
    held = []
    failed = []
    if semantic["holds"]:
        held.append(
            f"Same-class neighbors, summed over the six testable classes, beat the line shuffle "
            f"({semantic['observed']} pairs; {semantic['null_ge']} of {semantic['trials']}; "
            f"fraction {_fmt(semantic['null_fraction'])})."
        )
    else:
        failed.append(
            f"Same-class neighbors did not beat the line shuffle "
            f"({semantic['observed']} pairs; {semantic['null_ge']} of {semantic['trials']}; "
            f"fraction {_fmt(semantic['null_fraction'])}; add-one p {_fmt(semantic['p_add_one'])})."
        )
    step2 = semantic["step2"]
    step2_clear = [
        item["class"] for item in step2["by_class"] if item["pairs"] > 0 and item["null_fraction"] <= ADOPT_FRACTION
    ]
    if step2["holds_if_it_were_gated"]:
        held.append(
            f"The secondary count, different signs of one class two places apart, beats the same shuffle "
            f"({step2['observed']} pairs; {step2['null_ge']} of {semantic['trials']}; "
            f"fraction {_fmt(step2['null_fraction'])}; add-one p {_fmt(step2['p_add_one'])}). "
            f"Classes under 5% on their own: {', '.join(step2_clear) or 'none'}. It was not the gate."
        )
    else:
        failed.append(
            f"The secondary two-apart count does not beat the shuffle "
            f"({step2['observed']} pairs; fraction {_fmt(step2['null_fraction'])})."
        )
    if outside["holds"]:
        held.append(
            "The same neighbor count still beats the shuffle after the Mamari calendar stems are removed."
        )
    else:
        failed.append(
            "After the Mamari calendar stems are removed, the neighbor count does not beat the shuffle."
        )
    for item in semantic["by_class"]:
        if item["holds_bonferroni"]:
            held.append(
                f"Class {item['class']} survives the Bonferroni cut "
                f"({item['adjacent_different_signs']} pairs; fraction {_fmt(item['null_fraction'])})."
            )
    if cross["holds"]:
        held.append(
            "Cross-hundred parallel substitutions share a class more often than the label shuffle."
        )
    else:
        failed.append(
            "Cross-hundred parallel substitutions do not share a class more often than the label shuffle "
            f"({cross['observed']} of {cross['classified_pairs']}; "
            f"{cross['null_ge']} of {slots['trials']}; fraction {_fmt(cross['null_fraction'])})."
        )
    if r1["holds"]:
        held.append(
            f"R1 rebus hits beat the shuffled word assignment "
            f"({r1['hits']} hits; rate {_fmt(r1['hit_rate'])}; "
            f"{r1['null_ge']} of {r1['trials']}; fraction {_fmt(r1['null_fraction'])})."
        )
    else:
        failed.append(
            f"R1 rebus hits do not beat the shuffled word assignment "
            f"({r1['hits']} hits on {r1['windows']} windows; rate {_fmt(r1['hit_rate'])}; "
            f"null mean {_fmt(r1['null_mean_hits'])}; "
            f"{r1['null_ge']} of {r1['trials']}; fraction {_fmt(r1['null_fraction'])}; "
            f"add-one p {_fmt(r1['p_add_one'])})."
        )
    if r1["diverse_holds"]:
        held.append("R1 hits that mix two different words also beat the shuffle.")
    else:
        failed.append(
            "R1 hits that mix two different words do not beat the shuffle "
            f"({r1['diverse_hits']} hits; {r1['diverse_null_ge']} of {r1['trials']}; "
            f"fraction {_fmt(r1['diverse_null_fraction'])})."
        )
    if r2["holds"]:
        held.append("The sensitivity map R2 beats its own shuffle. It is not adopted.")
    else:
        failed.append(
            "The sensitivity map R2 does not beat its own shuffle "
            f"({r2['hits']} hits; {r2['null_ge']} of {r2['trials']}; "
            f"fraction {_fmt(r2['null_fraction'])})."
        )
    if result["reading"] is None:
        failed.append("No map is recorded.")
    else:
        held.append(
            "The adoption rule records R1 because the summed hits and the mixed-word hits both clear 5%. "
            "The calendar context and Gv6 do not. The record is not a translation."
        )
    held_text = "\n".join(f"- {line}" for line in held) or "- Nothing in the gates held."
    failed_text = "\n".join(f"- {line}" for line in failed)
    cross_bits = ", ".join(
        f"{name} {count}" for name, count in sorted(result["cross_hundred_by_class"].items())
    ) or "none"
    step2_rows = []
    for item in semantic["step2"]["by_class"]:
        step2_rows.append(
            f"| {item['class']} | {item['pairs']} | {item['null_ge']} of {semantic['trials']} | {_fmt(item['null_fraction'])} |"
        )
    outside_step2 = outside["step2"]
    calendar_ctx = next(item for item in r1["contexts"] if item["context"] == "calendar")
    gv6_ctx = next(item for item in r1["contexts"] if item["context"] == "gv6")
    parallel_ctx = next(item for item in r1["contexts"] if item["context"] == "parallels")
    return f"""# Round 4, Track A — pictographic meanings and rebus readings

Signs of one pictured class do not sit next to each other more than a shuffle ({semantic["observed"]} pairs, {semantic["null_ge"]} of {semantic["trials"]}, fraction {_fmt(semantic["null_fraction"])}). The same classes two signs apart do ({semantic["step2"]["observed"]} pairs, {semantic["step2"]["null_ge"]} of {semantic["trials"]}, fraction {_fmt(semantic["step2"]["null_fraction"])}). In the parallel passages, cross-series substitutions that share a class are {cross["observed"]} of {cross["classified_pairs"]} ({cross_bits}; {cross["null_ge"]} of {slots["trials"]}, fraction {_fmt(cross["null_fraction"])}). The rebus word list scores {r1["hits"]} hits against a shuffle mean of {_fmt(r1["null_mean_hits"])} ({r1["null_ge"]} of {r1["trials"]}, fraction {_fmt(r1["null_fraction"])}). The calendar context has {calendar_ctx["hits"]} hits and does not clear its own null (fraction {_fmt(calendar_ctx["null_fraction"])}). Gv6 has {gv6_ctx["windows"]} mapped windows. The parallel context has {parallel_ctx["hits"]} hits (fraction {_fmt(parallel_ctx["null_fraction"])}). Under the rule fixed beforehand the map is recorded as {result["reading"]}. Nothing here is a translation of a tablet.

Provider: `mock`. Provider calls: {result["provider_calls"]}.

The pictures below are cited. A word is a published proposal or it is marked HYPOTHESIS. The tests were fixed before these scores were read.

## What held, and what failed

### Held

{held_text}

### Failed

{failed_text}

## What was fixed first

Six classes can co-occur as two different signs: moon (`040`, `041`, `143`, `152`), hand (`006`, `061`, `062`, `063`, `064`), bird (Barthel 400–409 and 600–699), sea (700–759 and 770–799), human (200–299), and gaping-mouth human (300–399). `042` is not a moon sign. Guy's claim that 42 is 40 rotated is one stacked pair, and the Round 2 allograph note already refuses to apply it everywhere. `760` is the suggested lizard, not a fish. Series 410–599 are left unclassified because Guy 2006 says the digit code breaks down there.

The neighbor statistic counts adjacent stems on one line that fall in the same class and are not the same sign. The null shuffles the stems inside each line, {semantic["trials"]} draws, seed {semantic["seed"]}. A class is claimed only if its fraction is at or under {CLASS_BONFERRONI:.4f} (0.05 divided by 6). The sum is claimed at 0.05. A second distance, two signs apart, is counted on the same draws and is not a gate. The calendar control deletes the Mamari calendar stems and repeats the shuffle with seed {outside["seed"]}.

Parallel slots use the {result["significant_passages"]} significant stem passages already stored from Round 2. Each pair of slices is aligned again with the same Smith-Waterman scorer. The semantic gate is the cross-hundred subset: both signs are classified, their hundreds digits differ, and they share a class. The label null permutes class labels on the classified stems that occur in those mismatch columns, {slots["trials"]} draws, seed {slots["seed"]}. Sharing a class inside one hundred is reported and is not the gate, because that is where allographs live.

The rebus assigns each chosen sign one whole word. `064` copies whatever word `006` receives. A window is 2, 3, or 4 mapped signs in a row. An unmapped sign breaks the row. A hit is a window whose syllables are one attested word, or whose words occur in that order in the primary running text. A strict formula is the Round 3 rule, count at least 4. The primary hit does not require that. Contexts are the joined Mamari calendar, the Gv6 line, and the left slice of each significant parallel. The null shuffles the words among the signs, {r1["trials"]} draws. R1 seed {r1["seed"]}. R2 seed {r2["seed"]}. A context is claimed only under the Bonferroni cut {CONTEXT_BONFERRONI:.4f}. Adoption needs both the total and the diverse hits (two different words in the window) at or under 0.05. R2 cannot be adopted.

## Pictographs

| Sign | Icon confidence | Class | Tokens | Word | Word label | Rebus |
| --- | --- | --- | ---: | --- | --- | --- |
{chr(10).join(rows)}

Class token totals, every stem the class function labels, not only the rows above: moon {result["class_tokens"]["moon"]}, hand {result["class_tokens"]["hand"]}, bird {result["class_tokens"]["bird"]}, sea {result["class_tokens"]["sea"]}, human {result["class_tokens"]["human"]}, gaping-mouth human {result["class_tokens"]["human_gaping"]}, plant {result["class_tokens"]["plant"]}, lizard {result["class_tokens"]["lizard"]}. Corpus stems: {result["corpus_stems"]}.

### Sources, one row at a time

{chr(10).join(sources)}

### Left out

{chr(10).join(omitted)}

Identical neighbors of the two single-sign classes, not a gate: `067` sits next to itself {result["single_sign_adjacency"]["067"]} times, `760` {result["single_sign_adjacency"]["760"]} times.

## Semantic co-occurrence

Summed different-sign neighbors: **{semantic["observed"]}**. Line shuffle: {semantic["null_ge"]} of {semantic["trials"]} reach that count (fraction {_fmt(semantic["null_fraction"])}, add-one p {_fmt(semantic["p_add_one"])}). Holds at 5%: {_yn(semantic["holds"])}.

| Class | Pairs | Null | Fraction | Bonferroni |
| --- | ---: | --- | ---: | --- |
{chr(10).join(class_rows)}

Two signs apart, same draws, not the neighbor gate: {semantic["step2"]["observed"]} pairs, null {semantic["step2"]["null_ge"]} of {semantic["trials"]} (fraction {_fmt(semantic["step2"]["null_fraction"])}, add-one p {_fmt(semantic["step2"]["p_add_one"])}). Would have cleared 5% if it had been the gate: {_yn(semantic["step2"]["holds_if_it_were_gated"])}.

| Class | Two apart | Null | Fraction |
| --- | ---: | --- | ---: |
{chr(10).join(step2_rows)}

After the calendar is removed, the two-apart count is {outside_step2["observed"]} (null {outside_step2["null_ge"]} of {outside["trials"]}, fraction {_fmt(outside_step2["null_fraction"])}). A pattern that fits these two distances is Guy 2006's harmonic sequence: a repeated slot of one kind of sign, with something else between the repetitions. Neighbors are then often different classes, and the matching class sits two places away. That reading of the distances is an interpretation of a result that was already in the plan. It is not a new test.

Calendar stems removed ({result["calendar_stems"]} stems taken out of the Mamari passage). Sum: **{outside["observed"]}**. Null {outside["null_ge"]} of {outside["trials"]} (fraction {_fmt(outside["null_fraction"])}, add-one p {_fmt(outside["p_add_one"])}). Holds: {_yn(outside["holds"])}.

| Class | Pairs | Null | Fraction | Bonferroni |
| --- | ---: | --- | ---: | --- |
{chr(10).join(outside_rows)}

These classes are Barthel's appearance bins, plus the few signs Guy and the calendar papers single out. A positive neighbor count means those bins sit together in the text. It does not discover the pictures. The pictures were the input.

## Parallel slots

Passages: {slots["alignment"]["passages"]}. Published mismatch cells: {slots["alignment"]["published_mismatches"]}. Realigned mismatch cells: {slots["alignment"]["realigned_mismatches"]}. Realigned columns: {slots["alignment"]["realigned_columns"]}.

Classified mismatch pairs: {same["classified_pairs"]}. Same class: {same["observed"]} (rate {_fmt(same["rate"])}). Label shuffle: {same["null_ge"]} of {slots["trials"]} (fraction {_fmt(same["null_fraction"])}, add-one p {_fmt(same["p_add_one"])}). This rate includes pairs inside one hundred. It is not the semantic gate.

Cross-hundred classified pairs: {cross["classified_pairs"]}. Same class: {cross["observed"]} (rate {_fmt(cross["rate"])}). Label shuffle: {cross["null_ge"]} of {slots["trials"]} (fraction {_fmt(cross["null_fraction"])}, add-one p {_fmt(cross["p_add_one"])}). Holds at 5%: {_yn(cross["holds"])}.

Those {cross["observed"]} pairs break down by class as: {cross_bits}. Pair counts, order ignored: {", ".join(f"{item['signs'][0]}–{item['signs'][1]} ×{item['count']}" for item in result["cross_hundred_pairs"]) or "none"}. Series 400–409 was classed with series 600–699 because Guy 2006 says the first ten signs of series 400 are birds. Pozdniakov 1996 had already treated gaping-mouth and bird heads as variants, and the 2007 inventory still lists 400 apart from 600. This gate says those two hundreds fill the same parallel slots more than a relabeling. It does not say that fish, hands, or people do.

## Rebus

R1 words, and whether the vendored lists contain them. Running-text count is the mapped spelling, so `tagata` and `tangata` share a count.

| Sign | Word | Syllables | In a word list | Running-text tokens |
| --- | --- | --- | ---: | ---: |
{chr(10).join(attest)}

R1 windows: {r1["windows"]}. Hits: {r1["hits"]}. Hit rate: {_fmt(r1["hit_rate"])}. Null mean hits: {_fmt(r1["null_mean_hits"])}. Null: {r1["null_ge"]} of {r1["trials"]} (fraction {_fmt(r1["null_fraction"])}, add-one p {_fmt(r1["p_add_one"])}). Holds: {_yn(r1["holds"])}. Diverse hits: {r1["diverse_hits"]}. Diverse null: {r1["diverse_null_ge"]} of {r1["trials"]} (fraction {_fmt(r1["diverse_null_fraction"])}, add-one p {_fmt(r1["diverse_p_add_one"])}). Diverse holds: {_yn(r1["diverse_holds"])}. Adopted: {_yn(r1["adopted"])}.

| Context | Windows | Hits | Rate | Diverse | Phrase | Word | Strict formula | Null | Fraction | Bonferroni |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
{chr(10).join(context_rows)}

Hit windows, R1:

{chr(10).join(examples)}

Gv6 phrases under R1. An unmapped sign stays a number. These lines are the genealogy pattern from Track 3. They are not extra hits unless the mapped signs also form a window of length 2 or more.

{chr(10).join(gv6_lines)}

R2 adds `076` ure, `067` niu, and `760` moko. Windows: {r2["windows"]}. Hits: {r2["hits"]}. Rate: {_fmt(r2["hit_rate"])}. Null mean: {_fmt(r2["null_mean_hits"])}. Null: {r2["null_ge"]} of {r2["trials"]} (fraction {_fmt(r2["null_fraction"])}, add-one p {_fmt(r2["p_add_one"])}). Holds: {_yn(r2["holds"])}. Diverse: {r2["diverse_hits"]} ({r2["diverse_null_ge"]} of {r2["trials"]}, fraction {_fmt(r2["diverse_null_fraction"])}). Adopted: no.

| Context | Windows | Hits | Rate | Diverse | Null | Fraction |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
{chr(10).join(r2_rows)}

Fischer's Staff triad `606.076 700 008` is the example already locked in Track 3. R1 reads `700` as ika and does not assign `606` or `008`. `076` is only on R2. The triad is not scored as its own crib beyond whatever window the rules already catch.

## What this does not claim

No tablet is translated. A neighbor count inside Barthel's own series is not an independent identification of birds or fish. A rebus hit on a repeated crescent is the word assigned to that one sign, said twice. Guy's taxogram argument for sign 200 is still open, and it pulls against reading every 200 as tangata. Metoro's recitations are language material. Track 4 already found they do not label the signs, and this track does not pair them again.

The run uses `MockProvider` only. Provider calls: {result["provider_calls"]}.
"""


def write_round4_outputs(result: dict[str, Any]) -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_round4_tracka(result), encoding="utf-8")


def main() -> None:
    result = run_round4_tracka(MockProvider())
    write_round4_outputs(result)


if __name__ == "__main__":
    main()
