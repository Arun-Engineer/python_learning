# drill 1 - One template many flls(the eval-grid seed)
from dotenv import load_dotenv
from openai import OpenAI

PROMPT_TEMPLATE = {
    "test_cases": "Write{count} {case_type} for this feature:\n{feature}",
    "bug_report": "Write the Bug Report for this issue:\n{issue}",
    "regression_check": "Write the regression checklist for this feature:\n{feature}",
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
        max_tokens= 300,
        messages= [
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()

    system = "You are a senior QA engineer. Output only the testcases."
    variations = [
                    {"count": 3, "case_type": "positive", "feature": "login"},
                    {"count": 4, "case_type": "negative", "feature": "login"},
                    {"count": 2, "case_type": "edge_case", "feature": "login"}
                ]
    for values in variations:
        result = run_prompt(client, "test_cases", values, system)
        print(result)

# Drill 2: A new QA domain template(API tesing - your home turf)

# PROMPT_TEMPLATE = {
#     "test_cases": "Write{count} {case_type} for this feature:\n{feature}",
#     "bug_report": "Write the Bug Report for this issue:\n{issue}",
#     "regression_check": "Write the regression checklist for this feature:\n{feature}",
#     "api_test": "Write the api test {method} with www.jiomart.com{endpoint} for this scenarios:\n{scenario}",
# }

# def fill_template(template: str, values: dict) -> str:
#     """Fill a prompt template's {blank} for this feature."""
#     return template.format(**values)

# def make_prompt(name: str, values: dict) -> str:
#     """Look up a template and fill its blanks."""
#     prompt = PROMPT_TEMPLATE[name]
#     return fill_template(prompt, values)

# def run_prompt(client: OpenAI, name: str, values: dict, system: str) -> str:
#     """Build a prompt from the template. Send it to the model."""
#     user_prompt = make_prompt(name, values)
#     response = client.chat.completions.create(
#         model= "gpt-4o-mini",
#         max_tokens= 300,
#         messages= [
#             {"role": "system", "content": system},
#             {"role": "user", "content": user_prompt},
#         ],
#     )
#     return response.choices[0].message.content

# if __name__ == "__main__":
#     load_dotenv()
#     client = OpenAI()

#     system = "You are a senior QA engineer. Output only the testcases."
#     values = {"method": "POST", "endpoint": "/cart/add", "scenario": "adding an out-of-stock item"}
            
#     result = run_prompt(client, "api_test", values, system)
#     print(result)

# Drill: 3 - Break it on purpose(edge-case thinking)
# PROMPT_TEMPLATE = {
#     "test_cases": "Write{count} {case_type} for this feature:\n{feature}",
#     "bug_report": "Write the Bug Report for this issue:\n{issue}",
#     "regression_check": "Write the regression checklist for this feature:\n{feature}",
# }

# def fill_template(template: str, values: dict) -> str:
#     """Fill a prompt template's {blank} for this feature."""
#     return template.format(**values)

# def make_prompt(name: str, values: dict) -> str:
#     """Look up a template and fill its blanks."""
#     prompt = PROMPT_TEMPLATE[name]
#     return fill_template(prompt, values)

# def run_prompt(client: OpenAI, name: str, values: dict, system: str) -> str:
#     """Build a prompt from the template. Send it to the model."""
#     user_prompt = make_prompt(name, values)
#     response = client.chat.completions.create(
#         model= "gpt-4o-mini",
#         max_tokens= 300,
#         messages= [
#             {"role": "system", "content": system},
#             {"role": "user", "content": user_prompt},
#         ],
#     )
#     return response.choices[0].message.content

# if __name__ == "__main__":
#     load_dotenv()
#     client = OpenAI()

#     system = "You are a senior QA engineer. Output only the testcases."
#     variations = [
#                     {"count": 3, "case_type": "positive"},
#                     {"count": 4, "case_type": "negative"},
#                     {"count": 2, "case_type": "edge_case"}
#                 ]
#     for values in variations:
#         result = run_prompt(client, "test_cases", values, system)
#         print(result)

# Drill: 4 - List whats's available, then pick one.

# PROMPT_TEMPLATE = {
#     "test_cases": "Write{count} {case_type} for this feature:\n{feature}",
#     "bug_report": "Write the Bug Report for this issue:\n{issue}",
#     "regression_check": "Write the regression checklist for this feature:\n{feature}",
#     "api_test": "Write the api test {method} with www.jiomart.com{endpoint} for this scenarios:\n{scenario}",
# }

# def list_templates() -> list[str]:
#     """Return the names of all templates in the registry"""
#     return list(PROMPT_TEMPLATE.keys())

# def fill_template(template: str, values: dict) -> str:
#     """Fill a prompt template's {blank} for this feature."""
#     return template.format(**values)

# def make_prompt(name: str, values: dict) -> str:
#     """Look up a template and fill its blanks."""
#     prompt = PROMPT_TEMPLATE[name]
#     return fill_template(prompt, values)

# def run_prompt(client: OpenAI, name: str, values: dict, system: str) -> str:
#     """Build a prompt from the template. Send it to the model."""
#     user_prompt = make_prompt(name, values)
#     response = client.chat.completions.create(
#         model= "gpt-4o-mini",
#         max_tokens= 300,
#         messages= [
#             {"role": "system", "content": system},
#             {"role": "user", "content": user_prompt},
#         ],
#     )
#     return response.choices[0].message.content

# if __name__ == "__main__":
#     load_dotenv()
#     client = OpenAI()

#     list_temp = list_templates()
#     for index , temp in enumerate(list_temp, start= 1):
#         print(f"-> {index}. {temp}")
    
    
#     choosen = input(str("Enter the choosen template: "))
#     print(f"\n Chosen Template: {choosen}")
#     print()
#     if choosen not in PROMPT_TEMPLATE:
#         print("Invalid Template choosen")
#     else:
#         system = "You are a senior QA engineer. Output only the testcases."
#         variations = [
#                     {"count": 3, "case_type": "positive", "feature": "login"},
#                     {"count": 4, "case_type": "negative", "feature": "login"},
#                     {"count": 2, "case_type": "edge_case", "feature": "login"}
#                 ]
#         for values in variations:
#             result = run_prompt(client, choosen, values, system)
#             print(result)

# Drill 5 - same data, different policy(the trust anchor in action)

PROMPT_TEMPLATE = {
    "test_cases": "Write{count} {case_type} for this feature:\n{feature}",
    "bug_report": "Write the Bug Report for this issue:\n{issue}",
    "regression_check": "Write the regression checklist for this feature:\n{feature}",
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
        max_tokens= 300,
        messages= [
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()

    #system = "You are a terse senior QA engineer. Output only a numberd list, no explanations."
    system = "You are a friendly mentor. Explain your reasoning as you go."
    variations = [
                    {"count": 3, "case_type": "positive", "feature": "login"},
                    {"count": 4, "case_type": "negative", "feature": "login"},
                    {"count": 2, "case_type": "edge_case", "feature": "login"}
                ]
    for values in variations:
        result = run_prompt(client, "test_cases", values, system)
        print(result)