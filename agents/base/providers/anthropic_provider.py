"""Anthropic Claude LLM provider."""

import base64
import os
from typing import Optional

from ..llm_provider import LLMMessage, LLMProvider, LLMProviderFactory, LLMResponse


# Pricing per 1M tokens (as of 2024)
ANTHROPIC_PRICING = {
    "claude-3-opus-20240229": {"input": 15.00, "output": 75.00},
    "claude-3-sonnet-20240229": {"input": 3.00, "output": 15.00},
    "claude-3-haiku-20240307": {"input": 0.25, "output": 1.25},
    "claude-3-5-sonnet-20241022": {"input": 3.00, "output": 15.00},
}

DEFAULT_MODEL = "claude-3-5-sonnet-20241022"


class AnthropicProvider(LLMProvider):
    """
    Anthropic Claude LLM provider.

    Requires the 'anthropic' package and ANTHROPIC_API_KEY environment variable.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = DEFAULT_MODEL,
    ):
        """
        Initialize Anthropic provider.

        Args:
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
            model: Model ID to use
        """
        self._api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self._model = model
        self._client = None

        if not self._api_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY environment "
                "variable or pass api_key parameter."
            )

    def _get_client(self):
        """Lazy-load the Anthropic client."""
        if self._client is None:
            try:
                import anthropic
            except ImportError:
                raise ImportError(
                    "anthropic package required. Install with: pip install anthropic"
                )
            self._client = anthropic.Anthropic(api_key=self._api_key)
        return self._client

    @property
    def name(self) -> str:
        return "anthropic"

    @property
    def supports_vision(self) -> bool:
        return True  # All Claude 3 models support vision

    def _calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Calculate cost in USD."""
        pricing = ANTHROPIC_PRICING.get(
            self._model,
            ANTHROPIC_PRICING[DEFAULT_MODEL],
        )
        input_cost = (input_tokens / 1_000_000) * pricing["input"]
        output_cost = (output_tokens / 1_000_000) * pricing["output"]
        return input_cost + output_cost

    def _convert_messages(self, messages: list[LLMMessage]) -> tuple[str, list[dict]]:
        """Convert LLMMessages to Anthropic format."""
        system_prompt = ""
        converted = []

        for msg in messages:
            if msg.role == "system":
                system_prompt = msg.content
            else:
                content = []

                # Add images if present
                if msg.images:
                    for img_bytes in msg.images:
                        # Detect image type from magic bytes
                        media_type = "image/png"
                        if img_bytes[:2] == b"\xff\xd8":
                            media_type = "image/jpeg"
                        elif img_bytes[:4] == b"\x89PNG":
                            media_type = "image/png"
                        elif img_bytes[:4] == b"GIF8":
                            media_type = "image/gif"
                        elif img_bytes[:4] == b"RIFF":
                            media_type = "image/webp"

                        content.append({
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": base64.b64encode(img_bytes).decode("utf-8"),
                            },
                        })

                # Add text content
                if msg.content:
                    content.append({"type": "text", "text": msg.content})

                # If no images, use simple string format
                if not msg.images:
                    converted.append({"role": msg.role, "content": msg.content})
                else:
                    converted.append({"role": msg.role, "content": content})

        return system_prompt, converted

    def complete(
        self,
        messages: list[LLMMessage],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        """Generate a completion using Claude."""
        client = self._get_client()
        system_prompt, converted_messages = self._convert_messages(messages)

        kwargs = {
            "model": self._model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": converted_messages,
        }

        if system_prompt:
            kwargs["system"] = system_prompt

        response = client.messages.create(**kwargs)

        # Extract content
        content = ""
        for block in response.content:
            if hasattr(block, "text"):
                content += block.text

        # Calculate cost
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens
        cost = self._calculate_cost(input_tokens, output_tokens)

        return LLMResponse(
            content=content,
            model=self._model,
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
        """Generate a completion with image inputs."""
        # Add images to the last user message
        enhanced_messages = []
        for i, msg in enumerate(messages):
            if i == len(messages) - 1 and msg.role == "user":
                # Add images to the last user message
                enhanced_messages.append(
                    LLMMessage(
                        role=msg.role,
                        content=msg.content,
                        images=images,
                    )
                )
            else:
                enhanced_messages.append(msg)

        return self.complete(enhanced_messages, max_tokens, temperature)


# Register with factory
LLMProviderFactory.register("anthropic", AnthropicProvider)
