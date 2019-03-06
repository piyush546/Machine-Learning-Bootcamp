
# -*- coding: utf-8 -*-
""" A program to analyze the thanksgiving 2015 dataset """

# Importing the Data Analysis module
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Importing contextlib module to handle exception silently
import contextlib

# Importing regex module
# import re


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


# Function to analyse the most popular dish for thankgiving w.r.t state, salary etc.
def groupby_filter(df, col_1, col_2):

    data = df.iloc[:, [col_1, col_2]][df[1] == "Yes"]
    data = data.sort_values([col_1])

    # .groups returns a dictionary containing the grouped data
    data_repl = data.groupby([col_1, col_2]).groups

    # For fetching the keys(i.e the datas given in the row)
    keys = list(data_repl.keys())

    # values are the position where those keys exist/found
    values = [len(x) for x in list(data_repl.values())]

    final_anly = pd.DataFrame(keys, columns=['Col_1', 'Col_2'])
    final_anly['Count'] = values
    return final_anly

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
    final_statedish_anly = groupby_filter(thanks_df, 64, 2)

    # Analysing the main dish for thanksgiving income wise
    final_incomedish_anly = groupby_filter(thanks_df, 63, 2)

    # Analysing the salary range
    salary_anly = thanks_df[63].value_counts()

    # Function call
    state_vis = analysis_fun(thanks_df, 64, 1)

    salary_vis = analysis_fun(thanks_df, 63, 1)

    """ # To filter out the salary column
    # Regex pattern to filter out salary column
    regex = re.compile("\\$\d+\\W*\d+")

    # A function to be passed in .apply() method for filtering out the salaries
    def regex_fun(value):
        mod_value = regex.findall(value)
        return mod_value

    # Using the apply method to filter the income column
    thanks_df[63] = thanks_df[63].apply(regex_fun) """

    # Analysis of sauces used for thanksgiving based on various income grps
    final_sauce_anly = groupby_filter(thanks_df, 63, 8)

    # Visualizatin of the sauce analysis data
    """ """
    #
    area_dish_anly = thanks_df[60][(thanks_df[2]=="Tofurkey") & (thanks_df[1]=="Yes")].value_counts()