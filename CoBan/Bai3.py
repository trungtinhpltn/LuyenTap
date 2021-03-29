import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a+b >=2*c or a+c >= 2*b or b+c >= 2*a:
    print("La tam giac")
else:
    print("Khong la 3 canh cua mot tam giac")
cv = a+b+c
p = cv/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Chu vi: ", cv)
print("Dien tich: ", s)
