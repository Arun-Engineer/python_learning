# drill 1 - Hello function

def greet(name):
    """Say hello to someone"""
    return f"Hello, {name}! Welcome."

print(greet("Arun"))
print(greet("Jarvis"))

# drill 2 - Math machine
def calculate_severity_score(severity, frequency):
    """Calculate severity_score by muliplying the severity and no of time it repeated = severity * frequency"""
    return severity * frequency

print(f"severity_score: {calculate_severity_score(5, 3)}")

# drill 3 -- the boolean

def is_blocker(bugs):
    """That take bug dict and return True if bug['severity'] == 5""" 
    return bugs["severity"] == 5
bug1 = {"id": 1, "severity": 5, "status": "open"}
bug2 = {"id": 2, "severity": 3, "status": "open"}


print(is_blocker(bug1))
print(is_blocker(bug2))

# Drill 4: The counter
def count_bugs_by_status(bugs, target_status):
    """Return the number of bugs matching the given status"""
    open_count = []
    closed_count = []
    for bug in bugs:
        if bug["status"] == "open" and target_status == "open":
            open_count.append(bug)
        elif bug["status"] == 'closed' and target_status == "closed":
            closed_count.append(bug)
    return f"Open Bug Count: {len(open_count)}, Closed Bug Count: {len(closed_count)}"

bugs = [
    {"id": 1, "severity": 5, "status": "open"},
    {"id": 2, "severity": 3, "status": "open"},
    {"id": 3, "severity": 5, "status": "closed"},
]

print(count_bugs_by_status(bugs, "open"))
print(count_bugs_by_status(bugs, "closed"))

# Drill 5: the filter
def get_bugs_by_team(bugs, team_name):
    """get bug by team and return a list of bugs belonging to the given team"""
    bug_team = []
    for bug in bugs:
        if bug["team"] == team_name:
            bug_team.append(bug)
    return bug_team

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

print(get_bugs_by_team(bugs, "web"))

# Drill 6 - Trap test
def double_print(n):
    print(n * 2) # This function returns none when it called and stored in a variable and print that variable

def double_return(n):
    return(n * 2) # This function reutns the value for if input is given n=2 so 2*2=4 when stored in a variable and printed

print(double_print(2))
print(double_return(2))

# Drill 7 - Composition (functions calling functions)
def is_critical_bug(bugs):
    count = 0
    for bug in bugs:
        if bug["status"] == "open" and bug["severity"] >= 4:
            count = count + 1
    return count

print(is_critical_bug(bugs))