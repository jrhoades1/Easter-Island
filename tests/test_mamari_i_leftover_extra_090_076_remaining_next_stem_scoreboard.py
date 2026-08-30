"""I's cycle-226 leftover extra remaining next-stem lock.

Cycle 227 text-search lock. Uses already-vendored A–V and the
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

Leftover extra remaining = leftover extra I 090 076 sites
with a next token whose next token is not 070. Nested-check
leftover extra N_leftover==56, N_with_next==55, N_no_next==1
at Ia4[166], leftover extra exactly 8 share 070 (do not
retune cycles 225/226). Nested-check N_remaining==47
(55−8). Ia2[174] has next token 000 and is remaining; it is
not no-next. Off-I T sites are not this cycle. I-only of
090 076 G is leftover-of-leftover for a later cycle if K≥2.
076 071 and 076 070 do not count as this 2-gram. Inside-
family sites do not count as leftover extra.

Among remaining, G = the next stem with the highest remaining
count. If a tie, pick the larger Barthel id. K = that count.
Measured: N_remaining=47, N_distinct_remaining=29, G=071
uniquely most frequent (next is 013×5), K=6 at Ia4[154],
Ia5[2], Ia5[23], Ia5[66], Ia13[152], Ia14[105]. Claim that
can lose: i_leftover_extra_090_076_remaining_exactly_6_share_071.
True iff leftover extra 56/55/8 stay, N_remaining==47, G is
uniquely most frequent under the tie-break, and exactly K
remaining sites share G. The claim is true. Same claim-shape
as cycle 222 (leftover n=4 remaining exactly 5 contain
090 076) and cycle 226 (leftover extra exactly 8 share
forward 070). This can lose if N_remaining ≠ 47 or the
leftover extra remaining filter disagrees with nested counts.
Nested cycle 226 K=8 / G=070, cycle 223 69/3, cycle 222
leftover remaining K=5, cycle 207 8/1, and cycle 171 43/0
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

HYPOTHESIS_K = 6
LOCKED_FORWARD_STEM = "070"
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "071")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER = 56
STANDING_N_WITH_NEXT = 55
STANDING_N_NO_NEXT = 1
STANDING_N_SHARE_070 = 8
STANDING_N_REMAINING = 47
STANDING_N_DISTINCT_REMAINING = 29
STANDING_N_HAPAX_REMAINING = 19
STANDING_G = "071"
STANDING_K = 6
STANDING_N_WITHOUT_G = 41
STANDING_N_NEXT_AFTER_G = 5
STANDING_N_NEXT_AFTER_G_STEM = "013"
STANDING_G_UNIQUELY_MOST_FREQUENT = True
STANDING_REMAINING_SITES = (
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
    (SIDE_IA, "Ia4", 154),
    (SIDE_IA, "Ia4", 162),
    (SIDE_IA, "Ia5", 2),
    (SIDE_IA, "Ia5", 6),
    (SIDE_IA, "Ia5", 23),
    (SIDE_IA, "Ia5", 66),
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
    (SIDE_IA, "Ia13", 152),
    (SIDE_IA, "Ia14", 9),
    (SIDE_IA, "Ia14", 105),
    (SIDE_IA, "Ia14", 177),
)
STANDING_REMAINING_NEXT_STEMS = (
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
    "071",
    "087",
    "071",
    "013",
    "071",
    "071",
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
    "071",
    "530",
    "071",
    "670",
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia4", 154),
    (SIDE_IA, "Ia5", 2),
    (SIDE_IA, "Ia5", 23),
    (SIDE_IA, "Ia5", 66),
    (SIDE_IA, "Ia13", 152),
    (SIDE_IA, "Ia14", 105),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "071", "633"),
    ("090", "076", "071", "295"),
    ("090", "076", "071", "007"),
    ("090", "076", "071", "004"),
    ("090", "076", "071", "076"),
    ("090", "076", "071", "600"),
)
STANDING_REMAINING_FREQUENCY = (
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
STANDING_CLAIM = "i_leftover_extra_090_076_remaining_exactly_6_share_071"
STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071 = True
STANDING_RESULT = "i_leftover_extra_090_076_remaining_next_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE222 = False
STANDING_SAME_AS_CYCLE226 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE = True
STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_INSIDE_FAMILY_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN = True


def barthel_id(token: str) -> int:
    """Integer Barthel id for the cycle-227 remaining tie-break."""
    return int(token)


def leftover_extra_remaining(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: str = LOCKED_FORWARD_STEM,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra with-next sites whose next token is not 070."""
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt != locked
    )


