# section 1: your first error
bug = {"id": 1, "severity": 5}
#print(bug["status"])

# section 2: Try/except basics
try:
    print(bug["status"])
except KeyError:
    print("No status field - using default 'unknown'")

# section3: specifi errors
def safe_get_severity(bug):
    """Return severity, or -1 if missing."""
    try:
        return bug["severity"]
    except KeyError:
        return -1

print(safe_get_severity({"id": 1, "severity": 5}))
print(safe_get_severity({"id": 2}))

def safe_parse_severity(value):
    """Try to convert value to int. Return None if it fails."""

    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a number")
        return None
    except TypeError:
        print(f"Got a {type(value).__name__}, expected something parseable")
        return None

print(safe_parse_severity("5"))
print(safe_parse_severity("high"))
print(safe_parse_severity(None))

# section 5: reading a text file
# First, write a file so we have something to read
with open("greeting.txt", "w")as f:
    f.write("Hello form Day 4\nThis is line 2\n")
    
# Now read the file
with open("greeting.txt", "r")as f:    
    content = f.read()
    print("File contents:")
    print(content)

# section 6: Json write and read

import json

bugs = [
    {"id":1, "title": "Login crash on IOS", "severity": 5, "status": "open", "team": "mobile"},
    {"id":2, "title": "Typo on homepage", "severity": 1, "status": "open", "team": "web"},
]
with open("bugs.json", "w")as f:
    json.dump(bugs, f, indent=2)
print("wrote bugs.json")

# Read Back
with open("bugs.json", "r")as f:
    loaded_content = json.load(f)

print(f"Loaded {len(loaded_content)} bugs from file") 
print(loaded_content[0])

# section 7: File error handling

def load_bugs(filename):
    """Load bugs from a JSON file. Return [] if file missing or invalid."""
    try:
        with open(filename, "r")as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"No file '{filename}' yet - starting fresh")
        return[]
    except json.JSONDecodeError:
        print(f"file '{filename}' is corrupted - starting fresh")
        return []
    
print(load_bugs("bugs.json"))
print(load_bugs("missing.json"))