# -*- coding: utf-8 -*-

# Program to read a tabular data on remote server

# Importing pandas library
import pandas as pd

# gspread is an module to use google drive api with oauth2client module
import gspread
from oauth2client.service_account import ServiceAccountCredentials

try:
    # definig the url to fetch remote csv file
    url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

    # Passing the url in read_csv and storing the dataframe in variable remote_df
    remote_df = pd.read_csv(url)

    # Fetching the description of the remote csv file
    remote_desc = remote_df.describe()

    # Fetching few datas from starting using head
    remote_head = remote_df.head()

except NameError:
    print("name url not defined")

# ************************************************
# Reading a spreadsheet file from  google drive
# Defining the scope for enabled Api's of drive and spreadsheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

try:
    # Removed create_secret.json file from this folder for Google Security Reason
    # Getting the credentials for authenthication
    creds = ServiceAccountCredentials.from_json_keyfile_name('create_secret.json', scope)

    # Authenticating and connecting the drive
    gc = gspread.authorize(creds)

    # opening a spreadsheet in the google drive
    spread = gc.open("Section-C").sheet1

    # converting the data collected to a dataframe
    df = pd.DataFrame(spread.get_all_records())

except FileNotFoundError:
    print("No file named create_secret.json")
