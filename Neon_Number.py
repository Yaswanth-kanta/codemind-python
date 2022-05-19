n=int(input())
sqr=n*n
su=0
while(sqr):
    d=sqr%10
    su=su+d
    sqr=sqr//10
if su==n:
    print('Neon Number')
else:
    print('Not Neon Number')