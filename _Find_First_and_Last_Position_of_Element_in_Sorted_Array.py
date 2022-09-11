n=int(input())
a=list(map(int,input().split()))
k=int(input())
for i in range(n):
    if a[i]==k:
        print(i,end=' ')
        break
else:
    print(-1,end=' ')
for j in range(n-1,-1,-1):
    if a[j]==k:
        print(j)
        break
else:
    print(-1)