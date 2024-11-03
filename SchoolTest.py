import sqlite3

mySchool = sqlite3.connect('schooltest.db') # if file schooltest.db exist connection is successful otherwise schooltest.db file created and all set.

curSchool = mySchool.cursor()

# now to execute commands we need to use execute first.
# so code looks like

curSchool.execute('''CREATE TABLE STUDENTS(
    StudentId INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT (20) NOT NULL,
    house TEXT,
    marks REAL);''')

mySchool.close()