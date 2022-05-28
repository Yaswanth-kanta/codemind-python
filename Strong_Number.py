def fact(n):
    factorial=1
    if n==1:
        return 1
    for i in range(1,n+1):
       factorial=factorial*i
    return factorial
n=int(input())
temp=n
su=0
while(n):
    r=n%10
    res=fact(r)
    su=su+res
    n=n//10
if su==temp:
    print('The number {} is a strong number'.format(su))
else:
    print('The number {} is not a strong number'.format(temp))