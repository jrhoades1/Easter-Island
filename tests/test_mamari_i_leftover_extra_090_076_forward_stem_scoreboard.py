"""I's cycle-224 leftover extra 2-gram forward-stem lock.

Cycle 225 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover extra I sites of 2-gram 090 076 (the 56 I
sites that do not sit inside leftover n=4 remaining maximals
090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover extra sites, the leftover n=4 set, or
the already-closed leftover remaining family. Does not vendor
a new tablet. Does not scrape X. W has no Barthel (cycle 100);
skip W. Unpublished Ib is 0. Does not redo H∩P∩Q n≥8 or G–K
inventories. Raw stems. No invented Barthel. No G00n→Barthel
map. No type merge. No detector retune. No CV. No new agents.
Not a meaning dictionary.

For each leftover extra I site, record the next token
immediately after 090 076 when it exists (the X in 090 076 X;
forward 3-gram 090 076 X, and next 4-gram 090 076 X Y when it
exists). Sites with no next token (end of line) are
N_no_next, not a shared stem. Nested-assert N_I=69 /
N_inside=13 / N_leftover=56 from cycle 224; do not retune
cycles 223/224. Cycle 224's two no-next-4-gram sites
(Ia2[174], Ia4[166]) are not the same as no-next-token:
Ia2[174] has next token 000 (line ends after that one token);
only Ia4[166] is true end-of-line. Off-I T sites are not this
cycle. I-only of leftover extra 4-grams is leftover-of-leftover
for a later cycle. 076 071 and 076 070 do not count as this
2-gram. Inside-family sites do not count as leftover extra.

Claim that can lose:
i_leftover_extra_090_076_share_one_forward_stem. True only if
N_with_next>=2 and N_distinct==1. Measured: N_leftover=56,
N_with_next=55, N_no_next=1 at Ia4[166], N_distinct=30,
most frequent next stem G=070 K=8 (report; the claim is
share-one, not exactly-K). Those 8 G sites are the cycle-207
I 090 076 070 sites (already lost share-one, N_distinct=8).
The claim is false. Same claim-shape as cycle 216 (leftover
076 070 share-one-forward-stem lost, N_distinct=11) and
cycle 218 (I 090 076 070 share-one-forward-stem lost,
N_distinct=8). Nested cycle 223 69/3 on T, cycle 222 K=5 /
G=090 076, cycle 207 8/1, cycle 173 leftover 076 071 exactly
5 forward 076 071 076, cycle 172 leftover-34, and cycle 171
43/0 stay. Do not assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_070_forward_stem_scoreboard import (
    STANDING_I_090_076_070_SHARE_ONE_FORWARD_STEM as CYCLE218_SHARE_ONE,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE218_N_DISTINCT,
    STANDING_N_I as CYCLE218_N_I,
    TestMamariI090076070ForwardStemScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
    STANDING_LEFTOVER_NEXT_4GRAMS as CYCLE224_NEXT_4GRAMS,
    STANDING_LEFTOVER_SITES,
    STANDING_N_I as CYCLE224_N_I,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
    leftover_local_4grams,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
    STANDING_N_I as CYCLE171_N_I,
    STANDING_N_OFF_I as CYCLE171_N_OFF_I,
    TestMamariI2gram076071IOnlyScoreboard,
)
from tests.test_mamari_i_2gram_076_071_inside_family_scoreboard import (
    STANDING_N_LEFTOVER as CYCLE172_N_LEFTOVER,
    TestMamariI2gram076071InsideFamilyScoreboard,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_OFF_I,
    STANDING_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_070_i_only_scoreboard import (
    GRAM3 as CYCLE207_GRAM3,
    STANDING_I_SITES as CYCLE207_I_SITES,
    STANDING_N_I as CYCLE207_N_I,
    STANDING_N_OFF_I as CYCLE207_N_OFF_I,
    TestMamariI3gram090076070IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_070_forward_stem_scoreboard import (
    STANDING_I_LEFTOVER_076_070_SHARE_ONE_FORWARD_STEM as CYCLE216_SHARE_ONE,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE216_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE216_N_LEFTOVER,
    leftover_next_stems as leftover_2gram_next_stems,
    site_next_stem as site_2gram_next_stem,
    TestMamariILeftover076070ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    STANDING_I_LEFTOVER_076_071_EXACTLY_5_FORWARD_076_071_076 as CYCLE173_CLAIM,
    STANDING_N_LEFTOVER as CYCLE173_N_LEFTOVER,
    STANDING_N_WITH_FORWARD_076_071_076 as CYCLE173_N_WITH,
    site_forward_3gram,
    site_next_4gram,
    TestMamariILeftover076071Forward076Scoreboard,
)
from tests.test_mamari_i_leftover_076_071_previous_stem_scoreboard import (
    group_sites_by_previous_stem,
    leftover_sites_with_backward,
    leftover_sites_without_backward,
    previous_stem_frequency_table,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_next_2gram_scoreboard import (
    GRAM2 as CYCLE222_GRAM2,
    STANDING_G as CYCLE222_G,
    STANDING_I_LEFTOVER_N4_REMAINING_EXACTLY_5_CONTAIN_090_076 as CYCLE222_CLAIM,
    STANDING_K as CYCLE222_K,
    STANDING_N_REMAINING as CYCLE222_N_REMAINING,
    TestMamariILeftoverN4RemainingNext2gramScoreboard,
    i_leftover_n4_remaining_exactly_5_contain_090_076,
    leftover_n4_family_counts_hold,
    leftover_n4_rows,
    leftover_remaining_n4,
    leftover_remaining_with_g,
)
from tests.test_mamari_i_nge4_scoreboard import (
    nge4_sites,
)
from tests.test_mamari_i_overlap_3gram_inside_two_5grams_scoreboard import (
    line_stems_for_site,
)
from tests.test_mamari_k_max_n_gk_island_substring_scoreboard import (
    is_contiguous_substring,
)
from tests.test_mamari_santiago_ia_i_only_scoreboard import (
    GRAM5,
    IA_LINE_NAMES,
    SIDE_IA,
    TestMamariSantiagoIaIOnlyScoreboard,
    load_i_sides,
)
from tests.test_mamari_second_passage_scoreboard import load_corpus_survey

HYPOTHESIS_SHARE_ONE = True
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_WITH_NEXT = 55
STANDING_N_NO_NEXT = 1
STANDING_NO_NEXT_SITES = ((SIDE_IA, "Ia4", 166),)
STANDING_IA2_174 = (SIDE_IA, "Ia2", 174)
STANDING_IA2_174_NEXT_STEM = "000"
STANDING_N_DISTINCT_NEXT_STEMS = 30
STANDING_N_HAPAX_NEXT_STEMS = 19
STANDING_G = "070"
STANDING_K = 8
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_PER_SITE_NEXT_STEMS = (
    "012",
    "175",
    "755",
    "470",
    "430",
    "070",
    "600",
    "011",
    "384",
    "535",
    "050",
    "700",
    "147",
    "000",
    "070",
    "013",
    "005",
    "087",
    "090",
    "070",
    "386",
    "001",
    "071",
    "087",
    None,
    "071",
    "013",
    "071",
    "071",
    "505",
    "013",
    "013",
    "001",
    "280",
    "070",
    "001",
    "280",
    "070",
    "607",
    "070",
    "057",
    "072",
    "000",
    "530",
    "011",
    "300",
    "013",
    "005",
    "255",
    "700",
    "071",
    "530",
    "070",
    "071",
    "070",
    "670",
)
STANDING_PER_SITE_FORWARD_3GRAMS = tuple(
    (("090", "076", stem) if stem is not None else None)
    for stem in STANDING_PER_SITE_NEXT_STEMS
)
STANDING_PER_SITE_NEXT_4GRAMS = (
    ("090", "076", "012", "076"),
    ("090", "076", "175", "002"),
    ("090", "076", "755", "509"),
    ("090", "076", "470", "700"),
    ("090", "076", "430", "076"),
    ("090", "076", "070", "499"),
    ("090", "076", "600", "002"),
    ("090", "076", "011", "678"),
    ("090", "076", "384", "570"),
    ("090", "076", "535", "076"),
    ("090", "076", "050", "050"),
    ("090", "076", "700", "011"),
    ("090", "076", "147", "076"),
    None,
    ("090", "076", "070", "200"),
    ("090", "076", "013", "073"),
    ("090", "076", "005", "406"),
    ("090", "076", "087", "499"),
    ("090", "076", "090", "076"),
    ("090", "076", "070", "600"),
    ("090", "076", "386", "202"),
    ("090", "076", "001", "048"),
    ("090", "076", "071", "633"),
    ("090", "076", "087", "078"),
    None,
    ("090", "076", "071", "295"),
    ("090", "076", "013", "291"),
    ("090", "076", "071", "007"),
    ("090", "076", "071", "004"),
    ("090", "076", "505", "633"),
    ("090", "076", "013", "076"),
    ("090", "076", "013", "070"),
    ("090", "076", "001", "224"),
    ("090", "076", "280", "139"),
    ("090", "076", "070", "027"),
    ("090", "076", "001", "071"),
    ("090", "076", "280", "067"),
    ("090", "076", "070", "532"),
    ("090", "076", "607", "073"),
    ("090", "076", "070", "071"),
    ("090", "076", "057", "240"),
    ("090", "076", "072", "205"),
    ("090", "076", "000", "076"),
    ("090", "076", "530", "090"),
    ("090", "076", "011", "130"),
    ("090", "076", "300", "000"),
    ("090", "076", "013", "755"),
    ("090", "076", "005", "084"),
    ("090", "076", "255", "067"),
    ("090", "076", "700", "076"),
    ("090", "076", "071", "076"),
    ("090", "076", "530", "499"),
    ("090", "076", "070", "073"),
    ("090", "076", "071", "600"),
    ("090", "076", "070", "000"),
    ("090", "076", "670", "700"),
)
STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN = (
    "012",
    "175",
    "755",
    "470",
    "430",
    "070",
    "600",
    "011",
    "384",
    "535",
    "050",
    "700",
    "147",
    "000",
    "013",
    "005",
    "087",
    "090",
    "386",
    "001",
    "071",
    "505",
    "280",
    "607",
    "057",
    "072",
    "530",
    "300",
    "255",
    "670",
)
STANDING_G_SITES = (
    (SIDE_IA, "Ia2", 10),
    (SIDE_IA, "Ia3", 4),
    (SIDE_IA, "Ia4", 112),
    (SIDE_IA, "Ia7", 68),
    (SIDE_IA, "Ia7", 129),
    (SIDE_IA, "Ia8", 120),
    (SIDE_IA, "Ia14", 97),
    (SIDE_IA, "Ia14", 140),
)
STANDING_NEXT_STEM_FREQUENCY = (
    (
        "070",
        8,
        STANDING_G_SITES,
        (("090", "076", "070"),) * 8,
    ),
    (
        "071",
        6,
        (
            (SIDE_IA, "Ia4", 154),
            (SIDE_IA, "Ia5", 2),
            (SIDE_IA, "Ia5", 23),
            (SIDE_IA, "Ia5", 66),
            (SIDE_IA, "Ia13", 152),
            (SIDE_IA, "Ia14", 105),
        ),
        (("090", "076", "071"),) * 6,
    ),
    (
        "013",
        5,
        (
            (SIDE_IA, "Ia3", 37),
            (SIDE_IA, "Ia5", 6),
            (SIDE_IA, "Ia5", 164),
            (SIDE_IA, "Ia6", 92),
            (SIDE_IA, "Ia13", 67),
        ),
        (("090", "076", "013"),) * 5,
    ),
    (
        "001",
        3,
        (
            (SIDE_IA, "Ia4", 134),
            (SIDE_IA, "Ia6", 134),
            (SIDE_IA, "Ia7", 88),
        ),
        (("090", "076", "001"),) * 3,
    ),
    (
        "011",
        2,
        ((SIDE_IA, "Ia2", 37), (SIDE_IA, "Ia12", 47)),
        (("090", "076", "011"),) * 2,
    ),
    (
        "700",
        2,
        ((SIDE_IA, "Ia2", 159), (SIDE_IA, "Ia13", 143)),
        (("090", "076", "700"),) * 2,
    ),
    (
        "000",
        2,
        ((SIDE_IA, "Ia2", 174), (SIDE_IA, "Ia10", 141)),
        (("090", "076", "000"),) * 2,
    ),
    (
        "005",
        2,
        ((SIDE_IA, "Ia3", 71), (SIDE_IA, "Ia13", 109)),
        (("090", "076", "005"),) * 2,
    ),
    (
        "087",
        2,
        ((SIDE_IA, "Ia3", 87), (SIDE_IA, "Ia4", 162)),
        (("090", "076", "087"),) * 2,
    ),
    (
        "280",
        2,
        ((SIDE_IA, "Ia7", 2), (SIDE_IA, "Ia7", 113)),
        (("090", "076", "280"),) * 2,
    ),
    (
        "530",
        2,
        ((SIDE_IA, "Ia12", 42), (SIDE_IA, "Ia14", 9)),
        (("090", "076", "530"),) * 2,
    ),
    ("012", 1, ((SIDE_IA, "Ia1", 2),), (("090", "076", "012"),)),
    ("175", 1, ((SIDE_IA, "Ia1", 15),), (("090", "076", "175"),)),
    ("755", 1, ((SIDE_IA, "Ia1", 27),), (("090", "076", "755"),)),
    ("470", 1, ((SIDE_IA, "Ia1", 59),), (("090", "076", "470"),)),
    ("430", 1, ((SIDE_IA, "Ia1", 96),), (("090", "076", "430"),)),
    ("600", 1, ((SIDE_IA, "Ia2", 14),), (("090", "076", "600"),)),
    ("384", 1, ((SIDE_IA, "Ia2", 114),), (("090", "076", "384"),)),
    ("535", 1, ((SIDE_IA, "Ia2", 128),), (("090", "076", "535"),)),
    ("050", 1, ((SIDE_IA, "Ia2", 154),), (("090", "076", "050"),)),
    ("147", 1, ((SIDE_IA, "Ia2", 165),), (("090", "076", "147"),)),
    ("090", 1, ((SIDE_IA, "Ia4", 84),), (("090", "076", "090"),)),
    ("386", 1, ((SIDE_IA, "Ia4", 121),), (("090", "076", "386"),)),
    ("505", 1, ((SIDE_IA, "Ia5", 127),), (("090", "076", "505"),)),
    ("607", 1, ((SIDE_IA, "Ia7", 137),), (("090", "076", "607"),)),
    ("057", 1, ((SIDE_IA, "Ia9", 129),), (("090", "076", "057"),)),
    ("072", 1, ((SIDE_IA, "Ia10", 137),), (("090", "076", "072"),)),
    ("300", 1, ((SIDE_IA, "Ia12", 150),), (("090", "076", "300"),)),
    ("255", 1, ((SIDE_IA, "Ia13", 135),), (("090", "076", "255"),)),
    ("670", 1, ((SIDE_IA, "Ia14", 177),), (("090", "076", "670"),)),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_extra_090_076_share_one_forward_stem"
STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM = False
STANDING_RESULT = "i_leftover_extra_090_076_forward_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE216 = False
STANDING_SAME_AS_CYCLE218 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE216 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE218 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN = True


def site_next_stem(
    stems: list[str],
    index: int,
    gram2: tuple[str, ...] = GRAM2,
) -> str | None:
    """Next stem X after 090 076; None at end-of-line or mismatch."""
    n2 = len(gram2)
    if tuple(stems[index : index + n2]) != gram2:
        return None
    next_index = index + n2
    if next_index >= len(stems):
        return None
    return stems[next_index]


def leftover_extra_next_stems(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[str | None, ...]:
    """Per-site next stem or None for the locked leftover extra sites."""
    return tuple(
        site_next_stem(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_extra_forward_3grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site forward 3-gram or None for the locked leftover extra sites."""
    return tuple(
        site_forward_3gram(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_extra_next_4grams(
    i_sides: dict[str, list[list[str]]],
    sites: tuple[tuple[str, str, int], ...] = STANDING_LEFTOVER_SITES,
    gram2: tuple[str, ...] = GRAM2,
) -> tuple[tuple[str, ...] | None, ...]:
    """Per-site next 4-gram or None for the locked leftover extra sites."""
    return tuple(
        site_next_4gram(line_stems_for_site(i_sides, site), site[2], gram2)
        for site in sites
    )


def leftover_sites_with_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites that have a next stem after 090 076."""
    return leftover_sites_with_backward(sites, next_stems)


def leftover_sites_without_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra sites that are end-of-line (no next token)."""
    return leftover_sites_without_backward(sites, next_stems)


def group_sites_by_next_stem(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
) -> tuple[tuple[str, tuple[tuple[str, str, int], ...]], ...]:
    """Distinct next stems in first-seen order, with their sites."""
    return group_sites_by_previous_stem(sites, next_stems)


def next_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    forward_3grams: tuple[tuple[str, ...] | None, ...],
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Next-stem frequency: highest count first, then first-seen."""
    return previous_stem_frequency_table(sites, next_stems, forward_3grams)


def next_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_NEXT_STEM_FREQUENCY,
) -> list[dict]:
    """Survey-shaped next-stem frequency table, highest count first."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "next_stem": stem,
                "count": count,
                "leftover_sites": [list(site) for site in sites],
                "forward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def i_leftover_extra_090_076_share_one_forward_stem(
    n_distinct_next_stems: int,
    n_with_next: int,
) -> bool:
    """True iff N_distinct==1 and N_with_next>=2."""
    return n_distinct_next_stems == 1 and n_with_next >= 2


class TestILeftoverExtra090076ForwardStemHelpers(unittest.TestCase):
    """Helpers on leftover extra I 090 076 next stems. No CV, no LLM."""

    def test_next_requires_stem_after_2gram(self):
        """A next stem is a 3-gram; end-of-line is no-next. One extra token is a stem."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(STANDING_N3, STANDING_N2 + 1)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_012 = ["602", "999", "090", "076", "012", "076"]
        self.assertEqual(site_next_stem(has_012, 2, GRAM2), "012")
        self.assertEqual(
            site_forward_3gram(has_012, 2, GRAM2),
            ("090", "076", "012"),
        )
        self.assertEqual(
            site_next_4gram(has_012, 2, GRAM2),
            ("090", "076", "012", "076"),
        )
        has_070 = ["999", "090", "076", "070", "499"]
        self.assertEqual(site_next_stem(has_070, 1, GRAM2), "070")
        self.assertEqual(
            site_forward_3gram(has_070, 1, GRAM2),
            ("090", "076", "070"),
        )
        one_token_then_eol = ["009", "009", "090", "076", "000"]
        self.assertEqual(site_next_stem(one_token_then_eol, 2, GRAM2), "000")
        self.assertEqual(
            site_forward_3gram(one_token_then_eol, 2, GRAM2),
            ("090", "076", "000"),
        )
        self.assertIsNone(site_next_4gram(one_token_then_eol, 2, GRAM2))
        end_of_line = ["087", "078", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        self.assertIsNone(site_forward_3gram(end_of_line, 2, GRAM2))
        self.assertIsNone(site_next_4gram(end_of_line, 2, GRAM2))
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN)
        self.assertEqual(provider.get_call_history(), [])

    def test_share_one_requires_one_distinct_and_at_least_two_with_next(self):
        """Boolean is True only when N_distinct=1 and N_with_next>=2."""
        provider = MockProvider()
        self.assertTrue(i_leftover_extra_090_076_share_one_forward_stem(1, 2))
        self.assertTrue(i_leftover_extra_090_076_share_one_forward_stem(1, 55))
        self.assertFalse(i_leftover_extra_090_076_share_one_forward_stem(30, 55))
        self.assertFalse(i_leftover_extra_090_076_share_one_forward_stem(11, 11))
        self.assertFalse(i_leftover_extra_090_076_share_one_forward_stem(8, 8))
        self.assertFalse(i_leftover_extra_090_076_share_one_forward_stem(2, 55))
        self.assertFalse(i_leftover_extra_090_076_share_one_forward_stem(1, 1))
        self.assertFalse(i_leftover_extra_090_076_share_one_forward_stem(1, 0))
        self.assertFalse(i_leftover_extra_090_076_share_one_forward_stem(0, 0))
        self.assertEqual(STANDING_CLAIM, "i_leftover_extra_090_076_share_one_forward_stem")
        self.assertFalse(STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM)
        self.assertNotEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM,
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(STANDING_N_DISTINCT_NEXT_STEMS, 30)
        self.assertEqual(STANDING_N_WITH_NEXT, 55)
        self.assertEqual(STANDING_G, "070")
        self.assertEqual(STANDING_K, 8)
        self.assertEqual(provider.get_call_history(), [])

    def test_frequency_table_sorts_highest_count_first_and_skips_none(self):
        """Frequency table is count-desc; no-next sites are omitted."""
        provider = MockProvider()
        sites = STANDING_LEFTOVER_SITES[:6]
        nxt = ("012", "070", "600", "070", None, "012")
        grams = (
            ("090", "076", "012"),
            ("090", "076", "070"),
            ("090", "076", "600"),
            ("090", "076", "070"),
            None,
            ("090", "076", "012"),
        )
        table = next_stem_frequency_table(sites, nxt, grams)
        self.assertEqual(table[0][0], "012")
        self.assertEqual(table[0][1], 2)
        self.assertEqual(table[1][0], "070")
        self.assertEqual(table[1][1], 2)
        self.assertEqual(table[2][0], "600")
        self.assertEqual(table[2][1], 1)
        self.assertEqual(len(table), 3)
        self.assertEqual(leftover_sites_without_next(sites, nxt), (sites[4],))
        self.assertEqual(
            leftover_sites_with_next(sites, nxt),
            (sites[0], sites[1], sites[2], sites[3], sites[5]),
        )
        shared = ("070",) * 6
        shared_grams = (("090", "076", "070"),) * 6
        shared_table = next_stem_frequency_table(sites, shared, shared_grams)
        self.assertEqual(len(shared_table), 1)
        self.assertEqual(shared_table[0][0], "070")
        self.assertEqual(shared_table[0][1], 6)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076ForwardStemScoreboard(unittest.TestCase):
    """Cited-fixture leftover extra 090 076 next-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.leftover_sites = STANDING_LEFTOVER_SITES
        self.next_stems = leftover_extra_next_stems(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.forwards = leftover_extra_forward_3grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.leftover_sites,
            GRAM2,
        )
        self.with_next = leftover_sites_with_next(self.leftover_sites, self.next_stems)
        self.no_next = leftover_sites_without_next(self.leftover_sites, self.next_stems)
        self.first_seen = group_sites_by_next_stem(self.leftover_sites, self.next_stems)
        self.frequency = next_stem_frequency_table(
            self.leftover_sites,
            self.next_stems,
            self.forwards,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = CYCLE224_N_INSIDE
        self.n_leftover = len(self.leftover_sites)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.n_distinct = len(self.first_seen)
        self.g = self.frequency[0][0] if self.frequency else None
        self.k = self.frequency[0][1] if self.frequency else 0
        self.claim_holds = i_leftover_extra_090_076_share_one_forward_stem(
            self.n_distinct,
            self.n_with_next,
        )

    def test_tokens_and_sites_are_cycle_224_leftover_extra_not_retuned(self):
        """2-gram and leftover extra 56 stay the cycle-224/223/222 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_i, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.leftover_sites, STANDING_LEFTOVER_SITES)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_I"], 69)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(prior_224["i_090_076_all_inside_leftover_n4_remaining_family"])
        self.assertFalse(CYCLE224_ALL_INSIDE)
        self.assertEqual(
            tuple(tuple(row) for row in prior_224["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in prior_224["inside_sites"]),
            CYCLE224_INSIDE_SITES,
        )
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertEqual(prior_222["K"], CYCLE222_K)
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(tuple(prior_222["G"]), CYCLE222_G)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertTrue(CYCLE222_CLAIM)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        unused = leftover_2gram_next_stems
        self.assertTrue(callable(unused))
        self.assertTrue(callable(site_2gram_next_stem))
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_30_distinct_next_stems_and_claim_loses(self):
        """N_leftover=56, N_with_next=55, N_distinct=30, G=070 K=8. Claim loses."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 55)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 1)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ((SIDE_IA, "Ia4", 166),))
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_leftover)
        self.assertEqual(55 + 1, 56)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT_NEXT_STEMS)
        self.assertEqual(STANDING_N_DISTINCT_NEXT_STEMS, 30)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "070")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 8)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertGreater(STANDING_K, STANDING_NEXT_STEM_FREQUENCY[1][1])
        if self.n_distinct != 1:
            self.assertFalse(
                i_leftover_extra_090_076_share_one_forward_stem(
                    self.n_distinct,
                    self.n_with_next,
                )
            )
        self.assertNotEqual(self.n_distinct, 1)
        self.assertFalse(
            i_leftover_extra_090_076_share_one_forward_stem(
                self.n_distinct,
                self.n_with_next,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM,
        )
        self.assertFalse(STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM)
        self.assertTrue(HYPOTHESIS_SHARE_ONE)
        self.assertEqual(STANDING_CLAIM, "i_leftover_extra_090_076_share_one_forward_stem")
        self.assertEqual(self.next_stems, STANDING_PER_SITE_NEXT_STEMS)
        self.assertEqual(self.forwards, STANDING_PER_SITE_FORWARD_3GRAMS)
        self.assertEqual(self.next_4grams, STANDING_PER_SITE_NEXT_4GRAMS)
        self.assertEqual(
            tuple(stem for stem, _sites in self.first_seen),
            STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN,
        )
        self.assertEqual(len(STANDING_NEXT_STEM_FREQUENCY), 30)
        self.assertEqual(STANDING_N_HAPAX_NEXT_STEMS, 19)
        hapax = tuple(row for row in self.frequency if row[1] == 1)
        self.assertEqual(len(hapax), STANDING_N_HAPAX_NEXT_STEMS)
        self.assertEqual(
            sum(count for _stem, count, _sites, _grams in self.frequency),
            55,
        )
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE216)
        self.assertFalse(STANDING_SAME_AS_CYCLE218)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE216)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE218)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_frequency_table_and_no_next_token_vs_no_next_4gram(self):
        """Ia4[166] is the only no-next token; Ia2[174] is 000 / no 4-gram. G=070 is cycle 207."""
        self.assertEqual(self.frequency, STANDING_NEXT_STEM_FREQUENCY)
        counts = [row[1] for row in self.frequency]
        self.assertEqual(counts, sorted(counts, reverse=True))
        self.assertEqual(counts[0], 8)
        self.assertEqual(self.frequency[0][0], "070")
        self.assertEqual(self.frequency[0][2], STANDING_G_SITES)
        self.assertEqual(STANDING_G_SITES, CYCLE207_I_SITES)
        self.assertEqual(len(STANDING_G_SITES), CYCLE207_N_I)
        self.assertEqual(CYCLE207_GRAM3, ("090", "076", "070"))
        self.assertEqual(STANDING_LEFTOVER_SITES[13], STANDING_IA2_174)
        self.assertEqual(STANDING_LEFTOVER_SITES[24], STANDING_NO_NEXT_SITES[0])
        self.assertEqual(STANDING_PER_SITE_NEXT_STEMS[13], STANDING_IA2_174_NEXT_STEM)
        self.assertEqual(STANDING_PER_SITE_NEXT_STEMS[13], "000")
        self.assertIsNone(STANDING_PER_SITE_NEXT_STEMS[24])
        self.assertIsNone(STANDING_PER_SITE_NEXT_4GRAMS[13])
        self.assertIsNone(STANDING_PER_SITE_NEXT_4GRAMS[24])
        self.assertIsNone(CYCLE224_NEXT_4GRAMS[13])
        self.assertIsNone(CYCLE224_NEXT_4GRAMS[24])
        self.assertEqual(CYCLE224_NEXT_4GRAMS, STANDING_PER_SITE_NEXT_4GRAMS)
        local = leftover_local_4grams(self.i_sides, STANDING_LEFTOVER_SITES, GRAM2)
        self.assertIsNone(local[13][2])
        self.assertIsNone(local[24][2])
        ia2_stems = line_stems_for_site(self.i_sides, STANDING_IA2_174)
        ia2_index = STANDING_IA2_174[2]
        self.assertEqual(tuple(ia2_stems[ia2_index : ia2_index + STANDING_N2]), GRAM2)
        self.assertEqual(ia2_stems[ia2_index + STANDING_N2], "000")
        self.assertEqual(ia2_index + STANDING_N2, len(ia2_stems) - 1)
        ia4_stems = line_stems_for_site(self.i_sides, STANDING_NO_NEXT_SITES[0])
        ia4_index = STANDING_NO_NEXT_SITES[0][2]
        self.assertEqual(tuple(ia4_stems[ia4_index : ia4_index + STANDING_N2]), GRAM2)
        self.assertEqual(ia4_index + STANDING_N2, len(ia4_stems))
        for site, nxt, fwd3, nxt4 in zip(
            STANDING_LEFTOVER_SITES,
            STANDING_PER_SITE_NEXT_STEMS,
            STANDING_PER_SITE_FORWARD_3GRAMS,
            STANDING_PER_SITE_NEXT_4GRAMS,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(site_next_stem(stems, index, GRAM2), nxt)
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), fwd3)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), nxt4)
            if nxt is None:
                self.assertEqual(index + STANDING_N2, len(stems))
                self.assertIsNone(fwd3)
                self.assertIsNone(nxt4)
            else:
                self.assertLess(index + STANDING_N2, len(stems))
                self.assertEqual(stems[index + STANDING_N2], nxt)
                self.assertEqual(fwd3, ("090", "076", nxt))
                if nxt4 is not None:
                    self.assertEqual(nxt4[:3], fwd3)
                    self.assertEqual(nxt4[:2], GRAM2)
            self.assertEqual(side, SIDE_IA)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
        for stem, count, sites, grams in STANDING_NEXT_STEM_FREQUENCY:
            self.assertEqual(len(sites), count)
            self.assertEqual(len(grams), count)
            for site, gram3 in zip(sites, grams, strict=True):
                self.assertEqual(gram3[2], stem)
                self.assertEqual(gram3[:2], GRAM2)
                self.assertIn(site, STANDING_LEFTOVER_SITES)
        self.assertEqual(IA_LINE_NAMES[1], "Ia2")
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_224_223_222_218_216_207_173_172_and_171_still_compute(self):
        """Cycle 224 69/13/56, 223 69/3, 222 K=5, 218/216 share-one lost, 207 8/1, 173 5, 172 34, 171 43/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
        if prior_224.n_inside != 13 or prior_224.n_leftover != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_223 = TestMamariI2gram090076IOnlyScoreboard()
        prior_223.setUp()
        prior_223.test_i_hits_are_sixty_nine_on_ia()
        prior_223.test_2gram_is_three_off_i_and_not_i_only()
        prior_223.test_survey_matches_computed_lock()
        self.assertEqual(prior_223.i_hits, STANDING_N_I)
        self.assertEqual(prior_223.i_hits, 69)
        self.assertEqual(prior_223.off_i_hits, STANDING_N_OFF_I)
        self.assertEqual(prior_223.off_i_hits, 3)
        self.assertEqual(prior_223.off_i_sites, STANDING_OFF_I_SITES)
        self.assertFalse(prior_223.claim_holds)
        if prior_223.i_hits != 69 or prior_223.off_i_hits != 3:
            self.fail("nested cycle 223 090 076 I-only 69/3 drifted")
        prior_222 = TestMamariILeftoverN4RemainingNext2gramScoreboard()
        prior_222.setUp()
        prior_222.test_remaining_16_and_hypothesis_k_5_holds()
        prior_222.test_survey_matches_computed_lock()
        if not prior_222.claim_holds:
            self.fail("nested cycle 222 leftover remaining K=5 / G=090 076 drifted")
        prior_218 = TestMamariI090076070ForwardStemScoreboard()
        prior_218.setUp()
        prior_218.test_counts_8_distinct_next_stems_and_claim_loses()
        prior_218.test_survey_matches_computed_lock()
        self.assertEqual(prior_218.n_i, CYCLE218_N_I)
        self.assertEqual(prior_218.n_distinct, CYCLE218_N_DISTINCT)
        self.assertFalse(prior_218.claim_holds)
        self.assertFalse(CYCLE218_SHARE_ONE)
        prior_216 = TestMamariILeftover076070ForwardStemScoreboard()
        prior_216.setUp()
        prior_216.test_counts_11_distinct_next_stems_and_claim_loses()
        prior_216.test_survey_matches_computed_lock()
        self.assertEqual(prior_216.n_leftover, CYCLE216_N_LEFTOVER)
        self.assertEqual(prior_216.n_distinct, CYCLE216_N_DISTINCT)
        self.assertFalse(prior_216.claim_holds)
        self.assertFalse(CYCLE216_SHARE_ONE)
        prior_207 = TestMamariI3gram090076070IOnlyScoreboard()
        prior_207.setUp()
        prior_207.test_3gram_is_one_off_i_and_not_i_only()
        prior_207.test_survey_matches_computed_lock()
        self.assertEqual(prior_207.i_hits, CYCLE207_N_I)
        self.assertEqual(prior_207.i_hits, 8)
        self.assertEqual(prior_207.off_i_hits, CYCLE207_N_OFF_I)
        self.assertEqual(prior_207.off_i_hits, 1)
        self.assertFalse(prior_207.claim_holds)
        if prior_207.i_hits != 8 or prior_207.off_i_hits != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        prior_173 = TestMamariILeftover076071Forward076Scoreboard()
        prior_173.setUp()
        prior_173.test_counts_5_of_34_and_hypothesis_n_5_holds()
        prior_173.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE173_N_LEFTOVER, 34)
        self.assertEqual(CYCLE173_N_WITH, 5)
        self.assertTrue(CYCLE173_CLAIM)
        prior_172 = TestMamariI2gram076071InsideFamilyScoreboard()
        prior_172.setUp()
        prior_172.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE172_N_LEFTOVER, 34)
        prior_171 = TestMamariI2gram076071IOnlyScoreboard()
        prior_171.setUp()
        prior_171.test_2gram_is_zero_off_i_and_i_only()
        prior_171.test_survey_matches_computed_lock()
        self.assertEqual(CYCLE171_N_I, 43)
        self.assertEqual(CYCLE171_N_OFF_I, 0)
        if CYCLE171_N_I != 43 or CYCLE171_N_OFF_I != 0:
            self.fail("nested cycle 171 43/0 drifted")
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-225 leftover extra next-stem lock."""
        lock = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(lock["cycle"], 225)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertTrue(lock["hypothesis_share_one_forward_stem"])
        self.assertEqual(
            lock["hypothesis_share_one_forward_stem"],
            HYPOTHESIS_SHARE_ONE,
        )
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover"], STANDING_N_LEFTOVER)
        self.assertEqual(lock["N_leftover"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["leftover_sites"]),
            STANDING_LEFTOVER_SITES,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 55)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 1)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(lock["ia2_174_next_stem"], STANDING_IA2_174_NEXT_STEM)
        self.assertEqual(lock["ia2_174_next_stem"], "000")
        self.assertEqual(
            lock["N_distinct_next_stems"],
            STANDING_N_DISTINCT_NEXT_STEMS,
        )
        self.assertEqual(lock["N_distinct_next_stems"], 30)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "070")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 8)
        self.assertTrue(lock["g_uniquely_most_frequent"])
        self.assertEqual(
            tuple(tuple(row) for row in lock["G_sites"]),
            STANDING_G_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["G_sites"]),
            CYCLE207_I_SITES,
        )
        self.assertEqual(
            tuple(lock["distinct_next_stems"]),
            STANDING_DISTINCT_NEXT_STEMS_FIRST_SEEN,
        )
        self.assertEqual(
            [stem if stem is not None else None for stem in STANDING_PER_SITE_NEXT_STEMS],
            lock["per_site_next_stems"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_PER_SITE_FORWARD_3GRAMS],
            lock["per_site_forward_3grams"],
        )
        self.assertEqual(
            [list(gram) if gram is not None else None for gram in STANDING_PER_SITE_NEXT_4GRAMS],
            lock["per_site_next_4grams"],
        )
        self.assertEqual(
            lock["next_stem_frequency"],
            next_stem_frequency_rows(STANDING_NEXT_STEM_FREQUENCY),
        )
        self.assertEqual(len(lock["next_stem_frequency"]), 30)
        self.assertEqual(lock["next_stem_frequency"][0]["next_stem"], "070")
        self.assertEqual(lock["next_stem_frequency"][0]["count"], 8)
        self.assertEqual(lock["N_hapax_next_stems"], STANDING_N_HAPAX_NEXT_STEMS)
        self.assertEqual(lock["N_hapax_next_stems"], 19)
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_extra_090_076_share_one_forward_stem"])
        self.assertEqual(
            lock["i_leftover_extra_090_076_share_one_forward_stem"],
            STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle216"])
        self.assertFalse(lock["same_as_cycle218"])
        self.assertTrue(lock["same_claim_shape_as_cycle216"])
        self.assertTrue(lock["same_claim_shape_as_cycle218"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle224_no_next_4gram_is_not_no_next_token"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_090_076_070_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_070_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_076_071_forward_076_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_inside_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_I"], 69)
        self.assertEqual(
            self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"],
            13,
        )
        self.assertEqual(
            self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"],
            56,
        )
        self.assertFalse(
            self.survey["i_090_076_inside_leftover_n4_remaining_family"][
                "i_090_076_all_inside_leftover_n4_remaining_family"
            ]
        )
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertFalse(self.survey["i_2gram_090_076_i_only"]["i_2gram_090_076_i_only"])
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["i_leftover_n4_remaining_next_2gram"]["cycle"], 222)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_next_2gram"][
                "i_leftover_n4_remaining_exactly_5_contain_090_076"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_next_2gram"]["K"], 5)
        self.assertEqual(tuple(self.survey["i_leftover_n4_remaining_next_2gram"]["G"]), GRAM2)
        self.assertEqual(self.survey["i_090_076_070_forward_stem"]["cycle"], 218)
        self.assertFalse(
            self.survey["i_090_076_070_forward_stem"]["i_090_076_070_share_one_forward_stem"]
        )
        self.assertEqual(self.survey["i_090_076_070_forward_stem"]["N_distinct_next_stems"], 8)
        self.assertEqual(self.survey["i_leftover_076_070_forward_stem"]["cycle"], 216)
        self.assertFalse(
            self.survey["i_leftover_076_070_forward_stem"][
                "i_leftover_076_070_share_one_forward_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_076_070_forward_stem"]["N_distinct_next_stems"],
            11,
        )
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
        self.assertEqual(self.survey["i_leftover_076_071_forward_076"]["cycle"], 173)
        self.assertTrue(
            self.survey["i_leftover_076_071_forward_076"][
                "i_leftover_076_071_exactly_5_forward_076_071_076"
            ]
        )
        self.assertEqual(self.survey["i_leftover_076_071_forward_076"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["cycle"], 172)
        self.assertEqual(self.survey["i_2gram_076_071_inside_family"]["N_leftover"], 34)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["cycle"], 171)
        self.assertTrue(self.survey["i_2gram_076_071_i_only"]["i_2gram_076_071_i_only"])
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_I"], 43)
        self.assertEqual(self.survey["i_2gram_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["cycle"], 46)
        self.assertEqual(self.survey["tablet_i_santiago_staff"]["longest_n"], 5)
        self.assertEqual(self.survey["n_repeating_nge5"]["cycle"], 134)
        self.assertTrue(self.survey["n_repeating_nge5"]["n_repeating_nge5_all_substrings_of_n_6gram"])
        self.assertEqual(self.survey["s_repeating_nge6"]["cycle"], 133)
        self.assertTrue(self.survey["s_repeating_nge6"]["s_repeating_nge6_all_substrings_of_s_7gram"])
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["cycle"], 99)
        self.assertEqual(self.survey["corpus_longest_n_inventory"]["rows"]["I"]["longest_n"], 5)
        self.assertEqual(self.survey["corpus_max_n_leak_table"]["cycle"], 104)
        self.assertTrue(self.survey["corpus_max_n_leak_table"]["leak_table_holds"])
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverExtra090076ForwardStemImageSnapshot(unittest.TestCase):
    """Cycle 225 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
