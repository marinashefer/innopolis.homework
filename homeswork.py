import pandas as pd
import numpy as np

data = pd.read_csv('data.csv', sep=',')

print(data.head(5))
print(data.tail(5))

