"""Mock LLM provider for testing."""

from typing import Callable, Optional

from ..llm_provider import LLMMessage, LLMProvider, LLMProviderFactory, LLMResponse


class MockProvider(LLMProvider):
    """
    Mock LLM provider for testing.

    Can be configured with custom responses or use default behavior.
    """

    def __init__(
        self,
        default_response: str = "Mock response",
        response_callback: Optional[Callable[[list[LLMMessage]], str]] = None,
        supports_vision: bool = True,
        model_name: str = "mock-model",
        tokens_per_message: int = 100,
        cost_per_token: float = 0.00001,
    ):
        """
        Initialize mock provider.

        Args:
            default_response: Default response text
            response_callback: Optional callback to generate dynamic responses
            supports_vision: Whether to report vision support
            model_name: Model name to report
            tokens_per_message: Simulated tokens per message
            cost_per_token: Simulated cost per token
        """
        self._default_response = default_response
        self._response_callback = response_callback
        self._supports_vision = supports_vision
        self._model_name = model_name
        self._tokens_per_message = tokens_per_message
        self._cost_per_token = cost_per_token
        self._call_history: list[dict] = []

    @property
    def name(self) -> str:
        return "mock"

    @property
    def supports_vision(self) -> bool:
        return self._supports_vision

    def complete(
        self,
        messages: list[LLMMessage],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        """Generate a mock completion."""
        # Record the call
        self._call_history.append({
            "messages": [m.to_dict() for m in messages],
            "max_tokens": max_tokens,
            "temperature": temperature,
        })

        # Generate response
        if self._response_callback:
            content = self._response_callback(messages)
        else:
            content = self._default_response

        # Calculate mock metrics
        input_tokens = len(messages) * self._tokens_per_message
        output_tokens = len(content.split()) * 2  # Rough estimate
        total_tokens = input_tokens + output_tokens
        cost = total_tokens * self._cost_per_token

        return LLMResponse(
            content=content,
            model=self._model_name,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=cost,
            cached=False,
        )

    def complete_with_vision(
        self,
        messages: list[LLMMessage],
        images: list[bytes],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        """Generate a mock completion with vision."""
        if not self._supports_vision:
            raise NotImplementedError("Mock provider configured without vision support")

        # Record the call with image info
        self._call_history.append({
            "messages": [m.to_dict() for m in messages],
            "images": [f"<{len(img)} bytes>" for img in images],
            "max_tokens": max_tokens,
            "temperature": temperature,
        })

        # Generate response
        if self._response_callback:
            content = self._response_callback(messages)
        else:
            content = f"{self._default_response} (with {len(images)} images)"

        # Calculate mock metrics (vision costs more)
        input_tokens = len(messages) * self._tokens_per_message + len(images) * 500
        output_tokens = len(content.split()) * 2
        total_tokens = input_tokens + output_tokens
        cost = total_tokens * self._cost_per_token * 2  # Vision costs 2x

        return LLMResponse(
            content=content,
            model=self._model_name,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=cost,
            cached=False,
        )

    def get_call_history(self) -> list[dict]:
        """Get history of all calls made to this provider."""
        return self._call_history.copy()

    def clear_history(self) -> None:
        """Clear call history."""
        self._call_history.clear()

    def set_response(self, response: str) -> None:
        """Set the default response for subsequent calls."""
        self._default_response = response

    def set_callback(
        self, callback: Optional[Callable[[list[LLMMessage]], str]]
    ) -> None:
        """Set or clear the response callback."""
        self._response_callback = callback


# Register with factory
LLMProviderFactory.register("mock", MockProvider)
