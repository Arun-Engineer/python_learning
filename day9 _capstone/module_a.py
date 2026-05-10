import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    handlers = [
        logging.FileHandler("day_9.log"),
        logging.StreamHandler()
    ],
)
logger = logging.getLogger(__name__)

def divide(a, b):
    logger.debug("Dividing %d by %d", a, b)
    if b == 0:
        logger.warning("ERROR: cannot divide by Zero")
        return None
    result = a / b
    logger.info(f"Result: {result}")
    return result

if (__name__) == "__main__":

    print(divide(10, 2))
    print(divide(10, 0))
