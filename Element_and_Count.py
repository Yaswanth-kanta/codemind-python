n=int(input())
a=list(map(int,input().split()))[:n]
b=[]
for i in a:
    if i not in b:
        b.append(i)
for j in b:
    print(j,a.count(j),end=' ')
    