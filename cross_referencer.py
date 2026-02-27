#!/usr/bin/env python3
"""Symbolic Cross-Referencer - Links Rongorongo glyphs to Proto-Polynesian roots.

This script creates hypothetical associations between glyph clusters and linguistic
entries based on shape semantics. Since Rongorongo is undeciphered, all associations
are marked with confidence levels and supporting evidence.

Workflow:
    rongorongo_lexicon.json ──┐
                              ├──► cross_referencer.py ──► cross_reference_lexicon.json
    rapa_nui_language.json ───┘
"""

import argparse
import json
import os
import sys
from datetime import datetime

from config import CROSS_REFERENCE_CONFIG, GLYPH_CONFIG, LANGUAGE_CONFIG, OUTPUT_DIR
from models.cross_reference import CrossReferenceLexicon
from models.glyphs import RongorongoLexicon
from models.language import Etymology, LanguageEntry, Metadata, Translation
from processors.cross_reference_processor import CrossReferenceProcessor, ProcessorConfig


def load_glyph_lexicon(path: str) -> RongorongoLexicon:
    """Load the Rongorongo glyph lexicon from JSON.

    Args:
        path: Path to the glyph lexicon JSON file.

    Returns:
        RongorongoLexicon object.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        json.JSONDecodeError: If the file is invalid JSON.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return RongorongoLexicon.from_dict(data)


def load_language_entries(path: str) -> list[LanguageEntry]:
    """Load language entries from JSON.

    Args:
        path: Path to the language lexicon JSON file.

    Returns:
        List of LanguageEntry objects.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        json.JSONDecodeError: If the file is invalid JSON.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = []
    for entry_data in data.get("entries", []):
        # Parse translations
        translations = []
        for t in entry_data.get("translations", []):
            translations.append(
                Translation(
                    language=t.get("language", "en"),
                    text=t.get("text", ""),
                    gloss=t.get("gloss"),
                )
            )

        # Parse etymology if present
        etymology = None
        if entry_data.get("etymology"):
            etym_data = entry_data["etymology"]
            etymology = Etymology(
                origin=etym_data.get("origin"),
                cognates=etym_data.get("cognates", []),
                loan=etym_data.get("loan", False),
            )

        # Parse metadata if present
        metadata = None
        if entry_data.get("metadata"):
            meta_data = entry_data["metadata"]
            metadata = Metadata(
                source_url=meta_data.get("source_url", ""),
                source_name=meta_data.get("source_name", ""),
                scraped_at=meta_data.get("scraped_at", ""),
                confidence=meta_data.get("confidence", "medium"),
            )

        entry = LanguageEntry(
            word=entry_data.get("word", ""),
            normalized=entry_data.get("normalized", ""),
            ipa=entry_data.get("ipa"),
            translations=translations,
            part_of_speech=entry_data.get("part_of_speech"),
            semantic_category=entry_data.get("semantic_category"),
            etymology=etymology,
            metadata=metadata,
        )
        entries.append(entry)

    return entries


