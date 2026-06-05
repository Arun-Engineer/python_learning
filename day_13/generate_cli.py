"""CLI: python generate_cli.py 'feature description here'"""

import sys
import json
from dotenv import load_dotenv
from openai import OpenAI
from test_case_generator import generate_test_cases


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python generate_cli.py 'Feature description here'")
        return 1
    feature = " ".join(argv[1:])

    load_dotenv()
    client = OpenAI()

    try:
        cases = generate_test_cases(client, feature, n_cases= 5)
    except ValueError as e:
        print(f"ERROR: {e}")
        return 2
    
    print(json.dumps(cases, indent= 2))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
