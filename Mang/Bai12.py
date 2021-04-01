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
for i in range(n):
    for j in range(i+1,n,1):
        dc = []
        dc.append(a[i])
        ma = a[i]
        while j < n:
            if a[j] > ma:
                dc.append(a[j])
                ma = a[j]
            j +=1
        if len(dc) >= 2:
            print(dc)