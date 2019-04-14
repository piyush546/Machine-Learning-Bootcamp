# -*- coding: utf-8 -*-

"""
T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height and weight of a customer.

You want to standardize the production on three sizes: small, medium, and large. How would you figure out the actual size of these 3 types of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense out of the data as stated above.

"""

# Preprocessing and Visualization modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sklearn modules
from sklearn.cluster import KMeans

# Exceptioon Handling module
# import contextlib

# Loading the tshirt csv
tshirt_data = pd.read_csv("tshirts.csv")

# Extracting the features i.e height and weight
features = tshirt_data.iloc[:, 1:].values

# Visualizing the features to get information to form clusters
plt.scatter(features[:, 0], features[:, 1])
plt.title("Customers height and Weight records")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

# Calculating the WCSS and applying Elbow Method
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
# Elbow Method 
plt.plot(range(1,11), wcss)
plt.title("Elbow Method")
plt.xlabel("No. of clusters")
plt.ylabel("WCSS")
plt.show()

# Applying K-means using the K obtained by Elbow method
kmeans_1 = KMeans(n_clusters=3, init="k-means++", random_state=0)
pred_cluster = kmeans_1.fit_predict(features)

# Plotting the Clusters with centroid
plt.scatter(features[pred_cluster==0,0], features[pred_cluster==0,1],c='b',label='cluster1')
plt.scatter(features[pred_cluster==1,0], features[pred_cluster==1,1],c='g',label='cluster2')
plt.scatter(features[pred_cluster==2,0], features[pred_cluster==2,1],c='r',label='cluster3')
plt.scatter(kmeans_1.cluster_centers_[:, 0], kmeans_1.cluster_centers_[:, 1],c='y',label="centroids")
plt.title("Customers height and Weight records")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend()
plt.show()
