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