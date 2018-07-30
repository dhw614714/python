c=0
m=input()
n=m.split()
a,b=int(n[0]),int(n[1])
c=a-105
if b==c:
    print("正常")
elif b>c:
    print("偏胖")
elif b<c:
    print("偏瘦")
