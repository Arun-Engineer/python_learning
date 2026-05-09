from bug_tracker import Bug
from bug_tracker import BugTracker

bugs = [
        Bug(id=1, title= "A", severity= 1, status= "open", team= "web"),
        Bug(id=2, title= "B", severity= 4, status= "open", team= "mobile"),
        Bug(id=3, title= "C", severity= 2, status= "closed", team= "web"),
        Bug(id=4, title= "D", severity= 5, status= "open", team= "web"),
        Bug(id=5, title= "E", severity= 3, status= "open", team= "mobile"),
    ]

track = BugTracker("test_roundtrip.json")
track.bugs = bugs

def test_add_bug():
    new = track.add_bug("payment_failed", 5, "open", "mobile")
    assert new.id == 6
    assert new.title == "payment_failed"
    assert new.severity == 5
    assert new.status == "open"
    assert new.team == "mobile"
