def pal(n):
    t=n
    rev=0
    while(n):
        r=n%10
        rev=rev*10+r
        n=n//10
    if t==rev:
        return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if pal(i):
        c+=1
print(c)