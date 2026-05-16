import logging

def setup_logger(log_file: str = "tracker.log", level: int = logging.DEBUG):
    """Configure root logger. Call once at program start."""
    logging.basicConfig(
        level = level,
        format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
        handlers = [
            logging.FileHandler(log_file),
            logging.StreamHandler(),
        ],
    )