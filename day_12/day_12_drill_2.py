# Drill 2: A Multi Turn Conversation
from dotenv import load_dotenv
from openai import OpenAI

def have_conversation(turns: list[str]) -> list[str]:
    """
    Run a multi-turn conversation with OpenAI.
    Returns the assistant's responses in order.
    """
    load_dotenv()
    client = OpenAI()

    messages = []
    responses = []
    for user_message in turns:
        # Append the user's message
        messages.append({"role": "user", "content": user_message})

        # Send the FUll conversation so far
        response = client.chat.completions.create(
            model= "gpt-4o-mini",
            max_tokens= 1024,
            messages = messages,
        )

        # Extract the response text
        assistant_answer = response.choices[0].message.content
        responses.append(assistant_answer)

        # IMPORTANT: append the assistant's response so the next call sees it
        messages.append({"role": "assistant", "content": assistant_answer})

    return responses

if __name__ == "__main__":
    conversation =[
        "I m learning python. Whats the most important concept i should master first?",
        "Can you give  me one specific exercise to practice it?.",
        "How will i know when i ve mastered it?."
    ]
    responses = have_conversation(conversation)
    for i, (q, r) in enumerate(zip(conversation, responses), 1):
        print(f"\n--- Turn {i} ---")
        print(f"USER: {q}")
        print(f"ASSISTANT: {r[:200]}...")