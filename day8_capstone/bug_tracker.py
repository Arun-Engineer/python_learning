import json

from persistence import load_bugs, save_bugs
from reporting import format_report
from models import Bug

seed_bugs: list[Bug] = [
    Bug(id= 1, title= "Login crash on IOS", severity= 5, status= "open", team= "mobile"),
    Bug(id= 2, title= "Typo on homepage", severity= 1, status= "open", team= "web"),
    Bug(id= 3, title= "Payment timeout", severity= 5, status= "open", team= "backend"),
    Bug(id= 4, title= "Logo color wrong", severity= 1, status= "closed", team= "web"),
    Bug(id= 5, title= "API returns 500", severity= 4, status= "open", team= "backend"),
    Bug(id= 6, title= "Slow scroll on Android", severity= 3, status= "open", team= "mobile"),
    Bug(id= 7, title= "Forget password broken", severity= 4, status= "closed", team= "backend"),
    Bug(id= 8, title= "Footer link 404", severity= 2, status= "open", team= "web"),
]


class BugTracker:
    def __init__(self, filename: str):
        self.filename: str = filename
        self.bugs: list[Bug] = load_bugs(self.filename, seed_bugs)

    def next_bug_id(self) -> int:
        if not self.bugs:
            return 1

        return max(bug.id for bug in self.bugs) + 1


    def add_bug(self, title: str, severity: int, status: str, team: str) -> Bug:

        new_bug = Bug(
            id= self.next_bug_id(),
            title= title,
            severity= int(severity),
            status= status,
            team= team,
        )

        self.bugs.append(new_bug)

        save_bugs(self.bugs, self.filename)

        return new_bug
    
    def report(self) -> str:
        return format_report(self.bugs)