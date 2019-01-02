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
#G = []

leave = 0
total_rows = required_table.findAll("tr")
# Iterating over the required table
for rows in total_rows:
    data = rows.findAll("td")
    if len(data) == 7:
        #A.append(str(unicodedata.normalize('NFKD', a[0].find(text=True)).encode('ascii', 'ignore')))
        A.append(data[0].text.strip())
        B.append(data[1].text.strip())
        C.append(data[2].text.strip())
        D.append(data[3].text.strip())
        E.append(data[4].text.strip())
        F.append(data[5].text.strip())
    if leave == len(total_rows)-1:
        break
    leave += 1
#        if small == []:
#            F.append(str(small[0].find(text=True)))
#        else:
#            F.append(str(unicodedata.normalize('NFKD', small[0].find(text=True)).encode('ascii', 'ignore')))
#        G.append(str(a[1].find(text=True)))

head = [i.text.strip() for i in total_rows[0].findAll('th')]
# formimg the dataframe
df = pd.DataFrame()
df[head[0]] = A
df[head[1]] = B
df[head[2]] = C
df[head[3]] = D
df[head[4]] = E
df[head[5]] = F
df.to_csv("former2.csv", index=False)
print(df)
