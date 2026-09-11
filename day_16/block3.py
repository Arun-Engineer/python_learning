# Drill 1 - A single-step task(does it stop after one tool?)
import json
from openai import OpenAI
from dotenv import load_dotenv

class Tool:
    def __init__(self, name: str, description: str, func) -> str:
        self.name = name
        self.description = description
        self.func = func

    def run(self, text: str) -> str:
        return self.func(text)

def word_count(text: str) -> str:
    """Counts the number of words in text."""
    return  str(len(text.split()))

def shout(text: str) -> str:
    """Converts the text in to uppercase."""
    return text.upper()

TOOLS = {
    "WordCount": Tool("WordCount", "Counts the number of words in the text.", word_count),
    "Shout": Tool("Shout", "Converts the text into uppercase.", shout),

}

def build_tool_menu(tools: dict)-> dict:
    lines = []
    for tool in tools.values():
        lines.append(f" - {tool.name}: {tool.description}")
    return "\n".join(lines)

def decide_next_step(client, question: str, tools: dict, history: str) -> str:
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
            {"role": "user", "content": user}
        ]
    )

    return json.loads(response.choices[0].message.content)

def run_agent_loop(client, question: str, text: str, tools:dict, max_steps: int = 5)-> str:
    """Let the model drive mutiple answers until the final answer is derived."""

    history = f"The text to work on this is: {text}"

    for step in range(max_steps):
        decision = decide_next_step(client, question, tools, history)

        if decision["type"] == "final":
            return decision["answer"], history

        tool_name = decision["tool"]
        tool_input = decision["input"]

        if tool_name not in tools:
            observation = f"Error: No tool named {tool_name}"
        else:
            observation = tools[tool_name].run(tool_input)

        history += f"\nUsed {tool_name} ({tool_input} -> {observation})"

    return "Stopped reached max_step without a final answer."

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()                                                                                           
    answer, history = run_agent_loop(client, "How many words in this text?", "login password is success",TOOLS)

    print("---Answer---")
    print(answer)
    print()
    print("-------History------")
    print(history)

#-----Drill 2 - A Three Tool Task---------                            
class Tool:
    def __init__(self, name: str, description: str, func) -> str:
        self.name = name
        self.description = description
        self.func = func
    
    def run(self, text: str) -> str:
        return self.func(text)

def word_count(text: str) -> str:
    """Counts the number of words in text."""
    return  str(len(text.split()))

def shout(text: str) -> str:
    """Converts the text in to uppercase."""
    return text.upper()

def reverse(text: str) -> str:
    """Reverses the text."""
    return text[::-1]

TOOLS = {
    "WordCount": Tool("WordCount", "Counts the number of words in the text.", word_count),
    "Shout": Tool("Shout", "Converts the text into uppercase.", shout),
    "Reverse": Tool("Reverse", "Reverses the text.", reverse)
}

def build_tool_menu(tools: dict)-> dict:
    lines = []
    for tool in tools.values():
        lines.append(f" - {tool.name}: {tool.description}")
    return "\n".join(lines)

def decide_next_step(client, question: str, tools: dict, history: str) -> str:
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
            {"role": "user", "content": user}
        ]
    )

    return json.loads(response.choices[0].message.content)

def run_agent_loop(client, question: str, text: str, tools:dict, max_steps: int = 5)-> str:
    """Let the model drive mutiple answers until the final answer is derived."""

    history = f"The text to work on this is: {text}"

    for step in range(max_steps):
        decision = decide_next_step(client, question, tools, history)

        if decision["type"] == "final":
            return decision["answer"], history

        tool_name = decision["tool"]
        tool_input = decision["input"]

        if tool_name not in tools:
            observation = f"Error: No tool named {tool_name}"
        else:
            observation = tools[tool_name].run(tool_input)

        history += f"\nUsed {tool_name} ({tool_input} -> {observation})"

    return "Stopped reached max_step without a final answer."

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()                                                                                           
    answer, history = run_agent_loop(client, "Reverse the text, then shout it, then coun the words.", "login password is success",TOOLS)

    print("---Answer---")
    print(answer)
    print()
    print("-------History--")
    print(history)

#-----Drill 3 - Break It: force a bad tool(guard test)---------                            
class Tool:
    def __init__(self, name: str, description: str, func) -> str:
        self.name = name
        self.description = description
        self.func = func
    
    def run(self, text: str) -> str:
        return self.func(text)

def word_count(text: str) -> str:
    """Counts the number of words in text."""
    return  str(len(text.split()))

def shout(text: str) -> str:
    """Converts the text in to uppercase."""
    return text.upper()

def reverse(text: str) -> str:
    """Reverses the text."""
    return text[::-1]

TOOLS = {
    "WordCount": Tool("WordCount", "Counts the number of words in the text.", word_count),
    "Shout": Tool("Shout", "Converts the text into uppercase.", shout),
    "Reverse": Tool("Reverse", "Reverses the text.", reverse)
}

def build_tool_menu(tools: dict)-> dict:
    lines = []
    for tool in tools.values():
        lines.append(f" - {tool.name}: {tool.description}")
    return "\n".join(lines)

def decide_next_step(client, question: str, tools: dict, history: str) -> str:
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
            {"role": "user", "content": user}
        ]
    )

    return json.loads(response.choices[0].message.content)

