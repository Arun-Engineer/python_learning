# B1 all_docs_relevant

def all_docs_relevant(retrieved_docs: list, correct_doc) -> bool:

    for doc in retrieved_docs:
        if correct_doc not in retrieved_docs:
            return False
    return True

# B2 - count relevant

def count_relevant(retrieved_docs: list, correct_doc) -> int:
    count = 0

    for docs in retrieved_docs:
        if correct_doc in docs:
            count += 1
    return count