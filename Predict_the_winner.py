n=int(input())
a=list(map(int,input().split()))
r=n//2
c=0
d=0
for i in range(n):
    if i<r-1:
        c=c+a[i]
    else:
        d=d+a[i]
if (abs(c-d))%4:
    print('Y')
else:
    print('X')