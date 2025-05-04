a=int(input("请输入a的值:"))
b=int(input("请输入b的值:"))
c=int(input("请输入c的值:"))
d=b**2-4*a*c
if d>=0 :
    x1=(-b+d**(0.5))/2*a
    x2=(-b-d**(0.5))/2*a
    print("x1=",x1,"x2=",x2)
else :
    print("此方程无解")
