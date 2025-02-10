
from config import API_KEY
import json
import requests
import pytest

class TestWeatherApiData:
    """
    A class to test weather data fetched from the OpenWeather API.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Set up API parameters before each test case.
        """
        self.lat = 20.800301
        self.lon = 76.690903
    
    def open_json(self):
        """
        Load saved JSON file for comparison.
        
        :return: Parsed JSON data from file
        """
        with open('current_weather_data.json', 'r') as file:
            return json.load(file) 

    def test_response_properly(self):
        """
        Verify that the API responses return a 200 status code.
        """
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={API_KEY}")
        response2 = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={API_KEY}")

        assert response.status_code == 200, f"Weather API failed! Status Code: {response.status_code}"
        assert response2.status_code == 200, f"Forecast API failed! Status Code: {response2.status_code}"

    def test_data_null_or_empty(self):
        """
        Check if any field in the JSON is null or empty.
        """
        data = self.open_json()
        assert self.check_null_or_empty(data) == False

    def check_null_or_empty(self, json_data):
        """
        Recursively check if any value in JSON is null or empty.
        
        :param json_data: JSON object to check
        :return: True if any field is null or empty, otherwise False
        """
        if isinstance(json_data, dict):
            for key, value in json_data.items(): 
                if self.check_null_or_empty(value): 
                    return True  
            return False  

        elif isinstance(json_data, list):
            for item in json_data:  
                if self.check_null_or_empty(item): 
                    return True  
            return False 

        return json_data is None or json_data == ""
