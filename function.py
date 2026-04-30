# Write a function called add(a,b) that returns the sum of two numbers
def add(a , b):
     ad = a + b
     return ad

print(add(5,3))

# Modify the function above to also accept a model_name parameter with default "gpt-4" and return a dict like:
# {"model": gpt-4, "tokens": 1500, "cost": 0.045}
def calculate_token_cost(tokens, price_per_1k=0.045, model_name="gpt-4"):
    cost = (tokens / 1000) * price_per_1k
    return {"model": model_name, "tokens": tokens, "cost": round(cost,4)}

print(calculate_token_cost(1500))

# write a function find_cheapest(products) that takes a list of product dicts(each with "name" and "price") and returns the name of the cheapest one.
def cheapest_product(products):
     cheapest = min(products, key = lambda x : x ['price'])['name']
     return cheapest

products = [
    {"name": "Atta", "price": 10.99},
    {"name": "Basket", "price": 9.99},
    {"name": "Cooking_oil", "price": 12.99}
]

print(cheapest_product(products))

# write a code that tries to access user("age") on a dict without an "age" key . Catch the KeyError and print "Age not found" instead of crashing.
def get_age(user):
     try:
          age = user["age"]
          return age
     except KeyError:
          return "Age not found"

user_info = {"name": "Alice", "city": "New York"}
print(get_age(user_info))