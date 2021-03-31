a = []
n = 0
while n<=99:
    x = int(input())
    if x == -1:
        break
    a.append(x)
a.sort()
print(a)