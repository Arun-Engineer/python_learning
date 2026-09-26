def overlap_score(answer: str, source_doc: str) -> float:
    """What the function of the answer's words appear in the doc? (0.0 to 1.0)"""
    answer_words = answer.lower().split()
    doc_words = source_doc.lower().split()
    matches = sum(1 for word in answer_words if word in doc_words)
    return matches/len(answer_words)

def is_faithful_sort(answer: str, source_doc: str, threshold: float = 0.7) -> bool:
    """Faithful if enough of the answer's words are grounded """
    score = overlap_score(answer, source_doc)
    return score >= threshold

result = is_faithful_sort(
    "The store opens at 9 am", "The store opens at 9 am and closes at pm"
    )
print(result)