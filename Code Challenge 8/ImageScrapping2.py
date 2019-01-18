# -*- coding: utf-8 -*-

# Importing requests, cv2, os
import requests
# import cv2
import os

# Api key for bing image search
Api_key = "06cba81960bf48ee8d32aee706a2894a"

# Base url for image search
base_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

# creating headers and parameters
headers = {"Ocp-Apim-Subscription-key": Api_key}
params = {"q": '', "offset": 2, "count": 4}

# Taking input for the fruits name
fruits_name = input().split()

# Folder to store images
Path = "C:/Users/pc/AnacondaProjects/Machine learning bootcamp/Code Challenge 8/Fruits/"

# To create the folder if not present
if os.path.isdir(Path) is not True:
    os.mkdir(Path)


# function for downloading the images
def download(name, result):
    Folder = Path + name
    if os.path.isdir is not True:
        os.mkdir(Folder)
    data = result
    for var2 in range(0, len(data['value'])):
        ext = data['value'][var2]['encodingFormat']
        content_url = data['value'][var2]['contentUrl']
        img_name = f'{name}{var2}.{ext}'
        Full_image = f'{Folder}/{img_name}'
        image = requests.get(content_url)
        with open(Full_image, "wb") as fileobj:
            fileobj.write(image.content)


# To search and download images
for var in range(0, len(fruits_name)):
    params['q'] = fruits_name[var]
    search = requests.get(base_url, headers=headers, params=params)
    if search is not 0:
        download(fruits_name[var], search.json())
