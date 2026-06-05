import pytest

from probelms import count_word_lengths

@pytest.mark.parametrize("words, expected",
    [
        ([], {}),
        (["hi"], {2: 1}),
        (["hi", "ok"], {2: 2}),
        (["a", "bb", "ccc", "dd"], {1: 1, 2: 2, 3: 1})
    ],
)

def test_count_word_len(words, expected):
    """Count word lengths should map word length to count, across all 4 inputs."""
    result = count_word_lengths(words)
    assert result == expected