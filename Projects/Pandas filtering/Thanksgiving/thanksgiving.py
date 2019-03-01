# -*- coding: utf-8 -*-
""" A program to analyze the thanksgiving 2015 dataset """

# Importing the Data Analysis module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing contextlib module to handle exception silently
import contextlib

with contextlib.suppress((FileNotFoundError,UnicodeDecodeError)):
    # Loading the thanksgiving dataset
    thanks_df = pd.read_csv("thanksgiving.csv", encoding="")
