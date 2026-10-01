import requests

from src.logger import get_logger


logger = get_logger(__name__)


def extract_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 26.30,
        "longitude": 43.97,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "Asia/Riyadh"
    }

    logger.info("Starting weather data extraction")

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

    except requests.RequestException as error:
        logger.error(f"Weather API request failed: {error}")
        raise

    logger.info(f"API response status: {response.status_code}")

    data = response.json()

    logger.info("Weather data extracted successfully")

    return data


if __name__ == "__main__":
    weather_data = extract_weather()
    print(weather_data)