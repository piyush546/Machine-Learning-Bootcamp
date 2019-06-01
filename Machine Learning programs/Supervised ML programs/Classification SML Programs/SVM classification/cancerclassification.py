# -*- coding: utf-8 -*-
"""

Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)             ----> represented by column B.
Uniformity of Cell Size(1 - 10)      ----> represented by column C.
Uniformity of Cell Shape (1 - 10)    ----> represented by column D.
Marginal Adhesion (1 - 10)           ----> represented by column E.
Single Epithelial Cell Size (1 - 10) ----> represented by column F.
Bare Nuclei (1 - 10)                 ----> represented by column G.
Bland Chromatin (1 - 10)             ----> represented by column H.
Normal Nucleoli (1 - 10)             ----> represented by column I.
Mitoses (1 - 10)                     ----> represented by column J.
Class: (2 for Benign and 4 for Malignant) ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor.

Impute the missing values with the most frequent values.
Perform Classification on the given data-set to predict if the tumor is 
cancerous or not.
Check the accuracy of the model.
Predict whether a women has Benign tumor or Malignant tumor, if her 
Clump thickness is around 6, uniformity of cell size is 2, 
Uniformity of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9, 
Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2 and 
Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)

"""

# Data processing and visualization model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
import warnings
warnings.filterwarnings("ignore") 
"""
# Loading the data
dataset = pd.read_csv("breast_cancer.csv")

# Imputing the most frequent values of the respective column inplace of missing values
dataset = dataset.fillna(dataset.max())

# Splitting the features and lables
features = dataset.iloc[:, 1:-1].values
labels = dataset.iloc[:, -1].values

# Splitting into testing and training sets
from sklearn.cross_validation import train_test_split

feature_train, feature_test, label_train, label_test = train_test_split(features, labels, test_size=0.2, random_state=0)

# Applying SVM algorithm
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state=0)
classifier.fit(feature_train, label_train)

# Model testing and checking its accuracy
labels_pred = classifier.predict(feature_test)
result = classifier.predict(np.array([6,2,5,3,2,7,9,2,4]).reshape(1,-1))
if 4 in result:
    print("Patient is having cancerous tumor")
else:
    print("Patient doesn't have cancerous tumor")
train_score = classifier.score(feature_train, label_train)
test_score  = classifier.score(feature_test, label_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(label_test, labels_pred)

print("Training accuracy of model:", train_score*100,"%")
print("Testing accuracy of model:", test_score*100,"%")
