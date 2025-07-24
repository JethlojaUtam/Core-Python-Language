# EXAM PRACTICE

(1)
def sum(a,b):
	add=a+b
	print('Addition:',add)
#Calling the function
sum(25,13)

(2)
user=int(input('Enter the number:'))
for i in range(11):
	table=user*i
	print(user,'X',i,'=',user*i)

(3)
state=['Gujarat','Rajasthan','Maharastr','Kolkata','Utarpradesh']
capital=['Gandhinagar','Udaypur','Mumbai','Banguru','Gorkhpur']
dicts = dict(zip(state, capital))
print(dicts)

(4)
from numpy import*
votes=array([15000, 22000, 18500, 30000, 25000])
print(votes)
print(sum(votes))
print(mean(votes))

(5)
f1=open('image1.jpg','rb')
f2=open('image2.jpg','wb')
byte=f1.read()
f2.write(byte)
f1.close()
f2.close()

(6)
import re
string='utam@niketan$adarsh&bhargav'
result=re.split(r'\W',string)
print(result)

import re
string='utam niketan adarsh bhargav'
result=re.findall(r'\b\w{5,}\b',string)
print(result)

import re
string='utam 1 niketan 25 adarsh 3 bhargav'
result=re.findall(r'\b\d\b',string)
print(result)

(7)
import matplotlib.pyplot as plt 
state=('Gujarat','Rajasthan','Maharastr','Kolkata','Utarpradesh')
vote=(15000, 22000, 18500, 30000, 25000)
plt.bar(state,vote,label='Voting State',color='skyblue')
plt.xlabel('States')
plt.ylabel('Votes')
plt.title('Voting the state')
plt.legend()
plt.show()

(8)
import matplotlib.pyplot as plt 
state=['Gujarat','Rajasthan','Maharastr','Kolkata','Utarpradesh']
vote=[15000, 22000, 18500, 30000, 25000]
plt.pie(vote,labels='state')
plt.title('Voting the distributed')
plt.legend()
plt.show()

(1)
def arith(a,b):
	add=a+b
	sub=a-b
	mul=a*b 
	div=a/b 
	return add,sub,mul,div
#Calling the function
p,q,r,s=arith(20,5)
print('Addition:',p)
print('Substraction:',q)
print('multiplication:',r)
print('Division:',s)

(2)
user=int(input('Enter the number:'))
i=1
while i<=10:
	print(f'{user} X {i} = {user*i}')
	i=i+1

(3)
state=['Gujarat','Rajasthan','Maharastr','Kolkata','Utarpradesh']
capital=['Gandhinagar','Udaypur','Mumbai','Banguru','Gorkhpur']
dicts=dict(zip(state,capital))
print(dicts)

(4)
from numpy import*
array=array([95,90,80,100,70])
print(array)
print(sum(array))
print(mean(array))

(5)
f=open('abc1.txt','w')
user=input('Enter the string:')
f.write(user)
f1=open('abc.txt','r')
string=f1.read()
print(string)

(6)
import re
string='1utam 12niketan 25 adarsh 3 bhargav'
result=re.findall(r'\b\d\w*',string)
print(result)

import re
string='utamj 1 niketan adarsh 3 bhargav'
result=re.findall(r'\b\w{5}\b',string)
print(result)

import re
string='Welcome to india'
result=re.sub('india','Bharat',string)
print(result)

(7)
import matplotlib.pyplot as plt 
state=('Gujarat','Rajasthan','Maharastr','Kolkata','Utarpradesh')
vote=(15000, 22000, 18500, 30000, 25000)
plt.bar(state,vote,label='Voting State',color='skyblue')
plt.xlabel('States')
plt.ylabel('Votes')
plt.title('Voting the state')
plt.legend()
plt.show()

(8)
import matplotlib.pyplot as plt 
year=[2021,2022,2023,2024,2025]
population=[10,15,20,25,10]
plt.plot(year,population,color='red')
plt.title('population of india')
plt.xlabel('Yreas')
plt.ylabel('Populations in lakh')
plt.show()

(1)
user=input('Enter the polindrome string:')
if user==user[::-1]:
	print(f'{user} the string is polindrome')
else:
	print(f'{user} the string is not polindrome')

user=input('Enter the string polindrome:')
reverse=user[::-1]
if reverse in user:
	print(f'{user} the string is polindrome')
else:
	print(f'{user} the string is not polindrome')

(2)
from numpy import*
array1=array([1,2,3,4,5])
array2=array([6,7,8,9,0])
print(array1)
print(array2)
array3=where(array1==array2,array2,array1)
print(array3)
array4=where(array2>array1,array2,array1)
print(array4)

(3)
import re
string='utam niketan adarsh bhargav'
result=re.findall(r'\b\w{5,}\b',string)
print(result)

import re
string='Welcome to india'
result=re.sub('india','Bharat',string)
print(result)

(4)
user=float(input('Enter the mark:'))
if user>=90:
	print('A1 grade')
elif user>80 and user<=90:
	print('A garde')
elif user>70 and user<=80:
	print('B1 grade')
elif user>60 and user<=70:
	print('B garde')
