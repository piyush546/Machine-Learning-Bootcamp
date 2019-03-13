# -*- coding: utf-8 -*-

import pandas as pd
pumpkin_df = pd.read_csv("atlanta_pumpkin.csv")
col = list(pumpkin_df.columns)
dataset = pumpkin_df.loc[:,[col[10],col[11],col[14]]]

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values.reshape(-1,1)
labels = LabelEncoder().fit_transform(labels)
regressor = LinearRegression()
regressor.fit(features, labels)
dataset.loc[:,['col']] = 'missing'