# -*- coding: utf-8 -*-

# Program to read an excel file with no headers

# Importing pandas module
import pandas as pd

try:
    # Reading the excel file withou headers and storing it in the excel_df variable
    excel_df = pd.read_excel("testing.xlsx", header=None)

    # Getting the details of what has been read in the excel file
    excel_describe = excel_df.describe()

    # Fetching the few datas  from the beginning
    excel_head = excel_df.head()

except FileNotFoundError:
    print("File b'testing.xlsx' does not exist")