def leftover_extra_remaining_next_stems(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: str = LOCKED_FORWARD_STEM,
) -> tuple[str, ...]:
    """Next stems of leftover extra remaining sites."""
    return tuple(
        nxt
        for nxt in next_stems
        if nxt is not None and nxt != locked
    )


def leftover_extra_remaining_with_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining sites whose next token is G."""
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem
    )


def leftover_extra_remaining_without_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: str = LOCKED_FORWARD_STEM,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover extra remaining sites whose next token is not G."""
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt != locked and nxt != stem
    )


def remaining_next_stem_counts(next_stems: tuple[str, ...]) -> Counter:
    """Counts of next stems among leftover extra remaining."""
    return Counter(next_stems)


def rank_remaining_next_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Remaining next stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_remaining_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining has no G."""
    ranked = rank_remaining_next_stems(remaining_next_stem_counts(remaining_stems))
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_next_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    forward_3grams: tuple[tuple[str, ...] | None, ...],
    locked: str = LOCKED_FORWARD_STEM,
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Remaining next-stem frequency: highest count first, then larger id."""
    rem_sites = leftover_extra_remaining(sites, next_stems, locked)
    rem_stems = leftover_extra_remaining_next_stems(sites, next_stems, locked)
    rem_grams = tuple(
        gram
        for nxt, gram in zip(next_stems, forward_3grams, strict=True)
        if nxt is not None and nxt != locked
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


def remaining_next_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_REMAINING_FREQUENCY,
) -> list[dict]:
    """Survey-shaped remaining next-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "next_stem": stem,
                "count": count,
                "leftover_extra_remaining_sites": [list(site) for site in sites],
                "forward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def matching_leftover_extra_remaining_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover extra remaining next-4-gram rows."""
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


def leftover_extra_nested_counts_hold(
    n_leftover: int,
    n_with_next: int,
    n_no_next: int,
    n_share_070: int,
    expected_leftover: int = STANDING_N_LEFTOVER,
    expected_with_next: int = STANDING_N_WITH_NEXT,
    expected_no_next: int = STANDING_N_NO_NEXT,
    expected_share_070: int = STANDING_N_SHARE_070,
) -> bool:
    """Nested leftover extra 56/55/1 and exactly 8 share 070."""
    return (
        n_leftover == expected_leftover
        and n_with_next == expected_with_next
        and n_no_next == expected_no_next
        and n_share_070 == expected_share_070
    )


def i_leftover_extra_090_076_remaining_exactly_6_share_071(
    leftover_sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    expected_g: str = STANDING_G,
    expected_k: int = HYPOTHESIS_K,
    expected_remaining: int = STANDING_N_REMAINING,
    locked: str = LOCKED_FORWARD_STEM,
) -> bool:
    """True iff remaining=47, G is unique max, and exactly K share G."""
    with_next = leftover_sites_with_next(leftover_sites, next_stems)
    no_next = leftover_sites_without_next(leftover_sites, next_stems)
    share_070 = leftover_extra_with_forward_070(leftover_sites, next_stems)
    if not leftover_extra_nested_counts_hold(
        len(leftover_sites),
        len(with_next),
        len(no_next),
        len(share_070),
    ):
        return False
    remaining = leftover_extra_remaining(leftover_sites, next_stems, locked)
    rem_stems = leftover_extra_remaining_next_stems(leftover_sites, next_stems, locked)
    if len(remaining) != expected_remaining:
        return False
    if len(remaining) != len(with_next) - len(share_070):
        return False
    gram, count, unique = select_remaining_g(rem_stems)
    if not unique or gram != expected_g or count != expected_k:
        return False
    return len(leftover_extra_remaining_with_g(leftover_sites, next_stems, gram)) == expected_k


