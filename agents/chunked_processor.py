"""Chunked processor for handling large datasets without overload."""

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional, Iterator, Callable, TypeVar, Generic

from .base import BaseAgent, LLMProvider, LLMCache


T = TypeVar("T")


@dataclass
class ChunkResult:
    """Result from processing a single chunk."""

    chunk_index: int
    chunk_size: int
    start_index: int
    end_index: int
    success: bool
    result: Optional[dict] = None
    error: Optional[str] = None
    processing_time_seconds: float = 0.0


@dataclass
class ChunkedProcessingResult:
    """Aggregated result from processing all chunks."""

    total_items: int
    chunk_size: int
    total_chunks: int
    successful_chunks: int
    failed_chunks: int
    chunk_results: list[ChunkResult] = field(default_factory=list)
    aggregated_result: Optional[dict] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "total_items": self.total_items,
            "chunk_size": self.chunk_size,
            "total_chunks": self.total_chunks,
            "successful_chunks": self.successful_chunks,
            "failed_chunks": self.failed_chunks,
            "chunk_results": [
                {
                    "chunk_index": c.chunk_index,
                    "chunk_size": c.chunk_size,
                    "start_index": c.start_index,
                    "end_index": c.end_index,
                    "success": c.success,
                    "error": c.error,
                    "processing_time_seconds": c.processing_time_seconds,
                }
                for c in self.chunk_results
            ],
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
        }


class ChunkedProcessor:
    """
    Processes large datasets in chunks to avoid memory overload.

    Useful for:
    - Large glyph lexicons
    - Many cross-references
    - Extensive pattern mining
    """

    def __init__(
        self,
        chunk_size: int = 50,
        overlap: int = 0,
        progress_callback: Optional[Callable[[int, int], None]] = None,
    ):
        """
        Initialize the chunked processor.

        Args:
            chunk_size: Number of items per chunk
            overlap: Items to overlap between chunks (for context)
            progress_callback: Optional callback(current, total) for progress
        """
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.progress_callback = progress_callback

    def chunk_items(self, items: list) -> Iterator[tuple[int, int, list]]:
        """
        Yield chunks of items with their indices.

        Args:
            items: List to chunk

        Yields:
            Tuples of (start_index, end_index, chunk)
        """
        total = len(items)
        step = max(1, self.chunk_size - self.overlap)

        for start in range(0, total, step):
            end = min(start + self.chunk_size, total)
            yield start, end, items[start:end]

            if end >= total:
                break

    def process_with_agent(
        self,
        agent: BaseAgent,
        items: list,
        item_key: str,
        base_input: Optional[dict] = None,
        aggregator: Optional[Callable[[list[dict]], dict]] = None,
    ) -> ChunkedProcessingResult:
        """
        Process items through an agent in chunks.

        Args:
            agent: Agent to use for processing
            items: Items to process
            item_key: Key name for items in agent input
            base_input: Base input dict to merge with chunk
            aggregator: Function to aggregate chunk results

        Returns:
            Aggregated results from all chunks
        """
        result = ChunkedProcessingResult(
            total_items=len(items),
            chunk_size=self.chunk_size,
            total_chunks=0,
            successful_chunks=0,
            failed_chunks=0,
            started_at=datetime.now(),
        )

        chunk_outputs = []
        chunks = list(self.chunk_items(items))
        result.total_chunks = len(chunks)

        for i, (start, end, chunk) in enumerate(chunks):
            chunk_start = datetime.now()

            # Prepare input
            chunk_input = (base_input or {}).copy()
            chunk_input[item_key] = chunk
            chunk_input["chunk_info"] = {
                "index": i,
                "start": start,
                "end": end,
                "total_chunks": result.total_chunks,
            }

            # Process chunk
            try:
                output = agent.execute(chunk_input)
                success = output.get("success", False)

                chunk_result = ChunkResult(
                    chunk_index=i,
                    chunk_size=len(chunk),
                    start_index=start,
                    end_index=end,
                    success=success,
                    result=output if success else None,
                    error=output.get("error") if not success else None,
                    processing_time_seconds=(datetime.now() - chunk_start).total_seconds(),
                )

                if success:
                    result.successful_chunks += 1
                    chunk_outputs.append(output)
                else:
                    result.failed_chunks += 1

            except Exception as e:
                chunk_result = ChunkResult(
                    chunk_index=i,
                    chunk_size=len(chunk),
                    start_index=start,
                    end_index=end,
                    success=False,
                    error=str(e),
                    processing_time_seconds=(datetime.now() - chunk_start).total_seconds(),
                )
                result.failed_chunks += 1

            result.chunk_results.append(chunk_result)

            # Progress callback
            if self.progress_callback:
                self.progress_callback(i + 1, result.total_chunks)

        result.completed_at = datetime.now()

        # Aggregate results
        if aggregator and chunk_outputs:
            result.aggregated_result = aggregator(chunk_outputs)
        elif chunk_outputs:
            result.aggregated_result = self._default_aggregator(chunk_outputs)

        return result

    def _default_aggregator(self, chunk_outputs: list[dict]) -> dict:
        """Default aggregation: merge lists, sum numbers."""
        aggregated = {}

        for output in chunk_outputs:
            for key, value in output.items():
                if key in ("success", "run_metadata", "chunk_info"):
                    continue

                if isinstance(value, list):
                    if key not in aggregated:
                        aggregated[key] = []
                    aggregated[key].extend(value)
                elif isinstance(value, (int, float)):
                    if key not in aggregated:
                        aggregated[key] = 0
                    aggregated[key] += value
                elif isinstance(value, dict):
                    if key not in aggregated:
                        aggregated[key] = {}
                    aggregated[key].update(value)

        return aggregated


