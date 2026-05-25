"""Shared pytest fixture for the day12_capstone tests."""

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_openai_client():
    """A fake OpenAi client that returns a predictable response."""
    fake_client = MagicMock()

    # Build the fake response shape:
    # response.choices[0].messgage.content == This is a fake GPT response.
    fake_response = MagicMock()
    fake_response.choices = [MagicMock()]
    fake_response.choices[0].message = MagicMock()
    fake_response.choices[0].message.content = "This is a fake GPT response."

    fake_client.chat.completions.create.return_value = fake_response
    return fake_client

@pytest.fixture
def sample_question() -> str:
    """A resuable sample question for tests."""
    return "What is a Python?"