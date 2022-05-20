def pal(n):
    temp=n
    rev=0
    while(n):
        r=n%10
        rev=rev*10+r
        n=n//10
        if temp==rev:
            return rev
a=int(input())
b=int(input())
for i in range(a,b):
    if pal(i):
        print(i,end=' ')
    
