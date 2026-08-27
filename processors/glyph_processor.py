"""Computer vision processor for Rongorongo glyph detection and analysis."""

import os
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

import cv2
import numpy as np
from sklearn.cluster import DBSCAN

from models.glyphs import (
    BoundingBox,
    GlyphCluster,
    GlyphInstance,
    GlyphPosition,
    PositionStats,
)


@dataclass
class ProcessorConfig:
    """Configuration for the glyph processor."""

    # Preprocessing
    blur_kernel_size: int = 5
    adaptive_block_size: int = 11
    adaptive_c: int = 2

    # Contour filtering
    min_contour_area: int = 100
    max_contour_area: int = 50000
    min_aspect_ratio: float = 0.2
    max_aspect_ratio: float = 5.0

    # Bounding box
    bbox_padding: int = 5

    # Line detection
    line_merge_threshold: int = 20  # Vertical distance to merge into same line

    # Feature extraction
    target_glyph_size: tuple[int, int] = (64, 64)
    # "unsigned": abs of signed log-Hu so Hu5–Hu7 sign-flips do not split types.
    # "signed": cycle-1 path (−sign(h)·log10(|h|)). Detection is unchanged either way.
    hu_sign_mode: str = "unsigned"

    # Clustering
    dbscan_eps: float = 0.5
    dbscan_min_samples: int = 2

    # Same-line allograph stitch after DBSCAN. Unsigned crescent diameter is
    # ~3.41; stock eps=0.5 does not reach it. Same-line *any* pair at that
    # distance over-collapses (~65→29 types). Adjacent + area + tall-thin
    # keeps the opening crescents together without merging wide figures.
    same_line_allograph_merge: bool = True
    allograph_max_hu_distance: float = 3.5
    allograph_max_area_ratio: float = 1.1
    allograph_max_aspect: float = 0.5

    # Detection-time split of wide connected blobs. Inner RETR_TREE contours
    # on these GIFs are holes, not stems. A vertical ink-projection valley
    # is the honest cut: only boxes much wider than a tall-thin stem, and
    # only when a deep interior valley exists. Tall-thin crescents (aspect
    # ~0.4) never meet ligature_min_aspect. Set False for the cycle-3 lock.
    split_wide_ligatures: bool = True
    ligature_min_width: int = 70  # ~2.7× opening-crescent width (~26px)
    ligature_min_aspect: float = 0.90
    ligature_valley_ratio: float = 0.40  # valley < ratio × median column ink
    ligature_min_part_width: int = 12
    ligature_max_parts: int = 3  # Barthel 8.78.711 is three stems

    # Cross-image stitch of valley-split fragments after the tall-thin
    # same-line pass. Hu<2.0 and area ratio ~1 also match 34px vs 31px
    # parts from different slots of the same 3-part split; width ratio
    # 1.08 keeps those slots apart. Not the failed same-line Hu<3.5 rule.
    split_fragment_allograph_merge: bool = True
    split_allograph_max_hu_distance: float = 2.0
    split_allograph_max_width_ratio: float = 1.08

    # Wide-box column-ink profile stitch. Hu is a poor match for the
    # cycle-7 Ca8 left neighbors (wide, Hu>3, area/width ~1). Pearson
    # on a 32-bin column-ink profile of that pair is ~0.04; adjacent
    # same-line wide pairs on Ca7–Ca8 top out ~0.70. Threshold 0.85 is
    # above both, so this pass does not force a 4-gram. Tall-thin Hu
    # gates are unchanged (aspect ≤ allograph_max_aspect is excluded).
    wide_profile_allograph_merge: bool = True
    wide_profile_bins: int = 32
    wide_profile_min_correlation: float = 0.85

    # After allograph stitches, un-merge split-fragment types whose members
    # fail the cycle 7–8 honest pair test (unsigned Hu >= 2.0 or column-ink
    # r < 0.85). Union-find can stitch first/middle/last ligature slots
    # through a chain; this pass splits those instances back apart. Cycle
    # 11 re-applies the same gates to remaining multi-member split-fragment
    # types; pairs that pass keep a shared ID (do not force a split). Does
    # not read Barthel stems. False keeps the cycle-9 lock.
    split_inconsistent_types: bool = True

    # Global same-type stitch after DBSCAN. Stock eps=0.5 leaves almost
    # every glyph its own type. The cycle 7–8 keep-ID gate (unsigned Hu
    # < 2.0 and, when both profiles exist, r >= 0.85) is applied to
    # every instance pair, not only delimiter slots. Connected
    # components are re-partitioned so a shared ID never includes a
    # failing pair. Does not loosen the gate. False keeps cycle 14.
    global_type_consistency_merge: bool = True

    # Merge instances that occupy the same published delimiter SLOT
    # (0–7) across Guy windows. Starts are reading-order indexes only —
    # not stem identities. A pair unions if it passes type-consistency
    # (Hu < 2.0 and, when both profiles exist, r >= 0.85) and/or the
    # wide-profile gate. Features that disagree keep distinct IDs; a
    # slot is not forced to one type. False keeps the cycle-11 lock.
    delimiter_slot_merge: bool = True
    # Slot-0 leftover crop stitch. NCC / chamfer on the 64x64 bbox
    # image, not a lowered global r. Merged-pair floor is NCC 0.504 /
    # chamfer 0.544; leftover ceiling is NCC 0.229 / chamfer 1.017.
    # Column-ink leftover max r is 0.584, below the 0.70 adjacent
    # non-match ceiling, so r is not lowered. False keeps cycle 12.
    delimiter_slot_crop_merge: bool = True
    delimiter_slot_crop_slots: tuple[int, ...] = (0,)
    slot_crop_min_ncc: float = 0.45
    slot_crop_max_chamfer: float = 0.80
    # Cycle 19: leftover crop stitch on any published slot, but only
    # for a pair whose union drops published-window min Hamming, and
    # at most once. Slot-0 crop (cycle 13) is unchanged. False keeps
    # the cycle-18 published-H=7 lock.
    delimiter_slot_crop_hamming_merge: bool = True
    # Cycle 20: remaining leftover same-slot crop pairs (slot 2 and
    # slot 3) on top of the cycle-19 Hamming merge. Together they
    # leave published min Hamming at 6, so this stays off. Slot 0
    # leftovers still fail the crop gate and are not merged.
    delimiter_slot_crop_leftover_merge: bool = False
    # Cycle 21: slot-0 leftover crop under {identity, hflip, vflip,
    # 180°}. Same NCC/chamfer numbers. No leftover clears, so a
    # Hamming-drop merge cannot fire. False keeps the cycle-20 lock.
    delimiter_slot_crop_invariant_merge: bool = False
    # Cycle 22 is a strip diagnostic, not a merge: concatenated
    # 8-crop window images vs the same NCC/chamfer gate. No flag.
    # Cycle 23 is the same diagnostic on the raw line rectangle
    # (union bbox of the eight glyph boxes). No flag. No merge.
    delimiter_window_len: int = 8
    # Cycle 14 locked joint offset 0 (0/8 at every offset in {-2..+2}).
    delimiter_window_starts: tuple[tuple[int, int], ...] = (
        (0, 6),
        (0, 19),
        (0, 33),
        (1, 3),
        (1, 15),
        (1, 29),
    )


def _bbox_area_ratio(left: GlyphInstance, right: GlyphInstance) -> float:
    """max(area)/min(area). inf if either box has no area."""
    area_a = left.bounding_box.area
    area_b = right.bounding_box.area
    smaller = min(area_a, area_b)
    if smaller <= 0:
        return float("inf")
    return max(area_a, area_b) / smaller


def _bbox_width_ratio(left: GlyphInstance, right: GlyphInstance) -> float:
    """max(width)/min(width). inf if either box has no width."""
    width_a = left.bounding_box.width
    width_b = right.bounding_box.width
    smaller = min(width_a, width_b)
    if smaller <= 0:
        return float("inf")
    return max(width_a, width_b) / smaller


def _bbox_aspect(instance: GlyphInstance) -> float:
    """width/height. inf if height is 0."""
    height = instance.bounding_box.height
    if height <= 0:
        return float("inf")
    return instance.bounding_box.width / height


def _hu_distance(left: GlyphInstance, right: GlyphInstance) -> float:
    """Euclidean distance on stored log-Hu vectors."""
    if not left.features or not right.features:
        return float("inf")
    return float(
        np.linalg.norm(
            np.asarray(left.features, dtype=float)
            - np.asarray(right.features, dtype=float)
        )
    )


def passes_same_line_allograph_gates(
    left: GlyphInstance,
    right: GlyphInstance,
    config: Optional[ProcessorConfig] = None,
) -> bool:
    """True if the same-line stitch would union these two instances.

    Adjacent-position is the caller's job. This is only the unsigned-Hu,
    area, and tall-thin aspect gates. Does not look up stems.
    """
    cfg = config or ProcessorConfig()
    if _bbox_aspect(left) > cfg.allograph_max_aspect:
        return False
    if _bbox_aspect(right) > cfg.allograph_max_aspect:
        return False
    if _bbox_area_ratio(left, right) > cfg.allograph_max_area_ratio:
        return False
    if _hu_distance(left, right) >= cfg.allograph_max_hu_distance:
        return False
    return True


