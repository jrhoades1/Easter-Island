# Round 6C: the MNHN Santiago 3D models, checked against the Round 6A pre-registration

The models are the official 3D models of the Museo Nacional de Historia Natural (MNHN), Santiago de Chile.
- Santiago Staff (I), `RN02_L_MK1`: **CC BY-NC-SA, credit MNHN**. Renders derived from it carry the same licence and are for non-commercial use only.
- Great Santiago (H), `058AR_H_MK1`: CC0.
- Small Santiago (G), `057AR`: CC0.

The raw models are not in the repository. This round used the Round 6A protocol unchanged, with evidence `later_image`. The verdict is in `data/decipherment/round6c_santiago_verdict.json` and the per-row record is in `data/decipherment/round6c_santiago_results.json`.

## Method
`decipherment/round6c_santiago/render.py` ray-casts each mesh headless with trimesh and embree. Tablets are rendered orthographically, face by face, along their principal axes. The Staff is unwrapped cylindrically in four segments. Each view gets:
- a texture render;
- a relief map (depth minus a broad blur);
- normal shading with no texture;
- raking light from six azimuths at 15° elevation.

`lines.py` builds a high-pass "incised" image from the float relief, normalized by local contrast. It also straightens the curved lines by cross-correlating column profiles. `strips.py` cuts the crops.

## Faces
H face A is the recto. Its damaged upper-left area matches Barthel's short lines Hr9–Hr12. The long run of dotted `003a` groups on Hr3 (groups 25–36) is visible in the third line from the bottom. The line below it shows no such run.

## Verdicts
| Id | Verdict | Kept |
| --- | --- | --- |
| D05, Hr3:37 `064`/`006` | undecidable | `064` |
| D06, Hr3:43–44 order | undecidable | `006` then `042` |
| D07 (Q) | not covered | baseline |
| D08, the Q bird columns | undecidable: the disputed codes are on Q, and this is a classification question | baseline |
| D09, Gv6 `076` | undecidable: the G mesh does not resolve the signs | suffix |
| D10, Staff | no registered alternative | 91 of 96 |
| D12, Hr4:71 `042`/`048` | undecidable | `042` |

Why: the H mesh has a vertex spacing of about 0.45 mm, and the signs are about 10 mm tall. Dots and gross outlines resolve. Hand and finger shapes, stack order and small strokes do not; see `figures/round6c/H_r3_fullres_mesh_limit.png`. I counted 8 dotted columns in the candidate Hr3 region, where 10 were expected. That leaves the group-level alignment uncertain, so no single sign is claimed as located. The texture adds no usable carving evidence.

## Headline
Unchanged: `python -m decipherment.round6a_preregistration --verdict data/decipherment/round6c_santiago_verdict.json` gives `headline_delta: {}`. The counts stay at 28, 13/13, Staff 91 of 96, and H/Q 125/107/16, with 2 and 18 bird substitutions.

## What would decide these
A full-resolution mesh (an H_MK1 or above for the Staff, and an undecimated G) or RTI photographs of Hr3, Hr4 and Gv6.
