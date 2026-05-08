# test_reporting.py -- testing reporting functions

from models import Bug
from reporting import get_critical_bugs, get_bug_counts_by_status, count_open_bugs_by_team

def test_get_critical_bugs_finds_critical():
    """A bug that's open with severity >= 4 is crititcal."""
    bugs = [
        Bug(id=1, title= "Bad", severity= 5, status= "open", team= "mobile"),
        Bug(id=1, title= "OK", severity= 2, status= "open", team= "web"),
        Bug(id=1, title= "Closed crit", severity= 5, status= "closed", team= "backend"),
    ]

    critical = get_critical_bugs(bugs)
    assert len(critical) == 1
    assert critical[0].id == 1

def test_get_critical_bugs_empty_list():
    """An empty list of bugs has zero critical bugs."""

    assert get_critical_bugs([]) == []

def test_get_critical_bugs_all_closed():
    """No open bugs means no critical bugs, even if severity is high."""
    bugs = [
        Bug(id=1, title= "Closed", severity= 5, status= "closed", team= "x"),
        Bug(id=1, title= "Closed", severity= 4, status= "closed", team= "y"),
    ]

    assert get_critical_bugs(bugs) == []

def test_status_counts_basic():
    bugs = [
        Bug(id=1, title= "A", severity= 1, status= "open", team= "x"),
        Bug(id=1, title= "B", severity= 1, status= "open", team= "x"),
        Bug(id=1, title= "C", severity= 1, status= "closed", team= "x"),
    ]
    counts = get_bug_counts_by_status(bugs)
    assert counts == {"open": 2, "closed": 1}