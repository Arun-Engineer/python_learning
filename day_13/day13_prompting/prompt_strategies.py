"""Day 13 - Compare zero-shot, few-shot, COT, and role prompting on the same task."""

from dotenv import load_dotenv
from openai import OpenAI

def ask_with_prompt(client: OpenAI, system: str, user:str) -> str:
    """Send a single-turn prompt and return the response text."""
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_tokens = 500,
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user}, 
        ],
    )
    return response.choices[0].message.content

def zero_shot(client: OpenAI, problem: str) -> str:
    """Pattern 1 - Instruction only, no examples, no role, no COT"""
    system = "You are a helpful assistant."
    user = f"Classify this support ticket as Bug, Feature Request, or Question.\n\nTicket: {problem}"
    return ask_with_prompt(client, system, user)

def few_shot(client: OpenAI, problem: str) -> str:
    """Pattern 2 - show examples, then ask."""
    system = "You are a helpful assistant."
    user = f"""Classify each ticket as Bug, Feature Request, or Question.
    
Ticket: 'Login page shows 500 error on Chrome' -> Bug
Ticket: 'Please add dark mode to the dashboard'-> Feature Request
Ticket: 'How do I reset my password' -> Question

Ticket: '{problem}'
"""
    return ask_with_prompt(client, system, user)

def chain_of_thought(client: OpenAI, problem: str) -> str:
    """Pattern 3 - Explicit reasoning request."""
    system = "You are a helpful assistant."
    user = f"""Classify this support ticket as Bug, Feature Request, Question.

First think step by step about what the user is reporting.
Then give your final answer on a new line starting with "Answer:".

Ticket: {problem}"""
    return ask_with_prompt(client, system, user)

def role_prompt(client: OpenAI, problem: str) -> str:
    """Pattern 4 - strong role/persona in system message."""
    system = (
        "You are a senior QA triage lead with 15 years of experience."
        "You classify support tickets quickly and decisively."
        "Respond with only one word: Bug, Feature Request, or Question."
    )
    user = f"Ticket: {problem}"
    return ask_with_prompt(client, system, user)

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()
    test_ticket = "The cart total doesn't match the sum of items when i have a coupon applied"

    print(f"Ticket: {test_ticket}\n")
    print("=" * 60)

    print("\n--- ZERO SHOT ---")
    print(zero_shot(client, test_ticket))

    print("\n--- FEW SHOT ---")
    print(few_shot(client, test_ticket))

    print("\n--- CHAIN OF THOUGHT ---")
    print(chain_of_thought(client, test_ticket))

    print("\n--- ROLE PROMPT ---")
    print(role_prompt(client, test_ticket))