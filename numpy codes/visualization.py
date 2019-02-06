# -*- coding: utf-8 -*-

""" A program to visualize normal distributions """

# Importing nummpy modules
import numpy as np

# Matplotlib - use for visualization of the data in graph forms
import matplotlib.pyplot as plt

# To Frame normal distribution for income for specified mean and std.deviation
incomes = np.random.normal(100.0, 20.0, 10000)

# Plotting a histogram for the data in the incomes variable with 50 bars
plt.hist(incomes, bins=50)
plt.show()

# To get the mean and median of the data in the incomes
income_mean = np.mean(incomes)

income_median = np.median(incomes)

# To add outliers in the incomes
incomes = np.append(incomes, [2000000, 21000000, -2100000000])

# To see the effect of the outliers
plt.hist(incomes, bins=50)
plt.show()
income_mean_1 = np.mean(incomes)
income_median_1 = np.median(incomes)
