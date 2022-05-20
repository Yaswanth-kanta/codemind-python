def pal(n):
    rev=0
    temp=n
    while(n):
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return True
    else:
        return False
t=int(input())
while(t):
    a=int(input())
    temp=a
    if pal(a):
        print('True')
    else:
        print('False')
    t=t-1