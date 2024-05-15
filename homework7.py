list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def function(list_a):
    list_b = []

    for i in list_a:
        if isinstance(i, list):
            list_b.extend(function(i))
        else:
            list_b.append(i)

    return list_b

list_b = function(list_a)
print(list_b)