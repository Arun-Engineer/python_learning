import json
from dataclasses import asdict
from models import Bug


def load_bugs(filename: str, fallback: list[dict]) -> list[dict]:
    """Load bugs from JSON. On error, return fallback."""
    try:
        with open(filename, "r") as f:
            loaded_bugs = json.load(f)

        return [Bug(**d) for d in loaded_bugs]

    except FileNotFoundError:
        print(f"No '{filename}' - starting fresh")
        return fallback.copy()

    except json.JSONDecodeError:
        print(f"File '{filename}' is corrupted - resetting fresh")
        return fallback.copy()

def save_bugs(bugs: list[Bug], filename: str) -> None:
    """Save bugs to JSON file."""
    loaded_bugs =[asdict(bug) for bug in bugs]
    with open(filename, "w") as f:
        json.dump(loaded_bugs, f, indent=2)

    print("Bugs saved successfully")