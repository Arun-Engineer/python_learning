# Drill 3 - A System prompt (OpenAI Pattern Differs Slightly)
from dotenv import load_dotenv
from openai import OpenAI

def ask_with_persona(question: str, persona: str) -> str:
    """Ask OpenAI a question with a system prompt setting its persona."""
    load_dotenv()
    client = OpenAI()

    response = client.chat.completions.create(
        model= "gpt-4o-mini",
        max_tokens= 300,
        messages= [
            {"role": "system", "content": persona},
            {"role": "user", "content": question}
        ],
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    question = "Tell me how to write a python function."

    expert_answer = ask_with_persona(
        question,
        "You are a senior Python engineer with 15 years of experience. Be concise and direct"
    )

    teacher_answer = ask_with_persona(
        question,
        "You are a patient tecaher explaining Python to a complete beginner."
    )

    poet_answer = ask_with_persona(
        question,
        "You are a poet who writes everything in haiku form."
    )

    print("---- EXPERT ----")
    print(expert_answer[:300])
    print("\n---- TEACHER ----")
    print(teacher_answer[:300])
    print("\n---- POET ----")
    print(poet_answer[:300])