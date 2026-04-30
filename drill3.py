# Build a bug dict
# Create a dictionary representing one bug with at least 5 fields(id, title, severity, status, reporter). Then
# Print each field on its own line with a label
# Add a new field priorty
# Change the status to closed
# Print the final dict

bug_dict = {
    "Bug_id": 1,
    "Title": "Cart API Issue",
    "Severity": "Critical",
    "Status": "Open",
    "Reporter": "Arun"
}

print(bug_dict)
bug_dict["Priority"] = 1
print(bug_dict)
bug_dict["Status"] = "Closed"
print(bug_dict)