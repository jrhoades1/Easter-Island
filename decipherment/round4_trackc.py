"""Round 4 Track C: rock art and carved objects as external context.

Every sign number in this module is copied from a published source or
left null. A resemblance is not a reading. ``MockProvider`` is accepted
and never called. Corpus counts are recomputed from the vendored
Kohaumotu Barthel pages. Where a test cannot be run, the result is null.
"""

from __future__ import annotations

import json
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from agents.base.providers import MockProvider
from decipherment.barthel_corpus import load_located_sides
from decipherment.inventories import encode_token

REPO_ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = REPO_ROOT / "data" / "decipherment" / "round4c_petroglyphs.json"
DOC_PATH = REPO_ROOT / "docs" / "decipherment" / "round4_trackC_petroglyphs.md"

# Confirmatory tests are limited to signs with at least this many stems.
# Rarer signs are described and their confirmatory p-value stays null.
MIN_COUNT = 20
TRIALS = 2000
SEED = 4
ALPHA = 0.05

# Shape matches whose Barthel numbers are printed by the source.
# ``reading`` is always null. ``context_implies`` is the site's published
# function, not a gloss of the sign.
ADOPTED_MATCHES: tuple[dict[str, Any], ...] = (
    {
        "match_id": "mata_ngarau_fish_tail_bulb",
        "medium": "petroglyph",
        "motif": "fish with a bulb at the base of the tail",
        "location": (
            "Inside a house at Mata Ngarau, 'Orongo. The same tail bulb is "
            "rare in rock art; Lee records it on a marine creature north of "
            "'Anakena, a sea creature at 'Anakena, needlefish and tuna at "
            "Hau Koka, and a tuna at Papa Tataku Poki."
        ),
        "site_function": (
            "Mata Ngarau is the ceremonial court of the birdman competition. "
            "Its houses were used by the rongorongo men. The carving itself "
            "is a fish."
        ),
        "context_implies": (
            "The sign is being compared to a fish. Horley and Lee do not say "
            "it means a fishing chant. Lee later leaves the purpose of sea "
            "petroglyphs open."
        ),
        "barthel_signs": ["700b", "721", "733"],
        "surface_note": (
            "The source writes 700b, 721, and 733. 700b is one allograph, "
            "not every sign whose stem is 700. The test uses 700b itself. "
            "The plain stem 700 is counted beside it and is not treated as "
            "the tail-bulb sign."
        ),
        "published_count": None,
        "citation": (
            "Horley and Lee 2008, Rapa Nui Journal 22(2): 114, fig. 6a, "
            "citing Lee 1992: 93, 94, 164, 165, 185. Fish and turtle counts "
            "in the rock art, without a Barthel number, are Lee 2004, Rapa "
            "Nui Journal 18(1): 36, drawing on Lee 1992."
        ),
    },
    {
        "match_id": "orongo_house_44_gourd",
        "medium": "petroglyph",
        "motif": "hook-shaped or gourd-shaped figure with a komari cut on it",
        "location": "'Orongo house 44, Mata Ngarau.",
        "site_function": (
            "House interior at the birdman precinct, occupied by rongorongo "
            "men. Routledge called the figure hook-shaped. Horley and Lee "
            "call it a gourd. Komari were cut during later fertility "
            "ceremonies and often overlie birdmen."
        ),
        "context_implies": (
            "The matched outline is the hook or gourd, not the vulva cut on "
            "it. A fertility reading of sign 074 is a hypothesis, not what "
            "the paper states."
        ),
        "barthel_signs": ["074"],
        "surface_note": None,
        "published_count": {
            "074": {
                "count": 94,
                "corpus": 14552,
                "citation": "Barthel 1958: 109, as cited by Horley and Lee 2008: 114.",
            }
        },
        "citation": (
            "Horley and Lee 2008: 114, fig. 6b. Routledge 1920: 447 "
            "('a figure shaped like a hook'). Komari and the fertility "
            "ceremonies: Routledge 1919: 263, cited by Horley and Lee 2008: 111."
        ),
    },
    {
        "match_id": "orongo_house_40_long_beak",
        "medium": "petroglyph",
        "motif": "long-beaked bird",
        "location": (
            "'Orongo house 40 (Koll's group), and loci 31 and 17 at Mata "
            "Ngarau."
        ),
        "site_function": (
            "Birdman precinct. The long-beaked bird is one motif among "
            "birdmen, not a label for the whole cult."
        ),
        "context_implies": (
            "The sign is being compared to a long-beaked bird. Equating it "
            "with the word manu, with the sooty tern, or with Makemake is "
            "a hypothesis."
        ),
        "barthel_signs": ["660"],
        "surface_note": (
            "Horley and Lee say the beak is usually closed, and that "
            "open-beak forms occur on lines Br2, Br7, Pr2, and Ua3."
        ),
        "published_count": {
            "660": {
                "count": 29,
                "corpus": None,
                "citation": "Barthel 1958: 144, as cited by Horley and Lee 2008: 114.",
            }
        },
        "citation": (
            "Horley and Lee 2008: 114, fig. 6d, citing Koll 1991: fig. 1 and "
            "Lee 1992: figs. 4.48 and 4.97."
        ),
    },
    {
        "match_id": "mata_ngarau_two_headed_bird",
        "medium": "petroglyph",
        "motif": "two-headed long-beaked bird",
        "location": "Mata Ngarau loci 6 and 31.",
        "site_function": "Same birdman precinct as the single long-beaked bird.",
        "context_implies": (
            "The sign is being compared to a two-headed long-beaked bird. "
            "No name is attached."
        ),
        "barthel_signs": ["680"],
        "surface_note": None,
        "published_count": {
            "680": {
                "count": 23,
                "corpus": None,
                "citation": "Barthel 1958: 145, as cited by Horley and Lee 2008: 114.",
            }
        },
        "citation": "Horley and Lee 2008: 114, citing Lee 1992: figs. 4.45 and 4.48.",
    },
    {
        "match_id": "locus_17_reimiro",
        "medium": "petroglyph",
        "motif": "rei miro",
        "location": "Mata Ngarau locus 17.",
        "site_function": (
            "The rei miro is a breast ornament. The petroglyph is the "
            "ornament's crescent, carved at the birdman court. It is not "
            "the text cut on the wooden rei miro in museum collections."
        ),
        "context_implies": (
            "The sign has the outline of a rei miro. That does not say which "
            "word, if any, the sign spells."
        ),
        "barthel_signs": ["007"],
        "surface_note": None,
        "published_count": None,
        "citation": "Horley and Lee 2008: 114, on locus 17 (Lee 1992: fig. 4.97).",
    },
    {
        "match_id": "locus_17_sitting_man",
        "medium": "petroglyph",
        "motif": "sitting man",
        "location": "Mata Ngarau locus 17.",
        "site_function": "A human figure at the birdman court, grouped with the rei miro, an eye mask, and a bird.",
        "context_implies": "A seated person. No personal name and no title is given by the source.",
        "barthel_signs": ["240"],
        "surface_note": None,
        "published_count": None,
        "citation": "Horley and Lee 2008: 114. They put the words sitting man in quotation marks.",
    },
    {
        "match_id": "locus_17_eye_mask",
        "medium": "petroglyph",
        "motif": "eye mask",
        "location": "Mata Ngarau locus 17.",
        "site_function": (
            "Eye masks and Makemake faces are both carved at 'Orongo. "
            "Horley and Lee identify this petroglyph as an eye mask, not "
            "as a portrait of the god."
        ),
        "context_implies": (
            "An eye mask. Calling sign 513 'Makemake' is a hypothesis. "
            "Lee's Makemake faces are a larger class and are not given "
            "this number."
        ),
        "barthel_signs": ["513"],
        "surface_note": None,
        "published_count": None,
        "citation": "Horley and Lee 2008: 114.",
    },
    {
        "match_id": "locus_17_bird_with_star",
        "medium": "petroglyph",
        "motif": "bird with a star around its head",
        "location": "Mata Ngarau locus 17.",
        "site_function": "Bird image at the birdman court, on the same boulder as the rei miro, sitting man, and eye mask.",
        "context_implies": "A bird with a star-like form at the head. No star name and no bird species is assigned.",
        "barthel_signs": ["550"],
        "surface_note": None,
        "published_count": None,
        "citation": "Horley and Lee 2008: 114.",
    },
)

