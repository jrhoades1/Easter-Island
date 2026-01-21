"""
LLM-powered agents for Rongorongo glyph analysis.

This package provides three independent agents:
- GlyphSegmentationAgent: Enhance CV segmentation with LLM-guided decisions
- PatternMiningAgent: Discover n-gram sequences, structural patterns, visual clusters
- LexicalValidationAgent: Validate against expanded Polynesian corpora

Plus orchestration and processing utilities:
- AgentOrchestrator: Feedback loops for iterative refinement
- ChunkedProcessor: Handle large datasets without overload
- IterativeConfidenceReporter: Generate confidence reports
"""

from agents.base import (
    LLMProvider,
    LLMProviderFactory,
    LLMMessage,
    LLMResponse,
    BaseAgent,
    AgentRunMetadata,
    LLMCache,
)
from agents.orchestrator import (
    AgentOrchestrator,
    RefinementCycle,
    IterationReport,
    create_standard_feedback_function,
)
from agents.chunked_processor import (
    ChunkedProcessor,
    ChunkedProcessingResult,
    ChunkResult,
    IterativeConfidenceReporter,
    create_cross_reference_aggregator,
    create_pattern_mining_aggregator,
)

__all__ = [
    # Base components
    "LLMProvider",
    "LLMProviderFactory",
    "LLMMessage",
    "LLMResponse",
    "BaseAgent",
    "AgentRunMetadata",
    "LLMCache",
    # Orchestration
    "AgentOrchestrator",
    "RefinementCycle",
    "IterationReport",
    "create_standard_feedback_function",
    # Chunked processing
    "ChunkedProcessor",
    "ChunkedProcessingResult",
    "ChunkResult",
    "IterativeConfidenceReporter",
    "create_cross_reference_aggregator",
    "create_pattern_mining_aggregator",
]
