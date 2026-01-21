"""Tests for chunked processor and iterative confidence reporter."""

import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from agents.chunked_processor import (
    ChunkedProcessor,
    ChunkedProcessingResult,
    ChunkResult,
    IterativeConfidenceReporter,
    create_cross_reference_aggregator,
    create_pattern_mining_aggregator,
)
from agents.base import BaseAgent, LLMMessage
from agents.base.providers import MockProvider


class SimpleProcessingAgent(BaseAgent):
    """Simple agent for testing chunked processing."""

    AGENT_NAME = "simple_processor"
    VERSION = "1.0.0"

    def run(self, input_data: dict) -> dict:
        """Process items and return count."""
        items = input_data.get("items", [])
        chunk_info = input_data.get("chunk_info", {})

        return {
            "processed_count": len(items),
            "chunk_index": chunk_info.get("index", 0),
            "validated_references": [
                {
                    "reference_id": f"XR{i:03d}",
                    "validated_confidence": 0.5 + (i * 0.01),
                }
                for i in range(len(items))
            ],
        }

    def get_input_schema(self) -> dict:
        return {"type": "object", "properties": {"items": {"type": "array"}}}

    def get_output_schema(self) -> dict:
        return {"type": "object", "properties": {"processed_count": {"type": "integer"}}}


class TestChunkResult(unittest.TestCase):
    """Tests for ChunkResult dataclass."""

    def test_create_chunk_result(self):
        """Test creating a chunk result."""
        result = ChunkResult(
            chunk_index=0,
            chunk_size=10,
            start_index=0,
            end_index=10,
            success=True,
        )

        self.assertEqual(result.chunk_index, 0)
        self.assertEqual(result.chunk_size, 10)
        self.assertTrue(result.success)

    def test_chunk_result_with_error(self):
        """Test chunk result with error."""
        result = ChunkResult(
            chunk_index=1,
            chunk_size=10,
            start_index=10,
            end_index=20,
            success=False,
            error="Test error",
        )

        self.assertFalse(result.success)
        self.assertEqual(result.error, "Test error")


class TestChunkedProcessingResult(unittest.TestCase):
    """Tests for ChunkedProcessingResult."""

    def test_create_processing_result(self):
        """Test creating a processing result."""
        result = ChunkedProcessingResult(
            total_items=100,
            chunk_size=10,
            total_chunks=10,
            successful_chunks=8,
            failed_chunks=2,
        )

        self.assertEqual(result.total_items, 100)
        self.assertEqual(result.successful_chunks, 8)
        self.assertEqual(result.failed_chunks, 2)

    def test_processing_result_to_dict(self):
        """Test converting result to dictionary."""
        result = ChunkedProcessingResult(
            total_items=50,
            chunk_size=10,
            total_chunks=5,
            successful_chunks=5,
            failed_chunks=0,
            started_at=datetime(2024, 1, 1, 12, 0, 0),
            completed_at=datetime(2024, 1, 1, 12, 5, 0),
        )

        d = result.to_dict()

        self.assertEqual(d["total_items"], 50)
        self.assertEqual(d["total_chunks"], 5)
        self.assertIn("2024-01-01", d["started_at"])


