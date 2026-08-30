"""I's cycle-227 leftover extra remaining-after-071 next-stem lock.

Cycle 228 text-search lock. Uses already-vendored A–V and the
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

Leftover extra remaining-after-071 = leftover extra I 090 076
sites with a next token whose next token is neither 070 nor
071. Nested-check leftover extra N_leftover==56, N_with_next==55,
N_no_next==1 at Ia4[166], leftover extra exactly 8 share 070,
leftover extra remaining N_remaining==47 G=071 K=6 (do not
retune cycles 225–227). Nested-check cycle 195 090 076 071
6/0 still computes. Nested-check leftover extra remaining 6
share 071 equals the cycle-195 I 090 076 071 set (still
compute, do not retune). Nested-check N_remaining2==41
(47−6). Ia2[174] has next token 000 and is remaining-after-071;
it is not no-next. Off-I T sites are not this cycle. I-only of
090 076 G is leftover-of-leftover for a later cycle if K≥2.
076 071 and 076 070 do not count as this 2-gram. Inside-
family sites do not count as leftover extra.

Among remaining-after-071, G = the next stem with the highest
remaining-after-071 count. If a tie, pick the larger Barthel
id. K = that count. Measured: N_remaining2=41,
N_distinct_remaining2=28, G=013 uniquely most frequent (next
is 001×3), K=5 at Ia3[37], Ia5[6], Ia5[164], Ia6[92],
Ia13[67]. Cycle 227 reported next-after-G as 013×5; measure
it, do not assume it. Claim that can lose:
i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G.
True iff leftover extra 56/55/8 stay, leftover extra remaining
47/6/071 stay, N_remaining2==41, G is uniquely most frequent
under the tie-break, and exactly K remaining-after-071 sites
share G. The claim is true. Same claim-shape as cycle 227
(leftover extra remaining exactly 6 share 071) and cycle 226
(leftover extra exactly 8 share forward 070). This can lose
if N_remaining2 ≠ 41 or the leftover extra remaining-after-071
filter disagrees with nested counts. Nested cycle 226 K=8 /
G=070, cycle 223 69/3, cycle 195 6/0, and cycle 171 43/0
stay. Do not assume the result; measure. Do not retune.

Search lock, not a merge and not a translation. MockProvider only.
"""

from collections import Counter
import unittest

