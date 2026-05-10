import logging
from models import Bug
import json
from dataclasses import asdict

logger = logging.getLogger(__name__)

def load_bugs(filename: str, fallback: list[Bug]):
    logger.debug(f"loading bugs from {filename}")
    try:
        with open(filename, "r")as f:
            raw = json.load(f)
            loaded = [Bug(**d) for d in raw]
            logger.info(f"Loaded {len(loaded)} bugs from {filename}")
            return loaded
    except FileNotFoundError:
        logger.warning(f"{filename} not found - using fallback")
        return fallback.copy()
    except json.JSONDecodeError:
        logger.error(f"{filename} is corrupted - using fallback")
        return fallback.copy()
    
def save_bugs(bugs: list[Bug], filename: str) -> None:
    logger.debug(f"Saving {len(bugs)} bugs to {filename}")
    raw = [asdict(bug) for bug in bugs]
    with open(filename, "w")as f:
        json.dump(raw, f ,indent = 2)
        logger.info(f"Saved {len(bugs)} bugs to {filename}")
