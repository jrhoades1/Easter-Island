# Track 1: Mamari lunar calendar as an anchor

The only stretch of Rongorongo with a widely accepted reading is the lunar calendar on tablet Mamari (Barthel text C), side a, lines Ca6–Ca9. This note turns that reading into a set of **anchored signs**: Barthel numbers whose place in the calendar is measured on the vendored corpus, with a cited source or an explicit hypothesis for every meaning. It does not translate the tablet.

The counts below are locked by `tests/test_track1_mamari_calendar.py`. They are recomputed from the vendored Kohaumotu Barthel pages. No glyph number was invented, and no Barthel number was merged with another.

## Sources

| Source | What it is used for |
| --- | --- |
| Barthel 1958, *Grundlagen zur Entzifferung der Osterinselschrift*, pp. 242–247 | Identifies the Ca6–Ca9 passage as a lunar calendar. Numbering used throughout. |
| Guy 1990, “The lunar calendar of Tablet Mamari,” *Journal de la Société des Océanistes* 91: 135–149. DOI [10.3406/jso.1990.2882](https://doi.org/10.3406/jso.1990.2882) | Delimiter, glyph 40A as the repeated night sign, glyphs 143 and 152, the 12 / 13 count around 152, comparison with recorded night lists. |
| Horley 2011, “Lunar calendar in rongorongo texts and rock art of Easter Island,” *JSO* 132: 17–38. DOI [10.4000/jso.6314](https://doi.org/10.4000/jso.6314) | Agrees the passage is 30 nights and that sign 152 marks full moon. Disagrees with Guy about which crescents are intercalary. |
| Wieczorek 2011, “Astronomical Content in Rongorongo Tablet Keiti,” *JSO* 132. DOI [10.4000/jso.6272](https://doi.org/10.4000/jso.6272) | Restates Guy’s 28+2 analysis and the list lengths: Englert 28, Thomson 29, Métraux 30. |
| Thomson 1891, *Te Pito te Henua*, p. 546; Métraux 1940, Bishop Museum Bulletin 160, p. 50; Englert 1948, *La Tierra de Hotu Matu'a*, pp. 311–312 | The recorded Rapanui night names. Guy used the Englert and Métraux lists as quoted in Heyerdahl et al. 1961, p. 416. |
| [Kohaumotu Ca.html](http://kohaumotu.org/Rongorongo/C/Ca.html) and the [lunar commentary](http://kohaumotu.org/rongorongo_org/rosetta/lunar.html) | The Barthel numbers actually counted here. The commentary summarizes Guy: 28 basic nights plus Hotu and Hiro. |
| Wikipedia, “Rapa Nui calendar” | Secondary alignment of the Thomson / Englert / Métraux name lists. Not a primary source. |

The mean synodic month is about 29.53 days. A list of 28 nights does not stay aligned with the moon unless one or two nights are added. That astronomical point is Guy’s argument, cited above, not a new claim.

## Where the calendar is

The vendored fixture `tests/fixtures/mamari_ca6_ca9_barthel.json` is the calendar. On the full Ca.html side it is:

- Ca6 from the first `390.041` (stem index 24) through the end of the line
- all of Ca7 and Ca8
- the first two stems of Ca9 (`040 040`)

That slice is 101 stems: 16 + 43 + 40 + 2.

Ca.html and the fixture disagree in three tokens, and only by a trailing damage star: Ca6 `041` / `041*`, Ca7 `040` / `040*`, Ca8 `385` / `385*`. The mechanical stem parser strips those stars, so the stem sequences are the same. The stars are not readings.

Tablet C in some older search loaders is stored as calendar-slice + remainder-slice + verso, which splits Ca6 and Ca9. This search uses the intact lines Ca1–Ca14 and Cb1–Cb14. The two arrangements contain the same stems. Tablets A–V are included. W has no vendored Barthel page and is not searched.

## Anchored signs

“Anchored” here means: the sign’s **location and neighbors** are measured, and any **meaning** is tied to a publication. A lone crescent elsewhere on another tablet is not a calendar citation.

| Sign | Barthel stem | Where it is anchored | Meaning | Confidence |
| --- | --- | --- | --- | --- |
| Night crescent | `040` | 28 times in the calendar passage. Runs of 5 or more occur only here (see below). | Guy 1990: glyph 40A is the repeated night sign, sometimes ligatured to another sign. Barthel 1958 already treated the passage as lunar. | **High** that these 28 are the calendar’s night markers. **Not** high for a lone `040` anywhere else: the corpus has 152 of them. |
| Delimiter crescent | `041` | All 16 calendar occurrences sit inside the delimiter windows. None of the calendar’s `041` is a night slot. | Guy’s delimiter contains two `41` signs. He does not count them as nights. | **High** inside this passage. The stem also occurs on other tablets (54 in A–V), so a lone `041` is not the delimiter. |
| Near-full crescent | `143` | Once, immediately before `152`, on Ca7. Nowhere else in A–V. | **Hypothesis (Guy 1990):** a deep filled crescent, the moon at or near full, the night before the full moon. | **Medium.** Unique, and adjacent to `152`, but the picture-reading is Guy’s. |
| Full moon | `152` | Once, on Ca7, after `143`. Nowhere else in A–V. | Guy 1990: the figure in the moon. Horley 2011 also treats 152 as full moon. | **Medium-high** as the passage’s central lunar sign. The iconography is an argument, not a phonetic reading. |
| Eight-sign delimiter | `390 041 378 041 670 008 078 711` | Six exact hits, all in the calendar (three on Ca7, three on Ca8). | Guy 1990: the group that separates nights. Kohaumotu’s summary of Guy: some of these groups are observation instructions, and the fish groups mark waxing and waning. | **High** as a separator. **Low** for the waxing/waning and “observe the moon’s diameter” glosses. Those are Guy’s hypotheses, via the Kohaumotu summary. |
| Same delimiter, third sign `315` | `390 041 315 041 670 008 078 711` | One hit, Ca6 stem 24, the start of the calendar. | The fixture keeps `315` distinct from `378`. Guy calls these “close variants.” | **High** as the opening delimiter. Not rewritten to `378`. |
| Short delimiter | `390 041 375 041` | One hit, at the end of Ca6. The full eight-sign form with `375` does not occur. | Guy 1990: a shorter form `390.41 378y 41` occurs once. Here the third sign is the published `375`, not `378`. | **High** as the short separator. The `375`/`378` difference is left as published. |
| Two crescents on Ca9 | `040 040` | After the last delimiter and after `280 385 385`. | **Hypothesis (Guy 1990; Kohaumotu summary; Wieczorek 2011):** the intercalary nights Hotu and Hiro. **Hypothesis (Horley 2011):** the last two crescents are moonless nights inside a 30-night month, and the small superscript crescents are not intercalary insertions. | **High** that these two stand outside the repeated groups. **Low** for the names Hotu and Hiro. Guy and Horley do not agree on the mechanism. |
| Group before those two | `280 385 385` | End of Ca8, and **also** once on Ca5 (outside the calendar). | Kohaumotu, summarizing Guy: meaning uncertain; perhaps a phonetic hint for Hotu / Hiro. | **Low.** The same three signs occur before the calendar, so they are not an intercalation mark by themselves. |

Ligatures that contain `040` in the calendar, kept as published and split into stems: `040.010`, `074f.040`, `044.040`, `003.040`. Guy 1990 retranscribes Barthel’s 44 as 78 for the night Maure. This track does **not** apply that change. The stem `044` stays `044`.

### What is not equated

Allograph-tolerant search, labeled as such:

- **Delimiter slot only.** The third sign may be `315`, `375`, or `378`. Everything else in the eight-sign group must match. That finds the six `378` hits plus the one `315` hit. The eight-sign form with `375` has zero hits.
- **Crescent-number family `{040, 041}`.** These are counted separately and added only as a labeled family total. They are not the same sign. Merging them would pour 16 delimiter crescents into the night count.

Letter suffixes (`378y`, `041h`, `040*`) are already removed by the existing stem parser. That is the mechanical allograph strip. It is not a new identification.

## Night sequence

Reading order is Ca6–Ca9 joined. Line breaks are not signs. Delimiters stay in the sequence, so they break runs of `040`.

Eight delimiter windows, in order:

| # | Line | Stem index | Form |
| --- | --- | --- | --- |
| 1 | Ca6 | 24 | full, third sign `315` |
| 2 | Ca6 | 36 | short, third sign `375` |
| 3 | Ca7 | 6 | full, `378` |
| 4 | Ca7 | 19 | full, `378` |
| 5 | Ca7 | 33 | full, `378` |
| 6 | Ca8 | 3 | full, `378` |
| 7 | Ca8 | 15 | full, `378` |
| 8 | Ca8 | 29 | full, `378` |

`040` counts **between** those windows: **2, 6, 3, 2, 5, 3, 5**. Sum 26. After the last window the passage ends `280 385 385 040 040`. Those last two crescents bring the `040` total to 28.

The gaps are not equal. A model in which a delimiter falls every fixed number of nights **fails**. What repeats is the delimiter, not a constant period. The lunation, if the calendar hypothesis is right, is the whole passage, not the gap.

Guy 1990 counts glyph 40A from 152 back to the first eight-sign group (**12**) and forward to the last eight-sign group (**13**). On these stems the same cuts give **13** before 152 and **13** after. The forward count matches Guy. The backward count is one higher. The transcription was not adjusted to remove the extra `040`. One candidate, marked **hypothesis**, is Guy’s retranscription of the `044.040` ligature; it is not applied here.

Maximal `040` runs in the joined passage, split at the unique `152`:

- before `152`: lengths **1, 1, 6, 1, 1, 1, 2**
- after `152`: lengths **5, 2, 1, 5, 2**

The run of 6 is the six bare crescents at the start of Ca7. One run of 5 is internal to Ca8 (stems 24–29). The other run of 5 is what you get only by joining the end of Ca7 (`040 040`) to the start of Ca8 (`040 040 040`); no delimiter stands between them, only the line break. Within single lines, the only runs of length ≥ 5 in the whole of A–V are Ca7’s 6 and Ca8’s 5, both inside the calendar.

## Statistical tests

Two tests were specified from the publications, then measured. Neither test assigns a night name to a sign.

### 1. Length against 28–30

Recorded list lengths, as Wieczorek 2011 reports them from Englert, Thomson, and Métraux: **28, 29, 30**.

| Counting rule | Result | Inside 28–30? | Status |
| --- | --- | --- | --- |
| Every calendar stem `040`, including the two on Ca9 | 28 | yes | Measurement. Same length as Englert’s list. Those 28 already include Ca9. |
| `040` only in the seven gaps between delimiters | 26 | no | Measurement. Ca9 is outside those gaps. |
| The 26 gap crescents, plus `143` and `152` | 28 | yes | **Hypothesis.** This is one way to land on 28 without using Ca9. It is not Guy’s published 12+13 arithmetic (see above). |
| All 28 crescents, plus `143` and `152` as further nights | 30 | yes | **Hypothesis.** Adds the two non-crescent signs on top of every crescent, including Ca9. Same length as Métraux’s list. Not a second measurement of `040`. |

A crescent count of 28 matches a recorded list length. It does not choose 29 against 30, and it is not the same grouping as Guy’s 28 basic nights plus two intercalary nights. Guy’s 28 sits in the delimited portion; our delimited portion has 26 crescents, not 28. Getting to his 28+2 means counting signs that are not `040` (143, 152, and, in his transcription, glyph 78). That remains his hypothesis. Horley 2011 instead treats the whole passage as 30 nights and the last two crescents as moonless nights, not as optional insertions. Both are cited. Neither is applied as a relabeling of the stems.

### 2. Kokore run lengths around glyph 152

In the aligned Thomson / Englert / Métraux lists the unnamed *kokore* nights come in two series: six (*tahi* through *ono*) in the waxing half, and five (*tahi* through *rima*) after full moon. Guy places full moon at glyph 152.

The measured sequence has a maximal `040` run of **6 before** `152` and a maximal `040` run of **5 after** it. That is the pattern suggested by those two series. It is not a name-by-name alignment. No *kokore* name is written onto a glyph.

Null model: shuffle the 101 calendar stems, keeping the same multiset, and ask whether a run of 6 still falls before the unique `152` and a run of 5 after it. Fisher–Yates, seed 0, 5000 draws: **0 hits**. The Monte Carlo bound is 1/5001. The order of this passage is not what that shuffle produces.

This does not prove the runs are the *kokore* series. It shows that a pattern taken from the recorded lists and from Guy’s placement of `152` is rare under a token shuffle of this passage.

### 3. Is `040` just common?

No. The calendar is 101 stems out of 14,841 in A–V (0.7% of the corpus) but holds 28 of the 152 stems `040` (18%). Rates: 28/101 in the calendar, 124/14,740 outside it, about 33 times higher. The 2×2 chi-square statistic is 715.1 (numerator 2,376,887,638,931,856, denominator 3,323,951,482,720).

That chi-square treats stems as independent, and these stems come in runs, so it is only a rate comparison. The shuffle test above is the one that respects order. Both point the same way: this passage is where the crescents cluster.

## Recorded night names

These are the comparison lists. **None of these names is assigned to a Barthel number in this track.**

Lengths: Englert 28, Thomson 29, Métraux 30 (Wieczorek 2011). Guy’s explanation, quoted by Wieczorek: Englert’s informants may have given the basic 28-night month without Hotu and Hiro; Thomson includes Hotu but not Hiro; Métraux includes both.

The aligned names below follow the secondary table on Wikipedia’s “Rapa Nui calendar,” which lines the three lists up on *(o)ata* as new moon. Thomson’s own diary order started later in the month (kokore tahi on 27 November 1886). Spellings vary by a vowel or an *o-*. The *kokore* series that the run-length test uses are the six-night series and the five-night series visible in all three columns.

| | Englert | Thomson | Métraux | | Englert | Thomson | Métraux |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | oata | oata | ata | 15 | omotohi | omotohi | motohi |
| 2 | ohiro | oari | ari | 16 | kokore tahi | kokore tahi | kokore tahi |
| 3 | kokore tahi | kokore tahi | kokore tahi | 17 | kokore rua | kokore rua | kokore rua |
| 4 | kokore rua | kokore rua | kokore rua | 18 | kokore toru | kokore toru | kokore toru |
| 5 | kokore toru | kokore toru | kokore toru | 19 | kokore hâ | kokore ha | kokore ha |
| 6 | kokore hâ | kokore ha | kokore ha | 20 | kokore rima | kokore rima | kokore rima |
| 7 | kokore rima | kokore rima | kokore rima | 21 | tapume | tapume | tapume |
| 8 | kokore ono | kokore ono | kokore ono | 22 | matua | matua | matua |
| 9 | maharu | maharu | maharu | 23 | orongo | orongo | rongo |
| 10 | ohua | ohua | hua | 24 | orongo taane | orongo tane | rongo tane |
| 11 | otua | otua | atua | 25 | mauri nui | mauri nui | mauri nui |
| — | — | ohotu | hotu | 26 | mauri karo | mauri kero | mauri kero |
| 12 | maure | maure | maure | 27 | omutu | omutu | mutu |
| 13 | ina-ira | ina-ira | ina-ira | 28 | tireo | tireo | tireo |
| 14 | rakau | rakau | rakau | — | — | — | hiro |

*Kokore* is the unnamed series (*tahi, rua, toru, hâ/ha, rima, ono* = 1–6). The early series in this table is six nights; the later series is five.

## Search of the other tablets

Exact hits, unless the row says “family.” Context is up to three stems on the same line and does not cross a line break.

### Delimiter and the unique pair

| Cluster | Hits outside C | Hits on C | Context |
| --- | --- | --- | --- |
| `390 041 378 041 670 008 078 711` | 0 | 6 | Ca7:6 between `040 040 040` and `040 074 040`; Ca7:19 between `040 059 040` and `044 040 040`; Ca7:33 between `143 152 600` and `040 040`; Ca8:3 between `040 040 040` and `040 040 003`; Ca8:15 between `040 003 040` and `600 040 040`; Ca8:29 between `040 040 040` and `280 385 385` |
| `390 041 315 041 670 008 078 711` | 0 | 1 | Ca6:24 between `280 001 006` and `040 010 040` |
| `390 041 375 041 670 008 078 711` | 0 | 0 | — |
| `390 041 375 041` (the short form) | 0 | 1 | Ca6:36 after `010 040 030`, at the end of the line |
| `143 152` | 0 | 1 | Ca7:30 between `044 040 040` and `600 390 041` |
| `390 041` (opening pair) | 0 | 8 | The eight delimiter starts above. Not found elsewhere. |
| `670 008 078 711` (tail) | 0 | 7 | The seven full delimiters. The short Ca6 form has no tail. |

`600 040` is a **negative control**. It occurs once each on A, B, C, N, and P. A neighbor of the calendar delimiter is not, by itself, an anchor.

`280 385 385` occurs twice, both on C: Ca5:18 (before the calendar; between `036 550 022` and `038 007 600`) and Ca8:37 (end of the line, immediately before Ca9’s two crescents). Same signs, two contexts. Not used as an anchor.

### Stem `040`, exact

| Tablet | `040` | `041` | Family `{040, 041}` | Tablet | `040` | `041` | Family `{040, 041}` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 17 | 5 | 22 | L | 0 | 0 | 0 |
| B | 9 | 6 | 15 | M | 0 | 0 | 0 |
| C | 45 | 21 | 66 | N | 1 | 0 | 1 |
| D | 1 | 2 | 3 | O | 3 | 0 | 3 |
| E | 19 | 7 | 26 | P | 8 | 4 | 12 |
| F | 2 | 0 | 2 | Q | 9 | 1 | 10 |
| G | 5 | 0 | 5 | R | 12 | 0 | 12 |
| H | 10 | 6 | 16 | S | 5 | 1 | 6 |
| I | 4 | 1 | 5 | T | 0 | 0 | 0 |
| J | 0 | 0 | 0 | U | 1 | 0 | 1 |
| K | 1 | 0 | 1 | V | 0 | 0 | 0 |

Family cells are sums of the two exact columns. They are not extra hits.

Of C’s 45 crescents `040`, 28 are inside the calendar and 17 are outside it: Ca10 (3), Ca11 (2), Ca12 (1), and eleven more on Cb (Cb4, Cb9, Cb10, Cb11, Cb12, Cb13, Cb14). None of those outside occurrences is a run of five or longer. The long runs are calendar-only.

`143` and `152` do not occur outside that one Ca7 pair.

## What is safe to reuse

For a later search, these are the anchors, and only these:

1. The eight-sign delimiter, including the one Ca6 form with `315`, and the one short Ca6 form with `375`. Exact. Absent outside Mamari in this corpus.
2. The pair `143 152`. Exact. Unique in A–V. Lunar reading: Guy 1990 and Horley 2011, still a hypothesis about the picture, not a phonetic value.
3. Long runs of `040` (length at least 5). Calendar-only. A single `040` is too common to cite.
4. The structural fact that two `040`s on Ca9 sit past the last delimiter. The names Hotu and Hiro are Guy’s hypothesis, not an anchor.

`041` is part of the delimiter **in this passage**. It is not a night sign here, and it is not rare enough elsewhere to anchor a search by itself.

No other Mamari sign was given a meaning. The script remains undeciphered outside this passage.
