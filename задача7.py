sum = 0
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 5 == 0:
        sum += i
print(sum)