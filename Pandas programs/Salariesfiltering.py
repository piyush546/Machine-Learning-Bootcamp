# -*- coding: utf-8 -*-

# Data Preeprocessing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


try:
    
    # Loading the dataset
    data = pd.read_csv("Salaries.csv")
    
    # 1. Which Male and Female Professor has the highest and the lowest salaries
    male_professor = data[(data['sex']=='Male') & (data['rank']=='Prof')].sort_values('salary')
    female_professor = data[(data['sex']=='Female') & (data['rank']=='Prof')].sort_values('salary')
    
    # 2. Which Professor takes the highest and lowest salaries.
    prof_data = data[data['rank']=='Prof'].sort_values('salary')
    prof_data['salary'] = prof_data['salary'].fillna(np.mean(prof_data['salary']))
    max_salary = max(prof_data['salary'])
    min_salary = min(prof_data['salary'])

    
    """ Alternative - 
    1.prof_data = data[data['rank']=='Prof']
    prof_data['salary'] = prof_data.groupby('service')['salary'].apply(lambda x: x.fillna(x.mean()))
    max_salary = max(prof_data['salary'])
    min_salary = min(prof_data['salary'])
    
    2.prof_data = data[data['rank']=='Prof']
    salary_data = np.array(prof_data['salary'])
    salary_data = salary_data[~np.isnan(salary_data)]
    max_salary = np.max(salary_data)
    min_salary = np.min(prof_data['salary'])"""
    
    # 3. Missing Salaries - should be mean of the matching salaries of those whose service is the same
    """data['salary'] = data.groupby('discipline')['salary'].apply(lambda x: x.fillna(x.mean()))"""
    
    # First Finding the mean of the salries according to the different discipline 
    a = data['salary'][data['discipline'] == 'A'].mean()
    b = data['salary'][data['discipline'] == 'B'].mean()
    
    # Filling the mean salaries for the different categories of discipline
    data['salary'][data['discipline'] == 'A'] = data['salary'].fillna(a)
    data['salary'][data['discipline'] == 'B'] = data['salary'].fillna(b)
    
    # 4. Missing phd - should be mean of the matching service 
    """data['phd'] = data.groupby('discipline')['phd'].apply(lambda x: x.fillna(x.mean()))"""
    
    # First Finding the mean of the phd according to the different discipline 
    a1 = data['phd'][data['discipline'] == 'A'].mean()
    b1 = data['phd'][data['discipline'] == 'B'].mean()
    
    # Filling the mean phd by rounding its value for the different categories of discipline
    data['phd'][data['discipline'] == 'A'] = data['phd'].fillna(round(a1))
    data['phd'][data['discipline'] == 'B'] = data['phd'].fillna(round(b1))
    
    # 5. How many are Male Staff and How many are Female Staff. Show both in numbers and Graphically using Pie Chart.  Show both numbers and in percentage
    data_gender = data['sex'].value_counts().reset_index()
    """Alternative-
    1.data_gender = data.groupby('sex').size().reset_index()
    2. data_gender = pd.DataFrame(data['sex'].value_counts())
    """
    data_gender_ref = pd.DataFrame()
    data_gender_ref['Male'] = [data_gender['sex'][0]]
    data_gender_ref['Female'] = [data_gender['sex'][1]]
    
    vis1 = plt.pie([data_gender_ref['Male'], data_gender_ref['Female']], explode=[0, 0], labels=['male','female'], autopct="%1.1f%%")
    plt.axis('equal')
    plt.show(vis1)
    
    # Function to show the actual values in pie chart
    def absolute_value(val):
        a  = np.round(val/100.*(np.array([39,39])).sum(), 0)
        return a
    vis2 = plt.pie([data_gender_ref['Male'], data_gender_ref['Female']], explode=[0, 0], labels=['male','female'], autopct=absolute_value)
    plt.axis('equal')
    plt.show(vis2)
    
    # 6. How many are Prof, AssocProf and AsstProf. Show both in numbers adn Graphically using a Pie Chart
    data_rank = data['rank'].value_counts().reset_index()
    data_rank_ref = pd.DataFrame()
    data_rank_ref['Prof'] = [data_rank['rank'][0]]
    data_rank_ref['AsstProf'] = [data_rank['rank'][1]]
    data_rank_ref['AsscProf'] = [data_rank['rank'][2]]
    
    vis3 =  plt.pie([data_rank_ref['Prof'], data_rank_ref['AsstProf'],data_rank_ref['AsscProf'] ], explode=[0, 0,0], labels=['Prof','AsstProf', 'AsscProf'], autopct="%1.1f%%")
    plt.axis('equal')
    plt.show(vis3)
    def absolute_value(val):
        a  = np.round(val/100.*(np.array([46,19,13])).sum(), 0)
        return a
    vis4 = plt.pie([data_rank_ref['Prof'], data_rank_ref['AsstProf'],data_rank_ref['AsscProf'] ], explode=[0, 0,0], labels=['Prof','AsstProf', 'AsscProf'], autopct=absolute_value)
    plt.axis('equal')
    plt.show(vis4)
    
    # 7. Who are the senior and junior most employees in the organization.
    data_service = data.sort_values(['service'])
    
    # 8. Draw a histogram of the salaries divided into bin starting from 50K and increment of 15K
    plt.hist(data['salary'], bins=range(50000, 190000, 15000), facecolor='g')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.title('Salary distribution')
    plt.grid(True)
    plt.show()

except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except AttributeError as e:
    print(e)
