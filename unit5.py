Unit-05

#Working with cvs file
import pandas as pd 
df=pd.read_csv('product.csv')
print(df)

#Working with excel file
import pandas as pd
import xlrd
df=pd.read_excel('product.xlsx')
print(df)

#Taking data from the dictionary and convert into dataframe
student={'Enroll':[101,102,103,104,105],'Name':['ABC','CDE','EFG','GHI','JKL'],'City':['Rajkot','Mathura','Vrudavan','Ayodhya','Prayagraj']}
import pandas as pd
df=pd.DataFrame(student)
print(df)

#Taking data from the tuple and convert into dataframe
student=[(101,'ABC','Rajkot'),(101,'CDE','Mathura'),(101,'EFG','Vrudavan'),(101,'GHI','Ayodhya'),(101,'JKL','Prayagraj')]
import pandas as pd
df=pd.DataFrame(student,columns=['Enroll','Name','City'])
print(df)

#To know number of rows and columns
print(df.shape)

#Display first 5 records
print(df.head())
print(df.head(7))

#Display last 5 records
print(df.tail())
print(df.tail(2))

#Retrieve data in the range
print(df[3:6])

#Display specific columns only
print(df[['Name','Price']]) 

#Finding the highest price
print(df['Price'].max())

#Finding the lowest price
print(df['Price'].min())

#Display product whose manufacture city is Rajkot
print(df[df.Manufa_City=='Rajkot'])

#Display product whose price is more than 150
print(df[df.Price>150])

#Display name of product whose price is 35
print(df[df.Price==35])

#Visualising the data
# Bar Graph
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('population.xlsx')
print(df)
x=df['Year']
y=df['Population']
plt.bar(x,y,label='Population growth',color='Blue')
plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Population in billion')
plt.legend()
plt.show()

# Pie Chart
import matplotlib.pyplot as plt
sales_perc=[15,20,25,30,10]
prod=['Pencil','Eraser','Sharpner','Scale','Pen']
col=['Blue','Green','Red','Yellow','Pink']
plt.pie(sales_perc,labels=prod)
plt.title('Sales of product in percentage')
plt.legend()
plt.show()

# Line Chart
import matplotlib.pyplot as plt
years=['2020','2021','2022','2023','2024']
incr_pop_ind=[10,15,11,19,25]
incr_pop_china=[9,12,8,21,15]
plt.plot(years,incr_pop_ind,label='India')
plt.plot(years,incr_pop_china,label='China')
col=['Red','Blue']
plt.title('Population growth of India and China')
plt.xlabel('Years')
plt.ylabel('Increase of Population in lakhs')
plt.legend()
plt.show()

# Scatter Plot
import matplotlib.pyplot as plt
x=[2,9,7,6,3,4,8,10]
y=[8,2,4,9,6,3,2,5]
plt.scatter(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Diagram')
plt.legend()
plt.show()

# Area Plot
import matplotlib.pyplot as plt
import numpy as np 		#Only used because want to use range()
x=range(1,6)
y=[1,4,6,2,4]
plt.fill_between(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Plot')
plt.legend()
plt.show()