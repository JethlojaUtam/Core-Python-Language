UNIT-02

STATEMENTS...
i)if statement
ii)if..else statement
iii)if..elif..else statement
iv)nested if statement

i)if Statement
Syntax:
		if condition:
			statemnets
a=7
if a==7:
	print('The enterd value is 7')

a=7
if a>0:
	print('The enterd value is positive')

a='Atmiya'
if a=='Atmiya':
	print('Welcome to Atmiya')
	print('You are in Rajkot')

a=7
b=16
if a<b:
	print('The value b is greater than a')

a=int(input('Enter the price of product: '))
b=int(input('Enter the quantity you want to purchase: '))
bill=a*b
if bill<1000:
	print('We cannot deliver your goods')
print(bill)

ii)if..else statement
Syntax:
		if condition:
			statements
		else:
			statements
a=int(input('Enter the integer value: '))
if a%2==0:
	print('The entered number is even')
else:
	print('The entered number is odd')

a=int(input('Enter the integer valur: '))
if a>0:
	print('The enterd number is positive')
else:
	print('The enterd number is negative')

Quantity, price(bill>500)%10 using if..else statement
qty=int(input('Enter your quantity: '))
price=int(input('Enter your price: '))
total=qty*price
if total>500:
	discount=total*10/100
	final_cost=total-discount
	print('You have saved: ',discount)
	print('You have payed: ',final_cost)
else:
	print('You have payed: ',total)
	print('Total cost is too law to apply any discount please purchese more than 10 ruppes')

Write a program two values from user input and minimun number find using if..else statement
a=int(input('Enter the value of a: '))
b=int(input('Enter the value of b: '))
if a<b:
	print('a is minimum: ',a)
else:
	print('b is minimum: ',b)

Write a program two values from user input and maximum number find using if..else statement
a=int(input('Enter the value of a: '))
b=int(input('Enter the value of b: '))
if a>b:
	print('a is miximum: ',a)
else:
	print('b is miximum: ',b)

iii)if..elif..else statement
Syntax:
		if condition:1
			statements
		elif condition:2
			statements
		elif condition:3
		  statements
		else:
			statements

To konw if given number is positive,nagetive, or zero
a=int(input('Enter the number: '))
if a>0:
	print('Enter number is positive')
elif a==0:
	print("Enter number is zero")
else:
	print('Enter number is negative')

To know if given number enterd in words
num=int(input('Enter your number: '))
if num==0:
	print('Enterd number is zero')
elif num==1:
	print('Enterd number is one')
elif num==2:
	print('Enterd number is two')
elif num==3:
	print('Enterd number is three')
else:
	print('Please Enterd number is 0, 1, 2, and 3')

Order between 1000 and 1200=10%, 1201 and 1500=15% and above=20%
amt=int(input('Enter the amount: '))
if amt<=0:
	print('Bill amount cannot less than 1')
elif amt<=999:
	print('Please purchase more to 1 rupees available discount')
elif amt>=1000 and amt<=1200:
	discount1=amt*(10/100)
	print('You will get 10% purchase discount: ',discount1)
elif amt>=1201 and amt<=1500:
	discount2=amt*(15/100)
	print('You will get 15% purchase discount: ',discount2)
elif amt>=1501:
	discount3=amt*(20/100)
	print('You will get 20% purchase discount: ',discount3)

Write a program four values from user input and maximum number find using if..elif..else statement
number1=int(input('Enter the value1: '))
number2=int(input('Enter the value2: '))
number3=int(input('Enter the value3: '))
number4=int(input('Enter the value4: '))
if number1>number2 and number1>number3 and number1>number4:
	print('Enterd the value1 is maximum: ',number1)
elif number2>number1 and number2>number3 and number2>number4:
	print('Enterd the value2 is maximum: ',number2)
elif number3>number1 and number3>number2 and number3>number4:
	print('Enterd the value3 is maximum: ',number3)
else:
	print('Enterd the value4 is maximum: ',number4)

Write a program four values from user input and minimum number find using if..elif..else statement	
number1=int(input('Enter the value1: '))
number2=int(input('Enter the value2: '))
number3=int(input('Enter the value3: '))
number4=int(input('Enter the value4: '))
if number1<number2 and number1<number3 and number1<number4:
	print('Enterd the value1 is manimum: ',number1)
