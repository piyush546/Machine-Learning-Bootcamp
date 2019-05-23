
# -*- coding: utf-8 -*-
""" Minor Project-
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
""""

# Importing the required modules for data preprocessing and visualizing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing re module for using it i filtering out the income column
# import re

# Importing suppress from contextlib module to handle exceptions
from contextlib import suppress

# Loading the datasets and starting the required preprocessing
with suppress((FileNotFoundError, TypeError, AttributeError, ValueError)):
    # Encoding of the dataset is in Windows 1252 so it should be specified while loading it
    datath_df = pd.read_csv("thanksgiving.csv", encoding="Windows 1252")
    
    datath_df.head(10)

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
    datath_df[63] = datath_df[63].replace(np.nan, 'mising')
    """datath_df[63] = datath_df[63].replace(['Prefer not to answer', 'mising'],['0','0'])

     regex = re.compile("\d+\W*\d+")

    # A function to be passed in .apply() method for filtering out the salaries
    def income_filter(value):
        value = regex.findall(value)
        value = [int(x.replace(",", "")) for x in value]
        return sum(value)/(len(value)+0.1) """

    def clean_income(value):
        if value == "$200,000 and up":
            return 200000
        elif value == "Prefer not to answer" or value == 'Mising':
            return np.nan
        else:
            value = value.replace(",", "").replace("$", "")
            income= value.split(" to ")
            return (int(income[0]) + int(income[-1])) / 2

    # Using the apply method to filter the income column
    datath_df[63] = datath_df[63].apply(clean_income)

    # Fetching the average incomes for each type sauces

    sauce_compr = datath_df.groupby(8)[63]

    sauce_inc = sauce_compr.mean()

    # Visualizing the average income of the various sauces
    sauces_inc_visual = sauce_inc.plot.bar()
    plt.show()

    # Comparing the incomes of canned and homemade sauces
    craneberry_compr = sauce_inc.iloc[[0, 1]]

    # Visualizing the incomes of various craneberry sauces
    craneberry_compr_visual = craneberry_compr.plot.pie(autopct="%1.1f%%")
    plt.show()

    # Comparing the toufourkey eaten in Suburban and Rural areas
    toufurkey_compr = area_based.iloc[[1, 2], [-3]]

    # Visualizing the toufurkey eaten by suburban and rural people
    toufurkey_compr.plot.bar(color=["green"])  # yes suburban eat more toufurkey than rural people
    plt.show()
    # Checking for a correlation between thankgiving prayer seeker and their income
    prayer_inc = datath_df.groupby(51)[63].value_counts().unstack().fillna(0)

    # Visualizing the relation between prayer seeker and their income
    prayer_inc_visual = prayer_inc.plot.bar()
    plt.show()

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
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("thanksgiving.csv", encoding="Windows 1252")

col_names = list(dataset.columns)
refrence_number = [x for x in range(0,65)]  
refrence = dict(zip(refrence_number, col_names))   
dataset.columns = refrence_number

regions = list(dataset[64].unique())
income = list(dataset[63].unique())
regional_dish = pd.DataFrame()
income_dish = pd.DataFrame()
for var in regions:
    regional_dish[var] = dataset[2][dataset[64]==var].value_counts()
for var1 in income:
    income_dish[var1] = dataset[2][dataset[63]==var1].value_counts()
del(var)
del(var1)

def income_filter(value):
    if value is np.nan:
        return np.NaN
    else:
        value = value.replace("$","")
        value = value.replace(",","")
        value = value.split(" ")
        value = [int(x) for x in value if x.isdigit()]
        if len(value)!=0:
            return sum(value)/len(value)
        else:
            return np.NaN

dataset[63] = dataset[63].apply(income_filter)

homemade_data = dataset[63][(dataset[8]=="Homemade")].value_counts()
canned_data = dataset[63][(dataset[8] == "Canned")].value_counts()
saucido_compr = pd.DataFrame(columns=["homemade","canned"])
saucido_compr["homemade"] = homemade_data
saucido_compr["canned"] = canned_data

sauce_compr = dataset.groupby(8)[63]
sauce_inc = sauce_compr.mean()
sauce_inc.plot.bar(grid=True)


area_data = dataset[60][dataset[2]=="Tofurkey"].value_counts()
bf_data1 = dataset[57].value_counts()
bf_data2 = dataset[59].value_counts()


income_data = dataset.groupby(51)[63].value_counts()
#income_data = dataset.groupby(51)[63].count()

max_grp = list(saucido_compr['homemade'][saucido_compr["homemade"] == saucido_compr["homemade"].max()].index)

inc_dis_data = dataset.groupby(60)[2].value_counts()

pattern = dataset.groupby([2,8])[63].value_counts()

"""    
    
    
    
    
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

""" a = datath_df[63].reset_index()

a[63] = a[63].replace(np.nan, 'mising')
def clean_income(value):
    if value == "$200,000 and up":
        return 200000
    elif value == "Prefer not to answer" or value == 'mising':
        return np.nan
    else:
        value = value.replace(",", "").replace("$", "")
        income= value.split(" to ")
        return (int(income[0]) + int(income[-1])) / 2
a[63] = a[63].apply(clean_income) """