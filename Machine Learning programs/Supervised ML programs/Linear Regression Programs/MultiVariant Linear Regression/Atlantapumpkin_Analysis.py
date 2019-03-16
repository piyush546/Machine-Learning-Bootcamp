# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from contextlib import suppress
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

with suppress((FileNotFoundError)):
    pumpkin_df = pd.read_csv("atlanta_pumpkin.csv")
    col = list(pumpkin_df.columns)
    dataset = pumpkin_df.loc[:,[col[10],col[11],col[14]]]
    pumpkin_df = pumpkin_df.fillna(method='ffill')
    pumpkin_df = pumpkin_df.dropna(axis=1)

    """ features = dataset.iloc[:,:-1].values

    d = list(set(dataset.iloc[:,-1].values))
    m = [x for x in range(0,6)]
    d_m = dict(zip(d,m))
    dataset.iloc[:,-1] = dataset.iloc[:,-1].replace(d_m)
    labels = dataset.iloc[:,-1].values.reshape(-1,1)

    regressor = LinearRegression()
    regressor.fit(features, labels) """

    """ d = pumpkin_df.loc[:,['Origin']].value_counts()
    d = d['Origin'].value_counts()


    Origin          Mostly High
    ALABAMA         145.00          4
    CANADA          150.00          1
    MICHIGAN        154.75         21
                    150.00          7
                    286.00          7
                    15.00           4
                    145.00          1
    NORTH CAROLINA  135.00         10
    TENNESSEE       16.75           1
                    140.00          1
    Name: Mostly High, dtype: int64


    Origin          Item Size
    ALABAMA         med           4
    CANADA          med           1
    MICHIGAN        sml          18
                    jbo           7
                    med-lge       7
                    xlge          7
                    lge           1
    NORTH CAROLINA  sml          10
    TENNESSEE       lge           1
    Name: Item Size, dtype: int64
    """
