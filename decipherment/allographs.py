"""Cited allograph merges over Kohaumotu Barthel tokens.

Each scheme is switchable. A rule is either Barthel's own mark for a
variant, or a later author's explicit proposal. Uncertain rules stay in
the scheme that cites them and are flagged. The unpublished Pozdniakov
merge table is not reconstructed. No rule assigns a reading.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from decipherment.inventories import ILLEGIBLE, _prepare

# Barthel 1958: 38–42, as listed by kohaumotu.org (corpus/affixes.html)
# and Guy 2006, Rapa Nui Journal 20(1). These letters modify one Grundtypus.
# They are not separate signs.
_MODIFICATION = frozenset("fosxyht")
# a–d: Barthel's indices for distinct signs that share a number (not allographs).
# e, g: the same job in the CEIPP extended system (kohaumotu.org corpus/extended.html).
_INDEX = frozenset("abcdeg")
# i, j, k: CEIPP marks for a missing head protrusion, not in Barthel 1958.
# Left in place. Stripping them would be an uncited merge.
_PART = re.compile(r"^(V|D)?(\d+)([A-Za-z]*)$", re.IGNORECASE)

# Guy 2006: Barthel's own rules imply these catalog codes. He gives them as
# examples of inconsistency, not as a corrected catalog, so each use is uncertain.
# 545 is 39 upside down (39x). 41 is the mirror of 40 (40y). 180, 380, and 480
# "should be respectively 126, 370 and 470". 578 and 579 are the hollow-bellied
# forms he says should have been D570 and D575; the D prefix is a derivation mark.
GUY_CATALOG_MAP = {
    "545": "039",
    "041": "040",
    "180": "126",
    "380": "370",
    "480": "470",
    "578": "570",
    "579": "575",
}

# Horley 2005, Rapa Nui Journal 19(2): 107–116. Numeric equivalences he states.
# All are uncertain: the paper says "possible", "suggested", or "assuming".
# His two-digit element catalog renumbers 060–064 as elements 30–34. That is a
# new code, not a claim that Barthel 060 is Barthel 030, so it is not applied.
HORLEY_MAP = {
    "049": "048",
    "058": "075",
    "007": "071",
    "013": "070",
    "103": "037",
    "156": "101",
    "208": "200",
    "209": "200",
    "440": "660",
    "055": "005",
    "059": "520",
    "499": "520",
    "064": "006",
}
HORLEY_RANGES = (
    (521, 529, "520"),
    (530, 539, "005"),
    (661, 684, "660"),
)
# Decompositions into component stems. Applied only when ligatures are split.
# 280 and 126: Horley 2005 proposes 280 = 070.002, and 126 as the same body flipped.
# 386: the ligature 073.006 stands in for 386 in the parallel he cites.
HORLEY_EXPAND = {
    "280": ("070", "002"),
    "126": ("070", "002"),
    "386": ("073", "006"),
}

SCHEMA_IDS = (
    "barthel_families",
    "barthel_suffix_only",
    "pozdniakov_2007",
    "pozdniakov_1996_gaping_mouth",
    "horley_2005",
)


@dataclass(frozen=True)
class MergeRule:
    """One cited merge. ``uncertain`` is true when the source hedges or the
    step generalizes an example."""

    rule_id: str
    schemes: tuple[str, ...]
    uncertain: bool
    citation: str
    statement: str


MERGE_RULES: tuple[MergeRule, ...] = (
    MergeRule(
        "barthel_modification_affixes",
        ("barthel_families", "barthel_suffix_only"),
        False,
        "Barthel 1958: 38–42; kohaumotu.org corpus/affixes.html; Guy 2006, Rapa Nui Journal 20(1).",
        "Strip modification affixes and treat the bare number as the Grundtypus: "
        "f feathers, o and s adornments, x upside-down, y mirror, h superscript, "
        "t subscript, and the V/D variant or derivation mark.",
    ),
    MergeRule(
        "barthel_keep_index_letters",
        ("barthel_families", "barthel_suffix_only"),
        False,
        "Barthel 1958: 38–42; Guy 2006. CEIPP e/g: kohaumotu.org corpus/extended.html.",
        "Keep index letters a–d (and CEIPP e, g). Barthel used them to separate "
        "distinct signs that share a number. They are not allographs. "
        "CEIPP i/j/k (missing head protrusion) are also kept, because Barthel 1958 "
        "does not define them as variants.",
    ),
    MergeRule(
        "guy_catalog_corrections",
        ("barthel_families",),
        True,
        "Guy 2006, Rapa Nui Journal 20(1), on Barthel 1958: 40–41.",
        "Apply Guy's explicit 'should have been coded as' examples: "
        "545→039, 041→040, 180→126, 380→370, 480→470, 578→570, 579→575, and 160b→160a. "
        "Uncertain: examples of catalog inconsistency, not a full corrected list. "
        "Glyph 42 = glyph 40 rotated in one stacked pair (Br1) is not applied globally.",
    ),
    MergeRule(
        "pozdniakov_27_orientations",
        ("pozdniakov_2007", "pozdniakov_1996_gaping_mouth"),
        True,
        "Pozdniakov & Pozdniakov 2007, as tabulated in Wikipedia 'Rongorongo' "
        "(the 52-sign inventory, note on 27a/27b); Barthel's x affix, kohaumotu.org corpus/affixes.html.",
        "Keep 027a apart from 027b. Map 027x to 027b. Leave bare 027 untouched, "
        "because the stemmer cannot see which orientation it was. "
        "Uncertain: equating Barthel's x suffix with his 27b index.",
    ),
    MergeRule(
        "pozdniakov_strip_other_indexes",
        ("pozdniakov_2007", "pozdniakov_1996_gaping_mouth", "horley_2005"),
        True,
        "Pozdniakov & Pozdniakov 2007 published list (bare numbers except 27a); "
        "Horley 2005 states equivalences on three-digit Barthel numbers.",
        "Strip index letters other than the 27a/27b distinction. Uncertain: "
        "this follows the published labels, and it can merge signs Barthel indexed apart. "
        "The 2007 allograph table that would say which indexes are real variants was not published.",
    ),
    MergeRule(
        "hand_6_and_64",
        ("pozdniakov_2007", "pozdniakov_1996_gaping_mouth", "horley_2005"),
        False,
        "Pozdniakov 1996, Journal de la Société des Océanistes 103: 296; "
        "Horley 2005 discusses hand 064 corrected to a 600.064 ligature.",
        "Map isolated hand 064 to 006. The two hand shapes substitute in repeated phrases.",
    ),
    MergeRule(
        "hand_digit_4_to_6",
        ("pozdniakov_2007", "pozdniakov_1996_gaping_mouth"),
        True,
        "Pozdniakov 1996: 296–297, as illustrated by Guy 2006 (tablets P and H: "
        "304/306, 244/246, 254 with hand 4 vs hand 6). Guy 2006: the units digit "
        "encodes the hand in series 200 and 300 only.",
        "In codes 200–399, rewrite units digit 4 as 6. Uncertain generalization "
        "from the published hand pair and Guy's examples to every code in those two series. "
        "Not applied to series 400–799, where Guy says the digit system breaks down, "
        "and not applied to isolated 004 (Guy: digits 1–7 in isolation are different signs, except 6).",
    ),
    MergeRule(
        "abstract_56_and_84",
        ("pozdniakov_2007", "pozdniakov_1996_gaping_mouth"),
        True,
        "Guy 2006, citing Pozdniakov 1997: glyph 56 alternates with glyph 84 "
        "on the parallel of Pr1 and Hr1.",
        "Map 084 to 056. Uncertain: one parallel pair of abstract signs, not a series rule.",
    ),
    MergeRule(
        "gaping_mouth_to_bird",
        ("pozdniakov_1996_gaping_mouth",),
        True,
        "Pozdniakov 1996: 297, via Wikipedia 'Decipherment of rongorongo': "
        "gaping-mouth heads are variants of bird heads, so series 300 and 400 are "
        "ligatures or variants of series 600.",
        "Rewrite hundreds digit 3 or 4 as 6, after the hand-digit rewrite. "
        "Uncertain, and superseded by the 2007 basic inventory, which still lists "
        "380 and 400 as separate signs. Not part of the 2007 scheme. "
        "A hundreds rewrite is not the unpublished ligature table.",
    ),
    MergeRule(
        "do_not_split_099",
        ("pozdniakov_2007", "pozdniakov_1996_gaping_mouth", "horley_2005", "barthel_families"),
        False,
        "Pozdniakov & Pozdniakov 2007, via Wikipedia 'Decipherment of rongorongo': "
        "099 looks like 095 plus 014 but behaves as its own sign.",
        "Do not decompose 099. Negative rule.",
    ),
    MergeRule(
        "horley_one_to_one",
        ("horley_2005",),
        True,
        "Horley 2005, Rapa Nui Journal 19(2): 107–116.",
        "Map 049→048, 058→075, 007→071, 013→070, 103→037, 156→101, "
        "208→200, 209→200 (reduplications of 200), 440→660, 055→005, "
        "059→520, 499→520. Uncertain: Horley's wording is 'possible' or 'suggested'. "
        "208/209 collapsed to 200 loses the reduplication he proposed; "
        "it is an inventory test, not his element reading.",
    ),
    MergeRule(
        "horley_head_ranges",
        ("horley_2005",),
        True,
        "Horley 2005: 005 with heads 530–539; 055b with the same heads; "
        "059 and 499 with heads 520–529; long-beak heads 660–684, with 440 as an allograph.",
        "Map 521–529→520, 530–539→005, 661–684→660. Uncertain series reading of those paragraphs.",
    ),
    MergeRule(
        "horley_expansions",
        ("horley_2005",),
        True,
        "Horley 2005: 280 decomposed as 070.002; 126 as that body flipped; "
        "386 replaced by ligature 073.006 in Ca2/Pr9.",
        "When ligatures are decomposed, expand 280 and 126 to 070 002, and 386 to 073 006. "
        "Uncertain. Not expanded when ligatures are kept whole.",
    ),
    MergeRule(
        "ligature_dot_colon",
        SCHEMA_IDS,
        False,
        "Barthel 1958 coding, as used by Kohaumotu: '.' links signs, ':' stacks them. "
        "Guy 1982 and Pozdniakov 1996 read stacks bottom-to-top; this option only splits, "
        "it does not reorder.",
        "Option, default on: split 606.076 into 606 and 076, and 999.440.076 into "
        "999, 440, and 076. Off: keep the ligature as one token after per-component maps.",
    ),
)


def rules_for(scheme: str) -> tuple[MergeRule, ...]:
    if scheme not in SCHEMA_IDS:
        raise ValueError(f"unknown allograph scheme {scheme}")
    return tuple(rule for rule in MERGE_RULES if scheme in rule.schemes)


def _letters(raw: str) -> str:
    return "".join(character.lower() for character in raw if character.isalpha())


def _canonical(part: str, scheme: str) -> str | None:
    """One ligature component to a sign key. None if the component is not a code."""
    match = _PART.fullmatch(part)
    if match is None:
        return None
    digits = match.group(2).zfill(3)
    letters = _letters(match.group(3) or "")
    if scheme in {"barthel_families", "barthel_suffix_only"}:
        kept = "".join(character for character in letters if character not in _MODIFICATION and character not in {"v", "d"})
        return digits + kept
    if scheme in {"pozdniakov_2007", "pozdniakov_1996_gaping_mouth"}:
        if digits == "027":
            if "b" in letters or "x" in letters:
                return "027b"
            if "a" in letters:
                return "027a"
        return digits
    if scheme == "horley_2005":
        return digits
    raise ValueError(f"unknown allograph scheme {scheme}")


def _split_key(key: str) -> tuple[str, str]:
    match = re.fullmatch(r"(\d{3})([a-z]*)", key)
    if match is None:
        return key, ""
    return match.group(1), match.group(2)


def _with_digits(digits: str, suffix: str) -> str:
    return digits.zfill(3) + suffix


def _apply_identity(key: str, scheme: str) -> str:
    digits, suffix = _split_key(key)
    if not digits.isdigit():
        return key
    if scheme == "barthel_families":
        if digits == "160" and suffix == "b":
            suffix = "a"
        mapped = GUY_CATALOG_MAP.get(digits)
        if mapped is not None:
            digits = mapped
        return _with_digits(digits, suffix)
    if scheme in {"pozdniakov_2007", "pozdniakov_1996_gaping_mouth"}:
        if digits == "064":
            digits = "006"
        elif digits == "084":
            digits = "056"
        number = int(digits)
        if 200 <= number <= 399 and digits[2] == "4":
            digits = digits[:2] + "6"
        if scheme == "pozdniakov_1996_gaping_mouth" and digits[0] in {"3", "4"}:
            digits = "6" + digits[1:]
        return _with_digits(digits, suffix)
    if scheme == "horley_2005":
        if digits == "064":
            digits = "006"
        mapped = HORLEY_MAP.get(digits)
        if mapped is not None:
            digits = mapped
        number = int(digits)
        for low, high, target in HORLEY_RANGES:
            if low <= number <= high:
                digits = target
                break
        return _with_digits(digits, suffix)
    return key


def _expand(key: str, scheme: str, decompose_ligatures: bool) -> list[str]:
    if scheme != "horley_2005" or not decompose_ligatures:
        return [key]
    digits, suffix = _split_key(key)
    parts = HORLEY_EXPAND.get(digits)
    if parts is None:
        return [key]
    # Index letters have already been stripped on this scheme.
    if suffix:
        return [key]
    return list(parts)


def _components(token: str) -> list[tuple[str, str]] | None:
    cleaned = _prepare(token)
    if cleaned is None:
        return None
    pieces: list[tuple[str, str]] = []
    separator = ""
    for bit in re.split(r"([.:])", cleaned):
        if bit in ".:":
            separator = bit
            continue
        if not bit:
            continue
        pieces.append((separator, bit))
        separator = ""
    return pieces


def encode_scheme_token(
    token: str,
    scheme: str,
    *,
    decompose_ligatures: bool = True,
    drop_illegible: bool = True,
) -> list[str]:
    """Encode one Kohaumotu token under a cited scheme.

    ``decompose_ligatures`` splits on '.' and ':'. When it is off, each
    component is still rewritten, then joined back into one token.
    """
    if scheme not in SCHEMA_IDS:
        raise ValueError(f"unknown allograph scheme {scheme}")
    pieces = _components(token)
    if not pieces:
        return []
    rendered: list[tuple[str, list[str]]] = []
    for separator, part in pieces:
        key = _canonical(part, scheme)
        if key is None:
            continue
        key = _apply_identity(key, scheme)
        signs = _expand(key, scheme, decompose_ligatures)
        if drop_illegible:
            signs = [sign for sign in signs if _split_key(sign)[0] != ILLEGIBLE]
        if not signs:
            continue
        rendered.append((separator, signs))
    if not rendered:
        return []
    if decompose_ligatures:
        return [sign for _separator, signs in rendered for sign in signs]
    joined = rendered[0][1][0]
    for separator, signs in rendered[1:]:
        # Identity maps only: expansions are off when ligatures stay whole.
        joined += (separator or ".") + signs[0]
    return [joined]


def encode_scheme_lines(
    lines: list[list[str]] | tuple[tuple[str, ...], ...],
    scheme: str,
    *,
    decompose_ligatures: bool = True,
    drop_illegible: bool = True,
) -> list[list[str]]:
    """Encode every line. Empty lines are dropped."""
    output: list[list[str]] = []
    for line in lines:
        signs: list[str] = []
        for token in line:
            signs.extend(
                encode_scheme_token(
                    token,
                    scheme,
                    decompose_ligatures=decompose_ligatures,
                    drop_illegible=drop_illegible,
                )
            )
        if signs:
            output.append(signs)
    return output
