# Drill 1 - Build a string_utils.py module
def  count_words(text):
    words = text.split()
    return len(words)

def reverse_text(text):
    clean_txt = text.lower()
    return clean_txt[::-1]

def is_palindrome(text):
    cleaned_txt = text.lower
    if reverse_text(text) == cleaned_txt:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(count_words("aeroplane, cat, rat"))
    print(reverse_text("madam"))
    print(is_palindrome("madam"))

