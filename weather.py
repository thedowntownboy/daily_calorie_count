import requests
import os

api_key = os.environ.get('SECRET_KEY')


class WeatherLocation:
    def __init__(self, city, country, api_key=api_key):
        self.city = city
        self.country = country
        self.api_key = api_key

    def Temperature(self):

        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}," \
              f"{self.country}&appid={self.api_key}"
        response = requests.get(url)
        content = response.json()
        temperature = round(content['main']['temp'] - 273.15, 2)
        return temperature

if __name__ == "__main__":
    weather = WeatherLocation('london', 'uk')
    print(weather.Temperature())



















