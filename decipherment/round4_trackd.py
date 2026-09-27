"""Round 4, Track D: dating and a copying tree for the tablets.

Sign numbers and cited physical facts only. No reading is assigned.
``MockProvider`` is accepted and never called.

Passages are the gated alignments from Round 2 Track C (99 significant
parallels). The copying tree is neighbor-joining on those alignments, with
a passage bootstrap. The Great Tradition (H, P, Q) is also scored by
shared variants in columns where all three pairwise alignments agree.
"""

from __future__ import annotations

import json
import random
from collections import Counter, defaultdict
from dataclasses import dataclass
from math import comb
from pathlib import Path
from typing import Any, Sequence

from agents.base.providers import MockProvider
from decipherment.barthel_corpus import load_located_sides
from decipherment.inventories import encode_token
from decipherment.track_c_parallels import (
    JSON_PATH as SUBSTITUTION_JSON,
    Passage,
    SideText,
    find_passages,
    load_side_texts,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DOC_PATH = REPO_ROOT / "docs" / "decipherment" / "round4_trackD_dating_stemma.md"
JSON_PATH = REPO_ROOT / "data" / "decipherment" / "round4d_dating_stemma.json"

# Pre-specified before the tree is read. A pair enters the distance tree
# only when that pair has at least this many deduplicated aligned columns.
# Adding a tablet's short parallels together is not enough: a bridge of a
# few columns would connect separate texts, and shortest-path fill would
# then invent a distance between texts that were never aligned.
TREE_MIN_COLUMNS = 40
BOOTSTRAP_REPLICATES = 1000
PASSAGE_BOOTSTRAP_SEED = 4
COLUMN_BOOTSTRAP_SEED = 5
FORM_BOOTSTRAP_SEED = 6
RAREFACTION_K = 80
# Missing distances in a disconnected bootstrap replicate. Observed
# p-distances are at most 1, so this sits outside the observed range.
DISCONNECTED_DISTANCE = 1.5
GT_TABLETS = ("H", "P", "Q")
# Barthel modification letters (Barthel 1958: 38–42, as used in allographs.py).
MODIFICATION_LETTERS = frozenset("fosxyht")

KOHAUMOTU_TABLE = (
    "Vendored Kohaumotu tablets.html (P. Spaelti, last updated 2012-02-22; "
    "material footnote cites Orliac 2010), tests/fixtures/tahua_aa_html/tablets.html"
)
FERRARA_2024 = (
    "Ferrara, Tassoni, Kromer, Wacker, Friedrich, Tonini, Lastilla, Ravanelli, "
    "and Talamo 2024, Scientific Reports 14:2794, doi:10.1038/s41598-024-53063-7"
)
ORLIAC_2005 = (
    "Orliac 2005, Archaeology in Oceania 40:115–119, "
    "doi:10.1002/j.1834-4453.2005.tb00597.x"
)
ORLIAC_2007 = "Orliac 2007, Rapa Nui Journal 21:7–10"
ORLIAC_2010 = (
    "Orliac 2010, in Wallin and Martinsson-Wallin (eds.), The Gotland Papers, "
    "pp. 125–140, as cited by Ferrara et al. 2024 and by the Kohaumotu material note"
)
WIECZOREK_2021 = (
    "Wieczorek, Frankiewicz, Oskolski, and Horley 2021, Journal of Island and "
    "Coastal Archaeology, doi:10.1080/15564894.2021.1950874"
)
FISCHER_1997 = "Fischer 1997, Rongorongo: The Easter Island Script (Clarendon)"
HORLEY_2007 = (
    "Horley 2007, Rapa Nui Journal 21(1), as cited in this repository's "
    "Round 2 Track C for the G/K relationship"
)
DAVLETSHIN_2017 = (
    "Davletshin 2017, Journal of the Polynesian Society 126, as cited in "
    "Round 2 Track C: P is his reference copy against H and Q"
)
EYRAUD_VIA_WIECZOREK = (
    "Eyraud 1866, quoted by Wieczorek et al. 2021: the signs were drawn with sharp stones"
)
TOOL_CORPUS = (
    "No tablet-specific tool identification was read for this object. "
    + EYRAUD_VIA_WIECZOREK
    + ". The public corpus survey also reports an oral tradition of obsidian "
    "flakes and shark teeth, and Barthel's two-stage account (sketch, then "
    "deepen). That survey was not re-checked against Barthel's own pages here."
)
SECONDARY_CORPUS = (
    "Public corpus survey (the English Wikipedia article 'Rongorongo', read "
    "for this track). Used only where a primary page was not re-read, and labeled secondary."
)

# Dimensions are millimetres in the Kohaumotu table. None are remeasured here.
_CATALOG_ROWS: tuple[dict[str, Any], ...] = (
    {
        "code": "A",
        "name": "Tahua (the Oar)",
        "in_transcription": True,
        "wood": "Fraxinus excelsior (European ash)",
        "wood_citation": f"{FERRARA_2024}; {KOHAUMOTU_TABLE}",
        "radiocarbon": (
            "ETH-125842 / BRA-6125, 122±13 BP. With a felling offset of 50±5 years, "
            "the unmodelled 68.3% range is 1862–1977 cal AD. Ferrara et al. discard "
            "1934–1977 because the tablet was collected in 1869, and they keep "
            "1862–1887 (19.7%). Inside their Bayesian Rongorongo phase the "
            "felling-adjusted 68.3% range is 1752–1773 cal AD. The date is a "
            "terminus post quem for the board, not a carving date."
        ),
        "radiocarbon_citation": FERRARA_2024,
        "provenance": (
            "Congregazione dei Sacri Cuori, Rome. Collected with B–D in 1869 and "
            "sent to Bishop Tepano Jaussen."
        ),
        "provenance_citation": FERRARA_2024,
        "dimensions_mm": "Kohaumotu 909×115×26; Ferrara et al. 912×115×28",
        "condition": "Fine (Kohaumotu). Ferrara et al.: good preservation, no apparent damage.",
        "condition_citation": f"{KOHAUMOTU_TABLE}; {FERRARA_2024}",
        "carving": (
            "Inscribed on a European or American oar blade (Ferrara et al. 2024). "
            + TOOL_CORPUS
        ),
    },
    {
        "code": "B",
        "name": "Aruku Kurenga",
        "in_transcription": True,
        "wood": "Thespesia populnea (Pacific rosewood, makoi)",
        "wood_citation": f"{FERRARA_2024}; {ORLIAC_2005}; {KOHAUMOTU_TABLE}",
        "radiocarbon": (
            "ETH-125843 / BRA-6126, 125±13 BP. Felling offset 20±5 years: "
            "unmodelled 1732–1947 cal AD (68.3%). Ferrara et al. discard "
            "1903–1947 (45.5%) as after the collection, and treat 1832–1857 "
            "(20.7%) as the prominent remaining slice, with a small 1732–1736 "
            "slice (2.1%). Terminus post quem."
        ),
        "radiocarbon_citation": FERRARA_2024,
        "provenance": "Congregazione dei Sacri Cuori, Rome. Same 1869 Jaussen collection as A, C, and D.",
        "provenance_citation": FERRARA_2024,
        "dimensions_mm": "Kohaumotu 415×152×29; Ferrara et al. 415×152×31",
        "condition": "Fine (Kohaumotu). Ferrara et al.: masterfully carved, about a dozen lines each side.",
        "condition_citation": f"{KOHAUMOTU_TABLE}; {FERRARA_2024}",
        "carving": "Ferrara et al. 2024 call the carving masterful. " + TOOL_CORPUS,
    },
    {
        "code": "C",
        "name": "Mamari",
        "in_transcription": True,
        "wood": "Thespesia populnea",
        "wood_citation": f"{FERRARA_2024}; {ORLIAC_2005}; {KOHAUMOTU_TABLE}",
        "radiocarbon": (
            "ETH-125845 / BRA-6129, 189±13 BP. Felling offset 25±5 years: "
            "1694–1840 cal AD (68.3%), in four slices: 1694–1727 (32.4%), "
            "1744–1770 (18.2%), 1819–1840 (5.3%), 1781–1789 (2.4%). "
            "Terminus post quem. Orliac 2005, as cited by Wieczorek et al. 2021, "
            "argues the trunk was about 20 cm across and the tree about 15 m, "
            "larger than the trees European visitors described."
        ),
        "radiocarbon_citation": f"{FERRARA_2024}; {WIECZOREK_2021} citing {ORLIAC_2005}",
        "provenance": "Congregazione dei Sacri Cuori, Rome. Same 1869 Jaussen collection.",
        "provenance_citation": FERRARA_2024,
        "dimensions_mm": "Kohaumotu 290×196×25; Ferrara et al. 290×194×23",
        "condition": (
            "Fine (Kohaumotu). Ferrara et al.: damaged in places; some signs are "
            "carved inside a cavity, so the inscription is later than that damage."
        ),
        "condition_citation": f"{KOHAUMOTU_TABLE}; {FERRARA_2024}",
        "carving": (
            "Ferrara et al. 2024: signs cut into a pre-existing cavity. "
            + TOOL_CORPUS
        ),
    },
    {
        "code": "D",
        "name": "Échancrée",
        "in_transcription": True,
        "wood": (
            "Podocarpus latifolia in Ferrara et al. 2024 (citing Orliac 2010); "
            "Kohaumotu writes Podocarpus sp. cf. Latifolia. Not native to Rapa Nui. "
            "Orliac 2007 groups this wood with N, P, and S."
        ),
        "wood_citation": f"{FERRARA_2024}; {ORLIAC_2007}; {KOHAUMOTU_TABLE}",
        "radiocarbon": (
            "ETH-125844 / BRA-6127, 474±13 BP. Felling offset 50±5 years: "
            "1493–1509 cal AD (68.3%) and 1483–1520 (95.4%). This is the early "
            "outlier. Ferrara et al. warn that foreign wood can be driftwood or "
            "ship timber, and that a radiocarbon age of the wood is only a "
            "terminus post quem for the carving."
        ),
        "radiocarbon_citation": FERRARA_2024,
        "provenance": (
            "Congregazione dei Sacri Cuori, Rome. Ferrara et al.: the four Rome "
            "tablets were sent to Jaussen in 1869. The public corpus survey "
            "identifies D as the board Jaussen was given with a cord of hair wound on it."
        ),
        "provenance_citation": f"{FERRARA_2024}; {SECONDARY_CORPUS}",
        "dimensions_mm": "Kohaumotu 241×121×26; Ferrara et al. 239×123×24",
        "condition": (
            "Good (Kohaumotu). Ferrara et al., citing Fischer 1997: one side "
            "smoothed and well engraved, the other rougher, possibly two scribes. "
            "After the text, notches were cut into the long sides and the board "
            "was reused as a spool."
        ),
        "condition_citation": f"{KOHAUMOTU_TABLE}; {FERRARA_2024} citing {FISCHER_1997}",
        "carving": (
            "Ferrara et al. 2024, citing Fischer 1997: two hands are suggested. "
            "Notches for a cord are later than the inscription. The cutting tool "
            "is not identified in that paper. " + EYRAUD_VIA_WIECZOREK + "."
        ),
    },
    {
        "code": "E",
        "name": "Keiti",
        "in_transcription": True,
        "wood": "Unidentified in the Kohaumotu table.",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": (
            "Kohaumotu condition is Destroyed. The public corpus survey places "
            "the lost tablet at Leuven and says it burned in the First World War. Secondary."
        ),
        "provenance_citation": f"{KOHAUMOTU_TABLE}; {SECONDARY_CORPUS}",
        "dimensions_mm": "Kohaumotu 390×130×25",
        "condition": "Destroyed (Kohaumotu). The transcription used here is the published copy, not a surviving board.",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": TOOL_CORPUS,
    },
    {
        "code": "F",
        "name": "Stephen-Chauvet fragment",
        "in_transcription": True,
        "wood": "Unidentified in the Kohaumotu table. The public corpus survey guesses palm and marks the guess with a question mark. Secondary.",
        "wood_citation": f"{KOHAUMOTU_TABLE}; {SECONDARY_CORPUS}",
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "The public corpus survey places the fragment in New York. Secondary. Kohaumotu does not name a museum on the tablets table.",
        "provenance_citation": SECONDARY_CORPUS,
        "dimensions_mm": "Kohaumotu 111×80×15",
        "condition": "Good (Kohaumotu), but only a fragment: 51 signs in that table.",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": (
            "The public corpus survey calls the glyphs crudely executed. Secondary. "
            + TOOL_CORPUS
        ),
    },
    {
        "code": "G",
        "name": "Small Santiago",
        "in_transcription": True,
        "wood": "Thespesia populnea",
        "wood_citation": f"{ORLIAC_2005}; {KOHAUMOTU_TABLE} (Orliac 2010 note)",
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "Named Small Santiago on the vendored Kohaumotu pages. Museum accession was not re-read beyond that name.",
        "provenance_citation": "tests/fixtures/small_santiago_gr_html/Gr.html item title",
        "dimensions_mm": "Kohaumotu 319×122×22",
        "condition": "Fine (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": (
            "Horley 2007 treats London K as a copy of G recto (Track C citation). "
            + TOOL_CORPUS
        ),
    },
    {
        "code": "H",
        "name": "Great Santiago",
        "in_transcription": True,
        "wood": "Thespesia populnea",
        "wood_citation": f"{ORLIAC_2005}; {KOHAUMOTU_TABLE}",
        "radiocarbon": (
            "Not radiocarbon dated in the sources read for this track. "
            "It is one witness of the Great Tradition with P and Q."
        ),
        "radiocarbon_citation": None,
        "provenance": "Named Great Santiago on the vendored Kohaumotu pages.",
        "provenance_citation": "tests/fixtures/large_santiago_hr_html/Hr.html item title",
        "dimensions_mm": "Kohaumotu 449×125, thickness n/a",
        "condition": (
            "Good (Kohaumotu). The public corpus survey, attributing the "
            "observation to Orliac, describes a fire-plow groove on the recto. "
            "That page of Orliac was not re-read here. Secondary."
        ),
        "condition_citation": f"{KOHAUMOTU_TABLE}; {SECONDARY_CORPUS}",
        "carving": TOOL_CORPUS,
    },
    {
        "code": "I",
        "name": "Santiago Staff",
        "in_transcription": True,
        "wood": "Unidentified in the Kohaumotu table.",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "Named Santiago Staff on the vendored Kohaumotu pages. A chief's staff, not a flat tablet.",
        "provenance_citation": "tests/fixtures/santiago_ia_html/I_index.html",
        "dimensions_mm": "Kohaumotu length 1260, diameter 60",
        "condition": "Good (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": (
            "Track 3 of this repository records Barthel 999 as the staff's vertical "
            "stroke, from the Kohaumotu digitization note. That stroke is not a "
            "carving-tool identification. " + TOOL_CORPUS
        ),
    },
    {
        "code": "J",
        "name": "Reimiro 1",
        "in_transcription": True,
        "wood": "Unidentified in the Kohaumotu table.",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "The public corpus survey places the large reimiro in London. Secondary.",
        "provenance_citation": SECONDARY_CORPUS,
        "dimensions_mm": "Kohaumotu length 700",
        "condition": "Good (Kohaumotu). Two signs in that table.",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": "A pectoral, not a tablet. " + TOOL_CORPUS,
    },
    {
        "code": "K",
        "name": "Small London",
        "in_transcription": True,
        "wood": "Thespesia populnea with a question mark in the Kohaumotu table (Orliac 2010 note).",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "British Museum, from the link on the vendored K index page.",
        "provenance_citation": "tests/fixtures/small_london_kr_html/K_index.html",
        "dimensions_mm": "Kohaumotu 218×68×20",
        "condition": "Good (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": (
            f"{HORLEY_2007}. The public corpus survey calls the glyphs crude and "
            "lists K among pieces suspected of a steel blade. That suspicion is secondary. "
            + TOOL_CORPUS
        ),
    },
    {
        "code": "L",
        "name": "Reimiro 2",
        "in_transcription": True,
        "wood": (
            "Kohaumotu: unidentified. Orliac 2005 examined a reimiro with the "
            "tablets and found Thespesia; the public corpus survey assigns that "
            "pectoral to L. The letter assignment is secondary."
        ),
        "wood_citation": f"{KOHAUMOTU_TABLE}; {ORLIAC_2005}; {SECONDARY_CORPUS}",
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "The public corpus survey places the small reimiro in London. Secondary.",
        "provenance_citation": SECONDARY_CORPUS,
        "dimensions_mm": "Kohaumotu 423×178×15",
        "condition": "Fine (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": "A pectoral. " + TOOL_CORPUS,
    },
    {
        "code": "M",
        "name": "Great Vienna",
        "in_transcription": True,
        "wood": (
            "Thespesia populnea in the Kohaumotu table (no Orliac 2010 footnote on that cell). "
            "Lavachery 1934 is the earlier identification, cited by Orliac 2005."
        ),
        "wood_citation": f"{KOHAUMOTU_TABLE}; {ORLIAC_2005} citing Lavachery 1934",
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "Museum für Völkerkunde, Wien, from the link on the vendored M index page.",
        "provenance_citation": "tests/fixtures/vienna_ma_html/M_index.html",
        "dimensions_mm": "Kohaumotu 285×145×23",
        "condition": "Poor (Kohaumotu). Side b destroyed in that table; 54 signs remain on side a.",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": TOOL_CORPUS,
    },
    {
        "code": "N",
        "name": "Small Vienna",
        "in_transcription": True,
        "wood": "Podocarpus sp. (cf. latifolia). Same identification Orliac 2007 gives for D, P, and S.",
        "wood_citation": f"{ORLIAC_2007}; {KOHAUMOTU_TABLE}",
        "radiocarbon": (
            "Not separately dated. Orliac 2007 hypothesizes that D, N, P, and S "
            "were cut from one board. HYPOTHESIS, not a radiocarbon result."
        ),
        "radiocarbon_citation": ORLIAC_2007,
        "provenance": "Museum für Völkerkunde, Wien, from the vendored N index link. Wieczorek et al. 2021: the Vienna tablets came with the Schlubach shipment.",
        "provenance_citation": f"tests/fixtures/vienna_na_html/N_index.html; {WIECZOREK_2021} citing {FISCHER_1997}",
        "dimensions_mm": "Kohaumotu 260×53×21",
        "condition": "Good (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": (
            "The public corpus survey, citing Haberlandt, says the grooves look "
            "like a sharpened bone and that details were retouched with obsidian. "
            "Secondary; Haberlandt was not re-read. " + EYRAUD_VIA_WIECZOREK + "."
        ),
    },
    {
        "code": "O",
        "name": "Berlin tablet (Boomerang)",
        "in_transcription": True,
        "wood": (
            "Thespesia populnea, identified anatomically by Wieczorek et al. 2021. "
            "The 2012 Kohaumotu table still says unidentified. They reject the "
            "driftwood identification in Fischer 1997."
        ),
        "wood_citation": f"{WIECZOREK_2021}; {KOHAUMOTU_TABLE}",
        "radiocarbon": (
            "117±14 BP (University of Waikato). SHCal20 95% ranges: 1706–1721 "
            "(5.5%), 1811–1838 (23.1%), 1848–1868 (5.5%), 1878–1928 (61.4%). "
            "Collected in 1882, so the post-1882 tail is impossible. The authors' "
            "conservative window is 1706–1870, most likely the nineteenth century; "
            "the abstract says about 1830–1870. Old-wood inbuilt age for this "
            "species is unlikely to exceed about 40 years (their discussion)."
        ),
        "radiocarbon_citation": WIECZOREK_2021,
        "provenance": (
            "Ethnologisches Museum, Berlin, VI 4878. Acquired after HMS Hyäne's "
            "1882 visit, via Salmon and Schlubach; arrived April 1883."
        ),
        "provenance_citation": f"{WIECZOREK_2021}; tests/fixtures/boomerang_oa_html/O_index.html",
        "dimensions_mm": "Wieczorek et al. 1030×125×60, weight 2.6 kg; Kohaumotu length 1030, width 130",
        "condition": (
            "Poor (Kohaumotu). Wieczorek et al.: cave storage destroyed about 90% "
            "of the inscription; woodlice and wormholes; a few carbonized spots. "
            "Flutes survive on the eroded side."
        ),
        "condition_citation": f"{KOHAUMOTU_TABLE}; {WIECZOREK_2021}",
        "carving": (
            "Wieczorek et al. 2021: a sharp implement cut the signs inside shallow "
            "flutes. They say the flutes were perhaps polished with shark skin. "
            "The shark-skin step is their suggestion, marked as uncertain by them."
        ),
    },
    {
        "code": "P",
        "name": "Great St. Petersburg",
        "in_transcription": True,
        "wood": (
            "Podocarpus, same group as D, N, and S (Orliac 2007). Kohaumotu: "
            "Podocarpus sp. cf. Latifolia. The public corpus survey, citing Fischer, "
            "calls it a reshaped European or American oar. That oar description is secondary."
        ),
        "wood_citation": f"{ORLIAC_2007}; {KOHAUMOTU_TABLE}; {SECONDARY_CORPUS} citing {FISCHER_1997}",
        "radiocarbon": (
            "Not radiocarbon dated in the sources read for this track. "
            "Orliac 2007 hypothesizes one board for D, N, P, and S. HYPOTHESIS. "
            "Ferrara et al. 2024 repeat that N, P, and S may be contemporary with D, "
            "as a suggestion, not as a date."
        ),
        "radiocarbon_citation": f"{ORLIAC_2007}; {FERRARA_2024}",
        "provenance": "Museum of Anthropology and Ethnology, St. Petersburg, the large tablet of that collection (Orliac 2007; Kohaumotu item title).",
        "provenance_citation": f"{ORLIAC_2007}; tests/fixtures/large_st_petersburg_pr_html/Pr.html",
        "dimensions_mm": "Kohaumotu 620×144×27",
        "condition": (
            "Fine (Kohaumotu). The public corpus survey says P and S were later "
            "cut as canoe planking. Secondary, attributed there to the story of Niari."
        ),
        "condition_citation": f"{KOHAUMOTU_TABLE}; {SECONDARY_CORPUS}",
        "carving": TOOL_CORPUS,
    },
    {
        "code": "Q",
        "name": "Small St. Petersburg",
        "in_transcription": True,
        "wood": "Thespesia populnea. Orliac 2005 dated this tablet; Wieczorek et al. 2021 describe it as Pacific rosewood.",
        "wood_citation": f"{ORLIAC_2005}; {WIECZOREK_2021}; {KOHAUMOTU_TABLE}",
        "radiocarbon": (
            "Orliac 2005: 80±40 BP. The 95% ranges quoted by Wieczorek et al. 2021 "
            "are 1680–1740, 1800–1930, and 1950–1960. Ferrara et al. 2024 say a "
            "SHCal20 recalibration's most reliable slice is 1812–1836, citing "
            "Horley 2021. Orliac notes the poor condition could allow an earlier "
            "manufacture (Wieczorek et al. citing Orliac 2005: 118). Terminus post quem."
        ),
        "radiocarbon_citation": f"{ORLIAC_2005}; {WIECZOREK_2021}; {FERRARA_2024}",
        "provenance": (
            "Museum of Anthropology and Ethnology, St. Petersburg. Collected by "
            "Nicholai Miklouho-Maclay in 1871 from Rapanui expatriates on Mangareva or Tahiti."
        ),
        "provenance_citation": WIECZOREK_2021,
        "dimensions_mm": "Kohaumotu 418×112×28",
        "condition": (
            "Good (Kohaumotu). Wieczorek et al., citing Orliac 2005: wood degradation "
            "and insect damage. The public corpus survey adds clay, a cut end, "
            "gouges, and burns. Those extra details are secondary."
        ),
        "condition_citation": f"{KOHAUMOTU_TABLE}; {WIECZOREK_2021}; {SECONDARY_CORPUS}",
        "carving": TOOL_CORPUS,
    },
    {
        "code": "R",
        "name": "Atua Mata Riri (Small Washington)",
        "in_transcription": True,
        "wood": "Unidentified in the Kohaumotu table.",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "Smithsonian A129773-0, from the link on the vendored R index page.",
        "provenance_citation": "tests/fixtures/atua_ra_html/R_index.html",
        "dimensions_mm": "Kohaumotu 245×95×18",
        "condition": "Good (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": (
            "Horley 2007 reports a parallel with Tahua after recoding signs into "
            "glyph elements (Track C). That parallel did not clear the stem gate. "
            + TOOL_CORPUS
        ),
    },
    {
        "code": "S",
        "name": "Great Washington",
        "in_transcription": True,
        "wood": "Podocarpus sp. (cf. latifolia), with D, N, and P (Orliac 2007).",
        "wood_citation": f"{ORLIAC_2007}; {KOHAUMOTU_TABLE}",
        "radiocarbon": (
            "Not separately dated. Same one-board hypothesis as N and P (Orliac 2007). HYPOTHESIS."
        ),
        "radiocarbon_citation": ORLIAC_2007,
        "provenance": "Smithsonian, from the link on the vendored S index page.",
        "provenance_citation": "tests/fixtures/washington_sa_html/S_index.html",
        "dimensions_mm": "Kohaumotu 642×122×18",
        "condition": (
            "Good (Kohaumotu). The public corpus survey says it was later cut for "
            "planking, with P. Secondary."
        ),
        "condition_citation": f"{KOHAUMOTU_TABLE}; {SECONDARY_CORPUS}",
        "carving": TOOL_CORPUS,
    },
    {
        "code": "T",
        "name": "Honolulu 1 (B.03629)",
        "in_transcription": True,
        "wood": "Unidentified in the Kohaumotu table.",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "Bishop Museum B.03629, from the vendored T index link.",
        "provenance_citation": "tests/fixtures/honolulu_ta_html/T_index.html",
        "dimensions_mm": "Kohaumotu 305×95×20",
        "condition": "Poor (Kohaumotu). One inscribed side in that table.",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": TOOL_CORPUS,
    },
    {
        "code": "U",
        "name": "Honolulu 2 (B.03623)",
        "in_transcription": True,
        "wood": "Unidentified in the Kohaumotu table. The public corpus survey calls it a European or American beam. Secondary.",
        "wood_citation": f"{KOHAUMOTU_TABLE}; {SECONDARY_CORPUS}",
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "Bishop Museum B.03623, from the vendored U index link.",
        "provenance_citation": "tests/fixtures/honolulu_ua_html/U_index.html",
        "dimensions_mm": "Kohaumotu 680×80×22",
        "condition": "Poor (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": (
            "The public corpus survey says the two sides are different hands. Secondary. "
            + TOOL_CORPUS
        ),
    },
    {
        "code": "V",
        "name": "Honolulu 3 (B.03622)",
        "in_transcription": True,
        "wood": (
            "Unidentified in the Kohaumotu table. The public corpus survey, citing "
            "Fischer, groups it with the European or American oars. Secondary."
        ),
        "wood_citation": f"{KOHAUMOTU_TABLE}; {SECONDARY_CORPUS} citing {FISCHER_1997}",
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "Bishop Museum B.03622, from the vendored V index link.",
        "provenance_citation": "tests/fixtures/honolulu_va_html/V_index.html",
        "dimensions_mm": "Kohaumotu 710×88×30",
        "condition": "Poor (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": (
            "The public corpus survey lists V among texts suspected of a steel blade. Secondary. "
            + TOOL_CORPUS
        ),
    },
    {
        "code": "W",
        "name": "Honolulu 4 (B.00445)",
        "in_transcription": False,
        "wood": "Unidentified in the Kohaumotu table.",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "Bishop Museum B.00445, from the vendored W index link. No digit transcription is in the parallel-passage corpus.",
        "provenance_citation": "tests/fixtures/honolulu_w_html/W_index.html",
        "dimensions_mm": "Kohaumotu 63×20×15",
        "condition": "Splinter (Kohaumotu). The vendored page says the fragment is in very poor condition.",
        "condition_citation": f"{KOHAUMOTU_TABLE}; tests/fixtures/honolulu_w_html/W.html",
        "carving": TOOL_CORPUS,
    },
    {
        "code": "X",
        "name": "Tangata manu",
        "in_transcription": False,
        "wood": "Toromiro, in the Kohaumotu table only. Not one of the microscope identifications cited above.",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "The public corpus survey places a birdman statuette in New York. Secondary. No digit transcription is in the parallel-passage corpus.",
        "provenance_citation": SECONDARY_CORPUS,
        "dimensions_mm": "Kohaumotu length 440",
        "condition": "Fine (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": "A statuette. " + TOOL_CORPUS,
    },
    {
        "code": "Y",
        "name": "Paris snuffbox",
        "in_transcription": False,
        "wood": "Unidentified in the Kohaumotu table.",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "The public corpus survey places it in Paris and says it was pieced together from a tablet. Secondary. Not in the parallel-passage corpus.",
        "provenance_citation": SECONDARY_CORPUS,
        "dimensions_mm": "Kohaumotu 71×50×29",
        "condition": "Fine (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": (
            "The public corpus survey calls the glyphs crude and lists a steel-blade suspicion. Secondary. "
            + TOOL_CORPUS
        ),
    },
    {
        "code": "Z",
        "name": "Poike",
        "in_transcription": False,
        "wood": "Unidentified in the Kohaumotu table.",
        "wood_citation": KOHAUMOTU_TABLE,
        "radiocarbon": "Not dated in the sources read for this track.",
        "radiocarbon_citation": None,
        "provenance": "Named Poike in the Kohaumotu table. The public corpus survey says Fischer does not treat the legible layer as genuine. Secondary. Not in the parallel-passage corpus.",
        "provenance_citation": f"{KOHAUMOTU_TABLE}; {SECONDARY_CORPUS}",
        "dimensions_mm": "Kohaumotu 106×60×27",
        "condition": "Worn (Kohaumotu).",
        "condition_citation": KOHAUMOTU_TABLE,
        "carving": TOOL_CORPUS,
    },
)


