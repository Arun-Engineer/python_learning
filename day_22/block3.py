# Drill 1 - Given a sorted list of user IDs, check if user 4071 exists.

# def check_user(users: list, target: int) -> int:
#     low = 0
#     high = len(users)-1

#     while low <= high:

#         mid = (low + high) // 2
#         if users[mid] == target:
#             return f"User -> {target} exists at position {mid} in the list"
#         elif users[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return f"No such user -> {target} exists"

# users = [4065, 4066, 4067, 4068, 4069, 4070, 4071, 4072, 4073, 4074, 4075]
# print(check_user(users, 4071))

# Drill 2  - Given a list of test-case durations, return the 3 longest.

# def return_logest_duration(durations: list[float], longest: int) -> list[float]:
#     durations.sort(reverse= True)
#     return durations[:longest]

# durations = [2.5, 7.0, 1.2, 9.5, 4.0]
# print(return_logest_duration(durations, 3))

# Drill 3 - Given two  list of tag names,find the tags that are in the first but Not the second.

# def list_tags(tag1: list, tag2: list):

#     return set(tag1) - set(tag2) 

# tag1 = ["str1", "str2", "str4", "str3"]
# tag2 = ["str4", "str5", "str2", "str7"]
# print(list_tags(tag1, tag2))

# Drill4 - given a list of API response codes count how many were 500 errors:

# def count_common_errors(errors: list, target_error: int) -> int:

#     count = 0

#     for error in errors:
#         if error == target_error:
#             count += 1
#     return f" No of {target_error} errors in list of API response code is -> {count}"

# errors =["500", "400", "404", "500"]
# print(count_common_errors(errors, "500"))

# Drill 5: Given a list aof transaction amounts, is there any pair that adds up to exactly 1000?

def amount_pairs(amounts: list, target: int) -> list:
    seen = set()

    for amount in amounts:
        needed = target - amount

        if needed in seen:
            return [needed, amount]
        seen.add(amount)

    return []

amounts = [200, 300, 700, 400]

print(amount_pairs(amounts, 1000))
