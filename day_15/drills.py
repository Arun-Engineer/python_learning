# # Drill 1 - A fourth tool(your QA home turf)

# class Tool:
#     """A named tool that agent can choose and run."""
#     def __init__(self, name: str, description: str, func) -> str:
#         self.name = name
#         self.description = description
#         self.func = func
    
#     def run(self, text: str) -> str:
#         return self.func(text)

# def word_count(text: str):
#     """Count and returns the input given."""
#     return len(text.split())

# def shout(text: str):
#     """Returns the input in UPPERCASE format."""
#     return text.upper()

# def reversing(text: str):
#     """Return the reversed word or input given."""
#     return text[::-1]

# TOOLS = {
#     "WordCount": Tool("wordcount", "calculate number of words in the input", word_count),
#     "Shout": Tool("shout", "Conver the input into uppercase", shout),
#     "Reverse": Tool("reverse", "Reverse the given input", reversing),
# }

# def choose_tool(question: str) -> str:
#     """Agent chooses the tool based on the requirement."""
#     if "how many words" in question:
#         return "WordCount"
#     elif "Reverse" in question:
#         return "Reverse"
#     return "Shout"

# def run_agent(question: str, text:str) -> str:
#     """Choose a tool run and report it."""
#     tool_name = choose_tool(question)
#     tool = TOOLS[tool_name]
#     observation = tool.run(text)
#     return f"Tool used {tool_name} --> {observation}"

# if __name__ == "__main__":
#     q1 = "How many words are there in this bug report?"
#     print(run_agent(q1, "App crashes on login when password is empty"))

#     q2 = "Make this tile and stand out."
#     print(run_agent(q2, "Verify login with valid credentials"))

#     q3 = "Reverse his input and return"
#     print(run_agent(q3, "login"))


# Drill 2 - List the agent's tools(inspectability)

# class Tool:
#     """A named tool that agent can choose and run."""
#     def __init__(self, name: str, description: str, func) -> str:
#         self.name = name
#         self.description = description
#         self.func = func
    
#     def run(self, text: str) -> str:
#         return self.func(text)

# def word_count(text: str):
#     """Count and returns the input given."""
#     return len(text.split())

# def shout(text: str):
#     """Returns the input in UPPERCASE format."""
#     return text.upper()

# def reversing(text: str):
#     """Return the reversed word or input given."""
#     return text[::-1]

# TOOLS = {
#     "WordCount": Tool("wordcount", "calculate number of words in the input", word_count),
#     "Shout": Tool("shout", "Conver the input into uppercase", shout),
#     "Reverse": Tool("reverse", "Reverse the given input", reversing),
# }

# def choose_tool(question: str) -> str:
#     """Agent chooses the tool based on the requirement."""
#     if "How many words" in question:
#         return "WordCount"
#     elif "Reverse" in question:
#         return "Reverse"
#     return "Shout"

# def list_tools(tools: dict) -> str:
#     result = []
#     for tool in tools.values():
#         result.append (f"{tool.name} --> {tool.description}")
#     return "\n".join(result)

# def run_agent(question: str, text:str) -> str:
#     """Choose a tool run and report it."""
#     tool_name = choose_tool(question)
#     tool = TOOLS[tool_name]
#     available_tools = list_tools(TOOLS)
#     observation = tool.run(text)
#     return (
#         "Available Tools:\n"
#         f"{available_tools}\n\n"
#         f"Tool used {tool_name} --> {observation}\n"
#     )

# if __name__ == "__main__":
#     q1 = "How many words are there in this bug report?"
#     print(run_agent(q1, "App crashes on login when password is empty"))

#     q2 = "Make this tile and stand out."
#     print(run_agent(q2, "Verify login with valid credentials"))

#     q3 = "Reverse his input and return"
#     print(run_agent(q3, "login"))

# Drill 3 -Break it: ask for a tool that doesnt exist

# class Tool:
#     """A named tool that agent can choose and run."""
#     def __init__(self, name: str, description: str, func) -> str:
#         self.name = name
#         self.description = description
#         self.func = func
    
#     def run(self, text: str) -> str:
#         return self.func(text)

# def word_count(text: str):
#     """Count and returns the input given."""
#     return len(text.split())

# def shout(text: str):
#     """Returns the input in UPPERCASE format."""
#     return text.upper()

# def reversing(text: str):
#     """Return the reversed word or input given."""
#     return text[::-1]

# TOOLS = {
#     "WordCount": Tool("wordcount", "calculate number of words in the input", word_count),
#     "Shout": Tool("shout", "Conver the input into uppercase", shout),
#     "Reverse": Tool("reverse", "Reverse the given input", reversing),
# }

# def choose_tool(question: str) -> str:
#     """Agent chooses the tool based on the requirement."""
#     if "How many words" in question:
#         return "WordCount"
#     elif "Reverse" in question:
#         return "Reverse"
#     elif "Translate" in question:
#         return "Translate"
#     return "Shout"

# def list_tools(tools: dict) -> str:
#     result = []
#     for tool in tools.values():
#         result.append (f"{tool.name} --> {tool.description}")
#     return "\n".join(result)

