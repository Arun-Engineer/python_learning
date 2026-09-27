# Test 1 - overlap_score(the scoring math)

import pytest
from block4 import overlap_score, is_faithful_sort, run_rag_eval_suite

# OVERLAP_CASES = [
#     ("a b c", "a b c d", 1.0),
#     ("a x", "a b c", 0.5),
#     ("x y", "a b c", 0.0),
# ]

# @pytest.mark.parametrize("answer, doc, expected", OVERLAP_CASES)
# def test_overlap(answer, doc, expected):
#     assert overlap_score(answer, doc) == expected

# FAITHFUL_CASES = [
#     ("a b c", "a b c d", True),
#     ("a x", "a b c", False),
#     ("a b x", "a b c", True),
# ]

# @pytest.mark.parametrize("answer, doc, expected", FAITHFUL_CASES)
# def test_is_faithful_sort(answer, doc, expected):
#     assert is_faithful_sort(answer, doc) == expected

TEST_CASES = [
    {
        "retrieved":["d1"],
        "correct_doc": "d1",
        "answer": "a b",
        "source_doc": "a b c",
    },
    {
        "retrieved": ["d2"],
        "correct_doc": "d1",
        "answer": "x y",
        "source_doc": "a b c",
    },
]

def test_run_rag_eval_suite():
    result = run_rag_eval_suite(TEST_CASES)
    assert result["total_cases"] == 2
    assert result["recall_passed"] == 1
    assert result["avg_faithfulness"] == 0.5
