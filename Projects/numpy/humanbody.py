# -*- coding: utf-8 -*-
"""
    Test for Normal Distribution of Data with Python
    Check if your data is normally distributed in Python with a visualization 
    as well as a calculation given by the Scipy library.
"""
try:
    
    # Scipy module is imported to apply Normal Distribution Test
    # Data Processing and Visualization modules
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.mlab as mlab
    from scipy import stats
    
    # Loading the dataset
    data = pd.read_csv("human_body_temperature.csv")
    
    # Fetching the temperature data in numpy array for calculation for Normal disribution Test
    arr = np.array(data.iloc[:,0])
    mean = np.mean(arr)
    variance = np.var(arr)
    sigma = np.sqrt(variance)
    
    
    # To Plot a histogram and a Gaussian Curve To visualize the Normal Distribution
    plt.figure(1)
    plt.hist(arr,normed=True,color='black',bins=7)
    plt.xlim((min(arr), max(arr)))
    
    # For the Gaussian Curve
    x = np.linspace(min(arr), max(arr), 100)
    plt.plot(x, mlab.normpdf(x, mean, sigma),color="red")
    plt.show()
    
    # Normal distribution Test
    stats, pvalue = stats.normaltest(data['temperature'])
    if pvalue > 0.05:
        print("Data is normally distributed")
    else:
        print("Data is not normally distributed")
    """ ouput - statistics and pvlaue
    alpha value = 0.05
    if p-value > alpha then data follows normal distribution 
    else
    not
    """
except RuntimeError as e:
    print(e)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
""" 


BOX PLOT - 
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

plt.show() 

def histograms_plot():
    
    histograms plot
    
    # ??????
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # ??????
    num_bins = 50

    # ????,???????
    n, bins, patches = plt.hist(x, bins=num_bins, normed=1, color="green", alpha=0.6, label="hist")

    # ??????????,????
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, "r--", label="line")

    # ??????
    plt.legend(loc="upper left", shadow=True)

    # ????
    plt.show()
    return
histograms_plot() 
"""