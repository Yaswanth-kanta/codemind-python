n,m=map(int,input().split())
a=list(map(int,input().split()))[:n]
b=list(map(int,input().split()))[:m]
c=[]
d=[]
for i in a:
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        d.append(i)
print(*(c+d))
 