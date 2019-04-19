# -*- coding: utf-8 -*-
"""
NLP - Natural Language Processing
"""

"""
There are two categories: Pos (reviews that express a positive or favorable 
sentiment) and Neg (reviews that express a negative or unfavorable sentiment).
 For this assignment, we will assume that all reviews are either positive or 
 negative; there are no neutral reviews.

Perform sentiment analysis on the text reviews to determine whether its 
positive or negative and build confusion matrix to determine the accuracy
"""

# Data Preprocessing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from itertools import count

# Loading dataset
dataset = pd.read_csv("movie.csv")

# importing modules to handle text data processing
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Filtering the class column 1 for Pos and 0 for Neg using np.where
dataset['class'] = np.where(dataset['class'] == 'Pos', 1, 0)

# Noise elimination and root finding stage
corpus = []
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer() 
for var in count(0):
    review = re.sub('[^a-zA-Z]',' ', dataset['text'][var])
    review = review.lower()
    review = review.split()
    review = [word for word in review
              if word not in set(stopwords.words('english'))]
    review = [ps.stem(words) for words in review]    
    review = " ".join(review)
    corpus.append(review)
    if var == 2000:
        break
# Formimg bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:,0].values

# Seperating training and testing data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)

# Applying the classification algorithm
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB


# Applying Different Naive Bayes

gnb =  GaussianNB()
gnb.fit(features_train, labels_train)
labels_pred = gnb.predict(features_test)
print("GaussianNB score:",gnb.score(features_test, labels_test))

############################################

mnb =  MultinomialNB()
mnb.fit(features_train, labels_train)
labels_pred_1 = mnb.predict(features_test)
print("MultinomialNB:", mnb.score(features_test, labels_test))

###################################################

bnb =  BernoulliNB()
bnb.fit(features_train, labels_train)
labels_pred_2 = bnb.predict(features_test)
print("BernoulliNB:", bnb.score(features_test, labels_test))

##############################################

# Applying the KNN classifiaction algorithm
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(features_train, labels_train)
labels_pred_3 = knn.predict(features_test)
print("Knn score:", knn.score(features_test, labels_test))

##################################################

# Framing confusion matrix
from sklearn.metrics import confusion_matrix 
cm_gnb = confusion_matrix(labels_test, labels_pred)
cm_mnb = confusion_matrix(labels_test, labels_pred_1)
cm_bnb = confusion_matrix(labels_test, labels_pred_2)
cm_knn = confusion_matrix(labels_test, labels_pred_3)