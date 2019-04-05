# -*- coding: utf-8 -*-
"""
    Test for Normal Distribution of Data with Python
    Check if your data is normally distributed in Python with a visualization 
    as well as a calculation given by the Scipy library.
"""
try:
    
    # Modules
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.mlab as mlab
    
    # datasets
    data = pd.read_csv("human_body_temperature.csv")
    
    # array of data
    arr = np.array(data.iloc[:,0])
    mean = np.mean(arr)
    variance = np.var(arr)
    sigma = np.sqrt(variance)
    
    
    # To Plot a histogram and a Gaussian Curve
    plt.figure(1)
    plt.hist(arr, normed=True)
    plt.xlim((min(arr), max(arr)))
    x = np.linspace(min(arr), max(arr), 100)
    plt.plot(x, mlab.normpdf(x, mean, sigma))
    plt.show()

except ModuleNotFoundError as e:
    print(e)
except RuntimeError as e:
    print(e)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)



""" BOX PLOT - 
1st quartile - median of lower half dataset ---q1
2nd quartile - median of entire dataset----q2
3rd aurtile - median of upper half dataset-----q3
interquartile range - difference from quartile 1 to quartile 3
extreme values - smallest and the largest value in the dataset
ouliers - q1<1.5(IQR)<q3

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

arr = np.random.randn(100)

plt.figure(1)
plt.hist(arr, normed=True)
plt.xlim((min(arr), max(arr)))

mean = np.mean(arr)
variance = np.var(arr)
sigma = np.sqrt(variance)
x = np.linspace(min(arr), max(arr), 100)
plt.plot(x, mlab.mesh(x, mean, sigma))

plt.show() """