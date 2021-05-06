import json
from urllib.request import urlopen

api_key = "51d3a9ca0fe3bdbb76213aae41895cb6"
response = urlopen('http://api.openweathermap.org/data/2.5/weather?q=Paris&appid=' + api_key).read()

data = json.loads(response)

print(data["weather"][0]["description"])


