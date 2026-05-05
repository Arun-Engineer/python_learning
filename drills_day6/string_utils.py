# Drill 1 - Build a string_utils.py module
def  count_words(text):
    words = text.split()
    return len(words)

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    cleaned_txt = text.lower()
    return cleaned_txt == cleaned_txt[::-1]
    
if __name__ == "__main__":
    print(count_words("the quick brown fox"))
    print(count_words(""))
    print(reverse_text("Python"))
    print(is_palindrome("Madam"))

