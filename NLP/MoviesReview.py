# -*- coding: utf-8 -*-
"""
NLP - Natural Language Processing
"""

"""
There are two categories: Pos (reviews that express a positive or favorable 
sentiment) and Neg (reviews that express a negative or unfavorable sentiment).
 For this assignment, we will assume that all reviews are either positive or 
 negative; there are no neutral reviews.

Perform sentiment analysis on the text reviews to determine whether its 
positive or negative and build confusion matrix to determine the accuracy
"""

# Data Preprocessing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading dataset
dataset = pd.read_csv("movie.csv")

# importing modules to handle text data processing
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Filtering the class column 1 for Pos and 0 for Neg using np.where
dataset['class'] = np.where(dataset['class'] == 'Pos', 1, 0)

# Noise elimination and root finding stage
corpus = []
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer() 
for var in range(0,2000):
    review = re.sub('[^a-zA-Z]',' ', dataset['text'][var])
    review = review.lower()
    review = review.split()
    review = [word for word in review
              if word not in set(stopwords.words('english'))]
    review = [ps.stem(words) for words in review]    
    review = " ".join(review)
    corpus.append(review)

# Formimg bag of words model
from sklearn.feature_extraction.text import CountVectorizer