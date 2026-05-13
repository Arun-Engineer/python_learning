import requests
import logging
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)

@dataclass
class WeatherReport:
    lattitude: float
    longitude: float
    temperature_c: float
    wind_speed: float

def fetch_weather(lattitude: float, longitude: float) -> Optional[WeatherReport]:
    """Fetch current weather for given coordinates. Returns None on any error."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lattitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        current = data["current"]
        report = WeatherReport(
            lattitude= lattitude,
            longitude= longitude,
            temperature_c= current["temperature_2m"],
            wind_speed= current["wind_speed_10m"],
        )
        logger.info("Fetched weather for (%.2f, %.2f): %.1fdeg cel", lattitude, longitude, report.temperature_c)
        return report
    
    except requests.HTTPError as e:
        logger.error("HTTP error: %s", e)
        return None

    except requests.Timeout:
        logger.error("Timeout fetching weather")
        return None
    
    except requests.RequestException:
        logger.exception("Unexpected error fetching weather")
        return None
    
    except (KeyError, ValueError):
        logger.exception("Unexpected response format")
        return None