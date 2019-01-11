# -*- coding: utf-8 -*-

import requests
import json

website = "http://free.currencyconverterapi.com/api/v5/convert"
query = "?q=USD_INR"
appid = "&compact=y"
full_url = website+query+appid

fetched_data = requests.get(full_url).text

py_data = json.loads(fetched_data)

converter_value = py_data['USD_INR']['val']

print("USD:")
INR_Value = int(input())

print("INR:")
USD_value = INR_Value*converter_value
print(USD_value)
