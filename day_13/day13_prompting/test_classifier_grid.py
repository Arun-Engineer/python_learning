"""Prompt eval grid: parameterize the classifier over many inputs."""

import pytest
from prompt_strategies import zero_shot

# This is the eval grid: 10 test cases coverin the category space
CLASSIFIER_TEST_GRID = [
    # (ticket, expected_category_contains)
    ("Login page crashes with 500 error",              "bug"),
    ("Please add Hindi Languagae",                     "feature"),
    ("How do I change my email address?",              "question"),
    ("The submit button does nothing on Firefox",      "bug"),
    ("Can you add a dark mode toggle?",                "feature"),
    ("Where is the user manual?",                      "question"),
    ("Payment fails for cards from HDFC bank",         "bug"),
    ("Add export to PDF",                              "feature"),
    ("What does P0 mean in the docs?",                 "question"),
    ("Search results show items I deleted yesterday",  "bug"),
]


@pytest.mark.parametrize("ticket, expected_keyword", CLASSIFIER_TEST_GRID)
def test_classifier_response_contains_correct_category(
    mock_classifier_client, ticket, expected_keyword
):
    """The classifier should respond with the right category keyword.
    
    Note: we use 'contains' instead of '==' because LLM output isn't deterministic.
    The category word should be in the response but punctuation/phrasing varies.
    """

    # Build a mock that returns the expected category - to verify our assertion
    # logic works. (In Phase B well graduate to real-API eval tests.)
    fake_client = mock_classifier_client(returned_text = f"This looks like a {expected_keyword}.")
    result = zero_shot(fake_client, ticket)

    assert expected_keyword.lower() in result.lower(), \
        f"Expected '{expected_keyword}' in response for ticket: {ticket!r}"