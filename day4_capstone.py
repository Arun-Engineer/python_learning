import json

seed_bugs = [
    {"id":1, "title": "Login crash on IOS", "severity": 5, "status": "open", "team": "mobile"},
    {"id":2, "title": "Typo on homepage", "severity": 1, "status": "open", "team": "web"},
    {"id":3, "title": "Payment timeout", "severity": 5, "status": "open", "team": "backend"},
    {"id":4, "title": "Logo color wrong", "severity": 1, "status": "closed", "team": "web"},
    {"id":5, "title": "API returns 500", "severity": 4, "status": "open", "team": "backend"},
    {"id":6, "title": "Slow scroll on Android", "severity": 3, "status": "open", "team": "mobile"},
    {"id":7, "title": "Forget password broken", "severity": 4, "status": "closed", "team": "backend"},
    {"id":8, "title": "Footer link 404", "severity": 2, "status": "open", "team": "web"},
]

def load_bugs(filename):
    try:
        with open(filename, "r")as f:
            loaded_bug = json.load(f)
            return loaded_bug
    except FileNotFoundError:
        print("No previous bugs found - starting fresh")
        save_bugs(seed_bugs,filename)
        return seed_bugs
    except json.JSONDecodeError:
        print(f"file '{filename}' is corrupted - starting fresh")
        return []
    

#print(load_bugs("bug.json"))

def save_bugs(bugs, filename):

    with open (filename, "w")as f:
        json.dump(bugs, f, indent=2)
    print("Bug added to file successfully")

#print(save_bugs(bugs, "bug.json"))

new_bugs = [
    {"id":9, "title": "Login crash on Android", "severity": 3, "status": "open", "team": "mobile"},
    {"id":10, "title": "Typo on PDP", "severity": 2, "status": "closed", "team": "web"}
]

def next_bug_id(bugs):
    if not bugs:
        return 1
    return max(bug["id"] for bug in bugs) + 1

def add_bugs(filename, new_bugs):
    existing_bugs = load_bugs(filename)
    existing_bugs.extend(new_bugs)
    save_bugs(existing_bugs, filename)

print(add_bugs("bug.json", new_bugs))

def get_bug_counts_by_status(bugs):
    bugs_count_status = {}

    for bug in bugs:
        bug_status = bug.get("status")

        if bug_status is not None:
            bugs_count_status[bug_status] = bugs_count_status.get(bug_status, 0) + 1

    return bugs_count_status


def get_critical_bugs(bugs):
    critical_bugs = []

    for bug in bugs:
        if bug["status"] == "open" and bug["severity"] >= 4:
            critical_bugs.append(bug)

    return critical_bugs


def count_open_bugs_by_team(bugs):
    open_bug_count = {}

    for bug in bugs:
        if bug["status"] == "open":
            team = bug["team"]
            open_bug_count[team] = open_bug_count.get(team, 0) + 1

    return open_bug_count


def bug_report_from_json(filename):
    bugs = load_bugs(filename)

    print()
    print("=" * 10, "BUG REPORT", "=" * 10)
    print()

    bug_count = get_bug_counts_by_status(bugs)

    open_bugs = bug_count.get("open", 0)
    closed_bugs = bug_count.get("closed", 0)
    total_bugs = open_bugs + closed_bugs

    print(f"Total_bugs: {total_bugs}")
    print(f"Open_bugs: {open_bugs}")
    print(f"Closed_bugs: {closed_bugs}")

    print()
    print("CRITICAL BUGS NEEDING ATTENTION (open + severity >= 4)")

    critical_bugs = get_critical_bugs(bugs)

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

    open_bugs_team = count_open_bugs_by_team(bugs)

    if len(open_bugs_team) == 0:
        print("No open bugs found")
    else:
        for team, count in open_bugs_team.items():
            print(f"- {team}: {count}")

    print()
    print("=" * 10, "END OF REPORT", "=" * 10)


bug_report_from_json("bug.json")

# refactored add- bugs
def add_bugs(filename, new_bugs):
    existing_bugs = load_bugs(filename)
    updated_bugs = existing_bugs + new_bugs
    save_bugs(existing_bugs, filename)
    return updated_bugs