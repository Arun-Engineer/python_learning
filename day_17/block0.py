# def find_middle_index(numbers):

#     slow = 0
#     fast = 0

#     while fast +1 < len(numbers):
#         slow += 1
#         fast += 2

#     return slow

# print(find_middle_index([15,10,15,20,25])) 

def most_common(items: list) -> str:
    count = {}

    for item in items:
        count[item] = count.get(item, 0) + 1

    best_item = None
    best_count = 0

    for item, count in count.items():

        if count > best_count:
            best_item = item
            best_count = count

    return best_item 

print(most_common(["500", "200", "500", "300", "200", "500"]))  
