# перебор 
word = 'hello'
for char in word:
    print(char)

# контатенация строк
word = 'hello'
print(word + " " + 'world')

# нахождение длины строки
word = 'hello'
print(len(word))

# проверка вхождения в строку
word = 'pencil'
if 'pe' in word:
    print('yes')

# умножение строки на число
print(word * 10)

w = "python"
print(w[0])
print(w[1])
print(w[2])
print(w[3])
print(w[4])
print(w[5])

print(w[0:6])
print(w[4:6])
print(w[-3:-1])
print(w[-3:])

# задачка:)
s = 'abcdefg'
print(s[0] +s[-1] + s[4] + s[6])

print(s[:-1])

d = 'Python'
for i in range(len(d)):
    print(d)

for i in d:
    print(d)

for i in range(len(d)):
    print(d)

# задачка
s = '0123456789098768432'
for i in range(0, len(s), 5):
    print(s[i], end=' ')


s = 'Hello'
print(s[::-1])
print(s[::-2])
print(s[::-3])

name = 'Tom'
print(f'{name} Hello')

# задачка!
word = input('Введите строку:')
word2 = word[::-1]
if word == word2:
    print('строка палиндром')
else:
    print('строка не палиндром')