@dataclass(frozen=True)
class StemMark:
    """Graphic flags for one stem, in the same order as the stem text."""

    ligature: bool
    parts: int
    surface: str
    modification: bool
    pictorial: bool


Pos = tuple[str, int]


@dataclass(frozen=True)
class AlignedColumn:
    """One column of a pairwise passage, with absolute stem positions."""

    tablet_a: str
    tablet_b: str
    pos_a: Pos | None
    pos_b: Pos | None
    sign_a: str | None
    sign_b: str | None
    passage_index: int


def _round(value: float | None, places: int = 6) -> float | None:
    if value is None:
        return None
    return round(float(value), places)


def _pair_key(left: str, right: str) -> tuple[str, str]:
    return tuple(sorted((left, right)))  # type: ignore[return-value]


def _locus(texts: dict[str, SideText], pos: Pos | None) -> str | None:
    if pos is None:
        return None
    side, index = pos
    line, offset = texts[side].locate(index)
    return f"{line}:{offset}"


def _pictorial(stem: str) -> bool:
    """Headed or animate class in Barthel's hundreds digit.

    The public corpus survey of Barthel 1958 puts geometric and inanimate
    signs in hundreds 0–1, and headed or animate signs in 2–7. Sign 999,
    the staff bar, falls outside 2–7 and is counted as not pictorial.
    This is an operationalization, not a reading.
    """
    if len(stem) != 3 or not stem.isdigit():
        return False
    hundreds = int(stem[0])
    return 2 <= hundreds <= 7


