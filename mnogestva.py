#множества-уникальные(нет ограничений на кол-во элементов, но добавлять элементы нельзя)
a = {1, 2, 3}
a = set()
print(type(a))

#функция add
set1 = {1, 3, 4}
set1.add(2)
print(set1)

#update-добавляем
a = {1, 3, 4}
a.update([4, 5, 6])
print(a)

#remove-удаляем конкретный элемент и возвращаем ошибку!
set1 = {1, 3, 4, 'a', 'h'}
set1.remove(2)
print(set1)

#discard-удаляем,если нам не нужна ошибка
set1 = {1, 3, 4}
set1.discard(2)
print(set1)

#pop
set1 = {1, 3, 4, 'a', 'k'}
set1.pop()
print(set1)