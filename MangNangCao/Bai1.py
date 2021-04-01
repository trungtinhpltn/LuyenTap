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
k = int(input("Phan tu co gia tri lon thu: "))
a.sort(reverse=True)
print(a)
print(a[k-1])