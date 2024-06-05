#import numpy as np
#import pandas as pd

#Series - объект/элемент с массивом
#a = pd.Series([5, 6, 1, 8, 7, 9, 7])
#print(a.index) 
#print(a.values) #выводятся все значения
#print(a)
#print(a[3])

#a = pd.Series([5, 6, 1], index=['a', 'b', 'c'])
#print(a['b'])

#фильтруем
#a = pd.Series([5, 6, 1], index=['a', 'b', 'c'])
#print(a[a>6]*2)

#a = pd.Series([5, 6, 1], index=['a', 'b', 'c'])
#a.name = 'список'
#print(a)

#a = pd.Series([5, 6, 1], index=['a', 'b', 'c'])
#a.index.name = 'my_series'
#print(a)

#меняем индексы
#a = pd.Series('a': 5, 'b': 7, 'c': 2)
#a.index = [1, 2, 3]
#print(a)