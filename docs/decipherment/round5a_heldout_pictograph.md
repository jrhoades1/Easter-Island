# Round 5, Track A — held-out check of the pictograph results

The pictograph package **dies**. On the held-out tablets (D, F, I, J, L, M, N, O, S, T, U, V, W), mixed-word rebus hits are 6 on 36 eligible windows (sign-shuffle mean 18.356, effect -3.063, 500 of 500, add-one p 1.0000, Holm p 1.0000; noun-map mean 5.224, effect 0.150, 152 of 500, add-one p 0.3054, Holm p 1.0000). Same-class signs two apart are 65 (shuffle mean 59.096, effect 0.823, 110 of 500, add-one p 0.2216, Holm p 1.0000). Bird-class substitutions were not tested: no significant passage has both tablets in the held-out set. The Holm family has 24 tests. Nothing here is a translation of a tablet.

Provider: `mock`. Provider calls: 0. Reading: none.

Rebus dies. Two-apart dies. Bird substitutions: not tested.

## What was locked

The plan is `docs/decipherment/round5a_preregistration.md`. It was committed before these counts. R1 stays marama, rakau, omotohi, tangata, manu, makohe, ika, and rima, with `064` copying `006`. The six classes stay the Round 4 classes. No word was added. HYPOTHESIS: Churchill 1912 headwords that parse as (C)V, minus the closed particle and pronoun list in the pre-registration. The vocabulary file does not mark nouns. One headword is kept per mapped pronunciation, the first in alphabetical order.

Round 4 had already counted these held-out lines inside the corpus-wide shuffles. This is a second look at texts that share no significant passage with the discovery tablets. Holm is applied to the Round 4 pictograph tests and these Round 5 tests together so the second look does not get its own 5% gate. The two Round 4 two-apart rows can still clear Holm, because those counts were taken on the whole corpus. The package rule asks whether the held-out tests clear it. They are the ones that decide survives or dies.

## The split

Discovery, not scored: A, B, C, E, G, H, K, P, Q, R. Held-out: D, F, I, J, L, M, N, O, S, T, U, V, W. Held-out lines after the copy removal: 88. Held-out stems: 4088. Stems removed because they are the later copy of a held-out parallel: 0. The copying tree used as a check is `(G:0.089888,K:0.089888); (P:0.049072,(H:0.091764,Q:0.086139)0.663:0.049072);`.

## Mixed-word rebus

Mapped windows: 58. Pure sign repeats left out: 18. Doubled-word windows left out: 4. Eligible windows: 36. Hits: 6. Hit rate: 0.167.

The sign shuffle keeps adjacent repeats as blocks and moves those blocks inside the line. Mean hits 18.356 (sd 4.034). Effect -3.063. Draws at or above the observed count: 500 of 500. Mean eligible windows under that shuffle: 39.288. Mean hit rate: 0.468.

The noun-map null keeps the signs and replaces the eight words with content words of the same syllable length and the same running-text bin, widening the bin only when a slot has fewer than 8 words. Catalog size: 2023. Trials that had to reuse a word because a remaining pool was empty: 0. Mean hits 5.224 (sd 5.189). Effect 0.150. Draws at or above the observed count: 152 of 500. Mean hit rate: 0.145.

| Sign | R1 word | Syllables | Target bin | Bins used | Pool | Expanded |
| --- | --- | ---: | ---: | --- | ---: | --- |
| `006` | rima | 2 | 3 | 3 | 11 | no |
| `040` | marama | 3 | 2 | 1, 2, 3 | 69 | yes |
| `143` | rakau | 3 | 1 | 1 | 63 | no |
| `152` | omotohi | 4 | 0 | 0 | 609 | no |
| `200` | tangata | 3 | 4 | 2, 3, 4 | 8 | yes |
| `600` | manu | 2 | 3 | 3 | 11 | no |
| `680` | makohe | 3 | 0 | 0 | 508 | no |
| `700` | ika | 2 | 2 | 2 | 39 | no |

