import numpy as np

a = np.array([1, 2, 3, 4], float)
print(a)
print(a[:-2])
print(a[2:5])

a = np.array([[1, 2, 3, 4], [4, 5, 6]], float)
print(a[0, 1])
print(a[:,2])
print(a.shape)
print(a.dtype)
print(len(a))
print(2 in a)
print(7 in a)

b = a
print(b)
print(b is a) #true or false

c = a.copy()
print(c is a)

#shape - количество строк и столбцов
#dtype - тип данных
#len - количество символов в строке

#tolist -  массив преобразовываем в список
a = np.array([[1, 2, 3], [4, 5, 6]], float)
print(a.tolist())

#tostring - массив в строку
#fromstring

a = np.array([1, 2, 3, 4], float)
a.fill(0)
print(a)
#fill - заполнить массив элементом

#reshape
#transpose

#flatten - делаем одномерный массив из многомерного
a = np.array([1, 2, 3, 4], float)
print(a.flatten())

#concatenate - суммируем
a = np.array([1, 2], float)
b = np.array([3, 4, 5, 6], float)
c = np.array([7, 8, 9], float)
print(np.concatenate([a, b, c]))

#arange
a = np.arange(5, dtype=float)
print(a)

b = np.arange(1, 6 ,2, dtype=float)
print(b)

#ones
a = np.ones((2, 3), dtype=float)
print(a)

#zeros
b = np.zeros(7, dtype=float)
print(b)

#zeros_like/ones_like
a = np.array([[1, 2, 3], [4, 5, 6]], float)
b = np.zeros_like(a)
print(b)

#матрица - identity
a = np.identity(10, dtype=float)
print(a)

#eye - заполнение единицами по диагонали
#k - элемент с которого начинается заполнение единицами
a = np.eye(4, k=1, dtype=float)
print(a)