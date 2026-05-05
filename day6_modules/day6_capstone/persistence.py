import json

def load_bugs(filename, fallback):
    """Load bugs from JSON. On error, return fallback."""
    try:
        with open(filename, "r") as f:
            loaded_bugs = json.load(f)

        return loaded_bugs

    except FileNotFoundError:
        print(f"No '{filename}' - starting fresh")
        return fallback.copy()

    except json.JSONDecodeError:
        print(f"File '{filename}' is corrupted - resetting fresh")
        return fallback.copy()

def save_bugs(bugs, filename):
    """Save bugs to JSON file."""
    with open(filename, "w") as f:
        json.dump(bugs, f, indent=2)

    print("Bugs saved successfully")