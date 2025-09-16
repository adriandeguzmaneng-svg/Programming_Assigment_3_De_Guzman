# Programming_Assigment_3_De_Guzman
This Programming Assignment contains the python codes regarding certain panda codes while using an external data
___
## Problem # 1

### Overview
In this problem, we are tasked to create a python code using an external data that was needed to be download beforehand. Then we are tasked to load this data into the IDE. Then we are tasked to displayed the first 5 rows and last 5 columns.

### Code 
<img width="368" height="124" alt="image" src="https://github.com/user-attachments/assets/3b7ee2a0-66c6-4fe0-a1e5-8dc470719602" /> 

<img width="584" height="93" alt="image" src="https://github.com/user-attachments/assets/5894cc8c-24ac-4f31-98cf-2cd6b7049430" />

### How i made it:
First, according to the instructions, we are tasked to import or load the data into the data frame but we cant use data frames since we still havent imported the library of pandas to manipulate or read data frames. So i import the panda library using the code "import panda as pd". Next i loaded the data file into the IDE using the code "pd.read_csv('cars.csv)" then i procedded to display the data frame so that i can know if the data loaded properly. For the next part, i tried to simply display both the first and last 5 using the "head()" and "tail()" command but the output of that is only the last 5 thus leading me to concatenate both of the part of the array using the syntax "pd.concat([cars.head(), cars.tail()])" and i displayed the output so that i can know if the array displayed is correct.

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
<img width="1658" height="585" alt="image" src="https://github.com/user-attachments/assets/82b0c658-1f4a-4799-a132-372ae9e46497" />

### How i made it
a. For part a, i used cars.iloc[:,::2] so that we can only keep the columns we have moved by increments of 1 since the terminal value is 2, it is not icluded. Lastly i used .iloc to set a boundery to the data this creating a syntax "cars.iloc[0:5]" so that the data is only limited to 5 columns lastly i displayed the output so that i can know if the output is correct.
b. For this problem i searched using the "==" syntax if the specific model is "Mazda RX4" then replaced the whole data with the conditional statement. 
c. Using the same conditional statement we used of problem 2b, we also checked if the model of the car is a "Camaro Z28", that position is the rows but we need to also check for the columns with the cyl so that we can know the value of the cylnders with the specific car model so we put the condition on the row on the first postion and the column condition on the 2nd position on the index thus creating the syntax "cars.loc[cars['Model'] == 'Camaro Z28', 'cyl']". Then i just equated this to a variable and displayed that variable for correction purposes. 
d. Using the same syntaxes i used on problem 2b  and 2c, i first checked if the model matched the requred model which are  ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’. With this there are 2 columns we are required to check so we just need to put 2 column in the column seciton of the index thus creating the syntax: ars.loc[cars['Model'] == 'Mazda RX4 Wag', ['cyl', 'gear']]. I repeated this process for the 3 requested model of the cars and displayed them with appropriate message for the cylinders and gears of the specific car.

### Lesson Learned
This problem helped me to take things step by step since the difficulty of the problem as time goes on is increasing like how the problem 2b uses the simple conditional statement so that we can find the right values upto expanding our knowledge about this conditional statement by experimenting on using multiple variables


