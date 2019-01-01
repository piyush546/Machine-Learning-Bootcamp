# -*- coding: utf-8 -*-

# Beautifulsoup is use to extract data from a given web page
# request is used to connect the provided link to the actual web page
# unicodedata is used to perform actions on unicode data that are fetched during scrapping

from bs4 import BeautifulSoup
import requests
import unicodedata

# Using pandas to form dataframe from the stored data
import pandas as pd

# providing the url of the site required to be scrapped
url = "https://tradingeconomics.com/india/unemployment-rate"

# connecting the link to actual web site
Source = requests.get(url).text

# Scraping the data from the web page
Soup = BeautifulSoup(Source)

# cleaning the scrapped data and printing it
print(Soup.prettify())

# To find all the tables from the scrapped data
all_tables = Soup.find_all("table")

# to print all the tables fetched
print(all_tables)

# To find the required table
required_table = Soup.find("table", class_="table")

# to print the required table
print(required_table)

# lists to hold data of the required table
A = []
B = []
C = []
D = []
E = []
F = []
G = []

# Iterating over the required table
for rows in required_table.findAll("tr"):
    data = rows.findAll("td")
    a = rows.findAll("a")
    small = rows.findAll("small")
    print(":", small)
    if len(data) == 7:
        A.append(str(unicodedata.normalize('NFKD', a[0].find(text=True)).encode('ascii', 'ignore')))
        B.append(str(data[1].find(text=True)))
        C.append(str(data[2].find(text=True)))
        D.append(str(data[3].find(text=True)))
        E.append(str(data[4].find(text=True)))
        if small == []:
            F.append(str(small[0].find(text=True)))
        else:
            F.append(str(unicodedata.normalize('NFKD', small[0].find(text=True)).encode('ascii', 'ignore')))
        G.append(str(a[1].find(text=True)))


# formimg the dataframe
df = pd.DataFrame()
df['India Labour'] = A
df['Last'] = B
df['Previous'] = C
df['Highest'] = D
df['Lowest'] = E
df['Unit'] = F
df['Op'] = G
df.to_csv("former2.csv")
print(df)
