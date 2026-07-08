# def my_style_plaindrome(text: str) -> bool:
#     return text == text[::-1]

# print(my_style_plaindrome("level"))
# print(my_style_plaindrome("text"))

# # Task A
# def is_palindrome(text: str) -> bool:
#     left = 0
#     right = len(text)-1

#     while left < right:
#         if text[left] != text[right]:
#             return False
#         left +=1
#         right -=1
#     return True

# if __name__ == "__main__":
#     for word in ["level", "hello", "noon"]:
#         print(word, "-->", is_palindrome(word))

# Task B
def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    left = 0
    right = len(cleaned)-1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left +=1
        right -=1
    return True

if __name__ == "__main__":
    for word in ["race car", "hello cat", "noon noon"]:
        print(word, "-->", is_palindrome(word))

