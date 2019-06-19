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


#-----------------------------------------------------------------------------
"""
# Modules required for scrapping
from bs4 import BeautifulSoup as BS
import requests

# site which is to be scrapped
url = "https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html"

# Fetching the data
data = requests.get(url).text

# Applying Scrapping from the fetched data
soup = BS(data)

# Finding the required data
head = soup.find("h1").text.strip()[:14]
main_body = soup.find("dd")

abstract = main_body.findAll("p")[:2]

for index, value in enumerate(abstract):
	value = value.text.strip()
	abstract[index] = value
# Printing the fetched data
print("----------------Abstract-----------------------")
print(f"---------------{head}-----------------")
print("\n".join(abstract))
"""
#-----------------------------------------------------------------------------