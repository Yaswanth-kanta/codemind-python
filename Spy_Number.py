n=int(input())
su=0
pro=1
while(n):
    d=n%10
    su=su+d
    pro=pro*d
    n=n//10
if su==pro:
    print('Spy Number')
else:
    print('Not Spy Number')
    