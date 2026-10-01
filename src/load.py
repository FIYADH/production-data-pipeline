import psycopg2

from src.logger import get_logger


logger = get_logger(__name__)


def load_weather(data):

    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            database="pipeline_db",
            user="pipeline_user",
            password="pipeline_password"
        )

        cursor = connection.cursor()

        query = """
            INSERT INTO weather_data
            (time, temperature, humidity, wind_speed)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                data["time"],
                data["temperature"],
                data["humidity"],
                data["wind_speed"]
            )
        )

        connection.commit()

        logger.info("Weather data loaded successfully")

    except (psycopg2.Error, KeyError, TypeError, ValueError) as error:

        if connection:
            connection.rollback()

        logger.error(f"Weather data loading failed: {error}")
        raise

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()