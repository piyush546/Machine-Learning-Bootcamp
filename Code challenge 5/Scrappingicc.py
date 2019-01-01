# -*- coding: utf-8 -*-

# Importing BeautifulSoup, requests, unicodedata, pandas
from bs4 import BeautifulSoup
import requests
# import unicodedata
import pandas as pd

# url of the site which is to be scrapped
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

# To get the data in text format
Source = requests.get(url).text

# To convert data in html format
Soup = BeautifulSoup(Source)

# Cleaning the data and printing it
print(Soup.prettify())

# To extract all the table data
table_data = Soup.find_all("table")

print(table_data)

# Extracting the required table
required_table = Soup.find("table", class_="table")

print(required_table)

# list to store the table data
A = []
B = []
C = []
D = []
E = []

# extracting the data from the required_table
for rows in required_table.findAll("tr"):
    data = rows.findAll("td")
    if(len(data) == 5):
        print(A.append(data[0].find(text=True)))
        print(B.append(data[1].find(text=True)))
        print(C.append(data[2].find(text=True)))
        print(D.append(data[3].find(text=True)))
        print(E.append(data[4].find(text=True)))

# froming dataframe
df = pd.DataFrame()
df['Pos'] = A
df['Team'] = B
df['Weighted Matches'] = C
df['Points'] = D
df['Rating'] = E
df.to_csv("former3.csv")
print(df)
