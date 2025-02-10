
import json
from main import WeatherApi

class SaveData:
    """
    A class to save weather data into JSON files.
    """

    def save_current_weather_data(self, data):
        """
        Save current weather data to a JSON file.
        
        :param data: Dictionary containing current weather data
        """
        with open('current_weather_data.json', 'w') as f:
            json.dump(data, f, indent=4)

    def save_four_days_data(self, data):
        """
        Save four-day forecast data to a JSON file.
        
        :param data: Dictionary containing four-day weather forecast data
        """
        with open('historical_weather_data.json', 'w') as f:
            json.dump(data, f, indent=4)
