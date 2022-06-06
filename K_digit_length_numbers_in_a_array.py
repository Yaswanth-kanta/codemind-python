n,k=map(int,input().split())
a=list(map(int,input().split()))[:n]
b=[]
c=0
for i in a:
    b.append(abs(i))
for i in b:
    if (len(str(i))==k):
        c+=1
print(c)