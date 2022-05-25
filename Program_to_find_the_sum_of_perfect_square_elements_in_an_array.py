def fact(n):
    if n==1:
        return 1
    c=0
    for i  in range(1,n):
        if n==i*i:
            c=c+n
    return c
n=int(input())
a=list(map(int,input().split()))[:n]
c1=0
for i in a:
    if (fact(i)):
        c1=c1+(fact(i))
print(c1)
            