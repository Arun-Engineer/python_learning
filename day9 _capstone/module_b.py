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

def process_items(items):
    count = 0

    logger.info("Starting item processing")

    for item in items:
        logger.debug("Processing item: %s", item)
        count += 1
        logger.info("Current count: %d", count)

    logger.info("Finished processing. Total items: %d", count)

    return count


#print(process_items(["a", "b", "c"]))