"""Track 3: genealogy structure on the Santiago Staff and Small Santiago.

Uses the vendored Kohaumotu Barthel HTML already locked for I, Gr, and
Gv. Sign ids only. Glosses stay cited hypotheses. MockProvider only.
The corpus case runs the shuffled baselines once (a few tens of seconds).
"""

import re
import unittest
from html import unescape
from pathlib import Path

from agents.base.providers import MockProvider
from decipherment.track3_genealogy import (
    NULL_CONTENT_TRIALS,
    NULL_GV6_TRIALS,
    NULL_GV_TRIALS,
    NULL_IA_TEMPLATE_TRIALS,
    NULL_PLACEMENT_TRIALS,
    STEM_076,
    STEM_999,
    chain_links,
    extract_quad_phrases,
    extract_strict_phrases,
    group_stems,
    measure_genealogy,
)
from tests.test_mamari_santiago_ia_076_inventory_scoreboard import STANDING_076_COUNT
from tests.test_mamari_santiago_ia_999_scoreboard import STANDING_999_STEM_COUNT
from tests.test_mamari_santiago_ia_scoreboard import (
    IA_LINE_NAMES,
    extract_ia_published_tokens,
    load_vendored_ia_html,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    STANDING_STEM_TOTAL as IA_STEM_TOTAL,
)
from tests.test_mamari_second_passage_scoreboard import published_stems
from tests.test_mamari_small_santiago_gr_scoreboard import (
    GR_LINE_NAMES,
    extract_gr_published_tokens,
    load_vendored_gr_html,
)
from tests.test_mamari_small_santiago_gr_scoreboard import (
    STANDING_076_HITS as GR_076_HITS,
)
from tests.test_mamari_small_santiago_gr_scoreboard import (
    STANDING_STEM_TOTAL as GR_STEM_TOTAL,
)
from tests.test_mamari_small_santiago_gv_scoreboard import (
    GV_LINE_NAMES,
    extract_gv_published_tokens,
    load_vendored_gv_html,
)
from tests.test_mamari_small_santiago_gv_scoreboard import (
    STANDING_076_HITS as GV_076_HITS,
)
from tests.test_mamari_small_santiago_gv_scoreboard import (
    STANDING_STEM_TOTAL as GV_STEM_TOTAL,
)

DOC_PATH = Path(__file__).parent.parent / "docs" / "decipherment" / "track3_genealogy_staff.md"
FIXTURE_ROOT = Path(__file__).parent / "fixtures"

