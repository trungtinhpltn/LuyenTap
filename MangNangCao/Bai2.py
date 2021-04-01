a1 = [1,2,5,2,1]
a2 = [0,1,2,3,4]
def doixung(a):
    flag = True
    for i in range(len(a)//2):
        if a[i] != a[len(a)-i-1]:
            flag = False
            return flag
    return flag
if doixung(a1):
    print("Doi xung")
else:
    print("Khong doi xung")
if doixung(a2):
    print("Doi xung")
else:
    print("Khong doi xung")