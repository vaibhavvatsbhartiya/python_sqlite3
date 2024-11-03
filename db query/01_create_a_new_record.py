import sqlite3

mySchool=sqlite3.connect('schooltest2.db')

curSchool=mySchool.cursor()

# create a table
# 1. table is created

# curSchool.execute('''CREATE TABLE STUDENTS(
#     StudentId INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT (20) NOT NULL,
#     house TEXT,
#     marks REAL);''')

# To add a new record to the table, we execute the INSERT query.
curSchool.execute("INSERT INTO STUDENTS (StudentID, name, house, marks) VALUES (1,'Sherlock',322,50);")

# We now commit the changes to confirm them.
mySchool.commit()


# mySchool.close()