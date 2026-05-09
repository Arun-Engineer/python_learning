from bug_tracker import BugTracker

if __name__ == "__main__":
    tracker = BugTracker("bug.json")

    added_bug_1 = tracker.add_bug("Login crash on Android", 3, "open", "mobile")
    added_bug_2 = tracker.add_bug("Search broken on Safari", 4, "open", "web")
    added_bug_3 = tracker.add_bug("Cart drops items", 5, "open", "backend")

    print("Added bugs:")
    print(added_bug_1)
    print(added_bug_2)
    print(added_bug_3)

    tracker.report()