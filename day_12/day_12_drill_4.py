# Drill 4: Error Handling
from dotenv import load_dotenv
from openai import OpenAI, APIError, APITimeoutError, RateLimitError

def ask_safe(question: str) -> str | None:
    """Ask OpenAI a question. Return None on failure instead of crashing."""

    load_dotenv()
    client = OpenAI()

    try:
        response = client.chat.completions.create(
            model= "gpt-4o-mini",
            max_tokens= 100,
            messages=[
                {"role": "user", "content": question}
            ],
        )
        return response.choices[0].message.content
    except APITimeoutError:
        print("[ERROR] OpenAI timed out - the request took too long.")
        return None
    except RateLimitError:
        print("[WARN] Rate limited - you are sending too many requests.")
        return None
    except APIError as e:
        print("[ERROR] OpenAI error: {e}")
        return None
    
if __name__ == "__main__":
    result = ask_safe("Say hello in exactly 3 words.")

    if result is not None:
        print(f"--------- SUCCESS----------")
        print(result)
    else:
        print("----- FAILED  (handled gracefully) ------")