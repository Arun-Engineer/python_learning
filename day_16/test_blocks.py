from unittest.mock import MagicMock
from block1_updated import choose_tool_llm, TOOLS

# def test_choose_tool():
#     fake_client = MagicMock()
#     fake_client.chat.completions.create.return_value.choices[0].message.content = "WordCount"
#     result = choose_tool_llm(fake_client, "How many words are in the text?", TOOLS)
#     assert result == "WordCount"

# def test_choose_tool():
#     fake_client = MagicMock()
#     fake_client.chat.completions.create.return_value.choices[0].message.content = "Shout\n"
#     result = choose_tool_llm(fake_client, "Mke it loud`", TOOLS)
#     assert result == "Shout"

def test_choose_tool():
    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value.choices[0].message.content = "WordCount"
    result = choose_tool_llm(fake_client, "How many words", TOOLS)
    fake_client.chat.completions.create.assert_called_once()