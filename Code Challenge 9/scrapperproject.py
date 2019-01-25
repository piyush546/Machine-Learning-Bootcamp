# -*- coding: utf-8 -*-

""" A project which will provide the abstract of a research paper and according
to user choice it will be downloaded or discarded. """
# Importing regex to get the link
import re

# Importing selenium  for automation
from selenium import webdriver

# importing sleep from timw module for applying delay
from time import sleep

# Importing datetime from datetime to get the date
# Importing timedelta from datetime to get the difference of required days form a date
from datetime import datetime, timedelta

# importing beautifulsoup to scarp the research papers data
from bs4 import BeautifulSoup as BS

# Providing the url of the site from where research paper is to be searched
site_url = "https://arxiv.org/"

# Loading the driver
driver = webdriver.Chrome("C:/Users/pc/Downloads/chromedriver_win32/chromedriver.exe")

# opening the site
driver.get(site_url)

# adding a delay
sleep(2)

# function for sending the dates
def date_send(date, field_holder):
    for var in range(0, len(date)):
        field_holder.send_keys(int(date[var]))
        if var < len(date)-1:
            field_holder.send_keys('-')


# getting the machine learning research papers
#mlpapers = driver.find_element_by_xpath('//*[@id="content"]/ul[3]/li/a[29]')
#mlpapers.click()

# To fetch the date
today_date = datetime.now().strftime("%Y-%m-%d")
back_date = (datetime.now()- timedelta(7)).strftime("%Y-%m-%d")

# Clicking on the Advanced serach option for date setting
Adv_search = driver.find_element_by_xpath('//*[@id="search-arxiv"]/div/div[2]/a[2]')
Adv_search.click()

# To apply filters
Mlfilter = driver.find_element_by_xpath('//*[@id="terms-0-term"]')
Mlfilter.send_keys("Machine Learning")

# To get the from which date field
from_date = driver.find_element_by_xpath('//*[@id="date-from_date"]')

# Function call for sending from which date
date_send(back_date.split('-'), from_date)

# To get the to which date field
to_date = driver.find_element_by_xpath('//*[@id="date-to_date"]')

# Function call for sending to which date
date_send(today_date.split('-'), to_date)

# To click serach ml research paper within defined time
search = driver.find_element_by_xpath('/html/body/content/section/div/div/content/div[2]/div[1]/div/form/section[3]/div[2]/div[2]/button')
search.click()

# Getting the page source
journal_data = BS(driver.page_source, 'lxml')
# applying sleep
sleep(2)

# closing the site
driver.close()


# defining a function for cleaning the data
def clean(data_value):
    for var2 in range(0, len(data_value)):
        data_value[var2] = data_value[var2].text.strip()
    return data_value


# defining a function for cleaning data-2
def clean2(data_value2):
    data_value2 = clean(data_value2)
    for var3 in range(0, len(data_value2)):
        data_value2_repl = "".join(data_value2[var3])
        data_value2_repl = data_value2_repl.replace("\n", " ")
        data_value2_repl = data_value2_repl.replace(" ", "")
        data_value2[var3] = data_value2_repl
    return data_value2


# To write the journa_name, author, abstract and pdf link
journal_name = journal_data.find_all('p', class_='title is-5 mathjax')
journal_name = clean(journal_name)


journal_author = journal_data.find_all('p', class_="authors")
journal_author = clean2(journal_author)

regex = re.compile('https://arxiv.org/pdf/\d+.\d+')
journal_link = journal_data.findAll('a')
for var4 in range(0, len(journal_link)):
     journal_link[var4] = journal_link[var4].get('href')
final_link = []
for var5 in range(0,len(journal_link)):
    if regex.match(str(journal_link[var5])) is None:
        continue
    else:
        final_link.append(journal_link[var5])

# to write the values in a file
with open("file.txt","w+") as fileobj:
    for var6 in range(0, len(final_link)):
        fileobj.write(str(var6+1)+". "+journal_name[var6]+"\n")
        fileobj.write(journal_author[var6]+"\n")
        fileobj.write("download_link: "+final_link[var6]+"\n")
        fileobj.write("*****************"+"\n")
