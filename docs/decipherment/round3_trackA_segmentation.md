# Round 3, Track A — Segmenting the Great Tradition

This note cuts the Great Tradition (tablets H, P, and Q) into repeated sign-strings of roughly word length. It assigns no readings. A unit is a string of Barthel stems, nothing else. The provider is MockProvider and is never asked for a completion. Provider calls: 0.

## What is being segmented

The encoding is the Track C stem encoding: ligatures written with `.` or `:` are split, allograph letters and a leading orientation `V` are stripped, and illegible `000` is dropped. A Barthel group is one hyphen-separated Kohaumotu token. Lines stay lines. Tablets H, P, and Q are the Great Santiago tablet and the two St. Petersburg tablets, the three copies Track C aligned.

Corpus: 14488 stems, 277 lines, 630 stem types before normalization and 622 after it. Great Tradition: 4050 stems on Hr, Hv, Pr, Pv, Qr, Qv (64 lines).

## Normalization

Each stem is rewritten by `merge_table` in `data/decipherment/substitution_classes.json`. The table is the eight systematic classes from Round 2 Track C. A sign that is not listed stays itself. The representative is the more frequent member of the class, so `400` becomes `600`, `011` becomes `001`, `021` becomes `002`, `056` becomes `084`, `081` becomes `008`, `256` becomes `254`, `290` becomes `280`, and `385` becomes `381`. This is an allograph-or-homophone candidate, not a decipherment. `076` and `095` are not in the table.

Tokens rewritten: 489. `011` 114, `021` 93, `056` 19, `081` 60, `256` 25, `290` 56, `385` 41, `400` 81.

On matched columns of significant H/P/Q passages, raw identity is 1369/1588 and normalized identity is 1410/1588. The merge resolves 41 mismatches. Across every significant passage the same count is 44 (1752/2006 raw, 1796/2006 normalized).

## Rule cuts

Four cuts are taken from earlier rounds. They are boundaries, not glosses.

- **Group-final `076`.** Round 2 Track B found that `076` ends its group corpus-wide, suffix-like, and refused a phonetic value. A cut is placed after a stem `076` that is the last stem of its Barthel group. A medial `076` is not a cut.
- **`095`.** Round 2 Track C found `095` as a systematic insertion between `003` and `006`. Every `095` is its own segment: a cut before it and a cut after it. The note does not decide whether that sign is a particle, a determinative, or a boundary mark.
- **Pure `999`.** On the Staff a group whose only stem is `999` is the vertical bar (Round 1 Track 3). Those bars are utterance breaks and are left out of the lexicon. The Great Tradition has 0 such bars.
- **Parallel indels.** In a significant passage, a run of signs present on only one copy, with a matched neighbor on both sides, is an insertion. Cuts fall before and after that run, and between the two neighbors on the copy that lacks it. Track C counted these events; this track reuses the stored columns rather than searching again.

Group-final `076`: 653 corpus-wide, 15 on H/P/Q. Sign `095`: 93 corpus-wide, 27 on H/P/Q. Pure `999`: 96. Indel events: 128, at 293 loci. Union of cue loci: 1291.

The rule segmenter emits exactly those chunks. On H/P/Q, `076` is rare, so a rule chunk can be many groups long. That is a result about the cues, not a claim that a whole line is one word. The unsupervised searches are allowed to cut inside a chunk. They are not allowed to join across a cue when the cued version is the one being trained.

## Unsupervised segmentation

Both searches train on every line of every tablet, then the Great Tradition lines are read back out. The uncued search sees one utterance per inscribed line, each stem its own starting token. The cued search sees one utterance per rule chunk, and a pure `999` is not a token. No word is created by a merge longer than 12 stems. The cap was set before the Thomson comparison. A rule chunk that occurs once is opened back into stems before the cued search starts. A chunk that occurs twice or more starts as one token, so the search can keep it or split it. The rule segmenter itself does not open those chunks.

