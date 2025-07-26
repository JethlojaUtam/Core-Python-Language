PRACTICE-06

(1) Create a file with file name sample.txt, accept some data from the user and store it in the file.
f=open('sample.txt','w')
string=input('Enter the string: ')
f.write(string)
f.close()

(2) Display the data stored in the sample.txt file (created in question 1).
f=open('sample.txt','r')
string=f.read()
print(string)
f.close()

(3) Accept some data from the user and append it into the file sample.txt (created in question 1), also the data in the file.
f=open('sample.txt','a+')
string=input('Enter the append string: ')
f.write(string)
f=open('sample.txt','r')
string=f.read()
print(string)

f=open('sample.txt','w')
string=input('Enter the string: ')
f.write(string)
f.close()
f=open('sample.txt','a+')
string=input('Enter the append string: ')
f.write(string)
f=open('sample.txt','r')
string=f.read()
print(string)

(4) Accept the file name from the user, check the availability of the file: 
	i) If the file exists display the data on the screen and
	ii) If the file is not available, display the appropriate message.
import os
file_name=input('Enter the file name: ')
if os.path.isfile(file_name):
	f=open(file_name,'r')
	string=f.read()
	print(string)
	f.close()
else:
	print(f'{file_name} dose not exits')

(5) Accept the file name from the user, check the availability of the file: 
	a) If the file exists, display: 
	i) No. of characters, 
	ii) No. of words and 
	iii) No. of lines
	b) If the file does exist, than display the appropriate message.
import os,sys
file_name=input('Enter the file name: ')
if os.path.isfile(file_name):
	f=open(file_name,'r')
else:
	print(file_name+ 'dose not exits')
	sys.close()
cc=cw=cl=0
for line in f:
	words=line.split()
	cl=cl+1
	cw=cw+len(words)
	cc=cc+len(line)
print('Number of line in a file are: ',cl)
print('Number of the words in a file are: ',cw)
print('Number of characters in a file are: ',cc)
f.close()

(6) Create and open the binary file with ‘with’ option. Store names of all the subjects you study in semester 2. Ask user to enter the subject number they wanted to see and display that subject 
name.
record_len=15
with open('subject.bin','wb') as f:
	no=int(input('How many subject in the enter?: '))
	for i in range(no):
		subject=input('Enter the subject name: ')
		ln=len(subject)
		subject=subject+(record_len-ln)*''
		subject=subject.encode()
		f.write(subject)
		print()

(7) Create a file named ‘img1’, store an image into it. Open another file named ‘img2’, copy the same image as in the file ’img1’. Also store both files into the zip file named ‘imp_img’.
f1=open('image1.jpg','rb')
f2=open('image2.jpg','wb')
bytes=f1.read()
f2.write(bytes)
f1.close()
f2.close()
import zipfile
zip1=zipfile.ZipFile('imp_image','w',zipfile.ZIP_DEFLATED)
zip1.write('image1.jpg')
zip1.write('image2.jpg')
zip1.close()

(8) Create a file with ‘with’ option, name it as ‘marks.dat’.
	i) Accept subject name and marks from the user, store the data in the file.
	ii) Give three options to the user: 
		a) To view whole file, 
	b) Accept and edit the marks of a subject user want to change.
	iii) Exit


(9) Create a regular expression that:
	a) Identifies and display the string starting with ‘s’ and having 4 characters.
	b) Splits the string where some special characters are found.
	c) Display the word starting with number.
	d) Display the word having 3 or 4 or 5 characters.
	e) Display only the dates from the string.
	f) Create a string with name of the person and his Aadhar number, display only Aadhar number.
	g) Display all the words that starts with ‘at’ or ‘ap’.
	h) Check if the string starts with ‘at’ than display appropriate message and otherwise.
(i)
import re
word='sujal,sohan,sun,soon,utam'
result=re.findall(r's\w+',word)
print(result)
(ii)
import re
word='sujal,soon,utam,#,$'
result=re.findall(r'\W+',word)
print(result)
(iii)
import re
word='sujal,sohan,sun,soon,utam'
result=re.findall(r'\d[\w]*',word)
print(result)
(iv)
import re
word='sujal,sohan,sun,soon,utam,25 mar'
result=re.findall(r'\b\w{3,5}\b',word)
print(result)
(v)
import re
word='25 mar,16 aug'
result=re.findall(r'\b\d\d\b',word)
print(result)
(vi)
import re
string='ABC 123456789012,XYZ 098765432109'
result=re.findall(r'\b\d+\b',string)
print(result)

(vii)
import re
word='atmiya sujal bhargav aprit'
result=re.findall(r'a[t|p]\w+',word)
print(result)

(viii)
import re
string='atmiya parul marvadi'
result=re.findall(r'at\w+',string)
print(result)
if string.startswith('at'):
    print("The string starts with 'at'.")
else:
    print("The string does not start with 'at'.")

(10) Do as directed:
	a) Name the package used to deal with data frame.
	b) Name the package used to deal with data .xlsx file.
	c) Name the function used to read the .csv file.
	d) Name the function used to read the .xlsx file.
	e) Name the function used to read the tuple.
(a)
package={'Name':['Utam','Niketan','Adarsh','Bhargav'],'Rollno':[1,2,3,4],'Div':['A','B','C','D']}
import pandas as pd
df=pd.DataFrame(package)
print(df)

(c)
import pandas as pd
df=pd.read_csv('package.csv')
print(df)

(d)
import pandas as pd
import xlrd
df=pd.read_excel('package.xlsx')
print(df)

(e)
function=[(1,'Utam','Morbi'),(2,'Niketan','Kuchchh'),(3,'Adarsh','Rajkot'),(4,'Bhargav','Ahmdabad')]
import pandas as pd
df=pd.DataFrame(function,columns=['Id','Name','City'])
print(df)

(11) Create a dictionary which stores (at least 10 records)empid, name, city, salary and perform 
following operations:
	a) Display first three records
	b) Display last five records
	c) Display only Name and City
	d) Display employee who belongs to Mumbai
	e) Display employee name who belongs to Mumbai
	f) Display employee whose salary is more than 25000


(12) Create an xlsx file store marks of five subjects, plot the data on the bar graph.
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('bar.xlsx')
print(df)
x=df['Name']
y=df['Mark']
plt.bar(x,y,label='XYZ',color='red')
plt.bar(x,y)
plt.xlabel('Name')
plt.ylabel('Mark')
plt.title('Name & Rollno')
plt.legend()
plt.show()

(13) Take five income source of the Government and display it on the pie chart.


(14) Draw the line chart representing BSE(Bombay Stock Exchange) index in last 10 years.
import matplotlib.pyplot as plt
years=['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']
stock=[90,59,65,100,25,84,90,36,60,40]
plt.plot(years,stock,color='red')
plt.title('Bombay Stock Exchange')
plt.xlabel('Years')
plt.ylabel('Stock')
plt.show()

(15) Plot the grouped bar graph using the appropriate data.