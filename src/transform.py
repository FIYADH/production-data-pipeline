from src.logger import get_logger


logger = get_logger(__name__)


def transform_weather(data):

    try:
        current = data["current"]

        transformed_data = {
            "time": current["time"],
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind_speed": current["wind_speed_10m"]
        }

        logger.info("Weather data transformation completed")

        return transformed_data

    except (KeyError, TypeError, ValueError) as error:
        logger.error(f"Weather data transformation failed: {error}")
        raise
    