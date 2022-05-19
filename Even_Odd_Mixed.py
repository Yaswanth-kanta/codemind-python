n=int(input())
e=0
o=0
while(n):
    d=n%10
    n=n//10
    if(d%2):
        o+=1
    else:
        e+=1
if e>0 and o==0:
    print('Even')
elif e==0 and o>0:
    print("Odd")
else:
    print('Mixed')
