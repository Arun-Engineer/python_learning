import logging

# Log Config
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S",
    handlers = [
        logging.FileHandler("drills_day9.log"),
        logging.StreamHandler(),
    ],

)

# Drill 2: Convert print to log
# def divide(a, b):
#     print(f"Dividing {a} by {b}")
#     if b == 0:
#         print("ERROR: cannot divide by zero")
#         return None
#     result = a / b
#     print(f"Result: {result}")
#     return result

# converting print to log level
def divide(a, b):
    logging.debug("Dividing %d by %d", a, b)
    if b == 0:
        logging.error("ERROR: cannot divide by Zero")
        return None
    result = a / b
    logging.info(f"Result: {result}")
    return result

print(divide(10, 2))
print(divide(10, 0))

# Drill 3: Logging in try/except
def safe_int(value):
    try:
        logging.debug("Converting value = %s to integer", value)
        dig = int(value)
        logging.info("value = %d is safely converted to integer %r", value, dig)
        return dig
    except (ValueError, TypeError)as e:
        logging.exception("Value %r cannot be converted to integer", value)
        return "cannot be converted"
    
print(safe_int("42"))
print(safe_int("hello"))
print(safe_int(None))
print(safe_int(-5))

# Drill 4: Loggging in a loop
def process_items(items):
    count = 0

    logging.info("Starting item processing")

    for item in items:
        logging.debug("Processing item: %s", item)
        count += 1
        logging.info("Current count: %d", count)

    logging.info("Finished processing. Total items: %d", count)

    return count


print(process_items(["a", "b", "c"]))

# Drill 5: Module-level loggers
