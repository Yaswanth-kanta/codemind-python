n=int(input())
a=list(map(int,input().split()))[:n]
b=[]
c=0
for i in a:
    if a.count(i)==i:
        b.append(i)

for i in a:
    if a.count(i)!=i:
        c+=1
if c==n:
    print(-1)
print(min(b),max(b))