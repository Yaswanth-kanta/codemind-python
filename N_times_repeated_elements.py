n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
for i in a:
    if a.count(i)==k:
        if i not in b:
            b.append(i)
if b==[]:
    print(-1)
else:
    print(*b)