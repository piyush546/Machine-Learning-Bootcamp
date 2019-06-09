# -*- coding: utf-8 -*-

"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""


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
    
    # To count the total survived humans, total male counts
    # survived = titanic_df["Survived"].value_counts()[1]
    # male_counts = titanic_df["Sex"].value_counts()["male"]

    # Men's survival counts
    Men_survival_counts = (titanic_df['Survived'])[titanic_df['Sex']=='male'].value_counts()

    # Men's survival frequency
    Men_survival_frequency = (titanic_df['Survived'])[titanic_df['Sex']=='male'].value_counts(normalize=True)

    # Female survival counts
    Female_survival_counts = (titanic_df['Survived'])[titanic_df['Sex']=='female'].value_counts()

    # Female survival frequency
    Female_survival_frequency = (titanic_df['Survived'])[titanic_df['Sex']=='female'].value_counts(normalize=True)
    
    
    # Adding the column Child with values 0 in the existing dataframe stored in titanic_df
    titanic_df['Child'] = 0

    # Filling the empty numerical columns
    titanic_df = titanic_df.fillna(titanic_df.mean())

    # Filling child column with 1 where age is greater than 18
    titanic_df['Child'][titanic_df['Age'] > 18] = 1
    
    
    """
    # To create a dataframe where we have to fill 1 for age less than 18 and 0 for more than 18
    a = titanic_df.loc[:, ['Age']]
    a['Child'] = 'mising'
    
    
    # A function to be passed in apply method for performing the above operation
    def filter_data(value):
        if 0 <= value <= 18:
            return 1
        else:
            return 0
    
    
    a['Child'] = a['Age'].apply(filter_data)
    """