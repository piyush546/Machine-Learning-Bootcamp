# -*- coding: utf-8 -*-
"""import requests
import json
url = "http://127.0.0.1:5000/posttesting"
data = {"name":"piyush", "age":20}
data = json.dumps(data)
response = requests.post(url, json=data).text
print(response)"""

def mod_(name, age):
	return f"Hello {name} your age is:{age}"
