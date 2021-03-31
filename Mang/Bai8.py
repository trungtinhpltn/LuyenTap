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
k = int(input("Vi tri chen: "))
if k< 0 or k >= len(arr):
    print("Vi tri khong hop le")
else:
    arr.insert(k,x)
    print(arr)