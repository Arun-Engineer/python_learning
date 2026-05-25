"""Testable LLM interface - one function, client injected by caller"""

from openai import OpenAI

def ask(client: OpenAI, question: str, system: str | None = None) -> str:
    """Send a question to gpt-4o-mini and return the text response.
    
    The client is passed in (not created here) so tests can inject a fake.
    """
    messages: list[dict] = []
    if system is not None:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        max_tokens= 100,
        messages= messages,
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    # Smoke test - run this file directly to verify ask() works end to end.
    from dotenv import load_dotenv

    load_dotenv()
    client = OpenAI()

    answer = ask(
        client,
        "what is a Python list comprehension? one sentence.",
        system= "You are a senior engineer. Be concise."
    )

    print("--- SMOKE TEST ----")
    print(answer)
    