# Motifs the sources describe, without a Barthel number this round will use.
UNNUMBERED: tuple[dict[str, Any], ...] = (
    {
        "match_id": "orongo_birdman",
        "medium": "petroglyph",
        "motif": "tangata manu, the birdman",
        "location": (
            "Mata Ngarau and the 'Orongo houses. Horley and Lee, citing "
            "Lee 1990: 69, give 375 birdmen at the precinct. A large "
            "bas-relief birdman on locus 45 is partly hidden by a house wall."
        ),
        "site_function": (
            "The birdman competition decided a ritual office. The village "
            "was occupied seasonally. Rongorongo men chanted at Mata Ngarau."
        ),
        "context_implies": (
            "The cult is well documented. No source used here prints one "
            "Barthel number for the full birdman body. McLaughlin 2004's "
            "two-column page pairs the words tangata manu with glyph 638, "
            "but the columns collide in the text and that number is not adopted."
        ),
        "barthel_signs": None,
        "citation": (
            "Lee 1992: 36, 67, 70; Horley and Lee 2008: 110–112, citing "
            "Routledge 1919: 260 and 1920: 426, 446, and Métraux 1940: 331–332, 335. "
            "Dorsal birdmen on Hoa Hakananai'a: Horley and Lee 2008: 112, fig. 4, "
            "citing Routledge 1919: 261 and Métraux 1940: 298."
        ),
    },
    {
        "match_id": "komari",
        "medium": "petroglyph",
        "motif": "komari, the vulva form",
        "location": (
            "Across the island, and in quantity at Mata Ngarau: 195 on the "
            "precinct (Lee 1990: 69, via Horley and Lee) and 130 of 173 "
            "motifs inside 'Orongo houses (Koll 1991)."
        ),
        "site_function": "Routledge ties the komari to later fertility ceremonies. They are cut over earlier birdmen.",
        "context_implies": (
            "Fertility is the published function of the rock-art motif. "
            "It is not a reading of a Barthel sign. House 43 has an "
            "anthropomorph whose head is replaced by a komari; Horley and "
            "Lee say it may resemble a sign on Tahua and do not give a number. "
            "McLaughlin's glyph 51 is not adopted, for the same layout reason as glyph 638."
        ),
        "barthel_signs": None,
        "citation": (
            "Routledge 1919: 263; Horley and Lee 2008: 111, 114, fig. 6c; "
            "Koll 1991: 61–62; Lee 1992."
        ),
    },
    {
        "match_id": "makemake_faces",
        "medium": "petroglyph",
        "motif": "Makemake faces",
        "location": "Mata Ngarau, where Lee counted 140 faces, and elsewhere including panels that also carry komari and turtles.",
        "site_function": "Makemake is the creator god tied to the birdman cult. The faces are a rock-art class, often large-eyed.",
        "context_implies": (
            "The god's name belongs to the faces in the ethnographic "
            "literature. It is not transferred to sign 513, which Horley "
            "and Lee call an eye mask."
        ),
        "barthel_signs": None,
        "citation": (
            "Lee 1990: 69 as cited by Horley and Lee 2008: 112; Lee 2004, "
            "Rapa Nui Journal 18(1), on Makemake faces beside sea creatures; "
            "Métraux 1940 for the cult setting as used by Horley and Lee."
        ),
    },
    {
        "match_id": "turtle_petroglyphs",
        "medium": "petroglyph",
        "motif": "turtle",
        "location": (
            "Tongariki, the coast from Omohe to La Perouse, one example at "
            "'Orongo, and at least three on the canoe panel near Ahu Ra'ai. "
            "Lee's 1992 count is 34 turtle images."
        ),
        "site_function": (
            "Lee reviews Polynesian turtle ritual and an island legend in "
            "which a turtle is Makemake in disguise. She does not assign "
            "the petroglyphs to a rongorongo sign. Horley 2005, fig. 1, "
            "draws a turtle-shaped glyph and does not print its number in "
            "the caption text used here."
        ),
        "context_implies": "No sign is tested. A turtle reading of any glyph would be a hypothesis.",
        "barthel_signs": None,
        "citation": (
            "Lee 2004, Rapa Nui Journal 18(1): 36, citing Lee 1992: figs. "
            "4.65–4.70 and fig. 4.107. Horley 2005, Rapa Nui Journal 19(2): "
            "107–116, fig. 1."
        ),
    },
    {
        "match_id": "canoe_petroglyphs",
        "medium": "petroglyph",
        "motif": "canoe",
        "location": "The great canoe panel near Ahu Ra'ai, with fishhooks and turtles, and a panel at Pua Tivaka that also has canoe shapes.",
        "site_function": "Lee documents the canoes as rock art. No Barthel number is printed with them in the sources read for this round.",
        "context_implies": "No sign is tested. A canoe reading would be a hypothesis.",
        "barthel_signs": None,
        "citation": "Lee 2004, citing Lee 1992: fig. 4.72 and fig. 4.107.",
    },
    {
        "match_id": "hoa_hakananai_a_back",
        "medium": "carved_stone",
        "motif": "birdmen, sooty tern, dance paddles, and komari on the back of Hoa Hakananai'a",
        "location": "The moai removed from 'Orongo in 1868, now in the British Museum. The carvings were painted red on white.",
        "site_function": "An 'Orongo statue whose back carries the same motifs as the village: manu piri birdmen, manutara, ao or rapa, and komari.",
        "context_implies": "The motifs are identified. They are not given Barthel numbers on this statue. McLaughlin leaves the rapa paddle unnumbered.",
        "barthel_signs": None,
        "citation": (
            "Horley and Lee 2008: 112–113, figs. 4 and 5, citing Routledge "
            "1919: 257, 261, Métraux 1940: 298, and Orliac and Orliac 2008. "
            "McLaughlin 2004: 90–93 lists a rapa among petroglyph matches and "
            "gives it no glyph number."
        ),
    },
    {
        "match_id": "peabody_birdman_stones",
        "medium": "carved_stone",
        "motif": "birdman stones removed from 'Orongo",
        "location": "Peabody Museum of Archaeology and Ethnology, Cambridge, Massachusetts. The stones came from the 'Orongo birdman site.",
        "site_function": "Portable or removed stones carrying birdman carvings. This round did not verify a Barthel number from the article text.",
        "context_implies": "No sign is tested from this paper.",
        "barthel_signs": None,
        "citation": (
            "Horley and Lee 2012, Rapa Nui Journal 26(1): 5–20, "
            "'Easter Island's birdman stones in the collection of the "
            "Peabody Museum of Archaeology and Ethnology, Cambridge, Massachusetts.'"
        ),
    },
    {
        "match_id": "tahonga",
        "medium": "carved_object",
        "motif": "tahonga pendant",
        "location": "Museum examples of the spherical wooden pendant. About two dozen survive. No inscription with a published Barthel number was verified here.",
        "site_function": (
            "A neck pendant. Orliac and Orliac argue the shape follows a "
            "seabird egg, in the birdman and creation setting, rather than "
            "a coconut. Some designs used on figurine heads also appear on "
            "tahonga."
        ),
        "context_implies": "The egg interpretation belongs to the pendant. It is not a reading of a sign. No sign is tested.",
        "barthel_signs": None,
        "citation": (
            "Orliac and Orliac 2008, as summarized from their Treasures of "
            "Easter Island in the Museum of Cultural History, Oslo, note on "
            "the Arup tahonga; Forment 1993: 212, cited by Wieczorek and "
            "Horley 2023, Archaeometry, for designs shared onto tahonga; "
            "Orliac 2010 on makoi wood as the preferred material for tahonga and rei miro."
        ),
    },
    {
        "match_id": "moai_kavakava_handlike",
        "medium": "carved_object",
        "motif": "hand-like forms on the neck of a moai kavakava, under a hairdo of lozenges",
        "location": "Moai kavakava E 18646, Peabody Essex Museum, Salem. Collected in the mid nineteenth century.",
        "site_function": (
            "Moai kavakava are emaciated male figures treated as akuaku. "
            "Cranial carvings sit where the hair would be. Orliac and Orliac "
            "warn that those carvings are not literal portraits. Red pigment "
            "in the nostrils is described as the breath of life."
        ),
        "context_implies": (
            "Wieczorek and Horley say the hand-like forms are similar to "
            "signs 052, 52x, or 162. Similarity to three signs is not an "
            "identification, so none of the three is adopted as the carving's "
            "sign. No confirmatory test is attached."
        ),
        "barthel_signs": None,
        "candidate_signs_not_adopted": ["052", "162"],
        "citation": (
            "Wieczorek and Horley 2023, Archaeometry (cranial unwrapping), "
            "on E 18646, citing Barthel 1958, Formentafel 1–2, and Horley, "
            "Davletshin and Wieczorek 2018: 380, fig. 16. Akuaku and the "
            "non-literal reading of cranial glyphs: Orliac and Orliac 2008: "
            "106, quoted by Wieczorek and Horley. Red nostrils: Orliac and "
            "Orliac 2008: 113, cited by Horley and Lee 2008: 115. Métraux "
            "1940: 252–253 is the ethnographic discussion they point to."
        ),
    },
    {
        "match_id": "moai_kavakava_e5306",
        "medium": "carved_object",
        "motif": "bird heads, star or starfish shapes, and a rotated crescent on a figurine's cranium",
        "location": "Moai kavakava E 5306, Peabody Essex Museum. A second example is Kunstkamera 3707-1.",
        "site_function": "Same figurine type. Horley 2005 had already noted a possible relation to the script.",
        "context_implies": "No Barthel number is printed for this composition. Nothing is tested.",
        "barthel_signs": None,
        "citation": (
            "Wieczorek and Horley 2023, on E 5306, citing Horley 2005: 114, "
            "fig. 20d, and Butinov and Rozina 1962 for the St Petersburg figure."
        ),
    },
    {
        "match_id": "reimiro_pectorals",
        "medium": "carved_object",
        "motif": "inscribed rei miro pectorals",
        "location": (
            "Item J, rei miro 1, British Museum, and item L, rei miro 2, "
            "also London. J is a short text. L is a longer one. Both are "
            "already inside the Barthel corpus, so their signs are the "
            "script, not an outside picture of it."
        ),
        "site_function": "Breast ornaments. The crescent shape, as a petroglyph, is the separate match to sign 007.",
        "context_implies": (
            "The object class does not tell us the meaning of the signs cut "
            "on J or L. Those signs are listed from the vendored pages and "
            "are not given implications."
        ),
        "barthel_signs": None,
        "citation": (
            "Horley, Davletshin and Wieczorek 2018, corpus table: J is RR20, "
            "two glyphs; L is RR21. Vendored Kohaumotu pages Ja.html and "
            "La.html. Fischer 1997 is the catalog that paper updates. The "
            "shape parallel is Horley and Lee 2008, sign 007, not these inscriptions."
        ),
    },
    {
        "match_id": "new_york_birdman_figure",
        "medium": "carved_object",
        "motif": "tangata manu wood figure with short incised texts",
        "location": "Item X, American Museum of Natural History, New York. Not in the vendored Kohaumotu pages used here.",
        "site_function": "A sculpture of a man with a bird's head. The 2018 corpus table gives it about 37 glyphs in several short texts.",
        "context_implies": (
            "Signs were cut on a birdman figure. Which signs, and whether "
            "the text is about the birdman, is not tested. The transcription "
            "is not vendored, so the sign list is null."
        ),
        "barthel_signs": None,
        "citation": (
            "Horley, Davletshin and Wieczorek 2018, corpus table, item X / "
            "RR25, citing Fischer 1997. Kohaumotu corpus list: item X is a "
            "tangata manu."
        ),
    },
)