class TestILeftoverExtra090076RemainingNextStemHelpers(unittest.TestCase):
    """Helpers on leftover extra remaining next stems. No CV, no LLM."""

    def test_remaining_requires_with_next_not_070(self):
        """Remaining excludes no-next and the locked 070 cluster."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "071"))
        self.assertEqual(LOCKED_FORWARD_STEM, "070")
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_071 = ["999", "090", "076", "071", "633"]
        self.assertEqual(site_next_stem(has_071, 1, GRAM2), "071")
        self.assertEqual(site_forward_3gram(has_071, 1, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_071, 1, GRAM2),
            ("090", "076", "071", "633"),
        )
        has_070 = ["999", "090", "076", "070", "499"]
        self.assertEqual(site_next_stem(has_070, 1, GRAM2), "070")
        self.assertNotEqual(site_next_stem(has_070, 1, GRAM2), "071")
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
        )
        planted_stems = ("071", "070", None, "013")
        self.assertEqual(
            leftover_extra_remaining(planted_sites, planted_stems),
            (planted_sites[0], planted_sites[3]),
        )
        self.assertEqual(
            leftover_extra_remaining_next_stems(planted_sites, planted_stems),
            ("071", "013"),
        )
        self.assertNotIn(planted_sites[1], leftover_extra_remaining(planted_sites, planted_stems))
        self.assertNotIn(planted_sites[2], leftover_extra_remaining(planted_sites, planted_stems))
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        mismatch_070 = ["076", "070", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_070, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE224_NO_NEXT_4GRAM_IS_NOT_NO_NEXT_TOKEN)
        self.assertEqual(provider.get_call_history(), [])

    def test_exactly_6_can_fail(self):
        """Boolean is True only when remaining=47, unique G=071, K=6."""
        provider = MockProvider()
        leftover = STANDING_LEFTOVER_SITES
        stems = leftover_extra_next_stems(load_i_sides(), leftover, GRAM2)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_exactly_6_share_071(leftover, stems)
        )
        rem = leftover_extra_remaining(leftover, stems)
        rem_stems = leftover_extra_remaining_next_stems(leftover, stems)
        self.assertEqual(len(rem), STANDING_N_REMAINING)
        self.assertEqual(len(rem), 47)
        self.assertEqual(rem, STANDING_REMAINING_SITES)
        self.assertEqual(rem_stems, STANDING_REMAINING_NEXT_STEMS)
        g, k, unique = select_remaining_g(rem_stems)
        self.assertEqual(g, "071")
        self.assertEqual(k, 6)
        self.assertTrue(unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        empty_stems = (None,) * len(leftover)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_exactly_6_share_071(leftover, empty_stems)
        )
        planted = leftover + ((SIDE_IA, "Ia1", 0),)
        planted_stems = stems + ("071",)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_exactly_6_share_071(planted, planted_stems)
        )
        changed = False
        dropped = []
        for nxt in stems:
            if not changed and nxt == "071":
                dropped.append("013")
                changed = True
            else:
                dropped.append(nxt)
        dropped_stems = tuple(dropped)
        # first remaining 071 becomes 013: remaining still 47, but K=5
        self.assertEqual(len(leftover_extra_remaining(leftover, dropped_stems)), 47)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_exactly_6_share_071(leftover, dropped_stems)
        )
        tied_stems = tuple("013" if nxt == "001" else nxt for nxt in stems)
        tied_g, tied_k, tied_unique = select_remaining_g(
            leftover_extra_remaining_next_stems(leftover, tied_stems)
        )
        self.assertEqual(tied_g, "013")
        self.assertEqual(tied_k, 8)
        self.assertTrue(tied_unique)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_exactly_6_share_071(leftover, tied_stems)
        )
        # make 013 also 6: unique G=071 still, wait we need a tie at 6
        # 013 is 5; promote one hapax to 013... already 5. Promote one 001 to 071? 
        # Better: change three 001 to a new stem? For tie: change one hapax to 071? that is K=7.
        # Change remaining 013 sites so 013 count becomes 6 by converting one 001 to 013.
        one_more_013 = tuple("013" if nxt == "001" and leftover[i] == (SIDE_IA, "Ia4", 134) else nxt for i, nxt in enumerate(stems))
        tie_g, tie_k, tie_unique = select_remaining_g(
            leftover_extra_remaining_next_stems(leftover, one_more_013)
        )
        self.assertEqual(tie_k, 6)
        self.assertFalse(tie_unique)
        self.assertIn(tie_g, ("071", "013"))
        self.assertFalse(
            i_leftover_extra_090_076_remaining_exactly_6_share_071(leftover, one_more_013)
        )
        make_070 = tuple(None if nxt == "071" else nxt for nxt in stems)
        self.assertEqual(len(leftover_extra_remaining(leftover, make_070)), 41)
        self.assertFalse(
            i_leftover_extra_090_076_remaining_exactly_6_share_071(leftover, make_070)
        )
        self.assertEqual(STANDING_CLAIM, "i_leftover_extra_090_076_remaining_exactly_6_share_071")
        self.assertTrue(STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071)
        self.assertEqual(
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071,
            HYPOTHESIS_K == STANDING_K,
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING)
        self.assertEqual(6 + 41, 47)
        self.assertEqual(STANDING_N_WITH_NEXT - STANDING_N_SHARE_070, STANDING_N_REMAINING)
        self.assertEqual(55 - 8, 47)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal remaining counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"013": 4, "071": 4, "700": 2})
        ranked = rank_remaining_next_stems(counts)
        self.assertEqual(ranked[0], ("071", 4))
        self.assertEqual(ranked[1], ("013", 4))
        self.assertEqual(select_remaining_g(("013", "071", "013", "071", "013", "071", "013", "071"))[0], "071")
        self.assertFalse(select_remaining_g(("013", "071", "013", "071", "013", "071", "013", "071"))[2])
        self.assertEqual(select_remaining_g(("005", "700", "005", "700"))[0], "700")
        self.assertFalse(select_remaining_g(("005", "700", "005", "700"))[2])
        self.assertEqual(select_remaining_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
        self.assertFalse(STANDING_SAME_AS_CYCLE222)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverExtra090076RemainingNextStemScoreboard(unittest.TestCase):
    """Cited-fixture leftover extra remaining next-stem lock. Mock only."""

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
        self.remaining_stems = leftover_extra_remaining_next_stems(
            self.leftover_sites,
            self.next_stems,
        )
        self.matching = leftover_extra_remaining_with_g(
            self.leftover_sites,
            self.next_stems,
        )
        self.without = leftover_extra_remaining_without_g(
            self.leftover_sites,
            self.next_stems,
        )
        self.frequency = remaining_next_stem_frequency_table(
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
        self.n_distinct_remaining = len(self.frequency)
        self.g, self.k, self.unique = select_remaining_g(self.remaining_stems)
        self.n_without = len(self.without)
        self.claim_holds = i_leftover_extra_090_076_remaining_exactly_6_share_071(
            self.leftover_sites,
            self.next_stems,
        )

    def test_tokens_and_nested_leftover_extra_56_55_8_not_retuned(self):
        """2-gram and leftover extra 56/55/1 / exactly 8 share 070 stay."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "071"))
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
        prior_222 = self.survey["i_leftover_n4_remaining_next_2gram"]
        self.assertEqual(prior_222["cycle"], 222)
        self.assertEqual(prior_222["K"], CYCLE222_K)
        self.assertEqual(prior_222["K"], 5)
        self.assertEqual(tuple(prior_222["G"]), CYCLE222_G)
        self.assertTrue(prior_222["i_leftover_n4_remaining_exactly_5_contain_090_076"])
        self.assertTrue(CYCLE222_CLAIM)
        prior_207 = self.survey["i_3gram_090_076_070_i_only"]
        self.assertEqual(prior_207["cycle"], 207)
        self.assertEqual(prior_207["N_I"], 8)
        self.assertEqual(prior_207["N_off_I"], 1)
        self.assertFalse(prior_207["i_3gram_090_076_070_i_only"])
        if prior_207["N_I"] != 8 or prior_207["N_off_I"] != 1:
            self.fail("nested cycle 207 090 076 070 leak 8/1 drifted")
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_4GRAM_I_ONLY_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_47_remaining_g_071_k_6_and_hypothesis_holds(self):
        """N_remaining=47, N_distinct=29, G=071 K=6 unique. Claim holds."""
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
        self.assertEqual(self.share_070, CYCLE226_MATCHING_SITES)
        self.assertEqual(self.share_070, CYCLE225_G_SITES)
        self.assertEqual(self.share_070, CYCLE207_I_SITES)
        if (
            self.n_leftover != 56
            or self.n_with_next != 55
            or self.n_no_next != 1
            or self.n_share_070 != 8
        ):
            self.fail("nested leftover extra 56/55/1 / exactly 8 share 070 drifted")
        self.assertTrue(
            leftover_extra_nested_counts_hold(
                self.n_leftover,
                self.n_with_next,
                self.n_no_next,
                self.n_share_070,
            )
        )
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING)
        self.assertEqual(STANDING_N_REMAINING, 47)
        self.assertEqual(self.n_remaining, self.n_with_next - self.n_share_070)
        self.assertEqual(55 - 8, 47)
        if self.n_remaining != 47:
            self.fail("measured N_remaining drifted from 47")
        if self.n_remaining != self.n_with_next - self.n_share_070:
            self.fail("leftover extra remaining filter disagrees with nested 55−8")
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_NEXT_STEMS)
        self.assertEqual(len(self.remaining), len(self.remaining_stems))
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.remaining)
        self.assertIn(STANDING_IA2_174, self.remaining)
        self.assertEqual(STANDING_IA2_174_NEXT_STEM, "000")
        for site in self.share_070:
            self.assertNotIn(site, self.remaining)
        self.assertEqual(self.n_distinct_remaining, STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(STANDING_N_DISTINCT_REMAINING, 29)
        self.assertEqual(self.frequency, STANDING_REMAINING_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "071")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, HYPOTHESIS_K)
        self.assertEqual(STANDING_K, 6)
        self.assertTrue(self.unique)
        self.assertTrue(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "071")
        self.assertEqual(self.frequency[0][1], 6)
        self.assertEqual(self.frequency[1][0], STANDING_N_NEXT_AFTER_G_STEM)
        self.assertEqual(self.frequency[1][1], STANDING_N_NEXT_AFTER_G)
        self.assertEqual(STANDING_N_NEXT_AFTER_G, 5)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 41)
        self.assertEqual(self.k + self.n_without, self.n_remaining)
        self.assertEqual(6 + 41, 47)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX_REMAINING)
        self.assertEqual(STANDING_N_HAPAX_REMAINING, 19)
        self.assertTrue(
            i_leftover_extra_090_076_remaining_exactly_6_share_071(
                self.leftover_sites,
                self.next_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071,
        )
        self.assertTrue(STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071)
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_extra_090_076_remaining_exactly_6_share_071",
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE222)
        self.assertFalse(STANDING_SAME_AS_CYCLE226)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE222)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE226)
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
        self.assertEqual(CYCLE225_N_DISTINCT, 30)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_extra_remaining_sites_share_071(self):
        """Six leftover extra remaining sites are 090 076 071."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia4", 154), ("090", "076", "071", "633")),
            ((SIDE_IA, "Ia5", 2), ("090", "076", "071", "295")),
            ((SIDE_IA, "Ia5", 23), ("090", "076", "071", "007")),
            ((SIDE_IA, "Ia5", 66), ("090", "076", "071", "004")),
            ((SIDE_IA, "Ia13", 152), ("090", "076", "071", "076")),
            ((SIDE_IA, "Ia14", 105), ("090", "076", "071", "600")),
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
            self.assertEqual(stems[index + STANDING_N2], "071")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "071")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
            self.assertIn(site, STANDING_REMAINING_SITES)
            self.assertNotIn(site, CYCLE224_INSIDE_SITES)
            self.assertNotIn(site, CYCLE226_MATCHING_SITES)
            self.assertNotIn(site, CYCLE207_I_SITES)
        self.assertNotIn(STANDING_IA2_174, self.matching)
        self.assertNotIn(STANDING_NO_NEXT_SITES[0], self.matching)
        self.assertIn(STANDING_IA2_174, self.remaining)
        self.assertEqual(self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_IA2_174)], "000")
        self.assertIsNone(self.next_stems[STANDING_LEFTOVER_SITES.index(STANDING_NO_NEXT_SITES[0])])
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "071")
            self.assertNotEqual(nxt, "070")
            self.assertIn(site, STANDING_REMAINING_SITES)
        for site in self.share_070:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in CYCLE224_INSIDE_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[3], "Ia4")
        self.assertEqual(IA_LINE_NAMES[4], "Ia5")
        self.assertEqual(IA_LINE_NAMES[12], "Ia13")
        self.assertEqual(IA_LINE_NAMES[13], "Ia14")
        self.assertTrue(STANDING_I_ONLY_OF_090_076_G_IS_NOT_THIS_CYCLE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_226_223_222_207_and_171_still_compute(self):
        """Cycle 226 K=8 / G=070, 223 69/3, 222 K=5, 207 8/1, 171 43/0 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
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
        """CORPUS_SURVEY.json records the cycle-227 leftover extra remaining lock."""
        lock = self.survey["i_leftover_extra_090_076_remaining_next_stem"]
        self.assertEqual(lock["cycle"], 227)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(lock["hypothesis_k"], HYPOTHESIS_K)
        self.assertEqual(lock["hypothesis_k"], 6)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(lock["locked_forward_stem"], LOCKED_FORWARD_STEM)
        self.assertEqual(lock["locked_forward_stem"], "070")
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
        self.assertEqual(lock["ia2_174_next_stem"], STANDING_IA2_174_NEXT_STEM)
        self.assertEqual(lock["ia2_174_next_stem"], "000")
        self.assertEqual(lock["N_remaining"], STANDING_N_REMAINING)
        self.assertEqual(lock["N_remaining"], 47)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(tuple(lock["remaining_next_stems"]), STANDING_REMAINING_NEXT_STEMS)
        self.assertEqual(lock["N_distinct_remaining"], STANDING_N_DISTINCT_REMAINING)
        self.assertEqual(lock["N_distinct_remaining"], 29)
        self.assertEqual(lock["N_hapax_remaining"], STANDING_N_HAPAX_REMAINING)
        self.assertEqual(lock["N_hapax_remaining"], 19)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "071")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 6)
        self.assertTrue(lock["G_uniquely_most_frequent"])
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 41)
        self.assertEqual(lock["N_next_after_G"], STANDING_N_NEXT_AFTER_G)
        self.assertEqual(lock["N_next_after_G"], 5)
        self.assertEqual(lock["next_after_G"], STANDING_N_NEXT_AFTER_G_STEM)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_extra_remaining_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_extra_remaining_local_4grams"],
            matching_leftover_extra_remaining_local_4gram_rows(),
        )
        self.assertEqual(
            lock["remaining_next_stem_frequency"],
            remaining_next_stem_frequency_rows(),
        )
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertTrue(lock["i_leftover_extra_090_076_remaining_exactly_6_share_071"])
        self.assertEqual(
            lock["i_leftover_extra_090_076_remaining_exactly_6_share_071"],
            STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_EXACTLY_6_SHARE_071,
        )
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle222"])
        self.assertFalse(lock["same_as_cycle226"])
        self.assertTrue(lock["same_claim_shape_as_cycle222"])
        self.assertTrue(lock["same_claim_shape_as_cycle226"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_090_076_G_is_not_this_cycle"])
        self.assertTrue(lock["leftover_extra_4gram_i_only_is_not_this_cycle"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["inside_family_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["cycle224_no_next_4gram_is_not_no_next_token"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_070_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
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


class TestMamariILeftoverExtra090076RemainingNextStemImageSnapshot(unittest.TestCase):
    """Cycle 227 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
