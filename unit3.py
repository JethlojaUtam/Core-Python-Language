UNIT-03

Regular Expression(RE)
To work with regular expression, module 're' must be imported
String=r'm\w\w'
r mean : regular expression OR row string
m mean : first character must be 'm'
\w mean : 'm' must be followed by alpha numeric value

string1='This will be printed on the \n next line'
print(string1)
string2=r'This will be printed on the \n next line'
print(string2)

Using compile() of 're' module
import re
abc=re.compile(r'm\w\w')
string1='mat matter mount man mountain river'
result=abc.search(string1)
print(result)
print(result.group())

import re
string1='net m mat cat cater'
result=re.findall(r'm\w\w',string1)
print(result)

Using split()
import re
string='Greetings, Welcome to the class'
print(string1)
result=re.split(r'\W+',string1)
print(result)

Create RE that replaces the string with another string
import re
string1='Welcome to India'
print(string1)
result=re.sub('India','Bharat',string1)
print(result)

Create RE that finds 's' from the string and prints it characters there after
import re
string1='Sun  Shines Sooner or S later'
result=re.findall(r'S[\W]',string1)
print(result)
result=re.findall(r'S\w+',string1)
print(result)

Create RE that finds the words starting with a number
import re
string1='An extra classes are arranged on 26th and 28th of this month'
result=re.findall(r'\d[\w]*',string1)
print(result)

Create RE that retrieve words having 5 characters
import re
string1='Feb Marc April August Septemb December'
result=re.findall(r'\b\w{5}\b',string1)
print(result)

Create RE that retrieve words having 5 or 6 characters
import re
string1='Feb Marc April August Septemb December'
result=re.findall(r'\b\w{5,6}\b',string1)
print(result)

Create RE that retrieve words having 4 or more than 4 but less than 7 characters
import re
string1='Feb Marc April August Septemb December'
result=re.findall(r'\b\w{4,6}\b',string1)
print(result) 

Create RE that retrieve only single digits
import re
string1='Feb 16 Marc April 7 August'
result=re.findall(r'\b\d\b',string1)
print(result)

Create RE that retrieve two digits number from the string
import re
string1='Feb 16 Marc April 7 August'
result=re.findall(r'\b\d\d\b',string1)
print(result)

import re 
string1='One Two Three 4 14'
result=re.findall(r'\b\d\d\b',string1)
print(result)

Create RE that retrieves the phone number from the string
import re
string1='abc 898989889'
result=re.findall(r'\b\d+',string1)
print(result)

Create RE that retrieves the name from the string
import re
string1='abc 898989889'
result=re.findall(r'\b\D+',string1)
print(result)

Create RE that retrieves the words starting with 'st'
import re
string1='strange summer sun stands alone'
result=re.findall(r'st[\w]*',string1)
print(result)

Create RE that retrieves the words starting with 'st' or 'su'
import re
string1='strange summer sun stands alone'
result=re.findall(r's[t,u][\w]*',string1)
print(result)

FUNCTION

Defining and calling function
Syntax:
def function_name(para-1,para-2,para-n):
	function statements

Sum of two numbers using function
def sum(a,b):
	total=a+b
	print('The sum of two numbers is: ',total)
#Calling the function
sum(2,5)
sum(2.5,5.2)

Returning the result from a function(sum of two digits)
def sum(a,b):
	total=a+b
	return(total)
#Calling the function
x=sum(2,5)
print('The sum is: ',x)
y=sum(2.5,5.2)
print('The sum is: ',y)

Program to find whether the number is even or odd using function
def eve_odd(no):
	if no%2==0:
		print('The number is even')
	else:
		print('The number is odd')
#Calling the function
eve_odd(4)
eve_odd(15)

Program to find whether the number is possitive, negative, or zero 
Using function
def pos_neg_zer(no):
	if no>0:
		print('The number is positive')
	elif no==0:
		print('The number is zero')
	else:
		print('The number is negative') 
#Calling the function
no=int(input('Enter the number: '))
pos_neg_zer(no)

Returning multiple values from a function
Program to from basic arithmatic operations using function
def arith(a,b):
	add=a+b
	sub=a-b
	mul=a*b
	div=a/b
	return add,sub,mul,div
p,q,r,s=arith(20,5)
print('The addition of two numbers: ',p)
print('The subtraction of two numbers: ',q)
print('The multiplication of two numbers: ',r)
print('The divsion of two numbers: ',s)

Pass by object
immutable objects in python: int, float, string, tuple
mutable objects in python: lists
Program to pass integer to a function and modify it
def modify(x):
	x=25
	print('The value of x inside the function is',x,id(x))
#Calling the function
x=52
modify(x)
print('The value of x outside the function is',x,id(x))

Formal and Actual arguments
def modify(x,y):	-->formalarguments
	----
	----
#Calling the function
a=2,b=5 	-->actual arguments

There are four types of actual arguments:
(1)Positional arguments
(2)Keyword arguments
(3)Default argumnets
(4)Variable length arguments

(1)Positional arguments
The number of arguments and their positions in the function defination should be match exactly with the number and positions of argument in the function call 
def combine(str1,str2):
	str3=str1+str2
	print(str3)
