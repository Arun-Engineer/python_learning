"""Command - line tool: python ask_cli.py 'your question'"""

import sys
from dotenv import load_dotenv
from openai import OpenAI
from llm_client import ask

def main(argv: list[str]) -> int:
    """Run the CLI. Return an exit code(0 = success, 1 = usage error)"""

    if len(argv) < 2:
        print("Usage: python ask_cli.py 'your question'")
        return 1
    
    question = " ".join(argv[1:])
    load_dotenv()
    client = OpenAI()

    answer = ask(
        client,
        question,
        system = "you are a senior engineer. Be concise."
    )

    print()
    print("=" * 60)
    print(answer)
    print("=" * 60)
    return 0

if __name__ == "__main__":
    exit_code = main(sys.argv)
    sys.exit(exit_code)
    