def find_middle(items: list) -> object:
    slow = 0
    fast = 0

    while fast + 1 < len(items):
        slow += 1
        fast += 2
    
    return slow

if __name__ == "__main__":
    print(find_middle([10, 20, 30, 40, 50, 60, 70]))
    print(find_middle([10, 20, 30, 40]))
