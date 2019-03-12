# -*- coding: utf-8 -*-

"""A prgram to check total number of people survived in titanic accident and
then out of them check how many males survived and how many females survived"""

# Importing pandas module as pd
import pandas as pd

try:
    # Reading training_titanic.csv file and storing it in a variable namded titanic_df
    titanic_df = pd.read_csv("training_titanic.csv")

except FileNotFoundError as e:
    print(e)

else:
    # Fetching the count of survived and death peoples
    # 1 represent alive and 0 death
    survival_counts = titanic_df['Survived'].value_counts()

    # Fetching the frequency of the survival records
    # normalize setto True to get the frequency
    survival_frequency = titanic_df['Survived'].value_counts(normalize=True)

    # Men's survival counts
    Men_survival_counts = (titanic_df['Survived'])[titanic_df['Sex']=='male'].value_counts()

    # Men's survival frequency
    Men_survival_frequency = (titanic_df['Survived'])[titanic_df['Sex']=='male'].value_counts(normalize=True)

    # Female survival counts
    Female_survival_counts = (titanic_df['Survived'])[titanic_df['Sex']=='female'].value_counts()

    # Female survival frequency
    Female_survival_frequency = (titanic_df['Survived'])[titanic_df['Sex']=='female'].value_counts(normalize=True)

    # to use .apply method on a dataframe
    # To create a dataframe where we have to fill 1 for age less than 18 and 0 for more than 18
    a = titanic_df.loc[:,['Age']]
    a['Child'] = 'mising'
    def filter_data(value):
        if 0<= value <=18:
            return 1
        else:
            return 0


    a['Child'] = a['Age'].apply(filter_data)