STANDING_STROKE_CODES = 97
STANDING_PURE_BREAKS = 96
STANDING_FUSED = ("999.440.076",)
STANDING_STROKE_FORMS = (("999", 87), ("999h", 6), ("999t", 3), ("999.440.076", 1))
STANDING_IMMEDIATE_076 = 91
STANDING_IMMEDIATE_SUFFIX = 85
STANDING_IMMEDIATE_BARE = 3
STANDING_NON_IMMEDIATE = (
    ("Ia6", 27, "430"),
    ("Ia6", 38, "606"),
    ("Ia6", 72, "129"),
    ("Ia6", 95, "607.000!"),
    ("Ia13", 116, "161"),
)
STANDING_INTERIOR = 83
STANDING_LENGTH_HISTOGRAM = (
    (2, 1),
    (3, 16),
    (5, 2),
    (6, 11),
    (8, 7),
    (9, 8),
    (10, 3),
    (11, 2),
    (12, 5),
    (13, 1),
    (15, 3),
    (16, 1),
    (17, 3),
    (18, 3),
    (20, 1),
    (21, 1),
    (22, 1),
    (24, 2),
    (25, 1),
    (28, 1),
    (30, 1),
    (32, 2),
    (35, 1),
    (39, 1),
    (41, 1),
    (42, 1),
    (45, 2),
    (46, 1),
)
STANDING_LENGTH_EQ_3 = 16
STANDING_LENGTH_MOD_3 = 54
STANDING_LENGTH_LT_3 = 1
STANDING_LENGTH_MEDIAN = 9
STANDING_FIRST_CONTAINS = 79
STANDING_FIRST_SUFFIX = 73
STANDING_LAST_CONTAINS = 5
STANDING_PENULTIMATE = 4
STANDING_ANTE = 67
STANDING_ANTE_ELIGIBLE = 82
STANDING_TRIAD_ONLY_FIRST = 16
STANDING_ONSET = (218, 378)
STANDING_OTHER = (153, 718)
STANDING_ATTACHMENT = (("bare", 61), ("suffix", 481), ("initial", 8), ("medial", 10))
STANDING_EDGES = 26
STANDING_SHORT = (("Ia5", ("406.076?", "071.078")),)
STANDING_FINAL_076 = (
    ("Ia2", "076"),
    ("Ia7", "076"),
    ("Ia7", "076.073?"),
    ("Ia8", "076f"),
    ("Ia13", "020.010.076"),
)
STANDING_GV6_GROUPS = (
    ("200", "000!", "280.076"),
    ("200", "280", "730.076"),
    ("200", "730", "517a.076"),
    ("200", "517a", "222.076"),
)
STANDING_GV6_CHILD = (("000",), ("280",), ("730",), ("517",))
STANDING_GV6_FATHER = (("280",), ("730",), ("517",), ("222",))
STANDING_GV6_LINKS = 3
STANDING_QUAD = ("200", "769", "381", "002.076")
STANDING_IA_PHRASES = (
    ("Ia3", ("200", "690.090", "129.076")),
    ("Ia8", ("200f", "023", "440.076")),
    ("Ia11", ("200", "726", "571.076")),
    ("Ia12", ("200?", "380.061x", "002V:076")),
    ("Ia14", ("200", "700", "071.076")),
)
STANDING_FISCHER_EXAMPLE = ("Ia12", 55, ("606.076", "700", "008"))
STANDING_RULES = (
    ("I-999-break", "candidate"),
    ("I-999-076-bracket", "candidate"),
    ("I-span-multiple-of-3", "tendency"),
    ("Gv6-200-X-Y076", "candidate"),
    ("I-200-X-Y076", "withheld"),
)

_REPORT = None


def _lines(published: dict[str, list[str]], names: tuple[str, ...]):
    return [(name, published[name]) for name in names]


def corpus_report():
    """Vendored I / Gv / Gr report. Computed once per process."""
    global _REPORT
    if _REPORT is None:
        ia = extract_ia_published_tokens(load_vendored_ia_html())
        gv = extract_gv_published_tokens(load_vendored_gv_html())
        gr = extract_gr_published_tokens(load_vendored_gr_html())
        _REPORT = measure_genealogy(
            _lines(ia, IA_LINE_NAMES),
            _lines(gv, GV_LINE_NAMES),
            _lines(gr, GR_LINE_NAMES),
        )
    return _REPORT


def stroke_groups_by_fixture() -> dict[str, int]:
    """999-bearing hyphen groups in vendored Kohaumotu <td> text."""
    cell = re.compile(r"<td>([^<]*)</td>")
    counts: dict[str, int] = {}
    for path in sorted(FIXTURE_ROOT.rglob("*.html")):
        text = path.read_text(encoding="utf-8", errors="replace")
        found = 0
        for raw in cell.findall(text):
            cell_text = unescape(raw).strip()
            if not cell_text or not any(character.isdigit() for character in cell_text):
                continue
            for part in cell_text.split("-"):
                if STEM_999 in group_stems(part):
                    found += 1
        if found:
            counts[str(path.relative_to(FIXTURE_ROOT))] = found
    return counts


