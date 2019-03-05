# -*- coding: utf-8 -*-
""" A program to analyze the thanksgiving 2015 dataset """

# Importing the Data Analysis module
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Importing contextlib module to handle exception silently
import contextlib

# Importing regex module
import re


# A function for analyzing the thanksgiver count on basis of various other info
def analysis_fun(df, col_1, yes_col):
    # Analytics part
    total_counts = df[col_1].value_counts()

    yes_counts = df[col_1][df[yes_col] == "Yes"].value_counts()

    final_df = pd.concat([total_counts, yes_counts], axis=1)
    final_df.columns = ['Total', 'Thanksgiver']

    # Visualization part
    visual = final_df.plot.bar(color=['SkyBlue', 'IndianRed'])

    return visual


with contextlib.suppress((FileNotFoundError, UnicodeDecodeError, NameError, AssertionError)):
    # Loading the thanksgiving dataset
    thanks_df = pd.read_csv("thanksgiving.csv", encoding="Windows 1252")

    # Fetching the column names in a list
    columns_list = list(thanks_df.columns)

    # Replacing the missing values with the keyword Mising
    thanks_df = thanks_df.replace([np.nan], ['Mising'])

    # Renaming the columns with numerical values
    thanks_df.columns = [x for x in range(0, 65)]

    # Analysing how much celebrate thanksgiving
    thanksgiving_anly = thanks_df[1].value_counts()

    # Analysing the main dish for thanksgiving state wise
    state_dish_anly = thanks_df.iloc[:, [64, 2]][thanks_df[1] == "Yes"]
    state_dish_anly = state_dish_anly.sort_values([64])

    """ dem = state_dish_anly.groupby([64, 2]).groups
    keys = list(dem.keys())
    values = [len(x)  for x in list(dem.values())]
    final_state_dish_anly = pd.DataFrame(keys, columns=['States', 'Dish'])
    final_state_dish_anly['Count'] = values """

    # Analysing the main dish for thanksgiving income wise
    income_dish_anly = thanks_df.iloc[:, [63, 2]][thanks_df[1] == "Yes"]

    # Analysing the salary range
    salary_anly = thanks_df[63].value_counts()

    # Function call
    state_vis = analysis_fun(thanks_df, 64, 1)

    salary_vis = analysis_fun(thanks_df, 63, 1)

    # To filter out the salary column
    # Regex pattern to filter out salary column
    regex = re.compile("\$\d+\W*\d+")

    # A function to be passed in .apply() method for filtering out the salaries
    def regex_fun(value):
        mod_value = regex.findall(value)
        return mod_value

    # Using the apply method to filter the income column
    thanks_df[63] = thanks_df[63].apply(regex_fun)

