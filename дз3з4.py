def che():
    a = list()
    b = input()
    while b != '':
        a.append(b)
        b = input()
    return a 
y = che()
print('элемент | частота')
for i in set(y):
    x = y.count(i)
    print(i, "|", x)
