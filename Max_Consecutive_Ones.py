n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in a:
    if i==0:
        c=0
    else:
        c+=1
        d=max(c,d)
print(d)
        