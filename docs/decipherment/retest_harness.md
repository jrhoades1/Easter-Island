# Retest harness: headline tests on any transcription

The headline findings in [README.md](README.md) were computed on the Barthel/CEIPP codes in the vendored Kohaumotu pages. This harness reads the corpus from a transcription file instead. It re-runs every headline test with its existing shuffle null, then compares the result with the Barthel baseline. Later sources, such as the corrected INSCRIBE (Bologna) readings or the project's own image readings, only need to be written in the same file format.

The harness calls the existing round 1–6 functions and passes them lines from the file. It changes no test, statistic, seed, draw count or pre-registered decision rule. `MockProvider` is accepted and never called. There is no network access and no paid API.

## Commands

```
# Write the vendored Barthel/CEIPP corpus as a transcription file (committed)
python3 -m decipherment.transcription export --out data/decipherment/transcriptions/barthel_ceipp.csv

# Re-run every headline test on a file and compare it with the baseline
python3 -m decipherment.retest --transcription data/decipherment/transcriptions/barthel_ceipp.csv

# Synthetic variants: Pozdniakov's 400 -> 600 merge, or a partial corpus
python3 -m decipherment.transcription perturb --merge 400=600 --out /tmp/poz.csv
python3 -m decipherment.transcription perturb --tablets AMN --out /tmp/amn.csv
```

`retest` writes `results.json` and `comparison.md` to `data/decipherment/retest/<file stem>/`, which is git-ignored, or to `--out-dir`. It also prints the table. `--no-nulls` skips the shuffles and gives the counts in about a second; the full run takes about 35 seconds. The stored baseline is `data/decipherment/retest_baseline.json`. To rebuild it, run `--write-baseline`, which accepts only the Barthel file.

## File format

UTF-8 CSV, one row per sign, with a header row. Rows can come in any order. `position` and `slot` set the order.

| Column | Required | Meaning |
|---|---|---|
| `tablet` | yes | Barthel tablet letter (`A`–`Y`). It must equal the first letter of `side`. |
| `side` | yes | Side code as Barthel/CEIPP write it: `Aa`, `Br`, `Gv`, `Ia`, `Qr`. |
| `line` | yes | Line number on the side, as published. |
| `position` | yes | 0-based group position in the line. A group is one hyphen-separated Barthel token, either one sign or a ligature. Positions must run 0..n-1. |
| `slot` | no (0) | 0-based sign position inside the group. |
| `sign` | yes | Barthel sign number, digits only (`040`, `600`). Empty only for a lacuna mark that has no number. |
| `variant` | no | Allograph letters, such as `y` in `378y`, `h` in `041h`, or `V`. |
| `uncertainty` | no | Edition marks: `?` uncertain, `!` damaged, `*` editor's note, `…` broken edge. Empty when the reading is certain. |
| `join` | no | Joiner before this sign inside its group, `.` or `:`. Empty for slot 0. |
| `raw` | no | Exact source text of this sign. When present it is used as written. Otherwise the sign is written as `sign`+`variant`+`uncertainty`. |

The tests use stems: the sign number with the variant letters and marks removed, as in every round so far. `variant` and `uncertainty` are kept so that a later rule can use them, but they do not change any count today. The converter keeps `raw` so the baseline round-trips byte for byte. A new source can leave `raw` out.

## Tests

| Test | Counts | Null (existing code, seed, draws) | Lines needed |
|---|---|---|---|
| Mamari calendar | 28 × `040` in 101 stems, 13 before / 13 after `152`, `143` right before `152`, runs of 6 and 5 | kokore run shuffle, seed 0, 5000 (round 3B) | Ca6–Ca9 |
| Calendar delimiter gaps | `040` gaps 2,6,3,2,5,3,5; 6 full delimiters | none | Ca6–Ca9 |
| Gv6 handoff | 4 phrases, 3 handoffs (280, 730, 517) | Gv6 group shuffle, seed 0, 5000; whole-verso shuffle, seed 1, 2000 (track 3) | Gv6 (and all of Gv for the verso null) |
| Staff bar → `076` | 91 of 96 bare bars | bars fixed, groups shuffled, seed 0, 2000 (track 3) | Ia1–Ia14 |
| Staff `076` gaps | 564 × `076`, 550 gaps, 197 of length 3, 137 of length 4 | line shuffle, seed 0, 1000 (track 4) | Ia1–Ia14 |
| `076` ends its group | 393/408 on the Staff, 97/105 elsewhere | random slot, seed 5, 500 (round 2B) | any |
| Parallel passages | 99 passages above the null; 8 gated substitution pairs; `400`–`600` × 9 | within-side shuffle max score, seed 0, 24 (round 2C) | H, P, Q |
| H/Q headline span | span 125, 107 matches, 16 mismatches | none | Hr2–Hr4, Qr2–Qr3 |
| Bird swaps | 18 of 34 cross-hundred substitutions share a class, all bird; 18 on the stored alignment (round 6A) | class-label shuffle, seed 41, 500: 23/500 (round 4A) | H, P, Q |

The calendar window is set by Barthel group positions. It runs from Ca6 group 18 (stem 24, the `390.041 315y 041` delimiter) through Ca9 group 1, the same bounds as `tests/fixtures/mamari_ca6_ca9_barthel.json`. A source that splits groups differently needs that window checked first. The harness refuses the split if the window does not contain exactly one `152`.

The H/Q span and the round 6A bird count use the stored alignment in `substitution_classes.json`. Signs are read again from the new file at each (line, offset). If a line in the span changes length, the two loci are realigned with the same Smith–Waterman scorer, and the row says so. The parallel search and the round 4A bird test run again from scratch on the file.

## Status rules

- **holds (same):** every headline count and every null tally equals the baseline.
- **holds (changed):** a count moved, and each null still reaches the repository's adoption line (fraction ≤ 0.05, `ADOPT_FRACTION`). For the calendar, the 6-and-5 run pattern must also still be present.
- **breaks:** a count moved and a null no longer reaches 0.05.
- **changed (count only, no null):** a count with no shuffle null (the delimiter gaps and the H/Q span) moved.
- **not computable:** the lines, tablets or signs the test needs are missing. The row names them.
- **holds / inconclusive (partial corpus):** a corpus-wide test was run on a subset of tablets. Its counts are not comparable with the full corpus.

These labels describe how far a finding moves. They are not new decision rules. The bird row passes 0.05 on its own, but after the Round 5 Holm correction it does not (0.7186). See README.

## Results recorded when the harness was added

**Baseline.** The converted Barthel/CEIPP file reproduces every count and every null tally exactly, and matches `round6a_preregistration.headline_stats`. All nine rows read *holds (same)*.

**Pozdniakov merge (every `400` written as `600`).** The calendar, Gv6, Staff and `076` rows do not move. The H/Q span goes from 107 matches to 108 and from 16 mismatches to 15. The one `400`/`600` column in it is Qr2:30. The search now finds 103 passages above the null instead of 99. Gated substitution pairs drop from 8 to 7, because `400`–`600` disappears. The bird swaps drop from 18 of 34 to 7 of 24, and the label-shuffle null moves from 23/500 to 160/500, so the row breaks. That result is built in: the merge turns the commonest bird substitution into a match. On the stored alignment, 13 bird columns are lost and 2 are gained (`401` and `405` opposite a former `400`), so the count goes from 18 to 7.

**Partial corpus (A, M, N only).** The calendar, Gv6, Staff, parallel, H/Q and bird rows are not computable, and each row names the missing lines or tablets. The `076` row runs on 3 groups and is inconclusive.

Tests: `tests/test_retest_harness.py`.
