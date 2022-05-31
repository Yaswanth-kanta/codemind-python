n=input()
c=0
c1=0
for i in n:
    if i=='z':
        c+=1
for i in n:
    if i=='o':
        c1+=1
if c==c1/2:
    print('Yes')
else:
    print('No')