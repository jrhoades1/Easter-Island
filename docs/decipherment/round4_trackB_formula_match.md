# Round 4, Track B — Sign units against Rapanui formulas

**Verdict: the formulas do not match. A short-gap resemblance does, and it is not a reading.**

The formula profiles do not match. No sign-unit family is closer to a Rapanui formula family, or to the words, than both shuffles allow, and the Zipf slopes stay outside the pre-registered gap. Gv6's genealogy handoff is real on that one line and does not line up with a genealogical formula in the chant corpus or with the repeated units on H, P, and Q. Mamari has no glyph 076 and no two-frame tile. The Great Tradition units do not have that tile either. Fischer's elided triad is not distinguished from a shuffle. A gap histogram is closer to the chant's verse gaps than its own shuffle on Ia stem 076, Gv stem 076, Gr sign 001. The chant's gaps peak at 3 and 4 words. The sign gaps that clear the bar also peak on short distances. Track 4 already found this for Staff glyph 076 and did not treat it as a reading. The same limit holds here. Where the most frequent sign is 076, the second row repeats the first test. No sign is given the copula.

This note compares shapes of repetition. It does not match sounds, and it does not read a sign. `reading` is null. The provider is MockProvider and is never asked for a completion. Provider calls: 0.

## What was compared

The sign side is the 267 recurring units from Round 3 Track A (`mdl_cued` on tablets H, P, and Q). 23 of them contain more than one stem. 244 occur on more than one of those three tablets. That cross-copy recurrence has no twin in the chants, which are not written out three times, so it is reported and not forced into the match score.

The language side is the Round 3 running text: Thomson's chants without the love song, Metoro's recitations, and Routledge's timo formula. Mapped (C)V spellings are used, so `tagata` and `tangata` count as one word. Rejected tokens: 115. Three-word formulas at count at least 4: 577, the same 577 as Round 3. The most frequent is still `ki te henua` (87).

The two ranked lists below are separate. Sharing a row does not pair a sign with a word.

| Rank | Sign unit | H/P/Q count | Formula | Count |
| ---: | --- | ---: | --- | ---: |
| 1 | `001` | 211 | `ki te henua` | 87 |
| 2 | `600` | 139 | `ko te tangata` | 80 |
| 3 | `200` | 126 | `te hau tea` | 61 |
| 4 | `002` | 118 | `te henua te` | 57 |
| 5 | `003` | 111 | `i te henua` | 53 |
| 6 | `004` | 83 | `ki te rangi` | 49 |
| 7 | `010` | 81 | `te tangata kua` | 46 |
| 8 | `008` | 74 | `te henua kua` | 44 |

## How a match was defined

These rules were fixed before the shuffles ran.

Each type gets four numbers: burstiness of the gaps between its repeats on the same line (population standard deviation; at least two gaps), the share of its hits that start a line, the share that finish a line, and the share that are immediately followed by the same type. For a three-word formula, "immediately" means the next copy starts where this copy ends. The family score is the mean of those numbers across types. Families with fewer than 8 types are described and not tested. Burstiness is left out of a comparison when fewer than 8 types have two gaps. The distance is the sum of absolute differences on the features that remain, and at least three features are required.

The sign null shuffles units inside each Great Tradition line (400 draws, seed 0). The language null shuffles words inside each chant line (400 draws, seed 1) and rebuilds the formulas. A pair matches only when both fractions are at or under 0.0036, which is 0.05 divided by 14 pairs. Clearing 0.05 on its own is recorded and is not a match.

Zipf slopes are a separate test. Formula slopes are recomputed after the word shuffle. A match needs the absolute gap between the sign slope and the formula slope to be at most 0.15, and the closeness p-value at or under 0.05. Shuffling words does not change word frequencies, so the word slope is described and not given a p-value.

## Frequency, position, spacing

