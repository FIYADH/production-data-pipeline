from src.logger import get_logger


logger = get_logger(__name__)


def validate_weather(data):

    try:
        if "current" not in data:
            raise ValueError("Missing current weather data")

        current = data["current"]

        required_fields = [
            "time",
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m"
        ]

        for field in required_fields:
            if field not in current:
                raise ValueError(f"Missing field: {field}")

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]

        if not isinstance(temperature, (int, float)):
            raise ValueError("Invalid temperature")

        if not isinstance(humidity, (int, float)):
            raise ValueError("Invalid humidity")

        if not isinstance(wind_speed, (int, float)):
            raise ValueError("Invalid wind speed")

        if not 0 <= humidity <= 100:
            raise ValueError("Humidity must be between 0 and 100")

        if wind_speed < 0:
            raise ValueError("Wind speed cannot be negative")

        logger.info("Weather data validation passed")

        return True

    except (KeyError, TypeError, ValueError) as error:
        logger.error(f"Weather data validation failed: {error}")
        raise