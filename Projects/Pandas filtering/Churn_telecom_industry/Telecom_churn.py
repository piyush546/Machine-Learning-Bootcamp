"""
File Name : Telecom_Churn.py

problem Statement:
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?
"""


# In the churn column of the dataset - True represent the churned customer and False represent the non-churned customer

# Importing pandas module for performing data analytics
import pandas as pd

# Importing contextlib module to handle the exceptions
import contextlib as clb

# Loading the dataset and performing the mentioned tasks
with clb.suppress((FileNotFoundError)):
    churn_df = pd.read_csv("Telecom_churn.csv")

    # Filtering out the churned customers
    churned_df = churn_df[churn_df['churn'] == True]

    # Task-1
    plans_count = churned_df[(churned_df['international plan'] == 'yes') & (churned_df['voice mail plan'] == 'yes')].shape
    plans_count = plans_count[0]

    # Task-2
    call_charge = churn_df.groupby('churn')['total intl charge'].sum()
    visual_1 = call_charge.plot.pie(autopct='%1.1f%%')

    # Task-3
    night_call = churned_df['total night minutes'].max()

    # Task-4
    call_analysis = churned_df.iloc[:, 7:19].sum().sort_index()
    visual_2 = call_analysis.plot.bar()

    # Task-5
    non_churn_al = churn_df['account length'][churn_df['churn'] == False].max()
    churn_al = churned_df['account length'].max()
    if churn_al > non_churn_al:
        print('churned user have the maximum account lenght')
    else:
        print('regular user have the maximum account lenght')

    # Task-6
    customer_care = churned_df['customer service calls'].value_counts()

    # Task-7
    area_popl = churn_df.groupby('area code')['international plan'].value_counts().unstack()
