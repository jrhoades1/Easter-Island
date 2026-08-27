#!/usr/bin/env python3
"""Rongorongo Glyph Cataloger - Main orchestration script.

This script processes images of Rongorongo tablets to:
1. Detect individual glyphs using computer vision
2. Extract visual features from each glyph
3. Cluster similar glyphs and assign unique IDs
4. Output a lexicon with frequency counts and positional analysis
"""

import json
import os
import sys
from datetime import datetime

from config import GLYPH_CONFIG
from models.glyphs import GlyphInstance, LexiconStatistics, RongorongoLexicon
from processors.glyph_processor import GlyphProcessor, ProcessorConfig


def get_image_files(input_dir: str) -> list[str]:
    """Get all image files from the input directory.

    Args:
        input_dir: Path to the input directory.

    Returns:
        List of image file paths.
    """
    supported_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif"}
    image_files = []

    if not os.path.exists(input_dir):
        return []

    for filename in os.listdir(input_dir):
        ext = os.path.splitext(filename)[1].lower()
        if ext in supported_extensions:
            image_files.append(os.path.join(input_dir, filename))

    return sorted(image_files)


def process_images(
    processor: GlyphProcessor,
    image_paths: list[str],
    output_dir: str,
    save_glyphs: bool = True,
) -> tuple[list[GlyphInstance], dict[str, any]]:
    """Process multiple images and extract glyphs.

    Args:
        processor: The glyph processor instance.
        image_paths: List of paths to image files.
        output_dir: Directory to save extracted glyph images.
        save_glyphs: Whether to save individual glyph images.

    Returns:
        Tuple of (all instances, dict of loaded images by filename).
    """
    all_instances: list[GlyphInstance] = []
    images: dict[str, any] = {}

    for image_path in image_paths:
        filename = os.path.basename(image_path)
        print(f"  Processing: {filename}")

        # Load image
        image = processor.load_image(image_path)
        if image is None:
            print(f"    Warning: Could not load {filename}, skipping")
            continue

        images[filename] = image

        # Detect glyphs
        instances = processor.detect_glyphs(image, filename)
        print(f"    Detected {len(instances)} glyphs")

        if not instances:
            continue

        # Assign positions
        instances = processor.assign_positions(instances)

        # Extract features
        instances = processor.extract_features_batch(image, instances)

        # Save individual glyph images
        if save_glyphs:
            glyph_output_dir = os.path.join(output_dir, "glyphs")
            for instance in instances:
                processor.save_glyph_image(image, instance, glyph_output_dir)

        all_instances.extend(instances)

    return all_instances, images


def build_lexicon(
    processor: GlyphProcessor,
    instances: list[GlyphInstance],
    images: dict[str, any],
    output_dir: str,
    clustering_params: dict,
) -> RongorongoLexicon:
    """Build the glyph lexicon from detected instances.

    Args:
        processor: The glyph processor instance.
        instances: All detected glyph instances.
        images: Dict of loaded images by filename.
        output_dir: Directory for output files.
        clustering_params: Parameters used for clustering.

    Returns:
        The complete RongorongoLexicon.
    """
    # Cluster glyphs
    print("\nClustering glyphs...")
    clusters, instances = processor.cluster_glyphs(instances)
    print(f"  Found {len(clusters)} unique glyph types")

    # Compute position statistics for each cluster
    print("Computing position statistics...")
    for cluster in clusters:
        cluster.positions = processor.compute_position_stats(cluster, instances)

    # Save representative images
    print("Saving representative images...")
    glyph_output_dir = os.path.join(output_dir, "glyphs")
    for cluster in clusters:
        processor.save_representative_image(cluster, instances, images, glyph_output_dir)

    # Build lexicon
    lexicon = RongorongoLexicon(
        version="1.0.0",
        created_at=datetime.now(),
        source_images=list(images.keys()),
        clusters=clusters,
    )

    # Compute statistics
    lexicon.statistics = LexiconStatistics(clustering_params=clustering_params)
    lexicon.compute_statistics(instances)

    return lexicon