Sign-unit Zipf slope, every recurring unit (count at least 2): -1.0781. The same units kept only when the count is at least 4, which is the formula floor: -0.9502. Three-word formula slope: -0.5800. Words at that floor: -1.2894. All words: -1.3585. The Zipf test uses the shared floor of 4. Absolute gap between those sign units and the formulas: 0.3702. Among shuffles that still had a formula slope, 0/400 were at least as close (p = 0.000). Shuffles with no slope: 0. A p-value of zero here means the real formulas sit closer to the sign slope than the shuffled formulas do. The leftover gap is still 0.3702, and the gate is 0.15. Within that tolerance: False.

Family sizes. Sign units: all_recurring 267, monosign 244, multisign 23, gt_only 27, also_outside 240, ends_076 2, marker_095 1. Formula classes: all_trigrams 577, productive_frame 439, ko_initial 17, ki_te_initial 27. Words at count at least 4: 292.

| Sign family | Language family | Distance | Sign shuffle p | Language shuffle p | Match |
| --- | --- | ---: | --- | --- | --- |
| all_recurring | all_trigrams | 0.1026 | 24/400 = 0.060 | 238/400 = 0.595 | no |
| all_recurring | words_min4 | 0.2434 | 400/400 = 1.000 | 397/400 = 0.993 | no |
| monosign | all_trigrams | 0.0986 | 17/400 = 0.043 | 249/400 = 0.623 | no |
| monosign | words_min4 | 0.2259 | 400/400 = 1.000 | 397/400 = 0.993 | no |
| multisign | all_trigrams | 0.1721 | 400/400 = 1.000 | 278/400 = 0.695 | no |
| multisign | words_min4 | 0.1666 | 400/400 = 1.000 | 399/400 = 0.998 | no |
| gt_only | all_trigrams | 0.1096 | 399/400 = 0.998 | 278/400 = 0.695 | no |
| also_outside | all_trigrams | 0.1086 | 30/400 = 0.075 | 262/400 = 0.655 | no |
| all_recurring | productive_frame | 0.0743 | 24/400 = 0.060 | 104/400 = 0.260 | no |
| all_recurring | ko_initial | 0.1194 | 24/400 = 0.060 | 21/400 = 0.052 | no |
| multisign | productive_frame | 0.1703 | 400/400 = 1.000 | 214/400 = 0.535 | no |
| multisign | ko_initial | 0.1747 | 400/400 = 1.000 | 4/400 = 0.010 | no |
| all_recurring | ki_te_initial | 0.2369 | 400/400 = 1.000 | 85/400 = 0.212 | no |
| multisign | ki_te_initial | 0.1667 | 400/400 = 1.000 | 23/400 = 0.058 | no |

Productive frames are bigrams that occur at least 4 times and are followed by at least 4 different next words. Great Tradition units: 47 such bigrams (rate 0.0128 per adjacent pair). Rapanui words: 466 (rate 0.0289). Closeness of those rates: sign shuffle p = 0.988, word shuffle p = 0.000. A low word-shuffle p-value means the real chant is closer to the sign rate than a shuffled chant is. A high sign-shuffle p-value means shuffling the signs usually gets at least as close, so the signs are not the side that carries a formula shape. Match: False.

No pair, and not the Zipf test, and not the frame-rate test, clears its rule. The recurring sign units do not share a formula family's shape beyond chance.

## The creation chant

Thomson 1891, pp. 520–521, prints Ure Vaeiko's Atua Matariri. Of 48 verses, 41 contain both the copula (`Ki ai Kiroto` or `Kia ai Kiroto`) and a product marker (`Kapu te`, `Kapu to`, or the one `Mapu te`). There are 38 gaps between adjacent full verses. The paraphrase "X couples with Y and Z comes forth" is Thomson's heading for the chant, not a sign reading.

