def ss(n):
    a = 1
    for a in range(2, n + 1):
        a *= 1
    return a
n = int(input())
print(ss(n))
assert ss(3) == 6
assert ss(4) == 24
