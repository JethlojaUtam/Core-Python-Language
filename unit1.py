UNIT-01

converting the number of any number system to decimal.
a=0b01101101011
b=0o222
c=0xE222
d=int(a)
print('value of 01101101011 is',d)
e=int(b)
print('value of 222 is',e)
f=int(c)
print('value of E222 is',d)

a='01101101011'
b='222'
c='E222'
d=int(a,2)
print('value of 01101101011 is',d)
e=int(b,8)
print('value of 222 is',e)
f=int(c,16)
print('value of E222 is',d)

Datatype
(1) None
converting a decimal number to equivalent binary, octal and hexadecimal.
a=7
aa=bin(a)
print(aa)
bb=oct(a)
print(bb)
cc=hex(a)
print(cc)

(2) Numerical
converting datatype explicity
a=23.2
print(a)
b=int(a)
print(b)

a=23
print(a)
b=float(a)
print(b)

boolean datatype
a=7>35
print(a)
a=7<35
print(a)

(3) Sequences
I). str datatype
a='Welcome to Atmiya University'
print(a)

a="Welcome to Atmiya University"
print(a)

a='''Python is a very interesting programming language.
    It requris very less code.'''
print(a)

a="""Python is a very interesting programming language.
    It requris very less code."""
print(a)

To retieve a piece of string from the whole string [] is used.
a='Welcome to Atmiya University'
print(a)
print(a[0])
print(a[0:7])
print(a[11:17])
print(a[:11])
print(a[-13:-12])
print(a[-13:])
print(a[-13:-3])

'*' is a repetition operator
print(a*2)

II). bytes datatype
Numeric, 0-255, Positive, Can not update
a=[2,4,8,6,5,123]
print(a)
print(type(a))	#to see the type of the variable
b=bytes(a)	#to convert to a list a to bytes using 'bytes()'
print(type(b))	#to see the type of the variable
print(b)
print(b[1])
print(b[0:1])
print(b[0:5])
b[1]	#will generate an error 'object does not support item assinment'
print(b)

III). bytesarray datatype
is same as bytes datatype, with only one differnce that the value can be updates
a=[2,4,8,6,5,123]
print(a)
b=bytearray(a)
print(b[1])
print(b)
b[1]=8
print(b[1])
print(b[2])
print(type(b))

IV). list datatype
a=['atmiya','rajkot',22,22.3,-3.22]
print(a)
print(a[0])
print(a[0:4])
print(a[-1])
print(a*2)
a[1]='gujarat'
print(a)
print(type(a))

V). tuple datatype
a=('atmiya','rajkot',22,22.3,-3.22)
print(a)
print(a[0])
print(a[0:4])
print(a[-1])
print(a*2)
a[1]='gujarat'
print(a)
print(type(a))

VI). range datatype
a=range(8)	#8 is not includede [0-7]
print(a)
for i in a:
	print(i)
a=list(range(8))
print(a)
print(a[0])

(4) Sets
I). set datatype
a={7,16,43,25,34,43}
print(a)
a=set('Atmiya')
print(a)
a=set('AAtmiya')
print(a)

Converting a list into set
lst=[2,3,4,5,8,6,6,87]
print(type(lst))
a=set(lst)
print(type(a))
print(a)
Inserting the new value in exiting set the using 'update()'
a.update([9])
print(a)

Remove the elements form the exiting set using 'remove()'
a.remove(9)
print(a)

II). frozenset datatype
a={7,16,43,25,34,43}
print(a)
print(type(a))

Converting set into frozenset
b=frozenset(a)
print(b)
print(type(b))

(6) Mapping types (Dictionary)
Creating the dictionary
Syntax:
name_of_dictionary={key1:value1,key2:value2,key_n:value_n}
a={1:'abc',2:'cde',3:'efg',4:'ghi',5:'ijk'}
print(a)

We can create a empty dictionary
b={}
print(b)
b[1]='abc'
b[2]='cde'
b[3]='efg'
b[4]='ghi'
b[5]='ijk'
print(b)

We can retrieve value using key
print(b[3])

Retrieving all the keys 
print(b.keys())

Retrieving all the values
print(b.values())

Updating the v values of the particular key
b[1]='xyz'
print(b)

Deleting the key value pair
del b[1]
print(b)

The print statemant
print()

The print('string') statement
print('Atmiya')	#single quote (' ') and (" ") are same
print('This is the \n new line')
print('This is the \t new line')

