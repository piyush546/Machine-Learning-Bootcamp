# -*- coding: utf-8 -*-

"""
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, (zip code,job description)
 is given, deal with it.
 
 Seperate the salary column in hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with average value .
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("monster.csv")

dataset = dataset.drop(['country','country_code','job_board',
'has_expired','page_url','uniq_id'],axis=1)

#
l = dataset["location"].unique()
unique_location = {}
for var in range(len(l)):
    unique_location[var] = l[var]
    
for k in dataset["organization"].keys():
    if dataset.organization[k] in l:
            temp=dataset.organization[k]
            dataset.organization[k]=dataset.location[k]
            dataset.location[k]=temp

dataset = dataset[dataset["location"].apply(lambda x: len(x)<20)]
dataset = dataset[dataset["location"].str.contains('[A-Z/a-z]')]

def hourly_basis(value):
    if value is not np.nan:
        value = value.replace("-", " ")
        if value.find("$ /hour"):
            value = value.split("$ /hour")
    return value
    
dataset["salary"] = dataset.salary.apply(hourly_basis)