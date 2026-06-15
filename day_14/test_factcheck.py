from factcheck import ask_fact, is_factual

# --- Test the checker logic directly (no mock needed) ----

def test_is_factual_passes_when_fact_present():
    assert is_factual("The capital is Paris.", "Paris") is True

def test_is_factual_fails_when_fact_missig():
    assert is_factual("The capital is London.", "Paris") is False

# ---- Test ask_fact using the shared fake_clients fixture ----

def test_ask_fact_uses_the_client(fake_client):
    # tell the fake client what to reply when create() is called:
    fake_client.chat.completions.create.return_value.choices[0].message.content = "Paris"

    answer = ask_fact(fake_client, "what is the capital of France?")

    assert answer == "Paris"
    fake_client.chat.completions.create.assert_called_once()

# --- Factuality check against the shared knowledge_base fixture --- 

def test_answers_match_knowledge_base(fake_client, knowledge_base):
    for question, expected in knowledge_base.items():
        # Simulate the model returning the correct fact each time:
        fake_client.chat.completions.create.return_value.choices[0].message.content = expected
        answer = ask_fact(fake_client, question)
        assert is_factual(answer, expected)

def test_catches_wrong_answer(fake_client):
    fake_client.chat.completions.create.return_value.choices[0].message.conten = "London"
    answer = ask_fact(fake_client, "What is the capital of France?")
    assert is_factual(answer, "Paris") is False