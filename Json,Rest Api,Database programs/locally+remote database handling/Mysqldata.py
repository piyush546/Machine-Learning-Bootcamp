# -*- coding: utf-8 -*-

# Mysql is a database server
# Performimg database handling using mysql
# importing mysql.connector
import mysql.connector
from pandas import DataFrame as DF

# Opening the connection to connect to the database
mysqldb = mysql.connector.connect(user='root', password='piyushkumar', host='localhost')

# creating the cursor
cursor = mysqldb.cursor()

# Droping an existing database
# cursor.execute("DROP DATABASE employee")

# Creating a database
cursor.execute("CREATE DATABASE Student")

# Using the existing database
cursor.execute("USE Student")

# Creating a Table in the database
cursor.execute("""CREATE TABLE STUDENT_info2(
               roll INTEGER,
               name TEXT,
               branch TEXT,
               marks INTEGER)""")

# To enter data in the table
cursor.execute("INSERT INTO STUDENT_info2 VALUES(01,'Himanshu','CSE',450)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(02,'Vidhan','CSE',480)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(03,'Arun','CSE',460)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(04,'Anirudh','CSE',460)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(05,'Diwan','CSE',470)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(06,'Piyush','CSE',380)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(07,'Vibhooti','CSE',480)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(08,'Sahil','CSE',490)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(09,'Saket','CSE',478)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(10,'Harsh','CSE',455)")

# To view data stored in the table
cursor.execute("SELECT * from STUDENT_info2")

# To fetch whole data from the table
var = cursor.fetchall()

print(var)

# creating dataframe
df = DF(var)
df.columns = ['roll', 'name', 'branch', 'marks']
df.to_csv("Studentnew.csv", index=False)

# To commit and close the database
mysqldb.commit()
mysqldb.close()
