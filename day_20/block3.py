# # Drill 1 -> write count_failures(results: list) -> int - count how many results equal "fail".
# def count_failures(results: list) -> int:
#     """Counts how many fails in the given list."""
#     fail_count = 0

#     for result in results:
#         result_value = result.lower()
#         if result_value == "fail":
#             fail_count += 1
#     return fail_count

# results = ["pass", "Fail", "PASS", "FAIL", "FAiL"]
# print(count_failures(results))

# # Drill 2 -> write highest_score(scores: list) -> int - return the biggest score.

# def highest_score(scores: list) -> int:
#     return max(scores)

# scores = [72, 68, 88, 65, 91, 80]
# print(highest_score(scores))

# def highest_scores(scores: list) -> int:

#     high_score = scores[0]

#     for score in scores:
#         if score > high_score:
#             high_score = score
#     return high_score

# highest = [72, 68, 88, 65, 91, 80]
# print(highest_score(highest))

# # Drill 3 -> write is_relevant(doc: str, relevant_list: list) -> bool -is doc in relevant list?

# def is_relevant(doc: str, relevant_list: list) -> bool:
#     """Finding whether the fetched doc is available in the relevant list."""

#     docs = doc.lower()

#     relevant_lists = [item.lower() for item in relevant_list]

#     return docs in relevant_lists

# print(is_relevant("DOC2", ["doc1", "doc2", "doc3"]))

# # Drill 4 -> write all_passed(results: list) -> bool - True only if Every results is "pass".

# def all_passed(results: list) -> bool:
#     """Checks wether all results are pass. If pass returns true even if one fail it returns false."""

#     for pass_case in results:
#         if pass_case.lower() != "pass":
#             return False
#     return True

# case1 = ["pass", "PaSS", "PASS"]
# case2 = ["Pass", "Fail","pass"]
# print(all_passed(case1))
# print(all_passed(case2))

# Drill 5 -> Write has_pair_summing(nums: list, target: int) -> bool - return True if ANY two numbers add to target(just True/False, not positions).

def has_pair_summing(nums: list, target: int) -> bool:

    needed = target - nums[0]

    for i in nums:
        if needed + i != target:
            needed = i
    return needed + i == target

nums1 = [1, 5, 3]
nums2 = [1, 2, 4]
print(has_pair_summing(nums1, 8))
print(has_pair_summing(nums2, 10))