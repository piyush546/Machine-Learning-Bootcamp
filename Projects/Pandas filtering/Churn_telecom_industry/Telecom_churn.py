# -*- coding: utf-8 -*-
""" A program to perfrom analysis on the Telecom industry churn dataset """

# Importing pandas, numpy, matplotlib
import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# Importing contextlib to enhance with functionality
import contextlib

with contextlib.suppress(FileNotFoundError):
    # Loading the datasets containing the Telecom churn data
    churn_df = pd.read_csv("Telecom_churn.csv")

# ***************************************** #
with contextlib.suppress((NameError, ValueError, TypeError)):

    # To do churn analysis
    churn_analysis = churn_df['churn'].value_counts()

    # To analyse the popularity of international plan scheme
    intl_packs_anly = churn_df['international plan'].value_counts()

    # To analyse the popularity of voice mail plan
    voice_mail_anly = churn_df['voice mail plan'].value_counts()

    # To fetch the records of those states where Churning is True
    state_churn_anly = churn_df.iloc[:, :][churn_df['churn'] == True]

    # Churn analysis based on area code
    code_churn_anly = pd.DataFrame(state_churn_anly['area code'].value_counts())

    code_churn_anly.columns = ['count']
