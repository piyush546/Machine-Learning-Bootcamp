# -*- coding: utf-8 -*-

""" A program to apply Association algo on BreadBasket_DMS.csv """

import pandas as pd
# import numpy as np
from apyori import apriori

dataset = pd.read_csv("BreadBasket_DMS.csv")

transactions = []
dataset.groupby('Transaction')['Item'].apply(lambda x: transactions.append(list(set(x))))

"""
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
"""

rules = list(apriori(transactions, min_support = 0.003, min_confidence= 0.20,
                     min_lift = 2))

for var in rules:
    print("Rule:",list(var[2][0][0]), "->", list(var[2][0][1]))
    print("Support:"+ str(var[1]))
    print("Confidence:"+ str(var[2][0][2]))
    print("Lift:"+ str(var[2][0][3]))
    print("################################################################")