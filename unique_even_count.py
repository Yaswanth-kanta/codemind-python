n=int(input())
a=list(map(int,input().split()))[:n]
c=0
b=[]
for i in a:
    if i%2==0:
        if i not in b:
            b.append(i)
for i in b:
    if i%2==0:
        c+=1
print(c)