import logging
from module_a import divide
from module_b import process_items

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

print(divide(10, 2))
print(divide(10, 0))
print(process_items(["a", "b", "c"]))