class TestTrack3GenealogyHelpers(unittest.TestCase):
    """Extractor and stemmer on synthetic groups. No corpus, no LLM."""

    def test_stems_match_the_published_stemmer(self):
        """Colon ligatures and allograph marks follow published_stems."""
        samples = (
            "999h",
            "999t",
            "999.440.076",
            "280.076",
            "002V:076",
            "000!",
            "200f",
            "200?",
            "406.076?",
            "021:290.076",
        )
        for token in samples:
            self.assertEqual(group_stems(token), tuple(published_stems([token])))
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_strict_phrase_chains_when_the_father_is_the_next_child(self):
        """200 X Y.076 repeats, and the handoff is the father/child match."""
        groups = [
            "200",
            "001",
            "002.076",
            "200",
            "002",
            "003.076",
            "010",
            "200",
            "009",
            "008.076",
        ]
        phrases = extract_strict_phrases(groups, "toy")
        self.assertEqual(len(phrases), 3)
        self.assertEqual(chain_links(phrases), 1)
        self.assertEqual(phrases[0].child, ("001",))
        self.assertEqual(phrases[0].father, ("002",))
        self.assertEqual(phrases[1].child, ("002",))
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_a_stroke_is_not_a_name_slot_and_a_ligature_is_not_a_break(self):
        """999 inside a name slot is not a phrase. 999.440.076 is not pure."""
        groups = ["200", "999", "280.076", "200", "010", "011.076"]
        phrases = extract_strict_phrases(groups)
        self.assertEqual(len(phrases), 1)
        self.assertEqual(phrases[0].index, 3)
        self.assertEqual(phrases[0].groups, ("200", "010", "011.076"))
        self.assertEqual(extract_quad_phrases(["200", "001", "999", "002.076"]), ())
        self.assertEqual(group_stems("999.440.076"), ("999", "440", "076"))
        self.assertNotEqual(group_stems("999.440.076"), (STEM_999,))
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])

    def test_every_gloss_is_marked_hypothesis(self):
        """The module stores no reading that lacks a hypothesis tag."""
        from decipherment.track3_genealogy import GLOSSES

        self.assertGreaterEqual(len(GLOSSES), 3)
        for gloss in GLOSSES:
            self.assertEqual(gloss.status, "hypothesis")
            self.assertTrue(gloss.source)
            self.assertIn(gloss.sign, {STEM_076, "200", STEM_999})
        provider = MockProvider()
        self.assertEqual(provider.get_call_history(), [])