**Minimum description length.** The code has two parts. Each lexicon type is spelled with the normalized stem alphabet plus an end marker, at `log2(V + 1)` bits per symbol. The corpus is then a sequence of pointers into that lexicon, at the empirical unigram cost. Search is greedy. Each round applies the single merge, the single binary split, or the single full decomposition into stems that shortens the code the most. A merge is offered only when that adjacent pair occurs at least 2 times. One occurrence cannot become a repeated unit, and the code does not pay to spell it. Ties take the lexicographically smaller move. This is in the family of Brent (1999) and of Morfessor Baseline (Creutz and Lagus 2002), adapted to an unsegmented sign stream rather than to a list of already bounded words. It is not those programs.

**Unigram Dirichlet process.** The predictive probability of a word is `(n_w + α P0(w)) / (n + α)`, the Goldwater, Griffiths, and Johnson (2009) unigram model, with α = 20.0. The base measure is `P0(w) = (0.5 / V) ^ length(w)`. With the stop probability at one half, that distribution sums to 1 over every non-empty word and expects short words (mean length 2). That bias is prior, not a fit to Rapanui. Search is greedy on the joint probability: the same three move types, with the same twice-or-more gate on merges, kept when they raise the joint. This is a mode search, not a draw from the posterior. A site-wise Gibbs sweep of 5 passes, seeds 0 and 1, then starts from each DP segmentation. The sweep cannot cross a cue, because cues are utterance breaks. The state kept is the end-of-sweep sample with the highest joint, or the start if no sweep beats it.

A site-wise sampler started from one stem per word almost never proposes a new multi-sign word when the inventory is several hundred stems: the base measure of an unseen bigram is tiny next to the count of a frequent stem. The greedy move looks at every repeated collocation at once, which is the search the inventory size allows. The Gibbs sweep is there to see whether that mode is locally stable.

## Length, frequency, and the Thomson chants

The comparison text is the Thomson 1891 chant sample already used in Track 2 (`thomson_strict`, orthography `strict`), love song excluded. A word's length is its number of (C)V syllables. The sample has 1591 word tokens and rejects 54. Lengths use the 1536 words that yield at least one syllable (3400 syllables, 589 word types). Mean length 2.2135, median 2.0000, Zipf slope -0.7272. Sign-segment length and syllable-word length are different units. A similar mean is not evidence that a stem is a syllable, and it is not a reading.

| Source | Tokens | Types | Mean | Median | Zipf | TV vs Thomson | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |  ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Thomson words | 1536 | 589 | 2.2135 | 2.0000 | -0.7272 | 0 | 460 | 600 | 275 | 146 | 28 | 11 | 9 | 5 | 1 | 0 | 0 | 0 | 1 |
| rules on H/P/Q | 334 | 251 | 12.1257 | 5.0000 | -0.3445 | 0.5120 | 109 | 25 | 12 | 14 | 8 | 12 | 8 | 11 | 8 | 12 | 7 | 3 | 105 |
| mdl on H/P/Q | 3832 | 335 | 1.0569 | 1.0000 | -1.2301 | 0.6645 | 3689 | 125 | 5 | 0 | 8 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 |
| mdl_cued on H/P/Q | 3735 | 339 | 1.0843 | 1.0000 | -1.2217 | 0.6659 | 3597 | 108 | 5 | 0 | 11 | 2 | 1 | 0 | 0 | 4 | 0 | 3 | 4 |
| dp on H/P/Q | 3558 | 361 | 1.1383 | 1.0000 | -1.1852 | 0.6364 | 3319 | 162 | 21 | 10 | 30 | 3 | 2 | 0 | 0 | 5 | 0 | 6 | 0 |
| dp_cued on H/P/Q | 3542 | 361 | 1.1434 | 1.0000 | -1.1907 | 0.6414 | 3324 | 136 | 21 | 14 | 28 | 5 | 3 | 0 | 0 | 4 | 0 | 3 | 4 |
| gibbs on H/P/Q | 3558 | 361 | 1.1383 | 1.0000 | -1.1852 | 0.6364 | 3319 | 162 | 21 | 10 | 30 | 3 | 2 | 0 | 0 | 5 | 0 | 6 | 0 |
| gibbs_cued on H/P/Q | 3542 | 361 | 1.1434 | 1.0000 | -1.1907 | 0.6414 | 3324 | 136 | 21 | 14 | 28 | 5 | 3 | 0 | 0 | 4 | 0 | 3 | 4 |

TV is the total-variation distance between the length histograms. Zipf is the OLS slope of log frequency on log rank.

