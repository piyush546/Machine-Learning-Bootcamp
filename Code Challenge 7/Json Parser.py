# -*- coding: utf-8 -*-
# json module perform all operations related to json data
import requests
import json

# Forming the url required to perform rest api operation
website = "http://api.openweathermap.org/data/2.5/weather"
query = "?q=Jaipur"
appid = "&appid=e9185b28e9969fb7a300801eb026de9c"

full_url = website+query+appid

# requesting to fetch data from the web page
fetched_data = requests.get(full_url).text

# convertig the json data into python data
# json.loads(json_data) - converts json data to python data
# json.dumps(python_data) - converts python data to json data
py_data = json.loads(fetched_data)

print('Longitude:', py_data['coord']['lat'])
print('Latitude:', py_data['coord']['lon'])
print('Weather main:', py_data['weather'][0]['main'])
print('Wind speed:', py_data['wind']['speed'])
print('Sunrise:', py_data['sys']['sunrise'])
print('Sunset:', py_data['sys']['sunset'])
