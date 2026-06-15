from dotenv import load_dotenv
from openai import OpenAI

PROMPT_TEMPLATES = {
    "test_cases": "Write {count} {case_type} for this feature:\n{feature}",
    "bug_report": "Write a bug report for this issue:\n{issue}",
    "regression_check": "Write a regression checklist for this feature:\n{feature}",
}

def fill_template(template: str, values: dict) -> str:
    """Fill a prompt template's {blank} using dictionary of values."""
    return template.format(**values)

def make_prompt(name: str, values: dict) -> str:
    """Look up a template by name and fill its blanks."""
    template = PROMPT_TEMPLATES[name]
    return fill_template(template, values)

def run_prompt(client: OpenAI, name:str, values: dict, system: str) -> str:
    """Build a prompt from a template, send it to the model. Client passed in (DI)."""
    user_prompt = make_prompt(name, values)
    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        max_tokens= 150,
        messages= [
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()

    system = "You are a Senior QA engineer. Output only Test cases."
    values = {"count": 10, "case_type": "Both positive and negative", "feature": "checkout"}

    result = run_prompt(client, "regression_check", values, system)
    print(result)