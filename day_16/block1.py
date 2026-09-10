from openai import OpenAI
from dotenv import load_dotenv

class Tool:
    def __init__(self, name: str, description: str, func):
        self.name = name
        self.description = description
        self.func = func

    def run(self, text: str) -> str:
        return self.func(text)

def word_count(text: str) -> str:
    """Count the words in the text."""
    return str(len(text.split()))

def shout(text: str) -> str:
    """Return the text in uppercase."""
    return text.upper()

def char_count(text: str) -> str:
    """Count the characters in the text."""
    return str(len(text))

TOOLS = {
    "WordCount": Tool("WordCount", "Count the number of words", word_count),
    "Shout": Tool("Shout", "Converts the text to uppercase", shout),
    "CharCount": Tool("CharCount", "Count the number of characters", char_count)
}

def choose_tool(question: str) -> str:
    """Decide which tool to be use based on te question."""
    if "how many words" in question.lower():
        return "WordCount"
    elif "how many characters" in question.lower():
        return "CharCount"
    else:
        return "Shout"

def run_agent(question: str, text: str) -> str:
    """Then agent: brain picks a tool, hands run it."""
    tool_name = choose_tool(question)
    tool = TOOLS[tool_name]
    observation = tool.run(text)
    return f"Used {tool_name} -> {observation}"

if __name__ == "__main__":
    print(run_agent("How many words are here?", "login fails on empty password"))
    print(run_agent("Make this stand out", "checkout button broken"))
    print(run_agent("How many characters are here?", "Login failed"))