Fischer 1995, *Rapa Nui Journal* 9(4), writes the same frame as "X ki 'ai ki roto ki 'a Y: ka pu te Z" and says a further search found the same kind of text on Mamari (his RR 2), often without the phallic suffix he uses on the Staff. The Staff proposal is his *Journal of the Polynesian Society* paper the same year. Guy 1998, *Anthropos* 93: 552–555, rejects the reading. Barthel 1958, pp. 242–247, is a different Mamari claim: the lunar calendar on Ca6–Ca9, already tested in Track 1. Kohaumotu's staff note says Barthel read glyph 76 as a phallus; Fischer cites Barthel 1958 and 1963 for Metoro's sign-words. Those values stay hypotheses and are not used here.

Mapped tokens in the running text, counted as spelled, not rewritten into Fischer's spacing:

| Pattern | Total | Metoro on Mamari |
| --- | ---: | ---: |
| `ki ai kiroto` | 41 | 0 |
| `kia ai kiroto` | 0 | 0 |
| `ki ai ki roto` | 0 | 0 |
| `ki ai ki roto ki` | 0 | 0 |
| `ka pu te` | 5 | 2 |
| `kapu te` | 38 | 0 |
| `ka pu to` | 0 | 0 |
| `kapu to` | 2 | 0 |
| `mapu te` | 1 | 0 |
| `ma pu te` | 0 | 0 |

Lines that contain a full mapped frame (non-empty X, Y, and Z):

- thomson_1891 `atua_matariri`: 41

The sign test asks whether a passage repeats the way the chant repeats. Two constant delimiters must tile a line for at least 4 cycles, and both slots must have type/token ratio at least 0.75. Separately, gaps between stem 076, and gaps between the single most frequent token, are compared with the chant's verse-gap histogram. The bar for 14 texts is p ≤ 0.0036. A hit would be a spacing resemblance, not a reading.

Stem 076 counts: Ca 0, Cb 0, Ra 0, Rb 0, Ia 564, Gv 43, Gr 2, Hr 7, Hv 1, Pr 5, Pv 1, Qr 7, Qv 0.

| Text | 076-gap p (closer than shuffle) | Most frequent sign, and its gap p | Tiled lines | Tile p |
| --- | --- | --- | ---: | --- |
| Ca | no 076 gaps | `001`, 69/400 = 0.172 | 0 | 400/400 = 1.000 |
| Cb | no 076 gaps | `001`, 254/400 = 0.635 | 0 | 400/400 = 1.000 |
| Ra | no 076 gaps | `001`, 85/400 = 0.212 | 0 | 400/400 = 1.000 |
| Rb | no 076 gaps | `001`, 248/400 = 0.620 | 0 | 400/400 = 1.000 |
| Ia | 0/400 = 0.000 | `076`, 0/400 = 0.000 | 0 | 400/400 = 1.000 |
| Gv | 0/400 = 0.000 | `076`, 0/400 = 0.000 | 1 | 4/400 = 0.010 |
| Gr | 400/400 = 1.000 | `001`, 0/400 = 0.000 | 0 | 400/400 = 1.000 |
| Hr | 400/400 = 1.000 | `001`, 232/400 = 0.580 | 0 | 400/400 = 1.000 |
| Hv | no 076 gaps | `010`, 55/400 = 0.138 | 0 | 400/400 = 1.000 |
| Pr | 400/400 = 1.000 | `001`, 332/400 = 0.830 | 0 | 400/400 = 1.000 |
| Pv | no 076 gaps | `010`, 57/400 = 0.142 | 0 | 400/400 = 1.000 |
| Qr | 400/400 = 1.000 | `003`, 295/400 = 0.738 | 0 | 400/400 = 1.000 |
| Qv | no 076 gaps | `000`, 400/400 = 1.000 | 0 | 400/400 = 1.000 |
| GT-units | 379/400 = 0.948 | `001`, 66/400 = 0.165 | 0 | 400/400 = 1.000 |

On Ia and on Gv the most frequent sign is 076, so those two columns are one comparison written twice. The chant's 38 verse gaps are 18 of length 3, 15 of length 4, and five longer. Staff 076 has 550 gaps and peaks at 3 (197) and 4 (137). That is the resemblance Track 4 already measured. Gv's 35 gaps of 076 peak at 4 (13). Gr's most frequent sign is 001, with 47 gaps peaking at 3 (10). Closer than a shuffle is not the same as close: distances are on a scale from 0 to 2.