# Pairs named in advance, before the counts were examined.
# Each pair shares one published motif class.
PRESET_PAIRS: tuple[tuple[str, str, str], ...] = (
    ("660", "680", "two long-beaked bird forms"),
    ("700b", "721", "tail-bulb marine signs"),
    ("700b", "733", "tail-bulb marine signs"),
    ("721", "733", "tail-bulb marine signs"),
)

THEME_POOLS: tuple[dict[str, Any], ...] = (
    {
        "theme_id": "long_beaked_birds",
        "signs": ["660", "680"],
        "label": "long-beaked birds at the birdman court",
    },
    {
        "theme_id": "tail_bulb_marine",
        "signs": ["700b", "721", "733"],
        "label": "the tail-bulb forms named by Horley and Lee",
    },
    {
        "theme_id": "locus_17_panel",
        "signs": ["007", "240", "513", "550"],
        "label": "the four signs Horley and Lee name on locus 17",
    },
)

OPEN_BEAK_LINES: tuple[tuple[str, int], ...] = (
    ("Br", 2),
    ("Br", 7),
    ("Pr", 2),
    ("Ua", 3),
)

CONTROL_SIGN_COUNT = 8


def _require_mock(provider: MockProvider) -> None:
    if not isinstance(provider, MockProvider):
        raise TypeError("MockProvider only")


