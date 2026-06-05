"""DSA Day 13 - Problem 1: First non_repeating character."""
from collections import Counter

def first_non_repeating(s:str) -> str:
    """Return first character with count exactly 1, or '-' if none."""
    counts  = Counter(s)
    print(counts)
    for char in s:
        print(char)
        if counts[char] == 1:
            return char
    return '-'

if __name__ == "__main__":
    print(first_non_repeating("leetcode"))
    print(first_non_repeating("loveleetcode"))
    print(first_non_repeating("aabb"))
    print(first_non_repeating("a"))

# Problem 2: Pattern lock: Group Anagrams
"""DSA Day 13 - Problem 2: Group anagrams."""

from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group strings that are anagrams of each other."""

    groups: dict[str, list[str]] = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())

if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)