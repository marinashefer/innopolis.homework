import numpy as np
import pandas as pd

df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus'], 'population': [17.04, 143.5, 9.5], 'square': [2344, 6789, 3456]}, index=['KZ','RU', 'BY'])

print(df[0])
print(df.index)