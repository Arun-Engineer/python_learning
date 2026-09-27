TEST_CASES = [
    {
        "retrieved":["policy_doc_7", "doc2"],
        "correct_doc": "policy_doc_7",
        "answer": "refunds within seven days.",
        "source_doc": "refunds are processed within seven business days",
    },
    {
        "retrieved": ["doc1", "doc2"],
        "correct_doc": "policy_doc_7",
        "answer": "you get money back in a week.",
        "source_doc": "refunds are prrocessed within seven business days.",
    },
]

def recall_5(retrieved: list, correct_doc:list) -> bool:
    """Checks whether retrieved documents are valid and correct."""
    top_5 = retrieved[:5]
    return correct_doc in top_5

def overlap_score(answer: str, source_doc: str) -> float:
    """What the function of the answer's words appear in the doc? (0.0 to 1.0)"""
    correct_answer = answer.lower().split()
    sources = source_doc.lower().split()
    matches = sum(1 for word in correct_answer if word in sources)
    return matches/len(correct_answer)

def is_faithful_sort(answer: str, source_doc: str, threshold = 0.7) -> bool:
    score = overlap_score(answer, source_doc)
    return score >= threshold

def evaluate_rag_scored(retrieved: list, correct_doc: list, answer: str, source_doc: str):
    """Run all RAG checks and return a scored report."""
    recall_pass = recall_5(retrieved, correct_doc)
    score = overlap_score(answer, source_doc)
    faithful = is_faithful_sort(answer, source_doc, threshold = 0.7)

    return {
        "recall_pass": recall_pass,
        "faithfullness_score": score,
        "faithful_enough": faithful,
    }

def run_rag_eval_suite(testcase: list) -> dict:
    recall_passes = 0
    faithfulness_score = []

    for case in testcase:
        result = evaluate_rag_scored(case["retrieved"], case["correct_doc"], case["answer"], case["source_doc"])

        if result["recall_pass"]:
            recall_passes += 1
        faithfulness_score.append(result["faithfullness_score"])

    avg_faith = sum(faithfulness_score)/len(faithfulness_score)
    return {
            "total_cases": len(testcase),
            "recall_passed": recall_passes,
            "avg_faithfulness": round(avg_faith, 2),
    }

def print_report(results: dict) -> None:
    print("=" * 40)
    print("RAG EVALUATION SUITE REPORT")
    print("=" * 40)

    for name, values in results.items():
        print(f" {name} --> {values}")

    print("=" * 40)

result = run_rag_eval_suite(TEST_CASES)
print_report(result)