def create_cross_reference_aggregator() -> Callable[[list[dict]], dict]:
    """Create aggregator for cross-reference validation results."""

    def aggregator(outputs: list[dict]) -> dict:
        """Aggregate cross-reference validation results."""
        all_validated = []
        all_candidates = []
        total_stats = {
            "total_validated": 0,
            "confidence_improved": 0,
            "confidence_decreased": 0,
            "confidence_unchanged": 0,
            "etymologies_verified": 0,
            "new_candidates_found": 0,
        }

        for output in outputs:
            validated = output.get("validated_references", [])
            all_validated.extend(validated)

            candidates = output.get("new_candidates", [])
            all_candidates.extend(candidates)

            stats = output.get("statistics", {})
            for key in total_stats:
                if key in stats:
                    total_stats[key] += stats[key]

        # Deduplicate by reference_id
        seen_refs = set()
        unique_validated = []
        for ref in all_validated:
            ref_id = ref.get("reference_id")
            if ref_id and ref_id not in seen_refs:
                seen_refs.add(ref_id)
                unique_validated.append(ref)

        return {
            "validated_references": unique_validated,
            "new_candidates": all_candidates,
            "statistics": total_stats,
        }

    return aggregator


def create_pattern_mining_aggregator() -> Callable[[list[dict]], dict]:
    """Create aggregator for pattern mining results."""

    def aggregator(outputs: list[dict]) -> dict:
        """Aggregate pattern mining results."""
        all_ngrams = []
        all_structural = []
        all_visual = []

        for output in outputs:
            all_ngrams.extend(output.get("ngram_patterns", []))
            all_structural.extend(output.get("structural_patterns", []))
            all_visual.extend(output.get("visual_clusters", []))

        # Merge and deduplicate n-grams
        ngram_map = {}
        for pattern in all_ngrams:
            seq = tuple(pattern.get("sequence", []))
            if seq in ngram_map:
                ngram_map[seq]["frequency"] += pattern.get("frequency", 0)
            else:
                ngram_map[seq] = pattern.copy()

        return {
            "ngram_patterns": list(ngram_map.values()),
            "structural_patterns": all_structural,
            "visual_clusters": all_visual,
        }

    return aggregator


