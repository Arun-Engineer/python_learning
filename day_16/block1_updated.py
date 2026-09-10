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
    """Count the number of words in text."""
    return str(len(text.split()))

def shout(text: str) -> str:
    """Converts the text into uppercase."""
    return text.upper()

def char_count(text: str) -> str:
    """Counts the number of characters in the text."""
    return str(len(text))

TOOLS = {
    "WordCount": Tool("WordCount", "Count the number of words in the text", word_count),
    "Shout": Tool("Shout", "Converts the text into uppercase", shout),
}

def build_tool_menu(tools: dict) -> str:
    lines = []
    for tool in tools.values():
        lines.append(f" - {tool.name}: {tool.description}")
    return "\n".join(lines)

def choose_tool_llm(client, question: str, tools: dict) -> str:
    menu = build_tool_menu(tools)
    system = (
    "You are a tool-selection router.\n\n"
    "Available tools:\n"
    f"{menu}\n\n"
    "Rules:\n"
    "1. Select a tool only when its description directly matches the user's request.\n"
    "2. Never choose the closest available tool as a fallback.\n"
    "3. If no tool can perform the requested operation, return Unknown.\n"
    "4. Return ONLY the exact tool name or Unknown.\n"
    )
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_tokens = 20,
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": question}
        ],
    )
    return response.choices[0].message.content.strip()

def run_agent(client, question: str, text: str, tools: dict) -> str:
    tool_name = choose_tool_llm(client, question, tools)
    if tool_name == "Unknown":
        return f"No suitable tool is available."
    if tool_name not in tools:
        return f"Model picked an unkown tool: {tool_name}"
    observation = tools[tool_name].run(text)
    return f"Used {tool_name} -> {observation}"

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()

    print(run_agent(client, "how Many words in this?", "login bug is here", TOOLS))
    print(run_agent(client, "shout this at me please", "verify login", TOOLS))
    print(run_agent(client, "how Many characters in this?", "login bug is here", TOOLS))
    print(run_agent(client, "Reverse these texts in this?", "login bug is here", TOOLS))