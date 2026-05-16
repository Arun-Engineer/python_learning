import httpx
import logging
import asyncio
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)

@dataclass
class WeatherReport:
    city: str
    latitude: float
    longitude: float
    temperature_c: float
    wind_speed: float

async def fetch_weather_async(
        client: httpx.AsyncClient,
        city: str,
        latitude: float,
        longitude: float,
) -> Optional[WeatherReport]:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    }

    try:
        response = await client.get(url, params=params, timeout= 5)
        response.raise_for_status()
        data = response.json()
        current = data["current"]
        report = WeatherReport(
            city =city,
            latitude = latitude,
            longitude = longitude,
            temperature_c = current["temperature_2m"],
            wind_speed = current["wind_speed_10m"],
        )

        logger.info("Fetched %s: %.1f deg C", city, report.temperature_c)
        return report
    except httpx.HTTPStatusError:
        logger.exception("HTTP error for %s", city)
        return None
    except httpx.RequestError:
        logger.exception("Request error for %s", city)
        return None
    
async def fetch_all_weather(cities: dict) -> list:
    async with httpx.AsyncClient() as client:
        tasks = [
            fetch_weather_async(client, city, lat, lon)
            for city, (lat, lon) in  cities.items()
        ]
        return await asyncio.gather(*tasks)