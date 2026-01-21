"""OpenAI GPT LLM provider."""

import base64
import os
from typing import Optional

from ..llm_provider import LLMMessage, LLMProvider, LLMProviderFactory, LLMResponse


# Pricing per 1M tokens (as of 2024)
OPENAI_PRICING = {
    "gpt-4o": {"input": 5.00, "output": 15.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4-turbo": {"input": 10.00, "output": 30.00},
    "gpt-4": {"input": 30.00, "output": 60.00},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
}

DEFAULT_MODEL = "gpt-4o"


class OpenAIProvider(LLMProvider):
    """
    OpenAI GPT LLM provider.

    Requires the 'openai' package and OPENAI_API_KEY environment variable.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = DEFAULT_MODEL,
        organization: Optional[str] = None,
    ):
        """
        Initialize OpenAI provider.

        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: Model ID to use
            organization: Optional organization ID
        """
        self._api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self._model = model
        self._organization = organization or os.environ.get("OPENAI_ORGANIZATION")
        self._client = None

        if not self._api_key:
            raise ValueError(
                "OpenAI API key required. Set OPENAI_API_KEY environment "
                "variable or pass api_key parameter."
            )

    def _get_client(self):
        """Lazy-load the OpenAI client."""
        if self._client is None:
            try:
                import openai
            except ImportError:
                raise ImportError(
                    "openai package required. Install with: pip install openai"
                )
            kwargs = {"api_key": self._api_key}
            if self._organization:
                kwargs["organization"] = self._organization
            self._client = openai.OpenAI(**kwargs)
        return self._client

    @property
    def name(self) -> str:
        return "openai"

    @property
    def supports_vision(self) -> bool:
        # GPT-4o and GPT-4-turbo support vision
        return self._model in ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo"]

    def _calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Calculate cost in USD."""
        pricing = OPENAI_PRICING.get(
            self._model,
            OPENAI_PRICING[DEFAULT_MODEL],
        )
        input_cost = (input_tokens / 1_000_000) * pricing["input"]
        output_cost = (output_tokens / 1_000_000) * pricing["output"]
        return input_cost + output_cost

    def _convert_messages(self, messages: list[LLMMessage]) -> list[dict]:
        """Convert LLMMessages to OpenAI format."""
        converted = []

        for msg in messages:
            if msg.images:
                # Vision message with images
                content = []

                # Add text first
                if msg.content:
                    content.append({"type": "text", "text": msg.content})

                # Add images
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

                    b64_image = base64.b64encode(img_bytes).decode("utf-8")
                    content.append({
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{media_type};base64,{b64_image}",
                        },
                    })

                converted.append({"role": msg.role, "content": content})
            else:
                # Standard text message
                converted.append({"role": msg.role, "content": msg.content})

        return converted

    def complete(
        self,
        messages: list[LLMMessage],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        """Generate a completion using GPT."""
        client = self._get_client()
        converted_messages = self._convert_messages(messages)

        response = client.chat.completions.create(
            model=self._model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=converted_messages,
        )

        # Extract content
        content = response.choices[0].message.content or ""

        # Get token usage
        input_tokens = response.usage.prompt_tokens
        output_tokens = response.usage.completion_tokens
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
        if not self.supports_vision:
            raise NotImplementedError(
                f"Model {self._model} does not support vision. "
                "Use gpt-4o, gpt-4o-mini, or gpt-4-turbo."
            )

        # Add images to the last user message
        enhanced_messages = []
        for i, msg in enumerate(messages):
            if i == len(messages) - 1 and msg.role == "user":
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
LLMProviderFactory.register("openai", OpenAIProvider)