Using the '+' oparetor
print('I live in ' + 'Rajkot')

The print(variable list) statement
a=7
b=16
print(a)
print(b)
a,b=7,16
print(a,b)
print(a,b,sep=',')
print('Atmiya')
print('University')
print('Rajkot')

If we want the output to print on the same line we can use 'end' attribute 
print('Atmiya',end='')
print('University',end='')
print('Rajkot')

Using \t
print('Atmiya',end='\t')
print('University',end='')
print('Rajkot')

Using print('string',variable list) statement
a=7
print(a,'The value is printed here')
print('User has entered',a,'as an input')

EXTRA EXCERSICE(WORK)
Operator
(1) Arithmetic operator
Symbol: +,-,,/,%,* and //
a=10
b=2
print('Arithmetic operator')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

(2) Assignment operator
Symbol: +=,-=,=,/=,%=,*= and //=
a=10
b=2
print('Assignment operator')
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)
a**=b
print(a)
a//=b
print(a)

(3) Unary mins operator
print('Unary mins operator')
a=1
print(-a)
a=-1
print(-a)

(4) Relational operator
Symbol: <,>,<=,>=,== and !=
a=16
b=2
print('Relational operator')
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

(5) Logical operator
Symbol: and,or,not
a=200
b=250
print('Logical operator')
print(a and b)
print(a or b)
print(not b)

a=200
b=0
print('Logical operator')
print(a and b)
print(a or b)
print(not b)

a=0
b=250
print('Logical operator')
print(a and b)
print(a or b)
print(not b)

(6) Boolean Operator
Symbol: and, or and not
a=True
b=False
print('Boolean Operator')
print(a and b)

a=False
b=True
print(a and b)

a=True
b=True
print(a and b)

a=False
b=False
print(a and b)

a=True
b=False
print('Boolean Operator')
print(a or b)

a=False
b=True
print(a or b)

a=True
b=True
print(a or b)

a=False
b=False
print(a or b)

a=True
b=False
print('Boolean Operator')
print(not b)

a=False
b=True
print(not a)

a=True
b=True
print(not b)

a=False
b=False
print(not a)

(7) Membership Operator
Symbol: in,not in
flower=("Mogra","Rose","Sunflower")
print("Mogra" in flower)
print("mogra" in flower)
print("Mogra" not in flower)
print("mogra" not in flower)

(8) Identity Operator

(9) Bitwise Operators
i)   Bitwise AND Operator 
ii)  Bitwise OR Operator 
iii) Bitwise XOR Operator 
iv)  Bitwise NOT Operator 

i)	Bitwise AND Operator
It returns 1, if both bits are 1, else 0.
a=28
b=19
print(a & b) 

ii) Bitwise OR Operator
It returns 0, if both bits are 1, else 1.
a=28
b=19
print(a | b) 

iii) Bitwise XOR Operator
Returns 1, if both bits are different, otherwise 0.
a=28
b=19
print(a ^ b)  

iv) Bitwise NOT Operator
It works on one operand.
It does 2s complement.
a=28
print(~a) 

The print(formatted string) statement
To display single integer value
a=7
print('The value of a is %i'%a)

To display more than one integer
a,b=7,16
print('a=%i b=%i'%(a,b))

Working with string using print()
uni='Atmiya'
print('Hi %s'%uni)
print('Hi %20s'%uni)
print('Hi %-20s'%uni)

Working with character using print()
We can use %c to display the single character from the string
uni='Atmiya'
print('The 1st character is %c, The 2nd character is %c'%(uni[0],uni[1]))

Working with the floating value
a=123.21
print('The number is %f'%a)
print('The number is %8.2f'%a)

Inside the formatted string
a,b,c=10,20,30
print('The number is {0}, The number is {1} and The number is {2}'.format(a,b,c))
print('The number is {0}, The number is {1} and The number is {2}'.format(c,b,a))


a='WELCOME TO ATMIYA UNIVERSITY'
print(a)
print(a[0])
print(a[0:7])
print(a[11:17])
print(a[11:])
print(a[-13:-12])
print(a[-13:])
print(a[-13:-3])

a=[2,4,8,6,5,123]
print(a)
print(type(a))
b=bytes(a)
print(b)
print(b[1])
print(b[0:1])

