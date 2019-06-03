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
"""
Description -

Urban driver will have to travel less distance as due to good transportation
facilities but due to traffic it may be possible that speed may be low.

Rural driver will have to travel more distance due to lack of good 
transportation facilities but they can have high spped as they might speed up
for fast delievery 
"""

# Preprocessing and Visualization Modules
import pandas as pd
import matplotlib.pyplot as plt

# Import Contextlib module for exception handling
import contextlib 

# Scikit modules
# Importing kmeans module
from sklearn.cluster import KMeans


with contextlib.suppress((AttributeError, TypeError)):
    # Loading the datasets
    dataset = pd.read_csv("deliveryfleet.csv")
    
    # Extracting the features for formimg clusters
    features = dataset.iloc[:, 1:].values
    
    # Plotting the graph
    plt.scatter(features[:,0], features[:,1])
    plt.xlabel("Distance_Feature")
    plt.ylabel("Speeding_Feature")
    plt.show()
    
    # Stage to calculate WCSS and apply it in Elbow method to find minimum number
    # of clusters
    # WCSS - Wihin cLuster sum of squares
    wcss = []
    
    range_pred = [x for x in range(1,10)]
    
    for var in range_pred:
        kmeans = KMeans(n_clusters=var,init='k-means++',random_state=0)
        kmeans.fit(features)
        wcss.append(kmeans.inertia_)
        
    # Elbow method To find optimal numbers of clusters
    plt.plot(range(1,10), wcss)
    plt.title("Elbow Method")
    plt.xlabel('No.of clusters')
    plt.ylabel('Wcss')
    plt.show()
    
    """ Formimng Two clusters using Elbow method result to distinguish rural and 
    urban driver """
    kmeans = KMeans(n_clusters=2,init='k-means++',random_state=0)
    pred_cluster = kmeans.fit_predict(features)
    
    
    plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
    plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
    plt.title('Clusters of drivers')
    plt.xlabel('Distance_feature')
    plt.ylabel('Speeding_feature')
    plt.legend()
    
    # According to above visualization cluster 1 shows urban driver and cluster 2 shows rural driver
    
    """ To distinguish speeding drivers from those 
    who follow speed limits, in addition to the rural vs. urban division. """
    
    kmeans_1 = KMeans(n_clusters=4, init='k-means++', random_state=0)
    pred_cluster_1 = kmeans_1.fit_predict(features)
    
    
    plt.scatter(features[pred_cluster_1 == 0, 0], features[pred_cluster_1 == 0, 1], c = 'blue', label = 'Cluster 1')
    plt.scatter(features[pred_cluster_1 == 1, 0], features[pred_cluster_1 == 1, 1], c = 'red', label = 'Cluster 2')
    plt.scatter(features[pred_cluster_1 == 2, 0], features[pred_cluster_1 == 2, 1], c = 'green', label = 'Cluster 3')
    plt.scatter(features[pred_cluster_1 == 3, 0], features[pred_cluster_1 == 3, 1], c = 'cyan', label = 'Cluster 4')
    plt.scatter(kmeans_1.cluster_centers_[:, 0], kmeans_1.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
    plt.title('Clusters of drivers')
    plt.xlabel('Distance_feature')
    plt.ylabel('Speeding_feature')
    plt.legend()
    plt.show()
