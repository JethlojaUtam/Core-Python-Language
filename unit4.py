UNIT 04

MQSQL connectivity with python
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password=""
)
print(mydb)

To create the database
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password=""
)
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE mypy")

Display the databases which are available
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password=""
)
mycursor=mydb.cursor()
mycursor.execute('SHOW DATABASES')
for i in mycursor:
	print(i)

To create the table
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="mypy"
	)
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE stud1(ENR INTEGER,NAME VARCHAR(20))")
print(mycursor)

Insert data
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="mypy"
	)
insert='INSERT INTO stud1(ENR,NAME) VALUES(%s,%s)'
record=[(101,'ABC'),(102,'DEF')]
mycursor=mydb.cursor()
mycursor.executemany(insert,record)
mydb.commit()
mycursor.close()
mydb.close()

Show the data
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="mypy"
	)
mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM stud1')
myshow=mycursor.fetchall()
for i in myshow:
	print(i)

Update record
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="mypy"
	)
mycursor=mydb.cursor()
update="""UPDATE stud1 SET NAME='MNO' WHERE ENR=101"""
mycursor.execute(update)
mydb.commit()

Delete table
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="mypy"
	)
mycursor=mydb.cursor()
delete="""DELETE FROM stud1"""
mycursor.execute(delete)
mydb.commit()

Connectivity with SQLite
import sqlite3
con=sqlite3.connect('utam.dp')

Creating the table named stud1
con.execute('CREATE TABLE stud1(ENR integer,NAME varchar)')

Inserting records
con.execute("""
	INSERT INTO stud1 VALUES
	(101,'ABC'),
	(102,'CDE')
	""")
con.commit()

Display all the records
cursor=con.execute('SELECT * FROM stud1')
for i in cursor:
	print(i)


Display record whose ENR is 102
cursor=con.execute('SELECT * FROM stud1 WHERE ENR=102')
for i in cursor:
	print(i)

Update the NAME of the student whose ENR is 102
update='''UPDATE stud1 SET NAME='PQR' WHERE ENR=102'''
con.execute(update)
con.commit()
cursor=con.execute('SELECT * FROM stud1')
for i in cursor:
	print(i)
con.commit()

Deleting the student whose NAME is XYZ
delete='''DELETE FROM stud1 WHERE NAME="XYZ"'''
con.execute(delete)
cursor=con.execute('SELECT * FROM stud1')
for i in cursor:
	print(i)

Deleting all records
delete='''DELETE FROM stud1'''
con.execute(delete)
cursor=con.execute('SELECT * FROM stud1')
for i in cursor:
	print(i)


Connect table
import sqlite3
con=sqlite3.connect('data.dp')

Create table
import sqlite3
con=sqlite3.connect('data.dp')
con.execute('CREATE TABLE STUD(ENR integer,NAME varchar(10))')
print('Table created')

Insert record
import sqlite3
con=sqlite3.connect('data.dp')
con.execute("""INSERT INTO STUD VALUES(101,'ABC'),(102,'DEF')""")
print('Record inserted')
con.commit()

Retrive the data
import sqlite3
con=sqlite3.connect('data.dp')
cursor=con.execute('SELECT * FROM STUD')
for i in cursor:
	print(i)

Retrive the 1 record
import sqlite3
con=sqlite3.conncet('data.dp')
cursor=con.execute('SELECT * FROM STUD WHERE ENR=101')
for i in cursor:
	print(i)

Update record
import sqlite3
con=sqlite3.connect('data.dp')
update="""UPDATE STUD SET NAME="MNO" WHERE ENR=102"""
con.execute(update)
cursor=con.execute('SELECT * FROM STUD')
for i in cursor:
	print(i)

Delete record
import sqlite3
con=sqlite3.connect('data.dp')
delete="""DELETE FROM STUD WHERE ENR=102"""
con.execute(delete)
cursor=con.execute('SELECT * FROM STUD')
for i in cursor:
	print(i)

Delete table
import sqlite3
con=sqlite3.connect('data.dp')
delete="""DELETE FROM STUD"""
con.execute(delete)
cursor=con.execute('SELECT * FROM STUD')
for i in cursor:
	print(i)