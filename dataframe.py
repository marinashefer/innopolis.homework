#import numpy as np
import pandas as pd

df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus'], 'population': [17.04, 143.5, 9.5], 'square': [2344, 6789, 3456]}, index=['KZ','RU', 'BY'])
df.index.name = 'code'

print(df[0])
print(df.index)

#.loc - используется для доступа по строковой метке
print(df.loc[['KZ','BY']])

#.iloc - используется для доступа по числовому значению(начиная от 0)
print(df.iloc[0:3])

#сбрасываются индексы
print(df.reset_index())

df['density'] = df['population'] / df['square'] * 1000000
del df['density']
print(df)

#важно перед переименовкой
print(df.reser_index())
#переименовываем столбцы - rename
df = df.rename(columns={'country': 'country_code'})
print(df)