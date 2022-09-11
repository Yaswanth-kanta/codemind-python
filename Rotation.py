for _ in range(int(input())):
    n,r=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(r):
        x=a.pop()
        a.insert(0,x)
    print(*a)