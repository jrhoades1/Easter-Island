"""Abstract LLM provider interface and factory."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LLMMessage:
    """A message in an LLM conversation."""

    role: str  # "system" | "user" | "assistant"
    content: str
    images: Optional[list[bytes]] = field(default=None)  # For vision models

    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        result = {"role": self.role, "content": self.content}
        if self.images:
            result["images"] = [f"<{len(img)} bytes>" for img in self.images]
        return result


@dataclass
class LLMResponse:
    """Response from an LLM provider."""

    content: str
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    cached: bool = False

    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            "content": self.content,
            "model": self.model,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "cost_usd": self.cost_usd,
            "cached": self.cached,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "LLMResponse":
        """Create from dictionary representation."""
        return cls(
            content=data["content"],
            model=data["model"],
            input_tokens=data["input_tokens"],
            output_tokens=data["output_tokens"],
            cost_usd=data["cost_usd"],
            cached=data.get("cached", False),
        )


class LLMProvider(ABC):
    """Abstract interface for LLM providers."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Provider name (e.g., 'anthropic', 'openai')."""
        pass

    @property
    @abstractmethod
    def supports_vision(self) -> bool:
        """Whether provider supports image inputs."""
        pass

    @abstractmethod
    def complete(
        self,
        messages: list[LLMMessage],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        """
        Generate a completion from messages.

        Args:
            messages: List of conversation messages
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature (0.0 = deterministic)

        Returns:
            LLMResponse with content and usage metrics
        """
        pass

    def complete_with_vision(
        self,
        messages: list[LLMMessage],
        images: list[bytes],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        """
        Generate a completion with image inputs.

        Default implementation raises if vision not supported.

        Args:
            messages: List of conversation messages
            images: List of image bytes
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature

        Returns:
            LLMResponse with content and usage metrics

        Raises:
            NotImplementedError: If provider doesn't support vision
        """
        if not self.supports_vision:
            raise NotImplementedError(
                f"Provider {self.name} does not support vision inputs"
            )
        # Subclasses should override this
        raise NotImplementedError("Subclass must implement complete_with_vision")


class LLMProviderFactory:
    """Factory for creating LLM providers."""

    _providers: dict[str, type[LLMProvider]] = {}

    @classmethod
    def register(cls, name: str, provider_class: type[LLMProvider]) -> None:
        """
        Register a provider class.

        Args:
            name: Provider name (e.g., 'anthropic', 'openai')
            provider_class: The provider class to register
        """
        cls._providers[name] = provider_class

    @classmethod
    def create(cls, name: str, **kwargs) -> LLMProvider:
        """
        Create a provider instance.

        Args:
            name: Provider name
            **kwargs: Provider-specific configuration

        Returns:
            Configured LLMProvider instance

        Raises:
            ValueError: If provider name is not registered
        """
        if name not in cls._providers:
            available = ", ".join(cls._providers.keys()) or "none"
            raise ValueError(
                f"Unknown provider: {name}. Available providers: {available}"
            )
        return cls._providers[name](**kwargs)

    @classmethod
    def list_providers(cls) -> list[str]:
        """List all registered provider names."""
        return list(cls._providers.keys())

    @classmethod
    def is_registered(cls, name: str) -> bool:
        """Check if a provider is registered."""
        return name in cls._providers
