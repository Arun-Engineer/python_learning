# Problem 1 - Hash map count + group variant
"""Write a function count_word_lengths(words: list[str]) -> dict[int, int] that takes a list of words and returns
a dictionary mapping word length -> how many words have that length."""

from collections import Counter
from collections import defaultdict

words = ["hi", "ok", "yes", "no", "wow", "fine"]

def count_word_lengths(words: list[str]) -> dict[int, int]:
    lengths = []
    for word in words:
        word_length = len(word)
        lengths.append(word_length)

    counts = Counter(lengths)

    return dict(counts)

print(count_word_lengths(words))

def count_word_length(words: list[str]) -> dict[int,int]:
    counts = defaultdict(int)

    for word in words:
        word_len = len(word)
        counts[word_len] = + 1

    return dict(counts)
print(count_word_length(words))

from openai import OpenAI
from dotenv import load_dotenv

def summarize_with_role(client: OpenAI, text: str, audience: str) -> str:

    
    system = f"Your are summarizing for {audience} on this context{text}. Use simple words."
    
    summary_to_user = f"Summary: {text}"

    response =client.chat.completions.create(
        model = "gpt-4o-mini",
        max_tokens= 1000,
        messages= [
            {"role": "system", "content": system},
            {"role": "user", "content": summary_to_user},
        ],
    )

    return response.choices[0].message.content

if __name__ == "__main__":

    load_dotenv()
    client = OpenAI()

    text = """Anthropic co-founder Jack Clark has called for the ability to slow progression of artificial intelligence (AI), warning the technology is nearing a point where it could develop without human input.

"You want the option to be able to take your foot off the gas and put your foot on the brake", Clark told BBC Newsnight. "Right now, it's like the AI industry has a gas pedal, but it doesn't have a brake pedal."

He stressed people, through government policy, need to keep control of AI systems, which will only get more powerful and have broader impacts on society.

"The world needs to do some thinking and we need to eventually develop some new regulations that allow us to be confident in these systems," he said.

Already, Anthropic's popular chatbot Claude is operating on code of which 80% the system wrote itself. Getting to 100% is possible within two years, Clark said, and "would have huge implications".

Clark did not outline how a "brake pedal" for AI research and development could be created, but drew a parallel between AI and the oil boom and barons of the turn of the last century.

"Society's response was to come up with a sensible policy and regulatory framework that gave people confidence in oil and the benefits that oil could provide to the world, and meant that you didn't have to worry about the personalities of the people leading the companies", Clark said. "That's clearly where we end up here."

Yet, Anthropic this week welcomed an executive order on AI from US President Donald Trump that was relatively hands-off in its directives toward the companies.

"""
    summary = summarize_with_role(client, text, "5year-old child")
    summary1  = summarize_with_role(client, text, "machine learning reseacher")

    print()
    print(f"This summmary is for 5year-old child {summary}")
    print(f"\nThis summmary is for mchine learning reasearcher {summary1}")
