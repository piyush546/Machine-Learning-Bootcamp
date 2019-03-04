# -*- coding: utf-8 -*-
""" A program to analyze the thanksgiving 2015 dataset """

# Importing the Data Analysis module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing contextlib module to handle exception silently
import contextlib

with contextlib.suppress((FileNotFoundError, UnicodeDecodeError, NameError)):
    # Loading the thanksgiving dataset
    thanks_df = pd.read_csv("thanksgiving.csv", encoding="Windows 1252")

    # Fetching the column names in a list
    columns_list = list(thanks_df.columns)

    # Analysing how much celebrate thanksgiving
    thanksgiving_anly = thanks_df[columns_list[1]].value_counts()

    # Analysing the main dish for thanksgiving
    dish_anly = thanks_df[columns_list[2]].value_counts()

    # Analysing the salary range
    salary_anly = thanks_df[columns_list[63]].value_counts()

    # Analysing the regions
    states_anly = thanks_df.iloc[:,-1].value_counts()

    # getting states analysis for thanksgiving celebration
    states_thanks_anly = thanks_df.groupby([columns_list[64], columns_list[63], columns_list[1]])


