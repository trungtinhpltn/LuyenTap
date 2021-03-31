import math
from random import random

n = int(input())
a = [0]*n
for i in range(n):
    a[i] = random()*100
for i in range(n):
    print(a[i], end="\t")
x = float(input("Nhap gia tri x: "))
dem =0
for item in a:
    if math.fabs(item-x) <= 0.01:
        dem += 1;
print("So phan tu x co trong mang la: ", dem)