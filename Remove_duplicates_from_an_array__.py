a=int(input())
b=list(map(int,input().strip().split()))[:a]
c=[]
for i in b:
    if i not in c:
        c.append(i)
print(*c)