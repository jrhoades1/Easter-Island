"""Échancrée (D) Da 4-gram off-D lock.

Cycle 102 text-search lock. Uses already-vendored Da/Db from cycle 79
plus already-vendored A–V. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); do not invent W stems.
The 4-gram is the cycle-79 / cycle-99 longest repeating n-gram
(first of two n=4 ties). Cycle 99 already listed D's max as
tablet-only (counts only). Cycle 101 already showed a different
gram is V-only. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

Locks exact hits of 002 200 052 600 on every vendored tablet A–V.
Claim that can lose: d_only (D hits ≥ 2 and off-D hits == 0).
Da is exactly 2; Db is 0; every other vendored tablet is exact-0.
Not an n≥8 island. Not an exact match of the locked Va n=4,
M n=4, N n=6, S n=7, E n=9, or Er7 doubled 4-gram sequences.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from pathlib import Path

from agents.base.providers import MockProvider
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    VENDORED_TABLETS,
    load_vendored_a_through_v,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_N as INVENTORY_D_LONGEST_N,
)
from tests.test_mamari_corpus_longest_n_inventory_scoreboard import (
    STANDING_LONGEST_TOKENS as INVENTORY_LONGEST_TOKENS,
)
from tests.test_mamari_echancree_vendor_scoreboard import (
    DA_HTML_PATH,
    DA_JSON_PATH,
    DA_LINE_NAMES,
    DB_HTML_PATH,
    DB_LINE_NAMES,
    SIDE_DA,
    SIDE_DB,
    TestMamariEchancreeVendorScoreboard,
    load_da_barthel_json,
    load_d_sides,
)
from tests.test_mamari_echancree_vendor_scoreboard import (
    STANDING_EIGHTGRAM_EXISTS as D_EIGHTGRAM_EXISTS,
)
from tests.test_mamari_echancree_vendor_scoreboard import (
    STANDING_LONGEST_N as D_LONGEST_N,
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

GRAM4 = INVENTORY_LONGEST_TOKENS["D"]
OFF_D_TABLETS = tuple(tablet for tablet in VENDORED_TABLETS if tablet != "D")
STANDING_D_HITS = 2
STANDING_DA_HITS = 2
STANDING_DB_HITS = 0
STANDING_DA_SITES = (
    (SIDE_DA, "Da3", 5),
    (SIDE_DA, "Da3", 9),
)
STANDING_DB_SITES = ()
STANDING_DA_SPANS = (("Da3", 5, 9), ("Da3", 9, 13))
STANDING_OFF_D_HITS = 0
STANDING_OFF_D_BY_TABLET = (0,) * len(OFF_D_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_D_HITS if tablet == "D" else 0 for tablet in VENDORED_TABLETS
)
STANDING_D_ONLY = True
STANDING_N_GE_8_ISLAND = False
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_SAME_AS_V_N4 = False
STANDING_SAME_AS_M_N4 = False
STANDING_SAME_AS_N_N6 = False
STANDING_SAME_AS_S_N7 = False
STANDING_SAME_AS_E_N9 = False
STANDING_SAME_AS_ER7_4 = False
STANDING_TIED_COUNT = 2
STANDING_TIED_TOKENS4 = (
    ("002", "200", "052", "600"),
    ("380", "002", "003", "730"),
)
STANDING_RESULT = "d_echancree_da_d_only"
STANDING_CLAIM = "d_only"


def load_vendored_by_tablet() -> dict[str, list[list[str]]]:
    """Already-vendored A–V in letter order. No W stems."""
    raw = load_vendored_a_through_v()
    return {letter: raw[letter] for letter in VENDORED_TABLETS}


def is_d_only(d_hits: int, off_d_hits: int) -> bool:
    """True iff D hits ≥ 2 and off-D hits == 0."""
    return d_hits >= 2 and off_d_hits == 0


class TestEchancreeDaDOnlyHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 4-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(GRAM4, ("002", "200", "052", "600"))
        adjacent = [list(GRAM4), list(GRAM4)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM4), 2)
        overlap = [["002", "200", "052", "600", "002", "200", "052", "600"]]
        self.assertEqual(ngram_hit_count(overlap, GRAM4), 2)
        gapped = [list(GRAM4[:2]) + ["999"] + list(GRAM4[2:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM4), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM4), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_d_only_requires_d_ge_2_and_zero_off_d(self):
        """Boolean is True only when D ≥ 2 and off-D is 0."""
        provider = MockProvider()
        self.assertTrue(is_d_only(2, 0))
        self.assertTrue(is_d_only(3, 0))
        self.assertFalse(is_d_only(2, 1))
        self.assertFalse(is_d_only(1, 0))
        self.assertFalse(is_d_only(0, 0))
        self.assertFalse(is_d_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "d_only")
        self.assertEqual(provider.get_call_history(), [])

    def test_4gram_is_not_locked_v_m_n_s_e_or_er7(self):
        """Da 4-gram is a different string from locked local grams."""
        provider = MockProvider()
        self.assertNotEqual(GRAM4, V_N4_GRAM)
        self.assertNotEqual(GRAM4, M_N4_GRAM)
        self.assertNotEqual(GRAM4, N_N6_GRAM)
        self.assertNotEqual(GRAM4, S_N7_GRAM)
        self.assertNotEqual(GRAM4, E_GRAM_N9)
        self.assertNotEqual(GRAM4, ER7_GRAM4)
        self.assertEqual(V_N4_GRAM, ("048", "010", "048", "010"))
        self.assertEqual(M_N4_GRAM, ("006", "022", "006", "022"))
        self.assertEqual(N_N6_GRAM, ("004", "064", "034", "006", "004", "064"))
        self.assertEqual(S_N7_GRAM, ("004", "660", "081", "004", "660", "081", "004"))
        self.assertEqual(E_GRAM_N9, ("300", "040", "300", "028", "004", "430", "022", "380", "203"))
        self.assertEqual(ER7_GRAM4, ("092", "050", "006", "670"))
        self.assertFalse(STANDING_SAME_AS_V_N4)
        self.assertFalse(STANDING_SAME_AS_M_N4)
        self.assertFalse(STANDING_SAME_AS_N_N6)
        self.assertFalse(STANDING_SAME_AS_S_N7)
        self.assertFalse(STANDING_SAME_AS_E_N9)
        self.assertFalse(STANDING_SAME_AS_ER7_4)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariEchancreeDaDOnlyScoreboard(unittest.TestCase):
    """Cited-fixture Da 4-gram off-D lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_d_sides()
        self.da_sites = named_side_hits(
            self.by_side[SIDE_DA],
            DA_LINE_NAMES,
            SIDE_DA,
            GRAM4,
        )
        self.db_sites = named_side_hits(
            self.by_side[SIDE_DB],
            DB_LINE_NAMES,
            SIDE_DB,
            GRAM4,
        )
        self.da_hits = len(self.da_sites)
        self.db_hits = len(self.db_sites)
        self.d_hits = self.da_hits + self.db_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM4, VENDORED_TABLETS)
        self.off_d_counts = tablet_hit_counts(self.by_tablet, GRAM4, OFF_D_TABLETS)
        self.off_d_hits = sum(self.off_d_counts)

    def test_da3_hits_are_two_adjacent_4grams(self):
        """4-gram is cycle-99 longest; Da3[5] and Da3[9]; not n≥8."""
        self.assertEqual(GRAM4, INVENTORY_LONGEST_TOKENS["D"])
        self.assertEqual(GRAM4, ("002", "200", "052", "600"))
        self.assertEqual(len(GRAM4), D_LONGEST_N)
        self.assertEqual(D_LONGEST_N, 4)
        self.assertEqual(INVENTORY_D_LONGEST_N["D"], 4)
        self.assertEqual(self.da_hits, STANDING_DA_HITS)
        self.assertEqual(STANDING_DA_HITS, 2)
        self.assertEqual(self.da_hits, ngram_hit_count(self.by_side[SIDE_DA], GRAM4))
        self.assertEqual(tuple(site_tuple(hit) for hit in self.da_sites), STANDING_DA_SITES)
        da_json = load_da_barthel_json()
        self.assertEqual(da_json["tablet"], "D")
        self.assertEqual(DA_JSON_PATH.name, "Da_barthel.json")
        for side, line, index in STANDING_DA_SITES:
            names = DA_LINE_NAMES
            stems = self.by_side[side][names.index(line)][index : index + 4]
            self.assertEqual(tuple(stems), GRAM4)
            self.assertEqual(tuple(da_json["stems"][line][index : index + 4]), GRAM4)
            self.assertEqual(side, SIDE_DA)
            self.assertEqual(line, "Da3")
        self.assertEqual(
            tuple((line, start, start + 4) for _side, line, start in STANDING_DA_SITES),
            STANDING_DA_SPANS,
        )
        self.assertFalse(D_EIGHTGRAM_EXISTS)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(len(GRAM4), 4)
        self.assertLess(len(GRAM4), 8)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_da_db_split_is_da3_only(self):
        """Both Da and Db exist. Hits are Da3 only; Db is 0."""
        fixtures = Path(__file__).parent / "fixtures"
        self.assertTrue(DA_HTML_PATH.is_file())
        self.assertTrue(DB_HTML_PATH.is_file())
        self.assertTrue((fixtures / "echancree_da_html" / "Da.html").exists())
        self.assertTrue((fixtures / "echancree_db_html" / "Db.html").exists())
        self.assertEqual(self.da_hits, STANDING_DA_HITS)
        self.assertEqual(self.db_hits, STANDING_DB_HITS)
        self.assertEqual(STANDING_DB_HITS, 0)
        self.assertEqual(self.d_hits, STANDING_D_HITS)
        self.assertEqual(self.d_hits, STANDING_DA_HITS + STANDING_DB_HITS)
        self.assertEqual(STANDING_D_HITS, 2)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.da_sites), STANDING_DA_SITES)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.db_sites), STANDING_DB_SITES)
        self.assertEqual(STANDING_DB_SITES, ())
        self.assertEqual(self.da_hits, ngram_hit_count(self.by_side[SIDE_DA], GRAM4))
        self.assertEqual(self.db_hits, ngram_hit_count(self.by_side[SIDE_DB], GRAM4))
        self.assertEqual(ngram_hit_count(self.by_tablet["D"], GRAM4), STANDING_D_HITS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_4gram_is_zero_off_d_and_d_only(self):
        """4-gram is 0 on A–C and E–V. Da has exactly 2. W is not a tablet."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_D_TABLETS, tuple("ABCEFGHIJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_d_counts, STANDING_OFF_D_BY_TABLET)
        self.assertEqual(self.off_d_hits, STANDING_OFF_D_HITS)
        self.assertEqual(STANDING_OFF_D_HITS, 0)
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM4))
            if tablet == "D":
                self.assertEqual(count, STANDING_D_HITS)
                self.assertEqual(count, 2)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(is_d_only(self.d_hits, self.off_d_hits), STANDING_D_ONLY)
        self.assertTrue(STANDING_D_ONLY)
        self.assertEqual(STANDING_CLAIM, "d_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(GRAM4, ("002", "200", "052", "600"))
        self.assertNotEqual(GRAM4, V_N4_GRAM)
        self.assertNotEqual(GRAM4, M_N4_GRAM)
        self.assertNotEqual(GRAM4, N_N6_GRAM)
        self.assertNotEqual(GRAM4, S_N7_GRAM)
        self.assertNotEqual(GRAM4, E_GRAM_N9)
        self.assertNotEqual(GRAM4, ER7_GRAM4)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_tied_second_4gram_is_also_d_only(self):
        """Cycle 99 longest_count=2; the other n=4 is also D-only."""
        self.assertEqual(STANDING_TIED_COUNT, 2)
        self.assertEqual(STANDING_TIED_TOKENS4[0], GRAM4)
        tied = STANDING_TIED_TOKENS4[1]
        self.assertEqual(tied, ("380", "002", "003", "730"))
        self.assertNotEqual(tied, GRAM4)
        tied_hits = tablet_hit_counts(self.by_tablet, tied, VENDORED_TABLETS)
        self.assertEqual(tied_hits[VENDORED_TABLETS.index("D")], 2)
        self.assertEqual(sum(tied_hits) - tied_hits[VENDORED_TABLETS.index("D")], 0)
        for tablet, count in zip(VENDORED_TABLETS, tied_hits, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], tied))
            if tablet == "D":
                self.assertEqual(count, 2)
            else:
                self.assertEqual(count, 0)
        da_json = load_da_barthel_json()
        self.assertEqual(tuple(da_json["stems"]["Da5"][0:4]), tied)
        self.assertEqual(tuple(da_json["stems"]["Da5"][11:15]), tied)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_d_v_and_inventory_scoreboards_still_compute(self):
        """Cycle 79 D vendor, cycle 99 inventory, and cycle 101 V-only stay."""
        prior_d = TestMamariEchancreeVendorScoreboard()
        prior_d.setUp()
        prior_d.test_longest_repeating_ngram_has_no_8gram()
        prior_d.test_survey_matches_computed_lock()
        prior_v = TestMamariHonolulu3VaVOnlyScoreboard()
        prior_v.setUp()
        prior_v.test_4gram_is_zero_off_v_and_v_only()
        prior_v.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        prior_s = TestMamariWashingtonSb2SOnlyScoreboard()
        prior_s.setUp()
        prior_s.test_7gram_is_zero_off_s_and_s_only()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-102 Da D-only lock."""
        lock = self.survey["tablet_d_echancree_da_d_only"]
        self.assertEqual(lock["cycle"], 102)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_d"], "D")
        self.assertEqual(lock["name_d"], "Échancrée")
        self.assertEqual(tuple(lock["tokens4"]), GRAM4)
        self.assertEqual(lock["n4"], 4)
        self.assertEqual(lock["d_hits"], STANDING_D_HITS)
        self.assertEqual(lock["da_hits"], STANDING_DA_HITS)
        self.assertEqual(lock["db_hits"], STANDING_DB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["da_sites"]),
            STANDING_DA_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["db_sites"]), STANDING_DB_SITES)
        self.assertEqual(lock["tied_count"], STANDING_TIED_COUNT)
        self.assertEqual(
            tuple(tuple(row) for row in lock["tied_tokens4"]),
            STANDING_TIED_TOKENS4,
        )
        self.assertFalse(lock["eightgram_exists"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertEqual(lock["off_d_hits"], STANDING_OFF_D_HITS)
        self.assertEqual(tuple(lock["off_d_tablets"]), OFF_D_TABLETS)
        self.assertEqual(tuple(lock["off_d_by_tablet"]), STANDING_OFF_D_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["d_only"], STANDING_D_ONLY)
        self.assertTrue(lock["d_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertEqual(tuple(lock["v_n4_tokens"]), V_N4_GRAM)
        self.assertEqual(tuple(lock["m_n4_tokens"]), M_N4_GRAM)
        self.assertEqual(tuple(lock["n_n6_tokens"]), N_N6_GRAM)
        self.assertEqual(tuple(lock["s_n7_tokens"]), S_N7_GRAM)
        self.assertEqual(tuple(lock["e_n9_tokens"]), E_GRAM_N9)
        self.assertEqual(tuple(lock["er7_4gram_tokens"]), ER7_GRAM4)
        self.assertFalse(lock["same_as_v_n4"])
        self.assertFalse(lock["same_as_m_n4"])
        self.assertFalse(lock["same_as_n_n6"])
        self.assertFalse(lock["same_as_s_n7"])
        self.assertFalse(lock["same_as_e_n9"])
        self.assertFalse(lock["same_as_er7_4"])
        self.assertFalse(lock["w_barthel"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["standing_v_honolulu_va_v_only_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_d_echancree_vendor_unchanged"])
        self.assertTrue(lock["standing_s_washington_sb2_s_only_unchanged"])
        self.assertTrue(lock["standing_n_vienna_na1_n_only_unchanged"])
        self.assertTrue(lock["standing_m_vienna_ma2_m_only_unchanged"])
        self.assertTrue(lock["standing_e_keiti_vendor_unchanged"])
        self.assertTrue(lock["standing_e_keiti_er7_double_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_d_echancree_vendor"]["cycle"], 79)
        self.assertEqual(self.survey["tablet_d_echancree_vendor"]["longest_n"], 4)
        self.assertFalse(self.survey["tablet_d_echancree_vendor"]["eightgram_exists"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["D"]["longest_tokens"]),
            GRAM4,
        )
        self.assertTrue(self.survey["corpus_longest_n_inventory"]["rows"]["D"]["tablet_only"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["D"]["longest_count"], 2)
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


class TestMamariEchancreeDaDOnlyImageSnapshot(unittest.TestCase):
    """Cycle 102 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
