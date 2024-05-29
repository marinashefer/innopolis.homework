import numpy as np
import pandas as pd

data = pd.read_csv('data.csv', sep=',')

print(data)
print(data.columns)

print(data.head(5))
print(data.tail(5))

print(data.info)
print(data.describe())

missing_values = data.isnull().sum()
print(missing_values>0)

unique_values = data.columns.values.tolist()
print(unique_values)
#print(data.sort_values(by='PassengerID'))
