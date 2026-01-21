"""Tests for agent orchestrator."""

import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from agents.orchestrator import (
    AgentOrchestrator,
    RefinementCycle,
    IterationReport,
    create_standard_feedback_function,
)
from agents.base import BaseAgent, LLMMessage, LLMResponse
from agents.base.providers import MockProvider


class SimpleTestAgent(BaseAgent):
    """Simple agent for testing orchestration."""

    AGENT_NAME = "test_agent"
    VERSION = "1.0.0"

    def __init__(self, llm_provider, cache=None, confidence_boost=0.0):
        """Initialize with optional confidence boost."""
        super().__init__(llm_provider, cache)
        self.confidence_boost = confidence_boost

    def run(self, input_data: dict) -> dict:
        """Process input and optionally boost confidence."""
        refs = input_data.get("cross_references", input_data.get("validated_references", []))

        validated = []
        for ref in refs:
            new_ref = ref.copy()
            orig_conf = ref.get("validated_confidence", ref.get("overall_confidence", 0.5))
            new_ref["validated_confidence"] = min(1.0, orig_conf + self.confidence_boost)
            new_ref["original_confidence"] = orig_conf
            validated.append(new_ref)

        return {"validated_references": validated}

    def get_input_schema(self) -> dict:
        return {"type": "object", "properties": {"cross_references": {"type": "array"}}}

    def get_output_schema(self) -> dict:
        return {"type": "object", "properties": {"validated_references": {"type": "array"}}}


class TestIterationReport(unittest.TestCase):
    """Tests for IterationReport."""

    def test_create_report(self):
        """Test creating an iteration report."""
        report = IterationReport(
            iteration=1,
            agent_name="test_agent",
            started_at=datetime.now(),
        )

        self.assertEqual(report.iteration, 1)
        self.assertEqual(report.agent_name, "test_agent")
        self.assertIsNone(report.completed_at)
        self.assertEqual(len(report.changes_made), 0)

    def test_report_to_dict(self):
        """Test converting report to dictionary."""
        report = IterationReport(
            iteration=1,
            agent_name="test_agent",
            started_at=datetime(2024, 1, 1, 12, 0, 0),
            completed_at=datetime(2024, 1, 1, 12, 5, 0),
            changes_made=["change1", "change2"],
        )

        d = report.to_dict()

        self.assertEqual(d["iteration"], 1)
        self.assertEqual(d["agent_name"], "test_agent")
        self.assertEqual(len(d["changes_made"]), 2)


class TestRefinementCycle(unittest.TestCase):
    """Tests for RefinementCycle."""

    def test_create_cycle(self):
        """Test creating a refinement cycle."""
        cycle = RefinementCycle(
            cycle_id="test-123",
            started_at=datetime.now(),
        )

        self.assertEqual(cycle.cycle_id, "test-123")
        self.assertEqual(len(cycle.iterations), 0)
        self.assertEqual(len(cycle.convergence_metrics), 0)

    def test_cycle_to_dict(self):
        """Test converting cycle to dictionary."""
        cycle = RefinementCycle(
            cycle_id="test-123",
            started_at=datetime(2024, 1, 1, 12, 0, 0),
            completed_at=datetime(2024, 1, 1, 12, 30, 0),
            convergence_metrics={"converged": True},
        )

        d = cycle.to_dict()

        self.assertEqual(d["cycle_id"], "test-123")
        self.assertTrue(d["convergence_metrics"]["converged"])


