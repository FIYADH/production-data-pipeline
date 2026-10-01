from src.extract import extract_weather
from src.validate import validate_weather
from src.transform import transform_weather
from src.load import load_weather


data = extract_weather()

validate_weather(data)

transformed_data = transform_weather(data)

load_weather(transformed_data)

print("Pipeline completed successfully")