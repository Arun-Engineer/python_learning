def find_middle_index(num):
    """Finds the middle index of a list."""
    slow = 0
    fast = 0

    while fast +1 <len(num):
        slow += 1
        fast += 2
    return num[slow]

print(find_middle_index([10,20,30,40,50,60]))  