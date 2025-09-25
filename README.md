# Programming_Assigment_3_De_Guzman
This Programming Assignment contains the python codes regarding certain panda codes while using an external data
___
## Problem # 1

### Overview
In this problem, we are tasked to create a python code using an external data that was needed to be download beforehand. Then we are tasked to load this data into the IDE. Then we are tasked to displayed the first 5 rows and last 5 columns.

### Code 
```python
import pandas as pd
cars = pd.read_csv('cars.csv')
firstandlast = pd.concat([cars.head(), cars.tail()])
firstandlast
```
### How does it work
These lines loads the library panda for the manipulation of data frams and uploading the external data frame for the following code
```python
import pandas as pd #imports the panda library
cars = pd.read_csv('cars.csv') #loads the file cars.csv and stores it to the variable cars
```
This lines gets the first and last 5 of the data and displays it
```python
firstandlast = pd.concat([cars.head() #gets the first 5 from the data frame
  , cars.tail()]) #gets the last 5 from the data frame
firstandlast #displays the data frame for checking
```
### Output
<img width="894" height="474" alt="image" src="https://github.com/user-attachments/assets/ea133a8a-90fd-428c-b826-3817be89f8b2" />

### Lesson Learned
Through solving this problem, i learned that when we sometimes cant seem to get through a hardship or a wall in our way, it is sometimes better to take a step back and analyze the situation. Becuase of this problem i realized i needed to go back to the basics like putting the 2 strings together which has a syntax "concat" in which was one of the first lesson taught to us by our proffessor in Basic Computer Programming.
___

## Problem 2

### Overview
In this problem, we are tasked to manipulate the same data but we have to apply advanced methods of locating the specific values with conditions that is given to us. These inculdes: 

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### Code
```python
import pandas as pd
cars = pd.read_csv('cars.csv')

# Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars
oddall = cars.iloc[:, ::2]
print(oddall.iloc[0:5])

# Display the row that contains the ‘Model’ of ‘Mazda RX4’
mazdarx4 = cars[cars['Model'] == 'Mazda RX4']
mazdarx4

# How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
camarocyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl']
print("The number of cylinder that the Camaro Z28 has is:", camarocyl.values[0])

# Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
mazdacylgear = cars.loc[cars['Model'] == 'Mazda RX4 Wag', ['cyl', 'gear']]
fordcylgear = cars.loc[cars['Model'] == 'Ford Pantera L', ['cyl', 'gear']]
hondacylgear = cars.loc[cars['Model'] == 'Honda Civic', ['cyl', 'gear']]
print(" Mazda RX4 Wag = Cylinders:", mazdacylgear['cyl'].values[0], "|Gear:", mazdacylgear['gear'].values[0])
print("\n Ford Pantera L =  Cylinders:", fordcylgear['cyl'].values[0], "|Gear:", fordcylgear['gear'].values[0])
print("\n Honda Civic = Cylinders:", hondacylgear['cyl'].values[0], "|Gear:", hondacylgear['gear'].values[0])
```
### How does it work
Initial library and value
```python
import pandas as pd
cars = pd.read_csv('cars.csv')
```
Displays the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars
```python
oddall = cars.iloc[:, ::2] #only copies each column with an increament of 2
print(oddall.iloc[0:5]) #limits the column to only 5
```
Display the row that contains the ‘Model’ of ‘Mazda RX4
```python
mazdarx4 = cars[cars['Model'] == 'Mazda RX4'] #looks into the column "model" and looks for the string "Mazda RX4", if its true, it will store it to the mazdarx4
```
How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
```python
camarocyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'] #looks into the column "model" and looks for the string "Camaro X28", and looks into the row "cyl"
print("The number of cylinder that the Camaro Z28 has is:", camarocyl.values[0]) #prints the value of the cyl of camarocyl, the .values[0] ensure that that there are no indexes and only value of the camarocyl
```
Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RXG Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have
```python
mazdacylgear = cars.loc[cars['Model'] == 'Mazda RX4 Wag', ['cyl', 'gear']] #looks into the column "model" and looks for the string "Mazda RX4 Wag" and looks its value in the column cyl and gear
fordcylgear = cars.loc[cars['Model'] == 'Ford Pantera L', ['cyl', 'gear']] #gets teh value of the cyl and gear from the model Ford Pantera L
hondacylgear = cars.loc[cars['Model'] == 'Honda Civic', ['cyl', 'gear']] #gets the valye of the cyl and gear from the model Mazda Cyl Gear
print(" Mazda RX4 Wag = Cylinders:", mazdacylgear['cyl'].values[0], "|Gear:", mazdacylgear['gear'].values[0]) #prints the specified value with the supporting string for information
print("\n Ford Pantera L =  Cylinders:", fordcylgear['cyl'].values[0], "|Gear:", fordcylgear['gear'].values[0]) #prints the specified value with the supporting string for information
print("\n Honda Civic = Cylinders:", hondacylgear['cyl'].values[0], "|Gear:", hondacylgear['gear'].values[0]) #prints the specified value with the supporting string for information
```
### Lesson Learned
This problem helped me to take things step by step since the difficulty of the problem as time goes on is increasing like how the problem 2b uses the simple conditional statement so that we can find the right values upto expanding our knowledge about this conditional statement by experimenting on using multiple variables
___
# Version 2



