"""Off-tablet-C corpus ceiling: no honestly linked other Kohaumotu Barthel.

Cycle 35 text-search lock. Looks at the already-vendored Ca.html /
Cb.html navbar and sibling links, plus in-repo ATTRIBUTION /
CORPUS_SURVEY / README. No Kohaumotu Barthel page of a different
tablet is honestly linked from those navbars. Cycle 36 vendors
Aa.html from the parent catalog (folder above C/), not from Ca/Cb
siblings. Navbar hrefs stay C-only. Does not invent a URL or
digits. Does not fetch C/index.html (same-folder tablet-C contents).
No G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents.

Existing C scoreboards stay the lock: Guy delimiter, Ca 9-gram, three
Cb 5-grams, longest-n / 8-gram claims. Image track stays parked
83/62 / Hamming 6. MockProvider only.
"""

import re
import unittest
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_cb_5gram_ca_cross_scoreboard import (
    CB_5GRAMS,
    STANDING_CA_CROSS_TABLE,
    score_cb_5gram_ca_cross,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as CB_EIGHTGRAM_COUNT,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_LONGEST_N as CB_LONGEST_N,
)
from tests.test_mamari_cb_repeating_ngram_profile_scoreboard import (
    STANDING_LONGEST_NGRAMS,
    score_cb_repeating_ngrams,
)
from tests.test_mamari_cb_side_b_scoreboard import (
    CB_HTML_DIR,
    CB_HTML_PATH,
    CB_LINE_NAMES,
    CITED_CB_URL,
    cb_line_stems,
    extract_cb_published_tokens,
    load_vendored_cb_html,
)
from tests.test_mamari_remainder_9gram_motif_scoreboard import MOTIF_9GRAM
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as CA_REMAINDER_EIGHTGRAM_COUNT,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    STANDING_LONGEST_N as CA_REMAINDER_LONGEST_N,
)
from tests.test_mamari_remainder_ngram_profile_scoreboard import (
    score_remainder_repeating_ngrams,
)
from tests.test_mamari_second_passage_scoreboard import (
    CALENDAR_LINE_NAMES,
    CA_HTML_DIR,
    CA_HTML_PATH,
    CITED_CA_URL,
    REMAINDER_LINE_NAMES,
    extract_ca_published_tokens,
    find_ngram_hits,
    load_corpus_survey,
    load_vendored_ca_html,
    remainder_line_stems,
)

README_PATH = Path(__file__).resolve().parents[1] / "README.md"
CA7_ATTRIBUTION = (
    Path(__file__).parent / "fixtures" / "mamari_ca7_ca8" / "ATTRIBUTION"
)

HREF_RE = re.compile(r'href="([^"]+)"')
KOHAUMOTU_URL_RE = re.compile(r"https?://kohaumotu\.org/[^\s\"'<>)]+")
NAVBAR_START = '<div class="navbar">'
# Relative Barthel page: Ca.html / Cb.html / fi_Ca.html / Ca07.html.
_REL_TABLET_PAGE = re.compile(r"^(?:fi_)?([A-Z])[ab](?:\d+)?\.html$")
_ABS_TABLET_DIR = re.compile(r"kohaumotu\.org/Rongorongo/([A-Z])/")
_ABS_SVG_TABLET = re.compile(r"kohaumotu\.org/Rongorongo/svg/([A-Z])_")

SCOPED_SOURCE_PATHS = (
    CA_HTML_PATH,
    CB_HTML_PATH,
    CA_HTML_DIR / "ATTRIBUTION",
    CB_HTML_DIR / "ATTRIBUTION",
    CA7_ATTRIBUTION,
    CA_HTML_DIR / "CORPUS_SURVEY.json",
    README_PATH,
)