def run_agent_loop(client, question: str, text: str, tools:dict, max_steps: int = 5)-> str:
    """Let the model drive mutiple answers until the final answer is derived."""

    history = f"The text to work on this is: {text}"

    for step in range(max_steps):
        decision = decide_next_step(client, question, tools, history)

        if decision["type"] == "final":
            return decision["answer"], history

        tool_name = decision["tool"]
        tool_input = decision["input"]

        if tool_name not in tools:
            observation = f"Error: No tool named {tool_name}"
        else:
            observation = tools[tool_name].run(tool_input)

        history += f"\nUsed {tool_name} ({tool_input} -> {observation})"

    return "Stopped reached max_step without a final answer."

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()                                                                                           
    answer, history = run_agent_loop(client, "Translate the text to French.", "login password is success",TOOLS)

    print("---Answer---")
    print(answer)
    print()
    print("-------History--")
    print(history)

#-----Drill 4 - The infinite loop seatbelt(max-steps)---------                            
class Tool:
    def __init__(self, name: str, description: str, func) -> str:
        self.name = name
        self.description = description
        self.func = func
    
    def run(self, text: str) -> str:
        return self.func(text)

def word_count(text: str) -> str:
    """Counts the number of words in text."""
    return  str(len(text.split()))

def shout(text: str) -> str:
    """Converts the text in to uppercase."""
    return text.upper()

def reverse(text: str) -> str:
    """Reverses the text."""
    return text[::-1]

TOOLS = {
    "WordCount": Tool("WordCount", "Counts the number of words in the text.", word_count),
    "Shout": Tool("Shout", "Converts the text into uppercase.", shout),
    "Reverse": Tool("Reverse", "Reverses the text.", reverse)
}

def build_tool_menu(tools: dict)-> dict:
    lines = []
    for tool in tools.values():
        lines.append(f" - {tool.name}: {tool.description}")
    return "\n".join(lines)

def decide_next_step(client, question: str, tools: dict, history: str) -> str:
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
            {"role": "user", "content": user}
        ]
    )

    return json.loads(response.choices[0].message.content)

def run_agent_loop(client, question: str, text: str, tools:dict, max_steps: int = 2)-> str:
    """Let the model drive mutiple answers until the final answer is derived."""

    history = f"The text to work on this is: {text}"

    for step in range(max_steps):
        decision = decide_next_step(client, question, tools, history)

        if decision["type"] == "final":
            return decision["answer"], history

        tool_name = decision["tool"]
        tool_input = decision["input"]

        if tool_name not in tools:
            observation = f"Error: No tool named {tool_name}"
        else:
            observation = tools[tool_name].run(tool_input)

        history += f"\nUsed {tool_name} ({tool_input} -> {observation})"

    return "Stopped reached max_step without a final answer.", history

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()                                                                                           
    answer, history = run_agent_loop(client, "Reverse the text, then shout it, then coun the words.", "login password is success",TOOLS)

    print("---Answer---")
    print(answer)
    print()
    print("-------History--")
    print(history)


#-----Drill 5 - Observability upgrade---------                            
class Tool:
    def __init__(self, name: str, description: str, func) -> str:
        self.name = name
        self.description = description
        self.func = func
    
    def run(self, text: str) -> str:
        return self.func(text)

def word_count(text: str) -> str:
    """Counts the number of words in text."""
    return  str(len(text.split()))

def shout(text: str) -> str:
    """Converts the text in to uppercase."""
    return text.upper()

def reverse(text: str) -> str:
    """Reverses the text."""
    return text[::-1]

TOOLS = {
    "WordCount": Tool("WordCount", "Counts the number of words in the text.", word_count),
    "Shout": Tool("Shout", "Converts the text into uppercase.", shout),
    "Reverse": Tool("Reverse", "Reverses the text.", reverse)
}

def build_tool_menu(tools: dict)-> dict:
    lines = []
    for tool in tools.values():
        lines.append(f" - {tool.name}: {tool.description}")
    return "\n".join(lines)

def decide_next_step(client, question: str, tools: dict, history: str) -> str:
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
            {"role": "user", "content": user}
        ]
    )

    return json.loads(response.choices[0].message.content)

def run_agent_loop(client, question: str, text: str, tools:dict, max_steps: int = 5)-> str:
    """Let the model drive mutiple answers until the final answer is derived."""

    history = f"The text to work on this is: {text}"

    for step in range(max_steps):
        decision = decide_next_step(client, question, tools, history)

        if decision["type"] == "final":
            return decision["answer"], history

        tool_name = decision["tool"]
        tool_input = decision["input"]

        if tool_name not in tools:
            observation = f"Error: No tool named {tool_name}"
        else:
            observation = tools[tool_name].run(tool_input)

        print(f"[Step {step+1}] {tool_name}({tool_input}) -> {observation}")

        history += f"\nUsed {tool_name} ({tool_input} -> {observation})"

    return "Stopped reached max_step without a final answer.", history

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI()                                                                                           
    answer, history = run_agent_loop(client, "Reverse the text, then shout it, then coun the words.", "login password is success",TOOLS)

    print("---Answer---")
    print(answer)
    print()
    print("-------History--")
    print(history)
