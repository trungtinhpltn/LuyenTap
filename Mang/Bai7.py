from random import randrange

while True:
    n = int(input("Nhap so phan tu cua mang: "))
    if n > 0 and n<= 99:
        break;
    else:
        print("So phan tu cua mang nho hon 99")
arr = [0]*n
for i in range(n):
    arr[i] = randrange(-50,50)
print(arr)
x = int(input("Nhap gia tri x: "))
sx = arr.count(x)
while arr.count(x) > 0:
    arr.remove(x)
print("So phan tu co gia tri ",x, " bi xoa la:  ", sx )
print(arr)