# Round 3, Track B — Barthel transcription audit, Mamari Ca6–Ca9

Track 1 counted 28 night-crescents (`040`) on Mamari, lines Ca6–Ca9, and 13 of them on each side of the unique `152`. Those counts, and every later rate that quotes them, are only as good as Barthel’s 1958 numbers. This note checks that passage against the openly licensed photograph of the tablet and against later published corrections. It does not translate the tablet. The provider is `MockProvider` and it is never called. Counts are locked by `tests/test_round3_trackb_transcription_audit.py`.

## Which tablet

Mamari (Barthel text C) is the tablet behind the calendar. The other candidates carry other results — Small Santiago G, the Gv6 handoff, and Great Santiago H, the 125-sign parallel — and they were left alone. A 6000×4000 Commons photograph of Small Santiago is a reproduction of the verso, not the wood. The calendar is the count the other rounds cite, and Mamari has a licensed photograph of the original.

## Images and licenses

| Image | Role | Kept in git? |
| --- | --- | --- |
| Wikimedia `File:Rongorongo_C-a_Mamari.jpg`, 2040×1424, SHA-256 `33c768be356f158f614c6181ca8d66c8542f6c6f871d16ca045eab2f5c2d51f1` | The independent photograph. CC BY-SA 3.0 and GFDL 1.2+, VRT ticket 2008061210011949. File: `data/images/mamari/rongorongo_c-a_mamari.jpg`. | Yes. Not under the repository MIT license. |
| Kohaumotu / CEIPP Barthel strips `Ca0601.png`–`Ca0903.png` and the Fischer strips beside them | The publication’s own drawings, 74 px tall. Non-profit redistribution only. | No. URLs and SHA-256 are in `data/images/mamari/manifest.json`. |
| Kohaumotu `repro/ca.jpg`, 980×630, SHA-256 `68fdff7e3e3f60533a7d43a6a5f5efcf3655424953dff5871db45d4d68f93a84` | Whole side a, same non-profit terms. | No. |

The dark region on the Commons plate measures 1862×1251 pixels, starting at (117, 68). The tablet is 290×196 mm (Kohaumotu; Wikipedia gives 29×19.5 cm). The pixel box has the same proportions within one percent, about 6.4 pixels per millimetre. That shows the frame is the tablet. It does not identify a Barthel number. A difference of a few millimetres between catalog allographs is a handful of pixels on a compressed halftone of a 1935 plate.

The parked image track (`GlyphProcessor`, cluster ids `G001`, `G002`, …) was not run on this plate. Those ids are not Barthel numbers, and the earlier scoreboards already refuse a `G00n`→Barthel map. Using the cataloger here would invent one.

## What the photograph resolves

Nothing at catalog precision. All 75 published tokens in the calendar slice are marked **illegible**. A sign that cannot be read off this plate is not given a new number.

Two later sources were checked as text, not as a second look at the wood.

**CEIPP / Kohaumotu, and the Fischer numeric page on the same site.** The Fischer codes at `fi_Ca.html`, fetched with the Barthel page, are the same strings as vendored `Ca.html` for lines 6 through 9. Zero code differences. That page is not an independent transcription. The three damage stars already locked in Track 1 (`041` / `041*`, `040` / `040*`, `385` / `385*`) still strip to the same stems.

