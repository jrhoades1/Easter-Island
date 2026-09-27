# Round 2, Track C — Parallel passages and substitution classes

This note finds repeated passages across tablets and the sign substitutions inside them. It assigns no readings. The provider is MockProvider and is never asked for a completion. Counts below are produced by `decipherment/track_c_parallels.py` from the vendored Kohaumotu Barthel HTML.

## Corpus and encoding

The loader is `load_located_sides`. Sides with no digit transcription are omitted (36 sides, 14488 stem tokens, 630 stem types). A tablet is the first letter of the side code, so Hr and Hv are one tablet and are not aligned to each other. Lines of one side are concatenated. A line name such as `Hr8` is the Kohaumotu line number. Offsets are 0-based and inclusive, the same convention as the H/P/Q scoreboards. The end offset in a same-line locus is inclusive.

The primary encoding is `stem`: ligatures written with `.` or `:` are split, allograph letters and a leading orientation `V` are stripped, and illegible `000` is dropped. That is ligature decomposition. The option `ligature_atomic` keeps each dot or colon ligature as one sign. The merge table other tracks should consume is the stem table.

| Side | Tablet | Stems | Lines | Fixture |
| --- | --- | ---: | ---: | --- |
| Aa | A | 900 | 8 | `tests/fixtures/tahua_aa_html/Aa.html` |
| Ab | A | 921 | 8 | `tests/fixtures/tahua_ab_html/Ab.html` |
| Br | B | 557 | 10 | `tests/fixtures/aruku_br_html/Br.html` |
| Bv | B | 732 | 12 | `tests/fixtures/aruku_bv_html/Bv.html` |
| Ca | C | 512 | 14 | `tests/fixtures/mamari_ca_html/Ca.html` |
| Cb | C | 473 | 14 | `tests/fixtures/mamari_cb_html/Cb.html` |
| Da | D | 137 | 7 | `tests/fixtures/echancree_da_html/Da.html` |
| Db | D | 103 | 6 | `tests/fixtures/echancree_db_html/Db.html` |
| Er | E | 458 | 9 | `tests/fixtures/keiti_er_html/Er.html` |
| Ev | E | 422 | 8 | `tests/fixtures/keiti_ev_html/Ev.html` |
| Fa | F | 36 | 5 | `tests/fixtures/chauvet_fa_html/Fa.html` |
| Fb | F | 9 | 3 | `tests/fixtures/chauvet_fb_html/Fb.html` |
| Gr | G | 351 | 8 | `tests/fixtures/small_santiago_gr_html/Gr.html` |
| Gv | G | 353 | 8 | `tests/fixtures/small_santiago_gv_html/Gv.html` |
| Hr | H | 770 | 12 | `tests/fixtures/large_santiago_hr_html/Hr.html` |
| Hv | H | 826 | 12 | `tests/fixtures/large_santiago_hv_html/Hv.html` |
| Ia | I | 2431 | 14 | `tests/fixtures/santiago_ia_html/Ia.html` |
| Ja | J | 2 | 1 | `tests/fixtures/reimiro_ja_html/Ja.html` |
| Kr | K | 121 | 5 | `tests/fixtures/small_london_kr_html/Kr.html` |
| Kv | K | 94 | 5 | `tests/fixtures/small_london_kv_html/Kv.html` |
| La | L | 51 | 1 | `tests/fixtures/reimiro_la_html/La.html` |
| Ma | M | 48 | 6 | `tests/fixtures/vienna_ma_html/Ma.html` |
| Na | N | 140 | 5 | `tests/fixtures/vienna_na_html/Na.html` |
| Nb | N | 94 | 5 | `tests/fixtures/vienna_nb_html/Nb.html` |
| Oa | O | 92 | 7 | `tests/fixtures/boomerang_oa_html/Oa.html` |
| Pr | P | 823 | 11 | `tests/fixtures/large_st_petersburg_pr_html/Pr.html` |
| Pv | P | 735 | 11 | `tests/fixtures/large_st_petersburg_pv_html/Pv.html` |
| Qr | Q | 495 | 9 | `tests/fixtures/small_st_petersburg_qr_html/Qr.html` |
| Qv | Q | 401 | 9 | `tests/fixtures/small_st_petersburg_qv_html/Qv.html` |
| Ra | R | 249 | 8 | `tests/fixtures/atua_ra_html/Ra.html` |
| Rb | R | 207 | 8 | `tests/fixtures/atua_rb_html/Rb.html` |
| Sa | S | 365 | 8 | `tests/fixtures/washington_sa_html/Sa.html` |
| Sb | S | 384 | 8 | `tests/fixtures/washington_sb_html/Sb.html` |
| Ta | T | 146 | 9 | `tests/fixtures/honolulu_ta_html/Ta.html` |
| Ua | U | 24 | 2 | `tests/fixtures/honolulu_ua_html/Ua.html` |
| Va | V | 26 | 1 | `tests/fixtures/honolulu_va_html/Va.html` |

