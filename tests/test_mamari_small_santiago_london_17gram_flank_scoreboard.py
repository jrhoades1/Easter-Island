"""G–K 17-gram hit sites and one-token flanks.

Cycle 63 / focused-batch 2 of 5. Uses only the already-vendored
fixtures. No new tablet. Exact 17-gram from cycle 61/62. Raw stems.
No invented Barthel. No G00n→Barthel map. No type merge. No
detector retune. No CV. No new agents.

Locks the line/index of each cycle-62 hit and the left/right flank
stems (one token, or START/END at a line edge). Also locks whether
the two hits share the same flanks. Stem ids only — not meanings.
Image stays parked Hamming 6.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest
from dataclasses import dataclass

from agents.base.providers import MockProvider
from tests.test_mamari_second_passage_scoreboard import (
    find_ngram_hits,
    load_corpus_survey,
)
from tests.test_mamari_small_london_kr_scoreboard import KR_LINE_NAMES
from tests.test_mamari_small_santiago_gr_scoreboard import GR_LINE_NAMES
from tests.test_mamari_small_santiago_london_17gram_hit_scoreboard import (
    GRAM_17,
    PASSAGE_GR,
    PASSAGE_KR,
    STANDING_COMBINED_N,
    STANDING_STEM_076_IN_LONGEST,
    TestMamariSmallSantiagoLondon17gramHitScoreboard,
    existing_gk_17gram_lines,
)

FLANK_START = "START"
FLANK_END = "END"

# (passage, line, index, before, after)
STANDING_GR_SITE = (PASSAGE_GR, "Gr4", 3, "001", "003")
STANDING_KR_SITE = (PASSAGE_KR, "Kr5", 0, FLANK_START, "316")
STANDING_SITES = (STANDING_GR_SITE, STANDING_KR_SITE)
STANDING_SITE_COUNT = 2
STANDING_SAME_FLANKS = False
STANDING_NEW_TABLET = False
SITE_PASSAGES = (
    (PASSAGE_GR, GR_LINE_NAMES),
    (PASSAGE_KR, KR_LINE_NAMES),
)


@dataclass(frozen=True)
class SiteHit:
    """One exact 17-gram hit with one-token flanks. Ids only."""

    passage: str
    line: str
    index: int
    before: str
    after: str


def site_flanks(
    sequence: list[str],
    start: int,
    n: int,
) -> tuple[str, str]:
    """Token immediately before and after [start, start+n), or START/END."""
    before = sequence[start - 1] if start > 0 else FLANK_START
    end = start + n
    after = sequence[end] if end < len(sequence) else FLANK_END
    return before, after


def site_tuple(hit: SiteHit) -> tuple:
    """Stable lock row: passage, line, index, before, after."""
    return (hit.passage, hit.line, hit.index, hit.before, hit.after)


def same_flanks(left: SiteHit, right: SiteHit) -> bool:
    """True iff both hits have the same one-token left and right flanks."""
    return (left.before, left.after) == (right.before, right.after)


def score_site_hits(
    lines: list[list[str]],
    gram: tuple[str, ...],
    line_names: tuple[str, ...],
    passage: str,
) -> tuple[SiteHit, ...]:
    """Exact hits of gram with START/END flanks. Search only."""
    n = len(gram)
    hits: list[SiteHit] = []
    for line_index, start in find_ngram_hits(lines, gram):
        before, after = site_flanks(lines[line_index], start, n)
        hits.append(
            SiteHit(
                passage=passage,
                line=line_names[line_index],
                index=start,
                before=before,
                after=after,
            )
        )
    return tuple(hits)


def score_gk_17gram_sites(
    by_passage: dict[str, list[list[str]]],
    gram: tuple[str, ...] = GRAM_17,
) -> tuple[SiteHit, ...]:
    """Gr and Kr 17-gram sites with flanks. Search only."""
    hits: list[SiteHit] = []
    for passage, names in SITE_PASSAGES:
        hits.extend(score_site_hits(by_passage[passage], gram, names, passage))
    return tuple(hits)


class TestSmallSantiagoLondon17gramFlankHelpers(unittest.TestCase):
    """Helpers on synthetic sequences. No CV, no LLM."""

    def test_flanks_medial_and_line_edge(self):
        """Medial hits keep neighbors; start/end of line is START/END."""
        provider = MockProvider()
        gram = GRAM_17
        lines = [list(gram), ["X"] + list(gram) + ["Y"]]
        names = ("L0", "L1")
        hits = score_site_hits(lines, gram, names, "synth")
        self.assertEqual(
            tuple(site_tuple(hit) for hit in hits),
            (
                ("synth", "L0", 0, FLANK_START, FLANK_END),
                ("synth", "L1", 1, "X", "Y"),
            ),
        )
        self.assertEqual(site_flanks(list(gram), 0, len(gram)), (FLANK_START, FLANK_END))
        self.assertEqual(len(gram), STANDING_COMBINED_N)
        self.assertEqual(provider.get_call_history(), [])

    def test_same_flanks_compares_both_sides(self):
        """Shared flanks are True only when both sides match."""
        provider = MockProvider()
        match = (
            SiteHit("g", "Gr4", 3, "001", "003"),
            SiteHit("k", "Kr5", 0, "001", "003"),
        )
        miss = (
            SiteHit("g", "Gr4", 3, "001", "003"),
            SiteHit("k", "Kr5", 0, FLANK_START, "316"),
        )
        self.assertTrue(same_flanks(*match))
        self.assertFalse(same_flanks(*miss))
        self.assertEqual(score_site_hits([[]], GRAM_17, ("L0",), "empty"), ())
        self.assertEqual(provider.get_call_history(), [])


class TestMamariSmallSantiagoLondon17gramFlankScoreboard(unittest.TestCase):
    """Cited-fixture G–K 17-gram site and flank lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.by_passage = existing_gk_17gram_lines()
        self.sites = score_gk_17gram_sites(self.by_passage)
        self.locked = tuple(site_tuple(hit) for hit in self.sites)

    def test_gr_and_kr_hit_sites_and_flanks(self):
        """Gr4[3] flanks 001/003; Kr5[0] flanks START/316; flanks differ."""
        self.assertEqual(self.locked, STANDING_SITES)
        self.assertEqual(len(self.sites), STANDING_SITE_COUNT)
        self.assertEqual(site_tuple(self.sites[0]), STANDING_GR_SITE)
        self.assertEqual(site_tuple(self.sites[1]), STANDING_KR_SITE)
        self.assertEqual(self.sites[0].line, "Gr4")
        self.assertEqual(self.sites[0].index, 3)
        self.assertEqual((self.sites[0].before, self.sites[0].after), ("001", "003"))
        self.assertEqual(self.sites[1].line, "Kr5")
        self.assertEqual(self.sites[1].index, 0)
        self.assertEqual((self.sites[1].before, self.sites[1].after), (FLANK_START, "316"))
        self.assertEqual(same_flanks(self.sites[0], self.sites[1]), STANDING_SAME_FLANKS)
        self.assertFalse(STANDING_SAME_FLANKS)
        self.assertEqual(len(GRAM_17), STANDING_COMBINED_N)
        self.assertEqual("076" in GRAM_17, STANDING_STEM_076_IN_LONGEST)
        self.assertFalse(STANDING_STEM_076_IN_LONGEST)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_gk_17gram_hit_scoreboard_still_computes(self):
        """Cycle 62 twelve-row 17-gram hit table stays."""
        prior = TestMamariSmallSantiagoLondon17gramHitScoreboard()
        prior.setUp()
        prior.test_twelve_row_hit_table()
        prior.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-63 17-gram site/flank lock."""
        lock = self.survey["tablet_g_k_17gram_hit_sites"]
        self.assertEqual(lock["cycle"], 63)
        self.assertEqual(lock["focused_batch"], 2)
        self.assertEqual(lock["focused_batch_of"], 5)
        self.assertEqual(tuple(lock["tokens"]), GRAM_17)
        self.assertEqual(lock["n"], STANDING_COMBINED_N)
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertFalse(lock["new_tablet"])
        self.assertEqual(tuple(lock["gr_site"]), STANDING_GR_SITE)
        self.assertEqual(tuple(lock["kr_site"]), STANDING_KR_SITE)
        self.assertEqual(
            tuple(tuple(row) for row in lock["sites"]),
            STANDING_SITES,
        )
        self.assertEqual(lock["same_flanks"], STANDING_SAME_FLANKS)
        self.assertEqual(tuple(lock["edge_markers"]), (FLANK_START, FLANK_END))
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
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["tablet_g_k_17gram_hits_per_fixture"]["cycle"], 62)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariSmallSantiagoLondon17gramFlankImageSnapshot(unittest.TestCase):
    """Cycle 63 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