#Calling the function
combine('Atmiya','University')
combine('University','Atmiya')
combine('Atmiya')		#TypeError: combine() missing 1 required positional argument: 'str2'
combine('Atmiya','University','Rajkot')		#TypeError: combine() takes 2 positional arguments but 3 were given

(2)Keyword arguments
The keyword arguments are arguments that identify the parameters by their names
At the time of calling the function, we have to pass to pass two values and we can mention which value is for what
def stud(name,roll):
	print('Name of student is: ',name)
	print('Roll of student is: ',roll)
#Calling the function
stud(name='ABC',roll=1)
stud(roll=1,name='ABC')

(3)Default arguments
We can set a default value to the parameter
If while calling the function, one value which is set as default is not passed, than the default value will be taken
def stud(roll,name='ABC'):
	print('Student of name is: ',name)
	print('Student of roll is: ',roll)
#Calling the function
stud(roll=1)
stud(roll=2,name='ABC')

(4)Variable length arguments
In a situation where programmer is unaware about the requirement of the parameters in the program
Suppose while defining a function you have declared two parameters, but while executing three parameters are required than error will occur
In this case a programmer can use variable length arguments
A variable length arguments is an arguments that can accept any number of values

Format:
def name_of_function(farg,*args)

def add(farg,*args):
	sum=0
	for i in args:
		sum=sum+i
	print('Sum of all the number: ',(farg+sum))
#Calling the function
add(10,20)
add(1,2,3,4)

Passing a group of elements to a function
Some time it is reuired to receive group of elements like numbers or strings, we can accept them also a list and then pass the list to the functio
def disp(lst):
	for i in lst:
		print(i)
		#Take the input the user
print('Enter the number: ')
Calling the function
lst=[a for a in input().split( )]
disp(lst)

Anonymous Functions(Which is also known as lambda):
While writing a normal function we usuallu give the name to the function after the keyword 'def'
But in the case anonymous function the name is not defined, it is defined by the 'lambda' keyword

To find square of the number(normal function)
def sqr(no):
	return no*no
Finding the square of the number(using lambda/anonymous function)
lambda no:no*no

Finding the square of the entered number using lambda
sqr=lambda a:a*a
a=int(input('Enter the number: '))
print('The square of the entered number is: ',sqr(a))

Display the big value out of entered two values using lambda
big=lambda a,b:a if a>b else b
a,b=[int(n)for n in input('Enter two number: ').split( )]
print('The bigger number out of two entered number is: ',big(a,b))

File Handling In Python
Format: 
		file_name=open('file_name','open mode')
To white in the file
f=open('abc.txt','w')
str=input('Enter the text: ')
f.write(str)
f.close()

To read in the files
f=open('abc.txt','r')
str=f.read()
print(str)
f.close()

Append
f=open('abc.txt','a+')
str=' ,Jethloja'
f.write(str)
f=open('abc.txt','r')
a=f.read()
print(a)

Checking whether the file is available or not, if available open it
We need to import 'os' module
We will use 'path' sub-module of 'os' module
We will use 'isfile()' of 'path' sub-module to check whether file exits or not
import os 
file_name=input('Enter the name of file: ')
if os.path.isfile(file_name):
	f=open(file_name,'r')
	str=f.read()
	print(str)
	f.close()
else:
	print(file_name+ ' dose not exits')

To count number of characters, words, and lines in the file
import os,sys
file_name=input('Enter the name of file: ')
if os.path.isfile(file_name):
	f=open(file_name,'r')
else:
	print(file_name+ ' dose not exits')
	sys.exit()
cc=cw=cl=0
for line in f:
	words=line.split()
	cl=cl+1
	cw=cw+len(words)
	cc=cc+len(words)
print('Number of lines in a file are: ',cl)
print('Number of words in a file are: ',cw)
print('Number of characters in a file are: ',cc)
f.close()

Working with binary files
Copy the image file from one file to another
f1=open('20250401_103544.jpg','rb')
f2=open('utam.jpg','wb')
bytes=f1.read()
f2.write(bytes)
f1.close()
f2.close()

Using 'with' statement
It will take care of closing a file which is opened
Format: with open('file_name','open_mode') as file object:

seek(): It is helpful to know the position of the file pointer
		It returns the current position of the file pointer
		n=f.tell()
tell(): It is used to move the file pointer to another position
		f.seek(offset,fromwhere)
		offset: It represents how many bytes to move
		fromwhere: It represents from which position
encode(): converts the string into binary from

Take the data from the user and store it in the binary file
record_len=15
with open('restaurant.bin','wb') as f:
	no=int(input('How many food items you want to enter?: '))
	for i in range(no):
		food=input('Enter the name of the food item: ')
		ln=len(food)
		food=food+(record_len-ln)*' '
		food=food.encode()
		f.write(food)
		print()

Give choice to user regarding the record number to search, display the record as per the choice
record_len=15
with open('restaurant.bin','wb') as f:
	n=int(input('Enter record number to search: '))
	f.seek(record_len*(n-1))
	str=f.read(record_len)
	print(str.decode())

Zipping the contents of file
from zipfile import*
f=ZipFile('demo.zip','w',ZIP_DEFLATED)
f.write('utam.jpg')
f.write('restaurant.bin')
f.close()

Unzip the file
from zipfile import*
f=ZipFile('demo.zip','r')
f.extractall('d:')