## Matching

Seeds are exact stem 3-mers. Seeds on one diagonal band are chained when the gap is at most 18 signs. Each chain is extended by Smith-Waterman (Smith and Waterman 1981) with match +2, mismatch −1, and a linear gap −1. One trace can hold two exact islands separated by a looser stretch. Every maximal subpath that still clears the gates is kept, so the islands are not dropped with the stretch. A repetitive 3-mer, one that occurs more than 30 times on the target side, is seeded on every third query position so a run cannot explode the hit list. Nearby gated hits on the same sides are joined and realigned when the gap is at most 12 signs and the two gap lengths differ by at most 8.

A passage is kept when the longer copy covers at least 8 stems, identity is at least 0.80, and both end columns are matches. Identity is matches divided by columns (matches, mismatches, and gaps). This is the same 20% error budget Sproat (2003) used, with two differences: Sproat also required the last two glyphs to match, and he searched fixed lengths from a suffix array (Manber and Myers 1993) with the edit distance in Sankoff and Kruskal (1983). This search uses local alignment and lets the length fall out of the path.

The null shuffles signs inside each side (24 trials, seed 0) and reruns the same search. Each side keeps its inventory and its length. The threshold is the best score seen in any trial. A passage is significant when its score is higher than that maximum. Here the null maximum is 0 and the null median is 0. Null trial maxima: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.

Gated passages: 99. Significant passages: 99.

## Passages

H in this corpus is the Great Santiago tablet, P is the Great St. Petersburg tablet, and Q is the Small St. Petersburg tablet. Small Santiago is G. The long parallel discussed as the Great Tradition is H/P/Q. G parallels London K.