def _index_corpus() -> dict[str, Any]:
    stems: list[str] = []
    tablets: list[str] = []
    line_keys: list[tuple[str, int]] = []
    surfaces: list[str] = []
    lines: dict[tuple[str, int], list[str]] = {}
    for side in load_located_sides():
        tablet = side.side[0]
        for line_no, tokens in side.lines:
            key = (side.side, line_no)
            line_stems: list[str] = []
            for token in tokens:
                token_stems = encode_token(token, "stem")
                token_surfaces = encode_token(token, "surface")
                if len(token_stems) != len(token_surfaces):
                    raise RuntimeError(f"stem/surface split differs for {token!r}")
                for stem, surface in zip(token_stems, token_surfaces):
                    stems.append(stem)
                    surfaces.append(surface)
                    tablets.append(tablet)
                    line_keys.append(key)
                    line_stems.append(stem)
            lines[key] = line_stems
    return {
        "stems": stems,
        "tablets": tablets,
        "line_keys": line_keys,
        "surfaces": surfaces,
        "lines": lines,
    }


def _chi2(chosen: list[int], tablet_ids: list[int], sizes: list[int], total: int) -> float:
    counts = [0] * len(sizes)
    for index in chosen:
        counts[tablet_ids[index]] += 1
    k = len(chosen)
    score = 0.0
    for count, size in zip(counts, sizes):
        expected = k * size / total
        score += (count - expected) ** 2 / expected
    return score


def _permutation_p(
    observed: float,
    positions: list[int],
    tablet_ids: list[int],
    sizes: list[int],
    total: int,
    rng: random.Random,
) -> dict[str, Any]:
    k = len(positions)
    if k == 0:
        return {
            "observed": None,
            "trials": TRIALS,
            "ge": None,
            "p_greater": None,
        }
    ge = 0
    span = range(total)
    for _ in range(TRIALS):
        draw = rng.sample(span, k)
        if _chi2(draw, tablet_ids, sizes, total) >= observed:
            ge += 1
    return {
        "observed": observed,
        "trials": TRIALS,
        "ge": ge,
        "p_greater": (ge + 1) / (TRIALS + 1),
    }


def _line_overlap_p(
    lines_a: set[tuple[str, int]],
    lines_b: set[tuple[str, int]],
    universe: list[tuple[str, int]],
    rng: random.Random,
) -> dict[str, Any]:
    observed = len(lines_a & lines_b)
    if not lines_a or not lines_b:
        return {"observed_lines": observed, "p_greater": None, "trials": TRIALS, "ge": None}
    target = len(lines_b)
    ge = 0
    for _ in range(TRIALS):
        draw = set(rng.sample(universe, target))
        if len(lines_a & draw) >= observed:
            ge += 1
    return {
        "observed_lines": observed,
        "lines_with_first": len(lines_a),
        "lines_with_second": len(lines_b),
        "trials": TRIALS,
        "ge": ge,
        "p_greater": (ge + 1) / (TRIALS + 1),
    }


def _normalize_surface(surface: str) -> str:
    if surface.startswith("V") and len(surface) > 1 and surface[1].isdigit():
        return surface[1:]
    return surface


def _is_hit(spec: str, stem: str, surface: str) -> bool:
    """A bare number matches a stem. A suffixed number matches that allograph."""
    if spec.isdigit():
        return stem == spec.zfill(3)
    return _normalize_surface(surface) == spec


def _positions(spec: str, stems: list[str], surfaces: list[str]) -> list[int]:
    return [
        index
        for index, (stem, surface) in enumerate(zip(stems, surfaces))
        if _is_hit(spec, stem, surface)
    ]


