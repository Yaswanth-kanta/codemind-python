n=input()
t=int(n)
temp=t
res=0
i=len(n)
while(t>0):
    r=t%10
    res=res+pow(r,i)
    t=t//10
    i=i-1
if temp==res:
    print('True')
else:
    print('False')