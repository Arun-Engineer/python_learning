from drills import choose_tool

checks = [
    ("How many words here?",            "WordCount"),
    ("How many words in this text?",    "WordCount"),
    ("Make this loud",                  "Shout"),
    ("Make this title stand out",       "Shout"),
]

print("="* 50)
print("AGENT TOOL SELECTION CONFIDENCE CHECK")
print("=" * 50)

passed = 0
failed = 0

for question, expected in checks:
    actual = choose_tool(question)
    if actual == expected:
        status = "Correct"
        passed +=1
    else:
        status = f"Incorrect since expected is -> {expected}"
        failed +=1
    print(f"{question:<35} -> {actual:<10} {status}")

print("=" * 50)
print(f"Passed: {passed} | Failed: {failed} | Total: {passed+failed}")
print("=" * 50)
