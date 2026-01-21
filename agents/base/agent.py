"""Base agent class for Rongorongo analysis agents."""

import hashlib
import json
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from .cache import LLMCache
from .llm_provider import LLMMessage, LLMProvider, LLMResponse


@dataclass
class AgentRunMetadata:
    """Metadata for a single agent run."""

    run_id: str
    agent_name: str
    agent_version: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    total_llm_calls: int = 0
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_cost_usd: float = 0.0
    cache_hits: int = 0
    status: str = "running"  # "running" | "completed" | "failed"
    error_message: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "run_id": self.run_id,
            "agent_name": self.agent_name,
            "agent_version": self.agent_version,
            "started_at": self.started_at.isoformat(),
            "completed_at": (
                self.completed_at.isoformat() if self.completed_at else None
            ),
            "total_llm_calls": self.total_llm_calls,
            "total_input_tokens": self.total_input_tokens,
            "total_output_tokens": self.total_output_tokens,
            "total_cost_usd": self.total_cost_usd,
            "cache_hits": self.cache_hits,
            "status": self.status,
            "error_message": self.error_message,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "AgentRunMetadata":
        """Create from dictionary."""
        return cls(
            run_id=data["run_id"],
            agent_name=data["agent_name"],
            agent_version=data["agent_version"],
            started_at=datetime.fromisoformat(data["started_at"]),
            completed_at=(
                datetime.fromisoformat(data["completed_at"])
                if data.get("completed_at")
                else None
            ),
            total_llm_calls=data.get("total_llm_calls", 0),
            total_input_tokens=data.get("total_input_tokens", 0),
            total_output_tokens=data.get("total_output_tokens", 0),
            total_cost_usd=data.get("total_cost_usd", 0.0),
            cache_hits=data.get("cache_hits", 0),
            status=data.get("status", "completed"),
            error_message=data.get("error_message"),
        )


class BaseAgent(ABC):
    """
    Base class for all Rongorongo analysis agents.

    Provides common functionality for LLM interaction, caching, and metrics.
    """

    AGENT_NAME: str = "base_agent"
    VERSION: str = "1.0.0"

    def __init__(
        self,
        llm_provider: LLMProvider,
        cache: Optional[LLMCache] = None,
    ):
        """
        Initialize the agent.

        Args:
            llm_provider: The LLM provider to use for completions
            cache: Optional cache for LLM responses
        """
        self.llm = llm_provider
        self.cache = cache
        self.metadata: Optional[AgentRunMetadata] = None

    @abstractmethod
    def run(self, input_data: dict) -> dict:
        """
        Execute the agent's main task.

        Args:
            input_data: Agent-specific input data

        Returns:
            Agent-specific output data
        """
        pass

    @abstractmethod
    def get_input_schema(self) -> dict:
        """
        Get JSON schema for expected input.

        Returns:
            JSON schema dictionary
        """
        pass

    @abstractmethod
    def get_output_schema(self) -> dict:
        """
        Get JSON schema for output format.

        Returns:
            JSON schema dictionary
        """
        pass

    def validate_input(self, input_data: dict) -> list[str]:
        """
        Validate input against schema.

        Args:
            input_data: Input to validate

        Returns:
            List of validation errors (empty if valid)
        """
        errors = []
        schema = self.get_input_schema()

        required = schema.get("required", [])
        for field_name in required:
            if field_name not in input_data:
                errors.append(f"Missing required field: {field_name}")

        return errors

    def _start_run(self) -> AgentRunMetadata:
        """Start a new run and initialize metadata."""
        self.metadata = AgentRunMetadata(
            run_id=str(uuid.uuid4()),
            agent_name=self.AGENT_NAME,
            agent_version=self.VERSION,
            started_at=datetime.now(),
        )
        return self.metadata

    def _complete_run(self, success: bool = True, error: Optional[str] = None) -> None:
        """Mark the current run as complete."""
        if self.metadata:
            self.metadata.completed_at = datetime.now()
            self.metadata.status = "completed" if success else "failed"
            self.metadata.error_message = error

    def _compute_cache_key(self, messages: list[LLMMessage], **kwargs) -> str:
        """Compute cache key for messages."""
        key_data = {
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "kwargs": kwargs,
        }
        key_json = json.dumps(key_data, sort_keys=True)
        return hashlib.sha256(key_json.encode()).hexdigest()[:32]

    def _call_llm(
        self,
        messages: list[LLMMessage],
        max_tokens: int = 4096,
        temperature: float = 0.0,
        use_cache: bool = True,
    ) -> LLMResponse:
        """
        Call LLM with caching and metrics tracking.

        Args:
            messages: Conversation messages
            max_tokens: Maximum response tokens
            temperature: Sampling temperature
            use_cache: Whether to use cache

        Returns:
            LLM response
        """
        # Try cache first
        if use_cache and self.cache:
            cached = self.cache.get(
                messages, max_tokens=max_tokens, temperature=temperature
            )
            if cached:
                if self.metadata:
                    self.metadata.cache_hits += 1
                return cached

        # Make API call
        response = self.llm.complete(
            messages, max_tokens=max_tokens, temperature=temperature
        )

        # Update metrics
        if self.metadata:
            self.metadata.total_llm_calls += 1
            self.metadata.total_input_tokens += response.input_tokens
            self.metadata.total_output_tokens += response.output_tokens
            self.metadata.total_cost_usd += response.cost_usd

        # Cache response
        if use_cache and self.cache:
            self.cache.set(
                messages, response, max_tokens=max_tokens, temperature=temperature
            )

        return response

    def _call_llm_with_vision(
        self,
        messages: list[LLMMessage],
        images: list[bytes],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        """
        Call LLM with image inputs.

        Note: Vision calls are not cached due to image data size.

        Args:
            messages: Conversation messages
            images: List of image bytes
            max_tokens: Maximum response tokens
            temperature: Sampling temperature

        Returns:
            LLM response
        """
        response = self.llm.complete_with_vision(
            messages, images, max_tokens=max_tokens, temperature=temperature
        )

        # Update metrics
        if self.metadata:
            self.metadata.total_llm_calls += 1
            self.metadata.total_input_tokens += response.input_tokens
            self.metadata.total_output_tokens += response.output_tokens
            self.metadata.total_cost_usd += response.cost_usd

        return response

    def execute(self, input_data: dict) -> dict:
        """
        Execute the agent with full lifecycle management.

        This method handles:
        - Input validation
        - Run metadata
        - Error handling
        - Output formatting

        Args:
            input_data: Agent-specific input

        Returns:
            Output with run_metadata included
        """
        # Validate input
        errors = self.validate_input(input_data)
        if errors:
            return {
                "success": False,
                "errors": errors,
                "run_metadata": None,
            }

        # Start run
        self._start_run()

        try:
            # Execute agent logic
            result = self.run(input_data)

            # Complete successfully
            self._complete_run(success=True)

            # Add metadata to result
            result["run_metadata"] = self.metadata.to_dict()
            result["success"] = True

            return result

        except Exception as e:
            # Complete with error
            self._complete_run(success=False, error=str(e))

            return {
                "success": False,
                "error": str(e),
                "run_metadata": self.metadata.to_dict() if self.metadata else None,
            }
