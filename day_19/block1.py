def test_recall_at_5(retrieved_docs: list, correct_doc: str) -> bool:
    """check if hte correct doc is in the top 5 retrieved."""

    top_5 = retrieved_docs[::5]

    return correct_doc in top_5
