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