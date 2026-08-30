"""I's leftover n=4 remaining remaining-after-087 next-stem lock.

Cycle 294 text-search lock. Uses already-vendored A–V and the
cycle-224 leftover n=4 remaining I sites of 2-gram 090 076
(the 13 I sites that sit inside leftover n=4 remaining
maximals 090 076 020 010, 021 090 076 087, 600 090 076 011,
999 021 090 076, or 090 076 057 600). Does not retune that
2-gram, those leftover n=4 remaining sites, the leftover n=4
set, leftover extra peels (225–287), leftover n=4 remaining
share-one-forward-stem (cycle 288 lost), leftover n=4
remaining exactly 4 share next 020 (cycle 289), leftover n=4
remaining remaining-after-020 unique next stem (cycle 292),
or leftover n=4 remaining remaining-after-020 exactly 3 share
next 087 (cycle 293). Does not vendor a new tablet. Does not
scrape X. W has no Barthel (cycle 100); skip W. Unpublished
Ib is 0. Does not redo H∩P∩Q n≥8 or G–K inventories. Raw
stems. No invented Barthel. No G00n→Barthel map. No type
merge. No detector retune. No CV. No new agents. Not a
meaning dictionary.

Leftover n=4 remaining remaining-after-087 next stems are
not yet locked as unique-max. Cycle 292 unique-max G/K is
inventory for the 087 peel, not remaining-after-087
unique-max. Cycle 292 frequency of remaining-after-020
minus 087 (057×2, 011×2, hapax 607/021) is nested
inventory, not this claim; measure remaining-after-087
from the 6 sites. Cycle 245 leftover extra 090 076 087
I-only 5/0 extra I=3 equals leftover n=4 remaining
remaining-after-020 087 sites; do not retune 245/293. Do
not peel a specific remaining-after-087 stem this cycle.
Do not lock I-only of remaining-after-087 3-grams this
cycle. Off-I T sites are not this cycle. 076 071 and
076 070 do not count as this 2-gram. Leftover extra sites
do not count as leftover n=4 remaining.

Leftover n=4 remaining remaining-after-087 = leftover n=4
remaining I 090 076 sites whose next token is neither 020
nor 087. For each such site, take the next token if any
(lock line-final / no-next count separately). Nested-check
leftover n=4 remaining N_inside==13, K_020==4,
N_remaining_after_020==9, K_087==3, N_remaining_after_087==6
(do not retune 224/288/289/292/293). Nested-check cycle 245
extra I equals leftover n=4 remaining remaining-after-020
087 sites (do not retune 245/293). Count next-stem
frequencies among remaining-after-087 sites that have a
next token. G = the next stem with the highest remaining-
after-087 with-next count. If a tie, pick the larger
Barthel id. K = that count.

Claim that can lose:
i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem.
True iff remaining-after-087 leftover n=4 remaining I
090 076 has a unique most frequent next stem G with K ≥ 2
(no tie at max K). This can lose the same way cycle 234
lost (7-way tie at 2) and cycle 270 lost (5-way tie at
K=2), or hold the same way cycle 292 held (G=087 K=3).
Unique-max G/K is inventory for a later peel if the claim
holds or loses with K≥2. Measured: N_remaining_after_087=6,
N_with_next=6, N_no_next=0, N_distinct=4, 2-way tie at K=2
(057×2 / 011×2), G=057 (largest-id tie-break), unique-max
false. The claim is false. Nested cycle 293 K_087=3
N_remaining=6 extra I overlap, cycle 292 unique-max G=087
K=3, cycle 289 K_020=4, cycle 288 N_distinct=6 unique-max
G=020 K=4, cycle 245 5/0 extra I=3, cycle 224 13/56, and
cycle 223 69/3 stay. Do not assume the result; measure.
Do not retune.

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
    STANDING_INSIDE_SITES,
    STANDING_LEFTOVER_SITES,
    STANDING_N_I as CYCLE224_N_I,
    STANDING_N_INSIDE as CYCLE224_N_INSIDE,
    STANDING_N_LEFTOVER as CYCLE224_N_LEFTOVER,
    TestMamariI090076InsideLeftoverN4RemainingFamilyScoreboard,
    leftover_local_4grams,
)
from tests.test_mamari_i_2gram_076_071_i_only_scoreboard import (
    GRAM2 as CYCLE171_GRAM2,
)
from tests.test_mamari_i_2gram_090_076_i_only_scoreboard import (
    GRAM2,
    STANDING_I_SITES,
    STANDING_N_I,
    STANDING_N_OFF_I,
    STANDING_OFF_I_SITES,
    TestMamariI2gram090076IOnlyScoreboard,
)
from tests.test_mamari_i_3gram_090_076_087_i_only_scoreboard import (
    GRAM3 as CYCLE245_GRAM3,
    STANDING_EXTRA_I_SITES as CYCLE245_EXTRA_I_SITES,
    STANDING_I_3GRAM_090_076_087_I_ONLY as CYCLE245_CLAIM,
    STANDING_I_SITES as CYCLE245_I_SITES,
    STANDING_N_EXTRA as CYCLE245_N_EXTRA,
    STANDING_N_I as CYCLE245_N_I,
    STANDING_N_OFF_I as CYCLE245_N_OFF_I,
    TestMamariI3gram090076087IOnlyScoreboard,
)
from tests.test_mamari_i_leftover_076_071_forward_076_scoreboard import (
    site_forward_3gram,
    site_next_4gram,
)
from tests.test_mamari_i_leftover_extra_090_076_forward_stem_scoreboard import (
    group_sites_by_next_stem,
    leftover_sites_with_next,
    leftover_sites_without_next,
    site_next_stem,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_000_next_stem_scoreboard import (
    STANDING_G as CYCLE256_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE256_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_000_UNIQUE_MAX_NEXT_STEM as CYCLE256_CLAIM,
    STANDING_K as CYCLE256_K,
    STANDING_N_DISTINCT_REMAINING11 as CYCLE256_N_DISTINCT,
    STANDING_N_REMAINING11 as CYCLE256_N_REMAINING11,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_001_next_stem_scoreboard import (
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE234_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_001_EXACTLY_K_SHARE_G as CYCLE234_CLAIM,
    STANDING_K as CYCLE234_K,
    STANDING_N_TIED_AT_K as CYCLE234_N_TIED_AT_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_after_600_previous_stem_scoreboard import (
    STANDING_G as CYCLE270_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE270_UNIQUE,
    STANDING_I_LEFTOVER_EXTRA_090_076_REMAINING_AFTER_600_UNIQUE_PREVIOUS_STEM as CYCLE270_CLAIM,
    STANDING_K as CYCLE270_K,
    STANDING_N_TIED_AT_K as CYCLE270_N_TIED_AT_K,
)
from tests.test_mamari_i_leftover_extra_090_076_remaining_next_stem_scoreboard import (
    barthel_id,
)
from tests.test_mamari_i_leftover_n4_maximals_076_scoreboard import (
    EXCEPTION_GRAM,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_020_scoreboard import (
    GRAM3_FORWARD as GRAM3_NESTED_020,
    STANDING_G as CYCLE289_G,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_EXACTLY_4_SHARE_FORWARD_020 as CYCLE289_CLAIM,
    STANDING_K as CYCLE289_K,
    STANDING_MATCHING_SITES as CYCLE289_MATCHING_SITES,
    STANDING_N_INSIDE as CYCLE289_N_INSIDE,
    STANDING_N_REMAINING_AFTER_020 as CYCLE289_N_REMAINING_AFTER_020,
    STANDING_REMAINING_AFTER_020_SITES as CYCLE289_REMAINING_AFTER_020_SITES,
    TestMamariILeftoverN4Remaining090076Forward020Scoreboard,
    leftover_n4_remaining_with_forward_020,
    leftover_n4_remaining_without_forward_020,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_forward_stem_scoreboard import (
    STANDING_G as CYCLE288_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE288_UNIQUE_MAX,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_SHARE_ONE_FORWARD_STEM as CYCLE288_SHARE_ONE,
    STANDING_K as CYCLE288_K,
    STANDING_N_DISTINCT_NEXT_STEMS as CYCLE288_N_DISTINCT,
    STANDING_N_INSIDE as CYCLE288_N_INSIDE,
    STANDING_N_NO_NEXT as CYCLE288_N_NO_NEXT,
    STANDING_N_WITH_NEXT as CYCLE288_N_WITH_NEXT,
    STANDING_NEXT_STEM_FREQUENCY as CYCLE288_FREQUENCY,
    TestMamariILeftoverN4Remaining090076ForwardStemScoreboard,
    leftover_n4_remaining_forward_3grams,
    leftover_n4_remaining_next_4grams,
    leftover_n4_remaining_next_stems,
    leftover_n4_remaining_sites_with_next,
    leftover_n4_remaining_sites_without_next,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_forward_087_scoreboard import (
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_EXACTLY_3_SHARE_FORWARD_087 as CYCLE293_CLAIM,
    STANDING_K_087 as CYCLE293_K_087,
    STANDING_MATCHING_EQUALS_CYCLE245_EXTRA_I as CYCLE293_EQUALS_245,
    STANDING_MATCHING_SITES as CYCLE293_MATCHING_SITES,
    STANDING_N_REMAINING_AFTER_020 as CYCLE293_N_REMAINING_AFTER_020,
    STANDING_N_REMAINING_AFTER_087 as CYCLE293_N_REMAINING_AFTER_087,
    STANDING_REMAINING_AFTER_087_SITES as CYCLE293_REMAINING_AFTER_087_SITES,
    TestMamariILeftoverN4Remaining090076RemainingAfter020Forward087Scoreboard,
    leftover_n4_remaining_remaining_after_020_with_forward_087,
    leftover_n4_remaining_remaining_after_020_without_forward_087,
    matching_equals_cycle245_extra_i,
)
from tests.test_mamari_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_scoreboard import (
    STANDING_G as CYCLE292_G,
    STANDING_G_UNIQUELY_MOST_FREQUENT as CYCLE292_UNIQUE,
    STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_020_UNIQUE_NEXT_STEM as CYCLE292_CLAIM,
    STANDING_K as CYCLE292_K,
    STANDING_MATCHING_SITES as CYCLE292_MATCHING_SITES,
    STANDING_N_DISTINCT as CYCLE292_N_DISTINCT,
    STANDING_N_REMAINING_AFTER_020 as CYCLE292_N_REMAINING,
    STANDING_REMAINING_FREQUENCY as CYCLE292_REMAINING_FREQUENCY,
    STANDING_REMAINING_SITES as CYCLE292_REMAINING_SITES,
    leftover_n4_remaining_remaining_after_020,
    leftover_n4_remaining_remaining_after_020_nested_counts_hold,
    leftover_n4_remaining_remaining_after_020_next_stems,
    leftover_n4_remaining_remaining_after_020_with_next,
    leftover_n4_remaining_remaining_after_020_without_next,
    TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard,
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

LOCKED_FORWARD_STEMS = ("020", "087")
STANDING_N2 = 2
STANDING_N3 = 3
STANDING_N4 = 4
GRAM3_FORWARD = ("090", "076", "057")
STANDING_N_I = 69
STANDING_N_INSIDE = 13
STANDING_N_LEFTOVER_EXTRA = 56
STANDING_N_WITH_NEXT_INSIDE = 13
STANDING_N_NO_NEXT_INSIDE = 0
STANDING_K_020 = 4
STANDING_N_REMAINING_AFTER_020 = 9
STANDING_K_087 = 3
STANDING_N_REMAINING_AFTER_087 = 6
STANDING_N_WITH_NEXT = 6
STANDING_N_NO_NEXT = 0
STANDING_NO_NEXT_SITES = ()
STANDING_N_DISTINCT = 4
STANDING_N_HAPAX = 2
STANDING_G = "057"
STANDING_K = 2
STANDING_N_WITHOUT_G = 4
STANDING_N_TIED_AT_K = 2
STANDING_TIED_STEMS = ("057", "011")
STANDING_G_UNIQUELY_MOST_FREQUENT = False
STANDING_REMAINING_SITES = CYCLE293_REMAINING_AFTER_087_SITES
STANDING_REMAINING_NEXT_STEMS = (
    "011",
    "607",
    "057",
    "057",
    "021",
    "011",
)
STANDING_MATCHING_SITES = (
    (SIDE_IA, "Ia8", 114),
    (SIDE_IA, "Ia9", 28),
)
STANDING_MATCHING_NEXT_4GRAMS = (
    ("090", "076", "057", "600"),
    ("090", "076", "057", "600"),
)
STANDING_REMAINING_FREQUENCY = (
    (
        "057",
        2,
        STANDING_MATCHING_SITES,
        (("090", "076", "057"),) * 2,
    ),
    (
        "011",
        2,
        ((SIDE_IA, "Ia2", 107), (SIDE_IA, "Ia14", 54)),
        (("090", "076", "011"),) * 2,
    ),
    ("607", 1, ((SIDE_IA, "Ia8", 106),), (("090", "076", "607"),)),
    ("021", 1, ((SIDE_IA, "Ia13", 17),), (("090", "076", "021"),)),
)
STANDING_CYCLE292_REMAINING_AFTER_087_INVENTORY = (
    ("057", 2),
    ("011", 2),
    ("607", 1),
    ("021", 1),
)
STANDING_KNOWN_DISTINCT = True
STANDING_CLAIM = "i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem"
STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_UNIQUE_NEXT_STEM = False
STANDING_RESULT = "i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"
STANDING_NEW_TABLET = False
STANDING_W_BARTHEL = False
STANDING_N_GE_8_ISLAND = False
STANDING_TABLET_ONLY = True
STANDING_SAME_AS_I_5GRAM = False
STANDING_SAME_AS_CYCLE234 = False
STANDING_SAME_AS_CYCLE256 = False
STANDING_SAME_AS_CYCLE270 = False
STANDING_SAME_AS_CYCLE288 = False
STANDING_SAME_AS_CYCLE289 = False
STANDING_SAME_AS_CYCLE292 = False
STANDING_SAME_AS_CYCLE293 = False
STANDING_SAME_AS_CYCLE245 = False
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE270 = True
STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292 = True
STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE = True
STANDING_I_ONLY_OF_REMAINING_AFTER_087_3GRAM_IS_NOT_THIS_CYCLE = True
STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM = True
STANDING_CYCLE292_FREQUENCY_MINUS_087_IS_NESTED_INVENTORY = True
STANDING_CYCLE245_EXTRA_I_EQUALS_REMAINING_AFTER_020_087 = True
STANDING_076_071_DOES_NOT_COUNT = True
STANDING_076_070_DOES_NOT_COUNT = True
STANDING_LEFTOVER_EXTRA_DOES_NOT_COUNT = True
STANDING_LEFTOVER_N4_SET_NOT_RETUNED = True
STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED = True
STANDING_CYCLE167_268_293_NOT_OVERWRITTEN = True
STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL = True


def leftover_n4_remaining_remaining_after_087(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining sites whose next token is neither 020 nor 087."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt not in locked_set
    )


def leftover_n4_remaining_remaining_after_087_next_stems(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[str, ...]:
    """Next stems of remaining-after-087 sites that have a next token."""
    locked_set = set(locked)
    return tuple(
        nxt
        for nxt in next_stems
        if nxt is not None and nxt not in locked_set
    )


def leftover_n4_remaining_remaining_after_087_with_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-087 leftover n=4 remaining sites that have a next token."""
    remaining = leftover_n4_remaining_remaining_after_087(sites, next_stems, locked)
    rem_next = tuple(
        nxt
        for site, nxt in zip(sites, next_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_with_next(remaining, rem_next)


def leftover_n4_remaining_remaining_after_087_without_next(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Remaining-after-087 leftover n=4 remaining sites with no next token."""
    remaining = leftover_n4_remaining_remaining_after_087(sites, next_stems, locked)
    rem_next = tuple(
        nxt
        for site, nxt in zip(sites, next_stems, strict=True)
        if site in remaining
    )
    return leftover_sites_without_next(remaining, rem_next)


def leftover_n4_remaining_remaining_after_087_with_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-087 sites whose next token is G."""
    remaining = set(leftover_n4_remaining_remaining_after_087(sites, next_stems, locked))
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt == stem and site in remaining
    )


def leftover_n4_remaining_remaining_after_087_without_g(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    stem: str = STANDING_G,
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[tuple[str, str, int], ...]:
    """Leftover n=4 remaining remaining-after-087 sites whose next token is not G."""
    locked_set = set(locked)
    return tuple(
        site
        for site, nxt in zip(sites, next_stems, strict=True)
        if nxt is not None and nxt not in locked_set and nxt != stem
    )


def remaining_after_087_next_stem_counts(next_stems: tuple[str, ...]) -> Counter:
    """Counts of next stems among leftover n=4 remaining remaining-after-087 with-next."""
    return Counter(next_stems)


def rank_remaining_after_087_next_stems(
    counts: Counter,
) -> tuple[tuple[str, int], ...]:
    """Remaining-after-087 next stems by count, then larger Barthel id."""
    return tuple(
        sorted(
            counts.items(),
            key=lambda item: (-item[1], -barthel_id(item[0])),
        )
    )


def select_remaining_after_087_g(
    remaining_stems: tuple[str, ...],
) -> tuple[str | None, int, bool]:
    """Return (G, K, uniquely_most_frequent). Empty remaining-after-087 has no G."""
    ranked = rank_remaining_after_087_next_stems(
        remaining_after_087_next_stem_counts(remaining_stems)
    )
    if not ranked:
        return (None, 0, False)
    gram, count = ranked[0]
    unique = sum(1 for _stem, other in ranked if other == count) == 1
    return (gram, count, unique)


def remaining_after_087_next_stem_frequency_table(
    sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    forward_3grams: tuple[tuple[str, ...] | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> tuple[
    tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
    ...,
]:
    """Remaining-after-087 next-stem frequency: highest count first, then larger id."""
    rem_sites = leftover_n4_remaining_remaining_after_087_with_next(
        sites, next_stems, locked
    )
    rem_stems = leftover_n4_remaining_remaining_after_087_next_stems(
        sites, next_stems, locked
    )
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


def remaining_after_087_next_stem_frequency_rows(
    table: tuple[
        tuple[str, int, tuple[tuple[str, str, int], ...], tuple[tuple[str, ...], ...]],
        ...,
    ] = STANDING_REMAINING_FREQUENCY,
) -> list[dict]:
    """Survey-shaped remaining-after-087 next-stem frequency table."""
    rows = []
    for stem, count, sites, grams in table:
        rows.append(
            {
                "next_stem": stem,
                "count": count,
                "leftover_n4_remaining_remaining_after_087_sites": [
                    list(site) for site in sites
                ],
                "forward_3grams": [list(gram) for gram in grams],
            }
        )
    return rows


def leftover_n4_remaining_remaining_after_087_nested_counts_hold(
    n_inside: int,
    k_020: int,
    n_remaining_after_020: int,
    k_087: int,
    n_remaining: int,
    expected_inside: int = STANDING_N_INSIDE,
    expected_k_020: int = STANDING_K_020,
    expected_remaining_after_020: int = STANDING_N_REMAINING_AFTER_020,
    expected_k_087: int = STANDING_K_087,
    expected_remaining: int = STANDING_N_REMAINING_AFTER_087,
) -> bool:
    """Nested leftover n=4 remaining 13/4/9/3/6."""
    return (
        n_inside == expected_inside
        and k_020 == expected_k_020
        and n_remaining_after_020 == expected_remaining_after_020
        and k_087 == expected_k_087
        and n_remaining == expected_remaining
        and n_remaining_after_020 == n_inside - k_020
        and n_remaining == n_remaining_after_020 - k_087
    )


def i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem(
    inside_sites: tuple[tuple[str, str, int], ...],
    next_stems: tuple[str | None, ...],
    locked: tuple[str, ...] = LOCKED_FORWARD_STEMS,
) -> bool:
    """True iff remaining-after-087 has a unique most frequent next stem with K ≥ 2."""
    remaining = leftover_n4_remaining_remaining_after_087(
        inside_sites,
        next_stems,
        locked,
    )
    remaining_stems = leftover_n4_remaining_remaining_after_087_next_stems(
        inside_sites,
        next_stems,
        locked,
    )
    if len(remaining) != STANDING_N_REMAINING_AFTER_087:
        return False
    if remaining != leftover_n4_remaining_remaining_after_020_without_forward_087(
        inside_sites,
        next_stems,
    ):
        return False
    gram, count, unique = select_remaining_after_087_g(remaining_stems)
    return bool(unique and gram is not None and count >= 2)


def matching_leftover_n4_remaining_remaining_after_087_local_4gram_rows(
    leftover_sites: tuple[tuple[str, str, int], ...] = STANDING_MATCHING_SITES,
    next_4grams: tuple[tuple[str, ...], ...] = STANDING_MATCHING_NEXT_4GRAMS,
) -> list[dict]:
    """Survey-shaped matching leftover n=4 remaining remaining-after-087 next-4-gram rows."""
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


class TestILeftoverN4Remaining090076RemainingAfter087NextStemHelpers(unittest.TestCase):
    """Helpers on leftover n=4 remaining remaining-after-087 next stems. No CV, no LLM."""

    def test_remaining_after_087_requires_next_neither_020_nor_087(self):
        """Remaining-after-087 excludes next 020 and 087; line-final is remaining, no-next."""
        provider = MockProvider()
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "057"))
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("020", "087"))
        self.assertEqual(len(GRAM2), STANDING_N2)
        self.assertEqual(len(GRAM3_FORWARD), STANDING_N3)
        self.assertEqual(STANDING_N4, STANDING_N2 + 2)
        has_057 = ["090", "076", "057", "600"]
        self.assertEqual(site_next_stem(has_057, 0, GRAM2), "057")
        self.assertEqual(site_forward_3gram(has_057, 0, GRAM2), GRAM3_FORWARD)
        self.assertEqual(
            site_next_4gram(has_057, 0, GRAM2),
            ("090", "076", "057", "600"),
        )
        has_087 = ["090", "076", "087", "291"]
        self.assertEqual(site_next_stem(has_087, 0, GRAM2), "087")
        self.assertNotEqual(site_next_stem(has_087, 0, GRAM2), "057")
        has_020 = ["090", "076", "020", "010"]
        self.assertEqual(site_next_stem(has_020, 0, GRAM2), "020")
        self.assertNotEqual(site_next_stem(has_020, 0, GRAM2), "057")
        end_of_line = ["999", "021", "090", "076"]
        self.assertIsNone(site_next_stem(end_of_line, 2, GRAM2))
        planted_sites = (
            (SIDE_IA, "Ia1", 0),
            (SIDE_IA, "Ia1", 1),
            (SIDE_IA, "Ia1", 2),
            (SIDE_IA, "Ia1", 3),
            (SIDE_IA, "Ia1", 4),
        )
        planted_stems = ("057", "020", None, "011", "087")
        rem = leftover_n4_remaining_remaining_after_087(planted_sites, planted_stems)
        self.assertEqual(rem, (planted_sites[0], planted_sites[2], planted_sites[3]))
        self.assertEqual(
            leftover_n4_remaining_remaining_after_087_next_stems(
                planted_sites, planted_stems
            ),
            ("057", "011"),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_087_with_next(
                planted_sites, planted_stems
            ),
            (planted_sites[0], planted_sites[3]),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_087_without_next(
                planted_sites, planted_stems
            ),
            (planted_sites[2],),
        )
        self.assertEqual(
            leftover_n4_remaining_remaining_after_087_with_g(
                planted_sites, planted_stems
            ),
            (planted_sites[0],),
        )
        self.assertNotIn(planted_sites[1], rem)
        self.assertNotIn(planted_sites[4], rem)
        mismatch_071 = ["076", "071", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_071, 0, GRAM2))
        mismatch_070 = ["076", "070", "090", "999"]
        self.assertIsNone(site_next_stem(mismatch_070, 0, GRAM2))
        self.assertTrue(STANDING_076_071_DOES_NOT_COUNT)
        self.assertTrue(STANDING_076_070_DOES_NOT_COUNT)
        self.assertTrue(STANDING_CYCLE292_FREQUENCY_MINUS_087_IS_NESTED_INVENTORY)
        self.assertEqual(provider.get_call_history(), [])

    def test_unique_max_can_fail(self):
        """Boolean is True only when remaining=6 and some G has unique K≥2."""
        provider = MockProvider()
        inside = STANDING_INSIDE_SITES
        stems = leftover_n4_remaining_next_stems(load_i_sides(), inside, GRAM2)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem(
                inside,
                stems,
            )
        )
        rem = leftover_n4_remaining_remaining_after_087(inside, stems)
        rem_stems = leftover_n4_remaining_remaining_after_087_next_stems(inside, stems)
        self.assertEqual(len(rem), STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(len(rem), 6)
        self.assertEqual(rem, STANDING_REMAINING_SITES)
        self.assertEqual(rem_stems, STANDING_REMAINING_NEXT_STEMS)
        g, k, unique = select_remaining_after_087_g(rem_stems)
        self.assertEqual(g, "057")
        self.assertEqual(k, 2)
        self.assertFalse(unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        empty_stems = ("020",) * len(inside)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem(
                inside,
                empty_stems,
            )
        )
        hold_stems = list(stems)
        # Remaining-after-087 already has 057×2, 011×2. Promote one 011 to 057
        # so unique-max 057×3 (cycle-292 hold shape).
        promote = {(SIDE_IA, "Ia2", 107): "057"}
        for i, site in enumerate(inside):
            if site in promote:
                hold_stems[i] = promote[site]
        held = tuple(hold_stems)
        held_g, held_k, held_unique = select_remaining_after_087_g(
            leftover_n4_remaining_remaining_after_087_next_stems(inside, held)
        )
        self.assertEqual(held_g, "057")
        self.assertEqual(held_k, 3)
        self.assertTrue(held_unique)
        self.assertEqual(
            len(leftover_n4_remaining_remaining_after_087(inside, held)),
            6,
        )
        self.assertTrue(
            i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem(
                inside,
                held,
            )
        )
        hapax_stems = list(stems)
        replacements = {
            (SIDE_IA, "Ia8", 114): "801",
            (SIDE_IA, "Ia14", 54): "802",
        }
        for i, site in enumerate(inside):
            if site in replacements:
                hapax_stems[i] = replacements[site]
        hapax = tuple(hapax_stems)
        hap_g, hap_k, hap_unique = select_remaining_after_087_g(
            leftover_n4_remaining_remaining_after_087_next_stems(inside, hapax)
        )
        self.assertEqual(hap_k, 1)
        self.assertFalse(hap_unique)
        self.assertEqual(
            len(leftover_n4_remaining_remaining_after_087(inside, hapax)),
            6,
        )
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem(
                inside,
                hapax,
            )
        )
        self.assertEqual(
            STANDING_CLAIM,
            "i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem",
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_UNIQUE_NEXT_STEM
        )
        self.assertEqual(STANDING_K + STANDING_N_WITHOUT_G, STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(2 + 4, 6)
        self.assertEqual(
            STANDING_K_087 + STANDING_N_REMAINING_AFTER_087,
            STANDING_N_REMAINING_AFTER_020,
        )
        self.assertEqual(3 + 6, 9)
        self.assertEqual(STANDING_K_020 + STANDING_N_REMAINING_AFTER_020, STANDING_N_INSIDE)
        self.assertEqual(4 + 9, 13)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_087_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertEqual(provider.get_call_history(), [])

    def test_tie_break_picks_larger_barthel_id(self):
        """Equal remaining-after-087 counts pick the larger Barthel id."""
        provider = MockProvider()
        counts = Counter({"057": 2, "011": 2, "607": 1, "021": 1})
        ranked = rank_remaining_after_087_next_stems(counts)
        self.assertEqual(ranked[0], ("057", 2))
        self.assertEqual(ranked[1], ("011", 2))
        self.assertEqual(ranked[2], ("607", 1))
        self.assertEqual(ranked[3], ("021", 1))
        self.assertEqual(select_remaining_after_087_g(("057", "011", "057", "011"))[0], "057")
        self.assertFalse(select_remaining_after_087_g(("057", "011", "057", "011"))[2])
        self.assertEqual(select_remaining_after_087_g(("057", "057", "011"))[0], "057")
        self.assertTrue(select_remaining_after_087_g(("057", "057", "011"))[2])
        self.assertEqual(select_remaining_after_087_g(()), (None, 0, False))
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE270)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE270)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertFalse(CYCLE270_UNIQUE)
        self.assertTrue(CYCLE292_UNIQUE)
        self.assertEqual(provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter087NextStemScoreboard(
    unittest.TestCase
):
    """Cited-fixture leftover n=4 remaining remaining-after-087 next-stem lock. Mock only."""

    def setUp(self):
        self.provider = MockProvider()
        self.survey = load_corpus_survey()
        self.i_sides = load_i_sides()
        self.i_sites = nge4_sites(GRAM2, self.i_sides)
        self.inside_sites = STANDING_INSIDE_SITES
        self.next_stems = leftover_n4_remaining_next_stems(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.forwards = leftover_n4_remaining_forward_3grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.next_4grams = leftover_n4_remaining_next_4grams(
            self.i_sides,
            self.inside_sites,
            GRAM2,
        )
        self.with_next_inside = leftover_n4_remaining_sites_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next_inside = leftover_n4_remaining_sites_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.share_020 = leftover_n4_remaining_with_forward_020(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_after_020 = leftover_n4_remaining_remaining_after_020(
            self.inside_sites,
            self.next_stems,
        )
        self.share_087 = leftover_n4_remaining_remaining_after_020_with_forward_087(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining = leftover_n4_remaining_remaining_after_087(
            self.inside_sites,
            self.next_stems,
        )
        self.remaining_stems = leftover_n4_remaining_remaining_after_087_next_stems(
            self.inside_sites,
            self.next_stems,
        )
        self.with_next = leftover_n4_remaining_remaining_after_087_with_next(
            self.inside_sites,
            self.next_stems,
        )
        self.no_next = leftover_n4_remaining_remaining_after_087_without_next(
            self.inside_sites,
            self.next_stems,
        )
        self.matching = leftover_n4_remaining_remaining_after_087_with_g(
            self.inside_sites,
            self.next_stems,
        )
        self.without = leftover_n4_remaining_remaining_after_087_without_g(
            self.inside_sites,
            self.next_stems,
        )
        self.frequency = remaining_after_087_next_stem_frequency_table(
            self.inside_sites,
            self.next_stems,
            self.forwards,
        )
        self.matching_next_4grams = leftover_n4_remaining_next_4grams(
            self.i_sides,
            self.matching,
            GRAM2,
        )
        self.n_i = len(self.i_sites)
        self.n_inside = len(self.inside_sites)
        self.n_leftover_extra = len(STANDING_LEFTOVER_SITES)
        self.n_with_next_inside = len(self.with_next_inside)
        self.n_no_next_inside = len(self.no_next_inside)
        self.k_020 = len(self.share_020)
        self.n_remaining_after_020 = len(self.remaining_after_020)
        self.k_087 = len(self.share_087)
        self.n_remaining = len(self.remaining)
        self.n_with_next = len(self.with_next)
        self.n_no_next = len(self.no_next)
        self.n_distinct = len(self.frequency)
        self.g, self.k, self.unique = select_remaining_after_087_g(self.remaining_stems)
        self.n_without = len(self.without)
        self.claim_holds = (
            i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem(
                self.inside_sites,
                self.next_stems,
            )
        )

    def test_tokens_and_nested_leftover_n4_remaining_13_4_9_3_6_not_retuned(self):
        """2-gram and leftover n=4 remaining 13/4/9/3/6 stay the cycle-293/292/289/224 locks."""
        self.assertEqual(GRAM2, ("090", "076"))
        self.assertEqual(GRAM2, CYCLE222_G)
        self.assertEqual(GRAM2, CYCLE222_GRAM2)
        self.assertEqual(GRAM3_FORWARD, ("090", "076", "057"))
        self.assertEqual(GRAM3_NESTED_020, ("090", "076", "020"))
        self.assertEqual(CYCLE245_GRAM3, ("090", "076", "087"))
        self.assertEqual(LOCKED_FORWARD_STEMS, ("020", "087"))
        self.assertEqual(self.i_sites, STANDING_I_SITES)
        self.assertEqual(self.i_sites, CYCLE224_I_SITES)
        self.assertEqual(len(self.i_sites), STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        if self.n_i != 69:
            self.fail("nested cycle 223/224 N_I drifted from 69")
        self.assertEqual(self.inside_sites, STANDING_INSIDE_SITES)
        self.assertEqual(len(STANDING_INSIDE_SITES), STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE224_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE288_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, CYCLE289_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(len(STANDING_LEFTOVER_SITES), STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, CYCLE224_N_LEFTOVER)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        self.assertEqual(self.n_i, CYCLE224_N_INSIDE + CYCLE224_N_LEFTOVER)
        self.assertEqual(69, 13 + 56)
        if self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 13/56 drifted")
        prior_293 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"]
        self.assertEqual(prior_293["cycle"], 293)
        self.assertEqual(prior_293["K_087"], 3)
        self.assertEqual(prior_293["N_remaining_after_087"], 6)
        self.assertEqual(prior_293["N_remaining_after_020"], 9)
        self.assertTrue(
            prior_293["i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087"]
        )
        self.assertTrue(CYCLE293_CLAIM)
        self.assertEqual(CYCLE293_K_087, 3)
        self.assertEqual(CYCLE293_N_REMAINING_AFTER_087, 6)
        self.assertEqual(CYCLE293_N_REMAINING_AFTER_020, 9)
        prior_292 = self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]
        self.assertEqual(prior_292["cycle"], 292)
        self.assertEqual(prior_292["G"], "087")
        self.assertEqual(prior_292["K"], 3)
        self.assertEqual(prior_292["N_remaining_after_020"], 9)
        self.assertEqual(prior_292["N_distinct"], 5)
        self.assertTrue(prior_292["G_uniquely_most_frequent"])
        self.assertTrue(CYCLE292_CLAIM)
        self.assertEqual(CYCLE292_G, "087")
        self.assertEqual(CYCLE292_K, 3)
        self.assertEqual(CYCLE292_N_REMAINING, 9)
        self.assertEqual(CYCLE292_N_DISTINCT, 5)
        self.assertTrue(CYCLE292_UNIQUE)
        prior_289 = self.survey["i_leftover_n4_remaining_090_076_forward_020"]
        self.assertEqual(prior_289["cycle"], 289)
        self.assertEqual(prior_289["N_inside"], 13)
        self.assertEqual(prior_289["G"], "020")
        self.assertEqual(prior_289["K"], 4)
        self.assertEqual(prior_289["N_remaining_after_020"], 9)
        self.assertTrue(prior_289["i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"])
        self.assertTrue(CYCLE289_CLAIM)
        self.assertEqual(CYCLE289_G, "020")
        self.assertEqual(CYCLE289_K, 4)
        self.assertEqual(CYCLE289_N_REMAINING_AFTER_020, 9)
        prior_288 = self.survey["i_leftover_n4_remaining_090_076_forward_stem"]
        self.assertEqual(prior_288["cycle"], 288)
        self.assertEqual(prior_288["N_inside"], 13)
        self.assertEqual(prior_288["N_with_next"], 13)
        self.assertEqual(prior_288["N_no_next"], 0)
        self.assertEqual(prior_288["N_distinct_next_stems"], 6)
        self.assertEqual(prior_288["G"], "020")
        self.assertEqual(prior_288["K"], 4)
        self.assertTrue(prior_288["g_uniquely_most_frequent"])
        self.assertFalse(prior_288["i_leftover_n4_remaining_090_076_share_one_forward_stem"])
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertEqual(CYCLE288_N_DISTINCT, 6)
        self.assertEqual(CYCLE288_G, "020")
        self.assertEqual(CYCLE288_K, 4)
        self.assertTrue(CYCLE288_UNIQUE_MAX)
        prior_245 = self.survey["i_3gram_090_076_087_i_only"]
        self.assertEqual(prior_245["cycle"], 245)
        self.assertEqual(prior_245["N_I"], 5)
        self.assertEqual(prior_245["N_off_I"], 0)
        self.assertEqual(prior_245["N_extra"], 3)
        self.assertTrue(prior_245["i_3gram_090_076_087_i_only"])
        self.assertTrue(CYCLE245_CLAIM)
        self.assertEqual(CYCLE245_N_I, 5)
        self.assertEqual(CYCLE245_N_OFF_I, 0)
        self.assertEqual(CYCLE245_N_EXTRA, 3)
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
        unused_224_n = CYCLE224_N_I
        self.assertEqual(unused_224_n, 69)
        unused_288_n = CYCLE288_N_WITH_NEXT
        self.assertEqual(unused_288_n, 13)
        unused_288_no = CYCLE288_N_NO_NEXT
        self.assertEqual(unused_288_no, 0)
        unused_288_freq = CYCLE288_FREQUENCY
        self.assertEqual(unused_288_freq[0][0], "020")
        unused_292_freq = CYCLE292_REMAINING_FREQUENCY
        self.assertEqual(unused_292_freq[0][0], "087")
        unused_292_sites = CYCLE292_REMAINING_SITES
        self.assertEqual(len(unused_292_sites), 9)
        unused_292_match = CYCLE292_MATCHING_SITES
        self.assertEqual(len(unused_292_match), 3)
        unused_293_match = CYCLE293_MATCHING_SITES
        self.assertEqual(unused_293_match, unused_292_match)
        self.assertTrue(CYCLE293_EQUALS_245)
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertFalse(STANDING_W_BARTHEL)
        self.assertTrue(STANDING_KNOWN_DISTINCT)
        self.assertTrue(STANDING_OFF_I_T_SITES_ARE_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_087_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_LEFTOVER_N4_SET_NOT_RETUNED)
        self.assertTrue(STANDING_LEFTOVER_EXTRA_PEELS_NOT_RETUNED)
        self.assertTrue(STANDING_CYCLE167_268_293_NOT_OVERWRITTEN)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_counts_6_remaining_g_057_k_2_tie_and_hypothesis_loses(self):
        """N_remaining=6, N_with_next=6, N_distinct=4, G=057 K=2 2-way tie. Claim loses."""
        self.assertEqual(self.n_i, STANDING_N_I)
        self.assertEqual(STANDING_N_I, 69)
        self.assertEqual(self.n_inside, STANDING_N_INSIDE)
        self.assertEqual(STANDING_N_INSIDE, 13)
        self.assertEqual(self.n_leftover_extra, STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(STANDING_N_LEFTOVER_EXTRA, 56)
        if self.n_i != 69 or self.n_inside != 13 or self.n_leftover_extra != 56:
            self.fail("nested cycle 224 69/13/56 drifted")
        self.assertEqual(self.n_with_next_inside, STANDING_N_WITH_NEXT_INSIDE)
        self.assertEqual(STANDING_N_WITH_NEXT_INSIDE, CYCLE288_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT_INSIDE, 13)
        self.assertEqual(self.n_no_next_inside, STANDING_N_NO_NEXT_INSIDE)
        self.assertEqual(STANDING_N_NO_NEXT_INSIDE, CYCLE288_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT_INSIDE, 0)
        self.assertEqual(self.k_020, STANDING_K_020)
        self.assertEqual(STANDING_K_020, CYCLE289_K)
        self.assertEqual(STANDING_K_020, 4)
        self.assertEqual(self.share_020, CYCLE289_MATCHING_SITES)
        self.assertEqual(self.n_remaining_after_020, STANDING_N_REMAINING_AFTER_020)
        self.assertEqual(STANDING_N_REMAINING_AFTER_020, 9)
        self.assertEqual(self.k_087, STANDING_K_087)
        self.assertEqual(STANDING_K_087, CYCLE293_K_087)
        self.assertEqual(STANDING_K_087, 3)
        self.assertEqual(self.share_087, CYCLE293_MATCHING_SITES)
        self.assertEqual(self.share_087, CYCLE292_MATCHING_SITES)
        self.assertEqual(self.share_087, CYCLE245_EXTRA_I_SITES)
        self.assertTrue(matching_equals_cycle245_extra_i(self.share_087))
        self.assertTrue(STANDING_CYCLE245_EXTRA_I_EQUALS_REMAINING_AFTER_020_087)
        self.assertTrue(
            leftover_n4_remaining_remaining_after_020_nested_counts_hold(
                self.n_inside,
                self.n_with_next_inside,
                self.k_020,
                self.n_remaining_after_020,
            )
        )
        self.assertTrue(
            leftover_n4_remaining_remaining_after_087_nested_counts_hold(
                self.n_inside,
                self.k_020,
                self.n_remaining_after_020,
                self.k_087,
                self.n_remaining,
            )
        )
        self.assertEqual(self.n_remaining, STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, 6)
        self.assertEqual(STANDING_N_REMAINING_AFTER_087, CYCLE293_N_REMAINING_AFTER_087)
        self.assertEqual(self.n_remaining, self.n_remaining_after_020 - self.k_087)
        self.assertEqual(9 - 3, 6)
        self.assertEqual(self.n_remaining, self.n_inside - self.k_020 - self.k_087)
        self.assertEqual(13 - 4 - 3, 6)
        if self.n_remaining != 6:
            self.fail("measured N_remaining_after_087 drifted from 6")
        if self.n_remaining != self.n_remaining_after_020 - self.k_087:
            self.fail("leftover n=4 remaining remaining-after-087 filter disagrees with nested 9−3")
        self.assertEqual(self.remaining, STANDING_REMAINING_SITES)
        self.assertEqual(self.remaining, CYCLE293_REMAINING_AFTER_087_SITES)
        self.assertEqual(self.remaining_stems, STANDING_REMAINING_NEXT_STEMS)
        self.assertEqual(len(self.remaining), len(self.remaining_stems))
        self.assertEqual(
            self.remaining,
            leftover_n4_remaining_remaining_after_020_without_forward_087(
                self.inside_sites,
                self.next_stems,
            ),
        )
        self.assertEqual(
            self.remaining_after_020,
            leftover_n4_remaining_without_forward_020(
                self.inside_sites,
                self.next_stems,
            ),
        )
        self.assertEqual(self.n_with_next, STANDING_N_WITH_NEXT)
        self.assertEqual(STANDING_N_WITH_NEXT, 6)
        self.assertEqual(self.n_no_next, STANDING_N_NO_NEXT)
        self.assertEqual(STANDING_N_NO_NEXT, 0)
        self.assertEqual(self.no_next, STANDING_NO_NEXT_SITES)
        self.assertEqual(STANDING_NO_NEXT_SITES, ())
        self.assertEqual(self.n_with_next + self.n_no_next, self.n_remaining)
        self.assertEqual(6 + 0, 6)
        for site in self.share_020:
            self.assertNotIn(site, self.remaining)
        for site in self.share_087:
            self.assertNotIn(site, self.remaining)
            self.assertIn(site, self.remaining_after_020)
        self.assertEqual(self.n_distinct, STANDING_N_DISTINCT)
        self.assertEqual(STANDING_N_DISTINCT, 4)
        self.assertEqual(self.frequency, STANDING_REMAINING_FREQUENCY)
        self.assertEqual(self.g, STANDING_G)
        self.assertEqual(STANDING_G, "057")
        self.assertEqual(self.k, STANDING_K)
        self.assertEqual(STANDING_K, 2)
        self.assertFalse(self.unique)
        self.assertFalse(STANDING_G_UNIQUELY_MOST_FREQUENT)
        self.assertEqual(self.frequency[0][0], "057")
        self.assertEqual(self.frequency[0][1], 2)
        self.assertEqual(self.frequency[1][0], "011")
        self.assertEqual(self.frequency[1][1], 2)
        self.assertEqual(self.frequency[0][1], self.frequency[1][1])
        tied = tuple(stem for stem, count, _sites, _grams in self.frequency if count == 2)
        self.assertEqual(tied, STANDING_TIED_STEMS)
        self.assertEqual(len(tied), STANDING_N_TIED_AT_K)
        self.assertEqual(STANDING_N_TIED_AT_K, 2)
        hapax = sum(1 for _stem, count, _sites, _grams in self.frequency if count == 1)
        self.assertEqual(hapax, STANDING_N_HAPAX)
        self.assertEqual(STANDING_N_HAPAX, 2)
        self.assertEqual(self.n_without, STANDING_N_WITHOUT_G)
        self.assertEqual(STANDING_N_WITHOUT_G, 4)
        self.assertEqual(self.k + self.n_without, self.n_remaining)
        self.assertEqual(2 + 4, 6)
        cycle292_remaining_after_087_inventory = tuple(
            (stem, count)
            for stem, count, _sites, _grams in CYCLE292_REMAINING_FREQUENCY
            if stem != "087"
        )
        self.assertEqual(
            cycle292_remaining_after_087_inventory,
            STANDING_CYCLE292_REMAINING_AFTER_087_INVENTORY,
        )
        self.assertEqual(
            set(cycle292_remaining_after_087_inventory),
            {(stem, count) for stem, count, _sites, _grams in self.frequency},
        )
        self.assertTrue(STANDING_CYCLE292_FREQUENCY_MINUS_087_IS_NESTED_INVENTORY)
        self.assertFalse(
            i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem(
                self.inside_sites,
                self.next_stems,
            )
        )
        self.assertEqual(
            self.claim_holds,
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_UNIQUE_NEXT_STEM,
        )
        self.assertFalse(
            STANDING_I_LEFTOVER_N4_REMAINING_090_076_REMAINING_AFTER_087_UNIQUE_NEXT_STEM
        )
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertNotEqual(GRAM2, CYCLE171_GRAM2)
        self.assertEqual(CYCLE171_GRAM2, ("076", "071"))
        self.assertFalse(is_contiguous_substring(GRAM2, EXCEPTION_GRAM))
        self.assertFalse(STANDING_SAME_AS_I_5GRAM)
        self.assertFalse(STANDING_SAME_AS_CYCLE234)
        self.assertFalse(STANDING_SAME_AS_CYCLE256)
        self.assertFalse(STANDING_SAME_AS_CYCLE270)
        self.assertFalse(STANDING_SAME_AS_CYCLE288)
        self.assertFalse(STANDING_SAME_AS_CYCLE289)
        self.assertFalse(STANDING_SAME_AS_CYCLE292)
        self.assertFalse(STANDING_SAME_AS_CYCLE293)
        self.assertFalse(STANDING_SAME_AS_CYCLE245)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE234)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE256)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE270)
        self.assertTrue(STANDING_SAME_CLAIM_SHAPE_AS_CYCLE292)
        self.assertTrue(STANDING_TABLET_ONLY)
        self.assertFalse(STANDING_N_GE_8_ISLAND)
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_087_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        self.assertTrue(STANDING_CYCLE292_FREQUENCY_MINUS_087_IS_NESTED_INVENTORY)
        self.assertTrue(STANDING_G_K_IS_INVENTORY_FOR_LATER_PEEL)
        self.assertFalse(CYCLE288_SHARE_ONE)
        self.assertTrue(CYCLE289_CLAIM)
        self.assertTrue(CYCLE292_CLAIM)
        self.assertTrue(CYCLE293_CLAIM)
        self.assertTrue(CYCLE245_CLAIM)
        self.assertFalse(CYCLE234_CLAIM)
        self.assertFalse(CYCLE256_CLAIM)
        self.assertFalse(CYCLE270_CLAIM)
        self.assertEqual(CYCLE256_N_REMAINING11, 19)
        self.assertEqual(CYCLE256_N_DISTINCT, 19)
        self.assertEqual(CYCLE256_G, "755")
        self.assertEqual(CYCLE256_K, 1)
        self.assertFalse(CYCLE256_UNIQUE)
        self.assertEqual(CYCLE270_G, "090")
        self.assertEqual(CYCLE270_K, 2)
        self.assertEqual(CYCLE270_N_TIED_AT_K, 5)
        self.assertFalse(CYCLE270_UNIQUE)
        self.assertEqual(CYCLE234_N_TIED_AT_K, 7)
        self.assertEqual(CYCLE234_K, 2)
        self.assertFalse(CYCLE234_UNIQUE)
        self.assertEqual(CYCLE292_G, "087")
        self.assertEqual(CYCLE292_K, 3)
        self.assertTrue(CYCLE292_UNIQUE)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_matching_leftover_n4_remaining_remaining_after_087_sites_share_057(self):
        """Two leftover n=4 remaining remaining-after-087 sites are 090 076 057 (tie inventory)."""
        self.assertEqual(self.matching, STANDING_MATCHING_SITES)
        self.assertEqual(self.matching_next_4grams, STANDING_MATCHING_NEXT_4GRAMS)
        expected = (
            ((SIDE_IA, "Ia8", 114), ("090", "076", "057", "600")),
            ((SIDE_IA, "Ia9", 28), ("090", "076", "057", "600")),
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
            self.assertEqual(stems[index + STANDING_N2], "057")
            self.assertEqual(site_next_stem(stems, index, GRAM2), "057")
            self.assertEqual(site_forward_3gram(stems, index, GRAM2), GRAM3_FORWARD)
            self.assertEqual(site_next_4gram(stems, index, GRAM2), want_nxt)
            self.assertEqual(nxt, want_nxt)
            self.assertEqual(site, want_site)
            self.assertEqual(nxt[:3], GRAM3_FORWARD)
            self.assertEqual(len(nxt), STANDING_N4)
            self.assertEqual(side, SIDE_IA)
            self.assertIn(site, STANDING_INSIDE_SITES)
            self.assertIn(site, STANDING_REMAINING_SITES)
            self.assertNotIn(site, STANDING_LEFTOVER_SITES)
            self.assertNotIn(site, CYCLE289_MATCHING_SITES)
            self.assertNotIn(site, CYCLE292_MATCHING_SITES)
            self.assertNotIn(site, CYCLE245_EXTRA_I_SITES)
        for site in self.without:
            stems = line_stems_for_site(self.i_sides, site)
            index = site[2]
            self.assertEqual(tuple(stems[index : index + STANDING_N2]), GRAM2)
            nxt = site_next_stem(stems, index, GRAM2)
            self.assertIsNotNone(nxt)
            self.assertNotEqual(nxt, "057")
            self.assertNotEqual(nxt, "087")
            self.assertNotEqual(nxt, "020")
            self.assertIn(site, STANDING_REMAINING_SITES)
        for site in self.share_020:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE289_MATCHING_SITES)
        for site in self.share_087:
            self.assertNotIn(site, self.remaining)
            self.assertNotIn(site, self.matching)
            self.assertIn(site, CYCLE292_MATCHING_SITES)
            self.assertIn(site, CYCLE245_EXTRA_I_SITES)
        for site in STANDING_LEFTOVER_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
        for site in STANDING_OFF_I_SITES:
            self.assertNotIn(site, STANDING_INSIDE_SITES)
            self.assertNotIn(site, self.remaining)
        local = leftover_local_4grams(self.i_sides, STANDING_MATCHING_SITES, GRAM2)
        for (_site, _prev, nxt4), want in zip(
            local,
            STANDING_MATCHING_NEXT_4GRAMS,
            strict=True,
        ):
            self.assertEqual(nxt4, want)
        self.assertEqual(IA_LINE_NAMES[7], "Ia8")
        self.assertEqual(IA_LINE_NAMES[8], "Ia9")
        self.assertTrue(STANDING_I_ONLY_OF_REMAINING_AFTER_087_3GRAM_IS_NOT_THIS_CYCLE)
        self.assertTrue(STANDING_DO_NOT_PEEL_A_SPECIFIC_REMAINING_STEM)
        leftover_extra_087 = tuple(
            site for site in CYCLE245_I_SITES if site not in CYCLE245_EXTRA_I_SITES
        )
        for site in leftover_extra_087:
            self.assertNotIn(site, self.remaining)
            self.assertIn(site, STANDING_LEFTOVER_SITES)
        self.assertEqual(self.provider.get_call_history(), [])

    def test_existing_293_292_289_288_245_224_223_still_compute(self):
        """Cycle 293 K_087=3 N=6 extra I overlap, 292 G=087 K=3, 289 K_020=4, 288 N_distinct=6 G=020 K=4, 245 5/0 extra I=3, 224 13/56, 223 69/3 stay."""
        leftover = leftover_n4_rows()
        self.assertTrue(leftover_n4_family_counts_hold(leftover))
        self.assertEqual(len(leftover_remaining_n4(leftover)), CYCLE222_N_REMAINING)
        self.assertEqual(len(leftover_remaining_n4(leftover)), 16)
        self.assertEqual(len(leftover_remaining_with_g(leftover_remaining_n4(leftover))), 5)
        self.assertEqual(CYCLE222_G, GRAM2)
        self.assertEqual(CYCLE222_K, 5)
        self.assertTrue(i_leftover_n4_remaining_exactly_5_contain_090_076(leftover))
        prior_293 = TestMamariILeftoverN4Remaining090076RemainingAfter020Forward087Scoreboard()
        prior_293.setUp()
        prior_293.test_counts_3_of_9_and_hypothesis_k_3_holds()
        prior_293.test_survey_matches_computed_lock()
        self.assertEqual(prior_293.k_087, 3)
        self.assertEqual(prior_293.n_remaining_after_087, 6)
        self.assertEqual(prior_293.matching, CYCLE293_MATCHING_SITES)
        self.assertEqual(self.share_087, prior_293.matching)
        self.assertEqual(self.remaining, prior_293.without)
        self.assertTrue(prior_293.equals_cycle245)
        self.assertTrue(prior_293.claim_holds)
        self.assertTrue(CYCLE293_CLAIM)
        if (
            prior_293.k_087 != 3
            or prior_293.n_remaining_after_087 != 6
            or not prior_293.equals_cycle245
        ):
            self.fail(
                "nested cycle 293 leftover n=4 remaining remaining-after-020 exactly 3 share 087 / N_remaining=6 drifted"
            )
        prior_292 = TestMamariILeftoverN4Remaining090076RemainingAfter020NextStemScoreboard()
        prior_292.setUp()
        prior_292.test_counts_9_remaining_g_087_k_3_and_hypothesis_holds()
        prior_292.test_survey_matches_computed_lock()
        self.assertEqual(prior_292.n_remaining, 9)
        self.assertEqual(prior_292.n_distinct, 5)
        self.assertEqual(prior_292.g, "087")
        self.assertEqual(prior_292.k, 3)
        self.assertTrue(prior_292.unique)
        self.assertTrue(prior_292.claim_holds)
        self.assertTrue(CYCLE292_CLAIM)
        if (
            prior_292.n_remaining != 9
            or prior_292.g != "087"
            or prior_292.k != 3
            or not prior_292.unique
        ):
            self.fail(
                "nested cycle 292 leftover n=4 remaining remaining-after-020 unique-max G=087 K=3 drifted"
            )
        prior_289 = TestMamariILeftoverN4Remaining090076Forward020Scoreboard()
        prior_289.setUp()
        prior_289.test_counts_4_of_13_and_hypothesis_k_4_holds()
        prior_289.test_survey_matches_computed_lock()
        self.assertEqual(prior_289.n_inside, 13)
        self.assertEqual(prior_289.k, 4)
        self.assertEqual(CYCLE289_G, "020")
        self.assertEqual(prior_289.n_remaining_after_020, 9)
        self.assertEqual(prior_289.matching, CYCLE289_MATCHING_SITES)
        self.assertEqual(self.share_020, prior_289.matching)
        self.assertTrue(prior_289.claim_holds)
        self.assertTrue(CYCLE289_CLAIM)
        if (
            prior_289.n_inside != 13
            or prior_289.k != 4
            or prior_289.n_remaining_after_020 != 9
        ):
            self.fail(
                "nested cycle 289 leftover n=4 remaining exactly 4 share 020 / N_remaining=9 drifted"
            )
        prior_288 = TestMamariILeftoverN4Remaining090076ForwardStemScoreboard()
        prior_288.setUp()
        prior_288.test_counts_6_distinct_next_stems_and_claim_loses()
        prior_288.test_survey_matches_computed_lock()
        self.assertEqual(prior_288.n_inside, 13)
        self.assertEqual(prior_288.n_with_next, 13)
        self.assertEqual(prior_288.n_no_next, 0)
        self.assertEqual(prior_288.n_distinct, 6)
        self.assertEqual(prior_288.g, "020")
        self.assertEqual(prior_288.k, 4)
        self.assertTrue(prior_288.unique_max)
        self.assertFalse(prior_288.claim_holds)
        self.assertFalse(CYCLE288_SHARE_ONE)
        if (
            prior_288.n_inside != 13
            or prior_288.n_with_next != 13
            or prior_288.n_distinct != 6
            or prior_288.g != "020"
            or prior_288.k != 4
            or not prior_288.unique_max
        ):
            self.fail(
                "nested cycle 288 leftover n=4 remaining 13/13/0 N_distinct=6 G=020 K=4 unique-max drifted"
            )
        prior_245 = TestMamariI3gram090076087IOnlyScoreboard()
        prior_245.setUp()
        prior_245.test_3gram_is_zero_off_i_and_i_only()
        prior_245.test_survey_matches_computed_lock()
        self.assertEqual(prior_245.i_hits, CYCLE245_N_I)
        self.assertEqual(prior_245.i_hits, 5)
        self.assertEqual(prior_245.off_i_hits, CYCLE245_N_OFF_I)
        self.assertEqual(prior_245.off_i_hits, 0)
        self.assertEqual(len(prior_245.extra), CYCLE245_N_EXTRA)
        self.assertEqual(len(prior_245.extra), 3)
        self.assertEqual(prior_245.extra, CYCLE245_EXTRA_I_SITES)
        self.assertEqual(self.share_087, prior_245.extra)
        self.assertTrue(prior_245.claim_holds)
        self.assertTrue(CYCLE245_CLAIM)
        if prior_245.i_hits != 5 or prior_245.off_i_hits != 0 or len(prior_245.extra) != 3:
            self.fail("nested cycle 245 090 076 087 I-only 5/0 extra I=3 drifted")
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
        prior_103 = TestMamariSantiagoIaIOnlyScoreboard()
        prior_103.setUp()
        prior_103.test_5gram_is_zero_off_i_and_i_only()
        prior_w = TestMamariHonolulu4UnpublishedScoreboard()
        prior_w.setUp()
        prior_w.test_survey_matches_computed_lock()
        self.assertEqual(self.provider.get_call_history(), [])

    def test_survey_matches_computed_lock(self):
        """CORPUS_SURVEY.json records the cycle-294 leftover n=4 remaining remaining-after-087 lock."""
        lock = self.survey["i_leftover_n4_remaining_090_076_remaining_after_087_next_stem"]
        self.assertEqual(lock["cycle"], 294)
        self.assertEqual(lock["result"], STANDING_RESULT)
        self.assertEqual(tuple(lock["tokens2"]), GRAM2)
        self.assertEqual(lock["n2"], STANDING_N2)
        self.assertEqual(tuple(lock["forward_3gram"]), GRAM3_FORWARD)
        self.assertEqual(tuple(lock["forward_3gram"]), ("090", "076", "057"))
        self.assertEqual(lock["n3"], STANDING_N3)
        self.assertEqual(lock["n4"], STANDING_N4)
        self.assertEqual(tuple(lock["locked_forward_stems"]), LOCKED_FORWARD_STEMS)
        self.assertEqual(tuple(lock["locked_forward_stems"]), ("020", "087"))
        self.assertEqual(lock["N_I"], STANDING_N_I)
        self.assertEqual(lock["N_I"], 69)
        self.assertEqual(lock["N_inside"], STANDING_N_INSIDE)
        self.assertEqual(lock["N_inside"], 13)
        self.assertEqual(lock["N_leftover_extra"], STANDING_N_LEFTOVER_EXTRA)
        self.assertEqual(lock["N_leftover_extra"], 56)
        self.assertEqual(
            tuple(tuple(row) for row in lock["inside_sites"]),
            STANDING_INSIDE_SITES,
        )
        self.assertEqual(lock["N_with_next_inside"], STANDING_N_WITH_NEXT_INSIDE)
        self.assertEqual(lock["N_with_next_inside"], 13)
        self.assertEqual(lock["N_no_next_inside"], STANDING_N_NO_NEXT_INSIDE)
        self.assertEqual(lock["N_no_next_inside"], 0)
        self.assertEqual(lock["K_020"], STANDING_K_020)
        self.assertEqual(lock["K_020"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_020_sites"]),
            CYCLE289_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_020"], STANDING_N_REMAINING_AFTER_020)
        self.assertEqual(lock["N_remaining_after_020"], 9)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_020_sites"]),
            CYCLE292_REMAINING_SITES,
        )
        self.assertEqual(lock["K_087"], STANDING_K_087)
        self.assertEqual(lock["K_087"], 3)
        self.assertEqual(
            tuple(tuple(row) for row in lock["share_087_sites"]),
            CYCLE293_MATCHING_SITES,
        )
        self.assertEqual(lock["N_remaining_after_087"], STANDING_N_REMAINING_AFTER_087)
        self.assertEqual(lock["N_remaining_after_087"], 6)
        self.assertEqual(
            tuple(tuple(row) for row in lock["remaining_after_087_sites"]),
            STANDING_REMAINING_SITES,
        )
        self.assertEqual(
            tuple(lock["remaining_after_087_next_stems"]),
            STANDING_REMAINING_NEXT_STEMS,
        )
        self.assertEqual(lock["N_with_next"], STANDING_N_WITH_NEXT)
        self.assertEqual(lock["N_with_next"], 6)
        self.assertEqual(lock["N_no_next"], STANDING_N_NO_NEXT)
        self.assertEqual(lock["N_no_next"], 0)
        self.assertEqual(
            tuple(tuple(row) for row in lock["no_next_sites"]),
            STANDING_NO_NEXT_SITES,
        )
        self.assertEqual(lock["N_distinct"], STANDING_N_DISTINCT)
        self.assertEqual(lock["N_distinct"], 4)
        self.assertEqual(lock["N_hapax"], STANDING_N_HAPAX)
        self.assertEqual(lock["N_hapax"], 2)
        self.assertEqual(lock["G"], STANDING_G)
        self.assertEqual(lock["G"], "057")
        self.assertEqual(lock["K"], STANDING_K)
        self.assertEqual(lock["K"], 2)
        self.assertFalse(lock["G_uniquely_most_frequent"])
        self.assertEqual(tuple(lock["tied_stems_at_K"]), STANDING_TIED_STEMS)
        self.assertEqual(lock["N_tied_at_K"], STANDING_N_TIED_AT_K)
        self.assertEqual(lock["N_tied_at_K"], 2)
        self.assertEqual(lock["N_without_G"], STANDING_N_WITHOUT_G)
        self.assertEqual(lock["N_without_G"], 4)
        self.assertEqual(
            tuple(tuple(row) for row in lock["matching_leftover_n4_remaining_remaining_after_087_sites"]),
            STANDING_MATCHING_SITES,
        )
        self.assertEqual(
            [list(gram) for gram in STANDING_MATCHING_NEXT_4GRAMS],
            lock["matching_next_4grams"],
        )
        self.assertEqual(
            lock["matching_leftover_n4_remaining_remaining_after_087_local_4grams"],
            matching_leftover_n4_remaining_remaining_after_087_local_4gram_rows(),
        )
        self.assertEqual(
            lock["remaining_after_087_next_stem_frequency"],
            remaining_after_087_next_stem_frequency_rows(),
        )
        self.assertEqual(
            [list(pair) for pair in STANDING_CYCLE292_REMAINING_AFTER_087_INVENTORY],
            lock["cycle292_remaining_after_087_inventory"],
        )
        self.assertEqual(lock["cycle293_K_087"], 3)
        self.assertEqual(lock["cycle293_N_remaining_after_087"], 6)
        self.assertTrue(lock["cycle293_extra_i_overlap"])
        self.assertEqual(lock["cycle292_G"], "087")
        self.assertEqual(lock["cycle292_K"], 3)
        self.assertEqual(lock["cycle292_N_remaining_after_020"], 9)
        self.assertEqual(lock["cycle292_N_distinct"], 5)
        self.assertTrue(lock["cycle292_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle289_G"], "020")
        self.assertEqual(lock["cycle289_K"], 4)
        self.assertEqual(lock["cycle289_N_remaining_after_020"], 9)
        self.assertEqual(lock["cycle288_N_inside"], 13)
        self.assertEqual(lock["cycle288_N_with_next"], 13)
        self.assertEqual(lock["cycle288_N_distinct"], 6)
        self.assertEqual(lock["cycle288_G"], "020")
        self.assertEqual(lock["cycle288_K"], 4)
        self.assertTrue(lock["cycle288_g_uniquely_most_frequent"])
        self.assertEqual(lock["cycle245_N_I"], 5)
        self.assertEqual(lock["cycle245_N_off_I"], 0)
        self.assertEqual(lock["cycle245_N_extra"], 3)
        self.assertEqual(lock["cycle224_N_inside"], 13)
        self.assertEqual(lock["cycle224_N_leftover"], 56)
        self.assertEqual(lock["cycle223_N_I"], 69)
        self.assertEqual(lock["cycle223_N_off_I"], 3)
        self.assertEqual(lock["cycle256_N_remaining11"], 19)
        self.assertEqual(lock["cycle256_G"], "755")
        self.assertEqual(lock["cycle256_K"], 1)
        self.assertFalse(lock["cycle256_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle270_G"], "090")
        self.assertEqual(lock["cycle270_K"], 2)
        self.assertEqual(lock["cycle270_N_tied_at_K"], 5)
        self.assertFalse(lock["cycle270_G_uniquely_most_frequent"])
        self.assertEqual(lock["cycle234_N_tied_at_K"], 7)
        self.assertFalse(lock["cycle234_G_uniquely_most_frequent"])
        self.assertTrue(lock["known_distinct"])
        self.assertEqual(lock["claim"], STANDING_CLAIM)
        self.assertFalse(lock["i_leftover_n4_remaining_090_076_remaining_after_087_unique_next_stem"])
        self.assertTrue(lock["tablet_only"])
        self.assertFalse(lock["n_ge_8_island"])
        self.assertFalse(lock["w_barthel"])
        self.assertFalse(lock["new_tablet"])
        self.assertFalse(lock["same_as_i_5gram"])
        self.assertFalse(lock["same_as_cycle234"])
        self.assertFalse(lock["same_as_cycle256"])
        self.assertFalse(lock["same_as_cycle270"])
        self.assertFalse(lock["same_as_cycle288"])
        self.assertFalse(lock["same_as_cycle289"])
        self.assertFalse(lock["same_as_cycle292"])
        self.assertFalse(lock["same_as_cycle293"])
        self.assertFalse(lock["same_as_cycle245"])
        self.assertTrue(lock["same_claim_shape_as_cycle234"])
        self.assertTrue(lock["same_claim_shape_as_cycle256"])
        self.assertTrue(lock["same_claim_shape_as_cycle270"])
        self.assertTrue(lock["same_claim_shape_as_cycle292"])
        self.assertTrue(lock["off_i_t_sites_are_not_this_cycle"])
        self.assertTrue(lock["i_only_of_remaining_after_087_3gram_is_not_this_cycle"])
        self.assertTrue(lock["do_not_peel_a_specific_remaining_stem"])
        self.assertTrue(lock["cycle292_frequency_minus_087_is_nested_inventory"])
        self.assertTrue(lock["cycle245_extra_i_equals_remaining_after_020_087"])
        self.assertTrue(lock["076_071_does_not_count"])
        self.assertTrue(lock["076_070_does_not_count"])
        self.assertTrue(lock["leftover_extra_does_not_count"])
        self.assertTrue(lock["leftover_n4_set_not_retuned"])
        self.assertTrue(lock["leftover_extra_peels_not_retuned"])
        self.assertTrue(lock["cycle167_268_293_not_overwritten"])
        self.assertTrue(lock["g_k_is_inventory_for_later_peel"])
        self.assertTrue(lock["raw_stems_999_kept"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_020_forward_087_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_remaining_after_020_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_020_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_090_076_forward_stem_unchanged"])
        self.assertTrue(lock["standing_i_3gram_090_076_087_i_only_unchanged"])
        self.assertTrue(lock["standing_i_090_076_inside_leftover_n4_remaining_family_unchanged"])
        self.assertTrue(lock["standing_i_2gram_090_076_i_only_unchanged"])
        self.assertTrue(lock["standing_i_leftover_n4_remaining_next_2gram_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_000_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_600_previous_stem_unchanged"])
        self.assertTrue(lock["standing_i_leftover_extra_090_076_remaining_after_001_next_stem_unchanged"])
        self.assertTrue(lock["standing_i_santiago_ia_i_only_unchanged"])
        self.assertTrue(lock["standing_i_santiago_staff_unchanged"])
        self.assertTrue(lock["standing_n_repeating_nge5_unchanged"])
        self.assertTrue(lock["standing_s_repeating_nge6_unchanged"])
        self.assertTrue(lock["standing_corpus_longest_n_inventory_unchanged"])
        self.assertTrue(lock["standing_corpus_max_n_leak_table_unchanged"])
        self.assertTrue(lock["standing_w_honolulu_unpublished_unchanged"])
        self.assertEqual(lock["image_track"], "parked")
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"]["cycle"],
            293,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"][
                "i_leftover_n4_remaining_090_076_remaining_after_020_exactly_3_share_forward_087"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"]["K_087"],
            3,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_forward_087"][
                "N_remaining_after_087"
            ],
            6,
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]["cycle"],
            292,
        )
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"][
                "i_leftover_n4_remaining_090_076_remaining_after_020_unique_next_stem"
            ]
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]["G"],
            "087",
        )
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_remaining_after_020_next_stem"]["K"],
            3,
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_020"]["cycle"], 289)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_forward_020"][
                "i_leftover_n4_remaining_090_076_exactly_4_share_forward_020"
            ]
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_020"]["K"], 4)
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["cycle"], 288)
        self.assertEqual(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["N_distinct_next_stems"],
            6,
        )
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["G"], "020")
        self.assertEqual(self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["K"], 4)
        self.assertTrue(
            self.survey["i_leftover_n4_remaining_090_076_forward_stem"]["g_uniquely_most_frequent"]
        )
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["cycle"], 245)
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["N_I"], 5)
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["N_off_I"], 0)
        self.assertEqual(self.survey["i_3gram_090_076_087_i_only"]["N_extra"], 3)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["cycle"], 224)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_inside"], 13)
        self.assertEqual(self.survey["i_090_076_inside_leftover_n4_remaining_family"]["N_leftover"], 56)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["cycle"], 223)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_I"], 69)
        self.assertEqual(self.survey["i_2gram_090_076_i_only"]["N_off_I"], 3)
        self.assertEqual(self.survey["tablet_i_santiago_ia_i_only"]["cycle"], 103)
        self.assertTrue(self.survey["tablet_i_santiago_ia_i_only"]["i_only"])
        self.assertEqual(
            tuple(self.survey["tablet_i_santiago_ia_i_only"]["tokens5"]),
            GRAM5,
        )
        self.assertEqual(self.survey["tablet_w_honolulu_unpublished"]["cycle"], 100)
        self.assertFalse(self.survey["tablet_w_honolulu_unpublished"]["w_barthel"])
        self.assertFalse(STANDING_NEW_TABLET)
        self.assertEqual(self.provider.get_call_history(), [])


class TestMamariILeftoverN4Remaining090076RemainingAfter087NextStemImageSnapshot(
    unittest.TestCase
):
    """Cycle 294 does not touch clustering. 83/62 / Hamming 6 stays."""

    def test_image_snapshot_unchanged(self):
        """Text lock does not merge types. Parked image track stays 83/62 / 6."""
        image = load_corpus_survey()["standing_image_lock"]
        self.assertEqual(image["instances"], 83)
        self.assertEqual(image["types"], 62)
        self.assertEqual(image["published_min_hamming"], 6)


if __name__ == "__main__":
    unittest.main()
