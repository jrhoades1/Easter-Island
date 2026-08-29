"""B's distinct repeating n=8 grams (freq≥2 on B).

Cycle 115 text-search lock. Uses already-vendored A–V and the
cycle-99 / cycle-114 B representative plus the cycle-106
doubled 8-gram suffix. Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Does not redo
G–K n≥8 inventories. Raw stems. No invented Barthel. No
G00n→Barthel map. No type merge. No detector retune. No CV. No
new agents. Not a meaning dictionary.

Enumerates every distinct contiguous 8-gram with freq≥2 on B
(same per-line Barthel parser as the leak table / E eightgram
scoreboards). Hypothesis N=2: the home-only representative and
the G–K doubled suffix. The doubled suffix has freq=1 on B, so
it is not repeating. Measured N=1: only 002 065 042 300 385 003
065 200. Claim that can lose: b_has_exactly_2_repeating_8grams.
The claim is false. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_aruku_br_scoreboard import BR_LINE_NAMES
from tests.test_mamari_aruku_bv_scoreboard import BV_LINE_NAMES
from tests.test_mamari_b_gk_doubled_8gram_scoreboard import (
    GRAM8,
    TestMamariBGkDoubled8GramScoreboard,
)
from tests.test_mamari_b_max_n_gk_doubled_8gram_scoreboard import (
    GRAM8_B,
    STANDING_B_SITES as CYCLE_114_B_SITES,
    TestMamariBMaxNGkDoubled8GramScoreboard,
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
from tests.test_mamari_corpus_max_n_leak_table_scoreboard import leaks_from_hits
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import load_b_sides
from tests.test_mamari_keiti_eightgram_scoreboard import (
    TestMamariKeitiEightgramScoreboard,
)
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

SIDE_BR = "Br"
SIDE_BV = "Bv"
HYPOTHESIS_N = 2
STANDING_N = 1
STANDING_EIGHTGRAMS = (GRAM8_B,)
STANDING_FREQS = (2,)
STANDING_SITES = (CYCLE_114_B_SITES,)
STANDING_HITS_BY_TABLET = (
    (
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ),
)
STANDING_LEAK_COUNTS = ({},)
STANDING_OFF_B_HITS = (0,)
STANDING_B_HITS = (2,)
STANDING_BR_HITS = (0,)
STANDING_BV_HITS = (2,)
STANDING_HOME_IN_SET = True
STANDING_DOUBLED_IN_SET = False
STANDING_KNOWN_DISTINCT = True
STANDING_DOUBLED_B_FREQ = 1
STANDING_DOUBLED_B_SITES = ((SIDE_BV, "Bv8", 21),)
STANDING_B_HAS_EXACTLY_2_REPEATING_8GRAMS = False
STANDING_CLAIM = "b_has_exactly_2_repeating_8grams"
STANDING_RESULT = "b_repeating_8grams"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def repeating_8grams(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
) -> tuple[tuple[tuple[str, ...], int], ...]:
    """Distinct contiguous 8-grams with freq≥2. Search only."""
    return tuple(analyzer.extract_ngrams(lines, n=8, min_frequency=2))


def eightgram_sites(
    gram: tuple[str, ...],
    b_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Br then Bv. Search only."""
    hits = named_side_hits(b_sides[SIDE_BR], BR_LINE_NAMES, SIDE_BR, gram)
    hits += named_side_hits(b_sides[SIDE_BV], BV_LINE_NAMES, SIDE_BV, gram)
    return tuple(site_tuple(hit) for hit in hits)


def b_has_exactly_2_repeating_8grams(grams: tuple[tuple[str, ...], ...]) -> bool:
    """True iff B has exactly two distinct repeating 8-grams."""
    return len(grams) == HYPOTHESIS_N


