n=int(input())
a=list(map(int,input().split()))
t=len(str(abs(max(a))))
r=len(str(abs(min(a))))
if t>r:
    s=t
else:
    s=r
b=[]
for i in a:
    if len(str(abs(i)))==s:
        if i not in b:
            b.append(i)
print(*b)