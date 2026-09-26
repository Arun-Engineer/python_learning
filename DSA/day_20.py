def two_sum(nums: list, target: int) -> list:
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i
    return None
num = [2,5,7,3]
target = 9
print(two_sum(num, target))