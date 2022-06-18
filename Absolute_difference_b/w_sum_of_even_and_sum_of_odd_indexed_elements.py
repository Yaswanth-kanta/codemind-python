n=int(input())
a=list(map(int,input().split()))[:n]
su=0
su1=0
for i in range(0,n):
    if i%2==0:
        su=su+a[i]
    else:
        su1+=a[i]
print(abs(su-su1))