# main.py - uses the greeting module
from greetings import hello, goodbye, GREETING_LANGUAGAE
from calculator import add, multiply, is_even

print(f"Greeting Language: {GREETING_LANGUAGAE}")
print(hello("Priya"))
print(goodbye("Priya"))
print(f"2 + 3 = {add(2, 3)}")
print(f"2 * 3 = {multiply(2, 3)}")
print(f"Is 10 even? = {is_even(10)}")