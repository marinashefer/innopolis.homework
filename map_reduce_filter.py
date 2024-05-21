import functools
from functools import reduce

#functools.reduce()

#function - функция, которая будет применена к элементам коллеклции для их объединения
#sequence - коллекция данных, которую нужно объединить
#initial(опционально) - начальное значение аккумулятора, которое будет использовано в качестве первого аргумента при объединении

numbers = [1, 2, 8, 9]

def get_maximum(first_num, second_num):
    return first_num if first_num > second_num else second_num
print(reduce(get_maximum, numbers, 10))
print(reduce(get_maximum, numbers))

#filter(function or None, interable)
#print(reduce(get_maximum))


numbers = [2, 3, 8, 15, 34, 42]

def is_even(num):
    return num % 2 == 0
print(filter(is_even, numbers))
print(list(filter(is_even, numbers)))
#обертываем в список!

map(mul, 'abc', [3, 5, 7])
print(map(mul, 'abc', [3, 5, 7]))
print(list(map(mul, 'abc', [3, 5, 7])))