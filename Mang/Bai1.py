while True:
    n = int(input("Nhap so phan tu cua mang: "))
    if n > 0 and n<= 99:
        break;
    else:
        print("So phan tu cua mang nho hon 99")
arr = [0]*n
mi = 999999;
x = 0
dem = 0;
for i in range(n):
    x = int(input())
    if x == -1:
        break;
    arr[i] = x
    dem += 1;
    mi = min(mi,arr[i])
for i in range(dem):
    print(arr[i], end="\t")
print()
print("Gia tri nho nhat: ", mi)
