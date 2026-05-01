# section 1: Basic for loop
severities = [3,5,1,4,2]
# print('walking through each bug severity')
# for severity in severities:
#     print(f"Severities: {severity}")

# Section 2: Loop  + if
print("\n Finding critical bugs:")
for severity in severities:
    if severity >=4:
        print(f"Critical: Severity {severity}")
    else:
        print(f"Normal: Severity {severity}")

# Section 3: counting with the loop
critical_bug_count=[]
for severity in severities:
    if severity >=4:
        critical_bug_count.append(severity)
print(f"\n Total critical bugs: {len(critical_bug_count)}")

# Section 4: Looping over dicts
bug_dict = {
    "Bug_id": 1,
    "Title": "Cart API Issue",
    "Severity": "Critical",
    "Status": "Open",
}
print("\nAll fields of this bug: ")
for key, value in bug_dict.items():
    print(f"{key} : {value}")