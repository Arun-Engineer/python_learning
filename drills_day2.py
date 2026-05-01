# Drill 1
# Create a list of 6 severities. Use a for loop to print each one with the format: "Bug severity: 3".

severities = [1,2,4,5,3,2]
for severity in severities:
    print(f"Bug severity: {severity}")

# Drill 2 - the filter (the diagnostic from day 1!)
# printthe id of bug that are open and severity>3
bugs = [
    {"id": 1, "severity": 5, "status": "open"},
    {"id": 2, "severity": 2, "status": "closed"},
    {"id": 3, "severity": 4, "status": "open"},
    {"id": 4, "severity": 1, "status": "closed"},
    {"id": 5, "severity": 3, "status": "open"},
]

for bug in bugs:
    if bug["status"]=="open" and bug["severity"]>3:
        print(f"Bug ID: {bug["id"]}")
    else:
        pass

# Drill 3- The counter
# print the result of closed bugs

Closed_bugs=0
for bug in bugs:
    if bug["status"]=="closed":
        Closed_bugs = Closed_bugs + 1
print(f"Closed_bugs: {Closed_bugs}")

# Drill 4 - Two filter HUnt

critical_open = []
low_priority_closed =[]

for bug in bugs:
    if bug["status"]=="open" and bug["severity"]>=4:
        critical_open.append(bug)
    elif bug["status"]=="closed" and bug["severity"]<=2:
        low_priority_closed.append(bug)

print(f"crittical open bugs: {critical_open}")
print(f"low priority closed bugs: {low_priority_closed}")

# Drill 5 - The sum calculator

severity = []
for bug in bugs:
    if bug["id"] is not None:
        severity.append(bug["severity"])
total_severity_points = sum(severity)
print(f"Total severity points: {total_severity_points}")

# Drill 6 - Status Counter dict
open_bugs =[]
closed_bugs=[]
for bug in bugs:
    if bug["status"]=="closed":
        closed_bugs.append(bug["id"])
    if bug["status"]=="open":
        open_bugs.append(bug["id"])
print(f"Open: {len(open_bugs)}, Closed: {len(closed_bugs)}")