| Id | Tablets | Loci | Span | Identity | Score | Mismatches | Gaps | Status |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| P001 | H–Q | Hr2:36..Hr4:0 ‖ Qr2:0..Qr3:65 | 125 | 0.8492 | 195 | 16 | 3 | published |
| P002 | G–K | Gr5:39..Gr7:16 ‖ Kv2:3..Kv4:23 | 76 | 0.8228 | 116 | 7 | 7 | published |
| P003 | H–P | Hr5:0-65 ‖ Pr4:66..Pr5:39 | 69 | 0.8028 | 100 | 7 | 7 | published |
| P004 | H–Q | Hr6:32..Hr7:11 ‖ Qr6:0-49 | 52 | 0.8077 | 74 | 8 | 2 | published |
| P005 | H–P | Hr1:51..Hr2:34 ‖ Pr1:45..Pr2:24 | 50 | 0.8000 | 70 | 6 | 4 | published |
| P006 | P–Q | Pv3:1..Pv4:0 ‖ Qv3:40..Qv4:29 | 47 | 0.8298 | 70 | 7 | 1 | published |
| P007 | H–P | Hr3:15-57 ‖ Pr3:2-48 | 47 | 0.8085 | 67 | 5 | 4 | published |
| P008 | H–P | Hv7:26-72 ‖ Pv8:69..Pv9:26 | 47 | 0.8085 | 67 | 7 | 2 | published |
| P009 | H–P | Hr1:0-45 ‖ Pr1:1-45 | 46 | 0.8043 | 65 | 8 | 1 | published |
| P010 | G–K | Gr2:2..Gr3:6 ‖ Kr2:14..Kr3:27 | 45 | 0.8000 | 63 | 7 | 2 | published |
| P011 | H–Q | Hr9:15..Hr10:5 ‖ Qr9:9-53 | 45 | 0.8000 | 63 | 8 | 1 | published |
| P012 | P–Q | Pv4:38..Pv5:3 ‖ Qv5:0-38 | 39 | 0.8250 | 59 | 4 | 3 | published |
| P013 | G–K | Gr3:23..Gr4:23 ‖ Kr4:8..Kr5:19 | 41 | 0.8049 | 58 | 3 | 5 | published |
| P014 | H–P | Hr6:49..Hr7:14 ‖ Pr6:14-50 | 38 | 0.8158 | 55 | 6 | 1 | published |
| P015 | H–Q | Hr4:61..Hr5:15 ‖ Qr4:24-58 | 37 | 0.8108 | 53 | 5 | 2 | published |
| P016 | H–P | Hv6:17-52 ‖ Pv7:80..Pv8:19 | 36 | 0.8056 | 51 | 5 | 2 | published |
| P017 | H–Q | Hv2:26-58 ‖ Qv5:5-40 | 36 | 0.8056 | 51 | 4 | 3 | published |
| P018 | H–P | Hr7:44..Hr8:12 ‖ Pr7:7-41 | 35 | 0.8000 | 49 | 6 | 1 | published |
| P019 | H–Q | Hr5:59..Hr6:4 ‖ Qr5:40-68 | 31 | 0.8125 | 46 | 2 | 4 | published |
| P020 | P–Q | Pr3:14-45 ‖ Qr3:7-34 | 32 | 0.8125 | 46 | 2 | 4 | published |
| P021 | H–Q | Hr5:24-53 ‖ Qr5:3-31 | 30 | 0.8065 | 44 | 3 | 3 | published |
| P022 | H–Q | Hr11:10-40 ‖ Qv2:15-44 | 31 | 0.8065 | 44 | 5 | 1 | published |
| P023 | P–Q | Pr7:10-40 ‖ Qr7:28-58 | 31 | 0.8065 | 44 | 6 | 0 | published |
| P024 | H–P | Hr4:41-65 ‖ Pr4:18-44 | 27 | 0.8148 | 39 | 3 | 2 | published |
| P025 | H–Q | Hr7:31-54 ‖ Qr7:10-35 | 26 | 0.8077 | 37 | 3 | 2 | published |
| P026 | H–P | Hr9:40..Hr10:9 ‖ Pr9:0-24 | 25 | 0.8000 | 35 | 3 | 2 | published |
| P027 | H–P | Hv2:24-48 ‖ Pv4:42-66 | 25 | 0.8000 | 35 | 5 | 0 | published |
| P028 | H–P | Hv9:53-77 ‖ Pv10:72..Pv11:16 | 25 | 0.8000 | 35 | 4 | 1 | published |
| P029 | P–Q | Pr5:9-32 ‖ Qr5:15-38 | 24 | 0.8000 | 35 | 3 | 2 | published |
| P030 | H–Q | Hr1:20-38 ‖ Qr1:0..Qr2:1 | 19 | 0.9000 | 34 | 0 | 2 | published |
| P031 | H–P | Hv3:34-54 ‖ Pv5:42-61 | 21 | 0.8571 | 33 | 2 | 1 | published |
| P032 | P–Q | Pv2:16-34 ‖ Qv3:1-21 | 21 | 0.8182 | 32 | 0 | 4 | published |
| P033 | H–P | Hr6:1-20 ‖ Pr5:66-83 | 20 | 0.8500 | 31 | 1 | 2 | published |
| P034 | H–P | Hr12:0-19 ‖ Pv1:22..Pv2:8 | 20 | 0.8500 | 31 | 1 | 2 | published |
| P035 | P–Q | Pr4:58-78 ‖ Qr4:39-56 | 21 | 0.8095 | 30 | 1 | 3 | published |
| P036 | P–Q | Pr5:29-48 ‖ Qr5:35-55 | 21 | 0.8095 | 30 | 3 | 1 | published |
| P037 | P–Q | Pr9:1-19 ‖ Qr9:35-52 | 19 | 0.8421 | 29 | 2 | 1 | published |
| P038 | H–Q | Hr7:57..Hr8:11 ‖ Qr7:39-58 | 20 | 0.8000 | 28 | 4 | 0 | published |
| P039 | H–P | Hv5:40-59 ‖ Pv7:24-43 | 20 | 0.8000 | 28 | 4 | 0 | published |
| P040 | H–P | Hv9:10-29 ‖ Pv10:36-53 | 20 | 0.8000 | 28 | 2 | 2 | published |
| P041 | B–H | Br10:18-33 ‖ Hr9:21-34 | 16 | 0.8750 | 26 | 0 | 2 | uncited |
| P042 | H–P | Hv4:35-50 ‖ Pv6:33-49 | 17 | 0.8235 | 25 | 2 | 1 | published |
| P043 | H–P | Hv10:40-55 ‖ Pv11:47-63 | 17 | 0.8235 | 25 | 2 | 1 | published |
| P044 | P–Q | Pr1:21-37 ‖ Qr1:1-16 | 17 | 0.8235 | 25 | 2 | 1 | published |
| P045 | B–Q | Br10:18-32 ‖ Qr9:15-27 | 15 | 0.8667 | 24 | 0 | 2 | uncited |
| P046 | G–K | Gr1:3-14 ‖ Kr1:0-11 | 12 | 1.0000 | 24 | 0 | 0 | published |
| P047 | H–Q | Hr4:41-56 ‖ Qr4:6-19 | 16 | 0.8125 | 23 | 1 | 2 | published |
| P048 | H–P | Hv6:63-76 ‖ Pv8:30-43 | 14 | 0.8571 | 22 | 2 | 0 | published |
| P049 | A–P | Aa1:30-42 ‖ Pr5:68-81 | 14 | 0.8000 | 21 | 0 | 3 | uncited |
| P050 | E–P | Er9:28-41 ‖ Pr1:0-13 | 14 | 0.8000 | 21 | 1 | 2 | uncited |
| P051 | H–P | Hr10:11-23 ‖ Pr9:26-40 | 15 | 0.8000 | 21 | 1 | 2 | published |
| P052 | H–P | Hv3:10-24 ‖ Pv5:18-32 | 15 | 0.8000 | 21 | 3 | 0 | published |
| P053 | H–P | Hv6:71..Hv7:6 ‖ Pv8:38-52 | 15 | 0.8000 | 21 | 3 | 0 | published |
| P054 | H–Q | Hv5:29-43 ‖ Qv8:0-14 | 15 | 0.8000 | 21 | 3 | 0 | published |
| P055 | P–Q | Pr6:29-43 ‖ Qr6:31-45 | 15 | 0.8000 | 21 | 3 | 0 | published |
| P056 | H–P | Hv10:6-16 ‖ Pv11:21-31 | 11 | 0.9091 | 19 | 1 | 0 | published |
| P057 | H–R | Hv12:42-52 ‖ Ra5:5-14 | 11 | 0.9091 | 19 | 0 | 1 | uncited |
| P058 | B–G | Bv8:18-28 ‖ Gr1:3-14 | 12 | 0.8333 | 18 | 1 | 1 | uncited |
| P059 | B–K | Bv8:20-28 ‖ Kr1:3-11 | 9 | 1.0000 | 18 | 0 | 0 | uncited |
| P060 | H–P | Hv8:0-11 ‖ Pv9:29-40 | 12 | 0.8333 | 18 | 2 | 0 | published |
| P061 | H–Q | Hv4:21-32 ‖ Qv7:0-11 | 12 | 0.8333 | 18 | 2 | 0 | published |
| P062 | H–Q | Hv4:49-60 ‖ Qv7:26-37 | 12 | 0.8333 | 18 | 2 | 0 | published |
| P063 | P–Q | Pr8:2-12 ‖ Qr8:6-17 | 12 | 0.8333 | 18 | 1 | 1 | published |
| P064 | B–G | Bv9:27-36 ‖ Gr1:1-10 | 10 | 0.9000 | 17 | 1 | 0 | uncited |
| P065 | C–E | Ca1:0-9 ‖ Er9:28-36 | 10 | 0.9000 | 17 | 0 | 1 | uncited |
| P066 | A–P | Aa1:66-76 ‖ Pr5:96..Pr6:1 | 11 | 0.8182 | 16 | 2 | 0 | uncited |
| P067 | A–H | Ab3:3-13 ‖ Hr3:39-49 | 11 | 0.8182 | 16 | 2 | 0 | uncited |
| P068 | A–Q | Ab3:3-13 ‖ Qr3:19-29 | 11 | 0.8182 | 16 | 2 | 0 | uncited |
| P069 | B–E | Bv11:13-23 ‖ Er4:36-46 | 11 | 0.8182 | 16 | 2 | 0 | uncited |
| P070 | B–K | Bv9:29-36 ‖ Kr1:0-7 | 8 | 1.0000 | 16 | 0 | 0 | uncited |
| P071 | E–H | Ev6:9-19 ‖ Hv12:42-51 | 11 | 0.8182 | 16 | 1 | 1 | uncited |
| P072 | E–R | Ev6:9-19 ‖ Ra5:5-13 | 11 | 0.8182 | 16 | 0 | 2 | uncited |
| P073 | H–P | Hr2:74..Hr3:8 ‖ Pr2:67-77 | 11 | 0.8182 | 16 | 2 | 0 | published |
| P074 | H–P | Hr3:66-76 ‖ Pr3:57-67 | 11 | 0.8182 | 16 | 2 | 0 | published |
| P075 | H–P | Hr6:22-32 ‖ Pr5:94-103 | 11 | 0.8182 | 16 | 1 | 1 | published |
| P076 | H–Q | Hr4:35-45 ‖ Qr4:0-10 | 11 | 0.8182 | 16 | 2 | 0 | published |
| P077 | P–Q | Pr3:57-67 ‖ Qr3:46-56 | 11 | 0.8182 | 16 | 2 | 0 | published |
| P078 | P–Q | Pv7:23-33 ‖ Qv8:10-20 | 11 | 0.8182 | 16 | 2 | 0 | published |
| P079 | H–Q | Hv3:20-28 ‖ Qv6:0-8 | 9 | 0.8889 | 15 | 1 | 0 | published |
| P080 | P–Q | Pr4:25-33 ‖ Qr4:11-19 | 9 | 0.8889 | 15 | 1 | 0 | published |
| P081 | A–H | Aa1:36-43 ‖ Hr6:11-20 | 10 | 0.8000 | 14 | 0 | 2 | uncited |
| P082 | A–H | Ab3:13-22 ‖ Hr3:53-61 | 10 | 0.8000 | 14 | 1 | 1 | uncited |
| P083 | A–Q | Ab3:13-22 ‖ Qr3:33-41 | 10 | 0.8000 | 14 | 1 | 1 | uncited |
| P084 | B–H | Bv12:13-21 ‖ Hv12:45-54 | 10 | 0.8000 | 14 | 1 | 1 | uncited |
| P085 | E–G | Ev4:0-8 ‖ Gr5:22-30 | 9 | 0.8000 | 14 | 0 | 2 | uncited |
| P086 | G–K | Gr4:9-17 ‖ Kv2:17..Kv3:1 | 10 | 0.8000 | 14 | 1 | 1 | published |
| P087 | G–K | Gr4:40..Gr5:5 ‖ Kv2:16-24 | 10 | 0.8000 | 14 | 1 | 1 | published |
| P088 | H–P | Hr2:44-53 ‖ Pr2:35-44 | 10 | 0.8000 | 14 | 2 | 0 | published |
| P089 | H–P | Hr10:37-46 ‖ Pr10:0-9 | 10 | 0.8000 | 14 | 2 | 0 | published |
| P090 | H–Q | Hr8:50-58 ‖ Qr8:15-24 | 10 | 0.8000 | 14 | 1 | 1 | published |
| P091 | H–P | Hv1:20-29 ‖ Pv4:3-12 | 10 | 0.8000 | 14 | 2 | 0 | published |
| P092 | H–P | Hv9:28-37 ‖ Pv10:52-60 | 10 | 0.8000 | 14 | 1 | 1 | published |
| P093 | P–Q | Pr2:33-42 ‖ Qr2:6-15 | 10 | 0.8000 | 14 | 2 | 0 | published |
| P094 | P–Q | Pr2:68-77 ‖ Qr2:39-48 | 10 | 0.8000 | 14 | 2 | 0 | published |
| P095 | P–Q | Pr6:15-24 ‖ Qr6:17-26 | 10 | 0.8000 | 14 | 2 | 0 | published |
| P096 | P–Q | Pv1:5-14 ‖ Qv2:37-45 | 10 | 0.8000 | 14 | 1 | 1 | published |
| P097 | A–H | Aa1:65-72 ‖ Hr6:24-31 | 8 | 0.8750 | 13 | 1 | 0 | uncited |
| P098 | B–R | Bv12:13-20 ‖ Ra5:8-14 | 8 | 0.8750 | 13 | 0 | 1 | uncited |
| P099 | G–R | Gr2:27-33 ‖ Ra5:8-15 | 8 | 0.8750 | 13 | 0 | 1 | uncited |

