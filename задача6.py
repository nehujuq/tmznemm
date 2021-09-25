def is_int(n):
    try:
        return int(n) == float(n)
    except ValueError:
        return False
a = input()
print(is_int(a))