# test_models.py - testing the bug dataclass

from models import Bug

def test_bug_creator():
    """A bug can be created with all fields.."""

    bug = Bug(id=1, title= "Login Broken", severity= 5, status= "open", team= "mobile")
    assert bug.id == 1
    assert bug.title == "Login Broken"
    assert bug.severity == 5
    assert bug.status == 'open'
    assert bug.team == "mobile"

def test_bug_equality():
    """Two Bugs with same fields are equal - free from @dataclass"""

    bug1 = Bug(id=1, title= "X", severity= 5, status= "open", team= "mobile")
    bug2 = Bug(id=1, title= "X", severity= 5, status= "open", team= "mobile")

    assert bug1 == bug2

def test_bug_inequality():
    """Two Bugs with different fields are not equal."""
    bug1 = Bug(id=1, title= "X", severity= 5, status= "open", team= "mobile")
    bug2 = Bug(id=1, title= "X", severity= 5, status= "open", team= "mobile")

    assert bug1 != bug2
