# %%
import pandas as pd

cars = pd.read_csv('cars.csv')
cars

# %% [markdown]
# Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars

# %%
cars = pd.read_csv('cars.csv')
oddall = cars.iloc[:, ::2]
print(oddall.iloc[0:5])

# %% [markdown]
# Display the row that contains the ‘Model’ of ‘Mazda RX4’

# %%
mazdarx4 = cars[cars['Model'] == 'Mazda RX4']
mazdarx4

# %% [markdown]
# How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# %%
camarocyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl']
print("The number of cylinder that the Camaro Z28 has is:", camarocyl.values[0])

# %% [markdown]
# Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
# 

# %%
mazdacylgear = cars.loc[cars['Model'] == 'Mazda RX4 Wag', ['cyl', 'gear']]
fordcylgear = cars.loc[cars['Model'] == 'Ford Pantera L', ['cyl', 'gear']]
hondacylgear = cars.loc[cars['Model'] == 'Honda Civic', ['cyl', 'gear']]
print(" Mazda RX4 Wag = Cylinders:", mazdacylgear['cyl'].values[0], "|Gear:", mazdacylgear['gear'].values[0])
print("\n Ford Pantera L =  Cylinders:", fordcylgear['cyl'].values[0], "|Gear:", fordcylgear['gear'].values[0])
print("\n Honda Civic = Cylinders:", hondacylgear['cyl'].values[0], "|Gear:", hondacylgear['gear'].values[0])



