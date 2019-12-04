import requests
import json

city = input('City Name :')
api_address = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=c024db4252df483d3b82b661c1c4bb7f'.format(city)
city = input()
url = api_address + city
json_data = requests.get(url)
data = json_data.json()
print(data)