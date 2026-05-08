import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from drills_day6.string_utils import count_words, is_palindrome
from drills_day6.math_utils import factorial, is_prime
from models import Bug


def test_count_words_normal():
    """Multiply words seperated by spaces"""
    words = "the quick brown fox"
    assert count_words(words) == 4

def test_count_words_empty():
    """Empty string has zero words."""
    assert count_words("") == 0

def test_count_words_single():
    "One word returns 1."
    word = count_words("the")
    assert word == 1

def test_count_words_mutiple_spaces():
    """Multiple spaces between words still counts correctly."""
    assert count_words("hello  world") == 2

# drill2 - Test is_palindrome

def test_is_plaindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("Madam") == True

# drill- Test Factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(1) == 1

# drill 4 - Test is_prime
def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(15) == False
    assert is_prime(0) == False

# drill 5 - Find a real bug with a test

def test_next_bug_id_with_existing_bugs():
    """Next_bug_id returns max id + 1."""
    # Arrange  - create some bugs
    bugs = [
        Bug(id=5, title= "A", severity= 1, status= "open", team= "x"),
        Bug(id=2, title= "B", severity= 1, status= "open", team= "x"),
        Bug(id=8, title= "C", severity= 1, status= "closed", team= "x"),
    ]

    from bug_tracker import BugTracker
    track = BugTracker("bug.json")
    track.bugs = bugs
    assert track.next_bug_id() == 9

