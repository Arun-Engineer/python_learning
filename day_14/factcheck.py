from openai import OpenAI

def ask_fact(client, question: str) -> str:
    """Ask the model a factual question. Client passed in (DI)."""
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_toxens = 100,
        messages = [
            {"role": "system", "content": "Answer with only the fact, nothing else."},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content

def is_factual(answer: str, expected: str) -> bool:
    """True if the expected fact appears anywhere in the answer(case_insensitive)."""
    return expected.lower() in answer.lower()