## Published parallels

Recovered published pairs: H–P, H–Q, P–Q, G–K. Named pairs with no significant passage on this stemming: A–R.

- **H–P** (32 significant): Kudrjavtsev 1949 collation of the Great Santiago (H) and Great St. Petersburg (P) tablets, as later editors use it (Barthel 1958: 151–157; Pozdniakov 1996; Horley 2007).
- **H–Q** (18 significant): Same three-tablet parallel; Sproat 2003 records a 125-glyph approximate match between Great Santiago recto and Small St. Petersburg recto.
- **P–Q** (19 significant): Kudrjavtsev 1949 on the two St. Petersburg tablets; Barthel 1958; Pozdniakov 1996; Davletshin 2017 uses P as the reference copy against H and Q.
- **G–K** (6 significant): Small Santiago (G) and London (K). Horley 2007 treats K as a copy of Gr. The vendored scoreboards lock an exact 17-stem share on Gr/Kr.
- **A–R** (0 significant): Horley 2007: a passage shared by Tahua (A) and Atua Mata Riri (R), found after recoding signs into glyph elements.

Significant pairs outside that named list, flagged here as uncited rather than as a claim of priority: A–H (4), A–P (2), A–Q (2), B–G (2), B–H (2), B–K (2), B–E (1), B–Q (1), B–R (1), C–E (1), E–G (1), E–H (1), E–P (1), E–R (1), G–R (1), H–R (1). Sproat (2003) already notes shorter matches between various tablets beyond the long H/P/Q and G/K blocks, without listing every pair in the synopsis this track uses.

