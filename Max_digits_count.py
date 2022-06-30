n=int(input())
a=list(map(int,input().split()))
t=len(str(abs(max(a))))
c=0
for i in a:
    if len(str(abs(i)))==t:
        c+=1
print(c)