def _modification(surface: str) -> bool:
    return any(character in MODIFICATION_LETTERS for character in surface)


def annotate_corpus(
    texts: dict[str, SideText],
) -> dict[str, tuple[StemMark, ...]]:
    """One mark per stem. The stem sequence must match ``load_side_texts``."""
    marks: dict[str, tuple[StemMark, ...]] = {}
    for raw in load_located_sides():
        built: list[StemMark] = []
        for _number, tokens in raw.lines:
            for token in tokens:
                stems = encode_token(token, "stem")
                if not stems:
                    continue
                surfaces = encode_token(token, "surface")
                if len(surfaces) != len(stems):
                    surfaces = list(stems)
                ligature = ("." in token or ":" in token) and len(stems) > 1
                for stem, surface in zip(stems, surfaces):
                    built.append(
                        StemMark(
                            ligature=ligature,
                            parts=len(stems),
                            surface=surface,
                            modification=_modification(surface),
                            pictorial=_pictorial(stem),
                        )
                    )
        if not built:
            continue
        expected = texts[raw.side].signs
        if len(built) != len(expected):
            raise RuntimeError(f"{raw.side}: {len(built)} marks, {len(expected)} stems")
        marks[raw.side] = tuple(built)
    return marks


def walk_columns(passage: Passage, passage_index: int) -> list[AlignedColumn]:
    left_index = passage.left_start
    right_index = passage.right_start
    columns: list[AlignedColumn] = []
    for sign_a, sign_b in passage.columns:
        pos_a = (passage.left_side, left_index) if sign_a is not None else None
        pos_b = (passage.right_side, right_index) if sign_b is not None else None
        columns.append(
            AlignedColumn(
                tablet_a=passage.left_tablet,
                tablet_b=passage.right_tablet,
                pos_a=pos_a,
                pos_b=pos_b,
                sign_a=sign_a,
                sign_b=sign_b,
                passage_index=passage_index,
            )
        )
        if sign_a is not None:
            left_index += 1
        if sign_b is not None:
            right_index += 1
    return columns


def dedupe_columns(passages: Sequence[Passage]) -> list[AlignedColumn]:
    """Within one tablet pair, keep the higher-scoring passage's column.

    The same stem may still align to two different partners. H can sit in an
    H–P column and an H–Q column. Dropping it from the second pair would erase
    the triple comparison.
    """
    by_pair: dict[tuple[str, str], list[int]] = defaultdict(list)
    for index, passage in enumerate(passages):
        by_pair[_pair_key(passage.left_tablet, passage.right_tablet)].append(index)
    kept: list[AlignedColumn] = []
    for indexes in by_pair.values():
        used: dict[str, set[Pos]] = defaultdict(set)
        order = sorted(
            indexes,
            key=lambda index: (-passages[index].score, -passages[index].span, index),
        )
        for index in order:
            for column in walk_columns(passages[index], index):
                taken = False
                if column.pos_a is not None and column.pos_a in used[column.tablet_a]:
                    taken = True
                if column.pos_b is not None and column.pos_b in used[column.tablet_b]:
                    taken = True
                if taken:
                    continue
                if column.pos_a is not None:
                    used[column.tablet_a].add(column.pos_a)
                if column.pos_b is not None:
                    used[column.tablet_b].add(column.pos_b)
                kept.append(column)
    return kept


def _column_difference(column: AlignedColumn) -> bool:
    if column.sign_a is None or column.sign_b is None:
        return True
    return column.sign_a != column.sign_b


def pairwise_from_columns(
    columns: Sequence[AlignedColumn],
) -> dict[tuple[str, str], dict[str, int]]:
    stats: dict[tuple[str, str], dict[str, int]] = {}
    for column in columns:
        key = _pair_key(column.tablet_a, column.tablet_b)
        bucket = stats.setdefault(key, {"columns": 0, "differences": 0, "gaps": 0, "mismatches": 0})
        bucket["columns"] += 1
        if column.sign_a is None or column.sign_b is None:
            bucket["gaps"] += 1
            bucket["differences"] += 1
        elif column.sign_a != column.sign_b:
            bucket["mismatches"] += 1
            bucket["differences"] += 1
    return stats


def pairwise_from_passages(
    passages: Sequence[Passage],
) -> dict[tuple[str, str], dict[str, int]]:
    """Block counts. A resampled copy of a passage counts again."""
    stats: dict[tuple[str, str], dict[str, int]] = {}
    for index, passage in enumerate(passages):
        for column in walk_columns(passage, index):
            key = _pair_key(column.tablet_a, column.tablet_b)
            bucket = stats.setdefault(
                key, {"columns": 0, "differences": 0, "gaps": 0, "mismatches": 0}
            )
            bucket["columns"] += 1
            if column.sign_a is None or column.sign_b is None:
                bucket["gaps"] += 1
                bucket["differences"] += 1
            elif column.sign_a != column.sign_b:
                bucket["mismatches"] += 1
                bucket["differences"] += 1
    return stats


