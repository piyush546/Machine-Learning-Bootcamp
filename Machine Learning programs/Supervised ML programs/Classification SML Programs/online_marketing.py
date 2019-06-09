# -*- coding: utf-8 -*-

import mysql.connector

import pandas as pd

conn = mysql.connector.connect(user="root", password="", host="localhost", db="online_marketing")

query = "select * from online_marketing"
sql_datatset = pd.read_sql(query, conn)