def _adjacent_count(
    stems: list[str],
    surfaces: list[str],
    line_keys: list[tuple[str, int]],
    first: str,
    second: str,
) -> int:
    hits = 0
    for index in range(len(stems) - 1):
        if line_keys[index] != line_keys[index + 1]:
            continue
        left = _is_hit(first, stems[index], surfaces[index]) and _is_hit(
            second, stems[index + 1], surfaces[index + 1]
        )
        right = _is_hit(second, stems[index], surfaces[index]) and _is_hit(
            first, stems[index + 1], surfaces[index + 1]
        )
        if left or right:
            hits += 1
    return hits


def _neighbors(
    stems: list[str],
    line_keys: list[tuple[str, int]],
    positions: list[int],
) -> dict[str, Any]:
    left: Counter[str] = Counter()
    right: Counter[str] = Counter()
    for index in positions:
        if index > 0 and line_keys[index] == line_keys[index - 1]:
            left[stems[index - 1]] += 1
        if index + 1 < len(stems) and line_keys[index] == line_keys[index + 1]:
            right[stems[index + 1]] += 1
    return {
        "left": [{"sign": sign, "count": count} for sign, count in left.most_common(5)],
        "right": [{"sign": sign, "count": count} for sign, count in right.most_common(5)],
        "note": (
            "Neighbor lists are descriptive. The most common neighbor was "
            "not tested, because picking the maximum after looking would "
            "inflate a p-value."
        ),
    }


def _tablet_counts(positions: list[int], tablets: list[str]) -> list[dict[str, Any]]:
    counts = Counter(tablets[index] for index in positions)
    return [{"tablet": tablet, "count": count} for tablet, count in counts.most_common()]


def _surface_breakdown(surfaces: list[str], stem: str) -> list[dict[str, Any]]:
    counts: Counter[str] = Counter()
    for surface in surfaces:
        body = surface[1:] if surface.startswith("V") and len(surface) > 1 and surface[1].isdigit() else surface
        digits = "".join(character for character in body if character.isdigit())
        if digits.zfill(3) == stem:
            counts[surface] += 1
    return [{"surface": surface, "count": count} for surface, count in sorted(counts.items())]


def _sign_record(
    stem: str,
    corpus: dict[str, Any],
    tablet_ids: list[int],
    sizes: list[int],
    rng: random.Random,
    *,
    confirmatory: bool,
) -> dict[str, Any]:
    stems: list[str] = corpus["stems"]
    surfaces: list[str] = corpus["surfaces"]
    total = len(stems)
    positions = _positions(stem, stems, surfaces)
    k = len(positions)
    record: dict[str, Any] = {
        "stem": stem,
        "stem_count": k,
        "corpus_tokens": total,
        "rate": (k / total) if total else None,
        "tablets": _tablet_counts(positions, corpus["tablets"]) if k else [],
        "surfaces": (
            _surface_breakdown(corpus["surfaces"], stem)
            if stem.isdigit()
            else [{"surface": stem, "count": k}]
        ),
        "neighbors": _neighbors(stems, corpus["line_keys"], positions) if k else None,
        "reading": None,
    }
    if k == 0 or not confirmatory or k < MIN_COUNT:
        record["concentration"] = None
        record["confirmatory"] = False
        record["reason"] = "absent" if k == 0 else "below the pre-set count of 20" if confirmatory else "not in the confirmatory set"
        return record
    observed = _chi2(positions, tablet_ids, sizes, total)
    record["concentration"] = _permutation_p(observed, positions, tablet_ids, sizes, total, rng)
    record["confirmatory"] = True
    record["reason"] = None
    return record


def _status(record: dict[str, Any], threshold: float, control_median: float | None) -> str:
    if record["stem_count"] == 0:
        return "absent"
    if not record["confirmatory"]:
        return "not_tested"
    p_value = record["concentration"]["p_greater"]
    if p_value is None:
        return "not_tested"
    if p_value > ALPHA:
        return "ordinary"
    if p_value > threshold:
        return "nominal_only"
    if control_median is None or not p_value < control_median:
        return "nominal_only"
    return "more_concentrated_than_chance"