def passes_split_fragment_allograph_gates(
    left: GlyphInstance,
    right: GlyphInstance,
    config: Optional[ProcessorConfig] = None,
) -> bool:
    """True if the split-fragment stitch would union these two instances.

    from_ligature_split is the caller's job. This is only the unsigned-Hu,
    area, and width gates. Does not look up stems.
    """
    cfg = config or ProcessorConfig()
    if _bbox_width_ratio(left, right) > cfg.split_allograph_max_width_ratio:
        return False
    if _bbox_area_ratio(left, right) > cfg.allograph_max_area_ratio:
        return False
    if _hu_distance(left, right) >= cfg.split_allograph_max_hu_distance:
        return False
    return True


def bbox_column_ink(binary: np.ndarray, bbox: BoundingBox) -> np.ndarray:
    """Ink-pixel count per column of a bbox ROI. Empty if the crop is empty."""
    y0 = max(0, bbox.y)
    x0 = max(0, bbox.x)
    y1 = min(binary.shape[0], bbox.y + bbox.height)
    x1 = min(binary.shape[1], bbox.x + bbox.width)
    if y1 <= y0 or x1 <= x0:
        return np.zeros(0, dtype=float)
    roi = binary[y0:y1, x0:x1]
    if roi.size == 0:
        return np.zeros(0, dtype=float)
    return (roi > 0).sum(axis=0).astype(float)


def resample_profile(column_ink: np.ndarray, bins: int = 32) -> list[float]:
    """Linear-resample a column-ink vector to a fixed length."""
    values = np.asarray(column_ink, dtype=float).ravel()
    n = max(1, int(bins))
    if values.size == 0:
        return [0.0] * n
    if values.size == 1:
        return [float(values[0])] * n
    sample = np.interp(
        np.linspace(0.0, 1.0, n),
        np.linspace(0.0, 1.0, values.size),
        values,
    )
    return [float(v) for v in sample]


def profile_correlation(
    left_profile: list[float] | np.ndarray,
    right_profile: list[float] | np.ndarray,
    bins: int = 32,
) -> float:
    """Pearson correlation of two column-ink profiles. 0.0 if undefined."""
    left = np.asarray(left_profile, dtype=float).ravel()
    right = np.asarray(right_profile, dtype=float).ravel()
    if left.size != bins or right.size != bins:
        left = np.asarray(resample_profile(left, bins), dtype=float)
        right = np.asarray(resample_profile(right, bins), dtype=float)
    if left.size < 2 or right.size < 2:
        return 0.0
    if float(left.std()) == 0.0 or float(right.std()) == 0.0:
        return 0.0
    value = float(np.corrcoef(left, right)[0, 1])
    if np.isnan(value):
        return 0.0
    return value


def passes_type_consistency_gates(
    left: GlyphInstance,
    right: GlyphInstance,
    config: Optional[ProcessorConfig] = None,
) -> bool:
    """True if two co-typed instances are similar enough to stay together.

    Cycle 7–8 honest thresholds: unsigned Hu < 2.0, and when both
    instances have a column-ink profile, Pearson r >= 0.85. Missing
    profiles do not fail the pair (Hu decides). Does not look up stems.
    """
    cfg = config or ProcessorConfig()
    if _hu_distance(left, right) >= cfg.split_allograph_max_hu_distance:
        return False
    if left.ink_profile and right.ink_profile:
        corr = profile_correlation(
            left.ink_profile, right.ink_profile, cfg.wide_profile_bins
        )
        if corr < cfg.wide_profile_min_correlation:
            return False
    return True


def passes_delimiter_slot_gates(
    left: GlyphInstance,
    right: GlyphInstance,
    config: Optional[ProcessorConfig] = None,
) -> bool:
    """True if same-slot instances may share an ID.

    Honest pair test from cycles 7–11: type-consistency (unsigned Hu <
    2.0 and, when both profiles exist, Pearson r >= 0.85) and/or the
    wide-profile gate (aspect > 0.5 and r >= 0.85). Does not look up
    stems and does not require every occupant of the slot to match.
    Crop NCC/chamfer is a leftover gate (slot 0, the cycle-19
    Hamming-drop pass, and the cycle-20 leftover pass when enabled).
    """
    return passes_type_consistency_gates(
        left, right, config
    ) or passes_wide_profile_allograph_gates(left, right, config)


def bbox_binary_crop(
    binary: np.ndarray, bbox: BoundingBox, size: tuple[int, int] = (64, 64)
) -> list[int]:
    """Flattened 0/255 crop of a bbox ROI, resized to size. Empty if none."""
    width, height = int(size[0]), int(size[1])
    n = max(1, width * height)
    y0 = max(0, bbox.y)
    x0 = max(0, bbox.x)
    y1 = min(binary.shape[0], bbox.y + bbox.height)
    x1 = min(binary.shape[1], bbox.x + bbox.width)
    if y1 <= y0 or x1 <= x0:
        return [0] * n
    roi = binary[y0:y1, x0:x1]
    if roi.size == 0:
        return [0] * n
    resized = cv2.resize((roi > 0).astype(np.uint8) * 255, (width, height))
    return [int(v) for v in resized.ravel().tolist()]


def _crop_plane(
    crop: list[int] | np.ndarray, size: tuple[int, int] = (64, 64)
) -> np.ndarray:
    """Reshape a stored flatten crop to a 2-D 0/255 plane. Zeros if short."""
    width, height = int(size[0]), int(size[1])
    values = np.asarray(crop, dtype=np.uint8).ravel()
    if values.size != width * height:
        return np.zeros((height, width), dtype=np.uint8)
    return values.reshape((height, width))


def crop_ncc(
    left_crop: list[int] | np.ndarray,
    right_crop: list[int] | np.ndarray,
    size: tuple[int, int] = (64, 64),
) -> float:
    """Normalized cross-correlation of two same-size bbox crops. 0 if empty."""
    left = _crop_plane(left_crop, size).astype(np.float32)
    right = _crop_plane(right_crop, size).astype(np.float32)
    if float(left.max()) == 0.0 or float(right.max()) == 0.0:
        return 0.0
    value = float(cv2.matchTemplate(left, right, cv2.TM_CCOEFF_NORMED)[0, 0])
    if np.isnan(value):
        return 0.0
    return value


def crop_chamfer(
    left_crop: list[int] | np.ndarray,
    right_crop: list[int] | np.ndarray,
    size: tuple[int, int] = (64, 64),
) -> float:
    """Symmetric mean chamfer on ink pixels of two bbox crops. inf if empty."""
    left = _crop_plane(left_crop, size)
    right = _crop_plane(right_crop, size)
    left_ink = left > 0
    right_ink = right > 0
    if not left_ink.any() or not right_ink.any():
        return float("inf")
    dt_left = cv2.distanceTransform((~left_ink).astype(np.uint8) * 255, cv2.DIST_L2, 5)
    dt_right = cv2.distanceTransform((~right_ink).astype(np.uint8) * 255, cv2.DIST_L2, 5)
    return 0.5 * (float(dt_left[right_ink].mean()) + float(dt_right[left_ink].mean()))


def passes_slot_crop_gates(
    left: GlyphInstance,
    right: GlyphInstance,
    config: Optional[ProcessorConfig] = None,
) -> bool:
    """True if two bbox crops are similar enough to share a leftover ID.

    Both stored crops must exist. NCC >= 0.45 and chamfer <= 0.80 —
    just under the weaker already-merged pair (0.504 / 0.544) and above
    the strongest slot-0 leftover (0.229 / 1.017). Does not look up
    stems and does not loosen Hu or column-ink gates. Cycle 19 also
    requires a published-window Hamming drop before this gate unions
    a non-slot-0 leftover. Cycle 20 can union remaining crop-clear
    leftovers without a Hamming drop; that pass stays off because
    published min Hamming stays 6. Cycle 21 may consult flip/180
    invariance on slot-0 leftovers only; that pass stays off
    because no leftover clears these same numbers.
    """
    cfg = config or ProcessorConfig()
    size = cfg.target_glyph_size
    if not left.glyph_crop or not right.glyph_crop:
        return False
    if crop_ncc(left.glyph_crop, right.glyph_crop, size) < cfg.slot_crop_min_ncc:
        return False
    if crop_chamfer(left.glyph_crop, right.glyph_crop, size) > cfg.slot_crop_max_chamfer:
        return False
    return True


def window_hamming(
    left: list[str] | tuple[str, ...], right: list[str] | tuple[str, ...]
) -> int:
    """Positions that differ. Equal length required."""
    if len(left) != len(right):
        raise ValueError("Hamming requires equal-length windows")
    return sum(a != b for a, b in zip(left, right))


def min_pairwise_window_hamming(
    grams: list[tuple[str, ...]] | tuple[tuple[str, ...], ...],
) -> int:
    """Min Hamming among distinct window grams."""
    if len(grams) < 2:
        raise ValueError("need at least two windows")
    return min(
        window_hamming(grams[i], grams[j])
        for i in range(len(grams))
        for j in range(i + 1, len(grams))
    )


def slot_window_grams(
    instances: list[GlyphInstance],
    slot_members: list[list[int]],
) -> tuple[tuple[str, ...], ...]:
    """Per-window G00n 8-grams from slot occupant indexes. No stem lookup."""
    if not slot_members or not slot_members[0]:
        return ()
    n_windows = len(slot_members[0])
    window_len = len(slot_members)
    return tuple(
        tuple(instances[slot_members[slot][w]].cluster_id for slot in range(window_len))
        for w in range(n_windows)
    )