class TestTrack3GenealogyStaff(unittest.TestCase):
    """Locked counts on vendored I and G. MockProvider only."""

    @classmethod
    def setUpClass(cls):
        cls.provider = MockProvider()
        cls.report = corpus_report()

    def test_provider_is_unused(self):
        """Measurement does not call an LLM."""
        self.assertEqual(self.provider.get_call_history(), [])

    def test_stem_totals_match_the_standing_locks(self):
        """Same Barthel stems as the I / Gv / Gr scoreboards."""
        stems = self.report.stem_counts
        self.assertEqual(stems["I"]["all"], IA_STEM_TOTAL)
        self.assertEqual(stems["I"]["all"], 2469)
        self.assertEqual(stems["I"]["076"], STANDING_076_COUNT)
        self.assertEqual(stems["I"]["076"], 564)
        self.assertEqual(stems["I"]["999"], STANDING_999_STEM_COUNT)
        self.assertEqual(stems["I"]["999"], STANDING_STROKE_CODES)
        self.assertEqual(stems["I"]["200"], 22)
        self.assertEqual(stems["Gv"]["all"], GV_STEM_TOTAL)
        self.assertEqual(stems["Gv"]["076"], GV_076_HITS)
        self.assertEqual(stems["Gv"]["999"], 0)
        self.assertEqual(stems["Gr"]["all"], GR_STEM_TOTAL)
        self.assertEqual(stems["Gr"]["076"], GR_076_HITS)
        self.assertEqual(stems["Gr"]["999"], 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_vertical_strokes_are_already_encoded_as_999_on_i_only(self):
        """Staff bars are Barthel 999 in Ia.html. No second encoding was added."""
        strokes = self.report.strokes
        self.assertEqual(strokes.codes, STANDING_STROKE_CODES)
        self.assertEqual(strokes.pure_breaks, STANDING_PURE_BREAKS)
        self.assertEqual(strokes.fused_groups, STANDING_FUSED)
        self.assertEqual(strokes.form_counts, STANDING_STROKE_FORMS)
        self.assertEqual(stroke_groups_by_fixture(), {"santiago_ia_html/Ia.html": 97})
        self.assertEqual(self.provider.get_call_history(), [])

    def test_gv6_shift_register(self):
        """Four 200 X Y.076 phrases on Gv6, three father-to-child handoffs."""
        genealogy = self.report.genealogy
        phrases = genealogy.gv6_phrases
        self.assertEqual(tuple(phrase.groups for phrase in phrases), STANDING_GV6_GROUPS)
        self.assertEqual(tuple(phrase.child for phrase in phrases), STANDING_GV6_CHILD)
        self.assertEqual(tuple(phrase.father for phrase in phrases), STANDING_GV6_FATHER)
        self.assertEqual(genealogy.gv6_links, STANDING_GV6_LINKS)
        self.assertEqual(genealogy.gv6_max_run, 3)
        self.assertEqual(len(genealogy.gv6_quads), 1)
        self.assertEqual(genealogy.gv6_quads[0].groups, STANDING_QUAD)
        self.assertFalse(genealogy.gv6_quad_handoff_father)
        self.assertFalse(genealogy.gv6_quad_handoff_third)
        self.assertEqual(genealogy.gv567_strict, 4)
        self.assertEqual(genealogy.gv567_links, 3)
        self.assertEqual(genealogy.gv567_quads, 1)
        self.assertEqual(genealogy.child_types, 4)
        self.assertEqual(genealogy.child_tokens, 4)
        self.assertEqual(genealogy.father_types, 4)
        self.assertEqual(genealogy.father_tokens, 4)
        self.assertEqual(genealogy.gv_strict, 4)
        self.assertEqual(genealogy.gv_links, 3)
        self.assertEqual(genealogy.gr_strict, 0)
        self.assertEqual(genealogy.gr_links, 0)
        self.assertEqual(genealogy.ia_strict, 5)
        self.assertEqual(genealogy.ia_links, 0)
        ia_hits = tuple(
            (row.line, row.strict, row.links, row.quads)
            for row in genealogy.by_line
            if row.line.startswith("Ia") and (row.strict or row.quads or row.links)
        )
        self.assertEqual(
            ia_hits,
            (
                ("Ia3", 1, 0, 0),
                ("Ia8", 1, 0, 0),
                ("Ia11", 1, 0, 0),
                ("Ia12", 1, 0, 0),
                ("Ia14", 1, 0, 0),
            ),
        )
        self.assertEqual(
            tuple((phrase.line, phrase.groups) for phrase in self._ia_phrases()),
            STANDING_IA_PHRASES,
        )
        self.assertEqual(self.provider.get_call_history(), [])

    def _ia_phrases(self):
        ia = extract_ia_published_tokens(load_vendored_ia_html())
        found = []
        for name in IA_LINE_NAMES:
            found.extend(extract_strict_phrases(ia[name], name))
        return found

    def test_staff_spans_between_strokes(self):
        """Interior spans, 076 slots, and the cited 606.076 700 008 order."""
        fischer = self.report.fischer
        self.assertEqual(fischer.pure_breaks, STANDING_PURE_BREAKS)
        self.assertEqual(fischer.immediate_076_group, STANDING_IMMEDIATE_076)
        self.assertEqual(fischer.immediate_076_suffix, STANDING_IMMEDIATE_SUFFIX)
        self.assertEqual(fischer.immediate_bare_076, STANDING_IMMEDIATE_BARE)
        self.assertEqual(fischer.non_immediate, STANDING_NON_IMMEDIATE)
        self.assertEqual(fischer.interior, STANDING_INTERIOR)
        self.assertEqual(fischer.length_histogram, STANDING_LENGTH_HISTOGRAM)
        self.assertEqual(sum(count for _length, count in fischer.length_histogram), 83)
        self.assertEqual(fischer.length_eq_3, STANDING_LENGTH_EQ_3)
        self.assertEqual(fischer.length_mod_3, STANDING_LENGTH_MOD_3)
        self.assertEqual(fischer.length_lt_3, STANDING_LENGTH_LT_3)
        self.assertEqual(fischer.length_median, STANDING_LENGTH_MEDIAN)
        self.assertEqual(fischer.first_contains_076, STANDING_FIRST_CONTAINS)
        self.assertEqual(fischer.first_is_suffix, STANDING_FIRST_SUFFIX)
        self.assertEqual(fischer.last_contains_076, STANDING_LAST_CONTAINS)
        self.assertEqual(fischer.penultimate_contains_076, STANDING_PENULTIMATE)
        self.assertEqual(fischer.antepenultimate_contains_076, STANDING_ANTE)
        self.assertEqual(fischer.ante_eligible, STANDING_ANTE_ELIGIBLE)
        self.assertEqual(fischer.triad_only_first, STANDING_TRIAD_ONLY_FIRST)
        self.assertEqual(
            (fischer.onset_contains_076, fischer.onset_groups),
            STANDING_ONSET,
        )
        self.assertEqual(
            (fischer.other_contains_076, fischer.other_groups),
            STANDING_OTHER,
        )
        self.assertEqual(fischer.attachment, STANDING_ATTACHMENT)
        self.assertEqual(fischer.edge_nonempty, STANDING_EDGES)
        self.assertEqual(fischer.short_segment, STANDING_SHORT)
        self.assertEqual(fischer.interior_final_076, STANDING_FINAL_076)
        slots = self.report.triad_slots
        self.assertEqual(slots.x_tokens, 16)
        self.assertEqual(slots.x_types, 15)
        self.assertEqual(slots.y_types, 14)
        self.assertEqual(slots.z_types, 14)
        self.assertEqual(slots.x_suffix, 15)
        ia = extract_ia_published_tokens(load_vendored_ia_html())
        line, index, gram = STANDING_FISCHER_EXAMPLE
        self.assertEqual(tuple(ia[line][index : index + 3]), gram)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_shuffle_baselines(self):
        """Null hit counts for the pre-specified seeds and trial sizes."""
        content = self.report.content_null
        self.assertEqual(content["immediate_076_group"].trials, NULL_CONTENT_TRIALS)
        self.assertEqual(content["immediate_076_group"].ge, 0)
        self.assertEqual(content["first_contains_076"].ge, 0)
        self.assertEqual(content["first_is_suffix"].ge, 0)
        self.assertEqual(content["antepenultimate_contains_076"].ge, 0)
        self.assertEqual(content["triad_only_first"].ge, 0)
        self.assertEqual(content["onset_contains_076"].ge, 0)
        self.assertEqual(content["last_contains_076"].le, 0)
        self.assertEqual(content["penultimate_contains_076"].le, 0)
        self.assertEqual(content["other_contains_076"].le, 0)
        placement = self.report.placement_null
        self.assertEqual(placement["length_eq_3"].trials, NULL_PLACEMENT_TRIALS)
        self.assertEqual(placement["length_eq_3"].ge, 0)
        self.assertEqual(placement["length_mod_3"].ge, 0)
        self.assertEqual(placement["length_lt_3"].le, 1)
        self.assertEqual(placement["interior"].ge, 1)
        gv6 = self.report.gv6_null
        self.assertEqual(gv6["links"].trials, NULL_GV6_TRIALS)
        self.assertEqual(gv6["links"].ge, 0)
        self.assertEqual(gv6["max_run"].ge, 0)
        self.assertEqual(gv6["phrases"].ge, 5)
        gv = self.report.gv_null
        self.assertEqual(gv["links"].trials, NULL_GV_TRIALS)
        self.assertEqual(gv["links"].ge, 0)
        self.assertEqual(gv["phrases"].ge, 32)
        ia = self.report.ia_template_null
        self.assertEqual(ia["phrases"].trials, NULL_IA_TEMPLATE_TRIALS)
        self.assertEqual(ia["phrases"].observed, 5)
        self.assertEqual(ia["phrases"].ge, 185)
        self.assertEqual(ia["links"].observed, 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_boundary_rules_and_the_writeup_quote_the_locks(self):
        """Hooks stay scoped, and the note quotes the locked fractions."""
        rules = tuple((rule.rule_id, rule.status) for rule in self.report.rules)
        self.assertEqual(rules, STANDING_RULES)
        for gloss in self.report.glosses:
            self.assertEqual(gloss.status, "hypothesis")
        text = DOC_PATH.read_text(encoding="utf-8")
        for snippet in (
            "91/96",
            "4 phrases",
            "3 father-to-child",
            "0 of 5000",
            "16/83",
            "54/83",
            "999.440.076",
            "606.076, 700, 008",
            "I-999-break",
            "Gv6-200-X-Y076",
            "hypothesis",
            "185 of 2000",
        ):
            self.assertIn(snippet, text)
        self.assertEqual(self.provider.get_call_history(), [])
