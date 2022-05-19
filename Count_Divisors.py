l,r,k=map(int,input().split())
count=0
i=l
while(i<=r):
    if i%k==0:
        count=count+1
    i=i+1
print(count)