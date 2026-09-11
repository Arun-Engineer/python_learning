import json
from openai import OpenAI
from dotenv import load_dotenv

class Tool:
    def __init__(self, name: str,description: str, func):
        self.name = name
        self.description = description
        self.func = func

    def run(self, text: str) -> str:
        return self.func(text)

def word_count(text: str) -> str:
    """"counts the number of words in the text."""
    return str(len(text.split()))

def shout(text: str) -> str:
    """converts the text to uppercase."""
    return text.upper()

def reverse(text: str) -> str:
    """reverse the text."""
    return text[::-1]

def list_test_areas(feature: str) -> str:
    """return a few test areas for a feature, one per line."""
    areas = ["happy_path", "empty_input", "invalid_input", "security"]
    return "\n".join(f"- {feature}: {area}" for area in areas)

def count_lines(text: str) -> str:
    """counts the number of lines in the text."""
    return str(len(text.strip().split()))

TOOLS = {
    "WordCount": Tool("WordCount", "Counts the number of words in the text.", word_count),
    "Shout": Tool("Shout", "Converts the text to uppercase.", shout),
    "Reverse": Tool("Reverse", "Reverses the text.", reverse),
    "ListTestAreas": Tool("ListTestAreas", "Returns a few test areas for a feature, one per line.", list_test_areas),
    "CountLines": Tool("CountLines", "Counts the number of lines in the text.", count_lines),
}

def build_tool_menu(tools: dict) -> str:
    """Builds a menu of available tools."""
    lines = []

    for tool in tools.values():
        lines.append(f"{tool.name}: {tool.description}")

    return "\n".join(lines) 

def decide_next_step(client, question: str, tools: dict, history) -> str:
    """Decides the next step based on the question and available tools."""
    menu = build_tool_menu(tools)

    system = (
                "You are a step by step agent. You have these tools:\n"
                f"{menu}\n\n"
                "Given the question and history so far, reply with JSON only:\n"
                '{"type": "action", "tool": "ToolName", "input": "text} to use a tool, OR\n'
                '{"type": "final", "answer": "your answer"} when you are done.'
            )

    user = f"Question: {question}\nHistory:\n{history}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=200,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ]
    )
    return json.loads(response.choices[0].message.content)

def run_agent_loop(client, question: str, tools: dict, text: str, max_steps: int = 5) -> str:
    """Runs the agent loop until a final answer is produced."""
    history = f"The text to work on this: {text}\n"

    for step in range(max_steps):
        decision = decide_next_step(client, question, tools, history)

        if decision["type"] == "final":
            return decision["answer"]

        tool_name = decision["tool"]
        tool_input = decision["input"]

        if tool_name not in tools:
            observation = f"Error: Tool '{tool_name}' not found."
        else:
            observation = tools[tool_name].run(tool_input)  

        history += f"\nUsed tool '{tool_name}' with input '{tool_input}', got observation: '{observation}'\n"

    return "Error: Maximum steps reached without a final answer."

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()

    question = "List the test areas for the given feature," "then tell me how many areas you produced."
    text = "password reset via email."

    final_answer = run_agent_loop(client, question, TOOLS, text, max_steps = 10)
    print(f"Final Answer: {final_answer}")