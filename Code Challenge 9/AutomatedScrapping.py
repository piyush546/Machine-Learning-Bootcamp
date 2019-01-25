# -*- coding: utf-8 -*-

# Selenium is a web driver used for Web Automation.
# For more details visit https://www.seleniumhq.org/
# Importing selenium web driver for chrome
from selenium import webdriver
from time import sleep

# fetching the url
url = "https://www.facebook.com/"

# defining the driver path
driver = webdriver.Chrome("C:/Users/pc/Downloads/chromedriver_win32/chromedriver.exe")

# opening the site
driver.get(url)

# Applying sleep for 2 second for smooth functioning
sleep(2)

# Step 1
# log in the page
# Taking the mail-id
Email = driver.find_element_by_id("email")
mail = input("Enter your email:")
Email.send_keys(mail)

# Taking the password
Password = driver.find_element_by_id("pass")
pswd = int(input("Enter your password:"))
Password.send_keys(pswd)

# Applying sleep again for smooth functioning
sleep(2)

# Clicking the log in button
Login = driver.find_element_by_id('u_0_2')
Login.click()

# To get number of online contacts
online = driver.find_element_by_xpath('//*[@id="fbDockChatBuddylistNub"]/a/span[2]/span').text.strip('()')


# Again applying sleep
sleep(5)

# closing the site
driver.close()

print("Online contacts",online)