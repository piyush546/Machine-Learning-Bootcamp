# -*- coding: utf-8 -*-

# Importing BeautifulSoup
from bs4 import BeautifulSoup
import requests

# Importing collections.Counter to count the words
from collections import Counter

# Specifying the url from where wew have to scrap data
url = "http://www.sih.gov.in/"

# to get the data
data = requests.get(url).text

# Storing the data in html format
modified_data = BeautifulSoup(data)

print(modified_data.prettify())

# list to contain li items
li_items = []

# fetching li data in a varaiable
div_data = modified_data.find("div", class_="col-lg-5")
li_data = div_data.findAll("li")

# fetching the text only from the li
for var in range(0, len(li_data)):
    li_items.append(li_data[var].text.strip())
# *****************************************************
# Counting the words in the li_items
# To hold all the words in li_items
total_words = []
for var2 in range(0, len(li_items)):
    total_words.extend(li_items[var2].split())
print("Words in the li content:", Counter(total_words))
