import pandas as pd

data = pd.read_csv('titanic.csv')

print(data.head(5))
print(data.tail(5))

print(data.info)

print(data.describe())
