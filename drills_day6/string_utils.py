# Drill 1 - Build a string_utils.py module
def  count_words(text):
    words = text.split(",")
    return len(words)

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    if reverse_text(text) == text:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(count_words("aeroplane ,cat, rat"))
    print(reverse_text("madam"))
    print(is_palindrome("madam"))

