""" A program to analyse the Baltimore city Employess salries in 2014
datasets """

# Importing the data preprocessing and visualization module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing suppress from contextlib for exception handling
from contextlib import suppress

# Data preprocessing stage
with suppress((FileNotFoundError, ValueError)):

    # Loading the Baltimore city analysis
    Baltimore_df = pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")

    """
    1.Grouping the data on JobTitle and AnnualSalary, and aggregate with
    sum, mean, etc.
    2.Sorting the data and displaying to show who get the highest salary
    """
    job_salary_grp = Baltimore_df.groupby('JobTitle')['AnnualSalary']


    job_salary_sum = job_salary_grp.sum()

    job_salary_mean = job_salary_grp.mean()

    # idxmax gives the index of the maximum value in the DataFrame or Series
    print("Maximum salary:", job_salary_mean.max(), "is earned by:", job_salary_mean.idxmax())

    # Grouping on JobTitle and sorting it and displaying the data
    job_grp = Baltimore_df.sort_values('JobTitle')


    # Finding employess for each JobRoles and Graphing it using pie chart
    job_counts_grp = Baltimore_df['JobTitle'].value_counts()
    job_counts_grp = job_counts_grp.reset_index()
    job_counts_grp.columns = ['job_title', 'count']

    job_counts_grp_visual = Baltimore_df['JobTitle'].value_counts().plot.pie(autopct='%1.1f%%',subplots=True)

    # Listing all agency id and agency name
    agency_grp = Baltimore_df.groupby(['AgencyID', 'Agency']).size()
    agency_grp = agency_grp.reset_index()
    agency_grp_req = agency_grp.iloc[:, :-1].sort_values('Agency')

    # Finding all missing Gross data in the Baltimore_df
    missing_gross = Baltimore_df[Baltimore_df['GrossPay'].isnull() == True].index.tolist()

    # Replacing the missing values in the gross data with the mean of that particular group
    # For e.g AIDE BLUE
    Grosspay_fill = Baltimore_df.groupby('JobTitle')['Agency','GrossPay'].apply(lambda x:x.fillna(x.mean()))
    Grosspay_fill = Grosspay_fill.reset_index()
    Grosspay_fill = Grosspay_fill.mean()
    Grosspay_fill = Grosspay_fill.sort_values('level_1')
    Grosspay_fill = Grosspay_fill.set_index('level_1')

"""   Alternative -
import pandas as pd
import requests
import io
import numpy as np

url = "https://data.baltimorecity.gov/api/views/2j28-xzd7/rows.csv?accessType=DOWNLOAD"
r = requests.get(url)
data = str(r.content,'utf-8')
with open("text.csv","w+") as fileobj:
    fileobj.write(data)

dataframe = pd.read_csv('text.csv')

#dataframe['AnnualSalary'] = dataframe['AnnualSalary'].str.lstrip('$')
dataframe['AnnualSalary'] = dataframe['AnnualSalary'].astype(float)

# group the data
grouped = dataframe.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean, np.std, np.size, np.min, np.max])

# sort the data
pd.set_option('display.max_rows', 10000000)
output = aggregated.sort_values(['amax'],ascending=0)
output.head(15)


aggregated = grouped.agg([np.sum])
output = aggregated.sort_values(['sum'],ascending=0)
output = output.head(15)
output.rename(columns={'sum': 'Salary'}, inplace=True)


from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind='bar',title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d')) """