a=[2,4,8,6,5,123]
print(a)
b=bytearray(a)
print(b[1])
print(b)
b[1]=10
print(b[1:3])
print(type(b))
print(b)

Input statement
Input() takes a value from the keyboard and returns it as a string
a=input()		#OUTPUT:7
print(a)			   #7
# a=input('Enter your name: ')	#OUTPUT:utam
print(a)								   #utam

Restricting the user to enter the integer value only
num=input('Enter any integer number: ')		#OUTPUT:Enter any integer number: abc
print(num)														#abc
num=int(input('Enter any integer number: '))
print(num)	#output: abc -> invalid literal for int() with base 10: 'abc'
				OUTPUT:Enter any integer number: abc
						abc											
num=int(input('Enter any integer number: '))		#OUTPUT:Enter any integer number: 7
print(num)												#7
num=float(input('Enter any float number: '))
print(num)	#output: 11 -> it will be converted to 11.0
				OUTPUT:Enter any float number: 11
					    11.0
Storing only the 1st character from the string
character=input('Enter the string: ')
print(character)	#OUTPUT:Enter the string: utam
					        #utam

character=input('Enter the string: ')[0]
print(character)	#OUTPUT:Enter the string: utam
						   u
character=input('Enter the string: ')[3]
print(character)	#OUTPUT:Enter the string: utam
						   #m

Finding sum and product of two integer numbers
a=int(input('Enter the value for a: '))				#OUTPUT:Enter the value for a: 12
b=int(input('Enter the value for b: '))				#Enter the value for b: 13
print('The sum of {0} and {1} is {2}'.format(a,b,a+b))		#The sum of 12 and 13 is 25
print('The product of {0} and {1} is {2}'.format(a,b,a*b))		#The product of 12 and 13 is 156		

Use of split()
By default the entered numbers are considered and accepted as string
These strings are divided wherever a space is found by split()
These strings are read by for loop and converted into integers using int()

Accepting 3 values from from the user and printing it using split()
n1,n2,n3=[int(no) for no in input('Enter three numbers by living space in between: ').split()]
print(n1,n2,n3)		#OUTPUT:Enter three numbers by living space in between: 13 25 31
							13 25 31

Take 3 integer values from the user and return sum of it
n1,n2,n3=[int(no) for no in input('Enter three numbers by living space in between: ').split()]
print('The sum of three values: ',n1+n2+n3)		#OUTPUT:Enter three numbers by living space in between: 13 25 31
													The sum of three values:  69

Take group of strings
a=[a for a in input('Enter strings: ').split(',')]
print(a)	#OUTPUT: Enter strings: utam,shyam
					['utam', 'shyam']

Use of eval()
a=16
b=7
ans=eval('a/b')
print(ans)

a=int(input('Enter the value of a: '))
b=int(input('Enter the value of b: '))
ex=eval(input('Enter the expression: '))
print(ex)
print('The result of the entered expression is: %d',%ex)

Command line argument
import sys
print(sys.argv)

Retriving the name of the file where code is written 
import sys
a=sys.argv
print('The file in which the code is written is: ',a[0])

Program to accept two value of user at command line and display the total
import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
sum=a+b
print('The sum of two values is: 'sum)

Giving values from command line and expression after execution
a=int(sys.argv[1])
b=int(sys.argv[2])
sum=eval(input('Enter the expression: '))
print('The sum of two values is: 'sum)

Using a while loop, make the program that accepts numeric values from the users until user press 0
Give the sum of all the inserted values
sum=0
num=int(input('Enter the number1: '))
while num != 0:
	sum=sum+num
	num=int(input('Enter the number2: '))
print('The sum of all entered number is: ',sum)

Using while loop display the table of 2
n=2
counter=1
print('The table of n is as follow: ')
while counter<=10:
	ans=n*counter
	print(n,'x',counter,'=',ans)
	counter=counter+1

Display even numbers between 1-10
a=2
while a>=1 and a<=10:
	print(a)
	a=a+2

Display odd numbers between 1-10
a=1
while a>=1 and a<=10:
	print(a)
	a=a+2

Ask user whether they want odd numbers or even numbers
n=int(input('Enter your choice: 1 for odd numbers and 2 for even numbers: '))
if n==1:
	print('ALl the odd numbers between 1-10 are as follow:')
	while n>=1 and n<=10:
		print(n)
		n=n+2