def remap_window_types(
    grams: tuple[tuple[str, ...], ...] | list[tuple[str, ...]],
    left_id: str,
    right_id: str,
    shared_id: str = "MERGE",
) -> tuple[tuple[str, ...], ...]:
    """Union two cluster IDs inside published-window grams only."""
    keep = {left_id, right_id}
    return tuple(
        tuple(shared_id if token in keep else token for token in gram) for gram in grams
    )


def best_crop_hamming_pair(
    instances: list[GlyphInstance],
    slot_members: list[list[int]],
    config: Optional[ProcessorConfig] = None,
) -> Optional[tuple[int, int]]:
    """At most one leftover same-slot crop pair that drops min Hamming.

    Conservative cycle-13 crop gate (NCC / chamfer). Pairwise leftover
    occupants only — a slot is not forced to one ID. Returns instance
    indexes or None. Does not look up stems.
    """
    cfg = config or ProcessorConfig()
    grams = slot_window_grams(instances, slot_members)
    if len(grams) < 2:
        return None
    current = min_pairwise_window_hamming(grams)
    best: Optional[tuple] = None
    for slot, members in enumerate(slot_members):
        for a_i in range(len(members)):
            for b_i in range(a_i + 1, len(members)):
                left_i, right_i = members[a_i], members[b_i]
                if left_i == right_i:
                    continue
                left, right = instances[left_i], instances[right_i]
                if not left.cluster_id or not right.cluster_id:
                    continue
                if left.cluster_id == right.cluster_id:
                    continue
                if not passes_slot_crop_gates(left, right, cfg):
                    continue
                new_h = min_pairwise_window_hamming(
                    remap_window_types(grams, left.cluster_id, right.cluster_id)
                )
                if new_h >= current:
                    continue
                ncc = crop_ncc(left.glyph_crop, right.glyph_crop, cfg.target_glyph_size)
                rec = (new_h, -ncc, slot, left_i, right_i)
                if best is None or rec < best:
                    best = rec
    if best is None:
        return None
    return (best[3], best[4])


def leftover_crop_pairs(
    instances: list[GlyphInstance],
    slot_members: list[list[int]],
    config: Optional[ProcessorConfig] = None,
) -> tuple[tuple[int, int], ...]:
    """Leftover same-slot crop pairs that still clear NCC/chamfer.

    Slot 0 is excluded (cycle-13 leftovers fail and must stay split).
    Already-shared IDs are skipped. Does not require a Hamming drop.
    Pairwise only — a slot is not forced to one ID. No stem lookup.
    """
    cfg = config or ProcessorConfig()
    pairs: list[tuple[int, int]] = []
    for slot, members in enumerate(slot_members):
        if slot == 0:
            continue
        for a_i in range(len(members)):
            for b_i in range(a_i + 1, len(members)):
                left_i, right_i = members[a_i], members[b_i]
                if left_i == right_i:
                    continue
                left, right = instances[left_i], instances[right_i]
                if not left.cluster_id or not right.cluster_id:
                    continue
                if left.cluster_id == right.cluster_id:
                    continue
                if not passes_slot_crop_gates(left, right, cfg):
                    continue
                pairs.append((left_i, right_i))
    return tuple(pairs)


CROP_INVARIANT_TRANSFORMS = ("identity", "hflip", "vflip", "rot180")


def transform_glyph_crop(
    crop: list[int] | np.ndarray,
    name: str,
    size: tuple[int, int] = (64, 64),
) -> list[int]:
    """Apply one of {identity, hflip, vflip, rot180} to a stored bbox crop."""
    plane = _crop_plane(crop, size)
    if name == "identity":
        out = plane
    elif name == "hflip":
        out = np.fliplr(plane)
    elif name == "vflip":
        out = np.flipud(plane)
    elif name == "rot180":
        out = np.rot90(plane, 2)
    else:
        raise ValueError(f"unknown crop transform: {name}")
    return [int(v) for v in np.ascontiguousarray(out).ravel().tolist()]


def crop_invariant_match(
    left_crop: list[int] | np.ndarray,
    right_crop: list[int] | np.ndarray,
    size: tuple[int, int] = (64, 64),
) -> tuple[float, float, str]:
    """Max NCC over the four transforms; chamfer from that same transform."""
    best: Optional[tuple] = None
    for name in CROP_INVARIANT_TRANSFORMS:
        right_t = transform_glyph_crop(right_crop, name, size)
        ncc = crop_ncc(left_crop, right_t, size)
        chamfer = crop_chamfer(left_crop, right_t, size)
        rec = (ncc, -chamfer, name, chamfer)
        if best is None or rec[:3] > best[:3]:
            best = rec
    assert best is not None
    return (best[0], best[3], best[2])


def passes_slot_crop_invariant_gates(
    left: GlyphInstance,
    right: GlyphInstance,
    config: Optional[ProcessorConfig] = None,
) -> bool:
    """True if some transform satisfies the existing NCC/chamfer gate.

    Same numeric thresholds as passes_slot_crop_gates. Does not loosen
    the gate. Call sites restrict this to leftover slot-0 pairs.
    Does not look up stems.
    """
    cfg = config or ProcessorConfig()
    size = cfg.target_glyph_size
    if not left.glyph_crop or not right.glyph_crop:
        return False
    for name in CROP_INVARIANT_TRANSFORMS:
        right_t = transform_glyph_crop(right.glyph_crop, name, size)
        if crop_ncc(left.glyph_crop, right_t, size) < cfg.slot_crop_min_ncc:
            continue
        if crop_chamfer(left.glyph_crop, right_t, size) > cfg.slot_crop_max_chamfer:
            continue
        return True
    return False


def _leftover_slot0_pairs(
    instances: list[GlyphInstance],
    slot_members: list[list[int]],
):
    """Yield leftover slot-0 occupant index pairs. No stem lookup."""
    if not slot_members:
        return
    members = slot_members[0]
    for a_i in range(len(members)):
        for b_i in range(a_i + 1, len(members)):
            left_i, right_i = members[a_i], members[b_i]
            if left_i == right_i:
                continue
            left, right = instances[left_i], instances[right_i]
            if not left.cluster_id or not right.cluster_id:
                continue
            if left.cluster_id == right.cluster_id:
                continue
            yield left_i, right_i, left, right


def best_slot0_invariant_crop_pair(
    instances: list[GlyphInstance],
    slot_members: list[list[int]],
    config: Optional[ProcessorConfig] = None,
) -> Optional[tuple[int, int, float, float, str]]:
    """Highest-NCC leftover slot-0 pair under the four transforms.

    Returns (left_i, right_i, ncc, chamfer, transform) or None.
    Does not require the crop gate. Pairwise only. No stem lookup.
    """
    cfg = config or ProcessorConfig()
    size = cfg.target_glyph_size
    best: Optional[tuple] = None
    for left_i, right_i, left, right in _leftover_slot0_pairs(instances, slot_members):
        if not left.glyph_crop or not right.glyph_crop:
            continue
        ncc, chamfer, name = crop_invariant_match(left.glyph_crop, right.glyph_crop, size)
        rec = (ncc, -chamfer, left_i, right_i, chamfer, name)
        if best is None or rec[:2] > best[:2]:
            best = rec
    if best is None:
        return None
    return (best[2], best[3], best[0], best[4], best[5])


def best_slot0_invariant_crop_hamming_pair(
    instances: list[GlyphInstance],
    slot_members: list[list[int]],
    config: Optional[ProcessorConfig] = None,
) -> Optional[tuple[int, int]]:
    """At most one leftover slot-0 invariant pair that drops min Hamming.

    Same NCC/chamfer numbers as the upright crop gate. Slot 0 only.
    Pairwise leftover occupants. Returns instance indexes or None.
    Does not look up stems.
    """
    cfg = config or ProcessorConfig()
    grams = slot_window_grams(instances, slot_members)
    if len(grams) < 2:
        return None
    current = min_pairwise_window_hamming(grams)
    best: Optional[tuple] = None
    for left_i, right_i, left, right in _leftover_slot0_pairs(instances, slot_members):
        if not passes_slot_crop_invariant_gates(left, right, cfg):
            continue
        new_h = min_pairwise_window_hamming(
            remap_window_types(grams, left.cluster_id, right.cluster_id)
        )
        if new_h >= current:
            continue
        ncc, _chamfer, _name = crop_invariant_match(
            left.glyph_crop, right.glyph_crop, cfg.target_glyph_size
        )
        rec = (new_h, -ncc, left_i, right_i)
        if best is None or rec < best:
            best = rec
    if best is None:
        return None
    return (best[2], best[3])


def concat_glyph_strip(
    crops: list[list[int] | np.ndarray] | tuple[list[int] | np.ndarray, ...],
    cell_size: tuple[int, int] = (64, 64),
) -> list[int]:
    """Concatenate bbox crops left-to-right at a shared cell height."""
    if not crops:
        return []
    planes = [_crop_plane(crop, cell_size) for crop in crops]
    strip = np.concatenate(planes, axis=1)
    return [int(v) for v in np.ascontiguousarray(strip).ravel().tolist()]


