# создание модели кластеризации точек в двумерном пространстве с использованием DBSCAN
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs, make_circles
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt

# функция make_circles() в Python генерирует две концентрические окружности с тем же центром, один внутри другого
X_circles_unscaled, circles_labels_true = make_circles(n_samples=750, noise=0.04, random_state=42, factor=0.5)
# fit_transform используется в векторизаторах в Python для подгонки модели к данным и преобразования данных в векторизованный формат
X_circles = StandardScaler().fit_transform(X_circles_unscaled)
plt.scatter(X_circles[:,0], X_circles[:,1], c = circles_labels_true)
plt.show()


centers = [[1, 1], [-1, -1], [1, -1]]
# функция make_blobs() генерирует данные в виде больших двоичных объектов, которые могут быть использованы для кластеризации
X_blobs_unscaled, blobs_labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.3, random_state=42)
X_blobs = StandardScaler().fit_transform(X_blobs_unscaled)
plt.scatter(X_blobs[:,0], X_blobs[:,1])
plt.scatter(X_blobs[:,0], X_blobs[:,1], c = blobs_labels_true)
plt.show()


circles_model = DBSCAN(eps=0.3)
blobs_model = DBSCAN(eps=0.3)

circles_model.fit(X_circles)
blobs_model.fit(X_blobs)

X_blobs_predicted_labels = blobs_model.labels_
X_circles_predicted_labels = circles_model.labels_

plt.scatter(X_circles[:,0], X_circles[:,1], c = X_circles_predicted_labels)
plt.show()

plt.scatter(X_blobs[:,0], X_blobs[:,1], c = X_blobs_predicted_labels)
plt.show()