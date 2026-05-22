#!/usr/bin/env python3
"""Rongorongo Corpus Statistics - command-line analysis tool.

Computes descriptive statistics for a transliterated Rongorongo corpus:
sign frequencies, n-grams, recurring sequences, and positional tendencies.

This tool is intentionally *descriptive only*. It reports the statistical
structure of the script and makes no claim about what any glyph means.
Rongorongo remains undeciphered.

Usage:
    python corpus_stats.py --corpus data/corpus/ --output output/
    python corpus_stats.py --corpus data/corpus/sample_synthetic.rrt
"""

import argparse
import json
import sys
from pathlib import Path

from processors.corpus_loader import CorpusFormatError, load_corpus
from processors.corpus_statistics import CorpusStatistics, CorpusStatisticsReport


def _format_report(report: CorpusStatisticsReport) -> str:
    """Render a human-readable text summary of the statistics report."""
    lines: list[str] = []
    add = lines.append

    add("=" * 64)
    add("RONGORONGO CORPUS STATISTICS")
    add("=" * 64)
    if report.is_synthetic:
        add("")
        add("  *** WARNING: corpus contains SYNTHETIC (non-attested) data. ***")
        add("  *** Results are for pipeline testing only, not research.   ***")
    add("")
    add(f"  Tablets............ {report.tablet_count}")
    add(f"  Lines.............. {report.line_count}")
    add(f"  Tokens (written)... {report.total_tokens}")
    add(f"  Glyphs (decomposed) {report.total_glyphs}")
    add(f"  Unique glyphs...... {report.unique_glyphs}")
    add(f"  Hapax legomena..... {report.hapax_count}")
    add(f"  Type/token ratio... {report.type_token_ratio:.4f}")
    add(f"  Ligature tokens.... {report.ligature_token_count}")
    add(f"  Zipf correlation... {report.zipf_correlation:+.3f}  "
        f"(near -1.0 = language-like distribution)")
    ll = report.line_length
    add(f"  Line length........ min {ll['min']}, max {ll['max']}, "
        f"mean {ll['mean']}, stdev {ll['stdev']}")

    add("")
    add("-" * 64)
    add("SIGN FREQUENCY (top entries)")
    add("-" * 64)
    add(f"  {'rank':>4}  {'glyph':<12} {'count':>7}  {'relative':>9}")
    for entry in report.frequency_table:
        add(f"  {entry.rank:>4}  {entry.glyph:<12} {entry.count:>7}  "
            f"{entry.relative:>8.3%}")

    if report.ngrams:
        add("")
        add("-" * 64)
        add("RECURRING N-GRAMS")
        add("-" * 64)
        for n in sorted(report.ngrams):
            add(f"  {n}-grams:")
            for seq, freq in report.ngrams[n][:8]:
                add(f"    {' '.join(seq):<40} x{freq}")

    if report.repeated_sequences:
        add("")
        add("-" * 64)
        add("MAXIMAL REPEATED SEQUENCES (candidate formulae / parallelism)")
        add("-" * 64)
        for rep in report.repeated_sequences[:10]:
            add(f"  [{rep.length} glyphs x{rep.frequency}]  "
                f"{' '.join(rep.sequence)}")
            add(f"      lines: {', '.join(rep.lines)}")

    if report.positional:
        add("")
        add("-" * 64)
        add("POSITIONAL DISTRIBUTION (top glyphs)")
        add("-" * 64)
        add(f"  {'glyph':<12} {'count':>6}  {'initial':>8} {'medial':>8} "
            f"{'final':>8}")
        for pos in report.positional:
            add(f"  {pos.glyph:<12} {pos.count:>6}  {pos.initial:>7.1%} "
                f"{pos.medial:>7.1%} {pos.final:>7.1%}")

    add("")
    add("=" * 64)
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    """Entry point for the corpus statistics CLI."""
    parser = argparse.ArgumentParser(
        description="Compute descriptive statistics for a transliterated "
        "Rongorongo corpus.",
    )
    parser.add_argument(
        "--corpus",
        default="data/corpus",
        help="Path to a .rrt file or a directory of .rrt files "
        "(default: data/corpus).",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Directory to write corpus_statistics.json (optional).",
    )
    parser.add_argument(
        "--max-ngram",
        type=int,
        default=5,
        help="Largest n-gram size to extract (default: 5).",
    )
    parser.add_argument(
        "--min-frequency",
        type=int,
        default=2,
        help="Minimum count for an n-gram to be reported (default: 2).",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=25,
        help="Number of rows in top-N tables (default: 25).",
    )
    args = parser.parse_args(argv)

    corpus_path = Path(args.corpus)
    if not corpus_path.exists():
        print(f"Error: corpus path not found: {corpus_path}", file=sys.stderr)
        return 1

    try:
        corpus = load_corpus([corpus_path])
    except CorpusFormatError as exc:
        print(f"Error: failed to parse corpus: {exc}", file=sys.stderr)
        return 1

    if not corpus.tablets:
        print(f"Error: no .rrt tablets found at {corpus_path}", file=sys.stderr)
        return 1

    stats = CorpusStatistics(
        max_ngram=args.max_ngram,
        min_ngram_frequency=args.min_frequency,
        top_k=args.top_k,
    )
    report = stats.analyze(corpus)

    print(_format_report(report))

    if args.output:
        out_dir = Path(args.output)
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "corpus_statistics.json"
        out_file.write_text(
            json.dumps(report.to_dict(), indent=2), encoding="utf-8"
        )
        print(f"\nWrote {out_file}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
