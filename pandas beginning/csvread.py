# -*- coding: utf-8 -*-

# Program to read a csv file having no headers(coulumn name)
# Pandas - a library for Data Engineering
"""pandas is a Python package providing fast, flexible, and expressive
data structures designed to make working with structured
(tabular, multidimensional, potentially heterogeneous) and time series data
both easy and intuitive."""
# For more, visit- https://pypi.org/project/pandas/

# For using pandas features importing pandas library
import pandas as pd

# To open a csv file without any haeders and storing it in a variable df
df = pd.read_csv("testing.csv", header=None)

# To describe about the datas fetched while reading the csv file
df_describe = df.describe()

# To get the starting few datas in the dataframe
# By default head reads only first 5 data of the dataframe'
# We can spoecify the size of the head
df_head = df.head()
