# -*- coding: utf-8 -*-
# Data can be fetched from Kaggle IEEE competition.
# Importing Data analysis and visualization modules
import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt

# Loading the transaction data and identity data for training
train_transaction_data = pd.read_csv("train_transaction.csv")
train_identity_data = pd.read_csv("train_identity.csv")

# Showing the top data of transaction records
print(train_transaction_data.head())

# Showing top data of identity records
print(train_identity_data.head())

# Checking the nan values in each column in transaction data
print(train_transaction_data.isnull().sum(axis=0).values)

# Checking the nan values in identity records
print(train_identity_data.isnull().sum(axis=0).values)

# Checking the numbers of transaction_id that are similar in both transaction and identity dataset
tt_id = train_transaction_data.TransactionID.values
ti_id = train_identity_data.TransactionID.values
print("Total ids in transaction records", len(tt_id))
print("Total ids in identity records", len(ti_id))
print("Number of transaction id common in both the dataset", len(np.intersect1d(tt_id, ti_id)))

# Cleaning the transaction and identity data
# A function to drop the not required column
def data(dataset, values, limit):
    index = list(values<limit)
    return dataset.iloc[:,index]

val = train_transaction_data.isnull().sum(axis=0).values
val2 = train_identity_data.isnull().sum(axis=0).values

train_transaction_data = data(train_transaction_data,val, 250000)
train_identity_data = data(train_identity_data,val2, 60000)

# Handling the missing values
def miss(dataset):
    dataset = dataset.fillna(dataset.max())
    dataset = dataset.replace(np.nan, "Missing")
    return dataset

train_transaction_data = miss(train_transaction_data)
train_identity_data = miss(train_identity_data)

# Handling the categorical columns
from sklearn.preprocessing import LabelEncoder
encoders = []
cat_col = [x for x in train_transaction_data.columns if train_transaction_data.dtypes[x] == "object"]
for val in cat_col:
     obj= LabelEncoder()
     train_transaction_data[val] = obj.fit_transform(train_transaction_data[val])
     encoders.append(obj)

# Splitting the features and labels from the training dataset of transaction
features = train_transaction_data.drop("isFraud", axis=1).values
labels = train_transaction_data["isFraud"].values

# Spilitting the features and labels into temporary train and test data
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(
        features, labels, test_size=0.2, random_state=0)
                                                            

# Fitting the features and labels in classification models
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(features, labels)
print(dtc.score(features_test, labels_test))

# Loading the test data for transactions
test_transaction_data = pd.read_csv("test_transaction.csv")
print(test_transaction_data.head())
print(test_transaction_data.isnull().sum(axis=0).values)
col = list(train_transaction_data.columns)
col.remove("isFraud")
test_transaction_data = test_transaction_data.loc[:,col]
test_transaction_data = miss(test_transaction_data)
test_transaction_data = test_transaction_data.replace("scranton.edu", "gmail.com")
for index, val4 in enumerate(cat_col):
    test_transaction_data[val4] = encoders[index].transform(test_transaction_data[val4])

real_labels_test = dtc.predict(test_transaction_data)

# Creating the required csv file
result_dataset = pd.DataFrame()
result_dataset["TransactionID"] = test_transaction_data["TransactionID"].values
result_dataset["isFraud"] = real_labels_test
result_dataset.to_csv("submission.csv", index=False)
