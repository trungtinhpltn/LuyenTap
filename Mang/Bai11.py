from random import randrange

while True:
    n = int(input("Nhap so phan tu cua mang: "))
    if n > 0 and n<= 99:
        break;
    else:
        print("So phan tu cua mang nho hon 99")
a = [0]*n
for i in range(n):
    a[i] = randrange(-100,100)
print(a)
a2 = reversed(a)
for i in a2:
    print(i,end="\t")
print()
print("*"*30)
for i in range(len(a)//2):
    tmp =a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = tmp
print(a)
