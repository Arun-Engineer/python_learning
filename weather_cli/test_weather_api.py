from weather_api import fetch_weather

def test_fetch_weather_returns_report():
    """Real API call should return a Weather Report for valid coords."""
    report = fetch_weather(19.07, 72.87)
    assert report is not None
    assert isinstance(report.temperature_c, float)
    assert -50 < report.temperature_c < 60  

def test_fetch_weather_invalid_coords_returns_none():
    """Invalid coordinates should return None gracefully."""
    report = fetch_weather(999, 999)
    assert report is None