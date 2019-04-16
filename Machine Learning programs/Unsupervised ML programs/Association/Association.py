# -*- coding: utf-8 -*-
"""
Association rules analysis is a technique to uncover how items are associated 
to each other. 
There are three common ways to measure association.

Measure 1: Support. This says how popular an itemset is, 
as measured by the proportion of transactions in which an itemset appears.
Itemsets can also contain multiple items.
If you discover that sales of items beyond a certain proportion tend to have a 
significant impact on your profits, you might consider using that proportion 
as your support threshold. You may then identify itemsets with support values 
above this threshold as significant itemsets.

Measure 2: Confidence. This says how likely item Y is purchased when item X 
is purchased, expressed as {X -> Y}. This is measured by the proportion of 
transactions with item X, in which item Y also appears.
One drawback of the confidence measure is that it might misrepresent the 
importance of an association. This is because it only accounts for how popular 
apples are, but not beers. If beers are also very popular in general, 
there will be a higher chance that a transaction containing apples will also 
contain beers, thus inflating the confidence measure.

To account for the base popularity of both constituent items, 
we use a third measure called lift.
Measure 3: Lift. This says how likely item Y is purchased when item X is 
purchased, while controlling for how popular item Y is.
the lift is 1,which implies no association between items. A lift value greater 
than 1 means that item Y is likely to be bought if item X is bought, 
while a value less than 1 means that item Y is unlikely to be bought if 
item X is bought.
"""


# Preprocessing module
import pandas as pd
# import numpy as np


# Association module - Apriori
from apyori import apriori

# loading data
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# Fetching the transcations from the loaded data
# a = dataset.iloc[:,8].dropna().tolist()
"""This will check each element before entering it into the list and drop the nan value"""
#transactions = dataset.apply(lambda x: x.dropna().tolist(), axis=1).tolist()

transactions = dataset.applymap(lambda x: [x] if pd.notnull(x) else []).sum(1).tolist()

# To fetch the transcations using for loop
"""
d = []
for var in range(0,dataset.shape[0]):
    d.append([])
    for var1 in dataset.iloc[var, :]:
        if type(var1) is float:
          pass
        else:
            d[var].append(var1)
"""

# Inintializing the required conditions for fetching the associations using apriori algo
rules = list(apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4))

# Fetching the base items and their supported items uisng for loop
"""
m = []
count = 0
for var3 in range(0, len(rules)):
    
    m.append([])
    m[var3].extend(list(rules[var3][2][0][0]))
    m[var3].extend(list(rules[var3][2][0][1]))
"""


# Printing the associations satisfying the given conditions in the apriori algo    
for item in rules:
    #print(item[0])
    # first index of the inner list
    # Contains base item and add item
    
    pair = item[0] 
    items = [x for x in pair]
    if len(items) > 2:
        print("Rule: " + items[0] + " -> ", items[1:])
    else:
        print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")