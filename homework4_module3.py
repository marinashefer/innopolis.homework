# реализуйте добавление комбинаций столбцов, вычислимых столбцов, и результатов кластеризации, к исходному набору данных

import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv('3.4.2 housing.csv', sep=',')

#'Latitude' - широта
#'MedInc' – средний доход жильцов
#'HouseAge' – возраст дома
data['Latitude'] = data['HouseAge'] + data['MedInc']

#'MedHouseVal' – средняя цена квартиры, этот параметр мы и будем предсказывать
#'AveBedrms' – среднее количество спален в квартире
data['MedHouseVal'] = data['AveBedrms'] + data['AveOccup']

#'AveRooms' – среднее количество комнат в квартире
data['mean'] = data[['AveRooms', 'Latitude']].mean(axis=1)

kmeans = KMeans(n_clusters=3)
data['cluster'] = kmeans.fit_predict(data[['MedInc', 'Latitude']])

print(data)


#'Population' – население дома
#'AveOccup' – среднее количество жильцов в квартире
#'Longitude' - долгота