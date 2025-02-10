import requests

class WeatherApi:
    """
    A class to interact with the OpenWeather API and retrieve weather data.
    """
    
    def __init__(self, api_key, lat, lon):
        """
        Initialize the WeatherApi class with API key, latitude, and longitude.
        
        :param api_key: API key for OpenWeather API
        :param lat: Latitude of the location
        :param lon: Longitude of the location
        """
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
    
    def current_location(self):
        """
        Fetch current weather data for the given latitude and longitude.
        
        :return: JSON response containing current weather data
        """
        base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}"
        response = requests.get(base_url)
        data = response.json()
        return data 
    
    def four_days_data(self):
        """
        Fetch 4-day weather forecast for the given latitude and longitude.
        
        :return: JSON response containing weather forecast data
        """
        base_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={self.api_key}"
        response = requests.get(base_url)
        data = response.json()
        return data 
    
# Example usage:
obj = WeatherApi("432a3c83625b7c10c0030ecd572f3179", 20.800301, 76.690903)
