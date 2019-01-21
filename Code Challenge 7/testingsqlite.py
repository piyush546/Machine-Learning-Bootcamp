# -*- coding: utf-8 -*-

# importing time module for calculating the executiion time
import time
import sqlite3

# initializing the start time
start_time = time.time()

# Opening the file from where we have to import the data
with open("practce2.db", "r") as fileobj:
    list1 = fileobj.readlines()
    fileobj.close()

# opening the database
mydb = sqlite3.connect("practice2.db")

# creating the cursor
cursor = mydb.cursor()

# creating the table in the database
#
"""cursor.execute("CREATE table user_details(
               user_id INTEGER,
               username TEXT,
               first_name TEXT,
               last_name TEXT,
               gender TEXT,
               password TEXT,
               status INTEGER)")"""


# a function to insert values in table
def input_take(string):
    string = string.strip().split(",")
    string[0] = int(string[0])
    string[-1] = int(string[-1])
    for var_repl in range(1, len(string)-1):
        string[var_repl] = '\"'+string[var_repl]+'\"'
    return "INSERT INTO user_details VALUES(%d,%s,%s,%s,%s,%s,%d)"%(string[0],string[1],string[2],string[3],string[4],string[5],string[6])


for var in range(1, len(list1)):
    var2 = input_take(list1[var])
    cursor.execute(var2)

# To place the cursor
cursor.execute("SELECT *from user_details")

# printing the data
print(cursor.fetchall())

print("-----%s Seconds-----" % (time.time() - start_time))