Corpus-wide, the same segmenters (this is the training text, not only H/P/Q):

| Segmenter | Rounds | Tokens | Types | Repeated multi-sign types | Mean length |
| --- | ---: | ---: | ---: | ---: | ---: |
| rules | 0 | 1454 | 1173 | 56 | 9.8982 |
| mdl | 103 | 13487 | 652 | 53 | 1.0742 |
| mdl_cued | 138 | 13390 | 653 | 49 | 1.0748 |
| dp | 201 | 13064 | 701 | 100 | 1.1090 |
| dp_cued | 212 | 13048 | 698 | 94 | 1.1030 |
| gibbs | None | 13064 | 701 | 100 | 1.1090 |
| gibbs_cued | None | 13048 | 698 | 94 | 1.1030 |

## Agreement

Boundary F1 on Great Tradition line-internal sites. A site is the point between two successive stems of one line. The figure treats the row's cuts as the prediction and the column's cuts as the reference.

|  | rules | mdl | mdl_cued | dp | dp_cued | gibbs | gibbs_cued |
| --- |  ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| rules | — | 0.1308 | 0.1370 | 0.1387 | 0.1441 | 0.1387 | 0.1441 |
| mdl | 0.1308 | — | 0.9845 | 0.9617 | 0.9561 | 0.9617 | 0.9561 |
| mdl_cued | 0.1370 | 0.9845 | — | 0.9594 | 0.9705 | 0.9594 | 0.9705 |
| dp | 0.1387 | 0.9617 | 0.9594 | — | 0.9836 | 1.0000 | 0.9836 |
| dp_cued | 0.1441 | 0.9561 | 0.9705 | 0.9836 | — | 0.9836 | 1.0000 |
| gibbs | 0.1387 | 0.9617 | 0.9594 | 1.0000 | 0.9836 | — | 0.9836 |
| gibbs_cued | 0.1441 | 0.9561 | 0.9705 | 0.9836 | 1.0000 | 0.9836 | — |

Parallel agreement uses significant H–P, H–Q, and P–Q passages only (69 passages: H–P 32, H–Q 18, P–Q 19). A site is a pair of adjacent matched columns, the two stems neighbors on both copies and inside one line on both copies. Overlapping passages contribute a site once. F1 counts a cut that falls on both copies. A segmenter that leaves almost every stem as its own unit cuts at nearly every site, so both copies agree by both cutting and F1 sits near 1. The null keeps each copy's number of cuts and shuffles their positions (200 draws, seed 1). `null_reached` is how many draws match or beat the observed F1. That comparison is the one a near-unigram segmentation does not get for free.

| Segmenter | Sites | Both cut | F1 | Agreement | Null mean F1 | Null reached |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| rules | 1416 | 33 | 0.6055 | 0.9696 | 0.0388 | 0 |
| mdl | 1416 | 1306 | 0.9973 | 0.9951 | 0.9247 | 0 |
| mdl_cued | 1416 | 1200 | 0.9744 | 0.9555 | 0.8692 | 0 |
| dp | 1416 | 1117 | 0.9916 | 0.9866 | 0.7952 | 0 |
| dp_cued | 1416 | 1081 | 0.9656 | 0.9456 | 0.7907 | 0 |
| gibbs | 1416 | 1117 | 0.9916 | 0.9866 | 0.7952 | 0 |
| gibbs_cued | 1416 | 1081 | 0.9656 | 0.9456 | 0.7907 | 0 |

P001 is the 125-sign H/Q passage (Hr2:36..Hr4:0 ‖ Qr2:0..Qr3:65, span 125). Comparable sites inside it: 117.

| Segmenter | Both cut | F1 | Agreement |
| --- | ---: | ---: | ---: |
| rules | 3 | 0.8571 | 0.9915 |
| mdl | 115 | 0.9914 | 0.9829 |
| mdl_cued | 115 | 0.9914 | 0.9829 |
| dp | 96 | 0.9746 | 0.9573 |
| dp_cued | 98 | 0.9751 | 0.9573 |
| gibbs | 96 | 0.9746 | 0.9573 |
| gibbs_cued | 98 | 0.9751 | 0.9573 |