STANDING_CA_NAVBAR_HREFS = ("index.html", "Cb.html")
STANDING_CB_NAVBAR_HREFS = ("index.html", "Ca.html")
STANDING_CA_PAGE_HREFS = ("../rongorongo.css", "index.html", "Cb.html")
STANDING_CB_PAGE_HREFS = ("../rongorongo.css", "index.html", "Ca.html")
STANDING_OTHER_TABLET_HREFS = ()
STANDING_OTHER_TABLET_URLS = (
    "http://kohaumotu.org/Rongorongo/A/Aa.html",
    "http://kohaumotu.org/Rongorongo/A/Ab.html",
    "http://kohaumotu.org/Rongorongo/B/Br.html",
    "http://kohaumotu.org/Rongorongo/B/Bv.html",
    "http://kohaumotu.org/Rongorongo/D/Da.html",
    "http://kohaumotu.org/Rongorongo/D/Db.html",
    "http://kohaumotu.org/Rongorongo/E/Er.html",
    "http://kohaumotu.org/Rongorongo/E/Ev.html",
    "http://kohaumotu.org/Rongorongo/F/Fa.html",
    "http://kohaumotu.org/Rongorongo/F/Fb.html",
    "http://kohaumotu.org/Rongorongo/G/Gr.html",
    "http://kohaumotu.org/Rongorongo/G/Gv.html",
    "http://kohaumotu.org/Rongorongo/H/Hr.html",
    "http://kohaumotu.org/Rongorongo/H/Hv.html",
    "http://kohaumotu.org/Rongorongo/I/Ia.html",
    "http://kohaumotu.org/Rongorongo/J/J.html",
    "http://kohaumotu.org/Rongorongo/J/Ja.html",
    "http://kohaumotu.org/Rongorongo/K/Kr.html",
    "http://kohaumotu.org/Rongorongo/K/Kv.html",
    "http://kohaumotu.org/Rongorongo/L/L.html",
    "http://kohaumotu.org/Rongorongo/L/La.html",
    "http://kohaumotu.org/Rongorongo/M/Ma.html",
    "http://kohaumotu.org/Rongorongo/N/Na.html",
    "http://kohaumotu.org/Rongorongo/N/Nb.html",
    "http://kohaumotu.org/Rongorongo/O/Oa.html",
    "http://kohaumotu.org/Rongorongo/P/Pr.html",
    "http://kohaumotu.org/Rongorongo/P/Pv.html",
    "http://kohaumotu.org/Rongorongo/Q/Qr.html",
    "http://kohaumotu.org/Rongorongo/Q/Qv.html",
    "http://kohaumotu.org/Rongorongo/R/Ra.html",
    "http://kohaumotu.org/Rongorongo/R/Rb.html",
)
STANDING_RESULT = "tablet_c_corpus_ceiling"
STANDING_VENDABLE_TABLETS = ("C",)
STANDING_CITED_KOHAUMOTU_URLS = (
    "http://kohaumotu.org/Rongorongo/",
    "http://kohaumotu.org/Rongorongo/A/Aa.html",
    "http://kohaumotu.org/Rongorongo/A/Ab.html",
    "http://kohaumotu.org/Rongorongo/A/index.html",
    "http://kohaumotu.org/Rongorongo/B/Br.html",
    "http://kohaumotu.org/Rongorongo/B/Bv.html",
    "http://kohaumotu.org/Rongorongo/B/index.html",
    "http://kohaumotu.org/Rongorongo/C/Ca.html",
    "http://kohaumotu.org/Rongorongo/C/Ca07.html",
    "http://kohaumotu.org/Rongorongo/C/Cb.html",
    "http://kohaumotu.org/Rongorongo/C/fi_Ca.html",
    "http://kohaumotu.org/Rongorongo/D/Da.html",
    "http://kohaumotu.org/Rongorongo/D/Db.html",
    "http://kohaumotu.org/Rongorongo/D/index.html",
    "http://kohaumotu.org/Rongorongo/E/Er.html",
    "http://kohaumotu.org/Rongorongo/E/Ev.html",
    "http://kohaumotu.org/Rongorongo/E/index.html",
    "http://kohaumotu.org/Rongorongo/F/Fa.html",
    "http://kohaumotu.org/Rongorongo/F/Fb.html",
    "http://kohaumotu.org/Rongorongo/F/index.html",
    "http://kohaumotu.org/Rongorongo/G/Gr.html",
    "http://kohaumotu.org/Rongorongo/G/Gv.html",
    "http://kohaumotu.org/Rongorongo/G/index.html",
    "http://kohaumotu.org/Rongorongo/H/Hr.html",
    "http://kohaumotu.org/Rongorongo/H/Hv.html",
    "http://kohaumotu.org/Rongorongo/H/index.html",
    "http://kohaumotu.org/Rongorongo/I/Ia.html",
    "http://kohaumotu.org/Rongorongo/I/index.html",
    "http://kohaumotu.org/Rongorongo/J/J.html",
    "http://kohaumotu.org/Rongorongo/J/Ja.html",
    "http://kohaumotu.org/Rongorongo/J/index.html",
    "http://kohaumotu.org/Rongorongo/K/Kr.html",
    "http://kohaumotu.org/Rongorongo/K/Kv.html",
    "http://kohaumotu.org/Rongorongo/K/index.html",
    "http://kohaumotu.org/Rongorongo/L/L.html",
    "http://kohaumotu.org/Rongorongo/L/La.html",
    "http://kohaumotu.org/Rongorongo/L/index.html",
    "http://kohaumotu.org/Rongorongo/M/Ma.html",
    "http://kohaumotu.org/Rongorongo/M/index.html",
    "http://kohaumotu.org/Rongorongo/N/Na.html",
    "http://kohaumotu.org/Rongorongo/N/Nb.html",
    "http://kohaumotu.org/Rongorongo/N/index.html",
    "http://kohaumotu.org/Rongorongo/O/Oa.html",
    "http://kohaumotu.org/Rongorongo/O/index.html",
    "http://kohaumotu.org/Rongorongo/P/Pr.html",
    "http://kohaumotu.org/Rongorongo/P/Pv.html",
    "http://kohaumotu.org/Rongorongo/P/index.html",
    "http://kohaumotu.org/Rongorongo/Q/Qr.html",
    "http://kohaumotu.org/Rongorongo/Q/Qv.html",
    "http://kohaumotu.org/Rongorongo/Q/index.html",
    "http://kohaumotu.org/Rongorongo/R/Ra.html",
    "http://kohaumotu.org/Rongorongo/R/Rb.html",
    "http://kohaumotu.org/Rongorongo/R/index.html",
    "http://kohaumotu.org/Rongorongo/svg/C_svg_codes_b.html",
    "http://kohaumotu.org/Rongorongo/tablets.html",
    "http://kohaumotu.org/rongorongo_org/copy.html",
    "http://kohaumotu.org/rongorongo_org/mamari/ca0708.html",
    "http://kohaumotu.org/rongorongo_org/rosetta/lunar.html",
)
STANDING_CITED_TABLET_LETTERS = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R")
STANDING_VENDORED_BARTHEL_PAGES = (
    "Aa.html",
    "Ab.html",
    "Br.html",
    "Bv.html",
    "Ca.html",
    "Cb.html",
    "Da.html",
    "Db.html",
    "Er.html",
    "Ev.html",
    "Fa.html",
    "Fb.html",
    "Gr.html",
    "Gv.html",
    "Hr.html",
    "Hv.html",
    "Ia.html",
    "Ja.html",
    "Kr.html",
    "Kv.html",
    "La.html",
    "Ma.html",
    "Na.html",
    "Nb.html",
    "Oa.html",
    "Pr.html",
    "Pv.html",
    "Qr.html",
    "Qv.html",
    "Ra.html",
    "Rb.html",
)
STANDING_INDEX_KIND = "same_folder_contents"
STANDING_INDEX_DIFFERENT_TABLET = False
STANDING_INDEX_VENDORED = False
STANDING_INDEX_SCRAPED = False


