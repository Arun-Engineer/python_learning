import pytest
from unittest.mock import MagicMock

@pytest.fixture
def knowledge_base() -> dict:
    """Known true facts to check AI answers against."""
    return{
        "what is the capital of France?": "Paris",
        "Who was the first US president?": "George Washington",
    }

@pytest.fixture
def fake_client():
    """A fake client so tests runs fast, free, and identical every time."""
    return MagicMock()