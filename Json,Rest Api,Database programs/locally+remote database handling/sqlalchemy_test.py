# -*- coding: utf-8 -*-
""" A program to implement database handling through sqlalchemy module """

# to create engine to through the database importing create_engine from sqlalchemy
# Impporting some methods required for creating a table
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

# Importing declarative_base to create a base class to be inherited by other classes creating tables
from sqlalchemy.ext.declarative import declarative_base

# Importing sessionmaker to create session for exceuting various operations on our database
# sessionmaker allows to create a session factory
from sqlalchemy.orm import sessionmaker
# Initializing the base class
Base = declarative_base()

# Inintializing the class for employee table
class Employee_details(Base):
    # Initializing the table name
    __tablename__ ="Employee"

    # Creating our table field
    empid = Column('empid', Integer, primary_key=True)
    first = Column('first', String)
    last = Column ('last', String)
    pay = Column('pay', Integer)
# Using sqlite as dialect for database management
# dialect+driver :/// filename
# setting echo True will dump or show all the commands executed internally
engine = create_engine("sqlite:///employee.sqlite",echo=True)

# Creating our table schema bind to engine
Base.metadata.create_all(bind=engine)



# Initializing the values to be inseted in the table
ids = [1, 2, 3]
first_names = ['Sylvester', 'Yogendra', 'Kunal']
last_names =['Fernandes', 'Singh', 'Vaid']
salary = [50000, 70000, 30000]

# Ziping all the data in a single list
final_data = list(zip(ids,first_names,last_names,salary))





# Creating a function for adding data to the table
def add_data(c, var_0, var_1, var_2, var_3):

    # Creating a session factory bind to engine
    Session_c = sessionmaker(bind=engine)

    # Creating an object of table class
    emp_c = Employee_details()

    # Creating a session
    session_c = Session_c()

    # Inserting values in the employee table
    emp_c.empid = var_0
    emp_c.first = var_1
    emp_c.last = var_2
    emp_c.pay = var_3
    session_c.add(emp_c)
    # Commiting the changes made during the session
    session_c.commit()
    # closing the sesssion
    session_c.close()


# Initializing the count to create different session for adding multiple data
count = 0
for var in final_data:
    # Function call for adding data
    add_data(count, var[0], var[1], var[2], var[3])

    # Increasing count after adding the data to the table
    count += 1


# To view our data stored in the table
Session = sessionmaker(bind=engine)
session = Session()
empl = session.query(Employee_details)
for var2 in empl:
    print(var2.empid, var2.first, var2.last, var2.pay)
session.close()


######################################################################

""" Alternative-

from sqlalcheny import create_engine


# Creating  an common interface to database from Sqlalchemy
# sqlalchemy supports many dialects like mysql, sqlite etconn.
# sqlite:/// - dialect+driver
# employee.sqlite - filename
engine = create_engine('sqlite:///employee.sqlite')

# Connecting to a database
conn = engine.connect()

# Step 1
 conn.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
         )""")

# STEP 2
conn.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
conn.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
conn.execute("INSERT INTO employees VALUES (03,'Rohit', 'Mishra', 30000)")
conn.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
conn.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")

#
conn.execute("SELECT * FROM employees").fetchone()


#
conn.close()
"""