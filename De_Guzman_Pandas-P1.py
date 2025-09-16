# %%
import pandas as pd

# %%
cars = pd.read_csv('cars.csv')
cars

# %%
firstandlast = pd.concat([cars.head(), cars.tail()])
firstandlast


