n=int(input())
su=0
temp=n
while(n):
    r=n%10
    su=su+r
    n=n//10
if temp%su==0:
    print('True')
else:
    print('False')