class IterativeConfidenceReporter:
    """
    Generates iterative confidence reports in the requested format.

    Example output:
    'Glyph 076 maps to 'mana' (power) with 75% confidence based on 50 occurrences.'
    """

    def __init__(self, output_dir: str = "output"):
        """Initialize the reporter."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.report_history: list[dict] = []

    def generate_report(
        self,
        validated_references: list[dict],
        glyph_lexicon: Optional[dict] = None,
        iteration: Optional[int] = None,
    ) -> str:
        """
        Generate an iterative confidence report.

        Args:
            validated_references: List of validated cross-references
            glyph_lexicon: Optional glyph lexicon for occurrence data
            iteration: Optional iteration number

        Returns:
            Formatted report string
        """
        lines = []

        if iteration is not None:
            lines.append(f"## Iteration {iteration} Report")
            lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            lines.append("")

        # Get occurrence data from lexicon
        occurrence_map = {}
        if glyph_lexicon:
            for cluster in glyph_lexicon.get("clusters", []):
                cluster_id = cluster.get("cluster_id")
                frequency = cluster.get("frequency", 0)
                if cluster_id:
                    occurrence_map[cluster_id] = frequency

        # Sort by confidence descending
        sorted_refs = sorted(
            validated_references,
            key=lambda r: r.get("validated_confidence", r.get("overall_confidence", 0)),
            reverse=True,
        )

        for ref in sorted_refs:
            glyph_id = ref.get("glyph_cluster_id", "unknown")
            word = ref.get("language_entry_word", "unknown")
            meaning = ref.get("semantic_domain", "")
            confidence = ref.get("validated_confidence", ref.get("overall_confidence", 0))
            occurrences = occurrence_map.get(glyph_id, "unknown")

            pct = int(confidence * 100)

            # Format: 'Glyph 076 maps to 'mana' (power) with 75% confidence based on 50 occurrences.'
            if meaning:
                line = f"Glyph {glyph_id} maps to '{word}' ({meaning}) with {pct}% confidence"
            else:
                line = f"Glyph {glyph_id} maps to '{word}' with {pct}% confidence"

            if occurrences != "unknown":
                line += f" based on {occurrences} occurrences."
            else:
                line += "."

            lines.append(line)

        report = "\n".join(lines)

        # Store in history
        self.report_history.append({
            "iteration": iteration,
            "timestamp": datetime.now().isoformat(),
            "reference_count": len(validated_references),
            "report": report,
        })

        return report

    def generate_comparison_report(
        self,
        previous_refs: list[dict],
        current_refs: list[dict],
    ) -> str:
        """Generate a comparison report showing confidence changes."""
        lines = ["## Confidence Changes Report", ""]

        # Build maps
        prev_map = {
            r.get("reference_id"): r.get("validated_confidence", r.get("overall_confidence", 0))
            for r in previous_refs
        }

        changes = []
        for ref in current_refs:
            ref_id = ref.get("reference_id")
            curr_conf = ref.get("validated_confidence", ref.get("overall_confidence", 0))
            prev_conf = prev_map.get(ref_id)

            if prev_conf is not None:
                change = curr_conf - prev_conf
                if abs(change) > 0.01:
                    changes.append({
                        "reference_id": ref_id,
                        "word": ref.get("language_entry_word", "unknown"),
                        "previous": prev_conf,
                        "current": curr_conf,
                        "change": change,
                    })

        # Sort by absolute change
        changes.sort(key=lambda x: abs(x["change"]), reverse=True)

        improved = [c for c in changes if c["change"] > 0]
        decreased = [c for c in changes if c["change"] < 0]

        if improved:
            lines.append("### Improved Confidence")
            for c in improved[:10]:
                lines.append(
                    f"- {c['reference_id']} '{c['word']}': "
                    f"{int(c['previous']*100)}% -> {int(c['current']*100)}% "
                    f"(+{int(c['change']*100)}%)"
                )
            lines.append("")

        if decreased:
            lines.append("### Decreased Confidence")
            for c in decreased[:10]:
                lines.append(
                    f"- {c['reference_id']} '{c['word']}': "
                    f"{int(c['previous']*100)}% -> {int(c['current']*100)}% "
                    f"({int(c['change']*100)}%)"
                )
            lines.append("")

        if not improved and not decreased:
            lines.append("No significant confidence changes detected.")

        return "\n".join(lines)

    def save_report(
        self,
        report: str,
        filename: str = None,
        iteration: Optional[int] = None,
    ) -> str:
        """Save report to file."""
        if filename is None:
            if iteration is not None:
                filename = f"confidence_report_iter{iteration}.md"
            else:
                filename = f"confidence_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        path = self.output_dir / filename
        with open(path, "w", encoding="utf-8") as f:
            f.write(report)

        return str(path)

    def get_history_summary(self) -> str:
        """Get summary of report history."""
        if not self.report_history:
            return "No reports generated yet."

        lines = ["## Report History Summary", ""]
        for entry in self.report_history:
            lines.append(
                f"- Iteration {entry.get('iteration', 'N/A')}: "
                f"{entry['reference_count']} references at {entry['timestamp']}"
            )

        return "\n".join(lines)
