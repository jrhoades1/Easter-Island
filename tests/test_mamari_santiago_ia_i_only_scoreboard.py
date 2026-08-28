"""Santiago Staff (I) Ia 5-gram off-I lock.

Cycle 103 text-search lock. Uses already-vendored Ia from cycle 46
plus already-vendored A–V. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); do not invent W stems.
The 5-gram is the cycle-46 / cycle-99 longest repeating n-gram
(first of five n=5 ties). Cycle 99 already listed I's max as
tablet-only (counts only). Cycle 102 already showed a different
gram is D-only. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Locks exact hits of 999 071 076 010 079 on every vendored tablet
A–V. Claim that can lose: i_only (I hits ≥ 2 and off-I hits == 0).
Ia is exactly 3; Ib is unpublished 0; every other vendored tablet
is exact-0. Not an n≥8 island. Not an exact match of the locked
D n=4, Va n=4, M n=4, N n=6, S n=7, E n=9, or Er7 doubled
4-gram sequences.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_N as INVENTORY_I_LONGEST_N,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_TOKENS as INVENTORY_LONGEST_TOKENS,
)
from tests.test_mamari_echancree_da_d_only_scoreboard import (
    TestMamariEchancreeDaDOnlyScoreboard,
)
from tests.test_mamari_honolulu3_va_v_only_scoreboard import (
    TestMamariHonolulu3VaVOnlyScoreboard,
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
from tests.test_mamari_santiago_ia_scoreboard import (
    IA_HTML_PATH,
    IA_LINE_NAMES,
    TestMamariSantiagoIaScoreboard,
    extract_ia_published_tokens,
    ia_line_stems,
    load_vendored_ia_html,
    score_ia_repeating_ngrams,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as I_EIGHTGRAM_COUNT,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    STANDING_IR_HTML,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    STANDING_LONGEST_N as I_LONGEST_N,
)
from tests.test_mamari_santiago_ia_scoreboard import (
    STANDING_LONGEST_NGRAM as I_N5_GRAM,
)
from tests.test_mamari_santiago_ib_scoreboard import (
    IB_HTML_PATH,
    STANDING_IB_HTML,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_vienna_ma2_m_only_scoreboard import (
    tablet_hit_counts,
)
from tests.test_mamari_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as M_N4_GRAM,
)
from tests.test_mamari_washington_sb2_s_only_scoreboard import (
    TestMamariWashingtonSb2SOnlyScoreboard,
)
from tests.test_mamari_washington_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as S_N7_GRAM,
)

SIDE_IA = "Ia"
SIDE_IB = "Ib"
GRAM5 = INVENTORY_LONGEST_TOKENS["I"]
D_N4_GRAM = INVENTORY_LONGEST_TOKENS["D"]
OFF_I_TABLETS = tuple(tablet for tablet in VENDORED_TABLETS if tablet != "I")
STANDING_I_HITS = 3
STANDING_IA_HITS = 3
STANDING_IB_HITS = 0
STANDING_IA_SITES = (
    (SIDE_IA, "Ia4", 6),
    (SIDE_IA, "Ia4", 25),
    (SIDE_IA, "Ia5", 108),
)
STANDING_IB_SITES = ()
STANDING_IA_SPANS = (("Ia4", 6, 11), ("Ia4", 25, 30), ("Ia5", 108, 113))
STANDING_OFF_I_HITS = 0
STANDING_OFF_I_BY_TABLET = (0,) * len(OFF_I_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_I_HITS if tablet == "I" else 0 for tablet in VENDORED_TABLETS
)
STANDING_I_ONLY = True
STANDING_N_GE_8_ISLAND = False
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_SAME_AS_D_N4 = False
STANDING_SAME_AS_V_N4 = False
STANDING_SAME_AS_M_N4 = False
STANDING_SAME_AS_N_N6 = False
STANDING_SAME_AS_S_N7 = False
STANDING_SAME_AS_E_N9 = False
STANDING_SAME_AS_ER7_4 = False
STANDING_TIED_COUNT = 5
STANDING_TIED_TOKENS5 = (
    ("999", "071", "076", "010", "079"),
    ("430", "076", "006", "000", "076"),
    ("076", "010", "079", "006", "700"),
    ("076", "011", "090", "090", "076"),
    ("400", "070", "076", "020", "010"),
)
STANDING_RESULT = "i_santiago_ia_i_only"
STANDING_CLAIM = "i_only"


def load_i_sides() -> dict[str, list[list[str]]]:
    """Already-vendored Ia only. Ib is unpublished."""
    return {SIDE_IA: ia_line_stems(extract_ia_published_tokens(load_vendored_ia_html()))}


def load_vendored_by_tablet() -> dict[str, list[list[str]]]:
    """Already-vendored A–V in letter order. No W stems."""
    raw = load_vendored_a_through_v()
    return {letter: raw[letter] for letter in VENDORED_TABLETS}


def is_i_only(i_hits: int, off_i_hits: int) -> bool:
    """True iff I hits ≥ 2 and off-I hits == 0."""
    return i_hits >= 2 and off_i_hits == 0


class TestSantiagoIaIOnlyHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 5-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        adjacent = [list(GRAM5), list(GRAM5)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM5), 2)
        overlap = [["999", "071", "076", "010", "079", "999", "071", "076", "010", "079"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM5), 2)
        gapped = [list(GRAM5[:2]) + ["600"] + list(GRAM5[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM5), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM5), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_i_only_requires_i_ge_2_and_zero_off_i(self):
        """Boolean is True only when I ≥ 2 and off-I is 0."""
        provider = MockProvider()
        self.assertTrue(is_i_only(2, 0))
        self.assertTrue(is_i_only(3, 0))
        self.assertFalse(is_i_only(2, 1))
        self.assertFalse(is_i_only(1, 0))
        self.assertFalse(is_i_only(0, 0))
        self.assertFalse(is_i_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "i_only")
        self.assertEqual(provider.get_call_history(), [])

    def test_5gram_is_not_locked_d_v_m_n_s_e_or_er7(self):
        """Ia 5-gram is a different string from locked local grams."""
        provider = MockProvider()
        self.assertNotEqual(GRAM5, D_N4_GRAM)
        self.assertNotEqual(GRAM5, V_N4_GRAM)
        self.assertNotEqual(GRAM5, M_N4_GRAM)
        self.assertNotEqual(GRAM5, N_N6_GRAM)
        self.assertNotEqual(GRAM5, S_N7_GRAM)
        self.assertNotEqual(GRAM5, E_GRAM_N9)
        self.assertNotEqual(GRAM5, ER7_GRAM4)
        self.assertEqual(D_N4_GRAM, ("002", "200", "052", "600"))
        self.assertEqual(V_N4_GRAM, ("048", "010", "048", "010"))
        self.assertEqual(M_N4_GRAM, ("006", "022", "006", "022"))
        self.assertEqual(N_N6_GRAM, ("004", "064", "034", "006", "004", "064"))
        self.assertEqual(S_N7_GRAM, ("004", "660", "081", "004", "660", "081", "004"))
        self.assertEqual(E_GRAM_N9, ("300", "040", "300", "028", "004", "430", "022", "380", "203"))
        self.assertEqual(ER7_GRAM4, ("092", "050", "006", "670"))
        self.assertFalse(STANDING_SAME_AS_D_N4)
        self.assertFalse(STANDING_SAME_AS_V_N4)
        self.assertFalse(STANDING_SAME_AS_M_N4)
        self.assertFalse(STANDING_SAME_AS_N_N6)
        self.assertFalse(STANDING_SAME_AS_S_N7)
        self.assertFalse(STANDING_SAME_AS_E_N9)
        self.assertFalse(STANDING_SAME_AS_ER7_4)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSantiagoIaIOnlyScoreboard(unittest.TestCase):
    """Cited-fixture Ia 5-gram off-I lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_side = load_i_sides()
        self.profile = score_ia_repeating_ngrams(self.by_side[SIDE_IA], self.analyzer)
        self.ia_sites = named_side_hits(
            self.by_side[SIDE_IA],
            IA_LINE_NAMES,
            SIDE_IA,
            GRAM5,
        )
        self.ia_hits = len(self.ia_sites)
        self.ib_hits = STANDING_IB_HITS
        self.i_hits = self.ia_hits + self.ib_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM5, VENDORED_TABLETS)
        self.off_i_counts = tablet_hit_counts(self.by_tablet, GRAM5, OFF_I_TABLETS)
        self.off_i_hits = sum(self.off_i_counts)

    def test_ia_hits_are_three_5grams(self):
        """5-gram is cycle-99 longest; Ia4[6]/[25] and Ia5[108]; not n≥8."""
        self.assertEqual(GRAM5, I_N5_GRAM)
        self.assertEqual(GRAM5, INVENTORY_LONGEST_TOKENS["I"])
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_staff"]["longest_tokens"]),
            GRAM5,
        )
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_tokens"]),
            GRAM5,
        )
        self.assertEqual(self.profile.longest[0].tokens, GRAM5)
        self.assertEqual(len(GRAM5), I_LONGEST_N)
        self.assertEqual(I_LONGEST_N, 5)
        self.assertEqual(INVENTORY_I_LONGEST_N["I"], 5)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(STANDING_IA_HITS, 3)
        self.assertEqual(self.ia_hits, ngram_hit_count(self.by_side[SIDE_IA], GRAM5))
        self.assertEqual(tuple(site_tuple(hit) for hit in self.ia_sites), STANDING_IA_SITES)
        published = extract_ia_published_tokens(load_vendored_ia_html())
        stems = ia_line_stems(published)
        for side, line, index in STANDING_IA_SITES:
            names = IA_LINE_NAMES
            line_stems = self.by_side[side][names.index(line)][index : index + 5]
            self.assertEqual(tuple(line_stems), GRAM5)
            self.assertEqual(tuple(stems[names.index(line)][index : index + 5]), GRAM5)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(line, ("Ia4", "Ia5"))
        self.assertEqual(
            tuple((line, start, start + 5) for _side, line, start in STANDING_IA_SITES),
            STANDING_IA_SPANS,
        )
        self.assertEqual(self.profile.longest[0].spans, STANDING_IA_SPANS)
        self.assertEqual(I_EIGHTGRAM_COUNT, 0)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(len(GRAM5), 5)
        self.assertLess(len(GRAM5), 8)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_ia_only_side_and_no_ib(self):
        """Only Ia exists. Hits are Ia4/Ia5 only; Ib is unpublished 0."""
        fixtures = Path(__file__).parent / "fixtures"
        self.assertTrue(IA_HTML_PATH.is_file())
        self.assertTrue((fixtures / "santiago_ia_html" / "Ia.html").exists())
        self.assertFalse(IB_HTML_PATH.is_file())
        self.assertFalse((fixtures / "santiago_ib_html" / "Ib.html").exists())
        self.assertFalse((fixtures / "santiago_ia_html" / "Ib.html").exists())
        self.assertFalse((fixtures / "santiago_ia_html" / "Ir.html").exists())
        self.assertFalse(STANDING_IB_HTML)
        self.assertFalse(STANDING_IR_HTML)
        self.assertEqual(self.ia_hits, STANDING_IA_HITS)
        self.assertEqual(self.ib_hits, STANDING_IB_HITS)
        self.assertEqual(STANDING_IB_HITS, 0)
        self.assertEqual(self.i_hits, STANDING_I_HITS)
        self.assertEqual(self.i_hits, STANDING_IA_HITS + STANDING_IB_HITS)
        self.assertEqual(STANDING_I_HITS, 3)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.ia_sites), STANDING_IA_SITES)
        self.assertEqual(STANDING_IB_SITES, ())
        self.assertEqual(self.ia_hits, ngram_hit_count(self.by_side[SIDE_IA], GRAM5))
        self.assertEqual(ngram_hit_count(self.by_tablet["I"], GRAM5), STANDING_I_HITS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_5gram_is_zero_off_i_and_i_only(self):
        """5-gram is 0 on A–H and J–V. Ia has exactly 3. W is not a tablet."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_I_TABLETS, tuple("ABCDEFGHJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_i_counts, STANDING_OFF_I_BY_TABLET)
        self.assertEqual(self.off_i_hits, STANDING_OFF_I_HITS)
        self.assertEqual(STANDING_OFF_I_HITS, 0)
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM5))
            if tablet == "I":
                self.assertEqual(count, STANDING_I_HITS)
                self.assertEqual(count, 3)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(is_i_only(self.i_hits, self.off_i_hits), STANDING_I_ONLY)
        self.assertTrue(STANDING_I_ONLY)
        self.assertEqual(STANDING_CLAIM, "i_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(GRAM5, ("999", "071", "076", "010", "079"))
        self.assertNotEqual(GRAM5, D_N4_GRAM)
        self.assertNotEqual(GRAM5, V_N4_GRAM)
        self.assertNotEqual(GRAM5, M_N4_GRAM)
        self.assertNotEqual(GRAM5, N_N6_GRAM)
        self.assertNotEqual(GRAM5, S_N7_GRAM)
        self.assertNotEqual(GRAM5, E_GRAM_N9)
        self.assertNotEqual(GRAM5, ER7_GRAM4)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_tied_other_5grams_are_also_i_only(self):
        """Cycle 99 longest_count=5; the other n=5 grams are also I-only."""
        self.assertEqual(STANDING_TIED_COUNT, 5)
        self.assertEqual(len(self.profile.longest), STANDING_TIED_COUNT)
        self.assertEqual(STANDING_TIED_TOKENS5[0], GRAM5)
        measured_tied = tuple(row.tokens for row in self.profile.longest)
        self.assertEqual(measured_tied, STANDING_TIED_TOKENS5)
        for tied in STANDING_TIED_TOKENS5[1:]:
            self.assertNotEqual(tied, GRAM5)
            self.assertEqual(len(tied), 5)
            tied_hits = tablet_hit_counts(self.by_tablet, tied, VENDORED_TABLETS)
            self.assertEqual(tied_hits[VENDORED_TABLETS.index("I")], 2)
            self.assertEqual(sum(tied_hits) - tied_hits[VENDORED_TABLETS.index("I")], 0)
            for tablet, count in zip(VENDORED_TABLETS, tied_hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], tied))
                if tablet == "I":
                    self.assertEqual(count, 2)
                else:
                    self.assertEqual(count, 0)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_i_d_and_inventory_scoreboards_still_compute(self):
        """Cycle 46 I vendor, cycle 99 inventory, and cycle 102 D-only stay."""
        prior_i = TestMamariSantiagoIaScoreboard()
        prior_i.setUp()
        prior_i.test_longest_n_top_8gram_and_stem_count()
        prior_i.test_survey_matches_computed_lock()
        prior_d = TestMamariEchancreeDaDOnlyScoreboard()
        prior_d.setUp()
        prior_d.test_4gram_is_zero_off_d_and_d_only()
        prior_d.test_survey_matches_computed_lock()
        prior_v = TestMamariHonolulu3VaVOnlyScoreboard()
        prior_v.setUp()
        prior_v.test_4gram_is_zero_off_v_and_v_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        prior_s = TestMamariWashingtonSb2SOnlyScoreboard()
        prior_s.setUp()
        prior_s.test_7gram_is_zero_off_s_and_s_only()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-103 Ia I-only lock."""
        lock = self.survey["tablet_i_santiago_ia_i_only"]
        self.assertEqual(lock["cycle"], 103)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_i"], "I")
        self.assertEqual(lock["name_i"], "Santiago Staff")
        self.assertEqual(tuple(lock["tokens5"]), GRAM5)
        self.assertEqual(lock["n5"], 5)
        self.assertEqual(lock["i_hits"], STANDING_I_HITS)
        self.assertEqual(lock["ia_hits"], STANDING_IA_HITS)
        self.assertEqual(lock["ib_hits"], STANDING_IB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["ia_sites"]),
            STANDING_IA_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ib_sites"]), STANDING_IB_SITES)
        self.assertFalse(lock["ib_html"])
        self.assertFalse(lock["ir_html"])
        self.assertEqual(lock["tied_count"], STANDING_TIED_COUNT)
        self.assertEqual(
            tuple(tuple(row) for row in lock["tied_tokens5"]),
            STANDING_TIED_TOKENS5,
        )
        self.assertEqual(lock["eightgram_count"], 0)
        self.assertFalse(lock["eightgram_exists"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertEqual(lock["off_i_hits"], STANDING_OFF_I_HITS)
        self.assertEqual(tuple(lock["off_i_tablets"]), OFF_I_TABLETS)
        self.assertEqual(tuple(lock["off_i_by_tablet"]), STANDING_OFF_I_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["i_only"], STANDING_I_ONLY)
        self.assertTrue(lock["i_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertEqual(tuple(lock["d_n4_tokens"]), D_N4_GRAM)
        self.assertEqual(tuple(lock["v_n4_tokens"]), V_N4_GRAM)
        self.assertEqual(tuple(lock["m_n4_tokens"]), M_N4_GRAM)
        self.assertEqual(tuple(lock["n_n6_tokens"]), N_N6_GRAM)
        self.assertEqual(tuple(lock["s_n7_tokens"]), S_N7_GRAM)
        self.assertEqual(tuple(lock["e_n9_tokens"]), E_GRAM_N9)
        self.assertEqual(tuple(lock["er7_4gram_tokens"]), ER7_GRAM4)
        self.assertFalse(lock["same_as_d_n4"])
        self.assertFalse(lock["same_as_v_n4"])
        self.assertFalse(lock["same_as_m_n4"])
        self.assertFalse(lock["same_as_n_n6"])
        self.assertFalse(lock["same_as_s_n7"])
        self.assertFalse(lock["same_as_e_n9"])
        self.assertFalse(lock["same_as_er7_4"])
        self.assertFalse(lock["w_barthel"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_d_echancree_da_d_only_unchanged"])
        self.assertTrue(lock["standing_v_honolulu_va_v_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_s_washington_sb2_s_only_unchanged"])
        self.assertTrue(lock["standing_n_vienna_na1_n_only_unchanged"])
        self.assertTrue(lock["standing_m_vienna_ma2_m_only_unchanged"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_er7_double_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_staff"]["longest_tokens"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_n"], 5)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_freq"], 3)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["eightgram_count"], 0)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_tokens"]),
            GRAM5,
        )
        self.assertTrue(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["tablet_only"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_count"], 5)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["own_hits"], 3)
        self.assertEqual(self.survey["tablet_d_echancree_da_d_only"]["cycle"], 102)
        self.assertTrue(self.survey["tablet_d_echancree_da_d_only"]["d_only"])
        self.assertEqual(tuple(self.survey["tablet_d_echancree_da_d_only"]["tokens4"]), D_N4_GRAM)
        self.assertEqual(self.survey["tablet_v_honolulu_va_v_only"]["cycle"], 101)
        self.assertTrue(self.survey["tablet_v_honolulu_va_v_only"]["v_only"])
        self.assertEqual(tuple(self.survey["tablet_v_honolulu_va_v_only"]["tokens4"]), V_N4_GRAM)
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertEqual(self.survey["tablet_s_washington_sb2_s_only"]["cycle"], 95)
        self.assertTrue(self.survey["tablet_s_washington_sb2_s_only"]["s_only"])
        self.assertEqual(self.survey["tablet_n_vienna_na1_n_only"]["cycle"], 91)
        self.assertTrue(self.survey["tablet_n_vienna_na1_n_only"]["n_only"])
        self.assertEqual(self.survey["tablet_m_vienna_ma2_m_only"]["cycle"], 90)
        self.assertTrue(self.survey["tablet_m_vienna_ma2_m_only"]["m_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSantiagoIaIOnlyImageSnapshot(unittest.TestCase):
    """Cycle 103 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
