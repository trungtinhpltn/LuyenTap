a= int(input("Nhap vao he so a: "))
b = int(input("Nhap vao he so b: "))
if a == 0 and b == 0:
    print("PT {0}x+{1} <> 0 vo nghiem".format(a,b))
elif a == 0 and b != 0:
    print("PT {0}x+{1}=0 co vo so nghiem".format(a,b))
else:
    print("PT {0}x+{1}=0 co nghiem x <> ".format(a,b), -b/a)