# Drill 1 - safe dict access
import json

def safe_get(d, key, default):
    try:
        for keys, value in d.items():
            if keys == key:
                return f"{keys}: {value}"
    except KeyError:
        print("The given {key}key is found to be missing")
        return default
    
print(safe_get({'id': 1, 'title': 'Login crash on IOS', 'severity': 5, 'status': 'open', 'team': 'mobile'}, "team", -1))
print(safe_get({'id': 1, 'title': 'Login crash on IOS', 'severity': 5, 'status': 'open'}, "team", -1))

# Drill 2 - safe int conversion

def to_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"This is a {type(value)} error, so we have change it to required int type value")
        return[]
    except TypeError:
        print("This a Type error")
        return[]
print(to_int("5"))
print(to_int("abc"))
print(to_int(None))
print(to_int(5))

# Dril 4: write and read a text file
def save_message(filename, message):
    with open(filename, "w")as f:
        f.write(message)
    return f"Message written and file saved as {filename}"

def load_message(filename):
    try:
        with open(filename, "r")as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
   

print(save_message("notes.txt", "I am learning Python deeply"))
print(load_message("notes.txt"))

# Drill 5: JSON round trip
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

def save_bugs(bugs, filename):
    with open(filename , "w")as f:
        json.dump(bugs, f, indent=2)
    print("File has been written successfully")

def load_bugs(filename):
    try:
        with open(filename, "r")as f:
            loaded_bugs = json.load(f)
        print("checking wheteher loaded_bugs and original_bugs are same........")
        assert bugs == loaded_bugs
        return loaded_bugs
    except FileNotFoundError:
        print("File not found")
    return None

print(save_bugs(bugs, "bug.json"))
print(load_bugs("bug.json"))
      
# Drill 6 - Robust JSON loader
def load_bugs_safe(filename):
    try:
        with open(filename, "r")as f:
            load_bugs = json.load(f)
        return load_bugs
    except FileNotFoundError:
        print(f"No file '{filename}' yet - starting fresh")
        return[]
    except json.JSONDecodeError:
        print(f"file '{filename}' is corrupted - starting fresh")
        return[]
    
print(load_bugs_safe("bug.json"))
print(load_bugs_safe("notes.txt"))
print(load_bugs_safe("bugs1.json"))

# Drill 7: Defensive predicate

def is_critical_bug(bugs1):
    try:
        return bugs1["status"] == "open" and bugs1["severity"] >= 4
    except KeyError:
        print("Bug['Status'] key is missing")
        return None
    except TypeError:
        print(f"{type(bugs1['severity'])} value error. expected vlaue int type.")

print(is_critical_bug({"id":1, "title": "Login crash on IOS", "severity": 5, "status": "open", "team": "mobile"}))
print(is_critical_bug({"id":2, "title": "Typo on homepage", "severity": 1, "team": "web"}))
print(is_critical_bug({"id":3, "title": "Payment timeout", "severity": "high", "status": "open", "team": "backend"}))