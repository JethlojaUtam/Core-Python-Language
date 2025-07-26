PRACTICE-02

(1) Demonstrate the use of /n and \t by printing the long string. Take input from the user.
a=input('Enter the String: ')     #OUTPUT:
b=input('Enter the Number: ')     #OUTPUT:
print('\n',a)	#OUTPUT:
print('\t',b)	#OUTPUT:

string=input('Enter The String: ')
print('My name is \n  utam jethloja',string)
print('My name is \t  utam jethloja',string)

(2) Take one variable, store a string and display 3rd and 5th character of the string. Take input from the user.
a=input('Enter the Name: ')     #OUTPUT:Enter the Name: utamkumar
print(a[2])     #OUTPUT:a
print(a[4])     #OUTPUT:k

(3) Take 3 numeric values in one variable, add those three values and display.
num=(int(input('Enter the 1st value: ')),   #OUTPUT:Enter the 1st value:25
    int(input('Enter the 2nd value: ')),    #OUTPUT:Enter the 2nd value:13
    int(input('Enter the 3rd value: ')))    #OUTPUT:Enter the 3rd value:8
sum=sum(num)
print('Sum of three number is: ',sum)   #OUTPUT:Sum of three number is:46

(4) Perform the following calculation: a*7/b+a, where value of a=2 and b=16.
a=2
b=16
print('The calculation is: ',a*7/b+a)   #OUTPUT:The calculation is:2.875

(5) Take input from the user at command line. The values must be a number, a string and the list.
import sys
print(sys.argv)     #OUTPUT:['practice.py', 'utam', '25', '[16,13,8,29]']
-->>> niche ni 3 line nathi lakhvani samajva mate chhe.....
import sys 
a=(sys.argv)
print(a)

(6) Following the instruction of Q5, display the output as below:
    The name of file is abc.py and its values are [values added at command line].
import sys
a=(sys.argv)
print('The name of file is: ',a[0], 'and its values are: ',a[1],a[2])   #OUTPUT:The name of file is:  practice.py and its values are:  25 utam

7). Insert string into the variable and perform following tasks:
   -Print the type of the variable with a message “The type of the variable is:”
   -Print the string with a message “The string is:”
   -Display the 3rd character of the string
   -Display character from 4th to 6th from the string
   -Change the 3rd character of the string replace it with ‘A’.
a=('Welcome to python lab.')
print('The type of the variable is: ',type(a))      #OUTPUT:The type of the variable is:  <class 'str'>
print('The string is: ',a)      #OUTPUT:The string is:  Welcome to python lab
print(a[2])     #OUTPUT:l
print(a[3:5])   #OUTPUT:co
a[2]='A'    #OUTPUT:will generate an error 'str' object does not support item assignment
print(a[2])

(8) Store the integer value using int() class.
   -Insert an Octal value in the variable and convert it to decimal.
   -Insert the binary value in the variable and convert it to decimal.
   -Insert the float value in the variable convert it to decimal.
Octal=0o11
decimal=int(Octal)
print('Octal value 0c11 converted to decimal: ',decimal)    #OUTPUT:Octal value 0c11 converted to decimal:9

Binary=0b10110
decimal=int(Binary)
print('Binary value 0b10110 converted to decimal: ',decimal)    #OUTPUT:Binary value 0b10110 converted to decimal:22  

Float=25.8
decimal=int(Float)
print('Float value 25.8 converted to decimal: ',decimal)    #OUTPUT:Float value 25.8 converted to decimal:25

(9) Create a list with variety of data and perform following tasks:
   -Print all the element of the string.
   -Display the class.
   -Display the first element of the list.
   -Display the 4th element of the list using negative index.
   -Change the 4th element of the list
lst=['Utam','Adarsh','Bhargav','Raj']		#OUTPUT:['Utam','Adarsh','Bhargav','Raj']
print(lst)
print(type(lst))		#OUTPUT:<class 'list'>
a=lst[0]
print(a)		#OUTPUT:Utam
b=lst[-1]
print(b)		#OUTPUT:'Raj'
c=lst[3]='Niketan'
print(c)		#OUTPUT:Niketan
print(lst)		#OUTPUT:['Utam','Adarsh','Bhargav','Niketan']

