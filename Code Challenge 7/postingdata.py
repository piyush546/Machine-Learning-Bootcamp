# -*- coding: utf-8 -*-

""" Get and post both are used to send and fetch data but get sends the
parameter in the query string whereas post sends data in body format and this
make post more secure compare to get method.Also the size of content
we can send in get is fixed whereas in post it is unlimited and the body is
termed as payload in post.
In get we can send the queries directly with url or we can pass it through
params = Dict where we store the query string as key value pair in
Dict variable and pass it in params.
Also what sort of function get and post will perform depends upon api
wheteher that api provide sending and fetching data or any one type of
functionality."""

# Post contains body whereas get method doesn't have it.
import requests
import json

# Formimg the base for POST operation
Host = "http://httpbin.org/post"

# Fetching data using post method
# requests.post(Host).json()

body = {'firstname': ['charlie', 'charles', 'Chris'], 'language': ['English', 'Spanish', 'french']}

# to convert python data to json data
payload = json.dumps(body)

# Headers are used to send additional information
""" Headers basically instruct the server how to handle data or how to opearte
it.For example I am sending Content-Type as application/json then it will the
recieved data in json format means in programming we do not have to convert
our content from python dictionary to json.Server will automatically do that
as we have specified it. """
headers = {"Content-Type": "application/json", "Content-Length": len(payload), "data": payload}


# POST operation function
def client_api():

    # SEnding the data using post data
    client_data = requests.post(Host, payload, headers)
    return client_data


print(client_api().text)


# GET operation function
def server_api():

    # Sending the data by get method
    # Queries are associated whatever we pass into it
    # Query_param = {'firstname':'Kamela','Language':'African'}
    # server_data = requests.get("http://httpbin.org/get", params = Query_param)
    server_data = requests.get("http://httpbin.org/get?firstname=Kamela&language=African")


    return server_data


print(server_api().text)