def page_hrefs(html: str) -> tuple[str, ...]:
    """href values in document order. CSS / navbar / siblings only."""
    return tuple(HREF_RE.findall(html))


def navbar_hrefs(html: str) -> tuple[str, ...]:
    """href values inside the published navbar div."""
    start = html.find(NAVBAR_START)
    if start < 0:
        return ()
    end = html.find("</div>", start)
    return tuple(HREF_RE.findall(html[start:end]))


def kohaumotu_urls(text: str) -> tuple[str, ...]:
    """Absolute kohaumotu.org URLs already written in a source file."""
    return tuple(sorted(set(KOHAUMOTU_URL_RE.findall(text))))


def tablet_letter_from_ref(ref: str) -> str | None:
    """Barthel-page tablet letter, or None if the ref is not a tablet page.

    Does not invent a URL. Relative names come from vendored hrefs.
    Mamari / lunar paths already cited for tablet C stay C. License
    and same-folder contents are not tablet Barthel pages.
    """
    path = unescape(ref).split("#", 1)[0].split("?", 1)[0]
    lowered = path.lower()
    name = path.rsplit("/", 1)[-1]
    if name == "index.html" or lowered.endswith("/"):
        return None
    if lowered.endswith("rongorongo.css") or lowered.endswith(".js"):
        return None
    if lowered.endswith("copy.html"):
        return None
    if "mamari" in lowered or lowered.endswith("lunar.html"):
        return "C"
    if "/repro/ca." in lowered:
        return "C"
    absolute = _ABS_TABLET_DIR.search(path)
    if absolute:
        return absolute.group(1)
    svg = _ABS_SVG_TABLET.search(path)
    if svg:
        return svg.group(1)
    relative = _REL_TABLET_PAGE.match(name)
    if relative:
        return relative.group(1)
    return None


