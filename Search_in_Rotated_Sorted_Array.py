n=int(input())
a=list(map(int,input().split()))
k=int(input())
if k in a:
    print(a.index(k))
else:
    print(-1)