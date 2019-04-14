# -*- coding: utf-8 -*-

""" A program to develop a model for Kmeans clustering to fetch some useful 
information from the cluster formed from deliveryfleet.csv


Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv

Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the 
mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

Perform K-means clustering to distinguish urban drivers and rural drivers.
Perform K-means clustering again to further distinguish speeding drivers from those 
who follow speed limits, in addition to the rural vs. urban division.
Label accordingly for the 4 groups.
"""

# modules
import pandas as pd
import matplotlib.pyplot as plt


# Loading the datasets
dataset = pd.read_csv("deliveryfleet.csv")

# Extracting the features for formimg clusters
features = dataset.iloc[:, 1:].values

# Plotting the graph
plt.scatter(features[:,0], features[:,1])
plt.show()

# Finding number of clusters required
wcss = []
range_pred = [x for x in range(1,11)]


# Importing kmeans module
from sklearn.cluster import KMeans


for var in range_pred:
    kmeans = KMeans(n_clusters=var,init='k-means++',random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
    
# Elbow method
plt.plot(range_pred, wcss)
plt.title("Elbow Method")
plt.xlabel('No.of clusters')
plt.ylabel('Wcss')
plt.show()

# Formimng Two clusters using Elbow method result
kmeans = KMeans(n_clusters=4,init='k-means++',random_state=0)
pred_cluster = kmeans.fit_predict(features)


plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'cyan', label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of drivers')
plt.xlabel('Distance_feature')
plt.ylabel('Speeding_feature')
plt.legend()
plt.show()