def p_distance(stats: dict[str, int]) -> float | None:
    if stats["columns"] <= 0:
        return None
    return stats["differences"] / stats["columns"]


def complete_matrix(
    labels: Sequence[str],
    observed: dict[tuple[str, str], float],
) -> tuple[dict[tuple[str, str], float], list[tuple[str, str]]]:
    """Observed p-distances, with shortest-path fill for missing pairs."""
    index = {label: position for position, label in enumerate(labels)}
    size = len(labels)
    matrix = [[0.0 if row == col else 10.0 for col in range(size)] for row in range(size)]
    direct = [[False for _col in range(size)] for _row in range(size)]
    for (left, right), distance in observed.items():
        if left not in index or right not in index:
            continue
        i = index[left]
        j = index[right]
        matrix[i][j] = matrix[j][i] = distance
        direct[i][j] = direct[j][i] = True
    for mid in range(size):
        for row in range(size):
            for col in range(size):
                through = matrix[row][mid] + matrix[mid][col]
                if through < matrix[row][col]:
                    matrix[row][col] = through
    filled: dict[tuple[str, str], float] = {}
    imputed: list[tuple[str, str]] = []
    for row in range(size):
        for col in range(row + 1, size):
            key = _pair_key(labels[row], labels[col])
            distance = matrix[row][col]
            if distance >= 10.0:
                distance = DISCONNECTED_DISTANCE
                imputed.append(key)
            elif not direct[row][col]:
                imputed.append(key)
            filled[key] = distance
    return filled, imputed


def closest_pair(labels: Sequence[str], distances: dict[tuple[str, str], float]) -> str:
    """The nearest pair, or ``unresolved`` when the winner is tied."""
    pairs = list(distances.items())
    if not pairs:
        return "unresolved"
    best = min(distance for _pair, distance in pairs)
    winners = [pair for pair, distance in pairs if abs(distance - best) <= 1e-12]
    if len(winners) != 1:
        return "unresolved"
    left, right = winners[0]
    return f"{left}–{right}"


@dataclass
class PhyNode:
    name: str
    leaves: frozenset[str]
    left: PhyNode | None = None
    right: PhyNode | None = None
    left_length: float = 0.0
    right_length: float = 0.0

    @property
    def internal(self) -> bool:
        return self.left is not None and self.right is not None


def neighbor_joining(
    labels: Sequence[str],
    distances: dict[tuple[str, str], float],
) -> PhyNode:
    """Saitou and Nei 1987. Branch lengths may be negative."""
    nodes: list[PhyNode] = [PhyNode(name=label, leaves=frozenset((label,))) for label in labels]
    dist: dict[tuple[str, str], float] = dict(distances)
    counter = 0
    while len(nodes) > 2:
        size = len(nodes)
        names = [node.name for node in nodes]
        totals = {name: 0.0 for name in names}
        for i, left in enumerate(names):
            for right in names[i + 1 :]:
                value = dist[_pair_key(left, right)]
                totals[left] += value
                totals[right] += value
        best_q = None
        best_pair: tuple[str, str] | None = None
        for i, left in enumerate(names):
            for right in names[i + 1 :]:
                pair = _pair_key(left, right)
                q_value = (size - 2) * dist[pair] - totals[left] - totals[right]
                # For three taxa the Q scores can tie. Prefer the shorter
                # distance so the drawing matches the p-distances.
                closer = best_pair is not None and abs(q_value - best_q) <= 1e-12 and dist[pair] < dist[best_pair]
                if best_q is None or q_value < best_q - 1e-12 or closer:
                    best_q = q_value
                    best_pair = pair
        assert best_pair is not None
        left_name, right_name = best_pair
        separation = dist[_pair_key(left_name, right_name)]
        if size == 2:
            limb_left = separation / 2
        else:
            limb_left = 0.5 * separation + (totals[left_name] - totals[right_name]) / (2 * (size - 2))
        limb_right = separation - limb_left
        left_node = next(node for node in nodes if node.name == left_name)
        right_node = next(node for node in nodes if node.name == right_name)
        counter += 1
        parent = PhyNode(
            name=f"n{counter}",
            leaves=left_node.leaves | right_node.leaves,
            left=left_node,
            right=right_node,
            left_length=limb_left,
            right_length=limb_right,
        )
        remaining = [node for node in nodes if node.name not in best_pair]
        new_dist: dict[tuple[str, str], float] = {}
        for i, node in enumerate(remaining):
            for other in remaining[i + 1 :]:
                new_dist[_pair_key(node.name, other.name)] = dist[_pair_key(node.name, other.name)]
            new_dist[_pair_key(parent.name, node.name)] = 0.5 * (
                dist[_pair_key(left_name, node.name)]
                + dist[_pair_key(right_name, node.name)]
                - separation
            )
        nodes = remaining + [parent]
        dist = new_dist
    if len(nodes) == 1:
        return nodes[0]
    left_node, right_node = nodes
    separation = dist[_pair_key(left_node.name, right_node.name)]
    return PhyNode(
        name="root",
        leaves=left_node.leaves | right_node.leaves,
        left=left_node,
        right=right_node,
        left_length=separation / 2,
        right_length=separation / 2,
    )


def _newick_child(node: PhyNode, length: float, support: dict[frozenset[str], float]) -> str:
    body = node.name if not node.internal else _newick_body(node, support)
    value = support.get(node.leaves)
    if node.internal and value is not None:
        return f"{body}{value:.3f}:{_round(length)}"
    return f"{body}:{_round(length)}"


def _newick_body(node: PhyNode, support: dict[frozenset[str], float]) -> str:
    assert node.left is not None and node.right is not None
    left = _newick_child(node.left, node.left_length, support)
    right = _newick_child(node.right, node.right_length, support)
    return f"({left},{right})"


def newick(node: PhyNode, support: dict[frozenset[str], float]) -> str:
    if not node.internal:
        return f"{node.name};"
    return _newick_body(node, support) + ";"


def bipartitions(node: PhyNode) -> list[frozenset[str]]:
    found: list[frozenset[str]] = []

    def walk(current: PhyNode) -> None:
        if not current.internal:
            return
        assert current.left is not None and current.right is not None
        for child in (current.left, current.right):
            if child.internal and len(child.leaves) < len(node.leaves):
                found.append(child.leaves)
            walk(child)

    walk(node)
    return found


def _map_side(
    columns: Sequence[AlignedColumn],
    tablet: str,
) -> dict[Pos, tuple[Pos | None, str | None, str | None]]:
    """Position on ``tablet`` → (other position or gap, own sign, other sign)."""
    mapped: dict[Pos, tuple[Pos | None, str | None, str | None]] = {}
    for column in columns:
        if column.tablet_a == tablet and column.pos_a is not None:
            mapped[column.pos_a] = (column.pos_b, column.sign_a, column.sign_b)
        elif column.tablet_b == tablet and column.pos_b is not None:
            mapped[column.pos_b] = (column.pos_a, column.sign_b, column.sign_a)
    return mapped


def _classify_site(record: dict[str, Any], patterns: Counter[str]) -> None:
    signs = {name: record[name] for name in GT_TABLETS}
    present = [name for name in GT_TABLETS if signs[name] is not None]
    if len(present) == 3:
        if signs["H"] == signs["P"] == signs["Q"]:
            patterns["all_agree"] += 1
        elif signs["H"] == signs["P"] != signs["Q"]:
            patterns["H_P_agree"] += 1
        elif signs["H"] == signs["Q"] != signs["P"]:
            patterns["H_Q_agree"] += 1
        elif signs["P"] == signs["Q"] != signs["H"]:
            patterns["P_Q_agree"] += 1
        else:
            patterns["all_differ"] += 1
    elif signs["H"] is not None and signs["P"] is not None and signs["Q"] is None:
        patterns["gap_Q"] += 1
    elif signs["H"] is not None and signs["Q"] is not None and signs["P"] is None:
        patterns["gap_P"] += 1
    elif signs["P"] is not None and signs["Q"] is not None and signs["H"] is None:
        patterns["gap_H"] += 1
    elif signs["H"] is not None and signs["P"] is None and signs["Q"] is None:
        patterns["only_H"] += 1
    elif signs["P"] is not None and signs["H"] is None and signs["Q"] is None:
        patterns["only_P"] += 1
    elif signs["Q"] is not None and signs["H"] is None and signs["P"] is None:
        patterns["only_Q"] += 1


def great_tradition(
    columns: Sequence[AlignedColumn],
    texts: dict[str, SideText],
) -> dict[str, Any]:
    """Columns where H, P, and Q meet without the pairwise alignments contradicting.

    A gap on H cannot be keyed from an H position, so those sites are read
    off the P–Q alignment and checked against the other two pairs.
    """
    by_pair: dict[tuple[str, str], list[AlignedColumn]] = defaultdict(list)
    for column in columns:
        key = _pair_key(column.tablet_a, column.tablet_b)
        if set(key) <= set(GT_TABLETS):
            by_pair[key].append(column)
    hp_from_h = _map_side(by_pair[_pair_key("H", "P")], "H")
    hp_from_p = _map_side(by_pair[_pair_key("H", "P")], "P")
    hq_from_h = _map_side(by_pair[_pair_key("H", "Q")], "H")
    hq_from_q = _map_side(by_pair[_pair_key("H", "Q")], "Q")
    pq_from_p = _map_side(by_pair[_pair_key("P", "Q")], "P")
    sites: list[dict[str, Any]] = []
    conflicts = 0
    patterns: Counter[str] = Counter()
    seen_p: set[Pos] = set()

    def add_site(h_pos: Pos | None, p_pos: Pos | None, q_pos: Pos | None, h_sign, p_sign, q_sign) -> None:
        if p_pos is not None:
            seen_p.add(p_pos)
        record = {
            "H": h_sign,
            "P": p_sign,
            "Q": q_sign,
            "H_locus": _locus(texts, h_pos),
            "P_locus": _locus(texts, p_pos),
            "Q_locus": _locus(texts, q_pos),
        }
        sites.append(record)
        _classify_site(record, patterns)

    for h_pos, (p_pos, h_sign, p_sign) in hp_from_h.items():
        if h_pos not in hq_from_h:
            continue
        q_pos, h_sign_again, q_sign = hq_from_h[h_pos]
        if h_sign != h_sign_again:
            conflicts += 1
            continue
        if p_pos is not None and q_pos is not None:
            if p_pos not in pq_from_p:
                continue
            q_from_p, p_again, q_again = pq_from_p[p_pos]
            if q_from_p != q_pos or p_again != p_sign or q_again != q_sign:
                conflicts += 1
                continue
        elif p_pos is not None and q_pos is None and p_pos in pq_from_p:
            q_from_p, p_again, _q_again = pq_from_p[p_pos]
            if q_from_p is not None or p_again != p_sign:
                conflicts += 1
                continue
        add_site(h_pos, p_pos, q_pos, h_sign, p_sign, q_sign)

    for p_pos, (q_pos, p_sign, q_sign) in pq_from_p.items():
        if p_pos in seen_p or p_pos not in hp_from_p:
            continue
        h_pos, p_again, h_sign = hp_from_p[p_pos]
        if p_again != p_sign:
            conflicts += 1
            continue
        if h_pos is not None:
            continue
        if q_pos is None:
            add_site(None, p_pos, None, None, p_sign, None)
            continue
        if q_pos not in hq_from_q:
            continue
        h_from_q, q_again, h_from_q_sign = hq_from_q[q_pos]
        if q_again != q_sign or h_from_q is not None or h_from_q_sign is not None:
            conflicts += 1
            continue
        add_site(None, p_pos, q_pos, None, p_sign, q_sign)

    return {
        "sites": sites,
        "conflicts": conflicts,
        "patterns": patterns,
        "pairwise_columns": {
            f"{a}–{b}": len(by_pair[(a, b)]) for a, b in (("H", "P"), ("H", "Q"), ("P", "Q"))
        },
    }