class TestChunkedProcessor(unittest.TestCase):
    """Tests for ChunkedProcessor."""

    def setUp(self):
        """Set up test fixtures."""
        self.provider = MockProvider()
        self.processor = ChunkedProcessor(chunk_size=10)

    def test_chunk_items_basic(self):
        """Test basic chunking."""
        items = list(range(25))
        chunks = list(self.processor.chunk_items(items))

        self.assertEqual(len(chunks), 3)  # 10, 10, 5
        self.assertEqual(chunks[0][2], list(range(10)))
        self.assertEqual(chunks[1][2], list(range(10, 20)))
        self.assertEqual(chunks[2][2], list(range(20, 25)))

    def test_chunk_items_with_overlap(self):
        """Test chunking with overlap."""
        processor = ChunkedProcessor(chunk_size=10, overlap=2)
        items = list(range(25))
        chunks = list(processor.chunk_items(items))

        # With overlap, more chunks are created
        self.assertGreater(len(chunks), 2)

        # Check overlap
        first_end = chunks[0][1]
        second_start = chunks[1][0]
        self.assertLess(second_start, first_end)  # Overlap exists

    def test_chunk_items_exact_fit(self):
        """Test chunking when items fit exactly."""
        items = list(range(20))
        chunks = list(self.processor.chunk_items(items))

        self.assertEqual(len(chunks), 2)
        self.assertEqual(len(chunks[0][2]), 10)
        self.assertEqual(len(chunks[1][2]), 10)

    def test_chunk_items_smaller_than_chunk_size(self):
        """Test chunking with fewer items than chunk size."""
        items = list(range(5))
        chunks = list(self.processor.chunk_items(items))

        self.assertEqual(len(chunks), 1)
        self.assertEqual(len(chunks[0][2]), 5)

    def test_process_with_agent(self):
        """Test processing with agent."""
        agent = SimpleProcessingAgent(self.provider)
        items = list(range(25))

        result = self.processor.process_with_agent(
            agent=agent,
            items=items,
            item_key="items",
        )

        self.assertIsInstance(result, ChunkedProcessingResult)
        self.assertEqual(result.total_items, 25)
        self.assertEqual(result.total_chunks, 3)
        self.assertEqual(result.successful_chunks, 3)
        self.assertEqual(result.failed_chunks, 0)

    def test_process_with_agent_aggregates_results(self):
        """Test that results are aggregated."""
        agent = SimpleProcessingAgent(self.provider)
        items = list(range(25))

        result = self.processor.process_with_agent(
            agent=agent,
            items=items,
            item_key="items",
        )

        self.assertIsNotNone(result.aggregated_result)
        # Default aggregator should sum processed_count
        self.assertEqual(result.aggregated_result.get("processed_count"), 25)

    def test_process_with_progress_callback(self):
        """Test progress callback is called."""
        progress_calls = []

        def progress_callback(current, total):
            progress_calls.append((current, total))

        processor = ChunkedProcessor(chunk_size=10, progress_callback=progress_callback)
        agent = SimpleProcessingAgent(self.provider)
        items = list(range(25))

        processor.process_with_agent(agent, items, "items")

        self.assertEqual(len(progress_calls), 3)
        self.assertEqual(progress_calls[0], (1, 3))
        self.assertEqual(progress_calls[2], (3, 3))

    def test_process_with_custom_aggregator(self):
        """Test processing with custom aggregator."""
        def custom_aggregator(outputs):
            return {"total": sum(o.get("processed_count", 0) for o in outputs)}

        agent = SimpleProcessingAgent(self.provider)
        items = list(range(25))

        result = self.processor.process_with_agent(
            agent=agent,
            items=items,
            item_key="items",
            aggregator=custom_aggregator,
        )

        self.assertEqual(result.aggregated_result["total"], 25)

    def test_process_with_base_input(self):
        """Test processing with base input data."""
        agent = SimpleProcessingAgent(self.provider)
        items = list(range(10))
        base_input = {"extra_param": "value"}

        result = self.processor.process_with_agent(
            agent=agent,
            items=items,
            item_key="items",
            base_input=base_input,
        )

        self.assertTrue(result.successful_chunks > 0)


class TestCrossReferenceAggregator(unittest.TestCase):
    """Tests for cross-reference aggregator."""

    def test_aggregate_validated_references(self):
        """Test aggregating validated references."""
        aggregator = create_cross_reference_aggregator()

        outputs = [
            {
                "validated_references": [
                    {"reference_id": "XR001", "validated_confidence": 0.5},
                    {"reference_id": "XR002", "validated_confidence": 0.6},
                ],
                "statistics": {"total_validated": 2},
            },
            {
                "validated_references": [
                    {"reference_id": "XR003", "validated_confidence": 0.7},
                ],
                "statistics": {"total_validated": 1},
            },
        ]

        result = aggregator(outputs)

        self.assertEqual(len(result["validated_references"]), 3)
        self.assertEqual(result["statistics"]["total_validated"], 3)

    def test_deduplicates_references(self):
        """Test that duplicates are removed."""
        aggregator = create_cross_reference_aggregator()

        outputs = [
            {
                "validated_references": [
                    {"reference_id": "XR001", "validated_confidence": 0.5},
                ],
            },
            {
                "validated_references": [
                    {"reference_id": "XR001", "validated_confidence": 0.6},  # Duplicate
                ],
            },
        ]

        result = aggregator(outputs)

        # Should keep only one XR001
        self.assertEqual(len(result["validated_references"]), 1)