class TestAgentOrchestrator(unittest.TestCase):
    """Tests for AgentOrchestrator."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.provider = MockProvider()
        self.orchestrator = AgentOrchestrator(
            llm_provider=self.provider,
            output_dir=self.temp_dir,
        )

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_register_agent(self):
        """Test registering an agent."""
        agent = SimpleTestAgent(self.provider)
        self.orchestrator.register_agent("test", agent)

        self.assertIn("test", self.orchestrator.agents)

    def test_run_sequence_single_agent(self):
        """Test running a single agent sequence."""
        agent = SimpleTestAgent(self.provider, confidence_boost=0.1)
        self.orchestrator.register_agent("test", agent)

        initial = {
            "cross_references": [
                {"reference_id": "XR001", "overall_confidence": 0.5},
            ]
        }

        result = self.orchestrator.run_sequence(["test"], initial)

        self.assertTrue(result["success"])
        self.assertIn("test", result["results"])

    def test_run_sequence_multiple_agents(self):
        """Test running multiple agents in sequence."""
        agent1 = SimpleTestAgent(self.provider, confidence_boost=0.1)
        agent2 = SimpleTestAgent(self.provider, confidence_boost=0.1)
        self.orchestrator.register_agent("agent1", agent1)
        self.orchestrator.register_agent("agent2", agent2)

        initial = {
            "cross_references": [
                {"reference_id": "XR001", "overall_confidence": 0.5},
            ]
        }

        result = self.orchestrator.run_sequence(["agent1", "agent2"], initial)

        self.assertTrue(result["success"])
        self.assertIn("agent1", result["results"])
        self.assertIn("agent2", result["results"])

    def test_run_sequence_unknown_agent(self):
        """Test running with unknown agent raises error."""
        with self.assertRaises(ValueError):
            self.orchestrator.run_sequence(["unknown"], {})

    def test_run_refinement_loop_single_iteration(self):
        """Test refinement loop with single iteration."""
        agent = SimpleTestAgent(self.provider, confidence_boost=0.1)
        self.orchestrator.register_agent("test", agent)

        initial = {
            "cross_references": [
                {"reference_id": "XR001", "overall_confidence": 0.5},
            ]
        }

        cycle = self.orchestrator.run_refinement_loop(
            agents=["test"],
            initial_input=initial,
            max_iterations=1,
        )

        self.assertIsInstance(cycle, RefinementCycle)
        self.assertEqual(len(cycle.iterations), 1)
        self.assertIsNotNone(cycle.completed_at)

    def test_run_refinement_loop_convergence(self):
        """Test refinement loop converges."""
        # Agent with no change (will converge immediately)
        agent = SimpleTestAgent(self.provider, confidence_boost=0.0)
        self.orchestrator.register_agent("test", agent)

        initial = {
            "cross_references": [
                {"reference_id": "XR001", "overall_confidence": 0.5},
            ]
        }

        cycle = self.orchestrator.run_refinement_loop(
            agents=["test"],
            initial_input=initial,
            max_iterations=5,
            convergence_threshold=0.01,
        )

        # Should converge early since no changes
        self.assertTrue(cycle.convergence_metrics.get("converged", False))

    def test_run_refinement_loop_tracks_changes(self):
        """Test refinement loop tracks changes."""
        agent = SimpleTestAgent(self.provider, confidence_boost=0.1)
        self.orchestrator.register_agent("test", agent)

        initial = {
            "cross_references": [
                {"reference_id": "XR001", "overall_confidence": 0.5},
            ]
        }

        cycle = self.orchestrator.run_refinement_loop(
            agents=["test"],
            initial_input=initial,
            max_iterations=2,
        )

        # First iteration should have changes
        if cycle.iterations:
            first = cycle.iterations[0]
            # Changes should be detected (confidence increased)
            self.assertTrue(
                len(first.changes_made) > 0 or
                cycle.final_confidence_scores.get("XR001", 0) > 0.5
            )

    def test_generate_iterative_report(self):
        """Test generating iterative report."""
        cycle = RefinementCycle(
            cycle_id="test-123",
            started_at=datetime(2024, 1, 1, 12, 0, 0),
            completed_at=datetime(2024, 1, 1, 12, 30, 0),
            iterations=[
                IterationReport(
                    iteration=1,
                    agent_name="test",
                    started_at=datetime(2024, 1, 1, 12, 0, 0),
                    completed_at=datetime(2024, 1, 1, 12, 5, 0),
                    changes_made=["XR001: confidence 0.50 -> 0.60"],
                ),
            ],
            final_confidence_scores={"XR001": 0.75},
            convergence_metrics={"converged": True},
        )

        report = self.orchestrator.generate_iterative_report(cycle)

        self.assertIn("test-123", report)
        self.assertIn("Final Confidence Scores", report)
        self.assertIn("75%", report)
        self.assertIn("Iteration History", report)

    def test_save_cycle(self):
        """Test saving cycle to file."""
        cycle = RefinementCycle(
            cycle_id="test-123",
            started_at=datetime(2024, 1, 1, 12, 0, 0),
            convergence_metrics={},
        )

        path = self.orchestrator.save_cycle(cycle)

        self.assertTrue(Path(path).exists())


class TestFeedbackFunction(unittest.TestCase):
    """Tests for feedback function."""

    def test_create_standard_feedback(self):
        """Test creating standard feedback function."""
        feedback_fn = create_standard_feedback_function()
        self.assertTrue(callable(feedback_fn))

    def test_feedback_with_validated_refs(self):
        """Test feedback function with validated references."""
        feedback_fn = create_standard_feedback_function()

        data = {
            "validated_references": [
                {"reference_id": "XR001", "validated_confidence": 0.2},
                {"reference_id": "XR002", "validated_confidence": 0.8},
            ]
        }

        feedback = feedback_fn("test_agent", data, {})

        self.assertIn("low_confidence_refs", feedback)
        self.assertIn("XR001", feedback["low_confidence_refs"])
        self.assertNotIn("XR002", feedback["low_confidence_refs"])

    def test_feedback_with_patterns(self):
        """Test feedback function with pattern data."""
        feedback_fn = create_standard_feedback_function()

        data = {
            "ngram_patterns": [
                {"sequence": ["G001", "G002"], "frequency": 10},
                {"sequence": ["G003", "G004"], "frequency": 3},
            ]
        }

        feedback = feedback_fn("test_agent", data, {})

        self.assertIn("high_frequency_patterns", feedback)
        self.assertEqual(feedback["high_frequency_patterns"], 1)


if __name__ == "__main__":
    unittest.main()
