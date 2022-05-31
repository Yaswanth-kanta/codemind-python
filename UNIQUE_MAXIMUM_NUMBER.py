n=int(input())
a=list(map(int,input().split()))[:n]
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if b==[]:
    print(-1)
else:
    print(max(b))