(10) Create a tuple using a tuple() class.
    -Modify the 1st element of the tuple.
    -Display the 3rd to 6th element from the tuple.
    -Display the 3rd to 6th element from the tuple using negative index.the
tup=('Utam',25,'Adarsh',13,'Niketan',8)
print(tup)		#OUTPUT:<'Utam',25,'Adarsh',13,'Niketan',8>
print(type(tup))	#OUTPUT:<class 'tuple'>
# a=tup[0]='Bhargav'
# print(a)	#OUTPUT:error an 'tuple' object does not support item assignment
print(tup[2:6])		#OUTPUT:<'Adarsh',13,'Niketan',8>
print(tup[-4:])		#OUTPUT:<'Adarsh',13,'Niketan',8>

(11) Create a dictionary with at least 10 values and perform the following task:
    -Display all the elements of the dictionary.
    -Check the class of the dictionary you made.
    -Display the value stored in the key 7.
    -Change the value stored in the key 7.
    -Display all the values only.
dic={1:'Utam',2:'Adarsh',3:'Niketan',4:'Bhargav',5:25,6:13,7:8,8:16,9:'Shivpur',10:'Morbi'}
print(dic)		#OUTPUT:{1:'Utam',2:'Adarsh',3:'Niketan',4:'Bhargav',5:25,6:13,7:8,8:16,9:'Shivpur',10:'Morbi'}
print(type(dic))	#OUTPUT:<class 'dict'>
print(dic[7])	#OUTPUT:8
dic[7]='Raghuvir'
print(dic)		#OUTPUT:{1:'Utam',2:'Adarsh',3:'Niketan',4:'Bhargav',5:25,6:13,7:'Raghuvir',8:16,9:'Shivpur',10:'Morbi'}
print(dic.values())		#OUTPUT:dict_values<['Utam','Adarsh','Niketan','Bhargav',25,13,'Raghuvir',16,'Shivpur','Morbi']>
print(dic.keys())	    #OUTPUT:dict_keys<[1,2,3,4,5,6,7,8,9,10]>

(12) Create a set containing varieties of value and perform following task:
    -Try to insert the duplicate value.
    -Add two values in the set.
    -Remove two values from the set.
set1={13,25,8,16}
print(set1)		#OUTPUT:{8,25,13,16}
set1.update([25])
print(set1)       #OUTPUT:{8,25,13,16}
set1.update([5,19])
print(set1)		#OUTPUT:{5,8,13,16,19,25}
set1.remove(5)
print(set1)     #OUTPUT:{8, 13, 16, 19, 25}
set1.remove(19)
print(set1)     #OUTPUT:{8, 13, 16, 25}

(13) Create a set containing varieties of value and perform following task (the set must be not modifiable):
    -Try to insert the duplicate value.
    -Add two values in the set.
    -Remove two values from the set.
set2=frozenset({13,25,8,16})
print(set2)		#OUTPUT:{8,25,13,16}
print(type(set2))       #OUTPUT:<class 'frozenset'>
set2.update({25})       
print(set2)       #OUTPUT:AttributeError: 'frozenset' object has no attribute 'update'
set2.remove({25})
print(set2)     #OUTPUT:AttributeError: 'frozenset' object has no attribute 'remove'

(14) Create a bytes and perform the following tasks:
    -Display the first element using negative index.
    -Display the last element using positive index.
    -Add two values in to it.
    -Modify the last element.
byte=[25,13,16,8,29]
print(byte)		#OUTPUT:
print(type(byte))		#OUTPUT:<class 'list'>
b=bytes(byte)
print(type(b))		#OUTPUT:<class 'bytes'>
print(b)		#OUTPUT:b'\x19\r\x10\x08\x1d'
print(b[-5])	#OUTPUT:25
print(b[4])		#OUTPUT:29
b[2]=5
print(b)		#OUTPUT:will generate an error 'bytes' object does not support item assignment

(15) Create a bytes array and perform the following tasks:
	  -Display the first element using negative index.
    -Display the last element using positive index.
    -Add two values in to it.
    -Modify the last element.
    -Remove the last values from the set.
bytearay=[25,13,16,8,29]
print(bytearay)		#OUTPUT:
b=bytearray(bytearay)
print(b)		#OUTPUT:
print(type(b))	#OUTPUT:
b[2]=5
print(b[2])		#OUTPUT:
