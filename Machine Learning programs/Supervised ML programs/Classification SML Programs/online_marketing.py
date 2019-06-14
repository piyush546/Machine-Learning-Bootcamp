# -*- coding: utf-8 -*-
"""
#Online Marketing

(Click Here To Download Resource File) : 
    http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/online_marketing.sql

Objective of this case study is to explore Online Lead Conversion for a 
Life Insurance company. Some people are interested in buying insurance 
products from this company hence they visit the site of this Life Insurance 
Company and fill out a survey asking about attributes like income, age etc. 
These people are then followed and some of them become customers from leads. 
Company have all the past data of who became customers from lead. Idea is to 
learn something from this data and when some new lead comes, 
assign a propensity of him/her converting to a 
customer based on attributes asked in the survey. This sort of problem 
is called as Predictive Modelling

Concept:

Predictive modelling is being used by companies and individuals all over the 
world to extract value from historical data. These are the 
mathematical algorithms, which are used to "learn" the patterns hidden on 
all this data. The term supervised learning or classification is also used 
which means you have past cases tagged or classified 
(Converted to Customer or Not) and you want to use this learning on new data.(machine learning)

Here are the attributes of the survey:

ATTRIBUTE

AGE (AGE OF THE LEAD)
JOB (JOB CATEGORY E.G. MANAGEMENT)
MARITAL (MARITAL STATUS)
EDUCATION (EDUCATION OF LEAD)
SMOKER (IS LEAD SMOKER OR NOT (BINARY – YES / NO))
MONTHLYINCOME (MONTHLY INCOME)
HOUSEOWNER (IS HOME OWNER OR NOT (BINARY – YES / NO))
LOAN (IS HAVING LOAN OR NOT (BINARY – YES / NO))
CONTACT (CONTACT TYPE E.G. CELLPHONE)
MOD (DAYS ELAPSED SINCE SURVEY WAS FILLED)
MONTHLYHOUSEHOLDINCOME (MONTHLY INCOME OF ALL FAMILY MEMBER)

TARGET_BUY (ALTOGETHER IS CONVERTED TO CUSTOMER OR NOT (BINARY –YES /NO). 
THIS IS KNOWN AS TARGET OR RESPONSEAND THIS IS WHAT WE ARE MODELLING.)

ACTIVITIES YOU NEED TO PERFORM:

A. HANDLE THE MISSING DATA AND PERFORM NECESSARY DATA PRE-PROCESSING.
B. SUMMARISE THE DATA.
C. PERFORM FEATURE SELECTION AND TRAIN USING PREDICTION MODEL.
D. FOR A NEW LEAD, PREDICT IF IT WILL CONVERT TO A SUCCESSFUL LEAD OR NOT.
E. USE DIFFERENT CLASSIFICATION TECHNIQUES AND COMPARE ACCURACY SCORE AND ALSO PLOT THEM IN A BAR GRAPH.
"""

# Data Preprocessing and visualization modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Importing the mysql module to load the sql data
import mysql.connector
conn = mysql.connector.connect(user="root", password="", host="localhost", db="online_marketing")
query = "select * from online_marketing"

# Loading the sql data in the pandas dataframe using read_sql method
sql_dataset = pd.read_sql(query, conn)

# Handling the missing data
sql_dataset = sql_dataset.fillna(sql_dataset.max())
sql_dataset["job"] = sql_dataset["job"].ffill()

# Fetching the feature and the labels
features = sql_dataset.iloc[:,:-1]
labels = sql_dataset.iloc[:,-1].values
