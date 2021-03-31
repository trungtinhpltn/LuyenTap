from random import randrange

n= int(input("So phan tu cua mang: "))
a = [0]*n
s = 0
for i in range(n):
    a[i] = randrange(-100,100)
    s += a[i]
for i in range(n):
    print(a[i],end="\t")
print("Gia tri trung binh: ", s/n)