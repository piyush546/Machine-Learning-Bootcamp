""" A program to analyse the Balitmore city Employess salries in 2014
datasets """

# Importing the data preprocessing and visualization module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing suppress from contextlib for exception handling
from contextlib import suppress

# Data preprocessing stage
with suppress((FileNotFoundError)):

    # Loading the Balitmore city analysis
    Balitmore_df = pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")

    """
    1.Grouping the data on JobTitle and AnnualSalary, and aggregate with
    sum, mean, etc.
    2.Sorting the data and displaying to show who get the highest salary
    """
    job_salary_grp = Balitmore_df.groupby('JobTitle')['AnnualSalary'].value_counts()


    job_salary_sum = job_salary_grp.sum()

    job_salary_mean = job_salary_grp.mean()

    # idxmax gives the index of the maximum value in the DataFrame or Series
    print("Maximum salary:", job_salary_mean.max(), "is earned by:", job_salary_mean.idxmax())

    # Grouping on JobTitle and sorting it and displaying the data
    job_grp = Balitmore_df['AnnualSalary'].value_counts()
    job_grp = pd.DataFrame(list(job_grp))
    print(job_grp.)

    # Finding employess for each JobRoles and Graphing it using pie chart
    job_counts_grp = Balitmore_df['JobTitle'].value_counts()
    job_counts_grp = job_counts_grp.reset_index()
    job_counts_grp.columns = ['job_title', 'count']

    job_counts_grp_visual = job_counts_grp.plot.pie(radius=10, autopct="%1.1f%%")

    # Listing all agency id and agency name
    agency_grp = Balitmore_df.groupby(['AgencyID', 'Agency']).size()
    agency_grp = agency_grp.reset_index()
    agency_grp_req = agency_grp.iloc[:, :-1].sort_values('Agency')

    # Finding all missing Gross data in the Balitmore_df
    missing_gross = Balitmore_df[Balitmore_df['GrossPay'].isnull() == True].index.tolist()
