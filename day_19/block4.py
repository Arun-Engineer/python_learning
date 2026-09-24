def recall_at_5(retrieved_docs, correct_doc):
    """Check whether relevant docs are fetched."""
    top_5 = retrieved_docs[:5]
    return correct_doc in top_5

def did_retrieve_anything(retrieved_doc: list) -> bool:
    if not retrieved_doc:
        return False
    return True

def is_faithful(answer: str, source_doc: list) -> bool:
    """Check whether it is properly answered from retrieved documents"""
    for word in answer.lower().split():
        if word not in source_doc.lower():
            return False
    return True

def evaluate_rag(retrieved_docs, correct_doc, answer, source_doc):
    document = did_retrieve_anything(retrieved_docs)

    if document == True:
        recall_pass = recall_at_5(retrieved_docs, correct_doc)
        faithful = is_faithful(answer, source_doc)
        return {"recall_pass": recall_pass, "faithful": faithful}

def print_prag_result(eval_result: dict) -> None:
    print("=" * 40)
    print("RAG EVALUATION RESULT")
    print("=" * 40)

    for check, passed in eval_result.items():
        mark = "PASS" if passed else "FAIL"
        print (f" {mark} {check}: {passed}")
    print("=" * 40)

result = evaluate_rag(
    retrieved_docs=["policy_doc_7","doc2","doc3"],
    correct_doc ="policy_doc_7",
    answer = "refunds in 7 days",
    source_doc = "refunds are processed in 7 days",
)
print_prag_result(result)