import pytest
from block4 import evaluate_rag, recall_at_5,is_faithful

# ---- Recall Cases -------
RECALL_CASES = [
    (["a","b","policy_7","d","e"],"policy_7",True),
    (["a","b","c","d","e","policy_7"],"policy_7",False),
    (["a","b","c"],"missing",False),
]

@pytest.mark.parametrize("retrieved, correct, expected", RECALL_CASES)
def test_recall(retrieved, correct, expected):
    assert recall_at_5(retrieved,correct) == expected

# ----- Faithfulness ---------
FAITHFUL_CASES = [
    ("store opens at 9am", "the store opens at 9am daily", True),
    ("store opens at 9am and closes at midnight", "the store opens at 9am", False),
    ("refunds in 7 days", "refunds are processed in 7 days", True),
]

@pytest.mark.parametrize("answer, source_doc, expected", FAITHFUL_CASES)
def test_faithfullness(answer, source_doc, expected):
    assert is_faithful(answer, source_doc) == expected