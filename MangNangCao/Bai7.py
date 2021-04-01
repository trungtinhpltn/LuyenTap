while True:
    h = int(input("Nhap vao chieu cao h:"))
    if h>0 or h<= 20:
        break
    else:
        print("Chieu cao tu 0 den 20.")
def ckn(k,n):
    if k == 0 or k == n:
        return 1
    if k == 1:
       return n

    return ckn(k,n-1)+ckn(k-1,n-1)

for i in range(h):
    print(" "*(h-i-1),end="")
    for j in range(i+1):
        print(ckn(j,i),end=" ")
    print()