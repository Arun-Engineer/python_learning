# Given scores = [45,82,67,91,55,78] create a list of only scores above 70 using list comprehension.
scores = [45, 82, 67, 91, 55, 78]
high_scores = [i for i in scores if i > 70]
print(high_scores)

# Given words = ["hello", "world", "python", "AI"] create a list of their lengths
words = ["hello", "world", "python", "AI"]
lengths = [len(i) for i in words]
print(lengths)

# Create a dict Comprehension: word ---> word reversed(hint: word[::-1])
reversed_words = {i: i[::-1] for i in words}
print(reversed_words)