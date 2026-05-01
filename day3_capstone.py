bugs = [
    {"id":1, "title": "Login crash on IOS", "severity": 5, "status": "open", "team": "mobile"},
    {"id":2, "title": "Typo on homepage", "severity": 1, "status": "open", "team": "web"},
    {"id":3, "title": "Payment timeout", "severity": 5, "status": "open", "team": "backend"},
    {"id":4, "title": "Logo color wrong", "severity": 1, "status": "closed", "team": "web"},
    {"id":5, "title": "API returns 500", "severity": 4, "status": "open", "team": "backend"},
    {"id":6, "title": "Slow scroll on Android", "severity": 3, "status": "open", "team": "mobile"},
    {"id":7, "title": "Forget password broken", "severity": 4, "status": "closed", "team": "backend"},
    {"id":8, "title": "Footer link 404", "severity": 2, "status": "open", "team": "web"},
]

def get_bug_counts_by_status(bugs):
    bugs_count_status = {}
    for bug in bugs:
        if bug["status"] is not None:
            bug_status = bug["status"]
            bugs_count_status[bug_status] = bugs_count_status.get(bug_status, 0) + 1
    return bugs_count_status

print(get_bug_counts_by_status(bugs))

def get_critical_bugs(bugs):
    critical_bugs = []
    for bug in bugs:
        if bug['status'] == "open" and bug["severity"] >= 4:
            critical_bugs.append(bug)
    return critical_bugs
print(f"Critcial_bugs: {get_critical_bugs(bugs)}")

def count_open_bugs_by_team(bugs):
    open_bug_count = {}
    for bug in bugs:
        if bug["status"] == "open":
            team = bug["team"]
            open_bug_count[team] = open_bug_count.get(team, 0) + 1
    return open_bug_count
print(f"Count open bugs by team: {count_open_bugs_by_team(bugs)}")

def bug_report(bugs):
    print("\n")
    print("=" * 10, " BUG REPORT ","="*10)
    print()
    bug_count = get_bug_counts_by_status(bugs)
    total_bugs = bug_count["open"] + bug_count["closed"]
    print(f"Total_bugs: {total_bugs}")
    print(f"Open_bugs: {bug_count['open']}")
    print(f"Closed_bugs: {bug_count['closed']}")

    print()
    print("CRITICAL BUGS NEEDING ATTENTION (open + severity >= 4)")
    critical_bugs = get_critical_bugs(bugs)
    for critical_bug in critical_bugs:
        print(f"- Bug id: {critical_bug['id']} Title: {critical_bug['title']} ")
    print()
    print("Bugs by team (open only): ")
    open_bugs_team = count_open_bugs_by_team(bugs)
    for bugs_team, count in open_bugs_team.items():
        print(f"-{bugs_team}: {count}")
    print()
    return f"{'='*10} END OF REPORT {'='*10}"  
print(bug_report(bugs))
