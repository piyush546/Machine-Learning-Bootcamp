# -*- coding: utf-8 -*-

""" Program to add an emopty column Child and fill the values by 1 if
age is >18 and by 0 if age is <18"""

# Importing pandas module
import pandas as pd

# Opening the training_titanic.csv file and storing it in df_mod
df_mod = pd.read_csv("training_titanic.csv")

# Adding the column Child with values 0 in the existing dataframe stored in df_mod
df_mod['Child'] = 0

# Filling the empty numerical columns
df_mod = df_mod.fillna(df_mod.mean())

# Filling child column with 1 where age is greater than 18
df_mod['Child'][df_mod['Age'] > 18] = 1

# to use .apply method on a dataframe
# To create a dataframe where we have to fill 1 for age less than 18 and 0 for more than 18
a = df_mod.loc[:, ['Age']]
a['Child'] = 'mising'


# A function to be passed in apply method for performing the above operation
def filter_data(value):
    if 0 <= value <= 18:
        return 1
    else:
        return 0


a['Child'] = a['Age'].apply(filter_data)
