# -*- coding: utf-8 -*-

# NoSQL -for working with large sets of distributed data
# Mongodb is a type of NoSQL and its format is similar to json
# importing Mongodb for performimg nosql operations
# Also updating the data on mlab
from pymongo import MongoClient
import requests
# import json

# My api key for the accessing of mlab
api_key = "6ubdT8Ey8c_fB73B-2bRA8xU_BHLkoYR"
database = "student"
collection = "student_info"
# defining the base_url
# base_url = "https://api.mlab.com/api/1"

# creating client
client = MongoClient("localhost", 27017)
url = "https://api.mlab.com/api/1/databases/{}/collections/{}?apiKey={}".format(database, collection, api_key)
# making the database
mongodb = client.Student


# database -> collections-> key value pair data
# function to add data in the collections
def add_data(roll, name, marks):
    # setting an unique key to avoid duplicacy
    # return a boolean value
    unique_id = mongodb.Student_info.find_one({'roll': roll})
    if unique_id:
        print("Student already exist")
    else:
        mongodb.Student_info.insert({
                'roll': roll,
                'name': name,
                'marks': marks})
        print("Added successfully")


# function to fetch all the data
def fetch_All():
    # fetching all the data from the collection
    data = mongodb.Student_info.find({})
    # to hold the data to be deployed to mlab
    data_dict = {}

    for var in data:
        for k, v in var.items():
            if k == "_id":
                continue
            else:
                data_dict[k] = v
        response = requests.post(url, json=data_dict)
        print(response)
        print(var)


# inserting data
add_data(1, 'Himanshu', 450)
add_data(2, 'Vidhan', 480)
add_data(3, 'Arun', 460)
add_data(4, 'Anirudh', 460)
add_data(5, 'Diwan', 470)
add_data(6, 'Piyush', 380)
add_data(7, 'Vibhooti', 480)
add_data(8, 'Sahil', 490)
add_data(9, 'Saket', 478)
add_data(10, 'Harsh', 455)


# to fetch all data
fetch_All()