Santiago Staff (I) has no significant cross-tablet passage. That agrees with Sproat (2003), who found the Staff isolated, and with Pozdniakov (1996: 299) as cited by Horley (2007).

P001 is that Sproat anchor on this transcription: Great Santiago recto line 2 at offset 36 (Hr2:36..Hr4:0) against Small St. Petersburg recto line 2 at offset 0 (Qr2:0..Qr3:65), span 125, identity 0.8492, score 195.

Horley's A–R passage used a glyph-element transcription. An absence under Barthel stems means this encoding did not keep a span of 8 at identity 0.80 above the null. It is not a claim that his parallel is absent in his own encoding.

## Substitution classes

Substitutions are mismatch columns in significant passages only. The pair is unordered. The null re-pairs only those mismatch columns (400 trials, seed 7). Matches stay matched. A shuffle of every column would create far more mismatches than an alignment that already had to be 80% identical, and that artificial rate sits above the substitution counts. The busiest pair in any trial reached 6. A pair is systematic when its count is at least 3 and (1 + null hits) / (trials + 1) is at most 1/100. Recurrent pairs meet the count and miss that probability. Doubles and hapaxes are the scribal-noise bins. A double can have a small per-pair null hit count and still stay out of the merge table, because the count gate is 3. Hapax pairs: 122.

