PRACTICE-03

(1) Get the basic salary from the employee and display the net salary by calculating the following 
conditions:Applicable TA 4%, DA 30%, HRA 15% on basic salary.
	  Applicable 3% tax, 12% PF on basic salary.

salary = int(input("Enter your salary: "))		#OUTPUT:Enter your salary: 5000
print('Your salary is:',salary)		#OUTPUT:Your salary is: 5000
TA=salary*4/100
print('Your TA is: ',TA)	#OUTPUT:Your TA is:  200.0
DA=salary*30/100
print('Your DA is: ',DA)	#OUTPUT:Your DA is:  1500.0
HRA=salary*15/100
print('Your HRA is: ',HRA)		#OUTPUT:Your HRA is:  750.0
TAX=salary*3/100
print('Your TAX is: ',TAX)		#OUTPUT:Your TAX is:  150.0
PF=salary*12/100
print('Your PF is: ',PF)	#OUTPUT:Your PF is:  600.0
totalsalary=salary+TA+DA+HRA-TAX+PF
print('Your total salary is: ',totalsalary)		#OUTPUT:Your total salary is:  7900.0


(2) Get the marks of 5 subjects at the command line and display the total of marks, and percentage. 

import sys
sub1=int(sys.argv[1])
sub2=int(sys.argv[2])
sub3=int(sys.argv[3])
sub4=int(sys.argv[4])
sub5=int(sys.argv[5])
totalmarks=sub1+sub2+sub3+sub4+sub5
print('Your total marks is: ',totalmarks)		#OUTPUT:
percentage=totalmarks*100/500
print('Your percentage is: ',percentage)		#OUTPUT:

output
D:\>python excersice-3.py 50 40 66 67 87
Your Total marks is: 310
Your percentage is: 62.0

(3) Rajkot Corporation wants to make simple application to calculate Water Bill of Rajkotians. Water is being delivered by the Corporation on per litre charges as below: 
	  Upto 90 litres – Rs. 0/ltr 
	  Upto 150 litres – Rs. 2/ltr 
    Upto 250 litres – Rs. 5/ltr 
    More than 250 – Rs. 10/ltr 
    Accept unit consumption from consumer and display the bill amount.

liters=float(input('Enter water liters: '))	#OUTPUT:
if(liters<=90):
    print('Your bill is 0')
if(liters>90 and liters<=150):
    bill=liters*2
    print('Your bill is: ',bill)		#OUTPUT:
if(liters>150 and liters<=250):
    bill=liters*5
    print('Your bill is: ',bill)		#OUTPUT:
if(liters>250):
    bill=liters*10
    print('Your bill is: ',bill)		#OUTPUT:

output
enter water liters:180
Your bill is: 900.0

(4) A tuition class owner wants to make a simple application to allocate grade to the students on 
the basis of marks student have scored. Accept marks from the students. 
    Marks more than 90 – A1 grade 
	  Marks 80 or less than or equal 90 – A grade 
	  Marks 70 or less than or equal 80 – B1 
	  Marks 60 or less than or equal 70 – B 
	  Marks 50 or less than or equal 60 – Can do Better! 
	  Marks <50 – Need to work hard. 

Marks = float(input('Enter your marks: '))	#OUTPUT:
if Marks > 90:
    print('A1 Grade')
elif 80 <= Marks <= 90:
    print('A Grade')
elif 70 <= Marks < 80:
    print('B1 Grade')
elif 60 <= Marks < 70:
    print('B Grade')
elif 50 <= Marks < 60:
    print('Can do Better!')
else:
    print('Need to work hard')

output
Enter your marks: 87
A grade

(5) Income Tax department wants to make an application that calculates tax on the basis of the 
income. Accept yearly income earned by the taxpayer as an input and calculate tax to be paid. 
	  The tax slab  is as below: 
	  Income up to 8 lakhs – No tax 
	  Income more than 8 lakh and less than 10 lakhs – 15% of income 
	  Income more than 10 lakhs and less than 20 lakhs – 20% of income 
	  Income more than 20 lakhs – 30% of income 

income=int(input('Enter your income:- '))		#OUTPUT:
if income <=800000:
    print('No Tax...')
elif income>=800000 and income<=1000000:
    tax=income*15/100
    print('Your tax is: ',tax)
elif income>1000000 and income<=2000000:
    tax=income*20/100
    print('Your tax is: ',tax)
else:
    tax=income*30/100
    print('Your tax is: ',tax)	#OUTPUT:

output
Enter your income:-2500000
your tax is: 750000.0

b=int(input('Enter 2nd integer value: '))		#OUTPUT:
if a > b:
    print('The big number is: ',a)	#OUTPUT:
    print('The small number is: ',b)		#OUTPUT:
(6) Accept two integer values in separate variable, display the small value and big value out of it. 

a=int(input('Enter 1st integer value: 
else:
    print('The big number is: ',b)		#OUTPUT:
    print('The small number is: ',a)		#OUTPUT:

output
Enter First integer number:23
Enter Second integer number:45
The big number is: 45
The small number is: 23

(7) Accept marks from 4 students, display which mark is highest among all. 

student1=float(input('Enter your marks: '))	#OUTPUT:
student2=float(input('Enter your marks: '))	#OUTPUT:
student3=float(input('Enter your marks: '))	#OUTPUT:
student4=float(input('Enter your marks: '))	#OUTPUT:
if student1>student2 and student1>student3 and student1>student4:
    print('Student-1 has highest marks')
elif student2>student1 and student2>student3 and student2>student4:
    print('Student-2 has highest marks')
elif student3>sstudent1 and student3>student2 and student3>student4:
    print('Student-3 has highest marks')
else:
    print('Student-4 has highest marks')

output
Enter your marks:74
Enter your marks:85
Enter your marks:45
Enter your marks:87
student 4 has highest marks

8. An online selling app wants to develop a application to calculate shipping charges on the purchase. Accept amount from the user and calculate the shipping charges. 
	 The shipping charges are as below: 
	 Shopping amount less than 1500 – The shipping charges is Rs. 100/- --Type the message: Please purchase (1500-amount) to avail shipping charge of Rs. 80/- --Please pay (amount+100) 
	 Shopping amount more than 1500 and less than 3000 – The shipping charges is Rs. 70/- --Type the message: Please purchase (3000-amount) to avail shipping charge of Rs. 50/- --Please pay (amount+70) 
	 Shopping amount more than 3000 – Free shipping + 7% discount on amount --Type a message: You saved (amount*7/100) --Please pay (amount – discount)

amount=int(input('Enter your purchase amount: '))		#OUTPUT:
if amount < 1500:
    print('Please purchase (1500-amount) to avail shipping charge of Rs. 80/-')
    bill=amount+100
    print('Please pay Rs. ',bill)
elif amount >1500 and amount <3000:
    print('Please purchase (3000-amount) to avail shipping charge of Rs. 50/-')
    bill=amount+70
    print('Please pay Rs. ',bill)
else :
    saved=amount*7/100
    print('You saved Rs. ',saved)		#OUTPUT:
    bill=amount-saved
    print('Please pay Rs. ',bill)		#OUTPUT:

output
Enter your purchase Amount:12345
you saved Rs. 864.15
please pay Rs. 11480.85