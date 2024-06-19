import requests
import time

class WeatherService:
    def __init__(self):
        self.cache = {}
        self.cache_duration = 600  # cache duration in seconds

    # write a function to get weather which takes a city as a parameter
    def weatherGet(city):
    
        
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4523628bd365a0c61f43c9ba0c9cd1ff&units=imperial')
    # Fetch new data making an API call
        response.raise_for_status
        data = response.json
        weather_data ={
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity']
        }
    # write a function which Updates a cache
