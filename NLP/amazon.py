# -*- coding: utf-8 -*-

import pandas as pd
from itertools import count 
dataset = pd.read_csv("amazon_Sells.txt", delimiter = "\t",quoting=3, header=None)

import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

corpus = []
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
#from nltk.stem.porter import PorterStemmer
#ps = PorterStemmer() 
for var in count(0):
    if var == 1000:
        break
    review = re.sub('[^a-zA-Z]',' ', dataset[0][var])
    review = review.lower()
    review = review.split()
    review = [word for word in review
              if word not in set(stopwords.words('english'))]
    #review = [ps.stem(word) for word in review]
    review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = " ".join(review)
    corpus.append(review)


# Formimg bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 690)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:,1].values

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