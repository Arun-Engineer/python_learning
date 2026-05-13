import requests
import logging

# set Up logging like day 9
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Section 1: Your first GET request
# Free public API - JOSNPlaceholder is a fake API for learning

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

logger.info("Status: %d", response.status_code)
logger.info("Headers: %s", response.headers)
logger.info("Body type: %s", response.headers.get("content-type"))

# Parse the JSON
data = response.json()
logger.info("User name: %s", data["name"])
logger.info("User email: %s", data["email"])
logger.info("User company: %s", data["company"]["name"])

# Section 2: Error Handling
def fetch_user(user_id: int) -> dict | None:
    """Fetch a user by ID. Returns None on error."""

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url, timeout= 5)
        response.raise_for_status()
        return response.json
    except requests.HTTPError as e:
        logger.error("HTTP error fetching user %d: %s", user_id, e)
        return None
    except requests.Timeout:
        logger.error("Timeout fetching user %d, user_id")
        return None
    except requests.RequestException as e:
        # Catches all other requests-related errors (DNS, connection, etc.)
        logger.exception("Unexpected error fetching user %d", user_id)
        return None

# Test it
print(fetch_user(1))
print(fetch_user(9999))
print(fetch_user(0))

# Section 3: Your First POST Requests
def create_post(title: str, body: str, user_id: int) -> dict | None:
    """Send a POST to create a new post."""

    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": title,
        "body": body,
        "user_id": user_id,
    }

    try:
        response = requests.post(url, json=payload, timeout= 5)
        response.raise_for_status()
        return response.json
    except requests.RequestException:
        logger.exception("Failed to create POST")
        return None

result = create_post(
    title = "My first POST from Python",
    body = "This is the body of the POST",
    user_id = 1
)
logger.info("Created POST: %s", result)

# Section 4: Authenticated requests

# Pretend we have an API key
API_key = "fake-key-for-demo"

def fetch_with_auth(url: str) -> dict | None:
    """Make an authenticated GET request."""
    headers = {
        "Authorization": f"Bearer {API_key}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.get(url, headers= headers, timeout= 5)
        response.raise_for_status()
        return response.json
    except requests.RequestException:
        logger.exception("Auth request failed")
        return None