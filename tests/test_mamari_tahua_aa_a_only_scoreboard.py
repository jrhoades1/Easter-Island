"""Tahua (A) Aa 10-gram off-A lock.

Cycle 116 text-search lock. Uses already-vendored Aa/Ab from cycles
36–38 plus already-vendored A–V. Does not vendor a new tablet. Does
not scrape X. W has no Barthel (cycle 100); do not invent W stems.
The 10-gram is the cycle-36 / cycle-99 longest repeating n-gram
(only n=10; longest_count=1). Cycle 37 already locked it as an Aa
motif (C-absent). Cycle 99 already listed A's max as tablet-only
(counts only). Cycle 104 already listed A as exact-0 off home.
A has not been locked as home-only at max n the way D/V/I/M/N/S
were. Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a meaning
dictionary.

Locks exact hits of 080 004 280 182 048 022 025 025 009 005 on
every vendored tablet A–V. Claim that can lose: a_10gram_is_a_only
(A hits ≥ 2 and off-A hits == 0). Aa is exactly 2; Ab is 0; every
other vendored tablet is exact-0. Not a shared n≥8 island (cycle
99/104 island_status stays null). Not an exact match of the locked
I n=5, D n=4, Va n=4, M n=4, N n=6, S n=7, E n=9, Er7 doubled
4-gram, or B n=8 sequences.

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
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_small_vienna_vendor_scoreboard import (
    STANDING_LONGEST_NGRAM as N_N6_GRAM,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import (
    MOTIF_10GRAM,
    TestMamariTahuaAa10gramMotifScoreboard,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    AA_HTML_PATH,
    AA_LINE_NAMES,
    TestMamariTahuaAaScoreboard,
    aa_line_stems,
    extract_aa_published_tokens,
    load_vendored_aa_html,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    STANDING_EIGHTGRAM_COUNT as A_EIGHTGRAM_COUNT,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    STANDING_LONGEST_N as A_LONGEST_N,
)
from tests.test_mamari_tahua_aa_scoreboard import (
    STANDING_LONGEST_NGRAM as A_N10_GRAM,
)
from tests.test_mamari_tahua_ab_scoreboard import (
    AB_HTML_PATH,
    AB_LINE_NAMES,
    ab_line_stems,
    extract_ab_published_tokens,
    load_vendored_ab_html,
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

SIDE_AA = "Aa"
SIDE_AB = "Ab"
GRAM10 = INVENTORY_LONGEST_TOKENS["A"]
D_N4_GRAM = INVENTORY_LONGEST_TOKENS["D"]
I_N5_GRAM = INVENTORY_LONGEST_TOKENS["I"]
B_N8_GRAM = INVENTORY_LONGEST_TOKENS["B"]
OFF_A_TABLETS = tuple(tablet for tablet in VENDORED_TABLETS if tablet != "A")
STANDING_A_HITS = 2
STANDING_AA_HITS = 2
STANDING_AB_HITS = 0
STANDING_AA_SITES = (
    (SIDE_AA, "Aa7", 55),
    (SIDE_AA, "Aa7", 88),
)
STANDING_AB_SITES = ()
STANDING_AA_SPANS = (("Aa7", 55, 65), ("Aa7", 88, 98))
STANDING_OFF_A_HITS = 0
STANDING_OFF_A_BY_TABLET = (0,) * len(OFF_A_TABLETS)
STANDING_HITS_BY_TABLET = tuple(
    STANDING_A_HITS if tablet == "A" else 0 for tablet in VENDORED_TABLETS
)
STANDING_A_10GRAM_IS_A_ONLY = True
STANDING_N_GE_8_ISLAND = False
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
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
STANDING_RESULT = "a_tahua_aa_a_only"
STANDING_CLAIM = "a_10gram_is_a_only"


def load_a_sides() -> dict[str, list[list[str]]]:
    """Already-vendored Aa and Ab. No new A scrape."""
    return {
        SIDE_AA: aa_line_stems(extract_aa_published_tokens(load_vendored_aa_html())),
        SIDE_AB: ab_line_stems(extract_ab_published_tokens(load_vendored_ab_html())),
    }


def load_vendored_by_tablet() -> dict[str, list[list[str]]]:
    """Already-vendored A–V in letter order. No W stems."""
    raw = load_vendored_a_through_v()
    return {letter: raw[letter] for letter in VENDORED_TABLETS}


def a_10gram_is_a_only(a_hits: int, off_a_hits: int) -> bool:
    """True iff A hits ≥ 2 and off-A hits == 0."""
    return a_hits >= 2 and off_a_hits == 0


class TestTahuaAaAOnlyHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_counts_require_consecutive_tokens(self):
        """Adjacent 10-gram counts; a gap is not a hit."""
        provider = MockProvider()
        self.assertEqual(
            GRAM10,
            ("080", "004", "280", "182", "048", "022", "025", "025", "009", "005"),
        )
        adjacent = [list(GRAM10), list(GRAM10)]
        self.assertEqual(ngram_hit_count(adjacent, GRAM10), 2)
        overlap = [list(GRAM10) + list(GRAM10)]
        self.assertEqual(ngram_hit_count(overlap, GRAM10), 2)
        gapped = [list(GRAM10[:4]) + ["999"] + list(GRAM10[4:])]
        self.assertEqual(ngram_hit_count(gapped, GRAM10), 0)
        self.assertEqual(ngram_hit_count([[]], GRAM10), 0)
        self.assertEqual(provider.get_call_history(), [])

    def test_a_only_requires_a_ge_2_and_zero_off_a(self):
        """Boolean is True only when A ≥ 2 and off-A is 0."""
        provider = MockProvider()
        self.assertTrue(a_10gram_is_a_only(2, 0))
        self.assertTrue(a_10gram_is_a_only(3, 0))
        self.assertFalse(a_10gram_is_a_only(2, 1))
        self.assertFalse(a_10gram_is_a_only(1, 0))
        self.assertFalse(a_10gram_is_a_only(0, 0))
        self.assertFalse(a_10gram_is_a_only(0, 3))
        self.assertEqual(STANDING_CLAIM, "a_10gram_is_a_only")
        self.assertEqual(provider.get_call_history(), [])

    def test_10gram_is_not_locked_i_d_v_m_n_s_e_er7_or_b(self):
        """Aa 10-gram is a different string from locked local grams."""
        provider = MockProvider()
        self.assertNotEqual(GRAM10, I_N5_GRAM)
        self.assertNotEqual(GRAM10, D_N4_GRAM)
        self.assertNotEqual(GRAM10, V_N4_GRAM)
        self.assertNotEqual(GRAM10, M_N4_GRAM)
        self.assertNotEqual(GRAM10, N_N6_GRAM)
        self.assertNotEqual(GRAM10, S_N7_GRAM)
        self.assertNotEqual(GRAM10, E_GRAM_N9)
        self.assertNotEqual(GRAM10, ER7_GRAM4)
        self.assertNotEqual(GRAM10, B_N8_GRAM)
        self.assertNotEqual(GRAM10, GRAM8_B)
        self.assertEqual(I_N5_GRAM, ("999", "071", "076", "010", "079"))
        self.assertEqual(D_N4_GRAM, ("002", "200", "052", "600"))
        self.assertEqual(V_N4_GRAM, ("048", "010", "048", "010"))
        self.assertEqual(M_N4_GRAM, ("006", "022", "006", "022"))
        self.assertEqual(N_N6_GRAM, ("004", "064", "034", "006", "004", "064"))
        self.assertEqual(S_N7_GRAM, ("004", "660", "081", "004", "660", "081", "004"))
        self.assertEqual(E_GRAM_N9, ("300", "040", "300", "028", "004", "430", "022", "380", "203"))
        self.assertEqual(ER7_GRAM4, ("092", "050", "006", "670"))
        self.assertEqual(B_N8_GRAM, ("002", "065", "042", "300", "385", "003", "065", "200"))
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


class TestMamariTahuaAaAOnlyScoreboard(unittest.TestCase):
    """Cited-fixture Aa 10-gram off-A lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_a_sides()
        self.aa_sites = named_side_hits(
            self.by_side[SIDE_AA],
            AA_LINE_NAMES,
            SIDE_AA,
            GRAM10,
        )
        self.ab_sites = named_side_hits(
            self.by_side[SIDE_AB],
            AB_LINE_NAMES,
            SIDE_AB,
            GRAM10,
        )
        self.aa_hits = len(self.aa_sites)
        self.ab_hits = len(self.ab_sites)
        self.a_hits = self.aa_hits + self.ab_hits
        self.by_tablet = load_vendored_by_tablet()
        self.hits_by_tablet = tablet_hit_counts(self.by_tablet, GRAM10, VENDORED_TABLETS)
        self.off_a_counts = tablet_hit_counts(self.by_tablet, GRAM10, OFF_A_TABLETS)
        self.off_a_hits = sum(self.off_a_counts)

    def test_aa7_hits_are_two_10grams(self):
        """10-gram is cycle-99 longest; Aa7[55] and Aa7[88]; not a shared island."""
        self.assertEqual(GRAM10, A_N10_GRAM)
        self.assertEqual(GRAM10, INVENTORY_LONGEST_TOKENS["A"])
        self.assertEqual(GRAM10, MOTIF_10GRAM)
        self.assertEqual(
            GRAM10,
            ("080", "004", "280", "182", "048", "022", "025", "025", "009", "005"),
        )
        self.assertEqual(
            tuple(self.survey["tablet_a_tahua_side_a"]["longest_tokens"]),
            GRAM10,
        )
        self.assertEqual(
            tuple(self.survey["tahua_aa_10gram_motif"]["motif_tokens"]),
            GRAM10,
        )
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["longest_tokens"]),
            GRAM10,
        )
        self.assertEqual(len(GRAM10), A_LONGEST_N)
        self.assertEqual(A_LONGEST_N, 10)
        self.assertEqual(INVENTORY_LONGEST_N["A"], 10)
        self.assertEqual(self.aa_hits, STANDING_AA_HITS)
        self.assertEqual(STANDING_AA_HITS, 2)
        self.assertEqual(self.aa_hits, ngram_hit_count(self.by_side[SIDE_AA], GRAM10))
        self.assertEqual(tuple(site_tuple(hit) for hit in self.aa_sites), STANDING_AA_SITES)
        published = extract_aa_published_tokens(load_vendored_aa_html())
        stems = aa_line_stems(published)
        for side, line, index in STANDING_AA_SITES:
            names = AA_LINE_NAMES
            line_stems = self.by_side[side][names.index(line)][index : index + 10]
            self.assertEqual(tuple(line_stems), GRAM10)
            self.assertEqual(tuple(stems[names.index(line)][index : index + 10]), GRAM10)
            self.assertEqual(side, SIDE_AA)
            self.assertEqual(line, "Aa7")
        self.assertEqual(
            tuple((line, start, start + 10) for _side, line, start in STANDING_AA_SITES),
            STANDING_AA_SPANS,
        )
        self.assertEqual(
            [tuple(span) for span in self.survey["tahua_aa_10gram_motif"]["motif_spans"]],
            list(STANDING_AA_SPANS),
        )
        self.assertEqual(STANDING_LONGEST_COUNT, 1)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["longest_count"], 1)
        self.assertEqual(A_EIGHTGRAM_COUNT, 3)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(len(GRAM10), 10)
        self.assertGreaterEqual(len(GRAM10), 8)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_aa_ab_split_is_aa7_only(self):
        """Both Aa and Ab exist. Hits are Aa7 only; Ab is 0."""
        fixtures = Path(__file__).parent / "fixtures"
        self.assertTrue(AA_HTML_PATH.is_file())
        self.assertTrue(AB_HTML_PATH.is_file())
        self.assertTrue((fixtures / "tahua_aa_html" / "Aa.html").exists())
        self.assertTrue((fixtures / "tahua_ab_html" / "Ab.html").exists())
        self.assertEqual(self.aa_hits, STANDING_AA_HITS)
        self.assertEqual(self.ab_hits, STANDING_AB_HITS)
        self.assertEqual(STANDING_AB_HITS, 0)
        self.assertEqual(self.a_hits, STANDING_A_HITS)
        self.assertEqual(self.a_hits, STANDING_AA_HITS + STANDING_AB_HITS)
        self.assertEqual(STANDING_A_HITS, 2)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.aa_sites), STANDING_AA_SITES)
        self.assertEqual(tuple(site_tuple(hit) for hit in self.ab_sites), STANDING_AB_SITES)
        self.assertEqual(STANDING_AB_SITES, ())
        self.assertEqual(self.aa_hits, ngram_hit_count(self.by_side[SIDE_AA], GRAM10))
        self.assertEqual(self.ab_hits, ngram_hit_count(self.by_side[SIDE_AB], GRAM10))
        self.assertEqual(ngram_hit_count(self.by_tablet["A"], GRAM10), STANDING_A_HITS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_10gram_is_zero_off_a_and_a_only(self):
        """10-gram is 0 on B–V. Aa has exactly 2. W is not a tablet."""
        self.assertEqual(tuple(self.by_tablet), VENDORED_TABLETS)
        self.assertEqual(VENDORED_TABLETS, tuple("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertNotIn("W", self.by_tablet)
        self.assertEqual(OFF_A_TABLETS, tuple("BCDEFGHIJKLMNOPQRSTUV"))
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.off_a_counts, STANDING_OFF_A_BY_TABLET)
        self.assertEqual(self.off_a_hits, STANDING_OFF_A_HITS)
        self.assertEqual(STANDING_OFF_A_HITS, 0)
        for tablet, count in zip(VENDORED_TABLETS, self.hits_by_tablet, strict=True):
            self.assertEqual(count, ngram_hit_count(self.by_tablet[tablet], GRAM10))
            if tablet == "A":
                self.assertEqual(count, STANDING_A_HITS)
                self.assertEqual(count, 2)
            else:
                self.assertEqual(count, 0)
        self.assertEqual(
            a_10gram_is_a_only(self.a_hits, self.off_a_hits),
            STANDING_A_10GRAM_IS_A_ONLY,
        )
        self.assertTrue(STANDING_A_10GRAM_IS_A_ONLY)
        self.assertEqual(STANDING_CLAIM, "a_10gram_is_a_only")
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(
            GRAM10,
            ("080", "004", "280", "182", "048", "022", "025", "025", "009", "005"),
        )
        self.assertNotEqual(GRAM10, I_N5_GRAM)
        self.assertNotEqual(GRAM10, D_N4_GRAM)
        self.assertNotEqual(GRAM10, V_N4_GRAM)
        self.assertNotEqual(GRAM10, M_N4_GRAM)
        self.assertNotEqual(GRAM10, N_N6_GRAM)
        self.assertNotEqual(GRAM10, S_N7_GRAM)
        self.assertNotEqual(GRAM10, E_GRAM_N9)
        self.assertNotEqual(GRAM10, ER7_GRAM4)
        self.assertNotEqual(GRAM10, B_N8_GRAM)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_a_i_and_inventory_scoreboards_still_compute(self):
        """Cycle 37 motif, cycle 99/104 inventory, and cycle 103 I-only stay."""
        prior_aa = TestMamariTahuaAaScoreboard()
        prior_aa.setUp()
        prior_aa.test_longest_n_top_8gram_and_stem_count()
        prior_motif = TestMamariTahuaAa10gramMotifScoreboard()
        prior_motif.setUp()
        prior_motif.test_aa_motif_tokens_freq_spans_and_flanks()
        prior_motif.test_survey_matches_computed_lock()
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
        """CORPUS_SURVEY.json records the cycle-116 Aa A-only lock."""
        lock = self.survey["tablet_a_tahua_aa_a_only"]
        self.assertEqual(lock["cycle"], 116)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["tablet_a"], "A")
        self.assertEqual(lock["name_a"], "Tahua")
        self.assertEqual(tuple(lock["tokens10"]), GRAM10)
        self.assertEqual(lock["n10"], 10)
        self.assertEqual(lock["a_hits"], STANDING_A_HITS)
        self.assertEqual(lock["aa_hits"], STANDING_AA_HITS)
        self.assertEqual(lock["ab_hits"], STANDING_AB_HITS)
        self.assertEqual(
            tuple(tuple(row) for row in lock["aa_sites"]),
            STANDING_AA_SITES,
        )
        self.assertEqual(tuple(tuple(row) for row in lock["ab_sites"]), STANDING_AB_SITES)
        self.assertEqual(lock["longest_count"], STANDING_LONGEST_COUNT)
        self.assertEqual(lock["eightgram_count"], A_EIGHTGRAM_COUNT)
        self.assertTrue(lock["eightgram_exists"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertEqual(lock["off_a_hits"], STANDING_OFF_A_HITS)
        self.assertEqual(tuple(lock["off_a_tablets"]), OFF_A_TABLETS)
        self.assertEqual(tuple(lock["off_a_by_tablet"]), STANDING_OFF_A_BY_TABLET)
        self.assertEqual(tuple(lock["vendored_tablets"]), VENDORED_TABLETS)
        self.assertEqual(tuple(lock["hits_by_tablet"]), STANDING_HITS_BY_TABLET)
        self.assertEqual(lock["a_10gram_is_a_only"], STANDING_A_10GRAM_IS_A_ONLY)
        self.assertTrue(lock["a_10gram_is_a_only"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertEqual(tuple(lock["i_n5_tokens"]), I_N5_GRAM)
        self.assertEqual(tuple(lock["d_n4_tokens"]), D_N4_GRAM)
        self.assertEqual(tuple(lock["v_n4_tokens"]), V_N4_GRAM)
        self.assertEqual(tuple(lock["m_n4_tokens"]), M_N4_GRAM)
        self.assertEqual(tuple(lock["n_n6_tokens"]), N_N6_GRAM)
        self.assertEqual(tuple(lock["s_n7_tokens"]), S_N7_GRAM)
        self.assertEqual(tuple(lock["e_n9_tokens"]), E_GRAM_N9)
        self.assertEqual(tuple(lock["er7_4gram_tokens"]), ER7_GRAM4)
        self.assertEqual(tuple(lock["b_n8_tokens"]), B_N8_GRAM)
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
        self.assertTrue(lock["standing_tahua_aa_10gram_motif_unchanged"])
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
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_a_tahua_side_a"]["cycle"], 36)
        self.assertEqual(
            tuple(self.survey["tablet_a_tahua_side_a"]["longest_tokens"]),
            GRAM10,
        )
        self.assertEqual(self.survey["tablet_a_tahua_side_a"]["longest_n"], 10)
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["cycle"], 37)
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["motif_freq"], 2)
        self.assertTrue(self.survey["tahua_aa_10gram_motif"]["c_absent"])
        self.assertEqual(self.survey["tablet_a_tahua_side_b"]["cycle"], 38)
        self.assertEqual(self.survey["tablet_a_tahua_side_b"]["motif_10gram_freq"], 0)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["longest_tokens"]),
            GRAM10,
        )
        self.assertTrue(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["tablet_only"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["own_hits"], 2)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["leak_hits"], 0)
        self.assertIsNone(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["island_status"])
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["rows"]["A"]["tablet_only"])
        self.assertEqual(
            tuple(self.survey["corpus_max_n_leak_table"]["rows"]["A"]["hits_by_tablet"]),
            STANDING_HITS_BY_TABLET,
        )
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


class TestMamariTahuaAaAOnlyImageSnapshot(unittest.TestCase):
    """Cycle 116 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
