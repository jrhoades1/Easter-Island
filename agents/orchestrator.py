"""Agent Orchestrator for iterative refinement loops between agents."""

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable, Optional

from .base import BaseAgent, LLMCache, LLMProvider


@dataclass
class IterationReport:
    """Report for a single iteration of refinement."""

    iteration: int
    agent_name: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    input_summary: str = ""
    output_summary: str = ""
    changes_made: list[str] = field(default_factory=list)
    metrics: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "iteration": self.iteration,
            "agent_name": self.agent_name,
            "started_at": self.started_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "input_summary": self.input_summary,
            "output_summary": self.output_summary,
            "changes_made": self.changes_made,
            "metrics": self.metrics,
        }


@dataclass
class RefinementCycle:
    """A complete refinement cycle across agents."""

    cycle_id: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    iterations: list[IterationReport] = field(default_factory=list)
    convergence_metrics: dict = field(default_factory=dict)
    final_confidence_scores: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "cycle_id": self.cycle_id,
            "started_at": self.started_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "iterations": [i.to_dict() for i in self.iterations],
            "convergence_metrics": self.convergence_metrics,
            "final_confidence_scores": self.final_confidence_scores,
        }


class AgentOrchestrator:
    """
    Orchestrates iterative refinement loops between Rongorongo analysis agents.

    Supports:
    - Sequential agent execution
    - Feedback loops where agents refine each other's outputs
    - Convergence detection
    - Iterative confidence reporting
    """

    def __init__(
        self,
        llm_provider: LLMProvider,
        cache: Optional[LLMCache] = None,
        output_dir: str = "output",
    ):
        """
        Initialize the orchestrator.

        Args:
            llm_provider: Shared LLM provider for all agents
            cache: Shared cache
            output_dir: Directory for output files
        """
        self.llm_provider = llm_provider
        self.cache = cache
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.agents: dict[str, BaseAgent] = {}
        self.cycle_history: list[RefinementCycle] = []

    def register_agent(self, name: str, agent: BaseAgent) -> None:
        """Register an agent for orchestration."""
        self.agents[name] = agent

    def run_sequence(
        self,
        agent_sequence: list[str],
        initial_input: dict,
        transform_output: Optional[Callable[[str, dict], dict]] = None,
    ) -> dict:
        """
        Run agents in sequence, passing output to next agent.

        Args:
            agent_sequence: List of agent names to execute in order
            initial_input: Input for first agent
            transform_output: Optional function to transform output between agents

        Returns:
            Final output from last agent
        """
        current_input = initial_input
        results = {}

        for agent_name in agent_sequence:
            if agent_name not in self.agents:
                raise ValueError(f"Unknown agent: {agent_name}")

            agent = self.agents[agent_name]
            result = agent.execute(current_input)
            results[agent_name] = result

            if not result.get("success"):
                return {
                    "success": False,
                    "error": f"Agent {agent_name} failed: {result.get('error')}",
                    "partial_results": results,
                }

            # Transform output for next agent
            if transform_output:
                current_input = transform_output(agent_name, result)
            else:
                current_input = result

        return {
            "success": True,
            "results": results,
            "final_output": current_input,
        }

    def run_refinement_loop(
        self,
        agents: list[str],
        initial_input: dict,
        max_iterations: int = 5,
        convergence_threshold: float = 0.01,
        feedback_fn: Optional[Callable[[str, dict, dict], dict]] = None,
    ) -> RefinementCycle:
        """
        Run iterative refinement loop where agents refine each other's outputs.

        Args:
            agents: Agents to include in the loop
            initial_input: Starting input data
            max_iterations: Maximum refinement iterations
            convergence_threshold: Stop when confidence changes below this
            feedback_fn: Function to generate feedback between agents

        Returns:
            Complete refinement cycle with all iterations
        """
        import uuid

        cycle = RefinementCycle(
            cycle_id=str(uuid.uuid4())[:8],
            started_at=datetime.now(),
        )

        current_data = initial_input
        previous_scores = {}

        for iteration in range(max_iterations):
            iteration_changed = False

            for agent_name in agents:
                if agent_name not in self.agents:
                    continue

                agent = self.agents[agent_name]
                report = IterationReport(
                    iteration=iteration + 1,
                    agent_name=agent_name,
                    started_at=datetime.now(),
                )

                # Prepare input with feedback from previous iteration
                agent_input = self._prepare_agent_input(
                    agent_name, current_data, feedback_fn
                )
                report.input_summary = self._summarize_input(agent_input)

                # Execute agent
                result = agent.execute(agent_input)
                report.completed_at = datetime.now()

                if result.get("success"):
                    # Track changes
                    changes = self._detect_changes(current_data, result, agent_name)
                    report.changes_made = changes
                    report.output_summary = self._summarize_output(result)
                    report.metrics = result.get("run_metadata", {})

                    if changes:
                        iteration_changed = True

                    # Update current data
                    current_data = self._merge_results(current_data, result, agent_name)

                cycle.iterations.append(report)

            # Check convergence
            current_scores = self._extract_confidence_scores(current_data)
            if self._check_convergence(previous_scores, current_scores, convergence_threshold):
                cycle.convergence_metrics["converged"] = True
                cycle.convergence_metrics["converged_at_iteration"] = iteration + 1
                break

            if not iteration_changed:
                cycle.convergence_metrics["converged"] = True
                cycle.convergence_metrics["reason"] = "no_changes"
                break

            previous_scores = current_scores

        cycle.completed_at = datetime.now()
        cycle.final_confidence_scores = self._extract_confidence_scores(current_data)
        cycle.convergence_metrics.setdefault("converged", False)
        cycle.convergence_metrics["total_iterations"] = len(cycle.iterations)

        self.cycle_history.append(cycle)
        return cycle

    def _prepare_agent_input(
        self,
        agent_name: str,
        current_data: dict,
        feedback_fn: Optional[Callable] = None,
    ) -> dict:
        """Prepare input for an agent, including any feedback."""
        base_input = current_data.copy()

        if feedback_fn:
            feedback = feedback_fn(agent_name, current_data, {})
            base_input["feedback"] = feedback

        return base_input

    def _detect_changes(
        self,
        previous: dict,
        current: dict,
        agent_name: str,
    ) -> list[str]:
        """Detect significant changes between iterations."""
        changes = []

        # Check for confidence changes
        prev_refs = previous.get("validated_references", previous.get("cross_references", []))
        curr_refs = current.get("validated_references", [])

        if isinstance(prev_refs, list) and isinstance(curr_refs, list):
            for curr in curr_refs:
                ref_id = curr.get("reference_id")
                prev_conf = None

                for prev in prev_refs:
                    if prev.get("reference_id") == ref_id:
                        prev_conf = prev.get("validated_confidence", prev.get("overall_confidence"))
                        break

                curr_conf = curr.get("validated_confidence")
                if prev_conf is not None and curr_conf is not None:
                    if abs(curr_conf - prev_conf) > 0.05:
                        changes.append(
                            f"{ref_id}: confidence {prev_conf:.2f} -> {curr_conf:.2f}"
                        )

        return changes

    def _merge_results(
        self,
        current_data: dict,
        new_result: dict,
        agent_name: str,
    ) -> dict:
        """Merge new agent results into current data."""
        merged = current_data.copy()

        # Store agent-specific results
        merged[f"{agent_name}_results"] = new_result

        # Update cross-references if this agent validated them
        if "validated_references" in new_result:
            merged["validated_references"] = new_result["validated_references"]

        # Update patterns if this agent found them
        if "ngram_patterns" in new_result:
            merged["ngram_patterns"] = new_result["ngram_patterns"]

        # Update segmentation if this agent refined it
        if "segmentation_results" in new_result:
            merged["segmentation_results"] = new_result["segmentation_results"]

        return merged

    def _extract_confidence_scores(self, data: dict) -> dict[str, float]:
        """Extract confidence scores from data."""
        scores = {}

        refs = data.get("validated_references", data.get("cross_references", []))
        if isinstance(refs, list):
            for ref in refs:
                ref_id = ref.get("reference_id", "")
                conf = ref.get("validated_confidence", ref.get("overall_confidence", 0))
                if ref_id:
                    scores[ref_id] = conf

        return scores

    def _check_convergence(
        self,
        previous: dict[str, float],
        current: dict[str, float],
        threshold: float,
    ) -> bool:
        """Check if confidence scores have converged."""
        if not previous:
            return False

        total_change = 0.0
        count = 0

        for ref_id, curr_score in current.items():
            if ref_id in previous:
                total_change += abs(curr_score - previous[ref_id])
                count += 1

        if count == 0:
            return False

        avg_change = total_change / count
        return avg_change < threshold

    def _summarize_input(self, input_data: dict) -> str:
        """Create a brief summary of input data."""
        parts = []

        if "cross_references" in input_data:
            refs = input_data["cross_references"]
            if isinstance(refs, dict):
                refs = refs.get("cross_references", [])
            parts.append(f"{len(refs)} cross-references")

        if "glyph_lexicon" in input_data:
            clusters = input_data["glyph_lexicon"].get("clusters", [])
            parts.append(f"{len(clusters)} glyph clusters")

        return ", ".join(parts) if parts else "standard input"

    def _summarize_output(self, output: dict) -> str:
        """Create a brief summary of output data."""
        parts = []

        if "validated_references" in output:
            parts.append(f"{len(output['validated_references'])} validated")

        if "new_candidates" in output:
            parts.append(f"{len(output['new_candidates'])} new candidates")

        if "ngram_patterns" in output:
            parts.append(f"{len(output['ngram_patterns'])} patterns")

        return ", ".join(parts) if parts else "completed"

    def generate_iterative_report(
        self,
        cycle: RefinementCycle,
        include_details: bool = True,
    ) -> str:
        """
        Generate iterative confidence report.

        Format: 'Glyph 076 maps to 'mana' (power) with 75% confidence based on 50 occurrences.'
        """
        lines = [
            f"# Refinement Cycle Report: {cycle.cycle_id}",
            "",
            f"**Started:** {cycle.started_at.strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Completed:** {cycle.completed_at.strftime('%Y-%m-%d %H:%M:%S') if cycle.completed_at else 'In progress'}",
            f"**Iterations:** {len(cycle.iterations)}",
            f"**Converged:** {cycle.convergence_metrics.get('converged', False)}",
            "",
            "## Final Confidence Scores",
            "",
        ]

        # Sort by confidence descending
        sorted_scores = sorted(
            cycle.final_confidence_scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        for ref_id, confidence in sorted_scores:
            # Format in the requested style
            pct = int(confidence * 100)
            lines.append(f"- {ref_id}: **{pct}%** confidence")

        if include_details:
            lines.extend([
                "",
                "## Iteration History",
                "",
            ])

            for report in cycle.iterations:
                lines.append(f"### Iteration {report.iteration}: {report.agent_name}")
                lines.append(f"- Input: {report.input_summary}")
                lines.append(f"- Output: {report.output_summary}")

                if report.changes_made:
                    lines.append("- Changes:")
                    for change in report.changes_made[:5]:
                        lines.append(f"  - {change}")
                    if len(report.changes_made) > 5:
                        lines.append(f"  - ... and {len(report.changes_made) - 5} more")

                lines.append("")

        return "\n".join(lines)

    def save_cycle(self, cycle: RefinementCycle, filename: str = None) -> str:
        """Save cycle results to JSON file."""
        if filename is None:
            filename = f"refinement_cycle_{cycle.cycle_id}.json"

        path = self.output_dir / filename
        with open(path, "w", encoding="utf-8") as f:
            json.dump(cycle.to_dict(), f, indent=2, ensure_ascii=False)

        return str(path)


def create_standard_feedback_function() -> Callable:
    """Create a standard feedback function for refinement loops."""

    def feedback_fn(agent_name: str, current_data: dict, _context: dict) -> dict:
        """Generate feedback based on current data state."""
        feedback = {"source": "orchestrator", "iteration_context": {}}

        # If we have validation results, provide them as feedback
        if "validated_references" in current_data:
            validated = current_data["validated_references"]
            low_confidence = [
                r for r in validated
                if r.get("validated_confidence", 0) < 0.3
            ]
            feedback["low_confidence_refs"] = [
                r.get("reference_id") for r in low_confidence
            ]
            feedback["suggestion"] = "Focus on improving low-confidence references"

        # If we have pattern results, provide them
        if "ngram_patterns" in current_data:
            patterns = current_data["ngram_patterns"]
            high_freq = [p for p in patterns if p.get("frequency", 0) > 5]
            feedback["high_frequency_patterns"] = len(high_freq)
            feedback["pattern_suggestion"] = "Consider pattern context in validation"

        return feedback

    return feedback_fn
