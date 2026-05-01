# section 1: your first function
def greet(name):
    """Say hello to someone"""
    return f"Hello, {name}"

print(greet("Arun"))

# section 2: print vs return -- the trap
def add_print(a, b):
    print(a + b)
def add_return(a, b):
    return a + b
print(f"from add_print: {add_print(3, 2)}")
print(f"from add_return: {add_return(3, 2)}")

# section 3: A useful function
def is_critical(severity, status):
    """Return True if bug is open and severity >= 4."""
    return status == "open" and severity >=4
print(is_critical(5, "open"))
print(is_critical(2, "open"))
print(is_critical(5, "closed"))

# section 4: functions that work on dicts
def is_critical_bug(bug):
    """Return True if bug dict represents a critical issue."""
    return bug["status"] == "open" and bug["severity"] >=4

ex_bug = {"bug_id": 1, "severity": 5, "status": "open"}
print(is_critical_bug(ex_bug))

# section 5: functions that loop
def count_open(bugs):
    """Return the number of open bugs."""
    count = 0
    for bug in bugs:
        if bug["status"] == "open":
            count = count + 1
    return count

bugs = [
    {"id": 1, 'status': "open"},
    {"id": 2, 'status': "closed"},
    {"id": 3, 'status': "open"},
]

print(f"Open_bugs: {count_open(bugs)}")

# section 6: Default parameters
def filter_critical(bugs, min_serverity = 4):
    """Return bugs that are open and meet min_severity"""
    result = []
    for bug in bugs:
        if bug["status"] == "open" and  bug["severity"] >= min_serverity:
            result.append(bug)
    return result

bugs2 = [
    {"id": 1, "severity": 5, "status": "open"},
    {"id": 2, "severity": 3, "status": "open"},
    {"id": 3, "severity": 5, "status": "closed"},
]

print(filter_critical(bugs2))
print(filter_critical(bugs2, min_serverity=3))

