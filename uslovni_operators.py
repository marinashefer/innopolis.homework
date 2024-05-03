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
for i in range(len(s)):
    print(d[i])

for i in d:
    print(d)

for i in range(len(d)):
    print(d[i])

# задачка
s = '0123456789098765432'
for i in range(0, les(s), 5):
    print(s[i], end='')