**Jacques Guy, 1990**, “The lunar calendar of Tablet Mamari,” *JSO* 91: 135–149, [10.3406/jso.1990.2882](https://doi.org/10.3406/jso.1990.2882). The prose lists four departures from Barthel. The plates were not re-keyed; Persée did not serve the PDF, and the fixture already records that those plates are images. Unspecified “minor changes” from Guy 1985 are not applied, because the 1990 article does not list them.

**Paul Horley, 2011**, *JSO* 132, [10.4000/jso.6314](https://doi.org/10.4000/jso.6314). The abstract says the two small superscript crescents have a paleographic explanation and that the last two crescents are moonless nights inside a 30-night month. The article text was behind a bot wall. No Barthel number was changed from the abstract. The two Ca9 crescents stay `040`.

**Konstantin Pozdniakov.** No line transcription of Ca6–Ca9 that renumbers these tokens was in the open sources used here. His catalog is a different numbering system and is not applied.

**Fischer 1997, via the Wikipedia article “Rongorongo text C.”** That article says a distorted glyph was squeezed in at the start of recto line 7, is missing from Barthel, and does not appear in any photograph. Fischer’s suggestions for its shape are not copied in. A sign the photograph does not show is not inserted. The Kohaumotu Fischer codes, above, also do not add it.

## Line-by-line

The slice is the one Track 1 already uses: Ca6 from the first `390.041`, all of Ca7 and Ca8, and the first two stems of Ca9. Seventy-five tokens, 101 stems.

| Line | Tokens | Stems | Photograph | Adopted change | Left disputed |
| --- | ---: | ---: | --- | --- | --- |
| Ca6 | 11 | 16 | illegible | none | one `670` (token 3) |
| Ca7 | 32 | 43 | illegible | `044.040` → `078.040`; `600.390.041` → `*690.041` | three `670` (tokens 9, 18, and `670y` at 27) |
| Ca8 | 30 | 40 | illegible | none | three `670` (tokens 6, 14, 25) |
| Ca9 | 2 | 2 | illegible | none | none |

The other 66 tokens have no published code change in the sources above. “Unconfirmed” means that. It does not mean the photograph agrees.

| Line | Token | Barthel | Proposal | Source | In the corrected text? | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| Ca7 | 20 | `044.040` | `078.040` | Guy 1990, departure 2. Glyph 78 resembles this sign more than glyph 44. The crescent is not said to be removed. | Yes | Published. Photo illegible, so not confirmed on the wood. |
| Ca7 | 24 | `600.390.041` | `*690.041` | Guy 1990, departure 3. `600:390` is one sign, 600 with the lower limbs of 290 or 390. He asterisks `*690` because catalog 690 is a different sign (600 with a 200-series head). | Yes | Published, and Guy marks it as not the catalog sign. Photo illegible. |
| Ca6, Ca7, Ca8 | the seven `670` / `670y` | `670` | not one number | Guy 1990, departure 4. He writes V631B for these, and V671 once, in the group after the night he calls kokore ono. | No | The replacement is two shapes, and choosing which token is V671 uses his night alignment. The photograph does not decide. Left as Barthel `670`. |

`*690` is kept with Guy’s asterisk. It is not stemmed as catalog `690`, which already occurs on other tablets.

## What the measurements do

The corrected text is the Barthel slice with only the two adopted replacements. The seven `670`s stay `670`. No crescent is deleted to force Guy’s 12-before-`152` count.

| Measurement | Barthel, as in Track 1 | After the two adopted replacements |
| --- | --- | --- |
| Stems | 101 (16 + 43 + 40 + 2) | 100 (16 + 42 + 40 + 2) |
| `040` | 28 | 28 |
| `040` before / after `152`, inside the outer full delimiters | 13 / 13 | 13 / 13 |
| Guy’s published count for those same cuts | 12 / 13 | still not 12 / 13 |
| Gaps between delimiter windows | 2, 6, 3, 2, 5, 3, 5 | 2, 6, 3, 7, 3, 5 if the post-`152` group must still open with `390` |
| Same gaps, first sign `390` or `*690` | 2, 6, 3, 2, 5, 3, 5 | 2, 6, 3, 2, 5, 3, 5 |
| Maximal `040` runs before / after `152` | 1, 1, 6, 1, 1, 1, 2 / 5, 2, 1, 5, 2 | unchanged |
| Full 8-sign delimiters opening `390` | 6 | 5 |
| Same, opening `390` or `*690` | 6 | 6 |
| Shuffle of the passage, seed 0, 5000 draws, 6-run before `152` and 5-run after | 0 | 1 |
| 2×2 crescent rate, numerator / denominator | 2376887638931856 / 3323951482720 | 2378200559616000 / 3290817024000 |
| `044` / `078` / `600` / `390` / `*690` in the slice | 1 / 7 / 2 / 8 / 0 | 0 / 8 / 1 / 7 / 1 |
| `040` outside the calendar (corpus 152 minus the 28) | 124 | 124 |

The gap 7 is the old gap 2 joined to the old gap 5, because the group after `152` no longer opens with `390`. The crescents in those gaps are still there. Their sum is still 26. Treating `*690` as a variant first sign keeps all eight separators and the original gaps.

The chi-square moves because the slice loses one non-crescent stem (`600` and `390` become one `*690`), not because a `040` moved. It is still the Track 1 rate comparison. Stems are not independent. The shuffle is the order test. One draw in 5000 still shows the 6-before / 5-after pattern; the Barthel text showed none. The pattern does not become common.

Round 2’s outside-calendar crescent count is 124 because the calendar holds 28 of 152. Both of those are unchanged, so that crib’s crescent totals do not move. Gv6 and the H/Q 125-sign parallel were not on this tablet. They were not remeasured.

## What this does not say

Barthel’s crescent count survives the two corrections that name a single group and do not ask the photograph for a number it cannot show. That is not a certificate that every unconfirmed code is right. Sixty-six tokens are simply undisputed in the sources read here, and illegible on the plate. Guy’s `670` replacements are real disagreements and were not forced into one stem. Horley’s superscript crescents, and the missing glyph reported from Fischer 1997, did not become code changes. No night name is attached to a sign.
