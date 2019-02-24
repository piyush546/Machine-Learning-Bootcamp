# -*- coding: utf-8 -*-

# Importing requests and json modules for handling get,post calls
import requests
# for loads and dumps method we have to import json modules
# import json

# To handle connection error
from requests.exceptions import ConnectionError

# To handle inappropiate json format exception
#from json.decoder import JSONDecodeError

# Exception handling
try:
    website = "https://free.currencyconverterapi.com/api/v6/convert"
    query = "?apiKey=&q=USD_INR"
    appid = "&compact=ultra&apiKey=49edba13c6b9173ff03d"
    full_url = website+query+appid

    # Requesting data in json string format
    fetched_data = requests.get(full_url).json

    # json string converted in to python dictionary format using loads
    # py_data = json.loads(fetched_data)

    # python dictionary converted into json string using dumps

    converter_value = fetched_data['USD_INR']

    print("USD:")
    USD_Value = int(input())

    print("INR:")
    INR_value = USD_Value*converter_value
    print(INR_value)

# except JSONDecodeError as e:
    # print(e)

except ConnectionError as e:
    print(e)

except TypeError as e:
    print(e)