def _exclusive_winner(patterns: Counter[str]) -> str:
    scores = {
        "H–P": patterns["H_P_agree"],
        "H–Q": patterns["H_Q_agree"],
        "P–Q": patterns["P_Q_agree"],
    }
    best = max(scores.values()) if scores else 0
    winners = [name for name, score in scores.items() if score == best]
    if best == 0 or len(winners) != 1:
        return "unresolved"
    return winners[0]


def column_bootstrap(sites: Sequence[dict[str, Any]], replicates: int, seed: int) -> dict[str, Any]:
    """Resample triple-alignment columns. Sites are not independent inside a passage."""
    generator = random.Random(seed)
    votes: Counter[str] = Counter()
    if not sites:
        return {"replicates": replicates, "votes": {}, "support": {}}
    for _trial in range(replicates):
        patterns: Counter[str] = Counter()
        for _draw in range(len(sites)):
            site = sites[generator.randrange(len(sites))]
            if site["H"] is None or site["P"] is None or site["Q"] is None:
                continue
            if site["H"] == site["P"] == site["Q"]:
                continue
            if site["H"] == site["P"] != site["Q"]:
                patterns["H_P_agree"] += 1
            elif site["H"] == site["Q"] != site["P"]:
                patterns["H_Q_agree"] += 1
            elif site["P"] == site["Q"] != site["H"]:
                patterns["P_Q_agree"] += 1
        votes[_exclusive_winner(patterns)] += 1
    support = {name: _round(count / replicates, 4) for name, count in sorted(votes.items())}
    return {"replicates": replicates, "seed": seed, "votes": dict(votes), "support": support}


def connected_groups(
    labels: Sequence[str],
    observed: dict[tuple[str, str], float],
) -> list[tuple[str, ...]]:
    """Tablets joined by a direct passage. Separate texts stay separate."""
    parent = {label: label for label in labels}

    def find(label: str) -> str:
        while parent[label] != label:
            parent[label] = parent[parent[label]]
            label = parent[label]
        return label

    for left, right in observed:
        if left not in parent or right not in parent:
            continue
        root_left = find(left)
        root_right = find(right)
        if root_left != root_right:
            parent[root_right] = root_left
    groups: dict[str, list[str]] = defaultdict(list)
    for label in labels:
        groups[find(label)].append(label)
    return sorted(
        (tuple(sorted(group)) for group in groups.values() if len(group) >= 2),
        key=lambda group: group,
    )


def build_forest(
    labels: Sequence[str],
    observed: dict[tuple[str, str], float],
) -> tuple[list[PhyNode], list[tuple[str, str]], dict[tuple[str, str], float]]:
    """One neighbor-joining tree per connected group.

    A missing distance is filled only inside a group that is already connected
    by other passages. Two groups that share no passage are not glued together.
    The third return is the filled distance of every pair inside those groups.
    """
    trees: list[PhyNode] = []
    imputed: list[tuple[str, str]] = []
    filled_all: dict[tuple[str, str], float] = {}
    for group in connected_groups(labels, observed):
        subset = {key: distance for key, distance in observed.items() if set(key) <= set(group)}
        filled, missing = complete_matrix(group, subset)
        imputed.extend(missing)
        filled_all.update(filled)
        trees.append(neighbor_joining(group, filled))
    return trees, imputed, filled_all


def passage_bootstrap_closest(
    passages: Sequence[Passage],
    labels: Sequence[str],
    replicates: int,
    seed: int,
) -> dict[str, Any]:
    """Which Great Tradition pair is closest when passages are resampled."""
    generator = random.Random(seed)
    votes: Counter[str] = Counter()
    bipartition_hits: Counter[frozenset[str]] = Counter()
    gt = set(GT_TABLETS)
    for _trial in range(replicates):
        drawn = [passages[generator.randrange(len(passages))] for _index in range(len(passages))]
        stats = pairwise_from_passages(drawn)
        observed = {
            key: distance
            for key, bucket in stats.items()
            if (distance := p_distance(bucket)) is not None and set(key) <= set(labels)
        }
        # Keep a GT pair only when the replicate actually drew a passage for it.
        # The closeness vote uses every drawn column. The tree does not: a pair
        # joins two tablets only when the replicate still has enough columns.
        gt_observed = {key: distance for key, distance in observed.items() if set(key) <= gt}
        tree_observed = {
            key: distance
            for key, bucket in stats.items()
            if bucket["columns"] >= TREE_MIN_COLUMNS
            and (distance := p_distance(bucket)) is not None
            and set(key) <= set(labels)
        }
        if len(gt_observed) < 3:
            votes["missing"] += 1
        else:
            votes[closest_pair(GT_TABLETS, gt_observed)] += 1
        for tree in build_forest(labels, tree_observed)[0]:
            for split in bipartitions(tree):
                bipartition_hits[split] += 1
    support = {
        name: _round(count / replicates, 4)
        for name, count in sorted(votes.items())
        if name != "missing"
    }
    return {
        "replicates": replicates,
        "seed": seed,
        "votes": dict(votes),
        "support_closest_pair": support,
        "replicates_missing_a_gt_pair": votes["missing"],
        "bipartition_hits": bipartition_hits,
    }


def _rank(values: Sequence[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda index: values[index])
    ranks = [0.0] * len(values)
    cursor = 0
    while cursor < len(order):
        end = cursor
        while end + 1 < len(order) and values[order[end + 1]] == values[order[cursor]]:
            end += 1
        average = (cursor + end) / 2 + 1
        for index in order[cursor : end + 1]:
            ranks[index] = average
        cursor = end + 1
    return ranks


def spearman(xs: Sequence[float], ys: Sequence[float]) -> float | None:
    if len(xs) != len(ys) or len(xs) < 2:
        return None
    rx = _rank(xs)
    ry = _rank(ys)
    mean_x = sum(rx) / len(rx)
    mean_y = sum(ry) / len(ry)
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(rx, ry))
    den_x = sum((x - mean_x) ** 2 for x in rx) ** 0.5
    den_y = sum((y - mean_y) ** 2 for y in ry) ** 0.5
    if den_x == 0 or den_y == 0:
        return None
    return num / (den_x * den_y)


def permutation_p_negative(xs: Sequence[float], ys: Sequence[float]) -> float | None:
    """Exact one-sided p for a pre-specified negative Spearman. n is 3."""
    observed = spearman(xs, ys)
    if observed is None:
        return None
    size = len(ys)
    hits = 0
    total = 0
    # n=3 is the designed comparison. A larger n still uses all permutations
    # only while 7! stays cheap; here the call sites are size 3.
    from itertools import permutations

    for perm in permutations(ys):
        total += 1
        value = spearman(xs, perm)
        if value is not None and value <= observed + 1e-12:
            hits += 1
    if total == 0:
        return None
    return hits / total


def rarefied_types(counts: Counter[str], k: int) -> float | None:
    population = sum(counts.values())
    if k <= 0 or population < k:
        return None
    if population == k:
        return float(len(counts))
    denominator = comb(population, k)
    expected = 0.0
    for count in counts.values():
        remaining = population - count
        if remaining < k:
            expected += 1.0
        else:
            expected += 1.0 - comb(remaining, k) / denominator
    return expected


def _mark(marks: dict[str, tuple[StemMark, ...]], pos: Pos | None) -> StemMark | None:
    if pos is None:
        return None
    side, index = pos
    return marks[side][index]


def form_profile(
    texts: dict[str, SideText],
    marks: dict[str, tuple[StemMark, ...]],
) -> dict[str, dict[str, Any]]:
    profiles: dict[str, dict[str, Any]] = {}
    by_tablet: dict[str, list[StemMark]] = defaultdict(list)
    for side, text in texts.items():
        by_tablet[text.tablet].extend(marks[side])
    for tablet, rows in sorted(by_tablet.items()):
        stems = Counter()
        surfaces = Counter()
        # Stems are recovered from the side texts in the same order.
        stem_signs: list[str] = []
        for side, text in texts.items():
            if text.tablet == tablet:
                stem_signs.extend(text.signs)
        stems.update(stem_signs)
        surfaces.update(row.surface for row in rows)
        n = len(rows)
        profiles[tablet] = {
            "stems": n,
            "stem_types": len(stems),
            "surface_types": len(surfaces),
            "type_token": _round(len(stems) / n if n else None),
            "surface_type_token": _round(len(surfaces) / n if n else None),
            "ligature_rate": _round(sum(row.ligature for row in rows) / n if n else None),
            "mean_parts": _round(sum(row.parts for row in rows) / n if n else None),
            "modification_rate": _round(sum(row.modification for row in rows) / n if n else None),
            "pictorial_rate": _round(sum(row.pictorial for row in rows) / n if n else None),
            "rarefied_types_k80": _round(rarefied_types(stems, RAREFACTION_K)),
        }
    return profiles


def aligned_form_rates(
    columns: Sequence[AlignedColumn],
    marks: dict[str, tuple[StemMark, ...]],
    tablets: Sequence[str],
) -> dict[str, dict[str, Any]]:
    """Rates on stems that actually sit in a parallel column."""
    chosen: dict[str, dict[Pos, StemMark]] = {tablet: {} for tablet in tablets}
    for column in columns:
        pair = {column.tablet_a, column.tablet_b}
        if not pair <= set(tablets):
            continue
        for tablet, pos in ((column.tablet_a, column.pos_a), (column.tablet_b, column.pos_b)):
            if tablet not in chosen or pos is None or pos in chosen[tablet]:
                continue
            mark = _mark(marks, pos)
            if mark is not None:
                chosen[tablet][pos] = mark
    rates: dict[str, dict[str, Any]] = {}
    for tablet, row_map in chosen.items():
        rows = list(row_map.values())
        n = len(rows)
        rates[tablet] = {
            "aligned_stems": n,
            "ligature_rate": _round(sum(row.ligature for row in rows) / n if n else None),
            "modified_rate": _round(sum(row.modification for row in rows) / n if n else None),
            "pictorial_rate": _round(sum(row.pictorial for row in rows) / n if n else None),
            "mean_parts": _round(sum(row.parts for row in rows) / n if n else None),
        }
    return rates


def _rate_difference_bootstrap(
    columns: Sequence[AlignedColumn],
    marks: dict[str, tuple[StemMark, ...]],
    left: str,
    right: str,
    flag: str,
    replicates: int,
    seed: int,
) -> dict[str, Any]:
    paired: list[tuple[bool, bool]] = []
    for column in columns:
        if {column.tablet_a, column.tablet_b} != {left, right}:
            continue
        if column.pos_a is None or column.pos_b is None:
            continue
        mark_a = _mark(marks, column.pos_a)
        mark_b = _mark(marks, column.pos_b)
        if mark_a is None or mark_b is None:
            continue
        if column.tablet_a == left:
            paired.append((bool(getattr(mark_a, flag)), bool(getattr(mark_b, flag))))
        else:
            paired.append((bool(getattr(mark_b, flag)), bool(getattr(mark_a, flag))))
    if not paired:
        return {"columns": 0}
    left_rate = sum(item[0] for item in paired) / len(paired)
    right_rate = sum(item[1] for item in paired) / len(paired)
    generator = random.Random(seed)
    diffs: list[float] = []
    for _trial in range(replicates):
        draw = [paired[generator.randrange(len(paired))] for _index in range(len(paired))]
        diffs.append(
            sum(item[0] for item in draw) / len(draw) - sum(item[1] for item in draw) / len(draw)
        )
    diffs.sort()
    low = diffs[int(0.025 * (replicates - 1))]
    high = diffs[int(0.975 * (replicates - 1))]
    return {
        "columns": len(paired),
        "left": left,
        "right": right,
        "flag": flag,
        "left_rate": _round(left_rate),
        "right_rate": _round(right_rate),
        "difference_left_minus_right": _round(left_rate - right_rate),
        "bootstrap_replicates": replicates,
        "ci95": [_round(low), _round(high)],
        "ci_excludes_zero": low > 0 or high < 0,
    }


