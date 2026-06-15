# B1 - Hash map counting(Day 13 muscle)
from collections import Counter
error = ["500", "404", "500", "500", "404"]

def most_common_error(error):
    """Finding the common error with higher repetition."""
    error_counts = Counter(error)
    most_common_error = error_counts.most_common(1)
    return most_common_error[0][0]

print(most_common_error(error))


# B2 Safe template fil(today + the 8 word rule)

PROMPT_TEMPLATE = {
    "name" : "Greet using this name:{name}"
}

def safe_fill(template: str, values: dict) ->str:
    try:
        return template.format(**values)
    except KeyError as e:
        return f"Key value is missing{"name": name}"