Elided triads, the version Fischer offers for tablets that lack the phallic suffix: cut the line into threes and ask whether any slot repeats one sign more than a shuffle. A failure does not prove the unwritten-frame story. Variable slots are what a shuffle looks like too. The bar is p ≤ 0.0056.

| Text | Modal slot rate | Shuffles at least that high |
| --- | ---: | --- |
| Ca | 0.1012 | 174/400 = 0.435 |
| Cb | 0.1007 | 271/400 = 0.677 |
| Hr | 0.0683 | 215/400 = 0.537 |
| Hv | 0.0530 | 296/400 = 0.740 |
| Pr | 0.0769 | 168/400 = 0.420 |
| Pv | 0.0636 | 193/400 = 0.482 |
| Qr | 0.0848 | 264/400 = 0.660 |
| Qv | 0.0682 | 241/400 = 0.603 |
| GT-units | 0.0669 | 54/400 = 0.135 |

## Gv6 and the Great Tradition

Butinov and Knorozov 1956, as reported by Davletshin 2012 and Guy 2003, treat a short passage on the verso of Small Santiago as a genealogy. The structure used here is the one Track 3 measured, not the English sentence. Gv6 has 4 phrases of the form `200 X Y.076` and 3 father-to-child handoffs. In 400 shuffles of that line, 0 produced at least 3 handoffs (p = 0.000). Track 3's larger null was 0 of 5000. The glosses "200 = ko" and "076 = ure" stay hypotheses and are not applied.

The same bracket on other sides:

| Side | Phrases | Handoff links | Longest run |
| --- | ---: | ---: | ---: |
| Gv | 4 | 3 | 3 |
| Gr | 0 | 0 | 0 |
| Ia | 5 | 0 | 0 |
| Ca | 0 | 0 | 0 |
| Cb | 0 | 0 | 0 |
| Hr | 0 | 0 | 0 |
| Hv | 0 | 0 | 0 |
| Pr | 0 | 0 | 0 |
| Pv | 0 | 0 | 0 |
| Qr | 0 | 0 | 0 |
| Qv | 0 | 0 | 0 |

Pooled H/P/Q groups: 0 phrases and 0 links. Shuffles of those groups produce at least 3 links in 0/400 trials. The Great Tradition does not contain the bracket, so there is no lineup to test. The low chance rate only says a chain of that length is hard to get by shuffling. Lines up: False.

An abstract chain ignores sign numbers. It needs a constant opener, a handoff of the third slot into the next middle slot, child-slot diversity at least 0.75, and at least 3 links, the Gv6 length. The bar for three streams is p ≤ 0.0167.

| Stream | Longest links | Shuffles reaching 3 links | Lines up |
| --- | ---: | --- | --- |
| rapanui_words | 1 | 0/400 = 0.000 | no |
| gt_units | 0 | 0/400 = 0.000 | no |
| gt_stems | 1 | 0/400 = 0.000 | no |

rapanui_words: longest chain has 1 link, opener `te`, child slots `toto o`. That is a word or sign pattern in the sample. It is not a decipherment.
gt_units: no chain of even one handoff met the diversity rule.
gt_stems: longest chain has 1 link, opener `060`, child slots `001 069`. That is a word or sign pattern in the sample. It is not a decipherment.

## What this does not claim

No test in this note adopts a reading. A gap histogram that peaks on 3 or 4, on a tablet and in a chant, is a shared scale. It does not say which sign is `ki`, `ai`, `roto`, or `pu`.

No Barthel number is given a syllable or a gloss. Fischer's sentence and the genealogy's English wording stay in the source list as hypotheses. Metoro's words are a language sample. They are not re-paired with signs here; Track 4 already found they do not label the signs. A shared Zipf slope, or a shared habit of starting lines with a frequent item, would still not name a sign.

The run uses `MockProvider` only. Provider calls: 0.
