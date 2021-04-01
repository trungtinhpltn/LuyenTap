from math import fabs
from random import random
while True:
    n = int(input("Nhap so phan tu cua mang: "))
    if n > 0 and n<= 99:
        break;
    else:
        print("So phan tu cua mang nho hon 99")
a = [0]*n
for i in range(n):
    a[i] = random()*10
print(a)
x = float(input())
for i in a:
    if i <= x or fabs(x-i) <= 0.001:
        print(i,end="\t")