"""C's distinct repeating n=13 grams (freq≥2 on C).

Cycle 119 text-search lock. Uses already-vendored A–V and the
cycle-24 / cycle-99 / cycle-118 C representative 13-gram. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Does not redo G–K n≥8 inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents. Not a meaning
dictionary.

Enumerates every distinct contiguous 13-gram with freq≥2 on C
(same per-line Barthel parser as the leak table / A tengram
scoreboards). Hypothesis N=1: only the home-only representative
040 040 040 040 040 390 041 378 041 670 008 078 711. Measured
N=1: that same 13-gram at Ca7[1]/Ca8[24]. Claim that can lose:
c_has_exactly_1_repeating_13gram. The claim is true. Do not
retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_a_tengram_scoreboard import (
    TestMamariATengramScoreboard,
)
from tests.test_mamari_b_eightgram_scoreboard import (
    TestMamariBEightgramScoreboard,
)
from tests.test_mamari_ca_c_only_scoreboard import (
    CA_LINE_NAMES,
    GRAM13,
    SIDE_CA,
    SIDE_CB,
    STANDING_CA_SITES as CYCLE_118_CA_SITES,
    TestMamariCaCOnlyScoreboard,
    load_c_sides,
)
from tests.test_mamari_cb_side_b_scoreboard import CB_LINE_NAMES
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
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

HYPOTHESIS_N = 1
STANDING_N = 1
STANDING_THIRTEENGRAMS = (GRAM13,)
STANDING_FREQS = (2,)
STANDING_SITES = (CYCLE_118_CA_SITES,)
STANDING_HITS_BY_TABLET = (
    tuple(2 if tablet == "C" else 0 for tablet in VENDORED_TABLETS),
)
STANDING_LEAK_COUNTS = ({},)
STANDING_OFF_C_HITS = (0,)
STANDING_C_HITS = (2,)
STANDING_CA_HITS = (2,)
STANDING_CB_HITS = (0,)
STANDING_HOME_IN_SET = True
STANDING_KNOWN_DISTINCT = True
STANDING_C_HAS_EXACTLY_1_REPEATING_13GRAM = True
STANDING_CLAIM = "c_has_exactly_1_repeating_13gram"
STANDING_RESULT = "c_repeating_13grams"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def repeating_13grams(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
) -> tuple[tuple[tuple[str, ...], int], ...]:
    """Distinct contiguous 13-grams with freq≥2. Search only."""
    return tuple(analyzer.extract_ngrams(lines, n=13, min_frequency=2))


def thirteengram_sites(
    gram: tuple[str, ...],
    c_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Ca then Cb. Search only."""
    hits = named_side_hits(c_sides[SIDE_CA], CA_LINE_NAMES, SIDE_CA, gram)
    hits += named_side_hits(c_sides[SIDE_CB], CB_LINE_NAMES, SIDE_CB, gram)
    return tuple(site_tuple(hit) for hit in hits)


def c_has_exactly_1_repeating_13gram(grams: tuple[tuple[str, ...], ...]) -> bool:
    """True iff C has exactly one distinct repeating 13-gram."""
    return len(grams) == HYPOTHESIS_N


