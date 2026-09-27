"""Round 6A: pre-register scan verdicts before any higher-resolution image is opened.

The twelve disagreements are the ones logged in Round 5B. Each alternative
sign code named here is already in that log, in the Round 3 calendar audit,
or in the allograph notes. A verdict may select only those codes. The script
recomputes the Round 5B headline counts. It does not edit the vendored
transcription, it does not fetch a mesh, and it does not assign a reading.

``MockProvider`` is accepted and never called.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any

from agents.base.providers import MockProvider
from decipherment.round3_trackb import (
    between_delimiter_040,
    count_378_delimiters,
    flatten,
    guy_040_counts,
    load_fixture_tokens,
    stem_lines,
)
from decipherment.round5b_ceipp import _bird_pair
from decipherment.track3_genealogy import (
    chain_links,
    extract_strict_phrases,
    fischer_census,
    group_stems,
)
from decipherment.track_c_parallels import _column_counts, load_side_texts

REPO_ROOT = Path(__file__).resolve().parents[1]
PASSAGE_PATH = REPO_ROOT / "data" / "decipherment" / "substitution_classes.json"
OUTPUT_PATH = REPO_ROOT / "data" / "decipherment" / "round6a_preregistration.json"
ROUND5B_PATH = REPO_ROOT / "data" / "decipherment" / "round5b_ceipp_recheck.json"

# Tablets with a public INSCRIBE model, as listed in docs/round4e_image_sources.md.
# A–D are the Rome models. M and N are the downsampled Vienna meshes.
INSCRIBE_TABLETS = ("A", "B", "C", "D", "M", "N")
OPENERS = frozenset({"390"})
HEADLINE_PASSAGE_ID = "P001"
HEADLINE_LEFT_LOCUS = "Hr2:36..Hr4:0"
HEADLINE_RIGHT_LOCUS = "Qr2:0..Qr3:65"

EVIDENCE_INSCRIBE = "inscribe"
EVIDENCE_COUNTERFACTUAL = "counterfactual"
EVIDENCE_LATER_IMAGE = "later_image"
EVIDENCE_VALUES = (
    EVIDENCE_INSCRIBE,
    EVIDENCE_COUNTERFACTUAL,
    EVIDENCE_LATER_IMAGE,
)

HEADLINE_KEYS = (
    "calendar_040",
    "calendar_040_before_152",
    "calendar_040_after_152",
    "calendar_040_gaps",
    "calendar_full_delimiters",
    "calendar_152",
    "calendar_143",
    "gv6_phrases",
    "gv6_handoffs",
    "staff_076_after_999",
    "staff_pure_999",
    "staff_076_after_999_rate",
    "parallel_span",
    "parallel_matches",
    "parallel_mismatches",
    "parallel_bird_substitutions",
    "corpus_bird_substitutions",
)

# Stems the vendored pages must still have, so an edit cannot land on the wrong sign.
EXPECTED_STEMS: dict[tuple[str, str, int], str] = {
    ("Hr", "Hr2", 66): "600",
    ("Hr", "Hr3", 26): "607",
    ("Hr", "Hr3", 37): "064",
    ("Hr", "Hr3", 43): "006",
    ("Hr", "Hr3", 44): "042",
    ("Hr", "Hr4", 71): "042",
    ("Qr", "Qr2", 30): "400",
    ("Qr", "Qr3", 6): "407",
    ("Qr", "Qr3", 17): "064",
    ("Qr", "Qr3", 23): "006",
    ("Qr", "Qr3", 24): "042",
}


def _source(name: str, detail: str) -> dict[str, str]:
    return {"name": name, "detail": detail}


def _alternative(
    alternative_id: str,
    sign_codes: str,
    sources: tuple[dict[str, str], ...],
    *,
    baseline: bool = False,
) -> dict[str, Any]:
    return {
        "id": alternative_id,
        "sign_codes": sign_codes,
        "baseline": baseline,
        "sources": [dict(row) for row in sources],
    }


# Order matches data/decipherment/round5b_ceipp_recheck.json "disagreements".
DISAGREEMENTS: tuple[dict[str, Any], ...] = (
    {
        "id": "D01",
        "passage": "Ca7",
        "position": "the group after 152, one horizontal slot",
        "repo_code": "600.390.041",
        "tablets": ("C",),
        "baseline": "barthel_600_390_041",
        "alternatives": (
            _alternative(
                "barthel_600_390_041",
                "600.390.041",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "The calendar fixture keeps the group as three stems: 600, 390, 041.",
                    ),
                ),
                baseline=True,
            ),
            _alternative(
                "guy_1990_star690",
                "*690.041",
                (
                    _source(
                        "Guy 1990",
                        "Guy calls the stack one sign, *690, and says catalog 690 is a different sign. "
                        "Round 3 recorded the replacement as *690.041. The asterisk stays, so the stem is not catalog 690.",
                    ),
                ),
            ),
        ),
        "no_other_code": (
            "The CEIPP outline shows 600 and 390 sharing one slot, with crescent 041 in the next slot. The outline does not print *690.",
            "Horley 2011 and Pozdniakov do not renumber this group in the sources used in Round 3 and Round 5B.",
        ),
    },
    {
        "id": "D02",
        "passage": "Ca7",
        "position": "the group 044.040, before 143 and 152",
        "repo_code": "044.040",
        "tablets": ("C",),
        "baseline": "barthel_044_040",
        "alternatives": (
            _alternative(
                "barthel_044_040",
                "044.040",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "The fixture token is 044.040. The crescent is the second piece.",
                    ),
                ),
                baseline=True,
            ),
            _alternative(
                "guy_1990_078_040",
                "078.040",
                (
                    _source(
                        "Guy 1990",
                        "Guy proposes 078.040 and keeps the crescent. Round 3 adopted that pair as a published replacement of one group. Round 5B left the vendored code in place.",
                    ),
                    _source(
                        "CEIPP outline",
                        "Round 5B: a non-crescent figure sits beside a tall crescent. The outline fits 044 or 078 and was not given a third number.",
                    ),
                ),
            ),
        ),
        "no_other_code": (
            "Horley and Pozdniakov do not supply a different number for this group in the sources already used.",
        ),
    },
    {
        "id": "D03",
        "passage": "Ca7 and Ca8",
        "position": "the two signs coded 041h inside delimiter groups",
        "repo_code": "041h",
        "tablets": ("C",),
        "baseline": "barthel_041",
        "alternatives": (
            _alternative(
                "barthel_041",
                "041",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "041h stems to 041. One token sits in the Ca7 delimiter and one in the Ca8 delimiter.",
                    ),
                    _source(
                        "Horley 2011",
                        "Horley says the two small superscript crescents have a paleographic explanation. He does not replace the Barthel number.",
                    ),
                    _source(
                        "Guy 1990",
                        "Guy treats delimiter crescents as distinct from night crescents. The code stays 041.",
                    ),
                    _source(
                        "Pozdniakov",
                        "No renumbering of these two signs is recorded in the sources already used.",
                    ),
                    _source(
                        "CEIPP outline",
                        "Both outlines are short crescents. The check did not print a second catalog number.",
                    ),
                ),
                baseline=True,
            ),
        ),
        "no_other_code": (
            "No source used here names a second Barthel number. A scan verdict cannot relabel these crescents.",
        ),
    },
    {
        "id": "D04",
        "passage": "Ca7",
        "position": "an extra path overlapping the first 378",
        "repo_code": "378",
        "tablets": ("C",),
        "baseline": "not_a_separate_sign",
        "alternatives": (
            _alternative(
                "not_a_separate_sign",
                "378",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "The delimiter token is 378. No extra group is stored between 041 and 378.",
                    ),
                    _source(
                        "CEIPP vector edition",
                        "A narrow path labeled _ sits inside the horizontal span of 378. Round 5B did not treat it as a new slot.",
                    ),
                ),
                baseline=True,
            ),
        ),
        "no_other_code": (
            "No published correction inserts a sign at this slot. Fischer's reported extra glyph at the start of line 7 is a different claim and is not this path. That glyph was not given a number in the sources used here, so it is not a choice.",
        ),
    },
    {
        "id": "D05",
        "passage": "Hr3",
        "position": "offset 37, parallel column with Qr3:17",
        "repo_code": "064",
        "tablets": ("H",),
        "baseline": "barthel_064",
        "alternatives": (
            _alternative(
                "barthel_064",
                "064",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "Hr3 offset 37 is 064. The same column on Q, Qr3 offset 17, is 064 in the vendored text and in the vector labels.",
                    ),
                    _source(
                        "Pozdniakov 1996 and Guy 2006",
                        "Both describe 006 and 064 as alternating hands. Neither source corrects this column. The match rule remains exact stem equality.",
                    ),
                ),
                baseline=True,
            ),
            _alternative(
                "ceipp_outline_006",
                "006",
                (
                    _source(
                        "CEIPP vector label",
                        "The vector label on this H outline is 006?, an uncertain hand. The replacement used here is 006. The question mark is the edition's uncertainty mark, not a third code.",
                    ),
                ),
            ),
        ),
        "no_other_code": (
            "The hand-pair merge that maps every isolated 064 to 006 is a Round 2 inventory test. It is not applied to any other 064.",
        ),
    },
    {
        "id": "D06",
        "passage": "Hr3",
        "position": "offsets 43-44",
        "repo_code": "006 then 042",
        "tablets": ("H",),
        "baseline": "barthel_006_then_042",
        "alternatives": (
            _alternative(
                "barthel_006_then_042",
                "006 then 042",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "Hr3 offsets 43 and 44 are 006 then 042. The parallel Q stems at Qr3 offsets 23 and 24 are the same pair in the same order.",
                    ),
                ),
                baseline=True,
            ),
            _alternative(
                "ceipp_vector_042_then_006",
                "042 then 006",
                (
                    _source(
                        "CEIPP vector edition",
                        "The two outlines share one slot. The vector lists 042 then 006. Round 5B kept the vendored order. No published correction deletes either stem.",
                    ),
                ),
            ),
        ),
        "no_other_code": (
            "Guy 1982 and Pozdniakov 1996 read stacks bottom to top. The allograph note records that convention and does not reorder. This recheck did not record which outline is the lower one, so that convention is not a third sequence.",
            "Guy's equation of glyph 42 with glyph 40 is the stacked pair on Br1. It is not applied to this Hr3 pair.",
        ),
    },
    {
        "id": "D07",
        "passage": "Qr3",
        "position": "the stacked pair inside the H/Q stretch",
        "repo_code": "006 then 042",
        "tablets": ("Q",),
        "baseline": "barthel_006_then_042",
        "alternatives": (
            _alternative(
                "barthel_006_then_042",
                "006 then 042",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "Qr3 offsets 23 and 24 are 006 then 042.",
                    ),
                ),
                baseline=True,
            ),
            _alternative(
                "ceipp_vector_042_then_006",
                "042 then 006",
                (
                    _source(
                        "CEIPP vector edition",
                        "The outlines overlap, and the vector lists the short sign first: 042 then 006.",
                    ),
                ),
            ),
        ),
        "no_other_code": (
            "No published correction changes the pair. The same bottom-to-top note as on Hr3 adds no third sequence.",
        ),
    },
    {
        "id": "D08",
        "passage": "Hr2:66 / Qr2:30 and Hr3:26 / Qr3:6",
        "position": "the two bird-substitution columns in the Great Tradition stretch",
        "repo_code": "600 opposite 400, and 607 opposite 407",
        "tablets": ("H", "Q"),
        "baseline": "barthel_and_ceipp_labels",
        "alternatives": (
            _alternative(
                "barthel_and_ceipp_labels",
                "600 opposite 400, and 607 opposite 407",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "The stored P001 columns are 600/400 and 607/407. The uncertainty mark on 400! strips to 400, and 607a strips to 607.",
                    ),
                    _source(
                        "CEIPP vector labels",
                        "Round 5B: the vector labels match those codes, including the uncertain mark on Q's 400!.",
                    ),
                    _source(
                        "Guy 2006",
                        "Guy classes series 400–409 and 600–699 as birds. That class is the bird-count rule. It does not rename either sign.",
                    ),
                    _source(
                        "Pozdniakov and Pozdniakov 2007",
                        "The 2007 inventory still lists 400 apart from 600. It does not rewrite these two columns.",
                    ),
                ),
                baseline=True,
            ),
            _alternative(
                "pozdniakov_1996_series_400_as_600",
                "600 opposite 600, and 607 opposite 607",
                (
                    _source(
                        "Pozdniakov 1996",
                        "Pozdniakov treats series 400 as variants of series 600 (the gaping-mouth note's hundreds rewrite, Pozdniakov 1996: 297, as recorded in decipherment/allographs.py). "
                        "Applied only at the two logged columns: Qr2:30 400 becomes 600, and Qr3:6 407 becomes 607. Other 400-series signs stay as coded.",
                    ),
                ),
            ),
        ),
        "no_other_code": (
            "Round 5B did not move either sign out of the pair. A corpus-wide hundreds rewrite remains the Round 2 inventory test and is not rerun.",
        ),
    },
    {
        "id": "D09",
        "passage": "Gv6",
        "position": "each of the six 076 outlines",
        "repo_code": "Y.076",
        "tablets": ("G",),
        "baseline": "barthel_suffix_attachment",
        "alternatives": (
            _alternative(
                "barthel_suffix_attachment",
                "076 stays the last stem of its group",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "Six Gv6 groups end in 076. Four of them are the Y.076 groups in the 200 X Y.076 phrases.",
                    ),
                    _source(
                        "CEIPP outline",
                        "Each 076 outline overlaps the previous sign and is separated from the next sign by a gap.",
                    ),
                    _source(
                        "Guy and Horley",
                        "Round 5B: Guy and Horley do not renumber these groups.",
                    ),
                ),
                baseline=True,
            ),
            _alternative(
                "davletshin_2012_076_opens_next_group",
                "each suffix 076 is prefixed to the following group",
                (
                    _source(
                        "Davletshin 2012",
                        "Davletshin says 076 may be read as opening the next name even though the drawing attaches it to the previous sign. "
                        "The counterfactual moves all six suffix 076s onto the next group. The Barthel numbers themselves do not change. This is a regrouping, not a new catalog number, and it is not a reading.",
                    ),
                ),
            ),
        ),
        "no_other_code": (
            "No source used here replaces 076 with another number on this line.",
        ),
    },
    {
        "id": "D10",
        "passage": "Ia1-Ia14",
        "position": "all 97 strokes coded 999, and the group after each pure 999",
        "repo_code": "999, then a group that usually contains 076",
        "tablets": ("I",),
        "baseline": "barthel_999_bar",
        "alternatives": (
            _alternative(
                "barthel_999_bar",
                "999, and 076 remains inside the following group",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "The Staff census counts pure 999 groups and whether the next group contains 076.",
                    ),
                    _source(
                        "CEIPP outline",
                        "Every outline coded 999 is a narrow stroke. Where the vector order inside a ligature differs (Ia5 021:290.076, Ia8 and Ia13 021:090.076), 076 is still in that group. The differing order was not stored digit by digit.",
                    ),
                    _source(
                        "Horley, Pozdniakov, and Guy",
                        "They do not publish a replacement list for these Staff bars in the sources already used.",
                    ),
                ),
                baseline=True,
            ),
        ),
        "no_other_code": (
            "A few other vector labels differ by a digit. Those digits were not recorded. A verdict cannot supply them.",
        ),
    },
    {
        "id": "D11",
        "passage": "Pr2",
        "position": "two unnumbered paths",
        "repo_code": "202s and 306s",
        "tablets": ("P",),
        "baseline": "not_a_new_token",
        "alternatives": (
            _alternative(
                "not_a_new_token",
                "202 and 306, with no inserted sign",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "The paths are not tokens in the vendored line.",
                    ),
                    _source(
                        "CEIPP vector edition",
                        "Each path labeled _ sits inside the horizontal span of the sign before it.",
                    ),
                ),
                baseline=True,
            ),
        ),
        "no_other_code": (
            "No published correction inserts them. A verdict cannot invent a number for an unnumbered path.",
        ),
    },
    {
        "id": "D12",
        "passage": "Hr4",
        "position": "offset 71, after the Great Tradition stretch that ends at Hr4:0",
        "repo_code": "042",
        "tablets": ("H",),
        "baseline": "barthel_042",
        "alternatives": (
            _alternative(
                "barthel_042",
                "042",
                (
                    _source(
                        "Barthel 1958, vendored CEIPP text",
                        "Hr4 offset 71 is 042. The headline H/Q stretch ends at Hr4 offset 0, so this stem is outside that stretch.",
                    ),
                ),
                baseline=True,
            ),
            _alternative(
                "ceipp_outline_048",
                "048",
                (
                    _source(
                        "CEIPP vector label",
                        "The vector label at this outline is 048. Round 5B did not match it to a catalog cell and did not adopt it.",
                    ),
                ),
            ),
        ),
        "no_other_code": (
            "Horley's 049-to-048 suggestion is a different sign. It is not applied here.",
        ),
    },
)


def _by_id() -> dict[str, dict[str, Any]]:
    return {row["id"]: row for row in DISAGREEMENTS}


def _choice_ids(row: dict[str, Any]) -> set[str]:
    return {alternative["id"] for alternative in row["alternatives"]}


def _require_provider(provider: MockProvider | None) -> MockProvider:
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("MockProvider is required")
    if provider.get_call_history():
        raise RuntimeError("MockProvider must not be called")
    return provider


@lru_cache(maxsize=1)
def _sides() -> dict[str, Any]:
    return {side.side: side for side in load_side_texts("stem")}


@lru_cache(maxsize=1)
def _passages() -> tuple[dict[str, Any], ...]:
    payload = json.loads(PASSAGE_PATH.read_text(encoding="utf-8"))
    return tuple(payload["stem"]["passages"])


@lru_cache(maxsize=1)
def _gv6_groups() -> tuple[str, ...]:
    from tests.test_mamari_small_santiago_gv_scoreboard import (
        extract_gv_published_tokens,
        load_vendored_gv_html,
    )

    return tuple(extract_gv_published_tokens(load_vendored_gv_html())["Gv6"])


@lru_cache(maxsize=1)
def _staff_lines() -> tuple[tuple[str, tuple[str, ...]], ...]:
    from tests.test_mamari_santiago_ia_scoreboard import (
        IA_LINE_NAMES,
        extract_ia_published_tokens,
        load_vendored_ia_html,
    )

    published = extract_ia_published_tokens(load_vendored_ia_html())
    return tuple((name, tuple(published[name])) for name in IA_LINE_NAMES)


def _verify_sites() -> None:
    sides = _sides()
    for (side_name, line, offset), expected in EXPECTED_STEMS.items():
        side = sides[side_name]
        found = side.signs[side.absolute(line, offset)]
        if found != expected:
            raise RuntimeError(
                f"{side_name} {line}:{offset} is {found}, and the protocol expects {expected}"
            )
    tokens = load_fixture_tokens()
    if tokens["Ca7"].count("600.390.041") != 1:
        raise RuntimeError("Ca7 no longer has one 600.390.041 group")
    if tokens["Ca7"].count("044.040") != 1:
        raise RuntimeError("Ca7 no longer has one 044.040 group")
    if tokens["Ca7"].count("041h") != 1 or tokens["Ca8"].count("041h") != 1:
        raise RuntimeError("the two 041h delimiter crescents are not where the protocol expects them")
    ca7 = list(tokens["Ca7"])
    if ("390.041", "378", "041") != tuple(ca7[ca7.index("390.041") : ca7.index("390.041") + 3]):
        raise RuntimeError("the first Ca7 delimiter no longer begins 390.041, 378, 041")
    suffixes = [
        group
        for group in _gv6_groups()
        if len(group_stems(group)) > 1 and group_stems(group)[-1] == "076"
    ]
    if len(suffixes) != 6:
        raise RuntimeError(f"Gv6 has {len(suffixes)} suffix-076 groups, and the protocol expects 6")
    passage = _headline_passage(_passages())
    if passage["left"]["locus"] != HEADLINE_LEFT_LOCUS:
        raise RuntimeError("P001 left locus moved")
    if passage["right"]["locus"] != HEADLINE_RIGHT_LOCUS:
        raise RuntimeError("P001 right locus moved")


def _headline_passage(passages: tuple[dict[str, Any], ...] | list[dict[str, Any]]) -> dict[str, Any]:
    for passage in passages:
        if passage["id"] == HEADLINE_PASSAGE_ID:
            return passage
    raise KeyError(HEADLINE_PASSAGE_ID)


def _replace_token(tokens: dict[str, list[str]], line: str, old: str, new: str) -> None:
    hits = [index for index, token in enumerate(tokens[line]) if token == old]
    if len(hits) != 1:
        raise RuntimeError(f"{line} has {len(hits)} copies of {old}")
    tokens[line][hits[0]] = new


def detach_suffix_076(groups: list[str] | tuple[str, ...]) -> list[str]:
    """Move each suffix 076 onto the following group.

    The following group is not searched again. A final suffix with no
    following group would become its own group. Gv6 has no such case.
    """
    output: list[str] = []
    index = 0
    sequence = list(groups)
    while index < len(sequence):
        stems = group_stems(sequence[index])
        if len(stems) > 1 and stems[-1] == "076":
            output.append(".".join(stems[:-1]))
            if index + 1 >= len(sequence):
                output.append("076")
                break
            output.append("076." + sequence[index + 1])
            index += 2
            continue
        output.append(sequence[index])
        index += 1
    return output


def normalize_choices(raw: dict[str, str] | None) -> dict[str, str]:
    """Fill omitted rows with the Barthel choice. Reject unknown ids."""
    supplied = {} if raw is None else dict(raw)
    known = _by_id()
    unknown = sorted(set(supplied) - set(known))
    if unknown:
        raise ValueError(f"unknown disagreement ids: {', '.join(unknown)}")
    choices: dict[str, str] = {}
    for row in DISAGREEMENTS:
        choice = supplied.get(row["id"], row["baseline"])
        if choice not in _choice_ids(row):
            legal = ", ".join(sorted(_choice_ids(row)))
            raise ValueError(f"{row['id']} has no choice {choice}. Legal choices: {legal}")
        choices[row["id"]] = choice
    return choices


def _edits_for(choices: dict[str, str]) -> dict[tuple[str, str, int], str]:
    edits: dict[tuple[str, str, int], str] = {}

    def put(side: str, line: str, offset: int, stem: str) -> None:
        key = (side, line, offset)
        if key in edits and edits[key] != stem:
            raise ValueError(f"two choices write {side} {line}:{offset}")
        edits[key] = stem

    if choices["D05"] == "ceipp_outline_006":
        put("Hr", "Hr3", 37, "006")
    if choices["D06"] == "ceipp_vector_042_then_006":
        put("Hr", "Hr3", 43, "042")
        put("Hr", "Hr3", 44, "006")
    if choices["D07"] == "ceipp_vector_042_then_006":
        put("Qr", "Qr3", 23, "042")
        put("Qr", "Qr3", 24, "006")
    if choices["D08"] == "pozdniakov_1996_series_400_as_600":
        put("Qr", "Qr2", 30, "600")
        put("Qr", "Qr3", 6, "607")
    if choices["D12"] == "ceipp_outline_048":
        put("Hr", "Hr4", 71, "048")
    return edits


def _apply_stem_edits(
    passages: list[dict[str, Any]],
    edits: dict[tuple[str, str, int], str],
) -> None:
    if not edits:
        return
    sides = _sides()
    for passage in passages:
        left_meta = passage["left"]
        right_meta = passage["right"]
        left_text = sides[left_meta["side"]]
        right_text = sides[right_meta["side"]]
        left_index = left_meta["start"]
        right_index = right_meta["start"]
        for column in passage["columns"]:
            if column[0] is not None:
                line, offset = left_text.locate(left_index)
                replacement = edits.get((left_meta["side"], line, offset))
                if replacement is not None:
                    column[0] = replacement
                left_index += 1
            if column[1] is not None:
                line, offset = right_text.locate(right_index)
                replacement = edits.get((right_meta["side"], line, offset))
                if replacement is not None:
                    column[1] = replacement
                right_index += 1


def _calendar_stats(choices: dict[str, str]) -> dict[str, Any]:
    tokens = {name: list(groups) for name, groups in load_fixture_tokens().items()}
    if choices["D01"] == "guy_1990_star690":
        _replace_token(tokens, "Ca7", "600.390.041", "*690.041")
    if choices["D02"] == "guy_1990_078_040":
        _replace_token(tokens, "Ca7", "044.040", "078.040")
    frozen = {name: tuple(groups) for name, groups in tokens.items()}
    lines = stem_lines(frozen)
    flat = flatten(lines)
    before, after = guy_040_counts(lines, OPENERS)
    return {
        "calendar_040": flat.count("040"),
        "calendar_040_before_152": before,
        "calendar_040_after_152": after,
        "calendar_040_gaps": list(between_delimiter_040(lines, OPENERS)),
        "calendar_full_delimiters": count_378_delimiters(lines, OPENERS),
        "calendar_152": flat.count("152"),
        "calendar_143": flat.count("143"),
    }


def _gv6_stats(choices: dict[str, str]) -> dict[str, int]:
    groups: list[str] | tuple[str, ...] = _gv6_groups()
    if choices["D09"] == "davletshin_2012_076_opens_next_group":
        groups = detach_suffix_076(groups)
    phrases = extract_strict_phrases(list(groups), "Gv6")
    return {
        "gv6_phrases": len(phrases),
        "gv6_handoffs": chain_links(phrases),
    }


def _staff_stats() -> dict[str, Any]:
    lines = [(name, list(groups)) for name, groups in _staff_lines()]
    census = fischer_census(lines)
    return {
        "staff_076_after_999": census.immediate_076_group,
        "staff_pure_999": census.pure_breaks,
        "staff_076_after_999_rate": census.immediate_076_group / census.pure_breaks,
    }


def _parallel_stats(choices: dict[str, str]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    original = [copy.deepcopy(passage) for passage in _passages()]
    edited = [copy.deepcopy(passage) for passage in _passages()]
    _apply_stem_edits(edited, _edits_for(choices))
    headline = _headline_passage(edited)
    matches, mismatches, _gaps, left_used, right_used = _column_counts(headline["columns"])
    stretch_birds = sum(1 for left, right in headline["columns"] if _bird_pair(left, right))
    corpus_birds = 0
    for passage in edited:
        for left, right in passage["columns"]:
            if _bird_pair(left, right):
                corpus_birds += 1
    stats = {
        "parallel_span": max(left_used, right_used),
        "parallel_matches": matches,
        "parallel_mismatches": mismatches,
        "parallel_bird_substitutions": stretch_birds,
        "corpus_bird_substitutions": corpus_birds,
    }
    changes: list[dict[str, Any]] = []
    edited_by_id = {passage["id"]: passage for passage in edited}
    for passage in original:
        if passage["id"] == HEADLINE_PASSAGE_ID:
            continue
        before = _column_counts(passage["columns"])[0]
        after = _column_counts(edited_by_id[passage["id"]]["columns"])[0]
        if before == after:
            continue
        changes.append(
            {
                "id": passage["id"],
                "label": passage.get("publication_label"),
                "locus_left": passage["left"]["locus"],
                "locus_right": passage["right"]["locus"],
                "matches_before": before,
                "matches_after": after,
                "by": after - before,
                "headline": False,
            }
        )
    changes.sort(key=lambda row: row["id"])
    return stats, changes


def headline_stats(choices: dict[str, str]) -> dict[str, Any]:
    """The Round 5B headline bundle under one set of registered choices."""
    stats: dict[str, Any] = {}
    stats.update(_calendar_stats(choices))
    stats.update(_gv6_stats(choices))
    stats.update(_staff_stats())
    parallel, _changes = _parallel_stats(choices)
    stats.update(parallel)
    return {key: stats[key] for key in HEADLINE_KEYS}


def headline_delta(baseline: dict[str, Any], updated: dict[str, Any]) -> dict[str, Any]:
    """Keys whose values moved. Integer keys also carry the signed difference."""
    delta: dict[str, Any] = {}
    for key in HEADLINE_KEYS:
        if baseline[key] == updated[key]:
            continue
        row: dict[str, Any] = {"before": baseline[key], "after": updated[key]}
        if isinstance(baseline[key], int) and isinstance(updated[key], int):
            row["by"] = updated[key] - baseline[key]
        delta[key] = row
    return delta


def _check_evidence(
    evidence: str,
    choices: dict[str, str],
    image_note: str | None,
) -> None:
    if evidence not in EVIDENCE_VALUES:
        legal = ", ".join(EVIDENCE_VALUES)
        raise ValueError(f"unknown evidence {evidence}. Legal values: {legal}")
    note = (image_note or "").strip()
    if evidence == EVIDENCE_LATER_IMAGE and not note:
        raise ValueError("later_image requires image_note naming the image source")
    if evidence != EVIDENCE_LATER_IMAGE and note:
        raise ValueError("image_note is only used when evidence is later_image")
    if evidence != EVIDENCE_INSCRIBE:
        return
    known = _by_id()
    blocked = []
    for disagreement_id, choice in choices.items():
        row = known[disagreement_id]
        if choice == row["baseline"]:
            continue
        if set(row["tablets"]).issubset(INSCRIBE_TABLETS):
            continue
        blocked.append(disagreement_id)
    if blocked:
        names = ", ".join(blocked)
        raise ValueError(
            f"INSCRIBE models do not cover {names}. "
            "Those choices stay on the Barthel code under evidence inscribe."
        )


def recompute(
    verdict: dict[str, Any],
    provider: MockProvider | None = None,
) -> dict[str, Any]:
    """Recompute every headline count for one verdict file's contents.

    ``verdict`` has ``provider``, ``evidence``, optional ``image_note``,
    and ``choices``. Omitted choice ids keep the Barthel code. The vendored
    pages are not written.
    """
    provider = _require_provider(provider)
    if not isinstance(verdict, dict):
        raise TypeError("verdict must be an object")
    if verdict.get("provider") not in (None, "MockProvider"):
        raise ValueError("verdict provider must be MockProvider")
    evidence = verdict.get("evidence")
    if not isinstance(evidence, str):
        raise ValueError("verdict evidence is required")
    image_note = verdict.get("image_note")
    if image_note is not None and not isinstance(image_note, str):
        raise ValueError("image_note must be a string")
    raw_choices = verdict.get("choices") or {}
    if not isinstance(raw_choices, dict):
        raise ValueError("choices must be an object")
    choices = normalize_choices({str(key): str(value) for key, value in raw_choices.items()})
    _check_evidence(evidence, choices, image_note)
    _verify_sites()
    baseline_choices = normalize_choices({})
    baseline = headline_stats(baseline_choices)
    updated = headline_stats(choices)
    other_changes = _parallel_stats(choices)[1]
    return {
        "track": "round6a",
        "provider": "MockProvider",
        "provider_calls": len(provider.get_call_history()),
        "readings_assigned": False,
        "reading": None,
        "evidence": evidence,
        "image_note": image_note if evidence == EVIDENCE_LATER_IMAGE else None,
        "transcription_updated": False,
        "images_fetched": False,
        "choices": choices,
        "headline": updated,
        "headline_delta": headline_delta(baseline, updated),
        "other_passage_match_changes": other_changes,
    }


def _row_public(row: dict[str, Any]) -> dict[str, Any]:
    tablets = list(row["tablets"])
    return {
        "id": row["id"],
        "passage": row["passage"],
        "position": row["position"],
        "repo_code": row["repo_code"],
        "tablets": tablets,
        "inscribe_covered": set(tablets).issubset(INSCRIBE_TABLETS),
        "baseline": row["baseline"],
        "alternatives": [dict(alternative) for alternative in row["alternatives"]],
        "no_other_code": list(row["no_other_code"]),
    }


def _single_choice_record(
    row: dict[str, Any],
    alternative: dict[str, Any],
    baseline: dict[str, Any],
    provider: MockProvider,
) -> dict[str, Any]:
    verdict = {
        "provider": "MockProvider",
        "evidence": EVIDENCE_COUNTERFACTUAL,
        "choices": {row["id"]: alternative["id"]},
    }
    result = recompute(verdict, provider)
    return {
        "id": alternative["id"],
        "sign_codes": alternative["sign_codes"],
        "baseline": alternative["baseline"],
        "sources": alternative["sources"],
        "headline_after": result["headline"],
        "headline_delta": result["headline_delta"],
        "other_passage_match_changes": result["other_passage_match_changes"],
        "matches_baseline": result["headline"] == baseline,
    }


def build_preregistration(provider: MockProvider | None = None) -> dict[str, Any]:
    """The frozen catalog, the baseline counts, and each single-choice effect."""
    provider = _require_provider(provider)
    _verify_sites()
    baseline = headline_stats(normalize_choices({}))
    rows = []
    for row in DISAGREEMENTS:
        public = _row_public(row)
        public["alternatives"] = [
            _single_choice_record(row, alternative, baseline, provider)
            for alternative in row["alternatives"]
        ]
        rows.append(public)
    combinations = []
    for label, choices in (
        (
            "D01 and D02 together",
            {"D01": "guy_1990_star690", "D02": "guy_1990_078_040"},
        ),
        (
            "D06 and D07 together",
            {
                "D06": "ceipp_vector_042_then_006",
                "D07": "ceipp_vector_042_then_006",
            },
        ),
        (
            "D05, D06, and D08 together",
            {
                "D05": "ceipp_outline_006",
                "D06": "ceipp_vector_042_then_006",
                "D08": "pozdniakov_1996_series_400_as_600",
            },
        ),
    ):
        result = recompute(
            {
                "provider": "MockProvider",
                "evidence": EVIDENCE_COUNTERFACTUAL,
                "choices": choices,
            },
            provider,
        )
        combinations.append(
            {
                "label": label,
                "choices": choices,
                "headline_delta": result["headline_delta"],
                "other_passage_match_changes": result["other_passage_match_changes"],
            }
        )
    covered = [row["id"] for row in rows if row["inscribe_covered"]]
    uncovered = [row["id"] for row in rows if not row["inscribe_covered"]]
    logged_tablets = {tablet for row in DISAGREEMENTS for tablet in row["tablets"]}
    report = {
        "track": "round6a",
        "provider": "MockProvider",
        "provider_calls": len(provider.get_call_history()),
        "readings_assigned": False,
        "reading": None,
        "images_fetched": False,
        "transcription_updated": False,
        "inscribe": {
            "tablets": list(INSCRIBE_TABLETS),
            "source": "docs/round4e_image_sources.md",
            "viewer": "https://www.inscribercproject.com/Rongorongo.php",
            "rome_models": ["A", "B", "C", "D"],
            "downsampled_vienna_meshes": ["M", "N"],
            "tablets_with_a_model_and_no_logged_disagreement": [
                tablet for tablet in INSCRIBE_TABLETS if tablet not in logged_tablets
            ],
            "statement": (
                "The six models were not opened and were not copied into this repository. "
                "An INSCRIBE verdict may select a non-baseline code only for a disagreement "
                "whose tablets are all in this list."
            ),
        },
        "counting_rules": {
            "delimiter_openers": ["390"],
            "star690_is_not_an_opener": (
                "Guy's *690 keeps its asterisk and is not catalog 690. "
                "A delimiter still has to open on 390. Round 3 printed the gaps that remain "
                "if *690 is added to the opener set; this script does not add it."
            ),
            "parallel_match": "exact stem equality, the same rule as decipherment.track_c_parallels._column_counts",
            "headline_passage": {
                "id": HEADLINE_PASSAGE_ID,
                "section": "stem",
                "left": HEADLINE_LEFT_LOCUS,
                "right": HEADLINE_RIGHT_LOCUS,
            },
            "bird_pair": "400–409 opposite 600–699, or the reverse, and the hundreds digits differ",
            "gv6_phrase": "200, then a group without 200 or 076, then a group whose last stem is 076",
            "gv6_handoff": "the father stems of one phrase are the child stems of the next phrase",
            "staff": "a pure 999 group, then whether the next group contains 076",
            "corpus_birds": "every stem passage in data/decipherment/substitution_classes.json",
        },
        "verdict_schema": {
            "provider": "MockProvider",
            "evidence": list(EVIDENCE_VALUES),
            "image_note": "Required only when evidence is later_image. The script does not fetch it.",
            "choices": "Object of disagreement id to alternative id. Omitted ids keep the baseline.",
            "rejects": (
                "Unknown ids, a non-baseline choice on a tablet outside the INSCRIBE list "
                "when evidence is inscribe, and any code that is not registered here."
            ),
        },
        "baseline": baseline,
        "disagreement_ids_on_inscribe_tablets": covered,
        "disagreement_ids_outside_inscribe": uncovered,
        "disagreements": rows,
        "checked_combinations": combinations,
        "round5b_record": str(ROUND5B_PATH.relative_to(REPO_ROOT)),
    }
    return json.loads(json.dumps(report))


def write_preregistration(
    path: Path = OUTPUT_PATH,
    provider: MockProvider | None = None,
) -> dict[str, Any]:
    report = build_preregistration(provider if provider is not None else MockProvider())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Recompute headline counts from a Round 6A verdict.")
    parser.add_argument("--verdict", type=Path, help="Verdict JSON. Prints the recomputed counts.")
    parser.add_argument(
        "--write-preregistration",
        action="store_true",
        help="Write data/decipherment/round6a_preregistration.json.",
    )
    args = parser.parse_args(argv)
    if args.verdict is None and not args.write_preregistration:
        parser.error("pass --verdict, --write-preregistration, or both")
    provider = MockProvider()
    if args.write_preregistration:
        write_preregistration(provider=provider)
    if args.verdict is not None:
        verdict = json.loads(args.verdict.read_text(encoding="utf-8"))
        result = recompute(verdict, provider)
        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
