from дз3з1 import s
def ss(a, p):
    for x in range(p):
        a = a[-1:] + a[:-1]
        return a
a = s()
p = int(input())
print(ss(a, p))
assert ss([1, 2, 3, 4, 5,], 1) == [5, 1, 2, 3, 4]
assert ss([1, 2, 3, 4, 5,], 2) == [4, 5, 1, 2, 3]
assert ss([1, 2, 3, 4, 5,], 3) == [3, 4, 5, 1, 2]
