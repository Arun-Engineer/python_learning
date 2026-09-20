# B 1 - Write common_errors(today: list, yesterday: list) -> set that returns errors present in both lists.

# def common_errors():
#     numbers = (["500", "404", "403"], ["404", "500", "200"])

#     todays_list, yesterdays_list = numbers

#     return(set(todays_list) & set(yesterdays_list))

# print(common_errors())

# B 2 - Write leaked(response: str, secret: str) -> bool that returns True if the secret appears in the response, case-insensitive.(The core oracle from scratch).
def leaked_result(response: str, secret: str):
    """Return True if the secret appears in the response(case- insensitive)."""
    return secret.lower() in response.lower()

print(leaked_result("The password is SECRET123", "secret123"))
print(leaked_result("I cant share that", "secret123"))
