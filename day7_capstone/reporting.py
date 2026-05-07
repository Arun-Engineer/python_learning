from models import Bug
from typing import Optional

def get_critical_bugs(bugs: list[Bug]) -> list[Bug]:
    critical_bugs: list[Bug] = []

    for bug in bugs:
        if bug["status"] == "open" and bug["severity"] >= 4:
            critical_bugs.append(bug)

    return critical_bugs

def get_bug_counts_by_status(bugs: list[Bug]) -> dict[str, int]:
    bug_count_status: dict[str, int] = {}

    for bug in bugs:
        bug_status = bug.get("status")

        if bug_status is not None:
            bug_count_status[bug_status] = bug_count_status.get(bug_status, 0) + 1

    return bug_count_status

def count_open_bugs_by_team(bugs: list[Bug]) -> dict[str, int]:
    open_bug_count: dict[str, int] = {}

    for bug in bugs:
        if bug["status"] == "open":
            team = bug["team"]
            open_bug_count[team] = open_bug_count.get(team, 0) + 1

    return open_bug_count

def format_report(bugs: list[Bug]) -> Optional[dict]:
    print()
    print("=" * 10, "BUG REPORT", "=" * 10)
    print()

    bug_count = get_bug_counts_by_status(bugs)

    open_bugs = bug_count.get("open", 0)
    closed_bugs = bug_count.get("closed", 0)
    total_bugs = open_bugs + closed_bugs

    print(f"Total_bugs: {total_bugs}")
    print(f"Open_bugs: {open_bugs}")
    print(f"Closed_bugs: {closed_bugs}")

    print()
    print("CRITICAL BUGS NEEDING ATTENTION (open + severity >= 4)")

    critical_bugs = get_critical_bugs(bugs)

    if len(critical_bugs) == 0:
        print("No critical bugs found")
    else:
        for critical_bug in critical_bugs:
            print(
                f"- Bug id: {critical_bug['id']} "
                f"Title: {critical_bug['title']} "
                f"Severity: {critical_bug['severity']} "
                f"Team: {critical_bug['team']}"
            )

    print()
    print("Bugs by team (open only):")

    open_bugs_team = count_open_bugs_by_team(bugs)

    if len(open_bugs_team) == 0:
        print("No open bugs found")
    else:
        for team, count in open_bugs_team.items():
            print(f"- {team}: {count}")

    print()
    print("=" * 10, "END OF REPORT", "=" * 10)