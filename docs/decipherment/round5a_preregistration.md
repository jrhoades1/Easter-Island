# Round 5, Track A — pre-registration

This file is the plan. It was committed before the held-out counts were computed. The code that follows has to implement this page. It does not retune it.

Round 4 Track A (PR #1072) is left as it was. The word list R1 and the icon classes stay frozen. Nothing in this round is a translation. The provider is MockProvider and is never called.

## What is being asked again

Round 4 reported three pictograph results:

- Signs of one class sit two places apart more often than a line shuffle (394 pairs, 0 of 500, add-one p 0.002).
- In parallel passages, cross-hundred substitutions share a class more often than a label shuffle (18 of 34, add-one p 0.048). All 18 were birds (series 400–409 with series 600–699).
- Rebus map R1 scored 44 hits against a shuffle mean of 19.3 (add-one p 0.010). Hits that mix two different words scored 15 (add-one p 0.032). Most of the 44 were the same word twice.

This round asks whether those three results still appear on tablets that do not share a parallel passage with the tablets where the parallel and calendar counts were concentrated. R1 is not refit. Classes are not refit.

## Frozen inputs

R1, copied from `decipherment/round4_tracka.py` and not edited:

| Sign | Word | Label in Round 4 |
| --- | --- | --- |
| `040` | marama | HYPOTHESIS |
| `143` | rakau | HYPOTHESIS |
| `152` | omotohi | HYPOTHESIS |
| `200` | tangata | published_hypothesis |
| `600` | manu | HYPOTHESIS |
| `680` | makohe | HYPOTHESIS |
| `700` | ika | HYPOTHESIS |
| `006` | rima | HYPOTHESIS |

`064` copies the word assigned to `006`. It is not its own slot in a word shuffle or a noun map. That alias is Pozdniakov's hand pair, already fixed in Round 4.

Classes are `class_of` in that same module. The six testable classes remain moon, hand, bird, sea, human, and human_gaping. `042` is not a moon. `760` is not a fish. Series 410–599 stay unclassified. A hit still uses Round 4's rule: the mapped syllables are one word in the vendored lists, or the words occur in that order in the primary running text. Windows are still length 2, 3, or 4. An unmapped sign still breaks the window. Windows still do not cross a line.

## How the tablets are split

Sources, already stored:

- Significant stem passages in `data/decipherment/substitution_classes.json` (Round 2 Track C, PR #1066).
- The copying tree in `data/decipherment/round4d_dating_stemma.json` (Round 4 Track D, PR #1073). A pair is on that tree only when it has at least 40 aligned columns. The trees are G–K and H–P–Q.

Rule, applied by the code, not by hand:

1. Draw an edge between two tablets when a significant stem passage joins them.
2. The discovery set is the connected component with the most such passages. A tie would go to the component whose sorted letters come first. The published counts are H–P 32, H–Q 18, P–Q 19, and G–K 6, and no other pair. That rule therefore selects H, P, and Q.
3. The held-out set is every other tablet in `load_lines()`. G and K are held out. So is Mamari (C), the calendar tablet. So is every tablet that shares no significant passage with anybody.

The code recomputes the components and stops without a p-value if discovery is not exactly H, P, Q, or if any significant passage has one tablet in discovery and the other held out, or if a stemma pair (G–K, H–P, H–Q, P–Q) is split across the two sets.

G and K are both held out, and they copy each other. Scoring both full texts would count that copy twice. For the rebus test and the two-apart test, G is kept whole (it comes first in the alphabet) and the stems on K that sit inside a significant G–K passage are removed. A removal splits the line, so a window cannot jump the gap. The bird-substitution test is the exception: it needs both copies, so it still aligns G with K.

Round 4 already counted every tablet, including these held-out lines, in the corpus-wide two-apart shuffle, and it counted G–K inside the 99 passages. R1 and the classes were fixed from the citations before those scores. This round does not change them. The held-out numbers are a second look at text that is not a copy of H, P, or Q. They are not a sample Round 4 never saw. The Holm correction below is what keeps that second look from getting a fresh 5% gate.

## Tests on the held-out text only

Three tests. 500 draws each. One-sided: the null has to reach the observed count or more.

### (a) Mixed-word rebus hits

Scored on the held-out lines after the K-copy removal.

A window counts only when all three of these are true:

- It is a Round 4 mapped window of length 2, 3, or 4.
- It is not a pure sign repeat. The signs in the window are not all the same sign.
- It is not a doubled word. No word occurs more than once in the window. `tangata tangata` is out. `rima rima` from `006` plus `064` is out. A window that mixes words and also repeats one of them is out.

A hit is a window that survives those exclusions and matches Round 4's word-or-phrase rule. The statistic is the number of hits.

Two nulls:

1. Sign shuffle within each line, preserving repeats. A repeat is a maximal run of the same sign. The run moves as one block. Separated copies of the same sign are not glued together. Seed 50.
2. Random word maps of the same size, drawn from the noun pool below. The signs stay where they are. Seed 51.

The rebus subclaim survives only if both nulls survive Holm.

### (b) Same-class signs two apart

On the same held-out lines. Count positions i and i+2 when the two signs differ, both fall in the same testable class, and the class is one of the six. Sum the six classes. That sum is the statistic. Per-class counts are printed and are not extra tests. Seed 52. The null is the same block shuffle as in (a), with this seed, not seed 50.

### (c) Bird-class substitutions, where the held-out text has them

Use significant passages whose two tablets are both held out. Under the split above, that is G–K only. Align each pair again with the same Smith-Waterman scorer Round 4 used, on the same slices (`start` through `end` inclusive).

The statistic is Round 4's cross-hundred count: both signs classified, hundreds digits different, classes equal.

If that alignment yields no cross-hundred classified pair, test (c) is not available. It is left out of Holm. It is not given a p-value of 1.

If it is available, two nulls:

1. Permute class labels on the classified stems that occur in those mismatch columns. Seed 53. Same procedure as Round 4, new seed, held-out pairs only.
2. Block-shuffle signs inside each passage slice, each side on its own, then align again and recompute the count. Seed 54.

A word map does not apply to (b) or (c). Those tests do not use words.

## Noun pool for null (a2)

Churchill 1912's vendored file is headwords only. It does not mark nouns. The pool is a proxy, labeled as such.

A candidate is a Churchill headword that `cv_syllables_mapped` accepts, minus this closed list:

- Particles already listed in `decipherment/old_rapanui.py`: a, e, i, o, u, te, ki, ka, ko, ku, ma, mo, me, no, na, ni, ra, re, ri, ro, ru, he, hai, atu, mai, ana, ai.
- Pronouns in the pronoun table of the vendored English Wikipedia article "Rapa Nui language" (`tests/fixtures/wikipedia_rapa_nui.html`): au, maua, matou, taua, tatou, koe, korua, ia, raua.
- hoki and ina, named as a question particle and the negator in that same article.

Label: HYPOTHESIS that dropping those closed-class words is enough to stand in for "nouns." Verbs that Churchill lists stay in the pool. A larger pool makes a random map more able to score well, so it is harder for R1 to survive, not easier. The eight R1 words stay eligible when they match a slot. The pool is not a gloss-checked noun list, because the glosses were not vendored.

Frequency is the primary-running-text count Round 4 already uses (mapped syllables joined, so `tagata` and `tangata` share a count). Length is the number of those syllables.

Bins, fixed:

| Bin | Running-text count |
| --- | --- |
| 0 | 0 |
| 1 | 1 to 20 |
| 2 | 21 to 100 |
| 3 | 101 to 300 |
| 4 | 301 and above |

Each R1 sign draws from headwords with the same syllable length and the same bin as its frozen word. If that set has fewer than 8 words, add the next bin downward, then the next bin upward, and repeat outward until the set has 8 words or the bins run out. The code records the bins it actually used. That expansion is part of this plan. It is not a change to R1.

Signs are filled in this order: `006`, `040`, `143`, `152`, `200`, `600`, `680`, `700`. A trial draws without replacement across the eight signs. If a sign's remaining pool is empty, it draws from its full pool and the trial is flagged. One `random.Random` stream per null, not reseeded inside the loop.

## Holm correction

The family is the Round 4 pictograph tests below, plus every Round 5 test that this plan says is available. P-values are add-one: `(null_ge + 1) / (trials + 1)`. Round 4 values are read from `data/decipherment/round4a_pictograph_rebus.json`. They are not recomputed. Round 5 uses the same formula.

Holm (1979), alpha 0.05. Sort by p-value, then by the id string. For the test in position i (starting at 1) in a family of m, the step value is `(m - i + 1) * p`. The adjusted p is the running maximum of those step values, capped at 1. A test survives when its adjusted p is at or under 0.05.

Round 4 members, and why each is in:

| Id | What it is |
| --- | --- |
| `r4_neighbor_sum` | Adjacent same-class sum. The neighbor gate. |
| `r4_neighbor_moon` | That gate, moon only. |
| `r4_neighbor_hand` | Hand. |
| `r4_neighbor_bird` | Bird. |
| `r4_neighbor_sea` | Sea. |
| `r4_neighbor_human` | Human. |
| `r4_neighbor_human_gaping` | Gaping-mouth human. |
| `r4_two_apart_sum` | Two-apart sum. The secondary result this round retests. |
| `r4_calendar_neighbor_sum` | Neighbor sum after the Mamari calendar stems are removed. |
| `r4_calendar_two_apart_sum` | Two-apart sum on that same reduced text. |
| `r4_cross_hundred` | Cross-hundred same-class substitutions. The parallel gate. |
| `r4_r1_hits` | R1 hits. |
| `r4_r1_diverse` | R1 hits that mix words. |
| `r4_r1_calendar` | R1, calendar context. |
| `r4_r1_gv6` | R1, Gv6. |
| `r4_r1_parallels` | R1, parallel context. |
| `r4_r2_hits` | Sensitivity map R2, total hits. |
| `r4_r2_diverse` | R2, mixed words. |
| `r4_r2_calendar` | R2, calendar context. |
| `r4_r2_gv6` | R2, Gv6. |
| `r4_r2_parallels` | R2, parallel context. |

Left out on purpose. Per-class two-apart rows are a breakdown of `r4_two_apart_sum` on the same 500 draws, and Round 4 said the class gate applied to neighbors, not to that distance. The within-hundred substitution rate was marked "not the semantic gate" and its hold flag was fixed false. Per-class rows of the calendar-removed neighbor count repeat the six class gates on a control. Putting those in would count one shuffle several times. They stay in the Round 4 report and out of this family.

Round 5 members, when available:

| Id | Test |
| --- | --- |
| `r5_rebus_sign_shuffle` | (a) against the block shuffle |
| `r5_rebus_noun_map` | (a) against the noun maps |
| `r5_two_apart_sign_shuffle` | (b) |
| `r5_bird_label_shuffle` | (c) label permutation, only if available |
| `r5_bird_sign_shuffle` | (c) slice shuffle, only if available |

The smallest add-one p-value 500 draws can produce is 1/501, about 0.0020. Holm's first cutoff is 0.05/m. If m is 26 or more, that floor sits above the cutoff, and no test in the family can survive, including a held-out count that beats every draw. This plan does not shorten the list to avoid that. It does not rerun Round 4 with more draws.

## Effect sizes

For every Round 5 null, report the observed count, the null mean, the null standard deviation (the square root of the mean squared deviation from that mean, dividing by the number of draws), and the effect `(observed - mean) / sd` when the sd is above zero. Also report the hit rate and the null mean rate when the test has windows.

## Survives or dies

Adjusted p-values decide. Unadjusted p-values are printed beside them and do not override them.

- The rebus survives when both `r5_rebus_sign_shuffle` and `r5_rebus_noun_map` have adjusted p at or under 0.05.
- Two-apart survives when `r5_two_apart_sign_shuffle` does.
- Bird substitutions survive when both bird tests are available and both have adjusted p at or under 0.05. If they are not available, that subclaim is "not tested." It is not a pass and not a fail.

The package survives only when the rebus survives and two-apart survives and the bird subclaim either survives or was not tested. Otherwise the package dies. A pass is not a reading. `reading` in the output is null.

## Seeds and constants

| Constant | Value |
| --- | --- |
| Draws per null | 500 |
| Sign-shuffle seed for the rebus | 50 |
| Noun-map seed | 51 |
| Two-apart seed | 52 |
| Bird label-shuffle seed | 53 |
| Bird slice-shuffle seed | 54 |
| Alpha | 0.05 |
| Minimum noun-pool size before a bin expands | 8 |

## What the run will write

`data/decipherment/round5a_heldout_pictograph.json` and `docs/decipherment/round5a_heldout_pictograph.md`. The markdown is plain English. The first paragraph says whether the package survives or dies, then the three counts, the null means, the effect sizes, and the Holm-adjusted p-values.
