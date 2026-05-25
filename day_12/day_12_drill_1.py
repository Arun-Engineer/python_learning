# Drill 1 - Multiple Questions in sequence
from first_LLM_call import ask_openai

def ask_multiple(questions: list[str]) -> list[str]:
    """Ask OpenAI multiple separate questions, return the answer list."""
    
    answers = []
    for q in questions:
        answer = ask_openai(q)
        answers.append(answer)
    return answers

if __name__ == "__main__":
    questions = [
        "What is on thing every python developer should know about lists?",
        "What is the difference between a tuple and a list?.",
        "What is one thing every Python developer should know about dicts?."
    ]

    answers = ask_multiple(questions)
    for q, a in zip(questions, answers):
        print(f"\nQ: {q}")
        print(f"A: {a[:200]}.....")