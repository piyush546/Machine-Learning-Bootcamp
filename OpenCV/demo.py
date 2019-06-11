# -*- coding: utf-8 -*-
"""
This is the data for local classified advertisements. It has 9 prominent 
sections: jobs, resumes, gigs, personals, housing, community, services, 
for-sale and discussion forums. Each of these sections is divided into 
subsections called categories. For example, the services section has the 
following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), 
we provide to you data from four sections

for-sale
housing
community
services

and we have selected a total of 16 categories from the above sections.

activities
appliances
artists
automotive
cell-phones
childcare
general
household-services
housing
photography
real-estate
shared
temporary
therapeutic
video-games
wanted-housing

Each category belongs to only 1 section.

About Data:

city (string) : The city for which this Craigslist post was made.
section (string) : for-sale/housing/etc.
heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program 
has all the fields but category which you have to predict as the answer.

A total of approximately 20,000 records have been provided to you, 
proportionally represented across these sections, categories and cities. 
The format of training data is the same as input format but with an additional 
field "category", the category in which the post was made.

Task:

Given the city, section and heading of an advertisement, can you predict 
the category under which it was posted?
Also Show top 5 categories which has highest number of posts
"""


"""
train_data = pd.read_json("train_data.json", lines=True)
test_data = pd.read_json("test_data.json", lines=True)
import json
with open("train_data.json") as f:
    data = json.loads(f.read())  
with open("train_data.json") as f:
    data = f.read()
"""
import pandas as pd
import requests
train_url = "http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json"
test_url = "http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json"

train_data = requests.get(train_url).text
train_data = train_data[train_data.find("{"):]
train_data = pd.read_json(train_data, lines=True)

test_data = requests.get(test_url).text
test_data = test_data[test_data.find("{"):]
test_data = pd.read_json(test_data, lines=True)

corpus = []
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
def mod_data(var):
    var = 
    