n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=[]
for i in a:
    if a.count(i)>1:
        if i not in b:
            b.append(i)
print(*b)