def other_tablet_refs(refs: tuple[str, ...]) -> tuple[str, ...]:
    """Refs whose tablet letter is present and not C."""
    return tuple(ref for ref in refs if tablet_letter_from_ref(ref) not in (None, "C"))


def scoped_source_text() -> str:
    """Concatenate the already-used sources cycle 35 is allowed to read."""
    return "\n".join(path.read_text(encoding="utf-8") for path in SCOPED_SOURCE_PATHS)


class TestOffTabletCCeilingHelpers(unittest.TestCase):
    """Helpers on synthetic markup. No CV, no LLM, no invented corpus URL."""

    def test_navbar_and_classifier_on_synthetic_pages(self):
        """Same-tablet navbar is empty of other tablets; a foreign href is not."""
        ca = (
            '<link rel="stylesheet" href="../rongorongo.css" />'
            f'{NAVBAR_START}<ul>'
            '<li><a href="index.html">contents</a></li>'
            '<li><a href="Cb.html">side b</a></li>'
            "</ul></div>"
        )
        foreign = (
            f'{NAVBAR_START}<ul>'
            '<li><a href="index.html">contents</a></li>'
            '<li><a href="Xa.html">other</a></li>'
            "</ul></div>"
        )
        self.assertEqual(navbar_hrefs(ca), ("index.html", "Cb.html"))
        self.assertEqual(other_tablet_refs(navbar_hrefs(ca)), ())
        self.assertEqual(tablet_letter_from_ref("Cb.html"), "C")
        self.assertEqual(tablet_letter_from_ref("index.html"), None)
        self.assertEqual(tablet_letter_from_ref("../rongorongo.css"), None)
        self.assertEqual(tablet_letter_from_ref(CITED_CA_URL), "C")
        self.assertEqual(tablet_letter_from_ref(CITED_CB_URL), "C")
        self.assertIsNone(
            tablet_letter_from_ref("http://kohaumotu.org/rongorongo_org/copy.html")
        )
        self.assertEqual(other_tablet_refs(navbar_hrefs(foreign)), ("Xa.html",))
        self.assertEqual(tablet_letter_from_ref("Xa.html"), "X")
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])


