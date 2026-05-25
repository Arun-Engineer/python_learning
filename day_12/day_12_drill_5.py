# Drill 5- Inspect every meaningful field on the response object

from dotenv import load_dotenv
from openai import OpenAI

def inspect_response(question: str) -> dict:
    """Send a question to OpenAI and return all meaningful response fields."""
    load_dotenv()
    client = OpenAI()

    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        max_tokens= 100,
        messages= [
            {"role": "user", "content": question}
        ],
    )

    return {
        "response_id":          response.id,
        "model_returned":       response.model,
        "finish_reason":        response.choices[0].finish_reason,
        "prompt_token":         response.usage.prompt_tokens,
        "completion_tokens":    response.usage.completion_tokens,
        "total_tokens":         response.usage.total_tokens,
        "choices_count":        len(response.choices),
        "role":                 response.choices[0].message.role,
        "text":                 response.choices[0].message.content,
    }

if __name__ == "__main__":
    info = inspect_response("Say hello in exactly 5 words.")

    print("---- RESPONSE INSPECTION -----")
    for key, value in info.items():
        print(f"{key:20}: {value}")
