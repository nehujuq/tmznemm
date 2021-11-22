from дз3з1 import s
    while b != '':
        a.append(b)
        b = input()
    return a 
y = s()
print('элемент | частота')
for i in set(y):
    x = y.count(i)
    print(i, "|", x)