class TestMamariOffTabletCCeilingScoreboard(unittest.TestCase):
    """Tablet-C corpus ceiling. MockProvider only. No CV. No new scrape."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.ca_html = load_vendored_ca_html()
        self.cb_html = load_vendored_cb_html()
        self.ca_hrefs = page_hrefs(self.ca_html)
        self.cb_hrefs = page_hrefs(self.cb_html)
        self.ca_nav = navbar_hrefs(self.ca_html)
        self.cb_nav = navbar_hrefs(self.cb_html)
        self.cited_urls = kohaumotu_urls(scoped_source_text())
        self.calendar = fixture_line_stems(load_mamari_fixture())
        self.remainder = remainder_line_stems(
            extract_ca_published_tokens(self.ca_html)
        )
        self.cb_lines = cb_line_stems(extract_cb_published_tokens(self.cb_html))

    def test_navbar_siblings_are_tablet_c_only(self):
        """Ca/Cb navbars: same-folder contents + the other C side. No other tablet."""
        self.assertEqual(self.ca_nav, STANDING_CA_NAVBAR_HREFS)
        self.assertEqual(self.cb_nav, STANDING_CB_NAVBAR_HREFS)
        self.assertEqual(self.ca_hrefs, STANDING_CA_PAGE_HREFS)
        self.assertEqual(self.cb_hrefs, STANDING_CB_PAGE_HREFS)
        self.assertEqual(other_tablet_refs(self.ca_hrefs), STANDING_OTHER_TABLET_HREFS)
        self.assertEqual(other_tablet_refs(self.cb_hrefs), STANDING_OTHER_TABLET_HREFS)
        self.assertEqual(other_tablet_refs(self.ca_nav + self.cb_nav), ())
        self.assertIn("Item C:Mamari", self.ca_html)
        self.assertIn("Item C:Mamari", self.cb_html)
        self.assertNotIn("Item A:", self.ca_html)
        self.assertNotIn("Item B:", self.cb_html)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_index_html_is_same_folder_contents_not_a_different_tablet(self):
        """index.html is labeled contents. Not vendored. Not scraped. Not tablet X."""
        self.assertIn("index.html", self.ca_nav)
        self.assertIn("index.html", self.cb_nav)
        self.assertEqual(tablet_letter_from_ref("index.html"), None)
        self.assertFalse((CA_HTML_DIR / "index.html").is_file())
        self.assertFalse((CB_HTML_DIR / "index.html").is_file())
        attribution_ca = (CA_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        attribution_cb = (CB_HTML_DIR / "ATTRIBUTION").read_text(encoding="utf-8")
        self.assertIn("index.html", attribution_ca)
        self.assertIn("same C/ folder", attribution_ca)
        self.assertIn("index.html", attribution_cb)
        self.assertNotIn("http://kohaumotu.org/Rongorongo/C/index.html", attribution_ca)
        self.assertNotIn("http://kohaumotu.org/Rongorongo/C/index.html", attribution_cb)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_cited_kohaumotu_urls_are_tablet_c_or_license(self):
        """Navbar-era sources stay C. Cycles 36/38 cite A; 43/44 B; 46 I; 55/56 G; 59/60 K; 69 H/P; 70 Q; 79 D; 80 E; 85 F; 86 J; 87 L; 88 M; 89 N; 92 O; 93 R."""
        self.assertEqual(self.cited_urls, STANDING_CITED_KOHAUMOTU_URLS)
        letters = tuple(
            sorted(
                {
                    tablet_letter_from_ref(url)
                    for url in self.cited_urls
                    if tablet_letter_from_ref(url) is not None
                }
            )
        )
        self.assertEqual(letters, STANDING_CITED_TABLET_LETTERS)
        self.assertEqual(other_tablet_refs(self.cited_urls), STANDING_OTHER_TABLET_URLS)
        for url in self.cited_urls:
            self.assertTrue(url.startswith("http://kohaumotu.org/"))
            letter = tablet_letter_from_ref(url)
            self.assertIn(letter, (None, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"), url)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_no_other_tablet_html_was_vendored(self):
        """Ca/Cb plus Aa, Ab, Br, Bv, Ia, Gr, Gv, Kr, Kv, Hr/Hv/Pr/Pv, Qr/Qv, Da/Db, Er/Ev, Fa/Fb, Ja, La, Ma, Na/Nb, Oa, and cycle-93 Ra/Rb."""
        fixtures = Path(__file__).parent / "fixtures"
        barthel_pages = tuple(
            sorted(path.name for path in fixtures.glob("**/*[A-Z][abrv].html"))
        )
        self.assertEqual(barthel_pages, STANDING_VENDORED_BARTHEL_PAGES)
        self.assertTrue(CA_HTML_PATH.is_file())
        self.assertTrue(CB_HTML_PATH.is_file())
        self.assertTrue((CA_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertTrue((CB_HTML_DIR / "ATTRIBUTION").is_file())
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_c_scoreboards_still_compute(self):
        """Guy / Ca 9-gram / three Cb 5-grams / longest-n locks on C only."""
        guy_cal = find_ngram_hits(self.calendar, DELIMITER_MOTIF)
        guy_rem = find_ngram_hits(self.remainder, DELIMITER_MOTIF)
        guy_cb = find_ngram_hits(self.cb_lines, DELIMITER_MOTIF)
        self.assertTrue(guy_cal)
        self.assertEqual(guy_rem, [])
        self.assertEqual(guy_cb, [])

        motif_cal = find_ngram_hits(self.calendar, MOTIF_9GRAM)
        motif_rem = find_ngram_hits(self.remainder, MOTIF_9GRAM)
        motif_cb = find_ngram_hits(self.cb_lines, MOTIF_9GRAM)
        self.assertEqual(motif_cal, [])
        self.assertEqual(len(motif_rem), 2)
        self.assertEqual(motif_cb, [])

        cross = score_cb_5gram_ca_cross(
            CB_5GRAMS,
            self.calendar,
            CALENDAR_LINE_NAMES,
            self.remainder,
            REMAINDER_LINE_NAMES,
        )
        locked = tuple((row.tokens, row.calendar_hits, row.remainder_hits) for row in cross)
        self.assertEqual(locked, STANDING_CA_CROSS_TABLE)
        for gram in CB_5GRAMS:
            self.assertTrue(find_ngram_hits(self.cb_lines, gram))

        rem_profile = score_remainder_repeating_ngrams(self.remainder, self.analyzer)
        cb_profile = score_cb_repeating_ngrams(self.cb_lines, self.analyzer)
        self.assertEqual(rem_profile.longest_n, CA_REMAINDER_LONGEST_N)
        self.assertEqual(len(rem_profile.eightgrams), CA_REMAINDER_EIGHTGRAM_COUNT)
        self.assertGreaterEqual(CA_REMAINDER_EIGHTGRAM_COUNT, 1)
        self.assertEqual(cb_profile.longest_n, CB_LONGEST_N)
        self.assertEqual(len(cb_profile.eightgrams), CB_EIGHTGRAM_COUNT)
        self.assertEqual(CB_EIGHTGRAM_COUNT, 0)
        self.assertEqual(
            tuple(row.tokens for row in cb_profile.longest),
            tuple(tokens for tokens, _n, _freq, _spans in STANDING_LONGEST_NGRAMS),
        )
        self.assertEqual(tuple(CB_LINE_NAMES), tuple(f"Cb{n}" for n in range(1, 15)))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-35 tablet-C corpus ceiling."""
        lock = self.survey["off_tablet_c_ceiling"]
        self.assertEqual(lock["cycle"], 35)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["claim"], "expand_off_tablet_c")
        self.assertFalse(lock["other_tablet_vendored"])
        self.assertFalse(lock["invented_url"])
        self.assertFalse(lock["invented_digits"])
        self.assertEqual(tuple(lock["vendable_tablets"]), STANDING_VENDABLE_TABLETS)
        self.assertEqual(tuple(lock["navbar_hrefs"]["Ca.html"]), STANDING_CA_NAVBAR_HREFS)
        self.assertEqual(tuple(lock["navbar_hrefs"]["Cb.html"]), STANDING_CB_NAVBAR_HREFS)
        self.assertEqual(tuple(lock["all_hrefs"]["Ca.html"]), STANDING_CA_PAGE_HREFS)
        self.assertEqual(tuple(lock["all_hrefs"]["Cb.html"]), STANDING_CB_PAGE_HREFS)
        self.assertEqual(tuple(lock["other_tablet_hrefs"]), STANDING_OTHER_TABLET_HREFS)
        self.assertEqual(
            tuple(lock["other_tablet_kohaumotu_urls"]),
            STANDING_OTHER_TABLET_URLS,
        )
        self.assertEqual(tuple(lock["cited_kohaumotu_urls"]), STANDING_CITED_KOHAUMOTU_URLS)
        self.assertEqual(tuple(lock["cited_url_tablet_letters"]), STANDING_CITED_TABLET_LETTERS)
        index = lock["index_html"]
        self.assertEqual(index["href"], "index.html")
        self.assertEqual(index["kind"], STANDING_INDEX_KIND)
        self.assertEqual(index["different_tablet"], STANDING_INDEX_DIFFERENT_TABLET)
        self.assertEqual(index["vendored"], STANDING_INDEX_VENDORED)
        self.assertEqual(index["scraped"], STANDING_INDEX_SCRAPED)
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["cb_5gram_ca_cross"]["cycle"], 34)
        self.assertEqual(self.survey["cycle"], 28)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariOffTabletCCeilingImageSnapshot(unittest.TestCase):
    """Cycle 35 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