Hit windows, R1, after the exclusions: ika manu ×2, rima tangata ×1, tangata ika ×1, tangata manu ×1, ika tangata ×1.

## Two apart

Observed pairs: 65. Shuffle mean 59.096 (sd 7.173). Effect 0.823. Draws at or above the observed count: 110 of 500. The class rows are a breakdown of that one count. They are not extra Holm tests.

| Class | Pairs |
| --- | ---: |
| moon | 0 |
| hand | 7 |
| bird | 21 |
| sea | 5 |
| human | 26 |
| human_gaping | 6 |

## Cross-hundred substitutions

Held-out passages aligned: 0. Classified mismatches: 0. Same class, including pairs inside one hundred: 0. Cross-hundred classified pairs: 0. Cross-hundred same class: 0. By class: none.

Bird-class substitutions were not tested: no significant passage has both tablets in the held-out set.

## Holm

Alpha 0.05. Adjusted p is the running maximum of ``(tests left) × p``, in the order fixed by the plan. A row survives when that adjusted p is at or under 0.05. 500 draws cannot produce an add-one p smaller than 1/501. Holm's first cutoff is 0.05 divided by the family size. A family of 26 or more cannot pass any test at that floor.

| Test | Round | Add-one p | Rank | Holm p | Survives |
| --- | ---: | ---: | ---: | ---: | --- |
| `r4_calendar_two_apart_sum` | 4 | 0.0020 | 1 | 0.0479 | yes |
| `r4_two_apart_sum` | 4 | 0.0020 | 2 | 0.0479 | yes |
| `r4_r1_hits` | 4 | 0.0100 | 3 | 0.2196 | no |
| `r4_r2_parallels` | 4 | 0.0120 | 4 | 0.2515 | no |
| `r4_r2_hits` | 4 | 0.0140 | 5 | 0.2794 | no |
| `r4_r1_parallels` | 4 | 0.0180 | 6 | 0.3413 | no |
| `r4_neighbor_hand` | 4 | 0.0220 | 7 | 0.3952 | no |
| `r4_r1_diverse` | 4 | 0.0319 | 8 | 0.5429 | no |
| `r4_r2_diverse` | 4 | 0.0379 | 9 | 0.6068 | no |
| `r4_cross_hundred` | 4 | 0.0479 | 10 | 0.7186 | no |
| `r4_neighbor_bird` | 4 | 0.0699 | 11 | 0.9780 | no |
| `r5_two_apart_sign_shuffle` | 5 | 0.2216 | 12 | 1.0000 | no |
| `r5_rebus_noun_map` | 5 | 0.3054 | 13 | 1.0000 | no |
| `r4_r1_calendar` | 4 | 0.4691 | 14 | 1.0000 | no |
| `r4_r2_calendar` | 4 | 0.5609 | 15 | 1.0000 | no |
| `r4_calendar_neighbor_sum` | 4 | 0.6248 | 16 | 1.0000 | no |
| `r4_neighbor_sum` | 4 | 0.7784 | 17 | 1.0000 | no |
| `r4_neighbor_human` | 4 | 0.8802 | 18 | 1.0000 | no |
| `r4_neighbor_sea` | 4 | 0.9401 | 19 | 1.0000 | no |
| `r4_neighbor_human_gaping` | 4 | 0.9641 | 20 | 1.0000 | no |
| `r4_neighbor_moon` | 4 | 0.9741 | 21 | 1.0000 | no |
| `r4_r1_gv6` | 4 | 1.0000 | 22 | 1.0000 | no |
| `r4_r2_gv6` | 4 | 1.0000 | 23 | 1.0000 | no |
| `r5_rebus_sign_shuffle` | 5 | 1.0000 | 24 | 1.0000 | no |

## What this does not claim

No tablet is translated. R1 is still a list of cited pictures plus hypotheses, not a decipherment. A neighbor pattern inside Barthel's own series is not an independent identification of a bird or a fish. The noun pool is not a parsed dictionary of nouns. Surviving Holm would still not be a reading, and this run's reading field is empty.
