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

dataset[['location', 'organization']] = dataset[['location', 'organization']].fillna("missing")

import re
regex = re.compile("\,\s\w{2}\W*\d*")

def  mod_fun(value1, value2):
    if regex.search(value2):
        temp = value2
        value2  = value1
        value1 = temp
    return pd.Series((value1, value2))
#dataset[['location', 'organization']] =  dataset[['location', 'organization']].apply(mod_fun)
dataset[['location', 'organization']] = dataset.apply(lambda x: mod_fun(x["location"], x["organization"]), axis=1)

dataset = dataset[dataset["location"].map(lambda x: len(x) <20 )]
dataset = dataset[dataset["location"].map(lambda x: x.isdigit() is False)]

def mod_sal(sal):
    