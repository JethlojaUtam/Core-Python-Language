PRACTICE-01

USING SIMPLE METHOD(USING INPUT)
(1) Write a program that prints your name and your college name.
name=input('Enter your name: ')		#OUTPUT:Enter your name:Utam
collagename=input('Enter your collage name: ')		#OUTPUT:Enter your collage:Atmiya University
print(name)		#OUTPUT:Utam
print(collagename)		#OUTPUT:Atmiya University

(2) Write a program that prints your address with name, all in new lines.
name=input('Enter your name: ')		#OUTPUT:Enter your name:Utam
add=input('Enter your address: ')	#OUTPUT:Enter your address:Shivpur
print(name)		#OUTPUT:Utam
print(add)		#OUTPUT:Shivpur

(3) Write a program that accept two numbers and perform all basic mathematical operations.
a=int(input('Enter the value of a: '))		#OUTPUT:Enter the value of a: 20
b=int(input('Enter the vlaue of b: '))		#OUTPUT:Enter the value of a: 4
print(a+b)		#OUTPUT:24
print(a-b)		#OUTPUT:16
print(a*b)		#OUTPUT:80
print(a/b)		#OUTPUT:5.0
print(a%b)		#OUTPUT:0
print(a**b)		#OUTPUT:160000
print(a//b)		#OUTPUT:5

(4) Write a program to calculate simple interest.
a=int(input('Enter the value of a: '))		#OUTPUT:Enter the value of a:10
print(a)	#OUTPUT:10
b=int(input('Enter the value of b: '))		#OUTPUT:Enter the value of b:20
print(b)	#OUTPUT:20
c=int(input('Enter the value of c: '))		#OUTPUT:Enter the value of c:30
print(c)	#OUTPUT:30
si=(a*b*c/100)		#OUTPUT:10*20*30/100
print(si)	#OUTPUT:60.0

(5) Write a program to calculate 10% bonus of salary.
salary=int(input('Enter the salary: '))		#OUTPUT:Enter the salary:50000	
print('Salary is: ',salary)		#OUTPUT:Salary is:50000
bonus=(salary*10/100)		
print('Bonus is: ',bonus)		#OUTPUT:Bonus is:5000.0
print('Your bonus of salary is: ',salary+bonus)		#OUTPUT:Your bonus of salary is:55000.0

(6) Write a program to convert KM into Meter.
km=int(input('Enter your Kilometer: '))		#OUTPUT:Enter the Kilometer:25
print(km)		#OUTPUT:25
meter=km*1000
print(meter)	#OUTPUT:25000

(7) The distance between two cities is input through keyboard. 
	  Write a program to convert and print this distance in feet, meter, inch and centimeter.
distance=float(input('Enter the distance between two cities is: '))		#OUTPUT:Enter the distance between two cities is:1	
print(distance)		#OUTPUT:1.0
feet=distance*3280.84
print(feet)		#OUTPUT:3280.84
meter=distance*1000
print(meter)	#OUTPUT:1000.0
inch=distance*39370.1
print(inch)		#OUTPUT:39370.1
centimeter=distance*100000
print(centimeter)		#OUTPUT:100000.0

USING .FORMAT
(1) Write a program that prints your name and your college name.
name=input('Enter your name: ')		#OUTPUT:Enter your name:Utam
collagename=input('Enter your collage name: ')		#OUTPUT:Enter your collage:Atmiya University
print('Your name is {0} and Your collage name is {1}'.format(name,collagename))		#OUTPUT:Your name is Utam and Your collage name is Atmiya University

(2) Write a program that prints your address with name, all in new lines.
name=input('Enter your name: ')		#OUTPUT:Enter your name:Utam
add=input('Enter your address: ')	#OUTPUT:Enter your address:Shivpur
print('Your name is {0} and Your address is {1}'.format(name,add))		#OUTPUT:Your name is Utam and Your address is Shivpur

(3) Write a program that accept two numbers and perform all basic mathematical operations.
a=int(input('Enter the value of a: '))		#OUTPUT:Enter the value of a: 20
b=int(input('Enter the vlaue of b: '))		#OUTPUT:Enter the value of a: 4
print('The sum of {0} and {1} is {2}'.format(a,b,a+b))		#OUTPUT:The sum of 20 and 4 is 24
print('The substraction of {0} and {1} is {2}'.format(a,b,a-b))		#OUTPUT:The substraction of 20 and 4 is 16
print('The multiplication of {0} and {1} is {2}'.format(a,b,a*b))		#OUTPUT:The multiplication of 20 and 4 is 80
print('The division of {0} and {1} is {2}'.format(a,b,a/b))		#OUTPUT:The division of 20 and 4 is 5.0
print('The modulo of {0} and {1} is {2}'.format(a,b,a%b))		#OUTPUT:The modulo of 20 and 4 is 0
print('The multi of multi of {0} and {1} is {2}'.format(a,b,a**b))		#OUTPUT:The multi of multi of 20 and 4 is 160000
print('The sum dived of dived {0} and {1} is {2}'.format(a,b,a//b))		#OUTPUT:The sum dived of dived 20 and 4 is 5

(4) Write a program to calculate simple interest.
a=int(input('Enter the value of a: '))		#OUTPUT:Enter the value of a:10
b=int(input('Enter the value of b: '))		#OUTPUT:Enter the value of b:20
c=int(input('Enter the value of c: '))		#OUTPUT:Enter the value of c:30
print('The simple intrest of {0},{1},{2} is {3}'.format(a,b,c,a*b*c/100))		#OUTPUT:The simple intrest of 10,20,30 is 60.0

(5) Write a program to calculate 10% bonus of salary.
salary=int(input('Enter the salary: '))		#OUTPUT:Enter the salary:50000	
bonus=(salary*10/100)		
print('Your salary is {0} and Your bonus is {1} in 10% bonus of salary is {2}'.format(salary,bonus,salary+bonus))		#OUTPUT:Your salary is 50000 and Your bonus is 5000.0 in 10% bonus of salary is 55000.0

(6) Write a program to convert KM into Meter.
km=int(input('Enter your Kilometer: '))		#OUTPUT:Enter the Kilometer:25
print('Your Km is {0} and Your meter is {1}'.format(km,km*1000))		#OUTPUT:Your Km is 1 and Your meter is 1000

(7) The distance between two cities is input through keyboard. 
	  Write a program to convert and print this distance in feet, meter, inch and centimeter.
distance=float(input('Enter the distance between two cities is: '))		#OUTPUT:Enter the distance between two cities is:1	
print(' Your km is {0}\n Your feet is {1}\n Your meter is {2}\n Your inch is {3}\n Your centimeter is {4}'.format(distance,distance*3280.84,distance*1000,distance*39370.1,distance*100000))		#OUTPUT:Your Km is 1 and Your meter is 1000
feet=distance*3280.84
meter=distance*1000
inch=distance*39370.1
centimeter=distance*100000

USING EVAL
(1) Write a program that prints your name and your college name.
name=input('Enter your name: ')
collagename=input('Enter your college name: ')
print(name)		#OUTPUT:
print(collagename)		#OUTPUT:

(2) Write a program that prints your address with name, all in new lines.
name=input('Enter your name: ')
print(name)		#OUTPUT:

add=input('Enter your Address: ')
print(name)
print('The result is: %d'%ex)		#OUTPUT:
print(add)	#OUTPUT:

(3) Write a program that accept two numbers and perform all basic mathematical operations.
n1=int(input('Enter the number1: '))
n2=int(input('Enter the number2: '))	
ex=eval(input('Enter the expression: '))
print('The result is: %d'%ex)		#OUTPUT:

(4) Write a program to calculate simple interest.
a=int(input('Enter the number a: '))		#OUTPUT:
b=int(input('Enter the number b: '))		#OUTPUT:
c=int(input('Enter the number c: '))		#OUTPUT:
sip=eval(input('Enter the expression: '))		#OUTPUT:
print('The result is :%d'%sip)		#OUTPUT:


(5) Write a program to calculate 10% bonus of salary.
salary=int(input('Enter your salary: '))		#OUTPUT:
print('Salary is: ',salary)		#OUTPUT:
bonus=eval(input('Enter the expression: '))		#OUTPUT:
print('Bonus is: %d'%bonus)		#OUTPUT:
print('Your bonus of salary is: ',salary+bonus)		#OUTPUT:

(6) Write a program to convert KM into Meter.
km=int(input('Enter kilometer: '))	#OUTPUT:
print(km)		#OUTPUT:
meter=eval(input('Enter expression: '))		#OUTPUT:
print('The result is:%d'%meter)		#OUTPUT:


(7) The distance between two cities is input through keyboard.
distance=float(input('Enter distance between two city: '))	#OUTPUT:
print(distance)		#OUTPUT:
feet=eval(input('Enter expression: '))	#OUTPUT:
print('the result is:%f'%feet)		#OUTPUT:

feet=distance*3280.84
meter=distance*1000
inch=distance*39370.1
centimeter=distance*100000

USING COMMAND-LINE
(1) Write a program that prints your name and your college name.
import sys
name=(sys.argv[1])
print('Your name: ',name)		#OUTPUT:
college=(sys.argv[2])
print('Your college name: ',college)		#OUTPUT:


(2) Write a program that prints your address with name, all in new lines.
import sys
name=(sys.argv[1])
print('Name is :',name)	  #OUTPUT:

Address=(sys.argv[2])
print('Address is :',Address)		#OUTPUT:

(3) Write a program that accept two numbers and perform all basic mathematical operations.
import sys
n1=int(sys.argv[1])
print('Number1 is: ',n1)	#OUTPUT:
n2=int(sys.argv[2])
print('Number2 is: ',n2)	#OUTPUT:
sum=n1+n2
print('Addition is: ',sum)		#OUTPUT:
sub=n1-n2
print('Subtracation is: ',sub)		#OUTPUT:
mul=n1*n2
print('Multiplecation is: ',mul)		#OUTPUT:
div=n1-n2
print('Division is: ',div)		#OUTPUT:
mod=n1-n2
print('Module is: ',mod)		#OUTPUT:

(4) Write a program to calculate simple interest.
p=int(input('Enter p: '))		#OUTPUT:
print(p)		#OUTPUT:
r=int(input('Enter r: '))		#OUTPUT:
print(r)		#OUTPUT:
t=int(input('Enter t: '))		#OUTPUT:
print(t)		#OUTPUT:
simple=(p*r*t/100)
print(simple)		#OUTPUT:

(5) Write a program to calculate 10% bonus of salary.
salary=int(input('Enter your salary: '))		#OUTPUT:
print('Your salary is: ',salary)		#OUTPUT:
bonus=(salary*10/100)
print('Your bonus is: ',bonus)		#OUTPUT:
print('Your salary with bonus is: ',salary+bonus)		#OUTPUT:

(6) Write a program to convert KM into Meter.
km=int(input('Enter kilometer: '))	#OUTPUT:
print(km)		#OUTPUT:
meter=km*1000
print(meter)		#OUTPUT:

(7) The distance between two cities is input through keyboard.
distance=float(input('Enter distance between two city: '))	#OUTPUT:
print(distance)		#OUTPUT:
feet=distance*3280.84
print(feet)		#OUTPUT:
meter=distance*1000
print(meter)		#OUTPUT:
inch=distance*39370.1
print(inch)		#OUTPUT:
centimeter=distance*39370.1
print(centimeter)		#OUTPUT: