def fac(n):
    r=0
    for i in range(1,n+1):
        if n%i==0:
            r=r+i
    return r
a=list(map(int,input().split(',')))
b=[]
for i in a:
    s=fac(i)
    if s in a:
        b.append(i)
if b==[]:
    print(-1)
else:
    b.sort()
    print(*b)
        