elif n==2:
	print('ALl the even numbers between 1-10 are as follow:')
	while n>=1 and n<=10:
		print(n)
		n=n+2

Display numbers and their associated square
n=1
while(n<=10):
	print(n,'\t',n**2)
	n=n+1

Display numbers and their associated cube
n=1
while(n<=10):
	print(n,'\t',n**3)
	n=n+1

To find only even numbers from the list
lst=[4,9,6,7,7,8,1,2]
a=0
while(a<len(lst)):
	if lst[a]%2==0:
		print(lst[a])
	a=a+1

Function of len()
a='Welcome to the lab'
print(len(a))

a='Rajkot'
b=0
while(b<len(a)):
	print(a[b])
	b=b+1

for loop
for loop can work with sequence like(string, tuple, list, range, etc...)
Syntax:
for var in sequence:
	statements

Printing all the elements of the string
a='Rajkot'
for char in a:
	print(char)

Same program as above with indexing
a='Rajkot'
b=len(a)
for t in range(b):
	print(a[t])

Program to display 1 to 10
for t in range(11):
	print(t)	#it will print 0 to 10, index starts with 0, formula n-1

Program to display 1 to 10
for t in range(1,11):
	print(t)

Syntax:
Range(start, end, jump)

Program to display even numbers between 1 to 10
for t in range(2,11,2):
	print(t)

Program to display odd numbers between 1 to 10
for t in range(1,11,2):
	print(t)

Display numbers in reverse order from 10 to 1
for t in range(10,0,-1):
	print(t)

Give the sum of all the elements of the list
sum=0
lst=[4,5,9,3,7,12]
for t in lst:
	print(t)
	sum=sum+t
print('The sum of all the elements of the list is:',sum)

Using the if..else statement with for loop
lst=[4,5,9,3,7,12]
for t in lst:
	print(t)
else:
	print('All the elements are printed here')

DATE: 19/02/2025
UNIT: 02
Array
Syntax:
array_name=array(type_code,[array_elements])
There are three ways to declare an array
1st method
import array
a=array.array('i',[2,3,8,6])
print(a)

2nd method
import array as ar
a=ar.array('i',[2,3,8,6])
print(a)

3rd method
from array import*
a=array('i',[2,3,8,6])
print(a)

Indexing and Slicing on arrays
index with start a 'zero'
from array import*
a=array('i',[2,3,8,6])
print(a)
n=len(a)
for i in range(n):
	print(a[i])

Indexing using for loop
from array import*
a=array('i',[2,3,8,6])
print(a)
n=len(a)
for i in range(n):
	print(a[i],end='')	

Indexing using while loop
from array import*
a=array('i',[2,3,8,6])
print(a)
n=len(a)
i=0
while i<n:
	print(a[i],end='')
	i=i+1

from array import*
a=array('d',[2.2,3.3,8.8,6])
print(a)

from array import*
a=array('u',['a','b','c'])
print(a)

DATE: 20/02/2025()
Indexing and Slicing on arrays
Slicing
Use to retrieve range of elements
The fromat is: array_name[start:stop:stride]
Out of the format we can eliminate one or two from the parameters
from array import*
a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t'])
b=a[0:13]
print(b)
b=a[0:]
print(b)
b=a[:13]
print(b)
b=a[0:5]
print(b)
b=a[6:9]
print(b)
b=a[-13:]
print(b)
b=a[-13:-7]
print(b)
b=a[0:13:2]
print(b)

Slicing using for loop
from array import*
a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t'])
for i in a[0:16]:
	print(i)

from array import*
a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t'])
for i in a[0:16]:
	print(i,end=' ')

Processing the arrays / array methods
from array import*
a=array('i',[2,3,8,6,7,9])
print(a)

Appending the element into the array
a.append(10)
print(a)

Inserting the element at the desired position
a.insert(0,0)
a.insert(0,11)
print(a)

Removing the element
a.remove(6)
print(a)

Removing the last element
b=a.pop()
print('Poped element was',b)
print(a)

Finding the position of an element
b=a.index(7)
print('The element 7 is found at the position: ',b)

Converting array to list
lst=a.tolist()
print('Elements of list are: ',lst)
print('Elements of array are: ',a)

Take marks of students in the array, give the total of scored marks
from array import* 
a=input('Enter your marks: ').split(',')
marks=[int(number)for number in a]
total=0
for i in marks:
	print(i)
	total=total+i
print('The total of all marks is: ',total)