def load_systematic_pairs() -> list[dict[str, Any]]:
    payload = json.loads(SUBSTITUTION_JSON.read_text(encoding="utf-8"))
    rows = []
    for row in payload["stem"]["substitutions"]["pairs"]:
        if row["kind"] != "systematic":
            continue
        rows.append(
            {
                "a": row["a"],
                "b": row["b"],
                "count": row["count"],
                "corpus_note": "Track C systematic pair",
            }
        )
    frequencies = Counter()
    # Corpus counts live on the classes. Fall back to the pair order.
    for item in payload["stem"]["substitutions"]["classes"]:
        for sign, count in item["corpus_counts"].items():
            frequencies[sign] = count
    for row in rows:
        row["corpus_count_a"] = frequencies.get(row["a"])
        row["corpus_count_b"] = frequencies.get(row["b"])
        if frequencies[row["a"]] == frequencies[row["b"]]:
            row["commoner"] = None
        elif frequencies[row["a"]] > frequencies[row["b"]]:
            row["commoner"] = row["a"]
        else:
            row["commoner"] = row["b"]
    return rows


def binomial_two_sided(successes: int, trials: int) -> float | None:
    if trials <= 0:
        return None
    weights = [comb(trials, index) for index in range(trials + 1)]
    total = sum(weights)
    threshold = weights[successes]
    return sum(weight for weight in weights if weight <= threshold) / total


def substitution_direction(
    sites: Sequence[dict[str, Any]],
    columns: Sequence[AlignedColumn],
    pairs: Sequence[dict[str, Any]],
) -> dict[str, Any]:
    """Which member of a Track C pair sits on which witness.

    Direction is not taken from the majority vote alone. The majority vote
    would make the singleton's sign the innovation by definition. The test
    here counts, for each witness pair, which way the two signs face, and
    whether the witness that stands alone at a 2-against-1 site carries the
    rarer corpus form.
    """
    lookup = {frozenset((row["a"], row["b"])): row for row in pairs}
    pair_orientation: dict[str, Counter[str]] = defaultdict(Counter)
    for column in columns:
        if column.sign_a is None or column.sign_b is None or column.sign_a == column.sign_b:
            continue
        key = frozenset((column.sign_a, column.sign_b))
        if key not in lookup:
            continue
        label = f"{column.tablet_a}–{column.tablet_b}"
        pair_orientation[label][f"{column.tablet_a}:{column.sign_a}>{column.tablet_b}:{column.sign_b}"] += 1
    singleton_rarer = 0
    singleton_commoner = 0
    by_witness: Counter[str] = Counter()
    by_pair_and_witness: dict[str, Counter[str]] = defaultdict(Counter)
    examples: list[dict[str, Any]] = []
    for site in sites:
        if any(site[name] is None for name in GT_TABLETS):
            continue
        signs = {name: site[name] for name in GT_TABLETS}
        values = list(signs.values())
        if len(set(values)) == 1:
            continue
        counts = Counter(values)
        if counts.most_common(1)[0][1] != 2:
            continue
        majority = counts.most_common(1)[0][0]
        minority_name = next(name for name, sign in signs.items() if sign != majority)
        minority = signs[minority_name]
        key = frozenset((majority, minority))
        row = lookup.get(key)
        if row is None:
            continue
        commoner = row["commoner"]
        if commoner is None:
            continue
        if minority == commoner:
            singleton_commoner += 1
            kind = "singleton_has_commoner"
        else:
            singleton_rarer += 1
            kind = "singleton_has_rarer"
        by_witness[minority_name] += 1
        by_pair_and_witness[f"{row['a']}–{row['b']}"][f"{minority_name}:{minority}"] += 1
        if len(examples) < 12:
            examples.append(
                {
                    "pair": f"{row['a']}–{row['b']}",
                    "majority": majority,
                    "minority_witness": minority_name,
                    "minority_sign": minority,
                    "kind": kind,
                    "loci": {name: site[f"{name}_locus"] for name in GT_TABLETS},
                }
            )
    trials = singleton_rarer + singleton_commoner
    return {
        "hypothesis": (
            "HYPOTHESIS under test: a later copy levels variants toward the "
            "commoner corpus form, so the witness that stands alone should "
            "carry the commoner member of a Track C pair. The opposite count "
            "means the lone witness carries the rarer form."
        ),
        "singleton_has_rarer": singleton_rarer,
        "singleton_has_commoner": singleton_commoner,
        "binomial_p_two_sided": _round(binomial_two_sided(singleton_rarer, trials), 6),
        "lone_witness_counts": dict(by_witness),
        "by_pair": {key: dict(counter) for key, counter in sorted(by_pair_and_witness.items())},
        "pairwise_orientations": {
            key: dict(counter) for key, counter in sorted(pair_orientation.items())
        },
        "examples": examples,
    }


def _examples(sites: Sequence[dict[str, Any]], predicate, limit: int = 5) -> list[dict[str, Any]]:
    found = []
    for site in sites:
        if predicate(site):
            found.append(
                {
                    "H": site["H"],
                    "P": site["P"],
                    "Q": site["Q"],
                    "H_locus": site["H_locus"],
                    "P_locus": site["P_locus"],
                    "Q_locus": site["Q_locus"],
                }
            )
        if len(found) >= limit:
            break
    return found


def _gap_balance(columns: Sequence[AlignedColumn], left: str, right: str) -> dict[str, int]:
    extra = Counter()
    both = 0
    for column in columns:
        if {column.tablet_a, column.tablet_b} != {left, right}:
            continue
        if column.sign_a is None and column.sign_b is not None:
            extra[column.tablet_b] += 1
        elif column.sign_b is None and column.sign_a is not None:
            extra[column.tablet_a] += 1
        else:
            both += 1
    return {"extra_" + left: extra[left], "extra_" + right: extra[right], "aligned_both": both}


def run_round4_trackd(provider: MockProvider | None = None) -> dict[str, Any]:
    """Build the catalog, the copying tree, and the form test. No readings."""
    if provider is None:
        provider = MockProvider()
    if not isinstance(provider, MockProvider):
        raise TypeError("Round 4 Track D accepts MockProvider only")
    provider_calls = 0

    texts_tuple = load_side_texts("stem")
    texts = {text.side: text for text in texts_tuple}
    marks = annotate_corpus(texts)
    passages = find_passages(texts_tuple)
    columns = dedupe_columns(passages)
    stats = pairwise_from_columns(columns)
    observed = {
        key: distance
        for key, bucket in stats.items()
        if bucket["columns"] >= TREE_MIN_COLUMNS and (distance := p_distance(bucket)) is not None
    }
    tree_labels = tuple(sorted({label for pair in observed for label in pair}))
    trees, imputed, filled = build_forest(tree_labels, observed)
    gt_columns = [column for column in columns if {column.tablet_a, column.tablet_b} <= set(GT_TABLETS)]
    tradition = great_tradition(gt_columns, texts)
    sign_sites = [
        site
        for site in tradition["sites"]
        if site["H"] is not None and site["P"] is not None and site["Q"] is not None
    ]
    exclusive = _exclusive_winner(tradition["patterns"])
    col_boot = column_bootstrap(sign_sites, BOOTSTRAP_REPLICATES, COLUMN_BOOTSTRAP_SEED)
    pas_boot = passage_bootstrap_closest(
        passages, tree_labels, BOOTSTRAP_REPLICATES, PASSAGE_BOOTSTRAP_SEED
    )
    split_support = {
        frozenset(split): _round(count / BOOTSTRAP_REPLICATES, 4)
        for split, count in pas_boot["bipartition_hits"].items()
    }
    point_splits = [split for tree in trees for split in bipartitions(tree)]
    point_support = {split: split_support.get(split, 0.0) for split in point_splits}
    newicks = [newick(tree, point_support) for tree in trees]
    gt_direct = {
        f"{a}–{b}": {
            "p_distance": _round(p_distance(stats[_pair_key(a, b)])),
            **{name: stats[_pair_key(a, b)][name] for name in ("columns", "differences", "gaps", "mismatches")},
        }
        for a, b in (("H", "P"), ("H", "Q"), ("P", "Q"))
    }
    distance_winner = closest_pair(
        GT_TABLETS,
        {_pair_key(a, b): p_distance(stats[_pair_key(a, b)]) or 1.0 for a, b in (("H", "P"), ("H", "Q"), ("P", "Q"))},
    )
    profiles = form_profile(texts, marks)
    aligned_rates = aligned_form_rates(gt_columns, marks, GT_TABLETS)
    # Derivedness under the majority hypothesis: share of 2-against-1 sites
    # where this witness is the one that disagrees. Pre-specified as the
    # copying-direction score. It is not an independent date.
    singleton = Counter()
    comparable = 0
    for site in sign_sites:
        signs = [site[name] for name in GT_TABLETS]
        if len(set(signs)) == 1:
            continue
        counts = Counter(signs)
        if counts.most_common(1)[0][1] != 2:
            continue
        majority = counts.most_common(1)[0][0]
        lone = next(name for name in GT_TABLETS if site[name] != majority)
        singleton[lone] += 1
        comparable += 1
    derived = {
        name: _round(singleton[name] / comparable if comparable else None) for name in GT_TABLETS
    }
    ligature_values = [aligned_rates[name]["ligature_rate"] or 0.0 for name in GT_TABLETS]
    pictorial_values = [aligned_rates[name]["pictorial_rate"] or 0.0 for name in GT_TABLETS]
    modified_values = [aligned_rates[name]["modified_rate"] or 0.0 for name in GT_TABLETS]
    derived_values = [derived[name] or 0.0 for name in GT_TABLETS]
    pairs = load_systematic_pairs()
    direction = substitution_direction(tradition["sites"], columns, pairs)
    gk_columns = [column for column in columns if {column.tablet_a, column.tablet_b} == {"G", "K"}]
    form_tests = {
        "prediction": (
            "HYPOTHESIS: the witness with more unique variants (higher derivedness) "
            "has the lower ligature rate, the lower pictorial rate, and the lower "
            "modification rate inside the shared passages. One-sided exact "
            "permutation p on three witnesses."
        ),
        "derivedness_singleton_rate": derived,
        "singleton_counts": dict(singleton),
        "comparable_sites": comparable,
        "aligned_rates": aligned_rates,
        "spearman_derived_vs_ligature": _round(spearman(derived_values, ligature_values)),
        "p_ligature": _round(permutation_p_negative(derived_values, ligature_values)),
        "spearman_derived_vs_pictorial": _round(spearman(derived_values, pictorial_values)),
        "p_pictorial": _round(permutation_p_negative(derived_values, pictorial_values)),
        "spearman_derived_vs_modification": _round(spearman(derived_values, modified_values)),
        "p_modification": _round(permutation_p_negative(derived_values, modified_values)),
        "gk_ligature": _rate_difference_bootstrap(
            gk_columns, marks, "G", "K", "ligature", BOOTSTRAP_REPLICATES, FORM_BOOTSTRAP_SEED
        ),
        "gk_pictorial": _rate_difference_bootstrap(
            gk_columns, marks, "G", "K", "pictorial", BOOTSTRAP_REPLICATES, FORM_BOOTSTRAP_SEED + 1
        ),
        "hp_ligature": _rate_difference_bootstrap(
            gt_columns, marks, "H", "P", "ligature", BOOTSTRAP_REPLICATES, FORM_BOOTSTRAP_SEED + 2
        ),
        "hq_ligature": _rate_difference_bootstrap(
            gt_columns, marks, "H", "Q", "ligature", BOOTSTRAP_REPLICATES, FORM_BOOTSTRAP_SEED + 3
        ),
        "pq_ligature": _rate_difference_bootstrap(
            gt_columns, marks, "P", "Q", "ligature", BOOTSTRAP_REPLICATES, FORM_BOOTSTRAP_SEED + 4
        ),
    }
    distance_rows = []
    for key in sorted(stats):
        bucket = stats[key]
        distance_rows.append(
            {
                "a": key[0],
                "b": key[1],
                "columns": bucket["columns"],
                "differences": bucket["differences"],
                "gaps": bucket["gaps"],
                "mismatches": bucket["mismatches"],
                "p_distance": _round(p_distance(bucket)),
                "in_tree": key in observed,
                "imputed": False,
            }
        )
    for key in imputed:
        distance_rows.append(
            {
                "a": key[0],
                "b": key[1],
                "columns": 0,
                "p_distance": _round(filled[key]),
                "in_tree": True,
                "imputed": True,
            }
        )
    catalog = []
    for row in _CATALOG_ROWS:
        item = dict(row)
        item["whole_text_forms"] = profiles.get(row["code"])
        catalog.append(item)
    result = {
        "track": "round4_trackD",
        "provider": "MockProvider",
        "provider_calls": provider_calls,
        "readings_assigned": False,
        "passage_source": (
            "Round 2 Track C gated passages recomputed with find_passages. "
            "Track C's shuffle null peaked at 0, so every gated passage is "
            "the significant set of 99. Columns are not stored in "
            "substitution_classes.json and are rebuilt here."
        ),
        "passages": len(passages),
        "deduped_columns": len(columns),
        "tree_min_columns": TREE_MIN_COLUMNS,
        "tree_labels": list(tree_labels),
        "catalog": catalog,
        "whole_text_forms": profiles,
        "distances": distance_rows,
        "great_tradition": {
            "distance_closest_pair": distance_winner,
            "distance_bootstrap_support": pas_boot["support_closest_pair"],
            "distance_bootstrap_votes": pas_boot["votes"],
            "pairwise": gt_direct,
            "triple_sites": len(tradition["sites"]),
            "triple_sign_sites": len(sign_sites),
            "alignment_conflicts": tradition["conflicts"],
            "patterns": dict(tradition["patterns"]),
            "exclusive_agreement_closest": exclusive,
            "column_bootstrap_support": col_boot["support"],
            "column_bootstrap_votes": col_boot["votes"],
            "examples": {
                "H_P_agree": _examples(
                    sign_sites, lambda site: site["H"] == site["P"] != site["Q"]
                ),
                "H_Q_agree": _examples(
                    sign_sites, lambda site: site["H"] == site["Q"] != site["P"]
                ),
                "P_Q_agree": _examples(
                    sign_sites, lambda site: site["P"] == site["Q"] != site["H"]
                ),
                "gap_Q": _examples(
                    tradition["sites"],
                    lambda site: site["Q"] is None and site["H"] is not None and site["P"] is not None,
                ),
                "gap_P": _examples(
                    tradition["sites"],
                    lambda site: site["P"] is None and site["H"] is not None and site["Q"] is not None,
                ),
                "gap_H": _examples(
                    tradition["sites"],
                    lambda site: site["H"] is None and site["P"] is not None and site["Q"] is not None,
                ),
            },
            "published_reference_hypotheses": {
                "davletshin_2017_P_as_reference": DAVLETSHIN_2017,
            "P_singleton_rate": derived["P"],
            "singleton_counts": {name: singleton[name] for name in GT_TABLETS},
            "lowest_singleton": [
                name
                for name in GT_TABLETS
                if singleton[name] == min(singleton[name] for name in GT_TABLETS)
            ],
            },
        },
        "stemma": {
            "method": (
                "Neighbor-joining (Saitou and Nei 1987) on p-distances. "
                "A difference is a mismatch or a gap. Overlapping passages of "
                "one tablet pair contribute a column once, from the higher-scoring "
                "passage. The same stem may still be compared with a second tablet. "
                f"A pair is drawn only when it has at least {TREE_MIN_COLUMNS} "
                "aligned columns. Shorter parallels are reported and do not connect "
                "tablets. Tablets that share no such pair, even through a chain, "
                "stay in separate trees. Inside one connected group, a pair with no "
                "direct passage is filled by the shortest path and marked imputed. "
                "Bootstrap (Felsenstein 1985): passages drawn with replacement, "
                f"{BOOTSTRAP_REPLICATES} replicates, seed {PASSAGE_BOOTSTRAP_SEED}. "
                "The closest-pair vote uses every drawn Great Tradition column. "
                "A branch is counted only when the replicate still has at least "
                f"{TREE_MIN_COLUMNS} columns on the pairs that define it. "
                "Support is the fraction of replicates that contain that set of "
                "tablets on one side of an edge."
            ),
            "newick": " ".join(newicks),
            "newicks": newicks,
            "bipartitions": [
                {
                    "tablets": sorted(split),
                    "support": point_support[split],
                }
                for split in point_splits
            ],
            "imputed_pairs": [list(key) for key in imputed],
            "gk_gaps": _gap_balance(columns, "G", "K"),
            "hp_gaps": _gap_balance(gt_columns, "H", "P"),
            "hq_gaps": _gap_balance(gt_columns, "H", "Q"),
            "pq_gaps": _gap_balance(gt_columns, "P", "Q"),
        },
        "form_test": form_tests,
        "substitution_direction": direction,
        "systematic_pairs": pairs,
        "sources": [
            FERRARA_2024,
            ORLIAC_2005,
            ORLIAC_2007,
            ORLIAC_2010,
            WIECZOREK_2021,
            FISCHER_1997,
            HORLEY_2007,
            DAVLETSHIN_2017,
            "Saitou and Nei 1987, Molecular Biology and Evolution 4:406–425.",
            "Felsenstein 1985, Evolution 39:783–791.",
            "Sproat 2003, as cited in Round 2 Track C, for the 125-sign H/Q match this tree is built on.",
            "Pozdniakov 1996, Journal de la Société des Océanistes 103:289–303, the parallel-text study Track C cites.",
            "Kudrjavtsev 1949, as cited by Track C via Barthel 1958 and Davletshin 2017, for the H/P/Q collation.",
            KOHAUMOTU_TABLE,
            SECONDARY_CORPUS,
        ],
    }
    return result


