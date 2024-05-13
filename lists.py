#списки
numbers = [2, 4, 6, 8, 10]
numbers = ['Python', 'C++', 'Java', 'JavaScript']
info = ['Python', 2022, 24.2]

#numbers[0] == 2

print(numbers[0], numbers[3])

my_list = list()
new_list = []
print(new_list)

numbers = list(range(10))
print(numbers)

#четные/нечетные
even_numbers = list(range(0, 10, 2))
odd_numbers = list(range(1, 10, 2))
print(even_numbers)
print(odd_numbers)

s ='Hello'
chars = list(s)
print(chars)

#вложенные списки
numbers = [[1, 2, 3], [4, 5, 6]]
print(numbers[1][1])

#append
a = [1, 2, 3]
a.append(4)
print(a)

#remove
a = [1, 2, 3]
a.remove(3)
print(a)

a = [1, 2, 3]
a.remove(a[2])
print(a)

#pop
a = [1, 2, 3]
a.pop(0)
print(a)

#clear
a = [3, 5, 1]
a.clear(1)
print(a)

#sort
a = [11, 2, 93]
a.sort()
print(a)

#extend
a = [1, 2, 3]
b = [4, 8, 9]
a.extend(b)
print(a) 

#index
a = [1, 2, 3]
a.index(1)
print(a)

#insert
a = [4, 2, 3]
a.insert(3, 4)
print(a)