Take marks of students in the array, give the total of scored marks and percentage
from array import* 
a=input('Enter your marks: ').split(',')
marks=[int(number)for number in a]
total=0
for i in marks:
	print(i)
	total=total+i
print('The total of all marks is: ',total)
l=len(marks)
percentage=total/l
print('The percentage of the students is: ',percentage)

Types of array
(1) Single dimensioal array
(2) Multi dimensional array

1st way to declare an array
import numpy 
a=numpy.array([2,8,9,6,3])
print(a)		#OUTPUT:

2nd way to declare an array
import numpy as nu
a=nu.array([2,8,9,6,3])
print(a)		#OUTPUT:

3rd way to declare an array
from numpy import*
a=array([2,8,9,6,3])
print(a)		#OUTPUT:

It can also create array of other types
from numpy import*
a=array(['rose','lotus','mogra'])
print(a)		#OUTPUT:

Creating an array using linespace() 
Syntax:
linespace(start,stop,n)
start - The starting element
stop - The ending element
n - No. of parts elements should be divided(default 50)
from numpy import*
arr=linespace(1,10,5)
print(arr)	#OUTPUT:

Creating an array using arange() 
Syntax:
arange(start,stop,stepsize)
from numpy import*
arr=linespace(1,10,3)
print(arr)		#OUTPUT:

Operations on array
from numpy import*
a=array([10,20,30,40,50])
print(a)		#OUTPUT:
print('The answer: ',a+5)		#OUTPUT:
print('The answer: ',a-5)		#OUTPUT:
print('The answer: ',a*5)		#OUTPUT:
print('The answer: ',a/5)		#OUTPUT:
print('The answer: ',sum(a))		#OUTPUT:
print('The answer: ',max(a))		#OUTPUT:
print('The answer: ',min(a))		#OUTPUT:
print('The answer: ',mean(a))		#OUTPUT:

Using where()
Syntax:
where(comparison_condition,expression1,expression2)
from numpy import*
a1=array([1,2,3,14,5])
a2=([10,2,3,4,15])
a3=where(a2=a1,a2,a1)
print(a1)		#OUTPUT:
print(a2)		#OUTPUT:
print(a3)		#OUTPUT:

Using nonzero()
it returns the index of all non-zero elements
from numpy import*
a1=array([1,2,0,4,5])
a2=nonzero(a1)
print(a1)		#OUTPUT:
print(a2)		#OUTPUT:

Using view
from numpy import*
a1=array([1,2,0,4,5])
a2=a1.view()
print(a1)		#OUTPUT:[1 2 0 4 5]
print(a2)		#OUTPUT:[1 2 0 4 5]
a1[3]=40
print(a1)		#OUTPUT:[ 1  2  0 40  5]
print(a2)		#OUTPUT:[ 1  2  0 40  5]

Using copy()
from numpy import*
a1=array([1,2,0,4,5])
a2=a1.copy()
print(a1)		#OUTPUT:[1 2 0 4 5]
print(a2)		#OUTPUT:[1 2 0 4 5]
a1[3]=40
print(a1)		#OUTPUT:[ 1  2  0 40  5]
print(a2)		#OUTPUT:[1 2 0 4 5]

Slicing and indexing in numpy array
Slicing
Syntax:
array_name(start:stop:stepsize)
from numpy import*
a1=array([1,2,0,4,5])
print(a1[0:5])	    #OUTPUT:[1 2 0 4 5]
print(a1[:])		#OUTPUT:[1 2 0 4 5]
print(a1[::])		#OUTPUT:[1 2 0 4 5]
print(a1[1::2])		#OUTPUT:[2 4]

indexing
from numpy import*
a1=array([1,2,0,4,5])
i=0
while(i<len(a1-1)):
	print(a1[i])		#OUTPUT:1
	i=i+1					   #2
							   0
							   4
							   5

Attributes of an array
(1) ndim attribute
return 1 if array is single dimension, return 2 if the array is multi dimension
from numpy import*
a1=array([[1,2,0,4,5],[2,4,9,7,8],[2,6,10,8,5]])
print(a1.ndim)	#OUTPUT:2

(2) shape attribute
returns numbers of elements in case of single dimension, and in multidimension return dimensions of array
from numpy import*
a1=array([1,2,0,4,5])
print(a1.shape)		#OUTPUT:(5,)
a2=array([[1,2,0,4,5],[2,6,8,7,9],[3,1,0,4,2]])
print(a2.shape)	  #OUTPUT:(3, 5)

