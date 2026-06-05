import pytest

@pytest.mark.parametrize("ticket, expected_category", [
    ("Login broken for all users", "Bug"),
    ("Please add dark mode", "Feature Request"),
    ("How do i export data?", "Question"),
])

def test_classifier_categories_correctly(ticket, expected_category):
    result = classify(ticket)
    assert result == expected_category