# -*- coding: utf-8 -*-
""" A program to performm numpy operations on a csv file like array generation,
std.deviation etc """

# Importing pandas and numpy module
import pandas as pd
import numpy as np

# Reading the csv file using pandas and storing it in a variable named df
df = pd.read_csv("Automobile.csv")

# Handling the missing values and filing them with the max value of that column
df = df.fillna(df.max())

# getting the price and converting it into numpy array and storing it in price_arr
price_arr = np.array(df['price'])

# Calculating the max, min ,average, standard deviation from price_arr
max_price = np.max(price_arr)
min_price = np.min(price_arr)
avg_price = np.mean(price_arr)
std_dev_price = np.std(price_arr)

# Printing the prices
print("Maximum price:", max_price)
print("Minimum price:", min_price)
print("Average price:", avg_price)
print("Standard Deviation of price:", std_dev_price)