# def run_agent(question: str, text:str) -> str:
#     """Choose a tool run and report it."""
#     tool_name = choose_tool(question)
#     tool = TOOLS[tool_name]
#     available_tools = list_tools(TOOLS)
#     observation = tool.run(text)
#     return (
#         "Available Tools:\n"
#         f"{available_tools}\n\n"
#         f"Tool used {tool_name} --> {observation}\n"
#     )

# if __name__ == "__main__":
#     q1 = "How many words are there in this bug report?"
#     print(run_agent(q1, "App crashes on login when password is empty"))

#     q2 = "Make this tile and stand out."
#     print(run_agent(q2, "Verify login with valid credentials"))

#     q3 = "Reverse his input and return"
#     print(run_agent(q3, "login"))

#     q4 = "Translate this sentence to latin"
#     print(run_agent(q4, "How are you?"))

# # Drill 4 - Make drill 3 safe (catch close to the user)

# class Tool:
#     """A named tool that agent can choose and run."""
#     def __init__(self, name: str, description: str, func) -> str:
#         self.name = name
#         self.description = description
#         self.func = func
    
#     def run(self, text: str) -> str:
#         return self.func(text)

# def word_count(text: str):
#     """Count and returns the input given."""
#     return len(text.split())

# def shout(text: str):
#     """Returns the input in UPPERCASE format."""
#     return text.upper()

# def reversing(text: str):
#     """Return the reversed word or input given."""
#     return text[::-1]

# TOOLS = {
#     "WordCount": Tool("wordcount", "calculate number of words in the input", word_count),
#     "Shout": Tool("shout", "Conver the input into uppercase", shout),
#     "Reverse": Tool("reverse", "Reverse the given input", reversing),
# }

# def choose_tool(question: str) -> str:
#     """Agent chooses the tool based on the requirement."""
#     if "How many words" in question:
#         return "WordCount"
#     elif "Reverse" in question:
#         return "Reverse"
#     elif "Translate" in question:
#         return "Translate"
#     return "Shout"

# def list_tools(tools: dict) -> str:
#     result = []
#     for tool in tools.values():
#         result.append (f"{tool.name} --> {tool.description}")
#     return "\n".join(result)

# def run_agent(question: str, text:str) -> str:
#     """Choose a tool run and report it."""
#     tool_name = choose_tool(question)
#     if tool_name in TOOLS:
#         tool = TOOLS[tool_name]
#         available_tools = list_tools(TOOLS)
#         observation = tool.run(text)
#         return (
#             "Available Tools:\n"
#             f"{available_tools}\n\n"
#             f"Tool used {tool_name} --> {observation}\n"
#         )
#     return f"Unknown tool: {tool_name}"

# if __name__ == "__main__":
#     q1 = "How many words are there in this bug report?"
#     print(run_agent(q1, "App crashes on login when password is empty"))

#     q2 = "Make this tile and stand out."
#     print(run_agent(q2, "Verify login with valid credentials"))

#     q3 = "Translate this sentence to latin"
#     print(run_agent(q3, "How are you?"))

#     q4 = "Reverse his input and return"
#     print(run_agent(q4, "login"))

# Drill 5 - 

class Tool:
    """A named tool that agent can choose and run."""
    def __init__(self, name: str, description: str, func) -> str:
        self.name = name
        self.description = description
        self.func = func
    
    def run(self, text: str) -> str:
        return self.func(text)

def word_count(text: str):
    """Count and returns the input given."""
    return len(text.split())

def shout(text: str):
    """Returns the input in UPPERCASE format."""
    return text.upper()

def reversing(text: str):
    """Return the reversed word or input given."""
    return text[::-1]

TOOLS = {
    "WordCount": Tool("wordcount", "calculate number of words in the input", word_count),
    "Shout": Tool("shout", "Conver the input into uppercase", shout),
    "Reverse": Tool("reverse", "Reverse the given input", reversing),
}

def choose_tool(question: str) -> str:
    """Agent chooses the tool based on the requirement."""
    if "How many words" in question:
        return "WordCount"
    elif "Reverse" in question:
        return "Reverse"
    elif "Translate" in question:
        return "Translate"
    return "Shout"

def list_tools(tools: dict) -> str:
    result = []
    for tool in tools.values():
        result.append (f"{tool.name} --> {tool.description}")
    return "\n".join(result)

def run_agent(question: str, text:str) -> str:
    """Choose a tool run and report it."""
    tool_name = choose_tool(question)
    if tool_name in TOOLS:
        tool = TOOLS[tool_name]
        available_tools = list_tools(TOOLS)
        observation = tool.run(text)
        return (
            "Available Tools:\n"
            f"{available_tools}\n\n"
            f"Tool used {tool_name} --> {observation}\n"
        )
    return f"Unknown tool: {tool_name}"

if __name__ == "__main__":
    q1 = "How many words are there in this bug report?"
    print(run_agent(q1, "App crashes on login when password is empty"))

    q2 = "Make this tile and stand out."
    print(run_agent(q2, "Verify login with valid credentials"))

    q3 = "Translate this sentence to latin"
    print(run_agent(q3, "How are you?"))

    q4 = "Reverse his input and return"
    print(run_agent(q4, "login"))

    check = [
        
    ]