class TestPatternMiningAggregator(unittest.TestCase):
    """Tests for pattern mining aggregator."""

    def test_aggregate_ngrams(self):
        """Test aggregating n-gram patterns."""
        aggregator = create_pattern_mining_aggregator()

        outputs = [
            {
                "ngram_patterns": [
                    {"sequence": ["G001", "G002"], "frequency": 5},
                ],
            },
            {
                "ngram_patterns": [
                    {"sequence": ["G003", "G004"], "frequency": 3},
                ],
            },
        ]

        result = aggregator(outputs)

        self.assertEqual(len(result["ngram_patterns"]), 2)

    def test_merges_duplicate_ngrams(self):
        """Test that duplicate n-grams are merged."""
        aggregator = create_pattern_mining_aggregator()

        outputs = [
            {
                "ngram_patterns": [
                    {"sequence": ["G001", "G002"], "frequency": 5},
                ],
            },
            {
                "ngram_patterns": [
                    {"sequence": ["G001", "G002"], "frequency": 3},  # Same sequence
                ],
            },
        ]

        result = aggregator(outputs)

        # Should merge frequencies
        self.assertEqual(len(result["ngram_patterns"]), 1)
        self.assertEqual(result["ngram_patterns"][0]["frequency"], 8)


class TestIterativeConfidenceReporter(unittest.TestCase):
    """Tests for IterativeConfidenceReporter."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.reporter = IterativeConfidenceReporter(output_dir=self.temp_dir)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_generate_basic_report(self):
        """Test generating a basic report."""
        refs = [
            {
                "reference_id": "XR001",
                "glyph_cluster_id": "G076",
                "language_entry_word": "mana",
                "semantic_domain": "power",
                "validated_confidence": 0.75,
            },
        ]

        report = self.reporter.generate_report(refs)

        # Should match the requested format
        self.assertIn("G076", report)
        self.assertIn("mana", report)
        self.assertIn("power", report)
        self.assertIn("75%", report)

    def test_generate_report_with_occurrences(self):
        """Test generating report with occurrence data."""
        refs = [
            {
                "reference_id": "XR001",
                "glyph_cluster_id": "G076",
                "language_entry_word": "mana",
                "semantic_domain": "power",
                "validated_confidence": 0.75,
            },
        ]
        lexicon = {
            "clusters": [
                {"cluster_id": "G076", "frequency": 50},
            ]
        }

        report = self.reporter.generate_report(refs, glyph_lexicon=lexicon)

        # Should include occurrence count
        self.assertIn("50 occurrences", report)

    def test_generate_report_with_iteration(self):
        """Test generating report with iteration number."""
        refs = [
            {
                "reference_id": "XR001",
                "glyph_cluster_id": "G001",
                "language_entry_word": "manu",
                "validated_confidence": 0.8,
            },
        ]

        report = self.reporter.generate_report(refs, iteration=3)

        self.assertIn("Iteration 3", report)

    def test_generate_comparison_report(self):
        """Test generating comparison report."""
        prev_refs = [
            {"reference_id": "XR001", "language_entry_word": "manu", "validated_confidence": 0.5},
            {"reference_id": "XR002", "language_entry_word": "tangata", "validated_confidence": 0.6},
        ]
        curr_refs = [
            {"reference_id": "XR001", "language_entry_word": "manu", "validated_confidence": 0.7},
            {"reference_id": "XR002", "language_entry_word": "tangata", "validated_confidence": 0.55},
        ]

        report = self.reporter.generate_comparison_report(prev_refs, curr_refs)

        self.assertIn("Confidence Changes", report)
        self.assertIn("Improved Confidence", report)
        self.assertIn("Decreased Confidence", report)
        self.assertIn("manu", report)
        self.assertIn("tangata", report)

    def test_save_report(self):
        """Test saving report to file."""
        report = "Test report content"
        path = self.reporter.save_report(report)

        self.assertTrue(Path(path).exists())
        with open(path) as f:
            self.assertEqual(f.read(), report)

    def test_save_report_with_iteration(self):
        """Test saving report with iteration filename."""
        report = "Test report"
        path = self.reporter.save_report(report, iteration=5)

        self.assertIn("iter5", path)
        self.assertTrue(Path(path).exists())

    def test_report_history(self):
        """Test report history tracking."""
        refs = [{"reference_id": "XR001", "validated_confidence": 0.5}]

        self.reporter.generate_report(refs, iteration=1)
        self.reporter.generate_report(refs, iteration=2)

        self.assertEqual(len(self.reporter.report_history), 2)

    def test_get_history_summary(self):
        """Test getting history summary."""
        refs = [{"reference_id": "XR001", "validated_confidence": 0.5}]

        self.reporter.generate_report(refs, iteration=1)
        summary = self.reporter.get_history_summary()

        self.assertIn("Iteration 1", summary)


if __name__ == "__main__":
    unittest.main()