(3) size attribute
returns numbers of elements 
from numpy import*
a1=array([1,2,0,4,5]) 
print(a1.size)	  #OUTPUT:5
a2=array([[1,2,0,4,5],[2,4,9,7,8],[3,5,7,2,1]])
print(a2.size)	  #OUTPUT:15

(4) datatype attribute
return the datatype of an array
from numpy import*
a1=array([1,2,0,4,5])
print(a1.dtype)	   #OUTPUT:int64

Reshape Method
Syntax:
array_name.reshape(n,r,c)
from numpy import*
a1=array([1,2,0,4,5,7,6,4,9])
a2=a1.reshape(3,3)
print(a1)		#OUTPUT:[1 2 0 4 5 7 6 4 9]
print(a2)		#OUTPUT:[[1 2 0]
 					  [4 5 7]
 					  [6 4 9]]

from numpy import*
a1=array([1,2,0,4,5,6,7,4,9])
a2=a1.reshape(1,3,3)
print(a1)	#OUTPUT:[1 2 0 4 5 6 7 4 9]
print(a2)	#OUTPUT:[[[1 2 0]
  					[4 5 6]
 					[7 4 9]]]

Date: 28/02/25

Working with string
str1='Welcome to India, the New edge country'
str2="Welcome to India, the New edge country"
str3='Welcome to India, the "New edge" country'
str4='Welcome to \tIndia, \nthe "New edge" country'
str5=r'Welcome to \tIndia, \nthe "New edge" country'
print(str1)		#OUTPUT:
print(str2)		#OUTPUT:
print(str3)		#OUTPUT:
print(str4)		#OUTPUT:
print(str5)		#OUTPUT:
print(len(str1))		#OUTPUT:
 
OUTPUT:
Welcome to India, the New edge country
Welcome to India, the New edge country
Welcome to India, the "New edge" country
Welcome to 	India, 
the "New edge" country
Welcome to \tIndia, \nthe "New edge" country
38

s1='Rajkot'
s2='Gujarat'
s=s1+s2
print(s)		#OUTPUT:
string1='Rajkot Gujarat'
print(string1)		#OUTPUT:
size=len(string1)
i=0
while i<size:
    print(string1[i],end='')		#OUTPUT:
    i=i+1

OUTPUT:
RajkotGujarat
Rajkot Gujarat
Rajkot Gujarat

Display the entered string in the reverse order
Using while loop
string1='Rajkot Gujarat'
print(string1)	#OUTPUT:
size=len(string1)
i=1
while i<=size:
    print(string1[-i],end='')		#OUTPUT:
    i=i+1

OUTPUT:
Rajkot Gujarat
tarajuG tokjaR

Using the loop
string1='Rajkot Gujarat'
for i in string1[::-1]:
    print(i,end='')		#OUTPUT:

OUTPUT:
tarajuG tokjaR

Slicing the string
string1='Rajkot Gujarat'
print(string1[0:14:1])		#OUTPUT:
print(string1[::])		#OUTPUT:
print(string1[:])		#OUTPUT:
print(string1[0:14:2])		#OUTPUT:
print(string1[::-1])		#OUTPUT:

OUTPUT:
Rajkot Gujarat
Rajkot Gujarat
Rajkot Gujarat
Rjo uaa
tarajuG tokjaR

Allow user to enter the string, allow user to enter substring, find whether the substring exit in thge string or not
string1=input('Enter the string: ')		#OUTPUT:
substring=input('Enter the sub-string: ')		#OUTPUT:
if substring in string1:
    print(substring,'is found in the string')		#OUTPUT:
else:
    print(substring,'not found in the string')		#OUTPUT:

OUTPUT:
Enter the string: Welcome to my class
Enter the sub-string: lab
lab not found in the string 

Check whether entered string is palindrom or not 
string1=input('Enter the string: ')
string2=(string1[::-1])
if (string1==string2):
    print('The entered string is palindrome')		#OUTPUT:
else:
    print('The entered string is not Palindrome')		#OUTPUT:

OUTPUT:
Enter the string: racecar
The entered string is palindrome 

Counting the substring in a string
Format:
string_name.count(substring,beg(start),end)
Counting the substring in the string in range
string1= 'India the New edge country'
num_count=string1.count('New',0,9)
print (num_count)		#OUTPUT:
OUTPUT:
0

