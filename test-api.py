import requests
import json
from pprint import pprint

API_KEY = "6bbba9547602f48e4f0af927d8116c05"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?units=metric&lang=ja"
city = "id,1850147"

response = requests.get(BASE_URL + "&q={}&APPID={}".format(city, API_KEY))

weather_data = json.loads(response.text)

weather_tokyo_now = weather_data["weather"][0]["description"]

print("東京の天気は{}です".format(weather_tokyo_now))
