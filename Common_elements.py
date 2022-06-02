x,y=map(int,input().split())
a=list(map(int,input().split()))[:x]
b=list(map(int,input().split()))[:y]
c=[]
for i in a:
    if i in b:
        c.append(i)
d=[]
for i in c:
    if i not in d:
        d.append(i)
print(*d)
        