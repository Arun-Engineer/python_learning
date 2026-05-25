"""Tests for llm_client.ask() using fixtures + MagicMock."""

from llm_client import ask

def test_ask_returns_response_text(mock_openai_client, sample_question):
    """ask() should return the .content string from the API response."""
    result = ask(mock_openai_client, sample_question)
    assert result == "This is a fake GPT response."

def test_ask_calls_api_with_correct_model_and_messages(mock_openai_client, sample_question):
    """ask() should call create() with model='gpt-4o-mini' and a single user message."""
    ask(mock_openai_client, sample_question)

    mock_openai_client.chat.completions.create.assert_called_once()
    call_kwargs = mock_openai_client.chat.completions.create.call_args.kwargs

    assert call_kwargs["model"] == "gpt-4o-mini"
    assert call_kwargs["messages"] == [{"role": "user", "content": "What is a Python?"}]

def test_ask_includes_system_prompt_when_provided(mock_openai_client):
    ask(mock_openai_client, "Hi", system= "You are a senior engineer.")

    call_kwargs = mock_openai_client.chat.completions.create.call_args.kwargs

    assert call_kwargs["messages"][0] == {"role": "system", "content": "You are a senior engineer."}
    assert call_kwargs["messages"][1] == {"role": "user", "content": "Hi"}

def test_ask_skips_system_message_when_none(mock_openai_client):
    """When system is None, Only the user message should be sent."""

    ask(mock_openai_client, "Hi")
    call_kwargs = mock_openai_client.chat.completions.create.call_args.kwargs

    assert len(call_kwargs["messages"]) == 1
    assert call_kwargs["messages"][0] == {"role": "user", "content": "Hi"}