elif number2<number1 and number2<number3 and number2<number4:
	print('Enterd the value2 is manimum: ',number2)
elif number3<number1 and number3<number2 and number3<number4:
	print('Enterd the value3 is manimum: ',number3)
else:
	print('Enterd the value4 is manimum: ',number4)

iv)nested if statement
Syntax:
		if condition:1
			statements
			if condition:2
				statements
			elif condition:3
				statements
			else:
				statements
		else:
			statements
a=80
b=40
c=90
d=100
if a>b:
	if a>c:
		if a>d:
			print('a is biggest')
if b>a:
	if b>c:
		if b>d:
			print('b is biggest')
if c>a:
	if c>b:
		if c>d:
			print('c is biggest')
if d>a:
	if d>b:
		if d>c:
			print('b is biggest')

Write a program student mark
i) mark<50(re-uppear the exam)
ii) mark>=50 and mark<60(you have passed the exam)
iii) mark>=60 and mark<70(you have passed the exam with first class)
iv) mark>=70 and mark<80(you have passed the exam with distiction)
v) mark>=80 and mark<=100(you have passed the exam with honors's)
using the if.elif..else statement other else('Please enter valid mark')
mark=int(input('Enter the mark: '))
if mark<50:
	print('Re-uppear the exam')
elif mark>=50 and mark<60:
	print('You have passed the exam')
elif mark>=60 and mark<70:
	print('You have passed the exam with first class')
elif mark>=70 and mark<80:
	print('You have passed the exam with distiction')
elif mark>=80 and mark<=100:
	print('You have passed the exam with honors')
else:
	print('Please enter valid mark...')

LOOPING...
i)while loop
ii)for loop
iii)d0..while loop
iv)nested loop

i)while loop
Write a program 1 to 10 even numbers using while loop
a=2
while a>=1 and a<=10:
	print(a)
	a=a+2
print('While loop 1 to 10 even numbers ended')

Display odd numbers between 1 to 10
a=1
while a>=1 and a<=10:
	print(a)
	a=a+2
print('While loop 1 to 10 odd numbers ended')

Ask user whether they want odd numbers or even numbers
n=int(input('Enter your choice:1 for odd numbers and 2 for even numbers: '))
if n==1:
	print('All the odd numbers between 1 to 10 are as follow: ')
	while n>=1 and n<=10:
		print(n)
		n=n+2
elif n==2:
	print('All the even numbers between 1 to 10 are as follow: ')
	while n>=1 and n<=10:
		print(n)
		n=n+2

Using a while loop, make the program that accepts numeric values from the users until user press 0
Give the sum of all the inserted values
sum1=0
num=int(input('Enter the number1: '))
while num!=0:
	sum1=sum1+num
	num=int(input('Enter the number2: '))
print('The sum of all entered number is: ',sum1)

Using while loop display the table of 2
n=2
counter=1
print('The table of n is as follow: ')
while counter<=10:
	ans=n*counter
	print(n,'x',counter,'=',ans) 
	counter=counter+1

Display numbers and their associated square
n=1
print('Square of 1 to 10 is:')
while n<=10:
	print(n,'=>',n**2)
	n=n+1

n=1
while(n<=10):
	print(n,'\t',n**2)
	n=n+1

Display numbers and their associated cube
n=1
print('Cube of 1 to 10 is:')
while n<=10:
	print(n,'=>',n**3)
	n=n+1

n=1
while(n<=10):
	print(n,'\t',n**3)
	n=n+1

To find the only even numbers from the list
lst=[4,9,6,7,7,8,1,2]
a=0
while a<len(lst):
	if lst[a]%2==0:
		print(lst[a])
	a=a+1

Function of len()
len1='Welcome to Atmiya University'
print(len(len1))

len1='Welcome to the lab'
print(len(len1))

len1='Rajkot'
b=0
while b<len(len1):
	print(len1)
	b=b+1

len1='Rajkot'
b=0
while b<len(len1):
	print(len1[b])
	b=b+1

ii)for loop
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
	print(b)
	print(a)

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
print('The sum of all the elements of the list is: ',sum)

Using the if..else statement with for loop
lst=[4,5,9,3,7,12]
for t in lst:
	print(t)
else:
	print('All the elements are printed here')