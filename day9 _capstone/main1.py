from logger_config import setup_logger
from bug_tracker import BugTracker


if __name__ == "__main__":
    setup_logger("day9_bug_tracker.log")

    tracker = BugTracker("bug.json")

    added_bug = tracker.add_bug(
        "Search broken on Safari",
        4,
        "open",
        "web"
    )

    print("Added bug:")
    print(added_bug)

    print(tracker.report())
