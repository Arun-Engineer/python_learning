from logger_config import setup_logger
from weather_api import fetch_weather

CITIES = {
    "Mumbai": (19.07, 72.87),
    "Bangalore": (12.97, 77.59),
    "Delhi": (28.61, 77.21),
    "Chennai": (13.08, 80.27),
}

if __name__ == "__main__":
    setup_logger("weather.log")

    print("=" * 40)
    print("Weather Report")
    print("=" * 40)

    for city, (lat, lon) in CITIES.items():
        report = fetch_weather(lat, lon)
        if report:
            print(f"{city:12} {report.temperature_c:5.1f}deg C wind{report.wind_speed: .1f} km/h")
        else:
            print(f"{city:12} (unavailable)")
    
    print("=" * 40)