n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%2:
        c+=1
if c%2==0:
    print(1)
else:
    print(0)
