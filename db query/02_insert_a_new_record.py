# Instead of adding known values, you can also accept user input for these values. 
# Assuming that the database MySchool is created and contains the table student, we start by creating a connection:

import sqlite3
MySchool=sqlite3.connect('schooltest2.db')
curschool=MySchool.cursor()


# To accept user input, we use variables to store each of the values.

mysid= int(input("Enter ID: "))
myname=input("Enter name: ")
myhouse=int(input("Enter house: "))
mymarks=float(input("Enter marks: "))


# We now replaces the fixed VALUES in the INSERT query with the variables, mysid, myname, myhouse and mymarks. To do this, we use the DB-API’s parameter substitution. We put a ? as a placeholder wherever we want to use a value and then give a tuple of values as the second argument to the cursor’s execute() method.

curschool.execute("INSERT INTO students (StudentID, name, house, marks) VALUES (?,?,?,?);", (mysid,myname,myhouse,mymarks))

# We now commit the changes.
MySchool.commit()