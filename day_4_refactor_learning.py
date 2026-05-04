# step 1:
# list_a = [1, 2, 3]
# list_b = list_a
# list_c = list_a + [4]

# list_b.append(99)
# print("list_a: ", list_a)
# print("list_b:", list_b)
# print("list_c:", list_c)

# Step 2:
list_a = [1, 2, 3]
list_b = list_a.copy()

list_b.append(99)
print("list_a: ", list_a)
print("list_b:", list_b)

# step 3: 
list_a = [1, 2, 3]
list_b = list_a
list_b = list_b + [99]

print("list_a: ", list_a)
print("list_b:", list_b)