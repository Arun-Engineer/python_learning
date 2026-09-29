from unittest.mock import MagicMock
from semantic_faithfulness import semantic_faithfulness

def test_identical_vectors_score_1():
    # Arrange: a fake client that always returns the same vector

    fake_client = MagicMock()
    fake_client.embed.return_value = [1.0, 0.0, 0.0]

    # Act
    score= semantic_faithfulness("anything", "anything", fake_client)

    # Assert : identical vectors -> cosine should be ~1.0
    assert round(score, 3) == 1.0