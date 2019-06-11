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
# Data Preprocessing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Url to fetch data and requests module will be used to fetch data from url
# Pandas read_json method is used to convert fetched data in DataFrame
# Some special characters were creating probelm so find method is used
import requests
train_url = "http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json"
test_url = "http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json"

train_data = requests.get(train_url).text
train_data = train_data[train_data.find("{"):]
train_data = pd.read_json(train_data, lines=True)

test_data = requests.get(test_url).text
test_data = test_data[test_data.find("{"):]
test_data = pd.read_json(test_data, lines=True)

# Applying NLP on heading column
corpus = []
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

def mod_data(var):
    var = re.sub('[^a-zA-Z]',' ', var)
    var = var.lower()
    var = var.split()
    var = [word for word in var
              if word not in set(stopwords.words('english'))]
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer() 
    var = [ps.stem(words) for words in var]
    var = " ".join(var)
    corpus.append(var)
train_data["heading"].apply(mod_data)

# Generating the Bag of Words
from sklearn.feature_extraction.text import CountVectorizer
words = CountVectorizer(max_features=1500)
features = words.fit_transform(corpus).toarray()

features = np.append(features, train_data.iloc[:,[1,-1]].values, axis=1)


# Label Encoding function
label_encoders = []
counter = 0
def encode(index, data):
    if type(data) != np.ndarray:
        return None
    else:
        global counter
        global label_encoders
        counter+=1
        a = 'encoder'+str(counter)
        from sklearn.preprocessing import LabelEncoder
        a = LabelEncoder()
        data[:, index] = a.fit_transform(data[:, index])
        label_encoders.append(a)
        return data[:, index]
        
features[:, 1501] = encode(1501, features)
features[:, 1500] = encode(1500, features)
features = features.astype('int')
labels = encode(0, train_data.iloc[:,0].values.reshape(-1,1))
labels = labels.astype('int')        

# Splitting the train data in train and test data for model testing
from  sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)

# Model Testing Phase
from sklearn.naive_bayes import BernoulliNB
bnb = BernoulliNB()
bnb.fit(features_train, labels_train)
bnb_pred = bnb.predict(features_test)
print("---------------Bernoulli Naive Bayes--------------------------------")
print("Training score:->", bnb.score(features_train, labels_train))
print("Testing score:->", bnb.score(features_test, labels_test))
print("###################################################################")

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(features_train, labels_train)
dtc_pred = dtc.predict(features_test)
print("---------------Decision Tree Classifier--------------------------------")
print("Training score:->", dtc.score(features_train, labels_train))
print("Testing score:->", dtc.score(features_test, labels_test))
print("###################################################################")

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(features_train, labels_train)
lr_pred = lr.predict(features_test)
print("---------------Logistic Regression--------------------------------")
print("Training score:->", lr.score(features_train, labels_train))
print("Testing score:->", lr.score(features_test, labels_test))
print("###################################################################")
 
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(features_train, labels_train)
gnb_pred = bnb.predict(features_test)
print("---------------Gaussian Naive Bayes--------------------------------")
print("Training score:->", gnb.score(features_train, labels_train))
print("Testing score:->", gnb.score(features_test, labels_test))
print("###################################################################")

from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(features_train, labels_train)
mnb_pred = mnb.predict(features_test)
print("---------------Multinomial Naive Bayes--------------------------------")
print("Training score:->", mnb.score(features_train, labels_train))
print("Testing score:->", mnb.score(features_test, labels_test))
print("###################################################################")
      
# Real testing data processing
test_data["heading"].apply(mod_data)
red_features = words.transform(corpus).toarray()
red_features = np.append(red_features,test_data.iloc[:,[0,-1]], axis=1)
red_features[:, 1500] = label_encoders[1].transform(red_features[:, 1500])
red_features[:, 1501] = label_encoders[0].transform(red_features[:, 1501])
red_features = red_features.astype("int")
red_lr_pred = lr.predict(red_features)
highest_category = pd.Series(red_lr_pred).value_counts().reset_index()
highest_category.columns = ["category", "count"]
highest_category["category"]=label_encoders[2].inverse_transform(highest_category["category"])

# Visualizing the most popular category
sns.barplot(highest_category["category"], highest_category["count"])
plt.xticks(rotation=85)
plt.title("Category_share")
plt.xlabel("Category")
plt.ylabel("Count")
plt.grid(True)
plt.show()