def run_round4_trackc(provider: MockProvider) -> dict[str, Any]:
    """Cited parallels, then a permutation test. No reading is assigned."""
    _require_mock(provider)
    corpus = _index_corpus()
    stems: list[str] = corpus["stems"]
    total = len(stems)
    tablet_names = sorted(set(corpus["tablets"]))
    name_to_id = {name: index for index, name in enumerate(tablet_names)}
    tablet_ids = [name_to_id[name] for name in corpus["tablets"]]
    sizes = [0] * len(tablet_names)
    for tablet_id in tablet_ids:
        sizes[tablet_id] += 1

    adopted_signs: list[str] = []
    for match in ADOPTED_MATCHES:
        for sign in match["barthel_signs"]:
            if sign not in adopted_signs:
                adopted_signs.append(sign)

    rng = random.Random(SEED)
    sign_rows = {
        sign: _sign_record(sign, corpus, tablet_ids, sizes, rng, confirmatory=True)
        for sign in adopted_signs
    }
    family = [sign for sign in adopted_signs if sign_rows[sign]["confirmatory"]]
    threshold = (ALPHA / len(family)) if family else None

    frequencies = Counter(stems)
    controls = [
        sign
        for sign, _count in frequencies.most_common()
        if sign not in adopted_signs
    ][:CONTROL_SIGN_COUNT]
    control_rows = {
        sign: _sign_record(sign, corpus, tablet_ids, sizes, rng, confirmatory=True)
        for sign in controls
    }
    control_ps = [
        row["concentration"]["p_greater"]
        for row in control_rows.values()
        if row["concentration"] is not None
    ]
    control_median = sorted(control_ps)[len(control_ps) // 2] if control_ps else None

    for sign, row in sign_rows.items():
        row["distribution_status"] = _status(row, threshold if threshold is not None else 1.0, control_median)
        row["lexical_reading"] = None

    line_members: dict[str, set[tuple[str, int]]] = defaultdict(set)
    for spec in set(adopted_signs):
        for index in _positions(spec, stems, corpus["surfaces"]):
            line_members[spec].add(corpus["line_keys"][index])
    universe = list(corpus["lines"].keys())

    pairs = []
    for first, second, label in PRESET_PAIRS:
        overlap = _line_overlap_p(line_members[first], line_members[second], universe, rng)
        overlap["adjacent_either_order"] = _adjacent_count(
            stems, corpus["surfaces"], corpus["line_keys"], first, second
        )
        overlap["pair"] = [first, second]
        overlap["label"] = label
        overlap["reading"] = None
        pairs.append(overlap)

    themes = []
    for theme in THEME_POOLS:
        positions = [
            index
            for index in range(total)
            if any(_is_hit(spec, stems[index], corpus["surfaces"][index]) for spec in theme["signs"])
        ]
        k = len(positions)
        block: dict[str, Any] = {
            "theme_id": theme["theme_id"],
            "label": theme["label"],
            "signs": list(theme["signs"]),
            "stem_count": k,
            "reading": None,
        }
        if k < MIN_COUNT:
            block["concentration"] = None
            block["distribution_status"] = "not_tested"
        else:
            observed = _chi2(positions, tablet_ids, sizes, total)
            block["concentration"] = _permutation_p(observed, positions, tablet_ids, sizes, total, rng)
            p_value = block["concentration"]["p_greater"]
            if p_value > ALPHA:
                block["distribution_status"] = "ordinary"
            elif control_median is None or not p_value < control_median:
                block["distribution_status"] = "nominal_only"
            else:
                block["distribution_status"] = "more_concentrated_than_chance"
        themes.append(block)

    audits = []
    for side, line_no in OPEN_BEAK_LINES:
        line = corpus["lines"].get((side, line_no))
        beak_series = [] if line is None else sorted({sign for sign in line if sign.startswith("6")})
        audits.append(
            {
                "line": f"{side}{line_no}",
                "present_in_vendored_text": None if line is None else ("660" in line),
                "line_found": line is not None,
                "beak_series_stems": beak_series,
                "note": (
                    "Other signs in Barthel's 600s are listed so the line can "
                    "be checked. They are not renamed as open-beak 660."
                ),
            }
        )
    plain_700 = _sign_record("700", corpus, tablet_ids, sizes, rng, confirmatory=False)
    plain_700["distribution_status"] = "not_the_cited_allograph"
    plain_700["lexical_reading"] = None
    plain_700["note"] = (
        "Stem 700 pools every allograph. Horley and Lee named 700b. "
        "A surface such as 700bx is not counted as 700b. "
        "This count is context, not the test."
    )

    inscribed = {}
    for tablet, label in (("J", "rei_miro_1"), ("L", "rei_miro_2")):
        positions = [index for index, name in enumerate(corpus["tablets"]) if name == tablet]
        inscribed[label] = {
            "tablet": tablet,
            "stems": [stems[index] for index in positions],
            "stem_count": len(positions),
            "implication": None,
            "reading": None,
        }

    supported = [
        sign
        for sign, row in sign_rows.items()
        if row["distribution_status"] == "more_concentrated_than_chance"
    ]
    return {
        "round": 4,
        "track": "C",
        "provider": provider.name,
        "provider_calls": len(provider.get_call_history()),
        "reading": None,
        "corpus_tokens": total,
        "tablet_count": len(tablet_names),
        "tablets": [
            {"tablet": name, "tokens": sizes[name_to_id[name]]}
            for name in tablet_names
        ],
        "method": {
            "inventory": "Barthel stem, vendored Kohaumotu pages",
            "null": (
                "For a sign with k hits, k positions are drawn at random "
                "among the stems. The statistic is the chi-square of tablet "
                "counts against tablet length. The p-value is (hits + 1) / "
                "(trials + 1), one sided, greater than the observed statistic."
            ),
            "trials": TRIALS,
            "seed": SEED,
            "minimum_count": MIN_COUNT,
            "alpha": ALPHA,
            "bonferroni_signs": family,
            "bonferroni_threshold": threshold,
            "control_signs": controls,
            "control_median_p": control_median,
            "what_would_count": (
                "A sign is called more concentrated than chance only if it "
                "has at least 20 hits, its p-value clears 0.05 divided by "
                "the number of such signs, and that p-value is also smaller "
                "than the median p-value of the eight most common signs that "
                "are not in the petroglyph set. That status is about where "
                "the sign sits. It is not a meaning."
            ),
        },
        "adopted_matches": [dict(match) for match in ADOPTED_MATCHES],
        "unnumbered": [dict(row) for row in UNNUMBERED],
        "signs": sign_rows,
        "stem_700_not_cited": plain_700,
        "controls": control_rows,
        "preset_pairs": pairs,
        "themes": themes,
        "open_beak_audit": audits,
        "inscribed_reimiro": inscribed,
        "supported_distribution": supported,
        "supported_lexical_readings": [],
    }


def _fmt_p(value: Any) -> str:
    if value is None:
        return "null"
    return f"{value:.4f}"


def render_round4_trackc(result: dict[str, Any]) -> str:
    """Plain-English note. Numbers come from the run."""
    method = result["method"]
    lines = [
        "# Round 4, Track C: rock art and carved objects",
        "",
        "No sign gains a word. The supported claims are shape matches that a published paper already ties to a Barthel number. Where the tablets were tested, the question was only whether those signs pile up in particular texts more than a random placement of the same number of hits. A yes would still not be a translation.",
        "",
        f"Provider: `{result['provider']}`. Provider calls: {result['provider_calls']}. `reading` is null. Adopted lexical readings: none.",
        "",
        "## What was compared",
        "",
        "The outside material is the rock art catalogued by Georgia Lee and the carved objects discussed by Horley and Lee, the Orliacs, Fischer's corpus as updated by Horley, Davletshin and Wieczorek, Routledge, and Métraux. The sign corpus is the vendored Barthel text: "
        f"{result['corpus_tokens']} stems on {result['tablet_count']} tablets.",
        "",
        "Horley and Lee 2008 print Barthel numbers for the comparisons below. A suffixed number is tested as that allograph, not as the whole stem. Komari, Makemake faces, the full birdman body, turtles, canoes, tahonga, the back of Hoa Hakananai'a, the Peabody birdman stones, and the New York birdman figure are in the dataset with a null sign number, because this round did not verify a number for them. McLaughlin 2004's glyph 51 and glyph 638 were not adopted: on the published page the two columns run together, so the pairing is not clean enough to use.",
        "",
        "The wooden rei miro J and L are already rongorongo texts. Their signs are listed and then left without an implication. The crescent *shape* of a rei miro is a different claim, and that claim is sign 007.",
        "",
        "## How the test works",
        "",
        method["null"],
        "",
        f"Trials: {method['trials']}. Seed: {method['seed']}. A sign enters the corrected test only at {method['minimum_count']} hits or more. Signs in that set: {', '.join(method['bonferroni_signs']) or 'none'}. "
        f"The corrected threshold is {_fmt_p(method['bonferroni_threshold'])}. "
        f"Control signs, the eight most common stems outside the set: {', '.join(method['control_signs'])}. "
        f"Their median p-value is {_fmt_p(method['control_median_p'])}.",
        "",
        method["what_would_count"],
        "",
        "## Signs with a published number",
        "",
        "| Sign | Motif in the source | Vendored stems | Published count | Most used tablet | p | Status |",
        "|---|---|---:|---|---|---:|---|",
    ]
    motif_by_sign: dict[str, str] = {}
    published: dict[str, Any] = {}
    for match in result["adopted_matches"]:
        for sign in match["barthel_signs"]:
            motif_by_sign[sign] = match["motif"]
            block = match.get("published_count") or {}
            if sign in block:
                published[sign] = block[sign]
    for sign, row in result["signs"].items():
        top = row["tablets"][0]["tablet"] if row["tablets"] else "—"
        top_n = row["tablets"][0]["count"] if row["tablets"] else 0
        pub = published.get(sign)
        pub_text = "—" if not pub else str(pub["count"])
        p_value = None if row["concentration"] is None else row["concentration"]["p_greater"]
        lines.append(
            f"| {sign} | {motif_by_sign[sign]} | {row['stem_count']} | {pub_text} | {top} ({top_n}) | {_fmt_p(p_value)} | {row['distribution_status']} |"
        )
    lines.extend(
        [
            "",
            "Published counts are Barthel's, quoted by Horley and Lee. They are not replaced by the vendored recount. A difference means the Kohaumotu encoding and Barthel's 1958 total are not the same sample. It is not a new reading.",
            "",
            "Neighbor signs are in the JSON. They were not turned into a p-value.",
            "",
            (
                f"Stem 700, which is wider than the cited allograph 700b, occurs "
                f"{result['stem_700_not_cited']['stem_count']} times. "
                "700b itself occurs "
                + (
                    "once"
                    if result["signs"]["700b"]["stem_count"] == 1
                    else f"{result['signs']['700b']['stem_count']} times"
                )
                + ". "
                "The wider stem is not used as evidence for the tail-bulb petroglyph."
            ),
            "",
            "The eight common control signs, included so a small p-value can be compared with an ordinary sign:",
            "",
            "| Control sign | Stems | p |",
            "|---|---:|---:|",
        ]
    )
    for sign, row in result["controls"].items():
        p_value = None if row["concentration"] is None else row["concentration"]["p_greater"]
        lines.append(f"| {sign} | {row['stem_count']} | {_fmt_p(p_value)} |")
    floor = 1 / (TRIALS + 1)
    at_floor = sum(
        1
        for row in result["controls"].values()
        if row["concentration"] is not None and row["concentration"]["p_greater"] <= floor + 1e-12
    )
    lines.extend(
        [
            "",
            (
                f"{at_floor} of the {len(result['controls'])} common signs sit on the "
                f"floor of this permutation test (p = {floor:.4f}). A petroglyph sign "
                "is counted as more bunched than chance only when it clears the "
                "corrected threshold and is also past that median. "
                + (
                    "None does."
                    if not result["supported_distribution"]
                    else "The signs that do are listed below, and they still have no reading."
                )
            ),
            "",
            "## Do the themed signs cluster together?",
            "",
            "| Theme | Hits | p | Status |",
            "|---|---:|---:|---|",
        ]
    )
    for theme in result["themes"]:
        p_value = None if theme["concentration"] is None else theme["concentration"]["p_greater"]
        lines.append(
            f"| {theme['label']} | {theme['stem_count']} | {_fmt_p(p_value)} | {theme['distribution_status']} |"
        )
    lines.extend(
        [
            "",
            "Pre-set pairs, asked before the counts were read. The p-value is for sharing a line, not for sitting side by side. Adjacent hits are the raw count in either order.",
            "",
            "| Pair | Why it was paired | Lines in common | p | Adjacent hits |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for pair in result["preset_pairs"]:
        lines.append(
            f"| {' '.join(pair['pair'])} | {pair['label']} | {pair['observed_lines']} | {_fmt_p(pair['p_greater'])} | {pair['adjacent_either_order']} |"
        )
    lines.extend(
        [
            "",
            "## A check on one printed claim",
            "",
            "Horley and Lee say open-beak forms of sign 660 occur on Br2, Br7, Pr2, and Ua3. In the vendored pages:",
            "",
        ]
    )
    for audit in result["open_beak_audit"]:
        if not audit["line_found"]:
            state = "line not in the vendored text"
        elif audit["present_in_vendored_text"]:
            state = "stem 660 is on the line"
        else:
            others = ", ".join(audit["beak_series_stems"]) or "none"
            state = (
                "stem 660 is not on the line. Other 600-series stems there: "
                f"{others}. They are not treated as open-beak 660"
            )
        lines.append(f"- {audit['line']}: {state}.")
    j_row = result["inscribed_reimiro"]["rei_miro_1"]
    l_row = result["inscribed_reimiro"]["rei_miro_2"]
    lines.extend(
        [
            "",
            "## Carved objects that do not yield a sign meaning",
            "",
            f"Rei miro 1 (tablet J) has {j_row['stem_count']} stems in the vendored text: {' '.join(j_row['stems']) or 'none'}. Implication: null.",
            "",
            f"Rei miro 2 (tablet L) has {l_row['stem_count']} stems. Implication: null. The list is in the JSON.",
            "",
            "The New York birdman figure is not vendored, so its signs are null. Tahonga pendants, moai kavakava cranial carvings, and the 'Orongo stones are documented for what the objects were. The hand-like carving on Peabody Essex E 18646 is only called similar to 052, 52x, or 162, so those numbers stay unadopted and untested.",
            "",
            "## What is supported, and what is speculation",
            "",
        ]
    )
    threshold = result["method"]["bonferroni_threshold"]
    cleared = []
    if threshold is not None:
        for sign, row in result["signs"].items():
            if row["concentration"] is None:
                continue
            if row["concentration"]["p_greater"] <= threshold:
                cleared.append(sign)
    if result["supported_distribution"]:
        joined = ", ".join(result["supported_distribution"])
        lines.append(
            f"These signs are more bunched across tablets than the null and than the ordinary common signs: {joined}. Bunching is not a meaning. `supported_lexical_readings` is empty."
        )
    elif cleared:
        lines.append(
            "These signs meet the corrected threshold on their own: "
            + ", ".join(cleared)
            + ". They do not beat the ordinary common signs, which are bunched at least as tightly. "
            "The small p-value is the usual shape of this corpus, not evidence that the petroglyph theme gathered them. "
            "`supported_lexical_readings` is empty."
        )
    else:
        lines.append(
            "No tested sign meets the corrected threshold. None of them gains a distributional meaning on top of the picture. "
            "`supported_lexical_readings` is empty."
        )
    lines.extend(
        [
            "",
            "Supported, as iconography only:",
            "",
            (
                "- 700b, 721, and 733 are the fish forms Horley and Lee name. "
                f"In this corpus they occur {result['signs']['700b']['stem_count']}, "
                f"{result['signs']['721']['stem_count']}, and "
                f"{result['signs']['733']['stem_count']} times. "
                "That is below the pre-set count of 20, so the concentration test is null. "
                "The picture match is real as far as their paper goes. A fishing reading is speculation. "
                "Stem 700 is a wider sign and is not this match."
            ),
            "- 074 resembles the hook or gourd in house 44. Strength: printed number, plus Barthel's count of 94. Calling it a fertility sign because a komari was cut on the petroglyph is speculation.",
            "- 660 resembles a long-beaked bird, and 680 a two-headed one. Strength: printed numbers and counts. A manutara or Makemake reading is speculation.",
            "- 007 resembles a rei miro. Strength: printed number. It does not read the texts on the wooden pectorals.",
            "- 240 resembles a sitting man, 513 an eye mask, 550 a bird with a star at its head. Strength: one sentence in Horley and Lee 2008, with no count. A Makemake reading of 513 is speculation.",
            "",
            "Speculation, left null and untested: glyph 51 as komari, glyph 638 as the birdman, any turtle or canoe sign, any tahonga or egg sign, Fedorova's reading of a cranial carving as the name Vai Rapa, and Fischer's creation-chant decipherment. Those last two are someone else's hypotheses. This round does not adopt them.",
            "",
            "Horley and Lee themselves say the Mata Ngarau pictures match single signs and do not form a continuous text. Fischer's definition, as McLaughlin quotes it, requires a sequence of two or more glyphs before something counts as an inscription. The rock art can suggest what a picture is of. It cannot, by itself, supply the word.",
            "",
            "## Sources",
            "",
            "- Barthel, Thomas S. 1958. *Grundlagen zur Entzifferung der Osterinselschrift*. Hamburg: Cram, de Gruyter. Counts as cited by Horley and Lee, not re-read page by page here.",
            "- Fischer, Steven Roger. 1997. *Rongorongo: The Easter Island Script*. Oxford: Clarendon Press. Used for the object catalog as updated by Horley, Davletshin and Wieczorek 2018, and for the definition of an inscription as quoted by McLaughlin.",
            "- Forment, Francina. 1993. In Fischer, ed., *Easter Island Studies*. Cited at page 212 by Wieczorek and Horley for designs shared across figurines and tahonga.",
            "- Horley, Paul. 2005. Allographic variations and statistical analysis of the rongorongo script. *Rapa Nui Journal* 19(2): 107–116.",
            "- Horley, Paul, and Georgia Lee. 2008. Rock art of the sacred precinct at Mata Ngarau, 'Orongo. *Rapa Nui Journal* 22(2): 110–116.",
            "- Horley, Paul, and Georgia Lee. 2012. Easter Island's birdman stones in the collection of the Peabody Museum. *Rapa Nui Journal* 26(1): 5–20. No glyph number was verified from the article text in this round.",
            "- Horley, Paul, Albert Davletshin, and Rafal Wieczorek. 2018. How many scripts were there on Easter Island? In Jakubowska-Vorbrich, ed., *The Sleep of Reason Produces Monsters*.",
            "- Koll, Robert R. 1991. Petroglyphs inside Orongo's houses. *Rapa Nui Journal* 5(4): 61–62.",
            "- Lee, Georgia. 1990. *An Uncommon Guide to Easter Island*. Counts of 375 birdmen, 195 komari, and 140 faces, as quoted by Horley and Lee 2008.",
            "- Lee, Georgia. 1992. *The Rock Art of Easter Island*. Los Angeles: UCLA Institute of Archaeology.",
            "- Lee, Georgia. 2004. Rapa Nui's sea creatures. *Rapa Nui Journal* 18(1).",
            "- McLaughlin, Shawn. 2004. Rongorongo and the rock art of Easter Island. *Rapa Nui Journal* 18(2): 87–94.",
            "- Métraux, Alfred. 1940. *Ethnology of Easter Island*. Bernice P. Bishop Museum Bulletin 160. Pages as cited by Horley and Lee.",
            "- Orliac, Catherine, and Michel Orliac. 2008. *Trésors de l'Île de Pâques / Treasures of Easter Island*. Paris.",
            "- Routledge, Katherine. 1919. *The Mystery of Easter Island*. London.",
            "- Routledge, Katherine. 1920. Survey of the village and carved rocks of Orongo. *Journal of the Royal Anthropological Institute* 50: 425–451.",
            "- Wieczorek, Rafal M., and Paul Horley. 2023. New visualization method for cranial carvings of Rapanui wooden figurines. *Archaeometry*.",
            "",
        ]
    )
    return "\n".join(lines)


def write_round4_trackc(result: dict[str, Any]) -> None:
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    DOC_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    DOC_PATH.write_text(render_round4_trackc(result), encoding="utf-8")
