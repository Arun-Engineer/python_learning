import json
from openai import OpenAI
from dotenv import load_dotenv

class Tool:
    def __init__(self, name: str, description: str, func) -> str:
        self.name = name
        self.description = description
        self.func = func

    def run(self, text:str) -> str:
        return self.func(text)

def word_count(text: str) -> str:
    """Count the number of words in the text."""
    return str(len(text.split()))

def shout(text: str) -> str:
    """Converts the text into uppercase."""
    return text.upper()

def char_count(text: str) -> str:
    """Count the number of Characters in the text."""
    return str(len(text.strip()))

TOOLS = {
    "WordCount": Tool("WordCount", "Count the number of words in the text", word_count),
    "Shout": Tool("Shout", "Converts the text into uppercase", shout),
    "CharCount": Tool("CharCount", "Count the number of characters in the text", char_count)
}

def build_tool_menu(tools: dict) -> str:
    lines = []
    for tool in tools.values():
        lines.append(f" - {tool.name}: {tool.description}")
    return "\n".join(lines)

def decide_next_step(client, question: str, history: str, tools: dict) -> dict:
    """Ask the model for its next move as JSON: either an action or a final answer."""
    menu = build_tool_menu(tools)
    system = (
        "You are a step by step agent. You have these tools:\n"
        f"{menu}\n\n"
        "Given the question and history so far, reply with JSON only:\n"
        '{"type": "action", "tool": "ToolName", "input": "text} to use a tool, OR\n'
        '{"type": "final", "answer": "your answer"} when you are done.'
    )

    user = f"Question: {question}\n\nHistory so far:\n{history}"
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_tokens = 200,
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
    )
    return json.loads(response.choices[0].message.content)

def run_agent_loop(client, question: str, text: str, tools: dict, max_steps: int = 5):
    """Let the model drive multiple steps until it returns a final answer."""
    history = f"The text to work on is: {text}."

    for step in range(max_steps):
        decision = decide_next_step(client, question, history, tools)

        if decision["type"] == "final":
            return decision["answer"], history

        tool_name = decision["tool"]
        tool_input = decision["input"]

        if tool_name not in tools:
            observation = f"Error: no tool named {tool_name}"
        else:
            observation = tools[tool_name].run(tool_input)   

        history += f"\nUsed {tool_name} ({tool_input} -> {observation})"

    print("----- HISTORY TRACE -----")
    print(history)

    return "Stopped: reached max steps without a final answer." 

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()

    answer , history = run_agent_loop(
        client,
        question = "First shout the text, Then tell me how many word it has?",
        text = "login fails on empty password",
        tools = TOOLS,
    )
    print(answer)
    print(history)
    