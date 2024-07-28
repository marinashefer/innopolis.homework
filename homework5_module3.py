# напишите программу, которая обучит модель линейной регрессии, которая будет предсказывать значения Y по X

import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X,Y)

X_new = np.array([[6], [7]])

predictions = model.predict(X_new)
for i in range(len(X_new)):
    print(f"X={X_new[i][0]}: {predictions[i]}")
model