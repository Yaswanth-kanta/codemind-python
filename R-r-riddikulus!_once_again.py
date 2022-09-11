n,r=map(int,input().split())
a=list(map(int,input().split()))
for i in range(r):
    x=a.pop(0)
    a.append(x)
print(*a)