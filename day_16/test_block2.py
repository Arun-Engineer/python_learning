from unittest.mock import MagicMock
from block1_updated import choose_tool_llm, TOOLS, run_agent

def test_choose_tool():
    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value.choices[0].message.content = "Translate"
    result = run_agent(fake_client, "Translate this text to French.", "Hello, how are you?", TOOLS)
    print(f"Result: {result}")
    assert result .lower() == "model picked an unkown tool: Translate".lower()
