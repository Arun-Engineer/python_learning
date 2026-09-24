# Drill 1
def precision_at_5(retrieved_docs: list, relevant_docs: list) -> int:
    top_5 = retrieved_docs[:5]
    count = 0

    for doc in top_5:
        if doc in relevant_docs:
            count += 1
    return count

# Drill 2
def did_retrieve_anything(retrieved_docs: list) -> int:
    if not retrieved_docs:
        return False
    return True

# Drill 3
def is_faithful(answer, source_doc):
    for word in answer.lower().split():
        if word not in source_doc:
            return False
    return True

print(is_faithful("the store opens at 9 am", "the store opens at 9 am"))
print(is_faithful("the store opens at 9 am and closes at midnight", "the store opens at 9 am"))

# Drill 4

def test_recall_at_5(retrieved_docs: list, correct_doc: str)-> bool:
        """Check if the correct doc is in the top 5 retrieved."""
        top_5 = retrieved_docs[:5]
        return correct_doc in top_5

def evaluate_rag(retrieved_docs, correct_doc, answer, source_doc):
    document = did_retrieve_anything(retrieved_docs)

    if document == True:
        recall_pass = test_recall_at_5(retrieved_docs, correct_doc)
        faithful = is_faithful(answer, source_doc)

        return {"recall_pass": recall_pass, "faithful": faithful}

result = evaluate_rag(
    ["doc1", "doc2", "doc3"],
    "doc2",
    "the store opens at 9 am",
    "the store opens at 9 am"
)

print(result)