def strip_plane_size(
    n_cells: int, cell_size: tuple[int, int] = (64, 64)
) -> tuple[int, int]:
    """(width, height) of a concatenated n-cell strip."""
    return (int(cell_size[0]) * int(n_cells), int(cell_size[1]))


def window_glyph_strips(
    instances: list[GlyphInstance],
    slot_members: list[list[int]],
    cell_size: tuple[int, int] = (64, 64),
) -> tuple[list[int], ...]:
    """One concatenated 8-crop strip per published window. No stem lookup."""
    if not slot_members or not slot_members[0]:
        return ()
    n_windows = len(slot_members[0])
    window_len = len(slot_members)
    strips: list[list[int]] = []
    for window in range(n_windows):
        crops = [
            instances[slot_members[slot][window]].glyph_crop or []
            for slot in range(window_len)
        ]
        strips.append(concat_glyph_strip(crops, cell_size))
    return tuple(strips)


def window_strip_pair_table(
    strips: tuple[list[int], ...] | list[list[int]],
    cell_size: tuple[int, int] = (64, 64),
    min_ncc: float = 0.45,
    max_chamfer: float = 0.80,
) -> tuple[tuple[int, int, str, float, float, bool], ...]:
    """Pairwise strip NCC/chamfer under {identity, hflip, vflip, rot180}.

    Each row is (left, right, transform, ncc, chamfer, gate). Gate is
    the existing crop threshold (NCC >= 0.45 / chamfer <= 0.80).
    Ceiling diagnostic — does not merge types.
    """
    if len(strips) < 2:
        return ()
    n_pixels = int(cell_size[0]) * int(cell_size[1])
    if n_pixels <= 0:
        raise ValueError("cell_size must be positive")
    n_cells = len(strips[0]) // n_pixels
    size = strip_plane_size(n_cells, cell_size)
    rows: list[tuple[int, int, str, float, float, bool]] = []
    for i in range(len(strips)):
        for j in range(i + 1, len(strips)):
            ncc, chamfer, name = crop_invariant_match(strips[i], strips[j], size)
            gate = ncc >= min_ncc and chamfer <= max_chamfer
            rows.append((i, j, name, ncc, chamfer, gate))
    return tuple(rows)


def best_window_strip_pair(
    rows: tuple[tuple[int, int, str, float, float, bool], ...]
    | list[tuple[int, int, str, float, float, bool]],
) -> Optional[tuple[int, int, str, float, float, bool]]:
    """Highest-NCC strip pair. Tie → lower chamfer, then earlier indexes."""
    if not rows:
        return None
    return max(rows, key=lambda row: (row[3], -row[4], -row[0], -row[1]))


WINDOW_RECTANGLE_SIZE = strip_plane_size(8)


def union_bbox(
    boxes: list[BoundingBox] | tuple[BoundingBox, ...],
) -> BoundingBox:
    """Axis-aligned union of glyph boxes. Empty if none."""
    if not boxes:
        return BoundingBox(x=0, y=0, width=0, height=0)
    x0 = min(box.x for box in boxes)
    y0 = min(box.y for box in boxes)
    x1 = max(box.x + box.width for box in boxes)
    y1 = max(box.y + box.height for box in boxes)
    return BoundingBox(x=int(x0), y=int(y0), width=int(x1 - x0), height=int(y1 - y0))


def window_line_rectangles(
    instances: list[GlyphInstance],
    slot_members: list[list[int]],
    binaries: dict[str, np.ndarray],
    size: tuple[int, int] = WINDOW_RECTANGLE_SIZE,
) -> tuple[list[int], ...]:
    """One union-bbox crop per published window from the line raster.

    Cycle 22 concatenated eight independently resized bbox crops.
    Those strips can look unlike even when the tablet regions match.
    This crops the contiguous rectangle covering those eight boxes
    on that source image. Occupants must share a source_image.
    No stem lookup. Ceiling diagnostic — does not merge types.
    """
    if not slot_members or not slot_members[0]:
        return ()
    n_windows = len(slot_members[0])
    window_len = len(slot_members)
    crops: list[list[int]] = []
    for window in range(n_windows):
        occupants = [
            instances[slot_members[slot][window]] for slot in range(window_len)
        ]
        sources = {occ.source_image for occ in occupants}
        if len(sources) != 1:
            raise ValueError("window occupants span multiple line images")
        source = occupants[0].source_image
        if source not in binaries:
            raise KeyError(f"missing line raster for {source}")
        box = union_bbox(tuple(occ.bounding_box for occ in occupants))
        crops.append(bbox_binary_crop(binaries[source], box, size))
    return tuple(crops)


def tablet_line_key(source_image: str) -> str:
    """Kohaumotu strip stem (07/08). Other filenames stay distinct.

    Used only to concatenate Ca7/Ca8 reading-order slots. Does not
    assign glyph meanings.
    """
    name = source_image.rsplit("/", 1)[-1]
    if len(name) >= 5 and name.startswith("sca") and name[3:5].isdigit():
        return name[3:5]
    return name


def passes_wide_profile_allograph_gates(
    left: GlyphInstance,
    right: GlyphInstance,
    config: Optional[ProcessorConfig] = None,
) -> bool:
    """True if two WIDE boxes share a high column-ink profile correlation.

    Both aspects must exceed allograph_max_aspect (0.5). Does not use Hu
    and does not loosen the tall-thin same-line gates. Empty profiles fail.
    """
    cfg = config or ProcessorConfig()
    if _bbox_aspect(left) <= cfg.allograph_max_aspect:
        return False
    if _bbox_aspect(right) <= cfg.allograph_max_aspect:
        return False
    if not left.ink_profile or not right.ink_profile:
        return False
    corr = profile_correlation(
        left.ink_profile, right.ink_profile, cfg.wide_profile_bins
    )
    return corr >= cfg.wide_profile_min_correlation


def vertical_valley_cuts(
    column_ink: np.ndarray,
    valley_ratio: float = 0.40,
    min_part_width: int = 12,
    max_parts: int = 3,
    smooth_window: int = 5,
    interior_lo: float = 0.18,
    interior_hi: float = 0.82,
    cluster_gap: int = 4,
) -> list[int]:
    """Interior x offsets of deep valleys in a vertical ink projection.

    Returns at most max_parts-1 cuts, deepest first, clustered so adjacent
    minima count as one valley. Empty if the profile is too short or no
    valley is deeper than valley_ratio × median.
    """
    col = np.asarray(column_ink, dtype=float)
    n = int(col.size)
    if n < 16 or max_parts < 2 or min_part_width < 1:
        return []
    window = max(1, int(smooth_window))
    if window % 2 == 0:
        window += 1
    kernel = np.ones(window, dtype=float) / window
    smoothed = np.convolve(col, kernel, mode="same")
    median = float(np.median(smoothed))
    if median <= 0:
        return []
    lo = max(1, int(n * interior_lo))
    hi = min(n - 1, int(n * interior_hi))
    if hi <= lo:
        return []
    raw: list[tuple[int, float]] = []
    threshold = valley_ratio * median
    for x in range(lo, hi):
        value = smoothed[x]
        if value <= smoothed[x - 1] and value <= smoothed[x + 1] and value < threshold:
            raw.append((x, value))
    if not raw:
        return []
    groups: list[list[tuple[int, float]]] = [[raw[0]]]
    for item in raw[1:]:
        if item[0] - groups[-1][-1][0] <= cluster_gap:
            groups[-1].append(item)
        else:
            groups.append([item])
    candidates = [min(group, key=lambda pair: pair[1])[0] for group in groups]
    kept: list[int] = []
    for x in sorted(candidates, key=lambda idx: smoothed[idx]):
        if x < min_part_width or (n - x) < min_part_width:
            continue
        if any(abs(x - other) < min_part_width for other in kept):
            continue
        kept.append(x)
        if len(kept) >= max_parts - 1:
            break
    return sorted(kept)


