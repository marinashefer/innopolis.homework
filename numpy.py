import numpy as np

#a = np.array([1, 2, 3, 4], float)
#print(a)
#print(a[:-2])
#print(a[2:5])

#a = np.array([[1, 2, 3, 4], [4, 5, 6]], float)
#print(a[0, 1])
#print(a[:,2])
#print(a.shape)
#print(a.dtype)
#print(len(a))
#print(2 in a)
#print(7 in a)

#b = a
#print(b)
#print(b is a) #true or false

#c = a.copy()
#print(c is a)

#shape - количество строк и столбцов
#dtype - тип данных
#len - количество символов в строке

#tolist -  массив преобразовываем в список
#a = np.array([[1, 2, 3], [4, 5, 6]], float)
#print(a.tolist())

#tostring - массив в строку
#fromstring

#a = np.array([1, 2, 3, 4], float)
#a.fill(0)
#print(a)
#fill - заполнить массив элементом

#reshape
#transpose

#flatten - делаем одномерный массив из многомерного
#a = np.array([1, 2, 3, 4], float)
#print(a.flatten())

#concatenate - суммируем
#a = np.array([1, 2], float)
#b = np.array([3, 4, 5, 6], float)
#c = np.array([7, 8, 9], float)
#print(np.concatenate([a, b, c]))

#arange
#a = np.arange(5, dtype=float)
#print(a)

#b = np.arange(1, 6 ,2, dtype=float)
#print(b)

#ones
#a = np.ones((2, 3), dtype=float)
#print(a)

#zeros
#b = np.zeros(7, dtype=float)
#print(b)

#zeros_like/ones_like
#a = np.array([[1, 2, 3], [4, 5, 6]], float)
#b = np.zeros_like(a)
#print(b)

#матрица - identity
#a = np.identity(10, dtype=float)
#print(a)

#eye - заполнение единицами по диагонали
#k - элемент с которого начинается заполнение единицами
#a = np.eye(4, k=1, dtype=float)
#print(a)

#a = np.array([1, 2, 3], float)
#b = np.array([1, 2, 3], float)
#print(a*b)

#a = np.array([[1, 2, 3],[4, 5, 6]], float)
#b = np.array([[1, 2, 3],[2, 7, 8]], float)
#print(a*b)

#меньший массив используется несколько раз при умножении

#a = np.zeros((2, 2), float)
#b = np.array([-1.,3.], float)
#print(a+b)

#floor, ceil, rint
#floor - округляет в меньшую сторону
#ceil - округляет в большую сторону
#rint - округляет по правилам
#a = np.array([1.1, 1.4, 1.9], float)
#print(a)
#print(np.floor(a))

#a = np.array([1, 2, 3], float)
#for x in a:
#    print(x)

#a = np.array([[1, 2,], [8, 3], [4, 6]], float)
#for x in a:
#    print(x)

#перебируем массив через цикл
#a = np.array([[1, 2,], [8, 3], [4, 6]], float)
#for (x, y) in a:
#    print(x * y)

#суммируем - sum
#a = np.array([6, 2, 9], float)
#print(a.sum())

#перемножаем - prod
#a = np.array([6, 2, 9], float)
#print(a.prod())

#среднее значение - mean
#a = np.array([6, 2, 9], float)
#print(a.mean())

#вариация-дисперсия(на сколько сильно друг от друга разбросаны значения) - var !для фигур!
#a = np.array([6, 2, 9], float)
#print(a.var())

#девариация - std
#a = np.array([6, 2, 9], float)
#print(a.std())

#a = np.array([6, 2, 9], float)
#print(a.max())

#a = np.array([6, 2, 9], float)
#print(a.argmin())

#a = np.array([6, 2, -1, 0, 9], float)
#print(sorted(a))

#a = np.array([6, -1, 0, 2, 9], float)
#print(a.clip(0, 2))

#вытаскиваем уникальные элементы
#a = np.array([6, 6, 2, -1, -1, 2, 9], float)
#print(np.unique())

#выводим диагональ массива
#a = np.array([[6, 4], [3, 5]], float)
#print(a.diagonal())