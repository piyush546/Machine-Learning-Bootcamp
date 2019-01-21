# -*- coding: utf-8 -*-
# To check occurence of Api in a website scrapped
# importing regular expression, requests,BeautifulSoup
import re
import requests
from bs4 import BeautifulSoup as BS

# defining the word to be searched
regex = re.compile("APIs")
# Defining the url of the site which is to be scrapped
url = "https://www.dataquest.io/blog/web-scraping-tutorial-python/"

# Requetsing the data
data = requests.get(url).text

# To convert data into html
Soup = BS(data)

# prettifying the data
print(Soup.prettify())

# Getting the body of the data scrapped
body_data = Soup.find("body").text

# more cleaning of data
body_data = body_data.strip()

# To search the particular word from the collected data
count = regex.findall(body_data)
