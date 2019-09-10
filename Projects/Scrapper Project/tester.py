from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException as NSE
# from bs4 import BeautifulSoup
import pandas as pd
import re
url = "https://www.tofler.in"
city_name = input("Enter city name:")
work_field = input("Enter work field:")
n = []
driver = webdriver.Chrome("C:/Users/pc/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(url)
tab_click = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div/div/div[5]/center/a")
tab_click.click()

cities_list = driver.find_element_by_xpath("/html/body/main/div/div/div/div[3]/div[1]/div")
city_option = cities_list.find_element_by_link_text(city_name)
city_option.click()
w_fields = driver.find_element_by_xpath("/html/body/main/div/div/div/div[3]/div[2]/div")
field_s  = w_fields.find_element_by_link_text(work_field)
field_s.click()
try:
    while True:
        table_data = driver.find_element_by_tag_name("table")
        m = table_data.text.split("\n")
        for var in m[1:]:
            n.append(re.findall("\D+\d*\D+|\d+", var))
        next_page = driver.find_element_by_link_text("NEXT")
        next_page.click()
except NSE:
    print("Search Ends")
driver.close()

df = pd.DataFrame(n)
df.columns = ["Name", "Incorp.Date", "Status"]
df.to_excel("sanchit.xls", index=False)