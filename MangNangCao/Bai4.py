from random import randrange

while True:
    n = int(input("Nhap so phan tu cua mang: "))
    if n > 0 and n<= 99:
        break;
    else:
        print("So phan tu cua mang nho hon 99")
a = [0]*n
for i in range(n):
    a[i] = randrange(0,100)
print(a)
print("*"*20)
chan =[]
le = []
for item in a:
    if item%2 == 0:
        chan.append(item)
    else:
        le.append(item)
print(chan)
print(le)