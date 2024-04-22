print(5+5)

print(10-5)

print(5 * 2)

print(15/3)

print("целочисленное деление (без остатка)", 15//2)

print('** возведение в степень', 5**3)

print('% остаток от деления', 6%5)

#задание 
data = 1234
a = data // 1000
b = data // 100 % 10
c = data // 10 % 10
d = data % 10

print(a)
print(b)
print(c)
print(d)

#input
a = int(input('Enter a number:'))
print(type(a))

#decimal- библиотека для большей точности чисел
import decimal
a = 1/3
print(a)

b = decimal.Decimal(1)/decimal.Decimal(3)
print(b)

print(a*3)
print(b*3)