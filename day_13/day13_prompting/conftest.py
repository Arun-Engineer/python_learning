"""Shared fixtures for Day 13 tests."""

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_classifier_client():
    """OpenAI client mock that returns a predetermined category."""
    def make_client(returned_text: str):
        fake_client = MagicMock()
        fake_response = MagicMock()
        fake_response.choices = [MagicMock()]
        fake_response.choices[0].message = MagicMock()
        fake_response.choices[0].message.content = returned_text
        fake_client.chat.completions.create.return_value = fake_response
        return fake_client
    return make_client