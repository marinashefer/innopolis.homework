list1 =[]
for i in range(1, 11):
    list1.append(i)
print(list1)

# [выражение for элемент in последовательность]
list1 = [i for i in range(1, 11)]
print(list1)

#split - пробел(разделяет списк на элементы)
list2 = [int(i) for i in input('enter').split()]
print(list2)

list3 = [i * 2+1 for i in range(1, 11)]
print(list3)

# [выражение for элемент in последовательность if условие]
list4 = [i for i in range(1, 101) if i % 2 == 0]
print(list4)

list5 = [i * j for i in range(1, 10) for j in [1, ]]
print(list5)

#преобразование списка в кортеж
list6 = tuple([i * j for i in range(1, 10) for j in [1, 2, 3]])
print(list6)