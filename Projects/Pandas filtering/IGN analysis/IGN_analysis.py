# -*- coding: utf-8 -*-
""" A program to analyse the IGN dataset """

# Importing the preprocessing and visualization modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing suppress from contextlib to handle exceptions
from contextlib import suppress

# Preprocessing stage
with suppress((FileNotFoundError)):

    # Loading the ign datasets
    ign_df = pd.read_csv("ign.csv")
    ign_df = ign_df.iloc[:,1:]

    # finding games released for the Xbox One that have a score of more than 7.
    xbox1_sc7_find = ign_df[(ign_df['platform']=="Xbox One") & (ign_df['score']>7)]

    # Finding the games for Xbox one platform and PlayStation 4
    allgames_platform = ign_df.groupby('platform')['score_phrase'].value_counts().unstack().fillna(0)

    # To perfrom visualization by histogram
    xbox_visual = ign_df['score'][ign_df['platform']=="Xbox One"].plot.hist()
    ps4_visual = ign_df['score'][ign_df['platform']=="PlayStation 4"].plot.hist()
