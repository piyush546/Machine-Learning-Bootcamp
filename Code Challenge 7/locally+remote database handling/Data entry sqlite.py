# -*- coding: utf-8 -*-
# To perfrom database handling using SQLite - Structured data, query based
# SQLite is database engine that works against single database files.
# importing sqlite3 for SQLite operations
import sqlite3
# to create dataframe importing pandas
from pandas import DataFrame as DF


# Connecting to the database - if exist then open else first create and then connect
litedb = sqlite3.connect("db_Univ")

# To create cursor which point to the data
cursor = litedb.cursor()


# To create table in the database
cursor.execute("""CREATE TABLE STUDENT_info2(
               roll INTEGER,
               name TEXT,
               marks INTEGER)""")

# To enter data in the table
cursor.execute("INSERT INTO STUDENT_info2 VALUES(01,'Himanshu',450)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(02,'Vidhan',480)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(03,'Arun',460)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(04,'Anirudh',460)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(05,'Diwan',470)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(06,'Piyush',380)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(07,'Vibhooti',480)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(08,'Sahil', 490)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(09,'Saket',478)")
cursor.execute("INSERT INTO STUDENT_info2 VALUES(10,'Harsh',455)")

# To perform operation on table stored in database
cursor.execute("SELECT * from STUDENT_info2")

#  To view table data
# 3 methods - fetchone, fetchmany, fetchall
# using fetchall. data display depends on cursor
var = cursor.fetchall()

# printing the data in tables
print(var)

# Forming dataframes
df = DF(var)
df.columns = ['roll', 'name', 'marks']
print(df)

df.to_csv("Studentdata.csv", index=False)

# To commit and close the connection
litedb.commit()
litedb.close()
