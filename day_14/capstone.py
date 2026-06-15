from dotenv import load_dotenv
from openai import OpenAI

PROMPT_TEMPLATE = {
    "test_cases": "Write{count} {case_type} for this feature:\n{feature}",
    "bug_report": "Write the Bug Report for this issue:\n{issue}",
    "regression_check": "Write the regression checklist for this feature:\n{feature}",
    "test_plan": "List the areas that need testing for this feature,as a short bullet list.\nFeature: {feature}.",
    "cases_from_plan": "Write detailed test cases for each area in this test plan.\nTest plan:\n{plan}.",
    "top_priorities": "Pick the 3 highest priority test cases from {cases}"
}

def fill_template(template: str, values: dict) -> str:
    """Fill a prompt template's {blank} for this feature."""
    return template.format(**values)

def make_prompt(name: str, values: dict) -> str:
    """Look up a template and fill its blanks."""
    prompt = PROMPT_TEMPLATE[name]
    return fill_template(prompt, values)

def run_prompt(client: OpenAI, name: str, values: dict, system: str) -> str:
    """Build a prompt from the template. Send it to the model."""
    user_prompt = make_prompt(name, values)
    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        max_tokens= 1300,
        messages= [
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content

def generate_test_cases(client, feature: str, system: str) -> tuple[str, str]:
    """Two-step chain: feature -> test plan -> detailed test cases. Returns both steps."""
    plan = run_prompt(client, "test_plan", {"feature": feature}, system)
    cases = run_prompt(client, "cases_from_plan", {"plan": plan}, system)
    top = run_prompt(client, "top_priorities", {"cases": cases}, system)
    return plan, cases, top


if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()

    system = "You are a senior QA engineer. Be precise. Stay strictly on then given feature."
    feature = "password reset via email link."
    
    plan, cases, top = generate_test_cases(client, feature, system)

    print("==== STEP 1: TEST PLAN ====")
    print(plan)
    print("\n==== STEP 2: TEST CASES ====")
    print(cases)
    print("\n==== STEP 3: TOP PRIORITY TEST CASES ====")
    print(top)
