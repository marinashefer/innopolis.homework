first = 52
def function(second):
    global first
    first = second + 10
    def function2(number):
        second = 12
        return second

summa = first + second
print('Сумма:', summa)