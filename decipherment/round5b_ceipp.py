"""Round 5 Track B: recheck key passages against the CEIPP drawings.

The raster strips on the Kohaumotu mirror of rongorongo.org are Barthel's
tracings at about 74 pixels tall. Catalog numbers are not re-read off those
strips. Geometry (a crescent, a bar, a shared slot) comes from the vector
outlines on the same mirror, which trace each glyph separately. A Barthel
number is not replaced unless the outline contradicts the code and a
published correction names the replacement. None did. ``MockProvider`` is
accepted and never called.
"""

from __future__ import annotations

import json
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
from decipherment.track3_genealogy import (
    fischer_census,
    genealogy_census,
    group_stems,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
PASSAGE_PATH = REPO_ROOT / "data" / "decipherment" / "substitution_classes.json"
OUTPUT_PATH = REPO_ROOT / "data" / "decipherment" / "round5b_ceipp_recheck.json"

CEIPP_LICENCE = (
    "There are no restrictions on copying and distributing the contents of "
    "this site as long as the sources are acknowledged and the distribution "
    "is non-profit."
)
CEIPP_LICENCE_URL = "http://kohaumotu.org/rongorongo_org/copy.html"
CEIPP_SOURCE = (
    "Drawings and transliteration: C.E.I.P.P. (Cercle d'Études sur l'Île de "
    "Pâques et la Polynésie), from Thomas Barthel's materials, as published "
    "on rongorongo.org and mirrored at kohaumotu.org."
)

# Raster strips fetched for this check. Pixel size is width, height.
# Hashes are SHA-256 of the bytes retrieved on 2026-09-27.
RASTER_STRIPS: tuple[dict[str, Any], ...] = (
    {
        "file": "Ca0603.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/C/Ca0603.png",
        "pixels": [522, 74],
        "sha256": "9b00475d09f04698b24287ec5030c06c90edbc1672b1628ab488f3d7ff883acf",
    },
    {
        "file": "Ca0701.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/C/Ca0701.png",
        "pixels": [522, 74],
        "sha256": "1446d6208480df3a88de95f5baccf63f729a3e0c4448fa0a2d17a214c1e85f58",
    },
    {
        "file": "Ca0702.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/C/Ca0702.png",
        "pixels": [522, 74],
        "sha256": "fb8f6babc2cee306662945e7645f2cff561e4179b6c1f6edf1dcd495a76298db",
    },
    {
        "file": "Ca0703.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/C/Ca0703.png",
        "pixels": [522, 74],
        "sha256": "3a455b639daa210adc474cfccaf63c0a45169b23d4528d1cdfb8fdb7599d91f7",
    },
    {
        "file": "sca0701.gif",
        "url": "http://kohaumotu.org/rongorongo_org/mamari/sca0701.gif",
        "pixels": [522, 74],
        "sha256": "d24f2b41e36607cafec2fb1245ac3336ee57bc0fce8c5732a7abe5022c693e2b",
    },
    {
        "file": "Gv0601.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/G/Gv0601.png",
        "pixels": [622, 74],
        "sha256": "2c5c1c5d2760459dab8e04bc68cd0fd16185305b8126e91acc5fbb1c7ff594ad",
    },
    {
        "file": "Gv0602.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/G/Gv0602.png",
        "pixels": [622, 74],
        "sha256": "8fae737e1dd5a1fc009a0696737976e66ddc7cf260c5b4dcf51126544cbae794",
    },
    {
        "file": "Hr0204.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/H/Hr0204.png",
        "pixels": [622, 74],
        "sha256": "b452718d508984e6ce7a74a323d7209b6b3e2d3a42714576060e5a0c531ae647",
    },
    {
        "file": "Hr0302.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/H/Hr0302.png",
        "pixels": [622, 74],
        "sha256": "8000e2d56819d29a9ba7dee779553026b4c2a79af27566606b5918ab75d8e8f4",
    },
    {
        "file": "Qr0202.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/Q/Qr0202.png",
        "pixels": [622, 74],
        "sha256": "9c59f0b94568c84b3bdacb6b4b2b80f2e0a7ad94324f6dee6528591b403f4814",
    },
    {
        "file": "Qr0301.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/Q/Qr0301.png",
        "pixels": [622, 74],
        "sha256": "e49e7134c6604b2757ddd644e47eb9df70527acc68a65f9aacbb6bf877bb0065",
    },
    {
        "file": "Ia0503.png",
        "url": "http://kohaumotu.org/Rongorongo/images/ba/I/Ia0503.png",
        "pixels": [622, 74],
        "sha256": "daa8144ec575cfc67825ef658d4fb02881cf1194250939b2169ca087abcf1304",
    },
)

# Vector editions used for outline geometry. Same mirror, not a second corpus.
VECTOR_PAGES: tuple[dict[str, str], ...] = (
    {
        "tablet": "C",
        "url": "http://kohaumotu.org/Rongorongo/svg/C_svg_codes_b.html",
        "sha256": "f1c8d80d8e090f35696f67ac2024cfb9ccb96ed3cd9dba9ac3fcb8b9cf71c202",
    },
    {
        "tablet": "G",
        "url": "http://kohaumotu.org/Rongorongo/svg/G_svg_codes_b.html",
        "sha256": "6771f804e6f1b133697174edbe561e0395b55b5bef5b3e8bad666a15f1c9ab57",
    },
    {
        "tablet": "H",
        "url": "http://kohaumotu.org/Rongorongo/svg/H_svg_codes_b.html",
        "sha256": "bc7f50cb125bb671f9952336f205cd827b547a30d131b3478b1a8600eb3a688b",
    },
    {
        "tablet": "P",
        "url": "http://kohaumotu.org/Rongorongo/svg/P_svg_codes_b.html",
        "sha256": "27a19f29b23e085a519ccc064e2133ebf6a875e57185f3bb0f681955c6def1a3",
    },
    {
        "tablet": "Q",
        "url": "http://kohaumotu.org/Rongorongo/svg/Q_svg_codes_b.html",
        "sha256": "eae7d28c88d7931d13ada03b50a3d0fcd9f7b8ef6bddfdaad8d7f67bf642bc5e",
    },
    {
        "tablet": "I",
        "url": "http://kohaumotu.org/Rongorongo/svg/I_svg_codes_b.html",
        "sha256": "cf6418e104f5d904f7983266296d804c74c89c8cf1b924d4bffa8e818c57ccc3",
    },
)

# Measured on the vector outlines. A tall crescent here is height/width above
# 2.2 and width under 40 user units. A bar is width under 8.
GEOMETRY: dict[str, Any] = {
    "calendar_040_tall_crescents": 28,
    "calendar_040_expected": 28,
    "crescent_143_width": 39.1,
    "crescent_143_height": 78.1,
    "sign_152_width": 46.6,
    "sign_152_height": 76.8,
    "small_041h": (
        {"line": "Ca7", "index": 23, "width": 17.2, "height": 23.3},
        {"line": "Ca8", "index": 6, "width": 15.4, "height": 32.0},
    ),
    "post_152_stack": {
        "line": "Ca7",
        "repo_group": "600.390.041",
        "shared_slot": ["390", "600"],
        "shared_slot_heights": [53.6, 31.8],
        "following_crescent": "041",
    },
    "staff_999_count": 97,
    "staff_999_width_min": 2.38,
    "staff_999_width_max": 7.62,
    "gv6_076_overlaps_previous": 6,
    "gv6_076_gap_before_next_sign": 6,
    "bird_sites": (
        {
            "left": "Hr2:66",
            "left_label": "600",
            "right": "Qr2:30",
            "right_label": "400!",
            "both_full_height": True,
        },
        {
            "left": "Hr3:26",
            "left_label": "607a",
            "right": "Qr3:6",
            "right_label": "407",
            "both_full_height": True,
        },
    ),
}


def _disagreement(
    passage: str,
    position: str,
    repo_code: str,
    drawing: str,
    confidence: str,
    published: str,
    adopted: bool = False,
) -> dict[str, Any]:
    return {
        "passage": passage,
        "position": position,
        "repo_code": repo_code,
        "drawing": drawing,
        "confidence": confidence,
        "horley_pozdniakov_guy": published,
        "adopted": adopted,
    }


DISAGREEMENTS: tuple[dict[str, Any], ...] = (
    _disagreement(
        "Ca7",
        "the group after 152, one horizontal slot",
        "600.390.041",
        "The outlines labeled 600 and 390 share one horizontal slot and are both shorter than the full-height signs beside them. The crescent 041 is the next slot, not part of that stack.",
        "high that this is one slot plus a crescent; the catalog number of the stack was not re-read",
        "Guy 1990 calls the stack one sign, *690, and says catalog 690 is a different sign. Round 3 already recorded that proposal. Horley 2011 and Pozdniakov do not renumber this group in the sources used there. This recheck does not adopt *690, because the outline does not name that number.",
    ),
    _disagreement(
        "Ca7",
        "the group 044.040, before 143 and 152",
        "044.040",
        "A non-crescent figure sits beside a tall crescent. The figure is not a second crescent.",
        "high for figure-plus-crescent; low for choosing 044 or 078",
        "Guy 1990 proposes 078.040 and keeps the crescent. The outline fits either 044 or 078. Horley and Pozdniakov do not supply a different number in the sources already used. Not adopted.",
    ),
    _disagreement(
        "Ca7 and Ca8",
        "the two signs coded 041h inside delimiter groups",
        "041h",
        "Both outlines are short crescents, about a quarter to a third the height of the ordinary 041 crescents on the same lines.",
        "high that they are small crescents",
        "Horley 2011 says the two small superscript crescents have a paleographic explanation. He does not replace the Barthel number. Pozdniakov does not renumber them here. Guy 1990 treats delimiter crescents as distinct from night crescents. The code stays 041.",
    ),
    _disagreement(
        "Ca7",
        "an extra path overlapping the first 378",
        "378",
        "The vector edition traces a narrow unnumbered path, labeled _, inside the horizontal span of 378. It is not a separate slot between 041 and 378.",
        "high that it is not a new hyphen-group",
        "No published correction inserts a sign at this slot. Fischer's reported extra glyph at the start of line 7 is a different claim and is not this path. Not adopted.",
    ),
    _disagreement(
        "Hr3",
        "offset 37, parallel column with Qr3:17",
        "064",
        "The vector label on H is 006?, an uncertain hand. The same column on Q is 064 in both the vendored text and the vector labels. The outline is a full-height sign, not a bar or a crescent.",
        "low for replacing 064",
        "Pozdniakov 1996 treats hands 006 and 064 as alternating in repeated phrases. Guy 2006 describes the same alternation. Neither source corrects this column. Adopting 006 would create a mismatch with Q, which still reads 064. Not adopted.",
    ),
    _disagreement(
        "Hr3",
        "offsets 43-44",
        "006 then 042",
        "The two outlines share one horizontal slot. One is short and one is taller. The vector lists 042 then 006. The vendored text lists 006 then 042. The pair of stems is the same.",
        "high that the slot is shared; the internal order is the edition's stacking order",
        "No published correction splits or deletes this pair. Not adopted.",
    ),
    _disagreement(
        "Qr3",
        "the stacked pair inside the H/Q stretch",
        "006 then 042",
        "Same situation as Hr3: the outlines overlap, and the vector lists the short sign first.",
        "high that the slot is shared",
        "No published correction changes the pair. Not adopted.",
    ),
    _disagreement(
        "Hr2:66 / Qr2:30 and Hr3:26 / Qr3:6",
        "the two bird-substitution columns in the Great Tradition stretch that starts on recto line 2",
        "600 opposite 400, and 607 opposite 407",
        "Each outline is a full-height figure between a human figure and a fish sign, or in the same kind of parallel slot. The vector labels match the vendored codes, including the uncertain mark on Q's 400!.",
        "high that the labels match and that neither sign is a bar or a crescent; not a new species reading",
        "Guy 2006 classes series 400-409 and 600-699 as birds. Pozdniakov had treated gaping-mouth and bird heads as variants. Nothing here moves a sign out of that pair. Not adopted as a code change.",
    ),
    _disagreement(
        "Gv6",
        "each of the six 076 outlines",
        "Y.076",
        "Each 076 outline overlaps the previous sign and is separated from the next sign by a gap. The 200 outlines are full figures, not bars. All 38 stems match the vendored line.",
        "high for suffix attachment",
        "Davletshin 2012 says 076 may be read as opening the next name even though the drawing attaches it to the previous sign. The outlines attach it to the previous sign. Guy and Horley do not renumber these groups. Not adopted.",
    ),
    _disagreement(
        "Ia1-Ia14",
        "all 97 strokes coded 999, and the group after each pure 999",
        "999, then a group that usually contains 076",
        "Every outline coded 999 is a narrow stroke, width between 2.4 and 7.6 user units. No 999 is a full figure. Where the vector component order inside a ligature differs from the vendored colon order (Ia5 021:290.076, Ia8 and Ia13 021:090.076), 076 is still in that group. A few other vector labels differ by a digit from the vendored code; those outlines were not given a new number.",
        "high that 999 is a bar and that the 076-after-999 count is unchanged; low for the one-digit label conflicts",
        "Horley, Pozdniakov, and Guy do not publish a replacement list for these Staff bars in the sources already used. Not adopted.",
    ),
    _disagreement(
        "Pr2",
        "two unnumbered paths",
        "202s and 306s",
        "Each path labeled _ sits inside the horizontal span of the sign before it. Neither opens a new slot.",
        "high that they are not new tokens",
        "No published correction inserts them. Not adopted.",
    ),
    _disagreement(
        "Hr4",
        "offset 71, after the Great Tradition stretch that ends at Hr4:0",
        "042",
        "The vector label is 048. The outline is a separate tall narrow sign. It was not matched to a catalog cell.",
        "low",
        "Outside the counted stretch. No published correction of this sign was applied. Not adopted.",
    ),
)


def _bird_pair(left: str | None, right: str | None) -> bool:
    def number(sign: str | None) -> int | None:
        if not sign:
            return None
        digits = "".join(character for character in sign if character.isdigit())
        if not digits:
            return None
        return int(digits)

    left_number = number(left)
    right_number = number(right)
    if left_number is None or right_number is None or left_number // 100 == right_number // 100:
        return False

    def bird(value: int) -> bool:
        return 400 <= value <= 409 or 600 <= value <= 699

    return bird(left_number) and bird(right_number)


def bird_substitution_counts() -> dict[str, Any]:
    """Bird cross-hundred mismatches in the stored Round 2 passages.

    No stem in those passages was edited, so the count is the standing one.
    """
    payload = json.loads(PASSAGE_PATH.read_text(encoding="utf-8"))
    passages = payload["stem"]["passages"]
    corpus = 0
    stretch = 0
    stretch_pairs: list[dict[str, str]] = []
    p001 = None
    for passage in passages:
        if passage["id"] == "P001":
            p001 = passage
        for left, right in passage["columns"]:
            if not _bird_pair(left, right):
                continue
            corpus += 1
            if passage["id"] == "P001":
                stretch += 1
                stretch_pairs.append({"left": left, "right": right})
    if p001 is None:
        raise KeyError("P001")
    return {
        "corpus_bird_cross_hundred": corpus,
        "stretch_id": "P001",
        "stretch_locus_left": p001["left"]["locus"],
        "stretch_locus_right": p001["right"]["locus"],
        "stretch_span": p001["span"],
        "stretch_matches": p001["matches"],
        "stretch_mismatches": p001["mismatches"],
        "stretch_bird_pairs": stretch,
        "stretch_bird_columns": stretch_pairs,
    }


def _line_groups(published: dict[str, list[str]], names: tuple[str, ...]) -> list[tuple[str, list[str]]]:
    return [(name, list(published[name])) for name in names]


def calendar_stats() -> dict[str, Any]:
    """Track 1 calendar counts on the vendored slice. No code was replaced."""
    tokens = load_fixture_tokens()
    lines = stem_lines(tokens)
    flat = flatten(lines)
    openers = frozenset({"390"})
    return {
        "stems": len(flat),
        "040": flat.count("040"),
        "040_before_after_152": list(guy_040_counts(lines, openers)),
        "040_gaps": list(between_delimiter_040(lines, openers)),
        "full_delimiters_opening_390": count_378_delimiters(lines, openers),
        "152": flat.count("152"),
        "143": flat.count("143"),
    }


def genealogy_and_staff() -> dict[str, Any]:
    """Gv6 handoffs and the Staff 076-after-999 count, from the vendored pages."""
    from tests.test_mamari_santiago_ia_scoreboard import (
        IA_LINE_NAMES,
        extract_ia_published_tokens,
        load_vendored_ia_html,
    )
    from tests.test_mamari_small_santiago_gr_scoreboard import (
        GR_LINE_NAMES,
        extract_gr_published_tokens,
        load_vendored_gr_html,
    )
    from tests.test_mamari_small_santiago_gv_scoreboard import (
        GV_LINE_NAMES,
        extract_gv_published_tokens,
        load_vendored_gv_html,
    )

    ia = extract_ia_published_tokens(load_vendored_ia_html())
    gv = extract_gv_published_tokens(load_vendored_gv_html())
    gr = extract_gr_published_tokens(load_vendored_gr_html())
    genealogy = genealogy_census(
        _line_groups(gv, tuple(GV_LINE_NAMES)),
        _line_groups(gr, tuple(GR_LINE_NAMES)),
        _line_groups(ia, tuple(IA_LINE_NAMES)),
    )
    fischer = fischer_census(_line_groups(ia, tuple(IA_LINE_NAMES)))
    gv6_groups = [group for name, group in _line_groups(gv, ("Gv6",))][0]
    return {
        "gv6_phrase_count": len(genealogy.gv6_phrases),
        "gv6_handoffs": genealogy.gv6_links,
        "gv6_groups": [list(phrase.groups) for phrase in genealogy.gv6_phrases],
        "gv6_stem_count": sum(len(group_stems(group)) for group in gv6_groups),
        "staff_pure_999": fischer.pure_breaks,
        "staff_076_after_999": fischer.immediate_076_group,
        "staff_076_suffix": fischer.immediate_076_suffix,
        "staff_076_bare": fischer.immediate_bare_076,
        "staff_076_after_999_rate": fischer.immediate_076_group / fischer.pure_breaks,
    }


def build_report(provider: MockProvider | None = None) -> dict[str, Any]:
    """Headline counts with no drawing-based code change applied."""
    if not isinstance(provider, MockProvider):
        raise TypeError("MockProvider is required")
    calendar = calendar_stats()
    staff = genealogy_and_staff()
    birds = bird_substitution_counts()
    stats = {
        "calendar_040": calendar["040"],
        "calendar_040_before_152": calendar["040_before_after_152"][0],
        "calendar_040_after_152": calendar["040_before_after_152"][1],
        "calendar_040_gaps": calendar["040_gaps"],
        "calendar_full_delimiters": calendar["full_delimiters_opening_390"],
        "calendar_152": calendar["152"],
        "calendar_143": calendar["143"],
        "gv6_phrases": staff["gv6_phrase_count"],
        "gv6_handoffs": staff["gv6_handoffs"],
        "staff_076_after_999": staff["staff_076_after_999"],
        "staff_pure_999": staff["staff_pure_999"],
        "staff_076_after_999_rate": staff["staff_076_after_999_rate"],
        "parallel_span": birds["stretch_span"],
        "parallel_matches": birds["stretch_matches"],
        "parallel_mismatches": birds["stretch_mismatches"],
        "parallel_bird_substitutions": birds["stretch_bird_pairs"],
        "corpus_bird_substitutions": birds["corpus_bird_cross_hundred"],
    }
    adopted = [row for row in DISAGREEMENTS if row["adopted"]]
    report = {
        "track": "round5b",
        "provider": "MockProvider",
        "provider_calls": len(provider.get_call_history()),
        "readings_assigned": False,
        "adopted_corrections": adopted,
        "licence": {
            "holder": "C.E.I.P.P.",
            "url": CEIPP_LICENCE_URL,
            "statement": CEIPP_LICENCE,
            "source": CEIPP_SOURCE,
            "stored_in_git": (
                "Hashes, URLs, and this note. The raster strips and the vector "
                "pages were fetched for the check and were not committed. The "
                "repository licence is not the CEIPP licence."
            ),
        },
        "raster_strips": [dict(row) for row in RASTER_STRIPS],
        "vector_pages": [dict(row) for row in VECTOR_PAGES],
        "geometry": GEOMETRY,
        "disagreements": [dict(row) for row in DISAGREEMENTS],
        "stats_before": stats,
        "stats_after": stats,
        "what_changed": (
            "Nothing in the headline counts. No Barthel code was replaced. "
            "Crescent totals, delimiter gaps, Gv6 handoffs, the Staff "
            "076-after-999 count, the H/Q span, and the bird-substitution "
            "counts stay at the vendored Barthel figures."
        ),
        "calendar_detail": calendar,
        "genealogy_detail": {
            "gv6_groups": staff["gv6_groups"],
            "gv6_stem_count": staff["gv6_stem_count"],
            "staff_076_suffix": staff["staff_076_suffix"],
            "staff_076_bare": staff["staff_076_bare"],
        },
        "parallel_detail": birds,
    }
    # Tuples in the geometry notes become lists on disk. Return that form
    # so the saved file and a fresh report compare equal.
    return json.loads(json.dumps(report))


def write_report(path: Path = OUTPUT_PATH, provider: MockProvider | None = None) -> dict[str, Any]:
    report = build_report(provider if provider is not None else MockProvider())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report
