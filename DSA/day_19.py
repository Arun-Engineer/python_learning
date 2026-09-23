# def remove_duplicates(num: list) -> int:
#     if not num:
#         return 0

#     slow = 0
#     for fast in range(1, len(num)):
#         if num[fast]!= num[slow]:
#             slow += 1
#             num[slow] = num[fast]

#     return slow +1

# print(remove_duplicates([1,1,2,2,3,3]))

def find_largest_number(num: list) -> int:
    largest = num[0]

    for i in num:
        if i > largest:
            largest = i
    return largest

print(find_largest_number([10,50,35,15]))