PRACTICE-04

(1) Accept two integer values from the user; display the number which is smaller and the number which is bigger.
one=int(input('Enter the first value: '))		Enter the first value: 1
two=int(input('Enter the second value: '))		Enter the second value: 2
if one<two:
	print('Enterd value is smaller')		Enterd value is smaller
elif one>two:
	print('Enterd value is bigger')
else:
	print('Enterd value is equal')

(2) Accept one integer value from the user; check whether entered number is divisible by 5 or not.
division=int(input('Enter the number: '))		Enter the number: 25
if division%5==0:
	print('Enterd the number is divisible by 5')		Enterd the number is divisible by 5
else:
	print('Enterd the number is not divisible by 5')

(3) Accept one integer value from the user; check whether entered number is between 0-100 or not.
number=int(input('Enter the number: '))		Enter the number: 25
if number>=0 and number<=100:
	print('Enterd number is bteween 0-100')		Enterd number is bteween 0-100
else:
	print('Enterd number is not bteween 0-100')


(4) Accept one integer value from the user; display the length of the entered number, also display that the entered number is of four digits or not.
num=input('Enter the integer: ')		Enter the integer: 2582
size=len(num)
print('Enterd the integer of size is: ',size)		Enterd the integer of size is:  4
if size==4:
	print('Enterd the integer of size is 4 digit')		Enterd the integer of size is 4 digit
else:
	print('Enterd the integer of size is not 4 digit')

(5) Accept one integer value from the user; display appropriate day of the week.
day=int(input('Enter the number of day: '))		Enter the number of day: 4
if day==1:
	print('Monday..')
elif day==2:
	print('Tuesday..')
elif day==3:
	print('Wednesday..')
elif day==4:
	print('Thursday..')		Thursday..
elif day==5:
	print('Friday..')
elif day==6:
	print('Saturday..')
elif day==7:
	print('Sunday..')
else:
	print('"Invalid input! Please enter the number of day!!!')

(6) Take choice from the user, and perform the arithmetic operation as per the choice.
	Choices: 1) Addition, 2) Subtraction, 3) Multiplication 4) Division
print('Please your choice...')
print('1) Addition')
print('2) Subtraction')
print('3) Multiplication')
print('4) Division')
choice=int(input('Enter the your choice: '))	Enter the your choice: 4
number1=int(input('Enter the 1st value: '))		Enter the 1st value: 2
number2=int(input('Enter the 2nd value: '))		Enter the 2nd value: 4
if choice==1:
	output=number1+number2
	print(f'Addition is: {output}')
elif choice==2:
	output=number1-number2
	print(f'Subtraction is: {output}')
elif choice==3:
	output=number1*number2
	print(f'Multiplication is: {output}')
elif choice==4:
	output=number1/number2
	print(f'Division is: {output}')		Division is: 0.5
else:
	print('Invalid choice! Please enter a number of choice!!!')

(7) Accept the string from the user; display the count of vowels and consonants.
user=input('Enter the string: ')	Enter the string: utam
vowel=0
consonant=0
svar='aeiouAEIOU'
for char in user:
	if char.isalpha():
		if char in user:
			vowel+=1
		else:
			consonant+=1
print(vowel)	4
print(consonant)

(8) Accept one integer value from the user; display the table of it.


(9) Display square and cube of numbers 1-10.
for i in range(1,11):
	square=i*i
	print(f'Square is: {square}')   Square is: 1
									Square is: 4
									Square is: 9
									Square is: 16
									Square is: 25
									Square is: 36
									Square is: 49
									Square is: 64
									Square is: 81
									Square is: 100
for i in range(1,11):
	cube=i*i*i
	print(f'Cube is: {cube}')		Cube is: 1
									Cube is: 8
									Cube is: 27
									Cube is: 64
									Cube is: 125
									Cube is: 216
									Cube is: 343
									Cube is: 512
									Cube is: 729
									Cube is: 1000

(10) Accept string from the user; convert the string to upper case.
user=input('Enter the string: ')	Enter the string: utam
upper1=user.upper()
print(upper1)	UTAM

(11) Display the following output using loop:
	 i) 1 to 10
	 ii) 10 to 1
	 iii) 1 3 5 7 9
	 iv) 2 4 6 8 10
i)
for i in range(1,11):
	print(i,end=' ')	1 2 3 4 5 6 7 8 9 10

ii)
for i in range(10,0,-1):
	print(i,end=' ')	10 9 8 7 6 5 4 3 2 1

iii)
for i in range(1,10,2):
	print(i,end=' ')	1 3 5 7 9

iv)
for i in range(2,11,2):
	print(i,end=' ')	2 4 6 8 10

(12) Print 1 2 4 8 16 32 64 128 256 512 1024
for i in range(11):
	print(2**i,end=' ')		1 2 4 8 16 32 64 128 256 512 1024

(13) Accept the number from the user; display the table of that number.


(14) Accept numbers from the user; display the sum of the entered numbers.


(15) Accept numbers from the user; display the count of the entered numbers.


(16) Accept numbers from the user; find and display number of zeros available in the number.


(17) Accept an integer from the user; tell user that whether entered number is even or odd.
	 Required output: 
					Enter the number: 7
					7 is an odd number
					Do you want to check another number? Y
					Enter the number: 2
					2 is an even number
					Do you want to check another number? N