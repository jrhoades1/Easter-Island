# Round 6, Track A — pre-registration for a higher-resolution scan

This file is the plan. It was written before any higher-resolution image was opened. The twelve disagreements are the ones already logged in Round 5B. Each alternative sign code below is one of those logged codes, a Guy 1990 replacement already written down in Round 3, or a Pozdniakov 1996 rewrite already written down in the allograph notes. A later verdict selects from that list. The script then recomputes the headline counts. It does not invent a Barthel number, it does not edit the vendored transcription, and it does not assign a reading.

Provider: `MockProvider`. Provider calls: 0. `reading` is null.

The machine-readable copy is `data/decipherment/round6a_preregistration.json`. The program is `decipherment/round6a_preregistration.py`.

## Which images can decide a logged row

The public INSCRIBE models, as already listed in `docs/round4e_image_sources.md`, are tablets A (Tahua), B (Aruku Kurenga), C (Mamari), and D (Échancrée), plus downsampled meshes of M (Great Vienna) and N (Small Vienna). The viewer is [inscribercproject.com/Rongorongo.php](https://www.inscribercproject.com/Rongorongo.php). Those meshes were not opened for this file and are not stored in the repository. The viewer’s own terms keep the rights with the holders.

An INSCRIBE verdict may leave the Barthel code, or it may select a registered alternative, only when every tablet named in that disagreement is one of A, B, C, D, M, and N. Four of the twelve rows are on Mamari (C): D01, D02, D03, and D04. The other eight are on G, H, I, P, or Q. Those eight stay on the Barthel code for any verdict whose evidence is `inscribe`.

A, B, D, M, and N have a model and none of the twelve sites. A finding on those tablets is a new registration. It is not a choice under this file. M and N are the downsampled Vienna meshes.

## Headline counts, locked before any mesh is opened

These are the Round 5B figures, recomputed from the vendored Barthel pages with every disagreement left on its baseline code.

| Count | Value |
| --- | ---: |
| Calendar `040` | 28 |
| `040` before / after `152` | 13 / 13 |
| Gaps between delimiters | 2, 6, 3, 2, 5, 3, 5 |
| Full delimiters opening on `390` | 6 |
| Calendar `152` and `143` | 1 and 1 |
| Gv6 phrases / handoffs | 4 / 3 |
| Staff groups with `076` after a pure `999` | 91 of 96 |
| H/Q span, matches, mismatches | 125, 107, 16 |
| Bird substitutions in that stretch | 2 |
| Bird substitutions in the stored parallels | 18 |

Every registered alternative, taken one at a time, leaves the 28, the 13/13 split, the Staff 91 of 96, and the span of 125 where they are. The counts that can move are the delimiter gaps, the Gv6 handoff, the H/Q match count, and the bird substitutions.

## Counting rules the script uses

A delimiter opens on `390`. The rest of the eight-sign pattern is the one Round 3 already uses, and a full delimiter is one whose third stem is `378`. Guy’s `*690` keeps the asterisk. It is not catalog `690`, and it is not added to the opener set. Round 3 also printed the gaps that would remain if `*690` were treated as an opener. Those gaps are a different rule. This script does not use them.

An H/Q match is exact stem equality on the stored stem passage P001, Great Santiago `Hr2:36..Hr4:0` against Small St Petersburg `Qr2:0..Qr3:65`. That is the 125-sign span. A hand alternation of `006` with `064` does not count as a match.

A bird substitution is a cross-hundred pair in which both stems fall in 400–409 or 600–699. The corpus count walks every stem passage in `data/decipherment/substitution_classes.json`. The stretch count walks P001 only.

A Gv6 phrase is `200`, then a group that contains neither `200` nor `076`, then a group whose last stem is `076`. A handoff is the father stems of one phrase equaling the child stems of the next. The Staff count is a group whose only stem is `999`, then whether the next group contains `076`.

Same-sign edits are applied at the logged line and offset, in every stored passage that contains that stem. Passages other than P001 are reported when their match count moves. They are not the headline.

## The twelve disagreements

| Id | Where | Tablets | INSCRIBE can select an alternative | Second code, and who named it | Headline movement |
| --- | --- | --- | --- | --- | --- |
| D01 | Ca7, the group after `152` | C | yes | Guy 1990: `*690.041` | Delimiter gaps become 2, 6, 3, 7, 3, 5. Full delimiters 6 to 5. |
| D02 | Ca7, `044.040` | C | yes | Guy 1990: `078.040` | None |
| D03 | Ca7 and Ca8, two `041h` | C | the only code is `041` | None published | None |
| D04 | Ca7, path inside the first `378` | C | the path is not a sign | None published | None |
| D05 | Hr3 offset 37 | H | no | CEIPP vector label: `006` | H/Q matches 107 to 106. Mismatches 16 to 17. |
| D06 | Hr3 offsets 43–44 | H | no | CEIPP vector order: `042` then `006` | Matches 107 to 105 if Q stays in Barthel order. |
| D07 | Qr3 offsets 23–24 | Q | no | CEIPP vector order: `042` then `006` | Matches 107 to 105 if H stays in Barthel order. |
| D08 | Hr2:66 / Qr2:30 and Hr3:26 / Qr3:6 | H and Q | no | Pozdniakov 1996, at these two columns only: Q `400` to `600`, Q `407` to `607` | Matches 107 to 109. Stretch birds 2 to 0. Corpus birds 18 to 16. |
| D09 | Gv6, six suffix `076` groups | G | no | Davletshin 2012, as a regrouping: prefix each `076` to the next group | Phrases 4 to 0. Handoffs 3 to 0. |
| D10 | Staff, `999` and the next group | I | no | None. The unrecorded one-digit labels are not choices | None. Stays 91 of 96. |
| D11 | Pr2, two paths labeled `_` | P | no | None | None |
| D12 | Hr4 offset 71 | H | no | CEIPP vector label: `048` | None in the 125-sign span. |

### D01. The stack after 152

Barthel, in the vendored calendar fixture, writes `600.390.041`. The CEIPP outline shows `600` and `390` in one slot and crescent `041` in the next slot. The outline does not print a new number. Guy 1990 calls the stack one sign, `*690`, and says catalog `690` is a different sign. Round 3 recorded the group as `*690.041`. Horley 2011 and Pozdniakov do not renumber it in the sources already used.

Under Guy’s code the crescent total stays 28, and the split around `152` stays 13 / 13. The `390` inside the old group was the opener of the delimiter that sits just after `152`. With that opener gone, that delimiter drops out. The gap of 2 on one side of it and the gap of 5 on the other join into 7. The gap list becomes 2, 6, 3, 7, 3, 5. Full delimiters that open on `390` go from 6 to 5. Gv6, the Staff, the H/Q span, and the bird counts stay put. Pairing this choice with Guy’s `078.040` moves the same two calendar fields and nothing else.

### D02. The figure beside a crescent

Barthel writes `044.040`. Guy 1990 writes `078.040` and keeps the crescent. Round 5B says the outline fits either figure. Horley and Pozdniakov do not name a third number. The `040` stays, so the 28, the 13/13 split, and the gap list stay. No other headline moves.

### D03. The two small crescents

Both tokens are `041h`, one in a Ca7 delimiter and one in a Ca8 delimiter. They stem to `041`. Horley 2011 accounts for the two small superscript crescents and does not change the number. Guy 1990 treats delimiter crescents as distinct from night crescents. Pozdniakov does not renumber them in the sources already used. The outline calls them short crescents and does not print a second catalog number. The verdict list has one code, `041`.

### D04. The path inside the first 378

The vector edition traces a narrow path labeled `_` inside the first `378` on Ca7. It sits in that sign’s horizontal span. Barthel has no extra group there. No published correction inserts a sign at this slot. Fischer’s extra glyph at the start of line 7 is a different place, and the sources used here do not give it a number. It is not a choice. The verdict leaves the delimiter as it is.

### D05. The hand at Hr3 offset 37

The vendored text has `064` here, and the parallel column Qr3 offset 17 is `064` in the vendored text and in the vector labels. The vector label on H is `006?`. The choice is `006`. The question mark stays the edition’s uncertainty mark. Pozdniakov 1996 and Guy 2006 describe `006` and `064` as alternating hands, and neither source corrects this column. Exact equality is still the match rule, so the column stops matching. P001 matches go from 107 to 106, and mismatches from 16 to 17. The signs are hands, so the bird counts stay. The same H stem also sits in the shorter H–P passage P007 (`Hr3:15-57`), where the match count goes from 38 to 37. That passage is not the headline span. The Round 2 map of every isolated `064` to `006` is not applied to any other sign.

### D06 and D07. The stacked pair, and the order on each side

Vendored H at Hr3 offsets 43–44 is `006` then `042`. Vendored Q at Qr3 offsets 23–24 is the same pair in the same order. Both vector editions list `042` then `006`. No published correction deletes a stem. Guy 1982 and Pozdniakov 1996 read a stack from the bottom. The allograph note records that convention and does not reorder, and this recheck did not record which outline is the lower one, so the convention is not a third sequence. Guy’s equation of glyph 42 with glyph 40 is the pair on Br1. It is not this pair.

Flipping only H, or only Q, turns the two P001 matches into mismatches: matches 107 to 105, mismatches 16 to 18. Flipping both sides leaves both columns matched. The headline returns to 107 and 16. The shorter passages that contain one side still move: H’s pair is also in H–P passage P007 (matches 38 to 37), and Q’s pair is also in P–Q passage P020 (matches 26 to 25).

### D08. The two bird columns

Barthel and the CEIPP labels agree: H `600` opposite Q `400`, and H `607` opposite Q `407`. The uncertainty mark on `400!` strips to `400`. Guy 2006 classes series 400–409 with series 600–699 as birds. That class is the counting rule. It does not rename a sign. Pozdniakov and Pozdniakov 2007 still list `400` apart from `600`.

Pozdniakov 1996 treats series 400 as variants of series 600. The allograph note records that as a hundreds rewrite (Pozdniakov 1996: 297). Here it is applied only at the two logged columns: Qr2:30 `400` becomes `600`, and Qr3:6 `407` becomes `607`. Other 400-series signs stay as coded. Those two columns become matches, so P001 matches go from 107 to 109 and mismatches from 16 to 14. The hundreds digits now agree, so the stretch bird count goes from 2 to 0 and the corpus bird count from 18 to 16. A corpus-wide hundreds rewrite remains the Round 2 inventory test. It is not rerun.

Taking D05, D06, and this choice together touches three different columns. The match changes add: −1, −2, and +2, so the headline match count is 106. The bird counts follow D08 alone.

### D09. Where 076 sits on Gv6

The vendored line has six groups that end in `076`. The outlines overlap the previous sign and leave a gap before the next sign. Four of the six are the closing groups of the `200 X Y.076` phrases. Guy and Horley do not renumber them in the Round 5B sources. The baseline keeps the suffix, and the four phrases and three handoffs stay.

Davletshin 2012 says `076` may be read as opening the next name even though the drawing attaches it to the previous sign. The registered counterfactual moves each of the six suffix `076`s onto the following group. The numbers stay `076`. Phrases go from 4 to 0, and handoffs from 3 to 0. The regrouping assigns no word. Tablet G is outside the INSCRIBE set, so evidence `inscribe` cannot select it.

### D10. The Staff bars

The census is 97 codes `999`, 96 of them a bar by itself, and 91 of those 96 followed by a group that contains `076`. The outlines coded `999` are narrow strokes. On Ia5 (`021:290.076`) and on Ia8 and Ia13 (`021:090.076`) the vector order inside the ligature differs from the vendored colon, and `076` is still in the group. The other order was not stored sign by sign, so it is not a second code. A few further labels differ by a digit. Those digits were not written down. A verdict cannot supply them. Horley, Pozdniakov, and Guy do not publish a replacement list for these bars in the sources already used. The rate stays 91 of 96.

### D11. Two paths on Pr2

Each path labeled `_` sits inside `202` or `306`. Neither opens a slot. No published correction inserts a number. The verdict does not add a token. The H/Q span is a passage between H and Q, and the bird count is unchanged because no column changes.

### D12. Hr4 offset 71

The vendored code is `042`. The vector label is `048`. The 125-sign stretch ends at Hr4 offset 0, so this stem is outside it. Headline matches, mismatches, and bird counts stay. The same stem is a column in the shorter H–Q passage P015 (`Hr4:61..Hr5:15` against `Qr4:24-58`), where Q already has `048`. Adopting `048` on H turns that column from a mismatch into a match: P015 matches go from 30 to 31. P015 is not the headline span. Horley’s suggestion that `049` be read as `048` is a different sign and is not applied.

## How a verdict is filled in

A verdict is a JSON object:

```json
{
  "provider": "MockProvider",
  "evidence": "inscribe",
  "choices": {
    "D01": "guy_1990_star690"
  }
}
```

Omitted ids keep the baseline code. `evidence` is one of:

| Evidence | What it may select |
| --- | --- |
| `inscribe` | A non-baseline code only on D01–D04. Any other non-baseline choice is rejected. |
| `counterfactual` | Any registered choice. This is how the deltas in this file were computed. It is not a claim that a mesh was seen. |
| `later_image` | Any registered choice, and `image_note` must name the image source. The script does not fetch that source. |

The command is:

```bash
python -m decipherment.round6a_preregistration --verdict path/to/verdict.json
```

The script prints the recomputed headline bundle, the fields that moved, and any non-headline passage whose match count moved. It writes nothing into the Barthel pages. `readings_assigned` is false.

## What this plan refuses

A verdict code has to be one of the ids in the JSON. A new digit, a new insertion, or a corpus-wide merge is a different study. The opener list stays `390`. The bird class stays the series rule already used for the count of 18. No night name, no personal name, and no syllable is written onto a sign.
