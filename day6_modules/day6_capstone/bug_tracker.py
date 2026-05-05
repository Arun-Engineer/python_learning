import json

from persistence import load_bugs, save_bugs
from reporting import format_report

seed_bugs = [
    {"id": 1, "title": "Login crash on IOS", "severity": 5, "status": "open", "team": "mobile"},
    {"id": 2, "title": "Typo on homepage", "severity": 1, "status": "open", "team": "web"},
    {"id": 3, "title": "Payment timeout", "severity": 5, "status": "open", "team": "backend"},
    {"id": 4, "title": "Logo color wrong", "severity": 1, "status": "closed", "team": "web"},
    {"id": 5, "title": "API returns 500", "severity": 4, "status": "open", "team": "backend"},
    {"id": 6, "title": "Slow scroll on Android", "severity": 3, "status": "open", "team": "mobile"},
    {"id": 7, "title": "Forget password broken", "severity": 4, "status": "closed", "team": "backend"},
    {"id": 8, "title": "Footer link 404", "severity": 2, "status": "open", "team": "web"},
]


class BugTracker:
    def __init__(self, filename):
        self.filename = filename
        self.bugs = load_bugs(self.filename, seed_bugs)

    def next_bug_id(self):
        if not self.bugs:
            return 1

        return max(bug["id"] for bug in self.bugs) + 1


    def add_bug(self, title, severity, status, team):

        new_bug = {
            "id": self.next_bug_id(),
            "title": title,
            "severity": int(severity),
            "status": status,
            "team": team
        }

        self.bugs.append(new_bug)

        save_bugs(self.bugs, self.filename)

        return new_bug
    
    def report(self):
        return format_report(self.bugs)