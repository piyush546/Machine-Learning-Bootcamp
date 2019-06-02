# -*- coding: utf-8 -*-
"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""

# Data Preprocessing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
# loading the data
dataset = pd.read_csv("kc_house_data.csv")
order = [0,2,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
dataset = dataset[dataset.columns[order]]
dataset["sqft_above"] = dataset["sqft_above"].fillna(dataset["sqft_above"].min())
# To transform the date column 
import re
dataset["date"] = dataset["date"].apply(lambda x: re.findall(r"\d{4}", x)[0]).astype("int64")

# Model preparation
features = dataset.drop(["id"], axis=1)

"""
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features.iloc[:,1:] = scaler.fit_transform(features.iloc[:,1:])
"""
from sklearn.model_selection import train_test_split
feature_train, feature_test = train_test_split(features, test_size=0.2,random_state =2)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(feature_train.iloc[:,1:], feature_train["price"])
print(regression.score(feature_test.iloc[:,1:], feature_test["price"]))

from sklearn.linear_model import Ridge
ridge = Ridge(alpha=.5)
ridge.fit(feature_train.iloc[:,1:], feature_train["price"])
print(ridge.score(feature_test.iloc[:,1:], feature_test["price"]))

from sklearn.linear_model import Lasso
lasso = Lasso(alpha=.1)
lasso.fit(feature_train.iloc[:,1:], feature_train["price"])
print(lasso.score(feature_test.iloc[:,1:], feature_test["price"]))

from sklearn.linear_model import ElasticNet
elnet = ElasticNet()
elnet.fit(feature_train.iloc[:,1:], feature_train["price"])
print(elnet.score(feature_test.iloc[:,1:], feature_test["price"]))
