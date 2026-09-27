# # Part b - 1
# # write has_duplicate(nums: list) -> bool - return True if any number appears twice.

# def has_duplicate(num: list) -> bool:
#     count = {}

#     for i in num:
#         count[i] = count.get(i ,0) + 1

#         if count[i]> 1:
#             return True
#     return False

# num1 = [1, 2, 3, 2]
# print(has_duplicate(num1))
# num2 = [1, 2, 3]
# print(has_duplicate(num2))

# def has_duplicates(num: list) -> bool:
#     seen = set()

#     for i in num:
#         if i not in seen:
#             seen.add(i)
#         else:
#             return True
#     return False

# num1 = [1, 2, 3, 2]
# print(has_duplicates(num1))
# num2 = [1, 2, 3]
# print(has_duplicates(num2))

# B2 - Write count_above(nums: list, threshold: int) -> int - how many numbers are above the threshold?

def count_above(nums: list, threshold: int) -> int:
    numbers = []

    for i in nums:
        if i > threshold:
            numbers.append(i)
    return len(numbers)

nums = [5, 10, 3, 8]
print(count_above(nums, 6))