def save_lexicon(lexicon: RongorongoLexicon, output_path: str) -> None:
    """Save the lexicon to a JSON file.

    Args:
        lexicon: The lexicon to save.
        output_path: Path to the output JSON file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(lexicon.to_dict(), f, indent=2, ensure_ascii=False)


def main() -> int:
    """Main entry point for the glyph cataloger.

    Returns:
        Exit code (0 for success, 1 for failure).
    """
    # Ensure UTF-8 output on Windows
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 60)
    print("Rongorongo Glyph Cataloger")
    print("=" * 60)

    # Get configuration
    config = GLYPH_CONFIG

    input_dir = config["input_dir"]
    output_dir = config["output_dir"]
    output_file = os.path.join(output_dir, config["output_file"])

    # Check for input images
    print(f"\nScanning for images in: {input_dir}")
    image_paths = get_image_files(input_dir)

    if not image_paths:
        print(f"\nNo images found in {input_dir}")
        print("Please add tablet images (PNG, JPG, etc.) to the input directory.")

        # Create input directory if it doesn't exist
        os.makedirs(input_dir, exist_ok=True)

        return 1

    print(f"Found {len(image_paths)} image(s)")

    # Initialize processor with configuration
    processor_config = ProcessorConfig(
        min_contour_area=config["processing"]["min_contour_area"],
        max_contour_area=config["processing"]["max_contour_area"],
        bbox_padding=config["processing"]["bbox_padding"],
        line_merge_threshold=config["processing"]["line_merge_threshold"],
        dbscan_eps=config["clustering"]["eps"],
        dbscan_min_samples=config["clustering"]["min_samples"],
        hu_sign_mode=config["clustering"].get("hu_sign_mode", "unsigned"),
        same_line_allograph_merge=config["clustering"].get(
            "same_line_allograph_merge", True
        ),
        allograph_max_hu_distance=config["clustering"].get(
            "allograph_max_hu_distance", 3.5
        ),
        allograph_max_area_ratio=config["clustering"].get(
            "allograph_max_area_ratio", 1.1
        ),
        allograph_max_aspect=config["clustering"].get("allograph_max_aspect", 0.5),
        split_wide_ligatures=config["clustering"].get("split_wide_ligatures", True),
        ligature_min_width=config["clustering"].get("ligature_min_width", 70),
        ligature_min_aspect=config["clustering"].get("ligature_min_aspect", 0.90),
        ligature_valley_ratio=config["clustering"].get("ligature_valley_ratio", 0.40),
        ligature_min_part_width=config["clustering"].get("ligature_min_part_width", 12),
        ligature_max_parts=config["clustering"].get("ligature_max_parts", 3),
        split_fragment_allograph_merge=config["clustering"].get(
            "split_fragment_allograph_merge", True
        ),
        split_allograph_max_hu_distance=config["clustering"].get(
            "split_allograph_max_hu_distance", 2.0
        ),
        split_allograph_max_width_ratio=config["clustering"].get(
            "split_allograph_max_width_ratio", 1.08
        ),
        wide_profile_allograph_merge=config["clustering"].get(
            "wide_profile_allograph_merge", True
        ),
        wide_profile_bins=config["clustering"].get("wide_profile_bins", 32),
        wide_profile_min_correlation=config["clustering"].get(
            "wide_profile_min_correlation", 0.85
        ),
        split_inconsistent_types=config["clustering"].get(
            "split_inconsistent_types", True
        ),
    )
    processor = GlyphProcessor(processor_config)

    # Process images
    print("\nProcessing images...")
    instances, images = process_images(
        processor,
        image_paths,
        output_dir,
        save_glyphs=config["save_glyph_images"],
    )

    if not instances:
        print("\nNo glyphs detected in any images.")
        return 1

    print(f"\nTotal glyphs detected: {len(instances)}")

    # Build lexicon
    clustering_params = {
        "algorithm": "DBSCAN",
        "eps": config["clustering"]["eps"],
        "min_samples": config["clustering"]["min_samples"],
        "hu_sign_mode": config["clustering"].get("hu_sign_mode", "unsigned"),
        "same_line_allograph_merge": config["clustering"].get(
            "same_line_allograph_merge", True
        ),
        "split_wide_ligatures": config["clustering"].get(
            "split_wide_ligatures", True
        ),
        "split_fragment_allograph_merge": config["clustering"].get(
            "split_fragment_allograph_merge", True
        ),
        "wide_profile_allograph_merge": config["clustering"].get(
            "wide_profile_allograph_merge", True
        ),
        "split_inconsistent_types": config["clustering"].get(
            "split_inconsistent_types", True
        ),
    }
    lexicon = build_lexicon(processor, instances, images, output_dir, clustering_params)

    # Save lexicon
    print(f"\nSaving lexicon to: {output_file}")
    save_lexicon(lexicon, output_file)

    # Print summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Source images:        {len(lexicon.source_images)}")
    print(f"  Total glyphs:         {lexicon.total_glyphs_detected}")
    print(f"  Unique glyph types:   {lexicon.unique_glyph_types}")
    print(f"  Hapax legomena:       {lexicon.statistics.hapax_legomena}")
    print(f"  Avg glyphs/line:      {lexicon.statistics.avg_glyphs_per_line:.1f}")

    if lexicon.statistics.most_frequent_glyphs:
        top_glyphs = ", ".join(lexicon.statistics.most_frequent_glyphs[:5])
        print(f"  Most frequent:        {top_glyphs}")

    print(f"\nOutput saved to: {output_file}")
    if config["save_glyph_images"]:
        print(f"Glyph images saved to: {os.path.join(output_dir, 'glyphs')}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
