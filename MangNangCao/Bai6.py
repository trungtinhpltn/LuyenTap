from random import randrange, random

while True:
    n = int(input("Nhap so phan tu cua mang: "))
    if n > 0 and n<= 20:
        break;
    else:
        print("So phan tu cua mang nho hon 20")
a = [0]*n
for i in range(n):
    a[i] = randrange(0,11)
print(a)
print("*"*20)
ma =0
t=0
pt =0
while t<=10:
    m = a.count(t)
    if m >ma:
        pt = t
        ma =m
    t+=1

print("Phan tu ",pt," co so lan xuat hien nhieu nhat la : ",ma)