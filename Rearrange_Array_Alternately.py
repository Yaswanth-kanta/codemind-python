for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for j in range(n):
        if j%2==0:
            b.append(max(a))
            a.remove(max(a))
        else:
            b.append(min(a))
            a.remove(min(a))
    print(*b)