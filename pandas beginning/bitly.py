# -*- coding: utf-8 -*-

""" A program to fetch various information related to url shotener bit.ly
associated with USA Gov and applying pandas operations on them """

# Importing pandas module for performing the DataFrame operations
import pandas as pd

# For using np.nan I imported numpy module
import numpy as np

# I imported collections.Counter to check the timezones frequency
from collections import Counter

# Importing matplotlib.pyplot for pictorial representation of the stats
# import matplotlib.pyplot as plt

# Creating the dataframe of the json file containing all the url shortener hits
# pandas.read_json is convert json string to pandas object
# lines parameter reads the file as json object per line
json_df = pd.read_json("usagov_bitly_data.json", lines=True)

# Repalcing some data with some other data
# pandas.DataFrame.replace(to_replace=None, value=None,) - Replace values given in to_replace with 'value'.
json_df = json_df.replace([np.nan, ""], ["Mising", "Unknown"])

# Getting the top 10 timezones frequency using pandas method
json_df_tz = json_df['tz'].value_counts().head(10)

# Getting the top 10 timezones frequency not using pandas method
json_tz = Counter(json_df['tz'])

json_tz = sorted(json_tz.items(), key=lambda x: x[1], reverse=True)

json_tz = json_tz[:10]

# Getting frequency of each timezones
tz_count = json_df['tz'].value_counts()

# To draw the top 10 timezones frequnecy bar graph for a series we can use Series.plot.type()
json_df_tz.plot.bar()

# ************************************ #
# Fetching the browser capability i.e the first token (^\w+\/[\d\.\d]*)

# Spiliting the Fetched series of browser info. according to tokens
tokens_df = json_df['a'].str.split(n=1, expand=True).add_prefix("Token_")

# Fetching the frequency of the browser capability
tokens_frequency = tokens_df['Token_0'].value_counts()

# Plotting bar graph for top 5 browser capability
tokens_frequency.head().plot.bar()

# Fetching the os info
os_df = tokens_df['Token_1'].str.split(')',n=1,expand=True).add_prefix("os_info_")