class GlyphProcessor:
    """Processes images to detect, extract, and cluster Rongorongo glyphs."""

    def __init__(self, config: Optional[ProcessorConfig] = None):
        """Initialize the processor with optional configuration."""
        self.config = config or ProcessorConfig()

    # =========================================================================
    # Image Loading and Preprocessing
    # =========================================================================

    def load_image(self, image_path: str) -> Optional[np.ndarray]:
        """Load an image from file path.

        Args:
            image_path: Path to the image file.

        Returns:
            Image as numpy array, or None if loading fails.
        """
        if not os.path.exists(image_path):
            return None
        img = cv2.imread(image_path)
        if img is None:
            return None
        return img

    def convert_grayscale(self, image: np.ndarray) -> np.ndarray:
        """Convert image to grayscale.

        Args:
            image: Input image (color or grayscale).

        Returns:
            Grayscale image.
        """
        if len(image.shape) == 2:
            return image
        if len(image.shape) == 3 and image.shape[2] == 1:
            return image.squeeze()
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def apply_threshold(self, image: np.ndarray) -> np.ndarray:
        """Apply adaptive thresholding to binarize the image.

        Args:
            image: Grayscale input image.

        Returns:
            Binary image.
        """
        return cv2.adaptiveThreshold(
            image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            self.config.adaptive_block_size,
            self.config.adaptive_c,
        )

    def denoise(self, image: np.ndarray) -> np.ndarray:
        """Apply denoising to the image.

        Args:
            image: Input image.

        Returns:
            Denoised image.
        """
        return cv2.GaussianBlur(
            image,
            (self.config.blur_kernel_size, self.config.blur_kernel_size),
            0,
        )

    def preprocess(self, image: np.ndarray) -> np.ndarray:
        """Full preprocessing pipeline.

        Args:
            image: Input image.

        Returns:
            Preprocessed binary image ready for contour detection.
        """
        gray = self.convert_grayscale(image)
        denoised = self.denoise(gray)
        binary = self.apply_threshold(denoised)
        return binary

    # =========================================================================
    # Glyph Detection
    # =========================================================================

    def find_contours(self, binary_image: np.ndarray) -> list[np.ndarray]:
        """Find contours in binary image.

        Args:
            binary_image: Preprocessed binary image.

        Returns:
            List of contours.
        """
        contours, _ = cv2.findContours(
            binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        return list(contours)

    def filter_contours(self, contours: list[np.ndarray]) -> list[np.ndarray]:
        """Filter contours by area and aspect ratio.

        Args:
            contours: List of contours to filter.

        Returns:
            Filtered list of contours.
        """
        filtered = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area < self.config.min_contour_area:
                continue
            if area > self.config.max_contour_area:
                continue

            x, y, w, h = cv2.boundingRect(contour)
            if h == 0:
                continue
            aspect_ratio = w / h
            if aspect_ratio < self.config.min_aspect_ratio:
                continue
            if aspect_ratio > self.config.max_aspect_ratio:
                continue

            filtered.append(contour)
        return filtered

    def contour_to_bounding_box(
        self, contour: np.ndarray, image_shape: tuple[int, ...]
    ) -> BoundingBox:
        """Convert a contour to a bounding box with padding.

        Args:
            contour: OpenCV contour.
            image_shape: Shape of the source image for boundary clamping.

        Returns:
            BoundingBox with padding applied.
        """
        x, y, w, h = cv2.boundingRect(contour)
        padding = self.config.bbox_padding

        # Apply padding with boundary clamping
        x = max(0, x - padding)
        y = max(0, y - padding)
        w = min(image_shape[1] - x, w + 2 * padding)
        h = min(image_shape[0] - y, h + 2 * padding)

        return BoundingBox(x=x, y=y, width=w, height=h)

    def detect_glyphs(
        self, image: np.ndarray, source_image: str
    ) -> list[GlyphInstance]:
        """Detect glyphs in an image.

        Args:
            image: Input image.
            source_image: Filename of the source image.

        Returns:
            List of detected GlyphInstance objects.
        """
        binary = self.preprocess(image)
        contours = self.find_contours(binary)
        filtered = self.filter_contours(contours)

        instances = []
        index = 0
        for contour in filtered:
            bbox = self.contour_to_bounding_box(contour, image.shape)
            parts = (
                self.split_wide_ligature(binary, bbox)
                if self.config.split_wide_ligatures
                else [bbox]
            )
            split = len(parts) > 1
            for part in parts:
                instance_id = GlyphInstance.generate_id(source_image, index)
                instances.append(
                    GlyphInstance(
                        instance_id=instance_id,
                        source_image=source_image,
                        bounding_box=part,
                        from_ligature_split=split,
                    )
                )
                index += 1

        return instances

    def split_wide_ligature(
        self, binary: np.ndarray, bbox: BoundingBox
    ) -> list[BoundingBox]:
        """Split a wide connected blob at deep vertical ink valleys.

        Tall-thin stems are skipped (aspect gate). Returns [bbox] when
        the box is too narrow, too thin, or has no qualifying valley.
        Does not invent stem identities.
        """
        if bbox.height <= 0 or bbox.width < self.config.ligature_min_width:
            return [bbox]
        aspect = bbox.width / bbox.height
        if aspect < self.config.ligature_min_aspect:
            return [bbox]

        pad = self.config.bbox_padding
        x0 = bbox.x + pad
        x1 = bbox.x + bbox.width - pad
        y0 = bbox.y + pad
        y1 = bbox.y + bbox.height - pad
        if x1 <= x0 or y1 <= y0:
            return [bbox]
        y0 = max(0, y0)
        y1 = min(binary.shape[0], y1)
        x0 = max(0, x0)
        x1 = min(binary.shape[1], x1)
        if x1 <= x0 or y1 <= y0:
            return [bbox]

        roi = binary[y0:y1, x0:x1]
        if roi.size == 0:
            return [bbox]
        column_ink = (roi > 0).sum(axis=0)
        cuts = vertical_valley_cuts(
            column_ink,
            valley_ratio=self.config.ligature_valley_ratio,
            min_part_width=self.config.ligature_min_part_width,
            max_parts=self.config.ligature_max_parts,
        )
        if not cuts:
            return [bbox]
        return self._bboxes_from_vertical_cuts(bbox, x0, cuts)

    def _bboxes_from_vertical_cuts(
        self, bbox: BoundingBox, interior_origin_x: int, cuts: list[int]
    ) -> list[BoundingBox]:
        """Divide bbox at interior-relative cut offsets. Fallback: original box."""
        abs_cuts = [interior_origin_x + cut for cut in cuts]
        edges = [bbox.x, *abs_cuts, bbox.x + bbox.width]
        parts: list[BoundingBox] = []
        for left, right in zip(edges, edges[1:]):
            width = right - left
            if width < 8:
                return [bbox]
            parts.append(
                BoundingBox(x=left, y=bbox.y, width=width, height=bbox.height)
            )
        return parts if len(parts) > 1 else [bbox]

    # =========================================================================
    # Line Detection and Position Assignment
    # =========================================================================

    def detect_lines(self, instances: list[GlyphInstance]) -> list[list[GlyphInstance]]:
        """Group glyph instances into lines based on vertical position.

        Args:
            instances: List of detected glyph instances.

        Returns:
            List of lines, where each line is a list of instances.
        """
        if not instances:
            return []

        # Sort by vertical center position
        sorted_instances = sorted(
            instances, key=lambda g: g.bounding_box.center[1]
        )

        lines: list[list[GlyphInstance]] = []
        current_line: list[GlyphInstance] = []
        current_y = -1000  # Start with impossible value

        for instance in sorted_instances:
            center_y = instance.bounding_box.center[1]
            if abs(center_y - current_y) > self.config.line_merge_threshold:
                # Start a new line
                if current_line:
                    lines.append(current_line)
                current_line = [instance]
                current_y = center_y
            else:
                current_line.append(instance)
                # Update current_y to average of line
                current_y = sum(g.bounding_box.center[1] for g in current_line) / len(
                    current_line
                )

        if current_line:
            lines.append(current_line)

        # Sort each line left to right
        for line in lines:
            line.sort(key=lambda g: g.bounding_box.center[0])

        return lines

    def assign_positions(self, instances: list[GlyphInstance]) -> list[GlyphInstance]:
        """Assign line numbers and positions to glyph instances.

        Args:
            instances: List of detected glyph instances.

        Returns:
            Same instances with position information added.
        """
        lines = self.detect_lines(instances)

        for line_num, line in enumerate(lines):
            total = len(line)
            for pos, instance in enumerate(line):
                instance.position = GlyphPosition(
                    line_number=line_num,
                    position_in_line=pos,
                    total_in_line=total,
                )

        # Flatten back to list
        return [inst for line in lines for inst in line]

    # =========================================================================
    # Feature Extraction
    # =========================================================================

    def extract_glyph_image(
        self, image: np.ndarray, bbox: BoundingBox
    ) -> np.ndarray:
        """Extract and normalize a glyph image from the source.

        Args:
            image: Source image.
            bbox: Bounding box of the glyph.

        Returns:
            Normalized glyph image.
        """
        # Extract region
        roi = image[bbox.y : bbox.y + bbox.height, bbox.x : bbox.x + bbox.width]

        # Convert to grayscale if needed
        if len(roi.shape) == 3:
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Resize to target size
        resized = cv2.resize(roi, self.config.target_glyph_size)

        return resized

    def compute_hu_moments(self, glyph_image: np.ndarray) -> list[float]:
        """Compute Hu moments for a glyph image.

        Args:
            glyph_image: Normalized glyph image.

        Returns:
            List of 7 log-Hu values. Default is unsigned (abs of the
            signed log-Hu). Pass hu_sign_mode="signed" for the cycle-1
            −sign(h)·log10(|h|) path.
        """
        # Ensure binary
        _, binary = cv2.threshold(glyph_image, 127, 255, cv2.THRESH_BINARY)

        moments = cv2.moments(binary)
        hu_moments = cv2.HuMoments(moments).flatten()

        # Signed log transform (cycle-1). Unsigned takes abs so Hu5–Hu7
        # sign-flips do not inflate Euclidean distance.
        signed_log_hu = []
        for h in hu_moments:
            if h != 0:
                signed_log_hu.append(float(-np.sign(h) * np.log10(abs(h))))
            else:
                signed_log_hu.append(0.0)

        mode = self.config.hu_sign_mode
        if mode == "unsigned":
            return [abs(v) for v in signed_log_hu]
        if mode == "signed":
            return signed_log_hu
        raise ValueError(
            f"hu_sign_mode must be 'unsigned' or 'signed', got {mode!r}"
        )

    def extract_features(
        self, image: np.ndarray, instance: GlyphInstance
    ) -> list[float]:
        """Extract feature vector for a glyph instance.

        Args:
            image: Source image.
            instance: Glyph instance to extract features for.

        Returns:
            Feature vector.
        """
        glyph_img = self.extract_glyph_image(image, instance.bounding_box)
        hu_moments = self.compute_hu_moments(glyph_img)
        return hu_moments

    def extract_features_batch(
        self, image: np.ndarray, instances: list[GlyphInstance]
    ) -> list[GlyphInstance]:
        """Extract features for multiple glyph instances.

        Args:
            image: Source image.
            instances: List of glyph instances.

        Returns:
            Same instances with features added.
        """
        binary = self.preprocess(image)
        bins = self.config.wide_profile_bins
        crop_size = self.config.target_glyph_size
        for instance in instances:
            instance.features = self.extract_features(image, instance)
            ink = bbox_column_ink(binary, instance.bounding_box)
            instance.ink_profile = resample_profile(ink, bins)
            instance.glyph_crop = bbox_binary_crop(
                binary, instance.bounding_box, crop_size
            )
        return instances

    # =========================================================================
    # Clustering
    # =========================================================================

    def cluster_glyphs(
        self, instances: list[GlyphInstance]
    ) -> tuple[list[GlyphCluster], list[GlyphInstance]]:
        """Cluster glyph instances by visual similarity.

        Args:
            instances: List of glyph instances with features.

        Returns:
            Tuple of (clusters, instances with cluster_id assigned).
        """
        if not instances:
            return [], []

        # Build feature matrix
        features = np.array([inst.features for inst in instances])

        # Handle single instance case
        if len(instances) == 1:
            cluster_id = GlyphCluster.generate_id(1)
            instances[0].cluster_id = cluster_id
            cluster = GlyphCluster(
                cluster_id=cluster_id,
                instances=[instances[0].instance_id],
                mean_features=instances[0].features,
            )
            return [cluster], instances

        # Run DBSCAN
        clustering = DBSCAN(
            eps=self.config.dbscan_eps,
            min_samples=self.config.dbscan_min_samples,
            metric="euclidean",
        )
        labels = clustering.fit_predict(features)

        # Group instances by cluster
        cluster_map: dict[int, list[GlyphInstance]] = {}
        noise_instances: list[GlyphInstance] = []

        for instance, label in zip(instances, labels):
            if label == -1:
                noise_instances.append(instance)
            else:
                if label not in cluster_map:
                    cluster_map[label] = []
                cluster_map[label].append(instance)

        # Create GlyphCluster objects, sorted by frequency (most common first)
        sorted_labels = sorted(cluster_map.keys(), key=lambda label: -len(cluster_map[label]))
        clusters = []

        for i, label in enumerate(sorted_labels):
            cluster_instances = cluster_map[label]
            cluster_id = GlyphCluster.generate_id(i + 1)

            # Assign cluster_id to instances
            for inst in cluster_instances:
                inst.cluster_id = cluster_id

            # Calculate mean features
            mean_features = np.mean(
                [inst.features for inst in cluster_instances], axis=0
            ).tolist()

            cluster = GlyphCluster(
                cluster_id=cluster_id,
                instances=[inst.instance_id for inst in cluster_instances],
                mean_features=mean_features,
            )
            clusters.append(cluster)

        # Handle noise points - each becomes its own cluster
        for i, inst in enumerate(noise_instances):
            cluster_id = GlyphCluster.generate_id(len(clusters) + i + 1)
            inst.cluster_id = cluster_id
            cluster = GlyphCluster(
                cluster_id=cluster_id,
                instances=[inst.instance_id],
                mean_features=inst.features,
            )
            clusters.append(cluster)

        if self.config.global_type_consistency_merge:
            self._merge_global_type_consistency(instances)
        if self.config.same_line_allograph_merge:
            self._merge_same_line_allographs(instances)
        if self.config.split_fragment_allograph_merge:
            self._merge_split_fragment_allographs(instances)
        if self.config.wide_profile_allograph_merge:
            self._merge_wide_profile_allographs(instances)
        if self.config.split_inconsistent_types:
            self._split_inconsistent_types(instances)
        if self.config.delimiter_slot_merge:
            self._merge_delimiter_slot_allographs(instances)
        if (
            self.config.delimiter_slot_merge
            and self.config.delimiter_slot_crop_hamming_merge
        ):
            self._merge_crop_hamming_pair(instances)
        if (
            self.config.delimiter_slot_merge
            and self.config.delimiter_slot_crop_leftover_merge
        ):
            self._merge_leftover_crop_pairs(instances)
        if (
            self.config.delimiter_slot_merge
            and self.config.delimiter_slot_crop_invariant_merge
        ):
            self._merge_slot0_invariant_crop_hamming_pair(instances)
        if (
            self.config.global_type_consistency_merge
            or self.config.same_line_allograph_merge
            or self.config.split_fragment_allograph_merge
            or self.config.wide_profile_allograph_merge
            or self.config.split_inconsistent_types
            or self.config.delimiter_slot_merge
        ):
            clusters = self._clusters_from_assigned_ids(instances)

        return clusters, instances

    def _merge_global_type_consistency(self, instances: list[GlyphInstance]) -> None:
        """Union any instances that pass the cycle 7–8 same-type gates.

        Global: not limited to delimiter slots, same-line adjacency, or
        split fragments. Pairwise unsigned Hu < 2.0 and, when both
        profiles exist, r >= 0.85. Connected components are then
        re-partitioned so every pair that keeps a shared ID still
        passes. Instance-local. Does not look up stems.
        """
        if len(instances) < 2:
            return

        parent = list(range(len(instances)))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(i: int, j: int) -> None:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[rj] = ri

        merged = False
        for i in range(len(instances)):
            for j in range(i + 1, len(instances)):
                if passes_type_consistency_gates(
                    instances[i], instances[j], self.config
                ):
                    union(i, j)
                    merged = True
        if not merged:
            return

        components: dict[int, list[int]] = {}
        for i in range(len(instances)):
            components.setdefault(find(i), []).append(i)

        merge_n = 0
        for members in components.values():
            unique = sorted(set(members), key=lambda i: instances[i].instance_id)
            if len(unique) < 2:
                continue
            parts: list[list[int]] = []
            for i in unique:
                placed = False
                for part in parts:
                    if all(
                        passes_type_consistency_gates(
                            instances[i], instances[j], self.config
                        )
                        for j in part
                    ):
                        part.append(i)
                        placed = True
                        break
                if not placed:
                    parts.append([i])
            for part in parts:
                if len(part) < 2:
                    continue
                merge_n += 1
                shared_id = f"T{merge_n:03d}"
                for i in part:
                    instances[i].cluster_id = shared_id

    def _merge_same_line_allographs(self, instances: list[GlyphInstance]) -> None:
        """Union adjacent same-line instances that pass area / aspect / Hu gates.

        Instance-local: does not pull in other members of a pre-existing
        DBSCAN type. Mutates cluster_id on merged instances.
        """
        if len(instances) < 2:
            return

        parent = list(range(len(instances)))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(i: int, j: int) -> None:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[rj] = ri

        by_line: dict[tuple[str, int], list[int]] = {}
        for i, inst in enumerate(instances):
            if inst.position is None:
                continue
            key = (inst.source_image, inst.position.line_number)
            by_line.setdefault(key, []).append(i)

        for idxs in by_line.values():
            idxs.sort(key=lambda i: instances[i].position.position_in_line)
            for left, right in zip(idxs, idxs[1:]):
                a, b = instances[left], instances[right]
                if a.position.position_in_line + 1 != b.position.position_in_line:
                    continue
                if not passes_same_line_allograph_gates(a, b, self.config):
                    continue
                union(left, right)

        components: dict[int, list[int]] = {}
        for i in range(len(instances)):
            components.setdefault(find(i), []).append(i)

        merge_n = 0
        for members in components.values():
            if len(members) < 2:
                continue
            merge_n += 1
            shared_id = f"M{merge_n:03d}"
            for i in members:
                instances[i].cluster_id = shared_id

    def _merge_split_fragment_allographs(self, instances: list[GlyphInstance]) -> None:
        """Union valley-split fragments with similar bbox width/area and Hu.

        Cross-image and instance-local. Does not pull non-split members
        of a pre-existing DBSCAN type. Mutates cluster_id on merged
        instances. Tall-thin same-line stitch is a separate pass.
        """
        idxs = [i for i, inst in enumerate(instances) if inst.from_ligature_split]
        if len(idxs) < 2:
            return

        parent = list(range(len(instances)))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(i: int, j: int) -> None:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[rj] = ri

        for a_i in range(len(idxs)):
            for b_i in range(a_i + 1, len(idxs)):
                left, right = idxs[a_i], idxs[b_i]
                a, b = instances[left], instances[right]
                if not passes_split_fragment_allograph_gates(a, b, self.config):
                    continue
                union(left, right)

        components: dict[int, list[int]] = {}
        for i in idxs:
            components.setdefault(find(i), []).append(i)

        merge_n = 0
        for members in components.values():
            if len(members) < 2:
                continue
            merge_n += 1
            shared_id = f"S{merge_n:03d}"
            for i in members:
                instances[i].cluster_id = shared_id

    def _merge_wide_profile_allographs(self, instances: list[GlyphInstance]) -> None:
        """Union wide boxes with high column-ink profile correlation.

        Scopes: same-line adjacent, or corresponding neighbors of a
        repeating mixed n-gram (delimiter-adjacent proxy). Does not
        use Hu. Mutates cluster_id on merged instances.
        """
        if len(instances) < 2:
            return

        parent = list(range(len(instances)))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(i: int, j: int) -> None:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[rj] = ri

        by_line: dict[tuple[str, int], list[int]] = {}
        for i, inst in enumerate(instances):
            if inst.position is None:
                continue
            key = (inst.source_image, inst.position.line_number)
            by_line.setdefault(key, []).append(i)

        for idxs in by_line.values():
            idxs.sort(key=lambda i: instances[i].position.position_in_line)
            for left, right in zip(idxs, idxs[1:]):
                a, b = instances[left], instances[right]
                if a.position.position_in_line + 1 != b.position.position_in_line:
                    continue
                if not passes_wide_profile_allograph_gates(a, b, self.config):
                    continue
                union(left, right)

        line_indexes = self._reading_order_indexes(instances)
        for left_i, right_i in self._mixed_repeating_neighbor_index_pairs(
            instances, line_indexes
        ):
            a, b = instances[left_i], instances[right_i]
            if not passes_wide_profile_allograph_gates(a, b, self.config):
                continue
            union(left_i, right_i)

        components: dict[int, list[int]] = {}
        for i in range(len(instances)):
            components.setdefault(find(i), []).append(i)

        merge_n = 0
        for members in components.values():
            if len(members) < 2:
                continue
            merge_n += 1
            shared_id = f"W{merge_n:03d}"
            for i in members:
                instances[i].cluster_id = shared_id

    def _split_inconsistent_types(self, instances: list[GlyphInstance]) -> None:
        """Split split-fragment types whose members fail Hu or profile gates.

        Merge-time union-find is transitive: first/middle/last slots of a
        3-part valley split can share an ID through a chain even when the
        endpoints are dissimilar. Re-partition those members so every pair
        that keeps a shared ID passes passes_type_consistency_gates.
        Members that already pass Hu/profile stay together. Instance-local.
        Does not read Barthel stems.
        """
        groups: dict[str, list[int]] = {}
        for i, inst in enumerate(instances):
            if not inst.from_ligature_split or not inst.cluster_id:
                continue
            groups.setdefault(inst.cluster_id, []).append(i)

        split_n = 0
        for idxs in groups.values():
            if len(idxs) < 2:
                continue
            members = sorted(idxs, key=lambda i: instances[i].instance_id)
            parts: list[list[int]] = []
            for i in members:
                placed = False
                for part in parts:
                    if all(
                        passes_type_consistency_gates(
                            instances[i], instances[j], self.config
                        )
                        for j in part
                    ):
                        part.append(i)
                        placed = True
                        break
                if not placed:
                    parts.append([i])
            if len(parts) < 2:
                continue
            for part in parts:
                split_n += 1
                new_id = f"X{split_n:03d}"
                for i in part:
                    instances[i].cluster_id = new_id

    def _concatenated_tablet_line_indexes(
        self, instances: list[GlyphInstance]
    ) -> list[list[int]]:
        """Instance indexes grouped by tablet line key, concatenated reading order.

        Kohaumotu strips with the same stem (07/08) become one line so
        published window STARTS can address Ca7/Ca8 slots. Other source
        names stay one line each. Does not assign stem meanings.
        """
        buckets: dict[str, list[int]] = {}
        for i, inst in enumerate(instances):
            if inst.position is None:
                continue
            buckets.setdefault(tablet_line_key(inst.source_image), []).append(i)
        lines: list[list[int]] = []
        for key in sorted(buckets):
            idxs = buckets[key]
            idxs.sort(
                key=lambda i: (
                    instances[i].source_image,
                    instances[i].position.line_number,
                    instances[i].position.position_in_line,
                )
            )
            lines.append(idxs)
        return lines

    def _merge_delimiter_slot_allographs(self, instances: list[GlyphInstance]) -> None:
        """Union same-slot occupants that pass Hu, wide-profile, or crop gates.

        Published window starts define the eight slots. Pairwise only:
        a slot is not collapsed to one ID when other occupants fail.
        Crop NCC/chamfer is consulted for configured leftover slots
        (default: slot 0). The cycle-19 Hamming-drop crop stitch runs
        after this pass assigns IDs. Cycle 20 leftover crop unions
        are off by default. Instance-local. Does not read Barthel
        stem values.
        """
        if len(instances) < 2:
            return

        window_len = int(self.config.delimiter_window_len)
        starts = tuple(self.config.delimiter_window_starts)
        if window_len < 1 or not starts:
            return

        line_indexes = self._concatenated_tablet_line_indexes(instances)
        slot_members: list[list[int]] = [[] for _ in range(window_len)]
        for line_index, start in starts:
            if line_index < 0 or line_index >= len(line_indexes):
                continue
            line = line_indexes[line_index]
            end = start + window_len
            if start < 0 or end > len(line):
                continue
            for slot in range(window_len):
                slot_members[slot].append(line[start + slot])

        parent = list(range(len(instances)))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(i: int, j: int) -> None:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[rj] = ri

        crop_slots = (
            set(self.config.delimiter_slot_crop_slots)
            if self.config.delimiter_slot_crop_merge
            else set()
        )
        merged = False
        for slot, members in enumerate(slot_members):
            use_crop = slot in crop_slots
            for a_i in range(len(members)):
                for b_i in range(a_i + 1, len(members)):
                    left_i, right_i = members[a_i], members[b_i]
                    if left_i == right_i:
                        continue
                    left, right = instances[left_i], instances[right_i]
                    if passes_delimiter_slot_gates(left, right, self.config):
                        union(left_i, right_i)
                        merged = True
                        continue
                    if use_crop and passes_slot_crop_gates(left, right, self.config):
                        union(left_i, right_i)
                        merged = True

        if not merged:
            return

        components: dict[int, list[int]] = {}
        for members in slot_members:
            for i in members:
                components.setdefault(find(i), []).append(i)

        merge_n = 0
        for members in components.values():
            unique = sorted(set(members))
            if len(unique) < 2:
                continue
            merge_n += 1
            shared_id = f"D{merge_n:03d}"
            for i in unique:
                instances[i].cluster_id = shared_id

    def _merge_crop_hamming_pair(self, instances: list[GlyphInstance]) -> None:
        """Union at most one leftover crop pair that drops min Hamming.

        Runs after slot IDs are assigned so the Hamming check sees the
        cycle-12 shared slots. The winning pair keeps the left
        occupant's ID. Does not look up stems.
        """
        if len(instances) < 2:
            return
        window_len = int(self.config.delimiter_window_len)
        starts = tuple(self.config.delimiter_window_starts)
        if window_len < 1 or not starts:
            return
        line_indexes = self._concatenated_tablet_line_indexes(instances)
        slot_members: list[list[int]] = [[] for _ in range(window_len)]
        for line_index, start in starts:
            if line_index < 0 or line_index >= len(line_indexes):
                continue
            line = line_indexes[line_index]
            end = start + window_len
            if start < 0 or end > len(line):
                continue
            for slot in range(window_len):
                slot_members[slot].append(line[start + slot])
        pair = best_crop_hamming_pair(instances, slot_members, self.config)
        if pair is None:
            return
        left_i, right_i = pair
        shared = instances[left_i].cluster_id or instances[right_i].cluster_id
        if not shared:
            return
        instances[left_i].cluster_id = shared
        instances[right_i].cluster_id = shared

    def _merge_leftover_crop_pairs(self, instances: list[GlyphInstance]) -> None:
        """Union remaining leftover crop pairs after the Hamming-drop pass.

        Same cycle-13 crop gate. Slot 0 is not merged. Pairwise only.
        Shared ID is the first occupant's current ID. No stem lookup.
        """
        if len(instances) < 2:
            return
        window_len = int(self.config.delimiter_window_len)
        starts = tuple(self.config.delimiter_window_starts)
        if window_len < 1 or not starts:
            return
        line_indexes = self._concatenated_tablet_line_indexes(instances)
        slot_members: list[list[int]] = [[] for _ in range(window_len)]
        for line_index, start in starts:
            if line_index < 0 or line_index >= len(line_indexes):
                continue
            line = line_indexes[line_index]
            end = start + window_len
            if start < 0 or end > len(line):
                continue
            for slot in range(window_len):
                slot_members[slot].append(line[start + slot])
        pairs = leftover_crop_pairs(instances, slot_members, self.config)
        if not pairs:
            return
        parent = list(range(len(instances)))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(i: int, j: int) -> None:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[rj] = ri

        for left_i, right_i in pairs:
            union(left_i, right_i)
        components: dict[int, list[int]] = {}
        for left_i, right_i in pairs:
            for i in (left_i, right_i):
                components.setdefault(find(i), []).append(i)
        for members in components.values():
            unique = sorted(set(members))
            if len(unique) < 2:
                continue
            shared = instances[unique[0]].cluster_id
            if not shared:
                continue
            for i in unique:
                instances[i].cluster_id = shared

    def _merge_slot0_invariant_crop_hamming_pair(
        self, instances: list[GlyphInstance]
    ) -> None:
        """Union at most one leftover slot-0 flip/180 pair that drops Hamming.

        Same NCC/chamfer numbers as the upright crop gate. Other slots
        are not consulted. Shared ID is the left occupant's current ID.
        No stem lookup.
        """
        if len(instances) < 2:
            return
        window_len = int(self.config.delimiter_window_len)
        starts = tuple(self.config.delimiter_window_starts)
        if window_len < 1 or not starts:
            return
        line_indexes = self._concatenated_tablet_line_indexes(instances)
        slot_members: list[list[int]] = [[] for _ in range(window_len)]
        for line_index, start in starts:
            if line_index < 0 or line_index >= len(line_indexes):
                continue
            line = line_indexes[line_index]
            end = start + window_len
            if start < 0 or end > len(line):
                continue
            for slot in range(window_len):
                slot_members[slot].append(line[start + slot])
        pair = best_slot0_invariant_crop_hamming_pair(
            instances, slot_members, self.config
        )
        if pair is None:
            return
        left_i, right_i = pair
        shared = instances[left_i].cluster_id or instances[right_i].cluster_id
        if not shared:
            return
        instances[left_i].cluster_id = shared
        instances[right_i].cluster_id = shared

    def _reading_order_indexes(
        self, instances: list[GlyphInstance]
    ) -> list[list[int]]:
        """Instance indexes grouped by (source_image, line), reading order."""
        buckets: dict[tuple[str, int], list[int]] = {}
        for i, inst in enumerate(instances):
            if inst.position is None or not inst.cluster_id:
                continue
            key = (inst.source_image, inst.position.line_number)
            buckets.setdefault(key, []).append(i)
        lines: list[list[int]] = []
        for key in sorted(buckets):
            idxs = buckets[key]
            idxs.sort(key=lambda i: instances[i].position.position_in_line)
            lines.append(idxs)
        return lines

    def _mixed_repeating_neighbor_index_pairs(
        self,
        instances: list[GlyphInstance],
        line_indexes: list[list[int]],
    ) -> list[tuple[int, int]]:
        """Corresponding left/right neighbors of mixed n-grams with freq ≥2."""
        sequences = [
            [instances[i].cluster_id for i in idxs] for idxs in line_indexes
        ]
        occurrences: dict[tuple[str, ...], list[tuple[int, int, int]]] = defaultdict(
            list
        )
        for n in range(2, 9):
            for line_k, seq in enumerate(sequences):
                if len(seq) < n:
                    continue
                for start in range(len(seq) - n + 1):
                    gram = tuple(seq[start : start + n])
                    if len(set(gram)) < 2:
                        continue
                    occurrences[gram].append((line_k, start, n))

        pairs: list[tuple[int, int]] = []
        seen: set[tuple[int, int]] = set()
        for hits in occurrences.values():
            if len(hits) < 2:
                continue
            for a in range(len(hits)):
                for b in range(a + 1, len(hits)):
                    line_a, start_a, n_a = hits[a]
                    line_b, start_b, n_b = hits[b]
                    for offset in (-1, n_a):
                        idx_a = start_a + offset
                        idx_b = start_b + offset
                        if not (0 <= idx_a < len(line_indexes[line_a])):
                            continue
                        if not (0 <= idx_b < len(line_indexes[line_b])):
                            continue
                        left_i = line_indexes[line_a][idx_a]
                        right_i = line_indexes[line_b][idx_b]
                        key = (min(left_i, right_i), max(left_i, right_i))
                        if key in seen or left_i == right_i:
                            continue
                        seen.add(key)
                        pairs.append(key)
        return pairs

    def _clusters_from_assigned_ids(
        self, instances: list[GlyphInstance]
    ) -> list[GlyphCluster]:
        """Rebuild clusters from instance.cluster_id; G001 is most frequent."""
        groups: dict[str, list[GlyphInstance]] = {}
        for inst in instances:
            if not inst.cluster_id:
                continue
            groups.setdefault(inst.cluster_id, []).append(inst)

        ranked = sorted(
            groups.values(),
            key=lambda members: (-len(members), members[0].instance_id),
        )
        clusters = []
        for i, members in enumerate(ranked):
            cluster_id = GlyphCluster.generate_id(i + 1)
            for inst in members:
                inst.cluster_id = cluster_id
            mean_features = np.mean(
                [inst.features for inst in members], axis=0
            ).tolist()
            clusters.append(
                GlyphCluster(
                    cluster_id=cluster_id,
                    instances=[inst.instance_id for inst in members],
                    mean_features=mean_features,
                )
            )
        return clusters

    # =========================================================================
    # Position Statistics
    # =========================================================================

    def compute_position_stats(
        self,
        cluster: GlyphCluster,
        all_instances: list[GlyphInstance],
    ) -> PositionStats:
        """Compute position statistics for a cluster.

        Args:
            cluster: The cluster to compute stats for.
            all_instances: All instances (for neighbor analysis).

        Returns:
            PositionStats for the cluster.
        """
        # Get instances for this cluster
        cluster_instances = [
            inst for inst in all_instances if inst.cluster_id == cluster.cluster_id
        ]

        stats = PositionStats()

        # Line distribution
        for inst in cluster_instances:
            if inst.position:
                line = inst.position.line_number
                stats.line_distribution[line] = stats.line_distribution.get(line, 0) + 1

        # Average position in line
        positions = []
        for inst in cluster_instances:
            if inst.position and inst.position.total_in_line > 0:
                relative_pos = inst.position.position_in_line / inst.position.total_in_line
                positions.append(relative_pos)
        if positions:
            stats.avg_position_in_line = sum(positions) / len(positions)

        # Common neighbors (simplified - just count adjacent cluster IDs)
        neighbor_counts: dict[str, int] = {}
        for inst in cluster_instances:
            if inst.position:
                # Find neighbors in same line
                for other in all_instances:
                    if other.instance_id == inst.instance_id:
                        continue
                    if other.position and other.position.line_number == inst.position.line_number:
                        if abs(other.position.position_in_line - inst.position.position_in_line) == 1:
                            if other.cluster_id:
                                neighbor_counts[other.cluster_id] = (
                                    neighbor_counts.get(other.cluster_id, 0) + 1
                                )

        # Top 5 neighbors
        sorted_neighbors = sorted(neighbor_counts.items(), key=lambda x: -x[1])
        stats.common_neighbors = [n[0] for n in sorted_neighbors[:5]]

        return stats

    # =========================================================================
    # Glyph Image Saving
    # =========================================================================

    def save_glyph_image(
        self,
        image: np.ndarray,
        instance: GlyphInstance,
        output_dir: str,
    ) -> str:
        """Save an extracted glyph image to disk.

        Args:
            image: Source image.
            instance: Glyph instance to save.
            output_dir: Directory to save to.

        Returns:
            Path to saved image.
        """
        os.makedirs(output_dir, exist_ok=True)

        glyph_img = self.extract_glyph_image(image, instance.bounding_box)
        filename = f"{instance.instance_id}.png"
        filepath = os.path.join(output_dir, filename)

        cv2.imwrite(filepath, glyph_img)
        instance.image_path = filepath
        return filepath

    def save_representative_image(
        self,
        cluster: GlyphCluster,
        all_instances: list[GlyphInstance],
        images: dict[str, np.ndarray],
        output_dir: str,
    ) -> str:
        """Save a representative image for a cluster.

        Args:
            cluster: The cluster.
            all_instances: All glyph instances.
            images: Dict mapping source filenames to loaded images.
            output_dir: Directory to save to.

        Returns:
            Path to saved representative image.
        """
        os.makedirs(output_dir, exist_ok=True)

        # Find the first instance in this cluster
        for inst in all_instances:
            if inst.instance_id in cluster.instances:
                if inst.source_image in images:
                    image = images[inst.source_image]
                    glyph_img = self.extract_glyph_image(image, inst.bounding_box)
                    filename = f"{cluster.cluster_id}_representative.png"
                    filepath = os.path.join(output_dir, filename)
                    cv2.imwrite(filepath, glyph_img)
                    cluster.representative_image = filepath
                    return filepath

        return ""


def instances_to_line_sequences(instances: list[GlyphInstance]) -> list[list[str]]:
    """Map clustered cataloger instances to cluster-id sequences in reading order.

    Groups by (source_image, line_number) and sorts each group by
    position_in_line. Emits G00n IDs as assigned by cluster_glyphs.
    Does not remap those IDs to Barthel stems.

    PatternMiningAgent._extract_sequences is not the cataloger hook: it
    reads a lexicon dict with clusters[].positions.instances, which
    RongorongoLexicon.to_dict() does not emit. The real fields are on
    GlyphInstance.position and GlyphInstance.cluster_id.
    """
    buckets: dict[tuple[str, int], list[tuple[int, str]]] = {}
    for inst in instances:
        if inst.position is None or not inst.cluster_id:
            continue
        key = (inst.source_image, inst.position.line_number)
        buckets.setdefault(key, []).append(
            (inst.position.position_in_line, inst.cluster_id)
        )

    sequences: list[list[str]] = []
    for key in sorted(buckets):
        ordered = sorted(buckets[key], key=lambda item: item[0])
        sequences.append([cluster_id for _, cluster_id in ordered])
    return sequences