def save_lexicon(lexicon: CrossReferenceLexicon, output_path: str) -> None:
    """Save the cross-reference lexicon to JSON.

    Args:
        lexicon: The lexicon to save.
        output_path: Path to the output JSON file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(lexicon.to_dict(), f, indent=2, ensure_ascii=False)


def generate_report(lexicon: CrossReferenceLexicon, output_path: str) -> None:
    """Generate a markdown report of the cross-references.

    Args:
        lexicon: The cross-reference lexicon.
        output_path: Path to the output markdown file.
    """
    lines = [
        "# Rongorongo Cross-Reference Report",
        "",
        f"Generated: {datetime.now().isoformat()}",
        "",
        "## Methodology Warning",
        "",
        "> **Note:** Rongorongo is an undeciphered script. All associations in this",
        "> report are speculative hypotheses based on shape-semantic analysis.",
        "> These should be treated as research exploration tools, not established facts.",
        "",
        "## Statistics",
        "",
        f"- Total glyph profiles: {lexicon.statistics.total_glyphs_profiled}",
        f"- Total cross-references: {lexicon.statistics.total_cross_references}",
        "",
        "### By Confidence Level",
        "",
    ]

    for level, count in sorted(lexicon.statistics.by_confidence_level.items()):
        lines.append(f"- {level.title()}: {count}")

    lines.extend(
        [
            "",
            "### By Shape Category",
            "",
        ]
    )

    for category, count in sorted(lexicon.statistics.by_shape_category.items()):
        lines.append(f"- {category.title()}: {count}")

    lines.extend(
        [
            "",
            "### By Semantic Domain",
            "",
        ]
    )

    for domain, count in sorted(lexicon.statistics.by_semantic_domain.items()):
        lines.append(f"- {domain.title()}: {count}")

    lines.extend(
        [
            "",
            "## Cross-References",
            "",
        ]
    )

    # Group by confidence level
    by_level = {}
    for xref in lexicon.cross_references:
        level = xref.confidence_level
        if level not in by_level:
            by_level[level] = []
        by_level[level].append(xref)

    # Output in order of confidence (highest first)
    level_order = ["strong", "plausible", "tentative", "speculative"]

    for level in level_order:
        if level not in by_level:
            continue

        lines.extend(
            [
                f"### {level.title()} Associations",
                "",
            ]
        )

        for xref in by_level[level]:
            lines.append(
                f"#### {xref.glyph_cluster_id} → {xref.language_entry_word}"
            )
            lines.append("")
            lines.append(f"- **Reference ID:** {xref.reference_id}")
            lines.append(f"- **Confidence:** {xref.overall_confidence:.1%}")
            lines.append(f"- **Semantic Domain:** {xref.semantic_domain}")

            if xref.proto_polynesian_root:
                lines.append(f"- **Proto-Polynesian:** {xref.proto_polynesian_root}")

            lines.append("")
            lines.append("**Evidence:**")
            lines.append("")

            for ev in xref.evidence:
                lines.append(
                    f"- [{ev.evidence_type.value}] {ev.description} "
                    f"(strength: {ev.strength:.1%})"
                )

            if xref.notes:
                lines.append("")
                lines.append(f"*Notes: {xref.notes}*")

            lines.append("")

    # Write report
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> int:
    """Main entry point for the cross-referencer.

    Returns:
        Exit code (0 for success, 1 for failure).
    """
    # Ensure UTF-8 output on Windows
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")

    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Create symbolic cross-references between Rongorongo glyphs "
        "and Proto-Polynesian linguistic roots."
    )
    parser.add_argument(
        "--glyph-lexicon",
        default=os.path.join(OUTPUT_DIR, GLYPH_CONFIG["output_file"]),
        help="Path to the glyph lexicon JSON file",
    )
    parser.add_argument(
        "--language-lexicon",
        default=os.path.join(OUTPUT_DIR, LANGUAGE_CONFIG["rapa_nui"]["output_file"]),
        help="Path to the language lexicon JSON file",
    )
    parser.add_argument(
        "--annotations",
        default=os.path.join("input", CROSS_REFERENCE_CONFIG["annotations_file"]),
        help="Path to optional shape annotations YAML file",
    )
    parser.add_argument(
        "--output",
        default=os.path.join(OUTPUT_DIR, CROSS_REFERENCE_CONFIG["output_file"]),
        help="Path to output cross-reference lexicon JSON file",
    )
    parser.add_argument(
        "--report",
        default=os.path.join(OUTPUT_DIR, CROSS_REFERENCE_CONFIG["report_file"]),
        help="Path to output markdown report file",
    )
    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Skip generating the markdown report",
    )
    parser.add_argument(
        "--min-confidence",
        type=float,
        default=0.1,
        help="Minimum confidence threshold for cross-references (default: 0.1)",
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Rongorongo Symbolic Cross-Referencer")
    print("=" * 60)

    # Check input files exist
    if not os.path.exists(args.glyph_lexicon):
        print(f"\nError: Glyph lexicon not found: {args.glyph_lexicon}")
        print("Run glyph_cataloger.py first to generate the glyph lexicon.")
        return 1

    if not os.path.exists(args.language_lexicon):
        print(f"\nError: Language lexicon not found: {args.language_lexicon}")
        print("Run language_scraper.py first to generate the language lexicon.")
        return 1

    # Load glyph lexicon
    print(f"\nLoading glyph lexicon: {args.glyph_lexicon}")
    try:
        glyph_lexicon = load_glyph_lexicon(args.glyph_lexicon)
        print(f"  Loaded {len(glyph_lexicon.clusters)} glyph clusters")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"  Error loading glyph lexicon: {e}")
        return 1

    # Load language entries
    print(f"\nLoading language lexicon: {args.language_lexicon}")
    try:
        language_entries = load_language_entries(args.language_lexicon)
        print(f"  Loaded {len(language_entries)} language entries")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"  Error loading language lexicon: {e}")
        return 1

    # Initialize processor
    processor_config = ProcessorConfig(
        min_confidence_threshold=args.min_confidence,
    )
    processor = CrossReferenceProcessor(processor_config)

    # Load annotations if available
    if os.path.exists(args.annotations):
        print(f"\nLoading shape annotations: {args.annotations}")
        processor.load_annotations(args.annotations)
    else:
        print(f"\nNo shape annotations file found at {args.annotations}")
        print("  Using default (undetermined) shape tags for all glyphs")

    # Process cross-references
    print("\nGenerating cross-references...")
    lexicon = processor.process(glyph_lexicon, language_entries)

    # Set source file references
    lexicon.glyph_lexicon_file = os.path.basename(args.glyph_lexicon)
    lexicon.language_lexicon_file = os.path.basename(args.language_lexicon)

    # Save lexicon
    print(f"\nSaving cross-reference lexicon: {args.output}")
    save_lexicon(lexicon, args.output)

    # Generate report
    if not args.no_report and CROSS_REFERENCE_CONFIG.get("generate_report", True):
        print(f"Generating report: {args.report}")
        generate_report(lexicon, args.report)

    # Print summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  Glyph profiles created:    {lexicon.statistics.total_glyphs_profiled}")
    print(f"  Cross-references created:  {lexicon.statistics.total_cross_references}")

    if lexicon.statistics.by_confidence_level:
        print("\n  By confidence level:")
        for level in ["strong", "plausible", "tentative", "speculative"]:
            count = lexicon.statistics.by_confidence_level.get(level, 0)
            if count > 0:
                print(f"    {level.title():12} {count}")

    if lexicon.statistics.by_shape_category:
        print("\n  By shape category:")
        for category, count in sorted(
            lexicon.statistics.by_shape_category.items(),
            key=lambda x: x[1],
            reverse=True,
        ):
            print(f"    {category.title():16} {count}")

    print("\n" + "-" * 60)
    print("NOTE: Rongorongo is undeciphered. All associations are speculative")
    print("and should be used for research exploration only.")
    print("-" * 60)

    print(f"\nOutput saved to: {args.output}")
    if not args.no_report:
        print(f"Report saved to: {args.report}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
