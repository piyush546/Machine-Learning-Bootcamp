# -*- coding: utf-8 -*-
""" 
CODE CHALLENGE

Q1. (Create a program that fulfills the following specification.)
mushrooms.csv

Import mushrooms.csv file

This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one.

Attribute Information:

classes: edible=e, poisonous=p (outcome)

cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s

cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s

cap-color: brown=n, buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y

bruises: bruises=t, no=f

odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s

gill-attachment: attached=a,descending=d,free=f,notched=n

gill-spacing: close=c,crowded=w,distant=d

gill-size: broad=b,narrow=n

gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,

green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y

stalk-shape: enlarging=e,tapering=t

stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?

stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s

stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s

stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

veil-type: partial=p,universal=u

veil-color: brown=n,orange=o,white=w,yellow=y

ring-number: none=n,one=o,two=t

ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z

spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y

population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y

habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d

Perform Classification on the given dataset to predict if the mushroom is edible or poisonous w.r.t. it’s different attributes.
(you can perform on habitat, population and odor as the predictors)
Check accuracy of the model.

"""

# kNN Algorithm - k nearest neighbour algorithm
# Importing the preprocessing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Loading the dataset
mushroom_data = pd.read_csv("mushrooms.csv")

mushroom_data['class'] = mushroom_data['class'].replace(['p','e'],[0,1])

# Splitting the features and labels
features = mushroom_data.iloc[:, [22,21,5]].values
labels = mushroom_data.iloc[:, 0].values

# Preprocessing stage
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder1 = LabelEncoder()
features[:, 0] = labelencoder1.fit_transform(features[:, 0])

labelencoder2 = LabelEncoder()
features[:, 1] = labelencoder1.fit_transform(features[:, 1])

labelencoder3 = LabelEncoder()
features[:, 2] = labelencoder1.fit_transform(features[:, 2])

onehotencoder1 = OneHotEncoder(categorical_features= [0], sparse= False)
features = onehotencoder1.fit_transform(features)
features = features[:, 1:]

onehotencoder2 = OneHotEncoder(categorical_features= [6], sparse= False)
features = onehotencoder2.fit_transform(features)
features = features[:, 1:]


onehotencoder3 = OneHotEncoder(categorical_features= [11], sparse= False)
features = onehotencoder3.fit_transform(features)
features = features[:, 1:]

"""labelencoder = LabelEncoder()
labels = labelencoder.fit_transform(labels)"""

# Splitting the training and testing data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)

# training phase
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 1)
classifier.fit(features_train, labels_train)

# Testing phase
labels_pred = classifier.predict(features_test)
classifier.score(features_test, labels_test)
classifier.score(features_train, labels_train)

# confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred) # labels_test

