# -*- coding: utf-8 -*-


# Modules
import pandas as pd
import numpy as np

# datasets
data = pd.read_csv("human_body_temperature.csv")

# array of data
arr = np.array(data.iloc[:,0])
mean = np.mean(arr)

import matplotlib.pyplot as plt
plt.boxplot(arr)
plt.show()


""" BOX PLOT - 
1st quartile - median of lower half dataset ---q1
2nd quartile - median of entire dataset----q2
3rd aurtile - median of upper half dataset-----q3
interquartile range - difference from quartile 1 to quartile 3
extreme values - smallest and the largest value in the dataset
ouliers - q1<1.5(IQR)<q3