Cue recovery is the share of group-final `076` stems, and of `095` stems, that end a proposed unit. Ending a unit is automatic when nearly every stem is its own unit, so the next table splits those signs into a one-sign unit, the end of a longer unit, or a place inside a unit. The rule segmenter and every cued segmenter keep both signs at a cut by construction.

| Segmenter | `076`-final recovered | `095` recovered | `076` alone | `076` suffix | `076` inside | `095` alone | `095` inside |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| rules | 653/653 | 93/93 | 16 | 637 | 0 | 93 | 0 |
| mdl | 575/653 | 93/93 | 445 | 130 | 78 | 93 | 0 |
| mdl_cued | 653/653 | 93/93 | 521 | 132 | 0 | 93 | 0 |
| dp | 571/653 | 93/93 | 426 | 145 | 82 | 93 | 0 |
| dp_cued | 653/653 | 93/93 | 483 | 170 | 0 | 93 | 0 |
| gibbs | 571/653 | 93/93 | 426 | 145 | 82 | 93 | 0 |
| gibbs_cued | 653/653 | 93/93 | 483 | 170 | 0 | 93 | 0 |

Gibbs changed 0 of 14211 uncued boundary sites relative to the DP mode, and 0 of 12938 cued sites. A flip is a site whose on/off state in the kept sample differs from the greedy DP segmentation.

## Shuffled lines

Each null trial permutes stems inside each line (24 trials, seed 0) and retrains MDL and the DP search, with and without recomputed sign cues. Line lengths and the stem inventory of each line stay. Order does not. Indel cues are not recomputed: the shuffle breaks the parallels, and Track C's own sign-shuffle already produced no significant passage. `076`, `095`, and pure `999` are recomputed from the signs that landed in each group slot.

Two scores are the test. Repeated multi-sign types (length at least 2, count at least 2, corpus-wide) should be higher on the real text if the segmenter is finding repeated strings rather than inventory artifacts. Codelength per sign should be lower on the real text: bits per sign for MDL, nats per sign for the negative DP log probability. `null_reached` counts trials that tie or beat the real text. Mean length on H/P/Q is reported beside them and is not a gate.

| Segmenter | Statistic | Observed | Null mean | Null min | Null max | Null reached |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| mdl | Repeated multi-sign types | 53.0000 | 5.7083 | 3.0000 | 9.0000 | 0 |
| mdl | Code per sign | 7.7678 | 7.9200 | 7.9159 | 7.9229 | 0 |
| mdl | H/P/Q mean length | 1.0569 | 1.0004 | 1.0000 | 1.0010 | 0 |
| mdl_cued | Repeated multi-sign types | 49.0000 | 2.7917 | 0.0000 | 6.0000 | 0 |
| mdl_cued | Code per sign | 7.7185 | 7.9038 | 7.8986 | 7.9083 | 0 |
| mdl_cued | H/P/Q mean length | 1.0843 | 1.0001 | 1.0000 | 1.0007 | 0 |
| dp | Repeated multi-sign types | 100.0000 | 10.7083 | 3.0000 | 17.0000 | 0 |
| dp | Code per sign | 4.9672 | 5.1154 | 5.1125 | 5.1185 | 0 |
| dp | H/P/Q mean length | 1.1383 | 1.0017 | 1.0002 | 1.0045 | 0 |
| dp_cued | Repeated multi-sign types | 94.0000 | 7.2500 | 1.0000 | 13.0000 | 0 |
| dp_cued | Code per sign | 4.9425 | 5.1053 | 5.1018 | 5.1091 | 0 |
| dp_cued | H/P/Q mean length | 1.1434 | 1.0015 | 1.0000 | 1.0040 | 0 |

## Candidate lexicon

The lexicon is the Great Tradition inventory of `mdl_cued`: units with count at least 2. 267 units, of which 267 also occur at least twice under another segmenter, and 2 end in `076`. `corpus_count` is the same string under the same segmenter on the whole corpus, Staff included. `also_found_by` lists the other segmenters. Contexts are up to five Great Tradition loci, with the previous and next unit. `reading` is null on every row.

The strings are unread. Ending in `076`, or being the single sign `095`, is a distributional flag carried over from the cue definitions. It is not a gloss, a particle reading, or a suffix reading.

