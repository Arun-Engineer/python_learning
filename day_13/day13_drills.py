# Drill 1 - Zero-shot sentiment classification.

from dotenv import load_dotenv
from openai import OpenAI

# def classify_sentiment(client: OpenAI, review: str) -> str:
#     """Classify a product review as Positive, Negative, or Neutral."""
#     response = client.chat.completions.create(
#         model= "gpt-4o-mini",
#         max_tokens= 20,
#         messages= [
#             {"role": "system", "content": "You are a sentiment classifier. Respond with only one word: Positive, Negative, or Neutral."},
#             {"role": "user", "content": f"Review: {review}"},
#         ],
#     )
#     return response.choices[0].message.content

# if __name__ == "__main__":
#     load_dotenv()
#     client = OpenAI()

#     reviews = [
#         "Best product I've bought!",
#         "Complete waste of money, broke in 2 days.",
#         "It works. Nothing special."
#     ]

#     for review in reviews:
#         print(f"Review: {review}")
#         print(f" -> {classify_sentiment(client, review)}\n")

# Drill 2 - Few-Shot Custom Format(JSON Output)
"""Drill 2 - Few-Shot prompt to force JSON output."""

import json

# def extract_contact_info(client: OpenAI, text: str) -> str:
#     """Extract name, email, and phone as JSON using few-shot."""
#     examples = """
# Text: "Contact John Smith at john@example.com or call 555-1234."
# JSON: {"name": "John Smith", "email": "john@example.com", "phone": "555-1234"}

# Text: "Reach out to Priya Sharma - priya.s@example.in, mobile 9812345678."
# JSON: {"name": "Priya Sharma", "email": "priya.s@example.in, "phone": "9812345678"}
# """

#     response = client.chat.completions.create(
#         model= "gpt-4o-mini",
#         max_tokens= 150,
#         messages= [
#             {"role": "system", "content": "Extract contact info as JSON. Output ONLY the JSON object, no prose."},
#             {"role": "user", "content": f"{examples}\nText: \"{text}\"\nJSON:"},
#         ],
#     )
#     return response.choices[0].message.content

# if __name__ == "__main__":
#     load_dotenv()
#     client = OpenAI()

#     text = "For inquiries email Arun at arun@gmail.com or call 1234567890."
#     raw_output = extract_contact_info(client, text)
#     print(f"Raw output:\n{raw_output}\n")

#     # Bonus: try parsing it as actual JSON
#     try:
#         parsed = json.loads(raw_output)
#         print(f"Parsed JSON: {parsed}")
#         print(f"Email extracted: {parsed['email']}")
#     except json.JSONDecodeError as e:
#         print(f"WARNING: model didn't return valid JSON. Error: {e}")

# Drill 3 - Chain-of-thought on a Math Word Problem

"""Drill 3 - chain-of-thought on multi-step arithmetic."""

# def solve_with_reasoning(client: OpenAI, problem: str) -> str:
#     """Solve a word problem with explicit step by step reasoning."""
#     response = client.chat.completions.create(
#         model = "gpt-4o-mini",
#         max_tokens = 120,
#         messages = [
#             {"role": "system", "content": "Solve word problems carefully. Show every step."},
#             {"role": "user", "content": f"{problem}\nLet's think step by step."}
#         ],
#     )
#     return response.choices[0].message.content

# def solve_without_reasoning(client: OpenAI, problem: str) -> str:
#     """Same model, same problem - but no COT prompt. Compare quality."""
#     response = client.chat.completions.create(
#         model = "gpt-4o-mini",
#         max_tokens = 100,
#         messages = [
#             {"role": "system", "content": "Solve word problems. Give only the final numeric answer."},
#             {"role": "user", "content": problem}
#         ],
#     )
#     return response.choices[0].message.content

# if __name__ == "__main__":
#     load_dotenv()
#     client = OpenAI()

#     problem = (
#         "A store had 250 apples on Monday. On Tuesday they sold  30 percent of them."
#         "On Wednesday they received a new shipment of 100 apples."
#         "On Thursday they sold half of what they had. How many appples are left?"
#     )

#     print("--- WITHOUT CoT ---")
#     print(solve_without_reasoning(client, problem))
    
#     print("\n--- WITH CoT ---")
#     print(solve_with_reasoning(client, problem))

# Drill 4 - Role Prompt as a QA Reviewer

"""Drill 4 - Role prompt: make the LLM act as a QA reviewer."""

# def qa_review_test_case(client: OpenAI, test_case: str) -> str:
#     """Have the LLM critique a test case as a senior QA reviewer."""

#     response = client.chat.completions.create(
#         model = "gpt-4o-mini",
#         max_tokens= 400,
#         messages= [
#             {"role": "system",
#              "content": (
#                  "You are a senior QA engineer with 15 years of experience reviewing test cases."
#                  "You evaluate test cases on three criteria: "
#                  "(1) Clarity of steps, (2) Specificity of expected results, (3) Coverage of edge cases."
#                  "Give a score from 1-5 on each cirterion and on sentence of feedback per criterion."
#              ),
#             },
#             {"role": "user", "content": f"Review this test case:\n\n{test_case}"},
#         ]
#     )
#     return response.choices[0].message.content

# if __name__ == "__main__":
#     load_dotenv()
#     client = OpenAI()

#     test_case = """
#     Test Case: Login Test
#     Steps:
#       1. Go to login page.
#       2. Enter Credentials.
#       3. Click submit
#     Expected: User logs in
#     """

#     review = qa_review_test_case(client, test_case)
#     print(review)

# Drill 5 - Stacked: Role + Few Shot + CoT

"""Drill 5 - Combined all three patterns for highest-quality output."""

def severity_classifier(client: OpenAI, bug_report: str) -> str:
    """Classify bug severity using role + few-shot"""

    system = (
        "You are a senior QA triage lead."
        "You classify bug reports by severity: P0 (production-down), P1 (major broken),"
        "P2 (minor issue), P3 (cosmetic)."
        "Always reason step by step before giving the final label."
    )

    user = f"""Classify the severity of each bug. Examples:
Bug: "All users see 500 errors on checkout page."
Reasoning: All users affected, critical revenue path blocked. -> P0

Bug: ""Search returns no results when query has special characters like !@#."
Reasoning: Subset of users affected, feature partially works. -> P1.

Bug: "The footer 'Privacy' link has a tyo: 'Privac'"
Reasoning: No functional impact, cosmetic. -> P3

Bug: "{bug_report}"
Reasoning:
"""
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_tokens= 400,
        messages= [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()

    bug = "Cart total miscalculates when applying coupon + shipping discount together; users charged $5-$10 extra"

    print(severity_classifier(client, bug))