Classes are the connected components of systematic pairs. The representative is the member with the higher corpus count; ties take the smaller stem string. The merge table maps every member to that representative. It is a candidate allograph or homophone table for other tracks. It is not a decipherment, and a wide class (8 or more members) is a warning that transitivity may have chained distinct values.

Pairs whose count also exceeds the busiest null pair: 400–600 (9), 002–021 (7). Pairs that clear the per-pair probability and do not exceed that busiest null count: 001–011 (6), 254–256 (6), 056–084 (5), 008–081 (4), 280–290 (4), 381–385 (3).

Hand pair 006/064: observed count 0, kind `absent`, in a systematic class: false. Barthel 006 and 064 are the hand pair this repository already records from Pozdniakov's parallel phrases. This track does not force that merge.

| Class | Representative | Members | Pair count | Wide |
| --- | --- | --- | ---: | --- |
| S01 | 600 | 400 600 | 9 | false |
| S02 | 002 | 002 021 | 7 | false |
| S03 | 001 | 001 011 | 6 | false |
| S04 | 254 | 254 256 | 6 | false |
| S05 | 084 | 056 084 | 5 | false |
| S06 | 008 | 008 081 | 4 | false |
| S07 | 280 | 280 290 | 4 | false |
| S08 | 381 | 381 385 | 3 | false |

