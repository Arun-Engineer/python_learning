def recall_5(retrieved : list, correct_doc: list) -> bool:
    """Checks whether retrieved docs are correct."""
    retrieved_doc = retrieved[:5]
    return correct_doc in retrieved_doc

def overlap_score(answer: str, source_doc: str):
    """What the function of the answer's words appear in the doc? (0.0 to 1.0)"""
    answer_words = answer.lower().split()
    source = source_doc.lower().split()
    matches = sum(1 for word in answer_words if word in source)
    return matches/len(answer_words)

def is_faithful_sort(answer: str, source_doc: str, threshold = 0.7):
    score = overlap_score(answer, source_doc)
    return score >= threshold

def evaluate_rag_scored(retrieved, correct_doc, answer, source_doc):
    """Run all RAG checks and return a scored report."""
    recall = recall_5(retrieved, correct_doc)
    score = overlap_score(answer, source_doc)
    faithful = is_faithful_sort(answer, source_doc, threshold=0.7)

    return {
        "recall_pass": recall,
        "faithfulness_ score": round(score, 2),
        "faithful_enough": faithful
    }

def print_scored_report(report: dict) -> None:
    print("=" * 40)
    print("RAG SCORED EVALUATION REPORT")
    print("=" * 40)

    for check, value in report.items():
        print(f" {check} --> {value}")

    print("=" * 40)

result = evaluate_rag_scored(
    ["doc1", "doc2", "doc3", "doc4", "doc5"],
        "doc2",
        "the store opens at 9 am.",
        "the store opens at 9 am and closes at 10 pm"
)
print_scored_report(result)