elif user>50 and user<=60:
	print('Can do Better!')
else:
	print('Need to work hard')

(5)
def student(enrolment,name='ABC'):
	f=open('student.txt','w')
	f.write(f'Enrolment is: {enrolment}\n')
	f.write(f'Name is: {name}')

	f=open('student.txt','r')
	check=f.read()
	print('student information:\n')
	print(check)
#Calling the function
student(101,'XYZ')

(6)
f=open('image1.jpg','rb')
f1=open('image3.jpg','wb')
byte=f.read()
f1.write(byte)
f.close()
f1.close()
#Zip the file
from zipfile import*
f=ZipFile('ima.zip','w',ZIP_DEFLATED)
f.write('image2.jpg')
f.write('image3.jpg')
f.close()
#Unzip file
from zipfile import*
f=ZipFile('ima.zip','r')
f.extractall()

(7)
import matplotlib.pyplot as plt
import pandas as pd 
df=pd.read_excel('program.xlsx')
print(df)
programs=df['program']
addmissions=df['addmission']
plt.pie(addmissions,labels=programs)
plt.title('Addmission Offer')
plt.legend()
plt.show()

(1)
def simple(r,p,n):
	interest=r*p*n/100 
	return interest
#Calling the function
r=int(input('Enter the value of r:'))
p=int(input('Enter the value of p:'))
n=int(input('Enter the value of n:'))
# print('Simple interest',r,p,n)
print()

(2)
from numpy import*
array=array([1,2,3,4,5])
print(array)
array[1]=9
print(array)
array[0]=8
print(array)

(3)
user=float(input('Enter the number:'))
if user<=90:
	print('Your bill is 0')
elif user>90 and user<=150:
	bill=2*user
	print('Your bill is:',bill)
elif user>150 and user<=250:
	bill=5*user
	print('Your bill is:',bill)
elif user>250:
	bill=10*user
	print('Your bill is:',bill)

(4)
import re
string='utam 1 niketan 25 adarsh 3 bhargav'
result=re.findall(r'\b\d\b',string)
print(result)

import re
string='1utam 12niketan 25 adarsh 3 bhargav'
result=re.findall(r'\b\d\w*',string)
print(result)

(5)
f1=open('uni.txt','w')
f1.write('Atmiya University')
#Modify file	
f2=open('uni.txt','w')
f2.write('Atmiya University, Rajkot')
#Read file
f=open('uni.txt','r')
read=f.read()
print(read)

(6)
import os
file_name=input('Enter the file name:')
if os.path.isfile(file_name):
	f=open(file_name,'r')
	string=f.read()
	print(string)
	f.close()
else:
	print(f'{file_name} is does not exit')

(7)


(1)
import matplotlib.pyplot as plt
x=[5,8,3,6,1]
y=[9,3,6,2,5]
plt.scatter(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()

(2)
import re
string='bsc bms bab bmns bsyu'
result=re.findall(r'b[s,m][\w*]',string)
print(result)

import re 
string="abc 5'6"
result=re.search(r"\d+'\d+",string)
print(result.group())

(3)
square=lambda a:a*a 
user=int(input('Enter the number:'))
print('The square is:',square(user))

(4)

(5)

(6)
from numpy import*
a1=array([1,2,3,4,5,6])
a2=a1.reshape(2,3)
print(a2)
a3=a1.flatten()
print(a3)

(7)

(8)

(1)
import matplotlib.pyplot as plt
import numpy as np
x=range(1,6)
y=[3,5,7,2,4]
plt.fill_between(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area plot')
plt.show()

(2)
import re
string='apple abc annanas 1 93'
result=re.findall(r'a\w*',string)
print(result)

import re
string='apple abcd abc annanas 1 93'
result=re.findall(r'\b\w{3,4}\b',string)
print(result)

import re
string='utam 1 niketan 25 adarsh 3 bhargav'
result=re.findall(r'\b\d\b',string)
print(result)

(3)
from zipfile import*
f=ZipFile('zip1.zip','w',ZIP_DEFLATED)
f.write('abc.txt')
f.write('abc1.txt')
f.close()
#Unzip file
from zipfile import*
f=ZipFile('zip1.zip','r')
f.extractall()

(4)
amount=int(input('Enter the amount:'))
if amount<=1000:
	charge=amount+100
	print('Your bill:',charge)
elif amount>1000 and amount<=2000:
	charge=amount+80
	print('Your bill:',charge)
elif amount>2000 and amount<=3000:
	charge=amount+50
	print('Your bill:',charge)
elif amount>3000:
	charge=amount*10/100
	print('Your bill:',charge)

(5)
from numpy import*
array=array([1,2,3,4,5])
print(array)
print(array+2)
print(array-2)
print(max(array))
print(sum(array))
print(mean(array))

(6)
from numpy import*
array=array([90,70,80,60,50])
print(array)
print(sum(array))
print(mean(array))

(7)
import matplotlib.pyplot as plt 
import pandas as pd 
df=pd.read_excel('product.xlsx')
print(df)
x=df['product']
y=df['sale']
plt.bar(x,y,label='Product in sale')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales of product')
plt.legend()
plt.show()
