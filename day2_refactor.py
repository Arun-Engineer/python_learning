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

print("="*10, " BUG TRIAGE REPORT ", "="*10 )
print()
print(f"Total Bugs: {len(bugs)}")
open=[]
closed=[]
for bug in bugs:
    if bug["status"]=="open":
        open.append(bug["id"])
    else:
        closed.append(bug["id"])
print(f"\n Open: {len(open)}\n Closed: {len(closed)}")
print("\n")
print("CRITICAL BUGS NEEDING ATTENTION (open + severity >= 4): ")
for bug in bugs:
    if bug["severity"]>=4 and bug["status"]=="open":
        print(f"\n - Bug #{bug["id"]}: {bug["title"]}")
print()
print("Bugs by team (open only): ")
team_counts = {}
for bug in bugs:
    if bug["status"] == "open":
        team = bug["team"]
        team_counts[team]= team_counts.get(team, 0) + 1
print(team_counts)
