# # drill 1- Public weather API
# # use this free API: - https://api.open-meteo.com/v1/forecast

import requests
import json
import logging
import random

# set Up logging like day 9
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# def get_temperature(latitude: float, longitude: float) -> float | None:
#     """Return current temperature in celcius for the given coords."""

#     url = f"https://api.open-meteo.com/v1/forecast"
#     params = {"latitude":latitude,
#          "longitude":longitude,
#          "current":"temperature_2m"}
        
    
#     try:
#         response = requests.get(url, params=params, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#         logger.info("temperature_2m: %r", data["current"]["temperature_2m"])
#         return data
        
#     except requests.RequestException:
#         logger.exception("Failed to get response")
#         return None

# print(get_temperature(19.07, 72.87))
# print(get_temperature(999, 999))

# # Drill 2: - User-list API
# # use https://jsonplaceholder.typicode.com/users

# def get_user_emails() -> list[str]:
#     """Fetch all users and return list of their emails."""

#     url = "https://jsonplaceholder.typicode.com/users"
#     try:
#         response = requests.get(url, timeout=5)
#         response.raise_for_status
#         data = response.json()

#         # parse
#         email = []
#         for item in data:
#             logger.info("Username: %s" ,item["username"])
#             email.append(item["email"])
#         return email
#     except requests.RequestException:
#         logger.error("Not able to fetch the data")
#         return []
# print(get_user_emails())

# # Drill 3: POST a fake todo
# #use https://jsonplaceholder.typicode.com/todos.

# def create_todo(title: str, completed: bool = False) -> dict | None:
#     """POST a new todo, return the created object (with assigned id)."""
#     url = "https://jsonplaceholder.typicode.com/todos"
#     payload = {
#         "title": title,
#         "completed": completed,
#         "user_id": 1
#     }
#     try:
#         response = requests.post(url, json = payload, timeout=5)
#         response.raise_for_status()
#         return response.json()

#     except requests.RequestException:
#         logger.exception("Failed to get POST")
#         return None

# print(create_todo("Finish Day 10", False))

# Drill 4: Status code branching
def safe_fetch(url: str) -> dict | None:
    #url= "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=5)
        logger.info("Status code: %d for %s", response.status_code, url)
    except requests.HTTPError:
        logger.warning("URL not found")
        return None
    except requests.ConnectionError:
        logger.error("Unauthorised error")
        return None
    except requests.Timeout:
        logger.error("Time out error")

print(safe_fetch("https://jsonplaceholder.typicode.com/users/9999"))
print(safe_fetch("https://httpbin.org/status/500"))
print(safe_fetch("https://this-does-not-exist-asdfgh.com"))

# #Drill 5: Retry on 429/503
# import time
# def fetch_with_retry(url: str, max_retries: int=3) -> dict | None:
#     for attempt in range(max_retries +1):
#         try:
#             response = requests.get(url, timeout=5)
#         except requests.RequestException as e:
#             if attempt < max_retries:
#                 wait = 2 ** attempt+random.uniform(0, 1)
#                 logger.warning(
#                     "Atempt %d/%d failed with %s - retrying in %d seconds",
#                     attempt + 1, max_retries + 1, type(e).__name__, wait
#                 )
#                 time.sleep(wait)
#                 continue
#             else:
#                 logger.exception("All retries failed for %s, url")
#         logger.info("Status code: %d", response.status_code)
#         if response.status_code == 200:
#             return response.json()
#         if response.status_code in (429, 503):
#             if attempt < max_retries:
#                 wait = 2 ** attempt+random.uniform(0, 1)
#                 logger.warning(
#                     "Atempt %d/%d failed with %s - retrying in %d seconds",
#                     attempt + 1, max_retries + 1, response.status_code, wait
#                 )
#                 time.sleep(wait)
#                 continue
#             else:
#                 logger.warning(
#                     "Final attempt %d/%d got status %d",
#                     attempt + 1, max_retries + 1, response.status_code
#                 )
#                 break

#         logger.error("status %d for %s - not retrying", response.status_code, url)
#         return None
#     logger.error("Exhausted %d retries for %s", max_retries, url)
#     return None

# import time
# print("Wait sequence:")
# for a in range(4):
#     print(f"attempt= {a} --> wait {2**a}s")
# print("\n---- Test: Always-503 URL ----")
# start = time.time()
# result = fetch_with_retry("https://httpbin.org/status/503", max_retries = 3)