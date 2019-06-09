# -*- coding: utf-8 -*-
"""
In an experiment with a group of 30 volunteers within an age bracket of 19 to
48 years, each person performed six activities (WALKING, WALKING UPSTAIRS, 
WALKING DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone 
(Samsung Galaxy S II) on the waist. The experiments have been video-recorded 
to label the data manually.

The obtained dataset has been randomly partitioned into two sets, 
where 70% of the volunteers was selected for generating the training data 
and 30% the test data.


Attribute information 

For each record in the dataset the following is provided:

Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration. 
Triaxial Angular velocity from the gyroscope.
A 561-feature vector with time and frequency domain variables.
Its activity labels.
An identifier of the subject who carried out the experiment.

Train a tree classifier to predict the labels from the test data set using the following approaches:

(a) a decision tree approach,

(b) a random forest approach and

(c) a logistic regression.

(d) KNN approach  

Examine the result by reporting the accuracy rates of all approach on both the 
testing and training data set. Compare the results. Which approach would you recommend and why?

Perform feature selection and repeat the previous step. Does your accuracy improve?
Plot two graph showing accuracy bar score of all the approaches taken 
with and without feature selection.
"""

# Data Preprocessing modules
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# Loading the training and testing data
train_data, test_data = pd.read_csv("train.csv"), pd.read_csv("test.csv")

# splitting the data in feature and labels
features_train, features_test = train_data.iloc[:,:-1].values, test_data.iloc[:,:-1].values
labels_train, labels_test = train_data.iloc[:,-1].values, test_data.iloc[:,-1].values

# Applying LabelEncoding on the categorical labels
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
labels_train = encoder.fit_transform(labels_train)
labels_test = encoder.transform(labels_test)

# Since values in features are continuous so I am using GaussianNB
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(features_train, labels_train)
gnb_labels_pred = gnb.predict(features_test)
print("--------Gaussian Result-----------")
print("Gaussian train score:->",gnb.score(features_train, labels_train))
print("Gaussian test score:->",gnb.score(features_test, labels_test))
print("--------------------------------------------------------------")

# Mentioned in the code challenge we have apply DT, LR, RF, KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(features_train, labels_train)
knn_labels_pred = knn.predict(features_test)
print("----------KNN Result-----------")
print("KNN train score:->",knn.score(features_train, labels_train))
print("KNN test score:->",knn.score(features_test, labels_test))
print("--------------------------------------------------------------")

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(features_train, labels_train)
lr_labels_pred = lr.predict(features_test)
print("----------LogisticRegression Result-----------")
print("LR train score:->",lr.score(features_train, labels_train))
print("LR test score:->",lr.score(features_test, labels_test))
print("--------------------------------------------------------------")

from sklearn.tree import DecisionTreeClassifier 
dt = DecisionTreeClassifier()
dt.fit(features_train, labels_train)
dt_labels_pred = knn.predict(features_test)
print("----------Decision Tree Result-----------")
print("DT train score:->",dt.score(features_train, labels_train))
print("DT test score:->",dt.score(features_test, labels_test))
print("--------------------------------------------------------------")

from sklearn.ensemble import RandomForestClassifier
rft = RandomForestClassifier(n_estimators=20, random_state=0)
rft.fit(features_train, labels_train)
rft_labels_pred = knn.predict(features_test)
print("----------RFT Result-----------")
print("RFT train score:->", rft.score(features_train, labels_train))
print("RFT test score:->", rft.score(features_test, labels_test))
print("--------------------------------------------------------------")

from sklearn.svm import SVC
svc = SVC(kernel="poly", random_state=0)
svc.fit(features_train, labels_train)
svc_labels_pred = svc.predict(features_test)
print("----------SVC Result-----------")
print("SVC train score:->", svc.score(features_train, labels_train))
print("SVC test score:->", svc.score(features_test, labels_test))
print("--------------------------------------------------------------")

import statsmodels.api as sm
features_obj = features_train[:,:]
features_obj = sm.add_constant(features_obj)
# removed_feature = list(range(features_))
while(True):
    classifier_OLS = sm.OLS(endog = labels_train, exog = features_train).fit()
    p_values = classifier_OLS.pvalues
    if p_values.max() < 0.05:
        break
    else:
        val = list(p_values).index(p_values.max())
        # removed_features
    
from sklearn.svm import SVC
svc = SVC(kernel="poly", random_state=0)
svc.fit(features_train, labels_train)
svc_labels_pred = svc.predict(features_test)
print("----------SVC Result-----------")
print("SVC train score:->", svc.score(features_train, labels_train))
print("SVC test score:->", svc.score(features_test, labels_test))
print("--------------------------------------------------------------")
    



