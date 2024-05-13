#a = {ключ: значение}
a = {'a': 1, 'b': 2} 
print(a)

a = dict[[(1, 2), [4, 5]]]
print(a)

a = {'a': 1}
a['a'] = 4
a[7] = "alex"
print(a)

#clear
a = {2: 1}
print(a)
a.clear()
print(a)

#copy
a = {2: 1}
b = a.copy() #создаём копию
c = a
print(b)
print(b is a) #b не является а
print(c is a) #c является а

#get
a = {2: 1}
print(a.get(2, 3))
print(a.get(1, 3))

#items
a = {2: 1, 'a': 4}
print(a.items())

#keys
a = {2: 1, 'a': 4}
print(a.keys())

#pop-удаляет
a = {2: 1, 'a': 4}
b = a.pop('a')
print(b)
print(a)

#popitem
a = {2: 1}
b = a.popitem()
print(b)
print(a)

#update
a = {2: 1}
a.update({'a': 2})
print(a)

#values-выводит только значение
a = {2: 1, 'a':2}
print(a.values())

for key, value in a.items():
    print(key, value)

for item in a.items():
    print(item)