| Signs | Count | Kind | Null (ge+1)/(trials+1) |
| --- | ---: | --- | --- |
| 400 600 | 9 | systematic | 1/401 |
| 002 021 | 7 | systematic | 1/401 |
| 001 011 | 6 | systematic | 1/401 |
| 254 256 | 6 | systematic | 1/401 |
| 056 084 | 5 | systematic | 2/401 |
| 045 046 | 4 | recurrent | 29/401 |
| 205 305 | 4 | recurrent | 53/401 |
| 600 605 | 4 | recurrent | 13/401 |
| 008 081 | 4 | systematic | 3/401 |
| 280 290 | 4 | systematic | 1/401 |
| 001 004 | 3 | recurrent | 10/401 |
| 048 049 | 3 | recurrent | 13/401 |
| 200 205 | 3 | recurrent | 9/401 |
| 381 386 | 3 | recurrent | 6/401 |
| 381 385 | 3 | systematic | 3/401 |
| 003 006 | 2 | double | 119/401 |
| 006 061 | 2 | double | 34/401 |
| 006 093 | 2 | double | 78/401 |
| 010 062 | 2 | double | 1/401 |
| 022 041 | 2 | double | 16/401 |
| 034 045 | 2 | double | 23/401 |
| 040 042 | 2 | double | 119/401 |
| 045 074 | 2 | double | 18/401 |
| 060 254 | 2 | double | 1/401 |
| 065 710 | 2 | double | 1/401 |
| 072 117 | 2 | double | 91/401 |
| 078 079 | 2 | double | 14/401 |
| 087 088 | 2 | double | 17/401 |
| 090 091 | 2 | double | 15/401 |
| 093 095 | 2 | double | 27/401 |
| 109 711 | 2 | double | 1/401 |
| 200 206 | 2 | double | 1/401 |
| 201 202 | 2 | double | 7/401 |
| 214 215 | 2 | double | 27/401 |
| 220 226 | 2 | double | 102/401 |
| 220 320 | 2 | double | 1/401 |
| 244 246 | 2 | double | 41/401 |
| 244 254 | 2 | double | 69/401 |
| 300 330 | 2 | double | 40/401 |
| 316 356 | 2 | double | 23/401 |
| 324 326 | 2 | double | 6/401 |
| 376 379 | 2 | double | 19/401 |
| 400 605 | 2 | double | 287/401 |
| 430 431 | 2 | double | 18/401 |
| 450 710 | 2 | double | 35/401 |
| 710 711 | 2 | double | 74/401 |
| 730 790 | 2 | double | 401/401 |

### Merge table

