n=int(input())
a=list(map(int,input().strip().split()))[:n]
su=0
su1=0
for i in range(0,len(a)):
    if i%2==0:
        su=su+a[i]
    else:
        su1=su1+a[i]
if su-su1==0:
    print('YES')
else:
    print('NO')