"""Gr vs Kv longest shared stem n-gram: n, sites, 17-gram relation.

Cycle 66 / focused-batch 5 of 5. Uses only the already-vendored
Gr.html and Kv.html parsers. No new tablet. Cycle 61 already
reported Gr vs Kv longest shared n=15; this lock pins that exact
stem, its line/index on each side, and how the sequence sits on
the cycle-61/62 17-gram (prefix, suffix, overlap, or disjoint).
Raw stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents.

Stem ids only — not meanings. Image stays parked Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

from dataclasses import dataclass
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_second_passage_scoreboard import (
    find_ngram_hits,
    load_corpus_survey,
)
from tests.test_mamari_small_london_kv_scoreboard import KV_LINE_NAMES
from tests.test_mamari_small_santiago_gr_scoreboard import GR_LINE_NAMES
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import (
    GRAM_17,
    PASSAGE_GR,
    PASSAGE_KV,
    STANDING_COMBINED_N,
    STANDING_NEW_TABLET,
    STANDING_STEM_076_IN_LONGEST,
)
from tests.test_mamari_small_santiago_london_380_001_003_scoreboard import (
    GRAM_3,
    TestMamariSmallSantiagoLondon380001003Scoreboard,
)
from tests.test_mamari_small_santiago_london_parallel_ngram_scoreboard import (
    SIDE_GR,
    SIDE_KV,
    STANDING_GR_KV_FREQ,
    STANDING_GR_KV_N,
    STANDING_GR_KV_TOKENS,
    load_g_k_sides,
    longest_shared_ngram,
)

REL_PREFIX = "prefix"
REL_SUFFIX = "suffix"
REL_OVERLAP = "overlap"
REL_DISJOINT = "disjoint"
RELATIONS = (REL_PREFIX, REL_SUFFIX, REL_OVERLAP, REL_DISJOINT)

GRAM_15 = STANDING_GR_KV_TOKENS
STANDING_N = STANDING_GR_KV_N
STANDING_GR_SITE = (PASSAGE_GR, "Gr7", 0)
STANDING_KV_SITE = (PASSAGE_KV, "Kv4", 7)
STANDING_SITES = (STANDING_GR_SITE, STANDING_KV_SITE)
STANDING_SITE_COUNT = 2
STANDING_RELATION = REL_OVERLAP
STANDING_SHARED_RUN = GRAM_3
STANDING_FREQ = STANDING_GR_KV_FREQ


@dataclass(frozen=True)
class SharedSite:
    """One exact Gr/Kv 15-gram hit. Ids only; no meanings."""

    passage: str
    line: str
    index: int


def site_tuple(hit: SharedSite) -> tuple[str, str, int]:
    """Stable lock row: passage, line, index."""
    return (hit.passage, hit.line, hit.index)


def longest_shared_run(
    left: tuple[str, ...],
    right: tuple[str, ...],
) -> tuple[str, ...]:
    """Longest exact contiguous shared stem run. Ties: leftmost, then lex."""
    best: tuple[str, ...] = ()
    for i in range(len(left)):
        for j in range(len(right)):
            k = 0
            while (
                i + k < len(left)
                and j + k < len(right)
                and left[i + k] == right[j + k]
            ):
                k += 1
            if k > len(best) or (k == len(best) and k > 0 and left[i : i + k] < best):
                best = left[i : i + k]
    return best


def gram_relation(
    needle: tuple[str, ...],
    haystack: tuple[str, ...],
) -> str:
    """How needle sits on haystack: prefix, suffix, overlap, or disjoint."""
    n = len(needle)
    if n == 0 or not haystack:
        return REL_DISJOINT
    if n <= len(haystack) and haystack[:n] == needle:
        return REL_PREFIX
    if n <= len(haystack) and haystack[-n:] == needle:
        return REL_SUFFIX
    if longest_shared_run(needle, haystack):
        return REL_OVERLAP
    return REL_DISJOINT


def score_shared_sites(
    lines: list[list[str]],
    gram: tuple[str, ...],
    line_names: tuple[str, ...],
    passage: str,
) -> tuple[SharedSite, ...]:
    """Exact hits of gram as (passage, line, index). Search only."""
    return tuple(
        SharedSite(passage, line_names[line_index], start)
        for line_index, start in find_ngram_hits(lines, gram)
    )


def score_gr_kv_15gram(
    by_side: dict[str, list[list[str]]],
) -> tuple[object, tuple[SharedSite, ...], str]:
    """Longest Gr vs Kv shared n-gram, both sites, 17-gram relation."""
    shared = longest_shared_ngram(by_side[SIDE_GR], by_side[SIDE_KV])
    sites = score_shared_sites(
        by_side[SIDE_GR],
        shared.tokens,
        GR_LINE_NAMES,
        PASSAGE_GR,
    ) + score_shared_sites(
        by_side[SIDE_KV],
        shared.tokens,
        KV_LINE_NAMES,
        PASSAGE_KV,
    )
    return shared, sites, gram_relation(shared.tokens, GRAM_17)


class TestSmallSantiagoLondonGrKv15gramHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_relation_prefix_suffix_overlap_disjoint(self):
        """Prefix and suffix beat overlap; a shared run is overlap; none is disjoint."""
        provider = MockProvider()
        self.assertEqual(gram_relation(GRAM_17[:3], GRAM_17), REL_PREFIX)
        self.assertEqual(gram_relation(GRAM_17[-3:], GRAM_17), REL_SUFFIX)
        self.assertEqual(gram_relation(("001", "003", "315"), GRAM_17), REL_OVERLAP)
        self.assertEqual(gram_relation(("079", "450", "019"), GRAM_17), REL_DISJOINT)
        self.assertEqual(gram_relation((), GRAM_17), REL_DISJOINT)
        self.assertEqual(gram_relation(GRAM_15, GRAM_17), REL_OVERLAP)
        self.assertEqual(longest_shared_run(GRAM_15, GRAM_17), STANDING_SHARED_RUN)
        self.assertEqual(STANDING_RELATION, REL_OVERLAP)
        self.assertNotIn(STANDING_RELATION, (REL_PREFIX, REL_SUFFIX, REL_DISJOINT))
        self.assertEqual(provider.get_call_history(), [])

    def test_sites_follow_line_names(self):
        """Scorer walks find_ngram_hits; missing name is an error."""
        provider = MockProvider()
        lines = [list(GRAM_15), ["X"] + list(GRAM_15)]
        names = ("L0", "L1")
        hits = score_shared_sites(lines, GRAM_15, names, "synth")
        self.assertEqual(
            tuple(site_tuple(hit) for hit in hits),
            (("synth", "L0", 0), ("synth", "L1", 1)),
        )
        self.assertEqual(score_shared_sites([[]], GRAM_15, ("L0",), "empty"), ())
        self.assertEqual(len(GRAM_15), STANDING_N)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonGrKv15gramScoreboard(unittest.TestCase):
    """Cited-fixture Gr vs Kv 15-gram site and 17-gram relation lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_side = load_g_k_sides()
        self.shared, self.sites, self.relation = score_gr_kv_15gram(self.by_side)
        self.locked = tuple(site_tuple(hit) for hit in self.sites)

    def test_n_tokens_sites_and_17gram_relation(self):
        """Gr vs Kv longest n=15 at Gr7[0] / Kv4[7]; overlaps the 17-gram."""
        self.assertEqual(self.shared.n, STANDING_N)
        self.assertEqual(self.shared.tokens, GRAM_15)
        self.assertEqual(len(self.shared.tokens), STANDING_N)
        self.assertEqual(STANDING_N, 15)
        self.assertEqual(
            (self.shared.freq_left, self.shared.freq_right),
            STANDING_FREQ,
        )
        self.assertEqual(self.locked, STANDING_SITES)
        self.assertEqual(len(self.sites), STANDING_SITE_COUNT)
        self.assertEqual(site_tuple(self.sites[0]), STANDING_GR_SITE)
        self.assertEqual(site_tuple(self.sites[1]), STANDING_KV_SITE)
        self.assertEqual(self.sites[0].line, "Gr7")
        self.assertEqual(self.sites[0].index, 0)
        self.assertEqual(self.sites[1].line, "Kv4")
        self.assertEqual(self.sites[1].index, 7)
        self.assertEqual(self.relation, STANDING_RELATION)
        self.assertEqual(gram_relation(GRAM_15, GRAM_17), REL_OVERLAP)
        self.assertEqual(longest_shared_run(GRAM_15, GRAM_17), STANDING_SHARED_RUN)
        self.assertEqual(STANDING_SHARED_RUN, GRAM_3)
        self.assertNotEqual(gram_relation(GRAM_15, GRAM_17), REL_PREFIX)
        self.assertNotEqual(gram_relation(GRAM_15, GRAM_17), REL_SUFFIX)
        self.assertNotEqual(gram_relation(GRAM_15, GRAM_17), REL_DISJOINT)
        self.assertEqual(len(GRAM_17), STANDING_COMBINED_N)
        self.assertEqual("076" in GRAM_15, STANDING_STEM_076_IN_LONGEST)
        self.assertFalse(STANDING_STEM_076_IN_LONGEST)
        self.assertEqual(
            len(find_ngram_hits(self.by_side[SIDE_GR], GRAM_15)),
            STANDING_FREQ[0],
        )
        self.assertEqual(
            len(find_ngram_hits(self.by_side[SIDE_KV], GRAM_15)),
            STANDING_FREQ[1],
        )
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_380_001_003_scoreboard_still_computes(self):
        """Cycle 65 twelve-row 380 001 003 table stays."""
        prior = TestMamariSmallSantiagoLondon380001003Scoreboard()
        prior.setUp()
        prior.test_twelve_row_hit_table()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-66 Gr vs Kv 15-gram lock."""
        lock = self.survey["tablet_g_k_gr_kv_15gram_sites"]
        self.assertEqual(lock["cycle"], 66)
        self.assertEqual(lock["focused_batch"], 5)
        self.assertEqual(lock["focused_batch_of"], 5)
        self.assertEqual(lock["n"], STANDING_N)
        self.assertEqual(tuple(lock["tokens"]), GRAM_15)
        self.assertEqual(tuple(lock["gr_site"]), STANDING_GR_SITE)
        self.assertEqual(tuple(lock["kv_site"]), STANDING_KV_SITE)
        locked = tuple(
            (passage, line, index) for passage, line, index in lock["sites"]
        )
        self.assertEqual(locked, STANDING_SITES)
        self.assertEqual(lock["relation_to_17gram"], STANDING_RELATION)
        self.assertEqual(tuple(lock["shared_run_with_17gram"]), STANDING_SHARED_RUN)
        self.assertEqual(lock["freq_gr"], STANDING_FREQ[0])
        self.assertEqual(lock["freq_kv"], STANDING_FREQ[1])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["stem_076_in_gram"])
        self.assertTrue(lock["standing_aa_locks_unchanged"])
        self.assertTrue(lock["standing_ab_locks_unchanged"])
        self.assertTrue(lock["standing_br_locks_unchanged"])
        self.assertTrue(lock["standing_bv_locks_unchanged"])
        self.assertTrue(lock["standing_c_locks_unchanged"])
        self.assertTrue(lock["standing_ia_locks_unchanged"])
        self.assertTrue(lock["standing_gr_locks_unchanged"])
        self.assertTrue(lock["standing_gv_locks_unchanged"])
        self.assertTrue(lock["standing_kr_locks_unchanged"])
        self.assertTrue(lock["standing_kv_locks_unchanged"])
        self.assertTrue(lock["standing_gk_parallel_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_hits_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_sites_unchanged"])
        self.assertTrue(lock["standing_gk_17gram_hamming_unchanged"])
        self.assertTrue(lock["standing_gk_380_001_003_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["tablet_g_k_380_001_003_hits_per_fixture"]["cycle"],
            65,
        )
        self.assertEqual(self.survey["tablet_g_k_17gram_nearest_hamming"]["cycle"], 64)
        self.assertEqual(self.survey["tablet_g_k_17gram_hit_sites"]["cycle"], 63)
        self.assertEqual(self.survey["tablet_g_k_17gram_hits_per_fixture"]["cycle"], 62)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondonGrKv15gramImageSnapshot(unittest.TestCase):
    """Cycle 66 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
