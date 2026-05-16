import asyncio
import time
from logger_config import setup_logger
from weather_api_sync import fetch_all_weather

CITIES = {
    "Mumbai": (19.07, 72.87),
    "Bangalore": (12.97, 77.59),
    "Delhi": (28.67, 77.21),
    "Chennai": (13.08, 80.27)
}

async def main():
    setup_logger("weather_async.log")
    print("=" * 50)
    print("Weather Report (Async)")
    print("=" * 50)

    start = time.time()
    reports = await fetch_all_weather(CITIES)
    elapsed = time.time() - start

    for report in reports:
        if report:
            print(f"{report.city:12} {report.temperature_c:5.1f} def C wind{report.wind_speed:.1f} km/h")
        else:
            print("(unavailable)")
        
    print("=" * 50)
    print(f"Fetched {len(reports)} cities in {elapsed:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())