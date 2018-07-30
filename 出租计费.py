a=1
c=0
while a ==1:
    b=int(input())
    if b==0:
        print(" 请输入正确的公里数进行计算")
    elif b>0 and b<=2:
        print(8)
    elif b>2 and b<=12:
        c=8+1.2*(b-2)
        print(c)
    elif b>12:
        c=20+1.5*(b-12)
        print(c)
        
        
