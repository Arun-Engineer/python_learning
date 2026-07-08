class Tool:
    def __init__(self, name: str, description: str, func) -> str:
        self.name = name
        self.description = description
        self.func = func

    def run(self, text: str) -> str:
        return self.func(text)

def word_count(text: str):
    return len(text.split())

def shout(text: str) -> str:
    return text.upper()

def reversing(text: str) -> str:
    return text[::-1]

TOOLS = {
    "WordCount": Tool("wordcount", "calculate number of words in the input", word_count),
    "Shout": Tool("shout", "Conver the input into uppercase", shout),
    "Reverse": Tool("reverse", "Reverse the given input", reversing),
}

def choose_tool(question: str) -> str:
    if "How many words" in question:
        return "WordCount"
    elif "reverse" in question or "Reverse" in question:
        return "Reverse"
    return "Shout"

def run_agent_loop(steps: list[str], text: str) -> list[str]:
    """Run a sequence of tool-steps on the text. Returns on observation per step."""
    observations = []

    for step in steps:
        if step not in TOOLS:
            observations.append(f"Unknown Tool: {step}")
            continue
        tool = TOOLS[step]
        result = tool.run(text)
        observations.append(f"{step} -> {result}")
    return observations

if __name__ == "__main__":
    plan= ["WordCount", "CharCount", "Shout"]
    text= "App crashes on login when password is empty"

    results = run_agent_loop(plan, text)
    for line in results:
        print(line)