Counting the substring in the whole string
string1= 'India the New edge country'
num_count=string1.count('New')
print(num_count)		#OUTPUT:
OUTPUT:
1

Replacing the string with the new one
string1= 'Hello there'
str1='there'
str2='world'
print(string1)		#OUTPUT:
new_string=string1.replace(str1,str2)
print(new_string)		#OUTPUT:

OUTPUT:
Hello there
Hello world 

Changing the case of a string
string1='Your future is bright'
print(string1)		#OUTPUT:
print(string1.lower())		#OUTPUT:
print(string1.upper())		#OUTPUT:
print(string1.swapcase())		#OUTPUT:
print(string1.title())	#OUTPUT:

OUTPUT:
Your future is bright
your future is bright
YOUR FUTURE IS BRIGHT
yOUR FUTURE IS BRIGHT
Your Future Is Bright

String testing methods
aadhar=input('Enter your AADHAAR Number: ')
if aadhar.isdigit()==True:
    print('Your AADHAAR Number is accepted.')		#OUTPUT:
else:
    print('Enter valid AADHAAR Number')		#OUTPUT:

OUTPUT:
Enter your AADHAAR Number: 123556789999
Your AADHAAR Number is accepted.

Allow user to enter string, display the entered string in a sorted order
string1=[]
number=int(input('How many strings you want to enter? : '))		#OUTPUT:
for i in range(number):
    print('Enter the string: ',end='')		#OUTPUT:
												OUTPUT:
    string1.append(input())
print(string1)		#OUTPUT:
string=string1.sort()
print(string)		#OUTPUT:
for i in string1:
    print(i,end=',')		#OUTPUT:

OUTPUT:
How many strings you want to enter? : 2
Enter the string: utam
Enter the string: niketan
['utam', 'niketan']
None
niketan,utam,

Allow user to enter string and search the string within, return the position of the searched subtring
string1=[]
number=int(input('How many strings you want to enter? : '))		#OUTPUT:
for i in range(number):
    print('Enter the string: ',end='')		#OUTPUT:
												OUTPUT:
    string1.append(input())
print(string1)		#OUTPUT:
sub_str=input('Enter the string to be searched: ')
temp=False 
for i in range(len(string1)):
    if sub_str==string1[i]:
        print('The searched string is found at the',i+1,'position')		#OUTPUT:
        temp=True
if temp==False:
    print('The searched string is not found.')		#OUTPUT:

OUTPUT:-
How many strings you want to enter? : 2
Enter the string: utam
Enter the string: niketan
['utam', 'niketan']
Enter the string to be searched: niketan
The searched string is found at the 2 position 



Date: 03/03/25[Monday]

Working with Characters
string1='India'
print(string1)	#OUTPUT:
print(type(string1))		#OUTPUT:
character=string1[0]
print(character)		#OUTPUT:
print(type(character))		#OUTPUT:
character=string1[3]
print(character)		#OUTPUT:
character=string1[0:3]
print(character)		#OUTPUT:
character=string1[2]
print(character)		#OUTPUT:

OUTPUT:
India
<class 'str'>
I
<class 'str'>
i
Ind
d

String testing methods ()
1. isalnum()
2. isupper()
3. islower ()
4. isalpha()
5. isdigit()

Accept character from the user, check whether the entered character is string, upper case or lower case
string1=input('Enter the character: ')		#OUTPUT:
character=string1[0]
if character.isalpha():
    print('User has entered in alphabet.')		#OUTPUT:
    if character.isupper():
        print('User has entered an alphabet in upper case.')		#OUTPUT:
    else:
        print('User has entered an alphabet in lower case.')		
else:
    print('User has either entered the number or the special character.')

OUTPUT:
Enter the character: Utam
User has entered in alphabet.
User has entered an alphabet in upper case.

Working with List
Create the list using range()
Range 
Syntax:
range(start,stop, stepsize)
list1=range(10)
for i in list1:
    print(i,end=' ')		#OUTPUT:

OUTPUT:
0 1 2 3 4 5 6 7 8 9
    
list1=range(1,11)
for i in list1:
    print(i,end=' ')		#OUTPUT:
OUTPUT:
1 2 3 4 5 6 7 8 9 10

Store even numbers in the range of 1-10
list1=range(2,11,2)
for i in list1:
    print(i,end=' ')		#OUTPUT:

