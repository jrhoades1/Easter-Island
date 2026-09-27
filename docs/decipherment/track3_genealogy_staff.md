# Track 3 — Genealogy structure on the Santiago Staff (I) and Small Santiago (G)

This note tests two published structure claims and records the segmentation hooks that survive. It does not assign readings. Every gloss below is a **hypothesis** with a source. Sign numbers are Barthel codes from the vendored Kohaumotu HTML. Counts are locked in `tests/test_track3_genealogy_staff.py`. The measures live in `decipherment/track3_genealogy.py`.

## Corpus

The encodings were already in the repo. Nothing new was typed in.

| Text | Fixture | What was reused |
| --- | --- | --- |
| I, Santiago Staff | `tests/fixtures/santiago_ia_html/Ia.html` | Ia1–Ia14, Horley’s line order as published on that page |
| G recto | `tests/fixtures/small_santiago_gr_html/Gr.html` | Gr1–Gr8 |
| G verso | `tests/fixtures/small_santiago_gv_html/Gv.html` | Gv1–Gv8 |

Stem totals match the standing scoreboards: I has 2469 stems, of which 076 occurs 564 times; Gv has 359 stems and 43 times 076; Gr has 355 stems and 2 times 076. A group is one hyphen-separated token, so a dot ligature such as `280.076` stays one group. Stems use the same rule as `published_stems` (a colon is rewritten to a dot, then allograph letters are stripped).

### Vertical strokes are already encoded

The Staff’s vertical division lines are Barthel’s slash. The C.E.I.P.P. digitization notes say that stroke was coded 000 in their extended system, and that these web pages write it **999** so that 000 can stay “unidentified”:

> The sign consisting of a mere vertical stroke, found only on the Santiago Staff, represented in Barthel's system by a forward slash (/), and in the C.E.I.P.P.'s extended system by 000 … is represented here by 999.

