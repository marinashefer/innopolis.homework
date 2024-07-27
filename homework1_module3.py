import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accurancy_score

#загружаю данные
iris = load_iris()
x = iris.data
y = iris.target

#разделяю данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#создаю и обучаю модели случайного леса
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

#предсказание на тестовой выборки
y_pred = clf.predict(X_test)

#оценка точности модели
accurancy = accurancy_score(y_test, y_pred)
print(f'Точность модели:{accurancy:.2f}')

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)



import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

loaded_data = pd.read_csv("3.1 dataset.csv")

X = np.array(loaded_data['x']).reshape(-1, 1)
Y = np.loaded_data['y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)