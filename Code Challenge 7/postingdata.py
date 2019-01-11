# -*- coding: utf-8 -*-

import requests
import json

# Formimg the base for POST operation
Host = "http://httpbin.org/post"
body = {'firstname':['charlie', 'charles', 'Chris'],'language':['English', 'Spanish', 'french']}
# to convert python data to json data
json_body = json.dumps(body)
# headers are provided to distinguish the contents
headers = {"Content-Type":"application/json","Content-Length":len(json_body),"data":json_body}


# POST operation function
def client_api():
    client_data = requests.post(Host, json_body, headers)
    return client_data


print(client_api().text)


# GET operation function
def server_api():
    server_data = requests.get("http://httpbin.org/get?firstname=charles&language=Spanish")
    return server_data


print(server_api().text)
