n=int(input())
a=list(map(int,input().split()))[:n]
x,y=map(int,input().split())
b=[]
for i in a:
    if i<x or i>y:
        b.append(i)
if b==[]:
    print (-1)
else:
    print(min(b))