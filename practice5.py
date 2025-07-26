PRACTICE-05

(1) Create a list containing several strings. Take input from the user (search string); display whether entered string is available in the list or not.
list1=['Utam','Niketan','Adarsh','Bhargav']
user=input('Search the string: ')		Search the string: Niketan
if user in list1:
	print(f'{user} string is available in the list')		Utam string is available in the list
else:
	print(f'{user} string is not available in the list')

list1=input('Enter the string: ').split(',')
print(list1)
search=input('Enter the search string: ')
if search in list1:
	print('The search string is available')
else:
	print('The search string is not available')

(2) Accept the string from the user; display the message whether the entered string is palindrome or not.
user=input('Enter the palindrome string: ')		Enter the palindrome string: nitin
if user == user[::-1]:
	print(f'{user} is palindrome string')	nitin is palindrome string
else:
	print(f'{user} is not palindrome string')

(3) Accept the string from the user; display the string in the reverse order.
string=input('Enter the string: ')	Enter the string: Niketan
print('The string in the reverse order in',string[::-1])	The string in the reverse order in natekiN

user=input('Enter the string: ')
reverse=user[::-1]
print('The string in the reverse order in',reverse)

(4) Accept the string from the user; allow user to choose from the following options and perform the task as per user’s choice. 
	i). Convert to the upper case 
	ii). Convert to the lower case 
	iii). Convert to the swap case 
	iv). Convert to the title case.
case=input('Enter the string: ')	Enter the string: Utam & Niketan
print(case.upper())		UTAM & NIKETAN
print(case.lower())		utam & niketan	
print(case.swapcase())	uTAM & nIKETAN
print(case.title())		Utam & Niketan

user=input('Enter the string: ')
print(user)
print('1. Convert to the upper case')
print('2. Convert to the lower case')
print('3.Convert to the swap case')
print('4. Convert to the title case')
chooice=input('Enter the chooice?: ')
if chooice=='1':
	upper=user.upper()
	print('Convert to the upper case is:',upper)
elif chooice=='2':
	lower=user.lower()
	print('Convert to the lower case is:',lower)
elif chooice=='3':
	swap=user.swapcase()
	print('Convert to the swap case is:',swap)
elif chooice=='4':
	title=user.title()
	print('Convert to the title case is:',title)
else:
	print('Please enter the your chooice is not define!!!')

(5) Allow users to enter multiple strings in the list; arrange the entered string into alphabetical order and display.
list1=[]
number=int(input('How many string you want to enter?: '))	How many string you want to enter?: 2
for alpha in range(number):
	print('Enter the string: ',end=' ')		Enter the string:  Utan
											Enter the string:  Niketan
	list1.append(input())
print(list1)		['Utan', 'Niketan']
list2=list1.sort()
print('\nString are alphabetical:')		String are alphabetical:
for alpha in list1:
	print(alpha)	Niketan
					Utam

list1=input('Enter the string: ').split(',')
list1.sort()
print(list1)

(6) Create a tuple and display it. Enter 25 at the third position and display it again.
tuple1=(1,2,3,4,5)
print(tuple1)
tuple1[2]=25
print(tuple1)	TypeError: 'tuple' object does not support item assignment

(7) Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher).
	a. Display the dictionary
	b. Display the name of Author 
	c. Display the Bookid
	d. Display the length of the dictionary 
	e. Update the price 
	f. Insert year as the new key and display the dictionary again.
dict1={'Bookid':101,'Title':'Python','Author':'Utam','Price':2500,'Publisher':'Shah sir'}
print(dict1)
print(dict1['Author'])
print(dict1['Bookid'])
print(len(dict1))
dict1['Price']=1000
print(dict1)
dict1['Year']=2025
print(dict1)

(8) Create a numeric array and perform following operations on it: 
Add 2 to each elements, Subtract 3 from each element, Multiply each element with 3, Divide each element by 2, Find max and min, find the average of all elements.
from numpy import*
array=array([25,8,13,16])
print(array)
print(type(array))
print('Addition is: ',array+2)
print('Substrac is: ',array-3)
print('Multiply is: ',array*3)
print('Divition is: ',array/2)
print('Maximum is: ',max(array))
print('Minimum is: ',min(array))
print('Average is: ',mean(array))

(9) Create a numeric array and do the following: append the element, pop the element, insert an element at the desired postion, reverse the elements in the array, convert the array to list.
from array import*
array=array('i',[25,8,13,16])
print(array)
array.append(1)
print(array)
array.pop()
print(array)
array.insert(0,0)
print(array)
array.reverse()
print(array)
a=array.tolist()
print(a)
print(type(array))
print(type(a))

(10) Accept numeric elements from the user, store it to the array and display. Ask user to entersearch element. Display the position of the searched element.
from array import*
array=[]
number=int(input('Enter the numeric element: '))
print('The array is: ',array)
search=unt(input('Please enterd the numeric element?: '))
if search in array:
	print('The search element in the array')
else:
	print('The search element not in the array')

(11) Take two arrays enter 5 digits in both arrays. Compare the corresponding element from each array and display only the bigger number.
from numpy import*
array1=array([1,3,5,7,9])
array2=array([2,4,6,8,0])
array3=where(array2==array1,array2,array1)
array4=where(array2>array1,array2,array1)
print('The original array is: ',array1)
print('The original array is: ',array2)
print('Compare the corresponding element array is: ',array3)
print('The bigger array is: ',array4)

(12) Accept dimension of the array and its values from the user, create an array as desired.


(13) Create a function to calculate the simple interest.
def simple(r,p,n):
	interest=r*p*n 
	return interest
#Calling the function
interested=simple(5000,0.05,2)
print('Simple interest',interested)

(14) Create a function to perform basic arithmetic operations on the number.
def arith(a,b):
	add=a+b
	sub=a-b
	mul=a*b
	div=a/b 
	return add,sub,mul,div
#Calling the function
p,q,r,s=arith(20,5)
print('Addition: ',p)
print('Substraction: ',q)
print('Multiplication: ',r)
print('Division: ',s)

(15) Accept multiple strings and store it into the list using function.


(16) Find the biggest number from three values using lambda.


(17) Demonstrate the use of: i). break and ii). pass.
break1='Rajkot'
for b in break1:
	print(b)	#OUTPUT:R
	if b=='k':			a
		break			j		
						k

pass1=0
while pass1<10:
	pass1=pass1+1
	if pass1>5:
		pass
	print(pass1)	#OUTPUT:1
							2
							3
							4
							5
							6
							7
							8
							9
							10