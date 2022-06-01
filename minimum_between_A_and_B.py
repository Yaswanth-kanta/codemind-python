n=int(input())
a=list(map(int,input().split()))[:n]
x,y=map(int,input().split())
c=0
b=[]
for i in a:
    if i>=x and i<=y:
        b.append(i)
if b==[]:
    print(-1)
else:
    print(min(b))