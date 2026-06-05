"""Test case generator using few-shot + role prompting
Architecture follows Day 12 dependency-injection pattern:
- The LLM client is passed in, not created internally.
- This file is testable in isolation with a MagicMock.
"""

import json
from openai import OpenAI

def generate_test_cases(client: OpenAI, feature_description: str, n_cases: int = 5) -> list[dict]:
    """Generate n structured test cases for a feature description.
    
    Returns a list of dicts shaped like:
    {"title": str, "steps": list[str], "expected": str, "category": str}
    """

    system = (
        "You are a senior QA engineer who writes detailed, comprehensive test cases."
        "You output ONLY valid JSON - never prose, never markdown fences."
        "You cover happy path, edge cases, and negative cases."
    )

    example_output = """[
    {
      "title": "Successful login with valid credentials",
      "steps": ["Navigate to/ login", "Enter valid username and password", "click submit"],
      "expected": "User is redirected to dashboard; session cookie is set,
      "category": "happy_path"
      },
      {
      "title": "Login fails with wrong password."
      "steps": ["Navigate to/ login", Enter valid username, wrong password", "click submit"],
      "expected": "Error message 'Invalid login credentials' is shown ; user stays on login page,
      "category": "negative
    }
]"""

    user = f""" Generate{n_cases} test cases for the following feature.
Return a JSON array. Each item must have keys: title, steps(array of strings), expected, category.
Category must be one of: happpy_path, edge_case, negative, security.

Example output format:
{example_output}

JSON output:"""
    
    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        max_tokens= 2000,
        messages= [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown fences if the model added them despite instructions
    if raw.startswith("'''"):
        raw = raw.strip("'").lstrip("json").strip()

    try :
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"LLM returned invalid JSON: {e}\nRaw Output:\n{raw}")
    
if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    client = OpenAI()

    feature = ( 
        "Coupon code redemption at checkout: users can enter a coupon code, "
        "the system validates it (active, not expired, applicable to cart items), "
        "and applies the discount to the cart total."
    )

    cases = generate_test_cases(client, feature, n_cases= 5)

    print(f"Generted {len(cases)} test cases\n")
    for i, case in enumerate(cases, start= 1):
        print(f"--- Test Case {i}: [{case['category']}] {case['title']} ---")
        print("Steps:")
        for step in case['steps']:
            print(f" - {step}")
        print(f"Expected: {case['expected']}\n")