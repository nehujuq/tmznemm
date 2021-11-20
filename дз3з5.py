def sred(n):
    return sum(n) / len(n)
a = list()
b = input()
while b != '':
    a.append(float(b))
    b = input('')
print(sred(a))