def _pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{100 * value:.1f}%"


def _brief(text: str, limit: int = 280) -> str:
    flat = " ".join(text.split()).replace("|", "/")
    if len(flat) <= limit:
        return flat
    return flat[: limit - 1].rsplit(" ", 1)[0] + "…"


def _support_phrase(support: dict[str, Any], key: str) -> str:
    value = support.get(key)
    if value is None:
        return "not observed"
    return f"{100 * value:.1f}%"


def render_markdown(result: dict[str, Any]) -> str:
    gt = result["great_tradition"]
    stemma = result["stemma"]
    forms = result["form_test"]
    direction = result["substitution_direction"]
    lines: list[str] = []
    add = lines.append
    add("# Round 4, Track D — Dating the tablets and the copying tree")
    add("")
    add(
        "This note asks two questions. How old is the wood of each inscribed object, "
        "and which copies of the Great Tradition look like they were taken from which? "
        "It does not read a single sign. The provider is MockProvider and is never asked "
        f"for a completion. Provider calls: {result['provider_calls']}."
    )
    add("")
    distance_support = gt["distance_bootstrap_support"].get(gt["distance_closest_pair"])
    agreement_support = gt["column_bootstrap_support"].get(gt["exclusive_agreement_closest"])
    add(
        f"On the shared passages, the closest pair is {gt['distance_closest_pair']} "
        f"(passage bootstrap {_pct(distance_support)} of {BOOTSTRAP_REPLICATES} replicates). "
        f"Where all three of H, P, and Q have a sign, the pair that shares the most "
        f"sign numbers against the third is {gt['exclusive_agreement_closest']} "
        f"(column bootstrap {_pct(agreement_support)}). "
        "Three witnesses do not make a rooted tree by themselves. The percentages "
        "say which two copies sit nearer each other. They do not name a scribe, "
        "and they do not assign a sound to a sign."
    )
    add("")
    add(
        f"The copying tree uses the {result['passages']} significant parallel passages "
        "from Round 2 Track C. Those passages were found again with the same search, "
        "because the published JSON does not keep the alignment columns. "
        "Inside one pair of tablets, a stem is counted once, from the higher-scoring "
        "passage. The same stem may still be compared with a second tablet, which "
        f"is what lets H, P, and Q be scored together. {result['deduped_columns']} "
        "columns remain."
    )
    add("")
    add("## What is known about each object")
    add("")
    add(
        "Wood and radiocarbon facts are copied from the papers named in the JSON citation fields. "
        "Where a detail comes only from the public corpus survey, the cell says so. "
        "A blank date means those papers do not date that object. "
        "A radiocarbon age dates the wood. Ferrara et al. 2024 and Wieczorek et al. 2021 "
        "both say the carving can be later than the tree was cut. It cannot be earlier."
    )
    add("")
    add("| Code | Name | Wood | Date of the wood | Condition and place | Carving evidence |")
    add("| --- | --- | --- | --- | --- | --- |")
    for row in result["catalog"]:
        add(
            f"| {row['code']} | {row['name']} | {_brief(row['wood'])} | "
            f"{_brief(row['radiocarbon'] or 'Not dated in the sources read for this track.')} | "
            f"{_brief(row['condition'] + ' ' + row['provenance'])} | {_brief(row['carving'])} |"
        )
    add("")
    add(
        "The JSON file keeps the full wording and the citation on each field. "
        "The table above is the same text, shortened so it can be read."
    )
    add("")
    add(
        "The early date is tablet D, Échancrée: 474±13 BP, 1493–1509 cal AD at 68.3% "
        "after Ferrara et al. add 50±5 years to reach the outer rings (their Table 2). "
        "D does not share a significant passage with H, P, or Q in Track C, so that "
        "fifteenth-century wood date does not date the Great Tradition. "
        "Q, the Small St. Petersburg witness of the same tradition, is the tablet "
        "Orliac dated to 80±40 BP. The ranges that survive collection in 1871 fall "
        "in the late seventeenth or the nineteenth century; Ferrara et al., citing "
        "Horley 2021, call 1812–1836 the most reliable slice. "
        "O, the Berlin tablet, is Thespesia and most probably nineteenth century "
        "(Wieczorek et al. 2021). A, B, and C in Rome are also young boards on the "
        "dates Ferrara et al. are willing to keep, with C the one that still has a "
        "large late-seventeenth-century slice."
    )
    add("")
    add(
        "Orliac 2007's idea that D, N, P, and S were cut from one Podocarpus board "
        "is a hypothesis. It is not a radiocarbon date for P. If it were true, P's "
        "wood could be old while Q's rosewood is young. This track does not adopt it."
    )
    add("")
    add("## How the copying tree was built")
    add("")
    add(
        "A passage is a local alignment, so the distance between two tablets is the "
        "share of aligned columns that differ, counting a gap as a difference. "
        "Only the shared text is compared. A pair is drawn on the tree only when "
        f"it has at least {result['tree_min_columns']} aligned columns. Shorter "
        "parallels are listed below and do not connect tablets. Connecting them "
        "would let a few columns glue separate texts, and the shortest-path fill "
        "would then invent a distance between texts that were never aligned. "
        f"The tablets in the tree are {', '.join(result['tree_labels'])}."
    )
    add("")
    add(
        "With only three witnesses the unrooted tree is a single fork. What can be "
        "measured is which two are closer. Neighbor-joining (Saitou and Nei 1987) "
        "places the longer set of tablets around that fork. Each branch's support "
        "is a bootstrap (Felsenstein 1985): the 99 passages are drawn with "
        f"replacement {BOOTSTRAP_REPLICATES} times, the tree is rebuilt, and the "
        "percentage is how often the same group sat on one side of a branch. "
        "Columns inside one passage are not independent, so the passage is the "
        "thing that is resampled."
    )
    add("")
    add("### Distances inside the Great Tradition")
    add("")
    add("| Pair | Columns | Differences | Gaps | Mismatches | p-distance |")
    add("| --- | ---: | ---: | ---: | ---: | ---: |")
    for label, row in gt["pairwise"].items():
        add(
            f"| {label} | {row['columns']} | {row['differences']} | {row['gaps']} | "
            f"{row['mismatches']} | {row['p_distance']} |"
        )
    add("")
    add(
        f"Closest pair by distance: **{gt['distance_closest_pair']}**. "
        "Passage-bootstrap support for which pair is closest: "
        + ", ".join(
            f"{name} {_support_phrase(gt['distance_bootstrap_support'], name)}"
            for name in ("H–P", "H–Q", "P–Q", "unresolved")
            if name in gt["distance_bootstrap_support"] or name == gt["distance_closest_pair"]
        )
        + "."
    )
    add("")
    add("### Shared variants where all three texts are aligned")
    add("")
    add(
        f"Triple sites, including gaps: {gt['triple_sites']}. "
        f"Sites where all three have a sign: {gt['triple_sign_sites']}. "
        f"Places where the three pairwise alignments contradict one another "
        f"and were left out: {gt['alignment_conflicts']}."
    )
    add("")
    patterns = gt["patterns"]
    add(
        f"All three agree: {patterns.get('all_agree', 0)}. "
        f"H and P agree against Q: {patterns.get('H_P_agree', 0)}. "
        f"H and Q agree against P: {patterns.get('H_Q_agree', 0)}. "
        f"P and Q agree against H: {patterns.get('P_Q_agree', 0)}. "
        f"All three differ: {patterns.get('all_differ', 0)}."
    )
    add("")
    add(
        f"The pair that shares the most of those exclusive agreements is "
        f"**{gt['exclusive_agreement_closest']}**. "
        "Column bootstrap, which resamples sites and is less conservative than "
        "the passage bootstrap: "
        + ", ".join(
            f"{name} {_support_phrase(gt['column_bootstrap_support'], name)}"
            for name in sorted(gt["column_bootstrap_support"])
        )
        + "."
    )
    add("")
    add(
        "Gaps in that same triple alignment. A gap counts only where an alignment "
        "covers the spot. A tablet that simply has no parallel there is not scored as a deletion."
    )
    add("")
    add(
        f"Sign in H and P, gap in Q: {patterns.get('gap_Q', 0)}. "
        f"Sign in H and Q, gap in P: {patterns.get('gap_P', 0)}. "
        f"Sign in P and Q, gap in H: {patterns.get('gap_H', 0)}. "
        f"Sign only in H: {patterns.get('only_H', 0)}. "
        f"Sign only in P: {patterns.get('only_P', 0)}. "
        f"Sign only in Q: {patterns.get('only_Q', 0)}."
    )
    add("")
    add(
        "Shared gaps are the classical shared-error clue, on the hypothesis that "
        "two scribes are unlikely to omit the same sign unless one copied the other "
        "or both copied a text that already lacked it. That hypothesis is not proved here."
    )
    add("")
    add("### The trees")
    add("")
    add(
        "Each block below is one connected group. A group that shares no passage "
        "with another is not tied to it by a made-up distance."
    )
    add("")
    add("```")
    add(stemma["newick"])
    add("```")
    add("")
    add("Support on each internal group:")
    add("")
    add("| Group | Bootstrap support |")
    add("| --- | ---: |")
    for row in stemma["bipartitions"]:
        add(f"| {', '.join(row['tablets'])} | {_pct(row['support'])} |")
    add("")
    if stemma["imputed_pairs"]:
        rendered = ", ".join(f"{a}–{b}" for a, b in stemma["imputed_pairs"])
        add(
            "Some pairs in the tree never share a passage. Their distance is the "
            f"shortest path through pairs that do. Imputed pairs: {rendered}."
        )
        add("")
    add(
        "G and K are a second text, not the Great Tradition. Horley 2007 treats K "
        "as a copy of G recto. In the deduplicated G–K columns, extra signs sit "
        f"{stemma['gk_gaps'].get('extra_G', 0)} times on G and "
        f"{stemma['gk_gaps'].get('extra_K', 0)} times on K "
        f"({stemma['gk_gaps'].get('aligned_both', 0)} columns have a sign on both). "
        "More extra signs means that copy is longer in the alignment, not that it is the original."
    )
    add("")
    ref = gt["published_reference_hypotheses"]
    counts = ref["singleton_counts"]
    least = ", ".join(ref["lowest_singleton"])
    add(
        "Davletshin 2017 uses P as the reference copy against H and Q. "
        "Under the hypothesis that the lone sign at a 2-against-1 site is the "
        f"innovation, the lone counts are H {counts['H']}, P {counts['P']}, "
        f"Q {counts['Q']} "
        f"(P's share {_pct(ref['P_singleton_rate'])}). "
        f"The witness or witnesses that stand alone least often: {least}. "
        "P stands alone most often, so this count does not support treating P "
        "as the least changed copy. The margin is modest, and it is a count of "
        "sign numbers, not a reading or a date."
    )
    short = [
        row
        for row in result["distances"]
        if row["columns"] > 0 and not row["in_tree"] and not row["imputed"]
    ]
    if short:
        add("")
        add(
            "Parallels below the column cutoff. They are real Track C matches. "
            "They are too short to place a tablet on the tree."
        )
        add("")
        add("| Pair | Columns | Differences | p-distance |")
        add("| --- | ---: | ---: | ---: |")
        for row in sorted(short, key=lambda item: (-item["columns"], item["a"], item["b"])):
            add(
                f"| {row['a']}–{row['b']} | {row['columns']} | {row['differences']} | "
                f"{row['p_distance']} |"
            )
    add("")
    add("## Do later copies simplify the signs?")
    add("")
    add(
        "The prediction, stated before looking at the ranks, is that the witness "
        "with more unique variants will use fewer ligatures, fewer Barthel "
        "modification letters, and fewer headed signs inside the shared passages. "
        "A ligature is a Kohaumotu token that contains `.` or `:` and splits into "
        "more than one stem. A headed sign is Barthel's hundreds digit 2–7 "
        "(figures with ears, open mouths, beaks, fish, and the like), as the "
        "public corpus survey describes his catalog. Hundreds 0–1 stay in the "
        "other bin. This is a hypothesis about graphic variety, not a decipherment."
    )
    add("")
    add("| Witness | Lone-reading rate | Ligature rate in the parallels | Headed-sign rate | Modification rate |")
    add("| --- | ---: | ---: | ---: | ---: |")
    for name in GT_TABLETS:
        rate = forms["aligned_rates"][name]
        add(
            f"| {name} | {_pct(forms['derivedness_singleton_rate'][name])} | "
            f"{_pct(rate['ligature_rate'])} | {_pct(rate['pictorial_rate'])} | "
            f"{_pct(rate['modified_rate'])} |"
        )
    add("")
    add(
        f"Spearman of lone-reading rate against ligature rate: "
        f"{forms['spearman_derived_vs_ligature']} "
        f"(one-sided permutation p {forms['p_ligature']}). "
        f"Against headed signs: {forms['spearman_derived_vs_pictorial']} "
        f"(p {forms['p_pictorial']}). "
        f"Against modification letters: {forms['spearman_derived_vs_modification']} "
        f"(p {forms['p_modification']}). "
        "With three witnesses there are only six possible rank orders, so a "
        "perfect negative correlation still has p = 1/6. A non-negative "
        "correlation means this prediction fails."
    )
    add("")
    lig_rho = forms["spearman_derived_vs_ligature"]
    if lig_rho is not None and lig_rho >= 0:
        add(
            "Ligatures do not simplify in the witness with more lone readings. "
            "That part of the prediction fails."
        )
        add("")
    pic_rho = forms["spearman_derived_vs_pictorial"]
    if pic_rho is not None and pic_rho < 0:
        add(
            f"Headed signs move the predicted way (Spearman {pic_rho}), "
            f"and the permutation p is {forms['p_pictorial']}. "
            "With three witnesses that is not enough to say later copies drop pictorial signs."
        )
        add("")
    mod_rho = forms["spearman_derived_vs_modification"]
    if mod_rho is not None and mod_rho >= 0:
        add("Modification letters show no downward trend with lone readings.")
        add("")
    pair_cis = []
    for key, label in (("hp_ligature", "H–P"), ("hq_ligature", "H–Q"), ("pq_ligature", "P–Q")):
        row = forms[key]
        if not row.get("ci_excludes_zero"):
            pair_cis.append(label)
    if pair_cis:
        add(
            "The 95% intervals on the ligature difference include zero for "
            + ", ".join(pair_cis)
            + ". No Great Tradition pair is reliably simpler on ligatures inside the shared text."
        )
        add("")
    gk = forms["gk_ligature"]
    add(
        f"On the G–K parallel itself, ligature rate is {_pct(gk.get('left_rate'))} on G and "
        f"{_pct(gk.get('right_rate'))} on K "
        f"(difference G minus K {gk.get('difference_left_minus_right')}, "
        f"95% bootstrap interval {gk.get('ci95')}, "
        f"{gk.get('columns')} columns with a sign on both sides). "
        "Horley's copying hypothesis predicts that K, if it is the copy, should "
        "be the simpler one. "
        + (
            "The interval contains zero, so this alignment does not show K as simpler."
            if not gk.get("ci_excludes_zero")
            else "The interval excludes zero."
        )
    )
    add("")
    add("Whole-tablet rates, for the catalog only. Different texts are mixed together, so these are not the copying test.")
    add("")
    add("| Tablet | Stems | Stem types | Type/token | Ligature rate | Headed-sign rate | Rarefied types at 80 stems |")
    add("| --- | ---: | ---: | ---: | ---: | ---: | ---: |")
    for code, profile in result["whole_text_forms"].items():
        if profile is None:
            continue
        add(
            f"| {code} | {profile['stems']} | {profile['stem_types']} | {profile['type_token']} | "
            f"{_pct(profile['ligature_rate'])} | {_pct(profile['pictorial_rate'])} | "
            f"{profile['rarefied_types_k80']} |"
        )
    add("")
    add("## Which way do the substitution pairs face?")
    add("")
    add(
        "Track C's systematic pairs are the substitutions that repeat more often "
        "than a mismatch shuffle. This track does not add pairs and does not merge "
        "anything new. For each pair, the question is whether one member prefers "
        "one witness."
    )
    add("")
    add(
        f"At 2-against-1 sites that use one of those pairs, the lone witness has "
        f"the rarer corpus form {direction['singleton_has_rarer']} times and the "
        f"commoner form {direction['singleton_has_commoner']} times "
        f"(two-sided exact binomial p {direction['binomial_p_two_sided']}). "
        "The prediction under test was that a later copy would level toward the "
        "commoner form. Lone readings by witness: "
        + ", ".join(f"{name} {count}" for name, count in sorted(direction["lone_witness_counts"].items()))
        + "."
    )
    add("")
    if direction["by_pair"]:
        add("| Pair | Lone witness and the sign it carries |")
        add("| --- | --- |")
        for pair, counts in direction["by_pair"].items():
            rendered = ", ".join(f"{name} ({count})" for name, count in sorted(counts.items()))
            add(f"| {pair} | {rendered} |")
        add("")
    if direction["pairwise_orientations"]:
        add(
            "The same pairs in the ordinary two-tablet alignments, without waiting "
            "for a third copy. The arrow is only which sign sat on which tablet."
        )
        add("")
        add("| Tablets | Count |")
        add("| --- | ---: |")
        flat = []
        for tablets, counts in direction["pairwise_orientations"].items():
            for arrow, count in counts.items():
                flat.append((count, f"{tablets} {arrow}"))
        for count, label in sorted(flat, reverse=True):
            add(f"| {label} | {count} |")
        add("")
    add(
        "A pair that always puts the same sign on the same witness is a directional "
        "candidate: the form on the witness that otherwise stands apart is the "
        "candidate later form, and only under the hypothesis that unique variants "
        "are innovations. Where the counts split both ways, the pair is not directional "
        "in this alignment. None of these arrows is a sound value."
    )
    add("")
    add("## What this does not say")
    add("")
    add(
        "The tree is a tree of the shared passages, not of the whole island's scribal "
        "history. Tablets with no parallel, including the early board D and the Staff I, "
        "are not placed on it. Support below a clear majority means that fork is weak. "
        "Wood dates and the tree answer different questions, and this note does not "
        "treat a young board as proof that the text was composed in that century, "
        "nor an old board as proof that the signs were cut when the tree fell."
    )
    add("")
    add("## Sources")
    add("")
    for source in result["sources"]:
        add(f"- {source}")
    add("")
    return "\n".join(lines)


def render_json(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, sort_keys=True) + "\n"


def write_outputs(result: dict[str, Any]) -> None:
    DOC_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(render_json(result), encoding="utf-8")
    DOC_PATH.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    write_outputs(run_round4_trackd(MockProvider()))


if __name__ == "__main__":
    main()
