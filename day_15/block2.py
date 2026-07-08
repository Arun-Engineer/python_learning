class Tool:
    """A named tool that agent can choose and run."""
    def __init__(self, name: str, description: str, func):
        self.name = name
        self.description = description
        self.func = func

    def run(self, text: str) -> str:
        return self.func(text)
    
def count_word(text: str) -> str:
    """Count the words in the text."""
    return len(text.split())

def shout(text: str) -> str:
    """Return the text in the UPPERCASE."""
    return text.upper()

def char_count(text:str) -> str:
    """Count the characters in the text."""
    return(len(text.lower().replace(" ", "")))

TOOLS = {
    "WordCount": Tool("WordCount", "Counts the number of words in the input", count_word),
    "Shout": Tool("Shout", "Converts the input to uppercase", shout),
    "CharCount": Tool("CharCount", "Counts the number of characters of word in the input", char_count)
}

def choose_tool(question: str) -> str:
    """Decide which tool to use. (day16 replaces this rule with a real llm call.)"""

    if "how many words" in question.lower():
        return "WordCount"
    elif "how many characters" in question.lower():
        return "CharCount"
    return "Shout"

def run_agent(question: str, text: str) -> str:
    """One pass of the agent: choose a tools, run it, report."""

    tool_name = choose_tool(question)
    tool = TOOLS[tool_name]
    observation = tool.run(text)
    return f"Used {tool_name} -> {observation}"

if __name__ == "__main__":
    q1 = "How many words are there in this bug report?"
    print(run_agent(q1, "App crashes on login when password is empty"))

    q2 = "Make this tile and stand out."
    print(run_agent(q2, "Veirfy login with valid credentials"))

    q3 = "How many characters are there in this bug report description"
    print(run_agent(q3, "App crashes on login when password is empty"))