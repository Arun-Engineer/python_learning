import logging

# Section 1: Basic logger setup

# Confifure once at the top of your program

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    handlers = [
        logging.FileHandler("app.log"),
        logging.StreamHandler(),
    ],

)

# Get Logger (one per module is the convention)
logger = logging.getLogger(__name__)

# Section 2: The 5 Levels
logger.debug("This is a debug message - granular detail")
logger.info("This is an info message - normal flow")
logger.warning("This is an error - something failed")
logger.critical("This is critical - program may crash")

# Section 3: Logging Variables

bug_count = 25
logger.info(f"Loaded {bug_count} bugs from disk")

# or the more idiomatic way(pass values as args, let logger format)
logger.info("Loaded %d bugs from disk", bug_count)

# Section 4: Logging in real flow

def add_bug(title, severity):
    logger.debug(f"add_bug called with title ={title!r}, severity={severity}")

    if severity > 5:
        logger.warning(f"Severity {severity} exceeds max(5) - capping")

    logger.info(f"Adding bug: {title} (severity = {severity})") 
    return {"title": title, "severity": severity}

add_bug("Login broken", 5)
add_bug("Critcal issue", 10)

# section 5: Logging exceptions properly
try:
    result = 10/0
except ZeroDivisionError as e:
    # loggger.exception() captures the full traceback automatically
    logger.exception("Division failed - full traceback below:")
    # Program continues
    result = 0

logger.info(f"Result: {result}")