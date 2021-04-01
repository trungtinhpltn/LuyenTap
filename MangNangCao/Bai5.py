
from random import randrange, random

while True:
    n = int(input("Nhap so phan tu cua mang: "))
    if n > 0 and n<= 99:
        break;
    else:
        print("So phan tu cua mang nho hon 99")
a = [0]*n
for i in range(n):
    a[i] = round(random()*10,2)
print(a)
print("*"*20)
while True:
    k = int(input("Nhap k: "))
    if k >=0 or k< len(a):
        break
    else:
        print("gia tri k khong hop le")
l = 1
while l<=k:
    x = a[len(a)-1]
    for i in range(len(a)-2,-1,-1):
        a[i+1] = a[i]
    a[0] = x;
    l+=1
print(a)
