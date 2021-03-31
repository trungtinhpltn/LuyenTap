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
k = int(input("Nhap vao vi tri can xoa: "))

if k <= 0 or k>= len(arr):
    print("Vi tri khong hop le")
else:
    del arr[k]
    print(arr)