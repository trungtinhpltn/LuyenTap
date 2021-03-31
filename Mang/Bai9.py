from random import randrange

while True:
    n = int(input("Nhap so phan tu cua mang: "))
    if n > 0 and n<= 99:
        break;
    else:
        print("So phan tu cua mang nho hon 99")
arr = [0]*n
for i in range(n):
    x = randrange(0,1000)
    if i == 0:
        arr[i]=x
    else:
        while x < arr[i-1]:
            x = randrange(0,1000)
        arr[i] =x
print(arr)
x = int(input("Nhap gia tri x: "))
vt=0
for i in range(len(arr)):
    if arr[i] >= x:
        vt = i
        arr.insert(vt, x)
        break;
    if i == len(arr)-1 and arr[i]<=x :
        arr.append(x)
        break
print(arr)