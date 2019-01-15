# -*- coding: utf-8 -*-

# Importing BeautifulSoup
from bs4 import BeautifulSoup
import requests

# Specifying the url from where wew have to scrap data
url = "http://www.sih.gov.in/"

# to get the data
data = requests.get(url).text

# Storing the data in html format
modified_data = BeautifulSoup(data)

print(modified_data.prettify())

# list to contain