OUTPUT:
2 4 6 8 10 

Appending the list
list1=range(1,11)
for i in list1:
    print(i,end=' ')		#OUTPUT:
lst=list(list1)
lst.append(11)
print(lst)		#OUTPUT:

OUTPUT:
1 2 3 4 5 6 7 8 9 10
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Updating the list using the index
lst[2]=20
print(lst)	#OUTPUT:

OUTPUT:
[1, 2, 20, 4, 5, 6, 7, 8, 9, 10, 11]

Delete using index/positing 
del lst[2]
print(lst)	#OUTPUT:

OUTPUT:
[1, 2, 4, 5, 6, 7, 8, 9, 10, 11]

Deleting by value
lst.remove(4)
print(lst)	#OUTPUT:

OUTPUT:
[1, 2, 5, 6, 7, 8, 9, 10, 11]

Knowing the index of an element 
ind=lst.index(2)
print(ind)	#OUTPUT:

OUTPUT:
1

Finding the length of a list
size=len(lst)
print(size)	 #OUTPUT:

OUTPUT:
9

Clearing the list
lst.clear()
print(lst)	#OUTPUT:

OUTPUT:
[ ]

Display elements of the list in the reverse order
list1=['Kalawad road','Rajkot','Gujarat','India']
reverse_ord=list1.reverse()
print(list1)		#OUTPUT:

OUTPUT:
['India', 'Gujarat', 'Rajkot', 'Kalawad road']

Concatinating the list
list1=['Gujarat','Maharashtra','Madhya Pradesh']
list2=['Gandhinagar','Mumbai','Bhopal']
list3=list1+list2
print(list3)		#OUTPUT:

OUTPUT:
['Gujarat', 'Maharashtra', 'Madhya Pradesh', 'Gandhinagar', 'Mumbai', 'Bhopal']

Using the membership operator in list
list1=[10,20,30,40,50,60]
no1=22
no2=20
print(no1 in list1)		#OUTPUT:
print(no1 not in list1)	#OUTPUT:
print(no2 in list1)		#OUTPUT:
print(no2 not in list1)	#OUTPUT:

OUTPUT:
False
True
True
False

Aliasing a list
list1=[10,20,30,40,50,60]
list2=list1
print(list1)		#OUTPUT:
print(list2)		#OUTPUT:
list2[4]=500
print(list1)		#OUTPUT:
print(list2)		#OUTPUT:

OUTPUT:
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 500, 60]
[10, 20, 30, 40, 500, 60]

Clone the list
list1=[10,20,30,40,50,60]
list2=list1[:]
print(list1)		#OUTPUT:
print(list2)		#OUTPUT:
list2[4]=500
print(list1)		#OUTPUT:
print(list2)		#OUTPUT:

OUTPUT:
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 500, 60]

Conting the elements in the list, take elements from the user, and search elements from the user
list1=[]
no=int(input('How many elements you want to entry?: '))		#OUTPUT:
for i in range(no):
	print('Please enter elements: ',end='')		#OUTPUT:
												OUTPUT:
	list1.append(int(input()))
print(list1)		#OUTPUT:
find_ele=int(input('Enter an element you want to count: '))		#OUTPUT:
count=0
for i in list1:
	if find_ele==i:
		count=count+1
print('The element you want to count was found ',count,'time(s)')		#OUTPUT:

OUTPUT:
How many elements you want to entry?: 2
Please enter elements: 25
Please enter elements: 15
[25, 15]
Enter an element you want to count: 25
The element you want to count was found  1 time(s)

Finding common elements from two lists.
list1=[2,3,4,8,7,9]
list2=[2,30,4,80,7,9]
print(list1)		#OUTPUT:
print(list2)		#OUTPUT:

OUTPUT:
[2, 3, 4, 8, 7, 9]
[2, 30, 4, 80, 7, 9]

There is no direct way to compare the list.
So we need to convert list in to set.
set1=set(list1)
set2=set(list2)
print(set1)		#OUTPUT:
print(set2)		#OUTPUT:
set3=set1.intersection(set2)
print(set3)		#OUTPUT:
list3=list(set3)
print(list3)		#OUTPUT:

OUTPUT:
{2, 3, 4, 7, 8, 9}
{2, 4, 7, 9, 80, 30}
{9, 2, 4, 7}
[9,2,4,7]