| From | To |
| --- | --- |
| 001 | 001 |
| 002 | 002 |
| 008 | 008 |
| 011 | 001 |
| 021 | 002 |
| 056 | 084 |
| 081 | 008 |
| 084 | 084 |
| 254 | 254 |
| 256 | 254 |
| 280 | 280 |
| 290 | 280 |
| 381 | 381 |
| 385 | 381 |
| 400 | 600 |
| 600 | 600 |

## Insertions and deletions

A gap with a neighbor on both sides is an optional sign relative to the other copy: the parallel continues without it. The pattern is the inserted sign plus those two neighbors. The null shuffles inserted signs across the observed neighbor pairs (400 trials, seed 11). The busiest pattern in any trial reached 3. Events: 128. Hapax patterns: 100. A pattern is systematic on the same count and probability gates as a substitution. That pattern is the distributional candidate for an optional particle, a determinative, or a boundary mark. This track does not choose among those functions.

| Sign | Left | Right | Count | Kind | Null |
| --- | --- | --- | ---: | --- | --- |
| 095 | 003 | 006 | 4 | systematic | 1/401 |
| 006 | 003 | 006 | 2 | double | 31/401 |
| 006 | 008 | 022 | 2 | double | 13/401 |
| 006 | 027 | 077 | 2 | double | 2/401 |
| 015 | 008 | 022 | 2 | double | 5/401 |
| 021 | 372 | 020 | 2 | double | 2/401 |
| 060 | 001 | 069 | 2 | double | 4/401 |
| 060 | 770 | 070 | 2 | double | 1/401 |
| 163 | 700 | 386 | 2 | double | 1/401 |
| 430 | 076 | 076 | 2 | double | 1/401 |
| 600 | 004 | 600 | 2 | double | 2/401 |
| 681 | 003 | 254 | 2 | double | 1/401 |
| 755 | 076 | 063 | 2 | double | 1/401 |

## Ligatures kept whole

`ligature_atomic` uses the same gates and 24 shuffle trials. Null maximum 0. Gated passages 55, significant 55. Recovered published pairs: H–P, H–Q, P–Q, G–K. Absent: A–R. Systematic ligature classes: 1 (S01 002 021). Those classes are not the merge table. A ligature that stays in one cell cannot show a component substitution.

## Sources

- Barthel, Thomas S. 1958. *Grundlagen zur Entzifferung der Osterinselschrift*. Hamburg: Cram, de Gruyter.
- Davletshin, Albert. 2017. “Allographs, Graphic Variants and Iconic Formulae in the Kohau Rongorongo Script of Rapa Nui (Easter Island).” *Journal of the Polynesian Society* 126.
- Horley, Paul. 2007. “Structural Analysis of Rongorongo Inscriptions.” *Rapa Nui Journal* 21(1).
- Kudrjavtsev, Boris. 1949. Cited by Davletshin 2017 for the St. Petersburg collation and a sign count on P and Q. The article title is not re-copied here.
- Pozdniakov, Konstantin. 1996. “Les bases du déchiffrement de l’écriture de l’île de Pâques.” *Journal de la Société des Océanistes* 103: 289–303.
- Manber, Udi, and Gene Myers. 1993. “Suffix Arrays: A New Method for On-Line String Searches.” *SIAM Journal on Computing* 22: 935–948. Sproat's index, not the index used here.
- Sankoff, David, and Joseph Kruskal, eds. 1983. *Time Warps, String Edits, and Macromolecules.* The edit-distance method Sproat cites.
- Smith, T. F., and M. S. Waterman. 1981. “Identification of Common Molecular Subsequences.” *Journal of Molecular Biology* 147: 195–197.
- Sproat, Richard. 2003. “Approximate String Matches in the rongorongo Corpus.” Archived at https://web.archive.org/web/20080517071219/http://compling.ai.uiuc.edu/rws/ror/ .

## What the classes are for

Other tracks can apply `merge_table` in `data/decipherment/substitution_classes.json` with `dict.get(sign, sign)`. Signs absent from the table stay themselves. The JSON also stores every systematic, recurrent, and double pair with counts and null hits, so a later track can refuse the transitive closure and use the edges alone.
