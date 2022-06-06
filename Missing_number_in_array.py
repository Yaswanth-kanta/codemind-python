t=int(input())
while(t):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    b=[]
    for i in range(1,n+1):
        b.append(i)
    for i in a:
        if i in b:
            b.remove(i)
    print(*b)
    t-=1