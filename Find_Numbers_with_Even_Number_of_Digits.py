def count(n):
    c=0
    while(n):
        if (n):
            r=n%10
            c=c+1
        n=n//10
    c1=0
    if c%2==0:
        c1=c1+1
    return c1
a=int(input())
b=list(map(int,input().strip().split()))[:a]
su=0
for i in b:
    su=su+(count(i))
print(su)
    

        