# B1- Two pointers (today's DSA muscle):
# Write revers_in_place(items: list) -> list that reverses a list using the two-pointer
#swap(not [::-1], not .reverse()). Swap the ends, move inward

#eg -> reverse_in_place([1,2,3,4]) # -> [4,3,2,1]

def reverse_in_place(items: list) -> list:

    left = 0
    right = len(items)-1

    while left < right:
        temp = items[left]
        items[left] = items[right]
        items[right] = temp
        left = left + 1
        right = right - 1

    return items

print(reverse_in_place([1,2,3,4]))

# B2: Agent decision test(the career skill):

import block2

def check_tool_choice(question: str, expected: str) -> bool:
    result =  block2.choose_tool(question)
    return result == expected

print(check_tool_choice("How many words in this sentence", "WordCount"))

