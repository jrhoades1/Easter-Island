"""Tests for agent base infrastructure."""

import tempfile
import unittest
from datetime import datetime

from agents.base import (
    AgentRunMetadata,
    BaseAgent,
    LLMCache,
    LLMMessage,
    LLMProviderFactory,
    LLMResponse,
)
from agents.base.providers import MockProvider


class TestLLMMessage(unittest.TestCase):
    """Tests for LLMMessage dataclass."""

    def test_create_basic_message(self):
        """Test creating a basic message."""
        msg = LLMMessage(role="user", content="Hello")
        self.assertEqual(msg.role, "user")
        self.assertEqual(msg.content, "Hello")
        self.assertIsNone(msg.images)

    def test_create_message_with_images(self):
        """Test creating a message with images."""
        images = [b"image1", b"image2"]
        msg = LLMMessage(role="user", content="Analyze", images=images)
        self.assertEqual(len(msg.images), 2)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        msg = LLMMessage(role="assistant", content="Response")
        d = msg.to_dict()
        self.assertEqual(d["role"], "assistant")
        self.assertEqual(d["content"], "Response")

    def test_to_dict_with_images(self):
        """Test to_dict includes image info."""
        msg = LLMMessage(role="user", content="Test", images=[b"abc"])
        d = msg.to_dict()
        self.assertIn("images", d)
        self.assertEqual(d["images"], ["<3 bytes>"])


class TestLLMResponse(unittest.TestCase):
    """Tests for LLMResponse dataclass."""

    def test_create_response(self):
        """Test creating a response."""
        resp = LLMResponse(
            content="Answer",
            model="test-model",
            input_tokens=100,
            output_tokens=50,
            cost_usd=0.001,
        )
        self.assertEqual(resp.content, "Answer")
        self.assertEqual(resp.model, "test-model")
        self.assertFalse(resp.cached)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        resp = LLMResponse(
            content="Answer",
            model="test",
            input_tokens=10,
            output_tokens=5,
            cost_usd=0.0001,
            cached=True,
        )
        d = resp.to_dict()
        self.assertEqual(d["content"], "Answer")
        self.assertTrue(d["cached"])

    def test_from_dict(self):
        """Test creation from dictionary."""
        d = {
            "content": "Test",
            "model": "model-1",
            "input_tokens": 20,
            "output_tokens": 10,
            "cost_usd": 0.002,
            "cached": False,
        }
        resp = LLMResponse.from_dict(d)
        self.assertEqual(resp.content, "Test")
        self.assertEqual(resp.model, "model-1")


class TestMockProvider(unittest.TestCase):
    """Tests for MockProvider."""

    def test_provider_name(self):
        """Test provider name."""
        provider = MockProvider()
        self.assertEqual(provider.name, "mock")

    def test_supports_vision(self):
        """Test vision support flag."""
        provider = MockProvider(supports_vision=True)
        self.assertTrue(provider.supports_vision)

        provider = MockProvider(supports_vision=False)
        self.assertFalse(provider.supports_vision)

    def test_complete_default_response(self):
        """Test complete with default response."""
        provider = MockProvider(default_response="Test response")
        messages = [LLMMessage(role="user", content="Hello")]
        response = provider.complete(messages)
        self.assertEqual(response.content, "Test response")

    def test_complete_with_callback(self):
        """Test complete with custom callback."""
        def callback(msgs):
            return f"Got {len(msgs)} messages"

        provider = MockProvider(response_callback=callback)
        messages = [
            LLMMessage(role="system", content="You are helpful"),
            LLMMessage(role="user", content="Hi"),
        ]
        response = provider.complete(messages)
        self.assertEqual(response.content, "Got 2 messages")

    def test_call_history(self):
        """Test that calls are recorded."""
        provider = MockProvider()
        messages = [LLMMessage(role="user", content="Test")]
        provider.complete(messages)

        history = provider.get_call_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["messages"][0]["content"], "Test")

    def test_clear_history(self):
        """Test clearing call history."""
        provider = MockProvider()
        provider.complete([LLMMessage(role="user", content="Test")])
        provider.clear_history()
        self.assertEqual(len(provider.get_call_history()), 0)

    def test_complete_with_vision(self):
        """Test vision completion."""
        provider = MockProvider()
        messages = [LLMMessage(role="user", content="Describe")]
        images = [b"fake_image"]
        response = provider.complete_with_vision(messages, images)
        self.assertIn("1 images", response.content)

    def test_complete_with_vision_disabled(self):
        """Test vision completion when disabled."""
        provider = MockProvider(supports_vision=False)
        messages = [LLMMessage(role="user", content="Describe")]
        images = [b"fake_image"]
        with self.assertRaises(NotImplementedError):
            provider.complete_with_vision(messages, images)


