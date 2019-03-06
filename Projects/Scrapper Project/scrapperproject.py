# -*- coding: utf-8 -*-

""" A project which will provide all types of information of journals published
in the duration of a week from the present date in csv format"""

# Importing pandas to create dataframe and to save the data in csv format
from pandas import DataFrame as DF
import pandas as pd

# Importing regex to get the link
import re

# Importing selenium  for automation
from selenium import webdriver

# Importing the Exception modules of the Selenium
from selenium.common.exceptions import NoSuchElementException

# importing sleep from time module for applying delay
from time import sleep

# Importing datetime from datetime to get the date
# Importing timedelta from datetime to get the difference of required days form a date
from datetime import datetime, timedelta

# importing beautifulsoup to scrap the journals list page source data
from bs4 import BeautifulSoup as BS

try:
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


    """To fetch the present date and a week before date for defining duration of
    the fetched data"""
    today_date = datetime.now().strftime("%Y-%m-%d")
    back_date = (datetime.now() - timedelta(7)).strftime("%Y-%m-%d")

    # Clicking on the Advanced search option for date setting and applying filters
    # XPath is a syntax for defining parts of an XML document. XPath uses path expressions to navigate in XML documents.
    Adv_search = driver.find_element_by_xpath('//*[@id="search-arxiv"]/div/div[2]/a[2]')
    Adv_search.click()

    # To apply filters forspecifying the journals field
    Mlfilter = driver.find_element_by_xpath('//*[@id="terms-0-term"]')
    Mlfilter.send_keys("Machine Learning")

    # To get the from which date field
    from_date_field = driver.find_element_by_xpath('//*[@id="date-from_date"]')

    # Function call for sending from which date
    date_send(back_date.split('-'), from_date_field)

    # To get the to which date field
    to_date_field = driver.find_element_by_xpath('//*[@id="date-to_date"]')

    # Function call for sending to which date
    date_send(today_date.split('-'), to_date_field)

    # To find the search button and click it to get the journal list
    search = driver.find_element_by_css_selector('body > main > div.content > div.columns.is-desktop > div.column.is-three-fifths-desktop > div > form > section:nth-child(4) > div.level > div.level-right > button')
    search.click()

    # Getting the page source and explicitly defining the parser to lxml for speed
    # lxml is the best parser for parsing the data scrapped from web
    journal_data = BS(driver.page_source, 'lxml')


    # Exception handling block
    # to get the pagination link
    # pagination_link = driver.find_element_by_xpath('/html/body/content/section/div/div/content/nav[2]/a[2]')

# Base Eception class
except NoSuchElementException as e:
    print(e)

# If no exception then else part will be executed
# else:
    # pagination_link.click()

# Fianlly will exceute in any case whether exception arises or not
finally:
    # applying sleep
    sleep(2)

    # closing the site
    driver.close()

# ************************************************************************** #
# Process for writing the collected data to a file according to requirements


# defining a function for cleaning the data
def clean(data_value):
    for var2 in range(0, len(data_value)):
        data_value[var2] = data_value[var2].text.strip()
    return data_value

# Required to write the journa;_name, author, abstract and pdf link


# Fetching the journal name
journal_name = journal_data.find_all('p', class_='title is-5 mathjax')
journal_name = clean(journal_name)

# Fetching the journal author name
journal_author = journal_data.find_all('p', class_="authors")
for var3 in range(0, len(journal_author)):
    author_tag = journal_author[var3].findAll('a')
    journal_author[var3] = clean(author_tag)

# Fetching the abstract
journal_abstract = journal_data.find_all("span", class_="abstract-full has-text-grey-dark mathjax")
journal_abstract = clean(journal_abstract)

# Fetching the all the links present in the page source
journal_link = journal_data.findAll('a')
journal_link = [var.get('href') for var in journal_link]
journal_link = list(filter(lambda x: x != None, journal_link))

# Specifying the pattern for fetching the download link of the journals
regex = re.compile('https://arxiv.org/pdf/\d+.\d+')

# fetching the required download link for the journals
final_link = []
for var4 in journal_link:
    # try catch block to handle data iterated other than string or byte
    try:
        if regex.match(var4) is not None:
            final_link.append(var4)
        else:
            continue
    except TypeError as e:
        print(e)


# Creating dataframe for the collected data
# Converted to pd.Series to avoid ValueError of null records as Series will put NaN in the place of empty record
df = DF()
df['Name'] = journal_name
df['Author'] = journal_author
df['Abstract'] = journal_abstract
df['Download link'] = pd.Series(final_link)

# To attach timestamp to the name of the file
file_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-")+"journal.csv"

# Exception handling block to handle OSerror during file saving
try:
    # saving the dataframe as csv file including journals details
    df.to_csv(file_name)

except OSError as e:
    print(e)

except NameError as e:
    print(e)

except ValueError as e:
    print(e)

else:
    print("File saved")

finally:
    print("Program ended")
