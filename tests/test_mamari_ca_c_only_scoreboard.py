"""Mamari (C) Ca 13-gram off-C lock.

Cycle 118 text-search lock. Uses already-vendored Ca/Cb from cycles
24 / 28 / 32 plus already-vendored A–V. Does not vendor a new tablet.
Does not scrape X. W has no Barthel (cycle 100); do not invent W
stems. The 13-gram is the cycle-24 / cycle-99 longest repeating
n-gram (only n=13; longest_count=1). Cycle 24 already locked it as
the Ca6–Ca9 calendar longest (five 040 + Guy delimiter). Cycle 99
already listed C's max as tablet-only (counts only). Cycle 104
already listed C as exact-0 off home. C has not been locked as
home-only at max n the way A/B/D/E/I/M/N/S/V were. Raw stems. No
invented Barthel. No G00n→Barthel map. No type merge. No detector
retune. No CV. No new agents. Not a meaning dictionary.

Locks exact hits of 040 040 040 040 040 390 041 378 041 670 008
078 711 on every vendored tablet A–V. Claim that can lose:
c_maxn_is_c_only (C hits ≥ 2 and off-C hits == 0). Ca is exactly
2; Cb is 0; every other vendored tablet is exact-0. n=13 is ≥8
but not a shared n≥8 island (cycle 99/104 island_status stays
null). Not an exact match of the locked A n=10, I n=5, D n=4,
Va n=4, M n=4, N n=6, S n=7, E n=9, Er7 doubled 4-gram, or B n=8
sequences.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_b_eightgram_scoreboard import (
    TestMamariBEightgramScoreboard,
)
from tests.test_mamari_b_max_n_gk_doubled_8gram_scoreboard import (
    GRAM8_B,
)
from tests.test_mamari_calendar_scoreboard import (
    DELIMITER_MOTIF,
    fixture_line_stems,
    load_mamari_fixture,
)
from tests.test_mamari_cb_side_b_scoreboard import (
    CB_HTML_PATH,
    CB_LINE_NAMES,
    TestMamariCbSideBScoreboard,
    cb_line_stems,
    extract_cb_published_tokens,
    load_vendored_cb_html,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_N as INVENTORY_LONGEST_N,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_TOKENS as INVENTORY_LONGEST_TOKENS,
)
from tests.test_mamari_corpus_max_n_leak_table_scoreboard import (
    TestMamariCorpusMaxNLeakTableScoreboard,
)
from tests.test_mamari_honolulu3_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as V_N4_GRAM,
)
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_keiti_er7_double_scoreboard import (
    GRAM4 as ER7_GRAM4,
)
from tests.test_mamari_keiti_n9_scoreboard import (
    GRAM_N9 as E_GRAM_N9,
    named_side_hits,
    site_tuple,
)
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    TestMamariSantiagoIaIOnlyScoreboard,
)
from tests.test_mamari_second_passage_scoreboard import (
    CA_HTML_PATH,
    CALENDAR_LINE_NAMES,
    TestMamariSecondPassageScoreboard,
    extract_ca_published_tokens,
    load_corpus_survey,
    load_vendored_ca_html,
    published_stems,
)
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_tahua_aa_a_only_scoreboard import (
    TestMamariTahuaAaAOnlyScoreboard,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    STANDING_LONGEST_NGRAM as A_N10_GRAM,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as M_N4_GRAM,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as S_N7_GRAM,
)

SIDE_CA = "Ca"
SIDE_CB = "Cb"
CA_LINE_NAMES = tuple(f"Ca{n}" for n in range(1, 15))
GRAM13 = INVENTORY_LONGEST_TOKENS["C"]
A_N10 = INVENTORY_LONGEST_TOKENS["A"]
D_N4_GRAM = INVENTORY_LONGEST_TOKENS["D"]
I_N5_GRAM = INVENTORY_LONGEST_TOKENS["I"]
B_N8_GRAM = INVENTORY_LONGEST_TOKENS["B"]
OFF_C_TABLETS = tuple(tablet for tablet in VENDORED_TABLETS if tablet != "C")
STANDING_C_HITS = 2
STANDING_CA_HITS = 2
STANDING_CB_HITS = 0
STANDING_CA_SITES = (
    (SIDE_CA, "Ca7", 1),
    (SIDE_CA, "Ca8", 24),
)
STANDING_CB_SITES = ()
STANDING_CA_SPANS = (("Ca7", 1, 14), ("Ca8", 24, 37))
STANDING_OFF_C_HITS = 0
STANDING_OFF_C_BY_TABLET = (0,) * len(OFF_C_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_C_HITS if tablet == "C" else 0 for tablet in VENDORED_TABLETS
)
STANDING_C_MAXN_IS_C_ONLY = True
STANDING_N_GE_8_ISLAND = False
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_SAME_AS_A_N10 = False
STANDING_SAME_AS_I_N5 = False
STANDING_SAME_AS_D_N4 = False
STANDING_SAME_AS_V_N4 = False
STANDING_SAME_AS_M_N4 = False
STANDING_SAME_AS_N_N6 = False
STANDING_SAME_AS_S_N7 = False
STANDING_SAME_AS_E_N9 = False
STANDING_SAME_AS_ER7_4 = False
STANDING_SAME_AS_B_N8 = False
STANDING_LONGEST_COUNT = 1
STANDING_RESULT = "c_mamari_ca_c_only"
STANDING_CLAIM = "c_maxn_is_c_only"


def ca_line_stems(published: dict[str, list[str]]) -> list[list[str]]:
    """Ca1–Ca14 as stem sequences. Search only."""
    return [published_stems(published[name]) for name in CA_LINE_NAMES]


def load_c_sides() -> dict[str, list[list[str]]]:
    """Already-vendored Ca and Cb. No new C scrape."""
    return {
        SIDE_CA: ca_line_stems(extract_ca_published_tokens(load_vendored_ca_html())),
        SIDE_CB: cb_line_stems(extract_cb_published_tokens(load_vendored_cb_html())),
    }


def load_vendored_by_tablet() -> dict[str, list[list[str]]]:
    """Already-vendored A–V in letter order. No W stems."""
    raw = load_vendored_a_through_v()
    return {letter: raw[letter] for letter in VENDORED_TABLETS}


def c_maxn_is_c_only(c_hits: int, off_c_hits: int) -> bool:
    """True iff C hits ≥ 2 and off-C hits == 0."""
    return c_hits >= 2 and off_c_hits == 0


class TestMamariCaCOnlyHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 13-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(
            GRAM13,
            (
                "040",
                "040",
                "040",
                "040",
                "040",
                "390",
                "041",
                "378",
                "041",
                "670",
                "008",
                "078",
                "711",
            ),
        )
        adjacent = [list(GRAM13), list(GRAM13)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM13), 2)
        overlap = [list(GRAM13) + list(GRAM13)]
        self.assertEqual(ngram_hit_count(overlap, GRAM13), 2)
        gapped = [list(GRAM13[:6]) + ["999"] + list(GRAM13[6:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM13), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM13), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_c_only_requires_c_ge_2_and_zero_off_c(self):
        """Boolean is True only when C ≥ 2 and off-C is 0."""
        provider = MockProvider()
        self.assertTrue(c_maxn_is_c_only(2, 0))
        self.assertTrue(c_maxn_is_c_only(3, 0))
        self.assertFalse(c_maxn_is_c_only(2, 1))
        self.assertFalse(c_maxn_is_c_only(1, 0))
        self.assertFalse(c_maxn_is_c_only(0, 0))
        self.assertFalse(c_maxn_is_c_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "c_maxn_is_c_only")
        self.assertEqual(provider.get_call_history(), [])

    def test_13gram_is_not_locked_a_i_d_v_m_n_s_e_er7_or_b(self):
        """Ca 13-gram is a different string from locked local grams."""
        provider = MockProvider()
        self.assertNotEqual(GRAM13, A_N10)
        self.assertNotEqual(GRAM13, I_N5_GRAM)
        self.assertNotEqual(GRAM13, D_N4_GRAM)
        self.assertNotEqual(GRAM13, V_N4_GRAM)
        self.assertNotEqual(GRAM13, M_N4_GRAM)
        self.assertNotEqual(GRAM13, N_N6_GRAM)
        self.assertNotEqual(GRAM13, S_N7_GRAM)
        self.assertNotEqual(GRAM13, E_GRAM_N9)
        self.assertNotEqual(GRAM13, ER7_GRAM4)
        self.assertNotEqual(GRAM13, B_N8_GRAM)
        self.assertNotEqual(GRAM13, GRAM8_B)
        self.assertEqual(
            A_N10,
            ("080", "004", "280", "182", "048", "022", "025", "025", "009", "005"),
        )
        self.assertEqual(I_N5_GRAM, ("999", "071", "076", "010", "079"))
        self.assertEqual(D_N4_GRAM, ("002", "200", "052", "600"))
        self.assertEqual(V_N4_GRAM, ("048", "010", "048", "010"))
        self.assertEqual(M_N4_GRAM, ("006", "022", "006", "022"))
        self.assertEqual(N_N6_GRAM, ("004", "064", "034", "006", "004", "064"))
        self.assertEqual(S_N7_GRAM, ("004", "660", "081", "004", "660", "081", "004"))
        self.assertEqual(
            E_GRAM_N9,
            ("300", "040", "300", "028", "004", "430", "022", "380", "203"),
        )
        self.assertEqual(ER7_GRAM4, ("092", "050", "006", "670"))
        self.assertEqual(B_N8_GRAM, ("002", "065", "042", "300", "385", "003", "065", "200"))
        self.assertFalse(STANDING_SAME_AS_A_N10)
        self.assertFalse(STANDING_SAME_AS_I_N5)
        self.assertFalse(STANDING_SAME_AS_D_N4)
        self.assertFalse(STANDING_SAME_AS_V_N4)
        self.assertFalse(STANDING_SAME_AS_M_N4)
        self.assertFalse(STANDING_SAME_AS_N_N6)
        self.assertFalse(STANDING_SAME_AS_S_N7)
        self.assertFalse(STANDING_SAME_AS_E_N9)
        self.assertFalse(STANDING_SAME_AS_ER7_4)
        self.assertFalse(STANDING_SAME_AS_B_N8)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariCaCOnlyScoreboard(unittest.TestCase):
    """Cited-fixture Ca 13-gram off-C lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_c_sides()
        self.ca_sites = named_side_hits(
            self.by_side[SIDE_CA],
            CA_LINE_NAMES,
            SIDE_CA,
            GRAM13,
        )
        self.cb_sites = named_side_hits(
            self.by_side[SIDE_CB],
            CB_LINE_NAMES,
            SIDE_CB,
            GRAM13,
        )
        self.ca_hits = len(self.ca_sites)
        self.cb_hits = len(self.cb_sites)
        self.c_hits = self.ca_hits + self.cb_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM13, VENDORED_TABLETS)
        self.off_c_counts = tablet_hit_counts(self.by_tablet, GRAM13, OFF_C_TABLETS)
        self.off_c_hits = sum(self.off_c_counts)

    def test_ca7_ca8_hits_are_two_13grams(self):
        """13-gram is cycle-99 longest; Ca7[1] and Ca8[24]; not a shared island."""
        self.assertEqual(GRAM13, INVENTORY_LONGEST_TOKENS["C"])
        self.assertEqual(GRAM13[5:], DELIMITER_MOTIF)
        calendar_lines = fixture_line_stems(load_mamari_fixture())
        calendar_sites = named_side_hits(
            calendar_lines,
            CALENDAR_LINE_NAMES,
            SIDE_CA,
            GRAM13,
        )
        self.assertEqual(
            tuple(site_tuple(hit) for hit in calendar_sites),
            STANDING_CA_SITES,
        )
        self.assertEqual(A_N10, A_N10_GRAM)
        self.assertEqual(
            GRAM13,
            (
                "040",
                "040",
                "040",
                "040",
                "040",
                "390",
                "041",
                "378",
                "041",
                "670",
                "008",
                "078",
                "711",
            ),
        )
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["longest_tokens"]),
            GRAM13,
        )
        self.assertEqual(
            tuple(self.survey["corpus_max_n_leak_table"]["rows"]["C"]["longest_tokens"]),
            GRAM13,
        )
        self.assertEqual(len(GRAM13), INVENTORY_LONGEST_N["C"])
        self.assertEqual(INVENTORY_LONGEST_N["C"], 13)
        self.assertEqual(self.ca_hits, STANDING_CA_HITS)
        self.assertEqual(STANDING_CA_HITS, 2)
        self.assertEqual(self.ca_hits, ngram_hit_count(self.by_side[SIDE_CA], GRAM13))
        self.assertEqual(tuple(site_tuple(hit) for hit in self.ca_sites), STANDING_CA_SITES)
        published = extract_ca_published_tokens(load_vendored_ca_html())
        stems = ca_line_stems(published)
        for side, line, index in STANDING_CA_SITES:
            names = CA_LINE_NAMES
            line_stems = self.by_side[side][names.index(line)][index : index + 13]
            self.assertEqual(tuple(line_stems), GRAM13)
            self.assertEqual(tuple(stems[names.index(line)][index : index + 13]), GRAM13)
            self.assertEqual(side, SIDE_CA)
            self.assertIn(line, ("Ca7", "Ca8"))
        self.assertEqual(
            tuple((line, start, start + 13) for _side, line, start in STANDING_CA_SITES),
            STANDING_CA_SPANS,
        )
        self.assertEqual(STANDING_LONGEST_COUNT, 1)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["longest_count"], 1)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(len(GRAM13), 13)
        self.assertGreaterEqual(len(GRAM13), 8)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ca_cb_split_is_ca7_ca8_only(self):
        """Both Ca and Cb exist. Hits are Ca7/Ca8 only; Cb is 0."""
        fixtures = Path(__file__).parent / "fixtures"
        self.assertTrue(CA_HTML_PATH.is_file())
        self.assertTrue(CB_HTML_PATH.is_file())
        self.assertTrue((fixtures / "mamari_ca_html" / "Ca.html").exists())
        self.assertTrue((fixtures / "mamari_cb_html" / "Cb.html").exists())
        self.assertEqual(self.ca_hits, STANDING_CA_HITS)
        self.assertEqual(self.cb_hits, STANDING_CB_HITS)
        self.assertEqual(STANDING_CB_HITS, 0)
        self.assertEqual(self.c_hits, STANDING_C_HITS)
        self.assertEqual(self.c_hits, STANDING_CA_HITS + STANDING_CB_HITS)
        self.assertEqual(STANDING_C_HITS, 2)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.ca_sites), STANDING_CA_SITES)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.cb_sites), STANDING_CB_SITES)
        self.assertEqual(STANDING_CB_SITES, ())
        self.assertEqual(self.ca_hits, ngram_hit_count(self.by_side[SIDE_CA], GRAM13))
        self.assertEqual(self.cb_hits, ngram_hit_count(self.by_side[SIDE_CB], GRAM13))
        self.assertEqual(ngram_hit_count(self.by_tablet["C"], GRAM13), STANDING_C_HITS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_13gram_is_zero_off_c_and_c_only(self):
        """13-gram is 0 on A–B and D–V. Ca has exactly 2. W is not a tablet."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_C_TABLETS, tuple("ABDEFGHIJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_c_counts, STANDING_OFF_C_BY_TABLET)
        self.assertEqual(self.off_c_hits, STANDING_OFF_C_HITS)
        self.assertEqual(STANDING_OFF_C_HITS, 0)
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM13))
            if tablet == "C":
                self.assertEqual(count, STANDING_C_HITS)
                self.assertEqual(count, 2)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(
            c_maxn_is_c_only(self.c_hits, self.off_c_hits),
            STANDING_C_MAXN_IS_C_ONLY,
        )
        self.assertTrue(STANDING_C_MAXN_IS_C_ONLY)
        self.assertEqual(STANDING_CLAIM, "c_maxn_is_c_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(
            GRAM13,
            (
                "040",
                "040",
                "040",
                "040",
                "040",
                "390",
                "041",
                "378",
                "041",
                "670",
                "008",
                "078",
                "711",
            ),
        )
        self.assertNotEqual(GRAM13, A_N10)
        self.assertNotEqual(GRAM13, I_N5_GRAM)
        self.assertNotEqual(GRAM13, D_N4_GRAM)
        self.assertNotEqual(GRAM13, V_N4_GRAM)
        self.assertNotEqual(GRAM13, M_N4_GRAM)
        self.assertNotEqual(GRAM13, N_N6_GRAM)
        self.assertNotEqual(GRAM13, S_N7_GRAM)
        self.assertNotEqual(GRAM13, E_GRAM_N9)
        self.assertNotEqual(GRAM13, ER7_GRAM4)
        self.assertNotEqual(GRAM13, B_N8_GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_c_a_and_inventory_scoreboards_still_compute(self):
        """Cycle 28/32 C fixtures, cycle 99/104 inventory, and cycle 116 A-only stay."""
        prior_c = TestMamariSecondPassageScoreboard()
        prior_c.setUp()
        prior_c.test_survey_matches_computed_lock()
        prior_cb = TestMamariCbSideBScoreboard()
        prior_cb.setUp()
        prior_cb.test_survey_matches_computed_lock()
        prior_a = TestMamariTahuaAaAOnlyScoreboard()
        prior_a.setUp()
        prior_a.test_10gram_is_zero_off_a_and_a_only()
        prior_a.test_survey_matches_computed_lock()
        prior_i = TestMamariSantiagoIaIOnlyScoreboard()
        prior_i.setUp()
        prior_i.test_5gram_is_zero_off_i_and_i_only()
        prior_i.test_survey_matches_computed_lock()
        prior_leak = TestMamariCorpusMaxNLeakTableScoreboard()
        prior_leak.setUp()
        prior_leak.test_leak_table_holds_at_cycle_99_counts()
        prior_b = TestMamariBEightgramScoreboard()
        prior_b.setUp()
        prior_b.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-118 Ca C-only lock."""
        lock = self.survey["tablet_c_mamari_ca_c_only"]
        self.assertEqual(lock["cycle"], 118)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_c"], "C")
        self.assertEqual(lock["name_c"], "Mamari")
        self.assertEqual(tuple(lock["tokens13"]), GRAM13)
        self.assertEqual(lock["n13"], 13)
        self.assertEqual(lock["c_hits"], STANDING_C_HITS)
        self.assertEqual(lock["ca_hits"], STANDING_CA_HITS)
        self.assertEqual(lock["cb_hits"], STANDING_CB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["ca_sites"]),
            STANDING_CA_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["cb_sites"]), STANDING_CB_SITES)
        self.assertEqual(lock["longest_count"], STANDING_LONGEST_COUNT)
        self.assertFalse(lock["n_ge_8_island"])
        self.assertEqual(lock["off_c_hits"], STANDING_OFF_C_HITS)
        self.assertEqual(tuple(lock["off_c_tablets"]), OFF_C_TABLETS)
        self.assertEqual(tuple(lock["off_c_by_tablet"]), STANDING_OFF_C_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["c_maxn_is_c_only"], STANDING_C_MAXN_IS_C_ONLY)
        self.assertTrue(lock["c_maxn_is_c_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertEqual(tuple(lock["a_n10_tokens"]), A_N10)
        self.assertEqual(tuple(lock["i_n5_tokens"]), I_N5_GRAM)
        self.assertEqual(tuple(lock["d_n4_tokens"]), D_N4_GRAM)
        self.assertEqual(tuple(lock["v_n4_tokens"]), V_N4_GRAM)
        self.assertEqual(tuple(lock["m_n4_tokens"]), M_N4_GRAM)
        self.assertEqual(tuple(lock["n_n6_tokens"]), N_N6_GRAM)
        self.assertEqual(tuple(lock["s_n7_tokens"]), S_N7_GRAM)
        self.assertEqual(tuple(lock["e_n9_tokens"]), E_GRAM_N9)
        self.assertEqual(tuple(lock["er7_4gram_tokens"]), ER7_GRAM4)
        self.assertEqual(tuple(lock["b_n8_tokens"]), B_N8_GRAM)
        self.assertFalse(lock["same_as_a_n10"])
        self.assertFalse(lock["same_as_i_n5"])
        self.assertFalse(lock["same_as_d_n4"])
        self.assertFalse(lock["same_as_v_n4"])
        self.assertFalse(lock["same_as_m_n4"])
        self.assertFalse(lock["same_as_n_n6"])
        self.assertFalse(lock["same_as_s_n7"])
        self.assertFalse(lock["same_as_e_n9"])
        self.assertFalse(lock["same_as_er7_4"])
        self.assertFalse(lock["same_as_b_n8"])
        self.assertFalse(lock["w_barthel"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_tahua_aa_a_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_d_echancree_da_d_only_unchanged"])
        self.assertTrue(lock["standing_v_honolulu_va_v_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_b_repeating_8grams_unchanged"])
        self.assertTrue(lock["standing_s_washington_sb2_s_only_unchanged"])
        self.assertTrue(lock["standing_n_vienna_na1_n_only_unchanged"])
        self.assertTrue(lock["standing_m_vienna_ma2_m_only_unchanged"])
        self.assertTrue(lock["standing_c_side_b_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_c_side_b"]["cycle"], 32)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["longest_tokens"]),
            GRAM13,
        )
        self.assertTrue(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["tablet_only"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["own_hits"], 2)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["leak_hits"], 0)
        self.assertIsNone(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["island_status"])
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["rows"]["C"]["tablet_only"])
        self.assertEqual(
            tuple(self.survey["corpus_max_n_leak_table"]["rows"]["C"]["hits_by_tablet"]),
            STANDING_HITS_BY_TABLET,
        )
        self.assertEqual(self.survey["tablet_a_tahua_aa_a_only"]["cycle"], 116)
        self.assertTrue(self.survey["tablet_a_tahua_aa_a_only"]["a_10gram_is_a_only"])
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(self.survey["tablet_d_echancree_da_d_only"]["cycle"], 102)
        self.assertTrue(self.survey["tablet_d_echancree_da_d_only"]["d_only"])
        self.assertEqual(self.survey["tablet_v_honolulu_va_v_only"]["cycle"], 101)
        self.assertTrue(self.survey["tablet_v_honolulu_va_v_only"]["v_only"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertEqual(self.survey["b_repeating_8grams"]["cycle"], 115)
        self.assertFalse(self.survey["b_repeating_8grams"]["b_has_exactly_2_repeating_8grams"])
        self.assertEqual(self.survey["tablet_s_washington_sb2_s_only"]["cycle"], 95)
        self.assertTrue(self.survey["tablet_s_washington_sb2_s_only"]["s_only"])
        self.assertEqual(self.survey["tablet_n_vienna_na1_n_only"]["cycle"], 91)
        self.assertTrue(self.survey["tablet_n_vienna_na1_n_only"]["n_only"])
        self.assertEqual(self.survey["tablet_m_vienna_ma2_m_only"]["cycle"], 90)
        self.assertTrue(self.survey["tablet_m_vienna_ma2_m_only"]["m_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariCaCOnlyImageSnapshot(unittest.TestCase):
    """Cycle 118 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
