import json


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
        self.bugs = self.load_bugs()

    def load_bugs(self):
        try:
            with open(self.filename, "r") as f:
                loaded_bugs = json.load(f)

            return loaded_bugs

        except FileNotFoundError:
            print("No previous bugs found - starting fresh")
            self.bugs = seed_bugs.copy()
            self.save_bugs()
            return seed_bugs.copy()

        except json.JSONDecodeError:
            print(f"File '{self.filename}' is corrupted - resetting fresh")
            self.bugs = seed_bugs.copy()
            self.save_bugs()
            return seed_bugs.copy()

    def save_bugs(self):
        with open(self.filename, "w") as f:
            json.dump(self.bugs, f, indent=2)

        print("Bugs saved successfully")

    def next_id(self):
        if not self.bugs:
            return 1

        return max(bug["id"] for bug in self.bugs) + 1

    def add_bug(self, title, severity, status, team):
        new_bug = {
            "id": self.next_id(),
            "title": title,
            "severity": int(severity),
            "status": status,
            "team": team
        }

        self.bugs.append(new_bug)
        self.save_bugs()

        return new_bug

    def get_critical_bugs(self):
        critical_bugs = []

        for bug in self.bugs:
            if bug["status"] == "open" and bug["severity"] >= 4:
                critical_bugs.append(bug)

        return critical_bugs

    def get_bug_counts_by_status(self):
        bug_count_status = {}

        for bug in self.bugs:
            bug_status = bug.get("status")

            if bug_status is not None:
                bug_count_status[bug_status] = bug_count_status.get(bug_status, 0) + 1

        return bug_count_status

    def count_open_bugs_by_team(self):
        open_bug_count = {}

        for bug in self.bugs:
            if bug["status"] == "open":
                team = bug["team"]
                open_bug_count[team] = open_bug_count.get(team, 0) + 1

        return open_bug_count

    def print_report(self):
        print()
        print("=" * 10, "BUG REPORT", "=" * 10)
        print()

        bug_count = self.get_bug_counts_by_status()

        open_bugs = bug_count.get("open", 0)
        closed_bugs = bug_count.get("closed", 0)
        total_bugs = open_bugs + closed_bugs

        print(f"Total_bugs: {total_bugs}")
        print(f"Open_bugs: {open_bugs}")
        print(f"Closed_bugs: {closed_bugs}")

        print()
        print("CRITICAL BUGS NEEDING ATTENTION (open + severity >= 4)")

        critical_bugs = self.get_critical_bugs()

        if len(critical_bugs) == 0:
            print("No critical bugs found")
        else:
            for critical_bug in critical_bugs:
                print(
                    f"- Bug id: {critical_bug['id']} "
                    f"Title: {critical_bug['title']} "
                    f"Severity: {critical_bug['severity']} "
                    f"Team: {critical_bug['team']}"
                )

        print()
        print("Bugs by team (open only):")

        open_bugs_team = self.count_open_bugs_by_team()

        if len(open_bugs_team) == 0:
            print("No open bugs found")
        else:
            for team, count in open_bugs_team.items():
                print(f"- {team}: {count}")

        print()
        print("=" * 10, "END OF REPORT", "=" * 10)