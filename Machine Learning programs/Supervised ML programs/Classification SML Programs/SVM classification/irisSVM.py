"""
Q2. This famous classification dataset first time used in Fisher’s classic 
1936 paper, The Use of Multiple Measurements in Taxonomic Problems. 
Iris dataset is having 4 features of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features 
to train an svm classifier and use the trained svm model to predict the Iris 
species type. To begin with let’s try to load the Iris dataset.
"""

# Data preprocessing modules
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# Loading the dataset
from sklearn.datasets import load_iris

features = pd.DataFrame(load_iris().data)
labels = pd.Series(load_iris().target)

from sklearn.svm import SVC
svc = SVC()
svc.fit(features,labels)
print(svc.score(features, labels))

from sklearn.naive_bayes import GaussianNB
gaussian = GaussianNB()
gaussian.fit(features, labels)
print(gaussian.score(features, labels))
