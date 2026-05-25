"""
Day 12 - First LLM API call (OpenAI version).
sends a single message to OpenAI and prints the response.
"""
import os
import logging
from dotenv import load_dotenv
from openai import OpenAI

logging.basicConfig(
    level= logging.INFO,
    format= "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt= "%H:%M:%S"
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def ask_openai(question: str) -> str:
    """Sends a single question to OpenAI, return the text response."""
    # Load the API key from .env
    load_dotenv()

    # Create the client - the SDK auto-reads OPENAI_API_KEY from env
    client = OpenAI()

    logger.info("Asking OpenAI: %r", question)

    # Make the API call
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_tokens= 1024,
        messages= [
            {"role": "user", "content": question}
        ],
    )

    # Exctract the text from the response
    answer = response.choices[0].message.content

    logger.info("Got the response (%d input tokens, %d output tokens)",
                response.usage.prompt_tokens,
                response.usage.completion_tokens
                )
    return answer

if __name__ == "__main__":
    answer = ask_openai("What is one thing every Python developer should know about async/wait")
    print()
    print("=" * 60)
    print(answer)
    print("=" * 60)