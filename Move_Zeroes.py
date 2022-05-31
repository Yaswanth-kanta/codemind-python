n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i!=0:
        b.append(i)
for i in a:
    if i==0:
        b.append(i)
print(*b)