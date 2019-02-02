# -*- coding: utf-8 -*-

""" Program to read a well structured csv file with headers and applying
various functions on it like groupby, reshape, isnull , dropna, fillna """

# Importing pandas module
import pandas as pd

try:
    # Opening the csv file and storing it in the df
    df = pd.read_csv("Salaries.csv")

except FileNotFoundError:
    print("No file Salaries.csv exist")

else:
    # Applying groupby method and arranging the dataframe according to rank and discipline
    df_rank = df.groupby(['rank', 'discipline'])

    # Fetching mean of the all rank according to discipline
    df_dis_mean = df_rank.mean()

    # finding avg of the prof with discipline A
    # Applied multiple filters concept
    # Single filters can be applied following same pattern
    df_prof = df[(df['rank'] == 'Prof') & (df['discipline'] == 'A')].mean()

    # Reshaping the df_prof from series to other datatype
    # -1 retains the old values
    # we can also define the total values instead of -1 like .reshape(3,1) but it generalizes the code
    df_prof1 = df_prof.reshape(-1, 1)

    # Applying loc and iloc - indexer
    # ix is also an indexer but avoided to use
    # They are used to select particular rows and columns
    # loc is label based, here index and column_head should have string value and  range specified for row both are inclusive
    # iloc is integer based, here index and column-header should have integer value, and range specified for row and column upper range is exclusive
    df_refined = df.loc[2:10, ['rank', 'salary']]

    df_refined_iloc = df.iloc[2:10, 2:4]

    # -1 represent the last column
    df_refined_iloc = df.iloc[2:10, -1]

    # Finding the null values in the Salaries.csv
    # axis - 0 or 1 ,0 for column-wise searching and 1 for row wise searching
    # axis should be 1 in such case as here to find all the details according to row wise and design a dataframe
    # 0 can be used in such cases df.isnull().any(axis=0) means no dataframe framing
    try:
        df_null = df[df.isnull().any(axis=1)]
    except Exception as e:
        print(e)

    # Making a replica of the dataframe
    df_repl = df

    # Dropping the null containig rows using dropna, it should be the lst case to used
    # Instead of it fillna should be used as Machine Learning models do not support null values
    df_repl = df_repl.dropna()

    # Defining another replica of dataframe
    df_repl2 = df

    # Filling the null values with the mean values of that column
    df_repl2 = df_repl2.fillna(df.mean())
