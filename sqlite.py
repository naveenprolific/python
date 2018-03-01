import sqlite3 as sq
import sys

dbcnct = sq.connect("test.db")
print("database created")


curs = dbcnct.cursor()
dbcnct.execute("DROP TABLE IF EXISTS Employees")
dbcnct.commit()
try:
   dbcnct.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Fname TEXT NOT NULL,Lname TEXT NOT NULL,Age INTERG NOT NULL,Address TEXT):")

   dbcnct.commit()

except sq.OperationalError:
    print("error")
print("table created")
dbcnct.close()
print("database closed")