Of those, 23 contain two or more stems and 244 are single stems. The table is the twenty most frequent multi-sign units. The single-stem units with the highest H/P/Q counts are `001` 211, `600` 139, `200` 126, `002` 118, `003` 111, `004` 83.

2 multi-sign units are longer than the merge cap of 12. The search cannot build a word that long by merging. These are repeated rule chunks it left unsplit: `069+162+200+200+200+052+200+008+200+001+004+064+044+004+049+004+044+004+064+202+280` (length 21, count 2), `003+306+003+084+004+280+200+048+254+755+003+734+003+306+003` (length 15, count 2).

| Signs | Length | H/P/Q count | Corpus count | Sides | Also found by |
| --- | ---: | ---: | ---: | --- | --- |
| `004+064` | 2 | 28 | 76 | Hr, Hv, Pr, Pv, Qr, Qv | rules, mdl, dp, dp_cued, gibbs, gibbs_cued |
| `015+022` | 2 | 17 | 17 | Hr, Pr, Qr | mdl, dp, gibbs |
| `067+010` | 2 | 9 | 17 | Hv, Pv, Qv | rules, mdl, dp, dp_cued, gibbs, gibbs_cued |
| `260+001` | 2 | 8 | 23 | Hr, Hv, Pr, Qv | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `308+034` | 2 | 8 | 8 | Hv, Pv, Qv | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `002+010+002+010+144` | 5 | 8 | 8 | Hv, Pv, Qv | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `006+074` | 2 | 7 | 28 | Hr, Pr, Qv | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `020+010` | 2 | 7 | 27 | Hv, Pr, Pv, Qv | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `306+003+028` | 3 | 5 | 8 | Hr, Pr, Qr, Qv | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `306+003` | 2 | 4 | 15 | Pr, Qr | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `430+076` | 2 | 4 | 45 | Hr, Qr | rules, mdl, dp, dp_cued, gibbs, gibbs_cued |
| `702+008` | 2 | 4 | 4 | Hv, Pv | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `060+055+588+060+001` | 5 | 3 | 3 | Hr, Pr, Qr | rules, dp, dp_cued, gibbs, gibbs_cued |
| `002+144+002+662+680+005+010+005+052+022+243+001` | 12 | 3 | 3 | Hr, Pr, Qr | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `034+335` | 2 | 2 | 2 | Hv, Pv | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `073+064` | 2 | 2 | 9 | Hv | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `491+522` | 2 | 2 | 2 | Hr, Pr | mdl, dp, dp_cued, gibbs, gibbs_cued |
| `600+121` | 2 | 2 | 2 | Hr, Qr | mdl |
| `382+382+002+070+202+202` | 6 | 2 | 2 | Hr, Pr | rules, dp_cued, gibbs_cued |
| `050+504+003+144+020+003+200+006+003+180` | 10 | 2 | 2 | Hv, Pv | mdl, dp, dp_cued, gibbs, gibbs_cued |

The full list is `data/decipherment/candidate_units.json` (267 units).

## What this does not claim

No stem is given a Rapanui syllable, a word, or a meaning. The primary segmenter is `mdl_cued` because the task asked for the Round 1 and Round 2 cuts to be available to the search, not because its length histogram sits closer to Thomson than another row does. The DP base measure already prefers short units, so a mean near the Thomson mean would not be an independent confirmation. Shuffled-line scores are the check on whether repeated multi-sign units are an artifact of the unigram frequencies. Parallel F1 is the check on whether two copies of the same passage receive the same cuts. Neither check produces a translation.

## Sources

- Brent, Michael R. 1999. “An Efficient, Probabilistically Sound Algorithm for Segmentation and Word Discovery.” *Machine Learning* 34.
- Creutz, Mathias, and Krista Lagus. 2002. “Unsupervised Discovery of Morphemes.” In *Proceedings of the ACL Workshop on Morphological and Phonological Learning*.
- Goldwater, Sharon, Thomas L. Griffiths, and Mark Johnson. 2009. “A Bayesian Framework for Word Segmentation: Exploring the Effects of Context.” *Cognition* 112.
- The cue citations are the Round 1 and Round 2 notes in this directory: group-final `076` (Track B), `095` between `003` and `006` and the substitution classes (Track C), Staff `999` bars (Track 3), and the Thomson 1891 chant sample (Track 2).
