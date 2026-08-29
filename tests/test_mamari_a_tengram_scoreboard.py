"""A's distinct repeating n=10 grams (freq≥2 on A).

Cycle 117 text-search lock. Uses already-vendored A–V and the
cycle-36 / cycle-99 / cycle-116 A representative 10-gram. Does
not vendor a new tablet. Does not scrape X. W has no Barthel
(cycle 100); skip W. Does not redo G–K n≥8 inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type merge.
No detector retune. No CV. No new agents. Not a meaning
dictionary.

Enumerates every distinct contiguous 10-gram with freq≥2 on A
(same per-line Barthel parser as the leak table / B eightgram
scoreboards). Hypothesis N=1: only the home-only representative
080 004 280 182 048 022 025 025 009 005. Measured N=1: that
same 10-gram at Aa7[55]/Aa7[88]. Claim that can lose:
a_has_exactly_1_repeating_10gram. The claim is true. Do not
retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from agents.pattern_mining.ngram_analyzer import NgramAnalyzer
from tests.test_mamari_b_eightgram_scoreboard import (
    TestMamariBEightgramScoreboard,
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
from tests.test_mamari_keiti_n9_scoreboard import named_side_hits, site_tuple
from tests.test_mamari_santiago_ia_090_076_071_ngram_scoreboard import (
    ngram_hit_count,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey
from tests.test_mamari_tahua_aa_a_only_scoreboard import (
    GRAM10,
    SIDE_AA,
    SIDE_AB,
    STANDING_AA_SITES as CYCLE_116_AA_SITES,
    TestMamariTahuaAaAOnlyScoreboard,
    load_a_sides,
)
from tests.test_mamari_tahua_aa_10gram_motif_scoreboard import (
    MOTIF_10GRAM,
    TestMamariTahuaAa10gramMotifScoreboard,
)
from tests.test_mamari_tahua_aa_scoreboard import AA_LINE_NAMES
from tests.test_mamari_tahua_ab_scoreboard import AB_LINE_NAMES
from tests.test_mamari_vienna_ma2_m_only_scoreboard import tablet_hit_counts

HYPOTHESIS_N = 1
STANDING_N = 1
STANDING_TENGRAMS = (GRAM10,)
STANDING_FREQS = (2,)
STANDING_SITES = (CYCLE_116_AA_SITES,)
STANDING_HITS_BY_TABLET = (
    tuple(2 if tablet == "A" else 0 for tablet in VENDORED_TABLETS),
)
STANDING_LEAK_COUNTS = ({},)
STANDING_OFF_A_HITS = (0,)
STANDING_A_HITS = (2,)
STANDING_AA_HITS = (2,)
STANDING_AB_HITS = (0,)
STANDING_HOME_IN_SET = True
STANDING_KNOWN_DISTINCT = True
STANDING_A_HAS_EXACTLY_1_REPEATING_10GRAM = True
STANDING_CLAIM = "a_has_exactly_1_repeating_10gram"
STANDING_RESULT = "a_repeating_10grams"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True


def repeating_10grams(
    lines: list[list[str]],
    analyzer: NgramAnalyzer,
) -> tuple[tuple[tuple[str, ...], int], ...]:
    """Distinct contiguous 10-grams with freq≥2. Search only."""
    return tuple(analyzer.extract_ngrams(lines, n=10, min_frequency=2))


def tengram_sites(
    gram: tuple[str, ...],
    a_sides: dict[str, list[list[str]]],
) -> tuple[tuple[str, str, int], ...]:
    """(side, line, index) hits on Aa then Ab. Search only."""
    hits = named_side_hits(a_sides[SIDE_AA], AA_LINE_NAMES, SIDE_AA, gram)
    hits += named_side_hits(a_sides[SIDE_AB], AB_LINE_NAMES, SIDE_AB, gram)
    return tuple(site_tuple(hit) for hit in hits)


def a_has_exactly_1_repeating_10gram(grams: tuple[tuple[str, ...], ...]) -> bool:
    """True iff A has exactly one distinct repeating 10-gram."""
    return len(grams) == HYPOTHESIS_N


def off_a_hit_total(
    hits: tuple[int, ...],
    tablets: tuple[str, ...] = VENDORED_TABLETS,
) -> int:
    """Sum of exact hits off A. Counts only."""
    return sum(leaks_from_hits("A", hits, tablets).values())


class TestATengramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_repeating_filter_and_n_equals_1_can_fail(self):
        """Freq 1 is excluded; a planted second 10-gram makes N=2."""
        provider = MockProvider()
        analyzer = NgramAnalyzer(llm_provider=provider)
        home = GRAM10
        planted = ("X",) * 10
        self.assertNotEqual(home, planted)
        self.assertEqual(len(home), 10)
        self.assertEqual(len(planted), 10)
        self.assertEqual(
            home,
            ("080", "004", "280", "182", "048", "022", "025", "025", "009", "005"),
        )
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        once_each = [list(home), list(planted)]
        self.assertEqual(repeating_10grams(once_each, analyzer), ())
        self.assertFalse(a_has_exactly_1_repeating_10gram(()))
        twice_home = [list(home), list(home)]
        home_only = repeating_10grams(twice_home, analyzer)
        self.assertEqual(home_only, ((home, 2),))
        self.assertTrue(
            a_has_exactly_1_repeating_10gram(tuple(gram for gram, _freq in home_only))
        )
        twice_each = [list(home), list(home), list(planted), list(planted)]
        both = repeating_10grams(twice_each, analyzer)
        self.assertEqual(len(both), 2)
        self.assertFalse(
            a_has_exactly_1_repeating_10gram(tuple(gram for gram, _freq in both))
        )
        gapped = [list(home[:4]) + ["999"] + list(home[4:]), list(home)]
        self.assertEqual(repeating_10grams(gapped, analyzer), ())
        self.assertEqual(ngram_hit_count([[]], home), 0)
        self.assertEqual(STANDING_CLAIM, "a_has_exactly_1_repeating_10gram")
        self.assertTrue(STANDING_A_HAS_EXACTLY_1_REPEATING_10GRAM)
        self.assertEqual(STANDING_N, 1)
        self.assertEqual(STANDING_N, HYPOTHESIS_N)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariATengramScoreboard(unittest.TestCase):
    """Cited-fixture A repeating 10-grams. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.analyzer = NgramAnalyzer(llm_provider=self.provider)
        self.survey = load_corpus_survey()
        self.by_tablet = load_vendored_a_through_v()
        self.a_sides = load_a_sides()
        self.rows = repeating_10grams(self.by_tablet["A"], self.analyzer)
        self.tengrams = tuple(gram for gram, _freq in self.rows)
        self.freqs = tuple(freq for _gram, freq in self.rows)
        self.sites = tuple(tengram_sites(gram, self.a_sides) for gram in self.tengrams)
        self.hits_by_tablet = tuple(
            tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS)
            for gram in self.tengrams
        )
        self.leak_counts = tuple(
            leaks_from_hits("A", hits) for hits in self.hits_by_tablet
        )
        self.off_a_hits = tuple(off_a_hit_total(hits) for hits in self.hits_by_tablet)
        self.claim_holds = a_has_exactly_1_repeating_10gram(self.tengrams)

    def test_tokens_are_cycle_116_not_invented(self):
        """Home-only 10-gram is the cycle-36 / 99 / 116 lock. None invented."""
        self.assertEqual(GRAM10, INVENTORY_LONGEST_TOKENS["A"])
        self.assertEqual(GRAM10, MOTIF_10GRAM)
        self.assertEqual(INVENTORY_LONGEST_N["A"], 10)
        self.assertEqual(len(GRAM10), 10)
        self.assertEqual(
            GRAM10,
            ("080", "004", "280", "182", "048", "022", "025", "025", "009", "005"),
        )
        self.assertEqual(
            tuple(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["longest_tokens"]),
            GRAM10,
        )
        self.assertEqual(tuple(self.survey["tahua_aa_10gram_motif"]["motif_tokens"]), GRAM10)
        self.assertEqual(tuple(self.survey["tablet_a_tahua_aa_a_only"]["tokens10"]), GRAM10)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["cycle"], 37)
        self.assertEqual(self.survey["tablet_a_tahua_aa_a_only"]["cycle"], 116)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertNotIn("W", VENDORED_TABLETS)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_n_is_1_and_hypothesis_n_1_holds(self):
        """Exactly one repeating 10-gram. Claim that can lose is true."""
        self.assertEqual(len(self.tengrams), STANDING_N)
        self.assertEqual(self.tengrams, STANDING_TENGRAMS)
        self.assertEqual(self.freqs, STANDING_FREQS)
        self.assertEqual(STANDING_N, 1)
        self.assertEqual(HYPOTHESIS_N, 1)
        self.assertEqual(STANDING_N, HYPOTHESIS_N)
        self.assertTrue(a_has_exactly_1_repeating_10gram(self.tengrams))
        self.assertEqual(self.claim_holds, STANDING_A_HAS_EXACTLY_1_REPEATING_10GRAM)
        self.assertTrue(STANDING_A_HAS_EXACTLY_1_REPEATING_10GRAM)
        self.assertEqual(STANDING_CLAIM, "a_has_exactly_1_repeating_10gram")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_known_10gram_is_in_the_set(self):
        """Cycle-116 home-only representative is the only member."""
        self.assertIn(GRAM10, self.tengrams)
        self.assertEqual(self.tengrams, (GRAM10,))
        self.assertEqual(STANDING_HOME_IN_SET, True)
        self.assertTrue(STANDING_HOME_IN_SET)
        self.assertEqual(self.survey["tablet_a_tahua_aa_a_only"]["a_hits"], 2)
        self.assertTrue(self.survey["tablet_a_tahua_aa_a_only"]["a_10gram_is_a_only"])
        self.assertEqual(self.provider.get_call_history(), [])

    def test_sites_and_off_a_hits_on_every_vendored_tablet(self):
        """Home-only at Aa7[55]/Aa7[88]; A=2, Ab=0, else 0 on B–V."""
        self.assertEqual(self.sites, STANDING_SITES)
        self.assertEqual(self.hits_by_tablet, STANDING_HITS_BY_TABLET)
        self.assertEqual(self.leak_counts, STANDING_LEAK_COUNTS)
        self.assertEqual(self.off_a_hits, STANDING_OFF_A_HITS)
        self.assertEqual(STANDING_OFF_A_HITS, (0,))
        for gram, sites, hits, leaks, off_hits, freq, aa_hits, ab_hits in zip(
            self.tengrams,
            self.sites,
            self.hits_by_tablet,
            self.leak_counts,
            self.off_a_hits,
            self.freqs,
            STANDING_AA_HITS,
            STANDING_AB_HITS,
            strict=True,
        ):
            self.assertEqual(tengram_sites(gram, self.a_sides), sites)
            self.assertEqual(len(sites), freq)
            self.assertEqual(hits[VENDORED_TABLETS.index("A")], freq)
            self.assertEqual(ngram_hit_count(self.a_sides[SIDE_AA], gram), aa_hits)
            self.assertEqual(ngram_hit_count(self.a_sides[SIDE_AB], gram), ab_hits)
            self.assertEqual(
                tablet_hit_counts(self.by_tablet, gram, VENDORED_TABLETS),
                hits,
            )
            for letter, count in zip(VENDORED_TABLETS, hits, strict=True):
                self.assertEqual(count, ngram_hit_count(self.by_tablet[letter], gram))
                if letter != "A":
                    self.assertEqual(count, 0)
            self.assertEqual(leaks, {})
            self.assertEqual(off_hits, 0)
            for side, line, index in sites:
                names = AA_LINE_NAMES if side == SIDE_AA else AB_LINE_NAMES
                stems = self.a_sides[side][names.index(line)][index : index + 10]
                self.assertEqual(tuple(stems), gram)
                self.assertEqual(side, SIDE_AA)
                self.assertEqual(line, "Aa7")
        self.assertEqual(STANDING_SITES[0], CYCLE_116_AA_SITES)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_116_115_37_and_w_scoreboards_still_compute(self):
        """Cycle 116 A-only, 115 B eightgrams, 37 motif, and W stay."""
        prior_116 = TestMamariTahuaAaAOnlyScoreboard()
        prior_116.setUp()
        prior_116.test_10gram_is_zero_off_a_and_a_only()
        prior_116.test_survey_matches_computed_lock()
        prior_115 = TestMamariBEightgramScoreboard()
        prior_115.setUp()
        prior_115.test_survey_matches_computed_lock()
        prior_motif = TestMamariTahuaAa10gramMotifScoreboard()
        prior_motif.setUp()
        prior_motif.test_survey_matches_computed_lock()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-117 repeating 10-gram lock."""
        lock = self.survey["a_repeating_10grams"]
        self.assertEqual(lock["cycle"], 117)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["n"], 10)
        self.assertEqual(lock["tengram_count"], STANDING_N)
        self.assertEqual(lock["hypothesis_n"], HYPOTHESIS_N)
        self.assertEqual(tuple(tuple(row) for row in lock["tokens"]), STANDING_TENGRAMS)
        self.assertEqual(tuple(lock["freqs"]), STANDING_FREQS)
        self.assertEqual(
            tuple(tuple(tuple(site) for site in row) for row in lock["sites"]),
            STANDING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["hits_by_tablet"]),
            STANDING_HITS_BY_TABLET,
        )
        self.assertEqual(tuple(lock["a_hits"]), STANDING_A_HITS)
        self.assertEqual(tuple(lock["aa_hits"]), STANDING_AA_HITS)
        self.assertEqual(tuple(lock["ab_hits"]), STANDING_AB_HITS)
        self.assertEqual(tuple(lock["off_a_hits"]), STANDING_OFF_A_HITS)
        self.assertEqual(tuple(lock["leak_counts"]), STANDING_LEAK_COUNTS)
        self.assertEqual(tuple(lock["home_tokens10"]), GRAM10)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["known_distinct"], STANDING_KNOWN_DISTINCT)
        self.assertTrue(lock["home_in_set"])
        self.assertEqual(lock["home_in_set"], STANDING_HOME_IN_SET)
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["a_has_exactly_1_repeating_10gram"])
        self.assertEqual(
            lock["a_has_exactly_1_repeating_10gram"],
            STANDING_A_HAS_EXACTLY_1_REPEATING_10GRAM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_tahua_aa_a_only_unchanged"])
        self.assertTrue(lock["standing_tahua_aa_10gram_motif_unchanged"])
        self.assertTrue(lock["standing_b_repeating_8grams_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_a_tahua_aa_a_only"]["cycle"], 116)
        self.assertTrue(self.survey["tablet_a_tahua_aa_a_only"]["a_10gram_is_a_only"])
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["cycle"], 37)
        self.assertEqual(self.survey["tahua_aa_10gram_motif"]["motif_freq"], 2)
        self.assertEqual(self.survey["b_repeating_8grams"]["cycle"], 115)
        self.assertFalse(self.survey["b_repeating_8grams"]["b_has_exactly_2_repeating_8grams"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["A"]["longest_count"], 1)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariATengramImageSnapshot(unittest.TestCase):
    """Cycle 117 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
