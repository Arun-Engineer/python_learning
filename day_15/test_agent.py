import block2
import drills

# -----1) Test the brian's decisions directly (no patching needed)

def test_choose_tool_picks_wordcount():
    assert block2.choose_tool("How many words are there?") == "WordCount"

def test_choose_tool_defaults_to_shout():
    assert block2.choose_tool("Make this loud") == "Shout"

# ----2) Use monkeypatch to FORCE the brain's choice, then test the loop -----

def test_run_agent_uses_chosen_tool(monkeypatch):
    # force choose_tool to always return "WordCount", no matter the question:
    monkeypatch.setattr(block2, "choose_tool", lambda question: "WordCount")
    result = block2.run_agent ("anything at all", "login bug here")
    assert "WordCount" in result
    assert "3" in result

def test_agent_use_chosen_tool(monkeypatch):
    monkeypatch.setattr(drills, "choose_tool", lambda question: "Translate")
    results = drills.run_agent("Translate this sentence to latin", "How are you?")
    assert "Unknown tool: Translate" in results