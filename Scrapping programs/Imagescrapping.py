# -*- coding: utf-8 -*-

# Importing os for folder,file etc.related work
# Importing requests for http conncetion:get,post....
# Importin cv2 - Opencv used in advanced image processing operation like image recognisition
# cv2 is better alternative that Pillow
import requests
# import os
# import cv2

# My bing Image search api - valid for 7 days
Api_key = "06cba81960bf48ee8d32aee706a2894a"

# Base url
base_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

# Defining headers and parameters
headers = {"Ocp-Apim-Subscription-key": Api_key}
params = {"q": "Samosa", "offset": 0, "count": 1}

# request for searching the image
search = requests.get(base_url, headers=headers, params=params)

# To get the json format of the requests fetched
data = search.json()

# To get content url for downloading the image
content_url = data['value'][0]['contentUrl']

# Downloaded the image
image = requests.get(content_url)

# Storing the image
# .content gives the binary mode value of the downloaded image
with open("image.jpg", "wb+") as fileobj:
    fileobj.write(image.content)