Source: [Rongorongo digitized corpus](http://kohaumotu.org/rongorongo_org/corpus/digit.html).

`Ia.html` itself does not gloss 999 (that absence is the cycle-47 lock). The identification comes from the digitization note, not from a new transcription. A scan of every vendored Kohaumotu `<td>` finds stem 999 only in `santiago_ia_html/Ia.html`.

On that page the 999 codes are:

| Published form | Groups |
| --- | ---: |
| `999` | 87 |
| `999h` (superscript stroke) | 6 |
| `999t` (subscript stroke) | 3 |
| `999.440.076` (ligature, left intact) | 1 |
| **Codes** | **97** |
| **Pure breaks** (the group’s only stem is 999) | **96** |

Fischer (1995) says the Staff “displays as many as 97” vertical lines. That matches the 97 codes. A later count of 103 strokes (Wikipedia, “Rongorongo text I”, citing the artefact rather than this transcription) is a different tally. This track does not insert the missing six. `000!` in the same file is the illegible-sign code, not the stroke.

Davletshin (2012) discusses a staff-only sign he calls TB000, about 98 times, almost always one or two signs before 076, and argues it is a logogram rather than punctuation. Given the C.E.I.P.P. recoding, that sign is the stroke this corpus writes as 999. His function claim and Fischer’s divider claim are both **hypotheses**. The position tests below do not choose between them, because both expect 999 to sit next to 076.

## Hypotheses under test

These are the claims. None of them is adopted as a translation.

1. **Butinov and Knorozov (1956).** On the verso of the Small Santiago tablet, a short sequence is a genealogy: each name repeats as the next name’s father. Secondary statements of the same claim: Davletshin 2012 (*Journal de la Société des Océanistes* 134:95–110, doi:10.4000/jso.6658); Guy 2003 (*Rapa Nui Journal* 17(1)); the Kohaumotu genealogy page `http://kohaumotu.org/rongorongo_org/rosetta/g.html`. Wikipedia’s “Rongorongo text G” summarizes it as about 15 glyphs on Gv6, with 076 as a patronymic taxogram. Davletshin counts six names on Gv5–Gv6 and treats 200 (“man”) as a title-like opener and 076 as the patronymic marker *ure* (Metoro, as he cites it; Kondratov 1969, as he cites it). He also argues that 076 may **open** the next name even though the drawing attaches it to the previous sign.
2. **Fischer (1995, 1997).** The Staff is divided by the vertical lines into phrases whose minimum is a triad. The glyph to the right of each line bears a phallic suffix (076). Positions 1, 4, 7, … inside a division do the same. A division does not end on that suffix, and the sign before the end does not bear it either. The formula he writes as X¹YZ is the **hypothesis** “X copulated with Y: there issued forth Z.” The sign sequence he quotes for “all the birds … the fish … the sun” is `606.076`, then a fish sign, then a sun sign. Guy (1998, *Anthropos* 93:552–555) argues that this cosmogonic reading does not hold, and that if the Gv genealogy is real then 076 is a patronymic mark and the Staff is mostly names.

## What was measured

- **Strict phrase.** Three groups: a group whose only stem is 200; a name group that contains neither 200, 076, nor 999; a group that ends in 076 and has another stem. Search is left to right and non-overlapping.
- **Handoff.** The non-076 stem of phrase *n* equals the name stem of phrase *n*+1, and the next phrase starts immediately.
- **Quad.** The same pattern with two name groups before the 076-group (`200 A B C.076`). This is the longer first entry on Gv6.
- **Interior span.** The groups strictly between two pure-999 breaks on one line. Line edges are not Fischer’s “between two bars,” so they are counted separately and are not the test population.
- **Content null.** Pure-999 groups stay put. The other groups on each Staff line are shuffled. 2000 trials, seed 0. This asks whether 076 prefers the claimed slots.
- **Placement null.** Every group on each line is shuffled, so the strokes move. 2000 trials, seed 2. This asks whether span lengths prefer 3 and multiples of 3.
- **Gv6 null.** The 28 groups of Gv6 are shuffled. 5000 trials, seed 0.
- **Text-level template null.** Groups are pooled and dealt back into the same line lengths. Gv: 2000 trials, seed 1. Staff: 2000 trials, seed 3.

A **name-like slot**, inside one list only, means a high type/token ratio. A **marker slot** means the same sign in every phrase. That is a distributional label, not a gloss.

## Gv6, the genealogy sequence

Gv5 and Gv7 contain 200 and 076, and they contain no strict phrase. Joining Gv5–Gv7 does not add a phrase or a handoff. Gr has none. The whole pattern is on Gv6.

Immediately before the chain, Gv6 has one quad that does not hand off:

`200, 769, 381, 002.076`

The third group’s stem is 381 and the 076-host is 002. The next name stem is `000` (the token is `000!`, the illegible code). Neither 381 nor 002 equals 000.

The chain itself, in the vendored groups:

| Phrase | Groups | Name stem | 076-host |
| --- | --- | --- | --- |
| 1 | `200` `000!` `280.076` | 000 (illegible) | 280 |
| 2 | `200` `280` `730.076` | 280 | 730 |
| 3 | `200` `730` `517a.076` | 730 | 517 |
| 4 | `200` `517a` `222.076` | 517 | 222 |

That is **4 phrases** and **3 father-to-child** handoffs in one run (280, then 730, then 517). The child slot has 4 types in 4 tokens. The father slot has 4 types in 4 tokens. Sign 200 opens all four. Sign 076 closes all four, as the last stem of a ligature. Those two signs are the closed slots. The other stems are the open slots. One open slot is illegible in this transcription.

The same four phrases are the only strict phrases on Gv, Gr, and the joined Gv5–Gv7 window.

Shuffle of Gv6: **0 of 5000** trials had 3 or more handoffs, and 0 of 5000 had a run that long. 5 of 5000 had at least 4 strict phrases, so the phrase count on that short line is already uncommon; the handoff is the part that does not appear by chance. Shuffle of the whole verso, line lengths kept: **0 of 2000** trials had 3 handoffs. 32 of 2000 had at least 4 phrases.

The published “six names” and “15 glyphs” are not reproduced as counts. This encoding shows one non-chaining quad plus four chaining phrases (five 200…076 entries, not six). The chaining span is 12 groups and 16 stems if `000!` is counted, 15 stems if that illegible code is left out. The 15-glyph figure may be that arithmetic. It is not a reason to rewrite `000!`.

### What this does to the “X begat Y” sentence

The handoff is real. The English sentence is still a **hypothesis** (Butinov and Knorozov, via Davletshin 2012 and Guy 1998). Two cuts of the same stems both keep the handoff:

- The transcription’s dot reads as `[200 X Y.076]`, with 076 closing the phrase.
- Davletshin’s cut reads 076 as the start of the next name (`076-200-…`), with the dot explained as a graphic habit rather than a word boundary.

This track does not choose the cut. The hook other tracks can use is the bracket and the handoff, on Gv6 only.

## The Staff

### The bracket after a stroke

Of 96 pure breaks, the next group contains 076 in **91/96** cases. 85 of those 91 end in 076 with a host sign (a true suffix, `X.076`). 3 are a bare `076`. The other 3 contain 076 in a different position inside the group. The five breaks that are not followed immediately by 076 are Ia6 at group indexes 27, 38, 72, and 95, and Ia13 at index 116.

Under the content null, **0 of 2000** shuffles placed 076 on the following group 91 or more times. The association survives. It is also what both the divider hypothesis and Davletshin’s logogram hypothesis predict, so it does not decide what 999 means.

### Are the spans triads?

Interior spans: **83**. Median length **9**. Lengths:

| Length | Spans | Length | Spans |
| ---: | ---: | ---: | ---: |
| 2 | 1 | 18 | 3 |
| 3 | 16 | 20 | 1 |
| 5 | 2 | 21 | 1 |
| 6 | 11 | 22 | 1 |
| 8 | 7 | 24 | 2 |
| 9 | 8 | 25 | 1 |
| 10 | 3 | 28 | 1 |
| 11 | 2 | 30 | 1 |
| 12 | 5 | 32 | 2 |
| 13 | 1 | 35 | 1 |
| 15 | 3 | 39 | 1 |
| 16 | 1 | 41 | 1 |
| 17 | 3 | 42 | 1 |
| | | 45 | 2 |
| | | 46 | 1 |

- Exactly 3 groups: **16/83**.
- A multiple of 3: **54/83**.
- Shorter than 3: **1/83**, the span `406.076?`, `071.078` on Ia5.

Placement null (strokes free to move): 0 of 2000 trials had 16 or more length-3 spans, and 0 of 2000 had 54 or more multiples of 3. 1 of 2000 had as few as one span shorter than 3. So lengths really do prefer multiples of 3, and very short spans are scarce. The typical span is still longer than one triad (median 9). “Almost every division is one triad” does not hold. “A division is never shorter than three glyphs” is false on this transcription: one span has two groups.

### Where 076 sits inside a span

Among the 83 interior spans:

| Claim | Count | Content null |
| --- | ---: | --- |
| First group contains 076 | 79/83 | 0/2000 shuffles this high |
| First group is an `X.076` suffix | 73/83 | 0/2000 |
| 076 only in the first group, and the span has length 3 | 16/16 of the length-3 spans | 0/2000 |
| Last group contains 076 | 5/83 | 0/2000 shuffles this low |
| Penultimate group contains 076 | 4/83 | 0/2000 this low |
| Antepenultimate group contains 076 | 67/82 spans long enough | 0/2000 this high |
| Groups at offsets 0, 3, 6, … contain 076 | 218/378 (57.7%) | 0/2000 this high |
| Groups at the other offsets contain 076 | 153/718 (21.3%) | 0/2000 this low |

The length-3 subset is uniform: 076 is in the first group and absent from the other two. 15 of those 16 first groups are true suffixes. The exception is a bare `076` on Ia9 (`076`, `092f`, `535s`).

The positional bias survives. The universal wording does not. Four spans do not open on 076. Five end on a group that contains 076 (`076`, `076`, `076.073?`, `076f`, `020.010.076`). “Nearly every” 1st, 4th, 7th group bears 076 is too strong for a 57.7% rate.

On the Staff as a whole, groups that contain 076 break down as 481 suffixes, 61 bare, 8 with 076 first, and 10 with 076 in the middle (560 groups; the 564 stem hits include a few groups with more than one 076).

### The quoted bird / fish / sun order

`606.076, 700, 008` occurs once, on Ia12 at group index 55. It sits inside an interior span of 45 groups, so the vertical lines do not cut it out as its own triad. The sign order matches the sequence Fischer quotes. The reading “all the birds copulated with the fish: there issued forth the sun” stays his **hypothesis**.

### The same 200 X Y.076 triple on the Staff

Five isolated triples, and no handoff:

| Line | Groups |
| --- | --- |
| Ia3 | `200` `690.090` `129.076` |
| Ia8 | `200f` `023` `440.076` |
| Ia11 | `200` `726` `571.076` |
| Ia12 | `200?` `380.061x` `002V:076` |
| Ia14 | `200` `700` `071.076` |

`200f` and `200?` collapse to stem 200 under the existing stemmer. A shuffle of the Staff produces at least five such triples in **185 of 2000** trials. The triple is not a Staff grammar. The Gv6 result is the handoff, which this text does not have.

Inside the 16 length-3 spans, the host beside 076 has 15 types in 16 tokens, the middle group 14 types, and the last group 14 types. Those slots are diverse next to a sign that is present in every first group. Diversity is compatible with open name slots and also with any open class. It is not itself a reading.

## What survives

| Claim | Result | Confidence |
| --- | --- | --- |
| Gv6 is a shift-register of 4 phrases and 3 handoffs | Survives the line shuffle (0/5000) and the verso shuffle (0/2000) | High for this one locus. It is not a rule on Gr or on I |
| 200 and final 076 are the closed slots of that fragment; the other stems are open, and one of them is the illegible code 000 | Survives inside the four phrases (type/token 4/4 on each open slot) | High inside the fragment, no wider attestation |
| “X begat Y,” 076 = *ure* / son-of, 200 = *ko* | Not tested. Cited **hypothesis** | The handoff fits the hypothesis. The words are not a result of this track |
| A pure 999 is followed by a 076-bearing group | 91/96, 0/2000 content shuffles | High as a bracket. Does not decide divider vs logogram |
| Interior spans prefer multiples of 3, and length 3 is enriched | 54/83 and 16/83, both 0/2000 placement shuffles | The tendency survives. “Most spans are one triad” does not (median 9) |
| Every length-3 interior span is (076 in group 1 only) | 16/16, 0/2000 | High for that subset |
| 076 is scarce at the end and in penultimate position | 5/83 and 4/83, both 0/2000 for a count that low | The scarcity survives. “Never” is false |
| Spans are never shorter than 3 | False: one span has length 2. Spans that short are scarce (1/2000) | Universal fails; scarcity is a tendency |
| Offsets 0, 3, 6, … bear 076 “nearly every” time | 218/378 against 153/718 elsewhere, 0/2000 | Bias survives. “Nearly every” does not |
| Six names, or a Staff-wide 200 X Y.076 grammar | Five 200…076 entries on Gv6, not six. Five Staff triples, 0 handoffs, 185/2000 shuffles | These counts do not hold |
| Fischer’s phonetic triad, including the bird/fish/sun sentence | The sign order `606.076, 700, 008` is on Ia12. The sentence is untested | **Hypothesis** |

## Hooks other tracks can use

These are segmentation rules, not meanings. Status is what the counts support.

1. **`I-999-break` (candidate).** On text I, split a line at a group whose stem tuple is exactly `(999,)`, including `999h` and `999t`. Leave `999.440.076` as one group. Do not treat 999 as an ordinary lexical type when the question is about words. Do not confuse it with `000!`.
2. **`I-999-076-bracket` (candidate).** The group after a pure 999 usually contains 076 (91/96). Mark that pair as a bracket. Do not require the following span to be three groups long.
3. **`I-span-multiple-of-3` (tendency).** Span lengths fall on multiples of 3 more often than chance. A span of length 3 can be segmented as one (X with 076, Y, Z) unit: all 16 such spans have that shape. Longer spans are the common case (median 9). Do not force every span into a single triad.
4. **`Gv6-200-X-Y076` (candidate, Gv6 only).** Cut the four phrases in the table above. Closed slots: 200, and 076 at the end of the third group. Open slots: the middle group, and the host of 076. The host of phrase *n* is the middle group of phrase *n*+1. Keep both the suffix cut and Davletshin’s prefix cut on the table; the handoff is the same. Do not apply this cut to Gr or to the Staff.
5. **`I-200-X-Y076` (withheld).** The Staff’s five 200 X Y.076 triples have no handoff, and a shuffle reaches that count often (185 of 2000). They are not a phrase rule.

## Sources

- Butinov, N. A., and Yu. V. Knorozov. 1956. Preliminary report on the written language of Easter Island. *Sovetskaya etnografiya*. Cited here through Davletshin 2012; the issue number is not re-derived in this repo.
- Davletshin, Albert. 2012. “Name in the Kohau Rongorongo script (Easter Island).” *Journal de la Société des Océanistes* 134:95–110. doi:10.4000/jso.6658.
- Fischer, Steven Roger. 1995. “Further Evidence for Cosmogonic Texts in the Rongorongo Inscriptions of Easter Island.” *Rapa Nui Journal* 9(4), December 1995.
- Fischer, Steven Roger. 1997. *Rongorongo, the Easter Island Script: History, Traditions, Texts*. Oxford: Oxford University Press.
- Guy, Jacques B. M. 1998. “Easter Island — Does the Santiago Staff Bear a Cosmogonic Text?” *Anthropos* 93:552–555.
- Guy, Jacques B. M. 2003. “Some Observations Drawn from the Putative Genealogy of Tablet G.” *Rapa Nui Journal* 17(1).
- Horley, Paul. 2011. “Paleographic analysis of the Santiago Staff.” *Rapa Nui Journal* 25(1):31–43. Line order of the vendored `Ia.html`.
- Kohaumotu / C.E.I.P.P. Digitized corpus, including the 999 = vertical stroke note: `http://kohaumotu.org/rongorongo_org/corpus/digit.html`. Genealogy illustration: `http://kohaumotu.org/rongorongo_org/rosetta/g.html`.
- Barthel, Thomas S. 1958. *Grundlagen zur Entzifferung der Osterinselschrift*. Hamburg: Cram, de Gruyter. Numerical sign list used by the transcription.
