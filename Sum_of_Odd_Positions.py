n=int(input())
a=list(map(int,input().split()))[:n]
su=0
for i in range(0,n):
    if i%2!=0:
        su+=a[i]
print(su)