import requests
import json
from pprint import pprint

API_KEY = "1850147"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?units=metric&lang=ja"
city = "Kobe,jp"

response = requests.get(BASE_URL + "&q={}&APPID={}".format(city, API_KEY))

wheather_data = json.loads(response.text)

pprint(wheather_data)

print("神戸の天気は" + weather_data[weather][description] + "です")