def off_b_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off B. Counts only."""
    return sum(leaks_from_hits("B", hits, tablets).values())


class TestBEightgramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_n_equals_2_can_fail(self):
        """Freq 1 is excluded; a planted second 8-gram makes N=2."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = GRAM8_B
        doubled = GRAM8
        self.assertNotEqual(home, doubled)
        self.assertEqual(len(home), 8)
        self.assertEqual(len(doubled), 8)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(doubled)]
        self.assertEqual(repeating_8grams(once_each, analyzer), ())
        self.assertFalse(b_has_exactly_2_repeating_8grams(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_8grams(twice_home, analyzer)
        self.assertEqual(home_only, ((home, 2),))
        self.assertFalse(
            b_has_exactly_2_repeating_8grams(tuple(gram for gram, _freq in home_only))
        )
        twice_each = [list(home), list(home), list(doubled), list(doubled)]
        both = repeating_8grams(twice_each, analyzer)
        self.assertEqual(len(both), HYPOTHESIS_N)
        self.assertTrue(
            b_has_exactly_2_repeating_8grams(tuple(gram for gram, _freq in both))
        )
        gapped = [list(home[:4]) + ["999"] + list(home[4:]), list(home)]
        self.assertEqual(repeating_8grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "b_has_exactly_2_repeating_8grams")
        self.assertFalse(STANDING_B_HAS_EXACTLY_2_REPEATING_8GRAMS)
        self.assertEqual(STANDING_N, 1)
        self.assertNotEqual(STANDING_N, HYPOTHESIS_N)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariBEightgramScoreboard(unittest.TestCase):
    """Cited-fixture B repeating 8-grams. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.b_sides = load_b_sides()
        self.rows = repeating_8grams(self.by_tablet["B"], self.analyzer)
        self.eightgrams = tuple(gram for gram, _freq in self.rows)
        self.freqs = tuple(freq for _gram, freq in self.rows)
        self.sites = tuple(
            eightgram_sites(gram, self.b_sides) for gram in self.eightgrams
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in self.eightgrams
        )
        self.leak_counts = tuple(
            leaks_from_hits("B", hits) for hits in self.hits_by_tablet
        )
        self.off_b_hits = tuple(off_b_hit_total(hits) for hits in self.hits_by_tablet)
        self.claim_holds = b_has_exactly_2_repeating_8grams(self.eightgrams)
        self.doubled_b_freq = ngram_hit_count(self.by_tablet["B"], GRAM8)

    def test_tokens_are_cycle_99_and_106_not_invented(self):
        """Home-only and doubled 8-grams are prior locks. None invented."""
        self.assertEqual(GRAM8_B, INVENTORY_LONGEST_TOKENS["B"])
        self.assertEqual(INVENTORY_LONGEST_N["B"], 8)
        self.assertEqual(len(GRAM8_B), 8)
        self.assertEqual(
            GRAM8_B,
            ("002", "065", "042", "300", "385", "003", "065", "200"),
        )
        self.assertEqual(
            GRAM8,
            ("260", "001", "004", "711", "260", "001", "004", "711"),
        )
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["B"]["longest_tokens"]),
            GRAM8_B,
        )
        self.assertEqual(
            tuple(self.survey["b_max_n_gk_doubled_8gram"]["tokens8"]),
            GRAM8_B,
        )
        self.assertEqual(tuple(self.survey["b_gk_doubled_8gram"]["tokens8"]), GRAM8)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["b_max_n_gk_doubled_8gram"]["cycle"], 114)
        self.assertEqual(self.survey["b_gk_doubled_8gram"]["cycle"], 106)
        self.assertNotEqual(GRAM8_B, GRAM8)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n_is_1_and_hypothesis_n_2_loses(self):
        """Exactly one repeating 8-gram. Claim that can lose is false."""
        self.assertEqual(len(self.eightgrams), STANDING_N)
        self.assertEqual(self.eightgrams, STANDING_EIGHTGRAMS)
        self.assertEqual(self.freqs, STANDING_FREQS)
        self.assertEqual(STANDING_N, 1)
        self.assertEqual(HYPOTHESIS_N, 2)
        self.assertNotEqual(STANDING_N, HYPOTHESIS_N)
        self.assertFalse(b_has_exactly_2_repeating_8grams(self.eightgrams))
        self.assertEqual(self.claim_holds, STANDING_B_HAS_EXACTLY_2_REPEATING_8GRAMS)
        self.assertFalse(STANDING_B_HAS_EXACTLY_2_REPEATING_8GRAMS)
        self.assertEqual(STANDING_CLAIM, "b_has_exactly_2_repeating_8grams")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_known_8grams_are_distinct_and_only_home_repeats(self):
        """Home-only is in the set; doubled suffix is freq 1, not repeating."""
        self.assertNotEqual(GRAM8_B, GRAM8)
        self.assertIn(GRAM8_B, self.eightgrams)
        self.assertNotIn(GRAM8, self.eightgrams)
        self.assertEqual(STANDING_HOME_IN_SET, True)
        self.assertEqual(STANDING_DOUBLED_IN_SET, False)
        self.assertTrue(STANDING_HOME_IN_SET)
        self.assertFalse(STANDING_DOUBLED_IN_SET)
        self.assertEqual(self.doubled_b_freq, STANDING_DOUBLED_B_FREQ)
        self.assertEqual(STANDING_DOUBLED_B_FREQ, 1)
        self.assertLess(STANDING_DOUBLED_B_FREQ, 2)
        self.assertEqual(
            eightgram_sites(GRAM8, self.b_sides),
            STANDING_DOUBLED_B_SITES,
        )
        self.assertEqual(self.survey["b_gk_doubled_8gram"]["b_hits"], 1)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_sites_and_off_b_hits_on_every_vendored_tablet(self):
        """Home-only at Bv5[18]/Bv6[39]; B=2, else 0 on A–V."""
        self.assertEqual(self.sites, STANDING_SITES)
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.leak_counts, STANDING_LEAK_COUNTS)
        self.assertEqual(self.off_b_hits, STANDING_OFF_B_HITS)
        self.assertEqual(STANDING_OFF_B_HITS, (0,))
        for gram, sites, hits, leaks, off_hits, freq, br_hits, bv_hits in zip(
            self.eightgrams,
            self.sites,
            self.hits_by_tablet,
            self.leak_counts,
            self.off_b_hits,
            self.freqs,
            STANDING_BR_HITS,
            STANDING_BV_HITS,
            strict=True,
        ):
            self.assertEqual(eightgram_sites(gram, self.b_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("B")], freq)
            self.assertEqual(ngram_hit_count(self.b_sides[SIDE_BR], gram), br_hits)
            self.assertEqual(ngram_hit_count(self.b_sides[SIDE_BV], gram), bv_hits)
            self.assertEqual(tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS), hits)
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "B":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks, {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                names = BR_LINE_NAMES if side == SIDE_BR else BV_LINE_NAMES
                stems = self.b_sides[side][names.index(line)][index : index + 8]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_BV)
        self.assertEqual(STANDING_SITES[0], CYCLE_114_B_SITES)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_e_eightgram_114_106_and_w_scoreboards_still_compute(self):
        """Cycle 83 E eightgrams, 114, 106, and W stay."""
        prior_e = TestMamariKeitiEightgramScoreboard()
        prior_e.setUp()
        prior_e.test_eightgrams_sequences_and_sites()
        prior_e.test_survey_matches_computed_lock()
        prior_114 = TestMamariBMaxNGkDoubled8GramScoreboard()
        prior_114.setUp()
        prior_114.test_b_max_n_is_not_the_gk_doubled_8gram()
        prior_114.test_survey_matches_computed_lock()
        prior_106 = TestMamariBGkDoubled8GramScoreboard()
        prior_106.setUp()
        prior_106.test_8gram_hits_on_every_vendored_tablet()
        prior_106.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-115 repeating 8-gram lock."""
        lock = self.survey["b_repeating_8grams"]
        self.assertEqual(lock["cycle"], 115)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["n"], 8)
        self.assertEqual(lock["eightgram_count"], STANDING_N)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(tuple(tuple(row) for row in lock["tokens"]), STANDING_EIGHTGRAMS)
        self.assertEqual(tuple(lock["freqs"]), STANDING_FREQS)
        self.assertEqual(
            tuple(tuple(tuple(site) for site in row) for row in lock["sites"]),
            STANDING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["hits_by_tablet"]),
            STANDING_HITS_BY_TABLET,
        )
        self.assertEqual(tuple(lock["b_hits"]), STANDING_B_HITS)
        self.assertEqual(tuple(lock["br_hits"]), STANDING_BR_HITS)
        self.assertEqual(tuple(lock["bv_hits"]), STANDING_BV_HITS)
        self.assertEqual(tuple(lock["off_b_hits"]), STANDING_OFF_B_HITS)
        self.assertEqual(tuple(lock["leak_counts"]), STANDING_LEAK_COUNTS)
        self.assertEqual(tuple(lock["home_tokens8"]), GRAM8_B)
        self.assertEqual(tuple(lock["doubled_tokens8"]), GRAM8)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["home_in_set"])
        self.assertEqual(lock["home_in_set"], STANDING_HOME_IN_SET)
        self.assertFalse(lock["doubled_in_set"])
        self.assertEqual(lock["doubled_in_set"], STANDING_DOUBLED_IN_SET)
        self.assertEqual(lock["doubled_b_freq"], STANDING_DOUBLED_B_FREQ)
        self.assertEqual(
            tuple(tuple(row) for row in lock["doubled_b_sites"]),
            STANDING_DOUBLED_B_SITES,
        )
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["b_has_exactly_2_repeating_8grams"])
        self.assertEqual(
            lock["b_has_exactly_2_repeating_8grams"],
            STANDING_B_HAS_EXACTLY_2_REPEATING_8GRAMS,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_e_keiti_eightgrams_unchanged"])
        self.assertTrue(lock["standing_b_max_n_gk_doubled_8gram_unchanged"])
        self.assertTrue(lock["standing_b_gk_doubled_8gram_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_e_keiti_eightgrams"]["cycle"], 83)
        self.assertEqual(self.survey["tablet_e_keiti_eightgrams"]["eightgram_count"], 4)
        self.assertEqual(self.survey["b_max_n_gk_doubled_8gram"]["cycle"], 114)
        self.assertFalse(self.survey["b_max_n_gk_doubled_8gram"]["b_max_n_is_gk_doubled_8gram"])
        self.assertEqual(self.survey["b_gk_doubled_8gram"]["cycle"], 106)
        self.assertTrue(self.survey["b_gk_doubled_8gram"]["b_has_gk_doubled_8gram"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariBEightgramImageSnapshot(unittest.TestCase):
    """Cycle 115 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
