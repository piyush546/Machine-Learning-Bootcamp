
# -*- coding: utf-8 -*-
""" A program to analyze the thanksgiving 2015 dataset """

# Importing the required modules for data preprocessing and visualizing
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Importing re module for using it i filtering out the income column
import re

# Importing suppress from contextlib module to handle exceptions
from contextlib import suppress

# Loading the datasets and starting the required preprocessing
with suppress((FileNotFoundError, TypeError, AttributeError, ValueError)):
    # Encoding of the dataset is in Windows 1252 so it should be specified while loading it
    datath_df = pd.read_csv("thanksgiving.csv", encoding="Windows 1252")

    # Fetching the columns name for further reference
    columns_name = list(datath_df.columns)

    # Initializing a code number for each column name
    code_col = [x for x in range(0, 65)]

    # Storing the column name with their codes for further reference
    columns_ref = dict(zip(code_col, columns_name))

    # Initializing the dataframe with the codes of the column
    datath_df.columns = code_col

    # Fetching the data that perform thanksgiving for further processing
    datath_df = datath_df[datath_df[1] == "Yes"]

    # Filling out the empty values with 'Mising' keyword
    datath_df = datath_df.replace(np.nan, 'Mising')

    # Analysing for the state, area  and income based what is consumed in thankgiving dinner
    state_based = datath_df.groupby(64)[2].value_counts().unstack().fillna(0)

    income_based = datath_df.groupby(63)[2].value_counts().unstack().fillna(0)

    area_based = datath_df.groupby(60)[2].value_counts().unstack().fillna(0)

    # Analysis of the sauces prefered by each incomes group people
    sauce_incgrp = datath_df.groupby(8)[63].value_counts().unstack().fillna(0)

    # Filtering the gender and income columns using .apply method
    def gender_filter(value):
        if value == "Male":
            value = 'M'
        elif value == "Female":
            value = 'F'
        else:
            pass
        return value

    """ def fil(value):
        value = value.replace(",", "")
        value = value.replace("$","")
        return value
    datath_df[63] = datath_df[63].apply(fil) """
    datath_df[62] = datath_df[62].apply(gender_filter)
    datath_df[63] = datath_df[63].replace(['Prefer not to answer', 'mising'],['0','0'])

    regex = re.compile("\d+\W*\d+")

    # A function to be passed in .apply() method for filtering out the salaries
    def income_filter(value):
        value = regex.findall(value)
        value = [int(x.replace(",", "")) for x in value]
        return sum(value)/(len(value)+0.1)

    # Using the apply method to filter the income column
    datath_df[63] = datath_df[63].apply(income_filter)

    # Fetching the average incomes for each type sauces

    sauce_compr = datath_df.groupby(8)[63]

    sauce_inc = sauce_compr.mean()

    # Visualizing the average income of the various sauces
    sauces_inc_visual = sauce_inc.plot.bar()

    # Comparing the incomes of canned and homemade sauces
    craneberry_compr = sauce_inc.iloc[[0, 1]]

    # Visualizing the incomes of various craneberry sauces
    craneberry_compr_visual = craneberry_compr.plot.pie(autopct="%1.1f%%")

    # Comparing the toufourkey eaten in Suburban and Rural areas
    toufurkey_compr = area_based.iloc[[1, 2], [-3]]

    # Visualizing the toufurkey eaten by suburban and rural people
    toufurkey_compr.plot.bar(color=["green"])  # yes suburban eat more toufurkey than rural people

    # Checking for a correlation between thankgiving prayer seeker and their income
    prayer_inc = datath_df.groupby(51)[63].value_counts().unstack().fillna(0)

    # Visualizing the relation between prayer seeker and their income
    prayer_inc_visual = prayer_inc.plot.bar()

    # Analyzing the Blackfriday sales activity
    blackfri_sales = datath_df[57].value_counts()

    """
        Verifying a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes,
        but those who also have Roast Beef have the lowest incomes
    """

    pattern_income = datath_df.groupby([2, 8])[63].value_counts().unstack().fillna(0)
"""
import pandas as pd

data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")
data.head()

data["gender"] = data["What is your gender?"].apply(gender_code)
data["gender"].value_counts(dropna=False)

data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts(dropna=False)

import numpy as np
import math

def clean_income(value):
    if value == "$200,000 and up":
        return 200000
    elif value == "Prefer not to answer":
        return np.nan
    elif isinstance(value, float) and math.isnan(value):
        return np.nan
    value = value.replace(",", "").replace("$", "")
    income_high, income_low = value.split(" to ")
    return (int(income_high) + int(income_low)) / 2

data["income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(clean_income)
data["income"].head()



data["What type of cranberry saucedo you typically have?"].value_counts()

homemade = data[data["What type of cranberry saucedo you typically have?"] == "Homemade"]
canned = data[data["What type of cranberry saucedo you typically have?"] == "Canned"]

print(homemade["income"].mean())
print(canned["income"].mean())


grouped = data.groupby("What type of cranberry saucedo you typically have?")
grouped
grouped.groups
grouped.size()

for name, group in grouped:
    print(name)
    print(group.shape)
    print(type(group))

grouped["income"]
grouped["income"].size()


grouped["income"].agg(np.mean)
grouped.agg(np.mean)

grouped = data.groupby(["What type of cranberry saucedo you typically have?", "What is typically the main dish at your Thanksgiving dinner?"])
grouped.agg(np.mean)

grouped = data.groupby("How would you describe where you live?")["What is typically the main dish at your Thanksgiving dinner?"]
grouped.apply(lambda x:x.value_counts())

"""