# -*- coding: utf-8 -*-

# importing time module for checking the execution time
import time
import mysql.connector
# from pandas import DataFrame as DF
# initializing the start time
start_time = time.time()

# opening the connection
mydb = mysql.connector.connect(user='root', password='piyushkumar', host='localhost')

# creating the cursor
cursor = mydb.cursor()

# opening the database
cursor.execute("USE practice2")

# Opening the table to be used
cursor.execute("SELECT *from user_details")

print(cursor.fetchall())

# creating dataframe
"""data = cursor.fetchall()
df = DF(data)
df.columns = ["user_id", "username", "first_name", "last_name", "gender", "password", "status"]
df.to_csv("practce2.csv",index=False)
"""
print("-------%s seconds--------" % (time.time() - start_time))
