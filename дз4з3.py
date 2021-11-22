from дз3з1 import s
def x(y):
    r = list(y)
    if y == r:
        return "True"
    else:
        return "False"
y = s()
print(x(y))
assert x(1, 2, 3, 4, 5, 6, 7) == "True"
assert x(1, 2, 1, 4, 2, 6, 7) == "False"