class TestLLMProviderFactory(unittest.TestCase):
    """Tests for LLMProviderFactory."""

    def test_register_and_create(self):
        """Test registering and creating providers."""
        # Mock is already registered
        self.assertTrue(LLMProviderFactory.is_registered("mock"))

    def test_create_mock_provider(self):
        """Test creating mock provider."""
        provider = LLMProviderFactory.create("mock")
        self.assertEqual(provider.name, "mock")

    def test_create_unknown_provider(self):
        """Test creating unknown provider raises error."""
        with self.assertRaises(ValueError):
            LLMProviderFactory.create("unknown_provider")

    def test_list_providers(self):
        """Test listing registered providers."""
        providers = LLMProviderFactory.list_providers()
        self.assertIn("mock", providers)


class TestLLMCache(unittest.TestCase):
    """Tests for LLMCache."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.cache = LLMCache(cache_dir=self.temp_dir, ttl_hours=1)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_cache_miss(self):
        """Test cache miss returns None."""
        messages = [LLMMessage(role="user", content="Test")]
        result = self.cache.get(messages)
        self.assertIsNone(result)

    def test_cache_hit(self):
        """Test cache hit returns response."""
        messages = [LLMMessage(role="user", content="Test")]
        response = LLMResponse(
            content="Answer",
            model="test",
            input_tokens=10,
            output_tokens=5,
            cost_usd=0.001,
        )
        self.cache.set(messages, response)

        cached = self.cache.get(messages)
        self.assertIsNotNone(cached)
        self.assertEqual(cached.content, "Answer")
        self.assertTrue(cached.cached)
        self.assertEqual(cached.cost_usd, 0.0)  # Cached responses have zero cost

    def test_cache_with_kwargs(self):
        """Test cache differentiates by kwargs."""
        messages = [LLMMessage(role="user", content="Test")]
        response1 = LLMResponse("A", "m", 10, 5, 0.001)
        response2 = LLMResponse("B", "m", 10, 5, 0.001)

        self.cache.set(messages, response1, temperature=0.0)
        self.cache.set(messages, response2, temperature=0.5)

        cached1 = self.cache.get(messages, temperature=0.0)
        cached2 = self.cache.get(messages, temperature=0.5)

        self.assertEqual(cached1.content, "A")
        self.assertEqual(cached2.content, "B")

    def test_cache_stats(self):
        """Test cache statistics."""
        messages = [LLMMessage(role="user", content="Test")]
        response = LLMResponse("A", "m", 10, 5, 0.001)

        self.cache.set(messages, response)
        self.cache.get(messages)  # Hit
        self.cache.get([LLMMessage(role="user", content="Other")])  # Miss

        stats = self.cache.get_stats()
        self.assertEqual(stats["total_hits"], 1)
        self.assertEqual(stats["total_misses"], 1)
        self.assertEqual(stats["entries"], 1)

    def test_cache_clear(self):
        """Test clearing cache."""
        messages = [LLMMessage(role="user", content="Test")]
        response = LLMResponse("A", "m", 10, 5, 0.001)
        self.cache.set(messages, response)

        self.cache.clear()

        self.assertIsNone(self.cache.get(messages))
        self.assertEqual(self.cache.get_stats()["entries"], 0)

    def test_cache_persistence(self):
        """Test cache persists to disk."""
        messages = [LLMMessage(role="user", content="Persist test")]
        response = LLMResponse("Persisted", "m", 10, 5, 0.001)
        self.cache.set(messages, response)

        # Create new cache instance
        new_cache = LLMCache(cache_dir=self.temp_dir, ttl_hours=1)
        cached = new_cache.get(messages)

        self.assertIsNotNone(cached)
        self.assertEqual(cached.content, "Persisted")


class TestAgentRunMetadata(unittest.TestCase):
    """Tests for AgentRunMetadata."""

    def test_create_metadata(self):
        """Test creating metadata."""
        metadata = AgentRunMetadata(
            run_id="test-123",
            agent_name="test_agent",
            agent_version="1.0.0",
            started_at=datetime.now(),
        )
        self.assertEqual(metadata.run_id, "test-123")
        self.assertEqual(metadata.status, "running")
        self.assertIsNone(metadata.completed_at)

    def test_to_dict(self):
        """Test conversion to dictionary."""
        metadata = AgentRunMetadata(
            run_id="test-123",
            agent_name="test_agent",
            agent_version="1.0.0",
            started_at=datetime(2024, 1, 1, 12, 0, 0),
            total_llm_calls=5,
            total_cost_usd=0.01,
        )
        d = metadata.to_dict()
        self.assertEqual(d["run_id"], "test-123")
        self.assertEqual(d["total_llm_calls"], 5)
        self.assertIn("2024-01-01", d["started_at"])

    def test_from_dict(self):
        """Test creation from dictionary."""
        d = {
            "run_id": "test-456",
            "agent_name": "my_agent",
            "agent_version": "2.0.0",
            "started_at": "2024-01-15T10:00:00",
            "completed_at": "2024-01-15T10:05:00",
            "status": "completed",
        }
        metadata = AgentRunMetadata.from_dict(d)
        self.assertEqual(metadata.run_id, "test-456")
        self.assertEqual(metadata.status, "completed")


class ConcreteTestAgent(BaseAgent):
    """Concrete agent implementation for testing."""

    AGENT_NAME = "test_agent"
    VERSION = "1.0.0"

    def run(self, input_data: dict) -> dict:
        # Simple test: call LLM and return response
        messages = [LLMMessage(role="user", content=input_data.get("prompt", ""))]
        response = self._call_llm(messages)
        return {"response": response.content}

    def get_input_schema(self) -> dict:
        return {
            "type": "object",
            "required": ["prompt"],
            "properties": {"prompt": {"type": "string"}},
        }

    def get_output_schema(self) -> dict:
        return {
            "type": "object",
            "properties": {"response": {"type": "string"}},
        }


class TestBaseAgent(unittest.TestCase):
    """Tests for BaseAgent."""

    def test_create_agent(self):
        """Test creating an agent."""
        provider = MockProvider()
        agent = ConcreteTestAgent(provider)
        self.assertEqual(agent.AGENT_NAME, "test_agent")

    def test_validate_input_valid(self):
        """Test input validation with valid input."""
        provider = MockProvider()
        agent = ConcreteTestAgent(provider)
        errors = agent.validate_input({"prompt": "Hello"})
        self.assertEqual(len(errors), 0)

    def test_validate_input_missing_required(self):
        """Test input validation with missing required field."""
        provider = MockProvider()
        agent = ConcreteTestAgent(provider)
        errors = agent.validate_input({})
        self.assertEqual(len(errors), 1)
        self.assertIn("prompt", errors[0])

    def test_execute_success(self):
        """Test successful execution."""
        provider = MockProvider(default_response="Test answer")
        agent = ConcreteTestAgent(provider)
        result = agent.execute({"prompt": "Question"})

        self.assertTrue(result["success"])
        self.assertEqual(result["response"], "Test answer")
        self.assertIn("run_metadata", result)

    def test_execute_tracks_metrics(self):
        """Test that execution tracks metrics."""
        provider = MockProvider()
        agent = ConcreteTestAgent(provider)
        result = agent.execute({"prompt": "Test"})

        metadata = result["run_metadata"]
        self.assertEqual(metadata["total_llm_calls"], 1)
        self.assertEqual(metadata["status"], "completed")

    def test_execute_with_cache(self):
        """Test execution with caching."""
        with tempfile.TemporaryDirectory() as temp_dir:
            provider = MockProvider(default_response="Cached response")
            cache = LLMCache(cache_dir=temp_dir)
            agent = ConcreteTestAgent(provider, cache)

            # First call
            result1 = agent.execute({"prompt": "Same question"})
            # Second call (should hit cache)
            result2 = agent.execute({"prompt": "Same question"})

            # Both should have same response
            self.assertEqual(result1["response"], result2["response"])

    def test_execute_validation_failure(self):
        """Test execution with validation failure."""
        provider = MockProvider()
        agent = ConcreteTestAgent(provider)
        result = agent.execute({})  # Missing required 'prompt'

        self.assertFalse(result["success"])
        self.assertIn("errors", result)


if __name__ == "__main__":
    unittest.main()
