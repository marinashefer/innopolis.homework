number = int(input('Введите число:'))
a = 1
b = 1
for i in range(0, number, 1):
    c = a + b
    a = b
    b = c
    print(c)