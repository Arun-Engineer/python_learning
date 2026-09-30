# Given a list of test results, return them sorted by duration, slower first

def slowest_first(results: list[dict]) -> list[dict]:

    return sorted(results, key = lambda r : r["duration"], reverse= True)

if __name__ == "__main__":
    results = [
        {"name": "test_login", "duration": 2.5},
        {"name": "test_search", "duration": 9.1},
        {"name": "test_logout", "duration": 0.8},
    ]
    for r in slowest_first(results):
        print(r)
