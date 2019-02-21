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
# .content gives byte form of fetched data
fetched_data = requests.get(full_url)

# convertig the json data into python data
# json.loads(json_data) - converts json data to python data and used for string object
# json.load(json_data) - used for file objects means for json file
# json.dumps(python_data) - converts python data to json data
py_data = json.loads(fetched_data)

# fetched_data = requests.get(full_url).json() is the optimization of above
# two lines. It will directly fetch data in json format and loads it to python
# datatype

print('Longitude:', py_data['coord']['lat'])
print('Latitude:', py_data['coord']['lon'])
print('Weather main:', py_data['weather'][0]['main'])
print('Wind speed:', py_data['wind']['speed'])
print('Sunrise:', py_data['sys']['sunrise'])
print('Sunset:', py_data['sys']['sunset'])

""" with open("Json parser.json") as f:
   data = json.load(f)
data = json.dumps(data) """

# Basics of json initialization in python
""" >>> import json
>>> data = """[
{
"faculty 1":{
"name":"vps",
"age":42},
"faculty 2":{
"name":"ajay",
"age":30
}
}
]"""
>>> type(data)
<class 'str'>
>>> data_new = json.loads(data)
>>> data_new
[{'faculty 1': {'name': 'vps', 'age': 42}, 'faculty 2': {'name': 'ajay', 'age': 30}}]
>>> data = """{
"faculty":[
{
"faculty 1":{
"name":"vps",
"age":42},
"faculty 2":{
"name":"ajay",
"age":30
}
}
]
}"""
>>> type(data)
<class 'str'>
>>> data_new = json.loads(data)
>>> data_new
{'faculty': [{'faculty 1': {'name': 'vps', 'age': 42}, 'faculty 2': {'name': 'ajay', 'age': 30}}]}
"""