from agents.base.providers import MockProvider
from tests.test_mamari_honolulu4_unpublished_scoreboard import (
    TestMamariHonolulu4UnpublishedScoreboard,
)
from tests.test_mamari_i_090_076_inside_leftover_n4_remaining_family_scoreboard import (
    STANDING_I_090_076_ALL_INSIDE_LEFTOVER_N4_REMAINING_FAMILY as CYCLE224_ALL_INSIDE,
    STANDING_I_SITES as CYCLE224_I_SITES,
    STANDING_INSIDE_SITES as CYCLE224_INSIDE_SITES,
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
from tests.test_mamari_i_3gram_090_076_071_i_only_scoreboard import (
    GRAM3 as CYCLE195_GRAM3,
    STANDING_I_3GRAM_090_076_071_I_ONLY as CYCLE195_CLAIM,
    STANDING_I_SITES as CYCLE195_I_SITES,
    STANDING_N_I as CYCLE195_N_I,
    STANDING_N_OFF_I as CYCLE195_N_OFF_I,
    TestMamariI3gram090076071IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_070_scoreboard import (
    STANDING_G as CYCLE226_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_EXACTLY_8_SHARE_FORWARD_070 as CYCLE226_CLAIM,
    STANDING_K as CYCLE226_K,
    STANDING_MATCHING_SITES as CYCLE226_MATCHING_SITES,
    STANDING_N_LEFTOVER as CYCLE226_N_LEFTOVER,
    STANDING_N_NO_NEXT as CYCLE226_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE226_N_WITH_NEXT,
    leftover_extra_with_forward_070,
    TestMamariILeftoverExtra090076Forward070Scoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE225_G,
    STANDING_G_SITES as CYCLE225_G_SITES,
    STANDING_IA2_174,
    STANDING_IA2_174_NEXT_STEM,
    STANDING_I_LEFTOVER_EXTRA_090_076_SHARE_ONE_FORWARD_STEM as CYCLE225_SHARE_ONE,
    STANDING_K as CYCLE225_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE225_N_DISTINCT,
    STANDING_N_LEFTOVER as CYCLE225_N_LEFTOVER,
    STANDING_N_NO_NEXT as CYCLE225_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE225_N_WITH_NEXT,
    STANDING_NO_NEXT_SITES,
    group_sites_by_next_stem,
    leftover_extra_forward_3grams,
    leftover_extra_next_4grams,
    leftover_extra_next_stems,
    leftover_sites_with_next,
    leftover_sites_without_next,
    site_next_stem,
    TestMamariILeftoverExtra090076ForwardStemScoreboard,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    STANDING_G as CYCLE227_G,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071 as CYCLE227_CLAIM,
    STANDING_K as CYCLE227_K,
    STANDING_MATCHING_SITES as CYCLE227_MATCHING_SITES,
    STANDING_N_DISTINCT_REMAINING as CYCLE227_N_DISTINCT,
    STANDING_N_REMAINING as CYCLE227_N_REMAINING,
    STANDING_N_SHARE_070 as CYCLE227_N_SHARE_070,
    STANDING_N_WITHOUT_G as CYCLE227_N_WITHOUT_G,
    STANDING_REMAINING_SITES as CYCLE227_REMAINING_SITES,
    barthel_id,
    i_leftover_extra_090_076_remaining_exactly_6_share_071,
    leftover_extra_nested_counts_hold,
    leftover_extra_remaining,
    leftover_extra_remaining_next_stems,
    leftover_extra_remaining_with_g,
    leftover_extra_remaining_without_g,
    TestMamariILeftoverExtra090076RemainingNextStemScoreboard,
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

HYPOTHESIS_K = 5
LOCKED_FORWARD_STEM_070 = "070"
LOCKED_FORWARD_STEM_071 = "071"
LOCKED_FORWARD_STEMS = (LOCKED_FORWARD_STEM_070, LOCKED_FORWARD_STEM_071)
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "013")
GRAM3_NESTED_071 = ("090", "076", "071")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_WITH_NEXT = 55
STANDING_N_NO_NEXT = 1
STANDING_N_SHARE_070 = 8
STANDING_N_REMAINING = 47
STANDING_N_SHARE_071 = 6
STANDING_N_REMAINING2 = 41
STANDING_N_DISTINCT_REMAINING2 = 28
STANDING_N_HAPAX_REMAINING2 = 19
STANDING_G = "013"
STANDING_K = 5
STANDING_N_WITHOUT_G = 36
STANDING_N_NEXT_AFTER_G = 3
STANDING_N_NEXT_AFTER_G_STEM = "001"
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_REMAINING2_SITES = (
    (SIDE_IA, "Ia1", 2),
    (SIDE_IA, "Ia1", 15),
    (SIDE_IA, "Ia1", 27),
    (SIDE_IA, "Ia1", 59),
    (SIDE_IA, "Ia1", 96),
    (SIDE_IA, "Ia2", 14),
    (SIDE_IA, "Ia2", 37),
    (SIDE_IA, "Ia2", 114),
    (SIDE_IA, "Ia2", 128),
    (SIDE_IA, "Ia2", 154),
    (SIDE_IA, "Ia2", 159),
    (SIDE_IA, "Ia2", 165),
    (SIDE_IA, "Ia2", 174),
    (SIDE_IA, "Ia3", 37),
    (SIDE_IA, "Ia3", 71),
    (SIDE_IA, "Ia3", 87),
    (SIDE_IA, "Ia4", 84),
    (SIDE_IA, "Ia4", 121),
    (SIDE_IA, "Ia4", 134),
    (SIDE_IA, "Ia4", 162),
    (SIDE_IA, "Ia5", 6),
    (SIDE_IA, "Ia5", 127),
    (SIDE_IA, "Ia5", 164),
    (SIDE_IA, "Ia6", 92),
    (SIDE_IA, "Ia6", 134),
    (SIDE_IA, "Ia7", 2),
    (SIDE_IA, "Ia7", 88),
    (SIDE_IA, "Ia7", 113),
    (SIDE_IA, "Ia7", 137),
    (SIDE_IA, "Ia9", 129),
    (SIDE_IA, "Ia10", 137),
    (SIDE_IA, "Ia10", 141),
    (SIDE_IA, "Ia12", 42),
    (SIDE_IA, "Ia12", 47),
    (SIDE_IA, "Ia12", 150),
    (SIDE_IA, "Ia13", 67),
    (SIDE_IA, "Ia13", 109),
    (SIDE_IA, "Ia13", 135),
    (SIDE_IA, "Ia13", 143),
    (SIDE_IA, "Ia14", 9),
    (SIDE_IA, "Ia14", 177),
)
STANDING_REMAINING2_NEXT_STEMS = (
    "012",
    "175",
    "755",
    "470",
    "430",
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
    "087",
    "013",
    "505",
    "013",
    "013",
    "001",
    "280",
    "001",
    "280",
    "607",
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
    "530",
    "670",
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia3", 37),
    (SIDE_IA, "Ia5", 6),
    (SIDE_IA, "Ia5", 164),
    (SIDE_IA, "Ia6", 92),
    (SIDE_IA, "Ia13", 67),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "013", "073"),
    ("090", "076", "013", "291"),
    ("090", "076", "013", "076"),
    ("090", "076", "013", "070"),
    ("090", "076", "013", "755"),
)
STANDING_REMAINING2_FREQUENCY = (
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
        "700",
        2,
        ((SIDE_IA, "Ia2", 159), (SIDE_IA, "Ia13", 143)),
        (("090", "076", "700"),) * 2,
    ),
    (
        "530",
        2,
        ((SIDE_IA, "Ia12", 42), (SIDE_IA, "Ia14", 9)),
        (("090", "076", "530"),) * 2,
    ),
    (
        "280",
        2,
        ((SIDE_IA, "Ia7", 2), (SIDE_IA, "Ia7", 113)),
        (("090", "076", "280"),) * 2,
    ),
    (
        "087",
        2,
        ((SIDE_IA, "Ia3", 87), (SIDE_IA, "Ia4", 162)),
        (("090", "076", "087"),) * 2,
    ),
    (
        "011",
        2,
        ((SIDE_IA, "Ia2", 37), (SIDE_IA, "Ia12", 47)),
        (("090", "076", "011"),) * 2,
    ),
    (
        "005",
        2,
        ((SIDE_IA, "Ia3", 71), (SIDE_IA, "Ia13", 109)),
        (("090", "076", "005"),) * 2,
    ),
    (
        "000",
        2,
        ((SIDE_IA, "Ia2", 174), (SIDE_IA, "Ia10", 141)),
        (("090", "076", "000"),) * 2,
    ),
    ("755", 1, ((SIDE_IA, "Ia1", 27),), (("090", "076", "755"),)),
    ("670", 1, ((SIDE_IA, "Ia14", 177),), (("090", "076", "670"),)),
    ("607", 1, ((SIDE_IA, "Ia7", 137),), (("090", "076", "607"),)),
    ("600", 1, ((SIDE_IA, "Ia2", 14),), (("090", "076", "600"),)),
    ("535", 1, ((SIDE_IA, "Ia2", 128),), (("090", "076", "535"),)),
    ("505", 1, ((SIDE_IA, "Ia5", 127),), (("090", "076", "505"),)),
    ("470", 1, ((SIDE_IA, "Ia1", 59),), (("090", "076", "470"),)),
    ("430", 1, ((SIDE_IA, "Ia1", 96),), (("090", "076", "430"),)),
    ("386", 1, ((SIDE_IA, "Ia4", 121),), (("090", "076", "386"),)),
    ("384", 1, ((SIDE_IA, "Ia2", 114),), (("090", "076", "384"),)),
    ("300", 1, ((SIDE_IA, "Ia12", 150),), (("090", "076", "300"),)),
    ("255", 1, ((SIDE_IA, "Ia13", 135),), (("090", "076", "255"),)),
    ("175", 1, ((SIDE_IA, "Ia1", 15),), (("090", "076", "175"),)),
    ("147", 1, ((SIDE_IA, "Ia2", 165),), (("090", "076", "147"),)),
    ("090", 1, ((SIDE_IA, "Ia4", 84),), (("090", "076", "090"),)),
    ("072", 1, ((SIDE_IA, "Ia10", 137),), (("090", "076", "072"),)),
    ("057", 1, ((SIDE_IA, "Ia9", 129),), (("090", "076", "057"),)),
    ("050", 1, ((SIDE_IA, "Ia2", 154),), (("090", "076", "050"),)),
    ("012", 1, ((SIDE_IA, "Ia1", 2),), (("090", "076", "012"),)),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G"
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_after_071_next_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE222 = False
STANDING_SAME_AS_CYCLE226 = False
STANDING_SAME_AS_CYCLE227 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE227 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN = True


def leftover_extra_remaining_after_071(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra with-next sites whose next token is not 070 or 071."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_071_next_stems(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[str, ...]:
    """Next stems of leftover extra remaining-after-071 sites."""
    locked_set = set(locked)
    return tuple(
        nxt
        for nxt in next_stems
        if nxt is not None and nxt not in locked_set
    )


def leftover_extra_remaining_after_071_with_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-071 sites whose next token is G."""
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem
    )


def leftover_extra_remaining_after_071_without_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining-after-071 sites whose next token is not G."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set and nxt != stem
    )


def remaining_after_071_next_stem_counts(next_stems: tuple[str, ...]) -> Counter:
    """Counts of next stems among leftover extra remaining-after-071."""
    return Counter(next_stems)


def rank_remaining_after_071_next_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Remaining-after-071 next stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_remaining_after_071_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining-after-071 has no G."""
    ranked = rank_remaining_after_071_next_stems(
        remaining_after_071_next_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_after_071_next_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    forward_3grams: tuple[tuple[str, ...] | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Remaining-after-071 next-stem frequency: highest count first, then larger id."""
    rem_sites = leftover_extra_remaining_after_071(sites, next_stems, locked)
    rem_stems = leftover_extra_remaining_after_071_next_stems(sites, next_stems, locked)
    locked_set = set(locked)
    rem_grams = tuple(
        gram
        for nxt, gram in zip(next_stems, forward_3grams, strict=True)
        if nxt is not None and nxt not in locked_set
    )
    first_seen = group_sites_by_next_stem(rem_sites, rem_stems)
    grams_by_stem: dict[str, list[tuple[str, ...]]] = {
        stem: [] for stem, _ in first_seen
    }
    for nxt, gram in zip(rem_stems, rem_grams, strict=True):
        if gram is not None:
            grams_by_stem[nxt].append(gram)
    rows = tuple(
        (stem, len(stem_sites), stem_sites, tuple(grams_by_stem[stem]))
        for stem, stem_sites in first_seen
    )
    return tuple(sorted(rows, key=lambda row: (-row[1], -barthel_id(row[0]))))


def remaining_after_071_next_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_REMAINING2_FREQUENCY,
) -> list[dict]:
    """Survey-shaped remaining-after-071 next-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "next_stem": stem,
                "count": count,
                "leftover_extra_remaining_after_071_sites": [
                    list(site) for site in sites
                ],
                "forward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def matching_leftover_extra_remaining_after_071_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining-after-071 next-4-gram rows."""
    rows = []
    for (side, line, index), next_gram in zip(
        leftover_sites,
        next_4grams,
        strict=True,
    ):
        rows.append(
            {
                "tablet": "I",
                "side": side,
                "line": line,
                "index": index,
                "next_4gram": list(next_gram),
                "forward_3gram": list(next_gram[:3]),
            }
        )
    return rows


def leftover_extra_remaining_after_071_nested_counts_hold(
    n_leftover: int,
    n_with_next: int,
    n_no_next: int,
    n_share_070: int,
    n_remaining: int,
    n_share_071: int,
    n_remaining2: int,
    expected_leftover: int = STANDING_N_LEFTOVER,
    expected_with_next: int = STANDING_N_WITH_NEXT,
    expected_no_next: int = STANDING_N_NO_NEXT,
    expected_share_070: int = STANDING_N_SHARE_070,
    expected_remaining: int = STANDING_N_REMAINING,
    expected_share_071: int = STANDING_N_SHARE_071,
    expected_remaining2: int = STANDING_N_REMAINING2,
) -> bool:
    """Nested leftover extra 56/55/1, 8 share 070, remaining 47/6/071, remaining2=41."""
    return (
        leftover_extra_nested_counts_hold(
            n_leftover,
            n_with_next,
            n_no_next,
            n_share_070,
            expected_leftover,
            expected_with_next,
            expected_no_next,
            expected_share_070,
        )
        and n_remaining == expected_remaining
        and n_share_071 == expected_share_071
        and n_remaining2 == expected_remaining2
        and n_remaining2 == n_remaining - n_share_071
        and n_remaining == n_with_next - n_share_070
    )


def i_leftover_extra_090_076_remaining_after_071_exactly_k_share_g(
    leftover_sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    expected_g: str = STANDING_G,
    expected_k: int = HYPOTHESIS_K,
    expected_remaining2: int = STANDING_N_REMAINING2,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> bool:
    """True iff remaining2=41, G is unique max, and exactly K share G."""
    with_next = leftover_sites_with_next(leftover_sites, next_stems)
    no_next = leftover_sites_without_next(leftover_sites, next_stems)
    share_070 = leftover_extra_with_forward_070(leftover_sites, next_stems)
    remaining = leftover_extra_remaining(leftover_sites, next_stems)
    share_071 = leftover_extra_remaining_with_g(
        leftover_sites,
        next_stems,
        LOCKED_FORWARD_STEM_071,
    )
    remaining2 = leftover_extra_remaining_after_071(leftover_sites, next_stems, locked)
    rem2_stems = leftover_extra_remaining_after_071_next_stems(
        leftover_sites,
        next_stems,
        locked,
    )
    if not leftover_extra_remaining_after_071_nested_counts_hold(
        len(leftover_sites),
        len(with_next),
        len(no_next),
        len(share_070),
        len(remaining),
        len(share_071),
        len(remaining2),
    ):
        return False
    if len(remaining2) != expected_remaining2:
        return False
    if remaining2 != leftover_extra_remaining_without_g(
        leftover_sites,
        next_stems,
        LOCKED_FORWARD_STEM_071,
    ):
        return False
    gram, count, unique = select_remaining_after_071_g(rem2_stems)
    if not unique or gram != expected_g or count != expected_k:
        return False
    return (
        len(
            leftover_extra_remaining_after_071_with_g(
                leftover_sites,
                next_stems,
                gram,
            )
        )
        == expected_k
    )


class TestILeftoverExtra090076RemainingAfter071NextStemHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining-after-071 next stems. No CV, no LLM."""

    def test_remaining_after_071_requires_with_next_not_070_not_071(self):
        """Remaining-after-071 excludes no-next and the locked 070/071 clusters."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "013"))
        self.assertEqual(GRAM3_NESTED_071, ("090", "076", "071"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("070", "071"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_013 = ["999", "090", "076", "013", "073"]
        self.assertEqual(site_next_stem(has_013, 1, GRAM2), "013")
        self.assertEqual(site_forward_3gram(has_013, 1, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_013, 1, GRAM2),
            ("090", "076", "013", "073"),
        )
        has_071 = ["999", "090", "076", "071", "633"]
        self.assertEqual(site_next_stem(has_071, 1, GRAM2), "071")
        self.assertNotEqual(site_next_stem(has_071, 1, GRAM2), "013")
        has_070 = ["999", "090", "076", "070", "499"]
        self.assertEqual(site_next_stem(has_070, 1, GRAM2), "070")
        self.assertNotEqual(site_next_stem(has_070, 1, GRAM2), "013")
        end_of_line = ["087", "078", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        one_token_then_eol = ["009", "009", "090", "076", "000"]
        self.assertEqual(site_next_stem(one_token_then_eol, 2, GRAM2), "000")
        self.assertIsNone(site_next_4gram(one_token_then_eol, 2, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 4),
        )
        planted_stems = ("013", "070", "071", None, "001")
        self.assertEqual(
            leftover_extra_remaining_after_071(planted_sites, planted_stems),
            (planted_sites[0], planted_sites[4]),
        )
        self.assertEqual(
            leftover_extra_remaining_after_071_next_stems(planted_sites, planted_stems),
            ("013", "001"),
        )
        self.assertNotIn(
            planted_sites[1],
            leftover_extra_remaining_after_071(planted_sites, planted_stems),
        )
        self.assertNotIn(
            planted_sites[2],
            leftover_extra_remaining_after_071(planted_sites, planted_stems),
        )
        self.assertNotIn(
            planted_sites[3],
            leftover_extra_remaining_after_071(planted_sites, planted_stems),
        )
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        mismatch_070 = ["076", "070", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_070, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_k_can_fail(self):
        """Boolean is True only when remaining2=41, unique G=013, K=5."""
        provider = MockProvider()
        leftover = STANDING_LEFTOVER_SITES
        stems = leftover_extra_next_stems(load_i_sides(), leftover, GRAM2)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_071_exactly_k_share_g(
                leftover,
                stems,
            )
        )
        rem2 = leftover_extra_remaining_after_071(leftover, stems)
        rem2_stems = leftover_extra_remaining_after_071_next_stems(leftover, stems)
        self.assertEqual(len(rem2), STANDING_N_REMAINING2)
        self.assertEqual(len(rem2), 41)
        self.assertEqual(rem2, STANDING_REMAINING2_SITES)
        self.assertEqual(rem2_stems, STANDING_REMAINING2_NEXT_STEMS)
        g, k, unique = select_remaining_after_071_g(rem2_stems)
        self.assertEqual(g, "013")
        self.assertEqual(k, 5)
        self.assertTrue(unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        empty_stems = (None,) * len(leftover)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_071_exactly_k_share_g(
                leftover,
                empty_stems,
            )
        )
        planted = leftover + ((SIDE_IA, "Ia1", 0),)
        planted_stems = stems + ("013",)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_071_exactly_k_share_g(
                planted,
                planted_stems,
            )
        )
        changed = False
        dropped = []
        for nxt in stems:
            if not changed and nxt == "013":
                dropped.append("001")
                changed = True
            else:
                dropped.append(nxt)
        dropped_stems = tuple(dropped)
        self.assertEqual(len(leftover_extra_remaining_after_071(leftover, dropped_stems)), 41)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_071_exactly_k_share_g(
                leftover,
                dropped_stems,
            )
        )
        one_more_001 = tuple(
            "001"
            if nxt == "700" and leftover[i] == (SIDE_IA, "Ia2", 159)
            else nxt
            for i, nxt in enumerate(stems)
        )
        two_more_001 = tuple(
            "001"
            if leftover[i] == (SIDE_IA, "Ia13", 143) and nxt == "700"
            else nxt
            for i, nxt in enumerate(one_more_001)
        )
        tie_g, tie_k, tie_unique = select_remaining_after_071_g(
            leftover_extra_remaining_after_071_next_stems(leftover, two_more_001)
        )
        self.assertEqual(tie_k, 5)
        self.assertFalse(tie_unique)
        self.assertIn(tie_g, ("013", "001"))
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_071_exactly_k_share_g(
                leftover,
                two_more_001,
            )
        )
        make_071 = tuple("071" if nxt == "013" else nxt for nxt in stems)
        self.assertEqual(len(leftover_extra_remaining_after_071(leftover, make_071)), 36)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_after_071_exactly_k_share_g(
                leftover,
                make_071,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G",
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G
        )
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G,
            HYPOTHESIS_K == STANDING_K,
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING2)
        self.assertEqual(5 + 36, 41)
        self.assertEqual(
            STANDING_N_REMAINING - STANDING_N_SHARE_071,
            STANDING_N_REMAINING2,
        )
        self.assertEqual(47 - 6, 41)
        self.assertEqual(CYCLE227_N_WITHOUT_G, STANDING_N_REMAINING2)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal remaining-after-071 counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"001": 4, "013": 4, "700": 2})
        ranked = rank_remaining_after_071_next_stems(counts)
        self.assertEqual(ranked[0], ("013", 4))
        self.assertEqual(ranked[1], ("001", 4))
        self.assertEqual(
            select_remaining_after_071_g(
                ("001", "013", "001", "013", "001", "013", "001", "013")
            )[0],
            "013",
        )
        self.assertFalse(
            select_remaining_after_071_g(
                ("001", "013", "001", "013", "001", "013", "001", "013")
            )[2]
        )
        self.assertEqual(select_remaining_after_071_g(("005", "700", "005", "700"))[0], "700")
        self.assertFalse(select_remaining_after_071_g(("005", "700", "005", "700"))[2])
        self.assertEqual(select_remaining_after_071_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE227)
        self.assertFalse(STANDING_SAME_AS_CYCLE222)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE227)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingAfter071NextStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover extra remaining-after-071 next-stem lock. Mock only."""

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
        self.share_070 = leftover_extra_with_forward_070(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining = leftover_extra_remaining(
            self.leftover_sites,
            self.next_stems,
        )
        self.share_071 = leftover_extra_remaining_with_g(
            self.leftover_sites,
            self.next_stems,
            LOCKED_FORWARD_STEM_071,
        )
        self.remaining2 = leftover_extra_remaining_after_071(
            self.leftover_sites,
            self.next_stems,
        )
        self.remaining2_stems = leftover_extra_remaining_after_071_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.matching = leftover_extra_remaining_after_071_with_g(
            self.leftover_sites,
            self.next_stems,
        )
        self.without = leftover_extra_remaining_after_071_without_g(
            self.leftover_sites,
            self.next_stems,
        )
        self.frequency = remaining_after_071_next_stem_frequency_table(
            self.leftover_sites,
            self.next_stems,
            self.forwards,
        )
        self.matching_next_4grams = leftover_extra_next_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = CYCLE224_N_INSIDE
        self.n_leftover = len(self.leftover_sites)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.n_share_070 = len(self.share_070)
        self.n_remaining = len(self.remaining)
        self.n_share_071 = len(self.share_071)
        self.n_remaining2 = len(self.remaining2)
        self.n_distinct_remaining2 = len(self.frequency)
        self.g, self.k, self.unique = select_remaining_after_071_g(self.remaining2_stems)
        self.n_without = len(self.without)
        self.claim_holds = i_leftover_extra_090_076_remaining_after_071_exactly_k_share_g(
            self.leftover_sites,
            self.next_stems,
        )

    def test_tokens_and_nested_leftover_extra_56_55_8_and_47_6_071_not_retuned(self):
        """2-gram and leftover extra 56/55/1 / 8 share 070 / remaining 47/6/071 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "013"))
        self.assertEqual(GRAM3_NESTED_071, ("090", "076", "071"))
        self.assertEqual(GRAM3_NESTED_071, CYCLE195_GRAM3)
        self.assertNotEqual(GRAM3_FORWARD, CYCLE207_GRAM3)
        self.assertEqual(CYCLE207_GRAM3, ("090", "076", "070"))
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
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE225_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, CYCLE226_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        self.assertEqual(CYCLE224_N_INSIDE, 13)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_leftover != 56 or CYCLE224_N_INSIDE != 13:
            self.fail("nested cycle 224 13/56 drifted")
        prior_227 = self.survey["i_leftover_extra_090_076_remaining_next_stem"]
        self.assertEqual(prior_227["cycle"], 227)
        self.assertEqual(prior_227["N_leftover"], 56)
        self.assertEqual(prior_227["N_with_next"], 55)
        self.assertEqual(prior_227["N_no_next"], 1)
        self.assertEqual(prior_227["N_share_070"], 8)
        self.assertEqual(prior_227["N_remaining"], 47)
        self.assertEqual(prior_227["G"], "071")
        self.assertEqual(prior_227["K"], 6)
        self.assertEqual(prior_227["N_without_G"], 41)
        self.assertEqual(prior_227["next_after_G"], "013")
        self.assertEqual(prior_227["N_next_after_G"], 5)
        self.assertTrue(prior_227["i_leftover_extra_090_076_remaining_exactly_6_share_071"])
        self.assertTrue(CYCLE227_CLAIM)
        self.assertEqual(CYCLE227_G, "071")
        self.assertEqual(CYCLE227_K, 6)
        self.assertEqual(CYCLE227_N_REMAINING, 47)
        self.assertEqual(CYCLE227_N_WITHOUT_G, 41)
        prior_226 = self.survey["i_leftover_extra_090_076_forward_070"]
        self.assertEqual(prior_226["cycle"], 226)
        self.assertEqual(prior_226["N_leftover"], 56)
        self.assertEqual(prior_226["N_with_next"], 55)
        self.assertEqual(prior_226["N_no_next"], 1)
        self.assertEqual(prior_226["G"], "070")
        self.assertEqual(prior_226["K"], 8)
        self.assertTrue(prior_226["i_leftover_extra_090_076_exactly_8_share_forward_070"])
        self.assertTrue(CYCLE226_CLAIM)
        self.assertEqual(CYCLE226_G, "070")
        self.assertEqual(CYCLE226_K, 8)
        prior_225 = self.survey["i_leftover_extra_090_076_forward_stem"]
        self.assertEqual(prior_225["cycle"], 225)
        self.assertEqual(prior_225["N_leftover"], 56)
        self.assertEqual(prior_225["N_with_next"], 55)
        self.assertEqual(prior_225["N_no_next"], 1)
        self.assertEqual(prior_225["N_distinct_next_stems"], 30)
        self.assertEqual(prior_225["G"], "070")
        self.assertEqual(prior_225["K"], 8)
        self.assertFalse(prior_225["i_leftover_extra_090_076_share_one_forward_stem"])
        prior_224 = self.survey["i_090_076_inside_leftover_n4_remaining_family"]
        self.assertEqual(prior_224["cycle"], 224)
        self.assertEqual(prior_224["N_I"], 69)
        self.assertEqual(prior_224["N_inside"], 13)
        self.assertEqual(prior_224["N_leftover"], 56)
        self.assertFalse(prior_224["i_090_076_all_inside_leftover_n4_remaining_family"])
        self.assertFalse(CYCLE224_ALL_INSIDE)
        prior_223 = self.survey["i_2gram_090_076_i_only"]
        self.assertEqual(prior_223["cycle"], 223)
        self.assertEqual(prior_223["N_I"], STANDING_N_I)
        self.assertEqual(prior_223["N_I"], 69)
        self.assertEqual(prior_223["N_off_I"], STANDING_N_OFF_I)
        self.assertEqual(prior_223["N_off_I"], 3)
        self.assertFalse(prior_223["i_2gram_090_076_i_only"])
        prior_195 = self.survey["i_3gram_090_076_071_i_only"]
        self.assertEqual(prior_195["cycle"], 195)
        self.assertEqual(prior_195["N_I"], 6)
        self.assertEqual(prior_195["N_off_I"], 0)
        self.assertTrue(prior_195["i_3gram_090_076_071_i_only"])
        self.assertTrue(CYCLE195_CLAIM)
        self.assertEqual(CYCLE195_N_I, 6)
        self.assertEqual(CYCLE195_N_OFF_I, 0)
        prior_171 = self.survey["i_2gram_076_071_i_only"]
        self.assertEqual(prior_171["cycle"], 171)
        self.assertEqual(prior_171["N_I"], 43)
        self.assertEqual(prior_171["N_off_I"], 0)
        self.assertTrue(prior_171["i_2gram_076_071_i_only"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_41_remaining2_g_013_k_5_and_hypothesis_holds(self):
        """N_remaining2=41, N_distinct=28, G=013 K=5 unique. Claim holds."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover, STANDING_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, CYCLE225_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, CYCLE226_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 55)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, CYCLE225_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, CYCLE226_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 1)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ((SIDE_IA, "Ia4", 166),))
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_leftover)
        self.assertEqual(55 + 1, 56)
        self.assertEqual(self.n_share_070, STANDING_N_SHARE_070)
        self.assertEqual(STANDING_N_SHARE_070, 8)
        self.assertEqual(STANDING_N_SHARE_070, CYCLE226_K)
        self.assertEqual(STANDING_N_SHARE_070, CYCLE227_N_SHARE_070)
        self.assertEqual(self.share_070, CYCLE226_MATCHING_SITES)
        self.assertEqual(self.share_070, CYCLE225_G_SITES)
        self.assertEqual(self.share_070, CYCLE207_I_SITES)
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING)
        self.assertEqual(STANDING_N_REMAINING, 47)
        self.assertEqual(STANDING_N_REMAINING, CYCLE227_N_REMAINING)
        self.assertEqual(self.n_remaining, self.n_with_next - self.n_share_070)
        self.assertEqual(55 - 8, 47)
        self.assertEqual(self.remaining, CYCLE227_REMAINING_SITES)
        self.assertEqual(self.n_share_071, STANDING_N_SHARE_071)
        self.assertEqual(STANDING_N_SHARE_071, 6)
        self.assertEqual(STANDING_N_SHARE_071, CYCLE227_K)
        self.assertEqual(self.share_071, CYCLE227_MATCHING_SITES)
        self.assertEqual(self.share_071, CYCLE195_I_SITES)
        if self.share_071 != CYCLE195_I_SITES:
            self.fail("leftover extra remaining 6 share 071 drifted from cycle-195 I set")
        if (
            self.n_leftover != 56
            or self.n_with_next != 55
            or self.n_no_next != 1
            or self.n_share_070 != 8
            or self.n_remaining != 47
            or self.n_share_071 != 6
        ):
            self.fail("nested leftover extra 56/55/1 / 8 share 070 / remaining 47/6/071 drifted")
        self.assertTrue(
            leftover_extra_remaining_after_071_nested_counts_hold(
                self.n_leftover,
                self.n_with_next,
                self.n_no_next,
                self.n_share_070,
                self.n_remaining,
                self.n_share_071,
                self.n_remaining2,
            )
        )
        self.assertEqual(self.n_remaining2, STANDING_N_REMAINING2)
        self.assertEqual(STANDING_N_REMAINING2, 41)
        self.assertEqual(self.n_remaining2, self.n_remaining - self.n_share_071)
        self.assertEqual(47 - 6, 41)
        self.assertEqual(self.n_remaining2, CYCLE227_N_WITHOUT_G)
        if self.n_remaining2 != 41:
            self.fail("measured N_remaining2 drifted from 41")
        if self.n_remaining2 != self.n_remaining - self.n_share_071:
            self.fail("leftover extra remaining-after-071 filter disagrees with nested 47−6")
        self.assertEqual(self.remaining2, STANDING_REMAINING2_SITES)
        self.assertEqual(self.remaining2_stems, STANDING_REMAINING2_NEXT_STEMS)
        self.assertEqual(len(self.remaining2), len(self.remaining2_stems))
        self.assertEqual(
            self.remaining2,
            leftover_extra_remaining_without_g(
                self.leftover_sites,
                self.next_stems,
                LOCKED_FORWARD_STEM_071,
            ),
        )
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.remaining2)
        self.assertIn(STANDING_IA2_174, self.remaining2)
        self.assertEqual(STANDING_IA2_174_NEXT_STEM, "000")
        for site in self.share_070:
            self.assertNotIn(site, self.remaining2)
        for site in self.share_071:
            self.assertNotIn(site, self.remaining2)
        self.assertEqual(self.n_distinct_remaining2, STANDING_N_DISTINCT_REMAINING2)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING2, 28)
        self.assertEqual(self.n_distinct_remaining2, CYCLE227_N_DISTINCT - 1)
        self.assertEqual(self.frequency, STANDING_REMAINING2_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "013")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, HYPOTHESIS_K)
        self.assertEqual(STANDING_K, 5)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "013")
        self.assertEqual(self.frequency[0][1], 5)
        self.assertEqual(self.frequency[1][0], STANDING_N_NEXT_AFTER_G_STEM)
        self.assertEqual(self.frequency[1][1], STANDING_N_NEXT_AFTER_G)
        self.assertEqual(STANDING_N_NEXT_AFTER_G, 3)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 36)
        self.assertEqual(self.k + self.n_without, self.n_remaining2)
        self.assertEqual(5 + 36, 41)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX_REMAINING2)
        self.assertEqual(STANDING_N_HAPAX_REMAINING2, 19)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_after_071_exactly_k_share_g(
                self.leftover_sites,
                self.next_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G,
        )
        self.assertTrue(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE222)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE227)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE227)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_INSIDE_FAMILY_DOES_NOT_COUNT)
        self.assertFalse(CYCLE225_SHARE_ONE)
        self.assertTrue(CYCLE226_CLAIM)
        self.assertTrue(CYCLE227_CLAIM)
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_remaining_after_071_sites_share_013(self):
        """Five leftover extra remaining-after-071 sites are 090 076 013."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia3", 37), ("090", "076", "013", "073")),
            ((SIDE_IA, "Ia5", 6), ("090", "076", "013", "291")),
            ((SIDE_IA, "Ia5", 164), ("090", "076", "013", "076")),
            ((SIDE_IA, "Ia6", 92), ("090", "076", "013", "070")),
            ((SIDE_IA, "Ia13", 67), ("090", "076", "013", "755")),
        )
        for (site, nxt), (want_site, want_nxt) in zip(
            zip(self.matching, self.matching_next_4grams, strict=True),
            expected,
            strict=True,
        ):
            stems = line_stems_for_site(self.i_sides, site)
            side, line, index = site
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            self.assertEqual(tuple(stems[index : index + STANDING_N3]), GRAM3_FORWARD)
            self.assertEqual(stems[index + STANDING_N2], "013")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "013")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_REMAINING2_SITES)
            self.assertIn(site, CYCLE227_REMAINING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE226_MATCHING_SITES)
            self.assertNotIn(site, CYCLE227_MATCHING_SITES)
            self.assertNotIn(site, CYCLE207_I_SITES)
            self.assertNotIn(site, CYCLE195_I_SITES)
        self.assertNotIn(STANDING_IA2_174, self.matching)
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.matching)
        self.assertIn(STANDING_IA2_174, self.remaining2)
        self.assertEqual(
            self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_IA2_174)],
            "000",
        )
        self.assertIsNone(
            self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_NO_NEXT_SITES[0])]
        )
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "013")
            self.assertNotEqual(nxt, "071")
            self.assertNotEqual(nxt, "070")
            self.assertIn(site, STANDING_REMAINING2_SITES)
        for site in self.share_070:
            self.assertNotIn(site, self.remaining2)
            self.assertNotIn(site, self.matching)
        for site in self.share_071:
            self.assertNotIn(site, self.remaining2)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE195_I_SITES)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining2)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining2)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[2], "Ia3")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[5], "Ia6")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_227_226_223_195_and_171_still_compute(self):
        """Cycle 227 47/6/071, 226 K=8 / G=070, 223 69/3, 195 6/0, 171 43/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_227 = TestMamariILeftoverExtra090076RemainingNextStemScoreboard()
        prior_227.setUp()
        prior_227.test_counts_47_remaining_g_071_k_6_and_hypothesis_holds()
        prior_227.test_survey_matches_computed_lock()
        self.assertEqual(prior_227.n_leftover, 56)
        self.assertEqual(prior_227.n_with_next, 55)
        self.assertEqual(prior_227.n_no_next, 1)
        self.assertEqual(prior_227.n_remaining, 47)
        self.assertEqual(prior_227.k, 6)
        self.assertEqual(CYCLE227_G, "071")
        self.assertTrue(prior_227.claim_holds)
        self.assertTrue(CYCLE227_CLAIM)
        if (
            prior_227.n_leftover != 56
            or prior_227.n_with_next != 55
            or prior_227.n_no_next != 1
            or prior_227.n_remaining != 47
            or prior_227.k != 6
        ):
            self.fail("nested cycle 227 leftover extra remaining 47 G=071 K=6 drifted")
        prior_226 = TestMamariILeftoverExtra090076Forward070Scoreboard()
        prior_226.setUp()
        prior_226.test_counts_8_of_56_and_hypothesis_k_8_holds()
        prior_226.test_survey_matches_computed_lock()
        self.assertEqual(prior_226.n_leftover, 56)
        self.assertEqual(prior_226.n_with_next, 55)
        self.assertEqual(prior_226.n_no_next, 1)
        self.assertEqual(prior_226.k, 8)
        self.assertEqual(CYCLE226_G, "070")
        self.assertTrue(prior_226.claim_holds)
        self.assertTrue(CYCLE226_CLAIM)
        if (
            prior_226.n_leftover != 56
            or prior_226.n_with_next != 55
            or prior_226.n_no_next != 1
            or prior_226.k != 8
        ):
            self.fail("nested cycle 226 leftover extra 56/55/1 G=070 K=8 drifted")
        prior_225 = TestMamariILeftoverExtra090076ForwardStemScoreboard()
        prior_225.setUp()
        prior_225.test_counts_30_distinct_next_stems_and_claim_loses()
        prior_225.test_survey_matches_computed_lock()
        self.assertEqual(prior_225.n_leftover, 56)
        self.assertEqual(prior_225.n_with_next, 55)
        self.assertEqual(prior_225.n_no_next, 1)
        self.assertEqual(prior_225.n_distinct, 30)
        self.assertEqual(prior_225.g, "070")
        self.assertEqual(prior_225.k, 8)
        self.assertFalse(prior_225.claim_holds)
        self.assertFalse(CYCLE225_SHARE_ONE)
        prior_224 = TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard()
        prior_224.setUp()
        prior_224.test_sixty_nine_sites_split_13_inside_56_leftover_and_claim_loses()
        prior_224.test_survey_matches_computed_lock()
        self.assertEqual(prior_224.n_inside, 13)
        self.assertEqual(prior_224.n_leftover, 56)
        self.assertFalse(prior_224.claim_holds)
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
        prior_195 = TestMamariI3gram090076071IOnlyScoreboard()
        prior_195.setUp()
        prior_195.test_i_hits_are_six_on_ia()
        prior_195.test_3gram_is_zero_off_i_and_i_only()
        prior_195.test_survey_matches_computed_lock()
        self.assertEqual(prior_195.i_hits, CYCLE195_N_I)
        self.assertEqual(prior_195.i_hits, 6)
        self.assertEqual(prior_195.off_i_hits, CYCLE195_N_OFF_I)
        self.assertEqual(prior_195.off_i_hits, 0)
        self.assertEqual(prior_195.i_sites, CYCLE195_I_SITES)
        self.assertEqual(self.share_071, CYCLE195_I_SITES)
        self.assertTrue(prior_195.claim_holds)
        self.assertTrue(CYCLE195_CLAIM)
        if prior_195.i_hits != 6 or prior_195.off_i_hits != 0:
            self.fail("nested cycle 195 090 076 071 I-only 6/0 drifted")
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
        """CORPUS_SURVEY.json records the cycle-228 leftover extra remaining-after-071 lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_after_071_next_stem"]
        self.assertEqual(lock["cycle"], 228)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 5)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(tuple(lock["locked_forward_stems"]), ("070", "071"))
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
        self.assertEqual(lock["N_share_070"], STANDING_N_SHARE_070)
        self.assertEqual(lock["N_share_070"], 8)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_070_sites"]),
            CYCLE226_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 47)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_sites"]),
            CYCLE227_REMAINING_SITES,
        )
        self.assertEqual(lock["N_share_071"], STANDING_N_SHARE_071)
        self.assertEqual(lock["N_share_071"], 6)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_071_sites"]),
            CYCLE227_MATCHING_SITES,
        )
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_071_sites"]),
            CYCLE195_I_SITES,
        )
        self.assertEqual(lock["ia2_174_next_stem"], STANDING_IA2_174_NEXT_STEM)
        self.assertEqual(lock["ia2_174_next_stem"], "000")
        self.assertEqual(lock["N_remaining2"], STANDING_N_REMAINING2)
        self.assertEqual(lock["N_remaining2"], 41)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_071_sites"]),
            STANDING_REMAINING2_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_071_next_stems"]),
            STANDING_REMAINING2_NEXT_STEMS,
        )
        self.assertEqual(lock["N_distinct_remaining2"], STANDING_N_DISTINCT_REMAINING2)
        self.assertEqual(lock["N_distinct_remaining2"], 28)
        self.assertEqual(lock["N_hapax_remaining2"], STANDING_N_HAPAX_REMAINING2)
        self.assertEqual(lock["N_hapax_remaining2"], 19)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "013")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 5)
        self.assertTrue(lock["G_uniquely_most_frequent"])
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 36)
        self.assertEqual(lock["N_next_after_G"], STANDING_N_NEXT_AFTER_G)
        self.assertEqual(lock["N_next_after_G"], 3)
        self.assertEqual(lock["next_after_G"], STANDING_N_NEXT_AFTER_G_STEM)
        self.assertEqual(lock["next_after_G"], "001")
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_after_071_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_after_071_local_4grams"],
            matching_leftover_extra_remaining_after_071_local_4gram_rows(),
        )
        self.assertEqual(
            lock["remaining_after_071_next_stem_frequency"],
            remaining_after_071_next_stem_frequency_rows(),
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G"])
        self.assertEqual(
            lock["i_leftover_extra_090_076_remaining_after_071_exactly_K_share_G"],
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_071_EXACTLY_K_SHARE_G,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle222"])
        self.assertFalse(lock["same_as_cycle226"])
        self.assertFalse(lock["same_as_cycle227"])
        self.assertTrue(lock["same_claim_shape_as_cycle222"])
        self.assertTrue(lock["same_claim_shape_as_cycle226"])
        self.assertTrue(lock["same_claim_shape_as_cycle227"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_090_076_G_is_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle224_no_next_4gram_is_not_no_next_token"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_070_i_only_unchanged"])
        self.assertTrue(lock["standing_i_2gram_076_071_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["cycle"], 227)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_remaining_next_stem"][
                "i_leftover_extra_090_076_remaining_exactly_6_share_071"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["N_remaining"], 47)
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["G"], "071")
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["K"], 6)
        self.assertEqual(self.survey["i_leftover_extra_090_076_remaining_next_stem"]["N_without_G"], 41)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["cycle"], 226)
        self.assertTrue(
            self.survey["i_leftover_extra_090_076_forward_070"][
                "i_leftover_extra_090_076_exactly_8_share_forward_070"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["N_with_next"], 55)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["N_no_next"], 1)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["G"], "070")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_070"]["K"], 8)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["cycle"], 225)
        self.assertFalse(
            self.survey["i_leftover_extra_090_076_forward_stem"][
                "i_leftover_extra_090_076_share_one_forward_stem"
            ]
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["N_with_next"], 55)
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["N_no_next"], 1)
        self.assertEqual(
            self.survey["i_leftover_extra_090_076_forward_stem"]["N_distinct_next_stems"],
            30,
        )
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["G"], "070")
        self.assertEqual(self.survey["i_leftover_extra_090_076_forward_stem"]["K"], 8)
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
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["cycle"], 195)
        self.assertTrue(self.survey["i_3gram_090_076_071_i_only"]["i_3gram_090_076_071_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_I"], 6)
        self.assertEqual(self.survey["i_3gram_090_076_071_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["cycle"], 207)
        self.assertFalse(self.survey["i_3gram_090_076_070_i_only"]["i_3gram_090_076_070_i_only"])
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_I"], 8)
        self.assertEqual(self.survey["i_3gram_090_076_070_i_only"]["N_off_I"], 1)
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


class TestMamariILeftoverExtra090076RemainingAfter071NextStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 228 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