def off_c_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off C. Counts only."""
    return sum(leaks_from_hits("C", hits, tablets).values())


class TestCThirteengramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_n_equals_1_can_fail(self):
        """Freq 1 is excluded; a planted second 13-gram makes N=2."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = GRAM13
        planted = ("X",) * 13
        self.assertNotEqual(home, planted)
        self.assertEqual(len(home), 13)
        self.assertEqual(len(planted), 13)
        self.assertEqual(
            home,
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
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_13grams(once_each, analyzer), ())
        self.assertFalse(c_has_exactly_1_repeating_13gram(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_13grams(twice_home, analyzer)
        self.assertEqual(home_only, ((home, 2),))
        self.assertTrue(
            c_has_exactly_1_repeating_13gram(tuple(gram for gram, _freq in home_only))
        )
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_13grams(twice_each, analyzer)
        self.assertEqual(len(both), 2)
        self.assertFalse(
            c_has_exactly_1_repeating_13gram(tuple(gram for gram, _freq in both))
        )
        gapped = [list(home[:6]) + ["999"] + list(home[6:]), list(home)]
        self.assertEqual(repeating_13grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "c_has_exactly_1_repeating_13gram")
        self.assertTrue(STANDING_C_HAS_EXACTLY_1_REPEATING_13GRAM)
        self.assertEqual(STANDING_N, 1)
        self.assertEqual(STANDING_N, HYPOTHESIS_N)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariCThirteengramScoreboard(unittest.TestCase):
    """Cited-fixture C repeating 13-grams. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.c_sides = load_c_sides()
        self.rows = repeating_13grams(self.by_tablet["C"], self.analyzer)
        self.thirteengrams = tuple(gram for gram, _freq in self.rows)
        self.freqs = tuple(freq for _gram, freq in self.rows)
        self.sites = tuple(
            thirteengram_sites(gram, self.c_sides) for gram in self.thirteengrams
        )
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in self.thirteengrams
        )
        self.leak_counts = tuple(
            leaks_from_hits("C", hits) for hits in self.hits_by_tablet
        )
        self.off_c_hits = tuple(off_c_hit_total(hits) for hits in self.hits_by_tablet)
        self.claim_holds = c_has_exactly_1_repeating_13gram(self.thirteengrams)

    def test_tokens_are_cycle_118_not_invented(self):
        """Home-only 13-gram is the cycle-24 / 99 / 118 lock. None invented."""
        self.assertEqual(GRAM13, INVENTORY_LONGEST_TOKENS["C"])
        self.assertEqual(INVENTORY_LONGEST_N["C"], 13)
        self.assertEqual(len(GRAM13), 13)
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
        self.assertEqual(tuple(self.survey["tablet_c_mamari_ca_c_only"]["tokens13"]), GRAM13)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["tablet_c_mamari_ca_c_only"]["cycle"], 118)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n_is_1_and_hypothesis_n_1_holds(self):
        """Exactly one repeating 13-gram. Claim that can lose is true."""
        self.assertEqual(len(self.thirteengrams), STANDING_N)
        self.assertEqual(self.thirteengrams, STANDING_THIRTEENGRAMS)
        self.assertEqual(self.freqs, STANDING_FREQS)
        self.assertEqual(STANDING_N, 1)
        self.assertEqual(HYPOTHESIS_N, 1)
        self.assertEqual(STANDING_N, HYPOTHESIS_N)
        self.assertTrue(c_has_exactly_1_repeating_13gram(self.thirteengrams))
        self.assertEqual(self.claim_holds, STANDING_C_HAS_EXACTLY_1_REPEATING_13GRAM)
        self.assertTrue(STANDING_C_HAS_EXACTLY_1_REPEATING_13GRAM)
        self.assertEqual(STANDING_CLAIM, "c_has_exactly_1_repeating_13gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_known_13gram_is_in_the_set(self):
        """Cycle-118 home-only representative is the only member."""
        self.assertIn(GRAM13, self.thirteengrams)
        self.assertEqual(self.thirteengrams, (GRAM13,))
        self.assertEqual(STANDING_HOME_IN_SET, True)
        self.assertTrue(STANDING_HOME_IN_SET)
        self.assertEqual(self.survey["tablet_c_mamari_ca_c_only"]["c_hits"], 2)
        self.assertTrue(self.survey["tablet_c_mamari_ca_c_only"]["c_maxn_is_c_only"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_sites_and_off_c_hits_on_every_vendored_tablet(self):
        """Home-only at Ca7[1]/Ca8[24]; C=2, Cb=0, else 0 on A–V."""
        self.assertEqual(self.sites, STANDING_SITES)
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.leak_counts, STANDING_LEAK_COUNTS)
        self.assertEqual(self.off_c_hits, STANDING_OFF_C_HITS)
        self.assertEqual(STANDING_OFF_C_HITS, (0,))
        for gram, sites, hits, leaks, off_hits, freq, ca_hits, cb_hits in zip(
            self.thirteengrams,
            self.sites,
            self.hits_by_tablet,
            self.leak_counts,
            self.off_c_hits,
            self.freqs,
            STANDING_CA_HITS,
            STANDING_CB_HITS,
            strict=True,
        ):
            self.assertEqual(thirteengram_sites(gram, self.c_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("C")], freq)
            self.assertEqual(ngram_hit_count(self.c_sides[SIDE_CA], gram), ca_hits)
            self.assertEqual(ngram_hit_count(self.c_sides[SIDE_CB], gram), cb_hits)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS),
                hits,
            )
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "C":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks, {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                names = CA_LINE_NAMES if side == SIDE_CA else CB_LINE_NAMES
                stems = self.c_sides[side][names.index(line)][index : index + 13]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_CA)
                self.assertIn(line, ("Ca7", "Ca8"))
        self.assertEqual(STANDING_SITES[0], CYCLE_118_CA_SITES)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_118_117_115_and_w_scoreboards_still_compute(self):
        """Cycle 118 C-only, 117 A tengrams, 115 B eightgrams, and W stay."""
        prior_118 = TestMamariCaCOnlyScoreboard()
        prior_118.setUp()
        prior_118.test_13gram_is_zero_off_c_and_c_only()
        prior_118.test_survey_matches_computed_lock()
        prior_117 = TestMamariATengramScoreboard()
        prior_117.setUp()
        prior_117.test_survey_matches_computed_lock()
        prior_115 = TestMamariBEightgramScoreboard()
        prior_115.setUp()
        prior_115.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-119 repeating 13-gram lock."""
        lock = self.survey["c_repeating_13grams"]
        self.assertEqual(lock["cycle"], 119)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["n"], 13)
        self.assertEqual(lock["thirteengram_count"], STANDING_N)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(tuple(tuple(row) for row in lock["tokens"]), STANDING_THIRTEENGRAMS)
        self.assertEqual(tuple(lock["freqs"]), STANDING_FREQS)
        self.assertEqual(
            tuple(tuple(tuple(site) for site in row) for row in lock["sites"]),
            STANDING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["hits_by_tablet"]),
            STANDING_HITS_BY_TABLET,
        )
        self.assertEqual(tuple(lock["c_hits"]), STANDING_C_HITS)
        self.assertEqual(tuple(lock["ca_hits"]), STANDING_CA_HITS)
        self.assertEqual(tuple(lock["cb_hits"]), STANDING_CB_HITS)
        self.assertEqual(tuple(lock["off_c_hits"]), STANDING_OFF_C_HITS)
        self.assertEqual(tuple(lock["leak_counts"]), STANDING_LEAK_COUNTS)
        self.assertEqual(tuple(lock["home_tokens13"]), GRAM13)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["home_in_set"])
        self.assertEqual(lock["home_in_set"], STANDING_HOME_IN_SET)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["c_has_exactly_1_repeating_13gram"])
        self.assertEqual(
            lock["c_has_exactly_1_repeating_13gram"],
            STANDING_C_HAS_EXACTLY_1_REPEATING_13GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_c_mamari_ca_c_only_unchanged"])
        self.assertTrue(lock["standing_a_repeating_10grams_unchanged"])
        self.assertTrue(lock["standing_b_repeating_8grams_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_c_mamari_ca_c_only"]["cycle"], 118)
        self.assertTrue(self.survey["tablet_c_mamari_ca_c_only"]["c_maxn_is_c_only"])
        self.assertEqual(self.survey["a_repeating_10grams"]["cycle"], 117)
        self.assertTrue(self.survey["a_repeating_10grams"]["a_has_exactly_1_repeating_10gram"])
        self.assertEqual(self.survey["b_repeating_8grams"]["cycle"], 115)
        self.assertFalse(self.survey["b_repeating_8grams"]["b_has_exactly_2_repeating_8grams"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["C"]["longest_count"], 1)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariCThirteengramImageSnapshot(unittest.TestCase):
    """Cycle 119 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
