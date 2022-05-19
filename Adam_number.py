n=int(input())
sqr1=n*n
temp=n
rev1=0
while(n):
    r=n%10
    rev1=rev1*10+r
    n=n//10
sqr2=rev1*rev1
rev2=0
temp2=sqr2
while(sqr2):
    r=sqr2%10
    rev2=rev2*10+r
    sqr2=sqr2//10
if sqr1==rev2:
    print('True')
else:
    print('False')
    